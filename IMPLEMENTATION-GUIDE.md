# Cortex Cloud implementation study guide

**Review status:** This is a curriculum draft with references grouped primarily by objective. Before treating a section as a completed lesson, apply [the lesson standard](LESSON-STANDARD.md): source each factual explanation and procedural step, teach its concepts first, and map the lab to those concepts. No claim-level audit or live execution of the complete guide is asserted.

**Personalized study order:** Keep the objective numbering below as a reference, but follow the revised [study plan](STUDY-PLAN.md). Add the [CLI and Cytool lessons](COMMAND-LINE-LAB.md) to 5.5/4.1/6.2 and the [Kubernetes bridge](KUBERNETES-BRIDGE.md) to 3.7/4.1/3.4/6.2. Use [application and analysis practice](APPLICATION-ANALYSIS.md) throughout, beginning with unfamiliar topics in week 1. These additions preserve every original walkthrough.

This guide covers all **35 primary objectives and 11 numbered sub-objectives** in your July 2026 Cloud Security Engineer PDF. The PDF contains objectives rather than sample exam questions. Each section below turns one primary objective and its children into an implementation exercise, an observable result, and an explanation you should be able to give without notes.

Use [the weekly schedule](STUDY-PLAN.md) and [the objective tracker](objective-tracker.csv) together. Read the linked technical procedures **before** doing the exercise. The numbered steps are study exercises adapted from those procedures; lab names, fixtures, scheduling, and readiness thresholds are proposed study choices. Exact UI names and supported capabilities may differ with your tenant release. Sources were retrieved on **November 9, 2026**.

Start with one disposable application: a repository, a private AWS data store with synthetic records, one VM, one image/registry, and a simple function. Add a supported Kubernetes cluster, a CaaS deployment, and an API Gateway only for their exercises. Reuse these assets so you can follow the same application across code, build, deployment, and runtime. Use your authorized sandbox scope and keep a before-state and cleanup record for every exercise.

**Completion levels:** Read means you can explain the topic. Configured means you saved or deployed it. Verified means you observed the intended result and a useful negative/control case. Walkthrough means a complete configuration rehearsal without live access. Do not mark a walkthrough as a verified deployment. These labs have not been run in your tenant by this study-plan author.

**One unresolved documentation item:** Objective **5.2.2, AI-recommended guardrails**, appears in the supplied blueprint, but the reviewed public technical documentation did not establish its exact implementation workflow. It is explicitly retained below and in the tracker. The documented policy exercises do not substitute for that objective.

## Objective 1.1 Assess architecture and the existing environment

**Blueprint coverage:** 1.1. **Practice mode:** Build and explain.

**Read first:** [Plan and prepare](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/plan-and-prepare); [AWS security capabilities and deployment planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/aws-security-capabilities-and-deployment-planning); [Outpost fundamentals and planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-fundamentals-and-planning).

1. Inventory your sandbox: account IDs, regions, EC2, containers, Kubernetes, functions, registries, data stores, repositories, existing security tooling, and audit-log destinations. Record owners and what each source contributes.
2. Draw the intended flow from source systems to Cortex, including identity trust, scanning infrastructure, log collection, and runtime agents. Put current coverage and missing coverage next to each workload.
3. Write a migration sequence: establish asset visibility, validate scans and logs, introduce scoped policies, then validate protection. Identify which existing tools or log paths would overlap during transition.
4. Produce a one-page deployment design with a coverage table; do not assume that connecting an account proves every capability is working.

**Verify and save:** A diagram and inventory that explain how every lab workload will be discovered, scanned, and protected.

**Explain without notes:** Which components would you change for a customer with strict data-residency requirements?

## Objective 1.2 Choose licenses, retention, scanning, and IAM

**Blueprint coverage:** 1.2. **Practice mode:** Configure and explain.

**Read first:** [Understand license plans](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/get-started/understand-license-plans); [Data retention](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/get-started/understand-license-plans/data-retention); [Prerequisites for onboarding AWS](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/prerequisites-for-onboarding-aws); [AWS security capabilities and deployment planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/aws-security-capabilities-and-deployment-planning); [Outpost fundamentals and planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-fundamentals-and-planning); [AWS provider permissions](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/amazon-web-services-aws-provider-permissions).

1. Inspect Settings → Cortex License and record the actual base license, add-ons, workload capacity, and retention entitlements. Mark unavailable labs before you start them.
2. Build a capability matrix for posture, runtime, AppSec, log ingestion, and data scanning. Match your intended lab workloads to the documented metering categories.
3. Record retention requirements by dataset and compare them with the documented defaults and your purchased entitlements; do not treat all data types as having one retention period.
4. For AWS, distinguish the permissions needed by the person deploying the template from the permissions used by Cortex afterward. Read the generated IAM resources and the provider-permission explanation for each enabled capability.
5. Choose Cloud Scan or Outpost for this deployment and defend the choice using data handling, operations, permissions, and cost. Implement the chosen mode in week 2.

**Verify and save:** A license and permissions matrix, a retention worksheet, and a justified scanning choice.

**Explain without notes:** Why can a successful login coexist with an unavailable scanner or an API permission failure?

## Objective 1.3 Verify network communication

**Blueprint coverage:** 1.3. **Practice mode:** Implement.

**Read first:** [Enable access to required PANW resources](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/activate-cortex-cloud/enable-access-to-required-panw-resources); [Outpost fundamentals and planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-fundamentals-and-planning); [Set up and configure Broker VM](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/data-management/broker-vm/set-up-and-configure-broker-vm).

1. Find your tenant region and the exact current endpoint requirements for the components you intend to deploy. Create a matrix with source, destination FQDN, port, direction, and purpose.
2. Check DNS and HTTPS reachability from the actual lab VM, build runner, and outpost or Broker network, rather than only from your laptop. Use the documented regional endpoints.
3. Apply the required egress rules to the lab network. If a proxy or TLS inspection is present, compare its configuration with the component-specific documentation.
4. Record successful connectivity and one failed connection caused by a deliberately incorrect destination in a local test. Do not disrupt the shared tenant.

**Verify and save:** A region-specific connectivity matrix and evidence from each execution location.

**Explain without notes:** How would you distinguish a network failure from a successful network connection followed by a 403 response?

## Objective 1.4 Manage user identities, RBAC, SBAC, and API keys

**Blueprint coverage:** 1.4. **Practice mode:** Implement.

**Read first:** [Set up users, groups, and roles](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/set-up-users-and-roles); [Manage API keys](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/manage-api-keys); [Asset groups](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cloud-inventory-and-environment/asset-groups); [Manage user scope](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/post-deployment-steps/manage-user-roles-and-access-management/manage-user-scope).

1. In Settings → Configurations → Access Management, inspect a built-in role and create a restricted custom role for the lab. Record permitted actions separately from the assets the user may see.
2. Create a dynamic asset group using attributes supported for access management. Assign a lab test identity the custom role and an appropriate scope; keep an administrator session available.
3. With the test identity, compare an allowed asset with an out-of-scope asset and an allowed action with a disallowed action. Check both role and scope when results differ.
4. Create an API key with a suitable restricted role, scope, and expiration. Make a documented read operation, then revoke the key and verify authentication fails. Store only the key ID and results in your notes.
5. Explain the user lifecycle: identity source, group membership, role assignment, scope, key issuance, role changes, and revocation. Inspect your tenant authentication configuration without replacing its working identity provider.

