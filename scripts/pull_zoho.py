#!/usr/bin/env python3
"""
pull_zoho.py

Pulls Zoho CRM metadata via the REST API and writes JSON files
into zoho_exports/. Designed to run in GitHub Actions.

Raw API output is written to *_raw.json so it does NOT collide with
hand-curated *_summary.json files in the same directories.

Required environment variables:
  ZOHO_CLIENT_ID
  ZOHO_CLIENT_SECRET
  ZOHO_REFRESH_TOKEN
  ZOHO_ACCOUNTS_DOMAIN   e.g. https://accounts.zoho.com
  ZOHO_API_DOMAIN        e.g. https://www.zohoapis.com
"""

import os
import json
import sys
import time
import datetime
import requests
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

CLIENT_ID       = os.environ["ZOHO_CLIENT_ID"]
CLIENT_SECRET   = os.environ["ZOHO_CLIENT_SECRET"]
REFRESH_TOKEN   = os.environ["ZOHO_REFRESH_TOKEN"]
ACCOUNTS_DOMAIN = os.environ["ZOHO_ACCOUNTS_DOMAIN"].rstrip("/")
API_DOMAIN      = os.environ["ZOHO_API_DOMAIN"].rstrip("/")

BASE_DIR    = Path(__file__).resolve().parent.parent
EXPORTS_DIR = BASE_DIR / "zoho_exports"

ERRORS = []

# ---------------------------------------------------------------------------
# Auth
# ---------------------------------------------------------------------------

def get_access_token() -> str:
    """Exchange refresh token for a fresh access token."""
    url = f"{ACCOUNTS_DOMAIN}/oauth/v2/token"
    resp = requests.post(url, params={
        "refresh_token": REFRESH_TOKEN,
        "client_id":     CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type":    "refresh_token",
    })
    resp.raise_for_status()
    data = resp.json()
    if "access_token" not in data:
        raise RuntimeError(f"Token exchange failed: {data}")
    print(f"[auth] Access token obtained (expires in {data.get('expires_in')}s)")
    return data["access_token"]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def zoho_get(session, path, params=None):
    """GET from the Zoho CRM API. Returns parsed JSON body or {} on error."""
    url = f"{API_DOMAIN}/crm/v7{path}"
    resp = session.get(url, params=params or {})
    if resp.status_code == 204:
        return {}
    if not resp.ok:
        msg = f"GET {path} -> {resp.status_code}: {resp.text[:300]}"
        print(f"[warn] {msg}")
        ERRORS.append(msg)
        return {}
    return resp.json()


def write_json(rel_path, data):
    """Write data as indented JSON to zoho_exports/<rel_path>."""
    out = EXPORTS_DIR / rel_path
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"[write] {rel_path}  ({len(json.dumps(data))} bytes)")


def paginate(session, path, key, extra_params=None):
    """Fetch all pages for a Zoho endpoint that supports per_page/page."""
    results = []
    page = 1
    while True:
        params = {"per_page": 200, "page": page, **(extra_params or {})}
        data = zoho_get(session, path, params)
        items = data.get(key, [])
        results.extend(items)
        info = data.get("info", {})
        if not info.get("more_records", False):
            break
        page += 1
        time.sleep(0.2)
    return results


# ---------------------------------------------------------------------------
# Pullers - all write *_raw.json so they do not overwrite curated *_summary.json
# ---------------------------------------------------------------------------

def pull_modules(session):
    print("\n=== Modules ===")
    data = zoho_get(session, "/settings/modules")
    modules = data.get("modules", [])
    write_json("modules/modules_raw.json", modules)
    print(f"  {len(modules)} modules found")
    return modules


def pull_fields(session, modules):
    print("\n=== Fields by Module ===")
    for mod in modules:
        api_name = mod.get("api_name", "")
        if not api_name:
            continue
        data = zoho_get(session, "/settings/fields", {"module": api_name})
        fields = data.get("fields", [])
        if fields:
            write_json(f"modules/fields_{api_name}_raw.json", fields)
            print(f"  {api_name}: {len(fields)} fields")
        time.sleep(0.1)


def pull_layouts(session, modules):
    print("\n=== Layouts by Module ===")
    for mod in modules:
        api_name = mod.get("api_name", "")
        if not api_name:
            continue
        data = zoho_get(session, "/settings/layouts", {"module": api_name})
        layouts = data.get("layouts", [])
        if layouts:
            write_json(f"modules/layouts_{api_name}_raw.json", layouts)
            print(f"  {api_name}: {len(layouts)} layouts")
        time.sleep(0.1)


