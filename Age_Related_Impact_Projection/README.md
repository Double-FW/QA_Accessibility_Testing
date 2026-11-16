# Age-related impact projections for service planning

Version 1.0 · 16 November 2026 · Practitioner guidance

Estimate how changing customer age structures and functional needs may affect future service access, retention, support and investment. Age is not a diagnosis, a measure of competence or evidence of incapacity. Projections describe conditional futures, not individual predictions.

## Choose the population and horizon

Distinguish the addressable market, future customer base and retention of today's customers. They require different models. Set geography, disjoint age bands, base year and planning horizons, for example 1, 3, 5 and 10 years. Longer horizons require wider scenario analysis.

Use the organisation's lawful aggregate age distribution if suitable, recording coverage, missing age, selection bias and source dates. Avoid unnecessary dates of birth and individual health inference. If customer data are unavailable, use an explicitly labelled external market scenario; do not present national demographics as measured customer demographics.

## Evidence inputs

| Input | Record and quality checks |
| --- | --- |
| Population projections | Statistical office, series/base year, country, age bands, projection year, variant, retrieval date and assumptions |
| Functional prevalence by age | Definition/severity threshold, country, source year, denominator, disjoint bands and uncertainty |
| Customer composition | Unique customers, age/geography mix, unknown-age share, acquisitions, exits, retention and projection assumptions |
| Service outcomes | Actual task demand, technical findings, completion, effort, satisfaction, support, retention; period and sample |
| Business quantities | Relevant margin/value, support costs, investment costs, discount assumptions and attribution limits |

Starting points verified on 16 November 2026: [ONS population projections](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections) and [2024-based release](https://www.ons.gov.uk/releases/nationalpopulationprojections2024based); [Eurostat EUROPOP2023 metadata](https://ec.europa.eu/eurostat/cache/metadata/EN/proj_23n_esms.htm); [US Census projection tables](https://www.census.gov/programs-surveys/popproj/data/tables.html). Recheck for superseding releases before calculation. Match projection variants and jurisdictions rather than mixing vintages.

For functional-rate inputs consult [Double-FW's statistics catalogue](https://github.com/Double-FW/Accessibility_Demographics/blob/main/Accessibility_Demographic_Statistics_and_Estimation_Methods.md) and [ageing guidance](https://github.com/Double-FW/Accessibility_Demographics/blob/main/research/ageing-and-changing-needs.md), then inspect original sources. Age composition of people with sight loss is not sight-loss prevalence within each age band. Cumulative thresholds such as 65+ and 75+ overlap; use disjoint bands or a valid denominator-based conversion.

## Calculate and show assumptions

For a modelled customer base at time t:
`estimated people with functional need f at t = sum(N_i,t × p_f,i,t)`,
where i is a disjoint age/geography segment. The corresponding share divides by total modelled customers at t.

Set N from an explicit customer scenario. Options include:

- Apply official future age shares to a declared future customer total as a market-composition scenario. State the assumption that market changes transfer to customers.
- Model existing customer cohorts ageing, attrition, mortality where appropriate, new acquisition and changing service participation. National population change alone does not estimate customer retention.
- If customer totals are unavailable, report rates or an illustrative fixed-base scenario with its limitation.

Do not model the population ageing by simply moving every age band forward: deaths, births, migration and acquisition matter. Customer cohorts and the whole market should be reported separately.

Keep an ageing-only scenario with fixed age-specific functional rates distinct from scenarios with changing rates or service use. Show low/central/high assumptions and the official projection variants relevant to the decision. Analyst scenario ranges are not statistical confidence intervals. Address missing age, definition mismatch, correlated needs, small groups and source uncertainty.

## Connect projections to the backlog and future business

Join functional profiles to existing journey/test findings and context exposure. Projected people with a need are not automatically people blocked by the service. Estimate exposed customers/interactions only with task-use and barrier evidence, and do not sum overlapping functional groups.

For an illustrative planning scenario, assume 10,000 customers remain constant; older-band share rises from 20% to 30%; functional-need rates are assumed to be 5% in the other band and 20% in the older band. Modelled need rises from 800 (8%) to 950 (9.5%), an increase of 150 or 1.5 percentage points. These invented inputs demonstrate arithmetic only; they are not observed rates, a forecast or proof of business loss.

Assess likely demand for readable information, hearing alternatives, accessible authentication, reduced precision, memory support, continuity and help without lost autonomy. Recruit across ages and functional needs to test these assumptions.

Estimate financial scenarios from evidenced changes in completion/retention/support and relevant unit values, with costs and time horizon. Attribute only the incremental effect plausibly supported by evidence. Apply an approved discount rate for multi-year value and avoid counting retained customers again as new acquisition or counting a shared benefit once per persona.

Prioritise shared improvements that support long relationships and changing needs. Essential access duties and urgent harm remain priority overrides regardless of financial estimates.

## Projection report template

| Section | Required output |
| --- | --- |
| Decision | Planning question, service/market, owner and horizon |
| Baseline | Current population/customer age mix, functional definitions, current evidence and missing data |
| Method | Source versions, age bands, model, formulas, assumptions and calculation trail |
| Results | Year-by-year counts/shares by need, context and relevant task; no overlap inflation |
| Sensitivity | Variants, uncertain rates/customer growth/retention and interpretation limits |
| Business implications | Potential lost access, support/retention demand, customer and commercial value scenarios |
| Investment | Linked issues/design-system improvements, owner, timing, cost and verification |
| Refresh | Review annually, and after new official projections, material customer changes or new experience evidence |

Use the monthly reporting cycle to monitor leading evidence and investment delivery, while retaining the projection's longer planning horizon. No projection replaces direct customer research or establishes legal compliance.
