# ArchivesSpace to NAPWR Crosswalk

## Purpose

This document defines the relationship between ArchivesSpace descriptive structures and the NAPWR discovery layer.

NAPWR should expose enough information for cross-repository discovery without duplicating the entire ArchivesSpace data model.

## Architectural Relationship

```text
ArchivesSpace
    │
    ├── authoritative hierarchy
    ├── archival objects
    ├── agents
    ├── subjects
    ├── dates
    ├── containers
    └── digital objects
         ↓
Transformation / Reconciliation
         ↓
NAPWR Canonical Discovery Record
         ↓
Omeka S / Search / Name Index / Chatbot
```

## Mapping Principles

### ArchivesSpace Remains Authoritative

NAPWR records should preserve a source URL whenever a public source record exists.

### NAPWR Uses a Discovery Subset

Not every ArchivesSpace field should be copied.

Preference is given to information supporting:

- identification
- context
- cross-repository search
- person/congregation discovery
- place
- date
- subject
- digital access

### Container Data

Container values are generally processing/control data rather than primary portal facets.

Preserve them in ArchivesSpace and reconciliation documentation unless a public-use case requires exposure.

### Agents

Before creating or mapping an agent:

- compare against existing authorized agents;
- use stable identifiers when available;
- preserve variant forms;
- avoid accidental duplicate person creation.

### Dates

ArchivesSpace display and normalized dates may serve different functions.

NAPWR generally requires a researcher-readable date value, while normalized values may support sorting/filtering if implemented.

### Digital Objects

Verify that digital objects:

- correspond to the correct archival object;
- use the intended public derivative;
- preserve the relationship to the source description;
- do not duplicate the same media unintentionally.

## Canonical NAPWR Fields

| NAPWR Field | ArchivesSpace Source |
|---|---|
| Title | resource / archival object title |
| Collection | resource title / parent resource |
| Repository / Hub | repository context |
| Congregation | controlled project field / mapped authority |
| Creator | linked agent or origination |
| Date | date expression |
| Spatial | subject/geographic term |
| Subject | linked subjects/functions/occupations as mapped |
| Type | genre/form or media type |
| Description | scope/content, abstract, note |
| Source | public ArchivesSpace URL |
| Identifier | resource/component identifier |
| Rights | restriction/use note or shared statement |
| Media | linked digital object / approved derivative |

## Reconciliation Before Export

Do not treat a successful ArchivesSpace export as proof that the data is ready for NAPWR.

Check:

- hierarchy
- duplicate agents
- missing dates
- malformed titles
- inconsistent identifiers
- unexpected inheritance
- broken digital objects
- legacy terminology needing mapped variants
