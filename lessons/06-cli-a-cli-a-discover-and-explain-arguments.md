# Lesson 6: CLI A Discover and explain arguments

Week 1 · Lesson 6 of 45 · Objective/exercise CLI A

[Course start](../README.md) · [Previous lesson](05-1-4-manage-user-identities-rbac-sbac-and-api-keys.md)

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

1. **C1:** Install through the current tenant workflow if needed, then run `cortexcli --version`, `cortexcli --help`, and `cortexcli code scan --help`. Save version and relevant help output. [Connect Cortex CLI](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/connect-cortex-cli); [Common flags and Global flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide).
2. **C1–C4:** Annotate the scan example below: identify global options, module, subcommand, input, repository and branch. Before executing, explain which part changes if the exercise should upload results. [Common flags and Global flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide); [Code scan flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference).
3. **C2:** Configure credentials using the documented method for your execution environment. Record the method and required permission, not the secret. Compare the local-scan and upload requirements in the connection guide. [Credential methods](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/connect-cortex-cli/authenticate-credentials); [Connect Cortex CLI](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/connect-cortex-cli).

```sh
# Run inside the disposable repository chosen for this lesson.
cortexcli --upload-mode no-upload code scan --directory .
# Substitute the real owner/repo and branch for these lab examples.
cortexcli --upload-mode upload code scan --directory . --repo-id lab-owner/lab-app --branch main
```

Commands combine C3 and C4 using [Code scan flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference) and [Common flags and Global flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide). Our example names are placeholders. **Check:** explain each argument without looking at the lesson, then verify it against installed help. Upload permission is not proven by a local scan.

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [7. Optimize scanning and log costs](07-1-5-optimize-scanning-and-log-costs.md)**
