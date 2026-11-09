# Learning priorities and meeting guidance

## Source of the guidance

On November 9, 2026, you clarified that the Level 2 and Level 3 notes came from a meeting with exam creators, with David opening the presentation. You described Louise as someone who passed the exam, not an exam author. The original wording remains in [notes.md](../notes.md). The meeting date itself was not supplied.

- **Presenter guidance, as reported by you:** Level 2 application is the bulk of the exam: apply knowledge of a single service, product, feature, or concept to reach a conclusion. Level 3 analysis combines interconnected services/features and examines causes and effects. No numerical distribution was supplied.
- **Louise's study advice:** Learn basic Cortex CLI and Cytool arguments, including error tracking. This informs additional practice; it is not treated as an official change in blueprint weighting.
- **Your experience:** You work in CWP container security and contribute to Docker. You have limited Kubernetes experience and have not onboarded an organization.

Product facts and implementation steps still require official technical documentation. Meeting guidance determines practice emphasis, not command syntax or platform behavior.

## Initial priorities

| Area | Basis | Initial treatment |
| --- | --- | --- |
| Organization onboarding | Explicitly unfamiliar | Begin planning week 1; implement/rehearse week 2; repeat |
| Kubernetes | Explicitly less familiar | Begin foundations week 1; dedicated week 4; repeat |
| Cortex CLI and Cytool | Louise's advice; mastery not yet measured | Begin week 1; separate execution and diagnostic exercises |
| AppSec, posture, IAM, data security, API security, CDR | Familiarity unknown | Provisional high priority; baseline determines extra time |
| Docker and general container security | Reported professional strength | Short baseline; later validation; retain Cortex-specific work |

This is a starting order, not a diagnosis that every non-CWP topic is weak. Do not prefill competence or mark an objective verified from job experience alone.

## Baseline and weekly adjustment

During week 1, use one application scenario per domain from [the original question set](../PRACTICE-SCENARIOS.md), one CLI case, one Cytool case, and K1 from [the Kubernetes bridge](../KUBERNETES-BRIDGE.md). For each, explain the choice without notes, identify the supporting source, and propose the verification. An unavailable environment gets a walkthrough status, not a low knowledge score or a fabricated successful lab.

Score each attempt with our study rubric: 0 unable to explain; 1 recognizes terms but needs the procedure; 2 can apply the procedure and verify; 3 can explain tradeoffs and diagnose a changed scenario. Keep knowledge score separate from live verification.

At the end of each week, choose next week's extra practice in this order: unresolved prerequisites, failed application questions, failed analysis questions, then slow but correct responses. Revisit a new weak topic in the next session, the next week, and again two weeks later. This cadence is our study design. Preserve the planned first exposure to every domain.

For familiar container work, complete one sourced explanation, one available-environment verification, and one changed-condition diagnosis. If these succeed, use discretionary repetition time on weak topics. Keep every original exercise and objective available.
