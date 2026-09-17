
# Accessibility ACT-Style Test System
## Accessibility Manager Knowledge Base (Structured Pattern and Practice Test Library)

---

## Purpose of this Document

This knowledge base defines a structured ACT-style accessibility test system for evaluating design patterns, interaction models, content practices, and implementation quality. It is intended to be used as a standalone testing reference by accessibility managers, designers, developers, QA practitioners, procurement teams, and GPT-based systems that need to generate or reason about tests in a consistent way.

The purpose of this document is not only to state what should be true of an accessible interface, but to explain how that truth is evaluated in practice. Each section therefore explains the objective of the test, what needs to be prepared before running it, how the test should be carried out, and what the expected outcome must be. Where appropriate, the tests also clarify why the pattern matters, what kinds of barriers it is designed to detect, and what to do when the result is only partially successful.

This test system is derived from the uploaded source material and combines pattern-specific testing, design-practice testing, assistive technology validation, usability checks, progressive enhancement checks, and quality-assurance principles. It is built on the principle that conformance alone is not enough. A pattern or practice should only be considered successful when it is perceivable, operable, understandable, robust, and satisfactory in real use.

---

## How to Use This ACT-Style Test System

Each test entry in this document follows the same general structure. The first part defines the objective so the tester understands what is being proved. The second part explains the setup and any conditions that should be established before testing begins. The third part describes the test steps in a repeatable order. The fourth part defines the expected outcome. Some entries also include notes on interpretation, because a pattern can sometimes meet a narrow technical expectation while still failing in a broader experiential sense.

This document should be used at multiple stages of delivery. It can be applied during design-system authoring, component development, feature QA, release readiness, procurement assessment, regression testing, and periodic auditing. It can also be used to generate reusable test plans, to guide accessibility acceptance criteria, and to support GPT systems that need to produce structured test outputs.

Where a pattern is implemented differently across products, the test logic should remain stable while selectors, controls, or specific interface labels may change. The intent is to make accessibility testing repeatable without making it brittle.

---

## Core Testing Principles

Accessibility testing should be layered. Pattern tests are not a replacement for journey testing, and journey testing is not a replacement for design-practice review. Automated tests are valuable, but they cannot determine whether a user can complete a task with confidence or whether an unconventional interaction increases cognitive load. For this reason, tests should combine automation, manual inspection, assistive technology testing, and where possible testing with disabled users.

A good accessibility test should be observable, behaviour-based, and specific enough that two testers running the same test under the same conditions would come to the same conclusion. Ambiguous phrasing should be avoided. Terms like “good,” “clear,” or “accessible” should be translated into things that can be seen, heard, measured, or verified.

Testing should also reflect real user contexts. This includes keyboard-only use, screen reader use, touch interaction, voice control where naming matters, increased text size, reduced motion preferences, forced-colour or high-contrast modes, and where relevant no-JavaScript conditions. The broader aim is to verify equivalent access rather than a single idealised interaction path.

---

## Pattern Test Entries

### Pattern: Call to Action (CTA)

#### Test CTA-01 — Semantic Link Integrity

The objective of this test is to confirm that a CTA whose purpose is navigation behaves and is exposed as a link rather than as an on-page action control.

Before running the test, identify the CTA and confirm that it is intended to take the user to another destination rather than trigger an in-page function.

Run the test by navigating the page with a screen reader and opening the list of links. Then locate the CTA using keyboard Tab navigation and inspect the rendered markup if necessary.

The expected outcome is that the CTA appears in the screen reader’s links list, receives focus with Tab, can be activated with Enter, and is implemented with semantic link behaviour rather than button behaviour. The accessible name must come from visible text or an equivalent text alternative.

#### Test CTA-02 — Multi-Input Activation

The objective of this test is to verify that the CTA can be activated consistently by mouse, touch, keyboard, and where relevant voice control.

Set up the component on a page where it can be interacted with normally. If voice control software is available, enable it.

Click the CTA with a pointer, tap it on a touch device, activate it with Enter after focusing it by keyboard, and where possible use a voice command based on its visible label.

The expected outcome is that all input methods activate the same destination, that tapping or clicking anywhere within the CTA boundary activates it when that is the intended pattern, and that visible labels support one-step voice invocation such as “Click [label]”. Link context menus must also remain available where standard link behaviour should apply.

