---
title: "Human–AI Project Workflow Core"
short_title: "HAPW Core"
version: "0.2-public-candidate"
status: "PUBLIC-DERIVATIVE CANDIDATE / NON-CANONICAL / NOT 1.0"
date: "2026-09-11"
scope: "domain-neutral human–AI project operation"
origin: "Sanitized public derivative of the frozen HAPW Core v0.2 candidate"
validation_status: "SOURCE CANDIDATE BOUNDED VALIDATION COMPLETE; PUBLIC-DERIVATIVE RELEASE VALIDATION PENDING; NOT PROMOTED TO 1.0"
---

# Human–AI Project Workflow Core v0.2 — PUBLIC CANDIDATE

## 1. Purpose

The Human–AI Project Workflow Core (HAPW Core) defines a portable method for humans and AI assistants to work on projects over time without depending on hidden chat history, one specific AI product, one storage provider, or one technical domain.

The workflow is designed to help a user move from:

> “I want to accomplish X.”

through structured work toward:

> “X is completed or clearly bounded, important facts and evidence are preserved, and another capable human or AI can continue without reconstructing the project from old conversations.”

The workflow is intentionally smaller than a full project-management system. It should provide **minimum sufficient project control**: enough structure to preserve continuity, evidence, decisions, and next actions without making administration the project.

## 2. Status and Boundaries

This document is a **versioned candidate**, not yet a canonical cross-project standard.

It was derived from frozen HAPW Core v0.1-draft plus the bounded P-01 through P-05 change set accepted after cross-domain, tool-substitution, evidence-completeness, and burden review.

Version 0.2 deliberately separates:

1. **CORE** — rules intended to apply across most projects;
2. **MODULES** — optional rigor for troubleshooting, experiments, benchmarking, implementation, and research;
3. **ADAPTERS** — product/tool-specific implementations such as ChatGPT, Google Drive, Git, Obsidian, terminals, or cloud providers;
4. **PROJECT OVERLAYS** — domain-specific rules, goals, constraints, terminology, and evidence requirements;
5. **LIVE PROJECT STATE** — what is currently true for one project.

The Core must not require a particular AI product, file format, cloud provider, version-control system, operating system, or knowledge-management tool.

## 3. Design Principles

### 3.1 Minimum sufficient project control

Use the least structure that reliably preserves continuity, correctness, provenance, and recoverability.

Do not create registers, evidence, handoffs, or formal experiments when they add no meaningful value.

### 3.2 Externalized durable state

Important project state must not exist only in an AI conversation, temporary compute environment, one device, or one person's memory.

The project must identify a durable authoritative state store.

### 3.3 Tool independence

The workflow defines required functions, not mandatory products.

For example:

- the Core requires a durable authoritative state store;
- an adapter may implement that store with Google Drive, local files, Notion, a database, or another system.

### 3.4 Evidence before inference

When a claim materially affects a decision, preserve enough evidence to distinguish what was observed from what was inferred.

### 3.5 Historical integrity

Closed historical records should not be silently rewritten to match later knowledge. Corrections should be made through addenda, new records, or living-state updates.

### 3.6 Recoverability over memory

A project is well controlled when a fresh capable human or AI can recover the current state from durable records without needing the original conversation.

### 3.7 Composable rigor

Simple projects should remain simple.

Formal experiment control, benchmarking, Git provenance, large evidence indexes, and multi-lane orchestration are optional modules activated when the work justifies them.

### 3.8 Human authority

The AI may research, analyze, propose, document, automate, and execute actions when authorized, but project authority remains explicitly defined by the human's project rules and durable records.

## 4. Reference Architecture

```text
Human / operator
      │
      ▼
AI working interface
      │
      ├── reads current authoritative state
      ├── teaches / reasons / researches / troubleshoots
      ├── proposes or performs authorized actions
      └── writes back material project state
      │
      ▼
Authoritative durable project state
      │
      ├── project charter / scope
      ├── current state
      ├── next actions
      ├── decisions
      ├── evidence references
      └── optional specialist records
      │
      ├───────────────┐
      ▼               ▼
Implementation     Derived knowledge
authority          / retrieval systems
(optional)         (optional)
```

