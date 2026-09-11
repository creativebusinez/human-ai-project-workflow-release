# HAPW Quick Start

Use this when you have a simple project goal and want a durable, recoverable AI-assisted project without setting up a full project-management system first.

Target setup time: **about five minutes**.

## 1. State one project goal

Write one sentence describing what you want to accomplish.

Example form:

```text
Goal: <one concrete outcome>
```

Do not turn the first setup step into a complete plan.

## 2. Choose one authoritative durable state location

Pick one place that will hold the project's current authoritative state, such as a durable local folder or a document store you control.

Record the boundary explicitly:

```text
Authoritative project state: <location/system>
AI conversations: working sessions, not sole authority
```

If code or another artifact class needs a different authority later, declare that separately instead of maintaining competing current copies.

## 3. Copy the four core templates

Create a project folder and copy:

```text
templates/00_PROJECT.md
templates/01_STATE.md
templates/02_NEXT.md
templates/03_DECISIONS.md
```

Rename or reorganize them only if the authority boundary remains obvious.

## 4. Fill only the minimum fields

In `00_PROJECT.md`, fill:

- the goal;
- what observable result counts as success;
- material constraints;
- the authoritative state location.

In `01_STATE.md`, record only what is currently known, observed, unresolved, and the current stop point.

In `02_NEXT.md`, write **one exact actionable next step**.

In `03_DECISIONS.md`, record only decisions that matter to future work. Do not invent decisions merely to fill the file.

## 5. Perform one bounded unit of work

Do the smallest useful action that advances the project.

Before a material action, know:

- why you are doing it;
- what result would change the decision;
- what evidence, if any, must be preserved;
- what safety or privacy boundary matters.

Simple actions do not need ceremony. For troubleshooting or experiments, isolate meaningful variables when practical.

## 6. Checkpoint at a meaningful pause

When you stop at a point where context could be lost, copy `templates/CHECKPOINT.md` and fill only what is needed to resume safely:

- verified state;
- important decisions or constraints;
- unresolved problems;
- useful evidence locations;
- stop point;
- exact next action.

Do not create a checkpoint for every trivial pause.

## 7. Recover from durable state

In a fresh AI conversation or after time away, recover from the project files rather than hidden chat history.

Read, in order:

1. `00_PROJECT.md`
2. `01_STATE.md`
3. `02_NEXT.md`
4. relevant entries in `03_DECISIONS.md`
5. the latest checkpoint only if needed

Then state:

```text
Recovered stop point: <where work actually stopped>
Exact next action: <one actionable continuation step>
```

Do not change the project until the recovered state is coherent.

## A compact starter instruction for an AI assistant

```text
Use the project's declared authoritative records as durable state.
Do not rely on this chat as the sole project record.
Before substantive continuation, recover the goal, current state, unresolved
problems, stop point, constraints, and exact next action from those records.
Separate observed facts from interpretation when it matters.
At meaningful pauses, preserve enough state to resume without this chat.
```

## What to read next

The full candidate rules are in [`core/HAPW-v0.2-public-candidate.md`](core/HAPW-v0.2-public-candidate.md).

This Quick Start is onboarding material for the **HAPW v0.2 public candidate**. It does not replace the Core and does not imply HAPW 1.0.
