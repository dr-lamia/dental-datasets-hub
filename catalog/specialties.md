# Browse by specialty

This map is a crosswalk, not a separate dataset list. Follow the links to the CSV records; a record may appear relevant to multiple specialties. Check its source, access, licence, and verification note before use.

## Oral medicine, pathology, and cancer

| Specialty | Catalogue links | Coverage and gaps |
|---|---|---|
| Oral medicine and oral mucosal disease | [Oral medicine](oral_medicine.csv) | Clinical photographs, mucosal lesions, referral triage, and related resources |
| Oral pathology and oral cancer | [Oral medicine](oral_medicine.csv) | Histopathology, cytology, clinical images, and head-and-neck cohorts; confirm anatomical subsite and patient grouping |

## Imaging, diagnosis, and surgery

| Specialty | Catalogue links | Coverage and gaps |
|---|---|---|
| Oral and maxillofacial radiology | [Dental imaging](dental_imaging.csv), [benchmarks](clinical_reasoning_benchmarks.csv) | Panoramic and periapical radiographs, CBCT, annotations, segmentation, and panoramic VQA |
| Endodontics | [Dental imaging](dental_imaging.csv), [benchmarks](clinical_reasoning_benchmarks.csv) | Periapical images and benchmark questions; dedicated endodontic cohorts need further discovery |
| Periodontology | [Dental imaging](dental_imaging.csv), [clinical decision support](clinical_reasoning_benchmarks.csv), [dedicated periodontics catalogue](https://github.com/dr-lamia/periodontics-datasets) | Bone-loss imaging, ultrasound, periodontal maintenance (883 patients), single-cell, microbiome and restricted omics; dedicated repository has 29 metadata records, not independent cohorts |
| Oral surgery and implant planning | [Dental imaging](dental_imaging.csv), [Digital dentistry](digital_dentistry.csv) | CBCT anatomy, missing-tooth annotations, and multimodal resources; no implant-only dataset is verified in this snapshot |
| Pediatric dentistry | [Benchmarks](clinical_reasoning_benchmarks.csv) | Broad dental knowledge benchmarks may include pediatric questions; no dedicated pediatric patient-imaging cohort is verified |

## Restorative care and digital dentistry

| Specialty | Catalogue links | Coverage and gaps |
|---|---|---|
| Prosthodontics | [Digital dentistry](digital_dentistry.csv), [Dental imaging](dental_imaging.csv) | Intraoral scans, paired CBCT/oral scans, and jaw-motion resources; access terms vary |
| Restorative and operative dentistry | [Dental imaging](dental_imaging.csv), [benchmarks](clinical_reasoning_benchmarks.csv) | Panoramic disease labels, a 6,377-image caries photographic deposit, and a 753-image tooth-crack dataset; check patient grouping and licence |
| Orthodontics | [Digital dentistry](digital_dentistry.csv) | General dental scans and facial resources may support methods development; orthodontic labels and cohorts need further curation |
| Digital dentistry and dental materials | [Digital dentistry](digital_dentistry.csv) | Intraoral scans, facial/4D data used in virtual-patient work, and jaw tracking; material-specific datasets need further curation |

## Education and cross-specialty research

| Specialty or use | Catalogue links | Coverage and gaps |
|---|---|---|
| Dental education and knowledge assessment | [Clinical reasoning benchmarks](clinical_reasoning_benchmarks.csv) | DentalBench and GlobalDentBench include QA or clinical reasoning; no student-performance cohort is verified |
| General dentistry and multimodal research | [Dental imaging](dental_imaging.csv), [Digital dentistry](digital_dentistry.csv), [benchmarks](clinical_reasoning_benchmarks.csv) | Mixed-modality resources and controlled-access cohorts; verify each record's intended population and permitted use |

## Coverage rule

“Not yet verified” means maintainers have not confirmed a primary source and usable metadata for that specialty. It does not mean no dataset exists. Suggest candidates through an issue or pull request, following [the contribution guide](../CONTRIBUTING.md).
