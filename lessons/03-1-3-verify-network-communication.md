# Lesson 3: Verify network communication

Week 1 · Lesson 3 of 45 · Objective/exercise 1.3

[Course start](../README.md) · [Previous lesson](02-1-2-choose-licenses-retention-scanning-and-iam.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 1.3. **Practice mode:** Implement.

**Read first:** [Enable access to required PANW resources](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/activate-cortex-cloud/enable-access-to-required-panw-resources); [Outpost fundamentals and planning](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/onboard-and-configure/deployment-steps-and-checklist/cloud-service-provider-csp-onboarding/outpost-onboarding/outpost-fundamentals-and-planning); [Set up and configure Broker VM](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/data-management/broker-vm/set-up-and-configure-broker-vm).

1. Find your tenant region and the exact current endpoint requirements for the components you intend to deploy. Create a matrix with source, destination FQDN, port, direction, and purpose.
2. Check DNS and HTTPS reachability from the actual lab VM, build runner, and outpost or Broker network, rather than only from your laptop. Use the documented regional endpoints.
3. Apply the required egress rules to the lab network. If a proxy or TLS inspection is present, compare its configuration with the component-specific documentation.
4. Record successful connectivity and one failed connection caused by a deliberately incorrect destination in a local test. Do not disrupt the shared tenant.

**Verify and save:** A region-specific connectivity matrix and evidence from each execution location.

**Explain without notes:** How would you distinguish a network failure from a successful network connection followed by a 403 response?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [4. K1 Inspect before installing](04-k1-k1-inspect-before-installing.md)**
