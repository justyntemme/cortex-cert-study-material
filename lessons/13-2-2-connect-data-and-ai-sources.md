# Lesson 13: Connect data and AI sources

Week 2 · Lesson 13 of 45 · Objective/exercise 2.2

[Course start](../README.md) · [Previous lesson](12-k2-k2-review-permissions-and-onboard-the-connector.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 2.2. **Practice mode:** Conditional implementation and walkthrough.

**Read first:** [How to onboard Microsoft 365](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/microsoft/microsoft-365-posture/how-to-onboard-microsoft-365); [How to onboard Databricks](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/databricks/how-to-onboard-databricks); [Supported services in Cortex Cloud AI Security](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-ai-security/supported-services-in-cortex-cloud-ai-security); [How to configure the scanning settings for supported services](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/administration-and-troubleshooting/manage-instances/how-to-configure-the-scanning-settings-for-supported-services).

1. For Microsoft 365, add the data source, supply the documented tenant ID and region, perform administrator authorization, and verify the instance. Use a sandbox tenant with synthetic data if available.
2. For Databricks, collect the account and application IDs and required administrator permissions. Add Databricks, configure cloud/network details, review and run the generated script in the documented CLI environment, and use Verify Connection.
3. For Azure AI Foundry, follow Azure onboarding and the AI Security service prerequisites. Current documentation requires Outpost and DSPM for full Azure AI asset discovery; record those prerequisites in the worksheet before deployment.
4. Use AWS AI services already available in your lab to inspect AI asset discovery and related findings. Compare supported services with the AI inventory; do not provision costly AI training simply to populate a screen.
5. For an unavailable service, complete an input/permissions/network/verification worksheet and rehearse the wizard from the documentation. Leave its live validation unchecked.

**Verify and save:** One connection and discovery record for each available source; complete implementation worksheets for Microsoft 365, Databricks, and Foundry even when access is unavailable.

**Explain without notes:** Why might general cloud assets be visible while AI assets remain incomplete?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [14. Integrate GitHub and Jenkins](14-2-3-integrate-github-and-jenkins.md)**
