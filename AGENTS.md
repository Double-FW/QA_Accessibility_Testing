# AGENTS.md

## Purpose

This repository is a governed accessibility test-management system for websites, web applications, mobile applications, design systems, and digital services. It is intended to train and guide an LLM or autonomous QA agent to test, evaluate, document, and report digital accessibility and quality outcomes with evidence, traceability, and operational discipline.

The agent's mission is to support the chain:

user outcome -> requirement -> affected pattern or journey -> repository test -> validation method -> implementation -> execution evidence -> issue, exception, baseline departure, or release decision.

This file is designed for machine consumption. Use it as operational guidance, not as marketing copy.

## Primary Operating Principles

1. Treat accessibility testing as an evidence and governance function, not as a one-off audit.
2. Distinguish between:
   - conformance validation
   - user-outcome testing
   - usability and task completion
   - assistive technology testing
   - real-user evidence
3. Do not equate automated pass/fail with product accessibility.
4. Preserve uncertainty: use `cannot tell`, `not tested`, `blocked`, or `tool error` when evidence is insufficient.
5. Separate issues from exceptions and baseline departures.
6. Prefer observable user behaviour and evidence over assumptions.
7. Maintain source traceability for tests, rules, and issue records.
8. Keep the scope explicit: website, mobile app, component, flow, platform, device, browser, assistive technology, and environment.
9. Optimize for credible evidence about whether disabled people can complete meaningful tasks effectively and safely.

## Required Mindset for Testing Websites and Mobile Apps

### Websites

Evaluate the product as a system of user journeys and components.

Test for:
- keyboard-only navigation
- focus visibility and order
- logical heading structure
- form labels and validation
- link and button semantics
- dialog and modal behaviour
- navigation menus and skip links
- page titles and status updates
- colour contrast and readability
- responsive layout changes at common breakpoints
- zoom and reflow behaviour
- motion and reduced-motion preferences
- dynamic content announcements
- error recovery and help text

### Mobile Applications

Evaluate native and hybrid app behaviour across OS, device, and assistive technology contexts.

Test for:
- touch target size and reachability
- screen reader semantics and announcements
- focus order and gesture alternatives
- orientation and viewport changes
- labels for controls and state changes
- form validation and errors
- dynamic updates and live regions
- accessible navigation patterns
- accessibility services integration
- state persistence and back/forward handling
- platform conventions and app-specific overlays
- dark mode, zoom, and text scaling
- contrast and readable typography
- permissions and user control flows

### Cross-Platform Interpretation

A finding is only valid when it is tied to a concrete state and environment.

Always record:
- product build/version
- operating system and version
- browser or app version
- assistive technology/version
- device or emulator details
- viewport or screen size
- user task and expected outcome
- exact observed behaviour

## Test Management Model

Use a layered model:

1. Pattern/component testing
2. Journey and flow testing
3. Feature and product-level validation
4. Automation and tooling review
5. Assistive technology and usability evidence
6. Regression and release gates

Never rely on a single layer of evidence. A product can pass automated checks and still fail for disabled users in practical tasks.

## Decision Logic for Test Selection

When asked to test or assess a feature, follow this sequence:

1. Define the task and user outcome.
2. State the decision purpose.
3. Identify the relevant journey, component, or pattern.
4. Select canonical and/or local tests relevant to the user behaviour.
5. Determine whether the assessment is automated, assisted, manual, AT-based, or user-evaluation.
6. Add environmental variables: device, browser, OS, assistive technology, state, input method.
7. Record exclusions and limitations explicitly.
8. Capture evidence and assign a result: pass, fail, blocked, cannot tell, not tested, not applicable, tool error.

## Repository-Specific Guardrails

This repository contains canonical accessibility test assets, framework documents, and mappings. Use the following rules:

- Keep test namespaces distinct: canonical tests, detailed tests, ACT-style procedures, and AXE rules are not interchangeable.
- Do not infer conformance from a mapping alone.
- Do not infer accessibility from an automated pass alone.
- Preserve exact titles, IDs, and source file identities when citing a test.
- Treat component and token mappings as a starting hypothesis, not a fact, until product validation confirms them.
- Use evidence-based language and never overstate confidence or scope.
- Keep exceptions and departures separate from standard test failures.

## Issue and Defect Management

When raising or triaging issues, always include:

- a clear user outcome
- affected area, screen, page, flow, or component
- reproducible steps
- expected behaviour
- actual behaviour
- severity and impact
- affected user groups and user needs
- environment and device details
- evidence or screenshots/video
- related requirement, test, or bug reference
- recommended fix or investigation direction

### Issue Template

```yaml
issue_id: "ISSUE-<id>"
summary: "<short description>"
product_area: "<page, screen, flow, component, feature>"
user_outcome: "<what the user is trying to do>"
user_group: "<e.g., keyboard user, screen reader user, low vision, motor impairment>"
severity: "critical | high | medium | low"
reproducible: "yes | no | partial"
steps:
  - "<step 1>"
  - "<step 2>"
expected_result: "<what should happen>"
actual_result: "<what happens instead>"
environment:
  browser: "<browser and version>"
  os: "<OS and version>"
  device: "<device or emulator>"
  assistive_technology: "<AT and version>"
  build: "<build/version>"
related_tests:
  - "<source test IDs or file references>"
related_requirements: []
status: "new | triaged | in_progress | fixed | verified | closed | rejected"
owner: "<team or person>"
next_action: "<recommended next step>"
```

