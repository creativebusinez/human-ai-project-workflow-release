# HAPW Authority Model

HAPW treats authority as an explicit project decision. Storage location, filename, recency, or convenience alone does not decide what is current truth.

## One authority per artifact class

For each material artifact class, declare one current authority.

Examples of artifact classes include:

- project state and exact next action;
- decisions;
- source code and tests;
- raw evidence;
- published documentation;
- financial or operational records.

A small project may keep several classes in one durable folder. A larger project may split them across systems. The important rule is that the same current fact should not be maintained independently in two authorities.

## Split authority

Split authority is valid when ownership is unambiguous.

Example:

```text
project state -> durable document store
implementation -> version-control repository
large raw evidence -> evidence archive
AI conversation -> working surface only
```

References may cross systems. A project-state record can point to an implementation commit without copying the implementation into the state store. Likewise, an implementation repository can point to an evidence record without becoming the evidence authority.

## What is not automatically authoritative

The following are not automatically current authority:

- AI chat history;
- copied or exported files;
- screenshots of source files;
- backups;
- local clones;
- cached or indexed connector results;
- temporary working directories;
- branches, forks, or drafts that were not assigned authority;
- a newer timestamp with weaker evidence.

These may still be useful evidence or historical records.

## Conflict resolution

When records conflict, do not choose by recency alone. Resolve the conflict using the declared authority, evidence strength, directness, validated identities, and the scope of each claim.

A useful order is:

1. identify which artifact class is in conflict;
2. identify the declared authority for that class;
3. compare direct evidence and validated records before summaries or chat recollection;
4. preserve uncertainty when evidence is insufficient;
5. record the resolution without erasing the historical record.

A later timestamp does not automatically outrank a stronger earlier artifact.

## Historical integrity

Do not silently rewrite historical records to make them match the present. Correct current state with a new record, addendum, or updated living file while preserving the older artifact as historical evidence.

This makes it possible to answer both "what is true now?" and "what did we believe at that time?"

## Changing authority

Changing storage systems is an **authority migration**, not merely a copy operation.

A safe migration is:

1. identify the current authoritative records;
2. copy or export them through an appropriate transport;
3. verify completeness and important identities or hashes;
4. test recovery from the destination;
5. record the authority switch explicitly;
6. mark the old copy historical, backup, or retired.

Do not leave both systems acting as independent current authorities after migration.

## Human authority

HAPW does not transfer project ownership to an AI assistant. The human operator retains authority over goals, risk acceptance, publication, spending, destructive actions, and other decisions that require human judgment or authorization.