**Verify and save:** An access matrix with positive and negative checks, plus an API-key lifecycle record.

**Explain without notes:** Does granting a role automatically grant visibility to every asset? Why can a static asset group be unsuitable for SBAC?

## Objective 1.5 Optimize scanning and log costs

**Blueprint coverage:** 1.5. **Practice mode:** Measure and explain.

**Read first:** [How to onboard Amazon Web Services](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/how-to-onboard-amazon-web-services); [Cortex Cloud and AWS audit log collection architecture](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/cortex-cloud-and-aws-audit-log-collection-architecture); [Outpost fundamentals and planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-fundamentals-and-planning); [Configure registry scanning for cloud accounts](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/registry-scanning/configure-registry-scanning-for-cloud-accounts); [AWS Cost Explorer filtering](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-filtering.html); [AWS Cost Explorer data freshness and daily costs](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-exploring-data.html).

1. Record a baseline of enabled scans, selected regions, image scan scope, audit trails, and log destinations.
2. Compare the existing CloudTrail delivery path with the proposed Cortex path. Draw where duplicate collection could occur before enabling an additional trail or ingestion path.
3. Review registry initial-scan selection and the cost tradeoff of Cloud Scan versus Outpost. Choose the smallest lab scope that still exercises the capability.
4. In AWS Cost Explorer, compare days and filter by account, service, region, and usage type. Record the change date alongside any scan or logging configuration change.
5. Write an optimization proposal and its coverage tradeoff. Check later billing data before claiming savings; current-period cost data can arrive late.

**Verify and save:** A baseline, a proposed change, and a method for measuring both cost and retained security coverage.

**Explain without notes:** Which evidence would separate increased event volume from duplicated log collection?

## Objective 2.1 Onboard cloud providers and security capabilities

**Blueprint coverage:** 2.1, 2.1.1, 2.1.2. **Practice mode:** AWS implementation plus multicloud walkthrough.

**Read first:** [Prerequisites for onboarding AWS](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/prerequisites-for-onboarding-aws); [How to onboard Amazon Web Services](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/how-to-onboard-amazon-web-services); [AWS security capabilities and deployment planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/aws-security-capabilities-and-deployment-planning); [AWS post-deployment verification](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/aws-post-deployment-verification); [Outpost fundamentals and planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-fundamentals-and-planning); [Outpost creation workflow](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-creation-workflow); [How to onboard Microsoft Azure](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/microsoft-azure-cloud-onboarding/how-to-onboard-microsoft-azure); [How to onboard Google Cloud Platform](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/google-cloud-platform-cloud-onboarding/how-to-onboard-google-cloud-platform); [How to onboard Oracle Cloud Infrastructure](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/oracle-cloud-infrastructure-cloud-onboarding/how-to-onboard-oracle-cloud-infrastructure); [Deploy the authentication template in AWS](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/deploy-the-authentication-template-in-aws); [AWS provider permissions](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/amazon-web-services-aws-provider-permissions); [Create a standard outpost](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/working-with-standard-outposts/create-a-standard-outpost); [Analytics overview](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/threat-management/analytics/analytics-overview).

1. Start with AWS account scope: Settings → Data Sources & Integrations → Add New → AWS. Select environment, scope, scan mode, region restrictions, and required capabilities; inspect the generated template.
2. Deploy the account template using its supported CloudFormation or Terraform path. Preserve generated trust parameters. For Terraform, retain the original deployment directory and state for later updates.
3. Verify the new Connected cloud instance, discovered assets, and the status of each enabled capability. Validate audit logs, agentless disk scanning, registry scanning, serverless scanning, DSPM, and automation independently; a capability without a test resource remains unverified.
4. Repeat the configuration walkthrough for Organization or OU scope. Use CloudFormation for that scope, inspect the OU and account boundaries, deploy only into an authorized sandbox organization, and verify member-account results. If you only have one AWS account, record this as a walkthrough, not a completed organization lab.
5. For Outpost, create a standard AWS outpost, deploy its generated template, verify Connected status, then select it in cloud onboarding and run a scan. Compare its resource footprint with Cloud Scan. Use the appropriate template workflow rather than treating an outpost as an endpoint agent.
6. Build and explain three additional configuration sheets from the provider wizards: Azure tenant/management-group/subscription and service principal; GCP organization/folder/project; OCI tenancy and compartment selection. Include authentication, template deployment, enabled capabilities, and verification. Execute each only if that provider is available.
7. For the Cortex XSIAM analytics example in the blueprint, inspect the actual licensed analytics configuration and its required telemetry; do not mark analytics enabled simply because AWS ingestion is Connected. Complete the runtime analytics exercise in 4.4.

**Verify and save:** For AWS, save deployed-template references, discovered assets, capability statuses, and one scan/log result per exercised capability. For other providers, save complete deployment worksheets and explicitly mark whether deployed.

**Explain without notes:** How would you prove an organization integration covers a newly included member account? When would you choose Outpost?

## Objective 2.2 Connect data and AI sources

**Blueprint coverage:** 2.2. **Practice mode:** Conditional implementation and walkthrough.

**Read first:** [How to onboard Microsoft 365](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/microsoft/microsoft-365-posture/how-to-onboard-microsoft-365); [How to onboard Databricks](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/databricks/how-to-onboard-databricks); [Supported services in Cortex Cloud AI Security](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-ai-security/supported-services-in-cortex-cloud-ai-security); [How to configure the scanning settings for supported services](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/administration-and-troubleshooting/manage-instances/how-to-configure-the-scanning-settings-for-supported-services).

1. For Microsoft 365, add the data source, supply the documented tenant ID and region, perform administrator authorization, and verify the instance. Use a sandbox tenant with synthetic data if available.
2. For Databricks, collect the account and application IDs and required administrator permissions. Add Databricks, configure cloud/network details, review and run the generated script in the documented CLI environment, and use Verify Connection.
3. For Azure AI Foundry, follow Azure onboarding and the AI Security service prerequisites. Current documentation requires Outpost and DSPM for full Azure AI asset discovery; record those prerequisites in the worksheet before deployment.
4. Use AWS AI services already available in your lab to inspect AI asset discovery and related findings. Compare supported services with the AI inventory; do not provision costly AI training simply to populate a screen.
5. For an unavailable service, complete an input/permissions/network/verification worksheet and rehearse the wizard from the documentation. Leave its live validation unchecked.

**Verify and save:** One connection and discovery record for each available source; complete implementation worksheets for Microsoft 365, Databricks, and Foundry even when access is unavailable.

**Explain without notes:** Why might general cloud assets be visible while AI assets remain incomplete?

## Objective 2.3 Integrate GitHub and Jenkins

**Blueprint coverage:** 2.3. **Practice mode:** Implement where available.

**Read first:** [GitHub SaaS](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-version-control-systems/github-cloud); [Onboard the shared Cortex GitHub App](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-version-control-systems/github-cloud/onboard-a-cortex-github-app); [Jenkins for CI/CD pipeline scans](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-cicd-systems/jenkins-for-cicd-pipeline-scans); [Jenkins for code scans](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/integrate-ci-tools/jenkins-for-code-scans).

