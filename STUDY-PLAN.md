# Cloud Security Engineer study plan

Start unfamiliar skills early and revisit them throughout the course. Your Docker contribution and container-security work justify a shorter baseline review of those skills; Kubernetes, organization onboarding, and the two command-line tools receive early practice. AppSec, posture, and non-container runtime topics are provisionally high priority until the baseline shows otherwise. See [your learning profile](notes/LEARNING-PROFILE.md).

The expanded route is **eight weeks at 12–14 hours weekly**, about **96–112 hours**. A six-week route takes about **16–19 hours weekly**; a four-week route takes **24–28 hours weekly**. At 8–10 hours weekly, allow roughly 10–14 weeks. These are our planning estimates for the original coverage plus extra practice, not vendor requirements. No objectives or existing labs have been removed.

## Exam scope and study order

The six domain weights remain those in your supplied PDF. Study order changes to reflect your experience rather than the order printed in the blueprint. [Official exam blueprint](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/palo-alto-networks-cloudsec-engineer.pdf).

| Week | Primary module | Coverage | Why here |
| --- | --- | --- | --- |
| 1 | Planning and access | 1.1–1.5; initial CLI and Kubernetes exercises | Establish dependencies and expose gaps immediately |
| 2 | Integration | 2.1–2.6 and children; first organization and connector rehearsals | Organization onboarding is a known gap |
| 3 | Application Security | 5.1–5.5 and children; Cortex CLI | Earlier than before, allowing five further weeks of review |
| 4 | Kubernetes and agent diagnostics | Deep practice for 3.7, Kubernetes part of 4.1, 3.4, 6.2; Cytool | Dedicated time for your stated Kubernetes gap |
| 5 | Posture Security | 3.1–3.8; repeat Kubernetes policy tests | Build on the deployed environment and earlier concepts |
| 6 | Runtime Security | 4.1–4.4 and children | Familiar container work later; preserve non-container runtime coverage |
| 7 | Troubleshooting | 6.1–6.7 | Diagnose without being told the cause |
| 8 | Application and analysis review | All 46 objectives; capstone and weak-area retests | Additional practice, not replacement coverage |

| Exam domain | Weight |
| --- | --- |
| Planning and Installation | 12% |
| Integration | 16% |
| Posture Security | 22% |
| Runtime Security | 18% |
| Application Security | 16% |
| Troubleshooting | 16% |

## How to use each session

Use a two-hour session: 10 minutes of recall from an earlier weak topic, 25 minutes of linked documentation and lesson explanation, 55 minutes of implementation, 20 minutes of application/analysis questions, and 10 minutes for evidence and cleanup. Six sessions provide 12 hours; the optional two hours are for failed checks and deployment delays.

For every objective, first explain the concept with its technical source. Then perform its lab, predict the result, compare the observation, and diagnose a changed condition. Follow [the lesson standard](LESSON-STANDARD.md); legacy sections with grouped references still require paragraph/step-level review before being treated as fully audited lessons.

Use two single-feature application prompts for each cross-feature analysis prompt as our starting exercise mix. This ratio is a study choice, not a claimed exam percentage. Your meeting notes identify application as the bulk of the exam and describe analysis questions; Louise separately recommends Cortex CLI and Cytool. [Meeting provenance and learner profile](notes/LEARNING-PROFILE.md).

## Early practice and repeated review

These exercises occupy the retrieval, practice, and review periods above. If setup consumes that time, extend the schedule rather than omit a topic.

| Topic | First exposure | Implementation | Later review |
| --- | --- | --- | --- |
| AWS organization, IAM and Outpost | Week 1 architecture/permissions | Week 2 | Weeks 3, 5, 7, 8 |
| Cortex CLI arguments and error evidence | Week 1 CLI A | Week 3 CLI B and C | Weeks 4, 5, 7, 8 |
| Kubernetes concepts | Week 1 K1 | Week 2 K2 rehearsal; week 4 K2–K4 execution | Weeks 5, 6, 7, 8 |
| Cytool arguments and diagnostics | Week 1 CY A reading/help if agent available | Week 4 CY A and B on disposable VM | Weeks 5, 6, 7, 8 |
| AppSec and code-to-cloud | Week 2 repository integration | Week 3 | Weeks 4, 5, 7, 8 |
| Docker and familiar container security | Week 1 short diagnostic | Week 2 registry integration; week 6 validation | Week 8 and whenever a gap appears |

