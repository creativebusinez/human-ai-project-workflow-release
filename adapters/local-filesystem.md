# Adapter: Local Filesystem

## Adapter name/version

HAPW Local Filesystem Adapter 0.1 — candidate package guidance.

## Functions implemented

Durable project-state storage, file-based evidence references, checkpoint storage, handoff storage, and fresh-session recovery from a designated directory.

## Authority role

A declared local or mounted directory may be the authoritative durable store for the project records placed under that boundary.

Example:

```text
Authoritative project state: /path/to/project-control/
```

Authority comes from the project declaration, not from the fact that a file exists on disk.

## Non-authority role

The adapter does not automatically make every file on the device authoritative. Temporary directories, application caches, downloaded copies, editor buffers, backups, and synced replicas are not current authority unless the project explicitly assigns them that role.

## Persistence model

Files persist according to the storage medium and filesystem behind the declared directory. Local SSD/HDD storage, network mounts, removable media, containers, virtual machines, and cloud-mounted filesystems have different durability properties.

A path that exists inside an ephemeral runtime is not durable merely because it looks like a normal filesystem path.

## Minimum setup

1. Create or choose one durable project directory.
2. Put the minimum project-control records there.
3. Record the authoritative path in `00_PROJECT.md` or equivalent.
4. Ensure the directory survives the chat/session/process/host boundary relevant to the project.
5. Confirm the operator and any authorized AI/tool can read the required records before relying on the adapter.

## Read/write capabilities

An AI can read or write only when its environment exposes the declared directory with suitable permissions. When direct filesystem access is unavailable, the operator must provide a safe file-transfer or editing path.

Durable writes should target the authoritative files themselves, not an untracked temporary copy. For material changes, verify the written file exists and contains the intended state before claiming persistence.

## Authentication / secret boundary

Filesystem permissions, device accounts, disk encryption, mount permissions, and operating-system access controls protect the directory.

Do not store passwords, API keys, private keys, recovery codes, tokens, or secret-bearing URLs in routine HAPW records. If a project needs local secrets, keep them in a dedicated protected secret store or permission-restricted file outside publishable project state, and reference only the fact that the secret exists where necessary.

## Artifact references

Prefer paths relative to the declared project root so records remain portable:

```text
Evidence/logs/run-001.txt
checkpoints/2026-09-10.md
```

Record a hash when exact byte identity or provenance matters. Do not use a screenshot of a file as a substitute for the original file when the bytes themselves are the evidence.

## Known limitations

- A local path may be unavailable from another device or AI environment.
- Unsaved editor buffers can disappear.
- Container, notebook, sandbox, temporary VM, or `/tmp` storage may be ephemeral.
- Mounts can silently disconnect or remap.
- Sync software can create conflicts or stale replicas.
- Local storage can fail without backup.
- Relative and absolute paths can resolve to the wrong working directory.

## Product/version/date scope

This adapter is filesystem-model guidance, not an operating-system-specific installation recipe. Exact mount, permission, backup, and path behavior must be verified for the OS, filesystem, container, VM, or synchronization layer actually used.

## Recovery procedure

In a fresh session:

1. Resolve the declared authoritative project root.
2. Verify the root is the intended durable location, not a stale copy or temporary mount.
3. Read `00_PROJECT.md`, `01_STATE.md`, `02_NEXT.md`, relevant decisions, and the latest checkpoint only if needed.
4. Identify conflicts, missing files, or uncertain freshness instead of guessing.
5. State the recovered stop point and exact next action.
6. Do not mutate project state until recovery is coherent.

## Failure modes

- **Wrong root / wrong CWD:** files are read from or written to another directory.
- **Ephemeral storage:** state disappears with the runtime or host.
- **Permission failure:** the AI/operator can read but cannot durably write, or vice versa.
- **Stale replica:** a synchronized or copied folder is mistaken for current authority.
- **Partial write:** interruption leaves incomplete content.
- **Mount loss:** a path remains present but the expected backing store is absent or remounted elsewhere.
- **Duplicate authority:** two local copies are both treated as current and drift apart.

When a material failure occurs, stop writes until the authoritative root and current record identities are re-established.

## Portability / exit path

Copy the complete authoritative project-control set to the destination using a transport appropriate to the data. Verify required files and important hashes, test recovery from the destination, then explicitly change the recorded authority. Retain or label the former copy as historical/backup rather than leaving two living authorities.

## Irreducible user action

If the AI cannot access the filesystem directly, the user or an authorized local tool must expose, transfer, or edit the required files. The AI must not claim a durable write it could not verify.
