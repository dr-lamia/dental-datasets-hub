# Dental Datasets Hub

A growing, specialty-organized directory of dental and oral-health datasets for research, teaching, and tool development.

> **Scope:** this is a curated directory, not a claim that every dental dataset worldwide has already been found. It stores catalogue metadata and links only; it does not redistribute patient images or source dataset files. Dataset access, ethics, and reuse conditions are set by each original provider.

## Browse the catalogues

| Area | Catalogue | What it covers |
|---|---|---|
| Dental imaging, radiology, and cross-specialty datasets | [Dental imaging catalogue](catalog/dental_imaging.csv) | Panoramic and periapical radiographs, CBCT, diagnostic labels, and segmentation resources |
| Oral medicine, oral pathology, and oral cancer | [Oral medicine catalogue](catalog/oral_medicine.csv) | 25 records carried forward from the existing oral-medicine catalogue |
| Digital dentistry and virtual patients | [Digital dentistry catalogue](catalog/digital_dentistry.csv) | Intraoral scans, CBCT–oral-scan pairs, facial motion, and jaw tracking |
| Specialty map | [Browse by specialty](catalog/specialties.md) | Find resources by clinical specialty and see where coverage is still missing |
| Field definitions | [Catalogue schema](catalog/SCHEMA.md) | How to interpret access, licence, verification, and other fields |

## Repository layout

- `catalog/` — machine-readable catalogues and the specialty index.
- `scripts/check_catalog.py` — validates catalogue files and checks source links.
- `.github/workflows/weekly-catalog-review.yml` — weekly link audit and curator reminder.
- [Sources and verification rules](SOURCES.md)
- [How to contribute](CONTRIBUTING.md)
- [Update log](UPDATE_LOG.md)

## Weekly maintenance

Every Sunday, a GitHub Actions workflow checks links in the catalogues and opens a review issue with the audit outcome and a short curation checklist. It can also be run manually from the **Actions** tab.

The workflow does not silently add datasets or alter scientific metadata. New records need a human to check the original dataset page, publication, access rules, and licence before merging. This keeps the weekly process useful without turning search matches or broken links into unverified catalogue facts.

## Reuse and data protection

- Follow the original source's licence, ethics approval, access conditions, and data-use agreement.
- A link marked open or public describes the provider's record; confirm the current download conditions at the source before use.
- Do not upload patient-level data, restricted files, credentials, private links, or large third-party archives here.
- Cite the original dataset and publication in research. Cite this repository only for the catalogue itself.

## Starting coverage

The oral-medicine records and digital-dentistry records were imported from the existing repositories listed below. Their original catalogue fields and verification dates are preserved. The dental-imaging catalogue was seeded from primary dataset and publication pages checked on 2026-10-03. Check each source page again before a study, particularly where the catalogue says the licence or access terms are unclear.

- [Oral medicine source catalogue](https://github.com/dr-lamia/oral-medicine-ai-datasets)
- [Dental virtual-patient source catalogue](https://github.com/dr-lamia/dental-virtual-patient-datasets)
- [DentaGraph dataset and benchmark resources](https://github.com/dr-lamia/DentaGraph-research-hub)

## Citation

Please cite the original dataset providers when using data. A repository citation file will be added after the catalogue has a stable release and citation record.
