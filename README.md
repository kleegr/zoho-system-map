# Zoho System Map

This repository is an **automatically synced snapshot** of the Zoho CRM configuration for Kleegr, plus manually-curated companion data for things the API can't reach.

It is designed to be read by AI assistants (ChatGPT, Claude, etc.) to understand the full Zoho CRM system structure.

---

## Repository Structure

```
zoho-system-map/
  scripts/pull_zoho.py           # Python script that pulls all Zoho CRM metadata
  zoho_exports/                  # Auto-updated daily via GitHub Actions
    modules/
      modules_summary.json       # CURATED - AI-friendly module overview
      modules_raw.json           # AUTO - raw API output (first sync run)
      fields_<Module>_summary.json   # CURATED per module
      fields_<Module>_raw.json       # AUTO per module
      layouts_<Module>_raw.json      # AUTO per module
    workflows/
      workflow_rules_summary.json    # CURATED summary of all rules
      workflow_actions_note.json     # CURATED notes on what each rule does
      workflow_rules_raw.json        # AUTO list of all rules
      workflow_rule_details_raw.json # AUTO per-rule criteria + actions
      field_updates_raw.json         # AUTO workflow field-update actions (NEW)
      email_notifications_raw.json   # AUTO workflow email-notification actions (NEW)
    webhooks/                    # AUTO webhooks_raw.json + curated note
    variables/                   # AUTO variables_raw.json + curated note
    custom_links/                # AUTO custom_links_raw.json
    users/                       # AUTO users_raw.json + org_info_raw.json
    integrations/
      retell_pipedream_references.json   # CURATED Retell/Pipedream/Twilio cross-ref
    api_limitations.md           # What the Zoho API cannot expose
  manual_exports/                # Must be exported manually (API not available)
    functions/                   # Deluge function source code
    schedules/                   # Scheduled function configurations
    custom_buttons/              # Custom button definitions
    widgets/                     # Widget configurations
  external_code/                 # External code referenced by the Zoho system
    node_ivr_flows/              # Node.js / Twilio IVR flow source (per agency)
  .github/workflows/sync-zoho.yml  # GitHub Action for daily sync
```

### Naming convention

- `*_summary.json` - **curated** hand-edited overview files designed for AI consumption. Stable across syncs.
- `*_raw.json` - **auto-generated** raw output from the Zoho REST API. Overwritten on each sync run.
- `*_note.json` / `*_note.md` - small files noting an API limitation or context.

---

## Auto-Sync (GitHub Actions)

The sync runs **daily at 02:00 UTC** and can also be triggered manually from the Actions tab.

It executes `scripts/pull_zoho.py`, which:
1. Authenticates with Zoho using a refresh token
2. Pulls all available CRM metadata via the Zoho CRM REST API v7
3. Writes JSON files into `zoho_exports/` (using the `*_raw.json` naming)
4. Commits and pushes any changed files back to `main`

### Required GitHub Secrets

Set these in **Settings -> Secrets and variables -> Actions**:

| Secret | Description |
|---|---|
| `ZOHO_CLIENT_ID` | OAuth2 Client ID from Zoho API Console |
| `ZOHO_CLIENT_SECRET` | OAuth2 Client Secret |
| `ZOHO_REFRESH_TOKEN` | Long-lived refresh token |
| `ZOHO_ACCOUNTS_DOMAIN` | e.g. `https://accounts.zoho.com` |
| `ZOHO_API_DOMAIN` | e.g. `https://www.zohoapis.com` |

Refresh token scopes required: `ZohoCRM.settings.READ`, `ZohoCRM.settings.modules.READ`, `ZohoCRM.settings.fields.READ`, `ZohoCRM.settings.workflows.READ`, `ZohoCRM.settings.variables.READ`, `ZohoCRM.settings.automation.READ`, `ZohoCRM.users.READ`.

---

## Manual Exports (`manual_exports/`)

Items that cannot be retrieved via the API. See `manual_exports/MANUAL_CHECKLIST.md` for the priority list (Deluge function source code is the highest priority).

## External Code (`external_code/`)

Code that lives outside Zoho but is referenced by Zoho automations. `external_code/node_ivr_flows/` holds the Node.js / Twilio IVR flow logic per agency (Yedei Chesed, Rayim, HHA Hamaspik, Dragon, Ahivim) extracted from `XcellentStaffing Flows (Node.js).pdf`.

---

## How to Use with AI

Point ChatGPT or Claude at this repo (via GitHub MCP or file upload) and ask things like:
- *"What modules exist in this Zoho CRM?"*
- *"List all workflow rules and what they trigger"*
- *"What custom fields exist on Phone_Calls?"*
- *"How does an IVR call flow from Service_Schedules to a completed Phone_Call?"*

## Last Sync

See `zoho_exports/sync_meta.json` (created after first successful sync) or the latest commit timestamp.
