# HAPW Limitations

HAPW v0.2 is a **candidate**, not HAPW 1.0. This starter package is still being validated and should be treated as bounded workflow guidance rather than a universal project-management standard.

## It does not fit every project unchanged

Projects vary in risk, regulation, collaboration needs, data sensitivity, and operational complexity. The minimum four-file spine is intentionally small; some projects will need additional controls, while very small tasks may need less ceremony.

HAPW does not claim to work for every project or domain without adaptation.

## Durable state still depends on real storage

Declaring authority does not make storage durable. Files can be deleted, permissions can change, mounts can disappear, repositories can become inaccessible, and cloud services can fail.

Backup, retention, disaster recovery, and access-control requirements remain separate engineering decisions.

## AI access is tool-dependent

An AI assistant may be able to read a system but not write it, or may have partial, cached, indexed, or session-specific access. Product capabilities change over time.

Adapters describe the HAPW role of a system; they do not guarantee that every AI product or connector exposes every required operation.

## Recovery quality depends on record quality

A fresh session cannot recover facts that were never preserved, and it should not invent missing evidence. Poorly scoped authority, ambiguous stop points, stale current-state files, or competing copies can still create failure.

## Evidence does not guarantee correctness

Preserving evidence improves auditability, but an observed result can still be misinterpreted. Validation claims must remain scoped to the tested version, environment, data, hardware, workflow, or other relevant boundary.

## HAPW is not a substitute for specialized controls

HAPW does not replace:

- legal or regulatory compliance programs;
- professional safety review;
- access-control and secret-management systems;
- formal backup/disaster-recovery systems;
- source-control policy;
- issue tracking or project-management software when those are genuinely needed;
- domain-specific validation standards.

It can reference or coordinate those systems, but it should not pretend to provide their guarantees.

## Process burden can exceed value

More records are not automatically better. Over-documentation, excessive checkpoints, unnecessary branches, redundant screenshots, or formal experiments for trivial decisions can slow the work and make recovery harder.

Use the minimum sufficient control and evidence for the actual risk and complexity.

## License boundary

This release-candidate package is licensed under the **Apache License, Version 2.0** (`Apache-2.0`). The exact license text is included at the repository root as `LICENSE`.

## Current validation boundary

This candidate package has mechanical integrity checks and prior workflow-development evidence. Before public release it still requires the final publication-safety review of the complete licensed frozen bundle and a fresh unrelated-project bootstrap/recovery validation.

Passing those gates would still support only the tested scope; it would not establish universal validity.
