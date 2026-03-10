# Land Title and Survey Authority of British Columbia – Property Owner Credential Documentation

## 1 About this Document

This document describes the Land Title and Survey Authority of British Columbia’s (**LTSA**’s) use of the Property Owner Credential to help potential verifiers determine whether it is suitable for their needs. The intended audience includes policy analysts, privacy specialists, solution architects, developers, and data architects.

### 1.1 Version History

| Ver.      | Date        | Notes                |
| --------- | ----------- | -------------------- |
| 1.0       |2026-03-09   | Initial Version      |


## 2 Credential Overview

The Property Owner Credential is a secure digital credential issued to property owners registered in BC’s Land Title Register. The credential enables the holder to prove property ownership to third-party verifiers.

At this time, only individuals who hold fee simple ownership can receive a Property Owner Credential. Interests held by corporations or other legal entities, and other ownership types (e.g. lessees, mortgage holders) are not eligible. 

Effective April 16, 2026, eligible registered property owners can hold and use their credential in an approved digital wallet application.

- **Credential**: Property Owner Credential
- **Schema**: Property owner
- **Issuer:**
	- **Name**: Land Title and Survey Authority of British Columbia
	- **Description**: LTSA is a statutory corporation responsible for operating the land title and survey systems of BC.
	- **Website**: [https://www.ltsa.ca](https://www.ltsa.ca) 
	- **Contact info**: LTSA Customer Support, [bcpropertyconnect@ltsa.ca](mailto:bcpropertyconnect@ltsa.ca) 

## 3 Governance & Legal

### 3.1 Governing Authority & Administrative Authority

The LTSA, established under the [Land Title and Survey Authority Act](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/04066_01), is the governing body with authority to issue and revoke the credential.

### 3.2 Legal

#### 3.2.1 For Verifiers

The Property Owner Credential is provided on an "as-is", "as available" basis and LTSA makes no representations about or warranties regarding its accuracy or fitness for any particular purpose. Holders are responsible for their use of the Property Owner Credential in accordance with LTSA’s Terms of Use, and verifiers use the credential at their own discretion. LTSA is not responsible or liable for any loss, damage or claim arising from the use or reliance on the Property Owner Credential by holders, verifiers, or other parties.

The credential is intended to be used, both alone or alongside other credentials (e.g., BC Person Credential), as a trusted source to prove ownership for public sector verifiers such as municipalities and other government agencies.

#### 3.2.2 For End Users

The Terms of Use for this credential as it relates to End Users can be found here:  [Appendix E | System Help](https://help.ltsa.ca/appendix-e)

## 4 Credential Data, Issuance and Changes

### 4.1 Data Source(s)

The BC Land Title Register. LTSA maintains the BC Land Title Register in accordance with requirements in the *Land Title Act.* The register represents current information about registered title ownership.

#### 4.1.1 Data Updates

The Property Owner Credential accesses information in the Land Title Register on an ongoing basis to confirm property ownership. 

### 4.2 Issuance

To obtain a Property Owner Credential, property owner identity is confirmed using the BC Services Card and LTSA systems verify ownership through a search of the Land Title Register.  

If a reliable match is found, the property owner reviews and accepts LTSA’s [Terms of Use](https://help.ltsa.ca/appendix-e) and the Property Owner Credential is issued to an approved digital wallet using the account details of the logged-in user. In a small number of cases, LTSA may complete the verification manually.  Once a credential has been issued, the LTSA portal provides a means for connecting the property owner with their digital wallet using a QR scan process. 

### 4.3 Revocation

A Property Owner Credential will be automatically revoked in the following cases:

1. If property ownership changes, such as through sale or transfer. 
2. If the holder’s verified identity information changes. On confirmation property ownership has not changed, the individual can download a new Credential.

LTSA may revoke a credential if it becomes aware of any real or suspected violation of the [Terms of Use](https://help.ltsa.ca/appendix-e) of the Property Owner Credential.

A Property Owner Credential will be revoked and automatically re-issued in the following cases:

1. If any of the credential attribute values changes.

## 5 Credential Definition

### 5.1 Subject

The subject of the Property Owner Credential is the verified registered owner of a property as recorded in the BC Land Title Register. Verification includes confirming the individual’s identity through the [Person Credential](https://developer.gov.bc.ca/docs/default/component/digital-trust/governance/person/person-cred-doc/) and their digital BC Services Card, and verifying current property ownership by searching the Land Title Register. 

### 5.2 Attributes

| **Display Name** | **Attribute**   | **Description**                                                |   **Format**   | **Rules & Notes**               | **Examples**          |
|------------------|-----------------|----------------------------------------------------------------|----------------| --------------------------------|-----------------------|
| PID              | pid             |   A nine-digit number that uniquely identifies a parcel in the land title register of British Columbia. The registrar assigns PID numbers to parcels for which a title is being entered in the computer register as a registered title.                                                             |     String     | Format: ###-###-### (three groups of three digits separated by dashes)"                          |    012-345-678        | 
| Property Address | PropertyAddress |  Typically the Civic address of the property or user entered address information at the time a credential is issued                                                              |     String     |        Mandatory                |   Unit 305 – 1234 Main Street, Vancouver, BC                 |


  


## 6 Implementations

### 6.1 Technical Format

The credential uses the [Hyperledger AnonCreds](https://hyperledger.github.io/anoncreds-spec/) specification and the property-owner schema which has the attributes set out in this section.

### 6.2 Issuer List


| **Environment** | **Issuer Name**                        | **Issuer DID**                                                |  
|-----------------|----------------------------------------|---------------------------------------------------------------|
| CANdy Dev       | Land Title and Survey Authority of BC  | KKSXjEHUPVNGYHuof1J3xy                                        |
| CANdy Test      | Land Title and Survey Authority of BC  | TBC                                                           |   
| CANdy Prod      | Land Title and Survey Authority of BC  | TBC                                                           |    




### 6.3 Schema


| **Environment** | **Ledger**                             | **Schema ID**                                                 |  
|-----------------|----------------------------------------|---------------------------------------------------------------|
| CANdy Dev       |  https://candyscan.idlab.org/tx/CANDY_DEV/domain/35671                                      | KKSXjEHUPVNGYHuof1J3xy:2:property-owner:1.1.0                 |
| CANdy Test      | TBC  | TBC                                    |
| CANdy Prod      | TBC                                    | TBC                                                           |    



### 6.4 Credential


| **Environment** | **Ledger**                             | **Credential Definition ID**                                  |  **OCA Bundle**                  |
|-----------------|----------------------------------------|---------------------------------------------------------------|----------------------------------|
| CANdy Dev       | https://candyscan.idlab.org/tx/CANDY_DEV/domain/35671  | KKSXjEHUPVNGYHuof1J3xy:3:CL:39372:property-owner                                    |    TBC                              |
| CANdy Test      | TBC  								   | TBC                                    |    TBC                              |
| CANdy Prod      | TBC                                    | TBC                                    |    TBC                              |







