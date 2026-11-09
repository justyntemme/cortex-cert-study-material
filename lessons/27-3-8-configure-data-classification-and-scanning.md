# Lesson 27: Configure data classification and scanning

Week 4 · Lesson 27 of 45 · Objective/exercise 3.8

[Course start](../README.md) · [Previous lesson](26-3-3-create-cloud-security-rules-and-policies.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 3.8. **Practice mode:** Implement.

**Read first:** [How to onboard Amazon Web Services](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/how-to-onboard-amazon-web-services); [How to create and validate a custom data pattern](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-classification/how-to-create-and-validate-a-custom-data-pattern); [How to configure the scanning settings for supported services](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/administration-and-troubleshooting/manage-instances/how-to-configure-the-scanning-settings-for-supported-services).

1. Enable DSPM for the relevant AWS integration and inspect the supported-service scanning controls for your lab data store.
2. Use a private lab bucket containing synthetic records only. In Settings → Configurations → Data Classification → Data Patterns, add a pattern for an invented identifier such as LABID-[0-9]{6}.
3. Set a context word, proximity, and masking level. Use the built-in validator with a matching sample and nonmatching samples; include one sample where the context is too far away.
4. Associate the pattern with a custom data profile as described in the classification documentation. Run or await the configured supported scan and inspect the classification results.
5. Check scope, scanner permissions, profile association, and masking when the expected result is missing. Record that custom patterns have platform-wide applicability, so use a narrowly distinctive test format.

**Verify and save:** Validator results plus a discovered, classified synthetic record and the corresponding scan configuration.

**Explain without notes:** How can a valid regex still fail to classify a record because of context or proximity settings?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [28. Create workload rules and policies](28-3-4-create-workload-rules-and-policies.md)**
