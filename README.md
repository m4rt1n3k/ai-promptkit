# ai-promptkit

Agentic operating model for applied scientific software: from an evidence-backed idea and project proposal, through iterative development, to a scientific paper and transfer into practice.

The **DEV|L — Develop–Delivery Spiral** remains the central execution engine. Project initiation supplies its mandate; dissemination and business exploitation consume only evidence produced by it.

```mermaid
flowchart LR
    CALL[Published call] --> SCOUT[Projectant<br/>call + portfolio scan]
    SCOUT --> IDEA
    H[Human problem or opportunity] --> IDEA
    S0[Scientist<br/>state-of-art review] --> IDEA[Evidence-backed idea]
    B0[Business<br/>market landscape] --> IDEA
    E0[Engineer<br/>feasibility] --> IDEA
    IDEA --> P[Projectant<br/>proposal + consortium]
    P --> START{Authorized project start}
    START -- revise / no-go --> IDEA
    START -- go --> D

    subgraph SPIRAL[Central DEV|L development spiral]
        direction LR
        D[Develop<br/>maturity judgment + agent] --> SK[Native Spec Kit]
        SK --> DEL[Deliver]
        DEL --> APP[Authorized real-world application]
        APP --> EVID{Evidence sufficient?}
        EVID -- next turn --> D
    end

    EVID -- defensible result --> PAPER[Scientist<br/>scientific article]
    EVID -- transferable value --> BIZ[Business<br/>exploitation package]
    PAPER --> IMPACT[Knowledge and practice]
    BIZ --> IMPACT
    PAPER -. evidence gap .-> D
    BIZ -. transfer gap .-> D
    IMPACT -. new evidence or need .-> IDEA
```

Inside the spiral, maturity evolves through three reversible grades:

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

The grades express evolution, not automatic promotion. Evidence may require repetition or return. The human authorizes project entry, consequential actions, publication claims and business transfer.

Native `.specify/` and `specs/` artifacts remain the exclusive authority for software delivery. Proposal, publication and exploitation outputs live in their designated authoritative systems and reference development evidence; they never become shadow specifications, plans or logs.

## Start

- Full lifecycle: follow the [research-to-practice cascade](docs/research-lifecycle.md).
- New or existing codebase: follow [project takeover](docs/project-takeover.md).
- One spiral turn: choose [Engineer, Scientist, or Business](agents/README.md), then invoke native `speckit.specify` with the prepared input.
- Published call or project application: invoke [Projectant](agents/projectant.md).

## Repository

```text
agents/      # four lifecycle roles and their collaboration contracts
docs/        # lifecycle, DEV|L, setup, conventions and decisions
prompts/     # one-time takeover and integration maintenance
spec-kit/    # append-only DEV|L preset
```