1. Create or use a disposable repository within a GitHub organization you can administer. Add GitHub SaaS in Cortex, choose the GitHub App ownership model, authorize selected repository access, and finish repository selection.
2. Verify the instance and repository are connected. Run an initial repository scan and record the commit/branch scanned.
3. For Jenkins pipeline scanning, add Jenkins with CI/CD System Scan, download the provided HPI plugin, install it under Manage Jenkins → Plugins, and configure its generated JWT under Manage Jenkins → System → Cortex Cloud. Verify Connected status.
4. For Jenkins code scanning, create a separate Code Scan integration, store CORTEX_API_KEY and CORTEX_API_KEY_ID in Jenkins Credentials, and use the wizard-generated pipeline configuration on a suitable Docker-capable runner.
5. Run a build and confirm the scan is associated with the intended repository and commit. Keep the two Jenkins integration types distinct in your notes.

**Verify and save:** A connected repository and one attributable scan; Jenkins plugin and code-pipeline evidence if Jenkins is available.

**Explain without notes:** Why can a working Jenkins pipeline-risk integration still leave code scans absent?

## Objective 2.4 Integrate container registries

**Blueprint coverage:** 2.4. **Practice mode:** Implement one and compare all named examples.

**Read first:** [Configure registry scanning for cloud accounts](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/registry-scanning/configure-registry-scanning-for-cloud-accounts); [Configure registry scanning for third party integrations](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/registry-scanning/configure-registry-scanning-for-third-party-integrations); [Connect Docker Hub registry](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/docker/connect-docker-hub-registry); [Connect GitLab container registry](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/gitlab/connect-gitlab-container-registry); [Connect JFrog container registry](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/jfrog/connect-jfrog-container-registry).

1. Enable AWS ECR registry scanning in your AWS integration, choose an initial scan scope, and push a harmless lab image. Confirm the image identity and resulting scan details.
2. Add a separate third-party registry through Data Sources & Integrations → Add New → Container Registries. Select Docker Hub, GitLab, or JFrog according to your access.
3. Follow that connector’s credential, URL, network, and repository-selection requirements. Save the configuration and verify the intended registry repositories are visible.
4. For the other two named registry examples, prepare the exact input and permission worksheet from their individual documentation rather than assuming credentials are interchangeable.
5. Compare an in-scope image with an excluded image; explain which connector and scope control each result.

**Verify and save:** One cloud-registry scan, one third-party scan when available, and Docker/GitLab/JFrog configuration comparison sheets.

**Explain without notes:** How is third-party registry integration different from enabling a capability on an onboarded AWS account?

## Objective 2.5 Ingest third-party SAST and SCA results

**Blueprint coverage:** 2.5. **Practice mode:** Implement Generic SARIF and walk through vendors.

**Read first:** [Semgrep](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/semgrep); [Veracode](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/veracode); [Reference B: SARIF format and mapping](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/generic-3rd-party-appsec-collector/references/reference-b-sarif-format-and-mapping); [Configure Semgrep ingestion](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/semgrep/configure-semgrep-ingestion); [Configure the Generic 3rd Party AppSec Collector](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/generic-3rd-party-appsec-collector/tenant-console-workflow); [Upload findings from CI/CD pipelines](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/generic-3rd-party-appsec-collector/upload-findings-from-ci-cd-pipelines).

1. For Semgrep, add the integration, authorize its Web API token, select SAST/SCA, map projects to onboarded repositories, and verify the connected mapped projects.
2. For Veracode, provide the documented credentials and region, authorize, select applications, confirm repository mappings, and verify ingestion. Record its documented scan and enforcement limitations.
3. For Generic SARIF, create a 3rd Party AppSec Collector. Match its name to the SARIF tool name, save its generated credentials securely, and copy its upload endpoint.
4. Validate a SARIF 2.1.0 file containing a rule ID, matching result, message, relative file URI, and start line. Use the provided fixture in examples as a format exercise.
5. Upload through the documented API workflow or the collector’s generated example, then verify repository attribution and finding location. UI validation alone is not a completed ingestion test.

**Verify and save:** A validated and ingested synthetic finding tied to its repository and source location; vendor mapping worksheets.

**Explain without notes:** Why can an authenticated connector ingest no results when project mapping is missing?

## Objective 2.6 Deploy and configure Broker VM

**Blueprint coverage:** 2.6. **Practice mode:** Implement or supervised sandbox lab.

**Read first:** [Set up Broker VM on Amazon Web Services](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/data-management/broker-vm/set-up-and-configure-broker-vm/broker-vm-image-installations/set-up-broker-vm-on-amazon-web-services); [Set up and configure Broker VM](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/data-management/broker-vm/set-up-and-configure-broker-vm).

1. Read the Broker VM compatibility, sizing, network, and registration requirements. Choose an available supported deployment target and record why this lab needs a Broker.
2. For AWS, download the authorized Broker image, configure the documented VM import role, upload/import the image, and create the AMI using the AWS deployment procedure. Use the exact current import commands and AMI settings from that page.
3. Launch the Broker with the documented resources and network access; complete its initial configuration and registration with Cortex.
4. Activate only the collector applet needed for your selected test source, then send a small test record and verify collector health and received data.
5. Capture the image/instance identity, registration result, applet configuration, and cleanup plan. Explain the separate purposes of Broker VM and Outpost.

**Verify and save:** A registered Broker and a functioning test collector, or a fully specified deployment worksheet if sandbox access prevents deployment.

**Explain without notes:** Which component would you inspect for a collector failure versus a workload scanning failure?

## Objective 3.1 Create an XQL dashboard

**Blueprint coverage:** 3.1. **Practice mode:** Implement.

**Read first:** [Troubleshoot errors on cloud instances](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/troubleshoot-errors-on-cloud-instances); [Create XQL widgets](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/dashboards-and-reports/monitor-dashboards-and-reports/advanced-configuration/create-custom-widgets/create-xql-widgets); [Create dashboards](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/dashboards-and-reports/monitor-dashboards-and-reports/create-dashboards).

1. Run a query against a dataset that actually exists in your sandbox. Start with cloud_health_auditing and inspect the returned fields and time window.
2. In Widget Library, choose Create widget → XQL widget. Name it, keep visibility restricted to the lab, enter the query, and Preview the results.
3. Use a table initially; then create an appropriate count or grouped chart after verifying the query output. Compare the widget with the direct query over the same time range.
4. Create a custom dashboard, add the saved widget, and add a title describing its scope. Configure a parameterized filter or drilldown using the documented widget options.
5. Save evidence of the query, preview, dashboard, and filter behavior. An empty result is a coverage or time-window question to investigate, not proof of zero risk.

**Verify and save:** A working dashboard whose counts match a direct query and whose scope you can explain.

**Explain without notes:** Why might a dashboard show no events while its data source is Connected?

## Objective 3.2 Create static and dynamic asset groups

**Blueprint coverage:** 3.2. **Practice mode:** Implement.

**Read first:** [Asset groups](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cloud-inventory-and-environment/asset-groups).

