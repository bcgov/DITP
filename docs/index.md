# Common Hosted Digital Credential Service

Technical and non-technical documentation for Digital Trust and Verifiable Credentials

## About the Common Hosted Digital Credential Service

The Common Hosted Digital Credential Service is part of the Cybersecurity and Digital Trust (CDT) team at the Province of British Columbia.

Our focus is building tools to enable Digital Trust and supporting partners/adopter in their journey to improve their business processes and implement new ones that leverage this technology.

## Patterns

There are three main patterns that can be leveraged in the Digital Trust space, follow the links to learn more:

- [Verifier](patterns/verifier.md): verifies and consumes credentials issued by a third-party authority.
- [Issuer](patterns/issuer.md): defines a new credential schema and is responsible for issuing and revoking credentials.
- [Access](patterns/access.md): similar to the verifier pattern, it's used to obtain authorization to resources on the web.

## Solutions

Depending on which pattern you are looking to implement, the following solutions will provide a foundation to get started:

- [VC-AuthN and SSO](solutions/vc-authn-sso.md): a solution that allows the use of Digital Credentials in an OIDC authentication flow. As an identity Provider service integrated with the [Pathfinder SSO Service](https://developer.gov.bc.ca/docs/default/component/css-docs) it provides a lightweight, standard approach to web application authentication that does not require deep knowledge of Digital trust patterns and tools.
- [Traction](solutions/traction-overview.md): a Software-As-A-Service Enterprise agent service based on [ACA-Py](https://github.com/openwallet-foundation/aries-cloudagent-python), it provides streamlined onboarding for new adopters wanting to have full control over their Digital Trust processes, from receiving and presenting Digital credentials to acting as a verifier or even an issuer.
- [OrgBook BC](solutions/orgbook-bc.md): a repository of credentials for publicly available information. It contains information about entities registered as businesses in BC (data from BC registries), as well as [other permit/license credentials from different organizations](https://orgbook.gov.bc.ca/about/orgbook-data).
