# Research-to-practice cascade

ai-promptkit coordinates one lifecycle around a central iterative engine:

```text
published call ─┐
human need ─────┼→ IDEA → PROJECT INITIATION → [ DEV|L SPIRAL ] → EVIDENCE
portfolio ──────┘          Projectant             ↺               ├→ ARTICLE · Scientist
                                                                  └→ PRACTICE · Business
```

Project initiation, scientific dissemination and business exploitation are lifecycle stages, not additional software-delivery systems. Native Spec Kit remains the sole authority inside the DEV|L spiral.

## Stage 0 — form an evidence-backed idea

The human owns the problem and decision. Three specialist agents challenge and strengthen it:

| Contribution | Lead | Minimum output |
|--------------|------|----------------|
| Scientific justification | Scientist | Cited state of the art, closest work, gap, hypothesis and claim limits |
| Practice and market justification | Business | Sourced stakeholder need, alternatives, market structure, partner patterns and adoption risks |
| Feasibility | Engineer | Existing-system fit, data/resources, constraints, risks, cost/effort range and decisive first experiment |

The result is an **idea dossier**: problem, beneficiary, mechanism, novelty/value, current alternatives, feasibility, evidence needed, critical assumptions and rejection criteria. It may remain in chat until the human selects an authoritative project workspace.

A call-led path is also valid: Projectant reads a concrete published call, maps it against UCEEB capabilities, portfolio and partners, requests the three contributions above, and offers a ranked set of concepts. It does not select the project.

**Exit decision:** the human records proceed, revise, park or reject. Unsupported novelty, unavailable data, missing capability or absent practice need are reasons to revise or stop.

## Stage 1 — initiate the project

Projectant leads against a frozen call version and an authoritative proposal workspace. It:

1. validates eligibility and extracts every evaluation and formal requirement;
2. checks existing/ongoing UCEEB projects and global analogues for reuse, overlap and differentiation;
3. designs a capability-based consortium using confirmed internal and external partner facts;
4. requests and reconciles scientific, engineering and business contributions;
5. builds objectives, work packages, outputs, outcomes, indicators, schedule, budget, risks, governance, data/IP, dissemination and exploitation;
6. maintains requirement-to-application traceability and reports submission blockers.

The partner space is not limited to companies. Municipalities, regions, public bodies, infrastructure operators, regulators and other research organizations are considered where their real role improves call fit and impact.

**Exit decision:** authorized project start requires an executable scope, credible resources and partners, resolved institutional approvals and a traceable application or internal mandate. Proposal submission and commitments are human/institutional actions.

## Stage 2 — run the central DEV|L spiral

Projectant hands stable references to project objectives, commitments, evidence targets, deliverables, milestones and constraints into the first relevant feature specification. Development then follows [DEV|L](devl-workflow.md):

```text
human maturity judgment → Engineer | Scientist | Business
        → pre-spec prompt → native Spec Kit Delivery
        → authorized real-world application → evidence → next judgment
```

Each turn is bounded by one dominant uncertainty. Project schedule does not force a maturity grade, and completion of a feature does not prove a scientific or market claim.

## Stage 3A — disseminate as a scientific article

Scientist leads when the claims–evidence chain is defensible. It audits reproducibility, creates a claims–evidence–figure matrix, coordinates the manuscript and supporting artifacts, verifies claim limits and prepares a submission-ready package. Engineer, Business and Projectant supply requested facts. Human owners approve authorship, IP, ethics, venue and submission.

A missing control, weak validity domain or irreproducible result returns to the spiral; it is not repaired rhetorically.

## Stage 3B — transfer into practice

Business leads when value can be transferred responsibly. It prepares the exploitation package: target use, stakeholders, evidence strength, operating model, partner route, IP/licensing options, economics, adoption, procurement/regulatory constraints, pilots and decision gates. Scientist validates claims, Engineer validates delivery/operation and Projectant validates project and partner constraints.

Scientific publication and business exploitation are independent parallel tracks. Either, both or neither may be ready. A commercial deadline cannot suppress negative scientific evidence.

## Portfolio and feedback

Projectant uses authorized UCEEB project and partner sources as a living portfolio, always with a point-in-time snapshot. Scientist supplies comparable global research/projects; Business assesses partner and adoption fit; Engineer identifies reusable technical assets and capacity dependencies. Completed papers, deployments, rejected assumptions and partner feedback update the portfolio and may seed a new idea or another spiral turn.

## Artifact authority

| Information | Authoritative home |
|-------------|--------------------|
| Software principles, features, plans, tasks and implementation evidence | Native `.specify/`, `specs/`, code and version control |
| Call interpretation, proposal, budget and partner confirmations | Designated proposal system / UCEEB workspace / TAČR system |
| State-of-art evidence and manuscript | Designated research/publication workspace |
| Exploitation, market and transfer package | Designated business/project workspace |
| Institutional portfolio and partner data | Authorized UCEEB source systems |

Cross-phase handoffs use stable links, identifiers, versions and evidence snapshots. Do not create a second software backlog or silently copy mutable institutional facts.

## Common evidence envelope

Every agent contribution states: source, retrieval or cut-off date, applicable version, fact versus inference versus assumption, uncertainty, owner/permission where relevant, and the decision the evidence supports. Missing access is an explicit limitation, never an invitation to invent data.
