# Lesson 20: CLI B Track a scan through output and platform results

Week 3 · Lesson 20 of 45 · Objective/exercise CLI B

[Course start](../README.md) · [Previous lesson](19-5-5-install-authenticate-and-execute-cortex-cli.md)

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

1. **C3–C5:** Run a local scan of the same fixture used in objective 5.3. Capture stdout/stderr and exit status with the shell wrapper below. The wrapper is our evidence-capture method; CLI options are documented in [Common flags and Global flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide) and [Code scan flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference).
2. **C3–C4:** Run the uploaded variant for the same repository/branch. Compare the local output, upload response, and the corresponding platform scan. Record each observation separately. [Code scan flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference); [Common flags and Global flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide).
3. **C6:** Compare an available clean fixture with a fixture that previously produced a finding. Explain the status using the actual message and policy result; do not manufacture a result or presume every failure is a vulnerability. [Exit codes and suppression](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/exit-codes-and-error-handling).
4. **C4:** Rehearse `no-code` and explain what differs from `no-upload`; execute it on the disposable repository if that mode is permitted in your sandbox. [Common flags and Global flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide).

```sh
# Keep output outside the repository being scanned.
scan_evidence_dir="$(mktemp -d)"
if cortexcli --log-level DEBUG --log --upload-mode no-upload code scan --directory . > "$scan_evidence_dir/scan.log" 2>&1; then
  scan_rc=0
else
  scan_rc=$?
fi
printf 'Cortex CLI exit status: %s\n' "$scan_rc"
printf 'Local evidence: %s\n' "$scan_evidence_dir/scan.log"
```

**Check:** retain sanitized logs, version, repository, branch, scan time, raw status and platform evidence. Choose a local evidence directory outside the scanned repository so generated logs do not change the next scan input. This is a lab-design choice.

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [21. Use VS Code and JetBrains security plugins](21-5-4-use-vs-code-and-jetbrains-security-plugins.md)**
