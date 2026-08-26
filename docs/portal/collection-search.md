# Collection Search

## Purpose

The NAPWR collection search enables researchers to discover evidence across contributing repositories without first knowing where that evidence is held.

## Discovery Model

Traditional repository-first discovery asks:

> Which archive should I search?

NAPWR supports:

> What evidence exists across the archival network?

Repository location becomes a facet of the result rather than a prerequisite for the search.

## Core Facets

Current/target facets include:

- congregation
- contributing hub
- date
- spatial location
- creator
- subject

Additional facets should be introduced only when:

- source data is sufficiently consistent;
- the field is meaningful across repositories;
- normalization rules are documented;
- the facet improves rather than fragments discovery.

## Search Requirements

A portal record should ideally provide:

- recognizable title
- collection context
- congregation
- contributing repository
- date
- source link
- description where available
- creator/subject/place when useful
- media where appropriate

## Retrieval Quality

Evaluate search through:

### Precision

Are results relevant?

### Recall

Are known relevant records discoverable?

### Facet Stability

Do conceptually equivalent values group together?

### Provenance Visibility

Can the user tell where the record came from?

### Source Navigation

Can the user reach the authoritative finding aid or record?

## Search as QA

Problem patterns:

| Search Symptom | Possible Upstream Cause |
|---|---|
| Same congregation appears under multiple facet values | vocabulary inconsistency |
| Known record absent | ingest/filtering issue |
| Too many irrelevant results | overly broad inheritance |
| Creator missing | authority/crosswalk problem |
| Broken source link | source URL or identifier problem |
| Duplicate records | duplicate ingest or identifier collision |

## Design Rule

The portal should simplify discovery without hiding archival context.
