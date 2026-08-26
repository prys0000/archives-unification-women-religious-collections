# Spreadsheet Normalization Toolset

## Function

Repairs and restructures legacy tabular data before archival ingest.

## Common Problems

- mixed hierarchy in rows
- false subject columns
- duplicate semantic fields
- inconsistent headers
- hidden formatting artifacts
- encoding corruption
- multiline values
- inconsistent dates
- identifiers in multiple locations
- overlapping sheets

## Target

```text
One Row = One Archival Record
```

with explicit, stable fields and preserved provenance.

## Provenance Columns

Recommended working columns:

- source_file
- source_sheet
- source_row
- original_identifier
- raw_text
- normalization_note

## Principle

Normalize structure without discarding historical content.
