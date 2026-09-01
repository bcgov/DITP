# Municipal Services Digital Letter of Authorization (MSDiLOA) Credential Documentation

## 1. About this Document

This document describes the **Municipal Services Digital Letter of Authorization (MSDiLOA)** verifiable credential to help potential verifiers determine whether it is suitable for their needs. The intended audience includes policy analysts, privacy specialists, solution architects, developers, and data architects.

The MSDiLOA credential can be issued by any British Columbia municipality. The first municipality to govern and issue this credential is the **City of Vancouver**. The MSDiLOA represents a digital authorization for a person to consume municipal services on behalf of another person or on behalf of a business.

> **Note:** While the MSDiLOA has applicability across various interactions within the municipal context, its first use-case covers the issuance of authorization to apply for a Rental Property Business Licence for Short-term Rentals (STR). A property owner will be able to use the MSDiLOA to authorize a tenant interested in applying for a short-term rental, facilitating a digitally trusted submission of a STR business licence application form.

The initiative is designed to enhance municipal service delivery, increase governance, protect homeowners, and aim to establish a standard across municipalities in BC. This means that the MSDiLOA is designed to align with the digital verifiable credential ecosystem and can become a standard across BC municipalities, able to accommodate the distinct attributes needed by the ecosystem.

Acknowledgements: The development of this documentation follows the governance framework created by the [Trust over IP Foundation (ToIP)](https://trustoverip.org/), specifically the [Governance Metamodel Specification](https://trustoverip.org/permalink/ToIP-Governance-Metamodel-Specification-V1.0-2022-12-21.pdf) created by the [Governance Stack Working Group (GSWG)](https://wiki.trustoverip.org/display/HOME/Governance+Stack+Working+Group).

### 1.1 Version History

| Ver. | Date | Notes |
| :--: | :--: | :--: |
| <b>0.9</b> | 05-Jan-2026 | Draft Release |
| <b>0.9.2</b> | 05-Jun-2026 | Addressed BC review: attribute name casing normalized; added §3.6 Legal; `OCA_field` → `authorized_services_summary`; Source wording updated to reference the proof request; `authorized_services_json` specification defined. |
| <b>0.9.3</b> | 09-Jun-2026 | Addressed BC review (round 2): PID description aligned to the LTSA Property Owner credential (incl. `###-###-###` format); business-licence descriptions corrected "name" → "number"; JSON Schema added as Appendix C (draft v1). |
| <b>0.9.4</b> | 15-Jun-2026 | Added 18th attribute `authorized_location_short_address` (short address, for OCA card display). Schema and credential-definition IDs stripped pending re-registration to the verifiable data registry. |
| <b>0.9.5</b> | 16-Jun-2026 | Credential v1.1 (18 attributes) published to CANdy Dev; re-populated the Dev Schema ID (§5.3) and Credential Definition ID (§5.4) with the new ledger identifiers and candyscan links. |
| <b>0.9.6</b> | 21-Jul-2026 | Credential v1.1 endorsed on CANdy Test; populated the Test Schema ID (§5.3) and Credential Definition ID (§5.4) with the ledger identifiers and candyscan links; linked the live Dev OCA Bundle in §5.4. |
| <b>0.9.7</b> | 24-Jul-2026 | Credential v1.1 endorsed on CANdy Prod; populated the Production Schema ID (§5.3) and Credential Definition ID (§5.4) with the ledger identifiers and candyscan links; linked the Test and Production OCA Bundles in §5.4. |

### 1.2 Terminology and Notation

Please reference [Glossary - General Trust Over IP Terms](https://trustoverip.github.io/toip/glossary).

Requirements include any combination of Machine-Testable Requirements and Human-Auditable Requirements. Unless otherwise stated, all Requirements MUST be expressed as defined in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

- Mandates are Requirements that use a MUST, MUST NOT, SHALL, SHALL NOT, or REQUIRED keyword.
- Recommendations are Requirements that use a SHOULD, SHOULD NOT, or RECOMMENDED keyword.
- Options are Requirements that use a MAY or OPTIONAL keyword.

Machine-Testable Requirements are those with which compliance can be verified using an automated test suite and appropriate scripting or testing software.

Rules are Machine-Testable Requirements that are written in a Machine-Readable language and can be processed by a Rules Engine. They are expressed in a structured rules language as specified by the Governance Framework.

Human-Auditable Requirements are those with which compliance can only be verified by an audit of people, processes, and procedures.

Policies are Human-Auditable Requirements written using standard conformance terminology. The Policies used in the Governance Framework use the standard terminology detailed in RFC 2119 keywords. Note that all RFC 2119 keywords have weight from an auditing perspective. An implementer MUST explain why a SHOULD or RECOMMENDED requirement was not implemented and SHOULD explain why a MAY requirement was implemented.

Specifications are documents containing any combination of Machine-Testable Requirements and Human-Auditable Requirements needed to produce technical interoperability.

### 1.3 Localization

The standard language for this governing framework (GF) is English.

## 2. Credential Overview

The Municipal Services Digital Letter of Authorization (MSDiLOA) credential is a verifiable credential (VC) issued to individuals (authorized parties) to prove that they have been granted authorization by another individual or business (authorizer) to consume specific municipal services on their behalf.

The credential is intended to be used in a wide range of municipal service contexts, both alone or alongside other credentials (e.g., BC Person Credential, Business Licence credentials), as a trusted source of authorization information for verifiers such as municipal service departments, licensing and permitting offices, or other government agencies.

| | |
| --- | --- |
| **Credential:**          | Municipal Services Digital Letter of Authorization (MSDiLOA)    |
| **Schema:**              | Municipal Services Digital Letter of Authorization              |
| **Governing Authority:** | City of Vancouver (Founding Authority) <br> Future: Municipal Consortium |
| **First Issuer:**        | City of Vancouver <br> [https://vancouver.ca/](https://vancouver.ca/) |

### 2.1 Attribute Summary

The full set of attributes is described in [Section 4.3 Attributes](#43-attributes).

| **#** | **Name** | **Attribute** | **Data Type** |
| ----- | -------- | ------------- | ------------- |
| 001 | Given names | `authorized_person_given_names` | String |
| 002 | Surname | `authorized_person_family_name` | String |
| 003 | Business name | `authorized_business_name` | String |
| 004 | Licence number | `authorized_business_licence` | String |
| 005 | Location | `authorized_location_full_address` | String |
| 006 | Parcel Identifier (PID) | `authorized_parcel_identifier` | String |
| 007 | Authorized services | `authorized_services` | String |
| 008 | Permission Granted by | `authorizer_role_type` | String |
| 009 | Grantor business name | `authorizer_business_name` | String |
| 010 | Grantor licence number | `authorizer_business_licence` | String |
| 011 | Verification method | `verification_method` | String |
| 012 | Authorization statement | `authorization_details` | String |
| 013 | Valid from | `authorization_valid_from_dateint` | Integer |
| 014 | Valid until | `authorization_valid_until_dateint` | Integer |
| 015 | Authorization number | `authorization_id` | String |
| 016 | Authorized services (machine-readable) | `authorized_services_json` | JSON |
| 017 | Authorized services summary | `authorized_services_summary` | String |
| 018 | Short address | `authorized_location_short_address` | String |

## 3. Credential Details

### 3.1 Issuer

The Municipal Services Digital Letter of Authorization (MSDiLOA) is governed and issued by municipalities within British Columbia.

**Governing Authority:** The City of Vancouver currently serves as the governing authority for the MSDiLOA credential schema and framework. The governing authority is responsible for:

- Establishing and maintaining the credential schema
- Setting governance policies and principles
- Coordinating standardization across municipalities
- Evangelizing and communicating value to drive adoption

In future iterations, governance may evolve into a province-wide municipal steering committee as other municipalities adopt the credential.

**Issuing Municipalities:** Municipalities that issue MSDiLOA credentials are responsible for:

- Administering their local authorization processes
- Reviewing authorization applications and approving issuances
- Operating their Business Licence Systems of Record
- Reviewing foundational identity, property ownership, and authorization documentation
- Revoking and re-issuing credentials as circumstances change

The City of Vancouver is the first issuing municipality. Implementation-specific details for each issuing municipality are maintained in separate implementation guides.

### 3.2 Schema and Credential Definition Governance

The MSDiLOA credential definition implements the schema governed by the City of Vancouver (as founding authority). Both the schema and credential definitions are registered on a verifiable data registry (ledger).

The governing authority may, after appropriate consultation and notification, update the credential definition and/or schema to reflect policy or operational changes. Updates will follow the broader municipal credential governance framework and are designed for eventual province-wide interoperability.

Individual issuing municipalities maintain their own credential definitions based on the governed schema.

### 3.3 Issuer Data Source

The MSDiLOA is issued after collecting and verifying personal details, location information, and authorization relationships between parties. Some information is generated directly by the Issuer, while other elements are verified against trusted sources.

General data sources include:

- **Authorization Request** – the information provided by the applicant (authorized party) during the authorization request process
- **Municipal Systems** – system-generated data and verification records
- **Foundational Identity Verification** – identity confirmation using trusted digital credentials (such as Person Credentials)
- **Property or Business Ownership Verification** – records checked through authoritative sources to confirm the authorizer's eligibility
- **Authorization Documentation** – collected authorization agreements and supporting evidence

The source of each attribute is described in [Section 4.3 Attributes](#43-attributes).

#### 3.3.1 Data Updates

When a credential is issued, its data reflects the authorization and related records at the time of issuance. Changes to authorization records (e.g., revocation by authorizer, changes to authorized services, or changes to the authorized party) trigger a revocation and may result in re-issuance of the credential to reflect current information.

### 3.4 Assurance

To minimize risk to verifiers, municipalities, and credential holders, the MSDiLOA credential is only issued following successful authentication and validation of:

- **Authorized Party Identity** – verified using a high-assurance digital identity credential (such as a Person Credential)
- **Authorizer Identity** – verified using a high-assurance digital identity credential
- **Authorizer's Authority** – verified against authoritative records (e.g., property ownership records, business registration records)
- **Authorization Agreement** – verified through documented authorization by the authorizer

These checks ensure the authenticity of the relationship between the authorized party, the authorizer, and the services being authorized.

Specific verification methods used by each issuing municipality are detailed in their respective implementation guides.

### 3.5 Revocation

A MSDiLOA credential will be revoked in the following cases:

1. The authorizer revokes the authorization – the party who granted authorization may cancel it at any time before expiration
2. The authorization expires – authorizations have default expiration dates specific to each service type
3. The authorization record is updated – changes to authorized services, parties, or other key details require credential revocation and re-issuance
4. The underlying service licence or permission is withdrawn or invalidated – if the service that was authorized becomes invalid, the authorization credential is also revoked

In some cases, a revocation triggers a re-issuance of the credential with updated details to reflect the new authorization record.

### 3.6 Legal

> *Draft, generic language — to be reviewed by the governing authority's legal counsel before publication. Written at the schema level; each issuing municipality may add to or supersede these terms in its own implementation documentation.*

**For verifiers.** The MSDiLOA credential is provided on an "as-is" and "as-available" basis. The governing authority and issuing municipalities make no representations or warranties regarding its accuracy, completeness, or fitness for any particular purpose. Verifiers rely on the credential at their own discretion, and no party is responsible or liable for any loss, damage, or claim arising from the use of, or reliance on, the credential.

**For end users (holders).** Holders are responsible for their use of the MSDiLOA credential. The specific terms of use that govern holders are defined by the issuing municipality and provided through that municipality's implementation.

## 4. Credential Definition

### 4.1 Credential Schema

The Municipal Services Digital Letter of Authorization credential is based on the Municipal Services Digital Letter of Authorization schema, version 1.0, governed by the City of Vancouver and maintained on an appropriate verifiable data registry.

The Verifiable Credential format for this credential uses the AnonCreds specification.

### 4.2 Subject of the Credential

The subject of the credential is the authorization record, which establishes:

- The individual or business (authorized party/credential holder) who has been granted authorization, and
- The services, location, and authorizing party associated with the authorization.

The credential enables the holder to prove, in real time, that they are authorized to consume specific municipal services on behalf of another party at a specified location or for a specified purpose.

### 4.3 Attributes

The attributes of the Municipal Services Digital Letter of Authorization credential are organized by topic and described below.

#### 4.3.1 Attributes about the Authorized Party

*Given Names (001)*

| | |
| --- | --- |
| **Attribute** | `authorized_person_given_names` |
| **Description** | The given names of the person who has been granted authorization to consume municipal services. |
| **Source** | Verified via proof request presented by the BC Services Card App at time of application. |
| **Data Type** | String |
| **Examples** | `John`<br>`Mary Anne` |

*Surname (002)*

| | |
| --- | --- |
| **Attribute** | `authorized_person_family_name` |
| **Description** | The family name of the person who has been granted authorization to consume municipal services. |
| **Source** | Verified via proof request presented by the BC Services Card App at time of application. |
| **Data Type** | String |
| **Examples** | `Doe`<br>`Smith` |

#### 4.3.2 Attributes about the Authorization

*Business name (003)*

| | |
| --- | --- |
| **Attribute** | `authorized_business_name` |
| **Description** | The name of the business that is being authorized. |
| **Source** | Municipal system of record (authorization application). |
| **Data Type** | String |
| **Examples** | `XYZ Incorporated` |

*Licence number (004)*

| | |
| --- | --- |
| **Attribute** | `authorized_business_licence` |
| **Description** | The number of the related business licence that is being authorized. |
| **Source** | Municipal system of record (authorization application). |
| **Data Type** | String |
| **Examples** | `#BL 26-110904` |

#### 4.3.3 Attributes about the Location

*Location (005)*

| | |
| --- | --- |
| **Attribute** | `authorized_location_full_address` |
| **Description** | The complete address of the location for which the applicant is requesting authorization to consume services. |
| **Source** | Municipal system of record (verified against civic address records and property records). |
| **Data Type** | String |
| **Examples** | `Suite 301, 123 Main Street, Vancouver, BC, V6B 2Y5, Canada`<br>`456 Oak Avenue, Victoria, BC, V8W 1N7, Canada` |

*Parcel Identifier (PID) (006)*

| | |
| --- | --- |
| **Attribute** | `authorized_parcel_identifier` |
| **Description** | A PID (Parcel Identifier) is a nine-digit number that uniquely identifies a parcel in the land title register of British Columbia. The registrar assigns PID numbers to parcels for which a title is being entered in the computer register as a registered title. Format: `###-###-###` (three groups of three digits separated by dashes). |
| **Source** | Municipal system of record (authorization application). |
| **Data Type** | String |
| **Examples** | `031-144-956` |

*Short address (018)*

| | |
| --- | --- |
| **Attribute** | `authorized_location_short_address` |
| **Description** | Combination of unit number + street number + street name. |
| **Source** | Municipal system of record (verified against civic address records and property records). |
| **Data Type** | String |
| **Examples** | `111 Example St` |

#### 4.3.4 Attributes about the Authorizer

*Authorized services (007)*

| | |
| --- | --- |
| **Attribute** | `authorized_services` |
| **Description** | A human-readable, comma-separated list of the short names of the municipal services authorized under this credential. A single MSDiLOA may authorize multiple services. The authoritative, machine-readable list — including each service's identifier and individual expiry date — is carried in `authorized_services_json`. |
| **Source** | Municipal system of record (authorization application). |
| **Data Type** | String (comma-separated list) |
| **Examples** | `Short-Term Rental`<br>`Short-Term Rental, Residential Parking Permit` |

*Permission granted by (008)*

| | |
| --- | --- |
| **Attribute** | `authorizer_role_type` |
| **Description** | The role or capacity in which the authorizer is granting authorization (e.g., property owner, business owner). |
| **Source** | Municipal system of record (verified against property or business ownership records). |
| **Data Type** | String |
| **Examples** | `Property Owner`<br>`Business Owner` |

*Grantor business name (009)*

| | |
| --- | --- |
| **Attribute** | `authorizer_business_name` |
| **Description** | If applicable, the name of the business that is authorizing the consumption of services. The authorizing person may use a digital Business Licence credential to share this information. If not applicable, this value will be "N/A". |
| **Source** | Verified via digital Business Licence credential or municipal business records. |
| **Data Type** | String |
| **Examples** | `Downtown Properties Ltd.`<br>`N/A` |

*Grantor licence number (010)*

| | |
| --- | --- |
| **Attribute** | `authorizer_business_licence` |
| **Description** | The number of the related business licence of the authorizer. |
| **Source** | Verified via digital Business Licence credential or municipal business records. |
| **Data Type** | String |
| **Examples** | `Downtown Properties Ltd.`<br>`N/A` |

#### 4.3.5 Attributes about the Evidence

*Verification method (011)*

| | |
| --- | --- |
| **Attribute** | `verification_method` |
| **Description** | Indicates whether digital credentials were used as proof of verification. Value = "Manual" if no digital credentials were used. If a Property Owner Credential was used, value = "Digital". |
| **Source** | Municipal system of record (based on verification method used). |
| **Data Type** | String |
| **Examples** | `Manual`<br>`Digital` |

*Authorization statement (012)*

| | |
| --- | --- |
| **Attribute** | `authorization_details` |
| **Description** | Human readable natural language statement of the authorization (e.g., "I, [Authorizer Name], hereby authorize [Authorized Party Name]..."). |
| **Source** | Municipal system of record (generated from authorization record). |
| **Data Type** | String |
| **Examples** | `The [authorizer_role_type], hereby authorize [authorized_person_given_name + authorized_person_family_name] to apply for a [authorized_services] for the property located at [authorized_location_full_address]` |

*Valid from (013)*

| | |
| --- | --- |
| **Attribute** | `authorization_valid_from_dateint` |
| **Description** | The date on which the MSDiLOA credential was issued. |
| **Source** | Municipal system of record (system-generated timestamp). |
| **Data Type** | Integer (YYYYMMDD) |
| **Examples** | `20260105` |

*Valid until (014)*

| | |
| --- | --- |
| **Attribute** | `authorization_valid_until_dateint` |
| **Description** | The date on which the MSDiLOA credential will expire. |
| **Source** | Municipal system of record (system-generated timestamp). |
| **Data Type** | Integer (YYYYMMDD) |
| **Examples** | `20260205` |

*Authorization number (015)*

| | |
| --- | --- |
| **Attribute** | `authorization_id` |
| **Description** | A unique identifier that correlates to the underlying proof data and authorization documentation, stored in the system of record. |
| **Source** | Municipal system of record (system-generated). |
| **Data Type** | String |
| **Examples** | `AUTH-2026-00123-PROOF`<br>`LOA-456789-VER` |

*Authorized services — machine-readable (016)*

| | |
| --- | --- |
| **Attribute** | `authorized_services_json` |
| **Description** | The authoritative, machine-readable list of services authorized under this credential — one entry per service, each carrying its own identifier, short name, expiry date, and options. This is what allows multiple services in a single credential to carry _different_ expiry dates, and what enables interoperable parsing across municipalities (e.g., for business-to-business authorization). A formal, versioned JSON Schema for this value is defined in Appendix C; the `schema_version` field identifies the structure in use. This is an experimental structure and is expected to evolve. |
| **Source** | Municipal system of record (authorization application). |
| **Data Type** | JSON (string-encoded; conforms to the published, versioned `authorized_services_json` schema) |
| **Examples** | `{ "schema_version": "1.0", "services": [ { "service_id": "STR-001", "service_short_name": "Short-Term Rental", "auth_expiry_date": "2026-12-31", "service_options": [ { "name": "document_types", "value": "Development Permits, Building Permits", "type": "string_list", "mandatory": true } ] }, { "service_id": "RPP-002", "service_short_name": "Residential Parking Permit", "auth_expiry_date": "2027-06-30", "service_options": [] } ] }` |

*Authorized services summary (017)*

| | |
| --- | --- |
| **Attribute** | `authorized_services_summary` |
| **Description** | A human-readable summary of the authorized service(s) and validity, for display on the wallet card. Derived from `authorized_services` and the credential's validity dates. |
| **Source** | Municipal system of record (authorization application). |
| **Data Type** | String |
| **Examples** | `Short-Term Rental / EXP 2026-12-31` |

## 5. Implementations

### 5.1 Technical Format

This credential uses the [Hyperledger AnonCreds](https://github.com/hyperledger/anoncreds/) specification.

### 5.2 Issuer List

The Governing Authority of this Credential document attests that the following issuer information is accurate and can be relied upon by verifiers.

| **Environment** | **Issuer Name** | **Issuer DID** |
| :--: | :--: | :--: |
| CANdy Production | City of Vancouver | <code>R12pguaP3VF2WiE6vAsiPF</code> |
| CANdy Test | City of Vancouver (UAT) | <code>ARK5s3QZtjL5X65mLoubdk</code> |
| CANdy Dev | City of Vancouver (DEV) | <code>YWnESLB4SH275SMNvaJJ1L</code> |

> **Note:** Additional municipalities will be added to this list as they adopt the MSDiLOA credential.

### 5.3 Schema Implementation

| **Environment** | **Ledger** | **Schema ID** |
| :--: | :--: | :--: |
| CANdy Production | [Municipal Services Digital Letter of Authorization](https://candyscan.digitaltrust.gov.bc.ca/tx/CANDY_PROD/domain/8117) | <code>R12pguaP3VF2WiE6vAsiPF:2:Municipal Services Digital Letter of Authorization:1.1</code> |
| CANdy Test | [Municipal Services Digital Letter of Authorization](https://candyscan.digitaltrust.gov.bc.ca/tx/CANDY_TEST/domain/1205) | <code>ARK5s3QZtjL5X65mLoubdk:2:Municipal Services Digital Letter of Authorization:1.1</code> |
| CANdy Dev | [Municipal Services Digital Letter of Authorization](https://candyscan.digitaltrust.gov.bc.ca/tx/CANDY_DEV/domain/39764) | <code>YWnESLB4SH275SMNvaJJ1L:2:Municipal Services Digital Letter of Authorization:1.1</code> |

### 5.4 Credential Implementation

| **Environment** | **Ledger** | **Credential Definition ID** | **OCA Bundle** |
| :--: | :--: | :--: | :--: |
| CANdy Production | [Municipal Services Digital Letter of Authorization](https://candyscan.digitaltrust.gov.bc.ca/tx/CANDY_PROD/domain/8118) | <code>R12pguaP3VF2WiE6vAsiPF:3:CL:8117:Municipal Services Digital Letter of Authorization</code> | [prod-municipal-services-digital-letter-of-authorization](https://github.com/bcgov/aries-oca-bundles/tree/main/OCABundles/schema/CityOfVancouver/prod-municipal-services-digital-letter-of-authorization) |
| CANdy Test | [Municipal Services Digital Letter of Authorization](https://candyscan.digitaltrust.gov.bc.ca/tx/CANDY_TEST/domain/1207) | <code>ARK5s3QZtjL5X65mLoubdk:3:CL:1205:Municipal Services Digital Letter of Authorization</code> | [test-municipal-services-digital-letter-of-authorization](https://github.com/bcgov/aries-oca-bundles/tree/main/OCABundles/schema/CityOfVancouver/test-municipal-services-digital-letter-of-authorization) |
| CANdy Dev | [Municipal Services Digital Letter of Authorization](https://candyscan.digitaltrust.gov.bc.ca/tx/CANDY_DEV/domain/39765) | <code>YWnESLB4SH275SMNvaJJ1L:3:CL:39764:Municipal Services Digital Letter of Authorization</code> | [dev-municipal-services-digital-letter-of-authorization](https://github.com/bcgov/aries-oca-bundles/tree/main/OCABundles/schema/CityOfVancouver/dev-municipal-services-digital-letter-of-authorization) |

## Appendix A: Glossary

- **Authorized Party** – Either an 'Authorized Person' or an 'Authorized Business'; the party who has been granted authorization to consume municipal services on behalf of another party.
- **Authorized Person** – The holder of an MSDiLOA issued through a given jurisdiction with the approval of the authorizer party.
- **Authorizer Person** – Person approving the issuance of the Municipal Services Digital Letter of Authorization credential for specified services.
- **MSDiLOA** – Municipal Services Digital Letter of Authorization credential.
- **Person Credential** – A high-assurance digital identity credential (e.g., BC Person Credential) used to verify the identity of both the authorizer and authorized party.

## Appendix B: Risk Assessment

Issuing municipalities are responsible for completing appropriate risk assessments in accordance with their jurisdiction's procedures and policies. This may include Privacy Impact Assessments (PIA) and Security Threat and Risk Assessments (STRA) as required by local governance frameworks.

## Appendix C: `authorized_services_json` — JSON Schema (v1, draft)

> **Note:** This is a **first version** of the schema for the `authorized_services_json` attribute (Section 4.3, attribute 016) and **will likely change** as service use cases are socialized and refined across municipalities. The `schema_version` field carried in each credential's value identifies the structure in use. This draft is pending City of Vancouver / BC Digital Trust confirmation.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "MSDiLOA authorized_services_json",
  "description": "Schema for the string-encoded JSON value of the authorized_services_json attribute in the Municipal Services Digital Letter of Authorization (MSDiLOA) credential. Experimental first version; the schema_version field identifies the structure in use.",
  "type": "object",
  "required": ["schema_version", "services"],
  "additionalProperties": false,
  "properties": {
    "schema_version": {
      "type": "string",
      "description": "Version of this structure (major.minor), e.g. '1.0'.",
      "pattern": "^[0-9]+\\.[0-9]+$"
    },
    "services": {
      "type": "array",
      "description": "One entry per municipal service authorized under this credential.",
      "minItems": 1,
      "items": { "$ref": "#/$defs/service" }
    }
  },
  "$defs": {
    "service": {
      "type": "object",
      "required": ["service_id", "service_short_name", "auth_expiry_date"],
      "additionalProperties": false,
      "properties": {
        "service_id": {
          "type": "string",
          "description": "Stable identifier for the authorized service."
        },
        "service_short_name": {
          "type": "string",
          "description": "Human-readable short name of the service (matches an entry in the authorized_services list)."
        },
        "auth_expiry_date": {
          "type": "string",
          "format": "date",
          "description": "Expiry date of this service's authorization (ISO 8601, YYYY-MM-DD). Allows different services in one credential to expire at different times."
        },
        "service_options": {
          "type": "array",
          "description": "Optional per-service parameters.",
          "default": [],
          "items": { "$ref": "#/$defs/service_option" }
        }
      }
    },
    "service_option": {
      "type": "object",
      "required": ["name", "value", "type"],
      "additionalProperties": false,
      "properties": {
        "name": { "type": "string" },
        "value": { "type": "string" },
        "type": {
          "type": "string",
          "enum": ["string", "string_list", "integer", "boolean", "date"]
        },
        "mandatory": { "type": "boolean", "default": false }
      }
    }
  }
}
```
