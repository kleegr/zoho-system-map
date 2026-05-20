# Zoho CRM Integrations

This directory contains references to external integrations found in field metadata and automation rules.

## retell_pipedream_references.json

All discovered Retell and Pipedream touchpoints:

### Retell IVR
- `test_rettell` boolean field on both **Phone_Calls** and **Service_Schedules** (created Sep 2025)
- Active workflow: **TriggerRettelIVR** (Phone_Calls, create_or_edit)
- Active workflow: **AI - Handle Failed/Retry Phone Calls** (Phone_Calls, Status field_update)

### Pipedream
- `Pipedream_Update_Zoho_Crm_Trace_Id` — written by Pipedream when updating a Phone Call
- `Pipedream_Trigger_Ivr_Trace_Id` — set when Pipedream triggers IVR  
- Active workflow: **TriggerPipeDreamIVR** (Phone_Calls, create_or_edit)

### IVR Call Flow
```
Service_Schedules.Next_Clock_In/Next_Clock_Out (datetime fields)
  → Date-based workflows fire
  → Phone_Call record created
  → TriggerPipeDreamIVR + TriggerRettelIVR fire on create
  → Pipedream/Retell process the call
  → Phone_Call_Response + Status updated back
  → Failed Phone Call Notifications / AI retry rules fire
```