#### Test CTA-03 — Focus and Target Reliability

The objective of this test is to confirm that the CTA is discoverable, focus-visible, and large enough for reliable activation.

Navigate to the CTA with keyboard only. Observe the focus indicator. On touch, attempt activation using typical finger-size targeting rather than highly precise tapping.

The expected outcome is that focus is visibly indicated, the CTA remains clearly interactive, and target size supports reliable activation without requiring precision.

---

### Pattern: Card

#### Test CARD-01 — Reading Order Integrity

The objective of this test is to ensure that the reading order implied visually by the card is preserved in the DOM and therefore in assistive technology output.

Identify a card with multiple pieces of content, including text and interactive elements. Review its visual order, then inspect its source order using keyboard navigation, reading tools, or screen reader sequential reading.

The expected outcome is that the DOM order matches the intended reading order, that users do not encounter a “mishmash” sequence, and that interactive elements are encountered in a sensible progression matching the visual hierarchy.

#### Test CARD-02 — Link Duplication and Overlap

The objective of this test is to detect redundant or overlapping interactive regions within a card.

Use mouse, keyboard, and touch to inspect all interactive regions within the card. Compare destinations where multiple links are present.

The expected outcome is that adjacent or overlapping duplicate links to the same destination are avoided or consolidated, and that touch targets do not overlap in a way that causes accidental activation.

---

### Pattern: Links and Anchors

#### Test LINK-01 — Meaningful Link Text

The objective of this test is to confirm that links remain understandable out of context.

Use a screen reader’s links list or a browser accessibility panel to review the accessible names of all links on the page. Where screen reader tooling is unavailable, inspect visible text and accessible names directly.

The expected outcome is that each link has visible text or an equivalent text alternative, that its purpose remains understandable when listed out of context, and that vague labels such as “click here” are avoided.

#### Test LINK-02 — Visual Distinguishability

The objective of this test is to ensure that links can be identified visually without relying on colour alone.

Inspect links in context, then simulate greyscale or reduced-colour conditions if available.

The expected outcome is that links remain visually distinct from surrounding text through cues such as underlining, weight, decoration, or other non-colour indicators, and that focus visibility remains clear during keyboard navigation. Decorative icons inside links must be ignored by screen readers.

---

### Pattern: Accordion

#### Test ACC-01 — Keyboard Navigation and Toggle

The objective of this test is to verify that accordion controls are fully operable by keyboard.

Load the page, use Tab to reach the first accordion control, move through controls in sequence, and toggle each section with Enter or Space.

The expected outcome is that each control receives focus in logical order, can be toggled by keyboard, and displays a clear visible focus indicator during interaction. Focus must not become trapped.

#### Test ACC-02 — Screen Reader Role and State

The objective of this test is to confirm that accordion controls expose the correct label and expanded or collapsed state.

Enable a screen reader and move focus through each accordion control.

The expected outcome is that each control is announced with its label and current state, and that users hear an appropriate description of the control’s role.

#### Test ACC-03 — Focus Indicator Contrast

The objective of this test is to validate the visibility of focus indicators.

Navigate through accordion controls by keyboard and observe focus styling. Measure contrast if necessary.

The expected outcome is that each accordion control displays a clearly visible focus indicator with sufficient contrast against the background.

#### Test ACC-04 — Voice Control Operation

The objective of this test is to confirm that voice control users can operate accordion sections by visible label.

Enable voice control software and issue commands using the visible label text of each accordion control.

The expected outcome is that each section expands or collapses correctly when referenced by its visible label.

#### Test ACC-05 — Reduced Motion Compliance

The objective of this test is to ensure that opening and closing accordion panels respects reduced motion settings.

Enable reduced motion in the device or browser settings, then expand and collapse panels.

The expected outcome is that animations are reduced or removed appropriately.

#### Test ACC-06 — Content Scaling at 200%

The objective of this test is to ensure that the accordion remains usable when text is enlarged.

Increase text size or zoom to 200% and inspect the accordion.

The expected outcome is that content remains visible and functional, without clipping, overlap, or loss of control usability.

#### Test ACC-07 — JavaScript Independence

The objective of this test is to verify that content remains available when JavaScript is disabled.

Disable JavaScript, reload the page, and inspect the accordion content.

