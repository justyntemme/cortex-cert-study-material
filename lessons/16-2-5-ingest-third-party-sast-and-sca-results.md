# Lesson 16: Ingest third-party SAST and SCA results

Week 2 · Lesson 16 of 45 · Objective/exercise 2.5

[Course start](../README.md) · [Previous lesson](15-2-4-integrate-container-registries.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 2.5. **Practice mode:** Implement Generic SARIF and walk through vendors.

**Read first:** [Semgrep](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/semgrep); [Veracode](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/veracode); [Reference B: SARIF format and mapping](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/generic-3rd-party-appsec-collector/references/reference-b-sarif-format-and-mapping); [Configure Semgrep ingestion](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/semgrep/configure-semgrep-ingestion); [Configure the Generic 3rd Party AppSec Collector](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/generic-3rd-party-appsec-collector/tenant-console-workflow); [Upload findings from CI/CD pipelines](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/generic-3rd-party-appsec-collector/upload-findings-from-ci-cd-pipelines).

1. For Semgrep, add the integration, authorize its Web API token, select SAST/SCA, map projects to onboarded repositories, and verify the connected mapped projects.
2. For Veracode, provide the documented credentials and region, authorize, select applications, confirm repository mappings, and verify ingestion. Record its documented scan and enforcement limitations.
3. For Generic SARIF, create a 3rd Party AppSec Collector. Match its name to the SARIF tool name, save its generated credentials securely, and copy its upload endpoint.
4. Validate a SARIF 2.1.0 file containing a rule ID, matching result, message, relative file URI, and start line. Use the provided fixture in examples as a format exercise.
5. Upload through the documented API workflow or the collector’s generated example, then verify repository attribution and finding location. UI validation alone is not a completed ingestion test.

**Verify and save:** A validated and ingested synthetic finding tied to its repository and source location; vendor mapping worksheets.

**Explain without notes:** Why can an authenticated connector ingest no results when project mapping is missing?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [17. Manage business applications and issue SLAs](17-5-1-manage-business-applications-and-issue-slas.md)**
