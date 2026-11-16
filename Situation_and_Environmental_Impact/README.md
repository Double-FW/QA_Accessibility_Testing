# Situation and environmental impact reporting

Version 1.0 · 16 November 2026 · Practitioner guidance

Report how the product's actual use conditions change the impact of a barrier. Connect product facts and aggregate customer research to test results. A situational limitation can affect anyone; it does not establish that a person has a disability.

## Join product, context and test evidence

Use shared service/build, journey/task, component, execution, finding and ticket IDs from [regulatory reporting](../Reporting/README.md). Obtain legitimate aggregate product and customer information rather than inferring individual health or stress from behaviour.

| Context | Product/customer evidence to seek | Test or research emphasis |
| --- | --- | --- |
| Outdoors, glare, dim light | Product use setting, screen position, display constraints, customer accounts | Contrast, text size, glare, brightness preferences, non-visual alternatives |
| Noise or need for silence | Transport/public/private use, audio expectations, actual customer reports | Captions/text cues, audio controls, non-speech help and privacy |
| On the move, carrying items | Safe observations, one-hand use, interruptions, connectivity patterns | Large targets, reduced precision, save/resume, recovery and continuity |
| Fixed terminal or kiosk | Installation heights/angles, approach space, peripherals and physical access | Reach, wheelchair/seated use, dexterity, privacy, end-to-end transaction |
| Particular times of day | Aggregate task demand by time, chosen customer reports of fatigue or fluctuating capacity | Session/time limits, legibility, cognitive load, flexible recovery |
| Pressure, distress or urgency | Service purpose, deadlines, complaints, support research | Plain instructions, confirmation, reversible actions, support and error recovery |
| Poor connection or interruption | Actual supported locations/network conditions and session evidence | Retained state, duplication prevention, accessible loading/error messages |

Do not ask someone to use a device unsafely while moving or induce distress. Safe simulations can inform technical hypotheses; use consensual, safeguarded research for lived-experience claims. Do not assume a time of day predicts someone's capacity or collect medication/health data unnecessarily.

## Procedure

1. Define intended and foreseeable contexts from product strategy, usage research and service facts. Record observed, reported and assumed contexts separately.
2. Match tasks and functional demands to [persona profiles](../Persona_Led_Reporting/Functional_Profiles_and_Customer_Reach.md), including combinations.
3. Select representative conditions and safe test methods; record actual device, settings, lighting/noise measurements where relevant, network, posture and constraints. Do not invent universal environmental thresholds.
4. Execute technical checks and approved customer research as appropriate. Compare the same task in a reference and relevant context, retaining build and method.
5. Describe changes in accurate completion, effort, recovery, independence, privacy and satisfaction. Link direct observations and separately state anticipated impact.
6. Route issues through the [priority and ticket process](../Reporting/Prioritisation_Tickets_and_Monthly_Reporting.md); verify repairs in the context that exposed the issue.

## Estimate exposure and opportunity

For disjoint context/time segments, a useful model is:
`affected interactions = sum(interactions_in_segment × proportion_exposed_to_barrier_given_segment)`.
Add a functional-need dimension only when compatible joint/conditional evidence supports it. Do not multiply independent-looking marginal disability and context percentages as if they were independent.

These are interactions, not unique customers. For unique reach, deduplicate people in an authorised privacy-preserving system or report overlap bounds. Where data are missing, state unknown and show labelled low/central/high scenarios, not spurious confidence intervals.

Separate four value measures:

| Measure | Evidence and interpretation |
| --- | --- |
| Customer experience value | Observed improvement in access, effort, independence, confidence, privacy or successful completion |
| Reach opportunity | Unique customers or interactions potentially helped, with denominator, overlap and exposure limits |
| Commercial opportunity | Scenario: exposed customers × incremental outcome improvement × relevant value per outcome, less costs; all factors require evidence/assumptions |
| Engagement opportunity | A proposed way to explain and offer an improvement through accessible channels, followed by observed uptake/benefit |

Potential audience value is not revenue recovered. Do not sum saved support cost and retained margin when they overlap, or credit the full customer lifetime value to one fix. Show uncertainty, attribution limits and sensitivity. An A/B study may strengthen causal evidence where ethical and feasible.

## Report template

- Service/build, journey/task, reporting window and context.
- Product facts and aggregate customer evidence, sources and confidence.
- Functional profiles/intersections and anticipated versus observed impact.
- Test executions, actual findings, exposure estimate and denominator.
- Severity/urgent overrides; context-based priority rationale.
- Proposed repair, interim access, owner, ticket and retest conditions.
- Customer benefit, reach and commercial scenarios, with costs and uncertainty.
- Engagement plan: accessible release notes/help/support, broad opt-in communication, discovery of settings and feedback route.
- After repair: observed outcomes, uptake, unresolved barriers and next review.

Use engagement to make improvements discoverable and useful. Never target individuals with inferred health labels or publicise a participant's condition. Work with relevant communities and customer support; measure whether the communication reaches excluded customers as well as active users.

Supporting guidance: [Double-FW environment and situations](https://github.com/Double-FW/Accessibility_Demographics/blob/main/quick-guides/05-environment-and-situations.md), [combined needs and reach](https://github.com/Double-FW/Accessibility_Demographics/blob/main/methods/combined-needs-and-reach.md), [customer value](https://github.com/Double-FW/Accessibility_Demographics/blob/main/methods/customer-and-lifetime-value.md), and [data ethics](https://github.com/Double-FW/Data_Ethics_and_Disability).
