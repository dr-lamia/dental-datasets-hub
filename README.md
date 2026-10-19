# Dental Datasets Hub

A curated, specialty-organized directory of dental and oral-health dataset metadata for research, teaching, and tool development. This repository stores descriptions and source links; it does not redistribute patient images or dataset files.

## Website: dental and maxillofacial dataset atlas

- **[Interactive website preview](https://id-preview--75a91ea4-9e71-48ee-8219-b694a6e78983.lovable.app):** curated catalogue, speciality filters, compare, review queue, and **Discover** page.
- **[Browse automatically discovered leads](catalog/auto_discovery.json):** public metadata from Zenodo, Figshare, Hugging Face, and Europe PMC (publication leads). This is separate from the human-curated catalogues.
- **[Discovery script](scripts/discover_datasets.py):** nightly query with clinical relevance filtering, DOI/URL/title deduplication, first/last-seen dates, and per-source status.
- **[Daily automation](.github/workflows/daily-dataset-discovery.yml):** GitHub Actions refreshes auto_discovery.json every day. Discovery does **not** mean verified or downloadable; publication leads are not datasets. This automated feed does **not** promote rows into curated CSVs.
- The website also provides a manual **Search the web now** option using external public APIs. Some platforms (TCIA, PhysioNet, NIDCR, Kaggle, Mendeley Data, Grand Challenge, Dryad, institutional repositories) currently have manual research links rather than an automated ingestion connection. Coverage is not exhaustive.
- Records are only promoted into curated catalogues after primary-source, reuse-rights, and clinical relevance review. Always cite the original dataset source.

## Start here

- **[Catalogue index](catalog/README.md):** browse all catalogues, record counts, and how to find entries.
- **[Specialty map](catalog/specialties.md):** find datasets across clinical and technical areas, including known coverage gaps.
- **[Schema guide](catalog/SCHEMA.md):** interpret the catalogue fields, access labels, and licence notes.

## Catalogue overview

| Catalogue | Records | Main focus |
|---|---:|---|
| [Dental imaging](catalog/dental_imaging.csv) | 12 | Radiographs, CBCT, annotations, and segmentation |
| [Oral medicine](catalog/oral_medicine.csv) | 25 | Oral medicine, mucosal disease, pathology, and cancer |
| [Digital dentistry](catalog/digital_dentistry.csv) | 11 | Intraoral scans, virtual patients, facial motion, and jaw tracking |
| [Clinical reasoning benchmarks](catalog/clinical_reasoning_benchmarks.csv) | 5 | Dental QA and multimodal or controlled-access benchmarks |

These are 53 catalogue records, not necessarily 53 unique datasets; some resources may overlap. Use the [catalogue index](catalog/README.md) for details.

## How the repository is organized

- `catalog/*.csv` — machine-readable dataset records, grouped by data type or research use.
- `catalog/specialties.md` — specialty-to-catalogue crosswalk.
- `catalog/SCHEMA.md` — field definitions and status meanings.
- `scripts/check_catalog.py` — validates CSV structure and checks source links.
- `.github/workflows/weekly-catalog-review.yml` — scheduled link audit and curator reminder.
- [Sources and verification rules](SOURCES.md)
- [Contribution guide](CONTRIBUTING.md)
- [Update log](UPDATE_LOG.md)

## Weekly maintenance

Every Sunday, GitHub Actions checks catalogue structure and source links, then opens a review issue with the audit outcome and a curation checklist. The workflow can also be run manually from the **Actions** tab. It does not silently add datasets or change scientific metadata; a maintainer must verify the original source, access rules, and licence before adding a record.

## Reuse and data protection

- Follow the source provider's licence, ethics approval, access conditions, and data-use agreement.
- Confirm download and reuse terms on the source page before use; “public” does not necessarily mean unrestricted.
- Do not upload patient-level data, restricted files, credentials, private links, or third-party archives.
- Cite the original dataset and publication when using data. Cite this repository only for the catalogue.

## Initial coverage

The oral-medicine (25 rows) and digital-dentistry (11 rows) catalogues were imported from existing repositories. The dental-imaging catalogue was seeded with 11 rows on 2026-10-03 and expanded to 12 with an intraoral caries image dataset on 2026-10-19. The clinical-reasoning benchmark (5 rows) catalogue was seeded on 2026-10-03. Imported records were not all independently rechecked; see [SOURCES.md](SOURCES.md) and each record's verification note.

- [Original oral-medicine catalogue](https://github.com/dr-lamia/oral-medicine-ai-datasets)
- [Original dental virtual-patient catalogue](https://github.com/dr-lamia/dental-virtual-patient-datasets)

## Coverage and completeness

The repository aims for broad coverage, but no search can guarantee every dental dataset published anywhere online. It tracks confirmed catalogue records separately from discovery leads that still need primary-source checks. The review queue now includes 71 leads from dental dataset and NIH/NIDCR source indexes; some may be duplicates, outdated, unavailable, or require further review.

Coverage spans dental and oral-health imaging, oral medicine and pathology, digital dentistry, clinical reasoning, and other population or clinical resources as they are verified. See [the catalogue index](catalog/README.md) and [source search strategy](SOURCES.md).

## Citation

Please cite original dataset providers when using their data. See [CITATION.cff](CITATION.cff) to cite this catalogue.
