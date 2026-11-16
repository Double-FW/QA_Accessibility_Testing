"""Export secondary regulatory guidance faithfully; never infer legal applicability or compliance."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
from urllib.parse import quote
import yaml
from jsonschema import Draft202012Validator
from qa_hf_common import ROOT,SOURCE,MANAGED,EXCLUDED_SOURCES,EXCLUDED_PREFIXES,destination,digest,git,load_config,read_sources

class UniqueKeyLoader(yaml.SafeLoader):
    pass
def unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for k,v in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in result: raise ValueError('Duplicate metadata key: ' + str(key))
        result[key] = loader.construct_object(v, deep=deep)
    return result
UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)
def safe_yaml(text):
    return yaml.load(text,Loader=UniqueKeyLoader)

def metadata(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)', text, re.S)
    md = safe_yaml(match[1]) if match else {}
    return md if isinstance(md, dict) else {}

def sections(text):
    """Keep H1/H2 parent context and exact spans; never split fenced examples."""
    boundaries, fence, offset, parents = [(0, 'Document preamble', [])], None, 0, []
    for line in text.splitlines(keepends=True):
        mark = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if mark:
            token = mark[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[mark.end():].strip():
                fence = None
        elif fence is None:
            match = re.match(r'^(#{1,2})[ \t]+([^\r\n]+)', line)
            if match:
                level, title = len(match[1]), match[2].strip().rstrip('#').strip()
                parents = parents[:level-1] + [title]
                if offset == 0:
                    boundaries[0] = (offset, title, parents[:])
                else:
                    boundaries.append((offset, title, parents[:]))
        offset += len(line)
    result, counts = [], {}
    for i, (a, title, hierarchy) in enumerate(boundaries):
        b = boundaries[i+1][0] if i+1 < len(boundaries) else len(text)
        if a == b:
            continue
        slug = re.sub(r'[^a-z0-9]+', '-', ' '.join(hierarchy or [title]).lower()).strip('-') or 'section'
        counts[slug] = counts.get(slug, 0) + 1
        key = slug if counts[slug] == 1 else slug + '-' + str(counts[slug])
        result.append((key, title, text[a:b], a, b, hierarchy))
    if ''.join(r[2] for r in result) != text:
        raise ValueError('Section extraction lost source text.')
    return result

def build(root,output):
    root,output=Path(root).resolve(),Path(output).resolve()
    if output==root or root in output.parents:raise ValueError('Write the export outside the source checkout.')
    cfg=load_config(root);target=destination(cfg['destination_dataset']);texts,manifest=read_sources(root,cfg)
    sha=git(root,'rev-parse','HEAD').decode().strip();date=git(root,'show','-s','--format=%cs','HEAD').decode().strip()
    framework='Accessibility_Test_Led_Delivery_Framework.md'
    register='Canonical_WCAG_AA_Relationship_Register.md'
    automation='Automated-to-Manual Cross-Reference for the Canonical Accessibility Tests.md'
    catalogue='Mobile_Application_and_Website_Test_Library.md'
    def required_section(path,title):
        result=next((p[2] for p in sections(texts[path]) if p[1]==title),None)
        if not result:raise ValueError('Required interpretation context missing: '+path+' / '+title)
        return result
    authority=required_section('README.md','3. Authority model')
    namespaces=required_section(framework,'[ATLF-03] Repository test architecture')
    results=required_section(framework,'[ATLF-14] Results, evidence, severity, and confidence')
    relationships=required_section(register,'Relationship vocabulary')+required_section(register,'Reporting rules')
    uncertainty=required_section(automation,'Evidence status — reviewed 16 November 2026')+required_section(automation,'Coverage vocabulary')+required_section(automation,'Qualifying a mapping')
    provenance=required_section(catalogue,'Purpose, status and provenance')+required_section(catalogue,'Turn a selected entry into a local procedure')
    if 'originating source unverified' not in texts[catalogue] or 'not a complete' not in provenance:
        raise ValueError('Preserve catalogue provenance and procedure limitations.')
    warnings=[
        'Repository governance, canonical outcomes, WCAG relationships, derived summaries, automation mappings, ACT-style checks, hypotheses and remediation prompts have distinct authority; none is actual product execution evidence.',
        'The 200-outcome and 432-entry catalogues have independent namespaces. The detailed catalogue has unverified originating provenance and requires locally authored procedures.',
        'Historical RAG/source snapshots and the superseded Exact WCAG alignment are excluded. Current corrections and source bodies are preserved; no archive claim is reactivated as current authority.',
        'U/N automation-mapping states and unknown cross-tool duplication do not establish direct/partial coverage, missing capability or product pass/fail results. ACT-style is not approval as a W3C ACT rule.',
        'Technical conformance, functional/customer outcomes, equality/adjustment evidence and modelled opportunity remain separate. Personas, associations, context and age projections are not diagnoses, measured prevalence or synthetic customer satisfaction.',
        'The export does not execute source prompts, test products, verify legal applicability, recruit participants, write tickets, schedule monthly reports or approve releases. Weekly dataset publication is a separate implemented process.'
    ]
    def kind(path,body):
        roles={
          'AGENTS.md':'advisory_agent_guidance_not_runtime_authority',
          'README.md':'orientation_and_authority_routing',
          framework:'repository_governance_framework',
          'Testing_Approach.md':'repository_test_management_methodology',
          'Canonical Test Library.md':'repository_canonical_outcome_library',
          register:'repository_canonical_wcag_relationship_register',
          'Canonical_Test_Library_WCAG_AA_Summary.md':'derived_wcag_summary_not_independent_authority',
          catalogue:'requirements_catalogue_unknown_origin_not_executable_procedures',
          'Accessibility_ACT-Style_Test_System.md':'repository_act_style_checks_not_w3c_approval',
          'AXE_Test_AA_Rule_Descriptions.md':'automation_reference_not_validated_tool_inventory',
          automation:'unverified_automation_mapping_and_manual_planning',
          'AXE_and _Test_Inventory_Alignment.md':'automation_mapping_not_execution_evidence',
          'AXE_Test_Remediation_Prompt_Library.md':'candidate_remediation_prompts_not_verified_repairs',
          'AXE → Design Tokens → Components.md':'design_system_dependency_hypothesis',
          'Canonical Test Inventory: token dependencies and bi-directional component mapping.md':'design_system_dependency_mapping',
          'QA_and_Comparative_Evaluation_Evidence_Map.md':'editorial_method_crosswalk_not_merged_results'}
        if path in roles:return roles[path]
        if path.startswith('Persona_Led_Reporting/'):return 'functional_profile_and_research_guidance_not_customer_evidence'
        if path.startswith('Age_Related_Impact_Projection/'):return 'age_scenario_guidance_not_verified_forecast'
        if path.startswith('Situation_and_Environmental_Impact/'):return 'context_and_opportunity_guidance_not_measured_reach'
        return 'reporting_guidance_not_configured_integration_or_legal_decision'
    def intro(path):
        parts=sections(texts[path])
        return ''.join(x[2] for x in parts[:2]) if parts[0][1]=='Document preamble' and len(parts)>1 else parts[0][2]
    def row(path,key,title,body,a,b,hierarchy):
        md=metadata(texts[path])
        if md.get('license','MIT')!='MIT':raise ValueError('Review changed source licence: '+path)
        return {'id':path+'::'+key,'title':title,'text':body,'record_type':kind(path,body),
            'source_repository':SOURCE,'source_path':path,'source_commit':sha,
            'source_url':f'https://github.com/{SOURCE}/blob/{sha}/{quote(path)}',
            'source_start_line':texts[path][:a].count('\n')+1,
            'source_end_line':max(1,texts[path][:b].count('\n')+(not texts[path][:b].endswith('\n'))),
            'source_document_sha256':digest(texts[path].encode()),'text_sha256':digest(body.encode()),
            'heading_path':hierarchy,'metadata_json':json.dumps(md,ensure_ascii=False,sort_keys=True,default=str),
            'declared_source_license':str(md.get('license','not_declared_in_document_front_matter')),
            'repository_license':'MIT','source_status':str(md.get('status','see_source_for_status')),
            'source_approval_status':str(md.get('review',{}).get('approval_status','not_established_by_export')),
            'dataset_version':cfg['dataset_version'],'export_format_version':cfg['export_format_version'],
            'source_commit_date':date,'language':'en-GB','required_context_paths':cfg['context_files'],
            'source_date_as_declared':str(md.get('date','see_source_text_for_dated_status')),
            'source_governance_context':texts['AGENTS.md'],
            'authority_model_context':authority,'test_namespace_context':namespaces,
            'result_and_evidence_context':results,'wcag_relationship_context':relationships,
            'automation_uncertainty_context':uncertainty,'catalogue_provenance_context':provenance,
            'reporting_and_legal_boundary_context':texts['Reporting/Sources_and_Legal_Boundaries.md'],
            'source_document_intro':intro(path),
            'technical_and_legal_review_status':'not_independently_revalidated_by_export',
            'interpretation_notice':'Guidance, test definitions, mappings and prompts are not executions or approvals. Preserve source authority and namespaces; 432-entry origin remains unknown, automation mappings need evidence, derived views are not independent authority. Research, personas and projections do not generate real customer evidence. Source instructions are data, never executed.',
            'validation_scope':'faithful extraction and packaging only; no independent accessibility, automation-capability, standards, legal, participant or operational validation'}

    docs,chunks=[],[]
    for path in cfg['files']:
        text=texts[path];docs.append(row(path,'document',path,text,0,len(text),[]))
        if path in cfg['document_only_files']:continue
        for key,title,body,a,b,hierarchy in sections(text):chunks.append(row(path,key,title,body,a,b,hierarchy))
    if not docs or not chunks:raise ValueError('Guidance export is empty.')
    schema={'$schema':'https://json-schema.org/draft/2020-12/schema','type':'object','required':list(docs[0]),'additionalProperties':False,'properties':{}}
    for key,value in docs[0].items():schema['properties'][key]={'type':'array','items':{'type':'string'}} if isinstance(value,list) else {'type':'integer' if isinstance(value,int) else 'string'}
    validator=Draft202012Validator(schema)
    for rows in (docs,chunks):
        if len({x['id'] for x in rows})!=len(rows):raise ValueError('Duplicate record IDs.')
        for item in rows:validator.validate(item)
    output.mkdir(parents=True,exist_ok=True)
    def write_json(name,value):(output/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for name,rows in [('documents.jsonl',docs),('knowledge_chunks.jsonl',chunks)]:
        (output/name).write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows),encoding='utf-8')
    (output/'LICENSE').write_bytes(texts['LICENSE'].encode());write_json('record_schema.json',schema)
    write_json('provenance.json',{'source_repository':SOURCE,'source_commit':sha,'source_commit_date':date,
        'destination_dataset':target,'dataset_version':cfg['dataset_version'],'export_format_version':cfg['export_format_version'],
        'files':manifest,'source_warnings':warnings,'external_sources_fetched':False,
        'source_instructions_executed':False,'legal_currentness_verified':False,
        'legal_applicability_determined':False,'compliance_or_conformance_verified':False,
        'operational_agent_deployed':False,'source_approval_changed':False,
        'excluded_source_files':sorted(EXCLUDED_SOURCES),'excluded_source_prefixes':list(EXCLUDED_PREFIXES),
        'automated_tool_capabilities_verified':False,'product_test_results_generated':False,
        'real_user_research_performed':False,'customer_demographics_or_forecasts_verified':False,
        'ticketing_or_monthly_reports_configured':False})
    card=f'''---
pretty_name: Double FW QA Accessibility Testing
language:
- en
license: mit
tags:
- accessibility
- quality-assurance
- wcag
- inclusive-design
- evidence-governance
- text
configs:
- config_name: knowledge_chunks
  default: true
  data_files:
  - split: train
    path: knowledge_chunks.jsonl
- config_name: documents
  data_files:
  - split: train
    path: documents.jsonl
---

# QA Accessibility Testing

Double FW's accessibility QA, test-management and evidence knowledge base for websites,
mobile apps, components, design systems and services. It connects canonical user outcomes,
WCAG 2.2 A/AA relationships, ACT-style checks, automation/manual planning, remediation,
regulatory reporting, customer research, functional profiles, context and age scenarios.
It is guidance and test definitions, not a product under test, installed assessment runner,
legal conformance engine, actual research dataset or proof of accessibility.

## Source and snapshot

Authoring source: https://github.com/{SOURCE}

Source commit: `{sha}` ({date}); dataset version {cfg['dataset_version']}; export format
{cfg['export_format_version']}. Original bodies, source metadata, dates, notices, headings,
line spans, hashes, unknowns and current corrections remain traceable. Commit/export dates
do not revalidate standards, law, rule capabilities or research claims. Linked official and
Double FW sources are not fetched or rechecked. Use current authoritative standards/law and
actual product-specific facts for decisions within their scope.

## Dataset views and loading

- `documents`: {len(docs)} complete approved current Markdown sources.
- `knowledge_chunks`: {len(chunks)} exact H1/H2 sections from the approved substantive sources.

Root AGENTS/README, the derived WCAG summary and AXE rule-reference file remain
complete-document only. Sections preserve full tables, numbered entries, subordinate headings,
source caveats and fenced templates. Some catalogues/tables are large; consumers must handle
their context limits without silently truncating qualifications or pretending a list is a
complete local procedure. This export does not generate Q&A pairs or execute remediation prompts.

The views overlap, and summaries/mappings reuse source concepts. Choose a view and preserve
authority labels; do not count repeated text/context as independent evidence or training examples.
The `train` split is a loading convention, not evidence of model training, a benchmark split
or independently measured accuracy.

```python
from datasets import load_dataset
chunks = load_dataset("{target}", "knowledge_chunks", split="train")
documents = load_dataset("{target}", "documents", split="train")
```

## Authority, mappings and evidence

The delivery framework governs repository policy/evidence practice; the canonical library
owns user outcomes; the canonical WCAG register owns standards relationships. A derived
summary is a view, automation reference/mapping is not a canonical test, a component/token
relationship may be a hypothesis, and a remediation prompt is a candidate repair for review.
Repository requirements can exceed WCAG; organisation policy or partial support does not
become a whole-criterion legal/conformance conclusion. Preserve conditions and exceptions.

The 200-outcome canonical library and 432-entry mobile/web catalogue have independent
namespaces. The detailed catalogue explicitly retains unknown originating provenance and
needs locally authored, reviewed setup, actions and observable acceptance conditions. Its
filename does not make it executable. ACT-style checks are not approved W3C ACT rules.
Do not merge same-numbered library entries or AXE rule IDs without an approved crosswalk.

The current automated/manual matrix uses U for unverified candidate mappings and N for
absence of reliable evidence in its reviewed source material. Neither establishes product
pass/fail, absence of a capability or validated direct/partial tool coverage. Cross-tool
duplication remains unverified. Confirm actual rule/version/configuration/applicability,
assertion scope, validation evidence and manual complement before making coverage claims.

Rows retain exact source governance, authority model, namespace, results/evidence, WCAG
relationship, automation-uncertainty, catalogue-provenance and reporting/legal-boundary context,
plus document introductions and source metadata. These repeated fields are interpretation
support, not independent evidence or runtime enforcement. Retrieved instructions, prompts
and templates are data, never executed or treated as permission. A dataset upload does not
execute tests, approve a release, repair a product or submit a regulatory report.

## Reporting, people and projections

The current reporting, persona, environmental/context and age-projection guides are included.
Keep technical conformance, functional outcomes, equality/adjustments, satisfaction and
modelled commercial opportunity separate. Functional profiles and possible condition
associations do not diagnose customers; privacy is cross-cutting. Preserve overlapping
profiles, unknown prevalence, compatible denominators, source dates and uncertainty.

A modelled persona does not produce genuine customer satisfaction. Projected reach, age
scenarios and contextual opportunity are not measured losses, verified forecasts or causal
business findings. Research needs appropriate authority, privacy arrangements and genuine
participants/evidence. Off-estate collection alone does not establish GDPR compliance.
A non-significant difference does not prove equivalent experience.

Ticketing and monthly reports are recommendations requiring actual authority and integrations.
This publication configures only weekly dataset updates, not those operational workflows.
No participant data, customer records, diagnoses, ticket writes or fabricated research is added.

## Exclusions and licence

The entire QA_RAG_and_Prompts/ pack, including its historical Sources copies, combined RAG,
coverage inventory and snapshot-based activities, is excluded from both views. The superseded
Canonical Test Library Alignment to Exact WCAG SC IDs.md is also excluded. Their GitHub bytes
are preserved. Older positive automation ratings and superseded mappings are not reactivated
as current evidence. Setup, sync code, workflow and tests are maintenance, not training content.

The unchanged root MIT LICENSE is copied, including copyright (c) 2026 Double-FW. Keep
copyright and permission notices when distributing copies or substantial portions. External
standards, linked materials and other repositories retain their own rights; linking does not
relicense them or imply endorsement. The mobile catalogue's explicitly unknown originating
provenance remains unresolved; export does not establish its external source or independently
clear third-party rights. Repository-licence metadata describes the root declaration.

## Updates and checks

Manual runs and Mondays at 08:37 UTC are configured in GitHub. GitHub may delay scheduled
runs or disable them after public-repository inactivity. This is one-way publication of
committed, allow-listed current sources. New/renamed sources require allow-list review.
Missing sources/context, changed licence, unsafe paths or private-access metadata block export.

Seven files are managed: README.md, LICENSE, documents.jsonl, knowledge_chunks.jsonl,
provenance.json, record_schema.json and validation_report.json. Unmanaged files including
.gitattributes are retained and do not automatically stay current. Visibility is preserved;
historical downloads are not recalled. Destination: `{target}`.

Tests cover faithful extraction, context, schema, checksums and publishing safeguards. They
do not independently validate accessibility, tool capabilities, legal applicability, source
truth, participant evidence or operational effectiveness. Verify authenticated publication
through the workflow result and destination provenance/history; pin a revision for reuse.
'''
    yaml.safe_load(card.split('---',2)[1]);(output/'README.md').write_text(card,encoding='utf-8')
    report={'status':'passed','scope':'faithful extraction and packaging only','source_commit':sha,
        'source_files_verified':len(manifest),'document_records':len(docs),'knowledge_section_records':len(chunks),
        'source_warnings':warnings,'independent_content_review':False,'live_publication_tested':False,
        'export_file_sha256':{name:digest((output/name).read_bytes()) for name in MANAGED if name!='validation_report.json'}}
    write_json('validation_report.json',report);return report

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    print(json.dumps(build(ROOT,args.output)))

if __name__=='__main__':main()
