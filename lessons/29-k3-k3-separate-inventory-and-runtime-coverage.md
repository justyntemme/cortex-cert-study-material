# Lesson 29: K3 Separate inventory and runtime coverage

Week 4 · Lesson 29 of 45 · Objective/exercise K3

[Course start](../README.md) · [Previous lesson](28-3-4-create-workload-rules-and-policies.md)

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

1. **K3/K1c:** Inspect the selected runtime capability and any node selector. Compare eligible node labels with the agent DaemonSet's desired/current/ready state. Use observed names and namespaces. [Cortex Kubernetes connector procedure](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/onboard-the-kubernetes-connector); [DaemonSets](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/); [kubectl quick reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/).
2. **K3:** Compare two evidence records: discovered Kubernetes inventory and runtime protection status. Investigate mismatches using node eligibility and component health; the comparison is our lab hypothesis test. [Cortex Kubernetes connector procedure](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/onboard-the-kubernetes-connector); [Monitor agent operational status](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/install-and-manage-endpoints/manage-endpoint-protection/monitor-agent-operational-status).
3. **K1c:** For a non-ready lab Pod, collect `kubectl describe pod POD_NAME -n NAMESPACE` and `kubectl logs POD_NAME -n NAMESPACE` using actual identifiers. Explain the observed event or log before changing configuration. [kubectl quick reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/).

**Verify:** produce a node-to-agent coverage table and explain any gaps. For Fargate, read the separate workload deployment procedure in objective 4.1; do not apply this wizard's unsupported runtime option. [Cortex Kubernetes connector procedure](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/onboard-the-kubernetes-connector); [CaaS Workloads](https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/endpoint-security/endpoint-protection/caas-workloads).

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [30. K4 Connect trusted images to admission](30-k4-k4-connect-trusted-images-to-admission.md)**
