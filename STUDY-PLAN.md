# Cloud Security Engineer study plan

Use **six weeks**, with one primary exam domain per week and roughly **12–14 hours weekly** for the broad implementation coverage you requested. Runtime may take less time because you already focus on CWP. At 8–10 hours weekly, spread the same sessions across about eight to eleven weeks. These are planning estimates, not a vendor-required duration or a prediction of passing.

A four-week route is included below. It requires roughly **18–20 hours weekly** and still covers every domain; it does not omit AppSec or troubleshooting to fit the calendar.

## Exam scope

Your PDF identifies the **Palo Alto Networks Cloud Security Engineer** certification and these six weighted domains. Keep this blueprint as the scope reference even when current documentation changes a feature name. [Official exam blueprint](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/palo-alto-networks-cloudsec-engineer.pdf).

| Week | Primary module | Exam weight | Objectives | Practical result |
| --- | --- | --- | --- | --- |
| 1 | Planning and Installation | 12% | 1.1–1.5 | Deployment design, license/IAM/network matrices, scoped access |
| 2 | Integration | 16% | 2.1–2.6 and children | Verified AWS integration and rehearsed multicloud/data/development integrations |
| 3 | Posture Security | 22% | 3.1–3.8 | Rules, scoped policies, compliance report, data classification, Kubernetes connector |
| 4 | Runtime Security | 18% | 4.1–4.4 and children | Agents, endpoint policies, API ingestion, detections, tested response workflow |
| 5 | Application Security | 16% | 5.1–5.5 and children | Application context, repository/IDE/CLI scans, policy tests and drift exercise |
| 6 | Troubleshooting | 16% | 6.1–6.7 | Fault diagnosis, recovery evidence, full-scope review |

The weighting is from the PDF. Session order and time allocations below are the proposed study method. The implementation guide supplies the technical sources and procedures for every session.

## How to use each session

Reserve about two hours per session: 25 minutes for the relevant documentation sections, 70 minutes for configuration and verification, 15 minutes for retrieval practice, and 10 minutes for evidence and cleanup. Some deployments span sessions. Read only the assigned sections first; use the full linked pages as references when a prerequisite or failure requires them.

For each objective, answer: What problem does it solve? What are the prerequisites? How do I configure it? How do I prove it works? What commonly prevents it from working? Record your answer and supporting source in [the evidence template](evidence/TEMPLATE.md).

Use [the command-line lab](COMMAND-LINE-LAB.md) for Louise’s Cortex CLI/Cytool suggestions: week 4 for agent diagnostics, week 5 for CLI arguments and exit codes, and week 6 for fault analysis.

Revisit earlier material for ten minutes at the start of each session. Write original scenario questions from your labs; do not rely on memorizing interface positions.

## Week 1 Planning and Installation

| Session | Work | Evidence to keep |
| --- | --- | --- |
| 1 | Read PDF pages 2–5; baseline your confidence for all 46 numbered items; implement 1.1 | Inventory, architecture diagram, initial tracker |
| 2 | 1.2: inspect licenses, retention, IAM and scan models | Capability/entitlement matrix and deployment decision |
| 3 | 1.3: verify regional connectivity from each component location | Network matrix and successful/failed checks |
| 4 | 1.4: roles, scopes, test identity and API key lifecycle | Allowed/denied access results |
| 5 | 1.5: audit logging and scan cost baseline | Existing/proposed data-flow diagram and cost baseline |
| 6 | Rebuild the deployment design from memory; explain it; resolve prerequisite gaps | One coherent deployment worksheet and weak-topic list |

**Exit check:** Explain how your design meets its coverage, IAM, connectivity, retention, and cost requirements. Demonstrate a scoped user and a revoked API key. Sources and steps: implementation guide 1.1–1.5.

## Week 2 Integration

