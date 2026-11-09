# Lesson 2: Choose licenses, retention, scanning, and IAM

Week 1 · Lesson 2 of 45 · Objective/exercise 1.2

[Course start](../README.md) · [Previous lesson](01-1-1-assess-architecture-and-the-existing-environment.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 1.2. **Practice mode:** Configure and explain.

**Read first:** [Understand license plans](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/get-started/understand-license-plans); [Data retention](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/get-started/understand-license-plans/data-retention); [Prerequisites for onboarding AWS](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/prerequisites-for-onboarding-aws); [AWS security capabilities and deployment planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/aws-security-capabilities-and-deployment-planning); [Outpost fundamentals and planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-fundamentals-and-planning); [AWS provider permissions](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/amazon-web-services-aws-provider-permissions).

1. Inspect Settings → Cortex License and record the actual base license, add-ons, workload capacity, and retention entitlements. Mark unavailable labs before you start them.
2. Build a capability matrix for posture, runtime, AppSec, log ingestion, and data scanning. Match your intended lab workloads to the documented metering categories.
3. Record retention requirements by dataset and compare them with the documented defaults and your purchased entitlements; do not treat all data types as having one retention period.
4. For AWS, distinguish the permissions needed by the person deploying the template from the permissions used by Cortex afterward. Read the generated IAM resources and the provider-permission explanation for each enabled capability.
5. Choose Cloud Scan or Outpost for this deployment and defend the choice using data handling, operations, permissions, and cost. Implement the chosen mode in week 2.

**Verify and save:** A license and permissions matrix, a retention worksheet, and a justified scanning choice.

**Explain without notes:** Why can a successful login coexist with an unavailable scanner or an API permission failure?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [3. Verify network communication](03-1-3-verify-network-communication.md)**
