# HAPW Concepts

This document is a short map of the concepts used by the Human–AI Project Workflow (HAPW) starter package. The frozen Core remains the normative workflow description; this file is explanatory package material.

## Durable state

**Durable state** is project information that survives the current chat, process, device session, or temporary runtime. The important point is not the storage product but whether a fresh operator or AI session can recover what matters without depending on hidden conversation memory.

Typical durable state includes the project goal, current state, exact next action, decisions, checkpoints, and references to material evidence.

## Authority

An **authority** is the declared place that owns the current truth for a class of project facts. A file does not become authoritative merely because it exists or is newer.

HAPW uses two simple rules:

- declare the authoritative state explicitly;
- use one authority per artifact class unless a deliberate migration is in progress.

A project may use split authority when different systems own different classes of facts. For example, one durable store may own project state while a version-control repository owns source code. The same current fact should not be independently maintained as authoritative in both places.

## Evidence, observation, and interpretation

HAPW separates what was **observed** from what has been **validated**, inferred, interpreted, or recommended when that distinction matters.

Evidence should be proportional to the claim. A short exact fact may need only text; a long diagnostic may need a log; a static interface state may need a screenshot; dynamic behavior may need video. The least burdensome artifact that reliably proves the claim is usually best.

Failures are also evidence when they narrow the problem or preserve a useful boundary.

## Exact next action

The **exact next action** is one actionable continuation step, not a broad backlog. It reduces restart cost and prevents a fresh session from reopening settled work.

A good next action is specific enough that another operator can begin without guessing what "continue" means.

## Checkpoint

A **checkpoint** records enough current state to resume safely after a meaningful pause. It normally captures verified state, protected decisions or constraints, unresolved problems, evidence locations, the stop point, and the exact next action.

Do not create a checkpoint for every trivial pause. Checkpoint when losing context would create real rework, ambiguity, or risk.

## Handoff

A **handoff** is for moving work into another context, lane, team, tool, or formal work unit. It is not just a longer checkpoint.

A handoff should preserve the destination, purpose, verified state, protected decisions, open questions, results, evidence, stop point, and the exact first action in the destination.

## Adapter

An **adapter** implements HAPW functions in a particular storage or tooling system without redefining Core semantics. Adapters explain where state lives, how it is read or written, what can fail, how secrets are bounded, how recovery works, and how to leave the system without creating a second authority.

See [`../adapters/README.md`](../adapters/README.md) for the adapter contract and included examples.

## Optional rigor

HAPW is intentionally composable. Simple work can use only the minimum project-control spine. Troubleshooting, formal experiments, benchmarking, implementation provenance, or source-quality controls should be added only when the work actually needs them.

The goal is recoverability and trustworthy continuation, not ceremony for its own sake.
