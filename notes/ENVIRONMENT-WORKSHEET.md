# Sandbox and integration worksheet

Updated from your November 9, 2026 answers. Complete remaining fields in week 1. Use placeholders for credentials, not real values.

| Item | Your value | Evidence or documentation |
| --- | --- | --- |
| Cortex tenant and region | Cortex XSIAM; region not supplied | User report |
| Product release and enabled modules | Full XDR capabilities and enabled modules reported; record exact versions/module names | User report; inspect tenant |
| Base license, add-ons, and capacity | | |
| Test user, role, scope and permitted actions | Tenant-admin access reported; create scoped test identity for access labs | User report |
| AWS sandbox account and permitted regions | AWS is primary lab platform; record account and regions | User preference |
| AWS Organization or OU access available | Not yet specifically confirmed; required for live organization exercise | Record actual scope before deployment |
| Existing CloudTrail and log destination | | |
| Cloud Scan or Outpost and reason | | |
| Disposable VM, registry/image and function | | |
| Kubernetes cluster and runtime compatibility | | |
| Fargate deployment availability | | |
| Repository/VCS organization and owner access | | |
| Jenkins and runner availability | | |
| Third-party registry access | | |
| Microsoft 365, Databricks and AI service access | | |
| Azure, GCP and OCI sandbox availability | Study all; live environments may be stood up later | User preference; no availability assumed |
| API Gateway, Azure APIM and Apigee availability | | |
| Broker VM deployment capacity | | |
| Agreed lab spending limit and cleanup date | | |

For every unavailable integration, create a configuration worksheet containing: required role/scope; credential type; IDs, URLs and regions; network path; template or installer; feature-specific options; verification evidence; and recovery checks. Use the exact linked provider procedure in the implementation guide.

Primary schedule: [six-week plan](../STUDY-PLAN.md). Cross-platform procedures: [platform map](PLATFORM-MAP.md). XSIAM/XDR access is recorded as reported; confirm the actual availability of each AppSec, posture, DSPM and runtime lab in the tenant rather than treating an unspecified module list as tested capability.
