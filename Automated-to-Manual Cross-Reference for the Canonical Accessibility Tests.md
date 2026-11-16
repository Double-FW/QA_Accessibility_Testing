# Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests

## Purpose

This document cross-references the 200 canonical tests against the repository-visible scope of four automated testing tools:

1. IBM Equal Access Accessibility Checker
2. Alfa by Siteimprove
3. QualWeb
4. AccessLint

The document is designed for LLM retrieval, policy reasoning, audit planning, and human QA orchestration.

## Evidence status — reviewed 16 November 2026

This is a planning matrix, not a validated tool-capability inventory or execution record. The earlier D/P ratings inferred direct or partial coverage from general project descriptions. They did not provide a rule ID, pinned tool/ruleset version, applicability, assertion boundary or validation evidence for each mapping. Those positive ratings are now marked U. Cross-tool duplication is also unverified. This correction does not establish that a tool lacks a capability.

## Coverage vocabulary

- `U` = unverified candidate mapping. Do not count it as implemented, direct or partial coverage. Establish an evidence-backed mapping before selecting a tool on this basis.
- `N` = no reliable automation was evidenced in the source material used for this matrix. This is a limitation of available evidence, not proof that automation is impossible or absent from current tools.
- `unverified` in the duplication column = no validated cross-tool equivalence/overlap record. Do not use it to add coverage percentages or deduplicate findings automatically.

These are mapping states, not test-result statuses. The canonical 200 test IDs and titles are preserved. Manual complements are planning prompts and must be made specific to the product, state and task.

## Qualifying a mapping

Before classifying any tool relationship as direct or partial, record: canonical source/revision and exact ID/title; tool, package and ruleset version; exact rule/assertion ID; official source URL and revision; supported platform and applicability; inspected states and configuration; which part of the outcome is asserted; known exclusions; a reproducible validation fixture or execution reference; reviewer/date; and required manual or research complement. Record a subset assertion as partial support, not whole-outcome coverage.

Broad vendor claims or a check with a similar name do not establish coverage of focus contrast, complete resize/reflow behaviour, absence of functional loss, content meaning, task completion or satisfaction. Preserve the full canonical outcome and evaluate the remaining parts separately.

Select tools according to evidenced coverage, implementation effort and the actual service. There is no repository requirement to run all four tools or a preferred combination without that evaluation. Use the same evidence requirements when refreshing IBM Equal Access, Alfa, QualWeb or AccessLint mappings. Relate repeat findings through a reviewed root-cause record rather than rule-name similarity alone.

For actual execution and uncertainty use the [delivery framework](Accessibility_Test_Led_Delivery_Framework.md) and [AGENTS.md](AGENTS.md). A scan, mapping state or manual-plan entry cannot be converted to a product pass.

## A. Perception, presentation, and sensory independence

| ID | Canonical test name | IBM Equal Access | Alfa | QualWeb | AccessLint | Cross-tool duplication evidence | Manual complement |
|---:|---|:---:|:---:|:---:|:---:|:---:|---|
| 1 | Information Not Conveyed by Colour Alone | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 2 | Error States Not Conveyed by Colour Alone | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 3 | Required States Not Conveyed by Colour Alone | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 4 | Selection State Not Conveyed by Colour Alone | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 5 | Focus State Not Conveyed by Colour Alone | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 6 | Link Identification Not Conveyed by Colour Alone | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 7 | Data Series Not Differentiated Only by Colour | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 8 | Text Contrast Minimum | U | U | U | U | unverified | Manual confirms content quality, UX suitability, and cross-state behaviour |
| 9 | Large Text Contrast Minimum | U | U | U | U | unverified | Manual confirms content quality, UX suitability, and cross-state behaviour |
| 10 | Focus Indicator Contrast | U | U | U | U | unverified | Manual confirms content quality, UX suitability, and cross-state behaviour |
| 11 | Control Boundary Contrast | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 12 | Placeholder Contrast Adequacy | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 13 | Legibility Under Blur or Reduced Clarity | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 14 | Text Resizes to 200 Percent | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 15 | Text Resizes Beyond 200 Percent Where Supported | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 16 | Layout Reflows Without Horizontal Dependency | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 17 | No Text Clipping on Resize | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 18 | No Functional Loss on Resize | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 19 | Text Spacing Override Support | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 20 | Zoom Capability Preserved | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 21 | Content Usable Under Magnification | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 22 | Motion Respects Reduced Motion Preference | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 23 | Auto-Moving Content Can Be Paused | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 24 | Auto-Moving Content Can Be Stopped or Hidden | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 25 | Decorative Animation Time-Limited | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 26 | Flashing Content Frequency Safety | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 27 | Flickering Content Warning and Alternative | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 28 | Autoplay Audio Control | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 29 | Autoplay Video Control | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 30 | Media Does Not Mask Assistive Technology Audio | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 31 | Separate Audio Streams Adjustable | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 32 | Notification Sound Supplemented by Another Modality | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 33 | Decorative Images Ignored by Assistive Technology | U | U | U | U | unverified | Manual confirms content quality, UX suitability, and cross-state behaviour |
| 34 | Informative Images Have Equivalent Text | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 35 | Functional Images Describe Action | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 36 | Complex Visuals Have Summary | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 37 | Images of Text Avoided | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 38 | Background Images with Meaning Have Equivalent Content | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 39 | Visible Rating or Graphic Indicators Have Text Equivalent | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 40 | Supplementary Visual Cues Do Not Replace Meaningful Text | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |

