# ADR-0001: Prompts library over kit workers

- Status: accepted
- Date: 2026-06-09

## Context

Legacy `kits/*.md` + root `PROMPT.md`/`MANUAL.md` did not submodule cleanly.

## Decision

1. ai-promptkit = submodule at **`subs/ai-promptkit`** (read-only).
2. Base prompts in `subs/ai-promptkit/prompts/`; project prompts in `prompts/`.
3. Onboard via **`init.md`** → creates **`prompts/handoff.md`** extending base handoff.
4. Daily invoke: `Run prompts/handoff.md`.
5. Docs: `docs/{manual,conventions,devlog,adr}` replace monolithic handoff files.

## Consequences

- No kit dispatcher. Paste prompts or read file paths in Agent chat.
- `git submodule update` for base prompt changes; edit project prompts locally.
