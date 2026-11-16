# Rolling customer research, experience scoring and A/B testing

## When to recommend a quantitative study

Recommend research when technical results do not explain complaints/drop-off; a critical profile or intersection is missing; comparable experience data are stale or too uncertain; a major journey/terminal change is planned; or measured gaps remain after repair. Do not delay fixing an already evidenced blocker while waiting for survey significance.

The recommendation must state the decision, task/build, functional profiles, target customers, missing evidence, research method, proposed precision/sample plan, privacy review, owner, cost/capacity assumptions, accessible recruitment and how findings will lead to action. Real customers with relevant lived experience are needed for customer experience claims. Include people unable to start or complete the service, not just successful users.

## Privacy and accessible participation

An independent off-estate research environment is a useful default where it reduces production tracking and participant exposure. It is not a GDPR exemption. On-estate collection can be appropriate if lawfully designed; off-estate collection still needs the following review before recruitment:

- Identify the controller, processors/joint controllers and purposes; applicable EU/UK GDPR and local law; Article 6 lawful basis; and, if health/disability information is processed or inferred, an appropriate Article 9 condition and any additional national safeguards. Do not assume commercial UX work qualifies for scientific-research exemptions.
- Assess DPIA requirements and complete one where likely high risk. Review processor contracts, subprocessors, access, hosting, transfers, deletion, breach handling and prohibition of unapproved model-training reuse.
- Explain participation, collection, uses, recipients, retention and rights in an accessible notice. Research participation consent and a processing lawful basis are separate decisions. Where relying on consent, assess whether it is valid, specific and freely given; provide withdrawal routes and explain limits after genuine anonymisation.
- Minimise data: voluntary task-relevant functional questions, multiple needs, prefer-not-to-answer and no diagnosis requirement. Functional answers can still reveal health data. Do not infer health from device, AT, browsing or purchase history.
- Keep recruitment/contact/compensation records separate from responses. Use limited-purpose pseudonymous IDs and separately controlled linkage. Do not put identifiable research data in this public repository or project tickets.
- Set a justified retention schedule and deletion process, secure access, small-cell suppression and disclosure review. Pseudonymised data remain personal data when reidentification is possible; aggregation alone does not guarantee anonymity.
- Test the survey and off-estate handoff for keyboard, screen reader, magnification, plain language and alternative response modes. Offer reasonable payment, breaks and chosen support. Do not withdraw service access for refusing research.

Use realistic tasks in an approved safe environment, familiar AT/settings where relevant, synthetic transactions and no unnecessary production-account linkage. Obtain an appropriate research plan and human safeguards before live work. Never expose participants to suspected hazardous flashing to measure satisfaction.

## Define a rolling instrument

Use stable, cognitively tested questions and response endpoints. This is an illustrative question set requiring piloting, not a validated universal scale:

| Aspect | Example question after a defined task |
| --- | --- |
| Navigation | How satisfied were you with finding where to go? |
| Content | How satisfied were you with how understandable the information was? |
| Task completion | How satisfied were you with completing what you came to do? |
| Preference support | How satisfied were you with support for your settings and access method? |
| Recovery/support | How satisfied were you with recovering from problems or getting help? |
| Overall experience | Overall, how satisfied were you with this experience? |

Use 1 very dissatisfied, 2 dissatisfied, 3 neither satisfied nor dissatisfied, 4 satisfied, 5 very satisfied, plus not applicable/prefer not to answer. Keep no-response, not applicable and refusal distinct. Ask whether completion was accurate, independent, chosen-assisted, forced-assisted, abandoned or blocked. Record task time/effort, comprehension, confidence and privacy separately. Satisfaction cannot validate an incorrect completion.

For each collection retain instrument/version/language, task/build, period, channel/context, recruitment source, profile selections, valid answers and consent/processing records in approved systems. Publish aggregate data only after disclosure review.

## Compare experience honestly

For each aspect and profile report valid n, response distribution, completion/abandonment, assistance, uncertainty and exclusions. An optional descriptive index is `100 × (mean valid rating - 1) / 4`. This assumes equal spacing of the ordinal scale; label it and retain distributions. Missing answers are not zero.

For a chosen comparable reference group, `gap = profile index - reference index` in index points. Negative values indicate lower reported satisfaction. Show each aspect before any overall aggregate. A single composite can hide exclusion; if adopted, specify weights and missing-item rules in advance.

Compare the same tasks, versions, period, instrument and relevant experience/context. The reference may be another build, a prior matched period or customers without that particular functional constraint; it is not an assumed “normal user”. Profile overlap means observations are correlated. Use suitable statistical methods with participant clustering/repeated measures and weighting where justified.

Determine sample size from the estimand, meaningful difference, variance/base rate, precision, allocation and planned analysis, with research/statistical review. Do not invent variance or use a universal minimum. Report confidence intervals where valid; label model assumptions and survey design. Small or self-selected samples support bounded findings. Suppress unsafe cells without describing them as successful or unimportant.

Collect continuously or in agreed waves; review monthly and show rolling windows with dates. Overlapping windows are not independent. Keep cohort/build changes visible; separate population mix changes from experience change. Include adverse experiences and non-response bias. Do not manufacture scores for underrepresented groups.

## A/B testing before introducing change

Pre-register the task, hypotheses, meaningful improvement, profile-specific harm limits, outcome measures, analysis, sample size/power, allocation, duration and stopping/rollback rules. Combine technical regression checks with accurate completion, effort, privacy and satisfaction. Repair known exclusion before exposing users; both variants need appropriate safety review.

Randomise at an appropriate unit, preserve assignment and account for repeat participants, learning and contamination. Include actual customers across functional profiles and relevant intersections, with accessible alternative participation. For terminals consider location/time clustering and physical context.

A release candidate should meet the defined technical gates and show no unacceptable deterioration for a relevant profile, even if the overall average improves. Insufficient evidence for a smaller group calls for targeted follow-up and an explicit decision, not automatic clearance. Use pre-specified non-inferiority/equivalence margins and suitable intervals if making those claims; lack of statistical significance is not equivalence. Correct for planned multiple comparisons or label exploratory findings.

Track deployed outcomes and rollback triggers. Before/after observational surveys alone cannot attribute a change to the new design. A/B research reduces risk; it cannot guarantee that no barrier will be introduced.
