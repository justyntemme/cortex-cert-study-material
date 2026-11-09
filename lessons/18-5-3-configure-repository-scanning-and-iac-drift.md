# Lesson 18: Configure repository scanning and IaC drift

Week 3 · Lesson 18 of 45 · Objective/exercise 5.3

[Course start](../README.md) · [Previous lesson](17-5-1-manage-business-applications-and-issue-slas.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 5.3. **Practice mode:** Implement.

**Read first:** [IaC Drift Detection scans](https://cortex-docs.paloaltonetworks.com/application-security/code-security/code-security-scanners/iac-drift-detection-scans); [Scan settings](https://cortex-docs.paloaltonetworks.com/application-security/settings/application-security-settings/scan-settings); [Code to Cloud troubleshooting](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/code-to-cloud/code-to-cloud-troubleshooting); [Global scan configurations](https://cortex-docs.paloaltonetworks.com/application-security/settings/application-security-settings/scan-settings/global-scan-configurations); [Custom scan configurations](https://cortex-docs.paloaltonetworks.com/application-security/settings/application-security-settings/scan-settings/custom-scan-configurations).

1. Open the lab repository’s Scan Configuration through its VCS integration. Inspect whether it follows Global settings or uses Custom settings.
2. Use repository-specific settings to enable IaC, SCA, secrets, and PR scanning for the lab. Record history scanning, validation, path exclusions, and behavior on scan errors. Avoid overwriting other repositories’ custom settings.
3. Prepare separate fixtures: an IaC violation selected from a documented enabled rule, a dependency finding you can reproduce, and an obviously synthetic secret-pattern sample. Scan, fix, and rescan each; a synthetic string is not guaranteed to match every built-in secrets detector.
4. For drift, deploy a harmless IaC-defined resource only after cloud/repository integration and code-to-cloud mapping are working. Use the required mapping/tagging workflow and confirm lineage first.
5. Select a documented security rule, make a reversible lab configuration change that violates it while code remains compliant, and inspect the drift finding. Restore the configuration from code and recheck.
6. Distinguish raw findings from policy-created issues and security-relevant drift from arbitrary configuration differences. Record the missing prerequisites if a positive drift test cannot be reproduced.

**Verify and save:** Before/after results for IaC, SCA, and secrets; scanner configuration evidence; and a mapped resource with a drift/remediation trace.

**Explain without notes:** Why might changing a cloud resource fail to generate a drift issue even though its configuration differs from Git?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [19. Install, authenticate, and execute Cortex CLI](19-5-5-install-authenticate-and-execute-cortex-cli.md)**
