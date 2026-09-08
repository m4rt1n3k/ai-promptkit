# Takeover — incorporate an existing codebase into Spec Kit

Invoke once from a codebase that does not yet use Spec Kit:

```text
Read extern/ai-promptkit/prompts/takeover.md and incorporate Spec Kit into this workspace.
```

## Task

Adopt native Spec Kit safely without creating parallel project context.

### 1. Preflight

- Read `git status`; preserve unrelated and uncommitted work.
- Verify `specify version` and the pinned `extern/ai-promptkit` submodule.
- If `.specify/` already exists, do not reinitialize. Run [doctor](doctor.md) and report the next native command.
- Identify the active coding-agent integration from the current environment. If it is ambiguous, ask the human for its Spec Kit integration key.

### 2. Understand only what initialization needs

Inspect the existing repository read-only for language/toolchain, entry points, run/test commands, architecture boundaries, safety constraints and files that may collide with Spec Kit initialization. Do not persist a separate analysis or backlog.

Before any forced overwrite, list exact conflicting targets and request approval. Start from a clean, reviewable baseline where possible.

### 3. Initialize native Spec Kit

Follow the official existing-project procedure using the selected integration:

```text
specify init --here --force --integration <key>
```

Review generated changes immediately. Do not alter application code or unrelated documentation.

### 4. Install the DEV|L preset

```text
specify preset add --dev extern/ai-promptkit/spec-kit/presets/devl-spiral --priority 10
specify preset resolve constitution-template
specify preset resolve spec-template
specify preset resolve plan-template
```

All three resolutions must include `devl-spiral` and preserve native templates.

### 5. Hand control to Spec Kit

From inspected repository facts, prepare in chat only a concise proposal of durable principles for the native constitution command. Do not write a custom constitution or analysis file.

Output:

1. initialization and preset status;
2. generated files and reviewed collisions;
3. unresolved safety or repository facts;
4. proposed constitution principles;
5. exact next native constitution command;
6. request for initiation provenance; if none exists, route the human to idea formation and Projectant, otherwise request the first maturity judgment and grade-agent selection before `speckit.specify`.

### Constraints

- Create only native Spec Kit output and the installed DEV|L preset.
- Do not create project wrappers, logs, TODOs, ADRs, summaries or DEV|L context files.
- Do not commit, push, deploy, upgrade unrelated dependencies or modify application behavior.
- `takeover` is not used for daily sessions or an already initialized project.
