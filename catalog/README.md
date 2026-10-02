# Catalogue index

Use this page as the entry point to the repository's dataset records. The CSVs group records by data type or research use because many datasets support more than one clinical specialty. Use the [specialty map](specialties.md) to find records across catalogues.

## Catalogues

| Catalogue | Records | Main contents | File |
|---|---:|---|---|
| Dental imaging | 11 | Panoramic and periapical radiographs, CBCT, annotations, and segmentation | [dental_imaging.csv](dental_imaging.csv) |
| Oral medicine | 25 | Oral mucosal disease, oral pathology, and oral cancer resources | [oral_medicine.csv](oral_medicine.csv) |
| Digital dentistry | 11 | Intraoral scans, virtual-patient data, facial motion, and jaw tracking | [digital_dentistry.csv](digital_dentistry.csv) |
| Clinical reasoning benchmarks | 5 | Dental QA, multimodal benchmarks, and controlled-access clinical sets | [clinical_reasoning_benchmarks.csv](clinical_reasoning_benchmarks.csv) |

The 52 rows are catalogue records, not 52 confirmed unique datasets. Check identifiers, source URLs, and verification notes before counting or combining records.

## Find records

- **By specialty:** open the [specialty map](specialties.md), which links to every relevant catalogue and calls out known coverage gaps.
- **By data type or research use:** choose a catalogue from the table above.
- **By access, licence, or verification status:** inspect the corresponding CSV columns and read the [schema guide](SCHEMA.md).

## Discovery queue

[Open the discovery queue](discovery_queue.csv) for 42 additional leads from the [ITU/WHO dental dataset index](https://github.com/sergiouribe/dental_datasets_itu/blob/main/AI_Dental_Datasets_List.md). These are **unverified leads**, not confirmed records. The queue preserves reported platform, DOI, modality, and scale where listed; it flags each lead for a primary-source, access, licence, and duplicate check before promotion.

## Curation notes

- These files contain metadata and links, not copies of patient data.
- An empty dataset URL or an unclear access status means direct access was not verified.
- A live link check does not confirm that files remain available or that reuse is permitted.
- See [sources and verification rules](../SOURCES.md) before relying on a record.
