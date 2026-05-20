# manual_exports/custom_buttons/

## ⚠️ Manual Export Required

Zoho CRM **custom buttons are not available via the REST API**.
This folder must be populated manually.

## What belongs here

Custom button definitions from **Zoho CRM → Setup → Customization → Modules and Fields → [Module] → Links and Buttons**.

## How to export

1. For each module that has custom buttons, go to its **Links and Buttons** section
2. Note for each button:
   - Button name
   - Module it belongs to
   - Action type (open URL, run script, etc.)
   - Where it appears (list view, detail view, etc.)
   - The URL or Deluge script it triggers
3. Create `all_custom_buttons.json` in this folder

## Suggested format (`all_custom_buttons.json`)

```json
[
  {
    "name": "Send to Slack",
    "module": "Leads",
    "placement": "detail_view",
    "action_type": "deluge_script",
    "function": "sendLeadToSlack",
    "active": true
  }
]
```

## How to use with AI

Once populated, ask: *"What custom buttons exist on the Deals module?"*