The expected outcome is that all content remains accessible or that a suitable non-interactive fallback is provided.

---

### Pattern: Modal Dialog

#### Test MODAL-01 — Hidden Until Opened

The objective of this test is to confirm that the dialog is not available to keyboard or assistive technology users before opening.

Load the page before opening the dialog and attempt to navigate to dialog content by keyboard and screen reader.

The expected outcome is that the dialog is not reachable before activation.

#### Test MODAL-02 — Focus Transfer and Announcement

The objective of this test is to validate that opening the dialog moves focus into it and announces its role and label.

Open the dialog by mouse or keyboard. Observe focus movement. Use a screen reader if available.

The expected outcome is that focus moves to an appropriate element inside the dialog, the role “dialog” is announced, and the visible dialog label is exposed to assistive technologies.

#### Test MODAL-03 — Background Inertness and Scroll Lock

The objective of this test is to ensure that the underlying page cannot be used while the dialog is open.

Open the dialog and attempt to interact with background controls or scroll the page behind it.

The expected outcome is that the background becomes non-interactive, visually appears non-interactive, and background scrolling is disabled while the dialog is open.

#### Test MODAL-04 — Close Control and Focus Return

The objective of this test is to verify that the dialog provides a visible close mechanism and returns focus on dismissal.

Operate the visible close control or other intended dismissal mechanism.

The expected outcome is that the dialog closes, becomes hidden from assistive technologies, background interaction is restored, and focus returns to the opener.

---

### Pattern: Navigation Menu

#### Test NAV-01 — Toggle and Focus Behaviour

The objective of this test is to confirm that the navigation menu toggles correctly and moves focus appropriately.

Focus the menu control by keyboard. Use Enter or Space to open it. Observe focus movement. Use Escape to close it.

The expected outcome is that the control shows visible focus, Enter or Space toggles the menu, focus moves to the first link when opened if that is the intended interaction model, and Escape closes the menu and returns focus to the trigger.

#### Test NAV-02 — State Announcement

The objective of this test is to ensure that assistive technologies announce menu state correctly.

With a screen reader enabled, focus the menu control and toggle it.

The expected outcome is that the control is announced as a button with its label and expanded or collapsed state. Voice users must also be able to operate it by visible label.

---

### Pattern: Pagination

#### Test PAGE-01 — Landmark and Current Page

The objective of this test is to validate pagination as a labelled navigation region with a programmatically indicated current page.

Locate the pagination component and inspect it by landmark navigation, accessibility tree, or screen reader.

The expected outcome is that pagination is inside a navigation landmark with an accessible label and that the current page is indicated programmatically.

#### Test PAGE-02 — Gap and Target Clarity

The objective of this test is to confirm that omitted page ranges and link targets remain understandable and operable.

Navigate through pagination links with keyboard and inspect any separators or elided ranges.

The expected outcome is that omitted ranges are communicated meaningfully, interactive targets are large enough for touch, and the end of the navigation region is identifiable to assistive technology users.

---

### Pattern: Disclosure

#### Test DISC-01 — Keyboard Toggle and State

The objective of this test is to verify that the disclosure control can be operated by keyboard and that its state is communicated.

Focus the control with Tab and toggle it with Enter or Space. Use a screen reader if possible.

The expected outcome is that the disclosure opens and closes correctly, state changes are announced, and the role is described appropriately.

#### Test DISC-02 — Focus Visibility and Contrast

The objective of this test is to confirm that focus indicators are visible and usable on the disclosure control.

Use Tab to focus the disclosure control and visually assess the focus styling.

The expected outcome is that the focus indicator is clearly visible and has sufficient contrast against the background.

#### Test DISC-03 — High Contrast, Scaling, and No-JS Fallback

The objective of this test is to verify resilience under user preferences and reduced capability conditions.

Enable high contrast or forced-colour mode, then inspect the disclosure control and content. Increase text size to 200%. Disable JavaScript and reload the page.

The expected outcome is that content remains distinguishable and readable in high contrast mode, the control and content remain usable at larger text sizes, and content remains accessible or has a suitable fallback when JavaScript is disabled.

---

### Pattern: Promo

#### Test PROMO-01 — Single Primary Destination

The objective of this test is to ensure that the promo pattern expresses a single primary navigation destination.

Inspect the component structure and identify all interactive elements.

