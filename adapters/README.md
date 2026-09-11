# HAPW Adapters

Adapters implement HAPW Core functions in a particular storage system, version-control system, chat product, terminal, or other tool. They change **mechanics**, not Core semantics.

## Adapter selection rule

Use the smallest adapter set that gives the project the functions it actually needs. No adapter is mandatory merely because it exists.

Before work begins, declare which system owns each class of current authoritative fact. Avoid maintaining two independent living copies of the same current fact.

Example:

```text
project state -> one declared durable store
source code -> version-control repository
large/raw evidence -> evidence store
AI chat -> working surface, not sole authority
```

## Common adapter contract

Each HAPW adapter in this package states:

- **Adapter name/version**
- **Functions implemented**
- **Authority role** — what it may make authoritative
- **Non-authority role** — what it does not automatically make authoritative
- **Persistence model**
- **Minimum setup**
- **Read/write capabilities**
- **Authentication / secret boundary**
- **Artifact references**
- **Known limitations**
- **Product/version/date scope**
- **Recovery procedure**
- **Failure modes**
- **Portability / exit path**
- **Irreducible user action** when direct tool access is unavailable

Those fields implement the adapter contract in the frozen HAPW v0.2 candidate. Product-specific steps may change over time, so current capabilities must be verified when they matter.

## Composition without dual authority

Multiple adapters can be used together when their roles are different. For example, a document store can own current project state while GitHub owns source code and tests. That is not dual authority if the same current fact is not independently maintained in both places.

When a fact must be referenced across systems, link to the owning record rather than silently copying and maintaining a competing version.

## Migration rule

Changing adapters is an authority change, not a casual copy operation.

1. Identify the current authoritative records and the exact stop point.
2. Copy/export them through a byte-preserving or semantically verified path appropriate to the data.
3. Verify completeness and important identities or hashes.
4. Record the destination and the authority switch explicitly.
5. Only then treat the destination as current authority.
6. Mark old living copies historical, derived, or retired so they cannot drift into a second authority.

Do not delete the old store until recovery from the new authority has been proven and retention requirements are satisfied.

## Included adapters

- [`local-filesystem.md`](local-filesystem.md) — durable local or mounted project folder.
- [`google-drive.md`](google-drive.md) — designated Google Drive folder/files as durable project state.
- [`github.md`](github.md) — designated GitHub repository/branch/files as durable state or implementation authority.

These documents describe HAPW usage patterns, not guarantees that a particular AI product has every required permission or connector capability.