| Session | Work | Evidence to keep |
| --- | --- | --- |
| 1 | 2.1: implement AWS account onboarding and verify individual capabilities | Connected instance, assets, scan results, logs |
| 2 | 2.1.1–2.1.2: organization/OU and Outpost exercises; compare Azure, GCP, OCI | Organization deployment or explicit walkthrough; provider comparison |
| 3 | 2.2: Microsoft 365, Databricks, AI source walkthroughs | Permissions, fields, scan-mode and discovery worksheets |
| 4 | 2.3–2.4: GitHub, Jenkins and registries | Repository/commit scan and registry scan |
| 5 | 2.5: vendor ingestion and Generic SARIF exercise | Mapped synthetic finding and upload result |
| 6 | 2.6: Broker VM deployment/configuration; review an integration failure | Registration, collector data, integration health checklist |

**Exit check:** Explain every example provider and integration named in the blueprint. For systems you can access, prove fresh data arrival. For unavailable systems, show complete configuration and troubleshooting worksheets. A single-account lab does not satisfy the organization deployment check.

## Week 3 Posture Security

| Session | Work | Evidence to keep |
| --- | --- | --- |
| 1 | 3.2 and 3.7: asset groups and Kubernetes connector | Membership, connector health, discovered workloads |
| 2 | 3.3: configuration, identity and network rules | Tested rule logic and scoped policy |
| 3 | 3.3: data, AI and attack-path rules; 3.8 classification | Remaining rule worksheets and synthetic classification |
| 4 | 3.4–3.5: workload rules/policies, trusted images and vulnerability policies | Positive/negative policy tests; admission result |
| 5 | 3.6: standards, controls, assessment and reporting | Custom control chain and compliance report |
| 6 | 3.1: XQL dashboard; explain and remediate selected findings | Working dashboard and before/after findings |

**Exit check:** Demonstrate rule → policy → scope → result, and standard → control → rule → assessment. Explain the difference between an issue and a blocked action. Leave positive-result tests pending if the sandbox lacks the required data.

## Week 4 Runtime Security

| Session | Work | Evidence to keep |
| --- | --- | --- |
| 1 | 4.1: VM and Kubernetes deployment | Registration, operational state, coverage |
| 2 | 4.1: CaaS and serverless deployment variants | Build/deployment records and runtime evidence |
| 3 | 4.2: endpoint groups, prevention, extension and exception | Effective policy and harmless FIM event |
| 4 | 4.3: AWS API Gateway and APIM/Apigee walkthroughs | Request-to-Cortex trace and provider worksheets |
| 5 | 4.4.1: IOC, BIOC, correlation and analytics | Rule tests and telemetry prerequisites |
| 6 | 4.4.2: build/debug a playbook and validate its result | Detection-to-remediation evidence |

**Exit check:** Show coverage for all four workload deployment forms, effective policy assignment, an API ingestion path, and a tested response. Spend saved CWP review time on any weak posture/integration topic.

## Week 5 Application Security

| Session | Work | Evidence to keep |
| --- | --- | --- |
| 1 | 5.1: manual/dynamic business applications and SLAs | Application membership, lineage, SLA result |
| 2 | 5.3: IaC, SCA, secrets and repository configuration | Scan/fix/rescan evidence |
| 3 | 5.2.1 and 5.2.3: custom rule, code policy and CI/CD policy | Matching/nonmatching enforcement tests |
| 4 | 5.4–5.5: IDEs, CLI authentication, local/uploaded/CI scans | Reproducible scan and correct repository attribution |
| 5 | 5.3: IaC drift and code-to-cloud mapping | Drift test and correction from code |
| 6 | 5.2.2: resolve exact AI-recommended guardrails documentation; review all AppSec flows | Vendor-supported procedure or explicitly open gap; full application trace |

**Exit check:** Follow a finding from developer tooling through CI and a deployed asset, fix it, and confirm the outcome. Distinguish scanner configuration from policy enforcement. Do not close 5.2.2 by substituting an ordinary policy for its named feature.

## Week 6 Troubleshooting and exam readiness

