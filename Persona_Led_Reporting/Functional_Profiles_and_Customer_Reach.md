# Functional profiles, condition associations and customer reach

## A functional profile register

These are plain-language summaries of EAA Annex I Section VII (a)–(k), not medical categories. The condition associations are illustrative possibilities, not exhaustive medical mappings or evidence that everyone with a condition has a particular need. Validate relevance through voluntary functional questions and lived experience. Do not assign diagnoses or legal disability status from product use.

| Profile | Functional requirement/lens | Examples of groups that may share the need | Example service question |
| --- | --- | --- | --- |
| FP-a | Usage without vision | Blind people, including people with severe sight loss from different causes | Can the complete task and confirmation work non-visually? |
| FP-b | Usage with limited vision | People with low vision, including some with cataracts, glaucoma or macular degeneration | Does it work with magnification, chosen contrast and glare constraints? |
| FP-c | Usage without perception of colour | People with inherited or acquired colour vision deficiency | Are status and errors understandable without colour distinctions? |
| FP-d | Usage without hearing | Deaf people and people with profound hearing loss | Can information, alerts and support work without audio? |
| FP-e | Usage with limited hearing | People with partial or age-related hearing loss | Are appropriate enhanced audio and alternative channels available? |
| FP-f | Usage without vocal capability | Some people with dysarthria, acquired speech loss or a stammer who cannot reliably use a spoken route | Can input, identity checks and support work without speech? |
| FP-g | Usage with limited manipulation or strength | Some people with arthritis, motor impairments, limb differences, tremor or injury | Does operation avoid unnecessary precision, force and simultaneous actions? |
| FP-h | Usage with limited reach | Some wheelchair users, people with restricted upper-body movement or short stature | Can terminal controls and peripherals be reached in realistic positions? |
| FP-i | Minimise photosensitive seizure risk | People with photosensitive epilepsy; not everyone with epilepsy | Has flashing been assessed safely by appropriate methods? |
| FP-j | Usage with limited cognition | Some people with learning disabilities, acquired brain injury or dementia; some neurodivergent people with task-specific attention, memory or comprehension needs | Can the task be understood and recovered without excessive memory/attention demand? |
| FP-k | Privacy when using accessibility features | Everyone using accessibility features; no separate medical population | Can accessible use preserve confidentiality and control? |

For FP-j, autism, ADHD, dyslexia and dyspraxia can inform recruitment diversity where relevant, but none implies globally limited cognition or the same support needs. For FP-f, difficulty speaking is distinct from difficulty understanding. Access methods vary within every group.

For each persona add actual goal, experience/familiarity, AT/settings, constraints, success conditions, support choice and relevant intersections. Avoid fictitious personal histories presented as research. See [Double-FW's functional-needs guide](https://github.com/Double-FW/Accessibility_Demographics/blob/main/quick-guides/02-functional-needs-and-the-eaa.md) and the [source register](../Reporting/Sources_and_Legal_Boundaries.md) for associations and functional context.

## Estimate the audience for each profile

There is no defensible universal prevalence percentage for these profiles. A diagnosis prevalence rate does not automatically estimate a functional threshold, an access preference or exposure to a particular barrier.

Follow the [Double-FW estimation method](https://github.com/Double-FW/Accessibility_Demographics/blob/main/methods/estimating-demographics.md) and its [statistics catalogue](https://github.com/Double-FW/Accessibility_Demographics/blob/main/Accessibility_Demographic_Statistics_and_Estimation_Methods.md). Retrieve current sources and metric IDs; preserve the catalogue's exploratory/review status and inspect the underlying evidence.

1. Define unique customers, intended market or task users, geography, age bands and period. Accounts and visits are not unique people.
2. Select a functional measure matched to the profile, severity threshold and customer population. Use diagnosis data only as a labelled proxy scenario when no better data exists and explain its limitations.
3. Prefer compatible aggregate customer evidence; otherwise use age/country-specific population rates with explicit transport assumptions. A self-selected survey estimates experiences of its respondents, not population prevalence.
4. For disjoint customer segments i, calculate `estimated_count(profile) = sum(N_i × p_profile,i)`; percentage is count divided by the declared total unique customer count × 100.
5. Show source year, denominator, questionnaire/threshold, geography, exclusions, uncertainty, calculation and confidence. Age-standardised rates are not direct headcount multipliers.
6. Record “not estimable from available evidence” where a compatible rate is absent. Commission proportionate research rather than filling a blank with a guessed percentage.

Illustrative arithmetic only: a fictional 10,000-customer base with 6,000 in one age band and 4,000 in another, using assumed functional rates of 5% and 15%, gives 900 estimated customers (9%). These are invented inputs, not prevalence evidence for any profile.

## Avoid double counting

Report marginal counts for each profile, then report intersections or union reach separately. With compatible observed counts, `N(A or B) = N(A) + N(B) - N(A and B)`. Without overlap evidence, show bounds: union is at least the largest individual group and at most the smaller of the customer total and sum of groups. Do not assume independence.

FP-a/FP-b and FP-d/FP-e can overlap across tasks, time or source definitions; do not assume disjointness unless definitions ensure it. FP-k is evaluated across modes and counted as relevant accessible-use exposure, never an additional population to add to totals. Situational constraints are counted separately from disability prevalence.

For an issue, narrow from profile membership to people exposed to the affected task/state and the probability or observed incidence of the barrier. Record missing exposure data. Estimated affected people, interactions affected and commercially recoverable opportunity are different metrics.
