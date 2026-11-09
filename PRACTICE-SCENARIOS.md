# Original practice scenarios

These are original study questions, not exam items or a vendor practice test. Answer without notes, then compare with the rubric and read the supporting source. Score 0 for an unsupported guess, 1 for a partly correct diagnosis, and 2 for a correct answer with evidence and verification. Use different scenarios for the second readiness check rather than memorizing these answers.

Keep these 18 questions and add the 12 in [APPLICATION-ANALYSIS.md](APPLICATION-ANALYSIS.md). The added set uses a separate 0–3 reasoning rubric; normalize scores before comparing totals. For each original question, also ask one changed-input application question and one cross-feature analysis question using its linked sources. This supports the meeting guidance without claiming an exact exam difficulty distribution.

## Question 1 Objective 1.2

Your tenant login works, but an AppSec exercise is unavailable. What do you check?

## Question 2 Objective 1.4

A user opens the asset module but cannot see the lab asset. What is your investigation order?

## Question 3 Objective 1.5

New audit logging coincides with a cost increase. What evidence would establish the cause?

## Question 4 Objective 2.1

CloudFormation completed, but no new connected cloud instance appears. What next?

## Question 5 Objective 2.3

Jenkins pipeline-risk scanning is connected. Does this prove code scans are configured?

## Question 6 Objective 2.5

A vendor connector authenticates, but a project produces no imported findings. What do you inspect?

## Question 7 Objective 3.3

A rule query matches an asset, but no expected policy result appears. What must be checked?

## Question 8 Objective 3.4

A trusted-image policy exists but an unwanted image still deploys. Where do you look?

## Question 9 Objective 3.6

Your custom compliance standard exists, but its assessment does not reflect a custom cloud rule. What is missing?

## Question 10 Objective 4.1

Does choosing one agent installer cover a VM, Fargate container and Lambda function?

## Question 11 Objective 4.2

An endpoint has two matching prevention policies. Which result do you expect?

## Question 12 Objective 4.4

When would you use an IOC, BIOC or correlation rule?

## Question 13 Objective 5.1

An SLA rule exists but applies to no issue. What is a key configuration check?

## Question 14 Objective 5.3

A manual cloud change produced no IaC drift issue. Why might that be expected?

## Question 15 Objective 5.5

A local CLI scan succeeds but uploading fails. What changes?

## Question 16 Objective 6.1

Your AWS organization connector reports a warning. How do you narrow the problem?

## Question 17 Objective 6.4

How do GitHub SaaS and a GitLab container registry differ when troubleshooting credentials?

## Question 18 Objective 6.5

The raw AppSec finding exists but the build is allowed. What do you inspect?

# Answer rubrics

## Answer 1

Inspect the actual license/add-ons, module permissions and prerequisites. Login proves authentication, not feature entitlement or authorization.

[Understand license plans](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/get-started/understand-license-plans); [Set up users, groups, and roles](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/set-up-users-and-roles).

## Answer 2

Confirm tenant and authentication, then RBAC, dynamic scope membership and any relevant dataset access. Compare an administrator view without granting blanket administrator rights.

[Set up users, groups, and roles](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/set-up-users-and-roles); [Manage user scope](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/post-deployment-steps/manage-user-roles-and-access-management/manage-user-scope).

## Answer 3

Compare the existing and new log paths, trail/data-event settings and usage changes by service/account/region. Treat duplication as a hypothesis until the delivery and billing evidence agree.

[Cortex Cloud and AWS audit log collection architecture](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/cortex-cloud-and-aws-audit-log-collection-architecture); [AWS Cost Explorer filtering](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-filtering.html); [AWS Cost Explorer data freshness and daily costs](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-exploring-data.html).

## Answer 4

Check the registration Lambda and its CloudWatch errors and confirm the deployment notified Cortex; inspect the documented manual connection recovery if needed.

[AWS post-deployment verification](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/aws-post-deployment-verification).

## Answer 5

No. The documented pipeline and code scanning paths use separate integration instances. Verify the correct integration type, generated pipeline/plugin configuration and a fresh attributed scan.

[Jenkins for CI/CD pipeline scans](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-cicd-systems/jenkins-for-cicd-pipeline-scans); [Jenkins for code scans](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/integrate-ci-tools/jenkins-for-code-scans).

## Answer 6

Check selected scan types and project/application-to-repository mappings, plus the supported ingestion modes. Verify a fresh result from a mapped project.

