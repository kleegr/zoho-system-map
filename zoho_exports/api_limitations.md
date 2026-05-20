# Zoho API Limitations — What Cannot Be Exported

This document records what the Zoho CRM API **cannot** pull as of 2026-05-20.

---

## 1. Deluge Function Source Code

**Status: NOT AVAILABLE via API**

The Zoho CRM API can list functions (name, ID, module via `Functions__s` module records) but **cannot return the actual Deluge source code**. The `GET /settings/functions/{id}` endpoint returns metadata only. The source code lives exclusively in the Deluge editor UI and is not exposed over the API.

*Workaround*: Must be manually exported from `Setup > Automation > Functions` in the Zoho CRM web UI.

---

## 2. Scheduled Functions (Schedulers)

**Status: NOT AVAILABLE via API**

Zoho's scheduled functions (under `Setup > Automation > Schedules`) have no documented public API endpoint. The `Functions__s` module in the API only lists user-defined functions, not the schedule configurations that invoke them.

*Workaround*: Must be documented manually from the UI.

---

## 3. Custom Buttons / Custom Links

**Status: PARTIAL / NOT RELIABLY AVAILABLE**

The `getModules` tool includes a `custom_button` feature flag and custom buttons are theoretically accessible, but there is no direct `GET /settings/custom_links` or `GET /settings/custom_buttons` endpoint exposed via the connected MCP tools. The raw Zoho CRM v2/v3 API does have a `GET /settings/automation/actions` endpoint for some action types, but custom buttons are not part of the standard automation exports.

*Workaround*: Must be screenshotted/documented from `Setup > Customization > Modules > [Module] > Links and Buttons`.

---

## 4. Widget Source Code (Schedules Manager)

**Status: NOT AVAILABLE via API**

The org has a custom widget: **Schedules Manager** (`api_name: Schedules_Manager`, `module_name: WebTab1`) hosted at a Zapps URL (`82b8dcde-48ce-431e-843b-0e5d73e2c195.zappsusercontent.com`). The widget source (HTML/CSS/JS) is hosted in Zoho Cliq/Creator/Zapps and is **not retrievable** through the CRM API.

*Workaround*: Access the widget source via the Zoho Developer console or Zapps builder directly.

---

## 5. Workflow Rule Actions / Conditions (Full Detail)

**Status: PARTIALLY AVAILABLE**

The `GET /settings/automation/workflow_rules` (list) endpoint returns trigger type and basic metadata for all 31 rules but **does not include the conditions array or action details** (which functions/webhooks are triggered, what field updates are performed, etc.).

Getting full details requires one `GET /settings/automation/workflow_rules/{id}` call per rule (31 calls). The connected Workflow MCP only exposes an `updateWorkflowRuleById` tool (write), not a getById (read). The list tool (`getWorkflowRules`) returns summary only.

*What was exported*: Rule names, modules, trigger types, active/inactive status, last execution time.
*What is missing*: Per-rule conditions (criteria), instant_actions (which webhook/function IDs fire), scheduled_actions.

---

## 6. Webhooks List

**Status: NOT AVAILABLE via connected MCP tools**

The Workflow MCP exposes `createWebhooks`, `updateWebhooks`, and `getWebhookFailures` but **not a `getWebhooks` (list all) tool**. The underlying Zoho API endpoint `GET /settings/automation/webhooks` exists but is not exposed.

---

## 7. Variables

**Status: NOT AVAILABLE via connected MCP tools**

Zoho CRM variables (`Setup > Automation > Variables`) have a `GET /settings/variables` endpoint in the raw API but it is not exposed via the connected MCP tools.

---

## 8. Tasks / Calls Fields

**Status: NO_PERMISSION**

Calling `getFields` on the `Tasks` and `Calls` standard modules returns `{code: 'NO_PERMISSION', message: 'permission denied to access the module'}`. These are likely restricted system activity modules.

---

## Summary Table

| Item | API Available | MCP Tool Available | Notes |
|---|---|---|---|
| Module metadata | ✅ | ✅ | Exported |
| Field metadata (custom modules) | ✅ | ✅ | Exported |
| Field metadata (Tasks, Calls) | ⚠️ | ⚠️ | NO_PERMISSION |
| Workflow rule list | ✅ | ✅ | Exported (31 rules) |
| Workflow rule actions/conditions | ✅ | ❌ | No getById tool |
| Webhooks list | ✅ | ❌ | No get tool |
| Variables | ✅ | ❌ | No get tool |
| Custom buttons/links | ⚠️ | ❌ | No endpoint |
| Deluge function source | ❌ | ❌ | Not in API |
| Scheduled functions | ❌ | ❌ | Not in API |
| Widget source code | ❌ | ❌ | Not in API |
