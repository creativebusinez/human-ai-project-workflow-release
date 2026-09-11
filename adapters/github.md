# Adapter: GitHub

## Adapter name/version

HAPW GitHub Adapter 0.1 — candidate package guidance.

## Functions implemented

Version-controlled durable state, implementation/source authority, commit-addressable checkpoints, change history, and fresh-session recovery from a designated repository/branch/file set.

## Authority role

A declared GitHub repository, branch, and file set may be authoritative for project state or for a narrower class such as source code, tests, schemas, sanitized configuration, and CI.

Examples:

```text
Authoritative project state: owner/repository @ main / project-control/
```

or a split role:

```text
project state -> durable document store
implementation -> owner/repository @ main
```

Authority comes from the project contract, not from GitHub merely containing a copy.

## Non-authority role

GitHub does not automatically own project decisions, private evidence, credentials, large raw artifacts, or every document referenced by the repository. A README, issue, PR description, local clone, fork, branch, or exported archive is not current authority unless explicitly assigned that role.

Do not keep the same current project fact independently authoritative in GitHub and another store.

## Persistence model

Committed repository content is addressed through Git objects and refs. Commits provide durable history, but branch refs can move and repository settings/permissions can change. Uncommitted local working-tree changes are not durable repository state.

A commit SHA is a stronger continuation reference than an unqualified statement such as “latest main” when exact implementation identity matters.

## Minimum setup

1. Create or select a repository appropriate to the project and choose its visibility deliberately.
2. Establish the authoritative branch and paths.
3. Record the repository/branch/path role in project state.
4. Verify the operator/AI has the minimum read/write permission required.
5. Protect secrets from repository content and history.
6. Avoid branch/PR/issue ceremony unless it serves a concrete review, collaboration, rollback, or policy need.

## Read/write capabilities

Read current authoritative files from the declared branch or exact commit. Durable writes require committing the changed state and updating the intended branch/ref through the available Git client, API, or connector.

After a material write, verify the resulting commit and relevant file/blob identities. For read-only recovery, do not create a “cleanup” or “checkpoint” commit merely to prove access.

Some integrations can read/write repository contents but cannot create repositories, change visibility, manage branch protection, or perform other administrative actions. Verify the actual integration rather than assuming those capabilities.

## Authentication / secret boundary

Use GitHub account/repository permissions and an appropriate credential mechanism for access. Keep tokens, SSH private keys, passwords, recovery codes, OAuth secrets, and other credentials out of repository files and commit history.

Use a platform secret store, local credential manager, environment injection, or another protected mechanism for automation secrets. Public repositories require an additional publication/safety review; making a repository public is a separate authorization decision.

## Artifact references

For exact implementation identity, record:

- repository identity;
- branch when relevant;
- commit SHA;
- file path;
- blob/tree/hash identity when exact bytes materially matter.

Use repository-relative links for nearby package files. Large/private evidence may live elsewhere with a durable reference from the owning project record rather than being copied into Git history.

## Known limitations

- Repository discovery may fail when names/permissions are ambiguous.
- A connector may have read but not write/admin/repository-creation capability.
- Wrong branch or fork selection can recover stale state.
- Local uncommitted changes are invisible to fresh sessions.
- Force-push or ref movement can invalidate an assumed branch history.
- Binary/large-file handling may differ from normal text-file operations.
- Private repository access may not carry into a fresh AI session.
- Excessive PR/issue/branch machinery can add burden without improving durability.
- Git history is a poor secret-removal mechanism; committing a secret and deleting it later is not equivalent to never committing it.

## Product/version/date scope

This adapter describes GitHub/Git repository behavior and HAPW usage patterns, not one fixed GitHub UI or AI connector. Current REST/API permissions, Actions behavior, branch rules, repository settings, authentication methods, and connector capabilities must be verified when material.

## Recovery procedure

In a fresh session:

1. Identify the declared repository and authority role.
2. Resolve the authoritative branch or exact commit.
3. Locate the project-control or implementation files without asking the user to repeat recoverable state.
4. Read the goal/current state/next action/decisions or the implementation identity relevant to the assigned role.
5. Distinguish committed facts from interpretation and from uncommitted/local-only work.
6. State the recovered stop point, exact next action, and material repository/file/commit references.
7. Keep recovery read-only unless continuation is authorized.

## Failure modes

- **Adapter discovery failure:** the fresh session cannot locate the declared repository/state.
- **Adapter read failure:** known committed state exists but cannot be read.
- **Adapter write failure:** intended authoritative state cannot be committed/updated.
- **Wrong ref:** stale branch, fork, tag, or commit is treated as current.
- **Dual authority:** GitHub and another store both maintain competing current copies.
- **Uncommitted-state loss:** important work exists only in a local working tree.
- **Permission drift:** repository access available in one session is absent in another.
- **History mutation:** force updates or destructive rewrites break expected continuation references.
- **Secret exposure:** sensitive values enter tracked files or history.

## Portability / exit path

Capture the exact repository and commit identity, then clone/export/copy the authoritative paths with history when history is required. Verify important file hashes or Git object identities in the destination, test fresh recovery there, and explicitly change the project authority declaration. Retain the source repository as historical/read-only or retire its authority role so both systems do not continue as independent living state.

## Irreducible user action

If direct tool access cannot create/select the repository, grant access, change visibility, satisfy an organization policy, or perform another required administrative action, the user or authorized administrator must do that bounded step. The AI should minimize that burden and must not claim the action occurred until it can verify the result.
