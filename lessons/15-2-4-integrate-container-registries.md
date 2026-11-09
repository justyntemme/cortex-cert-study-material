# Lesson 15: Integrate container registries

Week 2 · Lesson 15 of 45 · Objective/exercise 2.4

[Course start](../README.md) · [Previous lesson](14-2-3-integrate-github-and-jenkins.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 2.4. **Practice mode:** Implement one and compare all named examples.

**Read first:** [Configure registry scanning for cloud accounts](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/registry-scanning/configure-registry-scanning-for-cloud-accounts); [Configure registry scanning for third party integrations](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/registry-scanning/configure-registry-scanning-for-third-party-integrations); [Connect Docker Hub registry](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/docker/connect-docker-hub-registry); [Connect GitLab container registry](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/gitlab/connect-gitlab-container-registry); [Connect JFrog container registry](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cortex-cloud-data-sources-and-connectors/vendor-specific-data-sources/jfrog/connect-jfrog-container-registry).

1. Enable AWS ECR registry scanning in your AWS integration, choose an initial scan scope, and push a harmless lab image. Confirm the image identity and resulting scan details.
2. Add a separate third-party registry through Data Sources & Integrations → Add New → Container Registries. Select Docker Hub, GitLab, or JFrog according to your access.
3. Follow that connector’s credential, URL, network, and repository-selection requirements. Save the configuration and verify the intended registry repositories are visible.
4. For the other two named registry examples, prepare the exact input and permission worksheet from their individual documentation rather than assuming credentials are interchangeable.
5. Compare an in-scope image with an excluded image; explain which connector and scope control each result.

**Verify and save:** One cloud-registry scan, one third-party scan when available, and Docker/GitLab/JFrog configuration comparison sheets.

**Explain without notes:** How is third-party registry integration different from enabling a capability on an onboarded AWS account?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [16. Ingest third-party SAST and SCA results](16-2-5-ingest-third-party-sast-and-sca-results.md)**
