---
title: "Accessibility Test-Led Delivery Framework"
subtitle: "An organisation-agnostic model for requirements, design, engineering, testing, release, and continuous improvement"
version: "1.1"
date: "2026-09-20"
status: "Reusable framework"
repository: "https://github.com/Double-FW/QA_Accessibility_Testing"
source_boundary: "Only documents and test assets in the Double FW QA_Accessibility_Testing repository"
audience:
  - product and service owners
  - delivery managers
  - designers and content specialists
  - architects and engineers
  - test managers and QA practitioners
  - accessibility specialists
  - researchers
  - procurement and operations teams
retrieval_unit: "Each H2 section with an ATLF chunk identifier is intended to stand alone"
retrieval_notes:
  - "Retrieve the smallest relevant ATLF chunk before expanding to linked repository files."
  - "Use repository test numbers with their library name; a number alone is ambiguous."
  - "Do not treat automated coverage as proof of accessibility or conformance."
  - "Do not merge the 200-item canonical library and the 432-item detailed library without an approved crosswalk."
  - "Treat WCAG and other target profiles as governed baselines and evidence sources, not as the complete definition of user experience."
  - "Use the canonical WCAG 2.2 A and AA relationship register; do not use the superseded Exact WCAG alignment table."
  - "Report highly recommended best-practice results separately from WCAG A/AA conformance."
---

# Accessibility Test-Led Delivery Framework

This framework defines a reusable way to make accessibility part of how digital products and services are specified, designed, built, tested, released, procured, and maintained. It is organisation-agnostic: role names, delivery methods, technologies, assurance thresholds, and regulatory targets can be adapted without changing the underlying evidence model.

