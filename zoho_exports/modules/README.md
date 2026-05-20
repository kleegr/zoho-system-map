# Zoho CRM Module Exports

This directory contains exported metadata from Zoho CRM modules.

## Field Files

| File | Module | Display Name |
|---|---|---|
| `fields_Accounts.json` | Accounts | Employers |
| `fields_Contacts.json` | Contacts | Agencies |
| `fields_Deals.json` | Deals | Service Profiles |
| `fields_Providers.json` | Providers | Providers |
| `fields_Students.json` | Students | Students |
| `fields_Service_Schedules.json` | Service_Schedules | Service Schedules |
| `fields_Phone_Calls.json` | Phone_Calls | Phone Calls |
| `fields_Notes.json` | Notes | Notes |

## Known API Gaps
- `Calls` (Zoho standard) — `getFields` returns NO_PERMISSION
- `Tasks` (Zoho standard) — `getFields` returns NO_PERMISSION

## Key Module Mapping

| API Name | Display Label | Internal Name | ID |
|---|---|---|---|
| Accounts | Employers | Accounts | 6028870000000002177 |
| Contacts | Agencies | Contacts | 6028870000000002179 |
| Deals | Service Profiles | Deals | 6028870000000002181 |
| Providers | Providers | CustomModule1 | 6028870000000479816 |
| Students | Students | CustomModule7 | 6028870000001004010 |
| Service_Schedules | Service Schedules | CustomModule2 | 6028870000000489844 |
| Phone_Calls | Phone Calls | CustomModule5 | 6028870000000491812 |
| Programs | Programs | CustomModule4 | 6028870000000485575 |
| Absentees | Absentees | CustomModule6 | 6028870000000493647 |
| Phone_Numbers | Phone Numbers | CustomModule3 | 6028870000001831032 |
| Students_X_Service_S | Students X Service S | LinkingModule1 | 6028870000001010179 |
| Agencies_X_Employers | Agencies X Employers | LinkingModule4 | 6028870000001014328 |
| IVR_Configs | IVR Configs | LinkingModule2 (subform of Programs) | 6028870000000486630 |
| Service_IVR_Configs | Service IVR Configs | LinkingModule3 (subform of Deals) | 6028870000000487552 |
| IVR_Hints | IVR Hints | LinkingModule5 (subform of Accounts) | 6028870000005950252 |

## Sync Info

Last synced: 2026-05-20
