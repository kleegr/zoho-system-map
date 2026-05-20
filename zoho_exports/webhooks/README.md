# Zoho CRM Webhooks Export

## Summary

No standalone webhook objects were found via the Zoho API (`GET /settings/automation/webhooks`).

## How Webhooks Work in This Org

Webhooks in this org are configured as **actions inside workflow rules**, not as independent objects. When a workflow rule fires (e.g., TriggerPipeDreamIVR), it executes a webhook action that calls an external URL.

## Known Integration Endpoints (inferred from field names)

- **Pipedream** — receives Phone_Call records, triggers IVR via Retell. Trace IDs stored in `Pipedream_Trigger_Ivr_Trace_Id` and `Pipedream_Update_Zoho_Crm_Trace_Id`.
- **Retell AI** — makes outbound IVR calls for clock-in/out verification. Workflow rules: TriggerRettelIVR (active, created Sep 2025), TriggerPipedreamCallForTriggerIvr (inactive, superseded).
- **Twilio (legacy)** — Phone_Calls module has `Link_for_Twilio` and `Recording_from_Twilio` fields, but the Twilio workflow rule (TriggerPipedreamCallForTriggerIvr) is now inactive.

## Last Synced
2026-05-20
