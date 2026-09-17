# Test Management Approach

## Purpose of this Document

This document defines how accessibility testing must be managed, structured, executed, and evidenced across products, services, design systems, and procured systems. It establishes accessibility testing as a continuous management discipline rather than a one-off audit activity. Its purpose is to ensure that accessibility is validated in ways that are technically credible, operationally repeatable, and meaningful to real users.

It is designed for both human practitioners and GPT-based systems. It explains not only what kinds of testing are required, but how they should be planned, combined, governed, interpreted, and used to support decisions about release readiness, remediation, procurement, risk, and continuous improvement. Accessibility testing must therefore be understood as an evidence system that links standards, usability, governance, and lived experience.

## Accessibility Testing as a Management Function

Accessibility testing must be treated as a managed function embedded across the delivery lifecycle. It is not sufficient to run occasional audits or rely on specialist review at the end of delivery. Testing must exist at multiple levels, including component testing, design pattern testing, journey testing, release testing, procurement validation, and post-release monitoring. When testing is positioned only as a final compliance gate, issues are discovered too late, rework costs rise, and accessibility becomes fragile and inconsistent.

A mature test management approach therefore begins with the assumption that accessibility needs to be expressed early as outcome-based requirements, translated into specific testable behaviours, and tracked throughout design, engineering, QA, and operations. Each accessibility requirement should have at least one automatable test and at least one manual or assisted test. This creates a more reliable model because automated checks help prevent regressions while manual and user-centred methods reveal the behavioural and experiential barriers that automation cannot detect.

## The Purpose of Accessibility Testing

Accessibility testing has several distinct purposes, and the organisation must be explicit about which purpose applies in each context. In some cases the purpose is conformance validation, where the organisation needs to know whether a product aligns with accessibility standards and policy expectations. In other cases the purpose is usability assurance, where the real question is whether disabled users can complete tasks with equivalent speed, effort, and confidence. Testing may also be used for procurement due diligence, executive assurance, legal risk management, regression control, or measuring whether accessibility improvements have produced meaningful benefit.

A good test management model does not collapse these purposes into one undifferentiated activity. It makes the decision context explicit. For example, “equivalent experience validation” is used when the organisation needs to know whether disabled users achieve comparable outcomes to non-disabled users. “Barrier identification” is used when complaints, drop-off, or support issues suggest that friction exists somewhere in the journey. “Compliance versus usability gap” testing is used when a system appears technically compliant but still generates evidence of exclusion. “Accessibility impact measurement” is used after remediation or investment, to determine whether accessibility work has delivered measurable value.

## Conformance Testing and Usability Testing Are Not the Same

A central principle of this knowledge base is that conformance testing and usability testing are different activities and must both exist. Conformance testing determines whether a product or component appears to meet technical requirements, usually through structured review against standards, semantic expectations, code behaviour, interaction states, and assistive technology support. Usability testing determines whether disabled users can actually use the product to complete meaningful tasks, with comparable outcomes and acceptable effort. A system can score well in conformance testing and still fail in practice if journeys are too slow, confusing, brittle, or dependent on hidden workarounds.

This distinction is especially important in procurement and internal workplace systems. A vendor may provide documentation, audit reports, or a VPAT suggesting compliance, yet disabled staff may still need significantly more time or effort to complete common tasks. In those circumstances, compliance evidence is not enough. The organisation must test for equivalence of experience and treat usability evidence as a decision-making requirement rather than an optional enhancement.

## A Layered Model of Accessibility Testing

Accessibility testing should be managed as a layered model. At the foundation is pattern-level testing, where reusable components and design patterns are validated for semantics, interaction behaviour, focus management, accessible naming, state communication, responsiveness, and progressive enhancement. Above this sits page and feature testing, where assembled interfaces are checked for structure, relationships, content order, visual and non-visual behaviour, and compatibility with common user settings and assistive technologies. Above that sits journey testing, where complete end-to-end tasks are validated to determine whether users can achieve meaningful outcomes. Finally, there is live service monitoring, where ongoing evidence is gathered from feedback, complaints, analytics, support contacts, and regression monitoring.

