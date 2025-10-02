---
title: Becoming a Verifier
sidebar_position: 2
---

# Guide to becoming a verifier

Becoming a verifier is an integral aspect of digital trust ecosystems, enabling services to leverage digital credentials issued by trusted entities and held by individuals or organizations. By implementing verification capabilities, services can enhance security, streamline processes and improve user experiences while maintaining privacy and control for credential holders. The following steps provide a guide to becoming a verifier, but remember that this is not a one-size-fits-all approach. You may need to adapt these steps to your specific needs and the process is often iterative rather than strictly linear.

## 1. Identify your verification use case

This involves analyzing your current processes, understanding your specific needs and identifying where digital credential verification can add the most value. 

**Things to consider:**
-   Review existing processes that could benefit from digital credential verification
-   Identify pain points in current identity or attribute verification methods  
-   Take a step back and consider your ecosystem, understanding your needs and how digital credentials fit within it
-   Evaluate which existing credentials would be most valuable to verify within your use case
-   Consider whether your use case requires existing credentials or if you need to work with a potential issuer to create new ones

**Resources:**
-   [Ideation Workshop](https://bcgov.github.io/digital-trust-toolkit/docs/delivery-manual/align/ideation_workshop): A structured approach to help you brainstorm and refine your verification use case.
-   [Examples of digital credentials](https://bcgov.github.io/digital-trust-toolkit/docs/foundations/credentials): Real-world scenarios demonstrating successful implementation of digital credential verification.
-   [Ecosystem builder](https://bcgov.github.io/digital-trust-toolkit/docs/delivery-manual/align/ecosystem_builder): Build an ecosystem map to visualize and understand how key actors, credentials and experiences in your use case fit within a digital trust ecosystem.

## 2. Select your experience pattern

Experience patterns define how users will interact with your verification system. Choosing the right pattern based on user needs and value add ensures a smooth integration of verification into your service.

**Things to consider:**
-   Understand common experience patterns and their use cases
-   Align the chosen pattern with your service's requirements and user needs    
-   Review the governance framework associated with your chosen solution        

**Resources:**
-   [Experience pattern library](https://bcgov.github.io/digital-trust-toolkit/docs/experience-patterns/): A comprehensive guide to different verification experience patterns and their applications.
-   [Overview of common digital trust experiences](https://bcgov.github.io/digital-trust-toolkit/docs/foundations/experiences): Explore typical user interactions and workflows in digital credential ecosystems.

## 3. Define your credential scheme and presentation requests

Schemas and presentation requests determine what data you'll verify and how. This step is crucial for ensuring you collect only necessary information while preserving user privacy.

**Things to consider:**
-   Determine whether your use case will rely on existing credentials or require new ones
-   Align with existing credential schemas where possible
-   Implement privacy-preserving techniques such as selective disclosure, zero-knowledge proofs, and predicates
-   Ensure your requests align with issuer governance frameworks
-   Request only information that is strictly necessary for your service        

**Resources:**
-   [AnonCreds Documentation](https://www.hyperledger.org/projects/anoncreds): Comprehensive guide to working with privacy-preserving credentials.
-   [Presentation request explorer](https://vc-authn-oidc-dev.apps.silver.devops.gov.bc.ca/ver_configs/explorer): review existing presentation request and best practices for privacy-respecting presentation requests.

## 4. Review relevant governance frameworks

Governance frameworks provide the rules and standards for digital credential ecosystems. Aligning with these frameworks ensures your verification process is compliant and interoperable.

**Things to consider:**
-   Identify applicable regulations (e.g., privacy laws, industry standards)    
-   Review existing governance frameworks for digital credentials in your domain
-   Consider how governance requirements might impact your verification process 

**Resources:**
-   [Governance](https://bcgov.github.io/digital-trust-toolkit/docs/governance/): A comprehensive resource for verifiable credentials governance documentation.
-   [UX and Governance Workshop](https://bcgov.github.io/digital-trust-toolkit/docs/delivery-manual/discover/ux_and_governance): a session to contextualize how your current governance fits in adopting digital trust.
-   [Pan-Canadian Intergovernmental Collaboration on Digital Trust](https://iccs-isac.github.io/Gouvernance-CICN-ICDT-Governance/): (under development)        

## 5. Map Service and User Journeys

A clear end-to-end service and user journey is essential for a seamless verification experience. This step involves visualizing how verification will fit into your users' interactions with your service.

**Things to consider:**
-   Analyze your current user journey and identify where verification fits      
-   Consider the impact on user experience when transitioning to digital credentials
-   Evaluate how verified data can streamline or eliminate existing steps in your digital service
-   Plan for user education and support during the transition
-   Consider multi-channel approaches (mobile, desktop, phone, in-person, paper, etc.)
-   Be aware that BC Wallet and credentials for individuals are currently only available via smartphone
-   Note that services relying solely on digital credentials may impose accessibility constraints

**Resources:**
-   [Service design methods and tools from the Government of British Columbia](https://www2.gov.bc.ca/gov/content/governments/services-for-government/service-experience-digital-delivery/service-content-design/methods-and-tools/document-and-visualize): guidance on how to map and visualize for digital government services - including user journeys.
-   [UX and Governance Workshop](https://bcgov.github.io/digital-trust-toolkit/docs/delivery-manual/discover/ux_and_governance): examine your current UX and governance and how they align with digital trust experience(s) being introduced.   
-   [Sequence Diagram Workshop](https://bcgov.github.io/digital-trust-toolkit/docs/delivery-manual/discover/sequence_diagram): template for mapping how credentials are managed, shared and verified in your digital trust use case.

## 6. Choose your tech stack

The technology you choose will form the foundation of your verification capabilities. This decision impacts everything from implementation ease to long-term maintenance.

**Things to consider:**
-   Evaluate different agent and wallet technologies available
-   Consider integration requirements with your existing systems
-   Assess scalability and performance needs
-   Review security and compliance requirements
-   Consider long-term maintenance and support

**Resources:**
-   [Technology overview](https://bcgov.github.io/digital-trust-toolkit/docs/foundations/technology): Comprehensive guide to digital trust technologies and architectures.
-   [ACAPy Integration How-to](https://bcgov.github.io/digital-trust-toolkit/docs/acapy-integration-howto): Step-by-step guide for integrating with Aries Cloud Agent Python (ACAPy).

## 7. Implement and test your verification system

Implementation involves building your verification capabilities and thoroughly testing them to ensure they work as expected.

**Things to consider:**
-   Start with a minimal viable implementation
-   Test thoroughly with real credentials and scenarios
-   Implement proper error handling and user feedback
-   Consider edge cases and failure scenarios
-   Plan for gradual rollout and user adoption

**Resources:**
-   [Traction tenant setup](https://bcgov.github.io/digital-trust-toolkit/docs/solutions/traction-overview): Guide to setting up a tenant in the Traction platform for testing and development.

## 8. Deploy and monitor your verification system

Once implemented and tested, deploy your verification system and establish monitoring to ensure it continues to work effectively.

**Things to consider:**
-   Plan for gradual deployment and user migration
-   Implement comprehensive monitoring and logging
-   Establish support processes for users and stakeholders
-   Monitor performance and user adoption metrics
-   Plan for ongoing maintenance and updates

**Resources:**
-   [Support model documentation](https://bcgov.github.io/digital-trust-toolkit/docs/delivery-manual/trial/Support%20model): Guidelines for establishing support processes for your digital trust implementation.

## Next steps

Once you've completed these steps, you'll have a solid foundation for becoming a verifier in the digital trust ecosystem. Remember that this is an iterative process, and you may need to revisit these steps as your use case evolves or as new technologies and governance frameworks become available.

For additional support and guidance, consider reaching out to the BC Government's Digital Trust team or participating in the digital trust community forums.
