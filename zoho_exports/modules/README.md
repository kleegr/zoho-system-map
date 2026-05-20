# Zoho CRM Module Exports

This directory contains exported metadata from Zoho CRM modules.

## Files

- `modules.json` — All modules with API names, labels, IDs, and visibility
- `fields_Accounts.json` — Field metadata for Accounts (Employers)
- Additional field files added on subsequent syncs

## Key Module Mapping

| API Name | Display Label | Type |
|---|---|---|
| Accounts | Employers | Standard |
| Contacts | Agencies | Standard |
| Deals | Service Profiles | Standard |
| Providers | Providers | Custom (CustomModule1) |
| Students | Students | Custom (CustomModule7) |
| Service_Schedules | Service Schedules | Custom (CustomModule2) |
| Phone_Calls | Phone Calls | Custom (CustomModule5) |
| Programs | Programs | Custom (CustomModule4) |
| Absentees | Absentees | Custom (CustomModule6) |
| Phone_Numbers | Phone Numbers | Custom (CustomModule3) |
| Students_X_Service_S | Students X Service S | Linking |
| Agencies_X_Employers | Agencies X Employers | Linking |
| IVR_Configs | IVR Configs | Subform of Programs |
| Service_IVR_Configs | Service IVR Configs | Subform of Deals |
| IVR_Hints | IVR Hints | Subform of Accounts |

## Sync Info

Last synced: 2026-05-20