1. Open Inventory → Assets → Groups → Add Group. Create one static group containing explicitly selected lab assets.
2. Create a dynamic group using attributes present on those assets, such as provider and region. Preview which assets match before saving.
3. Introduce or modify a lab asset so that it enters or leaves the dynamic criteria; observe membership after inventory refresh. Compare the static group.
4. Create an additional dynamic group using only access-management-supported fields and use it in the access-control lab.
5. Apply an asset group to a lab policy and verify that excluded assets are not targeted.

**Verify and save:** Static and dynamic membership evidence, plus a tested policy scope.

**Explain without notes:** How does changing an asset attribute affect dynamic membership, and why are static groups not the SBAC choice?

## Objective 3.3 Create cloud security rules and policies

**Blueprint coverage:** 3.3. **Practice mode:** Implement six rule types.

**Read first:** [Create a cloud security policy](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-policies/create-a-cloud-security-policy); [Create and manage cloud security rules](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules); [Create a configuration rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules/create-a-configuration-rule); [Create an identity rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules/create-an-identity-rule); [Create a network exposure rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules/create-a-network-exposure-rule); [Create an AI rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules/create-an-ai-rule); [Create a data rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules/create-a-data-rule); [Create an attack path (legacy) rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-security-rules-and-policies/create-and-manage-cloud-security-rules/create-an-attack-path-rule).

1. Under Posture Management → Rules & Policies → Rules → Cloud Security, create a Config rule. Name it, select severity, define a simple query against an observed lab configuration, and Search/Test before saving.
2. Create an Identity rule using an identity, its effective permissions, and a resource relationship. Test it against lab data and explain why the permission is excessive or unused.
3. Create a Network Exposure rule; choose inbound, outbound, or east-west and specify the relevant source, destination asset, and protocol/port conditions. Use existing sandbox examples; do not expose a vulnerable host merely to force a finding.
4. Create a Data rule using the available data criteria, and an AI rule using a discovered AI asset and its attributes. Use synthetic classified data. If there are no AI assets, save and test the rule configuration but mark positive-result validation as pending.
5. Create an Attack Path rule using the documented interface available in your tenant. The currently retrieved custom creation guide labels its workflow Attack Path (Legacy); combine observed finding/vulnerability conditions and test the result. Do not assume a newly named attack-path UI has identical behavior.
6. Create a Cloud Security policy, select the saved rules, explicitly scope it to lab accounts/groups, and save. Compare rule matches, policy scope, generated issues, and remediation after a controlled correction.

**Verify and save:** Six rule worksheets or saved configurations, a scoped policy, and before/after evidence for the rule types with available data.

**Explain without notes:** What does the rule decide, what does the policy decide, and why might a matching rule generate no issue for an excluded asset?

## Objective 3.4 Create workload rules and policies

**Blueprint coverage:** 3.4. **Practice mode:** Implement.

**Read first:** [Cloud workload policies and rules](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules); [Trusted image cloud workload policies](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/types-of-cloud-workload-policies/types-of-cloud-workload-policies); [Create a new custom detection rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-rules/create-a-new-custom-detection-rule); [Create a cloud workload policy](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/create-a-cloud-workload-policy).

1. Create a custom Cloud Workload rule. Choose its scanner deliberately: Agentless Disk Scan, Kubernetes Connector, or XDR Agent. Use the documented example for that scanner, adapt it to a harmless lab condition, and validate the rule logic.
2. Associate the rule with a custom compliance control where required. Explain the input data and execution mechanism for each scanner, even if only one scanner is available.
3. Create separate lab-scoped misconfiguration, malware, secrets, and trusted-image policy configurations. Inspect the available stages/actions for each type; do not assume every rule supports prevention.
4. Start with issue creation. Use an available known finding or benign vendor-supported test fixture; do not introduce real malware or live credentials to manufacture a match.
5. For trusted images, specify a trust criterion, enable the admission controller on the lab cluster, and test a compliant image and a harmless image that violates the trust criterion. Compare new deployment behavior with already-running workload findings.
6. Record policy scope, scanner coverage, action, and conflicting-policy behavior. Trusted-image policy resolution must be learned from its own documentation, rather than borrowed from endpoint policy ordering.

**Verify and save:** One validated custom rule, four policy-type configurations, and an admission-control allow/block result when the connector supports it.

**Explain without notes:** Can registry vulnerability scanning alone establish that an image is trusted by your organization?

## Objective 3.5 Manage vulnerability issue and prevention policies

**Blueprint coverage:** 3.5. **Practice mode:** Implement.

**Read first:** [Create a vulnerability policy](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/vunerability-management/vulnerability-policies/create-a-vulnerability-policy); [Trusted image cloud workload policies](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/types-of-cloud-workload-policies/types-of-cloud-workload-policies).

1. Open Posture Management → Rules & Policies → Policies → Vulnerability Management → Add Policy.
2. Create an issue-creation policy using a finding that already exists in the lab. Set conditions, preview matching findings, select an explicit asset group, and set the issue action/severity.
3. Save and position the policy intentionally in the policy list. Check a broad and a specific policy against the same finding.
4. Create a separate prevention policy and inspect its supported enforcement prerequisites in the linked policy documentation before testing on a disposable workload.
5. Fix or replace the affected test artifact, rescan, and check the subsequent policy result. Document CVSS alongside the environmental context used to prioritize the finding.

**Verify and save:** A matching issue, a nonmatching control case, a configured prevention test, and a verified remediation result.

**Explain without notes:** Why are a high CVSS score, an issue severity, and an actual prevention action different things?

## Objective 3.6 Build compliance standards, controls, assessments, and reports

**Blueprint coverage:** 3.6. **Practice mode:** Implement.

**Read first:** [Choose compliance standards from the compliance catalog](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/compliance/monitor-and-track-compliance-adherence/choose-compliance-standards-from-the-compliance-catalog); [Use an assessment profile to run compliance checks on your assets](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/compliance/monitor-and-track-compliance-adherence/use-an-assessment-profile-to-run-compliance-checks-on-your-assets); [Use a built-in or custom standard](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/compliance/monitor-and-track-compliance-adherence/choose-compliance-standards-from-the-compliance-catalog/use-a-built-in-or-custom-standard); [Use a built-in or custom control](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/compliance/monitor-and-track-compliance-adherence/choose-compliance-standards-from-the-compliance-catalog/use-a-built-in-or-custom-control).

1. Open Posture Management → Compliance → Catalogs and inspect an out-of-the-box standard, its controls, and associated rules.
2. Clone a built-in standard with Save as new, or create a small custom standard. Add a category and custom control and associate a custom detection rule with that control.
3. Ensure a cloud security policy includes the custom cloud rule and targets the same intended lab scope; the assessment configuration does not replace this policy.
4. Create an Assessment Profile, select the standard and lab asset group, review the summary, and save. Generate/review the resulting assessment and report; keep delivery within your sandbox.
5. Correct the tested configuration and rerun the assessment. Trace one failed control all the way to its rule and asset, then explain the new result.

**Verify and save:** Built-in and custom assessment results, a report, and a standard → control → rule → policy → asset trace.

**Explain without notes:** Why can a custom assessment be misleading when its custom rule is not enabled through a policy?

## Objective 3.7 Deploy the Kubernetes connector

**Blueprint coverage:** 3.7. **Practice mode:** Implement.

