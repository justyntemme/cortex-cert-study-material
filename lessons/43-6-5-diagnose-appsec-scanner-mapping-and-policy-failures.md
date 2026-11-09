# Lesson 43: Diagnose AppSec scanner, mapping, and policy failures

Week 6 · Lesson 43 of 45 · Objective/exercise 6.5

[Course start](../README.md) · [Previous lesson](42-6-4-resolve-oauth-pat-webhook-and-ci-integration-failures.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 6.5. **Practice mode:** Break and repair.

**Read first:** [Create an AppSec policy](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/unified-application-security-policies/tenant-ui-workflow/create-a-policy); [IaC Drift Detection scans](https://cortex-docs.paloaltonetworks.com/application-security/code-security/code-security-scanners/iac-drift-detection-scans); [Scan settings](https://cortex-docs.paloaltonetworks.com/application-security/settings/application-security-settings/scan-settings); [Code to Cloud troubleshooting](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/code-to-cloud/code-to-cloud-troubleshooting); [Global scan configurations](https://cortex-docs.paloaltonetworks.com/application-security/settings/application-security-settings/scan-settings/global-scan-configurations); [Custom scan configurations](https://cortex-docs.paloaltonetworks.com/application-security/settings/application-security-settings/scan-settings/custom-scan-configurations); [Cortex CLI Cortex Cloud Application Security command line reference](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference).

1. Use a fixture that produced a finding earlier. Deliberately exclude its path or disable its scanner in only the lab repository’s custom configuration.
2. Run another scan and compare scanner selection, branch, commit, exclusions, and scan health with the working baseline. Restore the setting and verify the finding returns.
3. Next, keep the finding but exclude the repository from the lab policy’s scope. Compare raw finding visibility with issue creation or blocking behavior.
4. Inspect finding type, conditions, supported trigger, action, exception, and policy scope when the expected enforcement is missing.
5. For missing lineage or drift, inspect cloud/repository integrations, YOR mapping signals, and pipeline execution. Restore the missing link and confirm the expected Code → Build → Deploy → Run relationship.
6. Save a diagnosis that separates no scan, no finding, no issue, and no blocking action.

**Verify and save:** Two deliberate misconfigurations repaired with before/after scan and policy evidence.

**Explain without notes:** Why can a scanner report a finding while a PR still passes?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [44. Diagnose an unexpected AWS cost increase](44-6-7-diagnose-an-unexpected-aws-cost-increase.md)**
