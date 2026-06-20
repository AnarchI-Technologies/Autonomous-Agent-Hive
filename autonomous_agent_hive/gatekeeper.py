from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AgentAction:
    agent_id: str
    action_type: str
    authority_level: int
    risk: float
    cooldown_remaining_seconds: int = 0


@dataclass(frozen=True)
class GateDecision:
    route: str
    reason: str
    can_execute: bool


def evaluate_action(action: AgentAction) -> GateDecision:
    if not action.agent_id.strip():
        return GateDecision("reject", "agent_id is required", False)
    if not 0 <= action.authority_level <= 5:
        return GateDecision("reject", "authority_level must be between 0 and 5", False)
    if not 0 <= action.risk <= 1:
        return GateDecision("reject", "risk must be between 0 and 1", False)
    if action.cooldown_remaining_seconds > 0:
        return GateDecision("wait", "cooldown gate is active", False)

    kind = action.action_type.strip().upper()
    if kind in {"POST", "TRANSFER", "DEPLOY", "DELETE"} and action.authority_level < 4:
        return GateDecision("review", "action requires higher authority", False)
    if action.risk >= 0.75:
        return GateDecision("review", "risk gate requires human review", False)
    return GateDecision("execute", "deterministic gates cleared", True)

