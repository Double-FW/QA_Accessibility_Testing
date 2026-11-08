---
title: "QA Accessibility Testing"
description: "Governed accessibility test-management system for web, mobile, design systems, and digital services."
repository: "Double-FW/QA_Accessibility_Testing"
repository_url: "https://github.com/Double-FW/QA_Accessibility_Testing"
version: "1.1"
status: "active"
schema_version: "1.0"
primary_use_cases:
  - "test planning"
  - "accessibility QA"
  - "WCAG mapping"
  - "automation-to-manual crosswalk"
  - "remediation brief generation"
  - "evidence and release governance"
authority_boundary:
  - "This repository provides a governed evidence model, not legal conformance interpretation."
  - "Use authoritative source files for testing and mapping decisions."
  - "Generated summaries and automation mappings are derived views."
---

# QA Accessibility Testing

This repository is a governed accessibility evidence and testing system for websites, web applications, mobile applications, design systems, components, and digital services.

It supports:
- canonical accessibility outcome testing
- WCAG 2.2 A/AA traceability
- layered QA workflows
- automation-to-manual crosswalks
- remediation prompt generation
- evidence-based release and governance decisions

This repository is not a legal conformance engine, and it does not replace authorised governance for legal interpretation, procurement sign-off, or regulatory claims.

---

## 1. Repository purpose

Use this repository to:
- identify the right accessibility tests for a product, journey, component, or design pattern
- differentiate conformance evidence from usability and quality evidence
- map tests to WCAG outcomes
- identify where automation is direct, partial, or manual-primary
- generate remediation briefs for human review
- maintain evidence, exceptions, and decision traceability

The repository must be used as a connected evidence system rather than as a collection of independent checklists.

---

## 2. What this repository is not

This repository is not:
- a legal or regulatory interpretation body
- a replacement for official WCAG or EN 301 549 interpretation
- a source of definitive claims that a product is accessible
- a replacement for human judgement in remediation, release, or exception decisions
- a set of AXE findings to be treated as canonical test results

---

## 3. Authority model

The repository contains multiple layers. Each layer has a different purpose and different authority.

```yaml
authority_layers:
  governance:
    file: "Accessibility_Test_Led_Delivery_Framework.md"
    role: "primary policy and evidence governance"
    authority_level: "authoritative-source"
  canonical_tests:
    file: "Canonical Test Library.md"
    role: "primary user-outcome test library"
    authority_level: "authoritative-source"
  wcag_mapping:
    file: "Canonical_WCAG_AA_Relationship_Register.md"
    role: "canonical WCAG relationship register"
    authority_level: "authoritative-source"
  generated_wcag_summary:
    file: "Canonical_Test_Library_WCAG_AA_Summary.md"
    role: "derived summary view of WCAG mappings"
    authority_level: "derived-view"
  detailed_procedures:
    file: "Mobile_Application_and_Website_Test_Library.md"
    role: "detailed procedures for testing"
    authority_level: "authoritative-source"
  act_style:
    file: "Accessibility_ACT-Style_Test_System.md"
    role: "pattern and design-practice validation system"
    authority_level: "authoritative-source"
  axe_rules:
    file: "AXE_Test_AA_Rule_Descriptions.md"
    role: "automation rule metadata and mapping data"
    authority_level: "automation-reference"
  axe_alignment:
    file: "AXE_and _Test_Inventory_Alignment.md"
    role: "automation-to-test and manual-complement mapping"
    authority_level: "automation-mapping"
  remediation_prompts:
    file: "AXE_Test_Remediation_Prompt_Library.md"
    role: "candidate fix prompts for review"
    authority_level: "remediation-prompt"
  design_system_mapping:
    file: "AXE → Design Tokens → Components.md"
    role: "component and token dependency hypothesis"
    authority_level: "design-system-hypothesis"
```

Important rules:
- Canonical tests are the primary source for user outcomes.
- AXE rules are not canonical tests.
- Generated summaries are derived views, not independent authorities.
- Best-practice guidance is important but not equivalent to WCAG A/AA criteria.
- Design-token and component mappings are hypotheses unless validated in context.

---

## 4. Resource catalog

