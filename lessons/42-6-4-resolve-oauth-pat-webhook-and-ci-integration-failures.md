# Lesson 42: Resolve OAuth, PAT, webhook, and CI integration failures

Week 6 · Lesson 42 of 45 · Objective/exercise 6.4

[Course start](../README.md) · [Previous lesson](41-6-6-diagnose-user-and-api-access-problems.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 6.4. **Practice mode:** Break and repair.

**Read first:** [GitHub SaaS](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-version-control-systems/github-cloud); [Onboard the shared Cortex GitHub App](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-version-control-systems/github-cloud/onboard-a-cortex-github-app); [Jenkins for CI/CD pipeline scans](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-cicd-systems/jenkins-for-cicd-pipeline-scans); [Jenkins for code scans](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/integrate-ci-tools/jenkins-for-code-scans); [Connect GitLab container registry](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/gitlab/connect-gitlab-container-registry); [GitLab SaaS](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-version-control-systems/gitlab-saas).

1. Identify the actual authentication mechanism before troubleshooting: GitHub SaaS currently uses GitHub Apps; GitLab SaaS uses its documented authorization workflow; GitLab registry uses a PAT; Jenkins integrations have their own credentials/configuration.
2. In a disposable token-based integration, use an expired/revoked test credential or missing scope, observe the failure, replace it with the documented scoped credential, and verify recovery.
3. For GitHub App integrations, check installation authorization and selected repository access. Do not try to repair installation-token authentication by supplying a PAT intended for a different connector.
4. For missing PR results, confirm the repository is selected, PR scanning is enabled, and webhook delivery reaches the expected integration. Inspect provider delivery details when available; compare timestamps with Cortex scan history.
5. For Jenkins, verify the selected integration type, installed plugin or pipeline configuration, runner network access, and secret names. Rerun a fresh build after repair.
6. Record a fresh commit/PR/build that succeeds after the fix. A Connected label without a new scan is incomplete verification.

**Verify and save:** A credential or repository-access repair plus a fresh PR/build result; webhook investigation worksheet.

**Explain without notes:** Which checks differ among a GitHub App installation, an OAuth integration, and a registry PAT?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [43. Diagnose AppSec scanner, mapping, and policy failures](43-6-5-diagnose-appsec-scanner-mapping-and-policy-failures.md)**
