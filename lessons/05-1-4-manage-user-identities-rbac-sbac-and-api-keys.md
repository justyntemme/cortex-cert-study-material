# Lesson 5: Manage user identities, RBAC, SBAC, and API keys

Week 1 · Lesson 5 of 45 · Objective/exercise 1.4

[Course start](../README.md) · [Previous lesson](04-k1-k1-inspect-before-installing.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 1.4. **Practice mode:** Implement.

**Read first:** [Set up users, groups, and roles](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/set-up-users-and-roles); [Manage API keys](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/manage-api-keys); [Asset groups](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cloud-inventory-and-environment/asset-groups); [Manage user scope](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/post-deployment-steps/manage-user-roles-and-access-management/manage-user-scope).

1. In Settings → Configurations → Access Management, inspect a built-in role and create a restricted custom role for the lab. Record permitted actions separately from the assets the user may see.
2. Create a dynamic asset group using attributes supported for access management. Assign a lab test identity the custom role and an appropriate scope; keep an administrator session available.
3. With the test identity, compare an allowed asset with an out-of-scope asset and an allowed action with a disallowed action. Check both role and scope when results differ.
4. Create an API key with a suitable restricted role, scope, and expiration. Make a documented read operation, then revoke the key and verify authentication fails. Store only the key ID and results in your notes.
5. Explain the user lifecycle: identity source, group membership, role assignment, scope, key issuance, role changes, and revocation. Inspect your tenant authentication configuration without replacing its working identity provider.

**Verify and save:** An access matrix with positive and negative checks, plus an API-key lifecycle record.

**Explain without notes:** Does granting a role automatically grant visibility to every asset? Why can a static asset group be unsuitable for SBAC?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [6. CLI A Discover and explain arguments](06-cli-a-cli-a-discover-and-explain-arguments.md)**