Use [COMMAND-LINE-LAB.md](COMMAND-LINE-LAB.md), [KUBERNETES-BRIDGE.md](KUBERNETES-BRIDGE.md), and [APPLICATION-ANALYSIS.md](APPLICATION-ANALYSIS.md). Begin each week with the weakest unresolved evidence-backed gap. A high confidence rating alone does not remove a lab.

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
## Week 3 Application Security

| Session | Work | Evidence to keep |
| --- | --- | --- |
| 1 | 5.1: manual/dynamic business applications and SLAs | Application membership, lineage, SLA result |
| 2 | 5.3: IaC, SCA, secrets and repository configuration | Scan/fix/rescan evidence |
| 3 | 5.2.1 and 5.2.3: custom rule, code policy and CI/CD policy | Matching/nonmatching enforcement tests |
| 4 | 5.4–5.5: IDEs, CLI authentication, local/uploaded/CI scans | Reproducible scan and correct repository attribution |
| 5 | 5.3: IaC drift and code-to-cloud mapping | Drift test and correction from code |
| 6 | 5.2.2: resolve exact AI-recommended guardrails documentation; review all AppSec flows | Vendor-supported procedure or explicitly open gap; full application trace |

**Exit check:** Follow a finding from developer tooling through CI and a deployed asset, fix it, and confirm the outcome. Distinguish scanner configuration from policy enforcement. Do not close 5.2.2 by substituting an ordinary policy for its named feature.
## Week 4 Kubernetes and agent diagnostics

| Session | Work | Evidence to keep |
| --- | --- | --- |
| 1 | K1: context, control plane, nodes, Pods, Deployments and DaemonSets | Explain each object and inspect an existing application |
| 2 | K2: permissions and Cortex connector; finish 3.7 implementation | Generated installer review, deployed objects and connector status |
| 3 | K3: Kubernetes runtime coverage from 4.1; CY A on separate Linux VM | Eligible-node comparison and diagnostic baseline |
| 4 | K4: admission and trusted-image policy from 3.4 | New permitted/denied deployment evidence and restored policy |
| 5 | CY B and 6.2: correlate connectivity, check-in and collection evidence | Root-cause hypotheses, correction and retest |
| 6 | Solve Kubernetes and CLI analysis cases; repeat failed checks | Commands selected from the symptom, explanations and source links |

**Exit check:** Explain what each component proves and what it leaves unproven. Docker image familiarity does not exempt cluster permissions, scheduling, admission, or telemetry validation. Use the linked Kubernetes and command-line lessons for procedures.

## Week 5 Posture Security

| Session | Work | Evidence to keep |
| --- | --- | --- |
| 1 | 3.2 and 3.7: asset groups and Kubernetes connector | Membership, connector health, discovered workloads |
| 2 | 3.3: configuration, identity and network rules | Tested rule logic and scoped policy |
| 3 | 3.3: data, AI and attack-path rules; 3.8 classification | Remaining rule worksheets and synthetic classification |
| 4 | 3.4–3.5: workload rules/policies, trusted images and vulnerability policies | Positive/negative policy tests; admission result |
| 5 | 3.6: standards, controls, assessment and reporting | Custom control chain and compliance report |
| 6 | 3.1: XQL dashboard; explain and remediate selected findings | Working dashboard and before/after findings |

**Exit check:** Demonstrate rule → policy → scope → result, and standard → control → rule → assessment. Explain the difference between an issue and a blocked action. Leave positive-result tests pending if the sandbox lacks the required data.
## Week 6 Runtime Security

