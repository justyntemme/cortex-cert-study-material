# Lesson 44: Diagnose an unexpected AWS cost increase

Week 6 · Lesson 44 of 45 · Objective/exercise 6.7

[Course start](../README.md) · [Previous lesson](43-6-5-diagnose-appsec-scanner-mapping-and-policy-failures.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 6.7. **Practice mode:** Investigate actual or supplied billing evidence.

**Read first:** [How to onboard Amazon Web Services](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/how-to-onboard-amazon-web-services); [Cortex Cloud and AWS audit log collection architecture](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/cortex-cloud-and-aws-audit-log-collection-architecture); [Outpost fundamentals and planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-fundamentals-and-planning); [Configure registry scanning for cloud accounts](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/registry-scanning/configure-registry-scanning-for-cloud-accounts); [AWS Cost Explorer filtering](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-filtering.html); [AWS Cost Explorer data freshness and daily costs](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-exploring-data.html).

1. Compare a baseline interval with the cost-rise interval in Cost Explorer. Group by service and filter the affected account/region, then examine usage types.
2. Correlate the first increase with onboarding, scan scope/cadence changes, new registry images, CloudTrail data events, or an Outpost deployment. Treat these as hypotheses until usage supports them.
3. Inventory the actual scanning/logging resources and compare them with the generated templates and selected capabilities. Check for redundant log paths and retained lab resources.
4. Make one scoped correction, record the intended coverage impact, and inspect subsequent usage and security coverage. Allow for billing-data delay.
5. Write a short explanation naming the service, resource or usage driver, configuration trigger, correction, and remaining uncertainty. Use existing data or a provided sample; do not intentionally generate a large bill.

**Verify and save:** A cost investigation backed by usage evidence and a measured correction.

**Explain without notes:** How would you prove that a scanning change caused the increase rather than ordinary workload growth?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [45. Full scope practice and readiness review](45-review-full-scope-practice-and-readiness-review.md)**
