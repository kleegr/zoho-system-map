# manual_exports/widgets/

## ⚠️ Manual Export Required

Zoho CRM **widget configurations are not available via the REST API**.
This folder must be populated manually.

## What belongs here

Widget definitions from **Zoho CRM → Setup → Developer Space → Widgets**.

## How to export

1. Go to **Zoho CRM → Setup → Developer Space → Widgets**
2. For each widget, note:
   - Widget name
   - Type (detail page, list page, home page, etc.)
   - Host URL or source
   - Which modules it appears in
   - Any configuration parameters
3. Create `all_widgets.json` in this folder

## Suggested format (`all_widgets.json`)

```json
[
  {
    "name": "Deal Health Dashboard",
    "type": "detail_page_widget",
    "module": "Deals",
    "hosted_at": "https://widgets.example.com/deal-health",
    "active": true
  }
]
```

## How to use with AI

Once populated, ask: *"What widgets are configured and where do they appear?"*