This layered approach is essential because not all accessibility problems emerge at the same level. A component can be individually sound but create a broken experience when composed into a larger journey. Equally, a journey may appear to work in a test environment while failing in production after updates, third-party integration changes, or content publishing drift. Test management must therefore connect all layers and make sure evidence flows upward into governance and downward into remediation.

## Shift-Left Testing and Early Evidence

Accessibility testing must begin before code is considered complete. The organisation should treat testing as something that starts in discovery and design, not something that begins when QA receives a build. Inclusive research, accessible wireframes, design review, and pattern specification all contribute to test readiness by defining what accessible behaviour should be before implementation decisions become fixed. Shift-left testing reduces rework, stabilises delivery, and prevents inaccessible patterns from entering the codebase in the first place.

In practical terms, this means pattern documentation must contain accessibility intent, implementation guidance, and test guidance per component. Acceptance criteria must be written in a way that describes what users must be able to do, not just which checklist item the team believes it has addressed. The more explicit this is upstream, the more precise and repeatable testing becomes downstream.

## Test Governance and Ownership

Accessibility testing requires explicit governance. It should not depend on individual enthusiasm or on a single specialist being available at the end of delivery. Governance must define who is responsible for writing tests, who executes them, who interprets the results, and who is accountable for acting on them. Accessibility is a shared responsibility across product, design, engineering, research, QA, content, operations, and leadership, and the test model must reflect that shared responsibility. Clear RACI structures are therefore required.

In practice, design teams should define accessibility behaviours and pattern expectations. Engineering teams should implement automatable checks and ensure semantic and interaction integrity. QA teams should run repeatable manual and behavioural validation. Research teams should include disabled participants in usability work. Product and service owners should decide whether residual risks are acceptable, but they should not be allowed to make those decisions without evidence. Governance must also ensure that testing results are visible in dashboards, release reviews, and remediation backlogs, and that repeated failures are escalated through formal channels.

## Evidence Standards for Testing

A strong accessibility testing model depends on evidence quality. Assertions such as “screen reader compatible,” “WCAG compliant,” or “tested for accessibility” are not sufficient without verifiable evidence. Testing outputs must show what was tested, how it was tested, under which conditions, what issues were found, what remains unresolved, and what level of confidence the evidence provides. This applies equally to internal delivery and vendor-provided evidence.

Evidence must therefore include, where relevant, structured results from automated checks, manual inspection, assistive technology testing, pattern-level binary tests, task-based usability testing, issue severity classification, and remediation status. For procured systems, the organisation should require vendors to provide recent audit reports, assistive technology test results, known issues, and remediation plans, and should independently verify critical journeys rather than relying only on vendor submissions.

## What a Comprehensive Test Set Should Cover

A comprehensive accessibility test set must cover more than standards clauses. It must validate whether the system is perceivable, operable, understandable, robust, and satisfactory in use. It must examine interaction through keyboard, pointer, touch, voice, and assistive technologies. It must test visual and non-visual pathways. It must check behaviour under text scaling, forced-colour or high-contrast modes, reduced-motion preferences, and where relevant narrow viewports and no-JavaScript conditions. It must also validate the persistence of access services and alternative representations through publishing and distribution workflows.

A test set that omits any of these dimensions is incomplete, because accessibility failure often arises not from the absence of a single feature but from the interaction of content, semantics, interaction design, platform behaviour, and user context.

## Pattern Testing as Infrastructure

Pattern testing should be treated as design system infrastructure rather than as an optional reference activity. Reusable patterns must be documented with their purpose, semantics, interaction behaviour by input type, accessibility constraints, and expected output behaviour. They should also include binary tests or clear pass/fail conditions so that the same pattern can be validated consistently across products and releases. This reduces variance across teams and prevents the same accessibility issues from being rediscovered in each project.

