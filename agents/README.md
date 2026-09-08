# Agent registry

ai-promptkit has four cooperating agents. Projectant leads project initiation; Engineer, Scientist and Business support idea formation, take grade-specific turns inside the central DEV|L spiral, and produce downstream evidence or exploitation outputs.

| Agent | Idea and initiation responsibility | DEV\|L responsibility | Exit responsibility |
|-------|------------------------------------|------------------------|---------------------|
| [Engineer](engineer.md) | Technical and operational feasibility | Grade 1: minimal working chain | Reproducible technical package |
| [Scientist](scientist.md) | State-of-art review, gap and hypotheses | Grade 2: defensible core solution | Leads and assures the scientific article |
| [Business](business.md) | Market, stakeholder and adoption landscape | Grade 3: market-ready ecosystem | Leads transfer and exploitation into practice |
| [Projectant](projectant.md) | UCEEB–CTU/TAČR call intelligence, portfolio fit, consortium and proposal | Supplies commitments and receives evidence; never replaces a grade agent | Project reporting and follow-on opportunity framing |

The human forms and approves the idea, selects the agent for every spiral turn and authorizes submission, publication, deployment and commercial action.

## Collaboration contract

### Idea formation

- Scientist supplies a cited state-of-art review and a defensible research gap.
- Business supplies a sourced market/stakeholder landscape and practice need.
- Engineer supplies a feasibility assessment and the smallest decisive experiment.
- Projectant may start from a published call and propose ranked concepts using the UCEEB portfolio and partner landscape.
- The human selects, changes or rejects the resulting idea.

### Project initiation

Projectant is the operational lead. It requests bounded contributions from the other three agents, resolves cross-document consistency and assembles the authoritative application package. Each specialist remains responsible for the truth of its domain; Projectant owns call compliance and proposal integration.

### Shared DEV|L pre-spec contract

The selected grade agent returns one concise prompt for native `speckit.specify` containing:

- human-selected grade and agent;
- initiation provenance, project commitments and inherited real-world evidence;
- actual problem, actors, value and current practice;
- existing physical, digital, organizational and commercial environment;
- credible existing solutions and reuse/integrate/build feasibility;
- the smallest grade-appropriate outcome for this turn;
- observable real-world success, uncertainty, constraints and explicit deferrals;
- evidence that must be preserved for scientific dissemination and business exploitation.

The agent creates no parallel delivery artifact. The human invokes installed Spec Kit, which persists approved development context in the feature specification.

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
