# Endorser Service

An Endorser Service is responsible for authorizing write transactions to each one of the ledgers supported by BCGov. An overview of the ledgers available in read/write mode can be found [here](traction-overview.md#ledgers).

When a write operation such as publishing a new schema definition to the ledger is required, tenant administrators will need to request authorization to the Digital trust team. Each request for endorsement will be reviewed and, if the governance terms are respected, will be approved.

!!! info "Note"
    Endorsement requests in the `dev` environment will be automatically approved in order to facilitate rapid prototyping and development of new solutions. `test` an `prod`, however, will require a DITP member to review the request and approve it before the transaction can be written and completed.

!!! warning "Endorsement is Asynchronous!"
    Endorsement requests are asynchronous and may take several hours or even days  to complete, especially when review by a DITP team member is required. Ensure your code does not expect an immediate endorsement request, especially when requesting new schemas or credential definitions to be published.
