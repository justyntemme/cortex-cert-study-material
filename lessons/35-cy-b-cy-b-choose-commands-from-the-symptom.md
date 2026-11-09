# Lesson 35: CY B Choose commands from the symptom

Week 5 · Lesson 35 of 45 · Objective/exercise CY B

[Course start](../README.md) · [Previous lesson](34-4-2-configure-endpoint-groups-prevention-extensions-and-exceptions.md)

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

1. **Y1–Y3:** For the controlled connectivity exercise in implementation objective 6.2, choose a command before seeing the answer rubric: component state, last successful communication, connectivity, or event collection. Repeat the baseline observations during the fault. [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux); [Monitor agent operational status](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/manage-endpoint-protection/monitor-agent-operational-status).
2. **Y5:** Collect logs and correlate them with the failure window. Read the version-specific `log set_level` syntax and component names. If you change verbosity, record and restore the original level; do not guess that every OS uses identical logging arguments. [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux); [Windows Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-windows/troubleshooting-resources-for-windows/cytool-for-windows).
3. **Y2–Y4:** Restore the lab's known-good configuration, request check-in, and verify fresh communication. Then verify the intended benign telemetry separately in Cortex. [Linux Cytool command table](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux); [Monitor agent operational status](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/manage-endpoint-protection/monitor-agent-operational-status).
4. **Analysis:** Compare the evidence for a stopped component, failed connection and missing collection. State what remains unknown. Selecting a likely command is not the same as establishing a cause. This is our reasoning exercise grounded in the diagnostic functions above.

**Check:** explain why each command was selected, what its output proves, and which additional observation you need. Never apply the Cortex CLI exit-code table to Cytool: the cited Cytool command tables do not establish that mapping.

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [36. Integrate API gateways](36-4-3-integrate-api-gateways.md)**
