# QA Accessibility Testing

This repository is a governed accessibility test-management system for websites, web applications, mobile applications, design systems, components, and digital services. It connects outcome-based accessibility requirements to detailed tests, design-system dependencies, automated rules, manual evaluation, evidence, release decisions, and continuous improvement.

The primary consumer of this README is an LLM or autonomous agent managing the framework. Human maintainers can use the same instructions to understand the repository's structure and controls.

> **Primary rule:** manage this repository as a connected evidence system, not as a collection of independent checklists.

---

## 1. Autonomous manager mission

An LLM managing this repository must preserve and improve the chain:

> user outcome → requirement → affected pattern or journey → repository test → validation method → implementation → execution evidence → issue or exception → release decision → operational learning

The manager should:

- keep the framework organisation-agnostic;
- preserve exact source identities and test titles;
- maintain traceability between the repository's different test layers;
- distinguish automated detection from manual judgement and real-user evidence;
- identify gaps, duplication, contradictions, and stale mappings;
- make low-risk maintenance changes autonomously;
- stop for human approval when a change affects meaning, scope, conformance interpretation, governance, or risk acceptance;
- report uncertainty instead of manufacturing a conclusion.

The manager must not optimise for the largest test count, the highest automated pass rate, or the appearance of completeness. It must optimise for credible evidence about whether disabled people can perceive, understand, operate, and successfully use the product or service being evaluated.

---

## 2. Repository invariants

These rules apply to every retrieval, analysis, edit, and generated artefact.

1. **Keep test namespaces separate.** The 200-item [Canonical Test Library](<Canonical Test Library.md>) and 432-item [Mobile Application and Website Test Library](Mobile_Application_and_Website_Test_Library.md) use independent numbering. `Test 94` is ambiguous unless the source library is named.
2. **Do not add inventory totals together.** The libraries overlap and have different purposes. `200 + 432` is not a meaningful coverage or completion target.
3. **Do not equate an AXE rule with a repository test.** AXE rule IDs, canonical test references, detailed test references, local test procedures, and execution IDs belong to different namespaces.
4. **Do not infer conformance from a mapping.** A WCAG, POUR, component, token, tool, or AXE mapping supports traceability; it is not proof that a criterion or user outcome has been fully evaluated.
5. **Do not infer accessibility from an automated pass.** Automated tools evaluate only conditions available to their rules in the state presented to them.
6. **Preserve uncertainty.** Use `cannot tell`, `not tested`, `blocked`, or `tool error` when the available evidence does not justify pass or fail.
7. **Preserve source text identity.** Store the source filename, test number or pattern name, exact title, and repository version whenever a test is cited or mapped.
8. **Treat component and token mappings as hypotheses.** Validate repository mappings against the product's actual design system before using them as implementation facts.
9. **Require an evidence purpose.** Every selected test must support a stated requirement, decision, risk, component, state, or journey.
10. **Keep the framework organisation-agnostic.** Product-specific profiles and evidence may be generated from the framework, but must not be written into canonical repository assets as universal rules.
11. **Do not silently renumber, delete, merge, or redefine tests.** These are governed semantic changes requiring explicit review.
12. **Never make an unrestricted accessibility claim from sampled evidence.** State scope, environments, versions, exclusions, and limitations.

---

## 3. Document map and authority by question

There is no single linear hierarchy for all questions. Use the file that is authoritative for the type of decision being made.