The expected outcome is that the headline link is the primary interactive element, that it is keyboard reachable, and that supporting images do not introduce redundant links. If multiple promos are present, they should be grouped in a list structure. Decorative images must use empty alternative text, while meaningful images must provide appropriate alternative text.

---

### Pattern: Pocket (Expandable Content)

#### Test POCKET-01 — Collapsed Content Behaviour

The objective of this test is to confirm that hidden content is not focusable or exposed before expansion.

Load the component in its collapsed state and navigate by keyboard and assistive technology.

The expected outcome is that hidden content is not reachable by keyboard and is not exposed to assistive technologies while collapsed. A “Show more” control should be present after the preview content.

#### Test POCKET-02 — Expansion, Continuation, and Focus

The objective of this test is to verify the behaviour of expansion and collapse.

Activate the “Show more” control by keyboard, pointer, or touch. Observe where focus moves. Then collapse the content again.

The expected outcome is that hidden content is revealed, the control label changes appropriately, a continuation cue appears between preview and revealed content, focus moves to the continuation cue after expansion, and on collapse focus returns to the toggle button. If enhancement does not run, the full content should remain available.

---

### Pattern: Metadata Strip

#### Test META-01 — List Structure and Icon Semantics

The objective of this test is to confirm that metadata items are grouped and exposed meaningfully.

Inspect the structure of the metadata strip with browser tools or a screen reader.

The expected outcome is that metadata items are presented as a list, icons are not focusable, decorative icons are hidden from assistive technologies, and alternative text or hidden labels are provided where icons carry meaning. Links must remain visually distinguishable beyond colour alone.

---

### Pattern: Information Panel / Pop-up Overlay

#### Test PANEL-01 — Trigger, Focus Transfer, and Return

The objective of this test is to confirm correct focus management for an information panel.

Focus the trigger and open the panel. Observe focus movement. Then dismiss the panel and observe where focus returns.

The expected outcome is that the trigger indicates it controls a popup and exposes expanded or collapsed state, opening moves focus inside the panel to a logical control such as the close button, Escape closes the panel, clicking outside closes the panel where that behaviour is intended, and focus returns to the trigger when the panel closes. The panel should have an accessible title and visible labels that support voice operation.

---

### Pattern: Filter and Sort

#### Test FILTER-01 — Navigation and Stateful Links

The objective of this test is to verify that filter and sort options work as accessible navigation.

Inspect the filter region and use keyboard and screen reader navigation.

The expected outcome is that filters are contained within a navigation region, grouped in a list, represented as links to concrete states, and that the active option is indicated programmatically. Functionality must work without JavaScript.

---

### Pattern: External Links

#### Test EXT-01 — External Destination Warning

The objective of this test is to ensure that users are warned when leaving the current environment.

Inspect the link visually and in the accessibility tree or with a screen reader.

The expected outcome is that external links include a visible icon indicator, a text-based warning available to assistive technologies, and that the icon itself is hidden from assistive technologies and does not receive focus. Lists of external links should use list semantics.

---

### Pattern: Comments

#### Test COMMENTS-01 — Structure, Labels, and Live Feedback

The objective of this test is to validate the accessibility of a comments pattern as a structured interaction area.

Inspect the component and test it by keyboard and, where possible, with a screen reader.

The expected outcome is that the comments section is inside a complementary region, has a heading, presents the comment form before the stream, uses a persistent label for the textarea, associates character counts and validation errors programmatically, structures comments as a list, uses nested lists for replies, exposes reaction button states, and announces status messages through a live region.

---

### Pattern: Video Controls

#### Test VIDEO-01 — Progressive Enhancement of Controls

The objective of this test is to verify that the video starts from a safe and accessible baseline before enhancement.

Load the page with and without scripting where possible.

The expected outcome is that native controls are available before enhancement, that custom controls only replace them after scripting succeeds, and that the video and controls are grouped semantically.

#### Test VIDEO-02 — Toggle Labels and Range Control

The objective of this test is to validate the accessibility of play, mute, and timeline controls.

Focus and operate play, pause, mute, and timeline controls using keyboard and screen reader, and inspect their accessible names.

The expected outcome is that play and mute are native buttons, labels change to reflect current state, icons are hidden from assistive technologies, the timeline is implemented as an accessible range control with a useful label, and keyboard users can scrub via arrow keys. Autoplay should not occur by default, and if present by user choice, obvious controls to pause, stop, or mute must be available immediately.

