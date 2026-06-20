# Autonomous Agent Hive

Deterministic action gating for modular AnarchI agents.

Hardcoding freedom into the systems of tomorrow.

## Purpose

Autonomous Agent Hive defines how agents request action authority. Identity and personality are separate from execution power; every action must pass deterministic gates before it can run.

## What Changed

- Removed local image-generation script with private absolute paths.
- Replaced placeholder agent files with a tested action gatekeeper.
- Added cooldown, authority, and risk gates.

## Verify

```bash
python -m unittest discover -s tests -q
```

## Public Safety

Do not commit private memory, prompts, generated identity assets, credentials, live account state, wallet material, or unreleased CERBERUS decision chains.
