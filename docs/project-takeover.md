# Project takeover

## New project

Install Spec Kit from its official [installation guide](https://github.github.com/spec-kit/installation.html). Select the active coding agent's integration key, then from the project root:

```text
specify init . --non-interactive --integration <key>
git submodule add -b main https://github.com/m4rt1n3k/ai-promptkit.git extern/ai-promptkit
specify preset add --dev extern/ai-promptkit/spec-kit/presets/devl-spiral --priority 10
```

Verify all three native templates resolve through the preset:

```text
specify preset resolve constitution-template
specify preset resolve spec-template
specify preset resolve plan-template
```

Inspect the resolution output for `devl-spiral`, a native base and no composition warning; an exit code alone is insufficient. Run [doctor](../prompts/doctor.md) to check the installed preset against its source.

Establish the native constitution. Reference an authorized project mandate, including a direct human assignment; Projectant is needed when formal project initiation is required. If no mandate exists, return to [idea formation](research-lifecycle.md). The human judges the first maturity grade, chooses an [agent](../agents/README.md), and invokes native `speckit.specify` with its output.

Engineer establishes the smallest data-to-computation-to-building-output chain and early data collection for later backtesting. Scientist uses that evidence to improve a selected component through mathematics, numerical methods, algorithms and data structures, with measured accuracy and resource cost. Each role loads its linked procedure on demand.

## Existing codebase without Spec Kit

Start from a clean, reviewable working tree, add the pinned kit, then invoke the one-time takeover:

```text
git submodule add -b main https://github.com/m4rt1n3k/ai-promptkit.git extern/ai-promptkit
```

```text
Read extern/ai-promptkit/prompts/takeover.md and incorporate Spec Kit into this workspace.
```

Takeover follows the official [existing-project guidance](https://github.github.com/spec-kit/guides/existing-projects.html), reviews collisions before forced initialization, installs the preset and stops at the first native command.

## Existing Spec Kit project

Add the submodule and preset using the corresponding commands above; do not run `specify init` again. Verify resolution, then deliberately update the native constitution if the DEV|L principles should apply. Preset installation preserves a human-authored constitution; a generated template may be refreshed by native Spec Kit.

## Result

```text
.specify/                       # native Spec Kit plus installed preset
specs/                          # native features when created
extern/ai-promptkit/            # pinned extension source
```

Only the preset is copied by native Spec Kit. No project wrappers, maturity files, development logs or agent/skill installations are created.

## Version policy

The committed submodule SHA pins the extension and preset source. Use [upgrade](../prompts/upgrade.md) deliberately; normal feature work never advances it. An authorized upgrade remains pending until its new gitlink is committed. Doctor distinguishes this expected pending pin from unexplained drift and checks that the installed copy matches the selected source.
