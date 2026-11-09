# Lesson 38: Diagnose IAM, template, organization, and ingestion failures

Week 6 · Lesson 38 of 45 · Objective/exercise 6.1

[Course start](../README.md) · [Previous lesson](37-4-4-configure-detection-rules-and-automation-playbooks.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 6.1. **Practice mode:** Break and repair in the lab.

**Read first:** [AWS post-deployment verification](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/aws-post-deployment-verification); [Troubleshoot errors on cloud instances](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/troubleshoot-errors-on-cloud-instances); [Deploy the authentication template in AWS](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/deploy-the-authentication-template-in-aws); [AWS provider permissions](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/amazon-web-services-aws-provider-permissions); [Verify collector connectivity](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/administration-and-troubleshooting/verify-collector-connectivity).

1. Start with a known working AWS integration and save its configuration. Use a dedicated disposable test instance for fault injection.
2. Practice a missing-permission case on that test role: record the exact denied action and capability error, compare with the provider permission table, restore the missing permission, and verify recovery.
3. For a stack failure, inspect CloudFormation Events and the first causal resource failure; for Terraform inspect the failing resource and retained state. Correct the stated prerequisite and rerun the supported template workflow.
4. For organization coverage, compare configured OU/account selection with discovered member accounts and per-account capability status. Inspect the generated organization deployment and its failed member deployment rather than treating the management-account status as sufficient.
5. For ingestion, follow the configured log path through delivery, permissions, notifications, and collector status. Query collection_auditing for collector transitions and cloud_health_auditing for cloud capability errors.
6. If CloudFormation succeeds but Cortex never shows a new connected instance, check the registration Lambda/CloudWatch evidence described in the post-deployment guide. Capture error, fix, recovery, and fresh ingested data.

**Verify and save:** A fault report with the causal error, minimal correction, and fresh post-recovery evidence.

**Explain without notes:** Why can CREATE_COMPLETE coexist with missing registration, missing member accounts, or missing logs?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [39. Diagnose outpost communication failures](39-6-3-diagnose-outpost-communication-failures.md)**
