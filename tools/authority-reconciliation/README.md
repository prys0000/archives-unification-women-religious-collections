# Authority Reconciliation Toolset

## Function

Supports consistent person, congregation, organization, subject, and geographic values across source systems and NAPWR.

## Workflow

```text
RAW VALUE
   ↓
NORMALIZATION
   ↓
CANDIDATE MATCH
   ↓
CONFIDENCE CLASS
   ↓
HUMAN REVIEW WHEN NEEDED
   ↓
AUTHORIZED / RECONCILED VALUE
   + preserved variant
```

## Match Classes

- exact
- probable
- ambiguous
- distinct
- new authority candidate

## Required Output

Preserve:

- source value
- normalized comparison value
- authority identifier if available
- selected authorized form
- confidence
- reviewer
- decision note

## Principle

Authority control improves interoperability only when it does not erase historically meaningful variants.
