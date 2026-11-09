# Lesson 19: Install, authenticate, and execute Cortex CLI

Week 3 · Lesson 19 of 45 · Objective/exercise 5.5

[Course start](../README.md) · [Previous lesson](18-5-3-configure-repository-scanning-and-iac-drift.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

Complete the [command-line troubleshooting supplement](../COMMAND-LINE-LAB.md) for argument inspection, exit-code handling and local debug logs.

**Blueprint coverage:** 5.5. **Practice mode:** Implement.

**Read first:** [Application Security Cortex CLI](https://cortex-docs.paloaltonetworks.com/application-security/code-security/application-security-cli); [Connect Cortex CLI](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/connect-cortex-cli); [Authenticate credentials](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/connect-cortex-cli/authenticate-credentials); [Cortex CLI Cortex Cloud Application Security command line reference](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference).

1. Use the current Connect Cortex CLI instructions for your host and tenant to obtain the executable. Validate local requirements and record the installed version/help output.
2. Configure CORTEX_API_BASE_URL, CORTEX_API_KEY, and CORTEX_API_KEY_ID through a protected credential file or environment variables. Select a Standard key and permissions appropriate to local-only versus uploaded scans.
3. From the disposable lab repository, run a local code scan using the documented directory flag and no-upload mode. Use examples/cli-and-xql.md as a starting command reference.
4. Run an uploaded scan with the correct owner/repo identifier and branch. Confirm its results are attributed to the intended repository rather than an unrelated asset ID.
5. Add the same scan to your CI job with credentials in its secret store. Test a finding-triggered failure, an authentication failure, and a clean run; record what each exit status actually means in your installed version.
6. Compare no-upload, no-code, and upload behavior from the documentation and choose the correct mode for your lab’s data handling requirements.

**Verify and save:** A reproducible local command, an attributed uploaded scan, and a CI run that distinguishes scan findings from scanner failure.

**Explain without notes:** Why might a scan run locally but fail when uploading, or upload into the wrong repository context?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [20. CLI B Track a scan through output and platform results](20-cli-b-cli-b-track-a-scan-through-output-and-platform-results.md)**
