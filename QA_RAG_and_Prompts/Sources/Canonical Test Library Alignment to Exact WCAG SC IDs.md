---
title: "Canonical Test Library Alignment to Exact WCAG SC IDs"
status: "Superseded"
superseded_on: "2026-09-20"
superseded_by:
  - "Canonical_WCAG_AA_Relationship_Register.md"
  - "Canonical_Test_Library_WCAG_AA_Summary.md"
retrieval_priority: "Do not use for current WCAG mapping or conformance reporting"
ai_ingestion_guidance:
  - "Do not treat the former comma-separated mappings as exact or equivalent WCAG requirements."
  - "Retrieve Canonical_WCAG_AA_Relationship_Register.md for canonical WCAG 2.2 A/AA traceability."
  - "Retrieve Canonical_Test_Library_WCAG_AA_Summary.md for a one-row-per-test view."
---

# Superseded: Canonical Test Library Alignment to Exact WCAG SC IDs

This filename is retained as a stable redirect for existing links. The former table must not be used for current WCAG mapping or conformance reporting.

The former table described every association as an `Exact WCAG SC ID`. That was inaccurate because it combined:

- direct or substantial WCAG relationships;
- partial evidence for a criterion;
- implementation and evaluation techniques;
- WCAG AAA associations; and
- stricter or broader Double FW requirements and inclusive-design practices.

## Current canonical files

- [Canonical WCAG 2.2 A and AA Relationship Register](Canonical_WCAG_AA_Relationship_Register.md) — normalized source of truth with one row per relationship, WCAG level, relationship type, classification and scope note.
- [Canonical Test Library — WCAG 2.2 A and AA Summary](Canonical_Test_Library_WCAG_AA_Summary.md) — one-row-per-test human-readable view generated from the register.
- [Canonical Test Library](<Canonical Test Library.md>) — the stable 200-item requirement and outcome library.

Only WCAG 2.2 Levels A and AA are included in the active relationship register. Stronger, broader or otherwise non-equivalent requirements remain active as **highly recommended best practices** and must not be reported automatically as WCAG failures.

```yaml
canonical: false
active_for_retrieval: false
replacement_register: "Canonical_WCAG_AA_Relationship_Register.md"
replacement_summary: "Canonical_Test_Library_WCAG_AA_Summary.md"
prohibited_uses:
  - "WCAG mapping"
  - "WCAG conformance reporting"
  - "automated attribution of a repository rule to WCAG"
```
