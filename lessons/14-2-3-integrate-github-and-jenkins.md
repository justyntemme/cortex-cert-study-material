# Lesson 14: Integrate GitHub and Jenkins

Week 2 · Lesson 14 of 45 · Objective/exercise 2.3

[Course start](../README.md) · [Previous lesson](13-2-2-connect-data-and-ai-sources.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 2.3. **Practice mode:** Implement where available.

**Read first:** [GitHub SaaS](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-version-control-systems/github-cloud); [Onboard the shared Cortex GitHub App](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-version-control-systems/github-cloud/onboard-a-cortex-github-app); [Jenkins for CI/CD pipeline scans](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-cicd-systems/jenkins-for-cicd-pipeline-scans); [Jenkins for code scans](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/integrate-ci-tools/jenkins-for-code-scans).

1. Create or use a disposable repository within a GitHub organization you can administer. Add GitHub SaaS in Cortex, choose the GitHub App ownership model, authorize selected repository access, and finish repository selection.
2. Verify the instance and repository are connected. Run an initial repository scan and record the commit/branch scanned.
3. For Jenkins pipeline scanning, add Jenkins with CI/CD System Scan, download the provided HPI plugin, install it under Manage Jenkins → Plugins, and configure its generated JWT under Manage Jenkins → System → Cortex Cloud. Verify Connected status.
4. For Jenkins code scanning, create a separate Code Scan integration, store CORTEX_API_KEY and CORTEX_API_KEY_ID in Jenkins Credentials, and use the wizard-generated pipeline configuration on a suitable Docker-capable runner.
5. Run a build and confirm the scan is associated with the intended repository and commit. Keep the two Jenkins integration types distinct in your notes.

**Verify and save:** A connected repository and one attributable scan; Jenkins plugin and code-pipeline evidence if Jenkins is available.

**Explain without notes:** Why can a working Jenkins pipeline-risk integration still leave code scans absent?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [15. Integrate container registries](15-2-4-integrate-container-registries.md)**