| File | Authority and purpose | Use it when |
|---|---|---|
| [Accessibility Test-Led Delivery Framework](Accessibility_Test_Led_Delivery_Framework.md) | Operating framework for lifecycle, governance, evidence, gates, adoption, and LLM behaviour. | Managing the end-to-end system or deciding how evidence affects delivery. |
| [Test Management Approach](Testing_Approach.md) | Testing philosophy covering layers, conformance versus usability, ownership, evidence, procurement, release, and continuous improvement. | Interpreting why different kinds of testing are required. |
| [Canonical Test Library](<Canonical Test Library.md>) | 200 numbered, outcome-based canonical tests grouped into ten domains. | Selecting stable accessibility outcomes and user behaviours. |
| [Canonical Test Library Alignment to Exact WCAG SC IDs](<Canonical Test Library Alignment to Exact WCAG SC IDs.md>) | One-by-one mapping of canonical tests to POUR and WCAG success-criterion identifiers. | Building standards traceability from a selected canonical outcome. |
| [Canonical Test Inventory: token dependencies and bi-directional component mapping](<Canonical Test Inventory: token dependencies and bi-directional component mapping.md>) | Test-to-component, test-to-token, and component-to-test mappings. | Assessing likely design-system impact or regression scope. |
| [Mobile Application and Website Test Library](Mobile_Application_and_Website_Test_Library.md) | 432 numbered detailed test entries with requirements and supported user behaviour. | Adding detailed web or mobile test coverage. |
| [Accessibility ACT-Style Test System](Accessibility_ACT-Style_Test_System.md) | Repeatable procedures for patterns, practices, and cross-cutting interpretation. | Generating or executing structured pattern-level tests. |
| [Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests](<Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests.md>) | Direct, partial, or unevidenced automated coverage for the 200 canonical tests, with manual complements. | Deciding whether automation can lead, assist, or should not be treated as primary. |
| [AXE Test AA Rule Descriptions](AXE_Test_AA_Rule_Descriptions.md) | Repository AXE rule descriptions and associated mappings. | Looking up the declared purpose of an AXE rule. |
| [AXE and Test Inventory Alignment](<AXE_and _Test_Inventory_Alignment.md>) | AXE rules aligned with canonical test areas and the manual work needed for a conclusive result. | Translating an AXE result into the wider evidence model. |
| [AXE Test Remediation Prompt Library](AXE_Test_Remediation_Prompt_Library.md) | Structured remediation prompts for AXE findings. | Investigating a finding or drafting a candidate remediation approach. |
| [AXE → Design Tokens → Components](<AXE → Design Tokens → Components.md>) | Bi-directional mapping between AXE rules, design-token dependencies, and components. | Finding likely upstream causes and downstream regression targets. |

### Authority rules

- For lifecycle and governance, follow the **Accessibility Test-Led Delivery Framework**.
- For stable user outcomes, use the **Canonical Test Library**.
- For a canonical test's exact title, number, requirement, and user behaviour, the **Canonical Test Library** is authoritative.
- For WCAG mappings, use the **Canonical Test Library Alignment** and flag suspected errors for human review rather than silently rewriting them.
- For procedural detail, use the **Mobile Application and Website Test Library** and **Accessibility ACT-Style Test System**.
- For automation suitability, use the **Automated-to-Manual Cross-Reference** and relevant AXE alignment files.
- For actual product behaviour, execution evidence overrides an assumed mapping. Record the discrepancy and propose a repository update.

---

## 4. Required bootstrap sequence

At the start of an autonomous management session:

1. Read this README completely.
2. Read `ATLF-00`, `ATLF-01`, `ATLF-03`, and `ATLF-20` in the [Accessibility Test-Led Delivery Framework](Accessibility_Test_Led_Delivery_Framework.md).
3. Read the [Test Management Approach](Testing_Approach.md) when the task involves strategy, evidence, governance, release, procurement, or usability.
4. Identify the exact repository version or commit being managed. If unavailable, state that the working tree is the version boundary.
5. Inventory filenames and detect additions, removals, and renames before editing mappings.
6. Identify the task's decision purpose: maintenance, test selection, design review, implementation support, execution planning, remediation, release, procurement, or research.
7. Retrieve only the files and sections needed for that decision, then expand retrieval if a mapping or conflict requires it.
8. Build or update an internal graph of source tests, mappings, components, tokens, automated rules, manual complements, and framework chunks.
9. Check the applicable invariants in section 2 before producing or modifying an artefact.

