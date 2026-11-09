# Cortex CLI and XQL practice examples

These are study examples assembled from the linked documentation. They have not been executed against your tenant. Use the generated commands for your current package/version where they differ.

## Local and uploaded code scans

Install the CLI with the documented tenant workflow. Configure CORTEX_API_BASE_URL, CORTEX_API_KEY and CORTEX_API_KEY_ID using the documented credential method; do not paste secrets into this file. Use a Standard API key with appropriate CLI permissions.

```sh
# Run from the disposable repository you intend to scan.
cortexcli --upload-mode no-upload code scan --directory .

# Replace the owner/repo identifier and branch with your actual lab repository.
cortexcli --upload-mode upload code scan --directory . --repo-id lab-owner/lab-app --branch main
```

Confirm repository attribution, scan status and exit behavior in your actual tenant. Read first: [Connect Cortex CLI](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/connect-cortex-cli); [Authenticate credentials](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/connect-cortex-cli/authenticate-credentials); [Cortex CLI Cortex Cloud Application Security command line reference](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference).

## Cloud capability and collector health

```text
dataset = cloud_health_auditing
| filter capability = "Outpost" and classification = "Error"
```

Use the query time picker to select the lab failure window. Inspect the returned fields before adding account/region filters. Start a separate query for collector connectivity transitions:

```text
dataset = collection_auditing
```

Filter that result using the actual collector identifiers shown in your tenant. An empty result may mean no matching event, no data, insufficient scope, or an incorrect time window; investigate before choosing an explanation. Read first: [Troubleshoot errors on cloud instances](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/troubleshoot-errors-on-cloud-instances); [Verify collector connectivity](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/administration-and-troubleshooting/verify-collector-connectivity).

## Synthetic classification sample

Use an invented pattern such as `LABID-[0-9]{6}` and the context word `training`. Test `training LABID-123456` as a positive sample, and `training LABID-ABCDEF` as a negative sample. Also test a valid identifier outside the configured proximity window. This is an original lab fixture, not a built-in detector name. Read first: [How to create and validate a custom data pattern](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-classification/how-to-create-and-validate-a-custom-data-pattern).

## Synthetic SARIF ingestion

Place `study-fixture.txt` in the disposable repository, and use `synthetic-findings.sarif.json` as the format fixture. Set the collector name to `cortex-study-fixture`. Validate in the collector UI, then use the generated API example to upload against the intended repository and branch. Verify the response, finding location and repository association. A successful format validation is not evidence of successful upload.

Read first: [Reference B: SARIF format and mapping](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/generic-3rd-party-appsec-collector/references/reference-b-sarif-format-and-mapping); [Configure the Generic 3rd Party AppSec Collector](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/generic-3rd-party-appsec-collector/tenant-console-workflow); [Upload findings from CI/CD pipelines](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/generic-3rd-party-appsec-collector/upload-findings-from-ci-cd-pipelines).
