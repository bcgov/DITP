# Verifier

A verifier is a service that requests information via a proof-request to other users and/or systems, processes the response and triggers the next steps in the interaction based on the outcome.

A verifier can request and validate information from any issuer rooted on a [ledger](../solutions/traction-overview.md#ledgers) to which its agent has access.

The verification process generally consists of:

- Determining which credential or credentials would satisfy the proof-request.
- Invoking the appropriate endpoints in the agent to prepare the proof-request.
- Sending the proof request to the holder: this could happen over a previously established connection, or out-of-band.
- Receiving and processing the holder's response.
- Completing the interaction based on the outcome of the verification.

To become a verifier, you will first need to request a tenant in [Traction](../solutions/traction-overview.md).
