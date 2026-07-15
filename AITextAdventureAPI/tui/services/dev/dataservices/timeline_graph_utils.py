"""
Shared graph-traversal helpers used by both the chronological validator
(timeline_validator.py) and the reachability engine (timeline_reachability.py).

All functions here are pure — no side effects, no I/O.
"""
from __future__ import annotations

from typing import Any, Dict, FrozenSet, List, Set, Tuple

from tui.services.dev.dataservices.models import (
    GameState,
    TimelineGroupNode,
    TimelineTaskNode,
)

# ── Dynamic NPC slot ids (runtime-resolved; treated as always-valid) ──────────
DYNAMIC_NPC_IDS: FrozenSet[str] = frozenset({
    "pending_character", "final_character", "twisted_character",
})

# ── Condition types → required param keys ────────────────────────────────────
CONDITION_REQUIRED_PARAMS: Dict[str, Tuple[str, ...]] = {
    "is_task_completed":  ("task_id",),
    "is_task_active":     ("task_id",),
    "is_task_not_active": ("task_id",),
    "has_item":           ("item_id",),
    "has_money":          ("amount",),
    "is_npc_met":         ("npc_id",),
    "is_npc_not_met":     ("npc_id",),
    "is_intro_complete":  (),
    "is_chapter_gte":     ("chapter",),
    "is_chapter_lte":     ("chapter",),
}


# ── Event iteration ───────────────────────────────────────────────────────────

def iter_events(task: Dict[str, Any]):
    """Yield (stage_label, event_dict) for all acquire then complete events."""
    for ev in task.get("task_acquire_events") or []:
        if isinstance(ev, dict):
            yield "acquire", ev
    for ev in task.get("task_complete_events") or []:
        if isinstance(ev, dict):
            yield "complete", ev


def events_for_stage(task: Dict[str, Any], stage: str) -> List[Dict[str, Any]]:
    """Return only the events for a given stage key."""
    return [e for e in (task.get(stage) or []) if isinstance(e, dict)]


# ── Award and option edge extraction ─────────────────────────────────────────

def award_and_option_edges(
    all_tasks: List[TimelineTaskNode],
) -> Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
    """Return (award_edges, option_edges) dicts for the full task set.

    award_edges[task_id]  → list of task_ids granted by award_task events.
    option_edges[task_id] → list of task_ids offered via initiate_option_dialog.

    Both are keyed by the *source* task that fires the edge (i.e. the task
    whose complete events contain the award/option).
    """
    award: Dict[str, List[str]]  = {tn.task_id: [] for tn in all_tasks}
    option: Dict[str, List[str]] = {tn.task_id: [] for tn in all_tasks}

    for tn in all_tasks:
        for _stage, ev in iter_events(tn.task):
            et     = ev.get("event_type", "")
            params = ev.get("params") or {}

            if et == "award_task":
                target = str(params.get("task_id") or "").strip()
                if target:
                    award[tn.task_id].append(target)

            elif et == "initiate_option_dialog":
                for opt in params.get("options") or []:
                    if isinstance(opt, (list, tuple)) and len(opt) == 2:
                        tid = str(opt[1]).strip()
                    elif isinstance(opt, dict):
                        tid = str(opt.get("task_id") or "").strip()
                    else:
                        tid = ""
                    if tid:
                        option[tn.task_id].append(tid)

    return award, option


# ── Condition evaluation ──────────────────────────────────────────────────────

def condition_satisfied(
    cond: Dict[str, Any],
    state: "GameState",
    known_task_ids: FrozenSet[str],
) -> bool:
    """Evaluate a single event condition against a simulated GameState.

    Returns True if the condition is satisfied (or unrecognised — fail-open
    so unknown conditions never silently block reachability exploration).
    """
    if not cond or not isinstance(cond, dict):
        return True

    ctype   = str(cond.get("type") or cond.get("condition_type") or "")
    cparams = cond.get("params") or {}

    if ctype == "is_task_completed":
        return str(cparams.get("task_id", "")) in state.completed

    if ctype == "is_task_active":
        return str(cparams.get("task_id", "")) in state.active

    if ctype == "is_task_not_active":
        return str(cparams.get("task_id", "")) not in state.active

    if ctype == "has_item":
        item_id = str(cparams.get("item_id", ""))
        return state.inv_count(item_id) >= 1

    if ctype == "has_money":
        try:
            return True  # Money is not tracked in GameState; assume satisfiable
        except (TypeError, ValueError):
            return True

    if ctype in ("is_npc_met", "is_npc_not_met"):
        return True  # NPC met-state not tracked in Phase 1 GameState; fail-open

    if ctype == "is_intro_complete":
        return True  # Assume intro done for reachability purposes

    if ctype == "is_chapter_gte":
        try:
            return state.chapter >= int(cparams.get("chapter", 0))
        except (TypeError, ValueError):
            return True

    if ctype == "is_chapter_lte":
        try:
            return state.chapter <= int(cparams.get("chapter", 999))
        except (TypeError, ValueError):
            return True

    # Unknown condition type — fail-open (validator will flag it separately)
    return True