The AI conversation is a **working surface**, not automatically the authoritative project record.

## 5. Core Authority Rules

### CORE-01 — Declare authoritative state

Every persistent project must identify where current authoritative state lives.

Minimum declaration:

```text
Authoritative project state: <location/system>
AI conversations: working sessions, not sole authority
```

### CORE-02 — One authority per artifact class

When multiple systems are used, assign roles rather than maintaining competing authoritative copies.

Example:

```text
project state/evidence -> durable document store
implementation code    -> version-control repository
retrieval projection   -> derived knowledge system
```

A project may use different systems, but the authority boundary must be explicit.

### CORE-03 — Resolve conflicts by evidence strength

When records disagree, do not assume the newest timestamp is correct.

Use this default precedence where applicable:

```text
1. raw/direct evidence
2. validated records or closeouts
3. living project registers/state
4. procedures/runbooks/knowledge notes
5. summaries, exports, historical snapshots, old chat
```

Preserve unresolved conflicts as conflicts until stronger evidence resolves them.

Generated snapshots or exports that could be mistaken for current living state should carry a date, version, or other freshness marker.

### CORE-04 — Separate factual status from reasoning

Use explicit vocabulary when useful:

- **OBSERVED** — directly seen or measured;
- **VALIDATED** — an explicit acceptance condition passed in defined scope;
- **INTERPRETATION** — reasoned conclusion from evidence;
- **RECOMMENDATION** — proposed action;
- **UNKNOWN** — current evidence does not establish the fact;
- **NOT RECOVERED** — evidence may have existed but is unavailable now;
- **HISTORICAL** — preserved past state, not necessarily current;
- **SUPERSEDED** — retained for provenance but replaced for current use.

Projects may simplify this vocabulary when the distinction is not material.

### CORE-05 — Scope claims

Do not generalize beyond the tested or observed conditions without evidence.

Record relevant scope such as version, date, environment, device, population, workflow, location, or other boundary when it affects the claim.

### CORE-06 — Preserve historical integrity

Do not silently rewrite closed records because later evidence changes the conclusion.

Use:

- addenda;
- explicit corrections;
- new measurements;
- updated living state;
- superseding records.

## 6. Core Continuity Rules

### CORE-07 — Documentation-first recovery

Before substantive continuation of a persistent project, recover the current state from authoritative records when those records exist and are materially relevant.

Minimum recovery questions:

1. What is the project trying to accomplish?
2. What is currently validated or known?
3. What remains uncertain, blocked, or unresolved?
4. Where did work stop?
5. What is the exact next action?
6. What constraints or decisions must not be accidentally reopened?

The user should not need to re-explain information already present in authoritative project state.

Before asking the operator to repeat or manually provide project information, inspect materially relevant authoritative and already-accessible project sources first when available.

### CORE-08 — Maintain an exact next action

A persistent project should normally have one explicit current next action.

The next action should be specific enough that a returning operator can resume without reconstructing intent.

Weak:

```text
Continue troubleshooting.
```

Better:

```text
Measure battery voltage at the starter during crank; record minimum voltage before replacing parts.
```

### CORE-09 — Checkpoint meaningful pauses

At a meaningful pause, interruption, dependency wait, risky transition, or before destructive cleanup, preserve enough state to resume safely.

Minimum checkpoint:

```text
current stage
verified facts
open problem(s)
stop point
exact next action
important evidence location(s)
```

Do not create a formal checkpoint for trivial pauses when current state is already obvious and durable.

### CORE-10 — Use handoffs only when context moves

A handoff is required when work moves to another materially distinct work context and the destination cannot safely infer continuation from shared state alone.

A handoff should include:

```text
purpose
destination
verified state
decisions/constraints
open questions
preserved evidence
stop point
exact first action
```

Do not use handoffs as routine ceremony within one continuous work unit.

### CORE-11 — Close work explicitly

When a work unit is terminal, record:

