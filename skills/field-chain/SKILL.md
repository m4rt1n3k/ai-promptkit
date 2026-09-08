---
name: field-chain
description: Prepare the first complete application chain from real site data through calculation to a result returned to the site, with early continuous collection for later experiments and backtesting. Use when framing or planning initial field integration.
---

# Field chain

Make the simplest useful path work in its actual environment. Load this procedure for Engineer's field integration work; native Spec Kit owns software planning and implementation.

## Trace the whole path

- Identify the physical source, acquisition interface, existing storage, calculation, output interface and actual recipient or actuator.
- Inspect real samples and interface behavior. Separate verified access and behavior from assumptions or unavailable connections.
- Define the smallest useful result returned to the site or building: a consumed signal, operator recommendation or authorized action, according to the task.
- Locate the dominant missing link. Reuse existing systems and manual steps where they shorten the path without hiding a broken connection.

## Collect usable history early

- Prioritize authorized continuous collection in the first delivery slice; advanced modelling need not be ready first.
- Retain raw source records where permitted and usable derived data in existing authorized storage. Reference that storage from native artifacts; do not make Git the default time-series store.
- Preserve physical quantity, units, sensor identity, measurement interval, time zone, missingness, quality indicators and transformations needed to interpret each signal.
- Distinguish event time from the time a value became available. For forecasts or revised measurements, retain issue times or versions needed to reconstruct information available at a past decision without future-data leakage.
- Preserve relevant operating inputs, overrides and returned outputs alongside observations, including when they were issued or confirmed, so later analysis can relate decisions to outcomes.
- Record collection gaps, clock errors and source changes where data consumers can discover them. Never fill an unknown history with unlabelled synthetic observations.
- Check sampling, retention and access against the intended later experiment. State limitations that make a retrospective test impossible or biased.

## Establish a transparent baseline

- Use the simplest calculation or heuristic that gives the site a useful result. State its assumptions and meaningful failure limits.
- Trace a real input through calculation to the receiving interface; verify its units, time basis and interpretation at the destination.
- Make stale input, missing data, calculation failure and rejected output observable. Define a proportionate fallback to the existing workflow.
- Distinguish a calculated recommendation, a transmitted command and confirmed physical execution; claim only the stage actually observed.
- A working chain proves integration; its scientific advantage remains a separate evidence question.
- Use the current authorized scope. If a required field action exceeds it, identify that specific action for an owner decision; continue unaffected work.
- Keep the operational change reversible through the existing control or deployment mechanism. A real actuator is needed only when the task requires it.

## Leave scientific improvement possible

- Define thin input/output contracts around replaceable calculations or chain sections: meaning, shape, timing and relevant resource limits.
- Keep acquisition and output adapters separate from scientific calculation where this enables a demonstrated substitution; avoid a generalized platform.
- Retain the baseline version, configuration and representative authorized samples or references needed to reproduce its behavior.
- Expose measured latency, memory, throughput or other resource constraints only where they affect the scientific choice or field use.
- Give Scientist the real data limits, baseline, observed failures and a bounded question. An improved method must fit the chain or make the required interface change explicit.

## Hand over once

Use the shared [DEV|L pre-spec handoff](../../agents/README.md#shared-devl-pre-spec-contract):

- WHAT/WHY: complete path, first useful result, dominant uncertainty, observable success and explicit deferrals.
- Planning evidence: verified interfaces, baseline, data semantics and availability, storage references, resource limits, failure behavior and unresolved dependencies.

Keep this handoff in chat until native Spec Kit persists the relevant context in its specification and planning artifacts. Existing authorized data systems retain measurements; native artifacts retain references and the knowledge needed to use them.