---

### Pattern: Toggle Button

#### Test TOGGLE-01 — Name, State, and Visibility

The objective of this test is to ensure that a toggle button clearly exposes what it is and what state it is in.

Navigate to the control by Tab, toggle it with Space, and inspect it visually, with a screen reader, and under high contrast if available.

The expected outcome is that the control is keyboard operable, has strong visible focus indication, announces its name and current state, maintains label association at 200% text size, and remains perceivable in forced-colour or high-contrast modes.

---

### Pattern: Theme Switcher

#### Test THEME-01 — Cross-Theme Visibility and Meaning

The objective of this test is to confirm that changing theme does not introduce visibility or meaning failures.

Operate the theme switcher with keyboard, pointer, or touch and inspect the interface in each theme.

The expected outcome is that the switcher is keyboard operable, default theme contrast is sufficient, no information is conveyed by colour alone, and inputs, buttons, scrollbars, focus indicators, icons, and status states remain visible and usable in every theme.

---

### Pattern: Carousel

#### Test CAR-01 — Navigation, Announcements, and Motion Control

The objective of this test is to validate a carousel as an accessible sequence rather than a visually attractive but operationally weak presentation.

Operate next, previous, and pause controls by keyboard, pointer, touch, and voice where possible. Use a screen reader to inspect titles and slide positions.

The expected outcome is that the carousel announces its title, role, and slide position, voice users can operate visible controls by name, reduced-motion preferences are respected, auto-advance can be paused or stopped, progress indicators include text equivalents, content remains usable at 200% text size, and a no-JavaScript fallback keeps all slides or an equivalent alternative available.

---

### Pattern: Multi-Step Dialog Chain

#### Test CHAIN-01 — Sequential Focus and Modal Integrity

The objective of this test is to verify that chained dialogs appear in a clear sequence without leaving multiple simultaneous layers active.

Open the first dialog and progress through the sequence. Observe focus movement on each open and close.

The expected outcome is that only one modal is visible at a time, each hidden dialog is inaccessible until opened, each open dialog blocks the underlying page, each dialog has a visible close control, and focus transitions either to the next dialog or back to the original opener when the sequence ends. Underlying scroll must remain disabled while any modal is open.

---

## Design Practice Test Entries

### Practice: Affordances, Semantics, and Accessibility

#### Test PRACTICE-AFF-01 — Visual and Semantic Alignment

The objective of this test is to ensure that interaction appearance, behaviour, and semantics align.

Inspect interactive elements visually, then validate with keyboard and accessibility tools.

The expected outcome is that native semantic elements are used where possible, links navigate, buttons trigger actions, interactive elements are visually distinguishable from static content, and ARIA roles do not duplicate or contradict native semantics. False, hidden, inconsistent, or hard-to-interpret affordances should not be present.

---

### Practice: Alternative Text

#### Test PRACTICE-ALT-01 — Non-Decorative Image Meaning

The objective of this test is to ensure that non-decorative images expose meaningful alternative text.

Use a screen reader to identify images and hear their alternatives. Inspect `alt` or equivalent labelling where needed.

The expected outcome is that all non-decorative images include alternatives that communicate purpose, meaning, or context, not just literal appearance, and that functional images describe the action they trigger.

#### Test PRACTICE-ALT-02 — Decorative Suppression

The objective of this test is to ensure that decorative images do not create noise.

Identify decorative images and navigate the page with a screen reader.

The expected outcome is that decorative images are ignored by assistive technologies, use empty alternative text where applicable, and do not repeat nearby content.

#### Test PRACTICE-ALT-03 — Disabled Images and High Contrast Readability

The objective of this test is to verify that alternatives remain usable when images are unavailable.

Disable images or use a mode where images are not visible, then inspect the page visually.

The expected outcome is that the replacement text remains visible, has sufficient contrast, and is not clipped or overlapped. Complex graphics should provide summary text and, where required, a route to more detailed information.

---

### Practice: Animation and Motion

#### Test PRACTICE-MOTION-01 — Reduced Motion Response

The objective of this test is to verify that the interface responds to reduced motion preferences.

Enable reduced motion in the operating system or browser and reload the interface.

