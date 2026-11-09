# Lesson 41: Diagnose user and API access problems

Week 6 · Lesson 41 of 45 · Objective/exercise 6.6

[Course start](../README.md) · [Previous lesson](40-6-2-diagnose-agent-and-kubernetes-connector-failures.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 6.6. **Practice mode:** Break and repair.

**Read first:** [Set up users, groups, and roles](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/set-up-users-and-roles); [Manage API keys](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/manage-api-keys); [Asset groups](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cloud-inventory-and-environment/asset-groups); [Manage user scope](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/post-deployment-steps/manage-user-roles-and-access-management/manage-user-scope).

1. Use the restricted lab identity from 1.4 and choose an asset/action it should access.
2. Check authentication and tenant selection first, then component RBAC, asset/endpoint/case scope, and any dataset-specific access relevant to the operation.
3. Compare with the administrator’s view to distinguish absent data from hidden data. Verify the dynamic group uses fields eligible for access management.
4. For an API failure, check key validity, security level, role, scope, and the permission required by the exact endpoint. Apply only the missing access, then repeat the read operation.
5. Retest an out-of-scope asset to prove that the correction did not broaden access beyond the intended lab boundary.

**Verify and save:** A least-privilege repair with a positive test and a still-denied negative test.

**Explain without notes:** How can a user have permission to open a module but see no relevant assets?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [42. Resolve OAuth, PAT, webhook, and CI integration failures](42-6-4-resolve-oauth-pat-webhook-and-ci-integration-failures.md)**
