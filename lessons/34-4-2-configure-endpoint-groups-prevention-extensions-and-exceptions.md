# Lesson 34: Configure endpoint groups, prevention, extensions, and exceptions

Week 5 · Lesson 34 of 45 · Objective/exercise 4.2

[Course start](../README.md) · [Previous lesson](33-4-1-deploy-agents-to-vms-caas-kubernetes-and-functions.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 4.2, 4.2.1, 4.2.2. **Practice mode:** Implement.

**Read first:** [Set up endpoint profiles and exception rules](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/set-up-endpoint-profiles-and-exception-rules); [Define endpoint groups](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/define-endpoint-groups); [Apply profiles to endpoints](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/apply-profiles-to-endpoints); [Set up exception profiles and rules](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/set-up-endpoint-profiles-and-exception-rules/set-up-exception-profiles-and-rules); [File Integrity Monitoring (FIM)](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/endpoint-protection/file-integrity-monitoring-fim).

1. Create a static and a dynamic endpoint group under Inventory → Endpoints → Groups. Verify membership using actual registered lab endpoints.
2. Create or clone the appropriate malware, exploit, restrictions, and agent-settings profiles for your lab platform. Review their settings before assignment.
3. Create a Prevention policy rule, attach the profiles, target the lab group, and deliberately position it in the ordered policy list. Verify the effective policy on the endpoint.
4. For an extension example, configure a FIM rule group for a harmless lab directory, create a FIM extension profile, and assign it through an Extensions policy. Check the FIM license/agent prerequisites first; modify a test file and find its event.
5. Create a narrowly scoped exception using the documented exception type applicable to your benign test. Compare behavior with and without it, then remove the exception.
6. Export or record the final policy configuration, membership, effective profile, and rollback steps.

**Verify and save:** Effective endpoint policy, a FIM event where licensed, and an exception test with restoration.

**Explain without notes:** Why can creating a profile have no effect until a policy assigns it? How does the first matching endpoint policy affect the result?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [35. CY B Choose commands from the symptom](35-cy-b-cy-b-choose-commands-from-the-symptom.md)**
