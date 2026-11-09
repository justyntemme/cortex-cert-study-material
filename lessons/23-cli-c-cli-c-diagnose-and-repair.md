# Lesson 23: CLI C Diagnose and repair

Week 3 · Lesson 23 of 45 · Objective/exercise CLI C

[Course start](../README.md) · [Previous lesson](22-5-2-deploy-appsec-rules-policies-and-guardrails.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

## Learn

| Concept | Documented behavior | Source |
| --- | --- | --- |
| C1 Discover syntax | `--help` lists options; `--version` identifies the installed version. Global flags precede the command. | [Common flags and Global flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide) |
| C2 Credentials | Configure a file, environment variables, or flags. The credential guide recommends CI secret-store environment variables for pipelines. | [Credential methods](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/connect-cortex-cli/authenticate-credentials) |
| C3 Scan and attribution | `--directory` selects the input; `--repo-id` uses `owner/repo`, not a tenant asset hash; `--branch` identifies the associated branch. | [Code scan flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference) |
| C4 Upload behavior | `upload` sends results and triggers policy evaluation; `no-upload` scans locally; `no-code` sends results without source code. | [Common flags and Global flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide) |
| C5 Diagnostic output | `--log-level DEBUG` sets stdout logging; `--log` reports the log path. `--support` also uploads logs. | [Common flags and Global flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide) |
| C6 Exit evidence | Standard codes: 0 successful/no findings; 1 findings or operational failure; 2 execution/configuration/internal failure. Interpret these with the output and suppression options. | [Exit codes and suppression](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/exit-codes-and-error-handling) |
| C7 Suppression | `--soft-fail` converts the documented blocking-finding status 1 to 0; `--no-fail-on-crash` converts status 2 to 0. | [Exit codes and suppression](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/exit-codes-and-error-handling) |

**Implementation choice:** Use unsuppressed results for the learning baseline so you can observe failure status. This is our lab choice. Use the documented CI secret-store method for pipeline credentials and leave TLS verification enabled; the common reference advises against `--no-cert-verify` in production. [Credential methods](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/connect-cortex-cli/authenticate-credentials); [Common flags and Global flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide).

## Practice

| Case | Practice tied to the lesson | Recovery evidence | Source |
| --- | --- | --- | --- |
| Configuration error | C3/C6: use a nonexistent input directory in a separate disposable invocation; capture the actual message/status | Correct the directory and rerun the baseline | [Code scan flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference); [Exit codes and suppression](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/exit-codes-and-error-handling) |
| Wrong attribution | C3: compare the actual repository/branch with the supplied arguments; correct a lab mismatch | New scan associated with the intended repository/branch | [Code scan flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference) |
| Green status with finding | C6/C7: compare the same blocking-finding case with and without `--soft-fail` | Finding remains visible; record the change in status | [Exit codes and suppression](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/exit-codes-and-error-handling) |
| Execution suppression | C6/C7: after observing a documented status-2 failure, compare a disposable invocation with `--no-fail-on-crash` | Explain why status 0 is insufficient evidence of a completed scan | [Exit codes and suppression](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/exit-codes-and-error-handling) |
| Need detailed logs | C5: obtain debug output and log path; explain what adding `--support` would send | Trace the error to a message and timestamp | [Common flags and Global flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide) |

If you cannot reproduce a failure, analyze its documented category and mark the live case pending. Restore the working command after each case. These experiments do not change shared pipelines. Use [Exit codes and suppression](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/exit-codes-and-error-handling) for code interpretation; a particular fixture's exact output must come from observation.

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [24. Create static and dynamic asset groups](24-3-2-create-static-and-dynamic-asset-groups.md)**
