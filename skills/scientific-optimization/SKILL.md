---
name: scientific-optimization
description: Design or compare scientific and computational mechanisms through first-principles mathematics, algorithms, numerical analysis and whole compute-storage costs. Use for a bounded research or performance question, from formulation to defensible evidence and a planning handoff.
---

# Scientific optimization

Find the simplest mechanism that materially improves the real decision. Work at the requested scope, preserving the existing end-to-end chain and data contracts. Scale the analysis to the dominant uncertainty; the six rules below are decision criteria, not a demand for six separate reports.

## 1. Model the actual problem

- State the decision, objective, variables, constraints, validity domain, required accuracy and available time, memory and data.
- Make physical semantics, units and time basis explicit; distinguish the desired outcome from the optimized proxy.
- Identify what is observable or identifiable, which assumptions are testable, and which unknown most limits progress.

## 2. Locate the contribution

- Examine the closest primary research, existing systems and strongest relevant simple and established baselines; retain sources, versions and search cut-off.
- State the precise proposed difference and why it could matter. Separate established knowledge, derivation and hypothesis, including missing evidence or access.
- Treat originality and publishability as conclusions requiring comparison and evidence. Reuse the best existing solution when a new mechanism offers no defensible advantage.

## 3. Remove work through structure

- Derive the mechanism before tuning its implementation. Look for useful invariants, symmetry, separability, sparsity, sufficient statistics, dimensional reduction or analytic reformulation.
- Consider algorithms and data structures together: representation, incremental updates, avoided enumeration and reusable computation can change the work required.
- For each proposed reduction, state why the answer is preserved or bound the introduced error. A simpler model must retain the decision-relevant mechanism.
- Use approximation only with an explicit accuracy/cost tradeoff; identify assumptions that make the shortcut invalid.

## 4. Count the whole cost

- Compare genuinely different candidates on time, space, error and scaling for the expected workload, including a simple baseline.
- Distinguish asymptotic, worst-case, amortized and measured costs where each affects the decision; expose constants and workload assumptions that can reverse the ranking.
- Include data acquisition, preprocessing, storage, memory traffic, I/O, communication and repeated execution when material. Evaluate precomputation or caching over its useful lifetime, including construction, refresh and invalidation.
- Check whether a compute saving survives memory capacity, bandwidth, latency, synchronization and data-change costs. State the break-even conditions for the tradeoff.

## 5. Preserve numerical reliability

- Separate problem conditioning from algorithmic stability; account for finite precision, scaling and error propagation where they affect the answer.
- Relate residuals and convergence criteria to solution error and the actual decision. State tolerances, validity limits and relevant failure regimes.
- Claim optimality only within the stated model and assumptions, supported by proof or a justified bound. Distinguish local solutions, heuristics and empirical superiority.

## 6. Make the evidence decisive

- Select the simplest candidate supported by the current tradeoffs. Identify the smallest experiment or proof that could reject it before extending scope.
- Fix the comparison, target accuracy, resource budget, stopping criteria and interpretation before observing results. Compare baselines fairly, including their tuning and preprocessing costs.
- Use representative conditions, uncertainty estimates, ablations and adverse cases as needed to isolate the claimed mechanism; prevent leakage and confounding.
- Retain provenance and reproducibility inputs. Distinguish analytical, simulated, benchmark and field evidence, and preserve negative and inconclusive results.

## Handoff

Return a concise decision and its traceable reasoning: the selected mechanism, assumptions, cost/error tradeoff, evidence strength, unresolved uncertainty and next decisive action. Keep WHAT/WHY requirements separate from derivations and candidate implementation choices so the native planning process can retain the knowledge without treating hypotheses as constraints. This skill grants no authority to implement, change scope or perform external actions.