## B. Structure, semantics, and document relationships

| ID | Canonical test name | IBM Equal Access | Alfa | QualWeb | AccessLint | Cross-tool duplication evidence | Manual complement |
|---:|---|:---:|:---:|:---:|:---:|:---:|---|
| 41 | Primary Page Language Declared | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 42 | Inline Language Changes Marked | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 43 | Language Direction Specified When Needed | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 44 | Page Title Present | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 45 | Page Title Describes Primary Content | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 46 | Page Title Is Unique Within Context | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 47 | SPA Title Updates on Route Change | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 48 | One Main Landmark Per Page | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 49 | Major Regions Use Appropriate Landmarks | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 50 | Landmark Labels Distinguish Similar Regions | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 51 | Content Belongs to Defined Regions | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 52 | Skip Link or Equivalent Bypass Present | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 53 | Skip Link Focuses Main Content Reliably | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 54 | Heading Structure Present | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 55 | One Primary Heading Per Page Context | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 56 | Heading Levels Follow Logical Hierarchy | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 57 | Heading Text Is Descriptive | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 58 | Visual Headings Match Semantic Headings | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 59 | Headings Are Visually Distinguishable | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 60 | Source Order Matches Intended Reading Order | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 61 | Tab Order Aligns With Logical Structure | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 62 | CSS Reordering Does Not Break Meaning | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 63 | Related Thematic Items Use List Semantics | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 64 | Arbitrary Layout Containers Avoid False Semantics | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 65 | Tables Used Only for Tabular Data | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 66 | Data Tables Include Header Cells | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 67 | Data Table Header Scope Defined | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 68 | Data Tables Include Caption | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 69 | Table Remains Structurally Intact on Small Screens | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 70 | Scrollable Table Container Is Accessible | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |

## C. Naming, labelling, and descriptive clarity

| ID | Canonical test name | IBM Equal Access | Alfa | QualWeb | AccessLint | Cross-tool duplication evidence | Manual complement |
|---:|---|:---:|:---:|:---:|:---:|:---:|---|
| 71 | Interactive Elements Have Accessible Names | U | U | U | U | unverified | Manual confirms content quality, UX suitability, and cross-state behaviour |
| 72 | Visible Labels Exist for Form Inputs | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 73 | Accessible Name Matches Visible Label | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 74 | Label Is Near the Control It Describes | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 75 | Label Remains Available During Input | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 76 | Placeholder Does Not Replace Label | U | U | U | U | unverified | Manual confirms content quality, UX suitability, and cross-state behaviour |
| 77 | Title Attribute Not Used as Primary Label | U | U | U | U | unverified | Manual confirms content quality, UX suitability, and cross-state behaviour |
| 78 | Instructions Associated With Relevant Field | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 79 | Error Messages Associated With Relevant Field | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 80 | Group Labels for Related Controls | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 81 | Control Text Describes Purpose | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 82 | Icon-Only Controls Have Equivalent Text | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 83 | Supplementary Help Does Not Duplicate Primary Name | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 84 | External Navigation Warns of Context Change | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 85 | New Window or New Tab Behaviour Disclosed | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 86 | Breadcrumb Current Item Labelled Correctly | U | U | U | U | unverified | Manual confirms content quality, UX suitability, and cross-state behaviour |
| 87 | Current Navigation Item Exposed | U | U | U | U | unverified | Manual confirms content quality, UX suitability, and cross-state behaviour |
| 88 | Metadata Values Clarified Non-Visually | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 89 | Breakout and Complementary Sections Uniquely Labelled | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 90 | Comments, Panels, and Supplemental Regions Clearly Named | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |

## D. Keyboard, focus, and input modality

