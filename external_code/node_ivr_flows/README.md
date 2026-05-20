# external_code/node_ivr_flows/

This folder holds the Node.js/Twilio IVR flow logic extracted from the XcellentStaffing system.

## Status

**PDF not yet uploaded.** The source document (`XcellentStaffing Flows (Node.js).pdf`) was requested but did not arrive in the upload.
Once uploaded, this folder will be populated with:

| File | Agency |
|---|---|
| `yedei_chesed.js` | Yedei Chesed |
| `rayim.js` | Rayim |
| `hha_hamaspik.js` | HHA Hamaspik |
| `dragon.js` | Dragon |
| `ahivim.js` | Ahivim |
| `cross_reference.md` | Full cross-reference of IVR variables against Zoho fields |

## Cross-Reference Targets (once PDF arrives)

When the PDF is processed, each agency flow will be mapped against:

### Phone_Calls fields
- `Status` (Scheduled / In Progress / Done / Failed / Failed / Retried / Review / Busy)
- `Type` (Clock In / Clock Out)
- `Phone_Call_Response` — IVR response payload destination
- `Call_Count` — retry counter
- `Child_Phone_Call_Id` — retry chain link
- `Pipedream_Trigger_Ivr_Trace_Id` / `Pipedream_Update_Zoho_Crm_Trace_Id`
- `test_rettell` / `Call_Summary` — Retell AI fields
- `Link_for_Twilio` / `Recording_from_Twilio` — Twilio legacy fields

### Service_Schedules fields
- `Next_Clock_In` / `Next_Clock_Out` — date triggers for IVR calls
- `Job_Pin` — PIN used during IVR authentication
- `Job_Code_Hash` — hashed job code
- `Program_IVR_Number` / `IVR_Agency_Number` — routing numbers
- `Provider_Pin` / `Provider_Code` (from Providers module) — provider authentication

### Integration references
- `ivr_call_status` — IVR internal status variable
- `crm_hints_object` — data passed from Zoho Accounts.IVR_Hints subform
- `current_employee_data` — provider/student record snapshot passed into IVR
- `CallSid` — Twilio call identifier
- `clock_in` / `clock_out` — IVR flow branch logic

### Retell/Pipedream references
- Any `retell.*` SDK calls, agent IDs, webhook URLs
- Any `pipedream` webhook URLs or trace ID writes
- Twilio `twiml` response builders

## Source Repository

The live Node.js IVR system is in `kleegr/excellent`:
- `src/controller/ivrFlows/` — per-agency playbooks
- `src/controller/ivrInteraction.js` — main IVR controller (35KB)