**Read first:** [Onboard the Kubernetes Connector](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/onboard-the-kubernetes-connector); [Trusted image cloud workload policies](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/types-of-cloud-workload-policies/types-of-cloud-workload-policies).

1. Use a disposable supported Kubernetes cluster. Open Data Sources & Integrations and add Kubernetes.
2. Choose Posture Management and, when licensed, Realtime Protection. Inspect advanced settings including scan cadence, admission-controller enforcement, and agent-related options.
3. Download the generated installer and review its requested cluster permissions and settings. Execute the generated instructions against the intended kubectl context.
4. Verify connector status, discovered cluster/namespaces/workloads, and scanner results. Keep posture collection and runtime protection validation as separate checks.
5. Test admission enforcement with the harmless trusted-image policy from 3.4. Confirm a permitted deployment still works, then restore the lab policy state.

**Verify and save:** Installer configuration, healthy connector evidence, discovered workload, and one scoped enforcement test.

**Explain without notes:** Why is a connected posture connector not sufficient proof that runtime prevention is active?

## Objective 3.8 Configure data classification and scanning

**Blueprint coverage:** 3.8. **Practice mode:** Implement.

**Read first:** [How to onboard Amazon Web Services](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/how-to-onboard-amazon-web-services); [How to create and validate a custom data pattern](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-classification/how-to-create-and-validate-a-custom-data-pattern); [How to configure the scanning settings for supported services](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/administration-and-troubleshooting/manage-instances/how-to-configure-the-scanning-settings-for-supported-services).

1. Enable DSPM for the relevant AWS integration and inspect the supported-service scanning controls for your lab data store.
2. Use a private lab bucket containing synthetic records only. In Settings → Configurations → Data Classification → Data Patterns, add a pattern for an invented identifier such as LABID-[0-9]{6}.
3. Set a context word, proximity, and masking level. Use the built-in validator with a matching sample and nonmatching samples; include one sample where the context is too far away.
4. Associate the pattern with a custom data profile as described in the classification documentation. Run or await the configured supported scan and inspect the classification results.
5. Check scope, scanner permissions, profile association, and masking when the expected result is missing. Record that custom patterns have platform-wide applicability, so use a narrowly distinctive test format.

**Verify and save:** Validator results plus a discovered, classified synthetic record and the corresponding scan configuration.

**Explain without notes:** How can a valid regex still fail to classify a record because of context or proximity settings?

## Objective 4.1 Deploy agents to VMs, CaaS, Kubernetes, and functions

**Blueprint coverage:** 4.1. **Practice mode:** Implement supported AWS variants.

**Read first:** [Create an agent installation package](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/create-an-agent-installation-package); [Monitor agent operational status](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/manage-endpoint-protection/monitor-agent-operational-status); [CaaS Workloads](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/endpoint-protection/caas-workloads); [Set up serverless function protection](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/serverless-function-runtime-security/set-up-serverless-function-protection).

1. Create an installation matrix for EC2 VM, Kubernetes, ECS Fargate/CaaS, and Lambda/serverless: supported runtime/OS, package type, resource requirements, permissions, and required connectivity. Check the linked compatibility matrix before deployment.
2. For the VM, open Inventory → Endpoints → Agent Installations, create a suitable Standalone package, and run that package’s installation procedure on the lab instance. Verify registration and operational status.
3. For Kubernetes, create the documented Kubernetes or Helm package, or use the runtime option in the Kubernetes onboarding workflow appropriate to your deployment. Check the intended nodes and namespaces and avoid installing the agent twice.
4. For CaaS, generate the CaaS Dockerfile/package, embed the agent according to the documented build instructions, and deploy the harmless image to supported ECS Fargate. Check architecture, resources, SYS_PTRACE, and entrypoint constraints against the CaaS guide.
5. For serverless, select the Serverless function package, use its generated instructions for the supported function runtime, and configure the applicable restriction profile and policy. Invoke the benign lab function and check runtime visibility.
6. For each variant, record successful deployment separately from demonstrated protection. Mark a variant as a walkthrough if your license or runtime cannot support it.

**Verify and save:** A four-row deployment matrix and live registration/protection evidence for each supported environment.

**Explain without notes:** How do VM installation, Kubernetes deployment, container-embedded agents, and function packages differ?

## Objective 4.2 Configure endpoint groups, prevention, extensions, and exceptions

**Blueprint coverage:** 4.2, 4.2.1, 4.2.2. **Practice mode:** Implement.

**Read first:** [Set up endpoint profiles and exception rules](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/set-up-endpoint-profiles-and-exception-rules); [Define endpoint groups](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/define-endpoint-groups); [Apply profiles to endpoints](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/apply-profiles-to-endpoints); [Set up exception profiles and rules](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/set-up-endpoint-profiles-and-exception-rules/set-up-exception-profiles-and-rules); [File Integrity Monitoring (FIM)](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/endpoint-protection/file-integrity-monitoring-fim).

1. Create a static and a dynamic endpoint group under Inventory → Endpoints → Groups. Verify membership using actual registered lab endpoints.
2. Create or clone the appropriate malware, exploit, restrictions, and agent-settings profiles for your lab platform. Review their settings before assignment.
3. Create a Prevention policy rule, attach the profiles, target the lab group, and deliberately position it in the ordered policy list. Verify the effective policy on the endpoint.
4. For an extension example, configure a FIM rule group for a harmless lab directory, create a FIM extension profile, and assign it through an Extensions policy. Check the FIM license/agent prerequisites first; modify a test file and find its event.
5. Create a narrowly scoped exception using the documented exception type applicable to your benign test. Compare behavior with and without it, then remove the exception.
6. Export or record the final policy configuration, membership, effective profile, and rollback steps.

**Verify and save:** Effective endpoint policy, a FIM event where licensed, and an exception test with restoration.

**Explain without notes:** Why can creating a profile have no effect until a policy assigns it? How does the first matching endpoint policy affect the result?

## Objective 4.3 Integrate API gateways

**Blueprint coverage:** 4.3. **Practice mode:** AWS implementation plus Azure and Apigee walkthrough.

**Read first:** [Ingest AWS API Gateway](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/api-security/ingest-data-for-api-security/ingest-aws-api-gateway); [Ingest Azure APIM](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/api-security/ingest-data-for-api-security/ingest-azure-apim); [Ingest Apigee Proxy](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/api-security/ingest-data-for-api-security/ingest-apigee-proxy).

1. Add AWS API Gateway in Cortex Data Sources & Integrations, create the collector, and securely retain its generated key and endpoint.
2. On a disposable AWS API Gateway REST API stage, configure the documented CloudWatch role, logs/tracing, and access-log format. Use synthetic request data.
3. Create the Data Firehose stream with the documented HTTP endpoint destination, authentication, compression, and failed-record backup. Add the CloudWatch subscription and IAM role described in the guide.
4. Send a benign request to the API and trace it through CloudWatch, delivery, and Cortex. Diagnose each hop separately if the event is absent.
5. For Azure APIM, create the Cortex collector, configure APIM named values (including the secret key), and apply the documented inbound/outbound policy to a test API; send a request and verify ingestion. For Apigee, create the collector, download its configuration package, set project/organization/environment/URL/key, deploy the documented shared flows and hooks, and validate a request. Rehearse these exact configurations from the docs when the services are unavailable.

