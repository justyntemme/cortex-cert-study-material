# Lesson 32: Build compliance standards, controls, assessments, and reports

Week 4 · Lesson 32 of 45 · Objective/exercise 3.6

[Course start](../README.md) · [Previous lesson](31-3-5-manage-vulnerability-issue-and-prevention-policies.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 3.6. **Practice mode:** Implement.

**Read first:** [Choose compliance standards from the compliance catalog](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/compliance/monitor-and-track-compliance-adherence/choose-compliance-standards-from-the-compliance-catalog); [Use an assessment profile to run compliance checks on your assets](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/compliance/monitor-and-track-compliance-adherence/use-an-assessment-profile-to-run-compliance-checks-on-your-assets); [Use a built-in or custom standard](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/compliance/monitor-and-track-compliance-adherence/choose-compliance-standards-from-the-compliance-catalog/use-a-built-in-or-custom-standard); [Use a built-in or custom control](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/compliance/monitor-and-track-compliance-adherence/choose-compliance-standards-from-the-compliance-catalog/use-a-built-in-or-custom-control).

1. Open Posture Management → Compliance → Catalogs and inspect an out-of-the-box standard, its controls, and associated rules.
2. Clone a built-in standard with Save as new, or create a small custom standard. Add a category and custom control and associate a custom detection rule with that control.
3. Ensure a cloud security policy includes the custom cloud rule and targets the same intended lab scope; the assessment configuration does not replace this policy.
4. Create an Assessment Profile, select the standard and lab asset group, review the summary, and save. Generate/review the resulting assessment and report; keep delivery within your sandbox.
5. Correct the tested configuration and rerun the assessment. Trace one failed control all the way to its rule and asset, then explain the new result.

**Verify and save:** Built-in and custom assessment results, a report, and a standard → control → rule → policy → asset trace.

**Explain without notes:** Why can a custom assessment be misleading when its custom rule is not enabled through a policy?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [33. Deploy agents to VMs, CaaS, Kubernetes, and functions](33-4-1-deploy-agents-to-vms-caas-kubernetes-and-functions.md)**