def pull_workflows(session):
    """List rules + per-rule details. Per-rule details contain criteria
    AND the actions array (instant_actions, scheduled_actions) - the key
    piece that closes the rule->function/webhook wiring gap."""
    print("\n=== Workflow Rules ===")
    rules = paginate(session, "/settings/automation/workflow_rules", "workflow_rules")
    write_json("workflows/workflow_rules_raw.json", rules)
    print(f"  {len(rules)} workflow rules found")

    details = []
    for rule in rules:
        rule_id = rule.get("id")
        if not rule_id:
            continue
        detail = zoho_get(session, f"/settings/automation/workflow_rules/{rule_id}")
        rule_data = detail.get("workflow_rules", detail)
        if isinstance(rule_data, list) and rule_data:
            details.append(rule_data[0])
        elif isinstance(rule_data, dict) and rule_data:
            details.append(rule_data)
        time.sleep(0.15)

    write_json("workflows/workflow_rule_details_raw.json", details)
    print(f"  {len(details)} workflow rule details pulled")


def pull_field_updates(session):
    """Workflow field-update actions. Try several v7 paths since the
    endpoint shape has shifted across Zoho releases."""
    print("\n=== Field Updates ===")
    updates = []
    for path, key in [
        ("/settings/automation/actions/field_updates", "field_updates"),
        ("/settings/field_updates", "field_updates"),
        ("/settings/automation/actions", "actions"),
    ]:
        data = zoho_get(session, path, {"per_page": 200})
        items = data.get(key) or []
        if items:
            updates = items
            print(f"  Found {len(updates)} via {path}")
            break
    write_json("workflows/field_updates_raw.json", updates)


def pull_email_notifications(session):
    """Workflow email-notification actions."""
    print("\n=== Email Notifications ===")
    emails = []
    for path, key in [
        ("/settings/automation/actions/email_notifications", "email_notifications"),
        ("/settings/email_notifications", "email_notifications"),
        ("/settings/automation/actions", "actions"),
    ]:
        data = zoho_get(session, path, {"per_page": 200, "type": "email_notification"})
        items = data.get(key) or []
        if items:
            emails = items
            print(f"  Found {len(emails)} via {path}")
            break
    write_json("workflows/email_notifications_raw.json", emails)


def pull_webhooks(session):
    print("\n=== Webhooks ===")
    data = zoho_get(session, "/settings/automation/webhooks", {"per_page": 200})
    webhooks = data.get("webhooks", [])
    write_json("webhooks/webhooks_raw.json", webhooks)
    print(f"  {len(webhooks)} webhooks found")


def pull_custom_links(session, modules):
    print("\n=== Custom Links ===")
    all_links = {}
    for mod in modules:
        api_name = mod.get("api_name", "")
        if not api_name:
            continue
        data = zoho_get(session, "/settings/link_names", {"module": api_name})
        links = data.get("link_names", [])
        if links:
            all_links[api_name] = links
        time.sleep(0.1)
    write_json("custom_links/custom_links_raw.json", all_links)
    print(f"  Custom links pulled for {len(all_links)} modules")


def pull_variables(session):
    print("\n=== CRM Variables ===")
    data = zoho_get(session, "/settings/variables")
    variables = data.get("variables", [])
    write_json("variables/variables_raw.json", variables)
    print(f"  {len(variables)} variables found")


def pull_users(session):
    print("\n=== Users ===")
    data = zoho_get(session, "/users", {"type": "AllUsers", "per_page": 200})
    users = data.get("users", [])
    safe_fields = [
        "id", "full_name", "email", "role", "profile",
        "status", "created_time", "modified_time",
        "time_zone", "locale", "language", "country_locale",
    ]
    users_safe = [{k: u.get(k) for k in safe_fields} for u in users]
    write_json("users/users_raw.json", users_safe)
    print(f"  {len(users_safe)} users written (sensitive fields stripped)")


def pull_org(session):
    print("\n=== Org Info ===")
    data = zoho_get(session, "/org")
    org = data.get("org", [])
    write_json("users/org_info_raw.json", org)
    print("  Org info written")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print(f"[start] Zoho CRM pull -- {datetime.datetime.utcnow().isoformat()}Z")

    token = get_access_token()
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Zoho-oauthtoken {token}",
        "Content-Type": "application/json",
    })

    modules = pull_modules(session)
    pull_fields(session, modules)
    pull_layouts(session, modules)
    pull_workflows(session)
    pull_field_updates(session)
    pull_email_notifications(session)
    pull_webhooks(session)
    pull_custom_links(session, modules)
    pull_variables(session)
    pull_users(session)
    pull_org(session)

    sync_meta = {
        "last_sync_utc": datetime.datetime.utcnow().isoformat() + "Z",
        "modules_count": len(modules),
        "errors": ERRORS,
    }
    write_json("sync_meta.json", sync_meta)

    if ERRORS:
        print(f"\n[done] Completed with {len(ERRORS)} warning(s):")
        for e in ERRORS:
            print(f"  - {e}")
        sys.exit(0)
    else:
        print("\n[done] All pulls completed successfully.")


if __name__ == "__main__":
    main()
