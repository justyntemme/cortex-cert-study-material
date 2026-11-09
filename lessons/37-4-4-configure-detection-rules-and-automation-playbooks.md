# Lesson 37: Configure detection rules and automation playbooks

Week 5 · Lesson 37 of 45 · Objective/exercise 4.4

[Course start](../README.md) · [Previous lesson](36-4-3-integrate-api-gateways.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 4.4, 4.4.1, 4.4.2. **Practice mode:** Implement.

**Read first:** [What are detection rules?](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/threat-management/detection-rules/what-are-detection-rules); [Create a correlation rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/threat-management/detection-rules/what-are-detection-rules/whats-a-correlation-rule/create-a-correlation-rule); [Test your playbook](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cases-and-issues/investigation-and-response/automation/playbooks/build-your-playbook/test-your-playbook); [Create a BIOC rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/threat-management/detection-rules/what-are-detection-rules/whats-a-bioc/create-a-bioc-rule); [Create an IOC rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/threat-management/detection-rules/what-are-detection-rules/whats-an-ioc/create-an-ioc-rule); [Build your playbook](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cases-and-issues/investigation-and-response/automation/playbooks/build-your-playbook); [Analytics overview](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/threat-management/analytics/analytics-overview).

1. Choose a harmless test event already observable in your sandbox. Identify its dataset, timestamp, asset, and relevant fields before creating any rule.
2. Create a lab IOC for a benign test artifact and a BIOC for a harmless observable behavior using the documented rule builders. Save, produce matching and nonmatching activity, and verify results; label all test artifacts clearly.
3. Create an XQL correlation rule, test the query, choose its schedule or supported real-time mode, map issue fields, and configure suppression and the action. Use a dataset output while tuning, then test issue generation in the lab.
4. Inspect Analytics configuration, available sensors, and an analytics-generated example. Explain what data the engine uses and why one manually generated event does not prove a baseline-driven analytics detector is working.
5. Build a small playbook with input validation, a condition, a manual review step, and a harmless enrichment or lab-only remediation task. Attach it to the appropriate test workflow.
6. Debug using mock issue data, breakpoints, and explicit input/output checks. Inspect actual external actions before running tasks; the debugger is not a guarantee that external commands are side-effect-free.
7. Validate the remediation against the source resource and a subsequent scan/event. Save the detection → issue → playbook → corrected-state trace.

**Verify and save:** IOC, BIOC, correlation and analytics worksheets; a tested playbook and one complete response trace.

**Explain without notes:** When should you use an IOC, BIOC, correlation rule, or analytics detection? How do you prove an automation succeeded beyond its task status?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [38. Diagnose IAM, template, organization, and ingestion failures](38-6-1-diagnose-iam-template-organization-and-ingestion-failures.md)**
