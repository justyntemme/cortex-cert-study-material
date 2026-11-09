# Lesson 1: Assess architecture and the existing environment

Week 1 · Lesson 1 of 45 · Objective/exercise 1.1

[Course start](../README.md) · [Previous lesson](../README.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 1.1. **Practice mode:** Build and explain.

**Read first:** [Plan and prepare](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/plan-and-prepare); [AWS security capabilities and deployment planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/aws-security-capabilities-and-deployment-planning); [Outpost fundamentals and planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-fundamentals-and-planning).

1. Inventory your sandbox: account IDs, regions, EC2, containers, Kubernetes, functions, registries, data stores, repositories, existing security tooling, and audit-log destinations. Record owners and what each source contributes.
2. Draw the intended flow from source systems to Cortex, including identity trust, scanning infrastructure, log collection, and runtime agents. Put current coverage and missing coverage next to each workload.
3. Write a migration sequence: establish asset visibility, validate scans and logs, introduce scoped policies, then validate protection. Identify which existing tools or log paths would overlap during transition.
4. Produce a one-page deployment design with a coverage table; do not assume that connecting an account proves every capability is working.

**Verify and save:** A diagram and inventory that explain how every lab workload will be discovered, scanned, and protected.

**Explain without notes:** Which components would you change for a customer with strict data-residency requirements?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [2. Choose licenses, retention, scanning, and IAM](02-1-2-choose-licenses-retention-scanning-and-iam.md)**