Do not preload every test entry when a narrow lookup will answer the question. Do not rely only on search snippets when exact wording or mappings will affect a decision.

---

## 5. Retrieval and task-routing protocol

| Task | Read first | Read next |
|---|---|---|
| Explain the framework | Framework `ATLF-01`, `ATLF-02`, and `ATLF-05` | Testing Approach |
| Create a product test profile | Framework `ATLF-06`, `ATLF-11`, and `ATLF-13` | Canonical Library; detailed and ACT-style libraries |
| Map requirements to WCAG | Canonical Library | Canonical WCAG Alignment; framework `ATLF-13` |
| Identify component or token impact | Canonical component/token mapping | Canonical Library; AXE component/token mapping if an AXE rule is involved |
| Decide automated versus manual coverage | Automated-to-Manual Cross-Reference | AXE Alignment; framework `ATLF-09` and `ATLF-12` |
| Generate a pattern test | ACT-Style Test System | Canonical Library; detailed library; Testing Approach |
| Interpret an AXE result | AXE Rule Descriptions | AXE Alignment; remediation prompts; related canonical test |
| Propose remediation | AXE Remediation Prompt Library | Related canonical test; component/token mappings; ACT-style pattern test |
| Plan a release assessment | Framework `ATLF-10`, `ATLF-14`, and `ATLF-15` | Testing Approach; selected tests and execution evidence |
| Assess repository consistency | This README sections 2, 8, 9, and 10 | Every affected source and derived mapping |

### Test lookup algorithm

When asked for tests covering a feature, component, or journey:

1. Define the required user outcome and decision purpose.
2. Select applicable canonical outcomes.
3. Use the component and token mapping to identify likely affected assets.
4. Add detailed web/mobile tests and ACT-style procedures where they provide necessary granularity.
5. Determine automation coverage as `direct`, `partial`, or `manual-primary`.
6. Add the human complement needed to answer questions of meaning, quality, sequence, effort, comprehension, or task completion.
7. Define states, environments, input methods, assistive technologies, and representative journeys.
8. Remove genuine duplication while retaining tests that differ by state, platform, method, or user outcome.
9. Return source-qualified references and state all exclusions.

---

## 6. Identifier and relationship model

### Required namespaces

Use explicit namespaces in generated data and prose:

| Namespace | Meaning | Example format |
|---|---|---|
| `ATLF` | Framework retrieval chunk | `ATLF-12` |
| `CTL` | Canonical Test Library reference | `CTL-094 — No Keyboard Trap` |
| `MAWTL` | Mobile Application and Website Test Library reference | `MAWTL-094 — Screen Reader Audio Priority Test` |
| `ACT-PATTERN` | ACT-style pattern procedure | `ACT-PATTERN-Modal-Dialog` |
| `ACT-PRACTICE` | ACT-style design-practice procedure | `ACT-PRACTICE-Focus-Indication` |
| `AXE` | AXE rule ID | `AXE-color-contrast` |
| `REQ` | Product or service requirement | Locally governed, for example `REQ-001` |
| `TEST` | Local executable procedure | Locally governed, for example `TEST-001` |
| `EXEC` | Test execution | Locally governed, for example `EXEC-2026-001` |
| `ISSUE` | Barrier or defect | Local issue-system identity |
| `EXC` | Approved exception | Locally governed exception identity |

The `CTL` and `MAWTL` prefixes are repository-management conventions supplied by this README. They do not alter the numbering or source text inside the libraries.

### Relationship vocabulary

Use one of these terms for every cross-reference:

- `implements`
- `evaluates`
- `supports`
- `partially covers`
- `manual complement to`
- `broader than`
- `narrower than`
- `equivalent after review`
- `duplicates after review`
- `not applicable because`
- `conflicts with`

Do not use an unqualified `maps to` when the relationship's strength matters.