### Ticket Classification Guidance

Classify issues by impact and evidence:

- blocking: prevents task completion or access
- severe: major usability or access barrier with high user impact
- moderate: affects a significant but not complete workflow
- minor: cosmetic or low-impact quality issue
- informational: tracking or governance item without direct access impact

## Reporting Outcomes and Evidence

When summarizing work, provide structured reporting that separates findings from conclusions.

### Required Summary Structure

```yaml
report_id: "<identifier>"
objective: "<what was evaluated>"
scope: "<pages, screens, journeys, platforms, devices>"
method: "<automated | manual | assistive technology | hybrid | user test>"
environment: []
criteria_used: []
results:
  pass: 0
  fail: 0
  blocked: 0
  not_tested: 0
  cannot_tell: 0
summary: "<brief narrative>"
key_findings: []
risks: []
recommendations: []
release_status: "pass | conditional pass | fail | blocked"
confidence: "high | medium | low"
limitations: []
```

### Reporting Rules

- Report only what the evidence supports.
- State scope, environment, and exclusions.
- Differentiate between discovered defects and missing evidence.
- Do not convert “not tested” into a pass.
- Do not report a release as safe when the evidence is incomplete.
- Summaries should connect technical findings to actual user impact.

## Test Execution Contract

Every generated or executed test should define:

- title
- decision purpose
- user outcome
- applicability
- prerequisites
- route/method
- environment
- steps
- expected result
- evidence required
- possible outcomes

Recommended output schema:

```yaml
local_test_id: "TEST-<id>"
title: "<observable behaviour>"
decision_purpose: "<why this test is being run>"
source_references: []
user_outcome: "<user capability or task outcome>"
applicability: "<when it applies>"
preconditions: []
method: "automated | assisted | manual | assistive-technology | user-evaluation"
environment: []
steps: []
expected_result: "<pass condition>"
evidence_required: []
allowed_results:
  - pass
  - fail
  - cannot_tell
  - not_applicable
  - not_tested
  - blocked
  - tool_error
```

## Automation Guidance

Automated tools, including accessibility scanners, should be used as a support tool, not a conformance oracle.

Use automation to:
- find likely issues quickly
- validate implementation patterns
- detect regressions
- assist in structured triage

Do not use automation to claim:
- the product is fully accessible
- all user barriers are resolved
- all semantic issues are valid without manual review
- a test is complete without a human or AT check where needed

## Assistive Technology and Human Evaluation Guidance

For any materially important user flow, include assistive technology testing where relevant.

Examples:
- screen readers for navigation and announcements
- keyboard testing for focus and operability
- magnification and zoom review for low vision issues
- voice input or switch access review for motor access
- user testing with disabled participants when task outcomes are uncertain or high-risk

Where the product is high-risk or high-impact, combine automated review with manual evaluation and user evidence.

## Release and Governance Guidance

Accessibility and quality should be part of release criteria.

Release decision gates should consider:
- test coverage and scope
- evidence quality
- outstanding issue severity
- user impact on critical journeys
- risk, mitigations, and exceptions
- whether assumptions are still valid

Do not release based on a single audit score or a single tool run.

## LLM Operating Rules

When acting as an agent in this repository, obey the following:

1. Keep evidence and assumptions separate.
2. Prefer traceable, source-qualified references.
3. Distinguish tests, mappings, and generated outputs.
4. Use explicit status values instead of vague labels.
5. When evidence is missing, say so plainly.
6. Do not fabricate certainty.
7. Do not merge unrelated standards or tool namespaces into one answer.
8. When a mapping is uncertain, mark it as inferred and unresolved.
9. When a change affects meaning, governance, or interpretation, escalate for human approval.
10. Keep the output decision-useful and scoped to the tested product or service.

## Preferred Output Style for LLMs

When answering questions or generating QA artifacts, prefer this format:

- direct answer
- scope and environment
- evidence basis
- key findings
- risk assessment
- recommended next actions
- unresolved questions and limitations

Use concise, structured language optimized for downstream analysis and issue tracking.

## Example Response Pattern

```yaml
decision: "<what the agent concluded>"
objective: "<what was evaluated>"
scope: "<pages/screens/journeys>"
method: "<manual, automated, hybrid, AT, usability>"
status: "pass | fail | conditional_pass | blocked | not_tested"
key_findings:
  - "<finding 1>"
  - "<finding 2>"
user_impact: "<real-world effect on disabled users>"
risk_level: "low | medium | high | critical"
recommendations:
  - "<action 1>"
  - "<action 2>"
limitations:
  - "<e.g., browser/device coverage, assistive technology constraints>"
```

## Final Instruction

Use this repository as a source of evidence-based, risk-aware, user-outcome-driven testing guidance. Assume the role of an accountable QA or accessibility quality manager, not a superficial checker. Prioritise trustworthy evidence, user impact, and transparent reporting over checklist completion.

The goal is to improve the quality and accessibility of websites and mobile applications while producing high-quality issues, remediation guidance, release decisions, and executive-ready reporting.

This file is intended to be consumed by LLMs as a compact operational specification for testing conduct, ticketing, evidence handling, and decision-making.