**Verify and save:** An end-to-end AWS API request trace and complete APIM/Apigee configuration walkthroughs.

**Explain without notes:** Which evidence separates a gateway logging problem from an HTTP collector authentication problem?

## Objective 4.4 Configure detection rules and automation playbooks

**Blueprint coverage:** 4.4, 4.4.1, 4.4.2. **Practice mode:** Implement.

**Read first:** [What are detection rules?](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/threat-management/detection-rules/what-are-detection-rules); [Create a correlation rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/threat-management/detection-rules/what-are-detection-rules/whats-a-correlation-rule/create-a-correlation-rule); [Test your playbook](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cases-and-issues/investigation-and-response/automation/playbooks/build-your-playbook/test-your-playbook); [Create a BIOC rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/threat-management/detection-rules/what-are-detection-rules/whats-a-bioc/create-a-bioc-rule); [Create an IOC rule](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/threat-management/detection-rules/what-are-detection-rules/whats-an-ioc/create-an-ioc-rule); [Build your playbook](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cases-and-issues/investigation-and-response/automation/playbooks/build-your-playbook); [Analytics overview](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/threat-management/analytics/analytics-overview).

1. Choose a harmless test event already observable in your sandbox. Identify its dataset, timestamp, asset, and relevant fields before creating any rule.
2. Create a lab IOC for a benign test artifact and a BIOC for a harmless observable behavior using the documented rule builders. Save, produce matching and nonmatching activity, and verify results; label all test artifacts clearly.
3. Create an XQL correlation rule, test the query, choose its schedule or supported real-time mode, map issue fields, and configure suppression and the action. Use a dataset output while tuning, then test issue generation in the lab.
4. Inspect Analytics configuration, available sensors, and an analytics-generated example. Explain what data the engine uses and why one manually generated event does not prove a baseline-driven analytics detector is working.
5. Build a small playbook with input validation, a condition, a manual review step, and a harmless enrichment or lab-only remediation task. Attach it to the appropriate test workflow.
6. Debug using mock issue data, breakpoints, and explicit input/output checks. Inspect actual external actions before running tasks; the debugger is not a guarantee that external commands are side-effect-free.
7. Validate the remediation against the source resource and a subsequent scan/event. Save the detection → issue → playbook → corrected-state trace.

**Verify and save:** IOC, BIOC, correlation and analytics worksheets; a tested playbook and one complete response trace.

**Explain without notes:** When should you use an IOC, BIOC, correlation rule, or analytics detection? How do you prove an automation succeeded beyond its task status?

## Objective 5.1 Manage business applications and issue SLAs

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

## Objective 5.2 Deploy AppSec rules, policies, and guardrails

**Blueprint coverage:** 5.2, 5.2.1, 5.2.2, 5.2.3. **Practice mode:** Implement policies; resolve one documented coverage gap.

