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

## New dental-imaging records

The entries in `catalog/dental_imaging.csv` were prepared from official Zenodo, PhysioNet, challenge, institutional project, or publication pages on 2026-10-03. The verification note records uncertainty that remained on the source page. Where a source exposed no licence field in the page view, the catalogue does not infer one from the platform's general policy.

## Clinical reasoning benchmark records

The entries in `catalog/clinical_reasoning_benchmarks.csv` link to dataset repositories/cards or primary publication pages where available. Each record's verification note states what was confirmed and what remains uncertain; a paper, code repository, or public benchmark page does not by itself establish data access or reuse rights.

## Discovery sources and coverage

The maintainers use these sources to find candidates across imaging, clinical, population-health, education, digital-dentistry, and oral-health research. They are discovery tools; each catalogue record should link to its own primary source.

- [ITU/WHO dental dataset index](https://github.com/sergiouribe/dental_datasets_itu/blob/main/AI_Dental_Datasets_List.md): an editable index focused on dental imaging and AI.
- [NLM Dataset Catalog](https://datasetcatalog.nlm.nih.gov/): search biomedical records with dental, oral-health, craniofacial, modality, and specialty terms.
- [NIDCR Data-Driven Science Hub](https://www.ddshub.nih.gov/data-sources): curated dental, oral, and craniofacial sources, including population, phenotype, multi-omic, imaging, and biospecimen data.
- [Systematic review of openly accessible oral-maxillofacial imaging datasets](https://doi.org/10.1038/s41746-025-01818-5): reports 105 datasets from searches of literature and dataset platforms through September 2024. Its imaging scope does not cover every dental or oral-health data type.
- [Dental image-analysis dataset review and project page](https://github.com/zhenhuanZ/DIA-Review): a separate review of publicly available AI dental-image datasets.

The current `catalog/discovery_queue.csv` holds 42 leads transcribed from the ITU/WHO index. Leads need primary-source verification and deduplication before they are promoted. The queue is a starting point, not an exhaustive inventory. Some datasets are private, controlled-access, newly released, poorly indexed, or described only in papers.

## What “checked” means

A maintainer should:

- Confirm the URL resolves to the intended dataset, not only a paper mentioning it.
- Record whether files can be downloaded directly, need an account, or require approval/training/a DUA.
- Copy the licence exactly as shown on the source record, or state that it was not shown.
- Record what a count measures: patients, cases, images, scans, slides, or annotations.
- Prefer patient/case-level information and note when it is unavailable.
- Record the date in ISO format. A live link check only confirms that a web server responds; it does not verify dataset contents or reuse rights.
