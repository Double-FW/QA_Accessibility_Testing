# Scope a service and create defensible test scripts

## 1. Establish the service facts

Record the actual service, its operator and suppliers, purpose, customer groups, countries served, sector, public/private status, consumer/workplace context, product categories, delivery channels and procurement terms. Include websites, apps, terminals, documents, communications, authentication, payment, support and third-party handoffs where part of the outcome. Identify essential tasks, failure/recovery routes and deadlines.

Declare technical and organisational baselines separately. This repository's active WCAG mapping is WCAG 2.2 A/AA; a law or contract may cite another edition or additional requirements. Do not rewrite the canonical register to pretend these editions are identical.

## 2. Build an obligation register

Start with the [Double-FW global regulatory overview](https://github.com/Double-FW/Global_Accessiblity_Regulatory_Requirements/blob/main/Global_Website_Accessibility_Regulatory_Overviews.md). It currently covers WAD, EAA, UK public-sector regulations, the Equality Act, Section 508, ADA Titles II and III, Canada's federal framework, Ontario AODA, France/RGAA, Australia, New Zealand, Israel, South Korea, Brazil and South Africa. Use its current contents to discover other relevant frameworks; do not assume every entry applies.

Verify applicable law, national implementation, regulator guidance, dates and standards citations using primary sources. Record:

| Field | Required content |
| --- | --- |
| Obligation ID | Stable local identifier, exact instrument and provision |
| Applicability | Country, operator/service/category, affected function, commencement and transition |
| Decision | Applies / does not apply with reason / unresolved; named legal or compliance reviewer |
| Requirement type | Technical, functional, equality/adjustment, information, process or reporting |
| Baseline | Exact standard/edition, incorporated clauses, exceptions and citation status |
| Evidence and output | Required evidence, reporting format, recipient, deadline and owner |
| Source | Official URL, version/date, access date and next review trigger |

Unresolved applicability creates a review action, not an exemption. Multiple laws may apply to the same task. Maintain separate obligation records and share evidence only when its scope supports each claim. An organisational exception does not waive a legal duty.

## 3. Map requirements and coverage

Create this chain: obligation → service requirement → journey/state → canonical test reference → local procedure → execution → finding → issue → verification → report claim.

Use the [Canonical Test Library](<../Canonical Test Library.md>) for outcomes, the [WCAG relationship register](../Canonical_WCAG_AA_Relationship_Register.md) for supported WCAG 2.2 A/AA relationships, and the [detailed procedures](../Mobile_Application_and_Website_Test_Library.md) and [ACT-style system](../Accessibility_ACT-Style_Test_System.md) for procedure design. Preserve source file, ID, title and revision. AXE IDs, CTL IDs and local executable IDs occupy separate fields.

Some obligations concern terminal hardware, support, communications, governance or legal information beyond these web/mobile libraries. Create a clearly identified local supplementary test and obtain relevant expertise. Never invent a canonical ID or imply WCAG covers an unmapped obligation.

The coverage matrix should contain obligation and requirement IDs; journey/component/state; source test reference and relationship (full, partial, supporting or gap); method; environments; expected evidence; selected/excluded rationale; executor; execution status; and evidence gaps. A sampled state does not prove all instances. Include representative shared templates, content types and configurations plus high-risk outliers.

## 4. Tailor each script

Use this copyable template. Blank fields are planning gaps, not completed checks.

| Script field | Content to supply |
| --- | --- |
| Identity | Local TEST ID, revision, requirement IDs, source library/ID/title/revision |
| Service scope | Journey, task goal, build, channel, component, initial and transition states |
| User/context | Functional lenses, intersections, input/AT/settings, relevant environment |
| Preconditions | Safe test account/data, access, device/OS/browser/AT versions, permissions |
| Procedure | Numbered reproducible actions including success, errors, recovery and confirmation |
| Expected result | Observable behaviour, correct end state, assistance/privacy conditions, criterion basis |
| Method | Automated, manual, AT-assisted, user research or process/document review; limitations |
| Evidence | Required record, protected storage reference, collection authority and retention |
| Execution | EXEC ID, tester/date, observed result, evidence references and result status |
| Follow-up | Impact, issue reference, proposed fix, verification conditions and reviewer |

Use the governed statuses: `pass`, `fail`, `blocked`, `cannot_tell`, `not_tested`, `not_applicable` (with reason), `tool_error`. Research findings and legal conclusions use separate fields. No script should force an automated assertion where no reliable one exists; document the manual or research route and gap.

## 5. Example: illustrative colour-independent error test

For a fictional checkout, connect local TEST-CHECKOUT-01 to Canonical Test Library entry 2, “Error States Not Conveyed by Colour Alone”, with its source revision. Retrieve the current relationship register before asserting a WCAG relationship.

Precondition: an approved test build and synthetic order; required address blank. Steps: reach checkout, submit, inspect the error visually and using relevant AT, correct the address, resubmit and verify the order's intended end state. Expected: errors have understandable non-colour identification; separately selected focus, announcement and recovery tests cover those behaviours. Record actual environments and observations when executed. This is a draft example, with status `not_tested`; it reports no real service result.

## 6. Assemble the evidence pack

Include signed-off scope, obligation register, coverage matrix, versioned scripts, actual executions, limitations, findings, linked backlog, retests, customer research and authorised decisions. For each proposed public/regulatory statement, identify the supporting evidence and what it cannot establish. Select the jurisdiction-specific reporting format from [the sources guide](Sources_and_Legal_Boundaries.md).