| Session | Work | Evidence to keep |
| --- | --- | --- |
| 1 | 4.1: VM and Kubernetes deployment | Registration, operational state, coverage |
| 2 | 4.1: CaaS and serverless deployment variants | Build/deployment records and runtime evidence |
| 3 | 4.2: endpoint groups, prevention, extension and exception | Effective policy and harmless FIM event |
| 4 | 4.3: AWS API Gateway and APIM/Apigee walkthroughs | Request-to-Cortex trace and provider worksheets |
| 5 | 4.4.1: IOC, BIOC, correlation and analytics | Rule tests and telemetry prerequisites |
| 6 | 4.4.2: build/debug a playbook and validate its result | Detection-to-remediation evidence |

**Exit check:** Show coverage for all four workload deployment forms, effective policy assignment, an API ingestion path, and a tested response. Spend saved CWP review time on any weak posture/integration topic.
## Week 7 Troubleshooting and exam readiness

| Session | Work | Evidence to keep |
| --- | --- | --- |
| 1 | 6.1: IAM/template/organization/ingestion failures | Cause, minimal fix, fresh data after recovery |
| 2 | 6.2–6.3: agent, connector and Outpost failures | Component diagnosis and restored scan/event |
| 3 | 6.4–6.5: credentials, webhooks, scanner and policy failures | Fresh PR/build and repaired configuration |
| 4 | 6.6–6.7: access failures and cost investigation | Scoped repair and supported cost explanation |
| 5 | Perform the capstone below and answer the scenario questions without notes | Complete application trace and corrected answers |
| 6 | Revisit every unchecked item; use the official learning path and current exam registration information | Final gap list and go/defer decision |

**Exit check:** For each fault, identify evidence that supports the diagnosis, make a minimal correction, prove recovery, and preserve the intended access/security boundary.
## Week 8 Application and analysis review

| Session | Work | Evidence to keep |
| --- | --- | --- |
| 1 | Diagnose all CLI and Cytool cases without the answer rubrics | Raw status/log evidence and justified command selection |
| 2 | Retest organization onboarding and Kubernetes weak points | Fresh verification or explicit access-dependent walkthrough |
| 3 | Complete original scenarios 1–9 plus analysis cases A1–A3 | Correct answer, rejected alternatives, supporting docs |
| 4 | Complete original scenarios 10–18 plus analysis cases A4–A6 | Correct answer, rejected alternatives, supporting docs |
| 5 | Repeat the capstone with a different controlled fault | Timeline, causal explanation, minimal fix and recovery |
| 6 | Review all 46 IDs and new exercise tracker; retest weakest areas | Readiness decision with any gaps still visible |

**Exit check:** A correct answer must include why it fits the evidence and which next observation could disprove it. Carry unresolved areas into additional sessions.

## Capstone

Using the same lab application, explain its deployment design, integrations, scope, policies, runtime protection, and developer controls. Demonstrate one code or dependency finding, one posture result, one runtime event, one compliance assessment, and one tested remediation. Select one reversible fault and diagnose it without being told its cause. Record missing links instead of claiming a complete trace where correlation is absent. Technical procedures: implementation objectives 2.1, 2.3, 3.3–3.7, 4.1–4.4, 5.1–5.5, and 6.1–6.6.

## Compressed routes

Use the same lessons and exercises in the same dependency order. Extra sessions remain required when a check fails.

| Six-week route at 16–19 hours weekly | Eight-week material to complete |
| --- | --- |
| 1 | Week 1 planning plus early tool/Kubernetes practice |
| 2 | Week 2 integration |
| 3 | Week 3 AppSec and first half of week 4 |
| 4 | Finish week 4 and week 5 posture |
| 5 | Week 6 runtime and first half of week 7 |
| 6 | Finish week 7 and week 8 review |

| Four-week route at 24–28 hours weekly | Eight-week material to complete |
| --- | --- |
| 1 | Weeks 1–2 |
| 2 | Weeks 3–4 |
| 3 | Weeks 5–6 |
| 4 | Weeks 7–8 |

A month is now an intensive option, not the default recommendation. Preserve time for repetition by starting unfamiliar skills immediately.

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
