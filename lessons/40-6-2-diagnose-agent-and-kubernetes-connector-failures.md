# Lesson 40: Diagnose agent and Kubernetes connector failures

Week 6 · Lesson 40 of 45 · Objective/exercise 6.2

[Course start](../README.md) · [Previous lesson](39-6-3-diagnose-outpost-communication-failures.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

Use the [Cytool diagnostic exercise](../COMMAND-LINE-LAB.md) to collect local evidence before and after the fault.

**Blueprint coverage:** 6.2. **Practice mode:** Break and repair in the lab.

**Read first:** [Enable access to required PANW resources](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/activate-cortex-cloud/enable-access-to-required-panw-resources); [Onboard the Kubernetes Connector](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/onboard-the-kubernetes-connector); [Create an agent installation package](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/create-an-agent-installation-package); [Monitor agent operational status](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/manage-endpoint-protection/monitor-agent-operational-status).

1. Choose a single disposable VM or cluster connector with known working telemetry. Record last-seen time, operational state, version, and assigned policy.
2. Use a controlled lab connectivity interruption or a deliberately incorrect test installation setting. Keep the restoration command/configuration ready.
3. Check local process/pod status, installation output, generated configuration, DNS/TLS/egress, platform compatibility, and registration credentials in that order where applicable.
4. Compare endpoint/connector health with actual data arrival and scanner coverage. A running process is not sufficient evidence that Cortex can receive its telemetry.
5. Restore the original setting, produce a harmless new event, and verify current timestamps and expected policy enforcement.

**Verify and save:** A diagnosis and recovery record with a new event after restoration.

**Explain without notes:** How do you tell an unsupported host from a connectivity failure or an incorrect target policy?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [41. Diagnose user and API access problems](41-6-6-diagnose-user-and-api-access-problems.md)**