```text
result: PASS / FAIL / PARTIAL / BLOCKED / COMPLETE as appropriate
what was learned
what was validated
remaining problems
records/evidence updated
continuation, if any
```

A closed conversation should not be required for future continuation.

## 7. Core Work Cycle

The default project loop is:

```text
UNDERSTAND
   ↓
ACT
   ↓
OBSERVE
   ↓
VERIFY
   ↓
PRESERVE what matters
   ↓
DECIDE
   ↓
NEXT ACTION
```

Before a material action, the AI should be able to answer:

1. Why are we doing this?
2. What result would change the decision?
3. What evidence, if any, needs to be preserved?
4. What are the relevant safety/privacy boundaries?

For simple tasks, these answers may remain implicit. For high-cost, risky, destructive, or formal work, they should be explicit.

## 8. Evidence Core

### CORE-12 — Minimum sufficient evidence

Capture the least burdensome artifact that reliably proves the material claim.

More evidence is not automatically better evidence.

### CORE-13 — Match medium to claim

Default evidence choices:

| Claim type | Preferred evidence |
|---|---|
| short exact fact | TEXT |
| long/searchable machine output | LOG / structured data |
| static visual state | SCREENSHOT / PHOTO |
| dynamic sequence/transient behavior | VIDEO |
| planning/routine navigation/waiting | NO CAPTURE |

### CORE-14 — Bound evidence collection

Specify exactly what must be captured.

Prefer:

```text
Return only the final version and PASS line.
```

over:

```text
Send everything.
```

### CORE-15 — Preserve material artifacts outside transient surfaces

Useful evidence must not remain only in chat, disposable compute, or a single client device when future reproduction, diagnosis, audit, or provenance may depend on it.

### CORE-16 — Avoid redundant evidence

Do not preserve multiple artifacts proving the same routine claim unless each contributes distinct evidentiary value.

### CORE-17 — Failures are evidence

Preserve failures when they materially affect diagnosis, conclusions, reproducibility, or future avoidance.

Do not rerun a failure solely to create a cleaner-looking artifact unless the rerun itself is explicitly a reproduction test.

### CORE-18 — Protect secrets and private data

Do not preserve passwords, private keys, authentication secrets, secret-bearing URLs, unnecessary account-private data, or other sensitive material as routine project evidence.

Pause or omit capture during sensitive entry and preserve only sanitized verification where possible.

## 9. Minimum New-User Implementation

A new user should be able to start with:

```text
1 AI assistant
1 durable project folder
4 core records
1 evidence folder
```

Recommended minimum:

```text
My Project/
├── 00 PROJECT.md
├── 01 STATE.md
├── 02 NEXT.md
├── 03 DECISIONS.md
└── Evidence/
```

### 9.1 `00 PROJECT.md`

```markdown
# Project

## Goal
What are we trying to accomplish?

## Success
What observable outcome would count as success?

## Constraints
Cost, time, safety, privacy, tools, scope, or other limits.

## Authority
Where does authoritative project state live?
What systems are working surfaces, implementation stores, or derived projections?
```

### 9.2 `01 STATE.md`

```markdown
# Current State

## Validated / Known
- ...

## Observed
- ...

## Unknown / Unresolved
- ...

## Current Stop Point
- ...
```

### 9.3 `02 NEXT.md`

```markdown
# Current Next Action

<one exact actionable continuation step>

## Do Not Accidentally Change
- frozen constraints or settled decisions that matter to the next step
```

### 9.4 `03 DECISIONS.md`

```markdown
# Decision Log

## YYYY-MM-DD — Decision title
Decision:
Reason:
Evidence/constraint:
Status: CURRENT / SUPERSEDED
```

### 9.5 `Evidence/`

Store only materially useful artifacts and use stable descriptive names.

For small projects, the files above may be merged if one concise document remains easier to maintain.

## 10. Compact AI Behavioral Kernel

A portable AI instruction may be as small as:

