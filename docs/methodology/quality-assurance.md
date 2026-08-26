# Quality Assurance Framework

## Purpose

Quality assurance is distributed across the full HARC/NAPWR workflow.

It is not a final proofreading step. It tests whether archival relationships remain intact as information moves among physical collections, spreadsheets, EAD, ArchivesSpace, digital storage, Omeka S, NAPWR, and public discovery.

## QA Domains

### Structural Integrity

Validate:

- parent-child hierarchy
- series/subseries relationships
- record granularity
- box/folder relationships
- component levels
- duplicate rows

### Metadata Completeness

Check required or expected values for:

- title
- collection relationship
- repository/hub
- congregation
- identifier
- date
- source link
- rights
- media when applicable

### Authority Integrity

Check:

- existing agent matches
- duplicate identities
- name variants
- congregation forms
- place normalization
- creator vs. subject distinctions

### Digital-Object Integrity

Validate:

- primary file URL
- thumbnail URL
- host
- file type
- duplicate media
- source-to-media relationship
- public accessibility where intended

### Provenance Integrity

Retain:

- source file
- source sheet
- original value
- source identifier
- authoritative URL
- transformation note when needed

### Semantic Integrity

Ask:

- Did normalization change meaning?
- Was a local term incorrectly collapsed?
- Was ambiguity converted into certainty?
- Was inherited context applied too broadly?

## QA Methods

- deterministic validation scripts
- audit CSVs
- exception logs
- stratified sampling
- box-level verification
- source-to-output comparison
- EAD comparison
- authority comparison
- link validation
- portal spot checks
- user/discovery feedback

## Severity Levels

| Level | Meaning | Action |
|---|---|---|
| Critical | Invalidates ingest, provenance, identity, or access | Stop and correct |
| High | Material descriptive or structural error | Correct before publication |
| Medium | Discoverability or consistency issue | Correct in current QA cycle |
| Low | Cosmetic or non-blocking normalization issue | Record and batch-correct |
| Informational | Review note or unusual source behavior | Document |

## Sampling Strategy

For large imports, combine automated validation with stratified human review.

Sample across:

- hierarchical levels
- date ranges
- congregations
- digital and non-digital records
- records with inherited values
- records with repaired dates
- authority matches
- exception categories

## Discovery as QA

Public interfaces may reveal upstream problems.

Examples:

- missing facet → inconsistent field mapping
- duplicate person → unresolved authority identity
- broken media → URL or derivative problem
- irrelevant results → uncontrolled vocabulary or poor mapping
- missing result → incomplete ingest or normalization failure

Discovery should therefore be monitored as part of systems validation.

## Required QA Outputs

Each major ingest should produce, when applicable:

1. normalized output
2. audit report
3. exception report
4. validation summary
5. source-to-output traceability
6. congregation case-file update