[Veracode](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/veracode); [Configure Semgrep ingestion](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/semgrep/configure-semgrep-ingestion).

## Answer 7

Check whether the rule is selected by the intended policy and whether the asset belongs to its scope; then inspect current findings/issues and the applicable scan/evaluation evidence.

[Create a cloud security policy](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-policies/create-a-cloud-security-policy); [Create a configuration rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules/create-a-configuration-rule).

## Answer 8

Inspect the action, cluster scope, admission-controller enablement, image trust data and other trust policies. Use trusted-image resolution semantics rather than endpoint first-match semantics.

[Trusted image cloud workload policies](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/types-of-cloud-workload-policies/types-of-cloud-workload-policies).

## Answer 9

Trace standard, control and rule associations; verify a cloud security policy includes that custom rule and targets the intended assessment assets.

[Use an assessment profile to run compliance checks on your assets](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/compliance/monitor-and-track-compliance-adherence/use-an-assessment-profile-to-run-compliance-checks-on-your-assets); [Use a built-in or custom control](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/compliance/monitor-and-track-compliance-adherence/choose-compliance-standards-from-the-compliance-catalog/use-a-built-in-or-custom-control).

## Answer 10

No. Select and validate the supported package/workflow for each deployment model, including compatibility, resources, permissions and registration.

[Create an agent installation package](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/create-an-agent-installation-package); [CaaS Workloads](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/endpoint-protection/caas-workloads); [Set up serverless function protection](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/serverless-function-runtime-security/set-up-serverless-function-protection).

## Answer 11

The agent applies the first matching rule in the ordered prevention-policy list. Confirm the effective policy and profiles on the endpoint.

[Apply profiles to endpoints](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/apply-profiles-to-endpoints).

## Answer 12

IOC: a known artifact. BIOC: suspicious behavior. Correlation: XQL-defined relationships across events/sources. Analytics also depends on its sensors/data and baseline-driven behavior.

[What are detection rules?](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/threat-management/detection-rules/what-are-detection-rules); [Analytics overview](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/threat-management/analytics/analytics-overview).

## Answer 13

Verify explicit matching criteria and preview matches; empty criteria match no cases/issues. Then inspect the first matching rule in the ordered SLA list.

[Create SLAs for case and issue resolution](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cases-and-issues/customize-cases-and-issues/create-slas-for-issue-resolution).

## Answer 14

Check live cloud/repository visibility and code-to-cloud mapping, then whether the change creates a runtime security-rule violation absent from the corresponding IaC. Drift detection is not a report of every possible difference.

[IaC Drift Detection scans](https://cortex-docs.paloaltonetworks.com/application-security/code-security/code-security-scanners/iac-drift-detection-scans); [Code to Cloud troubleshooting](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/code-to-cloud/code-to-cloud-troubleshooting).

## Answer 15

Check CLI upload permissions, Standard API key, upload mode, endpoint and owner/repo association. Use the actual scan response and exit status to distinguish authentication from validation and policy results.

[Connect Cortex CLI](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/connect-cortex-cli); [Authenticate credentials](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/connect-cortex-cli/authenticate-credentials); [Cortex CLI Cortex Cloud Application Security command line reference](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference).

## Answer 16

Open cloud instance details and inspect member accounts and individual capabilities; follow the specific permission, scan or ingestion evidence rather than relying on the top-level status.

[Troubleshoot errors on cloud instances](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/troubleshoot-errors-on-cloud-instances).

## Answer 17

Current GitHub SaaS uses a GitHub App and installation authorization; the GitLab registry connector uses a PAT. Apply the correct integration’s credential and access model.

[GitHub SaaS](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-version-control-systems/github-cloud); [Connect GitLab container registry](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/gitlab/connect-gitlab-container-registry).

## Answer 18

Finding type, scanner and scan health, policy conditions/scope, supported trigger, selected action and exceptions. A finding by itself does not identify the configured enforcement outcome.

[Create an AppSec policy](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/unified-application-security-policies/tenant-ui-workflow/create-a-policy); [Custom scan configurations](https://cortex-docs.paloaltonetworks.com/application-security/settings/application-security-settings/scan-settings/custom-scan-configurations).

# Additional prompts for all objectives

Every implementation-guide section ends with an explain-without-notes prompt. Use those 35 prompts to cover topics beyond the 18 scenarios here, including 5.2.2 after its documentation gap is resolved.