```yaml
resources:
  - file: "README.md"
    resource_type: "index"
    authority_level: "governance"
    purpose: "Repository overview, authority model, and safe-use guidance."
    machine_readable: true

  - file: "AGENTS.md"
    resource_type: "operating_guidance"
    authority_level: "governance"
    purpose: "Operational rules for autonomous or LLM-based repository management."
    machine_readable: true

  - file: "Accessibility_Test_Led_Delivery_Framework.md"
    resource_type: "framework"
    authority_level: "authoritative-source"
    purpose: "Lifecycle, policy, governance, evidence, and release handling."
    machine_readable: true

  - file: "Testing_Approach.md"
    resource_type: "methodology"
    authority_level: "authoritative-source"
    purpose: "Accessibility management model, layered testing, conformance vs usability."
    machine_readable: true

  - file: "Canonical Test Library.md"
    resource_type: "canonical_tests"
    authority_level: "authoritative-source"
    purpose: "Stable outcome-based accessibility tests."
    machine_readable: true

  - file: "Canonical_WCAG_AA_Relationship_Register.md"
    resource_type: "standards_mapping"
    authority_level: "authoritative-source"
    purpose: "Normalized WCAG 2.2 A/AA relationship register."
    machine_readable: true

  - file: "Canonical_Test_Library_WCAG_AA_Summary.md"
    resource_type: "derived_summary"
    authority_level: "derived-view"
    purpose: "Generated summary of canonical test to WCAG A/AA relationships."
    machine_readable: true

  - file: "Canonical Test Library Alignment to Exact WCAG SC IDs.md"
    resource_type: "historical_reference"
    authority_level: "historical"
    purpose: "Superseded exact mapping retained for traceability; not the active source."
    machine_readable: true

  - file: "Mobile_Application_and_Website_Test_Library.md"
    resource_type: "detailed_tests"
    authority_level: "authoritative-source"
    purpose: "Detailed mobile and web accessibility procedures and checks."
    machine_readable: true

  - file: "Accessibility_ACT-Style_Test_System.md"
    resource_type: "pattern_library"
    authority_level: "authoritative-source"
    purpose: "Pattern, design-practice, and procedural ACT-style checks."
    machine_readable: true

  - file: "Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests.md"
    resource_type: "automation_mapping"
    authority_level: "automation-mapping"
    purpose: "Maps automation to manual complement requirements."
    machine_readable: true

  - file: "AXE_Test_AA_Rule_Descriptions.md"
    resource_type: "automation_reference"
    authority_level: "automation-reference"
    purpose: "AXE rule descriptions and associated WCAG metadata."
    machine_readable: true

  - file: "AXE_and _Test_Inventory_Alignment.md"
    resource_type: "automation_mapping"
    authority_level: "automation-mapping"
    purpose: "Maps AXE rules to canonical test areas and manual evidence requirements."
    machine_readable: true

  - file: "AXE_Test_Remediation_Prompt_Library.md"
    resource_type: "remediation_prompt_library"
    authority_level: "remediation-prompt"
    purpose: "Candidate prompts for remediation review and human-guided repair."
    machine_readable: true

  - file: "AXE → Design Tokens → Components.md"
    resource_type: "dependency_mapping"
    authority_level: "design-system-hypothesis"
    purpose: "Relates AXE findings to design-token and component dependencies."
    machine_readable: true
```

---

## 5. Use-by-task routing

```yaml
task_routing:
  - task: "governance_or_policy"
    read_first:
      - "Accessibility_Test_Led_Delivery_Framework.md"
      - "Testing_Approach.md"
      - "AGENTS.md"
    read_next:
      - "README.md"

  - task: "select_canonical_tests"
    read_first:
      - "Canonical Test Library.md"
    read_next:
      - "Canonical_WCAG_AA_Relationship_Register.md"

  - task: "map_to_wcag"
    read_first:
      - "Canonical_WCAG_AA_Relationship_Register.md"
    read_next:
      - "Canonical_Test_Library_WCAG_AA_Summary.md"

  - task: "detailed_procedure_or_pattern"
    read_first:
      - "Mobile_Application_and_Website_Test_Library.md"
      - "Accessibility_ACT-Style_Test_System.md"

  - task: "automation_vs_manual"
    read_first:
      - "Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests.md"
      - "AXE_and _Test_Inventory_Alignment.md"

  - task: "understand_axe_result"
    read_first:
      - "AXE_Test_AA_Rule_Descriptions.md"
    read_next:
      - "AXE_Test_Remediation_Prompt_Library.md"
      - "Canonical Test Library.md"

  - task: "draft_remediation"
    read_first:
      - "AXE_Test_Remediation_Prompt_Library.md"
    read_next:
      - "Canonical Test Library.md"
      - "AXE → Design Tokens → Components.md"

  - task: "component_or_token_impact"
    read_first:
      - "AXE → Design Tokens → Components.md"
    read_next:
      - "Canonical Test Inventory: token dependencies and bi-directional component mapping.md"
```

