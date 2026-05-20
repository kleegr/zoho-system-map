# Zoho CRM Variables

## API Limitation

CRM Variables **cannot be listed or retrieved** via the Zoho CRM REST API. There is no `GET /settings/variables` endpoint.

Variables are only accessible inside Deluge code via:
- `zoho.crm.getOrgVariable("variable_name")` — org-level
- `zoho.crm.getUserVariable("variable_name")` — user-level

## Known Usage Context

Based on the architecture, variables in this org likely store:
- Pipedream webhook endpoint URLs
- Retell AI API key or agent IDs
- Internal flags or shared counters

To view variables: **Setup > Developer Space > CRM Variables** in the Zoho CRM UI.

## Last Synced
2026-05-20
