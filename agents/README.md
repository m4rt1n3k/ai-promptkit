# Agent registry

DEV|L has three top-level perspectives aligned with solution evolution. At the start of every spiral turn, the human judges current maturity and chooses the agent that will prepare input for native `speckit.specify`.

| Grade | Agent | Evolution objective |
|-------|-------|---------------------|
| **1 — Preliminary Mockup** | [Engineer](engineer.md) | Establish the smallest complete working chain through real connections, representative data, transparent heuristics and safe application |
| **2 — Minimum Viable Solution** | [Scientist](scientist.md) | Turn the working chain into an excellent, scientifically defensible core solution with measured validity and uncertainty |
| **3 — Versatile Systematic Solution** | [Business](business.md) | Turn validated core value into a scalable, attractive and market-ready ecosystem with repeatable adoption and economics |

The expected direction is Engineer → Scientist → Business, but this is not a gate sequence. Evidence may justify repeating a grade, returning to an earlier one, or choosing another lens for a specific uncertainty. The human decides.

## Shared pre-spec contract

The selected agent returns one concise prompt for native `speckit.specify` containing:

- human-selected grade and agent;
- evidence inherited from the preceding real-world application, if any;
- actual problem, actors, value and current practice;
- existing physical, digital, organizational and commercial environment;
- credible existing solutions and reuse/integrate/build feasibility;
- the smallest grade-appropriate outcome for this turn;
- observable real-world success, uncertainty, constraints and explicit deferrals.

The agent does not create or edit a parallel artifact. The human invokes the installed Spec Kit command, which persists the approved context in the feature specification.

## Invocation

```text
Read extern/ai-promptkit/agents/engineer.md and prepare the Grade 1 input for native speckit.specify: <problem>
Read extern/ai-promptkit/agents/scientist.md and prepare the Grade 2 input for native speckit.specify: <problem>
Read extern/ai-promptkit/agents/business.md and prepare the Grade 3 input for native speckit.specify: <problem>
```

## Boundaries

- Spec Kit exclusively owns constitution, specification, clarification, planning, tasks, implementation and Delivery completeness.
- No DEV|L record exists outside native Spec Kit artifacts.
- Passing tests or convergence does not establish real-world, scientific, user or market success.
- Consequential field and commercial actions require human authority.
- Preserve safety, ownership, units, provenance, uncertainty, reproducibility, observability and rollback where relevant.
