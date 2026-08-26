# EAD to Omeka S / NAPWR Crosswalk

## Purpose

This crosswalk documents transformation from EAD archival description into the shared NAPWR Omeka S discovery schema.

The output is intentionally narrower than the full EAD record. NAPWR is a discovery layer; the source finding aid remains authoritative.

## Core Mapping

| NAPWR / Omeka Field | EAD Source / Rule | Notes |
|---|---|---|
| `dcterms:title` | component `unittitle` | Required for portal record |
| `dcterms:alternative` | local alternate title when present | Otherwise blank |
| `dcterms:isPartOf` | collection / parent relationship | Preserve collection context |
| `dcterms:publisher` | repository / contributing institution | Controlled hub value |
| `dcterms:creator` | nearest valid `origination` | Inheritance must be reviewable |
| `dcterms:contributor` | mapped contributor when explicitly supported | Do not infer |
| `dcterms:date` | display/normalized `unitdate` | Prefer defensible display value |
| `dcterms:spatial` | geographic terms | May include controlled inheritance |
| `dcterms:subject` | subject, occupation, function, title terms | Normalize without erasing variants |
| `dcterms:type` | genre/form or conservative media inference | Avoid speculative classification |
| `dcterms:description` | scope/content, abstract, descriptive fallback | Preserve source meaning |
| `dcterms:source` | authoritative source finding-aid/ArchivesSpace URL | Required traceability |
| `dcterms:identifier` | component `unitid` | Preserve legacy values if needed |
| `dcterms:rights` | use restriction or shared rights statement | Do not overgeneralize |
| `Media URL` | approved digital object / derivative | Prefer thumbnail for portal display when documented |

## Hierarchy Rules

- Do not flatten collection relationships without retaining `isPartOf`.
- File/item records may inherit selected context only from documented valid parents.
- Inheritance should never fabricate record-specific facts.
- If the source hierarchy is malformed, log the exception before transformation.

## Creator Inheritance

Creator inheritance may be used when:

1. the child lacks a creator;
2. the parent creator clearly governs the child;
3. the relationship is structurally supported;
4. the inherited value is recorded as derived/inherited in audit output.

Do not inherit a creator merely because it is nearby in XML.

## Date Rules

Preferred order:

1. explicit component date;
2. normalized date expression from source;
3. conservative derivation from title when unambiguous and permitted by workflow;
4. blank + exception flag.

Never convert uncertainty into exactness.

## Subject and Spatial Inheritance

Inheritance can improve discovery but may create over-description.

Use only when:

- the parent term clearly applies to descendants;
- scope is documented;
- audit output identifies inherited values.

## Media Selection

Approved logic may:

- detect direct public digital-object URLs;
- prefer thumbnail derivatives for portal display;
- fall back to a primary file if no thumbnail exists;
- exclude representative series-level images unless explicitly configured;
- retain the source archival record URL separately.

## Required Audit Fields

Recommended:

- source_file
- source_component_id
- source_level
- output_identifier
- title
- creator_source
- date_source
- inherited_fields
- media_source
- warnings
- transformation_version

## Validation

Before Omeka ingest:

- verify exact header order
- verify UTF-8 encoding
- verify no malformed line breaks
- verify source URLs
- verify media URLs
- verify collection relationship
- review inherited metadata
- review exceptions
