# Lesson 11: Deploy the Kubernetes connector

Week 2 · Lesson 11 of 45 · Objective/exercise 3.7

[Course start](../README.md) · [Previous lesson](10-2-6-deploy-and-configure-broker-vm.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 3.7. **Practice mode:** Implement.

**Read first:** [Onboard the Kubernetes Connector](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/onboard-the-kubernetes-connector); [Trusted image cloud workload policies](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/types-of-cloud-workload-policies/types-of-cloud-workload-policies).

1. Use a disposable supported Kubernetes cluster. Open Data Sources & Integrations and add Kubernetes.
2. Choose Posture Management and, when licensed, Realtime Protection. Inspect advanced settings including scan cadence, admission-controller enforcement, and agent-related options.
3. Download the generated installer and review its requested cluster permissions and settings. Execute the generated instructions against the intended kubectl context.
4. Verify connector status, discovered cluster/namespaces/workloads, and scanner results. Keep posture collection and runtime protection validation as separate checks.
5. Test admission enforcement with the harmless trusted-image policy from 3.4. Confirm a permitted deployment still works, then restore the lab policy state.

**Verify and save:** Installer configuration, healthy connector evidence, discovered workload, and one scoped enforcement test.

**Explain without notes:** Why is a connected posture connector not sufficient proof that runtime prevention is active?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [12. K2 Review permissions and onboard the connector](12-k2-k2-review-permissions-and-onboard-the-connector.md)**
