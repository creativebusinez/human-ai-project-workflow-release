# Adapter: Google Drive

## Adapter name/version

HAPW Google Drive Adapter 0.1 — candidate package guidance.

## Functions implemented

Durable project-state storage in designated Drive files/folders, link-based evidence references, checkpoint/handoff preservation, and fresh-session recovery when the current Drive authority is accessible.

## Authority role

A specifically declared Google Drive folder and its designated control records may be authoritative for current project state, decisions, checkpoints, evidence indexes, or other assigned record classes.

Example:

```text
Authoritative project state: Google Drive / <project folder> / Canonical
```

The authority declaration should identify the project root or controlling files precisely enough that a fresh operator does not have to guess among similarly named folders.

## Non-authority role

Google Drive does not automatically make every file, shortcut, exported copy, synced desktop copy, attachment, or search result authoritative. AI chat remains a working surface unless separately declared. Git repositories or other stores may own different fact classes, but the same current fact should not be maintained independently in both places.

## Persistence model

Drive stores provider-managed file objects with stable file identities and sharing/permission state. Native Google Workspace documents and uploaded files have different byte/export behavior; an exported copy is a derivative unless the project explicitly promotes it.

Offline, cached, connector-indexed, or previously downloaded copies may be stale. Current authoritative state should be recovered from the live declared Drive source when freshness matters.

## Minimum setup

1. Create or choose one Drive project root.
2. Establish the minimum project-control records and clear folder roles.
3. Record the authoritative Drive location in the project record.
4. Set sharing permissions no broader than necessary.
5. Verify the operator and intended AI/connector can read the control records.
6. Verify write capability before relying on automated checkpoint updates.

## Read/write capabilities

Read/write mechanics depend on the current Drive UI, API, or connector available to the operator/AI. A tool may support search but not mutation, or may support file replacement but not every Google Workspace editing operation.

Before a material write, ground the exact target file/folder identity. After writing, read back the authoritative file or metadata when the claim depends on persistence. Do not infer success from an upload request alone.

## Authentication / secret boundary

Use Google account permissions, folder/file sharing, organization controls, and connector authorization as the access boundary.

Do not place passwords, API keys, OAuth client secrets/codes, private keys, recovery codes, tokens, secret-bearing URLs, or unnecessary account/billing details in ordinary Drive project records. Review link-sharing state before treating a folder as suitable for private evidence.

## Artifact references

Prefer stable Drive file/folder links or file IDs recorded in the authoritative project state. For exact-byte evidence, preserve the original uploaded file and record a cryptographic hash when provenance matters.

Native-document exports can change representation. Do not claim an exported PDF/DOCX/Markdown file is byte-identical to the native Drive object unless the comparison is explicitly defined and verified.

## Known limitations

- Connector/indexed results can lag the live file.
- Duplicate folders or similarly named documents can create discovery ambiguity.
- Sharing changes can expose or hide project state.
- A user can move, trash, rename, or replace a file while an old link/search result remains in circulation.
- Native Google document exports are representations, not the native object bytes.
- Offline/synced desktop copies can be stale or conflicted.
- Some AI integrations expose read-only or partial Drive capabilities.
- Search relevance is not proof that the returned file is the declared authority.

## Product/version/date scope

This adapter describes Google Drive as a durable-state mechanism without assuming one specific AI connector or Workspace plan. Current sharing behavior, API/connector capabilities, export formats, quotas, and permissions must be verified when material to a workflow.

## Recovery procedure

In a fresh session:

1. Locate the declared Drive project root or exact controlling file identities.
2. Prefer live current Drive records over cached/indexed/exported copies when freshness matters.
3. Read the project definition, current state, exact next action, relevant decisions, and latest checkpoint only if needed.
4. Reconcile contradictory records by authority and evidence strength; do not choose solely by filename or timestamp.
5. State the recovered stop point, exact next action, and any unresolved conflict.
6. Do not write until recovery is coherent.

## Failure modes

- **Wrong file/folder:** a similarly named Drive object is mistaken for authority.
- **Stale retrieval:** cached/indexed content is treated as current live state.
- **Permission loss:** a fresh session cannot read or update the declared authority.
- **Sharing exposure:** private material is placed in a broadly shared folder.
- **Duplicate authority:** exported/synced copies are maintained as competing current state.
- **Representation confusion:** a native document and an export are treated as byte-identical.
- **Write/readback mismatch:** a write is acknowledged but the authoritative object does not contain the expected result.

## Portability / exit path

Identify the exact authoritative Drive objects, export/download or copy them using a representation appropriate to each file class, preserve important hashes/identities where possible, and test recovery from the destination. Then update the project authority declaration. Keep the former Drive copy as historical/backup or retire it explicitly so it does not remain a second living authority.

## Irreducible user action

If the available AI integration cannot create a folder, change sharing, grant access, perform a required export, or write the needed file type, the user must perform that bounded Drive action or provide another authorized tool path. The AI must state the limitation instead of pretending the mutation occurred.
