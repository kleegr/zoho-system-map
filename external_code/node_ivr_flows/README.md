# external_code/node_ivr_flows/

This folder will hold the Node.js / Twilio IVR flow logic extracted from the source document **`XcellentStaffing Flows (Node.js).pdf`**.

## Expected agencies (per discovery)

- Yedei Chesed
- Rayim
- HHA Hamaspik
- Dragon
- Ahivim

## Status

⏳ Awaiting PDF source upload. Once the PDF is added to the repo, each agency flow should be extracted into its own file:

```
external_code/node_ivr_flows/
  source.pdf                     # original document
  yedei_chesed.js                # per-agency extracted flow
  rayim.js
  hha_hamaspik.js
  dragon.js
  ahivim.js
  cross_reference.md             # mapping to Zoho fields (Phone_Calls, Service_Schedules, etc.)
```

## Cross-reference targets (Zoho side)

When the flows are extracted, cross-reference each against:

- `Phone_Calls` module fields (especially `Status`, `Phone_Call_Response`, `Call_Count`, `Type`, `Pipedream_*_Trace_Id`, `test_rettell`, `Call_Summary`)
- `Service_Schedules` fields (`Next_Clock_In`, `Next_Clock_Out`, `Job_Pin`, `Job_Code_Hash`, `Program_IVR_Number`, `IVR_Agency_Number`)
- Retell / Pipedream / Twilio references documented in `zoho_exports/integrations/retell_pipedream_references.json`
- Concepts referenced in source code: `ivr_call_status`, `crm_hints_object`, `current_employee_data`, `CallSid`, `clock_in` / `clock_out` logic

Also compare against the IVR flow files already in `github.com/kleegr/excellent/src/controller/ivrFlows/` (ahivim, hamspik3, hhaHamaspik, ppl, rayim, yedei) and the mega-controller at `src/controller/ivrInteraction.js`.