| Session | Work | Evidence to keep |
| --- | --- | --- |
| 1 | 6.1: IAM/template/organization/ingestion failures | Cause, minimal fix, fresh data after recovery |
| 2 | 6.2–6.3: agent, connector and Outpost failures | Component diagnosis and restored scan/event |
| 3 | 6.4–6.5: credentials, webhooks, scanner and policy failures | Fresh PR/build and repaired configuration |
| 4 | 6.6–6.7: access failures and cost investigation | Scoped repair and supported cost explanation |
| 5 | Perform the capstone below and answer the scenario questions without notes | Complete application trace and corrected answers |
| 6 | Revisit every unchecked item; use the official learning path and current exam registration information | Final gap list and go/defer decision |

**Exit check:** For each fault, identify evidence that supports the diagnosis, make a minimal correction, prove recovery, and preserve the intended access/security boundary.

## Capstone

Using the same lab application, explain its deployment design, integrations, scope, policies, runtime protection, and developer controls. Demonstrate one code or dependency finding, one posture result, one runtime event, one compliance assessment, and one tested remediation. Select one reversible fault and diagnose it without being told its cause. Record missing links instead of claiming a complete trace where correlation is absent. Technical procedures: implementation objectives 2.1, 2.3, 3.3–3.7, 4.1–4.4, 5.1–5.5, and 6.1–6.6.

## Four week accelerated route

Use this only if you can reserve roughly 18–20 focused hours weekly and prerequisites are ready. It rearranges the same implementation guide rather than removing objectives.

| Week | Theme | Coverage |
| --- | --- | --- |
| 1 | Platform deployment and integration | All domain 1 and 2 objectives; troubleshoot 6.1 and 6.3 while deploying |
| 2 | Posture security | All domain 3 objectives; reinforce 6.6 and 6.7 |
| 3 | Runtime security | All domain 4 objectives; implement 6.2; review integration failures |
| 4 | Application security and final validation | All domain 5 objectives; implement 6.4 and 6.5; capstone and all-domain review |

If a lab or exit check is incomplete, add time. A calendar deadline is not evidence of exam readiness.

## Readiness criteria

These are study targets, not an official exam passing score.

- Every numbered objective has a documented explanation and an implementation record or clearly identified access-dependent walkthrough.
- You can repeat your available-environment core labs without following your previous notes line by line.
- You can diagnose fresh scenarios by identifying the missing permission, scope, data, connectivity, or enforcement prerequisite.
- Aim for at least 80% on two different sets of your own blueprint-balanced practice scenarios, with no domain below 70%; explain why alternative answers are wrong.
- Close the AI-recommended guardrails documentation gap and revisit any feature that differs in your tenant release before treating the tracker as complete.
- Use the official certification page to open the current digital learning path and exam-registration resources. The linked learning portal required an interactive session, so no course titles or mock-exam availability are asserted here. Exam-specific duration and question count remain unverified; the official program's scaled-score policy and remaining questions are recorded in [exam details](notes/EXAM-QUESTIONS.md). [Official certification and training links](https://www.paloaltonetworks.com/services/education/palo-alto-networks-cloudsec-engineer).

## Foundational skills from the PDF

The PDF also lists prerequisites beyond its numbered objectives: networking/TCP/IP, endpoint operating systems and hardening, cloud security boundaries, containers/Kubernetes, Terraform/CloudFormation/Bicep/Helm, JSON/YAML, SAML/OIDC/OAuth, IAM, compliance frameworks, CVSS, cloud CLIs, Linux, and REST API tooling. Assess these during week 1; they are prerequisites rather than additional weighted domains. [Supplied blueprint, pages 2–3](references/exam-blueprint.pdf).

Use the deployment/network exercises for networking and IAM; agent and connector exercises for OS/container fundamentals; policy and code exercises for IaC/JSON/YAML; identity/integration exercises for authentication; assessment exercises for controls; vulnerability exercises for CVSS/context; and generated templates/CLI/collector workflows for command-line and API practice. Read and explain a Bicep and Helm example from the supported AppSec frameworks even if AWS is your implementation platform. Add foundation sessions if you cannot explain these inputs before the associated lab.