Pattern-level testing is especially powerful because it allows teams to solve accessibility once in the pattern and inherit that quality repeatedly. It also makes regression detection more efficient because component updates can be tested against known behavioural requirements before they affect multiple downstream experiences.

## Comprehensive Pattern Tests: Links and Calls to Action

Links and CTA patterns must be tested to confirm that they are semantically correct, visually identifiable, keyboard operable, and understandable out of context. Every link must have meaningful visible text or an equivalent text alternative, and it must remain understandable when surfaced in a screen reader’s links list. Links must not be identified by colour alone, and keyboard focus must be visible. Decorative icons within links must be ignored by assistive technologies, and redundant adjacent links to the same destination should be consolidated rather than duplicated. Target size must be sufficient where links stand alone rather than forming part of running text.

CTA patterns must be treated as links when their purpose is navigation, even when their visual treatment is more prominent than standard inline text. Testing must verify that the CTA appears in a screen reader’s link list, is focusable by keyboard, has a clear visible and accessible name, can be activated by mouse, touch, and keyboard, and does not create a keyboard trap. The clickable area must be large enough to support reliable activation, and the component’s structure must remain understandable to assistive technologies.

## Comprehensive Pattern Tests: Accordion and Disclosure

Accordion and disclosure patterns must be tested for correct state communication, keyboard operability, focus order, and hidden-content behaviour. Keyboard users must be able to reach controls in a logical sequence and toggle sections with Enter or Space. Screen readers must announce each control with its label and current expanded or collapsed state. Collapsed panels must be hidden from assistive technologies and keyboard navigation until revealed. Focus must never become trapped within the pattern. The control’s visual state indicator must not rely on colour alone and must meet contrast expectations where it communicates meaning. The pattern must remain usable at increased text size and, where applicable, should continue to expose content or provide a comparable fallback if JavaScript is unavailable.

## Comprehensive Pattern Tests: Modal Dialog

Modal dialog testing must validate the entire lifecycle of the dialog. Before opening, the dialog must not be accessible to screen readers or keyboard users. When it opens, the underlying page must become non-interactive and appear as such visually, focus must move into the dialog, and screen readers must announce the dialog role and label. While open, the page behind must not scroll, all content within the dialog must remain accessible, and the dialog must include at least one usable close control. When the dialog closes, it must become inaccessible again, the underlying page must be restored, scrolling must resume, and focus must return to an appropriate location, ideally the control that opened it. The dialog must remain readable and operable at 200% zoom and on narrow screens. If nested dialogs are allowed, focus transitions between them must remain logical.

## Comprehensive Pattern Tests: Navigation Menu and Skip Link

Navigation menu testing must verify that the control is properly announced as a button, exposes expanded and collapsed state, can be toggled by keyboard using Enter or Space, moves focus to the first link when opened where that is the intended pattern, and closes with Escape, returning focus to the trigger. Colour must not be the only means of communicating state, and focus indication must remain visible. Voice users must be able to operate controls through clear visible labels.

Skip link testing must verify that the link is present at the start of the document, can be visually hidden until focused without being removed from assistive technologies, is first in keyboard tab order except where unavoidable consent controls exist, activates with Enter or Space, and moves focus to a useful destination such as the main content container. The target itself must be focusable in a way that makes the result of activation meaningful.

## Comprehensive Pattern Tests: Progress Indicators, Toggle Controls, Theme Switchers, and Motion Controls

Progress indicators must always provide a text-based label explaining their purpose and current status, not just a visual bar or spinner. They should be keyboard focusable where that is needed for inspection by assistive technology, must not trap focus, and must remain understandable in high-contrast or forced-colour modes. If animation is used to represent progress, reduced-motion preferences must be respected and spoken updates must be controlled to avoid verbosity.

Toggle buttons must be reachable with Tab, operable with Space, and expose both name and current state clearly to screen readers. Their visible focus indication must remain strong, and label association must survive increased text size and forced-colour environments. Theme switchers must preserve contrast and state clarity across all themes, ensuring that information is never communicated by colour alone and that focus indicators, controls, icons, and success or error states remain perceivable in each theme.

