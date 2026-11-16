# Prioritise findings, manage tickets and report monthly

## Assess impact before counting reach

Severity describes the consequence for a person. Priority also considers urgency, exposure, dependencies and delivery. A small affected group can face complete exclusion. Low estimated revenue or unknown prevalence must never downgrade a safety issue, essential-task blocker or applicable legal deadline.

Use the organisation's approved rubric where available. The following is an illustrative default for adoption, not a legal formula:

| Dimension | Proposed scale |
| --- | --- |
| S: consequence | 1 minor friction; 2 material extra effort; 3 serious disadvantage/forced assistance; 4 essential task blocked or safety/privacy harm |
| E: exposure frequency | 1 rare; 2 occasional; 3 frequent; 4 routine exposure within the affected journey |
| C: task criticality | 1 optional; 2 supporting; 3 important; 4 essential/time-critical |
| R: reach | 1 under 1%; 2 1–under 5%; 3 5–under 20%; 4 at least 20% of the declared relevant customer denominator |

For ordinary queue ordering, a proposed score is `4S + 2E + 2C + R` (9–36). Declare weights before use, record input evidence and retain dimension values. This ordinal score is not a probability, legal risk calculation or compliance score. If reach is unknown, show the score range with R=1–4 and investigate; do not assign zero. Report confidence separately from consequence.

Overrides come first: unsafe content, serious privacy/security exposure, essential-service exclusion, binding deadlines and recurring systemic regressions require urgent triage and escalation under local governance, regardless of the score. Preserve all applicable remediation duties. Use context exposure, customer benefit and root-cause reach to order comparable work after these overrides. Engineering effort affects scheduling and repair options; it does not alter severity.

## Strong recommendation: use the organisation's project system

Treat the existing project management system as the operational backlog. Avoid an unowned spreadsheet or report-only defect list. Connect to Jira, Azure DevOps, GitHub Issues or the organisation's actual tool when authorised and configured; otherwise provide import-ready draft records and state that tickets have not been created.

Before writing, confirm the project, permissions, issue types, workflow, required fields, labels, responsible teams and duplicate policy. Use a stable finding key and search for duplicates. Link repeated occurrences to a root-cause ticket and retain affected instances and obligations. Do not merge findings merely because an AXE rule matches.

Each ticket should include finding key; service/build and location; affected tasks/profiles/contexts; observed and expected behaviour; reproduction; source tests and obligations; protected evidence references; severity and priority rationale; reach assumptions; owner; due/review dates; interim accessible route; candidate remediation; dependencies; acceptance tests; and retest evidence. Keep participant identities, diagnoses and confidential data out of ticket bodies and public attachments.

Suggested lifecycle: triage → assigned → repair → ready for retest → verified → closed. Map this to actual local states. Only close as fixed after relevant technical and complete-task verification on the corrected build. A deployed patch is not a verified fix. Record duplicates, withdrawals, scope transfers and accepted exceptions separately; they are not repaired barriers. Exceptions follow the existing framework, have expiry/review, and do not change test results.

## Monthly reporting routine

At an agreed monthly cut-off, reconcile project records with the evidence system, preserve a snapshot and compare like-for-like scope. Report:

| Report section | Contents |
| --- | --- |
| Decision summary | Customer barriers removed, urgent unresolved harms, overdue action, decisions/funding needed |
| Scope/evidence | Builds, journeys, methods, coverage, exclusions, stale/missing evidence, changes since last month |
| Backlog movement | Opening, new, reopened, transfers, verified fixed, other removals and closing; by severity/owner |
| Age and delivery | Age bands, oldest critical items, median and upper-percentile time to verified fix, overdue items, blockers |
| Functional experience | Profile/task measures, satisfaction and completion gaps, sample/uncertainty, privacy-safe findings |
| Context/value | Real exposure, opportunity assumptions, evidence of reduced burden, engagement changes |
| Forward look | Capacity, next month's committed repairs, root-cause prevention, forecast and confidence |
| Accountability | Named owners, due dates, exceptions expiring, escalation and reviewer decisions |

Reconcile unique issue counts as:
`closing = opening + new + reopened + transfers_in - verified_fixed - other_removals - transfers_out`.
Define each movement once; do not count reopened issues as new as well. “Other removals” must disclose duplicate, withdrawn and reclassified counts. Also track affected occurrences/customer barriers because root-cause consolidation can reduce ticket count without improving access.

Show gross verified fixes, new/reopened inflow, net backlog change and severity mix. Report same-scope trends separately when new areas are tested. Never claim progress from lower test coverage or issue deletion.

For an illustrative stable queue with 120 open issues, 30 verified fixes/month and 15 new/reopened/month, net reduction is 15/month and a simple clearance estimate is 8 months. If repair throughput does not exceed inflow, no finite clearance date follows. Mark projections as scenarios, allow for severity, dependencies and capacity, and refresh monthly. The objective is sustained removal and prevention of barriers; no report can guarantee a zero backlog.

Use an accessible report template:

- Period, evidence cut-off, owner, scope and baseline changes.
- Verified improvements: issue IDs, affected outcomes, retest references and observed benefit.
- Backlog reconciliation and overdue/high-impact items.
- Persona/context comparisons with uncertainty and missing perspectives.
- Regulatory deliverables due, separate from this internal cadence.
- Next actions: owner, date, dependency, decision and follow-up evidence.

Monthly review must not delay urgent fixes, regulator notifications, required statements or time-critical escalation.
