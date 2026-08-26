# Sisters Name Authority Fields

## Purpose

The Sisters Name Index is a cross-congregational biographical discovery and identity-reconciliation environment.

Its purpose is not merely to display names. It helps reconcile the multiple identity forms under which women religious may appear across archival systems.

## Core Fields

| Field | Function |
|---|---|
| `dcterms:relation` | related collection, source, or archival context |
| `sbio:congregation` | congregation |
| `foaf:familyName` | family/surname |
| `sbio:religiousName` | religious name |
| `sbio:baptismalName` | baptismal name |
| `dcterms:title` | display title / preferred record label |
| `sbio:dateOfBirth` | birth date |
| `sbio:dateOfDeath` | death date |
| `sbio:lifeDates` | display life dates |
| `sbio:placeOfBirth` | birthplace |
| `sbio:entranceDate` | entrance date |
| `sbio:firstProfessionDate` | first profession |
| `sbio:finalProfessionDate` | final profession |
| `sbio:careerWork` | vocation / career / ministry work |
| `sbio:missionLocations` | mission locations |
| `dcterms:description` | biographical description |
| `sbio:archivistNotes` | internal/contextual notes |
| `dcterms:language` | language |

## Identity Problem

A single individual may appear under combinations of:

- civil name
- baptismal name
- religious name
- initials
- surname variants
- titles
- translated forms
- dates
- congregation-specific naming conventions

These should not automatically be treated as separate people.

## Matching Strategy

Candidate matching may use combinations of:

- family name
- religious name
- baptismal/civil name
- date of birth
- date of death
- entrance date
- congregation

No single field should be assumed sufficient in ambiguous cases.

## Authority Decision Classes

### Exact Match

Multiple stable fields align and no contradiction exists.

### Probable Match

Strong evidence exists but one or more fields are absent.

Requires review before destructive merging.

### Ambiguous

Conflicting or insufficient evidence.

Keep separate until reviewed.

### Distinct

Evidence demonstrates separate individuals.

## Variant Preservation

When identities are reconciled, do not discard alternate forms.

Preserve useful variants for:

- search recall
- historical context
- auditability
- source traceability

## Index Facets

Structured data may support filtering by:

- congregation
- record status
- birth decade
- birthplace
- work/vocation
- mission location
- entrance decade
- profession decades
- death decade
- departure status
- language

## AI Use

AI may identify candidate matches or suggest query expansions, but ambiguous identity resolution remains a human archival decision.
