# ai-promptkit

Engineering-scientific extension for projects delivered strictly through GitHub Spec Kit.

**DEV|L — Develop–Delivery Spiral** evolves a real-world solution through three maturity grades:

```text
Grade 1 · Engineer  → minimal working chain
Grade 2 · Scientist → excellent, defensible core solution
Grade 3 · Business  → scalable, market-ready ecosystem
                              ↕
human maturity judgment at every spiral turn
                              ↓
problem + environment + existing solutions + feasibility
                              ↓
native Spec Kit Delivery → real-world application → next turn
```

The sequence expresses evolution, not automatic promotion. A grade may repeat or move backward when evidence demands it. The human judges maturity and selects the top-level agent for each turn.

All persistent project context stays in native `.specify/` and `specs/` artifacts. ai-promptkit adds only three pre-spec perspectives and an append-only Spec Kit preset; it creates no parallel development logs, specifications, plans, tasks, session wrappers, or agent hierarchy.

## Start

- New project: follow [project takeover](docs/project-takeover.md).
- Existing codebase without Spec Kit: add this repository at `extern/ai-promptkit`, then run `Read extern/ai-promptkit/prompts/takeover.md and incorporate Spec Kit into this workspace.`
- Next feature: choose [Engineer, Scientist, or Business](agents/README.md), then invoke native `speckit.specify` with the prepared input.

## Repository

```text
agents/      # three maturity-oriented pre-spec perspectives
docs/        # workflow, project takeover, conventions, decisions
prompts/     # one-time takeover and integration maintenance
spec-kit/    # append-only DEV|L preset
```
