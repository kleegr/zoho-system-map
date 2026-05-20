# manual_exports/schedules/

## ⚠️ Manual Export Required

Zoho CRM **scheduled functions are not available via the REST API**.
This folder must be populated manually.

## What belongs here

Scheduled function configurations from **Zoho CRM → Setup → Developer Space → Scheduled Functions** (or **Automation → Schedules**).

## How to export

1. Go to **Zoho CRM → Setup → Automation → Schedules**
2. For each schedule, note:
   - Schedule name
   - Which Deluge function it calls
   - Frequency / cron expression
   - Active or inactive
   - Any parameters passed
3. Create a JSON file `all_schedules.json` in this folder with that information

## Suggested format (`all_schedules.json`)

```json
[
  {
    "name": "Daily Lead Score Refresh",
    "function": "refreshLeadScores",
    "frequency": "Daily at 06:00",
    "active": true,
    "notes": ""
  }
]
```

## How to use with AI

Once populated, ask: *"What scheduled functions are running and how often?"*
