# Lesson 45: Full scope practice and readiness review

Week 6 · Lesson 45 of 45 · Objective/exercise REVIEW

[Course start](../README.md) · [Previous lesson](44-6-7-diagnose-an-unexpected-aws-cost-increase.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

Work through both question sets below before reading each answer rubric. They are the complete existing sets, not a reduced sample. Record remaining weak areas and follow their linked documentation.

## Capstone

Using your lab application, explain its deployment design, integrations, scope, developer controls, posture and runtime protection. Demonstrate a code/dependency finding, posture result, runtime event, compliance assessment and tested remediation using the procedures from prior lessons. Diagnose one reversible fault without being told its cause. Missing evidence stays unresolved.

# Original practice scenarios

These are original study questions, not exam items or a vendor practice test. Answer without notes, then compare with the rubric and read the supporting source. Score 0 for an unsupported guess, 1 for a partly correct diagnosis, and 2 for a correct answer with evidence and verification. Use different scenarios for the second readiness check rather than memorizing these answers.

Keep these 18 questions and add the 12 in [APPLICATION-ANALYSIS.md](../APPLICATION-ANALYSIS.md). The added set uses a separate 0–3 reasoning rubric; normalize scores before comparing totals. For each original question, also ask one changed-input application question and one cross-feature analysis question using its linked sources. This supports the meeting guidance without claiming an exact exam difficulty distribution.

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


# Application and analysis practice

These 12 original scenarios supplement the existing 18 questions. Level labels follow the distinction in your meeting notes: application uses a feature; analysis connects features and evidence. They are not exam items. Our two-application-to-one-analysis practice mix is a scheduling choice, not a claim about exam percentages.

Answer the prompt before reading the rubric. Then implement or reproduce the associated lesson's lab, record your evidence, and repeat with one changed input. For every analysis answer, state: hypothesis, supporting observation, next discriminating check, minimal correction, and proof of recovery. Keep access-dependent walkthroughs distinct from live results.

Use a 0–3 study rubric: 0 unsupported guess; 1 partial answer; 2 correct application with a source and verification; 3 justified diagnosis/tradeoff with alternatives and recovery evidence. Record attempts in [practice-progress.csv](../practice-progress.csv).

## L1 Application

Objectives: 5.5. Lesson/lab: CLI A.

**Prompt:** You need a local scan of the current directory without a platform upload. Construct and explain the command.

**Answer and verification rubric:** Use `cortexcli --upload-mode no-upload code scan --directory .`. Explain the mode and input; then capture the actual scan output. Do not infer uploaded results from a local run.

[Cortex CLI common flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide); [Cortex CLI Cortex Cloud Application Security command line reference](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference).

## L2 Application

Objectives: 5.5. Lesson/lab: CLI B/C.

**Prompt:** The CLI returned 1. Can you conclude that it found a vulnerability?

**Answer and verification rubric:** No. The documented category includes findings and operational failure. Read the actual error/scan result before choosing a repair; repeat after correction.

[Cortex CLI exit codes and error handling](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/exit-codes-and-error-handling).

## L3 Application

Objectives: 6.2. Lesson/lab: CY A.

**Prompt:** You need the last successful agent check-in. Which Linux command supplies it, and how would you request another?

**Answer and verification rubric:** Use `./cytool last_checkin`, then `./cytool checkin`; compare the console check-in time. Keep this separate from proof of collected telemetry.

[Cytool for Linux 9.4](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux).

## L4 Application

Objectives: 5.5. Lesson/lab: CLI B.

**Prompt:** A colleague suggests --support just to obtain local debug output. Is it equivalent to --log-level DEBUG?

**Answer and verification rubric:** No. The common reference describes log upload as part of --support. For this local-evidence exercise, use DEBUG and the log-path option without requesting that upload.

[Cortex CLI common flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide).

## L5 Application

Objectives: 3.7;4.1. Lesson/lab: K3.

**Prompt:** The agent DaemonSet is absent from a node that does not match the configured node selector. Is that alone evidence of an installation failure?

**Answer and verification rubric:** No. Compare the selector with eligible node labels and DaemonSet desired/ready state before diagnosing failure. Check that node coverage matches the intended design.

[Onboard the Kubernetes Connector](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/onboard-the-kubernetes-connector); [DaemonSets](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/).

## L6 Application

Objectives: 3.4;3.7. Lesson/lab: K4.

**Prompt:** A newly created trusted-image policy generates issues but does not reject your test deployment. Which action and prerequisite do you inspect?

**Answer and verification rubric:** Check issue-only versus prevention action, cluster scope and enabled admission. An issue-only policy is not a blocking control. Rerun with a new lab workload after correcting the intended configuration.

[Trusted image cloud workload policies](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/types-of-cloud-workload-policies/types-of-cloud-workload-policies).

## A1 Analysis

Objectives: 1.4;5.5;6.5. Lesson/lab: CLI B/C.

**Prompt:** A pipeline is green, and no new Cortex scan is visible. The invocation uses no-upload and an error-suppression flag. Explain two separate gaps in the evidence.

**Answer and verification rubric:** No-upload does not send scan results; suppressed status can conceal a finding or execution failure. Inspect raw logs, mode and status first. Then verify upload credentials, repository attribution and an actual platform scan. A single green status cannot resolve these hypotheses.

[Cortex CLI common flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide); [Cortex CLI exit codes and error handling](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/exit-codes-and-error-handling); [Connect Cortex CLI](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/connect-cortex-cli); [Cortex CLI Cortex Cloud Application Security command line reference](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference).

## A2 Analysis

Objectives: 2.3;5.5;6.4. Lesson/lab: CLI B/C.

**Prompt:** An upload completes, but the team cannot find it under the expected repository/branch. Where do you investigate before granting broader access?

**Answer and verification rubric:** Compare the invocation and detected Git context with the expected owner/repo and branch. The repo-id is not a tenant asset hash. Verify the corrected scan attribution; if visibility remains different between users, investigate role/scope with evidence rather than assuming attribution was the only cause.

[Cortex CLI Cortex Cloud Application Security command line reference](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference); [Manage user scope](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/post-deployment-steps/manage-user-roles-and-access-management/manage-user-scope).

## A3 Analysis

Objectives: 4.1;6.2. Lesson/lab: CY B.

**Prompt:** Agent components are running, check-in is fresh, but an expected event is missing. What does each observation establish, and what remains to test?

**Answer and verification rubric:** Component and communication evidence do not identify the missing-event cause. Inspect collection status, logs and agent operational state; compare the event type, timing and configured policy with the expected data. Prove recovery with a new supported benign event, not merely another check-in.

[Cytool for Linux 9.4](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux); [Monitor agent operational status](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/manage-endpoint-protection/monitor-agent-operational-status).

## A4 Analysis

Objectives: 3.4;3.7;4.1. Lesson/lab: K2–K4.

**Prompt:** Cortex discovers the cluster. A test image still deploys, while runtime coverage is missing on selected nodes. Diagnose these as separate paths.

**Answer and verification rubric:** Inspect policy action/scope and admission for the new deployment. Separately inspect the runtime capability, node eligibility and agent DaemonSet state. Discovery alone does not establish either requested enforcement outcome. Verify admission and runtime independently after correction.

[Trusted image cloud workload policies](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/types-of-cloud-workload-policies/types-of-cloud-workload-policies); [Onboard the Kubernetes Connector](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/onboard-the-kubernetes-connector); [DaemonSets](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/).

## A5 Analysis

Objectives: 2.1;6.1;6.3. Lesson/lab: Implementation 2.1 and 6.1–6.3.

**Prompt:** The organization deployment completed, but one member account has no expected scan results. Explain how you narrow scope and capability issues.

**Answer and verification rubric:** Use the documented cloud-instance checks to identify the account, region and failing capability; inspect deployment scope and the corresponding permission/registration errors. A completed template does not identify which capability supplied data. Correct the evidenced cause and validate a new result in that member account.

[AWS post-deployment verification](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/aws-post-deployment-verification); [Troubleshoot errors on cloud instances](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/troubleshoot-errors-on-cloud-instances); [Deploy the authentication template in AWS](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/deploy-the-authentication-template-in-aws).

## A6 Analysis

Objectives: 3.3;3.6. Lesson/lab: Implementation 3.3 and 3.6.

**Prompt:** A rule matches your asset, but the custom compliance assessment omits the expected result. Trace the required configuration chain.

**Answer and verification rubric:** Inspect the standard/control rule association, cloud policy inclusion and assessment scope. The assessment profile does not replace the cloud security policy for the custom cloud rule. Correct the missing link and rerun the assessment against the intended asset.

[Use an assessment profile to run compliance checks on your assets](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/compliance/monitor-and-track-compliance-adherence/use-an-assessment-profile-to-run-compliance-checks-on-your-assets); [Use a built-in or custom control](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/compliance/monitor-and-track-compliance-adherence/choose-compliance-standards-from-the-compliance-catalog/use-a-built-in-or-custom-control); [Create a cloud security policy](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-policies/create-a-cloud-security-policy).

## Extend every original objective

For each of the 35 implementation sections, add two application prompts and one analysis prompt to your evidence record. Application: select the appropriate documented action for a stated requirement, then interpret one changed input/output. Analysis: connect this objective to a previously studied integration, identity, policy, or telemetry dependency. Cite the relevant sections for the answer and rejected alternatives; if a technical claim lacks a source, keep it unresolved rather than score it as fact.


## Completion check

Review every objective in objective-tracker.csv and every added exercise in practice-progress.csv. Keep 5.2.2 open until its implementation source is resolved. Choose your next exam step using the timeline linked below; no registration is implied.


**Course complete → [Review exam timing and your readiness decision](../notes/EXAM-TIMELINE.md)**
