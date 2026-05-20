# Zoho API Limitations - What Cannot Be Exported

This document records what the Zoho CRM API **cannot** pull as of 2026-05-20.

The limitations below are split into two groups:
- **Hard limits**: not retrievable by any API endpoint, must be manually exported.
- **MCP-tool limits (resolved)**: previously assumed unreachable due to limits of the connected MCP wrapper, but the underlying Zoho REST API does expose them. The script in `scripts/pull_zoho.py` calls these endpoints directly via the REST API and bypasses the MCP wrapper.

---

## HARD LIMITS (manual export required)

### 1. Deluge Function Source Code

**Status: NOT AVAILABLE via API.**

The Zoho CRM API can list functions (name, ID, module via `Functions__s` module records) but **cannot return the actual Deluge source code**. The source code lives exclusively in the Deluge editor UI and is not exposed over the API.

*Workaround*: Manually export from `Setup > Automation > Functions` in the Zoho CRM web UI, or use the Zoho Deluge VS Code plugin for bulk pull. Place under `manual_exports/functions/`.

### 2. Scheduled Functions (Schedulers)

**Status: NOT AVAILABLE via API.**

Zoho's scheduled functions (under `Setup > Automation > Schedules`) have no documented public API endpoint.

*Workaround*: Document manually under `manual_exports/schedules/`.

### 3. Custom Buttons

**Status: NOT AVAILABLE via API.**

Custom buttons are distinct from custom links (the latter ARE accessible via `/settings/link_names`). No public endpoint exposes custom buttons.

*Workaround*: Document from `Setup > Customization > Modules > [Module] > Links and Buttons`. Place under `manual_exports/custom_buttons/`.

### 4. Widget Source Code (Schedules Manager)

**Status: NOT AVAILABLE via API.**

The org has a custom widget: **Schedules Manager** (`api_name: Schedules_Manager`, `module_name: WebTab1`) hosted at a Zapps URL (`82b8dcde-48ce-431e-843b-0e5d73e2c195.zappsusercontent.com`). The widget source (HTML/CSS/JS) is hosted in Zoho Zapps and is **not retrievable** through the CRM API.

*Workaround*: Access via the Zoho Developer console / Zapps builder. Place under `manual_exports/widgets/`.

### 5. Tasks / Calls Fields

**Status: NO_PERMISSION.**

Calling `getFields` on the `Tasks` and `Calls` standard modules returns `{code: 'NO_PERMISSION', message: 'permission denied to access the module'}`. Workflow tasks for these modules return the same. This is an org-level permission setting, not an API limitation.

*Workaround*: Adjust profile permissions, or document field structure manually.

### 6. Blueprints / Approval Processes

**Status: NOT EXPOSED via standard v7 endpoints.**

The Zoho CRM API does not provide a clean endpoint to enumerate Blueprint state machines or Approval Process definitions.

*Workaround*: Document manually if used by the org.

---

## MCP-TOOL LIMITS (resolved via direct REST API in pull_zoho.py)

These were previously believed unreachable but are accessible via the v7 REST API endpoints the script calls directly:

### A. Workflow Rule Actions and Conditions (per-rule detail)

**API status: AVAILABLE.** The endpoint `GET /settings/automation/workflow_rules/{id}` returns the full rule including criteria, instant_actions, and scheduled_actions. The script loops over the 31 rule IDs and writes the output to `workflows/workflow_rule_details_raw.json`.

### B. Webhooks list

**API status: AVAILABLE.** `GET /settings/automation/webhooks` returns the webhooks list. The connected Workflow MCP tool returns an empty body for the org, consistent with the curated note that webhooks in this org are inline workflow actions rather than standalone webhooks. The script still calls the endpoint and writes the result to `webhooks/webhooks_raw.json`.

### C. CRM Variables

**API status: AVAILABLE.** `GET /settings/variables` returns CRM variables. The script writes them to `variables/variables_raw.json`.

### D. Field Updates (workflow actions)

**API status: AVAILABLE.** The MCP tool `ZohoCRM_getFieldUpdates` returns workflow field-update actions; for example, on `Phone_Calls` the org has at least two field updates (`Update to Failed and Retried` setting Status to `Failed / Retried`, and `Set Status to In Progress`). The script tries `/settings/automation/actions/field_updates`, `/settings/field_updates`, and `/settings/automation/actions` and writes to `workflows/field_updates_raw.json`.

### E. Email Notifications (workflow actions)

**API status: AVAILABLE.** Same shape as field updates. Script writes to `workflows/email_notifications_raw.json`.

### F. Custom Links

**API status: AVAILABLE.** `GET /settings/link_names?module={api_name}` returns per-module custom links. Script writes to `custom_links/custom_links_raw.json`.

---

## Summary Table

| Item | API Available | In sync script | Notes |
|---|---|---|---|
| Module metadata | YES | YES | `modules_raw.json` |
| Field metadata (custom modules) | YES | YES | `fields_<Module>_raw.json` |
| Field metadata (Tasks, Calls) | NO_PERMISSION | n/a | profile permission issue |
| Workflow rule list | YES | YES | `workflow_rules_raw.json` |
| Workflow rule actions/conditions | YES | YES | `workflow_rule_details_raw.json` |
| Field updates | YES | YES (NEW) | `field_updates_raw.json` |
| Email notifications | YES | YES (NEW) | `email_notifications_raw.json` |
| Webhooks list | YES | YES | `webhooks_raw.json` (often empty in this org) |
| Variables | YES | YES | `variables_raw.json` |
| Custom links | YES | YES | `custom_links_raw.json` |
| Custom buttons | NO | manual | Setup UI only |
| Deluge function source | NO | manual | `manual_exports/functions/` |
| Scheduled functions | NO | manual | `manual_exports/schedules/` |
| Widget source code | NO | manual | `manual_exports/widgets/` |
| Blueprints / Approval Processes | NO | manual | not standard endpoints |