Pause movement controls must be available wherever persistent motion would otherwise create a barrier. Testing must confirm that the control is visible and discoverable, implemented as a native interactive element, stops motion immediately within the defined scope, updates its label accurately between pause and resume states, works by keyboard, pointer, touch, and voice, and does not depend on script success for the usability of the surrounding content. Decorative icons associated with the control must be hidden from assistive technologies.

## Comprehensive Pattern Tests: Tooltips, Tabs, and Carousels

Tooltip patterns must not rely on hover alone. Testing must confirm that keyboard users can reveal the tooltip by focusing the trigger, that the trigger remains focused when the tooltip appears, that Escape dismisses it, that the trigger is associated to the tooltip through appropriate description semantics, and that essential information is not hidden only inside the tooltip. Progressive enhancement must ensure that the information remains available in a no-JavaScript or fallback condition.

Tabbed interfaces must support correct tablist, tab, and tabpanel semantics when scripted, provide visible focus indication, maintain correct selected state, remain usable on narrow screens, and provide a no-JavaScript fallback where all content remains available in some accessible form. Voice users must be able to operate tabs through distinct visible labels.

Carousel testing must validate previous and next controls, pause or stop functionality for auto-advance, reduced-motion compliance, slide position announcements such as “slide one of five,” readable and operable content at increased text size, and a no-JavaScript fallback where all content remains accessible. Progress indicators within the carousel must provide both visual and text alternatives, and voice users must be able to activate controls through visible labels.

## Practice-Level Tests for Design and Engineering

In addition to pattern-level checks, a complete test management model must include practice-level tests for design and engineering quality. These tests do not validate a single component; they validate whether teams are following the practices that make accessible delivery sustainable. Practice-level tests should cover affordances and semantics, alternative text, animation and motion, ARIA usage, colour and meaning, contrast, content order, display preferences, dynamic content, focus indication, forms, validation, heading structure, hidden content, icons, keyboard navigation, landmarks, mobile interaction, multimodal support, progressive enhancement, resize and zoom, client-side routing, typography, and accessibility of web components. These tests should be objective, measurable, and yes/no where possible so they can be reused consistently.

For example, teams should be able to answer yes or no to questions such as whether native semantic elements are used instead of generic containers, whether each link navigates and each button triggers an action, whether meaning is preserved when rendered in greyscale, whether focus remains visible in high-contrast mode, whether forms can be submitted with errors to trigger clear feedback, whether there is exactly one H1 per page, whether all functionality can be completed with keyboard alone, whether content reflows without horizontal scrolling, and whether core purpose remains usable without JavaScript. These kinds of objective tests convert accessibility from vague aspiration into enforceable delivery practice.

## Assistive Technology Testing

Assistive technology testing must be included wherever the user journey is meaningful, the risk is material, or the pattern is likely to behave differently from what automated tools can infer. AT testing should cover screen readers, magnification, keyboard-only interaction, voice control where naming and visible labels matter, and built-in platform accessibility features. The organisation must not assume that semantic code alone guarantees useful experience. Instead, it must verify what assistive technologies actually expose to users and whether the interaction remains workable under realistic conditions.

AT testing is also especially important in procurement. Vendors should provide evidence of testing across relevant platforms and tools, but internal teams should still independently validate critical paths, especially where the tool affects employment, internal productivity, or customer service outcomes.

## User Testing With Disabled Participants

Disabled users must be included in accessibility testing because some barriers only become visible in real use. User testing should not be treated as a symbolic last step. It must be integrated into release testing, redesign validation, service transformation, procurement assurance, and continuous improvement work. The purpose is to determine not only whether users can technically interact with a system, but whether they can do so with equivalent speed, confidence, and effort.

User testing should examine completion of meaningful tasks, not just component interaction. It should measure time-to-complete, error rate, abandonment points, perceived confidence, and satisfaction. It should also help teams identify which barriers are due to code, content, design, process, or cross-channel inconsistency. This provides a stronger basis for prioritisation than technical findings alone.

