# Manual

Use ai-promptkit to operate the [research-to-practice cascade](research-lifecycle.md). Native Spec Kit remains the delivery system inside its central [DEV|L spiral](devl-workflow.md).

## Start from a need or idea

1. Ask Scientist for a state-of-art review.
2. Ask Business for a market and practice landscape.
3. Ask Engineer for feasibility and a decisive first experiment.
4. Reconcile the evidence with the human's problem and define proceed/revise/park/reject criteria.
5. If proceeding toward a funded or formally governed project, hand stable references to Projectant.

Do not ask Projectant to hide an unsupported gap, missing practice need or infeasible dependency behind proposal language.

## Start from a published call

1. Give Projectant the authoritative call location and the authorized UCEEB/partner context.
2. Projectant verifies source access and call version, checks eligibility and portfolio overlap, then requests bounded contributions from Scientist, Engineer and Business.
3. Review the ranked concept set and select, revise or reject it.
4. Projectant assembles the selected application and reports exact submission blockers.
5. A human/institutional owner authorizes partner contact, commitments and submission.

## Enter development

Enter with a direct human mandate or an authorized formal project. For the latter, Projectant supplies references to accepted commitments, objectives, evidence targets, milestones, partners and constraints. Record relevant provenance in the first `spec.md`; do not copy the complete proposal into Spec Kit.

## Run one spiral turn

1. Review evidence from the latest real-world application or project mandate.
2. Judge the current grade and choose its primary [agent](../agents/README.md), or explicitly choose another lens.
3. Ask that agent for the shared [handoff](../agents/README.md#shared-devl-pre-spec-contract). It reads its focused skill as needed and consults other roles only for questions that can change the decision.
4. Review the result, then invoke the installed `speckit.specify` command.
5. Supply the handoff's planning evidence to native `speckit.plan`; preserve mathematical findings and data/interface contracts in its native outputs. Continue through native Delivery according to ambiguity and risk:

   ```text
   clarify? → plan → checklist? → tasks → analyze? → implement ↔ converge
   ```

6. Apply the result in an authorized real environment.
7. Feed observed evidence into the next spiral turn and preserve stable references for project reporting, publication and exploitation.

Start directly inside the active Spec Kit feature for implementation defects or already-specified work.

## Evolution focus

- **Engineer / Grade 1:** connect collection, simple computation and output at the real site/building quickly; start authorized data capture early and keep links replaceable.
- **Scientist / Grade 2:** improve the relevant link or section with the simplest original mechanism, justified numerics and measured total cost; use the collected history for credible experiments and backtesting.
- **Business / Grade 3:** make the validated solution scalable, usable, adoptable and economically sustainable.

Repeat or return when evidence contradicts maturity. Never promote because Delivery merely converged. Projectant never substitutes for a grade agent.

At a human-approved role change, follow the [lead handover](../agents/README.md#passing-the-lead): existing feature and evidence references, baseline, contracts, unresolved uncertainty and next decision. No separate handoff file is needed.

## Open exit tracks

- Ask Scientist to lead an article only when evidence supports a bounded claim. It returns missing evidence to DEV|L or prepares the manuscript and submission package.
- Ask Business to lead exploitation only when value and operational transfer are credible. It returns missing evidence to DEV|L or prepares the practice-transfer package.
- Run the tracks independently; publication readiness is not market readiness.
- Keep submission, authorship, IP, partner outreach, contracting and deployment under explicit human authority.

## Persistent context

Use `.specify/` and `specs/` as the sole software-delivery context. Keep proposals, manuscripts and exploitation packages in their designated authoritative systems. Handoffs use links, versions and evidence identifiers; they do not create a duplicate development ledger.

`takeover` is reserved for bringing an existing non-Spec-Kit codebase under Spec Kit. It is not part of normal feature work.

## Maintenance

- Diagnose: `Read extern/ai-promptkit/prompts/doctor.md and run on this workspace.`
- Upgrade the pinned kit/preset: `Read extern/ai-promptkit/prompts/upgrade.md and run on this workspace.`
