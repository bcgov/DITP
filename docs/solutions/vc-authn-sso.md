# VC-AuthN SSO

[VC-AuthN OIDC](https://github.com/bcgov/vc-authn-oidc) is an identity provider compatible with the OpenID Connect protocol, that uses Verifiable credentials as authentication method.

The service is composed of an agent ([ACA-Py](https://github.com/hyperledger/aries-cloudagent-python)) that is responsible for the secure communication and exchange nd credentials, and a controller that "drives" the agent to build authentication requests and translate them into the OIDC protocol.

## Getting Started

The easiest way to get started with verifiable credential authentication is to request access to the `Digital Credential` identity provider in the [Pathfinder SSO](https://developer.gov.bc.ca/docs/default/component/css-docs) service.

Once the identity provider is enabled, integration with your application is as simple as connecting it with a Keycloak client that can talk to the new IdP.

There are, however, a couple of things specific to VC-AuthN that your service will need to determine and keep in mind:

- You will need to choose a **presentation request configuration**: this is the setting that tells VC-AuthN which credentials you are requiring and want to obtain information from to allow access to your system. Once you have determined the `id` of the configuration you want to use, you will need to add a query parameter to your OIDC authentication request to indicate it to VC-AuthN: `pres_req_conf_id=my-chosen-config-id`.
  - Existing presentation configurations can be discovered [here](https://vc-authn-oidc-dev.apps.silver.devops.gov.bc.ca/ver_configs/explorer). If no existing configuration meets your application requirements, you can [contact us](../about-us.md) to explore options.
- Upon successful authentication, your application should check that the JWT includes a `pres_req_conf_id` attribute with the same value as the value that was provided to generate the authentication request. If this is not true, the authentication request could have been manually modified/hijacked.
- A successful authentication will return a JWT with attributes coming from the credentials stored in an object: `vc_presented_attributes`. Claims will be nested in this object and not presented at the top level.

## Limitations

VC-AuthN has a different approach when compared to "traditional" identity providers, and it does not store a user database. For this reason, and because there may be any combination of credentials in an authentication request, it is not possible for the IdP to provide a unique identifier to recognize returning users.

The consuming applications (clients) are therefore responsible for reconciling user access requests to the same user by using the attributes exposed as part of the proof-request or by other mechanism.
