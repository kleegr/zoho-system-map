# Manual Export Checklist — UI-Only Items

Scope: Phone Calls, Service Schedules, Pipedream, Retell, and IVR logic only.
Items that the Zoho REST API cannot return; must be captured manually.

---

## 1 — Deluge Function Source Code

**Path:** Setup → Developer Space → Functions

Open each function below. Tap the function name to open the editor. Copy the full Deluge source and paste it into `manual_exports/functions/<function_name>.deluge`.

### Priority functions (IVR / Phone Call / Service Schedule pipeline)

| # | Function name to look for | Why it matters |
|---|---|---|
| 1 | Any function named like `TriggerIVR`, `TriggerRetell`, `TriggerPipedream`, or similar | Called by TriggerPipeDreamIVR or TriggerRettelIVR workflow rule |
| 2 | Any function named like `HandleFailedCall`, `RetryPhoneCall`, or similar | Called by "AI - Handle Failed/Retry Phone Calls" rule |
| 3 | Any function named like `GenerateJobPin`, `PopulateJobPin`, or similar | Called by "S.Schedules.Created. Generate Job Pin" rule |
| 4 | Any function named like `PopulateNextCallTime`, `ScheduleClockIn`, or similar | Called by "S.Schedules.Created. Populate Next Call Time" rule |
| 5 | Any function named like `UpdateRelatedSchedules`, `SyncProfileToSchedule`, or similar | Called by "S. Profile. Update related SS" rule |
| 6 | Any function named like `SendNotification`, `FailedCallNotify`, or similar | Called by "Failed Phone Call Notifications" rule |
| 7 | Any function named like `UpdateAgency`, `SyncAgency`, or similar | Called by "Update Agency" (Phone_Calls) rule |

**How to copy:** Open function → select all code (Cmd+A / Ctrl+A) → copy → paste into file.

---

## 2 — Workflow Rule Actions

**Path:** Setup → Automation → Workflow Rules

The API returns rule names and triggers but NOT the actions. For each rule below, open it and note what actions are configured (function name, webhook URL, field update values, email template).

### Priority rules

| # | Rule name | Module | What to capture |
|---|---|---|---|
| 1 | **TriggerRettelIVR** | Phone Calls | Action type (function/webhook), function name or URL called, any conditions |
| 2 | **TriggerPipeDreamIVR** | Phone Calls | Same — note this is still active, check if it overlaps with Retell |
| 3 | **AI - Handle Failed/Retry Phone Calls** | Phone Calls | Action type, function/webhook name, Status field criteria |
| 4 | **Failed Phone Call Notifications** | Phone Calls | Action type (email/function), recipient, template or function name |
| 5 | **Update to Failed and Retried** | Phone Calls | Field update values: which fields get set to what values |
| 6 | **Update Last Response Field** | Phone Calls | Field update: which field, what value or formula |
| 7 | **S.Schedules.Daily Clock In Call** | Service Schedules | Action type, function or webhook called |
| 8 | **S.Schedules.Daily Clock Out Call** | Service Schedules | Action type, function or webhook called |
| 9 | **S.Schedules.Created. Generate Job Pin** | Service Schedules | Action type, function name |
| 10 | **S.Schedules.Created. Populate Next Call Time** | Service Schedules | Action type, function name |
| 11 | **S.Schedules.Updated. Generate Job Pin** | Service Schedules | Action type, function name |
| 12 | **S.Schedules.Updated. Populate Next Call Time** | Service Schedules | Action type, function name |

**Format to save:** One file per rule in `manual_exports/workflow_actions/<rule_name>.md`

Template per rule:
```
Rule: TriggerRettelIVR
Module: Phone_Calls
Trigger: create_or_edit
Criteria: (copy from UI)
Actions:
  1. Type: function | webhook | field_update | email
     Name/URL: <value>
     Details: <any params or field mappings>
```

---

## 3 — Scheduled Functions

**Path:** Setup → Developer Space → Functions → (filter by "Scheduled")

Or: Setup → Developer Space → Schedules

List every scheduled function. For each one capture:

| Field | What to note |
|---|---|
| Function name | |
| Schedule (cron / interval) | e.g. "Every day at 2 AM" |
| What it does | read from code or description |
| Active/inactive | |

**Save to:** `manual_exports/schedules/scheduled_functions.md`

### What to look for (IVR-related)
- Any schedule that creates or resets `Next_Clock_In` / `Next_Clock_Out` on Service Schedules records
- Any schedule that retries Failed phone calls
- Any schedule that syncs data to/from Pipedream or Retell

---

## 4 — Custom Buttons and Links

**Path:** Setup → Customization → Modules and Fields → [select module] → Links and Buttons

Check these modules in order:

| Module | Why |
|---|---|
| **Phone Calls** | May have a "Retry Call" or "Trigger IVR" button |
| **Service Schedules** | May have a "Create Phone Call" or "Force Clock In" button |
| **Accounts (Employers)** | May have a "View Schedule" or "IVR Config" button |

For each button/link found, capture:
- Name
- Type (button vs link)
- Location (list view / detail view / both)
- Action: opens URL / runs function / runs workflow
- URL or function name if applicable

**Save to:** `manual_exports/custom_buttons/<module_name>_buttons.md`

---

## 5 — Schedules Manager Widget Source

**Path (in Zoho):** Setup → Developer Space → Widgets

Find the widget named **"WebTab. Service Schedules"** (module: `Schedules_Manager`, ID `6028870000002367011`).

**What to capture:**
1. Widget name, version, deployment URL
2. If you have the Zoho CLI installed locally — run `zoho extension pull` to download source files
3. If not: screenshot the widget configuration page showing the deployment URL and settings

The deployment URL is already known:
```
https://82b8dcde-48ce-431e-843b-0e5d73e2c195.zappsusercontent.com/appfiles/v2/82b8dcde-48ce-431e-843b-0e5d73e2c195/1.0/...
```

**To get source code without CLI:**
1. Open the widget URL in a browser
2. View source (Cmd+U / Ctrl+U)
3. Copy the HTML/JS and save to `manual_exports/widgets/schedules_manager/index.html`

Note: the bundle JS may be minified. The original source is only in the developer's local project folder or version control.

**Save to:** `manual_exports/widgets/schedules_manager/`

---

## Completion Tracker

- [ ] Function: TriggerIVR / TriggerRetell equivalent
- [ ] Function: HandleFailedCall equivalent
- [ ] Function: GenerateJobPin equivalent
- [ ] Function: PopulateNextCallTime equivalent
- [ ] Function: UpdateRelatedSchedules equivalent
- [ ] Workflow actions: TriggerRettelIVR
- [ ] Workflow actions: TriggerPipeDreamIVR
- [ ] Workflow actions: AI - Handle Failed/Retry Phone Calls
- [ ] Workflow actions: S.Schedules.Daily Clock In Call
- [ ] Workflow actions: S.Schedules.Daily Clock Out Call
- [ ] Workflow actions: S.Schedules.Created rules (x2)
- [ ] Workflow actions: Failed Phone Call Notifications
- [ ] Scheduled functions list
- [ ] Custom buttons: Phone Calls module
- [ ] Custom buttons: Service Schedules module
- [ ] Widget: Schedules Manager source or screenshot

---

*Last updated: 2026-05-20. Items added by AI sync from Zoho MCP.*