```text
Use the project's declared authoritative records as durable state.
Do not rely on chat history as the sole project record.

Before substantive continuation, recover the project's goal, validated state,
unresolved problems, stop point, constraints, and exact next action from the
available authoritative records when relevant.

Distinguish observation/evidence from interpretation and recommendation.
Do not silently rewrite historical records; preserve corrections explicitly.

For material troubleshooting or experiments, change one meaningful variable at
a time when practical and prefer the smallest test that can resolve the current
uncertainty.

Capture the least burdensome evidence that reliably proves important claims.
Keep secrets and unnecessary private data out of project records.

At meaningful pauses or closeouts, preserve current state, decisions, useful
evidence references, and the exact next action so another capable human or AI
can continue without the current chat.
```

This behavioral kernel is an enforcement layer, not the complete workflow documentation.

## 11. Optional Module — Troubleshooting

Activate when diagnosis is a material part of the project.

### T-01 — Use the diagnostic loop

```text
OBSERVATION
   ↓
HYPOTHESIS
   ↓
SMALLEST DISCRIMINATING TEST
   ↓
RESULT
   ↓
CONCLUSION
   ↓
NEXT TEST / FIX
```

### T-02 — Do not confuse symptom with cause

A timeout, error message, missing utility, changed UI, or failed frontend request is evidence of a symptom, not automatically root cause.

Check the underlying state before making invasive changes.

### T-03 — Prefer isolation

When practical, change one meaningful cause at a time so the result remains interpretable.

### T-04 — Establish a baseline

Before optimizing, automating, or refactoring a working process, preserve enough baseline evidence to know whether the change improved or damaged it.

### T-05 — Preserve failed paths that teach something

Record dead ends when they prevent repetition or materially constrain future diagnosis.

## 12. Optional Module — Formal Experiments

Activate when a question requires controlled comparison or repeated testing.

### E-01 — Define the test before execution

Record as relevant:

```text
experiment ID
date/time
goal / hypothesis
condition / comparator
acceptance criteria
environment / versions
inputs/settings
expected output
cost/time limits
capture plan
```

### E-02 — Isolate materially different formal test units

Start a new formal work unit when the question, comparator, important variable, acceptance criteria, or experiment identity changes materially.

Repeated runs frozen within one condition may remain together.

When completed formal work is repeated, label the repeat as a control, reproduction, repeated run, or new test as applicable; do not erase or overwrite the prior execution identity.

Tool-specific adapters decide whether a new work unit means a new chat, notebook, branch, folder, ticket, or other container.

### E-03 — Record the result, not just the procedure

Minimum result:

```text
PASS / FAIL / PARTIAL / BLOCKED
observed result
material evidence
interpretation
limitations
next test or closeout
```

### E-04 — Negative results may still complete an experiment

A failed desired outcome can still be a complete and valuable experiment if the test question was answered and the evidence is sufficient.

## 13. Optional Module — Benchmarking

Activate when performance, cost, quality, speed, reliability, or resource usage is being compared.

### B-01 — Normalize comparators

Before attributing a difference to one component, normalize material conditions where practical.

### B-02 — Distinguish cold and warm state

Cache, process state, preloaded data, connection reuse, model warmth, filesystem cache, or other hidden state may change performance.

Record whether the run is cold, reconstructed, warm, resumed, or otherwise stateful when material.

### B-03 — Detect no-op/cache traps

A surprisingly fast repeated result may indicate caching or skipped work rather than real performance improvement.

Change an inference-relevant or work-relevant input when necessary to force genuine execution.

### B-04 — Prefer machine timing

Use machine-generated timing, structured logs, telemetry, or application timestamps when available. Video timing is secondary unless operator-inclusive interaction time is the claim.

### B-05 — Compare total job economics when cost matters

Hourly price alone may be misleading. Include setup, transfer, storage, runtime, failure/retry overhead, idle cost, and operator burden when relevant to the decision.

## 14. Optional Module — Implementation Provenance

Activate when code, scripts, automations, configurations, models, documents, or other versioned implementation artifacts materially affect a result.

### I-01 — Record exact implementation identity

Use the strongest practical identity available, such as:

```text
repository / source
exact commit or revision
release/tag as secondary context
clean/dirty state if relevant
content hash / bundle hash when useful
entrypoint / profile / schema/config version
```

