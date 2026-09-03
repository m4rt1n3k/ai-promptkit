# Project takeover

## New project

Install Spec Kit from its official [installation guide](https://github.github.com/spec-kit/installation.html), then from the project root:

```text
specify init .
git submodule add -b main https://github.com/m4rt1n3k/ai-promptkit.git extern/ai-promptkit
specify preset add --dev extern/ai-promptkit/spec-kit/presets/devl-spiral --priority 10
```

Verify all three native templates resolve through the preset:

```text
specify preset resolve constitution-template
specify preset resolve spec-template
specify preset resolve plan-template
```

Establish the native constitution, judge the first maturity grade, choose an [agent](../agents/README.md), and invoke native `speckit.specify` with its output.

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

Add the submodule and preset using the new-project commands, verify resolution, then deliberately update the native constitution if the DEV|L principles should apply. Preset installation does not silently rewrite an existing constitution.

## Result

```text
.specify/                       # native Spec Kit plus installed preset
specs/                          # native features when created
extern/ai-promptkit/            # pinned extension source
```

No project wrappers, maturity files, development logs or ai-promptkit copies are created.

## Version policy

The committed submodule SHA pins the extension and preset source. Use [upgrade](../prompts/upgrade.md) deliberately; normal feature work never advances it.
