# QA Accessibility Testing: human-managed QA, testing and evaluation activities and prompts

**Prepared:** 8 November 2026 · **Source revision:** `2245678da0fa140fca54c059d6501879c8e95071`  
**Source:** [Double-FW/QA_Accessibility_Testing](https://github.com/Double-FW/QA_Accessibility_Testing/tree/2245678da0fa140fca54c059d6501879c8e95071)  
**Audience:** test leads, QA practitioners, researchers, accessibility specialists, engineers, service owners, procurement and HR/employee-experience partners.

## Where the repository is useful

Use this repository as a connected evidence and test-management resource. The test-led delivery framework governs lifecycle, scope, traceability and decisions; the canonical library indexes outcomes; the relationship register owns WCAG 2.2 A/AA relationships; detailed mobile/web and ACT-style entries support procedures; automation and dependency mappings support method selection and investigation.

The repository contains guidance, not a product under test, execution environment or installed runner. Preserve CTL, detailed mobile/web, ACT-style and AXE identities; identical numbers are not identical tests. WCAG relationships, automation ratings, summaries and component/token maps are not execution evidence. The former Exact WCAG alignment file is superseded. Keep repository policy, technical conformance and human outcomes distinct, preserve uncertain result states and leave release, exceptions and risk decisions to authorised people.

The activities below are an editorial application of the repository, not a claim that it already contains a complete organisational process. AI prepares scoped test plans, analytical options and evidence summaries. Testers establish actual results with appropriate competence; researchers involve affected people and preserve the limits of observation and reports. Engineering and service owners repair systems. Accountable humans retain release, procurement, exception, risk and employment decisions. Assign these responsibilities to actual people locally; the examples do not establish a new team or approval body.

## How to use the prompts

1. Attach [RAG_Reference.md](RAG_Reference.md). For selective retrieval, use the source routes below and [Source_Coverage.md](Source_Coverage.md).
2. Replace bracketed inputs with the actual project brief, artefacts and evidence. Supply the target task, audience, platform/setting, constraints and intended decision. Treat missing information as unknown.
3. Use either example prompt for the activity. Both refer to this folder’s reference. Supply only appropriate project information; use anonymised research findings where possible.
4. Require source ID, filename and original section citations; distinguish source guidance, local proposal, observed result and uncertainty. Ask for evidence requests where an artefact cannot be inspected.
5. Review the result with the named human roles and record decisions. A prompt output is a draft test/evaluation aid, not implementation or evidence that a test ran. Do not defer disabled people’s involvement until final testing.

**Reusable response contract:** “Use the attached RAG_Reference.md as the knowledge source. Cite source IDs, files and sections. Distinguish source statements, project evidence, recommendations and unknowns. Preserve applicable source identifiers. Do not invent research, capability, approvals or test results. Give a concrete test/evaluation artefact, trade-offs, evidence requests and decisions for the human team.”

## Activity map

| Activity | Evaluation activity | Expected output |
| --- | --- | --- |
| 1. Mobilise a scoped test-led delivery plan | QA strategy and project initiation | A scoped QA strategy and evidence/decision plan. |
| 2. Select applicable canonical outcomes and detailed procedures | Test design and coverage analysis | A source-qualified test-selection and coverage matrix. |
| 3. Map standards relationships without overstating conformance | WCAG traceability and reporting design | A scoped requirement-to-WCAG relationship view and claim limitations. |
| 4. Plan meaningful automation and manual follow-up | Automation design and integrated testing | An automation/manual coverage plan with uncovered outcomes. |
| 5. Write repeatable manual and pattern test procedures | Manual test preparation and execution planning | A local procedure set with source crosswalk and uncertain result options. |
| 6. Scope assistive-technology and alternative-input evaluation | AT test planning and integrated QA | An AT/input/environment matrix and complete-task evaluation brief. |
| 7. Commission complementary disabled-user evaluation | Research coordination and outcome testing | A proposed research/evaluation brief linked to QA questions. |
| 8. Record execution evidence, status and traceability | Test management and evidence assurance | A proposed evidence ledger and traceability/orphan-check plan. |
| 9. Investigate causes and prepare remediation briefs | Defect analysis and repair planning | A defect/remediation brief with alternatives and retest scope. |
| 10. Prepare release and procurement evidence for human decisions | Assurance and decision support | A scoped evidence/decision brief and procurement questions. |
| 11. Plan regression and change-impact evaluation | Operations and continuous testing | A versioned regression plan and operational review triggers. |
| 12. Report QA quality and maintain the knowledge system | Test reporting and organisational learning | A management QA report and evidence/knowledge maintenance backlog. |

## 1. Mobilise a scoped test-led delivery plan

**Evaluation activity:** QA strategy and project initiation

**Retrieve:** [S001 — Accessibility_Test_Led_Delivery_Framework.md](RAG_Reference.md#s001).

**Relevant source sections:** ATLF-02, ATLF-04–06 and ATLF-11.

### Tasks the repository can support

- Define the product decision, scope, target profiles and accountable roles.
- Identify critical journeys, states, environments and evidence needs.
- Integrate early review, delivery and operational feedback.

**Expected output:** A scoped QA strategy and evidence/decision plan.

**Human review:** The test lead and product/service owner agree scope, competence, actual authority and resourcing.

### Example prompt 1

> Use the attached RAG_Reference.md to plan accessibility QA for [product, platform and decision]. Follow the test-led delivery framework: define intended outcomes, scope, target profiles, critical journeys/states, environments, methods, responsibilities and evidence. Mark unknown access, versions and authority explicitly. Produce a test strategy, not a claim that checks have run.

### Example prompt 2

> Challenge [QA strategy] against the RAG. Identify scanning treated as a complete programme, absent recovery/error states and gates without an accountable human. Propose practical scope and evidence changes with exact ATLF references.

## 2. Select applicable canonical outcomes and detailed procedures

**Evaluation activity:** Test design and coverage analysis

**Retrieve:** [S001 — Accessibility_Test_Led_Delivery_Framework.md](RAG_Reference.md#s001); [S012 — Canonical Test Library.md](RAG_Reference.md#s012); [S015 — Mobile_Application_and_Website_Test_Library.md](RAG_Reference.md#s015); [S008 — Accessibility_ACT-Style_Test_System.md](RAG_Reference.md#s008).

**Relevant source sections:** ATLF-03 and ATLF-11; canonical outcomes and detailed libraries.

### Tasks the repository can support

- Retrieve applicable outcomes by user task rather than take every test.
- Add detailed or pattern procedures using source-qualified identities.
- Identify gaps, duplicates, exclusions and risk-based sampling.

**Expected output:** A source-qualified test-selection and coverage matrix.

**Human review:** The test designer checks exact IDs/titles and applicability; the test lead agrees coverage and sampling limits.

### Example prompt 1

> Using the RAG, select tests for [journey/components/states]. Retrieve exact canonical outcome IDs and titles, then relevant mobile/web and ACT-style procedures. Preserve library names and versions, show many-to-many coverage, method, rationale and exclusions. Do not match tests by number alone or select every entry by default.

### Example prompt 2

> Audit [selected-test matrix] using the RAG. Find namespace collisions, a component test substituted for a complete journey and uncovered critical states. Return corrected source references, deduplication rationale and additional evidence needs.

## 3. Map standards relationships without overstating conformance

**Evaluation activity:** WCAG traceability and reporting design

**Retrieve:** [S014 — Canonical_WCAG_AA_Relationship_Register.md](RAG_Reference.md#s014); [S012 — Canonical Test Library.md](RAG_Reference.md#s012); [S013 — Canonical_Test_Library_WCAG_AA_Summary.md](RAG_Reference.md#s013); [S011 — Canonical Test Library Alignment to Exact WCAG SC IDs.md](RAG_Reference.md#s011).

**Relevant source sections:** Relationship register vocabulary/reporting rules; ATLF-03 and ATLF-13.

### Tasks the repository can support

- Use the canonical register for exact A/AA relationship types.
- Keep direct requirement, partial support, related technique and organisation policy distinct.
- Separate repository findings from full criterion assessment.

**Expected output:** A scoped requirement-to-WCAG relationship view and claim limitations.

**Human review:** The standards/evidence reviewer checks full applicable criterion conditions when a conformance conclusion is required.

### Example prompt 1

> Use the RAG’s canonical WCAG relationship register to map [selected CTL tests]. Preserve exact SC IDs, A/AA level, relationship type and scope note. Distinguish direct requirement, partial support, related technique and organisation policy. State what further evidence a whole-criterion conclusion needs; do not use the superseded Exact mapping or title similarity.

### Example prompt 2

> Challenge [WCAG report or mapping] against the RAG. Identify best-practice failures presented as WCAG failures, partial evidence treated as complete conformance and a derived summary overriding the register. Return corrected relationship/claim statements.

## 4. Plan meaningful automation and manual follow-up

**Evaluation activity:** Automation design and integrated testing

**Retrieve:** [S001 — Accessibility_Test_Led_Delivery_Framework.md](RAG_Reference.md#s001); [S009 — Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests.md](RAG_Reference.md#s009); [S007 — AXE_and _Test_Inventory_Alignment.md](RAG_Reference.md#s007); [S005 — AXE_Test_AA_Rule_Descriptions.md](RAG_Reference.md#s005).

**Relevant source sections:** ATLF-08 and ATLF-12; automated/manual cross-reference and AXE alignment.

### Tasks the repository can support

- Choose what automated analyzers and product assertions can actually establish.
- Define relevant rendered states and execution environments.
- Specify remaining manual, AT and user-outcome evidence.

**Expected output:** An automation/manual coverage plan with uncovered outcomes.

**Human review:** Engineering and QA verify actual tools/configurations; coverage ratings are analytical guidance, not passed tests.

### Example prompt 1

> Using the RAG, plan automation for [states, components and journeys]. Use the automated/manual cross-reference and AXE alignment to identify direct/partial/unevidenced coverage and manual complements. Specify actual rendered-state scope, tool version to confirm, assertions and evidence. Treat D/P/N as coverage indicators, not results, and do not invent automation where judgement is essential.

### Example prompt 2

> Review [automated accessibility coverage claim] with the RAG. Identify AXE rules treated as canonical tests, unvisited states counted as covered and analyzer incompletes hidden in a pass total. Produce a truthful coverage statement and follow-up plan.

## 5. Write repeatable manual and pattern test procedures

**Evaluation activity:** Manual test preparation and execution planning

**Retrieve:** [S001 — Accessibility_Test_Led_Delivery_Framework.md](RAG_Reference.md#s001); [S008 — Accessibility_ACT-Style_Test_System.md](RAG_Reference.md#s008); [S015 — Mobile_Application_and_Website_Test_Library.md](RAG_Reference.md#s015); [S016 — Testing_Approach.md](RAG_Reference.md#s016).

**Relevant source sections:** ATLF-09 and ATLF-20; ACT-style and detailed mobile/web procedures.

### Tasks the repository can support

- Specify preconditions, steps, expected outcomes and evidence.
- Cover pattern states, transitions, errors and recovery.
- Tailor procedures to actual platform/interaction routes.

**Expected output:** A local procedure set with source crosswalk and uncertain result options.

**Human review:** Competent QA reviewers verify procedure validity; no W3C approval or execution is implied by ACT-style formatting.

### Example prompt 1

> Use the RAG to write local manual procedures for [patterns and tasks]. Include local ID, exact repository reference, outcome, applicability, preconditions/state, steps, expected result, method/environment, evidence and result vocabulary. Cover meaningful state transitions and recovery, retain ACT-style source identity and leave execution Not tested.

### Example prompt 2

> Challenge [manual procedure] against the RAG. Find subjective expected results, missing setup, platform assumptions and state checks that do not exercise the user goal. Propose repeatable steps and evidence a second tester could assess.

## 6. Scope assistive-technology and alternative-input evaluation

**Evaluation activity:** AT test planning and integrated QA

**Retrieve:** [S001 — Accessibility_Test_Led_Delivery_Framework.md](RAG_Reference.md#s001); [S016 — Testing_Approach.md](RAG_Reference.md#s016); [S015 — Mobile_Application_and_Website_Test_Library.md](RAG_Reference.md#s015).

**Relevant source sections:** ATLF-09 and ATLF-11; Testing Approach: Assistive Technology Testing.

### Tasks the repository can support

- Choose relevant versions, inputs, platforms and actual tasks.
- Inspect semantics, announcement, focus, scaling and recovery in context.
- Explain sample limits and unsupported environments.

**Expected output:** An AT/input/environment matrix and complete-task evaluation brief.

**Human review:** AT-experienced testers confirm the actual environment and observations; unfamiliarity and system defects are not conflated.

### Example prompt 1

> Using the RAG, plan AT/alternative-input evaluation for [product and audience contexts]. Define relevant screen-reader, keyboard/switch, magnification and platform routes without assuming support or versions. Specify complete tasks, focus/state changes, errors/recovery, evidence and coverage limits. Add other relevant routes based on context rather than treating one matrix as universal.

### Example prompt 2

> Review [AT test evidence] with the RAG. Identify screenshots treated as proof of announced behaviour, missing product/AT versions and one successful control treated as a completed journey. Produce scoped conclusions and remaining checks.

## 7. Commission complementary disabled-user evaluation

**Evaluation activity:** Research coordination and outcome testing

**Retrieve:** [S001 — Accessibility_Test_Led_Delivery_Framework.md](RAG_Reference.md#s001); [S016 — Testing_Approach.md](RAG_Reference.md#s016).

**Relevant source sections:** ATLF-09: Evaluation with disabled people; Testing Approach: user testing.

### Tasks the repository can support

- Connect technical evidence with real-world understanding and task experience.
- Plan meaningful participation at suitable points throughout delivery.
- Define ethical, accessible research and preserve interpretation limits.

**Expected output:** A proposed research/evaluation brief linked to QA questions.

**Human review:** A researcher and accountable owner agree participation safeguards; synthetic personas and expert checks are not user findings.

### Example prompt 1

> Use the RAG to commission evaluation for [user-outcome questions and existing QA evidence]. Separate discovery/co-design participation from later evaluation; remove known avoidable technical barriers before asking users to evaluate a working experience. Plan relevant participants, accessible tasks, support and evidence of effort, understanding, control and satisfaction. Do not invent a sample size or completed findings.

### Example prompt 2

> Challenge [research/QA conclusion] against the RAG. Find user success called technical conformance, untested populations generalised from one participant and assisted completion reported as independence. Return bounded findings and further evidence questions.

## 8. Record execution evidence, status and traceability

**Evaluation activity:** Test management and evidence assurance

**Retrieve:** [S001 — Accessibility_Test_Led_Delivery_Framework.md](RAG_Reference.md#s001); [S003 — AGENTS.md](RAG_Reference.md#s003).

**Relevant source sections:** ATLF-13–14; AGENTS: status and reporting.

### Tasks the repository can support

- Keep requirements, source tests, local procedures, runs and issues separate.
- Record exact builds, versions, methods and actual observations.
- Preserve pass/fail and all uncertain or unexecuted states.

**Expected output:** A proposed evidence ledger and traceability/orphan-check plan.

**Human review:** The test lead validates evidence quality and state classification; illustrative fields are not an implemented data service.

### Example prompt 1

> Using the RAG, structure [supplied execution evidence] into separate requirement, test-reference, local procedure, execution and issue records. Preserve versions, method, environment and actual observation. Use pass, fail, blocked, cannot_tell, not_tested, not_applicable or tool_error with reasons; no conditional_pass or fabricated execution.

### Example prompt 2

> Audit [test report] using the RAG. Find incomplete analyzer results turned into passes, missing denominators/builds, or a planned procedure reported as executed. Produce corrected states, traceability gaps and evidence needed for a conclusion.

## 9. Investigate causes and prepare remediation briefs

**Evaluation activity:** Defect analysis and repair planning

**Retrieve:** [S006 — AXE_Test_Remediation_Prompt_Library.md](RAG_Reference.md#s006); [S004 — AXE → Design Tokens → Components.md](RAG_Reference.md#s004); [S010 — Canonical Test Inventory: token dependencies and bi-directional component mapping.md](RAG_Reference.md#s010); [S012 — Canonical Test Library.md](RAG_Reference.md#s012); [S001 — Accessibility_Test_Led_Delivery_Framework.md](RAG_Reference.md#s001).

**Relevant source sections:** AXE remediation prompts; ATLF-08 and ATLF-14; dependency mappings.

### Tasks the repository can support

- Connect the failure with an actual user outcome and reproducible scope.
- Treat token/component dependencies as hypotheses needing product validation.
- Separate candidate repair from confirmed cause and verified closure.

**Expected output:** A defect/remediation brief with alternatives and retest scope.

**Human review:** Engineering/design/content owners verify root cause; competent QA tests the changed implementation and affected journeys.

### Example prompt 1

> Use the RAG and [actual finding/evidence] to draft a remediation brief. Keep AXE rule, canonical outcome and local issue IDs distinct. Explain expected/observed behaviour, task impact, probable cause as a hypothesis, alternative repairs and manual/automated retest. Validate inferred token/component dependencies against supplied implementation evidence before asserting cause.

### Example prompt 2

> Challenge [remediation proposal] against the RAG. Find a token change assumed to fix every component, semantics changed without interaction review and an automated rerun treated as complete repair. Return a product-specific investigation and verification plan.

## 10. Prepare release and procurement evidence for human decisions

**Evaluation activity:** Assurance and decision support

**Retrieve:** [S001 — Accessibility_Test_Led_Delivery_Framework.md](RAG_Reference.md#s001); [S016 — Testing_Approach.md](RAG_Reference.md#s016); [S003 — AGENTS.md](RAG_Reference.md#s003).

**Relevant source sections:** ATLF-04, ATLF-10 and ATLF-15; Testing Approach: procurement.

### Tasks the repository can support

- Summarise coverage, unresolved barriers, uncertainty and actual outcomes.
- Distinguish test results from acceptance, exceptions and baseline departures.
- Identify required evidence, delegated decision owner and claim limits.

**Expected output:** A scoped evidence/decision brief and procurement questions.

**Human review:** Authorised product, procurement or governance owners decide; QA evidence does not itself accept risk or waive obligations.

### Example prompt 1

> Using the RAG, prepare a release/procurement evidence brief for [decision and evidence]. State tested scope, methods, coverage gaps, critical barriers and human outcomes. Identify missing authority and the evidence requirements for any exception or baseline departure without recommending or approving one. Keep conformance claims bounded by available evidence.

### Example prompt 2

> Challenge [release or supplier acceptance pack] against the RAG. Find pass percentages hiding blockers, expired exceptions, missing delegation or customer support used as proof of equal access. Return an unresolved-decision and evidence list for the accountable owner.

## 11. Plan regression and change-impact evaluation

**Evaluation activity:** Operations and continuous testing

**Retrieve:** [S001 — Accessibility_Test_Led_Delivery_Framework.md](RAG_Reference.md#s001); [S016 — Testing_Approach.md](RAG_Reference.md#s016); [S010 — Canonical Test Inventory: token dependencies and bi-directional component mapping.md](RAG_Reference.md#s010); [S004 — AXE → Design Tokens → Components.md](RAG_Reference.md#s004).

**Relevant source sections:** ATLF-10–12 and ATLF-18; component/token mappings.

### Tasks the repository can support

- Map changes to outcomes, patterns, states and complete journeys.
- Use shared-component reach to choose risk-based regression scope.
- Keep monitoring signals separate from confirmed product findings.

**Expected output:** A versioned regression plan and operational review triggers.

**Human review:** Engineering/QA owners confirm actual dependencies and execution; operations maintains incident and feedback routes.

### Example prompt 1

> Use the RAG to plan regression after [code, content, token, component, supplier or platform change]. Trace actual affected outcomes and dependencies, select relevant states/journeys/environments and define automated plus human evidence. Explain monitoring signals, escalation and retest triggers without inventing a pipeline or live service.

### Example prompt 2

> Review [regression coverage report] against the RAG. Find a snapshot scan treated as dynamic-state coverage, dependency assumptions not checked and changed mappings carried forward without version control. Produce focused additional testing and claim limits.

## 12. Report QA quality and maintain the knowledge system

**Evaluation activity:** Test reporting and organisational learning

**Retrieve:** [S001 — Accessibility_Test_Led_Delivery_Framework.md](RAG_Reference.md#s001); [S002 — README.md](RAG_Reference.md#s002); [S014 — Canonical_WCAG_AA_Relationship_Register.md](RAG_Reference.md#s014); [S013 — Canonical_Test_Library_WCAG_AA_Summary.md](RAG_Reference.md#s013).

**Relevant source sections:** ATLF-16–20; README: health checks and source routing.

### Tasks the repository can support

- Report requirements, states, journeys, environments and user outcomes separately.
- Preserve canonical/derived authority, supersession and namespace identity.
- Turn actual defects and coverage gaps into proportionate learning.

**Expected output:** A management QA report and evidence/knowledge maintenance backlog.

**Human review:** Evidence and source owners review changes; generated summaries or new mappings do not become authoritative by assertion.

### Example prompt 1

> Using the RAG and [QA period evidence], produce an action-oriented report with requirement/test coverage, state/journey/environment limits, actual results, critical barriers, human outcomes and next decisions. Keep standards, repository policy and inclusive-design findings separate and cite owning sources rather than deriving a conformance score from mappings.

### Example prompt 2

> Audit [QA knowledge or reporting process] against the RAG. Identify superseded mappings used for current claims, generated summaries edited independently, namespace collisions and remediation prompts counted as closed defects. Propose an evidence-backed maintenance and learning plan.

## Evaluation evidence and decision record

For each adopted result, record the project/task, source revision and sections used, observed test/evaluation question, barrier or outcome, chosen option and rejected alternatives, expected outcome, evidence available, assumptions, unresolved constraints, accountable person, next check and review trigger. Use actual names and dates when agreed; leave them unassigned when unknown. Record acceptance and residual risk only when the accountable person has made the decision.

Revisit the reference when repository sources change, a new platform or context is introduced, implementation changes invalidate assumptions, or user feedback exposes a barrier. Compare changed sources rather than silently replacing the basis of existing decisions.
