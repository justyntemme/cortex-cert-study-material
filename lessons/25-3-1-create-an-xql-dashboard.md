# Lesson 25: Create an XQL dashboard

Week 4 · Lesson 25 of 45 · Objective/exercise 3.1

[Course start](../README.md) · [Previous lesson](24-3-2-create-static-and-dynamic-asset-groups.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 3.1. **Practice mode:** Implement.

**Read first:** [Troubleshoot errors on cloud instances](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/troubleshoot-errors-on-cloud-instances); [Create XQL widgets](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/dashboards-and-reports/monitor-dashboards-and-reports/advanced-configuration/create-custom-widgets/create-xql-widgets); [Create dashboards](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/dashboards-and-reports/monitor-dashboards-and-reports/create-dashboards).

1. Run a query against a dataset that actually exists in your sandbox. Start with cloud_health_auditing and inspect the returned fields and time window.
2. In Widget Library, choose Create widget → XQL widget. Name it, keep visibility restricted to the lab, enter the query, and Preview the results.
3. Use a table initially; then create an appropriate count or grouped chart after verifying the query output. Compare the widget with the direct query over the same time range.
4. Create a custom dashboard, add the saved widget, and add a title describing its scope. Configure a parameterized filter or drilldown using the documented widget options.
5. Save evidence of the query, preview, dashboard, and filter behavior. An empty result is a coverage or time-window question to investigate, not proof of zero risk.

**Verify and save:** A working dashboard whose counts match a direct query and whose scope you can explain.

**Explain without notes:** Why might a dashboard show no events while its data source is Connected?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [26. Create cloud security rules and policies](26-3-3-create-cloud-security-rules-and-policies.md)**
