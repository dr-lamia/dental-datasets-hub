# Sources and verification rules

## Source order

1. Official dataset landing page or repository.
2. Dataset descriptor or peer-reviewed paper.
3. Maintainer or institutional page that explains access and reuse terms.
4. Existing curated index as a discovery aid only.

Useful discovery indexes include the [ITU/WHO dental imaging dataset review](https://github.com/sergiouribe/dental_datasets_itu) and the [NLM Dataset Catalog](https://datasetcatalog.nlm.nih.gov/). Discovery results must be checked against the original source before a record is marked verified.

## Imported catalogues

Two existing repositories owned by the maintainer were carried into this hub:

- [oral-medicine-ai-datasets](https://github.com/dr-lamia/oral-medicine-ai-datasets): 25 records in its source README/catalogue, with original access, provenance, and verification fields preserved in `catalog/oral_medicine.csv`. That source README states a verification date of 2026-09-28. This hub has not independently rechecked all 25 primary sources.
- [dental-virtual-patient-datasets](https://github.com/dr-lamia/dental-virtual-patient-datasets): 11 records, with the original schema preserved in `catalog/digital_dentistry.csv`. Recheck source access and licence before reuse.

The import preserves these records for continuity; it does not certify every inherited detail as independently verified.

- [DentaGraph research hub](https://github.com/dr-lamia/DentaGraph-research-hub): public benchmark leads from its dataset/benchmark resource page were checked against their official dataset or publication pages and added to `catalog/clinical_reasoning_benchmarks.csv`. A private project-study Drive link in the working document was not copied into this public repository.

## New dental-imaging records

The entries in `catalog/dental_imaging.csv` were prepared from official Zenodo, PhysioNet, challenge, institutional project, or publication pages on 2026-10-03. The verification note records uncertainty that remained on the source page. Where a source exposed no licence field in the page view, the catalogue does not infer one from the platform's general policy.

## What “checked” means

A maintainer should:

- Confirm the URL resolves to the intended dataset, not only a paper mentioning it.
- Record whether files can be downloaded directly, need an account, or require approval/training/a DUA.
- Copy the licence exactly as shown on the source record, or state that it was not shown.
- Record what a count measures: patients, cases, images, scans, slides, or annotations.
- Prefer patient/case-level information and note when it is unavailable.
- Record the date in ISO format. A live link check only confirms that a web server responds; it does not verify dataset contents or reuse rights.
