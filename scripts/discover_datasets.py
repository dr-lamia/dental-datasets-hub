#!/usr/bin/env python3
"""Nightly metadata discovery for the Dental & Maxillofacial Dataset Atlas.

Reads public metadata only. New discoveries are unverified leads; this code
never promotes items into manually curated catalog/*.csv files.
Sources: Zenodo, Figshare, Hugging Face, Europe PMC (paper leads).
"""
from __future__ import annotations

import concurrent.futures
import csv
import datetime as dt
import html
import json
import pathlib
import re
import time
import urllib.parse
import urllib.request
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "catalog" / "auto_discovery.json"
TOPICS = [
    "dental", "maxillofacial", "CBCT", "orthodontic",
    "oral cancer", "periodontal", "tooth", "temporomandibular",
    "implant dentistry", "cephalometric",
]
DENTAL = re.compile(
    r"\b(?:dental|dentistry|dentition|dentofacial|odontogenic|odontology|"
    r"tooth|teeth|caries|periodont\w*|endodont\w*|orthodont\w*|"
    r"maxillofacial|mandib\w*|maxilla(?:ry)?|craniofacial|cephalometric|"
    r"temporomandibular|cbct|cone[\s-]?beam|intraoral|"
    r"oral[\s-]+(?:cancer|cavity|lesion|mucosa|patholog\w*|health|surgery|"
    r"medicine|squamous)|oscc|implant[\s-]+dent|"
    r"occlus\w*|prosthodont\w*|pulpal|periapical|gingiv\w*)\b", re.I
)
DATA_HINT = re.compile(r"\b(?:dataset|data\s+set|database|benchmark|corpus|cohort|image\s+collection|annotation|segmentation|open\s+data|repository|data\s+descriptor)\b", re.I)
STRIP_HTML = re.compile(r"<[^>]*>")
NOW = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
TODAY = NOW[:10]
HEADERS = {"User-Agent": "DentalMaxillofacialDatasetAtlas/1.0 (academic metadata discovery; github.com/dr-lamia/dental-datasets-hub)", "Accept": "application/json"}

def clean(value, limit=400):
    if not value:
        return ""
    return " ".join(html.unescape(STRIP_HTML.sub(" ", str(value))).split())[:limit]

def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", (value or "").lower()).strip("-")

def get_json(url, payload=None):
    data = json.dumps(payload).encode("utf8") if payload is not None else None
    req = urllib.request.Request(url, data=data, headers={
        **HEADERS, **({"Content-Type": "application/json"} if data else {})
    })
    with urllib.request.urlopen(req, timeout=12) as reply:
        if reply.status != 200:
            raise RuntimeError(f"HTTP {reply.status}")
        return json.load(reply)

def link(value):
    v = (value or "").strip()
    return v if v.startswith(("https://", "http://")) else ""

def doi_norm(value):
    v = (value or "").lower().strip()
    v = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", v)
    return re.sub(r"^doi:\s*", "", v).split("?")[0].strip("/")

def canonical_url(url):
    try:
        p = urllib.parse.urlparse(url)
        return (p.netloc.lower() + p.path.rstrip("/")).lower()
    except (ValueError, TypeError):
        return ""

def known_ids():
    names, dois, urls = set(), set(), set()
    for file in (ROOT / "catalog").glob("*.csv"):
        if file.name in ("discovery_queue.csv", "template.csv"):
            continue
        try:
            with file.open(encoding="utf-8-sig", newline="") as f:
                for row in csv.DictReader(f):
                    n = row.get("dataset_name") or row.get("name")
                    if n: names.add(slug(n))
                    for k in ("dataset_url", "url", "publication_url"):
                        u = row.get(k, "")
                        if u:
                            urls.add(canonical_url(u))
                            if "doi.org" in u: dois.add(doi_norm(u))
                    if row.get("doi"): dois.add(doi_norm(row["doi"]))
        except (OSError, UnicodeDecodeError):
            pass
    return names, dois, urls

