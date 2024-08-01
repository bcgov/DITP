# Traction

## What is Traction

[Traction](https://github.com/bcgov/traction) is an application built on top of [Aries Cloudagent Python](https://github.com/hyperledger/aries-cloudagent-python) to facilitate the provisioning and management of tenant agents. With Traction, the DITP team does not need to prepare and deploy new agent instances for each adopter: users submit a request for a tenant and are able to self check-in and manage their settings when approved.

## Tenants

A tenant is a "resident" of Traction: similar to occupants of a condominium, different entities/organizations access the same resources, but remain isolated and independent.

There are several instances of Traction that can be used for different purposes:

- [Sandbox](https://traction-sandbox-tenant-ui.apps.silver.devops.gov.bc.ca): this instance is completely self-serve and can be used for prototyping and discovery of short-lived projects. The sandbox is reset automatically, on the 1st and 15th day of the month.
- [Development](https://traction-tenant-ui-dev.apps.silver.devops.gov.bc.ca): this instance would be the first step after prototyping in the `sandbox` and requires a request to be created in-app and reviewed by the DITP team.
- [Test](https://traction-tenant-ui.apps.silver.devops.gov.bc.ca) and [Production](https://traction-tenant-ui.apps.silver.devops.gov.bc.ca) access can be requested the same way as for `development`, once the integration is ready to move further.

A Traction tenant provides full access to an Aries agent connected to pre-approved [ledgers](#ledgers), however the functionality to become `issuers` is not enabled by default: a request outlining the business case/requirement to become an issuer should be submitted to DITP when the tenant request is initially created, or any time after that when integrating with credential issuance processes becomes necessary.

More information about becoming an issuer can be found [here](traction-becoming-an-issuer.md).

## Ledgers

Traction is connected to several ledgers in read mode, which allows teh tenant to receive, present and verify credentials from issuers rooted on those ledgers - if necessary. In general, the `development` ledger can also read from `test` and `production` ledgers and the `test` environment can also read from `production`. The `production` environment is limited to production ledgers for security reasons.

Each environment can also connects in write mode - for tenants who become issuers - to ledgers that are of the same level.

!!! info "Info"
Please note that an issuer can only ever connect to ONE ledger in write mode and that "moving" to another ledger is generally not recommended or supported at this time.

### Sandbox

- [BCovrin Test](http://test.bcovrin.vonx.io)

### Development

- [CANdy Dev](https://candyscan.idlab.org/txs/CANDY_DEV/domain)
- [BCovrin Test](http://test.bcovrin.vonx.io)

### Test

- [CANdy Test](https://candyscan.idlab.org/txs/CANDY_TEST/domain)
- [BCovrin Test](http://test.bcovrin.vonx.io)
- [Sovrin TestNet](https://indyscan.io/txs/SOVRIN_STAGINGNET/domain) (only used in special circumstances, generally for legacy issuers)

### Production

- [CANdy Prod](https://candyscan.idlab.org/txs/CANDY_PROD/domain)
- [Sovrin MainNet](https://indyscan.io/txs/SOVRIN_MAINNET/domain) (only used in special circumstances, generally for legacy issuers)