The expected outcome is that animation is removed, reduced, or slowed where appropriate, and that any meaning-dependent motion is gated, controllable, or replaced by a safer alternative. Animations longer than five seconds must be pausable or stoppable, and auto-playing sounds longer than three seconds must be controllable. Flashing content must be warned or gated appropriately.

---

### Practice: ARIA

#### Test PRACTICE-ARIA-01 — Validity and Behavioural Match

The objective of this test is to ensure that ARIA is used only where needed and behaves consistently with what it implies to users.

Inspect elements using ARIA roles, states, and properties. Compare accessible output with actual interaction behaviour.

The expected outcome is that ARIA attributes are valid and lowercase, ID references resolve to existing elements, screen reader output matches intended role, name, and state, and required ARIA attributes are present where needed. ARIA must not be used to create misleading expectations without the corresponding behaviour being implemented.

---

### Practice: Colour and Meaning

#### Test PRACTICE-COLOUR-01 — Meaning Survives Without Colour

The objective of this test is to ensure that colour is never the only conveyor of meaning.

View the interface in greyscale or by ignoring colour cues. Inspect errors, status indicators, and state communication.

The expected outcome is that meaning is preserved without colour, error states include text as well as colour, and high-contrast mode retains clear meaning.

---

### Practice: Colour Contrast

#### Test PRACTICE-CONTRAST-01 — Foreground and Interface Contrast

The objective of this test is to verify sufficient contrast for both text and interface components.

Use a contrast tool or design inspection to measure text and key control contrast.

The expected outcome is that body text meets the documented contrast expectation, interface components meet the required threshold, and the content remains legible under blurred-vision simulation or equivalent practical inspection. Contrast must also be evaluated in context, including different themes and states.

---

### Practice: Typography and Readability

#### Test PRACTICE-TYPE-01 — Font Suitability

The objective of this test is to ensure that font choice supports reading rather than undermining it.

Review the chosen typeface and test with representative users where possible.

The expected outcome is that the font has clear letterform differentiation, open counters, and strong readability characteristics, and that it performs acceptably in measures such as reading speed, error rate, and comprehension. Decorative or highly stylised fonts should not be relied on for body copy or key interactions.

#### Test PRACTICE-TYPE-02 — Spacing, Alignment, and Reflow

The objective of this test is to verify that layout adapts to user text adjustments without information loss.

Increase text size and apply spacing overrides approximating documented values for paragraph, line, word, and letter spacing. Inspect line length and paragraph separation.

The expected outcome is that there is no loss of information or functionality, body text remains left-aligned for left-to-right languages, full justification is avoided, line spacing remains readable, paragraph separation is clear, and line length is controlled to support scanning. Hyphenation should not be disabled where it is needed to preserve readability in narrow columns.

---

### Practice: Content Order

#### Test PRACTICE-ORDER-01 — Source Order Integrity

The objective of this test is to verify that source order reflects logical meaning.

Use keyboard navigation and screen reader reading order on layouts that visually reorder content.

The expected outcome is that reading order and tab order follow the logical content flow and that visual reordering does not change meaning or cause confusion.

---

### Practice: Display Modes and Preferences

#### Test PRACTICE-DISPLAY-01 — Preference Mode Support

The objective of this test is to verify support for dark mode, contrast preferences, and forced-colour environments.

Change display preferences at OS or browser level and reload the interface.

The expected outcome is that the site responds appropriately to colour scheme and contrast preferences and remains readable in forced-colour mode.

---

### Practice: Dynamic Content

#### Test PRACTICE-DYNAMIC-01 — Necessary Announcements

The objective of this test is to ensure that dynamic updates are announced when they matter and are not announced when they do not.

Trigger dynamic content changes and observe screen reader output.

The expected outcome is that necessary live regions are present, dynamic updates are announced when relevant, and live regions are not overused for noise or non-essential updates.

---

### Practice: Focus Indication

#### Test PRACTICE-FOCUS-01 — Visibility and Robustness

The objective of this test is to ensure that focus remains visible under normal and adjusted display conditions.

Navigate through interactive elements using keyboard only, then repeat in high contrast mode where possible.

The expected outcome is that focus is clearly visible, outlines are not removed without an accessible replacement, and focus remains visible in High Contrast Mode.

---

### Practice: Forms and Labels