def make_item(source, title, url, date="", description="", doi="", license_text="", access="", kind="dataset", query=""):
    title = clean(title, 220)
    description = clean(description, 1000)
    url = link(url)
    doi = doi_norm(doi)
    if not title or not url or not DENTAL.search(title + " " + description):
        return None
    # Papers are discovery leads only, even when title says "dataset".
    if kind == "publication_lead" and not DATA_HINT.search(title + " " + description):
        return None
    # Require a dental-relevant title OR a very clear dataset description for dataset platform results.
    if kind == "dataset" and not DENTAL.search(title) and not DATA_HINT.search(description[:250]):
        return None
    date = (str(date)[:10] if date else "")
    if date and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        date = ""
    ident = doi or canonical_url(url) or slug(title)
    return {
        "id": slug(source) + "-" + slug(ident)[:110],
        "title": title, "source": source, "url": url, "doi": doi,
        "date": date, "description": description,
        "license": clean(license_text, 160), "access": clean(access, 100),
        "source_type": kind, "status": "unverified",
        "query": query, "first_seen": TODAY, "last_seen": TODAY
    }

def zenodo(topic):
    q = urllib.parse.urlencode({"q": topic, "size": 25, "sort": "mostrecent"})
    data = get_json("https://zenodo.org/api/records?" + q)
    out = []
    for rec in data.get("hits", {}).get("hits", []):
        m = rec.get("metadata", {})
        kind = (m.get("resource_type") or {}).get("type", "").lower()
        # Skip clearly non-dataset literature, code, presentation records.
        if kind not in ("dataset", "other", ""): continue
        item = make_item(
            "Zenodo", m.get("title"), (rec.get("links") or {}).get("self_html") or (rec.get("links") or {}).get("html") or f"https://zenodo.org/records/{rec.get('id')}",
            m.get("publication_date"), m.get("description"), rec.get("doi") or rec.get("conceptdoi"),
            (m.get("license") or {}).get("id", "") if isinstance(m.get("license"), dict) else m.get("license", ""),
            "See original record", "dataset" if kind == "dataset" else "unclear", topic
        )
        if item: out.append(item)
    return out

def figshare(topic):
    data = get_json("https://api.figshare.com/v2/articles/search",
        {"search_for": topic, "order": "published_date", "order_direction": "desc", "page_size": 25, "page": 1})
    out = []
    for rec in data if isinstance(data, list) else []:
        item_type = str(rec.get("defined_type_name") or "").lower()
        if item_type and item_type not in ("dataset", "fileset"): continue
        item = make_item(
            "Figshare", rec.get("title"),
            rec.get("url_public_html") or f"https://figshare.com/articles/dataset/{rec.get('id')}",
            rec.get("published_date"), rec.get("description"), rec.get("doi"),
            "", "See original record", "dataset" if item_type in ("dataset", "fileset") else "unclear", topic)
        if item: out.append(item)
    return out

def huggingface(topic):
    args = urllib.parse.urlencode({"search": topic, "limit": 25, "sort": "lastModified", "direction": "-1"})
    data = get_json("https://huggingface.co/api/datasets?" + args)
    out = []
    for rec in data if isinstance(data, list) else []:
        card = rec.get("cardData") or {}
        title = rec.get("id") or rec.get("name") or ""
        description = rec.get("description") or card.get("description", "")
        item = make_item("Hugging Face", title, "https://huggingface.co/datasets/" + urllib.parse.quote(title, safe="/"),
            rec.get("createdAt") or rec.get("lastModified"), description,
            card.get("doi", ""), str(card.get("license", "")), "Gated" if rec.get("gated") else "See dataset card", "dataset", topic)
        if item: out.append(item)
    return out