---

## 6. Required namespace and identifier model

```yaml
identifier_namespaces:
  ATLF: "Framework chunk ID"
  CTL: "Canonical Test Library test identifier"
  MAWTL: "Mobile Application and Website Test Library"
  ACT_PATTERN: "ACT-style pattern procedure"
  ACT_PRACTICE: "ACT-style practice procedure"
  AXE: "AXE rule ID"
  REQ: "Product or service requirement"
  TEST: "Local executable test ID"
  EXEC: "Test execution ID"
  ISSUE: "Issue or defect record"
  EXC: "Exception"
  BDEP: "Baseline departure"
```

Rules:
- Never treat an AXE rule ID as a canonical test ID.
- Preserve exact source identity and title when referencing tests.
- Generated output must not collapse CTL, MAWTL, ACT, and AXE namespaces into one label.

---

## 7. Data interpretation rules

```yaml
interpretation_rules:
  - id: "IR-01"
    rule: "Mappings do not prove accessibility."
    explanation: "A WCAG mapping, component mapping, or AXE mapping supports traceability but is not proof of completion or success."

  - id: "IR-02"
    rule: "Automation does not replace manual judgement."
    explanation: "An automated pass or fail result can only establish a result for the rendered state it inspected."

  - id: "IR-03"
    rule: "Best practice is not conformance."
    explanation: "Recommended practices may be valuable and should be tracked, but they are not equivalent to WCAG A/AA criteria."

  - id: "IR-04"
    rule: "Remediation prompts are candidate guidance."
    explanation: "Prompts are instructions for human or machine review, not evidence that a fix is complete."

  - id: "IR-05"
    rule: "Uncertainty must be preserved."
    explanation: "Use cannot_tell, not_tested, blocked, tool_error, or similar states where evidence is incomplete."
```

---

## 8. Remediation prompt schema

```yaml
remediation_prompt_schema:
  fields:
    issue_id: "string"
    issue_type: "string"
    source_rule: "string"
    wcag_reference: "string | null"
    user_outcome: "string"
    likely_root_cause: "string"
    remediation_prompt: "string"
    required_human_review: "boolean"
    alternative_approaches: "array[string]"
    validation_method: "string"
```

Example:

```yaml
issue_id: "AXE-color-contrast"
issue_type: "contrast"
source_rule: "color-contrast"
wcag_reference: "1.4.3"
user_outcome: "Users can read text and controls without strain."
likely_root_cause: "Low foreground contrast on text or focus states."
remediation_prompt: "Review the text and interactive states for the affected component. Adjust foreground/background colours to meet the required contrast ratio and verify focus, hover, and disabled states."
required_human_review: true
alternative_approaches: ["Increase contrast using the design system token set", "Use a darker text token or lighter surface token"]
validation_method: "visual inspection + contrast measurement + keyboard/focus review"
```

---

## 9. Supported repository questions

```yaml
question_support:
  - question: "Which tests cover a user outcome?"
    answer: "Use the Canonical Test Library and the relevant WCAG mapping register."
  - question: "How does an AXE issue relate to a canonical test?"
    answer: "Use AXE rule descriptions and the AXE alignment file."
  - question: "What is the best manual follow-up to an automated result?"
    answer: "Use the automation-to-manual cross-reference and related canonical test."
  - question: "How do I remediate a finding?"
    answer: "Use the remediation prompt library and review the canonical and pattern test context."
  - question: "What is the governance model?"
    answer: "Use the delivery framework and testing approach."
```

---

## 10. Repository health checks

