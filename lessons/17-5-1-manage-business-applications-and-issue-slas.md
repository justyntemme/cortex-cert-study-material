# Lesson 17: Manage business applications and issue SLAs

Week 3 · Lesson 17 of 45 · Objective/exercise 5.1

[Course start](../README.md) · [Previous lesson](16-2-5-ingest-third-party-sast-and-sca-results.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 5.1, 5.1.1, 5.1.2. **Practice mode:** Implement.

**Read first:** [Define business applications by code or cloud criteria](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/applications/defining-business-applications); [Create SLAs for case and issue resolution](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cases-and-issues/customize-cases-and-issues/create-slas-for-issue-resolution); [Manually build an application](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/applications/manually-build-an-application); [Code to Cloud troubleshooting](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/code-to-cloud/code-to-cloud-troubleshooting).

1. Create a manual business application under Application Security → Business Applications. Set a lab name, criticality, ownership context, and starting code or cloud assets.
2. Inspect the connected assets across Code, Build, Deploy, and Run. Record missing relationships and their evidence; a business application label alone does not prove code-to-cloud lineage.
3. Create a criteria-based application using supported code hierarchy or cloud tags. Preview the matched assets, create it, and verify membership after changing a harmless matching attribute.
4. Open Settings → Configurations → Object Setup → Issues → SLA Rules. Create a lab SLA with explicit matching conditions, a resolution goal, and intentional rule ordering.
5. Inspect a matching issue and a nonmatching issue. Verify the assigned SLA and test how a higher-priority matching rule affects selection.
6. Use the resulting application context and issue state to write a short prioritization explanation for the lab application.

**Verify and save:** Manual and criteria-based application records, a lineage check, and a matching issue with its assigned SLA.

**Explain without notes:** How do application grouping, code-to-cloud mapping, policy scope, and SLA timing serve different purposes?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [18. Configure repository scanning and IaC drift](18-5-3-configure-repository-scanning-and-iac-drift.md)**
