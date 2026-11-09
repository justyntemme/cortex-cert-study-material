# Lesson 36: Integrate API gateways

Week 5 · Lesson 36 of 45 · Objective/exercise 4.3

[Course start](../README.md) · [Previous lesson](35-cy-b-cy-b-choose-commands-from-the-symptom.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 4.3. **Practice mode:** AWS implementation plus Azure and Apigee walkthrough.

**Read first:** [Ingest AWS API Gateway](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/api-security/ingest-data-for-api-security/ingest-aws-api-gateway); [Ingest Azure APIM](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/api-security/ingest-data-for-api-security/ingest-azure-apim); [Ingest Apigee Proxy](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/api-security/ingest-data-for-api-security/ingest-apigee-proxy).

1. Add AWS API Gateway in Cortex Data Sources & Integrations, create the collector, and securely retain its generated key and endpoint.
2. On a disposable AWS API Gateway REST API stage, configure the documented CloudWatch role, logs/tracing, and access-log format. Use synthetic request data.
3. Create the Data Firehose stream with the documented HTTP endpoint destination, authentication, compression, and failed-record backup. Add the CloudWatch subscription and IAM role described in the guide.
4. Send a benign request to the API and trace it through CloudWatch, delivery, and Cortex. Diagnose each hop separately if the event is absent.
5. For Azure APIM, create the Cortex collector, configure APIM named values (including the secret key), and apply the documented inbound/outbound policy to a test API; send a request and verify ingestion. For Apigee, create the collector, download its configuration package, set project/organization/environment/URL/key, deploy the documented shared flows and hooks, and validate a request. Rehearse these exact configurations from the docs when the services are unavailable.

**Verify and save:** An end-to-end AWS API request trace and complete APIM/Apigee configuration walkthroughs.

**Explain without notes:** Which evidence separates a gateway logging problem from an HTTP collector authentication problem?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [37. Configure detection rules and automation playbooks](37-4-4-configure-detection-rules-and-automation-playbooks.md)**
