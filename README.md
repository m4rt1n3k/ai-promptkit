# ai-promptkit

Kit workers for **other** project workspaces. Outputs are written to the project you have open—not into this repo.

**Clone:** `C:\Users\VLAD\HOME\CODE_m4rt1n3k\ai-promptkit` · [github.com/m4rt1n3k/ai-promptkit](https://github.com/m4rt1n3k/ai-promptkit)

## Invoke (Agent chat in your project)

```text
from workspace ai-promptkit run kit_prompt
```

```text
from workspace ai-promptkit run kit_todo
```

```text
from workspace ai-promptkit run kit_handoff
```

```text
from workspace ai-promptkit run kit_design
```

The agent reads `kits/<name>.md` from ai-promptkit and updates files at **your workspace root**.

Optional lines in the same message:

```text
session: my-label
topics: tag-one, tag-two
notes: what changed in this chat
```

## Kits

| Command | File | Writes |
|---------|------|--------|
| `kit_prompt` | [kits/kit_prompt.md](kits/kit_prompt.md) | `PROMPT.md` |
| `kit_todo` | [kits/kit_todo.md](kits/kit_todo.md) | `TODO.md` |
| `kit_handoff` | [kits/kit_handoff.md](kits/kit_handoff.md) | both |
| `kit_design` | [kits/kit_design.md](kits/kit_design.md) | `.cursor/rules/kit-design.mdc` |

Templates: [kits/templates/](kits/templates/).
