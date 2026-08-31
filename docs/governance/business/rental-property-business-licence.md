# Rental Property Business Licence Credential Documentation

## 1. About this Document

This document describes the **Rental Property Business Licence** verifiable credential to help potential verifiers determine whether it is suitable for their needs. The intended audience includes policy analysts, privacy specialists, solution architects, developers, and data architects.

The Rental Property Business Licence credential can be issued by any British Columbia municipality. The first municipality to do so is the **City of Vancouver**, and represents a valid municipal business licence for operating rental properties.

> **Note:** This credential schema was originally designed to support both short-term rental (STR) and long-term rental (LTR) business licence types.

### 1.1 Version History

| Ver.      | Date | Notes |
| ----------- | ----------- | ----------- |
| <b>1.0</b>      | 15-Oct-2025       | Initial release |

## 2 Credential Overview
The Rental Property Business Licence credential is a verifiable credential (VC) issued to individuals or authorized representatives of businesses to prove that they hold a valid City of Vancouver rental business licence.

The credential is intended to be used in a wide range of contexts, both alone or alongside other credentials (e.g., BC Person Credential, Digital Business Card), as a trusted source of business licence information for verifiers such as property listing platforms, municipal inspectors, or other government agencies.

| Field | Value |
| --- | --- |
| **Credential:**         | Rental Property Business Licence                                                                    |
| **Schema:**             | Rental Property Business Licence                                                                    |
| **Issuer:**             | City of Vancouver (Business Licenses Division) <br> [https://vancouver.ca/](https://vancouver.ca/) |

### 2.1 Attribute Summary

The full set of attributes is described in [Section 4.3 Attributes](#43-attributes).

| **#**       | **Name**                      | **Attribute**                        | **Data Type** |
|-------------|-------------------------------|--------------------------------------|---------------|
| 001         | Business Licence Type         | `business_licence_type`              | String        |
| 002         | Business Sub-Type             | `business_sub_type`                  | String        |
| 003         | Business / Trade Name         | `business_trade_name`                | String        |
| 004         | Licence Number                | `licence_number`                     | String        |
| 005         | Licence Revision Number       | `licence_revision_number`            | String        |
| 006         | Licence Holder First Name     | `licence_holder_given_name`          | String        |
| 007         | Licence Holder Last Name      | `licence_holder_family_name`         | String        |
| 008         | Issue Date                    | `licence_issued_dateint`             | Integer       |
| 009         | Licence Start Date            | `licence_valid_from_dateint`         | Integer       |
| 010         | Expiry Date                   | `licence_expiry_dateint`             | Integer       |
| 011         | Unit Number                   | `unit`                               | String        |
| 012         | Unit Type                     | `unit_type`                          | String        |
| 013         | Street Number                 | `street_number`                      | String        |
| 014         | Street Name                   | `street_name`                        | String        |
| 015        | Municipality                  | `municipality`                       | String        |
| 016         | Municipality Status           | `municipality_status`                | String        |
| 017         | Regional District             | `regional_district`                  | String        |
| 018         | Province / Territory          | `province_territory`                 | String        |
| 019         | Postal Code                   | `postal_code`                        | String        |
| 020         | Country                       | `country`                            | String        |
| 021         | Full Licence Address          | `full_licence_address`               | String        |
| 022         | Property Residence Type       | `property_residence_type`            | String        |
| 023         | Neighbourhood / Local Area    | `local_area`                         | String        |
| 024         | Location Type                 | `location_type`                      | String        |
| 025         | Number of Dwelling Units      | `number_of_dwelling_unitsint`        | Integer       |
| 026         | Parcel Identifier (PID)       | `PID`                                | String        |
| 027         | Strata Flag                   | `strata_flag`                        | Boolean       |
| 028         | GIS Coordinates               | `GIS_coordinates`                    | String        |
| 029         | Identity Verification Proof   | `identity_verification_proof`        | String        |
| 030         | Primary Address Proof         | `primary_address_verification_proof` | String        |
| 031         | Property Owner Proof          | `property_owner_proof`               | String        |
| 032         | Authorized Verification Proof | `authorized_verification_proof`      | String        |
| 033         | Licence Summary               | `licence_summary`                    | String        |
| 034         | Short Address                 | `short_address`                      | String        |

## 3. Credential Details

### 3.1 Issuer

The Rental Property Business Licence credential is issued by **City of Vancouver's Business Licence Office**. The issuer municipality is responsible for reviewing business licence applications, approving, issuing, renewing and revoking all municipal business licences within their jurisdiction and in some cases they could delegate such activities to other organizations.

The City of Vancouver is responsible for:

- Administering the <a href="https://vancouver.ca/your-government/licence-bylaw.aspx">Licence Bylaw</a>, including processing applications, renewals, and amendments to licences.
- Operating the **Business Licence System of Record**, which records licence issuance, renewals, revocations, and changes to attributes such as business trade name or location.
- Reviewing foundational identity, property ownership, and authorization documentation as part of the licensing process.

### 3.2 Schema and Credential Definition Governance

The Rental Property Business Licence credential definition implements the schema published by the City of Vancouver. Both the schema and credential definition are registered on the CANdy Dev Ledger.

The City of Vancouver may, after appropriate consultation and notification, update the credential definition and/or schema to reflect policy or operational changes. Updates will follow the broader municipal credential governance framework and are designed for eventual province-wide interoperability.

### 3.3 Issuer Data Source

The data in the Rental Property Business Licence credential is sourced from applicant identity credentials and municipal systems of record. Some information is generated directly by the Issuer, while other elements are verified against trusted external sources.

- **Business Licence Filing** – the information provided by or on behalf of the applicant during the licence application or renewal process.
- **City of Vancouver Business Licence System** – system-generated data such as licence number, revision number, and timestamps.
- **Foundational Identity Verification** – the applicant’s identity is confirmed using the BC Person Credential.
- **Property Ownership Verification** – records are checked through internal systems of record to confirm ownership or authorized use of the property.
- **Authorization Verification** – an Owner’s Letter of Authorization, where applicable, is collected and retained.

The source of each attribute is described in [Section 4.3 Attributes](#43-attributes).

#### 3.3.1 Data Updates

When a credential is issued, its data reflects the business licence record at the time of issuance. Changes to licence records (*e.g., business trade name, ownership, address*) trigger a revocation and re-issuance of the credential so that the holder’s credential always reflects current information.

### 3.4 Assurance

To minimize risk to verifiers, the City, and licence holders, the Rental Property Business Licence credential is only issued following successful authentication and validation of:

- **Applicant identity** – via the BC Person Credential (high-assurance, Level 3 trusted digital identity).
- **Primary address history** – verified using ICBC address records or the Person Credential, for short-term rental licence applications.
- **Property ownership** – verified against internal systems, for long-term rental licence applications.
- **Authorization** – verified by requiring an Owner’s Letter of Authorization if the applicant is not the property owner, for short term rental applications.

These checks ensure the authenticity of the relationship between the applicant, the business, and the property location.

### 3.5 Revocation

A Rental Property Business Licence credential will be revoked in the following cases:

1. The underlying business licence is withdrawn, invalidated, or expires.
2. The business licence record is updated (e.g., new address, ownership, or trade name).
3. The licence holder or designated representative is no longer authorized, leading to a permanent revocation.

In most cases, a revocation triggers a **re-issuance** of the credential with updated details to reflect the new licence record.

## 4. Credential Definition

### 4.1 Credential Schema

The Rental Property Business Licence credential is based on the rental-property-business-licence schema, version 1.0, published by the City of Vancouver and maintained on the CANdy Dev Ledger.

### 4.2 Subject of the Credential

The subject of the credential is the licence record, which ties:

- The individual or authorized representative (credential holder), and
- The business/property information associated with the licence.

The credential enables the holder to prove, in real time, that they are licensed by the City of Vancouver to operate a rental property business (short-term or long-term) at the specified location/address.

### 4.3 Attributes

The attributes of the Rental Property Business Licence credential are organized by topic and described below.

#### 4.3.1 Attributes about the Licence

*Business Licence Type (001)*

| Field | Value |
| --- | --- |
| **Attribute** | `business_licence_type` |
| **Description** | The category of licence issued. |
| **Source** | Municipal Business Licence System of Record. |
| **Data Type** | String |
| **Examples** | `Short-Term Rental`<br>`Long-Term Rental` |

*Business Sub-Type (002)*

| Field | Value |
| --- | --- |
| **Attribute** | `business_sub_type` |
| **Description** | The sub type of business licence being issued. |
| **Source** | Municipal Business Licence System of Record. |
| **Data Type** | String |
| **Examples** | `Multiple Dwelling - 99 Year Lease`<br>`Non-profit Housing` |

*Licence Number (004)*

| Field | Value |
| --- | --- |
| **Attribute** | `licence_number` |
| **Description** | The issued licence number of the business licence. |
| **Source** | Municipal Business Licence System of Record. |
| **Data Type** | String |
| **Examples** | `24-123456` |

*Licence Revision Number (005)*

| Field | Value |
| --- | --- |
| **Attribute** | `licence_revision_number` |
| **Description** | The revision number of the issued business licence. |
| **Source** | Municipal Business Licence System of Record. |
| **Data Type** | String |
| **Examples** | `1`<br>`2` |

*Issue Date (008)*

| Field | Value |
| --- | --- |
| **Attribute** | `licence_issued_dateint` |
| **Description** | The issued date of the business licence. |
| **Source** | Municipal Business Licence System of Record. |
| **Data Type** | Integer (YYYYMMDD) |
| **Examples** | `20250115` |

*Licence Start Date (009)*

| Field | Value |
| --- | --- |
| **Attribute** | `licence_valid_from_dateint` |
| **Description** | The date on which the business is permitted to begin operating under the issued licence. |
| **Source** | Municipal Business Licence System of Record. |
| **Data Type** | Integer (YYYYMMDD) |
| **Examples** | `20250115`<br>`20240901` |


*Expiry Date (010)*

| Field | Value |
| --- | --- |
| **Attribute** | `licence_expiry_dateint` |
| **Description** | The expiry date of the business licence. |
| **Source** | Municipal Business Licence System of Record. |
| **Data Type** | Integer (YYYYMMDD) |
| **Examples** | `20251231` |

*Licence Summary (033)*

| Field | Value |
| --- | --- |
| **Attribute** | `licence_summary` |
| **Description** | A concatenated summary of the business licence number and expiry date. |
| **Source** | Municipal Business Licence System of Record (derived from `licence_number` and `licence_expiry_dateint`). |
| **Data Type** | String |
| **Examples** | `BL-123456 | Expires 20250907`<br> `LTR-987654 | Expires 20241231` |


#### 4.3.2 Attributes about the Business / Licence Holder

*Business / Trade Name (003)*

| Field | Value |
| --- | --- |
| **Attribute** | `business_trade_name` |
| **Description** | The business name of the operator of the business licence. |
| **Source** | Municipal Business Licence System of Record (as reported by the applicant). |
| **Data Type** | String |
| **Examples** | `West End Suites`<br>`Maple Rentals` |

*Licence Holder First Name (006)*

| Field | Value |
| --- | --- |
| **Attribute** | `licence_holder_given_name` |
| **Description** | Licence holder given name of the business licence. |
| **Source** | Verified via BC Person Credential and government-issued photo ID. |
| **Data Type** | String |
| **Examples** | `Jane` |

*Licence Holder Last Name (007)*

| Field | Value |
| --- | --- |
| **Attribute** | `licence_holder_family_name` |
| **Description** | Licence holder family name of the business licence. |
| **Source** | Verified via BC Person Credential and government-issued photo ID. |
| **Data Type** | String |
| **Examples** | `Doe` |

#### 4.3.3 Attributes about the Location

*Unit (011)*

| Field | Value |
| --- | --- |
| **Attribute** | `unit` |
| **Description** | The unit number of the business licence. |
| **Source** | Municipal Business Licence System of Record (provided by the applicant and verified against property records). |
| **Data Type** | String |
| **Examples** | `101`<br>`3B` |

*Unit Type (012)*

| Field | Value |
| --- | --- |
| **Attribute** | `unit_type` |
| **Description** | The unit type of the business licence. |
| **Source** | Municipal Business Licence System of Record. |
| **Data Type** | String |
| **Examples** | `Suite`<br>`Basement` |

*Street Number (013)*

| Field | Value |
| --- | --- |
| **Attribute** | `street_number` |
| **Description** | The street number that precedes the street name of the business licence location. |
| **Source** | Municipal Business Licence System of Record (verified against civic address records). |
| **Data Type** | String |
| **Examples** | `1234` |

*Street Name (014)*

| Field | Value |
| --- | --- |
| **Attribute** | `street_name` |
| **Description** | The street name of the business licence. |
| **Source** | Municipal Business Licence System of Record (verified against civic address records). |
| **Data Type** | String |
| **Examples** | `Main Street`<br>`West 4th Avenue` |

*Municipality (015)*

| Field | Value |
| --- | --- |
| **Attribute** | `municipality` |
| **Description** | The municipality of the business licence. |
| **Source** | Municipal Business Licence System of Record. |
| **Data Type** | String |
| **Examples** | `Vancouver` |

*Municipality Status (016)*

| Field | Value |
| --- | --- |
| **Attribute** | `municipality_status` |
| **Description** | Municipality type of the licensed location. |
| **Source** | Municipal Business Licence System of Record. |
| **Data Type** | String |
| **Examples** | `City` |

*Regional District (017)*

| Field | Value |
| --- | --- |
| **Attribute** | `regional_district` |
| **Description** | One of the twenty-seven regional districts in British Columbia. |
| **Source** | Municipal Business Licence System of Record (derived from property records). |
| **Data Type** | String |
| **Examples** | `Metro Vancouver` |

*Province or Territory (018)*

| Field | Value |
| --- | --- |
| **Attribute** | `province_territory` |
| **Description** | The province or territory of the business licence. |
| **Source** | Municipal Business Licence System of Record. |
| **Data Type** | String |
| **Examples** | `British Columbia` |

*Postal Code (019)*

| Field | Value |
| --- | --- |
| **Attribute** | `postal_code` |
| **Description** | The postal code of the business licence. |
| **Source** | Municipal Business Licence System of Record (verified against Canada Post format). |
| **Data Type** | String |
| **Examples** | `V6B 2Y5` |

*Country (020)*

| Field | Value |
| --- | --- |
| **Attribute** | `country` |
| **Description** | The country of the business licence. |
| **Source** | Municipal Business Licence System of Record. |
| **Data Type** | String |
| **Examples** | `Canada` |

*Full Licence Address (021)*

| Field | Value |
| --- | --- |
| **Attribute** | `full_licence_address` |
| **Description** | Combination of individual address attributes. |
| **Source** | Municipal Business Licence System of Record (derived from applicant submissions and verified against property and identity records). |
| **Data Type** | String |
| **Examples** | `Suite, Unit 201, 123 Main Street, Vancouver, BC, V6B 2Y1, Canada` |

*Local Area (023)*

| Field | Value |
| --- | --- |
| **Attribute** | `local_area` |
| **Description** | Local area definition. For Vancouver, one of the twenty-two neighbourhoods where the licensed location exists. |
| **Source** | Municipal Business Licence System of Record (derived from municipal planning datasets). |
| **Data Type** | String |
| **Examples** | `Kitsilano`<br>`Downtown` |

*GIS Coordinates (028)*

| Field | Value |
| --- | --- |
| **Attribute** | `GIS_coordinates` |
| **Description** | The geographic coordinates of the licensed location. |
| **Source** | City of Vancouver GIS dataset. |
| **Data Type** | String (lat,long) |
| **Examples** | `49.2827,-123.1207` |

*Short Address (034)*

| Field | Value |
| --- | --- |
| **Attribute** | `short_address` |
| **Description** | A shortened address string consisting of unit, street number, and street name of the licensed property. |
| **Source** | Municipal Business Licence System of Record (derived from `unit`, `street_number`, and `street_name`). |
| **Data Type** | String |
| **Examples** | `#201 123 Main Street`<br> `456 Granville St` |

#### 4.3.4 Attributes about the Property

*Property Residence Type (022)*

| Field | Value |
| --- | --- |
| **Attribute** | `property_residence_type` |
| **Description** | The type of property residence. |
| **Source** | Municipal Business Licence System of Record. |
| **Data Type** | String |
| **Examples** | `Condominium`<br>`Single Family` |

*Location Type (024)*

| Field | Value |
| --- | --- |
| **Attribute** | `location_type` |
| **Description** | The type of business licensed location. |
| **Source** | Applicant declaration in Municipal Business Licence System of Record; validated against BC Person Credential attributes. |
| **Data Type** | String |
| **Examples** | `Principal Residence`<br>`Secondary Suite` |

*Number of Dwelling Units (025)*

| Field | Value |
| --- | --- |
| **Attribute** | `number_of_dwelling_unitsint` |
| **Description** | The number of dwelling units at the licensed location. Specific to LTR business licence types. |
| **Source** | Municipal Business Licence System of Record (verified against property assessment records). |
| **Data Type** | Integer |
| **Examples** | `1`<br>`12` |

*Parcel Identifier (PID) (026)*

| Field | Value |
| --- | --- |
| **Attribute** | `PID` |
| **Description** | The nine digit parcel identifier. |
| **Source** | Municipal Business Licence System of Record. |
| **Data Type** | String (9-digit numeric) |
| **Examples** | `012-345-678` |

*Strata Flag (027)*

| Field | Value |
| --- | --- |
| **Attribute** | `strata_flag` |
| **Description** | Indicates whether the property is part of a strata (condominium) development. |
| **Source** | Municipal Business Licence System of Record. |
| **Data Type** | Boolean |
| **Examples** | `true`<br>`false` |

#### 4.3.5 Attributes about Evidence

> **Note:** The example values for evidence attributes are shown as JSON objects, since this is the expected data structure. However, in Section 2.1 they are defined as **String** types, as credential attribute values must remain flat.

*Identity Verification Proof (029)*

| Field | Value |
| --- | --- |
| **Attribute** | `identity_verification_proof` |
| **Description** | Specifies the method and proofs used to confirm the applicant’s identity (e.g., BC Person Credential). |
| **Source** | Municipal Business Licence System of Record (validated against BC Person Credential). |
| **Data Type** | JSON |
| **Examples** | `BC Person Credential`<br> `{ "verification_method": "digital", "proofs": ["Person Credential"] }` |

*Primary Address Verification Proof (030)*

| Field | Value |
| --- | --- |
| **Attribute** | `primary_address_verification_proof` |
| **Description** | Specifies the method used to verify the applicant’s primary residential address. |
| **Source** | Municipal Business Licence System of Record (verified against ICBC address history) |
| **Data Type** | JSON |
| **Examples** | `ICBC Address Record`<br> `{ "verification_method": "manual", "proofs": ["ICBC Residential Address History"] }` |

*Property Owner Proof (031)*

| Field | Value |
| --- | --- |
| **Attribute** | `property_owner_proof` |
| **Description** | Specifies the evidence provided to demonstrate legal ownership of the property associated with the business licence. |
| **Source** | Municipal Business Licence System of Record. |
| **Data Type** | JSON |
| **Examples** | `Title Record`<br> `{ "verification_method": "digital", "proofs": ["Property Ownership Record"] }` |

*Authorized Verification Proof (032)*

| Field | Value |
| --- | --- |
| **Attribute** | `authorized_verification_proof` |
| **Description** | Specifies the evidence used to confirm that the applicant is authorized by the property owner to apply for or hold the business licence. |
| **Source** | Applicant-submitted authorization letters or municipal approval records; stored in the Municipal Business Licence System of Record. |
| **Data Type** | JSON |
| **Examples** | `Signed Owner Authorization Letter`<br> `{ "verification_method": "manual", "proofs": ["Owner Authorization Letter", "Municipal Approval Form"] }` |

## 5. Implementations

## 5.1 Technical Format

This credential uses the [Hyperledger AnonCreds](https://github.com/hyperledger/anoncreds/) specification and the "Rental Property Business Licence" schema which has the following defined attributes.

### 5.2 Issuer List
The Governing Authority of this Credential document attests that the following issuer information is accurate and can be relied upon by verifiers.
| Environment | Issuer Name | Issuer DID |
|------|------|-------|
| CANdy Production  | City of Vancouver  | <code>R12pguaP3VF2WiE6vAsiPF</code>   |
| CANdy Test  | City of Vancouver (UAT)  | <code>ARK5s3QZtjL5X65mLoubdk</code>   |
| CANdy Dev  | City of Vancouver (DEV)   | <code>YWnESLB4SH275SMNvaJJ1L</code>   |

### 5.3 Schema Implementation
|Environment|Ledger|Schema ID|
|---|---|---|
|CANdy Production|[Rental Property Business Licence](https://candyscan.digitaltrust.gov.bc.ca/tx/CANDY_PROD/domain/4574) | <code>R12pguaP3VF2WiE6vAsiPF:2:Rental Property Business Licence:1.0</code>|
|CANdy Test|[Rental Property Business Licence](https://candyscan.digitaltrust.gov.bc.ca/tx/CANDY_TEST/domain/921) | <code>ARK5s3QZtjL5X65mLoubdk:2:Rental Property Business Licence:1.0</code>|
|CANdy Dev|[Rental Property Business Licence](https://candyscan.digitaltrust.gov.bc.ca/tx/CANDY_DEV/domain/38195) | <code>YWnESLB4SH275SMNvaJJ1L:2:Rental Property Business Licence:1.0</code>|

### 5.4 Credential Implementation
|Environment|Ledger|Credential Definition ID|OCA Bundle|
|---|---|---|---|
|CANdy Production|[Rental Property Business Licence](https://candyscan.digitaltrust.gov.bc.ca/tx/CANDY_PROD/domain/4575)|<code>R12pguaP3VF2WiE6vAsiPF:3:CL:921:Rental Property Business Licence</code>|[prod-property-rental-business-licence](https://github.com/bcgov/aries-oca-bundles/tree/main/OCABundles/schema/CityOfVancouver/prod-property-rental-business-licence)|
|CANdy Test|[Rental Property Business Licence](https://candyscan.digitaltrust.gov.bc.ca/tx/CANDY_TEST/domain/922)|<code>ARK5s3QZtjL5X65mLoubdk:3:CL:921:Rental Property Business Licence</code>|[test-property-rental-business-licence](https://github.com/bcgov/aries-oca-bundles/tree/main/OCABundles/schema/CityOfVancouver/test-property-rental-business-licence)|
|CANdy Dev|[Rental Property Business Licence](https://candyscan.digitaltrust.gov.bc.ca/tx/CANDY_DEV/domain/38196)|<code>YWnESLB4SH275SMNvaJJ1L:3:CL:38195:Rental Property Business </code>|[dev-property-rental-business-licence](https://github.com/bcgov/aries-oca-bundles/tree/main/OCABundles/schema/CityOfVancouver/dev-property-rental-business-licence)|
