"""
event_condition_service: evaluates TaskEventCondition instances against
a live PlayerGame, returning True if the event should fire.

Imported by task_completion_service.handle_task_event to guard conditional
events without polluting the main dispatch table.

Adding a new condition type:
  1. Add an entry to TaskEventConditionType in task.py.
  2. Add a matching branch in evaluate_condition() below.
  3. Document the params shape in the TaskEventConditionType docstring.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.objects.task import TaskEventCondition


def evaluate_condition(condition: "TaskEventCondition", player_game) -> bool:
    """Return True if *condition* is satisfied by the current *player_game* state.

    If the condition type is unrecognised, a debug prompt is raised and the
    event is **skipped** (returns False) to avoid silent data corruption.
    """
    from game.objects.task import TaskEventConditionType  # local to avoid cycle

    ct = condition.condition_type
    p  = condition.params

    # ── task state ────────────────────────────────────────────────────────
    if ct == TaskEventConditionType.IS_TASK_COMPLETED:
        task_id = p.get("task_id")
        return any(
            t.task_id == task_id and t.completed
            for t in getattr(player_game, "tasks", [])
        )

    if ct == TaskEventConditionType.IS_TASK_ACTIVE:
        task_id = p.get("task_id")
        return any(
            t.task_id == task_id and not t.completed
            for t in getattr(player_game, "tasks", [])
        )

    if ct == TaskEventConditionType.IS_TASK_NOT_ACTIVE:
        task_id = p.get("task_id")
        return not any(
            t.task_id == task_id and not t.completed
            for t in getattr(player_game, "tasks", [])
        )

    # ── inventory / economy ───────────────────────────────────────────────
    if ct == TaskEventConditionType.HAS_ITEM:
        item_id = p.get("item_id")
        return any(
            getattr(i, "id", None) == item_id and getattr(i, "quantity", 0) > 0
            for i in getattr(player_game, "inventory", [])
        )

    if ct == TaskEventConditionType.HAS_MONEY:
        amount = int(p.get("amount", 0))
        return getattr(player_game, "money", 0) >= amount

    # ── npc state ─────────────────────────────────────────────────────────
    if ct == TaskEventConditionType.IS_NPC_MET:
        npc_id = p.get("npc_id")
        return any(
            n.id == npc_id and getattr(n, "met", False)
            for n in getattr(player_game, "npcs", [])
        )

    if ct == TaskEventConditionType.IS_NPC_NOT_MET:
        npc_id = p.get("npc_id")
        return not any(
            n.id == npc_id and getattr(n, "met", False)
            for n in getattr(player_game, "npcs", [])
        )

    # ── world / progression ───────────────────────────────────────────────
    if ct == TaskEventConditionType.IS_INTRO_COMPLETE:
        return bool(getattr(player_game, "intro_complete", False))

    if ct == TaskEventConditionType.IS_CHAPTER_GTE:
        chapter = int(p.get("chapter", 0))
        return getattr(player_game, "current_chapter", 0) >= chapter

    if ct == TaskEventConditionType.IS_CHAPTER_LTE:
        chapter = int(p.get("chapter", 0))
        return getattr(player_game, "current_chapter", 0) <= chapter

    # ── unhandled ─────────────────────────────────────────────────────────
    input(f"evaluate_condition: unhandled condition type '{ct}' with params {p}")
    return False