---
title: "Test Catalog Execution Clarifications"
version: "1.0"
status: "Operational clarification for AI and human test management"
repository: "Double-FW/QA_Accessibility_Testing"
scope:
  - "Canonical Test Library.md"
  - "Mobile_Application_and_Website_Test_Library.md"
  - "Accessibility_ACT-Style_Test_System.md"
  - "Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests.md"
  - "Accessibility_Test_Led_Delivery_Framework.md"
precedence:
  - "This document clarifies operational interpretation; it does not change source test IDs, titles, or WCAG mappings."
  - "The source library remains authoritative for its test identity and requirement. Use this document to resolve the execution ambiguities listed below."
  - "Where a product's declared target profile or applicable standard requires a stricter or more specific rule, record and use that profile; do not infer it from this document."
---

# Test Catalog Execution Clarifications

## Purpose and authority

Use this document when selecting, recommending, executing, or reporting repository tests. The repository contains distinct kinds of records: outcome requirements, detailed checks, pattern procedures, automation mappings, and research or process evaluations. They are related, but they are not interchangeable tests and their identifiers must remain namespaced.

This is an operational supplement, not a replacement for any library, standards relationship register, or product-specific test plan. Preserve the exact source library, test number or ID, title, version, and source requirement when creating a local execution record. Do not mark a source requirement as executed merely because a related automated rule ran.

## Required execution record

Before recommending or running a test, create or resolve a local test procedure with these fields:

| Field | Minimum content |
|---|---|
| Identity | Source library, source ID/number, exact source title, source version, local procedure ID and version. |
| Decision and outcome | What decision this evidence supports and the user outcome being evaluated. |
| Applicability | Explicit include conditions, exclude conditions, and how to decide each. If applicability cannot be decided, record `cannot_tell`; do not assume `not_applicable`. |
| Scope | Product/page/screen/component, task or journey, relevant states, platforms, content types, and sampled instances. |
| Preconditions | Build, account/data state, permissions, device/browser/OS, input method, assistive technology and version where relevant, user preferences, and any required setup. Record unknowns. |
| Procedure | Reproducible, ordered steps; identify the actor or tool and state to reach. Avoid combining independent checks unless each has a separately recorded result. |
| Expected result | Observable pass and fail conditions, including any permitted alternatives and their rationale. Avoid adjectives such as “appropriate,” “sufficient,” “clear,” or “usable” unless the procedure defines how a competent reviewer determines them. |
| Method and competence | Automated, manual technical, assistive-technology, expert judgment, or user research. Identify required reviewer competence and any human review that automation cannot replace. |
| Evidence | Actual observation or raw tool output, environment/build, date, tester/runner, evidence reference, and known limitations. Never fabricate evidence. |
| Result | Use `pass`, `fail`, `blocked`, `cannot_tell`, `not_tested`, `not_applicable` (with reason), or `tool_error`. Record separate outcomes for independent assertions. |
| Traceability | Related product requirement, component, state/journey, automation implementation/rule ID, issue, retest, and applicable WCAG relationship where supported by the canonical register. |

A test with no usable procedure is a requirement needing test design, not an executable test recommendation. An AI system may draft a procedure, but must label it as proposed and obtain appropriate review before treating it as approved or executing it.

## Applicability and conditional methods

- Interpret “where appropriate,” “where needed,” “where possible,” “if available,” and similar phrases as a requirement to decide and record applicability, not as permission to silently skip a check.
- Record the decision rule and its result. If the necessary product facts, target profile, technology, or method are unknown, use `cannot_tell` or `blocked` as applicable; do not convert the gap to a pass or `not_applicable`.
- If a method is unavailable (for example, a particular assistive technology or voice-control setup), record the unavailable method as `not_tested` or `blocked` with the reason. Report any completed methods separately; do not claim the combined test passed.
- “All” means all items in the explicitly declared test scope and sample, not every item in the product, unless the procedure actually tests the entire product. State the denominator and sampling limits.
- Test JavaScript-disabled, no-styling, reduced-motion, forced-colour, zoom, touch, voice, or assistive-technology modes only when applicable to the product and declared scope. Define the tested configuration and expected fallback instead of assuming every product must expose identical behavior in every mode.

## Clarifications for ambiguous or conflicting catalog wording

### Flashing and flicker (Mobile Application and Website Test Library tests 22–23; Canonical Test Library tests 26–27)

Treat the frequency-safety check and warning/alternative check as separate assertions. A warning, opt-out, or alternative is not by itself evidence that content meeting an unsafe flashing condition is safe. Evaluate the content against the product's declared applicable safety threshold and record the measurement method, content, and result. If the threshold, measurement, or exception conditions are not specified for the decision, record the gap and do not infer a pass from a warning.

### Images and text alternatives (detailed tests 13–15 and 88; Canonical tests 33–36)

Do not apply “all images must have an alternative text attribute” as a blanket rule that every image needs non-empty text. First classify the image's function in context:

- **Decorative/redundant:** should not create a redundant assistive-technology announcement; an empty alternative or equivalent suppression may be appropriate.
- **Informative:** provide an alternative that communicates the relevant information or purpose in context.
- **Functional:** ensure the control's accessible name communicates its action or destination; do not assess the image in isolation from its control.
- **Complex:** provide an accessible equivalent sufficient for the information or task; a short alt string alone may not be sufficient.