**Read first:** [Create an AppSec policy](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/unified-application-security-policies/tenant-ui-workflow/create-a-policy); [Create CI/CD configuration policies](https://cortex-docs.paloaltonetworks.com/application-security/software-supply-chain-security/governance-and-enforcement/cicd-policies/create-cicd-configuration-policies); [Create custom Cortex Cloud Application Security rules](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/application-security-rules/tenant-ui-workflow/create-custom-cortex-cloud-application-security-rules); [Cloud Security Engineer July 2026 exam blueprint](https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/datasheets/palo-alto-networks-cloudsec-engineer.pdf).

1. For 5.2.1, create a custom IaC or secrets rule under Application Security → AppSec Rules. Set framework/scanner, severity, category, and remediation; validate the YAML and test it against one matching and one nonmatching lab fixture.
2. Create an AppSec policy using the current wizard: General, Conditions, Scope, Triggers & Actions, Exceptions, Summary. Select the relevant finding types, the lab repository/application, and supported periodic/PR/CI triggers.
3. Trigger a violating pull request or CI scan, inspect its policy result, fix the fixture, and rerun. Confirm that the intended policy caused the outcome rather than relying on a generic pipeline failure.
4. For 5.2.3, create a CI/CD Configuration Scanners policy, define a CI/CD risk condition, choose a lab scope, and use the triggers/actions supported by that policy type. Inspect an actual pipeline or VCS configuration finding.
5. For 5.2.2, preserve the exact blueprint topic, AI-recommended guardrails. The public documentation reviewed did not establish a step-by-step workflow under that name. Keep this child objective marked Documentation gap. Locate the applicable lesson in the official learning path or obtain a current vendor documentation link for the feature in your tenant, then add its verified steps here.
6. Once that documentation is available, record the recommendation, inspect the proposed scope/action, apply it only to the lab, and run matching/nonmatching checks. This last line is a proposed validation exercise, not a claim that a particular recommendation UI exists.

**Verify and save:** A custom rule, an exercised code policy, and a CI/CD policy. Objective 5.2.2 remains open until its exact documented workflow is identified and rehearsed.

**Explain without notes:** How do code scan policies differ from CI/CD configuration policies? What must you verify before accepting an AI-proposed control?

## Objective 5.3 Configure repository scanning and IaC drift

**Blueprint coverage:** 5.3. **Practice mode:** Implement.

**Read first:** [IaC Drift Detection scans](https://cortex-docs.paloaltonetworks.com/application-security/code-security/code-security-scanners/iac-drift-detection-scans); [Scan settings](https://cortex-docs.paloaltonetworks.com/application-security/settings/application-security-settings/scan-settings); [Code to Cloud troubleshooting](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/code-to-cloud/code-to-cloud-troubleshooting); [Global scan configurations](https://cortex-docs.paloaltonetworks.com/application-security/settings/application-security-settings/scan-settings/global-scan-configurations); [Custom scan configurations](https://cortex-docs.paloaltonetworks.com/application-security/settings/application-security-settings/scan-settings/custom-scan-configurations).

1. Open the lab repository’s Scan Configuration through its VCS integration. Inspect whether it follows Global settings or uses Custom settings.
2. Use repository-specific settings to enable IaC, SCA, secrets, and PR scanning for the lab. Record history scanning, validation, path exclusions, and behavior on scan errors. Avoid overwriting other repositories’ custom settings.
3. Prepare separate fixtures: an IaC violation selected from a documented enabled rule, a dependency finding you can reproduce, and an obviously synthetic secret-pattern sample. Scan, fix, and rescan each; a synthetic string is not guaranteed to match every built-in secrets detector.
4. For drift, deploy a harmless IaC-defined resource only after cloud/repository integration and code-to-cloud mapping are working. Use the required mapping/tagging workflow and confirm lineage first.
5. Select a documented security rule, make a reversible lab configuration change that violates it while code remains compliant, and inspect the drift finding. Restore the configuration from code and recheck.
6. Distinguish raw findings from policy-created issues and security-relevant drift from arbitrary configuration differences. Record the missing prerequisites if a positive drift test cannot be reproduced.

**Verify and save:** Before/after results for IaC, SCA, and secrets; scanner configuration evidence; and a mapped resource with a drift/remediation trace.

**Explain without notes:** Why might changing a cloud resource fail to generate a drift issue even though its configuration differs from Git?

## Objective 5.4 Use VS Code and JetBrains security plugins

**Blueprint coverage:** 5.4. **Practice mode:** Implement at least one and rehearse both.

**Read first:** [Visual Studio (VS) Code and VS Code compatible IDEs](https://cortex-docs.paloaltonetworks.com/application-security/code-security/ide/visual-studio-vs-code-and-vs-code-compatible-ides); [JetBrains](https://cortex-docs.paloaltonetworks.com/application-security/code-security/ide/jetbrains).

1. Check each plugin’s documented host architecture, runtime dependencies, AppSec entitlement, and CLI permissions before installing.
2. Generate a suitably scoped Standard API key and retrieve its ID and tenant API URL. Use the documented authentication fields rather than assuming an Advanced key works.
3. Install the official Cortex plugin in VS Code, configure authentication, open the lab project, and scan a known fixture. Read the finding’s explanation and apply a correction; rescan.
4. Repeat in JetBrains if installed. Otherwise, walk through its actual configuration screens from the documentation and record the required fields and dependencies.
5. Compare IDE results with the repository/CLI scan of the same commit and configuration. Investigate path exclusions or scanner differences before assuming results must be identical.

**Verify and save:** A successful IDE scan and remediation, plus configuration evidence or a complete walkthrough for the second IDE.

**Explain without notes:** What would you check when authentication works elsewhere but IDE scanning fails?

## Objective 5.5 Install, authenticate, and execute Cortex CLI

Complete the [command-line troubleshooting supplement](COMMAND-LINE-LAB.md) for argument inspection, exit-code handling and local debug logs.

**Blueprint coverage:** 5.5. **Practice mode:** Implement.

**Read first:** [Application Security Cortex CLI](https://cortex-docs.paloaltonetworks.com/application-security/code-security/application-security-cli); [Connect Cortex CLI](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/connect-cortex-cli); [Authenticate credentials](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/connect-cortex-cli/authenticate-credentials); [Cortex CLI Cortex Cloud Application Security command line reference](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference).

1. Use the current Connect Cortex CLI instructions for your host and tenant to obtain the executable. Validate local requirements and record the installed version/help output.
2. Configure CORTEX_API_BASE_URL, CORTEX_API_KEY, and CORTEX_API_KEY_ID through a protected credential file or environment variables. Select a Standard key and permissions appropriate to local-only versus uploaded scans.
3. From the disposable lab repository, run a local code scan using the documented directory flag and no-upload mode. Use examples/cli-and-xql.md as a starting command reference.
4. Run an uploaded scan with the correct owner/repo identifier and branch. Confirm its results are attributed to the intended repository rather than an unrelated asset ID.
5. Add the same scan to your CI job with credentials in its secret store. Test a finding-triggered failure, an authentication failure, and a clean run; record what each exit status actually means in your installed version.
6. Compare no-upload, no-code, and upload behavior from the documentation and choose the correct mode for your lab’s data handling requirements.

**Verify and save:** A reproducible local command, an attributed uploaded scan, and a CI run that distinguishes scan findings from scanner failure.

**Explain without notes:** Why might a scan run locally but fail when uploading, or upload into the wrong repository context?

## Objective 6.1 Diagnose IAM, template, organization, and ingestion failures

**Blueprint coverage:** 6.1. **Practice mode:** Break and repair in the lab.

**Read first:** [AWS post-deployment verification](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/aws-post-deployment-verification); [Troubleshoot errors on cloud instances](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/troubleshoot-errors-on-cloud-instances); [Deploy the authentication template in AWS](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/deploy-the-authentication-template-in-aws); [AWS provider permissions](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/amazon-web-services-aws-provider-permissions); [Verify collector connectivity](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/administration-and-troubleshooting/verify-collector-connectivity).

1. Start with a known working AWS integration and save its configuration. Use a dedicated disposable test instance for fault injection.
2. Practice a missing-permission case on that test role: record the exact denied action and capability error, compare with the provider permission table, restore the missing permission, and verify recovery.
3. For a stack failure, inspect CloudFormation Events and the first causal resource failure; for Terraform inspect the failing resource and retained state. Correct the stated prerequisite and rerun the supported template workflow.
4. For organization coverage, compare configured OU/account selection with discovered member accounts and per-account capability status. Inspect the generated organization deployment and its failed member deployment rather than treating the management-account status as sufficient.
5. For ingestion, follow the configured log path through delivery, permissions, notifications, and collector status. Query collection_auditing for collector transitions and cloud_health_auditing for cloud capability errors.
6. If CloudFormation succeeds but Cortex never shows a new connected instance, check the registration Lambda/CloudWatch evidence described in the post-deployment guide. Capture error, fix, recovery, and fresh ingested data.

**Verify and save:** A fault report with the causal error, minimal correction, and fresh post-recovery evidence.

**Explain without notes:** Why can CREATE_COMPLETE coexist with missing registration, missing member accounts, or missing logs?

## Objective 6.2 Diagnose agent and Kubernetes connector failures

Use the [Cytool diagnostic exercise](COMMAND-LINE-LAB.md) to collect local evidence before and after the fault.

**Blueprint coverage:** 6.2. **Practice mode:** Break and repair in the lab.

**Read first:** [Enable access to required PANW resources](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/activate-cortex-cloud/enable-access-to-required-panw-resources); [Onboard the Kubernetes Connector](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/onboard-the-kubernetes-connector); [Create an agent installation package](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/create-an-agent-installation-package); [Monitor agent operational status](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/manage-endpoint-protection/monitor-agent-operational-status).

1. Choose a single disposable VM or cluster connector with known working telemetry. Record last-seen time, operational state, version, and assigned policy.
2. Use a controlled lab connectivity interruption or a deliberately incorrect test installation setting. Keep the restoration command/configuration ready.
3. Check local process/pod status, installation output, generated configuration, DNS/TLS/egress, platform compatibility, and registration credentials in that order where applicable.
4. Compare endpoint/connector health with actual data arrival and scanner coverage. A running process is not sufficient evidence that Cortex can receive its telemetry.
5. Restore the original setting, produce a harmless new event, and verify current timestamps and expected policy enforcement.

**Verify and save:** A diagnosis and recovery record with a new event after restoration.

**Explain without notes:** How do you tell an unsupported host from a connectivity failure or an incorrect target policy?

## Objective 6.3 Diagnose outpost communication failures

**Blueprint coverage:** 6.3. **Practice mode:** Break and repair or evidence walkthrough.

**Read first:** [Outpost fundamentals and planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-fundamentals-and-planning); [Outpost troubleshooting](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-troubleshooting); [Troubleshoot errors on cloud instances](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/troubleshoot-errors-on-cloud-instances); [Create a standard outpost](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/working-with-standard-outposts/create-a-standard-outpost).

1. Begin with the outpost identity, selected region/account, current template version, and associated cloud instance.
2. Inspect the outpost’s open errors and the cloud instance’s individual capability statuses. Query cloud_health_auditing for Outpost events over the failure window.
3. Compare deployment/registration evidence with connectivity and IAM evidence. For a completed template with no registered outpost, inspect the outbound path used for registration.
4. Reproduce one documented fault on a disposable deployment, such as an acknowledged template prerequisite or a lab network error; do not randomly remove production permissions.
5. Apply the correction from the matching troubleshooting entry, verify Connected status, and execute a fresh scan to prove end-to-end recovery. If Outpost is unavailable, write a diagnosis against a supplied sandbox example and leave the live test pending.

**Verify and save:** An error timeline, identified root cause, and scan after recovery.

**Explain without notes:** Why is a healthy outpost VM different from a registered outpost with successful scans?

## Objective 6.4 Resolve OAuth, PAT, webhook, and CI integration failures

**Blueprint coverage:** 6.4. **Practice mode:** Break and repair.

**Read first:** [GitHub SaaS](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-version-control-systems/github-cloud); [Onboard the shared Cortex GitHub App](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-version-control-systems/github-cloud/onboard-a-cortex-github-app); [Jenkins for CI/CD pipeline scans](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-cicd-systems/jenkins-for-cicd-pipeline-scans); [Jenkins for code scans](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/integrate-ci-tools/jenkins-for-code-scans); [Connect GitLab container registry](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/gitlab/connect-gitlab-container-registry); [GitLab SaaS](https://cortex-docs.paloaltonetworks.com/application-security/application-security/onboard-data-sources/onboard-version-control-systems/gitlab-saas).

1. Identify the actual authentication mechanism before troubleshooting: GitHub SaaS currently uses GitHub Apps; GitLab SaaS uses its documented authorization workflow; GitLab registry uses a PAT; Jenkins integrations have their own credentials/configuration.
2. In a disposable token-based integration, use an expired/revoked test credential or missing scope, observe the failure, replace it with the documented scoped credential, and verify recovery.
3. For GitHub App integrations, check installation authorization and selected repository access. Do not try to repair installation-token authentication by supplying a PAT intended for a different connector.
4. For missing PR results, confirm the repository is selected, PR scanning is enabled, and webhook delivery reaches the expected integration. Inspect provider delivery details when available; compare timestamps with Cortex scan history.
5. For Jenkins, verify the selected integration type, installed plugin or pipeline configuration, runner network access, and secret names. Rerun a fresh build after repair.
6. Record a fresh commit/PR/build that succeeds after the fix. A Connected label without a new scan is incomplete verification.

**Verify and save:** A credential or repository-access repair plus a fresh PR/build result; webhook investigation worksheet.

**Explain without notes:** Which checks differ among a GitHub App installation, an OAuth integration, and a registry PAT?

## Objective 6.5 Diagnose AppSec scanner, mapping, and policy failures

**Blueprint coverage:** 6.5. **Practice mode:** Break and repair.

**Read first:** [Create an AppSec policy](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/unified-application-security-policies/tenant-ui-workflow/create-a-policy); [IaC Drift Detection scans](https://cortex-docs.paloaltonetworks.com/application-security/code-security/code-security-scanners/iac-drift-detection-scans); [Scan settings](https://cortex-docs.paloaltonetworks.com/application-security/settings/application-security-settings/scan-settings); [Code to Cloud troubleshooting](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/code-to-cloud/code-to-cloud-troubleshooting); [Global scan configurations](https://cortex-docs.paloaltonetworks.com/application-security/settings/application-security-settings/scan-settings/global-scan-configurations); [Custom scan configurations](https://cortex-docs.paloaltonetworks.com/application-security/settings/application-security-settings/scan-settings/custom-scan-configurations); [Cortex CLI Cortex Cloud Application Security command line reference](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cli/cortex-cli-for-code-security/cortex-cli-cortex-cloud-application-security-command-line-reference).

1. Use a fixture that produced a finding earlier. Deliberately exclude its path or disable its scanner in only the lab repository’s custom configuration.
2. Run another scan and compare scanner selection, branch, commit, exclusions, and scan health with the working baseline. Restore the setting and verify the finding returns.
3. Next, keep the finding but exclude the repository from the lab policy’s scope. Compare raw finding visibility with issue creation or blocking behavior.
4. Inspect finding type, conditions, supported trigger, action, exception, and policy scope when the expected enforcement is missing.
5. For missing lineage or drift, inspect cloud/repository integrations, YOR mapping signals, and pipeline execution. Restore the missing link and confirm the expected Code → Build → Deploy → Run relationship.
6. Save a diagnosis that separates no scan, no finding, no issue, and no blocking action.

**Verify and save:** Two deliberate misconfigurations repaired with before/after scan and policy evidence.

**Explain without notes:** Why can a scanner report a finding while a PR still passes?

## Objective 6.6 Diagnose user and API access problems

**Blueprint coverage:** 6.6. **Practice mode:** Break and repair.

**Read first:** [Set up users, groups, and roles](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/set-up-users-and-roles); [Manage API keys](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/manage-api-keys); [Asset groups](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cloud-inventory-and-environment/asset-groups); [Manage user scope](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/post-deployment-steps/manage-user-roles-and-access-management/manage-user-scope).

1. Use the restricted lab identity from 1.4 and choose an asset/action it should access.
2. Check authentication and tenant selection first, then component RBAC, asset/endpoint/case scope, and any dataset-specific access relevant to the operation.
3. Compare with the administrator’s view to distinguish absent data from hidden data. Verify the dynamic group uses fields eligible for access management.
4. For an API failure, check key validity, security level, role, scope, and the permission required by the exact endpoint. Apply only the missing access, then repeat the read operation.
5. Retest an out-of-scope asset to prove that the correction did not broaden access beyond the intended lab boundary.

**Verify and save:** A least-privilege repair with a positive test and a still-denied negative test.

**Explain without notes:** How can a user have permission to open a module but see no relevant assets?

## Objective 6.7 Diagnose an unexpected AWS cost increase

**Blueprint coverage:** 6.7. **Practice mode:** Investigate actual or supplied billing evidence.

**Read first:** [How to onboard Amazon Web Services](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/how-to-onboard-amazon-web-services); [Cortex Cloud and AWS audit log collection architecture](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/amazon-web-services-cloud-onboarding/cortex-cloud-and-aws-audit-log-collection-architecture); [Outpost fundamentals and planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-fundamentals-and-planning); [Configure registry scanning for cloud accounts](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/registry-scanning/configure-registry-scanning-for-cloud-accounts); [AWS Cost Explorer filtering](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-filtering.html); [AWS Cost Explorer data freshness and daily costs](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-exploring-data.html).

1. Compare a baseline interval with the cost-rise interval in Cost Explorer. Group by service and filter the affected account/region, then examine usage types.
2. Correlate the first increase with onboarding, scan scope/cadence changes, new registry images, CloudTrail data events, or an Outpost deployment. Treat these as hypotheses until usage supports them.
3. Inventory the actual scanning/logging resources and compare them with the generated templates and selected capabilities. Check for redundant log paths and retained lab resources.
4. Make one scoped correction, record the intended coverage impact, and inspect subsequent usage and security coverage. Allow for billing-data delay.
5. Write a short explanation naming the service, resource or usage driver, configuration trigger, correction, and remaining uncertainty. Use existing data or a provided sample; do not intentionally generate a large bill.

**Verify and save:** A cost investigation backed by usage evidence and a measured correction.

**Explain without notes:** How would you prove that a scanning change caused the increase rather than ordinary workload growth?

