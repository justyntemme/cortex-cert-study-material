# Lesson 30: K4 Connect trusted images to admission

Week 4 · Lesson 30 of 45 · Objective/exercise K4

[Course start](../README.md) · [Previous lesson](29-k3-k3-separate-inventory-and-runtime-coverage.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

## Learn

| Concept | Explanation | Official reference |
| --- | --- | --- |
| K1a Cluster and execution | A cluster has a control plane and worker nodes. Identify which component manages cluster state and which node runs a workload. | [Kubernetes components](https://kubernetes.io/docs/concepts/overview/components/) |
| K1b Context | A kubeconfig context combines a cluster, user and namespace. The selected context determines the target of ordinary kubectl commands. | [Kubeconfig contexts](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) |
| K1c Controllers | A Deployment manages application Pods through declarative updates; a DaemonSet maintains a Pod on all or selected nodes. | [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/); [DaemonSets](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) |
| K2a Authorization | RoleBindings grant permissions within a namespace; ClusterRoleBindings grant across the cluster. A RoleBinding can reference a ClusterRole while retaining namespace scope. | [Kubernetes RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) |
| K2b Connector | Cortex generates an installer from the capabilities chosen in its Kubernetes wizard. Execute it in the target cluster to complete deployment. | [Cortex Kubernetes connector procedure](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/onboard-the-kubernetes-connector) |
| K3 Runtime selection | The documented Realtime Protection option deploys agents as a DaemonSet; node selectors restrict eligible nodes. That wizard option is not supported for Fargate. | [Cortex Kubernetes connector procedure](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/onboard-the-kubernetes-connector) |
| K4a Admission | Admission handles API requests after authentication/authorization and before persistence. It is a different stage from scanning an already-running workload. | [Admission controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) |
| K4b Trust action | Trusted-image prevention requires admission enabled on the policy's cluster scope. Already-running untrusted images receive posture issues; test prevention with a new deployment. | [Trusted image actions and prerequisites](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/types-of-cloud-workload-policies/types-of-cloud-workload-policies) |

**Lab choice:** Use an existing disposable, supported cluster with Linux worker nodes and known workloads. Check the actual connector/agent compatibility documentation before choosing a platform. For a Docker-only local cluster, do not assume vendor support merely because Kubernetes commands work. See [Cortex Kubernetes connector procedure](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/onboard-the-kubernetes-connector) and [Create an agent installation package](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/set-up-endpoint-protection/create-an-agent-installation-package).

## Practice

1. **K4a/K4b:** First read the trusted-image policy actions, scope and admission prerequisite. Record why an issue-only action would not satisfy a request to stop a new deployment. [Trusted image actions and prerequisites](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/types-of-cloud-workload-policies/types-of-cloud-workload-policies); [Admission controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/).
2. **K4b:** Enable the documented admission option on the disposable cluster, then implement the lab-scoped trusted-image policy from objective 3.4. Use harmless images with known trust results; no exploit is required. [Cortex Kubernetes connector procedure](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/onboard-the-kubernetes-connector); [Trusted image actions and prerequisites](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/types-of-cloud-workload-policies/types-of-cloud-workload-policies).
3. **K4a/K4b:** Submit a new allowed workload and a new workload that violates the criterion using your reviewed lab manifest. Save the actual admission response and Cortex issue evidence. Compare an already-running workload separately. [Trusted image actions and prerequisites](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/types-of-cloud-workload-policies/types-of-cloud-workload-policies); [Admission controllers](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/); [kubectl quick reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/).
4. **K4b:** Restore the saved policy configuration and remove only your test workload using its recorded manifest/resource identity. Repeat a permitted deployment to verify the restored state. Procedure references: [Trusted image actions and prerequisites](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/rules-and-policies/cloud-workload-policies-and-rules/cloud-workload-policies/types-of-cloud-workload-policies/types-of-cloud-workload-policies); [kubectl quick reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/). The before/after record is our lab method.

**Verify:** explain why registry scan findings, trust rules, admission decisions and runtime observations answer different questions. Use L5–L6 and A4 in [the application/analysis set](../APPLICATION-ANALYSIS.md), then retest during weeks 5–6.

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [31. Manage vulnerability issue and prevention policies](31-3-5-manage-vulnerability-issue-and-prevention-policies.md)**
