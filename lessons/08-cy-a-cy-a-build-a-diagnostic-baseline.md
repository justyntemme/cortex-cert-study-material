# Lesson 8: CY A Build a diagnostic baseline

Week 1 · Lesson 8 of 45 · Objective/exercise CY A

[Course start](../README.md) · [Previous lesson](07-1-5-optimize-scanning-and-log-costs.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

## Learn

These references are for agent 9.4. Match the guide to the installed agent version and OS before executing. Cytool is an agent administration/diagnostic tool; its commands are not Cortex CLI scan arguments. [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux); [Windows Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-windows/troubleshooting-resources-for-windows/cytool-for-windows).

| Concept | Linux command from the installed binary directory | What it reports or does | Source |
| --- | --- | --- | --- |
| Y1 Help and state | `./cytool --help`; `./cytool health`; `./cytool runtime query` | Help, agent health, component state | [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux) |
| Y2 Communication | `./cytool last_checkin`; `./cytool connectivity_test` | Last successful check-in and server connectivity test | [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux) |
| Y3 Collection | `./cytool event_collection query` | Event-collection state | [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux) |
| Y4 Recheck | `./cytool checkin` | Initiates a check-in; compare console check-in time | [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux) |
| Y5 Logs | `./cytool log collect` | Collects a TGZ support archive | [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux) |

## Practice

1. **Y1:** On a disposable Linux VM with the installed agent, inspect help and execute the Y1 commands with the privileges required by your version. Save actual state and agent version. [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux).
2. **Y2–Y3:** Run the communication and collection queries. Build a timeline of local status and tenant observations. Do not interpret one successful check-in as proof of a particular collected event; that is a hypothesis requiring separate evidence. [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux); [Monitor agent operational status](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/manage-endpoint-protection/monitor-agent-operational-status).
3. **Y4–Y5:** Trigger a check-in, verify its console timestamp, then collect an archive for the lab if needed. Record the archive location and keep it out of the study repository. [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux).
4. **Windows comparison:** On an available Windows endpoint use the Windows procedure and an elevated command prompt: inspect `cytool info`, `cytool runtime query`, `cytool last_checkin`, `cytool event_collection query`, and `cytool log collect`. Do not transfer OS-specific subcommands by assumption. [Windows Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-windows/troubleshooting-resources-for-windows/cytool-for-windows).

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [9. Onboard cloud providers and security capabilities](09-2-1-onboard-cloud-providers-and-security-capabilities.md)**
