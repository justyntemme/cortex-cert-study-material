# Application and analysis practice

These 12 original scenarios supplement the existing 18 questions. Level labels follow the distinction in your meeting notes: application uses a feature; analysis connects features and evidence. They are not exam items. Our two-application-to-one-analysis practice mix is a scheduling choice, not a claim about exam percentages.

Answer the prompt before reading the rubric. Then implement or reproduce the associated lesson's lab, record your evidence, and repeat with one changed input. For every analysis answer, state: hypothesis, supporting observation, next discriminating check, minimal correction, and proof of recovery. Keep access-dependent walkthroughs distinct from live results.

Use a 0–3 study rubric: 0 unsupported guess; 1 partial answer; 2 correct application with a source and verification; 3 justified diagnosis/tradeoff with alternatives and recovery evidence. Record attempts in [practice-progress.csv](practice-progress.csv).

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
