# EAD-to-Omeka Toolset

## Function

Transforms EAD exported from archival systems into the shared NAPWR DCTERMS-oriented Omeka S import structure.

## Expected Components

Typical production folder may include:

- `RUN_EAD_TO_OMEKA.bat`
- `ead_to_omeka.py`
- NAPWR import template
- audit output
- parse-warning output

## Workflow

```text
EAD/XML
  ↓
BAT launcher
  ↓
Python parser
  ↓
crosswalk + normalization
  ↓
validation
  ↓
Omeka-ready CSV
  + audit report
  + warnings
```

## Required Controls

- preserve source filename
- preserve source component identifiers
- log inherited metadata
- preserve authoritative source URL
- validate UTF-8
- validate exact CSV headers
- validate media selection
- output warnings rather than silently dropping malformed records

## Do Not

- overwrite source EAD
- infer uncertain creators
- convert ambiguous dates into exact dates
- treat a successful parse as sufficient QA
