# Lesson 10: Deploy and configure Broker VM

Week 2 · Lesson 10 of 45 · Objective/exercise 2.6

[Course start](../README.md) · [Previous lesson](09-2-1-onboard-cloud-providers-and-security-capabilities.md)

Follow this lesson in sequence; use the source links where a procedure or explanation calls for them. Save your checkpoint if you stop mid-lab. Current procedures require the [exam-era comparison](../notes/EXAM-VERSION-BASELINE.md) before being treated as June/July 2026 behavior.

**Blueprint coverage:** 2.6. **Practice mode:** Implement or supervised sandbox lab.

**Read first:** [Set up Broker VM on Amazon Web Services](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/data-management/broker-vm/set-up-and-configure-broker-vm/broker-vm-image-installations/set-up-broker-vm-on-amazon-web-services); [Set up and configure Broker VM](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/data-management/broker-vm/set-up-and-configure-broker-vm).

1. Read the Broker VM compatibility, sizing, network, and registration requirements. Choose an available supported deployment target and record why this lab needs a Broker.
2. For AWS, download the authorized Broker image, configure the documented VM import role, upload/import the image, and create the AMI using the AWS deployment procedure. Use the exact current import commands and AMI settings from that page.
3. Launch the Broker with the documented resources and network access; complete its initial configuration and registration with Cortex.
4. Activate only the collector applet needed for your selected test source, then send a small test record and verify collector health and received data.
5. Capture the image/instance identity, registration result, applet configuration, and cleanup plan. Explain the separate purposes of Broker VM and Outpost.

**Verify and save:** A registered Broker and a functioning test collector, or a fully specified deployment worksheet if sandbox access prevents deployment.

**Explain without notes:** Which component would you inspect for a collector failure versus a workload scanning failure?

## Before moving on

Record the procedure you performed, observed result, supporting source and any unresolved point in [your evidence](../evidence/TEMPLATE.md). Answer one application question about this feature and one analysis question connecting it to an earlier lesson. Use documented behavior to justify your answer. A missing environment stays an explicit walkthrough; an unfinished live lab stays unfinished.

**Next lesson → [11. Deploy the Kubernetes connector](11-3-7-deploy-the-kubernetes-connector.md)**