Attribute presence or non-empty text alone cannot pass an alternative-quality test. If the image's role or meaning cannot be determined from the evidence, record `cannot_tell` and request contextual review.

### Meaningful background images (detailed tests 95–97)

The outcome is access to the meaningful information, not a requirement that a CSS background image itself be exposed as an image node. Accept an equivalent available through appropriate text or another accessible presentation in context. Test decorative background imagery for absence of noisy or misleading announcements. Record the relevant content and user task; do not require duplicate announcements when an equivalent is already present.

### Decorative, static, disabled, and unavailable elements (detailed tests 11–12)

Keep these categories distinct. Decorative or static non-interactive content should not be made a keyboard focus stop. A disabled control, when present, should expose its unavailable state through the platform semantics and remain understandable; it is not required to be focusable in every platform or pattern. Test for false interactive affordances and misleading semantics, not for a universal rule that all exposed non-meaningful elements must be labelled “unavailable.”

### Focus, modal behavior, and pattern-specific interaction (ACT-style tests)

Focus expectations depend on the declared interaction model. For each menu, dialog, panel, disclosure, or other composite, state the intended focus-entry, in-component navigation, dismissal, and return behavior before execution. If behavior is conditional in the source test, the local procedure must select and document the applicable branch. Do not pass an undefined branch as a result.

A modal's background-inertness check concerns interaction and accessibility exposure while open. Scroll locking is a separate product behavior: test and report it separately when required by the product specification or test profile, rather than making scroll lock a universal accessibility pass condition. A focus containment check must also confirm that the user has a defined way to exit the modal; “background cannot be used” must not be interpreted as trapping the user without a dismissal route.

### Reduced motion and animation

Specify which motion is being tested, how the preference is set, whether the setting is read before or after load, and the expected behavior for essential versus non-essential motion. Do not assume that “remove,” “slow,” or “reduce” are equivalent without an approved product-specific expected result. Record the preference and observed motion. A missing preference control is not automatically a failure where the test concerns a system preference; test the declared system preference response.

### Zoom, text resize, and reflow

Name the exact zoom or text-resize mechanism, target level, viewport, orientation, and task. Do not treat browser zoom, text-only resize, and platform text scaling as interchangeable. Record content or functionality loss separately from horizontal scrolling; identify any content whose two-dimensional presentation is essential and the applicable exception or product requirement. A general “200%” observation without these details is insufficient evidence for a pass.

### Contrast and visual judgment

For a contrast measurement, identify foreground/background states, the measurement tool/version, measured values, and the threshold source in the declared target profile. For qualitative checks such as blur simulation or general legibility, state that the outcome is expert/user evaluation and record the method and limitations; do not present simulation as a substitute for user evidence or a standards measurement.

### Captions, audio description, and media alternatives

Separate presence, synchronization/technical playback, and content accuracy/completeness. Identify the media asset, language, track, relevant scenes, and reviewer method. Presence of a caption or audio-description track alone does not establish that it is accurate or conveys the needed information. If content quality requires human review, automated metadata checks are only partial evidence.

### User research and continuous-improvement checks (ACT-style X-01–X-03)

Classify these as research/evaluation or process-health activities, not ordinary component pass/fail tests. Before running them, define the decision question, sample and recruitment rationale, participant safeguards, tasks/data sources, measures, analysis method, comparison basis if any, and limitations. Do not require statistical significance by default or infer population-wide equivalence from a small sample. Report observed results and uncertainty separately; a research result does not erase a separately established technical or standards finding.

For X-03, define the review period, comparable product/build scope, data sources, and the signal that would count as an improvement. Missing historical data is `cannot_tell` or a stated evidence gap, not an automatic failure of the product.

## Overlap, mapping, and automation controls

- Similar titles or themes do not prove duplicate coverage. Keep distinct test identities and record a reviewed relationship such as `equivalent`, `broader than`, `narrower than`, `partially covers`, `manual complement to`, or `duplicates`, with rationale and version.
- Do not add test counts across libraries or count one automated finding as multiple independent passes. Report coverage by source library, requirement/outcome, method, state, and journey.
- Interpret automation labels conservatively: `direct` means only that a tool can test a specified, observable subcondition in a specified rendered state; `partial` means it cannot establish the complete outcome; `manual-primary` means human evaluation is required for a conclusion. These labels do not imply that any tool has been configured or run.
- Store tool rule IDs separately from repository test IDs. Record tool, rule-set, runner, browser, build, state, exclusions, raw output, and human review. Treat incomplete/needs-review output as unresolved until reviewed.
- Use the Canonical WCAG 2.2 A and AA Relationship Register for standards traceability. Keep WCAG outcomes, repository requirements, and broader inclusive-design or user-research findings in separate result fields. Do not infer a WCAG failure from a repository best-practice failure, or complete criterion conformance from one related test pass.

## Recommended result reporting

Every report should make clear:

1. what source test and local procedure were used;
2. what product scope, sample, and state were tested;
3. what method, environment, and versions were used;
4. what was directly observed and what was inferred;
5. the result for each assertion and any untested or blocked methods;
6. the user outcome, impact, and evidence limitations;
7. related issue, retest, or next action; and
8. whether any standards statement is supported by the canonical relationship register and a sufficiently broad conformance assessment.

A report must not imply that a test was executed merely because it was recommended, generated, mapped to an automated rule, or included in a plan.