#### Test PRACTICE-FORM-01 — Label Association

The objective of this test is to confirm that every form input has a visible and programmatically associated label.

Inspect forms visually and with assistive technologies.

The expected outcome is that each input has an associated label, required fields are clearly indicated, and labels are announced correctly by screen readers.

#### Test PRACTICE-FORM-02 — Validation and Recovery

The objective of this test is to ensure that errors can be reached, understood, and resolved.

Submit forms with missing or invalid information and inspect the feedback flow.

The expected outcome is that the form can be submitted with errors to trigger feedback, invalid fields are programmatically identified, validation errors are announced clearly, and messages are specific and actionable.

---

### Practice: Headings and Structure

#### Test PRACTICE-HEAD-01 — Heading Integrity

The objective of this test is to validate a meaningful heading structure.

Inspect the heading hierarchy in browser tools or a screen reader heading list.

The expected outcome is that there is a single main heading, heading levels follow a logical progression without inappropriate skipping, and page structure is understandable by scanning headings.

---

### Practice: Hiding Content

#### Test PRACTICE-HIDE-01 — Hidden but Still Available Where Intended

The objective of this test is to ensure that visually hidden content remains available to assistive technologies when that is the intended design, and that hidden elements do not become accidentally focusable.

Inspect visually hidden content and navigate by keyboard and screen reader.

The expected outcome is that content intended for assistive technologies remains available, while hidden elements that should be inactive do not receive focus.

---

### Practice: Icons

#### Test PRACTICE-ICON-01 — Decorative and Functional Distinction

The objective of this test is to ensure icons are treated according to their meaning.

Inspect icons inside links, buttons, and passive content with accessibility tools.

The expected outcome is that decorative icons are hidden from assistive technologies, functional icons have accessible labels or are paired with equivalent text, and icons are not focusable unless they are themselves the interactive control.

---

### Practice: Keyboard Navigation

#### Test PRACTICE-KEY-01 — Full Keyboard Operation

The objective of this test is to ensure that all functionality is operable without a mouse.

Use keyboard only to navigate and operate the interface, including dialogs, menus, forms, and custom controls.

The expected outcome is that all functionality can be completed using keyboard only, tab order is logical and predictable, and Escape closes expandable or dismissible components where that is part of the pattern.

---

### Practice: Landmarks

#### Test PRACTICE-LANDMARK-01 — Landmark Navigation Clarity

The objective of this test is to ensure that page regions are exposed clearly to assistive technologies.

Use a screen reader’s landmark navigation features or inspect region semantics.

The expected outcome is that there is exactly one main landmark where appropriate and that assistive technology users can move between landmarks meaningfully.

---

### Practice: Mobile Accessibility

#### Test PRACTICE-MOBILE-01 — Reflow, Target Size, and Orientation

The objective of this test is to verify usability in mobile and responsive conditions.

Test on a mobile device or responsive emulator. Increase text size where possible. Check portrait and landscape.

The expected outcome is that touch targets are sufficiently large, layout reflows without horizontal scrolling where not essential, and content works in both portrait and landscape orientations.

---

### Practice: Multimodal Interaction

#### Test PRACTICE-MULTI-01 — Equivalent Interaction Paths

The objective of this test is to ensure that functionality does not rely on one form of interaction.

Run the same task using keyboard, touch, voice control, and assistive technology where available.

The expected outcome is that tasks can be completed using multiple interaction modes and that drag interactions or gesture-only behaviours have simpler equivalents such as click or sequential actions.

---

### Practice: Progressive Enhancement and Responsive Design

#### Test PRACTICE-PE-01 — Core Purpose Without Enhancements

The objective of this test is to ensure that the core purpose of a page remains usable with minimal dependencies.

Disable JavaScript where practical, test on more limited devices or browsers where possible, and identify the page’s core purpose before evaluating it.

The expected outcome is that the core content and functionality remain accessible and understandable without JavaScript, that the site works across multiple browsers and devices, and that it does not depend on narrow platform or software assumptions.

---

### Practice: Resize and Zoom

#### Test PRACTICE-ZOOM-01 — 200% Usability

The objective of this test is to ensure that enlargement does not break the interface.

Zoom to 200% or increase text size and inspect key tasks.

The expected outcome is that content remains fully visible, there is no unnecessary horizontal scrolling, and interaction remains functional.

