# Human–AI Project Workflow

A general-purpose Human–AI Project Workflow starter for bootstrapping durable, recoverable AI-assisted projects.

**Status:** HAPW Core **v0.2 public candidate**. This is a sanitized release candidate under active validation. It is **not HAPW 1.0** and is not yet an approved public release.

## Start in about five minutes

Go directly to the [Quick Start](QUICKSTART.md). You can begin a small project without reading the full Core first.

The minimum project-control spine is four files:

- `00_PROJECT.md` — goal, success condition, constraints, and authority.
- `01_STATE.md` — what is known, observed, unresolved, and where work stopped.
- `02_NEXT.md` — one exact next action and any protected constraints.
- `03_DECISIONS.md` — durable decisions and why they were made.

Copy them from [`templates/`](templates/).

## What HAPW is for

HAPW is a lightweight method for keeping important project state outside transient AI conversations. It emphasizes:

- an explicitly declared durable authority for current project state;
- separation of observation, validation, interpretation, and recommendation when that distinction matters;
- one exact next action for reliable continuation;
- minimum sufficient evidence for material claims;
- checkpoints at meaningful pauses;
- recovery from durable records instead of hidden chat history.

It is intentionally smaller than a full project-management system. It does not claim universal applicability or that one unchanged setup fits every project or domain.

## Package layers

The package keeps three concerns separate:

1. **Core** — [`core/HAPW-v0.2-public-candidate.md`](core/HAPW-v0.2-public-candidate.md) contains the tool-independent workflow rules. It is a sanitized public derivative of the frozen v0.2 source candidate.
2. **Starter package** — README, Quick Start, templates, adapters, examples, validation, security/limitations guidance, and release metadata help people apply the Core.
3. **Adapters** — tool-specific instructions explain how a product or storage system implements Core functions. Adapters may change mechanics, but they do not redefine Core semantics.

The release-candidate package includes the onboarding layer, generic templates, adapters, explanatory docs, a minimal unrelated example, changelog, Apache-2.0 license, and mechanical validation. Final release-safety review, fresh unrelated-project validation, and explicit public-release authorization remain open.

## Repository structure

```text
README.md
QUICKSTART.md
CHANGELOG.md
VERSION
LICENSE
core/
templates/
adapters/
examples/minimal-project/
docs/
scripts/
.github/workflows/
```

## License

This package is licensed under the **Apache License, Version 2.0** (`Apache-2.0`). See [`LICENSE`](LICENSE).

## Documentation and example

- [`docs/concepts.md`](docs/concepts.md) explains the package vocabulary.
- [`docs/authority-model.md`](docs/authority-model.md) explains one-authority-per-artifact-class and split authority.
- [`docs/recovery.md`](docs/recovery.md) gives the fresh-session recovery procedure.
- [`docs/security.md`](docs/security.md) defines the package security/privacy boundary.
- [`docs/limitations.md`](docs/limitations.md) states the candidate limitations and validation boundary.
- [`examples/minimal-project/`](examples/minimal-project/) shows the four-file spine using a small pantry-inventory example.

## Core vs. adapters

The Core describes required functions such as durable authoritative state, recovery, evidence handling, checkpoints, and handoffs without requiring a particular product.

Adapters describe product-specific mechanics: where state lives, how an AI reads or writes it, what persists, what can disappear, how recovery works, and where secrets must not go. Replacing an adapter should not require rewriting the Core.

## Safety and privacy

Do not put passwords, API keys, tokens, private keys, recovery codes, secret-bearing URLs, or unnecessary private account data into routine AI chat or project evidence. Keep raw/private evidence separate from sanitized derivatives when publication is possible.

## Validation

Run:

```bash
python scripts/validate.py
```

The validator checks the public-candidate Core identity, candidate version, exact Apache-2.0 license identity, complete package structure, non-empty Markdown, template/adapter/document/example structure, basic scope markers, package integrity, and generic secret/private-reference patterns. Mechanical checks do not replace human review for clarity, secrets, or release scope.

## Current scope

This tree packages **HAPW v0.2 public candidate** as a licensed release candidate. Public release still requires final release-safety review, a fresh unrelated-project bootstrap/recovery validation against these frozen bytes, and explicit release authorization.
