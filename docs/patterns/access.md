# Access

In the access pattern, a system will require users to prove that they can access its functionalities by presenting information contained in one or more verifiable credentials. Depending on the needs of each integration, there are two ways to enable Digital Trust Access in your application:

- OIDC based access
- Direct access

## OIDC Based Access

OIDC based access is the simplest way to add Digital Trust verification capabilities to an application. It leverages [VC-AuthN OIDC](../solutions/vc-authn-sso.md) as Identity Provider and is fully integrated with the [Pathfinder SSO](https://developer.gov.bc.ca/docs/default/component/css-docs) service. It relies on the OpenID Connect authentication protocol and can generally be introduced with minor changes to your application if it already uses another OIDC identity provider to gate access (e.g.: IDIR, GitHub).

Please refer to the [VC-AuthN OIDC](../solutions/vc-authn-sso.md) page for additional details.

## Direct Access

For more advanced interaction, a direct access pattern may be considered: this will provide the application with full control over the interaction the same way as if it was a [verifier](verifier.md).

Direct access, however, requires a significantly higher amount of work when compared to OIDC based access since the application team will be responsible for directly integrating with [Traction's](../solutions/traction-overview.md) APIs to create and process proof-requests as well as developing a custom authentication framework.