```yaml
health_checks:
  structural:
    - "Each top-level file has a clear purpose."
    - "Internal links resolve."
    - "The repository remains source-qualified and traceable."

  identity:
    - "Canonical tests remain unique and stable."
    - "AXE rule IDs are not treated as canonical test IDs."
    - "Historical or superseded files remain clearly labeled."

  mapping:
    - "Derived summaries remain clearly marked as derived."
    - "AXE mappings remain distinct from canonical tests."
    - "WCAG mappings remain restricted to WCAG 2.2 A/AA in active canonical records."

  evidence:
    - "Uncertainty is preserved where evidence is missing."
    - "Manual complements are listed where automation is partial."
    - "Prompts are presented as drafts requiring review."

  governance:
    - "Conformance claims remain bounded by the available evidence."
    - "No semantic or standards interpretation is hidden inside automation output."
```

---

## 11. External references and purpose summary

```yaml
external_links:
  - name: "EAA Scope and Applicability Gate"
    url: "https://github.com/Double-FW/Articles_and_other_LLM_Training_Resources/blob/main/EAA_Scope_and_Applicability_Gate.md"
    purpose: "Assesses whether the European Accessibility Act applies and what scope is in play."

  - name: "Inclusive Digital Service Outcome Dataset"
    url: "https://github.com/Double-FW/Inclusive_and_Effective_Design/blob/main/Inclusive_Digital_Service_Outcome_Dataset.md"
    purpose: "Provides outcome-based service and inclusion evidence context."

  - name: "EAA Evidence and Conformity Record Model"
    url: "https://github.com/Double-FW/Articles_and_other_LLM_Training_Resources/blob/main/EAA_Evidence_and_Conformity_Record_Model.md"
    purpose: "Structures evidence and conformity records for review and governance."
```

These are supporting resources. They do not replace this repository’s internal source-of-truth files.

---

## 12. Safety and usage policy

```yaml
usage_policy:
  do:
    - "Use canonical tests for stable user outcome selection."
    - "Use WCAG mapping files for standards traceability."
    - "Use automation files for automation interpretation and manual follow-up."
    - "Use remediation prompts as candidate fix guidance."
    - "Preserve uncertainty when evidence is incomplete."

  do_not:
    - "Do not treat AXE rules as canonical tests."
    - "Do not equate a mapping with proof of compliance."
    - "Do not present best practice as WCAG requirement."
    - "Do not claim accessibility without evidence."
    - "Do not silently convert an uncertainty state into a pass."
```

---

## 13. Summary

This repository is best used as a layered accessibility evidence system:

- governance layer for decision-making
- canonical layer for outcomes
- standards layer for WCAG mapping
- detailed procedural layer for execution
- automation layer for interpretation
- remediation layer for candidate fixes
- design-system layer for dependency analysis

When used correctly, it supports evidence-based QA, safe remediation planning, and clear separation between conformance evidence, design quality, and human judgement.

---

## 14. Quick machine-readable index

```json
{
  "repo": "Double-FW/QA_Accessibility_Testing",
  "url": "https://github.com/Double-FW/QA_Accessibility_Testing",
  "version": "1.1",
  "purpose": "Governed accessibility evidence and QA system",
  "primary_sources": [
    "Accessibility_Test_Led_Delivery_Framework.md",
    "Testing_Approach.md",
    "Canonical Test Library.md",
    "Canonical_WCAG_AA_Relationship_Register.md",
    "Mobile_Application_and_Website_Test_Library.md"
  ],
  "derived_views": [
    "Canonical_Test_Library_WCAG_AA_Summary.md"
  ],
  "automation_layers": [
    "AXE_Test_AA_Rule_Descriptions.md",
    "AXE_and _Test_Inventory_Alignment.md",
    "Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests.md"
  ],
  "remediation_layer": [
    "AXE_Test_Remediation_Prompt_Library.md"
  ],
  "dependency_layer": [
    "AXE → Design Tokens → Components.md"
  ]
}
```

---

## 15. Repository management guidance for autonomous systems

Autonomous systems managing this repository should:
- preserve source identities and titles
- keep canonical, rules, prompts, and mappings separate
- report uncertainty explicitly
- treat generated summaries as derived views
- avoid claiming conformance from automation alone
- require human review for semantic, governance, or standards-related changes
- maintain traceability between tests, mappings, and evidence

This repository is most effective when it is used as a structured evidence graph rather than a flat collection of documents.
