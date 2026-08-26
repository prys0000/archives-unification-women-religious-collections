# Templates

## NAPWR Import Template

`NAPWR-import-template-dcterms.csv` contains the canonical 15-field import header used for shared Omeka/NAPWR transformation.

Do not casually reorder or rename these columns in production workflows without updating the crosswalk documentation and transformation scripts.

## Validation Templates

- `validation-checklist.csv` — record/check-level QA results
- `exception-log.csv` — unresolved or resolved processing exceptions
- `authority-reconciliation-template.csv` — candidate authority decisions

Rows included in the templates are clearly marked as examples and should be removed or replaced in production.
