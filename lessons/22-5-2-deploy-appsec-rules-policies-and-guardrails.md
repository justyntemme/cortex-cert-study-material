# Lesson 22: Deploy AppSec rules, policies, and guardrails

Week 3 · Lesson 22 of 45 · Objective/exercise 5.2

[Course start](../README.md) · [Previous lesson](21-5-4-use-vs-code-and-jetbrains-security-plugins.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 5.2, 5.2.1, 5.2.2, 5.2.3. **Practice mode:** Implement policies; resolve one documented coverage gap.

**Read first:** [Create an AppSec policy](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/unified-application-security-policies/tenant-ui-workflow/create-a-policy); [Create CI/CD configuration policies](https://cortex-docs.paloaltonetworks.com/application-security/software-supply-chain-security/governance-and-enforcement/cicd-policies/create-cicd-configuration-policies); [Create custom Cortex Cloud Application Security rules](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/application-security-rules/tenant-ui-workflow/create-custom-cortex-cloud-application-security-rules); [Cloud Security Engineer July 2026 exam blueprint](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/palo-alto-networks-cloudsec-engineer.pdf).

1. For 5.2.1, create a custom IaC or secrets rule under Application Security → AppSec Rules. Set framework/scanner, severity, category, and remediation; validate the YAML and test it against one matching and one nonmatching lab fixture.
2. Create an AppSec policy using the current wizard: General, Conditions, Scope, Triggers & Actions, Exceptions, Summary. Select the relevant finding types, the lab repository/application, and supported periodic/PR/CI triggers.
3. Trigger a violating pull request or CI scan, inspect its policy result, fix the fixture, and rerun. Confirm that the intended policy caused the outcome rather than relying on a generic pipeline failure.
4. For 5.2.3, create a CI/CD Configuration Scanners policy, define a CI/CD risk condition, choose a lab scope, and use the triggers/actions supported by that policy type. Inspect an actual pipeline or VCS configuration finding.
5. For 5.2.2, preserve the exact blueprint topic, AI-recommended guardrails. The public documentation reviewed did not establish a step-by-step workflow under that name. Keep this child objective marked Documentation gap. Locate the applicable lesson in the official learning path or obtain a current vendor documentation link for the feature in your tenant, then add its verified steps here.
6. Once that documentation is available, record the recommendation, inspect the proposed scope/action, apply it only to the lab, and run matching/nonmatching checks. This last line is a proposed validation exercise, not a claim that a particular recommendation UI exists.

**Verify and save:** A custom rule, an exercised code policy, and a CI/CD policy. Objective 5.2.2 remains open until its exact documented workflow is identified and rehearsed.

**Explain without notes:** How do code scan policies differ from CI/CD configuration policies? What must you verify before accepting an AI-proposed control?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [23. CLI C Diagnose and repair](23-cli-c-cli-c-diagnose-and-repair.md)**
