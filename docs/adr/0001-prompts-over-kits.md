# ADR-0001: Prompts library over kit workers

- Status: accepted
- Date: 2026-06-09

## Context

Legacy `kits/*.md` + root `PROMPT.md`/`MANUAL.md` did not submodule cleanly.

## Decision

1. ai-promptkit = submodule at **`extern/ai-promptkit`** (read-only).
2. Base prompts in `extern/ai-promptkit/prompts/`; project prompts in `prompts/`.
3. Onboard via **`init.md`** → creates **`prompts/handoff.md`** + **`prompts/takeover.md`** extending base prompts.
4. Daily invoke: `Run prompts/handoff.md` / `Run prompts/takeover.md` (short: `run /prompts/handoff`, `run /prompts/takeover`).
5. Docs: `docs/{manual,conventions,devlog,adr}` replace monolithic handoff files.

## Consequences

- No kit dispatcher. Paste prompts or read file paths in Agent chat.
- `git submodule update --init --recursive --remote` runs in **takeover** (daily); commit the pin when the team should move; edit project prompts locally.