### Minimum source reference

Every generated test reference must contain:

```yaml
source_file: "Canonical Test Library.md"
source_namespace: "CTL"
source_id: 94
source_title: "No Keyboard Trap"
source_version: "<repository commit, tag, or working-tree date>"
relationship: "evaluates"
```

---

## 7. Autonomous management loop

Use this loop for repository maintenance or a framework-management task.

### Step 1: Observe

- Identify changed files and the nature of each change.
- Determine whether the change is editorial, structural, semantic, mapping-related, procedural, or governance-related.
- Find incoming and outgoing references to the changed item.

### Step 2: Assess impact

- Identify affected test identities, mappings, framework chunks, counts, and retrieval routes.
- Check whether the change alters user outcomes, applicability, standards interpretation, automation suitability, manual complement, component scope, or release logic.
- Classify the change as low-risk autonomous maintenance or governed semantic change.

### Step 3: Act within authority

- Apply safe maintenance changes directly.
- For governed changes, prepare a concise proposal with evidence, affected records, options, and a recommendation; do not silently apply the semantic decision.
- Preserve backward traceability when retiring or replacing an item.

### Step 4: Validate

- Run the checks in section 9.
- Re-read every changed record in context.
- Confirm that exact titles, source identities, and links remain valid.
- Check that a fix has not narrowed manual coverage or inflated an automated claim.

### Step 5: Report

Return a management record containing:

- task and decision purpose;
- files changed;
- semantic changes versus editorial changes;
- mappings added, removed, or revised;
- validation performed and results;
- unresolved conflicts or uncertainty;
- approvals required;
- recommended next action.

---

## 8. Autonomous authority and approval boundaries

### Changes the manager may make autonomously

- Correct broken relative links when the intended target is unambiguous.
- Correct formatting, table structure, heading hierarchy, obvious typographical errors, and retrieval metadata without changing meaning.
- Add missing source qualification to an existing unambiguous reference.
- Update a derived count after verifying the complete source inventory.
- Add or repair reverse links when an existing relationship is explicit and unambiguous.
- Flag contradictions, gaps, duplicate candidates, orphan records, and stale mappings.
- Generate proposed crosswalks, test plans, impact reports, and maintenance reports.
- Add retrieval aids, indexes, aliases, and examples that do not redefine source content.
- Update the README's file manifest when a new repository file has an approved and clear purpose.

### Changes requiring human approval

- Add, remove, merge, split, retire, or renumber a canonical or detailed test.
- Change a requirement, supported user behaviour, expected outcome, or applicability condition.
- Change a WCAG or POUR mapping.
- Change an automation rating or claim that a test is conclusively automatable.
- Change the meaning of a component or design-token dependency.
- Change severity, release, exception, evidence, or risk-acceptance policy.
- Declare two tests equivalent or duplicate when the relationship requires judgement.
- Introduce an external source, standard, tool, or policy into the repository's authority model.
- Publish a conformance statement or claim that a product, service, component, or repository is accessible.
- Delete historical traceability or rewrite evidence from a past release.

### Required proposal format

For an approval-bound change, provide:

```yaml
proposal_id: "<stable local identifier>"
change_type: "semantic | mapping | governance | deletion | renumbering"
affected_files: []
affected_ids: []
current_state: "<what the repository says now>"
proposed_state: "<exact proposed change>"
evidence: "<repository evidence and conflict>"
user_impact: "<why the change matters>"
downstream_effects: []
alternatives: []
recommendation: "<recommended decision and reason>"
approval_required_from: "<named role or human maintainer>"
```

---

## 9. Repository validation checks

Run relevant checks after every change. A full consistency review should run all checks.

### Structural checks

- All files named in section 3 exist at the expected relative path.
- All internal Markdown links resolve.
- The framework contains one H1 and unique `ATLF-00` through `ATLF-20` chunk identifiers unless an approved version changes the sequence.
- Tables have consistent column counts and readable headers.
- Files remain valid UTF-8 and preserve meaningful punctuation in filenames and titles.