---

### Practice: Client-Side Routing

#### Test PRACTICE-ROUTE-01 — Route Change Communication

The objective of this test is to ensure that single-page application route changes are perceivable and understandable.

Navigate between routes in a client-rendered application.

The expected outcome is that the page title updates, focus resets appropriately, and animated transitions are disabled or reduced when reduced motion is enabled.

---

### Practice: Web Components and Custom Controls

#### Test PRACTICE-COMP-01 — Graceful Degradation and Assistive Use

The objective of this test is to ensure that custom elements do not fail basic accessibility expectations.

Inspect the component with and without JavaScript where possible, and use screen readers and enlarged text.

The expected outcome is that the component supports its core purpose without JavaScript where feasible, remains usable with screen readers, and supports 200% text resizing.

---

### Practice: Caption UX and Safe Zones

#### Test PRACTICE-CAPTION-01 — Caption Placement Safety

The objective of this test is to verify that captions remain readable without obscuring important visual information.

Play captioned content across representative device sizes and aspect ratios.

The expected outcome is that captions do not obscure speakers’ mouths or essential graphics, remain within a safe zone, and are validated with users from the relevant caption-using groups. Success is defined by zero caption obstructions in final content.

---

### Practice: Bi-Media Production and Audio Description

#### Test PRACTICE-BIMEDIA-01 — Scripted Accessibility by Default

The objective of this test is to determine whether audiovisual content is accessible by narrative design before additional access services are layered in.

Review scripts, then watch the final media with and without relying on visuals.

The expected outcome is that the script conveys essential actions, speakers, and context verbally wherever possible, that only residual visual information needs separate audio description, and that the team can measure the percentage of content accessible without additional AD.

---

## Cross-Cutting Interpretation Tests

### Test X-01 — Compliance Versus Accessibility

The objective of this test is to ensure that a technically compliant experience is also usable with equivalent ease.

Run representative journeys with disabled participants or simulated assistive workflows, measure task completion, time, error rate, and satisfaction, and compare results to non-disabled baselines where available.

The expected outcome is that disabled users can complete major flows with comparable ease, and any gap is treated as an accessibility defect even where standards conformance appears to be met.

### Test X-02 — Pattern Innovation Against Convention

The objective of this test is to ensure that unconventional patterns do not increase cognitive load or exclusion.

Compare the new pattern to a conventional alternative in usability testing, particularly with users who experience cognitive barriers.

The expected outcome is that the unconventional pattern performs at least as well as the conventional one in task completion, error rate, and effort. If it performs worse, it should not be adopted.

### Test X-03 — Continuous Improvement Signal

The objective of this test is to verify that testing contributes to improvement over time rather than one-off reporting.

Review historical test outputs, issue trends, support contacts, and satisfaction data.

The expected outcome is that results can be compared before and after changes, recurrent issues are visible, and prioritisation decisions are linked to evidence. Accessibility should be continuously measured and improved, not treated as a one-time pass or fail exercise.

---

## How to Extend This Test System

When a new pattern is introduced, the same ACT-style structure should be used. Start by defining the pattern’s purpose, semantic intent, and interaction model. Then write tests that validate keyboard behaviour, assistive technology exposure, visible and non-visible state, responsiveness, fallback behaviour, and where relevant voice interaction and reduced motion support. If the pattern is intended to scale across teams, it should also be added to the design system with pre-written automated checks and pre-written manual scenarios.

For new design practices, create measurable yes or no tests where possible, and supplement them with practice notes explaining why the test exists and what kinds of user barriers it is trying to detect. This prevents the system becoming a compliance-only checklist and keeps it aligned with the broader goal of equivalent user experience.

---

## Closing Principle

A structured ACT-style test system is valuable because it turns accessibility from a loosely interpreted aspiration into a repeatable quality discipline. When every pattern and design practice has a clear objective, a defined way to test it, and an explicit expected outcome, teams can evaluate accessibility more consistently, prevent regressions earlier, and generate evidence that is useful for design, release, procurement, risk management, and continuous improvement.

The system becomes strongest when it combines standards-based checks with assistive technology validation, disabled user evidence, and robust regression practice. At that point, accessibility testing becomes not a separate activity performed only at the end, but a stable part of how quality is defined and maintained.
