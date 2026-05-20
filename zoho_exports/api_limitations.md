# Zoho API Limitations — What Cannot Be Exported

This document records what the Zoho CRM API **cannot** pull, as of 2026-05-20.

---

## 1. Deluge Function Source Code

**Status: NOT AVAILABLE via API**

The Zoho CRM API can list functions (name, ID, module) but **cannot return the actual Deluge source code**. The `GET /settings/functions/{id}` endpoint returns metadata only. Source lives exclusively in the Deluge editor UI.

*Workaround*: Manually export from `Setup > Automation > Functions`. See `manual_exports/functions/`.

---

## 2. Scheduled Functions (Schedulers)

**Status: NOT AVAILABLE via API**

No public API endpoint. Schedule configurations are only visible in `Setup > Automation > Schedules`.

*Workaround*: Document manually from the UI.

---

## 3. Custom Buttons

**Status: NOT RELIABLY AVAILABLE via API**

Custom links (`GET /settings/link_names`) are attempted by the sync script; custom **buttons** are a separate concept and not reliably exposed.

*Workaround*: Screenshot/document from `Setup > Customization > Modules > [Module] > Links and Buttons`.

---

## 4. Widget Source Code (Schedules Manager)

**Status: NOT AVAILABLE via API**

The org has a custom widget: **Schedules Manager** (`api_name: Schedules_Manager`, `module_name: WebTab1`) hosted at `82b8dcde-48ce-431e-843b-0e5d73e2c195.zappsusercontent.com`. Source is not retrievable through the CRM API.

*Workaround*: Access source via the Zoho Developer console or Zapps builder directly.

---

## 5. Workflow Rule Actions/Conditions (Full Detail)

**Status: PARTIALLY AVAILABLE — will be complete after first successful sync**

The list endpoint (`GET /settings/automation/workflow_rules`) returns trigger type and basic metadata only. However, the per-rule detail endpoint `GET /settings/automation/workflow_rules/{id}` **does** return criteria and actions (instant_actions, scheduled_actions) — including which function/webhook IDs fire.

The sync script loops over all 31 rule IDs and calls the detail endpoint for each. Once the GitHub Action runs successfully, `workflows/workflow_rule_details_raw.json` will contain the full wiring.

---

## 6. Tasks / Calls Field Metadata

**Status: NO_PERMISSION**

Calling `getFields` on the `Tasks` and `Calls` standard activity modules returns `{code: 'NO_PERMISSION', message: 'permission denied to access the module'}`. These are system-restricted modules.

---

## Summary Table

| Item | API Available | Script Pulls It | Notes |
|---|---|---|---|
| Module metadata | ✅ | ✅ | `modules_raw.json` on first sync |
| Field metadata (custom modules) | ✅ | ✅ | `fields_{Name}_raw.json` on first sync |
| Field metadata (Tasks, Calls) | ⚠️ | ⚠️ | NO_PERMISSION |
| Layouts per module | ✅ | ✅ | `layouts_{Name}_raw.json` on first sync |
| Workflow rule list | ✅ | ✅ | `workflow_rules_raw.json` on first sync |
| Workflow rule details (actions+criteria) | ✅ | ✅ | `workflow_rule_details_raw.json` on first sync |
| Field update actions | ✅ | ✅ | `field_updates_raw.json` on first sync |
| Email notification actions | ✅ | ✅ | `email_notifications_raw.json` on first sync |
| Webhooks list | ✅ | ✅ | `webhooks_raw.json` on first sync (likely empty — none defined standalone in this org) |
| CRM Variables | ✅ | ✅ | `variables_raw.json` on first sync |
| Custom links | ✅ | ✅ | `custom_links_raw.json` on first sync |
| Users + org info | ✅ | ✅ | `users_raw.json`, `org_info_raw.json` on first sync |
| Custom buttons | ⚠️ | ❌ | Separate concept, no reliable endpoint |
| Deluge function source | ❌ | ❌ | Not in API — manual export required |
| Scheduled functions | ❌ | ❌ | Not in API — manual export required |
| Widget source code | ❌ | ❌ | Not in API — manual export required |
| Blueprints, Approvals, Blueprints | ❌ | ❌ | Not exposed via standard API |