A branch name or filename alone may be insufficient when reproducibility matters.

### I-02 — Separate implementation authority from project-state authority

Version-control systems may be authoritative for code while another durable system remains authoritative for project decisions, evidence, and current state.

Avoid manually maintaining competing living copies.

### I-03 — Version control is not secret storage

Do not treat a private repository as a credential vault.

## 15. Optional Module — Research and Source Quality

Activate when external claims materially affect decisions.

### R-01 — Separate source roles

Distinguish, when relevant:

```text
primary/upstream source
implementation/integration layer
secondary tutorial or commentary
community claim
observation from current testing
interpretation/recommendation
```

### R-02 — Verify change-sensitive claims

Current versions, prices, licenses, availability, APIs, requirements, policies, and named-role facts should be verified against current authoritative sources when material.

### R-03 — Preserve uncertainty

Do not turn a plausible explanation or community consensus into a validated project fact without supporting evidence.

## 16. Adapter Contract

An adapter implements Core functions using a specific tool or product.

Every adapter should state:

```text
Adapter name/version
Function(s) implemented
Authority role, if any
Persistence model
Read/write capabilities
Authentication/secret boundary
Known limitations
Product/version/date scope
Recovery procedure
Failure modes
```

### Required adapter questions

1. How does the AI access authoritative state?
2. How are durable writes performed?
3. What can disappear when a chat/session/device/host closes?
4. How are artifacts linked or referenced?
5. Where do secrets live?
6. How does a fresh session recover current state?
7. What user action remains irreducible when direct tool access is unavailable?

### Example adapter categories

- AI/chat interface adapter;
- durable storage adapter;
- version-control adapter;
- knowledge/RAG adapter;
- terminal/remote-control adapter;
- evidence-capture adapter;
- automation adapter.

No adapter is mandatory unless the project needs the function it provides.

## 17. Project Overlay Contract

A project overlay contains rules that are real but not universal.

Recommended overlay fields:

```text
project name
goal / mission
success criteria
domain terminology
domain safety constraints
domain evidence requirements
hardware/software/service assumptions
cost/time limits
project-specific authority additions
project-specific modules enabled
project-specific lifecycle rules
```

The overlay may strengthen a Core rule but should not silently weaken historical integrity, security, or authority boundaries.

## 18. Work-Unit Isolation

The Core does **not** require “one chat = one lane.”

The portable rule is:

> Keep materially distinct work units isolated when mixing them would create ambiguity in state, variables, evidence, responsibility, or continuation.

Possible implementations:

```text
new chat
new issue/ticket
new branch
new notebook
new experiment folder
new lab record
new document section
```

The adapter chooses the mechanism.

## 19. Security and Privacy Baseline

At minimum:

1. do not place passwords, private keys, tokens, OAuth secrets/codes, recovery codes, or equivalent credentials into routine AI chat or project evidence;
2. do not preserve secret-bearing URLs;
3. minimize unrelated private account/billing/personal information;
4. sanitize derivative/public artifacts rather than modifying raw evidence destructively;
5. keep raw/private evidence separate from public-safe derivatives when publication is possible;
6. do not use the absence of direct tool access as justification for exposing credentials to the AI.

Project overlays may add stronger domain-specific requirements.

## 20. Fresh-Session Recovery Protocol

A fresh AI or human should be able to perform:

```text
RECOVER
1. identify authoritative records
2. read project goal/scope
3. read current state
4. read exact next action
5. read material decisions/constraints
6. inspect relevant evidence only when needed
7. reconcile conflicts using authority/evidence rules
8. state recovered stop point
9. state exact next action
10. do not change anything until recovery is coherent
```

The user should not need to provide an old technical handoff when the authoritative state already contains sufficient continuation information.

## 21. Checkpoint Template

```markdown
# Checkpoint

Date:
Work unit:
Stage:

## Verified State
- ...

## Decisions / Constraints
- ...

## Problems / Unknowns
- ...

## Evidence Preserved
- ...

## Stop Point
- ...

## Exact Next Action
- ...
```

