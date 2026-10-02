# Catalogue schema and status guide

The hub keeps three CSV catalogues so the pre-existing specialist inventories can be carried over without discarding their original fields:

- `dental_imaging.csv` uses the common fields below.
- `oral_medicine.csv` preserves the fields from the established oral-medicine dataset inventory.
- `digital_dentistry.csv` preserves the fields from the established virtual-patient inventory.

## Common fields

| Field | Meaning |
|---|---|
| `dataset_id` | Stable short identifier used in this catalogue |
| `dataset_name` | Name used by the dataset provider or publication |
| `specialties` | Relevant clinical or technical areas, separated by semicolons |
| `modality` | Type of data, such as panoramic radiograph, periapical image, CBCT, or intraoral scan |
| `scale_or_cases` | Reported number of cases, images, scans, or other scale detail; retain the unit |
| `labels_or_tasks` | Labels, annotations, or intended task reported by the source |
| `access_status` | `public_download`, `account_required`, `controlled_access`, or `unclear` |
| `license_status` | Exact licence if the source states one; otherwise say `Not stated on source page checked` or `Needs verification` |
| `dataset_url` | Primary dataset page or repository |
| `publication_url` | Descriptor paper or source publication, if known |
| `last_checked` | Date a maintainer checked the linked source page (ISO `YYYY-MM-DD`) |
| `verification_note` | Limits or uncertainty that a researcher should know |

## Important distinctions

- **Public record** does not always mean unrestricted download or unrestricted reuse.
- **Account required** means the source page says an account is needed; additional terms may apply.
- **Controlled access** means an application, approval, training, or data-use agreement is required.
- **Not stated** is not a licence. Ask the provider or consult the full record before reuse.
- Counts from a paper can refer to images, slices, scans, or patients. Never combine them into one count.
- A dataset used for a specialty is not necessarily representative of that specialty.
