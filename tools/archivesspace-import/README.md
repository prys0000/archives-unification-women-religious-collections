# ArchivesSpace Import Toolset

## Function

Prepares and validates records for ArchivesSpace ingest while preserving hierarchy, authority relationships, containers, dates, and digital-object associations.

## Typical Tasks

- normalize CSV/XLSX structure
- verify required bulk-import columns
- repair invalid workbook artifacts
- validate parent-child hierarchy
- populate defensible date expressions
- match creators against existing agent authorities
- verify container values
- validate digital-object links
- generate upload-ready output

## Validation Priority

1. structure
2. hierarchy
3. agents
4. identifiers
5. dates
6. containers
7. digital objects
8. encoding

## Principle

Successful spreadsheet loading is not the same as successful archival ingest. The output must also be contextually and relationally valid.
