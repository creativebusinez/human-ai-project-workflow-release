# HAPW Security and Privacy

HAPW improves continuity; it is not a secret-management system. Project records should preserve enough information to recover work without turning durable state into a credential store or unnecessary privacy risk.

## Keep secrets out of routine project state

Do not place the following in ordinary project Markdown, AI chat, screenshots, public repositories, or publishable evidence:

- passwords;
- API keys or tokens;
- OAuth secrets or authorization codes;
- SSH private keys;
- recovery codes;
- secret-bearing URLs;
- session cookies;
- private credential-file contents.

Use a dedicated secret store, credential manager, protected environment injection, or another mechanism designed for secrets. Project records may note that a credential exists and where the approved secret mechanism is, without copying the secret itself.

## Minimize private data

Preserve only the personal, account, billing, customer, or operational information needed to prove the claim or continue the work. Redact or omit unrelated data.

When screenshots or logs contain mixed public and private information, prefer a bounded sanitized derivative while retaining the raw source only in an appropriately protected evidence store when the raw artifact is actually necessary.

## Least privilege

Give humans, AI integrations, automation, and service accounts only the access required for the current task. Read-only recovery should not require write permission. Publication should not require administrative access.

Verify actual permissions and connector capabilities instead of assuming that a tool can create, delete, publish, share, or administer resources.

## Evidence safety

Before preserving evidence:

1. identify what claim the artifact needs to prove;
2. capture only the necessary scope;
3. screen for secrets and unnecessary private data;
4. store the raw artifact in the correct authority;
5. create a sanitized/public derivative separately when needed;
6. link the derivative to the raw evidence without exposing protected content.

Do not use screenshots as substitutes for original files when exact bytes are the evidence.

## Version-control safety

Version control is not secret storage. Removing a secret from the current file does not guarantee it disappeared from history.

Before committing, scan for credentials, private URLs, account data, and material that is not licensed or authorized for distribution.

## Publication boundary

Making a repository, document, or evidence package public is a separate decision from making it technically complete.

Before publication, perform a dedicated safety review for:

- secrets and credentials;
- private file or repository references;
- private validation evidence;
- unnecessary personal or account data;
- material with distribution restrictions;
- scope claims that exceed the evidence;
- licensing requirements.

A technical PASS does not authorize publication.

## Destructive and costly actions

Deletion, irreversible changes, spending, and external publication should use explicit human authorization when the action carries meaningful cost, risk, or loss of recoverability.

When possible, verify the exact target before destructive action and preserve the minimum evidence needed to prove the result afterward.
