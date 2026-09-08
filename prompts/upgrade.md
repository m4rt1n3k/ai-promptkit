# Upgrade — advance the pinned extension and preset

Invoke from an initialized consumer repository:

```text
Read extern/ai-promptkit/prompts/upgrade.md and run on this workspace.
```

## Task

1. Verify the registered `extern/ai-promptkit` submodule and record its committed, staged and checked-out SHAs. Stop on local edits or an unexplained SHA mismatch. Record the installed preset's version, priority and enabled state; resolve any existing source/install drift before upgrading.
2. Preserve unrelated working-tree changes. Keep the previous preset files and settings in a temporary location for recovery; do not add backup files to project context.
3. For a new upgrade, initialize the submodule at its pinned SHA only if needed, then advance only this extension:

   ```text
   git submodule update --init --recursive extern/ai-promptkit
   git submodule update --remote --recursive extern/ai-promptkit
   ```

   If an authorized upgrade is already awaiting commit, review that checked-out SHA instead of resetting or advancing it again.

4. Before removing the installed preset, review relevant workflow, agent, preset and compatibility changes. Check `specify version` against the new `requires.speckit_version`; verify the new manifest and referenced template files. If incompatible or incomplete, leave the installed preset intact, restore the prior checkout if this run advanced it, and report the blocker.
5. Refresh the installed preset using its recorded priority:

   ```text
   specify preset remove devl-spiral
   specify preset add --dev extern/ai-promptkit/spec-kit/presets/devl-spiral --priority <recorded-priority>
   specify preset resolve constitution-template
   specify preset resolve spec-template
   specify preset resolve plan-template
   ```

6. Restore the recorded enabled state and run [doctor](doctor.md). Inspect resolution output and installed/source content equality. If replacement or verification fails, reinstall the preserved prior preset with its settings and restore the prior submodule checkout if this run advanced it; report any incomplete recovery. Discard the temporary recovery copy only after success or confirmed restoration.

Do not change feature artifacts, application code, Spec Kit CLI version or unrelated dependencies. Do not stage, commit or push unless asked. Report old/new SHA, relevant changes, preset resolution, recovery status and residual incompatibilities. A successful uncommitted upgrade leaves the new submodule pin pending review; doctor must not treat that expected difference as a failed installation.
