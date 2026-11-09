# Exam era and sandbox version baseline

You report that the exam was created in June/July 2026 and that its questions concern features existing then. We use that as the working exam-era focus. It is meeting information from you, not independently verified proof of an immutable official cutoff for every later exam form. The supplied July blueprint remains the topic checklist.

## Rules for lessons

1. Keep every blueprint objective, including a feature whose older implementation procedure is still unresolved.
2. For exam behavior, prefer an official dated/versioned guide, release note or assigned official course that establishes the behavior in June/July 2026. Record the exact source and version beside the claim.
3. Use current documented procedures for the actual sandbox version. Label current UI/commands separately where historical applicability has not been established.
4. If the two differ, explain the difference instead of merging steps. A current page's existence or retrieval date does not prove its historical availability.
5. Mark additions established to postdate the exam era as operational enrichment unless the current blueprint or official course requires them. Do not remove an objective merely because its current implementation changed.
6. A missing historical reference remains an open fact check. Do not invent an older command, authentication flow, policy rule or UI label.

## Items requiring version comparison

| Area | Current procedure available | Exam-era status |
| --- | --- | --- |
| Unified CLI flags, upload modes, suppression, exit categories | [Cortex CLI common flags](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-common-command-line-reference-guide); [Cortex CLI exit codes and error handling](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/exit-codes-and-error-handling) | June/July syntax and behavior not yet established |
| CLI repository attribution/authentication | [Cortex CLI Cortex Cloud Application Security command line reference](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference); [Authenticate credentials](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/connect-cortex-cli/authenticate-credentials) | Compare with assigned course/version before treating current flags as exam-era syntax |
| Cytool | [Cytool for Linux 9.4](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-linux/troubleshooting-resources-for-linux/cytool-for-linux); [Cytool for Windows 9.4](https://cortex-docs.paloaltonetworks.com/cortex-xdr-agent/9.4-cortex-xdr-agent-admin-guide/cortex-xdr-agent-for-windows/troubleshooting-resources-for-windows/cytool-for-windows) | Existing lessons use agent 9.4 references; match installed version and separately verify exam-era reference |
| Kubernetes connector runtime options | [Onboard the Kubernetes Connector](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/onboard-the-kubernetes-connector) | Current wizard options do not by themselves establish June/July availability |
| GitHub integration authentication | [GitHub SaaS](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-version-control-systems/github-cloud) | Compare current app-based procedure with exam-era/course expectations |
| Attack Path interface | [Create an attack path (legacy) rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules/create-an-attack-path-rule) | Current source labels its creation workflow Legacy; historical/current differences remain to reconcile |
| AI-recommended guardrails 5.2.2 | Blueprint objective retained | Exact implementation procedure remains unresolved |

The existing technical register records retrieval dates, not historical feature availability. The original guide still needs the finer-grained support review described in [the lesson standard](../LESSON-STANDARD.md). This new baseline does not retroactively certify its examples as June/July behavior.
