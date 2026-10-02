#!/usr/bin/env python3
"""Validate catalogue CSVs and check linked source pages without editing catalogue data."""
from __future__ import annotations

import csv
import os
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog"
URL_FIELDS = {"dataset_url", "publication_url", "code_url", "url"}
TIMEOUT = 12
MAX_WORKERS = 8


def inspect_catalogues():
    errors = []
    links = {}
    files = [path for path in sorted(CATALOG.rglob("*.csv")) if path.name != "template.csv"]
    for path in files:
        try:
            with path.open(newline="", encoding="utf-8-sig") as stream:
                reader = csv.DictReader(stream)
                if not reader.fieldnames:
                    errors.append(f"{path.relative_to(ROOT)}: missing CSV header")
                    continue
                for line_no, row in enumerate(reader, start=2):
                    if None in row:
                        errors.append(f"{path.relative_to(ROOT)}:{line_no}: inconsistent number of columns")
                    for field in URL_FIELDS:
                        value = (row.get(field) or "").strip()
                        if not value:
                            continue
                        for url in value.split(";"):
                            url = url.strip()
                            if not url:
                                continue
                            parsed = urlparse(url)
                            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                                errors.append(f"{path.relative_to(ROOT)}:{line_no}: invalid URL in {field}: {url}")
                                continue
                            links.setdefault(url, []).append(f"{path.relative_to(ROOT)}:{line_no}:{field}")
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
    return errors, links, files


def check_url(url):
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "DentalDatasetsHub-LinkAudit/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            return url, response.status, None
    except urllib.error.HTTPError as exc:
        if exc.code in {405, 501}:
            request = urllib.request.Request(
                url, headers={"User-Agent": "DentalDatasetsHub-LinkAudit/1.0", "Range": "bytes=0-0"}
            )
            try:
                with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
                    return url, response.status, None
            except urllib.error.HTTPError as retry:
                return url, retry.code, str(retry.reason)
            except Exception as retry:
                return url, None, str(retry)
        return url, exc.code, str(exc.reason)
    except Exception as exc:
        return url, None, str(exc)


def main():
    errors, links, files = inspect_catalogues()
    print("## Dental dataset catalogue link audit")
    print(f"\nCSV files checked: {len(files)}")
    print(f"Unique source links checked: {len(links)}")

    results = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        jobs = [pool.submit(check_url, url) for url in links]
        for future in as_completed(jobs):
            results.append(future.result())

    broken, uncertain = [], []
    for url, status, error in sorted(results):
        if status in {404, 410}:
            broken.append((url, status, error))
        elif status is None or status in {401, 403, 405, 429} or (status and status >= 500):
            uncertain.append((url, status, error))

    summary = (
        f"\n- Broken links (404/410): **{len(broken)}**"
        f"\n- Inaccessible or inconclusive links: **{len(uncertain)}**"
        f"\n- CSV/schema errors: **{len(errors)}**\n"
    )
    print(summary)
    if broken:
        print("\n### Broken links")
        for url, status, _ in broken[:30]:
            print(f"- [{status}] {url}")
    if uncertain:
        print("\n### Inaccessible or inconclusive (check manually)")
        for url, status, error in uncertain[:30]:
            print(f"- [{status or 'no response'}] {url} — {error or 'access may be restricted'}")
    if errors:
        print("\n### CSV errors")
        for error in errors[:30]:
            print(f"- {error}")

    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with open(step_summary, "a", encoding="utf-8") as stream:
            stream.write(summary)
            for heading, items in (("Broken links", broken), ("Inaccessible or inconclusive", uncertain)):
                if items:
                    stream.write(f"\n### {heading}\n")
                    for url, status, error in items[:30]:
                        suffix = f" — {error}" if error else ""
                        stream.write(f"- [{status or 'no response'}] {url}{suffix}\n")
            if errors:
                stream.write("\n### CSV errors\n")
                for error in errors[:30]:
                    stream.write(f"- {error}\n")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
