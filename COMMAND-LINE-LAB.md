# Cortex CLI and Cytool application labs

Objectives: 5.5, 4.1, 6.2, with connections to 1.4, 2.3, 6.4 and 6.5. Louise's suggestion is recorded in [your learning profile](notes/LEARNING-PROFILE.md). Start CLI A and CY A in week 1, complete CLI B/C in week 3 and CY B in week 4, then repeat selected cases through week 8. Exercise order and fixtures are our study choices.

## Learn the Cortex CLI concepts

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

## CLI A Discover and explain arguments

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

## CLI B Track a scan through output and platform results

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

## CLI C Diagnose and repair

| Case | Practice tied to the lesson | Recovery evidence | Source |
| --- | --- | --- | --- |
| Configuration error | C3/C6: use a nonexistent input directory in a separate disposable invocation; capture the actual message/status | Correct the directory and rerun the baseline | [Code scan flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference); [Exit codes and suppression](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/exit-codes-and-error-handling) |
| Wrong attribution | C3: compare the actual repository/branch with the supplied arguments; correct a lab mismatch | New scan associated with the intended repository/branch | [Code scan flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference) |
| Green status with finding | C6/C7: compare the same blocking-finding case with and without `--soft-fail` | Finding remains visible; record the change in status | [Exit codes and suppression](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/exit-codes-and-error-handling) |
| Execution suppression | C6/C7: after observing a documented status-2 failure, compare a disposable invocation with `--no-fail-on-crash` | Explain why status 0 is insufficient evidence of a completed scan | [Exit codes and suppression](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/exit-codes-and-error-handling) |
| Need detailed logs | C5: obtain debug output and log path; explain what adding `--support` would send | Trace the error to a message and timestamp | [Common flags and Global flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide) |

If you cannot reproduce a failure, analyze its documented category and mark the live case pending. Restore the working command after each case. These experiments do not change shared pipelines. Use [Exit codes and suppression](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/exit-codes-and-error-handling) for code interpretation; a particular fixture's exact output must come from observation.

## Learn the Cytool concepts

These references are for agent 9.4. Match the guide to the installed agent version and OS before executing. Cytool is an agent administration/diagnostic tool; its commands are not Cortex CLI scan arguments. [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux); [Windows Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-windows/troubleshooting-resources-for-windows/cytool-for-windows).

| Concept | Linux command from the installed binary directory | What it reports or does | Source |
| --- | --- | --- | --- |
| Y1 Help and state | `./cytool --help`; `./cytool health`; `./cytool runtime query` | Help, agent health, component state | [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux) |
| Y2 Communication | `./cytool last_checkin`; `./cytool connectivity_test` | Last successful check-in and server connectivity test | [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux) |
| Y3 Collection | `./cytool event_collection query` | Event-collection state | [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux) |
| Y4 Recheck | `./cytool checkin` | Initiates a check-in; compare console check-in time | [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux) |
| Y5 Logs | `./cytool log collect` | Collects a TGZ support archive | [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux) |

## CY A Build a diagnostic baseline

1. **Y1:** On a disposable Linux VM with the installed agent, inspect help and execute the Y1 commands with the privileges required by your version. Save actual state and agent version. [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux).
2. **Y2–Y3:** Run the communication and collection queries. Build a timeline of local status and tenant observations. Do not interpret one successful check-in as proof of a particular collected event; that is a hypothesis requiring separate evidence. [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux); [Monitor agent operational status](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/manage-endpoint-protection/monitor-agent-operational-status).
3. **Y4–Y5:** Trigger a check-in, verify its console timestamp, then collect an archive for the lab if needed. Record the archive location and keep it out of the study repository. [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux).
4. **Windows comparison:** On an available Windows endpoint use the Windows procedure and an elevated command prompt: inspect `cytool info`, `cytool runtime query`, `cytool last_checkin`, `cytool event_collection query`, and `cytool log collect`. Do not transfer OS-specific subcommands by assumption. [Windows Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-windows/troubleshooting-resources-for-windows/cytool-for-windows).

## CY B Choose commands from the symptom

1. **Y1–Y3:** For the controlled connectivity exercise in implementation objective 6.2, choose a command before seeing the answer rubric: component state, last successful communication, connectivity, or event collection. Repeat the baseline observations during the fault. [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux); [Monitor agent operational status](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/manage-endpoint-protection/monitor-agent-operational-status).
2. **Y5:** Collect logs and correlate them with the failure window. Read the version-specific `log set_level` syntax and component names. If you change verbosity, record and restore the original level; do not guess that every OS uses identical logging arguments. [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux); [Windows Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-windows/troubleshooting-resources-for-windows/cytool-for-windows).
3. **Y2–Y4:** Restore the lab's known-good configuration, request check-in, and verify fresh communication. Then verify the intended benign telemetry separately in Cortex. [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux); [Monitor agent operational status](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/manage-endpoint-protection/monitor-agent-operational-status).
4. **Analysis:** Compare the evidence for a stopped component, failed connection and missing collection. State what remains unknown. Selecting a likely command is not the same as establishing a cause. This is our reasoning exercise grounded in the diagnostic functions above.

**Check:** explain why each command was selected, what its output proves, and which additional observation you need. Never apply the Cortex CLI exit-code table to Cytool: the cited Cytool command tables do not establish that mapping.

## Application and analysis questions

Complete L1–L4 and A1–A3 in [the additional question set](APPLICATION-ANALYSIS.md), then repeat with a different fixture or failure window. Track attempts separately in [practice-progress.csv](practice-progress.csv). Keep the original scenarios and command examples in your review rotation.
