# Manual

Use ai-promptkit only to frame maturity evolution around native Spec Kit. Setup is in [project takeover](project-takeover.md); semantics are in [DEV|L](devl-workflow.md).

## Run one spiral turn

1. Review evidence from the latest real-world application or current system.
2. Judge the current grade and choose its primary [agent](../agents/README.md), or explicitly choose another lens.
3. Ask that agent for one native `speckit.specify` prompt.
4. Review the result, then invoke the installed `speckit.specify` command.
5. Continue through native Delivery according to ambiguity and risk:

   ```text
   clarify? → plan → checklist? → tasks → analyze? → implement ↔ converge
   ```

6. Apply the result in an authorized real environment.
7. Feed the observed evidence into the next spiral turn. Do not create a separate DEV|L report.

Start directly inside the active Spec Kit feature for implementation defects or already-specified work.

## Evolution focus

- **Engineer / Grade 1:** make the smallest real end-to-end chain work.
- **Scientist / Grade 2:** make the core solution exceptionally sound, effective and defensible.
- **Business / Grade 3:** make the validated solution scalable, usable, adoptable and economically sustainable.

Repeat or return when evidence contradicts maturity. Never promote because the previous Delivery merely converged.

## Persistent context

Use only `.specify/` and `specs/`. Resume work from the active feature, its native artifacts and version-control state. ai-promptkit intentionally creates no session log, development ledger, duplicate specification or handoff artifact.

`takeover` is reserved for bringing an existing non-Spec-Kit codebase under Spec Kit. It is not part of normal feature work.

## Maintenance

- Diagnose: `Read extern/ai-promptkit/prompts/doctor.md and run on this workspace.`
- Upgrade the pinned kit/preset: `Read extern/ai-promptkit/prompts/upgrade.md and run on this workspace.`
