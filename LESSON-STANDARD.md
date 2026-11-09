# Lesson and lab standard

This is our study-design agreement, based on your requirement for documentation-driven lessons. It is not a Palo Alto Networks exam policy or an assertion that every existing exercise has passed the review below.

Your clarified meeting guidance prioritizes application and analysis; [the learning profile](notes/LEARNING-PROFILE.md) distinguishes the presenters' guidance from Louise's CLI/Cytool advice. Start weak topics early, pair each technical concept with a practice step, and revisit it through changed-condition questions. Preserve the full blueprint and the original labs.

## Required lesson structure

1. **Exam objective and lesson outcome.** Identify the exact blueprint objective/sub-objective. State what you should be able to explain, configure, verify, and diagnose after the lesson.
2. **Documented concepts.** Teach the behavior and prerequisites before asking you to implement them. Link each factual paragraph, table row, permission requirement, command, default, limitation, and ordering rule to the official page and relevant section. A source list at the start of an objective is reading material; it does not establish that every later assertion is supported.
3. **Implementation choice.** Explain the documented options and the conditions that make one suitable. Identify a vendor recommendation only when the source actually recommends it. Label our selection for a small sandbox as a lab-design choice, with its rationale and tradeoffs. Avoid presenting “best” as unconditional.
4. **Lesson-to-lab mapping.** Give each taught concept an ID and map every lab step to one of those IDs. If a step introduces another prerequisite or feature, teach and source it first. Preserve all blueprint objectives, including unavailable integrations.
5. **Implementation.** Give the inputs, roles, scope, version-specific UI or command, and expected change. Link the supporting procedure beside the step. Use the tenant-generated template/command where the documented workflow generates one; do not invent IDs, endpoints, permissions, flags, or click paths.
6. **Verification.** Separate documented behavior, our predicted result for the fixture, and the result actually observed in the sandbox. Include a positive case and a control case when useful. Do not invent ingestion times or assume an empty result proves success.
7. **Diagnosis and recovery.** Explain which evidence distinguishes causes, then practice a supported fault and correction within the disposable lab scope. Link the relevant diagnostic procedure. Record cleanup and the restored state.
8. **Application and analysis.** Ask an original application question about the feature, then an analysis question combining it with earlier lessons. Give a source-linked answer and explain why plausible alternatives do not satisfy the scenario. These are study questions, not claimed exam items.

## Evidence labels

| Label | Required support |
| --- | --- |
| Documented behavior | Official product procedure/reference, section, version where applicable, and access date |
| Vendor recommendation | Official text that actually recommends the choice, including its conditions |
| Lab-design choice | Explicitly our choice; explain the learning purpose and scope |
| Observed result | Dated sandbox evidence, product version, inputs, and actual output |
| Unverified | State what is missing; do not teach it as established fact or mark the objective verified |

Use official Cortex Cloud documentation for Cortex behavior, version-matched Cortex agent documentation for Cytool, and official AWS/provider documentation for that provider's behavior. A blueprint establishes scope, not an implementation procedure. Internal lessons can guide the curriculum; product assertions in those lessons still need their technical references.

When current documentation, a course, the blueprint, and the tenant differ, record the conflict and affected version. Do not silently combine procedures from different releases. Keep the unresolved part open until the correct procedure or exam scope is established.

## Current review status

The implementation guide maps all supplied objective IDs to readings and exercises, but its existing citations are primarily grouped by objective. It still needs a paragraph/step-level support review and explicit taught-concept-to-lab mapping before it can be described as meeting this stricter standard throughout. A working URL alone is not proof that the cited page supports a claim. No lab is marked as executed by the author.

Objective 5.2.2 remains an explicit documentation gap. Related AppSec policy documentation must not be presented as proof of the exact AI-recommended guardrails workflow.

Use [the lesson template](notes/LESSON-TEMPLATE.md) for expanded lessons and [the evidence template](evidence/TEMPLATE.md) to record execution.
