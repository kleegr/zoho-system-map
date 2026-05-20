# Zoho System Map

This repository is an **automatically synced snapshot** of the Zoho CRM configuration for Kleegr.

It is designed to be read by AI assistants (ChatGPT, Claude, etc.) to understand the full Zoho CRM system structure.

---

## 📁 Repository Structure

```
zoho-system-map/
  scripts/pull_zoho.py          # Python script that pulls all Zoho CRM metadata
  zoho_exports/                 # Auto-updated daily via GitHub Actions
    modules/                    # All CRM module metadata
    workflows/                  # Workflow rule lists + details
    webhooks/                   # Webhook definitions
    custom_links/               # Custom links per module
    variables/                  # CRM variables
    users/                      # Users and org info
  manual_exports/               # Must be exported manually (API not available)
    functions/                  # Deluge functions source
    schedules/                  # Scheduled functions
    custom_buttons/             # Custom buttons
    widgets/                    # Widgets
  .github/workflows/sync-zoho.yml  # GitHub Action for daily sync
```

---

## 🤖 Auto-Sync (GitHub Actions)

The sync runs **daily at 02:00 UTC** and can also be triggered manually from the Actions tab.

It executes `scripts/pull_zoho.py`, which:
1. Authenticates with Zoho using a refresh token
2. Pulls all available CRM metadata via the Zoho CRM API
3. Writes JSON files into `zoho_exports/`
4. Commits and pushes any changed files back to `main`

### Required GitHub Secrets

Set these in **Settings → Secrets and variables → Actions**:

| Secret | Description |
|---|---|
| `ZOHO_CLIENT_ID` | OAuth2 Client ID from Zoho API Console |
| `ZOHO_CLIENT_SECRET` | OAuth2 Client Secret |
| `ZOHO_REFRESH_TOKEN` | Long-lived refresh token |
| `ZOHO_ACCOUNTS_DOMAIN` | e.g. `https://accounts.zoho.com` |
| `ZOHO_API_DOMAIN` | e.g. `https://www.zohoapis.com` |

---

## ✋ Manual Exports (`manual_exports/`)

The following Zoho CRM items **cannot be retrieved via API** and must be manually exported:

| Folder | What to put here |
|---|---|
| `manual_exports/functions/` | Deluge function source code (copy from Zoho CRM → Setup → Functions) |
| `manual_exports/schedules/` | Scheduled function configurations |
| `manual_exports/custom_buttons/` | Custom button definitions |
| `manual_exports/widgets/` | Widget configurations |

Each folder contains a `README.md` with instructions.

---

## 🔍 How to Use with AI

Point ChatGPT or Claude at this repo (e.g. via GitHub MCP or file upload) and ask:
- *"What modules exist in this Zoho CRM?"*
- *"List all workflow rules and what they trigger"*
- *"What webhooks are configured and where do they point?"*
- *"What custom fields exist on the Leads module?"*

---

## 📅 Last Sync

See the latest commit timestamp or the `zoho_exports/sync_meta.json` file.