### Identity checks

- Canonical test numbers are unique within the Canonical Test Library.
- Detailed test numbers are unique within the Mobile Application and Website Test Library.
- Cross-references include source namespace, number or pattern name, and exact title.
- AXE rule IDs are not stored or reported as canonical test IDs.
- Retired identities are not reused.

### Current baseline checks

- The Canonical Test Library contains 200 numbered entries.
- The Mobile Application and Website Test Library contains 432 numbered entries.
- The two counts remain descriptive baselines, not completion targets.
- If a count changes through an approved semantic update, update this README, framework provenance, derived mappings, and validation fixtures together.

### Mapping checks

- Every row in the Canonical WCAG Alignment refers to an existing canonical test with the same number and title.
- Every canonical component/token mapping refers to an existing canonical test.
- Component-to-test reverse mappings agree with the corresponding test-to-component mappings or record an explained exception.
- Automated-to-manual rows refer to existing canonical tests and preserve exact titles.
- AXE alignments use valid AXE rule IDs from the repository rule-description file.
- Remediation prompts do not claim that a fix has passed without execution evidence.

### Evidence-model checks

- Every in-scope requirement has a validation route or an explicit test gap.
- Manual-primary outcomes have not been replaced by automated proxies.
- Tool `incomplete`, `needs review`, and `error` states are not counted as passes.
- Exceptions have owners, rationale, compensating actions, review dates, and expiry dates.
- Release claims do not exceed the tested scope.

### LLM-specific checks

- No answer relies on an unqualified test number.
- No generated output merges `CTL`, `MAWTL`, `ACT`, or `AXE` identifiers.
- Inferred relationships are labelled as inferred and not written as source facts.
- Missing evidence is reported explicitly.
- Retrieval stayed inside the repository unless a human explicitly expanded the source boundary.

---

## 10. Change-impact matrix

When a file changes, review the listed dependants.

| Changed source | Mandatory impact review |
|---|---|
| Accessibility Test-Led Delivery Framework | README routing, chunk range, governance instructions, and any generated operating templates |
| Test Management Approach | Framework lifecycle and evidence language; ACT-style interpretation; README authority rules |
| Canonical Test Library | WCAG Alignment; component/token mapping; automated-to-manual cross-reference; AXE alignment; README counts and examples |
| Canonical WCAG Alignment | Standards traceability outputs and any product profiles using affected canonical tests |
| Canonical component/token mapping | Reverse mappings, design-system impact analysis, regression profiles, and AXE component/token mapping where concepts overlap |
| Mobile Application and Website Test Library | README counts, crosswalks, detailed test profiles, and generated procedures |
| Accessibility ACT-Style Test System | Pattern routing, generated test templates, and any local executable procedures derived from it |
| Automated-to-Manual Cross-Reference | Automation plans, manual capacity plans, and coverage claims |
| AXE Test AA Rule Descriptions | AXE alignment, remediation prompts, component/token mappings, and automation profiles |
| AXE and Test Inventory Alignment | AXE interpretation, manual complements, and canonical crosswalks |
| AXE Test Remediation Prompt Library | Remediation guidance, affected component analysis, and validation warnings |
| AXE → Design Tokens → Components | Design-system dependencies, reverse mappings, and regression selection |

Do not update only the changed file when a derived artefact has become stale. Either update all affected artefacts in the same change or record the repository as temporarily inconsistent and block claims based on the stale mapping.

---

## 11. Test generation and execution contract

Every generated local test must contain:

```yaml
local_test_id: "TEST-<id>"
title: "<observable behaviour>"
decision_purpose: "<why the test is being run>"
source_references: []
user_outcome: "<what a user must be able to perceive, understand, or do>"
applicability: "<when this test applies>"
exclusions: []
preconditions: []
required_state: "<initial, expanded, invalid, loading, success, etc.>"
method: "automated | assisted | manual | assistive-technology | user-evaluation"
environment: []
steps: []
expected_result: "<observable pass condition>"
evidence_required: []
allowed_results:
  - pass
  - fail
  - cannot_tell
  - not_applicable
  - not_tested
  - blocked
  - tool_error
related_requirements: []
related_components: []
related_journeys: []
competence_required: "<role or skill>"
version: "<test version>"
```

### Execution evidence

Every execution must add:

- execution ID;
- product build or version;
- repository and local-test versions;
- exact environment and assistive-technology versions where relevant;
- actual observation, not only a status;
- raw machine output or human evidence location;
- result and confidence;
- issue, exception, and retest links;
- tester or runner identity and date.

### Automated-result interpretation

An automated rule result may establish that a detectable condition passed or failed in a particular rendered state. It cannot by itself establish that text is helpful, alternative content conveys the correct meaning, interaction is predictable, error recovery is effective, or a complete journey is usable. Add the manual complement identified by the repository when those questions affect the decision.

---

## 12. Conflict-resolution protocol

When repository files disagree:

1. Identify the exact conflicting statements and their source locations.
2. Classify the conflict as editorial, identity, mapping, procedural, semantic, or governance-related.
3. Apply the authority rules in section 3 for the question being answered.
4. Check whether one file is explicitly a derived mapping from another.
5. Prefer the primary source for identity and wording; do not let a derived table silently redefine it.
6. Preserve both claims in the issue record when the conflict cannot be resolved mechanically.
7. Assess affected tests, mappings, generated outputs, and historical evidence.
8. Correct editorial or clearly derived errors autonomously when unambiguous.
9. Submit semantic, standards, automation, and governance conflicts for human approval.
10. Mark affected outputs as provisional until the conflict is resolved.

Silence is not resolution. If a conflict could change test selection, a pass or fail result, conformance interpretation, or release decision, the manager must surface it.

---

## 13. Maintenance outputs

### Repository health report

Use this structure for periodic or change-triggered reviews:

```yaml
repository_version: "<commit, tag, or working-tree date>"
review_date: "<ISO date>"
files_checked: []
structural_status: "pass | issues_found"
identity_status: "pass | issues_found"
mapping_status: "pass | issues_found"
broken_links: []
duplicate_candidates: []
orphan_records: []
stale_derived_files: []
semantic_conflicts: []
approval_requests: []
recommended_actions: []
```

### Change record

Every repository change should state:

- what changed;
- why it changed;
- whether meaning changed;
- affected IDs and files;
- validation performed;
- backward-compatibility or migration implications;
- unresolved questions;
- approval reference where required.

### Suggested review triggers

Run an impact review when:

- a test is added, edited, retired, or renumbered;
- an accessibility target or mapping changes;
- an automated rule or tool version changes;
- a component or design-token model changes;
- a new platform, input method, or assistive technology becomes in scope;
- production evidence conflicts with a repository assumption;
- repeated defects indicate a missing or ineffective test;
- the framework's lifecycle, gate, evidence, or governance model changes.

---

## 14. Definition of repository health

The repository is healthy when:

- each file has a distinct and documented purpose;
- test identities are stable and source-qualified;
- the 200-item and 432-item libraries remain distinguishable;
- primary tests and derived mappings agree or carry explicit exceptions;
- automation claims have valid manual complements;
- component and token mappings work in both directions;
- broken links, orphans, ambiguous references, and unexplained count changes are absent;
- semantic changes have approval and traceable history;
- generated test profiles can identify scope, versions, evidence, and limitations;
- the framework can support requirements, design, engineering, testing, release, procurement, and operations without overstating what the evidence proves.

The repository is not healthy merely because every file parses or every automated check passes. Its real quality is whether it enables accurate, reproducible, and appropriately cautious decisions about accessibility.
