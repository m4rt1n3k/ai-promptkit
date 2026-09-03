# DEV|L — Develop–Delivery Spiral

DEV|L evolves an applied solution while preserving one delivery authority. External **Develop** decides what the next maturity improvement should achieve; native GitHub Spec Kit **Delivery** specifies and builds it. `|` marks that boundary.

## Evolution

```text
real-world evidence
       ↓
human maturity judgment + top-level agent selection
       ↓
DEVELOP: problem → environment → existing solutions → feasibility
       ↓
grade-appropriate WHAT/WHY prompt
       │
       │ DEV|L boundary
       ▼
DELIVERY: native Spec Kit
constitution* → specify → clarify? → plan → checklist?
             → tasks → analyze? → implement ↔ converge
       ↓
authorized real-world application
       ↺ next spiral turn

* establish once; revise only when principles change
```

Every turn begins with human judgment of current maturity. The human normally selects the corresponding agent, but may choose another lens when a different uncertainty dominates. Grades guide evolution; they are not Spec Kit acceptance gates. Evidence may repeat a grade or return the solution to an earlier one.

## Grades

| Grade | Primary agent | Evolution objective | Typical evidence at this maturity |
|-------|---------------|---------------------|-----------------------------------|
| **1 — Preliminary Mockup** | **Engineer** | Minimal working chain through existing systems, real connections and data, a transparent heuristic and safe observable application | End-to-end path works; semantics, constraints and failures are known; reusable interfaces and diagnostics exist |
| **2 — Minimum Viable Solution** | **Scientist** | Excellent core solution that addresses the underlying problem with the simplest defensible mechanism | Real-environment value exceeds credible baselines; validity, uncertainty, reproducibility and failure limits are measured |
| **3 — Versatile Systematic Solution** | **Business** | Scalable, market-ready ecosystem around validated core value | Adoption, UX, integration, operation, support and economics repeat across justified contexts |

“Excellent” or “market-ready” is an evidence claim, never a label earned merely by selecting a grade.

## One spiral turn

1. The human judges maturity and selects Engineer, Scientist or Business.
2. The agent explores the real problem, environment, current practice, existing solutions and feasibility through that grade's lens.
3. The agent returns a concise prompt; it creates no persistent artifact.
4. The human invokes native `speckit.specify`. The DEV|L preset records the maturity judgment, inherited evidence, target evolution and application target in `spec.md`.
5. Native Spec Kit exclusively performs clarification, planning, quality checks, tasking, analysis, implementation and convergence.
6. The delivered result is applied to an authorized real-world problem.
7. Observed evidence becomes input to the next feature specification and maturity judgment.

One turn should normally map to one bounded Spec Kit feature. If evidence only exposes a software defect against the current specification, remain inside the current Delivery loop instead of opening another Develop turn.

## Single artifact system

Persistent project context exists only in native Spec Kit locations:

```text
.specify/   # constitution, templates, scripts and active-feature state
specs/      # specification, plan, tasks and native supporting artifacts
```

Do not create DEV|L logs, maturity files, feature summaries, shadow plans or session records elsewhere. When prior application evidence matters, reference or summarize it in the next `spec.md`; use native supporting artifacts produced by Spec Kit commands where appropriate.

The [DEV|L preset](../spec-kit/presets/devl-spiral/README.md) appends context to native constitution, specification and plan templates. It does not replace commands or add a competing workflow.

## Takeover and session continuity

`takeover` is a one-time brownfield operation: inspect an existing codebase, initialize Spec Kit safely, install the preset and hand control to native commands. It is not a daily context-restoration prompt.

Spec Kit does not itself manage generic chat-session summaries. This kit intentionally provides no separate handoff: active feature artifacts and version control are the project record, while platform-level conversation continuity remains outside the repository workflow.

## Engineering rules

- Work with existing physical, digital, organizational and commercial reality; greenfield replacement needs evidence.
- Explore current practice, reuse, standards, open and commercial solutions before custom construction.
- Fix application criteria before observing outcomes; preserve negative and inconclusive evidence.
- Keep domain semantics, units, time basis, missingness, provenance, uncertainty and reproducibility explicit.
- Keep UX, identity, licensing, monetization and marketing policy modular around scientific/domain truth.
- Consequential real-system changes require human and environment-owner authority, monitoring and rollback.

References: [Spec Kit Quick Start](https://github.github.com/spec-kit/quickstart.html) · [Existing projects](https://github.github.com/spec-kit/guides/existing-projects.html) · [Presets](https://github.github.io/spec-kit/reference/presets.html)