## 22. Handoff Template

```markdown
# Handoff

Destination:
Purpose:

## Verified State
- ...

## Decisions / Constraints
- ...

## Open Questions
- ...

## Results
- ...

## Preserved Evidence
- ...

## Stop Point
- ...

## Exact First Action in Destination
- ...
```

## 23. Closeout Template

```markdown
# Closeout

Result: PASS / FAIL / PARTIAL / BLOCKED / COMPLETE

## Learned
- ...

## Validated
- ...

## Problems Remaining
- ...

## Records / Evidence Updated
- ...

## Continuation
- none / exact next work unit or action
```

## 24. Validation Suite for the Workflow Itself

The workflow should be tested rather than accepted because it sounds reasonable.

During workflow validation, count and disclose rescue interventions or hidden-state injections that materially help the agent pass. A pass must not depend on undisclosed rescue.

A rescue intervention is an operator/controller action that supplies missing project state, corrects workflow mechanics, reveals an expected answer, or otherwise materially improves the agent's chance of passing beyond normal domain participation required by the frozen test.

Each workflow-validation run should preserve a durable grading/closeout record containing the workflow version, test setup and scope, result, material deviations, rescue interventions or hidden-state injections, evidence references, limitations, and next action or terminal status.

### V-01 — Fresh-agent recovery test

Give a fresh capable AI the Core, relevant adapter instructions, and one project's authoritative records without old conversation history.

Ask it to recover:

1. project goal;
2. authoritative sources;
3. validated/current state;
4. unresolved uncertainty;
5. stop point;
6. exact next action;
7. protected/frozen decisions;
8. evidence supporting material conclusions.

Score correctness and conflict handling.

### V-02 — Cross-domain transfer test

Apply the same Core to an unrelated project domain.

Suggested domains should differ materially, for example:

- home/vehicle repair;
- research/writing;
- software development;
- personal learning project;
- creative production.

The test should determine which rules remain useful, which become unnecessary burden, and which missing domain-neutral rules appear.

### V-03 — Tool-substitution test

Replace one adapter without changing the Core.

Examples:

```text
Google Drive -> local Git-backed Markdown
ChatGPT -> another capable AI interface
Obsidian -> another retrieval system
```

If the methodology collapses because one named product is missing, the extraction is not yet sufficiently portable.

### V-04 — Low-complexity burden test

Apply the Core to a small personal project.

PASS requires that the workflow can operate with the minimal four-record implementation without demanding lab-style experiment administration.

### V-05 — Historical integrity test

Introduce later evidence that contradicts an earlier closed conclusion.

PASS requires preserving the old record while updating current understanding explicitly.

## 25. Versioning and Change Control

The workflow itself should be versioned.

Example:

```text
workflow_core: HAPW 0.1
project_overlay: Example Project 1.0
adapter_chat: Chat Adapter 0.1
adapter_storage: Drive Adapter 0.1
```

A project should record which workflow version materially governed formal work when reproducibility matters.

Do not silently redefine old project history when the Core changes.

Substantive Core changes should include:

```text
change
reason
evidence/problem motivating change
backward-compatibility impact
migration recommendation, if any
```

## 26. Public Derivation Note

This file is a sanitized public derivative of the frozen HAPW Core v0.2 candidate.

The derivation is deliberately narrow: publication/provenance metadata and private or internal evidence references were removed or generalized so the workflow can be distributed without exposing source-project records. The normative workflow rules in Sections 1–25 were not intentionally changed by this sanitization step.

The source candidate remains preserved outside the public package for release-engineering provenance. A public operator does not need that private source material to use this Core.

This derivative remains a candidate and is **not HAPW 1.0**.

## 27. Known Open Questions After v0.2 Candidate

1. Should PROJECT, STATE, NEXT, and DECISIONS remain four recommended records or become one default compact project-control document for small projects?
2. Which Core rules should be mandatory versus advisory?
3. How should non-technical creative projects express evidence without over-formalizing subjective judgment?
4. What is the smallest reliable cross-domain recovery rubric?
5. Should work-unit isolation remain Core guidance or live entirely in project overlays?
6. How should multiple AI agents declare responsibility and write authority without creating competing state?
7. Which adapter capabilities can be machine-tested automatically?
8. What migration path should projects use when adopting a newer Core version?

