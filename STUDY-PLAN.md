# Six week Cloud Security Engineer study plan

Your active plan targets six weeks of preparation, with AWS as the primary implementation platform and documented comparisons for every other platform in the blueprint. Your sandbox is Cortex XSIAM with full XDR capabilities, tenant-admin access, and enabled modules, as you reported. Record the actual product/module versions and available cloud features in [the environment worksheet](notes/ENVIRONMENT-WORKSHEET.md).

You have **1–2 hours each weekday plus one hour per weekend**. We interpret the weekend hour as a total, giving **6–11 hours weekly** and **36–66 hours over six weeks**. The working target is **90 minutes per weekday plus 60 minutes on the weekend: 8.5 hours weekly, 51 hours total**. Use these as pacing targets based on your experience; do not remove content or downgrade live labs because of an author estimate.

**The full course remains assigned.** Follow the numbered lessons from [README.md](README.md), using the Next lesson link at the bottom of each file. All original implementation exercises, CLI/Cytool work, Kubernetes lessons and practice questions remain. Your six-week goal and available hours govern the pacing; earlier duration estimates are superseded. Walkthrough status is for unavailable environments, not a way to reduce content to match an estimate.

## Calendar and exam planning

If starting Monday November 9, 2026, the six study weeks run through December 20. December 21 is a provisional first-attempt target, subject to readiness and availability; nothing is booked. The exact February deadline is still being clarified. See [exam timing](notes/EXAM-TIMELINE.md) for the two- versus three-attempt constraint, one-voucher planning, and alternative dates.

Use June/July 2026 as the exam-era focus based on your meeting information. Current documentation supports current sandbox procedures, but does not by itself prove that a command or feature existed at exam creation. Follow [the version rules](notes/EXAM-VERSION-BASELINE.md); keep every objective in the July blueprint even if the implementation's historical wording is unresolved.

## Weekly sequence

| Week and dates | Main module | Coverage and repeated practice |
| --- | --- | --- |
| 1 • Nov 9–15 | Planning and access | 1.1–1.5; first Kubernetes concepts, CLI help and Cytool concepts |
| 2 • Nov 16–22 | Integrations and Kubernetes entry | 2.1–2.6 and children; 3.7 first implementation; 6.1/6.3/6.4 while integrating |
| 3 • Nov 23–29 | Application Security | 5.1–5.5 and children; CLI arguments/errors; 6.4/6.5 |
| 4 • Nov 30–Dec 6 | Posture and Kubernetes enforcement | 3.1–3.8; K2–K4; 6.6/6.7 |
| 5 • Dec 7–13 | Runtime and agent diagnostics | 4.1–4.4 and children; Cytool; 6.2 |
| 6 • Dec 14–20 | Troubleshooting and analysis | All 6.1–6.7; full coverage review and capstone |

Weights remain Planning 12%, Integration 16%, Posture 22%, Runtime 18%, AppSec 16%, Troubleshooting 16%. Study order reflects your known gaps, not changed exam weights. [Official blueprint](references/exam-blueprint.pdf).

## A sustainable session

For a 90-minute weekday: 10 minutes recall, 20 minutes linked lesson/documentation, 40 minutes implementation or diagnostic work, 15 minutes application/analysis answers, and 5 minutes evidence/cleanup. For a 60-minute day use 5/15/25/10/5 minutes; stop at a recorded checkpoint. An available second hour resumes unfinished lab work. One weekend hour is review and planning, not a new complex deployment.

Begin each week with your weakest unresolved topic. Keep Kubernetes, organization onboarding, CLI and Cytool in rotation from their first exposure. Use two application prompts and one analysis prompt as our practice pattern, not an asserted exam percentage. Teach each concept before its corresponding step, following [the lesson standard](LESSON-STANDARD.md).

## Daily work

Each weekday below has a 90-minute target. Scope is a learning target, not a promise that every listed integration will finish in that session. Complete the linked lesson and lab. If a session ends mid-lab, record the checkpoint and resume; use a documented walkthrough only when the required environment is unavailable. Current technical procedures live in [IMPLEMENTATION-GUIDE.md](IMPLEMENTATION-GUIDE.md), [COMMAND-LINE-LAB.md](COMMAND-LINE-LAB.md), and [KUBERNETES-BRIDGE.md](KUBERNETES-BRIDGE.md).

