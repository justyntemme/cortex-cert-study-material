# Cortex CLI and Cytool troubleshooting lab

Use this supplement for objectives **4.1, 5.5 and 6.2**, following the suggestions in your [notes](notes.md). Allocate one hour in week 4, one hour in week 5, and revisit the failure scenarios in week 6. These are study exercises; the descriptions in your notes are not treated as independently verified exam statistics.

## Cortex CLI arguments and error tracking

1. Record `cortexcli --version`, inspect `cortexcli --help`, and inspect `cortexcli code scan --help`. Identify global options versus code-scan options.
2. Explain `--directory`, `--repo-id`, `--branch`, and the three upload modes. Run the same fixture locally and with upload using [the scan examples](examples/cli-and-xql.md).
3. Capture local debug output and the exit status. Run this from the disposable repository after configuring credentials through the documented credential method:

```sh
if cortexcli --log-level DEBUG --upload-mode no-upload code scan --directory . > scan.log 2>&1; then
  scan_rc=0
else
  scan_rc=$?
fi
printf 'Cortex CLI exit status: %s\n' "$scan_rc"
```

4. Compare a clean scan, a policy/finding failure, and an invalid configuration or execution failure. Use the log and scan response to identify the cause; an exit status alone is not a complete diagnosis.
5. Explain how suppression options could make a failed security check look successful to a CI runner. Repeat the diagnosis without suppression and check the actual results.

The current reference defines **0** as successful execution without findings, **1** as findings or a general operational failure, and **2** as an execution/internal/configuration failure. `--soft-fail` can convert the finding-related failure to success; `--no-fail-on-crash` can suppress execution failure. Always interpret the status with the actual error and installed-version documentation. [Exit codes and error handling](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/exit-codes-and-error-handling).

Use `--log-level DEBUG` for local output. The separate `--support` option enables debugging **and uploads logs** to the platform; do not confuse it with local logging. [Common CLI flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide).

**Application question:** The scanner exits with 2. Which evidence tells you whether the problem is configuration, version compatibility, authentication, or the scanning engine?

**Analysis question:** The pipeline is green, but no new scan appears in Cortex. Trace upload mode, exit suppression, credentials, repository attribution, and scan health before accepting the pipeline result.

## Cytool on the Linux lab VM

Cytool is supplied with the Cortex XDR agent and provides agent-management and diagnostic commands. Use the documentation matching the installed agent version; the reference consulted here is 9.4. From the installed agent's binary directory, inspect help before running these commands with the required local privileges:

```sh
./cytool --help
./cytool health
./cytool runtime query
./cytool last_checkin
./cytool connectivity_test
./cytool event_collection query
```

Record component state, protection/health, last successful check-in, connectivity, and collection status. Then run `./cytool checkin` and compare the console timestamp. Collect a diagnostic archive with `./cytool log collect` if needed. Review the reference for log-level controls and which commands require administrative authentication. [Cytool for Linux](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux).

1. Capture a healthy baseline before the agent-connectivity exercise in 6.2.
2. During the controlled fault, repeat the diagnostics and correlate local evidence with tenant status and timestamps.
3. Restore the connectivity/configuration, trigger a check-in, and prove a fresh benign event reaches Cortex.
4. Write a diagnosis that distinguishes a running agent process, working management communication, enabled event collection, and actual telemetry delivery.

On a Windows lab endpoint, use an elevated command prompt and the Windows reference. Practice `cytool info`, `cytool runtime query`, `cytool last_checkin`, `cytool event_collection query`, and `cytool log collect`. Do not assume Linux and Windows offer identical subcommands or component names. [Cytool for Windows](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-windows/troubleshooting-resources-for-windows/cytool-for-windows).

**Application question:** Which command would you use to inspect the last successful check-in, and what would you compare it against?

**Analysis question:** Agent components are running and check-in succeeds, but the event you expected is missing. How do collection status, policy, supported telemetry, time range, and tenant visibility narrow the cause?

**Evidence:** Save versions, commands, sanitized output, timestamps, diagnosis, correction, and fresh post-recovery data. Keep diagnostic archives local unless your support workflow calls for sharing them.
