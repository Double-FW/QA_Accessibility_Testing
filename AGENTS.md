# AGENTS.md

## Purpose and scope

These instructions apply to AI agents working in this repository, at its root and in all subdirectories unless a more specific `AGENTS.md` is added later. This repository is an accessibility QA and test-management knowledge base; it does not itself provide a product under test, an execution environment, or a test runner.

This file serves two related but distinct purposes:

1. **Repository work:** guide agents that inspect, edit, organize, or summarize this repository's guidance and resources.
2. **QA assistance:** guide agents asked to plan, conduct, or report accessibility testing of a product, only to the extent that the user and available tools authorize and enable that work.

Do not present QA methodology as proof that a test was executed. Do not treat repository guidance as a substitute for product-specific instructions, human judgment, or authoritative standards sources.

For repository methodology, consult [Testing_Approach.md](Testing_Approach.md), the [delivery framework](Accessibility_Test_Led_Delivery_Framework.md), and the [README authority model](README.md#3-authority-model) as relevant. Follow their stated source and evidence distinctions. If sources conflict or a referenced file is unavailable, state the conflict or gap; do not silently invent a resolution.

## Authority, safety, and limits

- Follow higher-priority system and platform instructions, then applicable user instructions, then this file and relevant repository guidance. Where instructions conflict, obey the higher-priority instruction and explain any material limitation.
- Use repository files as reference material. Preserve source identities, titles, and distinctions between canonical tests, WCAG mappings, automation rules, derived summaries, hypotheses, and remediation suggestions.
- Do not claim that a product is accessible, conforms to a standard, is legally compliant, or is ready for release unless the claim is explicitly within the requested decision scope and supported by appropriately scoped evidence. State limitations and uncertainty.
- Never fabricate observations, execution, evidence, issue references, approvals, ownership, or tool capabilities. Distinguish direct observation from inference and from guidance or a proposed test.
- Do not access, collect, expose, or retain personal, sensitive, or confidential data beyond what is necessary and authorized for the task. Avoid including identifying information in test evidence; seek an approved safe test account or synthetic data if needed.
- Do not make consequential changes to a product, publish externally, create or modify issues, accept exceptions, approve a release, or communicate on someone's behalf without explicit authorization for that action. Drafting a recommendation is not approval.
- Stop and report when authorization, access, environment, participant safeguards, or evidence is insufficient. Do not recruit or test with disabled participants without an appropriate human-approved research process and safeguards.

## Repository work

For tasks involving this knowledge base:

- First identify the requested change and inspect relevant source files, including their declared authority and relationships.
- Make changes only within the user's requested scope. Do not add supporting files or claim that schemas, checks, automations, or enforcement exist unless the repository actually contains them.
- Keep normative requirements, recommendations, examples, and derived mappings distinct. Label illustrative material as illustrative when it could be mistaken for a configured process or executable artifact.
- Preserve traceability and avoid duplicating authoritative content when a concise link to its source is sufficient.
- Report files changed, the substance of the changes, and any checks actually performed. If no check was run, say so.

## QA planning and execution

### Before testing

Define and report, as applicable:

- the product area, platform, user journey, intended outcome, and decision purpose;
- the scope: pages, screens, flows, components, states, devices, browsers, and operating systems;
- relevant input methods and assistive technologies, including versions when known;
- preconditions, access limitations, and the test method.

Use a method suited to the question: automation for detectable issues and regression signals; keyboard review for focus and operability; assistive-technology review for semantics and announcements; manual inspection for content, visual presentation, and recovery; and user research where real-world outcomes are needed. Do not imply that one method substitutes for another.

If details are unknown or unavailable, record them as unknown or out of scope. Do not guess a build, environment, assistive technology, or user group. Tailor checks to the actual platform and journey rather than treating a checklist as a claim that every item applies.

### During testing

For each test or finding, record what is available and relevant:

- preconditions and reproducible steps;
- expected and observed result;
- test method and environment, including product build/version when known;
- evidence reference or a concise observation, and whether it is direct evidence or inference;
- status and user outcome/impact;
- related issue or requirement reference, if one exists.

Capture screenshots, recordings, logs, or other evidence only when authorized and appropriate. Identify missing evidence; do not imply that evidence was preserved when it was not. For automated results, identify the tool and scope where known and do not infer coverage beyond the states it inspected.

### Status and reporting

Use these result statuses consistently:

- `pass`: the defined check was performed and its expected result was observed;
- `fail`: the defined check was performed and a barrier or unmet expected result was observed;
- `blocked`: execution could not proceed because of an external prerequisite or access barrier;
- `cannot_tell`: available evidence does not support a pass/fail conclusion;
- `not_tested`: the check was not performed;
- `not_applicable`: the check does not apply to the stated scope, with a reason;
- `tool_error`: a tool failure prevented a reliable result.

Never convert `not_tested`, `blocked`, `cannot_tell`, or `tool_error` to `pass`. Do not use `conditional_pass` as a test status; report a decision with its conditions and evidence limits separately from individual test results.

Summaries should state what was tested, how, what was observed, user impact, unresolved risks or defects, evidence limitations, and next steps. Tie each defect to an affected user outcome and task; distinguish observed impact from anticipated impact. Severity labels may be used only with a stated basis or the applicable project rubric. Do not claim a formal compliance result from an automated scan, a mapping, or incomplete coverage.

## Practical accessibility coverage

Select relevant checks based on scope and risk. Consider the full task, including success, error, and recovery paths.

### Websites and web applications

As relevant, inspect title, headings, landmarks, navigation and skip links; keyboard access, visible focus, logical order and restoration; names, roles, states, labels and instructions; form errors and recovery; dialogs and overlays; dynamic status updates; responsive layouts, text scaling, zoom/reflow, readability and contrast; media alternatives; and motion preferences and controls. Verify behavior through the interaction methods and assistive technologies in scope.

### Mobile applications

As relevant, inspect screen structure and control semantics; touch and alternative interaction routes; screen-reader traversal and announcements; focus across screens and overlays; text scaling, contrast, orientation and layout adaptation; forms, errors, loading, alerts and dynamic changes; and completion of the task without inaccessible gestures or hidden controls.

These are prompts for selecting tests, not a universal checklist or a statement that any check has been executed.

## Issues, remediation, and release decisions

When asked to report a defect, include a concise description, affected area, user task and impact, reproduction steps, expected and observed behavior, status, relevant environment/evidence, and a suggested next step when supported. Separate a proposed remediation from a verified fix. Use an existing issue process only when it is available and the user has authorized its use.

For release or procurement advice, describe tested scope, evidence methods, coverage gaps, unresolved defects and risks, and any known exceptions. An agent may summarize evidence and recommend next steps but MUST NOT grant approval, accept risk, or assert organizational sign-off without explicit authority. If evidence is incomplete, say so clearly; do not imply release readiness.

## Response expectations

Keep reports concise and specific to the request. Separate:

- **Evidence:** what was actually observed or returned by a tool;
- **Inference:** what the evidence may indicate, with uncertainty;
- **Recommendation:** what should be considered next.

State when work was only planned, when a check was not run, and when a conclusion depends on information not available. Link to relevant repository sources where useful. Do not output an invented structured record or imply that an illustrative format is a repository schema.
