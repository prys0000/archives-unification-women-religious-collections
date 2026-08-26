# Adaptive Learning Model

## Purpose

The HARC/NAPWR adaptive learning model converts repeated archival problem-solving into reusable, transparent institutional knowledge.

The model is **human-supervised**. It does not assume that automated systems should independently determine archival meaning.

Instead:

```text
NEW INGEST
    ↓
EXCEPTION
    ↓
ARCHIVIST REVIEW
    ↓
DECISION
    ↓
RULE FORMALIZATION
    ↓
VALIDATION
    ↓
REUSE
```

## What "Learning" Means

Learning occurs when a resolved processing problem becomes an explicit and reusable element of the system.

Examples include:

- a new date-normalization pattern
- an EAD parsing exception
- an authority-name mapping
- a congregation-specific vocabulary rule
- a malformed spreadsheet repair
- a hierarchy-validation test
- a digital-object selection rule
- a known character-encoding repair
- a controlled repository or congregation value
- a new exception category

## Institutional Computational Memory

The accumulated knowledge is stored in:

- scripts
- BAT launchers
- crosswalks
- authority tables
- exception logs
- validation templates
- data dictionaries
- congregation case records
- documented processing decisions

This collection of artifacts functions as **institutional computational memory**.

## Decision Classes

### Deterministic

Safe to automate when inputs meet defined conditions.

Examples:

- trim whitespace
- convert known encoding corruption
- populate a fixed repository value
- transform a known EAD element into a defined DCTERMS field
- prefer an existing thumbnail when a documented naming rule is satisfied

### Conditional

Automate only when evidence passes a test.

Examples:

- deriving a date from a title when a date pattern is unambiguous
- inheriting a creator from the nearest valid parent component
- applying geographic inheritance
- identifying a digital object from an approved host

### Interpretive

Require archivist review.

Examples:

- changing intellectual arrangement
- resolving ambiguous personal identity
- choosing between competing provenance claims
- determining whether local terminology is synonymous
- interpreting restrictions
- assigning uncertain creators

## Rule Lifecycle

Every reusable rule should record:

| Element | Requirement |
|---|---|
| Rule ID | Stable identifier |
| Trigger | Condition that activates the rule |
| Source | Where the problem was first observed |
| Action | Transformation or validation behavior |
| Confidence | Deterministic / conditional / interpretive |
| Reviewer | Person or role approving the rule |
| Version | Rule version |
| Exceptions | Known cases where the rule should not run |
| Evidence | Source fields or documentation supporting the decision |

## Change Control

A rule should not silently change historical results.

When a rule is revised:

1. assign a new version;
2. describe the reason;
3. identify affected collections;
4. determine whether prior outputs require reprocessing;
5. record the result in the congregation case file or validation log.

## Relationship to AI

AI can assist with:

- suggesting potential mappings
- summarizing exception patterns
- interpreting natural-language user queries
- identifying candidate entities
- generating review queues

AI should not silently:

- create authoritative biographical facts
- alter provenance
- resolve ambiguous identities
- impose arrangement decisions
- change rights or restrictions
- overwrite source evidence

The governing principle is **AI-assisted review, not AI-derived archival authority**.

## Measures of Success

The adaptive model should reduce:

- repeated manual cleanup
- inconsistent decisions
- undocumented exceptions
- hub-to-hub variation
- ingest failures

while increasing:

- traceability
- consistency
- explainability
- processing speed
- recoverability
- reuse of prior archival knowledge
