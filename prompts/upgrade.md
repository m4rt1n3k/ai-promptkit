# Upgrade — advance the pinned extension and preset

Invoke from an initialized consumer repository:

```text
Read extern/ai-promptkit/prompts/upgrade.md and run on this workspace.
```

## Task

1. Verify the registered `extern/ai-promptkit` submodule, record its committed and checked-out SHAs, and stop if it has local edits.
2. Preserve unrelated working-tree changes.
3. Advance only the tracked extension:

   ```text
   git submodule update --init --recursive extern/ai-promptkit
   git submodule update --remote --recursive extern/ai-promptkit
   ```

4. Review relevant workflow, agent, preset and compatibility changes.
5. Refresh the installed preset:

   ```text
   specify preset remove devl-spiral
   specify preset add --dev extern/ai-promptkit/spec-kit/presets/devl-spiral --priority 10
   specify preset resolve constitution-template
   specify preset resolve spec-template
   specify preset resolve plan-template
   ```

6. Run [doctor](doctor.md).

Do not change feature artifacts, application code, Spec Kit CLI version or unrelated dependencies. Do not commit or push unless asked. Report old/new SHA, relevant changes, preset resolution and residual incompatibilities.
