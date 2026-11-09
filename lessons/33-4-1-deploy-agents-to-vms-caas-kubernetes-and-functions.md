# Lesson 33: Deploy agents to VMs, CaaS, Kubernetes, and functions

Week 5 · Lesson 33 of 45 · Objective/exercise 4.1

[Course start](../README.md) · [Previous lesson](32-3-6-build-compliance-standards-controls-assessments-and-reports.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

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

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [34. Configure endpoint groups, prevention, extensions, and exceptions](34-4-2-configure-endpoint-groups-prevention-extensions-and-exceptions.md)**
