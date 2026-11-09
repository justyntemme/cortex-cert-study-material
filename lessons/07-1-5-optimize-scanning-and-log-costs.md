# Lesson 7: Optimize scanning and log costs

Week 1 · Lesson 7 of 45 · Objective/exercise 1.5

[Course start](../README.md) · [Previous lesson](06-cli-a-cli-a-discover-and-explain-arguments.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 1.5. **Practice mode:** Measure and explain.

**Read first:** [How to onboard Amazon Web Services](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/how-to-onboard-amazon-web-services); [Cortex Cloud and AWS audit log collection architecture](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/cortex-cloud-and-aws-audit-log-collection-architecture); [Outpost fundamentals and planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-fundamentals-and-planning); [Configure registry scanning for cloud accounts](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/registry-scanning/configure-registry-scanning-for-cloud-accounts); [AWS Cost Explorer filtering](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-filtering.html); [AWS Cost Explorer data freshness and daily costs](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-exploring-data.html).

1. Record a baseline of enabled scans, selected regions, image scan scope, audit trails, and log destinations.
2. Compare the existing CloudTrail delivery path with the proposed Cortex path. Draw where duplicate collection could occur before enabling an additional trail or ingestion path.
3. Review registry initial-scan selection and the cost tradeoff of Cloud Scan versus Outpost. Choose the smallest lab scope that still exercises the capability.
4. In AWS Cost Explorer, compare days and filter by account, service, region, and usage type. Record the change date alongside any scan or logging configuration change.
5. Write an optimization proposal and its coverage tradeoff. Check later billing data before claiming savings; current-period cost data can arrive late.

**Verify and save:** A baseline, a proposed change, and a method for measuring both cost and retained security coverage.

**Explain without notes:** Which evidence would separate increased event volume from duplicated log collection?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [8. CY A Build a diagnostic baseline](08-cy-a-cy-a-build-a-diagnostic-baseline.md)**
