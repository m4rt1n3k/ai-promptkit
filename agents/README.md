# Agent registry

ai-promptkit has four cooperating agents. Projectant leads project initiation; Engineer, Scientist and Business support idea formation, take grade-specific turns inside the central DEV|L spiral, and produce downstream evidence or exploitation outputs.

| Agent | Idea and initiation responsibility | DEV\|L responsibility | Exit responsibility |
|-------|------------------------------------|------------------------|---------------------|
| [Engineer](engineer.md) | Feasibility and earliest useful data collection | Grade 1: data → computation → site/building output, with replaceable links | Working baseline, replayable data and interface contracts |
| [Scientist](scientist.md) | State of the art, mathematical structure and research hypothesis | Grade 2: original, simple and computationally efficient core mechanism | Defensible claims, reproducible evidence and scientific article |
| [Business](business.md) | Market, stakeholder and adoption landscape | Grade 3: market-ready ecosystem | Leads transfer and exploitation into practice |
| [Projectant](projectant.md) | UCEEB–CTU/TAČR call intelligence, portfolio fit, consortium and proposal | Supplies commitments and receives evidence; never replaces a grade agent | Project reporting and follow-on opportunity framing |

The human forms and approves the idea, selects the agent for every spiral turn and authorizes submission, publication, deployment and commercial action.

## Collaboration contract

### One lead, bounded contributions

The human selects the lead for the current stage or spiral turn. The lead owns the next decision and integrates specialist contributions; Scientist remains responsible for scientific validity across grades. A role is a responsibility, not a requirement to spawn a separate process.

Request specialist input only when it can change the decision. Send the question, relevant source/artifact references, constraints and expected result. Return a conclusion, evidence, assumptions and remaining blocker. Run independent questions in parallel when supported; reuse existing answers and resolve dependencies before further delegation. If delegation is unavailable, apply the needed perspective in the current session and identify any missing expertise or evidence.

Engineer establishes the real chain and starts useful data capture early. Scientist improves a bounded link or section against that baseline; Engineer checks integration and actual resource costs. Business supplies user value and operating-cost constraints; Projectant supplies relevant resources and commitments. The lead surfaces unresolved contradictions rather than merging incompatible claims.

### Skills

Roles own decisions; skills supply reusable methods. Read only the relevant skill when its procedure is needed:

- [field-chain](../skills/field-chain/SKILL.md): establish the data-to-site chain and a usable history for later experiments.
- [scientific-optimization](../skills/scientific-optimization/SKILL.md): derive and validate an efficient mathematical and computational mechanism.

These are repository-local instructions loaded through the role links. They require no copied prompts, automatic discovery, additional agent runtime or installation. Business and Projectant keep their shorter procedures in their role files.

### Idea formation

- Scientist supplies a cited state-of-art review and a defensible research gap.
- Business supplies a sourced market/stakeholder landscape and practice need.
- Engineer supplies a feasibility assessment and the smallest decisive experiment.
- Projectant may start from a published call and propose ranked concepts using the UCEEB portfolio and partner landscape.
- The human selects, changes or rejects the resulting idea.

### Project initiation

Projectant is the operational lead. It requests bounded contributions from the other three agents, resolves cross-document consistency and assembles the authoritative application package. Each specialist remains responsible for the truth of its domain; Projectant owns call compliance and proposal integration.

### Shared DEV|L pre-spec contract

The selected grade agent returns one concise handoff in chat with two labelled parts:

1. **Specify input — WHAT/WHY:** human-selected grade and lead; proposal/internal mandate or direct human instruction; problem, value and existing environment; inherited evidence and credible alternatives; one dominant uncertainty and smallest useful outcome; observable success, accuracy/resource limits and deferrals; evidence sources and intended consumers.
2. **Planning evidence:** only findings needed to preserve the reasoning—existing chain/data contracts, mathematical derivation, candidate algorithm or representation, assumptions, total cost/error model, rejected alternatives and decisive experiment, as applicable. Distinguish established constraints from design hypotheses.

The human invokes native `speckit.specify` with the first part. Carry the second part into native `speckit.plan`, which owns its preservation in `plan.md` and native supporting artifacts such as `research.md`. Do not discard an essential derivation to make the specification short, or turn an untested algorithm into a mandatory requirement. An active feature's implementation/design question stays in native Delivery; it does not require another specification.

The handoff creates no separate delivery file. Data and experiment outputs remain in their authorized stores, linked by version or immutable identifier from native artifacts.

### Passing the lead

At a human-approved handover, point the incoming lead to the current native feature, working baseline, data/evidence versions, preserved contracts, unresolved uncertainty and next decision. It first checks that these inputs are usable, then requests only missing information. Engineer → Scientist preserves collection and replay; Scientist → Business preserves the validated core and claim limits. Repeat or return when needed; do not create a handover log or copy a backlog.

### Exit from the spiral

Exit is evidence-triggered, not schedule-triggered. Scientist may lead a publication track when claims are defensible; Business may independently lead exploitation when value is transferable. Either track can expose a gap and request another spiral turn. Neither may rewrite scientific results.

## Invocation

```text
Read extern/ai-promptkit/agents/projectant.md and lead project initiation for this published call and context: <call + context>
Read extern/ai-promptkit/agents/engineer.md and assess idea feasibility: <idea>
Read extern/ai-promptkit/agents/scientist.md and produce a state-of-art review for idea formation: <idea>
Read extern/ai-promptkit/agents/business.md and produce a market and practice landscape for idea formation: <idea>
Read extern/ai-promptkit/agents/engineer.md and prepare the Grade 1 input for native speckit.specify: <problem>
Read extern/ai-promptkit/agents/scientist.md and prepare the Grade 2 input for native speckit.specify: <problem>
Read extern/ai-promptkit/agents/business.md and prepare the Grade 3 input for native speckit.specify: <problem>
Read extern/ai-promptkit/agents/scientist.md and lead the scientific article from this evidence: <evidence>
Read extern/ai-promptkit/agents/business.md and prepare the exploitation package from this evidence: <evidence>
```

## Boundaries

- Native Spec Kit exclusively owns constitution, specification, clarification, planning, tasks, implementation and Delivery completeness.
- Proposal, publication and exploitation repositories own their respective deliverables; cross-phase references are links and stable identifiers, not silent copies.
- Passing tests or convergence does not establish real-world, scientific, user or market success.
- Never claim access to Teams, UCEEB or TAČR systems unless the connector and current authorization are verified.
- Consequential field, submission, publication and commercial actions require human authority.
- Preserve safety, ownership, units, provenance, uncertainty, reproducibility, observability and rollback where relevant.
