# Session summary

Step 1 of [handoff.md](handoff.md). Copy below the line.

---

## Task: Draft commit message

Target repository (cwd = repo root). **Do not commit** unless asked.

Use **`topic - detail`** phrasing, not full sentences.

| Avoid | Prefer |
|-------|--------|
| Split AO Configurator into API/Python branches and centralize docs | configurator - API/Python branches, centralize docs |
| Add init onboarding and simplify handoff prompts | promptkit - init onboarding, slim handoff |

**Topic** = area or component (lowercase, 1–2 words). **Detail** = comma-separated phrases, no verbs needed.

### Output

Print **two separate fenced blocks** so the user can copy each independently.

**Subject** — one line only, no `Subject:` prefix:

```text
<topic - detail>
```

**Body** — bullet lines, same pattern:

```text
- <topic - detail>
- <optional topic - detail>
```

No file lists. If nothing committable, say so.

### Rules

- No sentence-style subject or bullets.
- Focus on intent and outcome, not a file manifest.