| Week | Monday | Tuesday | Wednesday | Thursday | Friday | Weekend • 60 min |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Baseline; 1.1 inventory and architecture | 1.2 licenses, retention, IAM and scan choice | 1.3 network; K1 cluster/context concepts | 1.4 RBAC/SBAC/API keys; CLI A help/auth | 1.5 costs; organization deployment design; CY A concepts | Recall weakest items; verify week 2 prerequisites |
| 2 | 2.1 AWS deployment and capability checks | Organization/OU and Outpost; Azure/GCP/OCI comparison | 3.7/K2 connector; 2.6 Broker worksheet and deployment checkpoint | 2.3 GitHub/Jenkins; 2.4 registries | 2.2 data/AI sources; 2.5 vendor/SARIF ingestion | Review integration evidence and 6.1/6.3/6.4 diagnostic cases |
| 3 | 5.1 applications/SLAs; 5.3 scanner configuration | 5.5 CLI B local/uploaded scans; 5.4 IDE workflows | 5.2.1/5.2.3 rules and policies; keep 5.2.2 gap visible | CLI C errors; 6.4/6.5 troubleshooting | 5.3 drift and lineage; fix/rescan; remaining 5.2.2 source work | Application/analysis cases L1–L4, A1–A2; weak-topic recall |
| 4 | 3.2 groups; 3.1 XQL/dashboard | 3.3 configuration/identity/network rules | 3.3 data/AI/attack-path; 3.8 classification | 3.4/3.5 workload/vulnerability controls; K3/K4 admission | 3.6 compliance chain; remaining 3.7 connector checks | L5–L6/A4/A6; access/cost cases 6.6/6.7 |
| 5 | 4.1 VM/Kubernetes; CY A baseline | 4.1 CaaS/serverless; compare supported deployments | 4.2 profiles/groups/extensions/exceptions; CY B/6.2 | 4.3 AWS API Gateway; Azure APIM/Apigee comparison | 4.4 detections/analytics/playbook; capture missing prerequisites | Cytool selection, A3, remaining runtime gaps |
| 6 | 6.1/6.3 onboarding/Outpost faults | 6.2/6.6 agents and scoped access | 6.4/6.5 integrations/scanning; 6.7 cost diagnosis | Capstone: explain code → deployment → posture/runtime evidence | Fresh scenarios; audit all 46 IDs; readiness decision | Light recall and logistics if ready; otherwise targeted remediation |

Week 3 overlaps U.S. Thanksgiving. No extra holiday study time is assumed. If work or family commitments reduce the week, revise the dated plan and attempt targets explicitly.

## Live work and platform comparisons

Prioritize available AWS labs: account/organization integration, a small VM, ECR/image, private synthetic data, a supported Kubernetes cluster, and the applicable serverless/API examples. Do not treat AWS Organization access or a cluster as provisioned until verified. Follow the specific linked procedures in [the platform map](notes/PLATFORM-MAP.md).

For every other named platform, study its actual permissions, identity model, scope, deployment steps, capabilities, verification and failure modes. Produce its procedure worksheet now, then upgrade it to live evidence if the environment becomes available. AWS credentials, resource hierarchy and deployment templates are not substitutes for another provider's procedure.

## Completion and readiness

- All 46 IDs have an explanation with sources and a status: read, configured, verified, documented walkthrough, or unresolved. No deployment is implied by a walkthrough.
- For the known gaps, demonstrate a working procedure and diagnose a changed condition; repeated confidence ratings alone are insufficient.
- Use the original 18 scenarios and added 12 scenarios, explain alternatives, and separate raw logs/status from inferred causes. The scoring thresholds in the extended plan are study targets, not validated predictors of passing.
- Finish the source review for material being studied, and resolve objective 5.2.2 before calling the curriculum complete. A scheduled exam is not proof of readiness.
- If behind at the end of week 2 or week 4, use available second hours for the highest-priority gaps and update the attempt plan. Do not silently turn the six-week route into 16-hour weeks or mark unperformed labs complete.

## After the first attempt

If successful, use the course for continued job practice as desired. If unsuccessful, use the domain feedback and your evidence gaps to focus the next available study period, subject to the official waiting period in [the exam timeline](notes/EXAM-TIMELINE.md). Maintain the same 6–11-hour weekly budget. Reserve additional exam funding only after verifying voucher terms; no purchase or registration has been made.
