# manual_exports/functions/

## ⚠️ Manual Export Required

Zoho CRM **does not expose Deluge function source code via any public API**.
This folder must be populated manually.

## What belongs here

Deluge functions created in **Zoho CRM → Setup → Developer Space → Functions**.

## How to export

1. Go to **Zoho CRM → Setup → Developer Space → Functions**
2. For each function, open it and copy the Deluge source code
3. Save each function as a `.dg` or `.txt` file named after the function, e.g. `updateDealStage.dg`
4. Optionally create a `_index.json` listing all functions with their names, descriptions, and argument signatures
5. Commit the files to this folder

## Suggested file naming

```
manual_exports/functions/
  _index.json              # optional: list all functions with metadata
  myFunctionName.dg        # Deluge source for each function
  anotherFunction.dg
```

## How to use with AI

Once populated, ask: *"What Deluge functions exist? What does `updateDealStage` do?"*
