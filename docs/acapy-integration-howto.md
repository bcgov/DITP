# Integration How-To

Implementing a custom integration with an ACA-Py/Traction agent is fairly straightforward: the agent exposes a set of REST APIs that cover all of the Digital trust functionality that may be implemented. There are, however, some concepts that need to be considered when making requests to these endpoints. This page outlines some of the most important concepts and "gotchas" that need to be considered.

## Authentication

When requesting a new Traction tenant, you will be provided with a set of credentials that should be used to authenticate with the service (via Tenant UI and/or API endpoints). At the time of writing, the system will provide a `wallet_id` and `wallet_key` automatically upon checking-in to the system after a reservation is approved. These credentials are like a username/password combination and should be stored and protected appropriately. Losing `wallet_id` and `wallet_key` means that nobody, even the Traction administrator, will be able to recover access to your tenant. For this reason in the near future we will be switching to using exclusively `tenant_id` and `api_key` as authentication mechanism.

### Tenant ID and Api Keys

Similarly to `wallet_id` and `wallet_key`, `tenant_id` and `api_key` can be used to authenticate with a Traction tenant. While the value for `tenant_id` will always be the same (like a username), a tenant can independently create and delete as many API keys keys as desired. API keys can be used to provide different members of the development team with their own credentials to authenticate against a tenant, and are the preferred method to provide external applications with access to the tenant. When an API key is deleted, it ceases to function immediately and it cannot be recovered.

API Keys can be managed from the section with the same name in the Tenant UI, accessible by clicking the account image in the top-right corner.

### Obtaining an access token

To authenticate using tenant ID and API key, execute a `POST` request to the `/multitenancy/tenant/{tenant_id}/token` endpoint. This will return a JWT that should be added in the `Authorization` header as `Bearer <jwt-that-was-obtained>` to make requests as that tenant.

!!! warning "Token Lifecycle"
    Once a valid token is issued, there is no need to re-authenticate for the subsequent requests until the token expires. Expiry is configured by the system administrator and its validity is currently set to 24 hours. Consuming applications should *NOT* request a new token before every PI request, as this would generate a significant amount of overhead in the system. Issued tokens should be stored in the application's execution context and their expiry should be checked before submitting a request to ACA-Py/Traction: if the token is expired (or very close to being expired) a new token should be requested using Tenant ID and api-key.

## Webhooks

Webhooks are a fundamental tool to orchestrate asynchronous calls and sequences of requests to ACA-Py. Each tenant can specify one (or more) URLs that the agent will deliver webhooks to by accessing the *Settings* section in the tenant UI.

The webhook URL must be a URL able to receive `POST` requests. A path parameter will be used by ACA-Py to specify the type of action (topic) the webhook refers to, and the body of the webhook will contain the related data.

!!! info "Example"
    If the tenant is configured to deliver webhooks to `https://my-application.example/webhooks`, a connection event will post a webhook to `https://my-application.example/webhooks/connections`.

To secure the webhook endpoint, it is possible to specify a webhook key: when one is set, its value will be included in an `x-api-key` header so that the receiving application can check for it and authorize or deny the request. It is best practice to always specify an api-key to be used to protect webhook delivery and prevent unauthorized access to your service.

## Persisting Transaction Data

Most ACA-Py operations will trigger a webhook and while not all of them require handling, there are several scenarios where correct handling of webhooks is required to receive and store information that will be required in future interactions.

### Connections

When establishing a connection with another agent (mobile or not, it is indifferent), webhooks will allow your application to follow through the protocol responsible for creating the connection and, most importantly, will provide your application with the `connection_id`: this should be stored alongside the information related to the contact it belongs to, so that future interactions (sending messages, issuing/revoking credentials, requesting proofs) can be completed without having to re-establish a new contact.

### Issuing Credentials

When issuing credentials, webhooks will be delivered to inform the application of the current state of the issue-credential protocol. In particular, when the protocol is completed successfully two pieces of information will be produced: `revocation_id` and `revoc_reg_id` identify the specific issuance interaction and, if applicable, will be required when revoking the credential. As such, these data points should be stored by the application so that they can be retrieved and used if/when  necessary.

### Other Credential Exchanges

When completing credential exchange interactions (e.g.: requesting a proof), ACA-Py will create a credential exchange record that will be available only until the exchange is completed, after which it will be automatically purged. If necessary, the information about the exchange should therefore be persisted by the application.

## Extra ACA-Py Settings

The *Settings* page also includes extra ACA-Py settings that can be modified independently by each tenant. As an example, it is possible to increase the tenant's log level when troubleshooting. It is however recommended that these settings are left with their default value.
