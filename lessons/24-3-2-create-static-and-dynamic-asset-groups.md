# Lesson 24: Create static and dynamic asset groups

Week 4 · Lesson 24 of 45 · Objective/exercise 3.2

[Course start](../README.md) · [Previous lesson](23-cli-c-cli-c-diagnose-and-repair.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 3.2. **Practice mode:** Implement.

**Read first:** [Asset groups](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/cloud-inventory-and-environment/asset-groups).

1. Open Inventory → Assets → Groups → Add Group. Create one static group containing explicitly selected lab assets.
2. Create a dynamic group using attributes present on those assets, such as provider and region. Preview which assets match before saving.
3. Introduce or modify a lab asset so that it enters or leaves the dynamic criteria; observe membership after inventory refresh. Compare the static group.
4. Create an additional dynamic group using only access-management-supported fields and use it in the access-control lab.
5. Apply an asset group to a lab policy and verify that excluded assets are not targeted.

**Verify and save:** Static and dynamic membership evidence, plus a tested policy scope.

**Explain without notes:** How does changing an asset attribute affect dynamic membership, and why are static groups not the SBAC choice?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [25. Create an XQL dashboard](25-3-1-create-an-xql-dashboard.md)**