## Acceptance Testing, Release Gates, and Done Criteria

Accessibility must be part of acceptance testing and release governance. Before launch, teams should define accessibility done criteria, pair manual and automated testing, involve disabled users where the risk or impact justifies it, maintain a pre-launch compliance and evidence log, and ensure post-launch monitoring is ready. Acceptance testing must ask whether critical issues are resolved, whether remaining issues are documented with remediation timelines, whether evidence supports claims of conformance and usability, and whether the release introduces unacceptable risk.

Release readiness should therefore never be based on a single audit score. It should be based on the weight of evidence across the full test set.

## Regression Management and Continuous Monitoring

Accessibility regressions must be expected and managed. Changes in code, content, dependencies, platform behaviour, browser behaviour, and publishing workflows can all reintroduce barriers that were previously resolved. Test management must therefore include regression suites on key journeys, automatable checks in CI/CD, spot checks after release, and mechanisms for gathering user-reported issues. Governance dashboards should track complaints, audit scores, satisfaction measures, training completion where relevant, backlog trends, and remediation progress.

A mature organisation also uses trend reporting and roadmaps rather than isolated issue lists. Accessibility testing is then not merely about finding defects, but about showing whether the service is becoming more usable, more stable, and less risky over time.

## Severity, Prioritisation, and Risk

Accessibility issues must be prioritised according to user impact, journey criticality, frequency, and organisational risk, not only according to standards references. A minor contrast issue on a rarely used page may be less urgent than a form error that blocks task completion for screen reader users, even if both are technically important. Severity analysis should therefore consider whether the issue prevents task completion, increases time or effort, undermines equivalence of experience, affects core legal or commercial journeys, or creates repeated complaints and support burden.

This approach also supports better executive decision-making because it links technical issues to real-world consequences.

## Test Management for Procured Systems

Procured systems require a specialised test management approach. Accessibility must be evaluated at pre-qualification, tendering, award, acceptance, ongoing monitoring, and renewal or replacement. Vendors must provide evidence, but the organisation must also perform independent testing on critical workflows and compare the delivered experience to the vendor’s claims. Testing should validate standards alignment, AT support, task usability, equivalence of experience, unresolved issues, remediation timelines, and the supplier’s ability to maintain accessibility through future changes.

For workplace systems especially, the organisation must test whether disabled staff can complete standard tasks with comparable speed, accuracy, and effort. If they cannot, the system is not acceptable simply because the vendor supplied compliance documentation.

## Core Questions for Accessibility Test Management

An accessibility test management model should repeatedly ask the same disciplined questions. What exactly is being validated: conformance, usability, equivalence, regression resilience, or procurement assurance? What evidence is required to support that decision? Which tests are automatable, and which require human or user-centred validation? Have disabled users been involved where the decision risk justifies it? Are unresolved issues documented clearly, prioritised rationally, and linked to remediation? Are changes improving the experience measurably over time?

These questions help ensure that accessibility testing remains objective, operational, and decision-useful.

## GPT Retrieval and Reasoning Guidance

When used by a GPT, this document should guide the system to treat accessibility testing as a layered evidence practice. It should distinguish between standards conformance and usable experience, recommend combined automated, manual, assistive technology, and disabled-user validation, and explain why different decision contexts require different forms of evidence. It should also be able to generate comprehensive tests for common design patterns by defining expected semantics, interaction behaviour by input type, focus and state management, fallback behaviour, and pass or fail outcomes. When asked to evaluate a design pattern or practice, it should default to describing both what must be true and how that would be tested in practice.

## Closing Principle

Accessibility testing is successful when it proves not only that a system appears to meet requirements, but that people can actually use it with confidence and equivalent outcome. When component tests, practice tests, assistive technology testing, disabled-user research, acceptance testing, and monitoring all work together, accessibility stops being a periodic audit exercise and becomes a managed quality system. At that point, testing no longer sits at the end of delivery. It becomes part of how accessible products and services are continuously designed, released, and improved.
