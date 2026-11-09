# Lesson 26: Create cloud security rules and policies

Week 4 · Lesson 26 of 45 · Objective/exercise 3.3

[Course start](../README.md) · [Previous lesson](25-3-1-create-an-xql-dashboard.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 3.3. **Practice mode:** Implement six rule types.

**Read first:** [Create a cloud security policy](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-policies/create-a-cloud-security-policy); [Create and manage cloud security rules](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules); [Create a configuration rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules/create-a-configuration-rule); [Create an identity rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules/create-an-identity-rule); [Create a network exposure rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules/create-a-network-exposure-rule); [Create an AI rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules/create-an-ai-rule); [Create a data rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules/create-a-data-rule); [Create an attack path (legacy) rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules/create-an-attack-path-rule).

1. Under Posture Management → Rules & Policies → Rules → Cloud Security, create a Config rule. Name it, select severity, define a simple query against an observed lab configuration, and Search/Test before saving.
2. Create an Identity rule using an identity, its effective permissions, and a resource relationship. Test it against lab data and explain why the permission is excessive or unused.
3. Create a Network Exposure rule; choose inbound, outbound, or east-west and specify the relevant source, destination asset, and protocol/port conditions. Use existing sandbox examples; do not expose a vulnerable host merely to force a finding.
4. Create a Data rule using the available data criteria, and an AI rule using a discovered AI asset and its attributes. Use synthetic classified data. If there are no AI assets, save and test the rule configuration but mark positive-result validation as pending.
5. Create an Attack Path rule using the documented interface available in your tenant. The currently retrieved custom creation guide labels its workflow Attack Path (Legacy); combine observed finding/vulnerability conditions and test the result. Do not assume a newly named attack-path UI has identical behavior.
6. Create a Cloud Security policy, select the saved rules, explicitly scope it to lab accounts/groups, and save. Compare rule matches, policy scope, generated issues, and remediation after a controlled correction.

**Verify and save:** Six rule worksheets or saved configurations, a scoped policy, and before/after evidence for the rule types with available data.

**Explain without notes:** What does the rule decide, what does the policy decide, and why might a matching rule generate no issue for an excluded asset?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [27. Configure data classification and scanning](27-3-8-configure-data-classification-and-scanning.md)**