| ID | Canonical test name | IBM Equal Access | Alfa | QualWeb | AccessLint | Cross-tool duplication evidence | Manual complement |
|---:|---|:---:|:---:|:---:|:---:|:---:|---|
| 91 | All Interactive Elements Reachable by Keyboard | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 92 | All Interactive Elements Operable by Keyboard | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 93 | Standard Keyboard Activation Preserved | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 94 | No Keyboard Trap | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 95 | Focus Indicator Always Visible | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 96 | Focus Indicator Not Suppressed Without Equivalent | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 97 | Focus Order Logical Through Forms | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 98 | Focus Order Logical Through Navigation | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 99 | Focus Does Not Move Unexpectedly During Input | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 100 | Focus Moves to New Context on Open | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 101 | Focus Returns on Close | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 102 | Programmatic Focus Uses Appropriate Targets | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 103 | Hidden Focusable Elements Revealed on Focus | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 104 | Positive Tabindex Avoided | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 105 | Tabindex Zero Used Only on Intended Interactive Targets | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 106 | Tabindex Minus One Used for Programmatic Focus Only | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 107 | Alternative Input Method Support | U | U | U | N | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 108 | Gesture Functions Have Non-Gesture Alternatives | U | U | U | N | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 109 | Pointer Precision Not Required for Basic Tasks | U | U | U | N | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 110 | Target Size Meets Minimum Usability Threshold | U | U | U | N | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |

## E. Forms, input, and validation

| ID | Canonical test name | IBM Equal Access | Alfa | QualWeb | AccessLint | Cross-tool duplication evidence | Manual complement |
|---:|---|:---:|:---:|:---:|:---:|:---:|---|
| 111 | Explicit Submit Control Present | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 112 | Submission Occurs Only on Explicit Action | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 113 | Required Fields Indicated Programmatically | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 114 | Required Fields Indicated Visually | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 115 | Optional Fields Marked Where Pattern Requires | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 116 | Input Format Expectations Communicated | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 117 | Appropriate Input Type Used | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 118 | Autocomplete Used for Personal Data Where Appropriate | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 119 | Related Inputs Grouped Semantically | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 120 | Radio Groups Operate as One Logical Question | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 121 | Checkbox Sets Grouped Where They Share a Question | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 122 | Error Messages Shown When Submission Fails | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 123 | Error Messages Are Announced to Assistive Technology | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 124 | Error Message Identifies the Relevant Field | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 125 | Error Message Explains the Problem | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 126 | Error Message Tells User How to Fix It | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 127 | Error Summary Provided for Multiple Errors | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 128 | Error Summary Supports Navigation to Fields | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 129 | User Input Preserved After Validation Failure | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 130 | Validation Does Not Interrupt Every Keystroke Inappropriately | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 131 | Error Cues Persist Long Enough to Be Used | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 132 | Reset Buttons Avoided or Safe | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 133 | Form Completion Possible by Keyboard Only | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 134 | Password and Complex Input Assistance Available | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 135 | Submit Controls Not Inaccessibly Disabled | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |

## F. Links, navigation systems, and routing

| ID | Canonical test name | IBM Equal Access | Alfa | QualWeb | AccessLint | Cross-tool duplication evidence | Manual complement |
|---:|---|:---:|:---:|:---:|:---:|:---:|---|
| 136 | Link Purpose Understandable in Isolation | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 137 | Repeated Link Text Distinguishable Where Destinations Differ | U | U | U | U | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 138 | Adjacent Duplicate Links Consolidated | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 139 | External Link Warning Included | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 140 | Download or Alternate Format Links Identified | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 141 | Breadcrumbs Structured as Navigation List | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 142 | Breadcrumb Current Page Is Not an Active Link | U | U | U | N | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 143 | Navigation Menus Use Correct Structural Semantics | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 144 | Current Navigation State Programmatically Exposed | U | U | U | U | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 145 | Search Region Identifiable | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 146 | Search Suggestions Announced Accessibly | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 147 | Share and Auxiliary Tool Clarity | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 148 | SPA Route Changes Update Focus Position | U | U | U | N | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 149 | SPA Route Changes Update History | U | U | U | N | unverified | Manual confirms structural meaning, orientation, and navigation outcome |
| 150 | Route Change Loading State Communicated | U | U | U | N | unverified | Manual confirms structural meaning, orientation, and navigation outcome |

## G. Dynamic content, notifications, and state change