The framework is grounded only in the documents and tests held in the [Double FW QA Accessibility Testing repository](https://github.com/Double-FW/QA_Accessibility_Testing). It does not rely on organisation-specific policies, personas, governance processes, test counts, or internal documents.

---

## [ATLF-00] Retrieval map and document conventions

**Chunk purpose:** Route human readers and retrieval systems to the smallest useful section.

**Keywords:** retrieval, chunking, source boundary, test identifiers, repository routing

| Need | Retrieve first | Then consult |
|---|---|---|
| Understand the operating model | ATLF-01 and ATLF-02 | ATLF-05 |
| Select repository tests | ATLF-03 and ATLF-11 | ATLF-12 |
| Define responsibilities or approve an exception | ATLF-04 | ATLF-10 and ATLF-16 |
| Plan requirements, design, or architecture | ATLF-06 and ATLF-07 | ATLF-13 |
| Implement automated checks | ATLF-08 and ATLF-12 | ATLF-13 |
| Plan manual, assistive-technology, or user testing | ATLF-09 and ATLF-11 | ATLF-14 |
| Make a release decision | ATLF-10, ATLF-14, and ATLF-15 | ATLF-17 |
| Introduce the framework | ATLF-16 | ATLF-17 and ATLF-18 |
| Find the authoritative repository asset | ATLF-19 | The linked repository file |

### Retrieval rules

- Every H2 heading beginning `ATLF-` is a self-contained retrieval chunk.
- A repository test must be cited as `library name + test number + test title`. For example, `Canonical Test Library, test 94, No Keyboard Trap` is unambiguous; `test 94` is not.
- The [Canonical Test Library](<Canonical Test Library.md>) contains 200 numbered outcome-based tests. The [Mobile Application and Website Test Library](Mobile_Application_and_Website_Test_Library.md) contains 432 numbered, more detailed test entries. Their number spaces are independent.
- `AXE rule ID` means an identifier in the repository's AXE artefacts. It is not a canonical test ID and must not be stored in the same field.
- A link in this framework points only to a file in the repository or to the repository itself.
- When a repository file and this framework differ in granularity, the repository file supplies the test detail; this framework supplies the delivery and governance context.

**Repository sources:** [Canonical Test Library](<Canonical Test Library.md>); [Mobile Application and Website Test Library](Mobile_Application_and_Website_Test_Library.md).

---

## [ATLF-01] Executive summary

**Chunk purpose:** Explain the framework's outcome, central controls, and limits.

**Keywords:** executive summary, test-led delivery, traceability, evidence, release confidence

Accessibility test-led delivery begins with user outcomes, not with a scanner. Requirements define what people must be able to perceive, understand, and do. Design and architecture translate those outcomes into reusable patterns and testable behaviour. Engineering implements them. Automated, manual, assistive-technology, and user-centred evaluation produce complementary evidence. Release and operational decisions use that evidence and retain any unresolved risk.

The core outcome is a traceable evidence chain:

> user outcome → requirement → affected pattern or journey → selected repository test → test implementation → execution result → issue, exception, or baseline departure → release decision → operational follow-up

The framework has seven controls:

1. **One governed source model.** Requirements, tests, implementations, executions, issues, exceptions, and baseline departures are different records linked by stable identifiers.
2. **Layered testing.** Component, page or feature, journey, and live-service evidence answer different questions and must not be collapsed into one score.
3. **Automation with declared limits.** Automated checks provide repeatability and scale. They do not decide whether language is helpful, a journey is understandable, focus behaviour is usable, or an alternative conveys the right meaning.
4. **Human evidence by design.** Manual technical checks, assistive-technology evaluation, and research with disabled people are planned work, not late-stage contingency.
5. **Evidence-based gates.** Work moves forward because the expected evidence exists and is credible, not because a checklist total or automated score looks favourable.
6. **Continuous correction.** Repeated failures are corrected in shared patterns, tokens, components, content rules, and test infrastructure so that later teams inherit the improvement.
7. **Governed flexibility.** WCAG, repository tests, and declared target profiles provide strong baselines, but they do not by themselves define the full quality or equality of an experience. Any departure must be evidence-led, explicitly authorised, limited in scope, and monitored against real user outcomes.

The framework is deliberately tool-agnostic. The repository contains AXE-specific rule, remediation, and design-system mappings, plus a broader automated-to-manual comparison. Those assets support selection and implementation; they do not require every organisation to use the same runner or pipeline.

The framework also avoids a misleading promise: not every accessibility outcome has a reliable automated assertion. The repository's automated-to-manual cross-reference explicitly classifies some canonical tests as having no evidenced automated coverage. The correct control is therefore that every in-scope requirement has a sufficient validation route, with automation used where it produces valid evidence.

**Repository sources:** [Test Management Approach](Testing_Approach.md); [Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests](<Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests.md>).

---

## [ATLF-02] Purpose, scope, and boundaries

**Chunk purpose:** Define what the framework covers and prevent overclaiming.

**Keywords:** scope, products, services, web, mobile, procurement, conformance, usability

### Purpose

The Accessibility Test-Led Delivery Framework enables a team to:

- express accessibility as outcome-based, testable requirements;
- connect requirements to designs, patterns, components, journeys, and repository tests;
- select an appropriate combination of automated and human evaluation;
- retain evidence that supports design, remediation, procurement, release, and risk decisions;
- detect regression and improve shared delivery infrastructure over time.

### Applicability

The framework can be applied to websites, web applications, mobile applications, design systems, internal tools, customer services, content platforms, and procured technology. It can support iterative, continuous-delivery, stage-gated, outsourced, or hybrid delivery models.

### Boundaries

- The framework does not set an organisation's legal or policy target. The target profile must be declared for each product or service.
- WCAG and other declared target profiles are governed baselines and evidence sources. They do not cover every aspect of expectation, effort, autonomy, privacy, equivalence, satisfaction, or enjoyment, and they may not fully anticipate every specialist or emerging service context.
- A departure from a baseline is not automatically a conformance exception. It may be considered only where applicable legal, contractual, regulatory, and policy obligations permit it, and it must follow the authority and evidence controls in ATLF-04.
- A successful automated run is not a conformance statement and does not establish that disabled people can complete a task.
- A technical conformance review is not the same as usability evaluation. Both may be needed for a decision.
- Test volume is not coverage. The repository contains overlapping and differently structured libraries; teams must select tests because they cover in-scope outcomes and risks.
- Personas and simulations may prompt test scenarios, but they do not substitute for assistive-technology expertise or research with disabled people.
- Supplier claims and accessibility reports are inputs to due diligence, not replacements for independent validation of critical workflows.
- Sampling must be disclosed. A result applies only to the tested versions, states, environments, content, components, and journeys.

### Default completion rule

An in-scope accessibility requirement is complete only when it has:

- a stated user outcome and applicability condition;
- one or more selected repository tests or a documented reason that a new test is needed;
- a defined validation method and expected evidence;
- a result for every required environment and representative state;
- an owned issue, approved time-bound exception, approved evidence-based departure, or pass supported by evidence;
- a clear effect on the release or operational decision.

**Repository sources:** [Test Management Approach](Testing_Approach.md); [Accessibility ACT-Style Test System](Accessibility_ACT-Style_Test_System.md).

---

## [ATLF-03] Repository test architecture

**Chunk purpose:** Explain how the repository's parallel assets should be used without merging their identities.

**Keywords:** canonical library, detailed library, ACT-style, AXE, WCAG mapping, tokens, components

The repository is a set of related layers rather than one flat checklist.

| Repository layer | Operational use | Important constraint |
|---|---|---|
| [Test Management Approach](Testing_Approach.md) | Defines testing philosophy, evidence expectations, layers, governance, and release thinking. | It guides decisions; it is not an executable test inventory. |
| [Canonical Test Library](<Canonical Test Library.md>) | Supplies 200 outcome-based requirements and supported user behaviours across ten domains. | Its numeric IDs are local to this library. |
| [Canonical WCAG 2.2 A and AA Relationship Register](Canonical_WCAG_AA_Relationship_Register.md) | Supplies the canonical normalized A/AA relationship records, classification and scope notes. | A direct relationship remains bounded by the criterion's complete conditions and exceptions; partial support and organisation policy are not equivalent to criterion conformance. |
| [Canonical Test Library — WCAG 2.2 A and AA Summary](Canonical_Test_Library_WCAG_AA_Summary.md) | Supplies the generated one-row-per-test view and identifies highly recommended best practices. | It is a generated view; the normalized relationship register is authoritative. |
| [Superseded Exact WCAG Alignment](<Canonical Test Library Alignment to Exact WCAG SC IDs.md>) | Retains historical link continuity. | Do not use it for current mapping or conformance reporting. |
| [Canonical Test Inventory: token dependencies and bi-directional component mapping](<Canonical Test Inventory: token dependencies and bi-directional component mapping.md>) | Connects canonical tests to affected patterns, components, and inferred design-token dependencies in both directions. | Token and component dependencies are implementation inferences that must be validated against the product's design system. |
| [Mobile Application and Website Test Library](Mobile_Application_and_Website_Test_Library.md) | Supplies 432 detailed test entries with requirements and supported user behaviour. | This is a separate number space and may overlap with the canonical library. |
| [Accessibility ACT-Style Test System](Accessibility_ACT-Style_Test_System.md) | Supplies repeatable pattern and design-practice procedures with objectives, setup, steps, expected outcomes, and interpretation. | Pattern tests complement rather than replace journey testing. |
| [Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests](<Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests.md>) | Indicates direct, partial, or unevidenced automated coverage for each canonical test and identifies the needed manual complement. | Its `D`, `P`, and `N` ratings are analytical coverage indicators, not execution results. |
| [AXE Test AA Rule Descriptions](AXE_Test_AA_Rule_Descriptions.md) | Provides AXE rule descriptions and associated mappings. | AXE rule IDs remain distinct from repository test IDs. |
| [AXE and Test Inventory Alignment](<AXE_and _Test_Inventory_Alignment.md>) | Links AXE rules to related canonical areas and states whether manual work is needed for a conclusive result. | A related test is not necessarily a one-to-one or complete implementation mapping. |
| [AXE Test Remediation Prompt Library](AXE_Test_Remediation_Prompt_Library.md) | Supports structured investigation and remediation after an AXE finding. | A remediation prompt is guidance, not proof that a fix is correct. |
| [AXE → Design Tokens → Components](<AXE → Design Tokens → Components.md>) | Connects AXE rules, token dependencies, and components in both directions. | The mapping must be adapted to the actual component and token model. |

### Repository authority rule

Use the canonical library as the stable outcome index. Use the detailed web/mobile and ACT-style libraries to add procedure and context. Use the cross-reference and AXE assets to select an execution method. Preserve the original source identity of every mapped item.

### Reconciliation rule

Do not deduplicate by title alone. Two tests may share a theme while evaluating different states, methods, platforms, or user outcomes. Create a reviewed crosswalk with `equivalent`, `broader than`, `narrower than`, `supports`, `duplicates`, and `unrelated` relationships.

---

## [ATLF-04] Governance, roles, and decision rights

**Chunk purpose:** Define generic accountability without imposing an organisation chart.

**Keywords:** governance, RACI, accountability, ownership, exceptions, risk acceptance

Role names can be adapted, but responsibilities and delegation limits must remain explicit. One person may hold several roles in a small team; that does not remove the decisions or allow evidence production, exception recommendation, and risk acceptance to be treated as the same decision.

| Capability or role | Core responsibility |
|---|---|
| Business or service accountable owner | Funds the work, owns service risk, and approves release risk within documented delegated authority, organisational risk appetite, and escalation thresholds. |
| Product owner or manager | Owns in-scope outcomes, prioritisation, acceptance criteria, customer impact, remediation priorities, and exception or departure recommendations. This role does not accept release risk or approve a departure unless the same person has been explicitly delegated the accountable-owner authority. |
| Executive or enterprise-risk authority | Sets or applies organisational risk appetite and decides exceptions or departures above delegated thresholds, including systemic, high-impact, legally sensitive, and long-duration matters. |
| Delivery manager | Plans gates, dependencies, capacity, reporting, and handover. |
| Design and content | Define perceptible, operable, understandable, and robust behaviour in designs, content, and reusable patterns. |
| Architecture | Owns structural choices, platform constraints, shared contracts, integration risks, and testability. |
| Engineering | Implements accessible behaviour, developer checks, automated assertions, and remediation at source. |
| Test management and QA | Own the integrated strategy, coverage model, environments, execution, evidence quality, governed result classification, and completion recommendation. They do not accept business risk merely because they produced or reviewed the evidence. |
| Accessibility specialist | Supports interpretation, complex assessment, assurance, capability building, and repository quality. Specialist advice informs but does not transfer accountability for business risk. |
| Research | Plans and conducts ethical evaluation with disabled participants where real-world usability evidence is required, and reports the limits and uncertainty of that evidence. |
| Procurement and supplier management | Sets evidence requirements, evaluates supplier claims, records commitments, and manages contractual remediation. |
| Operations or service management | Owns production monitoring, accepted defects, exception expiry, incident response, and regression after change. |
| Disabled participants and customer representatives | Provide evidence about task effectiveness, effort, error recovery, comprehension, autonomy, equivalence, satisfaction, and experience; they do not carry compliance or risk-acceptance accountability. |

### Required decision rights

The governance model must distinguish the following decisions. A named person may hold more than one role, but the decision record must show which authority they exercised.

| Decision | Default authority | Required control |
|---|---|---|
| Classify a test result and its evidential confidence | Test management, QA, or another competent reviewer | Use the governed result vocabulary and record uncertainty; delivery pressure cannot convert a fail or an inconclusive result into a pass. |
| Assess user and service impact | Product, research, accessibility, and relevant service specialists | Consider the affected population, task, context, frequency, severity, workarounds, compounding barriers, and limits of the evidence. |
| Prioritise remediation | Product or service owner | Record rationale, owner, target date, dependencies, and consequences of delay. |
| Recommend an exception or evidence-based departure | Product or service owner | For an exception, provide the evidence set, alternatives, residual disadvantage, compensating action, proposed duration, and monitoring. For a departure, provide equal-or-better-outcome evidence, uncertainty, claim limits, monitoring, and review triggers. |
| Accept an exception or approve a departure within the documented threshold | Business or service accountable owner | Act only within delegated authority. Record the decision conditions and review date, plus an expiry for every exception or time-limited approval. |
| Accept an exception or approve a departure above the documented threshold | Executive or enterprise-risk authority | Apply organisational risk appetite and any required legal, compliance, procurement, or independent challenge. |
| Set organisational risk appetite and oversight | Board, executive committee, or equivalent governing authority | Define delegation and escalation boundaries and review aggregate or systemic exposure. |

An organisation must also name who can approve the canonical requirement and test profile; change mappings, procedures, rule profiles, and thresholds; set gate evidence; stop or delay release; accept supplier evidence or require independent testing; close an issue after remediation and retest; and own unresolved work after release.

### Delegated authority and escalation

Delegation must be documented before a release decision. It must state the risk levels, service contexts, maximum duration, financial or customer thresholds, and types of obligation that the accountable owner may accept. The following normally require escalation rather than routine product-level acceptance:

- material loss of independent access, privacy, dignity, or equivalent outcome;
- exclusion from a critical, safety-related, high-value, or high-consequence task;
- a high-impact or critical barrier, including a low-frequency barrier with severe consequences;
- systemic failure in a shared component, platform, supplier, or design pattern;
- repeated or renewed exceptions that indicate remediation is not progressing;
- departure from an applicable legal, regulatory, contractual, or organisational target;
- an exception that would exceed the maximum delegated duration; or
- evidence whose uncertainty is too great for the proposed claim or decision.

### Evidence-based departure from a baseline

WCAG, declared target profiles, repository tests, and organisational requirements are default baselines and evidence sources. They do not alone define the total quality, equality, or acceptability of a user experience. A departure may be approved only where applicable legal, regulatory, contractual, and policy obligations permit it and proportionate evidence supports the conclusion that the alternative provides equal or better outcomes for the relevant disabled users in the real service context.

An exception and an evidence-based departure are not interchangeable. An exception accepts a known unresolved failure, limitation, or residual disadvantage and must be time-bound. An evidence-based departure records that a different approach has been chosen because the evidence supports an equal or better outcome in context; it remains subject to periodic review and change-triggered reassessment. Neither changes the result of a standards test or permits an unsupported claim of conformance.

Assessment must consider task success, time and effort, errors and recovery, autonomy, privacy, dignity, equivalence, predictability, satisfaction, and, where relevant to the service, enjoyment. Evidence may combine standards analysis, expert assessment, task-based evaluation with disabled people, quantitative research or analytics, qualitative findings, complaints, support data, and operational evidence.

Statistical significance can strengthen a general claim when the sample and study design support population-level inference, but it is neither always necessary nor sufficient. The absence of an observed barrier in a sample is not proof that no barrier exists. Decisions must consider under-represented users, rare but severe exclusion, contradictory evidence, and the limits of the research.

The decision record must identify the baseline being departed from; the service context and rationale; affected user groups and tasks; evidence and uncertainty; alternatives considered; any residual disadvantage; compensating action; monitoring signals; the authorised approver and delegation basis; and the review date. Exceptions and time-limited approvals must also have an expiry. A material service change, complaint pattern, research finding, standards change, or other significant new evidence must trigger reassessment. A departure must not be described as conformance where the relevant conformance rules do not permit that claim.

### Independence and challenge

The person who implemented a material fix may provide evidence, but high-risk closure should be reviewed by someone able to challenge the interpretation. Product pressure must not silently change a fail into a pass, and positive research evidence must not silently change a standards failure into conformance. Where independence is limited, record that limitation as part of confidence in the evidence. Disabled participants provide evidence; they must not be asked to carry the organisation's accountability for accepting risk.

**Repository source:** [Test Management Approach](Testing_Approach.md).

---

## [ATLF-05] Lifecycle and quality-gate overview

**Chunk purpose:** Show how evidence moves through delivery.

**Keywords:** lifecycle, quality gates, artefacts, discovery, release, operations

| Stage | Primary output | Gate question |
|---|---|---|
| Mobilise and scope | Scope statement, target profile, ownership, risk tier, and repository version | Do teams know what is being decided, what is in scope, and what evidence will be required? |
| Requirements | Outcome-based requirements, applicability, acceptance conditions, and preliminary test mapping | Is accessible completion explicit and testable before solution choices are fixed? |
| Design and content | Pattern behaviour, content rules, states, alternatives, and design evidence | Do the proposed interactions and content support the required outcomes? |
| Architecture | Accessibility decision records, component contracts, state model, and environment matrix | Can the solution meet the outcomes and expose them to reliable evaluation? |
| Engineering | Implemented behaviour, component tests, automated checks, and developer evidence | Has the product been built against the agreed contracts and checked before QA handover? |
| Integrated verification | Automated, manual, assistive-technology, and user evidence linked to requirements | Is coverage sufficient across components, states, journeys, and environments? |
| Release | Accessibility test report, unresolved issues, exception or departure decisions, accountable approval, and any escalation | Does the weight of evidence justify release, is the decision within delegated authority, and are all claims accurately constrained? |
| Operations | Monitoring, regression, feedback, exception review, and improvement backlog | Is accessibility maintained as the service and its dependencies change? |

The stages are not a rigid waterfall. A continuous-delivery team may run them repeatedly at different scopes. A procured-system team may perform many of them during evaluation, acceptance, renewal, and replacement. The control is that required evidence must exist before the relevant decision, regardless of the delivery method.

### Evidence flow

Evidence should move in two directions:

- **Forward:** requirements guide design, architecture, implementation, test selection, and release decisions.
- **Backward:** failures and user evidence update components, design tokens, patterns, content rules, requirements, and future test selection.

This feedback loop is the main advantage of test-led delivery. Testing does not merely detect defects; it changes the system that produces them.

**Repository sources:** [Test Management Approach](Testing_Approach.md); [Canonical Test Inventory: token dependencies and bi-directional component mapping](<Canonical Test Inventory: token dependencies and bi-directional component mapping.md>).

---

## [ATLF-06] Mobilisation, scope, and requirements

**Chunk purpose:** Define the work required before detailed solution and test implementation.

**Keywords:** mobilisation, scope, target profile, requirements, applicability, definition of ready

### Mobilisation activities

- Define the product, service, platform, content, languages, integrations, supplier boundaries, and critical journeys in scope.
- State the decision purpose: conformance, regression control, usability, equivalent experience, procurement assurance, release readiness, remediation validation, or a combination.
- Define the applicable accessibility target profile and any additional organisational requirements.
- Select and record the repository commit, tag, release, or dated snapshot used for planning and execution.
- Assign governance roles and decision rights from ATLF-04.
- Agree identifiers, evidence storage, result vocabulary, severity model, exception process, review frequency, and reporting cadence.
- Assess delivery risk using user impact, journey criticality, scale, change frequency, complexity, and difficulty of recovery.

### Requirement activities

- Write each requirement as a user outcome rather than a tool rule or implementation instruction.
- Record a stable requirement ID, title, statement, rationale, applicability, priority, owner, acceptance conditions, and version.
- Start selection from the [Canonical Test Library](<Canonical Test Library.md>), then add procedural detail from the [Mobile Application and Website Test Library](Mobile_Application_and_Website_Test_Library.md) or [Accessibility ACT-Style Test System](Accessibility_ACT-Style_Test_System.md).
- Map the requirement to affected components, patterns, content types, states, and journeys using the repository's component and token mapping as an initial hypothesis.
- Map the requirement to every relevant validation method. Do not force an automated method where the repository cross-reference indicates that reliable automated coverage is absent.
- Put product-specific acceptance conditions into delivery work while preserving the link to the reusable requirement.

### Requirement quality check

A requirement is ready when:

- its intended user outcome is clear without reading a standard or tool rule;
- its applicability can be decided consistently;
- pass conditions are observable;
- affected states and journeys are named;
- the selected test combination can answer the decision question;
- missing repository coverage is recorded as a test-authoring task rather than hidden in prose.

### Required outputs

- scope and exclusions register;
- declared target profile;
- risk classification and evidence depth;
- versioned requirement set;
- initial requirement-to-test crosswalk;
- test gaps and assumptions register;
- Definition of Ready and Definition of Done criteria.

**Repository sources:** [Canonical Test Library](<Canonical Test Library.md>); [Canonical WCAG 2.2 A and AA Relationship Register](Canonical_WCAG_AA_Relationship_Register.md); [Canonical Test Library — WCAG 2.2 A and AA Summary](Canonical_Test_Library_WCAG_AA_Summary.md); [Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests](<Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests.md>).

---

## [ATLF-07] Design, content, and architecture

**Chunk purpose:** Turn requirements into accessible, reusable, and testable solution contracts.

**Keywords:** design review, content, architecture, component contract, design tokens, interaction states

### Design and content activities

- Define the semantic intent and expected behaviour of every new or changed pattern.
- Specify visible and non-visual names, instructions, states, relationships, errors, status messages, alternatives, and help.
- Define keyboard, pointer, touch, voice, and assistive-technology behaviour where each method is relevant.
- Include initial, focused, hovered, selected, expanded, collapsed, disabled, invalid, error, loading, empty, success, and reduced-motion states where applicable.
- Review content for purpose, clarity, consistency, error recovery, and the quality of text alternatives; presence alone is insufficient.
- Validate designs under resizing, reflow, increased text spacing, forced-colour or high-contrast modes, reduced motion, and narrow viewports as applicable.
- Select relevant pattern and practice procedures from the [Accessibility ACT-Style Test System](Accessibility_ACT-Style_Test_System.md).

### Architecture activities

- Define component contracts for role, name, description, state, value, relationships, keyboard behaviour, focus entry and return, errors, status changes, and fallback behaviour.
- Identify requirements that should be satisfied centrally through tokens, components, templates, navigation shells, content models, or platform services.
- Use the [canonical component and token mapping](<Canonical Test Inventory: token dependencies and bi-directional component mapping.md>) to identify likely dependencies, then validate them against the actual system.
- Use the [AXE-to-token-and-component mapping](<AXE → Design Tokens → Components.md>) when planning prevention and remediation for AXE-detectable conditions.
- Define representative states that automation must create before analysis. A scan of initial page load alone is not representative coverage.
- Define the browser, operating system, viewport, device, input method, and assistive-technology combinations required by product risk.
- Record third-party constraints, evidence, compensating measures, replacement options, and owners.

### Architecture gate

Architecture is ready when the team can explain how each high-priority outcome will be implemented, exposed through platform accessibility information, exercised in representative states, and evidenced. Unknowns must be tracked; they must not be converted into implicit assumptions.

### Required outputs

- accessibility annotations and content rules;
- approved pattern behaviour and variants;
- component accessibility contracts;
- state and journey model;
- accessibility architecture decision records;
- environment and assistive-technology matrix;
- updated requirement-to-test mapping.

**Repository sources:** [Accessibility ACT-Style Test System](Accessibility_ACT-Style_Test_System.md); [Canonical Test Inventory: token dependencies and bi-directional component mapping](<Canonical Test Inventory: token dependencies and bi-directional component mapping.md>); [AXE → Design Tokens → Components](<AXE → Design Tokens → Components.md>).

---

## [ATLF-08] Engineering and automated implementation

**Chunk purpose:** Define how engineers implement accessible behaviour and trustworthy automated evidence.

**Keywords:** engineering, CI, automation, AXE, component testing, state coverage, regression

### Engineering activities

- Prefer native platform semantics and behaviour; add custom semantics only when the native platform cannot express the required interaction.
- Implement the approved component contract, including names, relationships, state, focus behaviour, alternatives, errors, and status updates.
- Add component and journey checks while the feature is built, using requirement and repository-test identifiers in test metadata.
- Automate deterministic conditions such as required semantics, accessible-name presence, attribute validity, relationship integrity, and other reliably observable states.
- Create the required interaction state before running an analyser. Open dialogs, expand disclosures, trigger validation, load dynamic content, and enter authenticated states where these are part of scope.
- Add behavioural assertions outside an analyser when a reliable outcome can be tested directly, such as focus destination, focus return, route title change, state exposure, or content persistence.
- Complete developer keyboard and basic assistive-technology smoke checks before integrated QA.
- Correct recurring causes in shared components, tokens, utilities, templates, or content models rather than patching each instance.

### Using the repository's AXE assets

- Use [AXE Test AA Rule Descriptions](AXE_Test_AA_Rule_Descriptions.md) to identify the rule's stated purpose and mapping.
- Use [AXE and Test Inventory Alignment](<AXE_and _Test_Inventory_Alignment.md>) to determine the related canonical area and the human work needed for a conclusive result.
- Use [AXE Test Remediation Prompt Library](AXE_Test_Remediation_Prompt_Library.md) to structure investigation and candidate remediation.
- Use [AXE → Design Tokens → Components](<AXE → Design Tokens → Components.md>) to identify upstream design-system dependencies and downstream regression targets.

### Automation controls

- Pin analyser, rule set, runner, browser, and repository versions for release evidence.
- Define the active rule profile explicitly; do not depend on changing defaults.
- Keep `violation`, `needs review or incomplete`, `tool error`, `not run`, and `pass` as different statuses.
- Treat exclusions, suppressions, baselines, and ignored targets as governed exceptions with rationale, owner, review date, and expiry.
- Store raw machine output alongside a normalized result that links the rule ID, canonical test, state, component, journey, build, and issue.
- Review rule and dependency changes before upgrading. A new result may reflect a changed analyser rather than a changed product.

### Engineering exit outcome

The feature is ready for integrated verification when its required states are reachable, automated checks are stable, developer evidence is linked, known limitations are explicit, and human test work is not being deferred without an owner.

---

## [ATLF-09] Integrated manual, assistive-technology, and user evaluation

**Chunk purpose:** Define the human evidence that automation cannot supply.

**Keywords:** manual testing, assistive technology, disabled users, usability, test environment

### Manual technical evaluation

Manual testing should evaluate meaning and behaviour across representative components, pages, states, and journeys. Coverage should include, where applicable:

- keyboard-only completion, visible focus, focus order, traps, bypass mechanisms, and focus return;
- accessible names, visible labels, instructions, errors, status messages, and link purpose;
- content order, headings, landmarks, tables, and relationships;
- zoom, text resize, reflow, text spacing, orientation, and narrow viewports;
- colour independence, contrast across states, forced-colour or high-contrast modes, and theme changes;
- touch targets, gestures, drag alternatives, pointer precision, and multiple input methods;
- motion, flashing, autoplay, time limits, interruptions, and reduced-motion behaviour;
- captions, audio description or equivalent alternatives, transcripts, and media controls;
- authentication, failure states, embedded content, and third-party integrations.

### Assistive-technology evaluation

Assistive-technology evaluation must use declared combinations of platform, browser or host application, and technology version. It should record commands, announcements, focus behaviour, task outcome, unexpected behaviour, and workarounds. Critical journeys deserve deeper evaluation than incidental pages. One screen reader or one platform does not represent all assistive-technology use.

### Evaluation with disabled people

Research with disabled participants answers whether people can complete realistic tasks and what the experience requires of them. Depending on the decision, measures may include success, time, effort, errors, recovery, confidence, comprehension, autonomy, privacy, equivalence, predictability, satisfaction, and service-relevant enjoyment. It does not replace technical testing, and participants should not be asked to act as conformance auditors or risk approvers. Research plans must define the decision question, recruitment rationale, access needs, consent, tasks, success measures, analysis, uncertainty, and how findings will influence delivery.

### Selection method

Use the `D`, `P`, and `N` classifications in the [automated-to-manual cross-reference](<Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests.md>) as planning evidence:

- `D`: automation may directly evaluate part of the condition; confirm whether qualitative or cross-state judgement remains.
- `P`: automation supports discovery or structure checking; human evaluation is needed for a conclusion.
- `N`: manual or user-centred evaluation is primary unless the team develops and validates a reliable product-specific assertion.

### Human evidence record

Record the test identity, purpose, preconditions, steps, expected result, actual result, environment, tester competence, date, evidence, issue, confidence, and retest outcome. A note such as “checked with a screen reader” is not reproducible evidence.

**Repository sources:** [Test Management Approach](Testing_Approach.md); [Accessibility ACT-Style Test System](Accessibility_ACT-Style_Test_System.md); [Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests](<Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests.md>).

---

## [ATLF-10] Release, procurement, and operations

**Chunk purpose:** Connect testing evidence to release, supplier, and live-service decisions.

**Keywords:** release, procurement, supplier, operations, residual risk, monitoring

### Release activities

- Produce an accessibility test report that states the decision purpose, scope, exclusions, repository version, product build, environments, components, journeys, states, test methods, results, limitations, and dates.
- Confirm that every in-scope requirement has sufficient evidence, an owned defect, an approved time-bound exception, or an approved evidence-based departure.
- Review user impact, affected tasks, reach, frequency, workaround, detectability, persistence, compounding barriers, autonomy, privacy, equivalence, expectation, satisfaction, and any service-relevant experiential outcome; do not prioritise only from a tool's severity label.
- Confirm that the proposed approver has documented authority for the risk level and that every escalation trigger in ATLF-04 has been considered.
- Restrict claims to what the evidence supports. Sampled evidence cannot justify an unrestricted claim about every page, state, platform, or user.
- Archive evidence so the decision can be reconstructed.

### Procurement activities

- Define accessibility outcomes and evidence requirements before supplier selection.
- Request current test evidence, known issues, supported technologies, remediation plans, change controls, and named ownership.
- Validate critical workflows independently using the same traceability and result model as internally built services.
- Record gaps between supplier claims and observed behaviour.
- Carry remediation commitments, review dates, and exit or replacement options into contract and service management.

### Operations activities

- Transfer unresolved defects, exceptions, and baseline departures with impact, priority or decision status, owner, target or review date, monitoring, and evidence.
- Re-run proportionate regression after changes to shared components, tokens, content templates, dependencies, platforms, or rule versions.
- Monitor feedback, complaints, support contacts, defects, and production changes for signals that planned coverage missed a barrier.
- Review exceptions before expiry; an expired exception becomes an unresolved decision, not an automatic renewal.
- Reassess evidence-based departures at their review date and whenever a defined trigger occurs; prior approval is not proof that the alternative continues to produce an equal or better outcome.
- Update patterns, components, tests, training, and requirements when evidence identifies a repeated cause.

### Release decision rule

Release readiness is based on the weight and quality of evidence, not a single audit score or standards result. A release may require delay even when automated checks or a technical conformance review pass. It may sometimes proceed with a documented limitation or an evidence-based departure from a baseline when the conditions in ATLF-04 are met.

The product or service owner recommends the treatment of unresolved issues. The business or service accountable owner accepts release risk only within documented delegated authority. An executive or enterprise-risk authority decides matters above that threshold. The decision must be explicit, reviewable, time-bound where it creates an exception, and accurately separated from any claim of conformance.

**Repository source:** [Test Management Approach](Testing_Approach.md).

---

## [ATLF-11] Test selection and coverage model

**Chunk purpose:** Provide a repeatable method for choosing tests and exposing gaps.

**Keywords:** test selection, risk, coverage, sampling, canonical test, detailed test

### Selection sequence

1. **State the decision.** Define whether the evidence will support design approval, development completion, regression, release, procurement, remediation closure, or research.
2. **Identify outcomes.** Select applicable outcomes from the [Canonical Test Library](<Canonical Test Library.md>).
3. **Identify affected assets.** Use the [component and token mapping](<Canonical Test Inventory: token dependencies and bi-directional component mapping.md>) to find components, patterns, and design-system dependencies.
4. **Add procedure.** Select detailed entries from the [Mobile Application and Website Test Library](Mobile_Application_and_Website_Test_Library.md) and relevant pattern procedures from the [Accessibility ACT-Style Test System](Accessibility_ACT-Style_Test_System.md).
5. **Choose methods.** Use the [automated-to-manual cross-reference](<Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests.md>) and AXE alignment artefacts to decide what automation can contribute and which human checks remain necessary.
6. **Define the test matrix.** Name the components, content types, states, journeys, platforms, inputs, assistive technologies, and user groups required by risk.
7. **Check for gaps and duplication.** Record uncovered outcomes and redundant executions before work starts.

### Risk-based depth

Increase evidence depth when a barrier would block a critical task; expose sensitive or legal decisions; affect employment, finance, health, safety, identity, or communication; reach many people; recur through a shared component; or be difficult to work around. High-risk journeys normally require automated regression, manual technical evaluation, assistive-technology evaluation, and appropriate disabled-user evidence.

### Coverage dimensions

Coverage reporting must distinguish:

- requirements covered;
- repository tests selected and executed;
- components and templates sampled;
- interaction and error states exercised;
- end-to-end journeys completed;
- platforms, viewports, and input methods used;
- assistive technologies used;
- user evaluation completed;
- exclusions, blocked tests, and unknowns.

A percentage without its denominator and coverage dimensions is not useful. “95% passed” may hide untested critical journeys, unsupported environments, or numerous tests marked not applicable.

### Sampling rule

Sample every unique shared pattern and high-risk state, every critical journey, and representative content and platform variants. Expand the sample when defects suggest a systemic cause. State what was excluded so readers do not mistake a sample for exhaustive coverage.

---

## [ATLF-12] Automated testing model

**Chunk purpose:** Separate automation eligibility, implementation, and human interpretation.

**Keywords:** automated testing, AXE, direct coverage, partial coverage, false assurance

### Automation categories

| Category | Meaning | Required action |
|---|---|---|
| Direct rule coverage | A tool can reliably evaluate a defined condition in the rendered state. | Automate, retain raw output, and decide whether qualitative manual review is also required. |
| Partial or assisted coverage | A tool can locate candidates or verify structure but cannot judge meaning, quality, or complete behaviour. | Combine machine output with a recorded human decision. |
| Product-specific behavioural assertion | The product runner can deterministically verify behaviour not supplied by a general analyser. | Define preconditions, expected behaviour, failure diagnostics, and maintenance ownership. |
| Manual-primary | Repository evidence does not support a reliable automated conclusion. | Plan a manual, assistive-technology, or user-centred method; do not manufacture a proxy metric. |

### AXE implementation pattern

For AXE-supported checks, the automation process is:

1. Load a known product build and environment.
2. Create the representative component or journey state.
3. Run the declared AXE rule profile.
4. Preserve violations, incomplete or review results, errors, exclusions, targets, and versions.
5. Map the AXE rule ID to the related repository test and requirement.
6. Perform the manual complement identified by the repository alignment where a conclusive decision needs human judgement.
7. Link any issue and retest to the same evidence chain.

### Guardrails

- Do not equate an AXE rule with a complete canonical test.
- Do not count the same underlying condition multiple times merely because several tools report it.
- Do not treat `no violations found` as evidence that a page, journey, or product is accessible.
- Do not suppress a result without an approved, reviewable record.
- Do not apply remediation text mechanically; confirm that the proposed fix matches the component's purpose and does not create a new barrier.
- Do not let unstable automation silently reduce scope. Record runner failures separately from accessibility results.

### Repository use

The [AXE Test AA Rule Descriptions](AXE_Test_AA_Rule_Descriptions.md) explains the repository rule set. The [AXE and Test Inventory Alignment](<AXE_and _Test_Inventory_Alignment.md>) identifies related canonical areas and manual complements. The [AXE Test Remediation Prompt Library](AXE_Test_Remediation_Prompt_Library.md) supports remediation reasoning. The [AXE-to-token-and-component mapping](<AXE → Design Tokens → Components.md>) supports prevention and regression selection.

---

## [ATLF-13] Traceability and data model

**Chunk purpose:** Define the minimum records and relationships needed for auditable delivery.

**Keywords:** traceability, schema, identifiers, mappings, implementation, execution

Do not place requirements, tests, tool rules, execution results, and defects in one overloaded row. They change at different rates and have many-to-many relationships.

| Record type | Minimum fields |
|---|---|
| Requirement | requirement ID; title; outcome; rationale; applicability; priority; owner; target-profile references; acceptance conditions; status; version |
| Repository test reference | source library; source test number or pattern name; exact title; source version; relationship to requirement |
| Local test procedure | local test ID; purpose; preconditions; steps; expected result; evidence; method; competence; environment; applicability; version |
| Requirement–test mapping | requirement ID; local or repository test identity; relationship; coverage role; rationale; affected asset; state or journey |
| Automated implementation | implementation ID; test reference; analyser or assertion; rule ID where relevant; code location; target state; pipeline stage; owner; version |
| Execution | execution ID; build; source and implementation versions; environment; date; tester or runner; actual result; confidence; evidence location |
| Issue | issue ID; failed outcome; user impact; affected scope; cause; owner; priority; remediation; status; retest links |
| Exception | exception ID; requirement, issue, and baseline links; service context and rationale; affected users and tasks; evidence and uncertainty; alternatives considered; residual disadvantage; compensating action; monitoring signals; recommender; authorised approver and delegation basis; approval date; review triggers; review date; expiry; review status |
| Baseline departure | departure ID; requirement and baseline links; service context and rationale; affected users and tasks; equal-or-better-outcome evidence and uncertainty; alternatives considered; standards result and permitted claims; monitoring signals; recommender; authorised approver and delegation basis; approval date; review triggers; review date; status |
| Release decision | release ID; evidence set; open issues; exceptions; departures; limitations; decision; recommendation owner; authorised approver and delegation basis; escalation record where applicable; date; operational handover |

### Identifier rules

- Namespace every repository reference. Example: `CTL-094` may be used locally for the Canonical Test Library's test 94 only if the crosswalk records that convention.
- Preserve the exact repository title even when a local title is shortened.
- Store AXE rule IDs in an AXE-rule field, not in the canonical-test field.
- Version mappings as well as source tests. A changed mapping can alter coverage without changing the test text.
- Never reuse an identifier for a different meaning after retirement.

### Mapping relationships

Use explicit relationships: `implements`, `evaluates`, `supports`, `partially covers`, `manual complement to`, `broader than`, `narrower than`, `duplicates`, and `not applicable because`. This prevents an LLM or reporting layer from treating every link as equivalent.

### Orphan checks

Automated governance checks should identify requirements without validation, tests without purpose, automated implementations without source tests, executions without version data, issues without owners, exceptions without an authorised approver, delegation basis, monitoring, review date, or expiry, departures without equal-or-better-outcome evidence, claim limits, monitoring, or review, and release decisions without a complete evidence set.

**Repository sources:** [Canonical Test Library](<Canonical Test Library.md>); [Canonical WCAG 2.2 A and AA Relationship Register](Canonical_WCAG_AA_Relationship_Register.md); [Canonical Test Library — WCAG 2.2 A and AA Summary](Canonical_Test_Library_WCAG_AA_Summary.md); [Canonical Test Inventory: token dependencies and bi-directional component mapping](<Canonical Test Inventory: token dependencies and bi-directional component mapping.md>).

---

## [ATLF-14] Results, evidence, severity, and confidence

**Chunk purpose:** Standardise result interpretation and evidence quality.

**Keywords:** pass, fail, cannot tell, not applicable, severity, confidence, evidence

### Result vocabulary

| Result | Meaning |
|---|---|
| Pass | The expected result was met in the declared scope and environment, with sufficient evidence. |
| Fail | The expected result was not met. An issue and affected scope must be recorded. |
| Cannot tell | Available evidence is insufficient or conflicting; further evaluation is required. |
| Not applicable | The applicability condition is not present. The reason must be recorded. |
| Not tested | The item is in scope but has not been evaluated. |
| Blocked | Execution could not be completed because of an identified dependency or environment problem. |
| Tool error | The automated mechanism failed; this is not a product pass or fail. |

Use `incomplete` or `needs review` as tool-output detail, then resolve it to the governed result vocabulary through human review. Never convert uncertainty into a pass by default.

### Evidence minimum

Evidence must allow another competent person to understand:

- what was evaluated and why;
- the repository test, local procedure, and versions used;
- the exact component, content, state, page, or journey;
- the platform, environment, input, and assistive technology;
- the steps performed and actual observation;
- the raw automated output or human notes;
- the result, confidence, issue, exception, and retest history.

Screenshots can support evidence but rarely prove dynamic, keyboard, or announced behaviour on their own. Video can show sequence but should be accompanied by text that makes the evidence searchable and accessible.

### Severity and priority

Separate severity from remediation priority. Severity describes user impact. Priority also considers reach, frequency, criticality, legal or policy exposure, recurrence, workaround quality, effort, and release timing. A frequently repeated moderate barrier in a shared component may deserve faster action than an isolated severe defect in an unavailable edge case.

### Confidence

Confidence should reflect coverage breadth, environment fidelity, repeatability, reviewer competence, independence, unresolved `cannot tell` results, and consistency across evidence sources. Confidence is not another pass score; it is a statement about how strongly the evidence supports the decision.

**Repository sources:** [Test Management Approach](Testing_Approach.md); [Accessibility ACT-Style Test System](Accessibility_ACT-Style_Test_System.md).

---

## [ATLF-15] Quality gates and completion criteria

**Chunk purpose:** Define the evidence required to move work forward.

**Keywords:** gate, entry criteria, exit criteria, definition of done, release readiness

| Gate | Required automated or structural evidence | Required human evidence | Exit condition |
|---|---|---|---|
| Requirement ready | Mapping completeness and orphan checks where available | Product, design, QA, and accessibility review proportionate to risk | Outcome, applicability, acceptance conditions, and validation route are approved. |
| Design ready | Design-system and token dependency checks where available | Pattern, content, state, responsive, and interaction review | Material behaviour and content are specified in testable form. |
| Architecture ready | Prototype or component checks where feasible | Architecture, focus, semantics, integration, and testability review | Component contracts, state model, environments, and risks are recorded. |
| Engineering complete | Stable component and journey assertions plus declared analyser checks | Developer keyboard and targeted assistive-technology smoke checks | Implementation evidence exists and known limitations are explicit. |
| Integrated verification complete | Agreed regression profile executed with no unreviewed tool states | Planned manual, assistive-technology, specialist, and user evaluation complete | Every in-scope outcome has sufficient evidence, an issue, an approved time-bound exception, or an approved evidence-based departure. |
| Release ready | Versioned results and evidence bundle complete | Residual-risk, user-outcome, delegation, escalation, and claim review complete | The business or service accountable owner records a release decision within delegated authority, or the executive or enterprise-risk authority records an above-threshold decision, followed by operational handover. |
| Operationally controlled | Scheduled and change-triggered checks run | Feedback, incidents, exception expiry, and baseline-departure evidence reviewed | New evidence is triaged and improvement work is owned. |

### Stop conditions

Work should not pass a gate when:

- a critical outcome has no validation route;
- a critical journey is untested in the required state or environment;
- automation failed and the missing evidence was silently treated as a pass;
- a manual-primary outcome was represented only by an automated proxy;
- a material supplier claim cannot be reconciled with observed behaviour;
- a high-impact issue lacks a decision by the authorised accountable or escalation authority;
- an exception has no evidence record, authorised approver, delegation basis, owner, compensating action, monitoring, review date, or expiry;
- an evidence-based departure has no equal-or-better-outcome evidence, authorised approver, delegation basis, claim limits, monitoring, or review date;
- a departure is being represented as conformance when the relevant conformance rules do not permit that claim;
- the evidence cannot be traced to the tested product and repository versions.

### Completion principle

Completion is not a predetermined count. It is the point at which all applicable outcomes have credible evidence and every unresolved barrier has an explicit, owned decision.

**Repository source:** [Test Management Approach](Testing_Approach.md).

---

## [ATLF-16] Deliverables and acceptance criteria

**Chunk purpose:** Define the reusable outputs needed to operate the framework.

**Keywords:** deliverables, acceptance criteria, test profile, crosswalk, report template

| Deliverable | Acceptance criteria |
|---|---|
| Scope and evidence plan | Decision purpose, product boundary, target profile, risks, exclusions, environments, methods, roles, and gates are explicit. |
| Requirement profile | Requirements are outcome-based, uniquely identified, versioned, applicable, and linked to acceptance conditions. |
| Repository crosswalk | Every selected item retains source library, number or pattern, exact title, version, and relationship; overlaps between the 200- and 432-item libraries are reviewed rather than assumed. |
| Test profile | Each local procedure has purpose, preconditions, steps, expected result, evidence, method, competence, environment, applicability, owner, and version. |
| Component and token mapping | Relevant requirements and tests map in both directions to actual components and tokens; inferred repository mappings are validated. |
| Automation profile | Rule and assertion scope, states, versions, reporting, error handling, exclusions, and exception controls are declared and demonstrated. |
| Manual and assistive-technology plan | Journeys, states, environments, technologies, competence, sampling, evidence, and escalation are defined and resourced. |
| User evaluation plan | Decision question, participant rationale, access needs, tasks, success measures, ethics, analysis, and action route are defined where required. |
| Evidence and result schema | Results preserve source, environment, version, actual observation, confidence, issue, exception, baseline-departure, decision, and retest links. |
| Accessibility test report | Scope, methods, coverage, results, limitations, issues, exceptions, release recommendation, delegation or escalation basis, approval, claims, and handover are reconstructable. |
| Governance model | Owners, delegation thresholds, escalation triggers, and decision rights exist for tests, mappings, upgrades, failures, risk acceptance, evidence-based departures, suppliers, and operations. |
| Improvement backlog | Repeated causes are routed to components, tokens, patterns, content rules, test infrastructure, or capability development. |

### Framework implementation is complete when

- a representative product or service has exercised the model from requirement selection through operational handover;
- the organisation can distinguish the two repository test number spaces and the AXE rule namespace;
- the traceability model produces no unexplained critical orphans;
- automated and human evidence can be reviewed together without losing their different meanings;
- release, exception, and baseline-departure decisions have been tested in practice;
- owners have accepted repository update, crosswalk, automation, training, and evidence-retention responsibilities.

---

## [ATLF-17] Phased adoption plan

**Chunk purpose:** Introduce the framework in a controlled sequence.

**Keywords:** implementation, pilot, rollout, maturity, adoption

| Phase | Principal work | Exit outcome |
|---|---|---|
| 1. Baseline | Define scope and decision purpose; record repository snapshot; inventory existing requirements, tests, automation, evidence, and roles. | Agreed baseline, risks, owners, and gaps. |
| 2. Reconcile | Create namespaces and a reviewed crosswalk between canonical, detailed, ACT-style, and AXE assets. | Stable source model without ambiguous test numbers. |
| 3. Profile | Select applicable outcomes, affected assets, methods, environments, journeys, and evidence depth. | Approved requirement and test profile. |
| 4. Integrate | Add component contracts, automated checks, manual procedures, evidence schema, and delivery gates. | Working test-led process in a non-production or controlled context. |
| 5. Pilot | Apply the complete model to a representative service with dynamic states, forms, responsive behaviour, and at least one integration. | Evidence of effort, coverage, defects, decision quality, and lessons. |
| 6. Improve | Correct crosswalks, procedures, components, tokens, reports, training, and ownership based on pilot evidence. | Approved operating version of the framework. |
| 7. Scale | Roll out by product risk, reuse shared tests and components, and monitor consistency. | Sustainable portfolio or service-line adoption. |
| 8. Operate | Review repository changes, analyser changes, regression, user feedback, supplier evidence, exception expiry, and baseline-departure evidence. | Continuous, versioned improvement. |

### Pilot selection

Choose a service that is representative but bounded. It should contain several interaction states, validation, responsive behaviour, shared components, a critical journey, and at least one dependency. A trivial content page will not test the operating model. A highly exceptional legacy system may make it difficult to distinguish framework problems from accumulated remediation debt.

### Adoption warning

Do not begin by automating the largest possible set of rules. First establish the outcome profile, state model, identifiers, evidence schema, and manual capacity. Automation built against an unreconciled inventory can increase activity while reducing confidence.

**Repository sources:** [Test Management Approach](Testing_Approach.md); [Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests](<Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests.md>).

---

## [ATLF-18] Measures, risks, and review questions

**Chunk purpose:** Measure whether the framework improves evidence and user outcomes rather than only increasing test activity.

**Keywords:** metrics, risks, KPIs, effectiveness, governance review

### Measures

| Measure | Useful interpretation |
|---|---|
| Traceability completeness | Proportion of in-scope requirements linked to affected assets, tests, implementations, executions, and decisions. |
| Coverage by dimension | Coverage of requirements, states, journeys, platforms, inputs, assistive technologies, and user evaluation, reported separately. |
| Early detection | Where barriers are first found: requirement, design, architecture, component, integration, release, or production. |
| Escape and recurrence | Barriers first found after release and repeated causes linked to shared patterns or components. |
| Evidence quality | Results with sufficient environment, version, observation, and traceability data. |
| Manual plan health | Planned versus completed manual and assistive-technology work, blocked tests, and capacity constraints. |
| Exception health | Number, impact, age, affected users, decision tier, delegation basis, owner, compensating action, monitoring, review, renewal, and expiry status of exceptions. |
| Baseline-departure health | Number, scope, age, affected users, decision tier, delegation basis, evidence confidence, claim limits, monitoring, review status, and outcomes after approval. |
| Remediation effectiveness | Time to resolution, retest success, recurrence, and whether the cause was corrected upstream. |
| User outcome | Task completion, time, effort, errors, recovery, autonomy, privacy, equivalence, predictability, confidence, satisfaction, and service-relevant enjoyment for disabled participants where measured. |
| Repository health | Ambiguous references, orphan tests, stale mappings, duplicated implementations, and version drift. |

### Principal risks and controls

| Risk | Control |
|---|---|
| Automated results create false assurance | Require the coverage model, human complements, and explicit limitations. |
| The 200- and 432-item libraries are treated as one list | Namespace every reference and maintain a reviewed crosswalk. |
| Quantity replaces relevance | Select from outcomes, risk, assets, states, and journeys; report dimensions, not only totals. |
| Manual evaluation becomes a late bottleneck | Estimate skill and capacity during mobilisation and distribute testing across delivery. |
| Results cannot be reproduced | Preserve versions, environments, steps, observations, and evidence. |
| Supplier evidence is accepted without challenge | Independently test critical workflows and reconcile claims with observed behaviour. |
| Exceptions become permanent or bypass delegated authority | Require an authorised approver, recorded delegation basis, compensating action, monitoring, review triggers, and expiry; escalate renewals and above-threshold risks. |
| User research is used to erase a known standards failure | Record the standards result separately, test the alternative against broader user outcomes, disclose uncertainty, and constrain conformance claims. |
| Fixes recur across products | Route root causes to shared tokens, components, patterns, and content models. |
| LLM retrieval merges identifiers or overstates mappings | Use chunk IDs, namespaces, exact titles, relationship types, and source versions. |

### Review questions

- What decision is this evidence intended to support?
- Which user outcomes and critical tasks are at risk?
- What can automation determine reliably, and what judgement remains?
- Are the tested states and environments representative?
- What is not covered, and could that omission change the decision?
- Is the result about conformance, usability, autonomy, equivalence, satisfaction, or another service outcome, and have those conclusions been kept distinct?
- Is the proposed decision within the approver's documented authority, or must it be escalated?
- Does evidence for a departure include the users most likely to be disadvantaged, including rare but severe cases and people missing from the sample?
- Are repeated failures being fixed at source?
- Does the release claim say more than the evidence supports?

**Repository source:** [Test Management Approach](Testing_Approach.md).

---

## [ATLF-19] Repository source register

**Chunk purpose:** Provide the complete and exclusive document source boundary for this framework.

**Keywords:** sources, provenance, repository, document register

This framework references only the following repository files:

1. [Testing_Approach.md](Testing_Approach.md) — management principles, testing layers, evidence, governance, release, procurement, and LLM reasoning guidance.
2. [Canonical Test Library.md](<Canonical Test Library.md>) — 200 numbered canonical outcomes and supported user behaviours.
3. [Canonical_WCAG_AA_Relationship_Register.md](Canonical_WCAG_AA_Relationship_Register.md) — canonical normalized mapping to WCAG 2.2 A/AA with relationship type, classification and scope note.
4. [Canonical_Test_Library_WCAG_AA_Summary.md](Canonical_Test_Library_WCAG_AA_Summary.md) — generated one-row-per-test standards and best-practice summary.
5. [Canonical Test Inventory: token dependencies and bi-directional component mapping.md](<Canonical Test Inventory: token dependencies and bi-directional component mapping.md>) — test, component, pattern, and token dependency mappings.
6. [Mobile_Application_and_Website_Test_Library.md](Mobile_Application_and_Website_Test_Library.md) — 432 numbered detailed web and mobile test entries.
7. [Accessibility_ACT-Style_Test_System.md](Accessibility_ACT-Style_Test_System.md) — repeatable pattern, practice, and cross-cutting interpretation tests.
8. [Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests.md](<Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests.md>) — direct, partial, and unevidenced automation coverage plus manual complements for the 200 canonical tests.
9. [AXE_Test_AA_Rule_Descriptions.md](AXE_Test_AA_Rule_Descriptions.md) — AXE rule descriptions and mappings used by the repository.
10. [AXE_and _Test_Inventory_Alignment.md](<AXE_and _Test_Inventory_Alignment.md>) — AXE-to-canonical alignment and manual work needed for conclusive results.
11. [AXE_Test_Remediation_Prompt_Library.md](AXE_Test_Remediation_Prompt_Library.md) — structured prompts for investigating and remediating AXE findings.
12. [AXE → Design Tokens → Components.md](<AXE → Design Tokens → Components.md>) — AXE, design-token, component, and pattern mappings.
13. [Canonical Test Library Alignment to Exact WCAG SC IDs.md](<Canonical Test Library Alignment to Exact WCAG SC IDs.md>) — superseded redirect retained only for historical link continuity.

### Provenance and maintenance

The counts of 200 canonical tests and 432 detailed web/mobile tests are derived from the supplied repository files. They describe separate inventories and must not be added together, compared as if equivalent, or used as completion targets without an approved crosswalk.

When a repository file changes, review this framework's affected mappings, terminology, counts, and retrieval routing. Record the repository version used by each delivery project so that historical evidence remains interpretable.

---

## [ATLF-20] LLM use instructions

**Chunk purpose:** Constrain retrieval, reasoning, and generated outputs based on this framework.

**Keywords:** LLM, RAG, retrieval, reasoning, citations, generated test plans

When an LLM uses this framework and the repository:

1. Retrieve the ATLF chunk that matches the decision, then retrieve the linked repository files needed for exact test detail.
2. Preserve source-library identity, test number, exact title, and source version in every answer or generated artefact.
3. Never infer that identical test numbers in different libraries refer to the same test.
4. Treat component and token mappings as implementation hypotheses until validated against the target system.
5. Treat WCAG and AXE mappings as traceability aids, not proof of complete criterion coverage or conformance.
6. Distinguish an automated rule result from a canonical test conclusion and from a user-journey outcome.
7. Recommend manual or user-centred evaluation whenever meaning, quality, effort, comprehension, timing, orientation, or real task completion is material.
8. State missing evidence and uncertainty. Use `cannot tell`, `not tested`, `blocked`, or `tool error` rather than inventing a pass.
9. Generate test plans from applicable outcomes, assets, states, journeys, environments, and risk; do not select every repository test by default.
10. Cite only repository files when explaining this framework. Do not introduce an external document as an authority unless the user explicitly expands the source boundary.
11. Treat WCAG and other target profiles as governed baselines and evidence sources, not as complete measures of experience. Keep technical conformance, usability, autonomy, equivalence, satisfaction, and service-relevant enjoyment as distinct findings.
12. Do not recommend or approve an exception. Identify the required evidence, delegation tier, escalation triggers, uncertainty, compensating action, review, expiry, and human decision-maker defined in ATLF-04.

### Minimum generated-test format

Every LLM-generated test should include:

- local test ID;
- repository source reference;
- objective and user outcome;
- applicability and exclusions;
- preconditions and required state;
- steps;
- expected result;
- method and environment;
- evidence to retain;
- possible results, including uncertainty;
- related requirement, component, journey, and issue fields;
- reviewer competence and version.

### Minimum answer warning

If the available chunk or repository source cannot support a conclusion, the LLM must say what is missing and identify the next evidence needed. Retrieval confidence is not accessibility confidence.

**Repository sources:** [Test Management Approach](Testing_Approach.md); [Accessibility ACT-Style Test System](Accessibility_ACT-Style_Test_System.md).