## 28. Candidate Acceptance Criteria Toward 1.0

The v0.2 candidate does not by itself complete or waive the eventual 1.0 promotion criteria. Before promotion beyond `0.2-candidate` toward `1.0`, require at least:

- [ ] source-provenance audit complete;
- [ ] duplicate Core rules consolidated without losing meaning;
- [ ] project-specific assumptions removed from Core text;
- [ ] at least one unrelated low-complexity project trial;
- [ ] at least one unrelated technical/troubleshooting project trial;
- [ ] fresh-agent recovery test completed;
- [ ] tool-substitution review completed;
- [ ] operator burden reviewed;
- [ ] security review completed;
- [ ] known conflicts/limitations documented;
- [ ] final authority and storage location selected;
- [ ] version `1.0` promotion decision made explicitly.

## 29. v0.2 Public-Candidate Change Summary

### Public derivative identity

This `0.2-public-candidate` is a new sanitized derivative of the frozen `0.2-candidate` source. It does not overwrite or retroactively redefine that source candidate. Exact source/derivative identities and the bounded derivation diff are preserved in release-engineering records during staging.

### Bounded substantive changes carried by the source candidate

| ID | Location | Change | Generalized basis |
|---|---|---|---|
| P-01 | CORE-07 | Require checking materially relevant authoritative/already-accessible project sources before asking the operator to repeat recoverable information. | prior recovery validation and burden review |
| P-02 | CORE-03 | Require a date, version, or equivalent freshness marker only for snapshots/exports that could be mistaken for living state. | prior snapshot-freshness and burden review |
| P-03 | §24 Validation Suite | Count/disclose rescue interventions or hidden-state injections; a pass must not depend on undisclosed rescue. | prior workflow-validation practice |
| P-04 | §24 Validation Suite | Require a durable grading/closeout record for each formal workflow-validation run. | workflow-validation durability review |
| P-05 | §12 Formal Experiments / E-02 | Label repeats as control, reproduction, repeated run, or new test and preserve prior execution identity. | prior repeat-run and experiment-isolation review |

### Source-candidate validation summary

Before this public sanitization step, the source candidate had completed bounded checks covering tool substitution, an unrelated technical/troubleshooting trial, evidence completeness, operator burden, and version integrity. Those checks support the source candidate only within their tested scope; they do not by themselves qualify this public derivative for release.

The public derivative still requires the release-specific safety, licensing, and fresh bootstrap/recovery gates defined by the starter package.

### Explicit exclusions

The following are **not** part of this v0.2 public candidate:

- G-01 Optional Operational Documentation module — **DO NOT SUPPORT / DEFER**; future reconsideration requires new positive evidence from a new formal test.
- G-02 Knowledge/RAG traceability — adapter-only research guidance; no direct HAPW retrieval-quality test has isolated the feature.
- D-01 dirty/uncommitted implementation-delta requirement.
- D-02 independent milestone-backup requirement.
- D-03 adapter migration/rollback policy.
- D-04 RAG qualifier-proximity requirement.
- D-05 mixed-transcript/chunking requirement.

### Public-sanitization changes

- generalized front-matter origin and validation metadata;
- replaced source-project provenance mapping with this public derivation note;
- removed private grading/storage identifiers and source-project names;
- generalized internal validation labels and evidence references;
- intentionally preserved the normative workflow rules.

### Backward-compatibility / migration assessment

The v0.2 public candidate remains intentionally additive and low-burden. It does not require migration of existing v0.1 project records. Projects adopting v0.2 may continue using one compact project-control document for small projects and keep optional modules disabled unless justified. Historical work governed by v0.1 remains labeled v0.1 and is not reinterpreted as having used v0.2.

---

# End of Human–AI Project Workflow Core v0.2 — PUBLIC CANDIDATE
