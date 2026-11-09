# Lesson 39: Diagnose outpost communication failures

Week 6 · Lesson 39 of 45 · Objective/exercise 6.3

[Course start](../README.md) · [Previous lesson](38-6-1-diagnose-iam-template-organization-and-ingestion-failures.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 6.3. **Practice mode:** Break and repair or evidence walkthrough.

**Read first:** [Outpost fundamentals and planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-fundamentals-and-planning); [Outpost troubleshooting](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-troubleshooting); [Troubleshoot errors on cloud instances](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/troubleshoot-errors-on-cloud-instances); [Create a standard outpost](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/working-with-standard-outposts/create-a-standard-outpost).

1. Begin with the outpost identity, selected region/account, current template version, and associated cloud instance.
2. Inspect the outpost’s open errors and the cloud instance’s individual capability statuses. Query cloud_health_auditing for Outpost events over the failure window.
3. Compare deployment/registration evidence with connectivity and IAM evidence. For a completed template with no registered outpost, inspect the outbound path used for registration.
4. Reproduce one documented fault on a disposable deployment, such as an acknowledged template prerequisite or a lab network error; do not randomly remove production permissions.
5. Apply the correction from the matching troubleshooting entry, verify Connected status, and execute a fresh scan to prove end-to-end recovery. If Outpost is unavailable, write a diagnosis against a supplied sandbox example and leave the live test pending.

**Verify and save:** An error timeline, identified root cause, and scan after recovery.

**Explain without notes:** Why is a healthy outpost VM different from a registered outpost with successful scans?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [40. Diagnose agent and Kubernetes connector failures](40-6-2-diagnose-agent-and-kubernetes-connector-failures.md)**
