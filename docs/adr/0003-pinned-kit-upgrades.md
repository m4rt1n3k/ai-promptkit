# ADR-0003: Pinned extension and preset upgrades

- Status: accepted
- Date: 2026-09-02

## Context

Implicit extension updates make feature work non-reproducible and can separate an installed preset from its source.

## Decision

1. Consumer repositories pin ai-promptkit through the committed submodule SHA.
2. Normal Spec Kit work never updates that pointer.
3. Explicit upgrade advances the submodule, reinstalls the local preset, verifies template resolution and runs the read-only doctor.
4. The new pointer is committed only after human acceptance.

## Consequences

- Workflow changes are visible dependency updates.
- Preset/source drift is detectable.
- Consumers receive no implicit upgrades.
