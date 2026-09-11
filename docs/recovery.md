# HAPW Recovery

Recovery is the process of reconstructing the current project state from durable records rather than relying on hidden chat memory.

## Recovery objective

A successful recovery should establish, at minimum:

- the project goal and success condition;
- the declared authoritative state;
- what is already complete;
- what remains unresolved;
- material decisions or constraints that must not be reopened accidentally;
- the exact stop point;
- the exact next action;
- material evidence or implementation references required for continuation.

## Read before changing

Treat initial recovery as read-only. Do not "clean up," rewrite, checkpoint, or otherwise mutate project state until the recovered picture is coherent.

This matters because a fresh session may initially find stale copies, incomplete summaries, old checkpoints, or conflicting records.

## Minimum recovery order

For the starter package, read:

1. `00_PROJECT.md` — purpose, success, constraints, authority;
2. `01_STATE.md` — validated facts, observations, unknowns, stop point;
3. `02_NEXT.md` — exact continuation step and protected constraints;
4. relevant entries in `03_DECISIONS.md`;
5. the latest checkpoint only when needed to resolve the current state.

If another artifact class has its own authority, resolve the exact relevant identity there as well. For example, implementation work may require a repository commit reference.

## Fresh-session recovery protocol

In a fresh context:

1. locate the declared authority rather than asking the user to restate recoverable facts;
2. verify that the records belong to the intended project and are not a stale copy;
3. read the minimum current-state set;
4. identify contradictions, missing evidence, and uncertain freshness;
5. distinguish recovered facts from interpretation;
6. state the recovered stop point and exact next action;
7. continue only after the recovery is coherent and the requested action is authorized.

## Conflicts and missing evidence

When two records disagree:

- prefer the declared authority for that artifact class;
- prefer raw/direct evidence and validated records over summaries;
- use timestamps only as one factor, not the sole deciding rule;
- preserve the conflict if it cannot be resolved;
- do not invent a missing state simply to make continuation easier.

If the authoritative record is unavailable, say what is missing and what bounded action is required to recover it.

## Checkpoints and recovery

A checkpoint helps recovery but does not automatically override living current-state files. It records where work stood at a meaningful pause. If work later continued, the current state may supersede that checkpoint while the checkpoint remains valid history.

## Handoffs and recovery

Use a handoff only when work moves into another context. A handoff should make the destination recoverable without depending on the source chat. Once the destination has recovered and established its own durable state, the old chat should not be required for continuation.

## Recovery test

A strong workflow should periodically be tested from a genuinely fresh context. The fresh operator or agent should recover the project without hidden rescue information, report uncertainty instead of guessing, and continue from the exact durable next action.
