# Lesson 28: Create workload rules and policies

Week 4 · Lesson 28 of 45 · Objective/exercise 3.4

[Course start](../README.md) · [Previous lesson](27-3-8-configure-data-classification-and-scanning.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 3.4. **Practice mode:** Implement.

**Read first:** [Cloud workload policies and rules](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules); [Trusted image cloud workload policies](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/types-of-cloud-workload-policies/types-of-cloud-workload-policies); [Create a new custom detection rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-rules/create-a-new-custom-detection-rule); [Create a cloud workload policy](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/create-a-cloud-workload-policy).

1. Create a custom Cloud Workload rule. Choose its scanner deliberately: Agentless Disk Scan, Kubernetes Connector, or XDR Agent. Use the documented example for that scanner, adapt it to a harmless lab condition, and validate the rule logic.
2. Associate the rule with a custom compliance control where required. Explain the input data and execution mechanism for each scanner, even if only one scanner is available.
3. Create separate lab-scoped misconfiguration, malware, secrets, and trusted-image policy configurations. Inspect the available stages/actions for each type; do not assume every rule supports prevention.
4. Start with issue creation. Use an available known finding or benign vendor-supported test fixture; do not introduce real malware or live credentials to manufacture a match.
5. For trusted images, specify a trust criterion, enable the admission controller on the lab cluster, and test a compliant image and a harmless image that violates the trust criterion. Compare new deployment behavior with already-running workload findings.
6. Record policy scope, scanner coverage, action, and conflicting-policy behavior. Trusted-image policy resolution must be learned from its own documentation, rather than borrowed from endpoint policy ordering.

**Verify and save:** One validated custom rule, four policy-type configurations, and an admission-control allow/block result when the connector supports it.

**Explain without notes:** Can registry vulnerability scanning alone establish that an image is trusted by your organization?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [29. K3 Separate inventory and runtime coverage](29-k3-k3-separate-inventory-and-runtime-coverage.md)**
