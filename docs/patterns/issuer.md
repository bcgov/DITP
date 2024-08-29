# Issuer

An issuer is an entity with the authority to define, issue and revoke credentials.

Issuers create Digital Credentials that [verifiers](verifier.md) can then request and use, and often times they also are verifiers of the credentials they have issued.

To become an issuer, you will first need to request a tenant in [Traction](../solutions/traction-overview.md).

## Governance

Issuers should meet the requirements set by the Governance defined by the organization they belong to, the Digital Trust team as well as the ledger chosen as trust root (where the issuer will publish its public keys and other cryptographic identifiers).

An [endorser service](../solutions/endorser-service.md) is generally responsible for overseeing an issuer's request to publish new information to a ledger and approving/rejecting it.