| ID | Canonical test name | IBM Equal Access | Alfa | QualWeb | AccessLint | Cross-tool duplication evidence | Manual complement |
|---:|---|:---:|:---:|:---:|:---:|:---:|---|
| 151 | Status Messages Announced Without Forced Focus Change | U | U | U | U | unverified | Manual confirms content quality, UX suitability, and cross-state behaviour |
| 152 | Critical Alerts Perceivable in Multiple Modalities | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 153 | Notifications Not Overbearing | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 154 | Standard OS or Platform Notifications Used When Appropriate | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 155 | Dynamic Content Discoverable After Update | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 156 | Focus Not Stolen by Non-Critical Updates | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 157 | State Changes Reflected Programmatically | U | U | U | U | unverified | Manual confirms content quality, UX suitability, and cross-state behaviour |
| 158 | State Change Announced When It Matters | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 159 | Live Regions Used Appropriately | U | U | U | U | unverified | Manual confirms content quality, UX suitability, and cross-state behaviour |
| 160 | Update Timing Allows Perception | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |

## H. Components: disclosure, overlays, and grouped interaction

| ID | Canonical test name | IBM Equal Access | Alfa | QualWeb | AccessLint | Cross-tool duplication evidence | Manual complement |
|---:|---|:---:|:---:|:---:|:---:|:---:|---|
| 161 | Disclosure Controls Expose Expanded State | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 162 | Disclosure Controls and Content Linked | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 163 | Collapsed Disclosure Content Removed Accessibly | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 164 | Revealed Content Follows Control Logically | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 165 | Accordion Items Use Heading + Button Pattern | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 166 | Single-Select Accordions Enforce One Open Item | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 167 | Tabs Use Correct Roles When Enhanced | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 168 | Tabs Preserve Non-JavaScript Access | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 169 | Only Active Tab Panel Exposed | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 170 | Information Panels Open and Close Predictably | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 171 | Information Panels Not Used for Essential-Only Content | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 172 | Modal Dialog Announces Identity and Modality | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 173 | Modal Dialog Blocks Background Interaction | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 174 | Modal Dialog Has Accessible Close Method | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 175 | Modal Dialog Content Fits or Scrolls | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 176 | Action Dialog Uses Buttons vs Links Appropriately | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 177 | Mega Menu Trigger Uses Button Semantics | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 178 | Mega Menu Closes on Escape, Blur, or Outside Click | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 179 | Carousel Is Entirely User Driven | U | U | U | N | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 180 | Carousel Hidden or Faint Items Not Presented as Fully Available | U | U | U | N | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |

## I. Media, promos, cards, comments, and rich content patterns

| ID | Canonical test name | IBM Equal Access | Alfa | QualWeb | AccessLint | Cross-tool duplication evidence | Manual complement |
|---:|---|:---:|:---:|:---:|:---:|:---:|---|
| 181 | Native Media Controls or Accessible Equivalent Present | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 182 | Media Does Not Autoplay Unexpectedly | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 183 | Captions Available for Spoken Video | U | U | U | U | unverified | Manual confirms real user perceptibility, control usability, and behavioural safety |
| 184 | Audio Description or Equivalent for Essential Visual Information | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 185 | Promo Has One Clear Primary Action | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 186 | Promo Headline Consistent With Destination | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 187 | Promo Media Indicators Explained Non-Visually | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 188 | Card Collections Use List Structure | U | U | U | U | unverified | Manual confirms content quality, UX suitability, and cross-state behaviour |
| 189 | Card Headline Comes First in Source Order | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 190 | Card Expandable Regions Follow Toggle State | U | U | U | U | unverified | Manual confirms content quality, UX suitability, and cross-state behaviour |
| 191 | Comment Stream Uses Nested Structure for Replies | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 192 | Comment Submission Feedback Accessible | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 193 | Comment Controls Clearly Labelled | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 194 | Character Limits Communicated During Comment Entry | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 195 | Rating Displays Express Value in Text | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 196 | Interactive Ratings Use Semantic Form Controls | U | U | U | U | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |

## J. Time, persistence, and system behaviour

| ID | Canonical test name | IBM Equal Access | Alfa | QualWeb | AccessLint | Cross-tool duplication evidence | Manual complement |
|---:|---|:---:|:---:|:---:|:---:|:---:|---|
| 197 | Time Limits Can Be Extended, Disabled, or Adjusted | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 198 | Timeout Warning Issued Before Expiry | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
| 199 | Timeout Consequences Communicated | U | U | U | N | unverified | Manual confirms semantic correctness, wording quality, and task-level appropriateness |
| 200 | Unexpected Context Changes Prevented | U | U | U | N | unverified | Manual confirms full interaction flow, focus lifecycle, and recovery behaviour |