def europepmc(topic):
    # Scientific paper search: NEVER assert dataset is hosted by this publication.
    query = f'({topic}) AND (dataset OR "data descriptor" OR benchmark OR "publicly available") sort_date:y'
    args = urllib.parse.urlencode({"query": query, "format": "json", "pageSize": 25, "resultType": "lite"})
    data = get_json("https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + args)
    out = []
    for rec in (data.get("resultList") or {}).get("result", []):
        source_id = rec.get("id")
        source = rec.get("source", "")
        url = (f"https://europepmc.org/article/{source}/{source_id}"
               if source_id and source else f"https://doi.org/{rec.get('doi')}" if rec.get("doi") else "")
        item = make_item("Europe PMC", rec.get("title"), url,
            rec.get("firstPublicationDate") or rec.get("firstIndexDate"),
            rec.get("journalTitle") or "", rec.get("doi"),
            "", "Publication; dataset access unconfirmed", "publication_lead", topic)
        if item: out.append(item)
    return out

def load_prior():
    if not OUTPUT.exists(): return []
    try:
        with OUTPUT.open(encoding="utf8") as f:
            obj = json.load(f)
        return obj.get("records", [])
    except (ValueError, OSError, AttributeError):
        return []

def main():
    previous = load_prior()
    curated_names, curated_dois, curated_urls = known_ids()
    seen = set()
    records = {}
    for r in previous:
        if not isinstance(r, dict): continue
        key = r.get("doi") or canonical_url(r.get("url", "")) or slug(r.get("title", ""))
        if key: records[key] = r
    sources = ["Zenodo", "Figshare", "Hugging Face", "Europe PMC"]
    counts = Counter()
    successes = Counter()
    failures = Counter()
    recent = 0
    jobs = [(fn, topic) for fn in (zenodo, figshare, huggingface, europepmc) for topic in TOPICS]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        future_map = {pool.submit(fn, topic): (fn.__name__, topic) for fn, topic in jobs}
        for future in concurrent.futures.as_completed(future_map):
            source, topic = future_map[future]
            try:
                items = future.result()
                successes[source] += 1
                for r in items:
                    name = slug(r["title"])
                    doi = r.get("doi", "")
                    url = canonical_url(r.get("url", ""))
                    if name in curated_names or (doi and doi in curated_dois) or (url and url in curated_urls):
                        continue
                    key = doi or url or name
                    old = records.get(key)
                    if old:
                        r["first_seen"] = old.get("first_seen") or TODAY
                        # preserve richer metadata where API response is missing information
                        for k in ("description", "license", "doi", "date"):
                            if not r.get(k): r[k] = old.get(k, "")
                        if old.get("source_type") == "dataset" and r["source_type"] == "publication_lead":
                            r["source_type"] = "dataset"
                        if old.get("source") and old["source"] != r["source"]:
                            r["source"] = old["source"] + "; " + r["source"] if r["source"] not in old["source"] else old["source"]
                    else:
                        recent += 1
                    records[key] = r
                    counts[source] += 1
            except Exception as exc:
                failures[source] += 1
                print(f"Warning: {source} query {topic!r} failed: {type(exc).__name__}: {str(exc)[:140]}")
    # Reduce storage, prioritize currently active records and recent discoveries.
    ordered = sorted(records.values(), key=lambda r: (r.get("last_seen", ""), r.get("date", ""), r.get("first_seen", "")), reverse=True)[:1500]
    stats = []
    for label, internal in zip(sources, ("zenodo", "figshare", "huggingface", "europepmc")):
        stats.append({"source": label, "query_count": len(TOPICS), "successful_queries": successes[internal],
                      "failed_queries": failures[internal], "retrieved_candidate_matches": counts[internal]})
    result = {"updated_at": NOW, "sources": stats, "records": ordered,
              "total_records": len(ordered), "new_this_scan": recent,
              "note": "Automatically discovered public metadata only. Every record is unverified; Europe PMC records are publication leads, not confirmed datasets. Sources may fail or be rate-limited. Not an exhaustive index."}
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
    print(f"Saved {len(ordered)} discovery leads ({recent} newly noticed), source API successes: {sum(successes.values())}/{len(jobs)}")

if __name__ == "__main__":
    main()
