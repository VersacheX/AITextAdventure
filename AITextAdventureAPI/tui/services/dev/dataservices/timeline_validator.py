"""
Timeline integrity validator.

Call ``validate_timeline_integrity(tree, const)`` to run all rules against
the current timeline tree and annotate each ``TimelineTaskNode.errors``.

Rules
-----
R1  ITEM_REMOVE_WITHOUT_SOURCE
    remove_item with no prior award_item / dungeon_add_treasure for the same item_id.
    ITEM_REMOVE_EXCESS_COUNT (warning)
    remove_item count exceeds award/dungeon source count for the item.

R2  MEET_NPC_WITHOUT_CREATE / MEET_NPC_DYNAMIC_REFERENCE
    meet task targeting a static NPC with no prior create_npc.
    Dynamic ids (pending_character etc.) emit a warning instead.

R3  AWARD_TASK_TARGET_MISSING
    award_task referencing a task_id that doesn't exist in the known set.

R4  TASK_UNREACHABLE_NO_INBOUND_AWARD
    Non-root task with zero inbound award_task edges.

R5  TASK_ID_DUPLICATE
    Same task_id appears more than once.

R6  DIALOG_REF_MISSING
    initiate_dialog / initiate_character_dialog references an (npc_id, dialog_id)
    pair not present in the dialog index.

R7  DIALOG_NPC_UNKNOWN
    npc_id used in a dialog event is not in the known NPC set (narrator / dynamic
    ids are exempted).

R8  TASK_SCHEMA_INVALID
    meet  → must have to_type + to_id
    deliver → must have item_id + to_type + to_id
    defeat  → must have to_type == "mob" and to_id

R9  AWARD_GRAPH_CYCLE
    Cycle detected in the award_task directed graph.

R10 CHAPTER_NO_ROOT
    A chapter bucket has no root task (no task with an inbound award from
    outside the chapter, or a recognized root pattern).

R11 CHAPTER_NO_ADVANCE
    A main-story chapter bucket has no advance_chapter event anywhere in its tasks.
    (Warning level — some chapters legitimately delay advance.)

R12 NPC_LIFECYCLE_INVALID
    show_npc / hide_npc / set_npc_standing_text / character_join reference an
    NPC id that was never created (create_npc) and is not in the static NPC list.

R13 DUNGEON_EVENT_UNKNOWN_DUNGEON
    dungeon_add_treasure / dungeon_add_npc / set_player_in_dungeon /
    remove_player_from_dungeon / lock_dungeon / unlock_dungeon reference a
    dungeon_id never created by a prior create_dungeon event.

R14 REMOVE_TASK_TARGET_MISSING
    remove_task / cancel_task referencing a task_id that doesn't exist.

R15 CONDITION_PAYLOAD_INVALID
    Condition block present but missing required fields for its type.
"""
from __future__ import annotations

import logging
from collections import defaultdict, deque
from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple

from tui.services.dev.dataservices.models import (
    TimelineGroupNode,
    TimelineTaskNode,
    TimelineValidationError,
)

log = logging.getLogger(__name__)

# ── Constants ─────────────────────────────────────────────────────────────

# task_ids / suffixes / types treated as roots (no required inbound award)
_ROOT_TASK_ID_SUFFIXES: Tuple[str, ...] = ("_initialize",)
_ROOT_TASK_TYPES: FrozenSet[str] = frozenset({
    "complete_intro_story",
    "initialize",
})
# Explicit allowlist for edge-case roots that don't match patterns
_ROOT_TASK_ALLOWLIST: FrozenSet[str] = frozenset()

# NPC ids whose absence from create_npc is expected (global preloads)
_DYNAMIC_NPC_IDS: FrozenSet[str] = frozenset({
    "pending_character", "final_character", "twisted_character",
})

# Condition types → required param keys
_CONDITION_REQUIRED_PARAMS: Dict[str, Tuple[str, ...]] = {
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

# Dungeon event types that require a known dungeon_id
_DUNGEON_REF_EVENT_TYPES: FrozenSet[str] = frozenset({
    "dungeon_add_treasure", "dungeon_add_npc",
    "set_player_in_dungeon", "remove_player_from_dungeon",
    "lock_dungeon", "unlock_dungeon", "set_dungeon_locked_text",
})

# NPC lifecycle events that require the NPC to already exist
_NPC_LIFECYCLE_EVENT_TYPES: FrozenSet[str] = frozenset({
    "show_npc", "hide_npc", "set_npc_standing_text",
})

# ── helpers ───────────────────────────────────────────────────────────────────

def _events(task: Dict[str, Any], stage: str) -> List[Dict[str, Any]]:
    return [e for e in (task.get(stage) or []) if isinstance(e, dict)]


def _all_events(task: Dict[str, Any]) -> List[Dict[str, Any]]:
    return _events(task, "task_acquire_events") + _events(task, "task_complete_events")


def _all_task_nodes(groups: List[TimelineGroupNode]) -> List[TimelineTaskNode]:
    nodes: List[TimelineTaskNode] = []
    for g in groups:
        for b in g.buckets:
            nodes.extend(b.tasks)
    return nodes


# ── checks ────────────────────────────────────────────────────────────────────

def _check_missing_task_id(node: TimelineTaskNode) -> List[TimelineValidationError]:
    if not node.task_id or node.task_id == "?":
        return [TimelineValidationError(
            code="MISSING_TASK_ID",
            message="Task has no task_id.",
        )]
    return []


def _check_award_task_refs(
    node: TimelineTaskNode,
    known_ids: Set[str],
) -> List[TimelineValidationError]:
    errors: List[TimelineValidationError] = []
    for ev in _all_events(node.task):
        if ev.get("event_type") != "award_task":
            continue
        params  = ev.get("params") or {}
        awarded = str(params.get("task_id") or params.get("id") or "")
        if awarded and awarded not in known_ids:
            errors.append(TimelineValidationError(
                code="AWARD_TASK_UNKNOWN",
                message=f"award_task references unknown task id '{awarded}'.",
                event_type="award_task",
                related_task_id=awarded,
            ))
    return errors


def _check_remove_task_refs(
    node: TimelineTaskNode,
    known_ids: Set[str],
) -> List[TimelineValidationError]:
    errors: List[TimelineValidationError] = []
    for ev in _all_events(node.task):
        if ev.get("event_type") not in ("remove_task", "cancel_task"):
            continue
        params     = ev.get("params") or {}
        target     = str(params.get("task_id") or params.get("id") or "")
        event_type = ev.get("event_type", "")
        if target and target not in known_ids:
            errors.append(TimelineValidationError(
                code="REMOVE_TASK_UNKNOWN",
                message=f"{event_type} references unknown task id '{target}'.",
                event_type=event_type,
                related_task_id=target,
            ))
    return errors


def _check_advance_chapter(node: TimelineTaskNode) -> List[TimelineValidationError]:
    """Warn when advance_chapter is missing a chapter number."""
    errors: List[TimelineValidationError] = []
    for ev in _all_events(node.task):
        if ev.get("event_type") != "advance_chapter":
            continue
        params  = ev.get("params") or {}
        chapter = params.get("chapter")
        if chapter is None:
            errors.append(TimelineValidationError(
                code="ADVANCE_CHAPTER_NO_PARAM",
                message="advance_chapter event is missing 'chapter' param.",
                event_type="advance_chapter",
            ))
    return errors


def _check_dungeon_treasure(node: TimelineTaskNode) -> List[TimelineValidationError]:
    """Warn when dungeon_add_treasure has no dungeon_id or item_id."""
    errors: List[TimelineValidationError] = []
    for ev in _all_events(node.task):
        if ev.get("event_type") != "dungeon_add_treasure":
            continue
        params    = ev.get("params") or {}
        dungeon   = params.get("dungeon_id") or params.get("dungeon")
        item      = params.get("item_id") or params.get("item")
        if not dungeon:
            errors.append(TimelineValidationError(
                code="DUNGEON_TREASURE_NO_DUNGEON",
                message="dungeon_add_treasure event is missing dungeon_id.",
                event_type="dungeon_add_treasure",
            ))
        if not item:
            errors.append(TimelineValidationError(
                code="DUNGEON_TREASURE_NO_ITEM",
                message="dungeon_add_treasure event is missing item_id.",
                event_type="dungeon_add_treasure",
            ))
    return errors


def _check_initiate_option_dialog(node: TimelineTaskNode) -> List[TimelineValidationError]:
    """Warn when an option dialog has no options list."""
    errors: List[TimelineValidationError] = []
    for ev in _all_events(node.task):
        if ev.get("event_type") != "initiate_option_dialog":
            continue
        params  = ev.get("params") or {}
        options = params.get("options")
        if not options:
            errors.append(TimelineValidationError(
                code="OPTION_DIALOG_NO_OPTIONS",
                message="initiate_option_dialog event has an empty options list.",
                event_type="initiate_option_dialog",
            ))
    return errors


def _check_duplicate_events(node: TimelineTaskNode) -> List[TimelineValidationError]:
    """Flag events that appear more than once in the same stage."""
    errors: List[TimelineValidationError] = []
    for stage in ("task_acquire_events", "task_complete_events"):
        seen: Dict[str, int] = {}
        for ev in _events(node.task, stage):
            et = ev.get("event_type", "")
            seen[et] = seen.get(et, 0) + 1
        for et, count in seen.items():
            if count > 1:
                errors.append(TimelineValidationError(
                    code="DUPLICATE_EVENT",
                    message=(
                        f"event_type '{et}' appears {count}× in "
                        f"{'acquire' if 'acquire' in stage else 'complete'} events."
                    ),
                    event_type=et,
                ))
    return errors


# ── public API ────────────────────────────────────────────────────────────────

def validate_timeline_integrity(groups: List[TimelineGroupNode]) -> int:
    """Annotate every ``TimelineTaskNode.errors`` list in-place.

    Clears any previous errors before running all checks.

    Args:
        groups: The full (or filtered) timeline group tree from
                ``get_timeline_tree()`` / ``filter_timeline_tree()``.

    Returns:
        Total number of errors found across all tasks.
    """
    all_nodes  = _all_task_nodes(groups)
    known_ids  = {n.task_id for n in all_nodes}
    total      = 0

    for node in all_nodes:
        node.errors.clear()
        node.errors.extend(_check_missing_task_id(node))
        node.errors.extend(_check_award_task_refs(node, known_ids))
        node.errors.extend(_check_remove_task_refs(node, known_ids))
        node.errors.extend(_check_advance_chapter(node))
        node.errors.extend(_check_dungeon_treasure(node))
        node.errors.extend(_check_initiate_option_dialog(node))
        node.errors.extend(_check_duplicate_events(node))
        total += len(node.errors)

    return total

def _err(
    code: str,
    message: str,
    event_type: str = "",
    related_task_id: str = "",
    related_entity_id: str = "",
) -> TimelineValidationError:
    return TimelineValidationError(
        code=code,
        message=message,
        event_type=event_type,
        related_task_id=related_task_id,
        related_entity_id=related_entity_id,
    )


def _is_root(task: Dict[str, Any], task_id: str) -> bool:
    """Return True if this task is exempt from the inbound-award requirement."""
    if task_id in _ROOT_TASK_ALLOWLIST:
        return True
    for suffix in _ROOT_TASK_ID_SUFFIXES:
        if task_id.endswith(suffix):
            return True
    ttype = str(task.get("type", "")).lower()
    return ttype in _ROOT_TASK_TYPES


def _iter_events(task: Dict[str, Any]):
    """Yield (stage_label, event_dict) for all acquire then complete events."""
    for ev in task.get("task_acquire_events") or []:
        if isinstance(ev, dict):
            yield "acquire", ev
    for ev in task.get("task_complete_events") or []:
        if isinstance(ev, dict):
            yield "complete", ev


def _flat_tasks(tree: List[TimelineGroupNode]) -> List[TimelineTaskNode]:
    """Deterministic flat list of all task nodes in traversal order."""
    out: List[TimelineTaskNode] = []
    for group in tree:
        for bucket in group.buckets:
            out.extend(bucket.tasks)
    return out


def _flat_tasks_by_bucket(
    tree: List[TimelineGroupNode],
) -> List[Tuple[str, str, List[TimelineTaskNode]]]:
    """Yield (group_id, bucket_id, [tasks]) in traversal order."""
    out = []
    for group in tree:
        for bucket in group.buckets:
            out.append((group.group_id, bucket.bucket_id, list(bucket.tasks)))
    return out


# ── Public API ────────────────────────────────────────────────────────────

def validate_timeline_integrity(
    tree: List[TimelineGroupNode],
    const: Any,
) -> Dict[str, int]:
    """Run all integrity rules on *tree*, annotating each ``TimelineTaskNode.errors``.

    Returns a summary dict::

        {
            "tasks_scanned": int,
            "events_scanned": int,
            "invalid_tasks": int,
            "total_errors": int,
            "by_code": {code: count, ...},
        }

    Never raises — malformed inputs produce validation errors, not exceptions.
    All existing errors on nodes are cleared before re-validation.
    """
    # ── Reset ─────────────────────────────────────────────────────────────
    all_tasks = _flat_tasks(tree)
    for tn in all_tasks:
        tn.errors.clear()

    errors_map: Dict[str, List[TimelineValidationError]] = defaultdict(list)

    # ── Build known-entity sets from const ────────────────────────────────
    known_task_ids: Set[str] = {tn.task_id for tn in all_tasks}

    known_npc_ids: Set[str] = set()
    for npc in list(getattr(const, "NPCS", []) or []) + list(getattr(const, "PLAYER_NPCS", []) or []):
        if isinstance(npc, dict) and npc.get("npc_id"):
            known_npc_ids.add(str(npc["npc_id"]))

    known_dialog_pairs: Set[Tuple[Any, Any]] = set()
    for dlg in getattr(const, "NPC_DIALOG", []) or []:
        if isinstance(dlg, dict):
            known_dialog_pairs.add((dlg.get("npc_id"), dlg.get("dialog_id")))

    known_dungeon_ids: Set[str] = set()
    for ds in getattr(const, "DUNGEON_SETTINGS", []) or []:
        if isinstance(ds, dict):
            did = ds.get("dungeon_id") or ds.get("id")
            if did:
                known_dungeon_ids.add(str(did))

    # ── R5: Duplicate task ids ────────────────────────────────────────────
    seen_ids: Dict[str, str] = {}  # task_id → first task_id (same key, kept for dup detection)
    for tn in all_tasks:
        if tn.task_id in seen_ids:
            errors_map[tn.task_id].append(_err(
                "TASK_ID_DUPLICATE",
                f"Duplicate task_id '{tn.task_id}' — first seen at same id.",
                related_task_id=tn.task_id,
            ))
        else:
            seen_ids[tn.task_id] = tn.task_id

    # ── Traversal-order state for rules that require "prior" context ───────
    item_source_counts: Dict[str, int] = defaultdict(int)   # item_id → net sources
    item_remove_counts: Dict[str, int] = defaultdict(int)   # item_id → net removes
    created_npc_ids:    Set[str]       = set()
    created_dungeon_ids: Set[str]      = set()

    # award_task graph: target_task_id → list of awarding task_ids
    inbound_awards: Dict[str, List[str]] = defaultdict(list)
    # for cycle detection: awarding_task_id → [target_task_ids]
    award_edges: Dict[str, List[str]] = defaultdict(list)

    tasks_scanned  = 0
    events_scanned = 0

    for tn in all_tasks:
        tasks_scanned += 1
        task      = tn.task
        task_id   = tn.task_id
        task_type = str(task.get("type", "")).lower()

        # ── R8: Schema validation ─────────────────────────────────────
        if task_type == "meet":
            if not task.get("to_type") or not task.get("to_id"):
                errors_map[task_id].append(_err(
                    "TASK_SCHEMA_INVALID",
                    f"'meet' task missing required field(s): to_type={task.get('to_type')!r}, "
                    f"to_id={task.get('to_id')!r}",
                ))
        elif task_type == "deliver":
            missing = [f for f in ("item_id", "to_type", "to_id") if not task.get(f)]
            if missing:
                errors_map[task_id].append(_err(
                    "TASK_SCHEMA_INVALID",
                    f"'deliver' task missing required field(s): {', '.join(missing)}",
                ))
        elif task_type == "defeat":
            if str(task.get("to_type", "")).lower() != "mob" or not task.get("to_id"):
                errors_map[task_id].append(_err(
                    "TASK_SCHEMA_INVALID",
                    f"'defeat' task must have to_type='mob' and to_id, "
                    f"got to_type={task.get('to_type')!r} to_id={task.get('to_id')!r}",
                ))

        # ── R2: meet-NPC check (pre-event pass) ───────────────────────
        if task_type == "meet" and str(task.get("to_type", "")).lower() == "npc":
            to_id = str(task.get("to_id", ""))
            if to_id in _DYNAMIC_NPC_IDS:
                errors_map[task_id].append(_err(
                    "MEET_NPC_DYNAMIC_REFERENCE",
                    f"NPC id '{to_id}' is dynamic and cannot be statically verified.",
                    related_entity_id=to_id,
                ))
            elif to_id and to_id not in created_npc_ids:
                errors_map[task_id].append(_err(
                    "MEET_NPC_WITHOUT_CREATE",
                    f"No prior create_npc for NPC '{to_id}' before meet task.",
                    related_entity_id=to_id,
                ))

        for stage, ev in _iter_events(task):
            events_scanned += 1
            raw_type = str(ev.get("event_type", ""))
            params   = ev.get("params") or {}

            # ── R15: Condition payload ─────────────────────────────────
            cond = ev.get("condition")
            if cond and isinstance(cond, dict):
                ctype = str(cond.get("type") or cond.get("condition_type") or "")
                cparams = cond.get("params") or {}
                required = _CONDITION_REQUIRED_PARAMS.get(ctype)
                if required is None:
                    errors_map[task_id].append(_err(
                        "CONDITION_PAYLOAD_INVALID",
                        f"Unknown condition type '{ctype}' in event '{raw_type}'.",
                        event_type=raw_type,
                    ))
                else:
                    for req_key in required:
                        if req_key not in cparams:
                            errors_map[task_id].append(_err(
                                "CONDITION_PAYLOAD_INVALID",
                                f"Condition '{ctype}' missing required param '{req_key}'.",
                                event_type=raw_type,
                            ))

            # ── R1: Item economy ──────────────────────────────────────
            if raw_type == "award_item":
                item_id = str(params.get("item_id") or params.get("id") or "")
                if item_id:
                    item_source_counts[item_id] += 1

            elif raw_type == "dungeon_add_treasure":
                item_id = str(params.get("item_id") or params.get("id") or "")
                if item_id:
                    item_source_counts[item_id] += 1

            elif raw_type == "remove_item":
                item_id = str(params.get("item_id") or params.get("id") or "")
                if not item_id:
                    errors_map[task_id].append(_err(
                        "ITEM_REMOVE_WITHOUT_SOURCE",
                        "remove_item event has no item_id.",
                        event_type=raw_type,
                    ))
                else:
                    if item_source_counts[item_id] == 0:
                        errors_map[task_id].append(_err(
                            "ITEM_REMOVE_WITHOUT_SOURCE",
                            f"remove_item for '{item_id}' with no prior award_item or "
                            f"dungeon_add_treasure.",
                            event_type=raw_type,
                            related_entity_id=item_id,
                        ))
                    item_remove_counts[item_id] += 1
                    if item_remove_counts[item_id] > item_source_counts[item_id]:
                        errors_map[task_id].append(_err(
                            "ITEM_REMOVE_EXCESS_COUNT",
                            f"remove_item for '{item_id}' exceeds known source count "
                            f"({item_remove_counts[item_id]} removes vs "
                            f"{item_source_counts[item_id]} sources).",
                            event_type=raw_type,
                            related_entity_id=item_id,
                        ))

            # ── R3: award_task target exists ──────────────────────────
            elif raw_type == "award_task":
                target = str(params.get("task_id") or "")
                if not target:
                    errors_map[task_id].append(_err(
                        "AWARD_TASK_TARGET_MISSING",
                        "award_task event has no task_id param.",
                        event_type=raw_type,
                    ))
                else:
                    if target not in known_task_ids:
                        errors_map[task_id].append(_err(
                            "AWARD_TASK_TARGET_MISSING",
                            f"award_task references unknown task_id '{target}'.",
                            event_type=raw_type,
                            related_task_id=target,
                        ))
                    inbound_awards[target].append(task_id)
                    award_edges[task_id].append(target)

            # ── R14: remove/cancel task target ────────────────────────
            elif raw_type in ("remove_task", "cancel_task"):
                target = str(params.get("task_id") or "")
                if not target:
                    errors_map[task_id].append(_err(
                        "REMOVE_TASK_TARGET_MISSING",
                        f"{raw_type} event has no task_id param.",
                        event_type=raw_type,
                    ))
                elif target not in known_task_ids:
                    errors_map[task_id].append(_err(
                        "REMOVE_TASK_TARGET_MISSING",
                        f"{raw_type} references unknown task_id '{target}'.",
                        event_type=raw_type,
                        related_task_id=target,
                    ))

            # ── NPC lifecycle tracking ────────────────────────────────
            elif raw_type in ("create_npc", "create_character_npc"):
                npc_id = str(params.get("npc_id") or params.get("id") or "")
                if npc_id:
                    created_npc_ids.add(npc_id)

            # ── R12: NPC lifecycle validity ───────────────────────────
            elif raw_type in _NPC_LIFECYCLE_EVENT_TYPES:
                npc_id = str(params.get("npc_id") or params.get("id") or "")
                if npc_id and npc_id not in _DYNAMIC_NPC_IDS:
                    if npc_id not in created_npc_ids and npc_id not in known_npc_ids:
                        errors_map[task_id].append(_err(
                            "NPC_LIFECYCLE_INVALID",
                            f"'{raw_type}' targets NPC '{npc_id}' which was never "
                            f"created or statically defined.",
                            event_type=raw_type,
                            related_entity_id=npc_id,
                        ))

            elif raw_type == "character_join":
                char_id = str(params.get("character_id") or "")
                if char_id and char_id not in known_npc_ids:
                    errors_map[task_id].append(_err(
                        "NPC_LIFECYCLE_INVALID",
                        f"character_join references unknown character_id '{char_id}'.",
                        event_type=raw_type,
                        related_entity_id=char_id,
                    ))

            # ── Dungeon tracking ──────────────────────────────────────
            elif raw_type == "create_dungeon":
                did = str(params.get("dungeon_id") or params.get("id") or "")
                if did:
                    created_dungeon_ids.add(did)
                    known_dungeon_ids.add(did)

            # ── R13: Dungeon event references known dungeon ───────────
            elif raw_type in _DUNGEON_REF_EVENT_TYPES:
                did = str(params.get("dungeon_id") or "")
                if not did:
                    errors_map[task_id].append(_err(
                        "DUNGEON_EVENT_UNKNOWN_DUNGEON",
                        f"'{raw_type}' has no dungeon_id param.",
                        event_type=raw_type,
                    ))
                elif did not in known_dungeon_ids:
                    errors_map[task_id].append(_err(
                        "DUNGEON_EVENT_UNKNOWN_DUNGEON",
                        f"'{raw_type}' references dungeon '{did}' which was never created.",
                        event_type=raw_type,
                        related_entity_id=did,
                    ))

            # ── R6/R7: Dialog reference validity ──────────────────────
            elif raw_type in ("initiate_dialog", "initiate_character_dialog"):
                npc_id    = params.get("npc_id")
                dialog_id = params.get("dialog_id")
                pair      = (npc_id, dialog_id)
                if pair not in known_dialog_pairs:
                    errors_map[task_id].append(_err(
                        "DIALOG_REF_MISSING",
                        f"'{raw_type}' references (npc_id={npc_id!r}, "
                        f"dialog_id={dialog_id!r}) which has no dialog lines.",
                        event_type=raw_type,
                        related_entity_id=str(npc_id or ""),
                    ))
                if npc_id and str(npc_id) not in _DYNAMIC_NPC_IDS | {None, ""}:
                    if str(npc_id) not in known_npc_ids:
                        errors_map[task_id].append(_err(
                            "DIALOG_NPC_UNKNOWN",
                            f"'{raw_type}' uses npc_id '{npc_id}' which is not in "
                            f"the known NPC set.",
                            event_type=raw_type,
                            related_entity_id=str(npc_id),
                        ))

    # ── R4: Unreachable tasks (no inbound award) ──────────────────────────
    for tn in all_tasks:
        if _is_root(tn.task, tn.task_id):
            continue
        if not inbound_awards.get(tn.task_id):
            errors_map[tn.task_id].append(_err(
                "TASK_UNREACHABLE_NO_INBOUND_AWARD",
                f"Task '{tn.task_id}' has no inbound award_task and is not a root task.",
                related_task_id=tn.task_id,
            ))

    # ── R9: Cycle detection (DFS on award graph) ──────────────────────────
    visited:   Set[str] = set()
    rec_stack: Set[str] = set()

    def _dfs_cycle(node: str) -> bool:
        visited.add(node)
        rec_stack.add(node)
        for neighbour in award_edges.get(node, []):
            if neighbour not in visited:
                if _dfs_cycle(neighbour):
                    return True
            elif neighbour in rec_stack:
                return True
        rec_stack.discard(node)
        return False

    for task_id in list(award_edges.keys()):
        if task_id not in visited:
            if _dfs_cycle(task_id):
                errors_map[task_id].append(_err(
                    "AWARD_GRAPH_CYCLE",
                    f"award_task graph contains a cycle reachable from '{task_id}'.",
                    event_type="award_task",
                    related_task_id=task_id,
                ))

    # ── R10/R11: Per-bucket chapter checks ───────────────────────────────
    for group_id, bucket_id, bucket_tasks in _flat_tasks_by_bucket(tree):
        if not bucket_tasks:
            continue

        bucket_task_ids = {tn.task_id for tn in bucket_tasks}

        # R10: at least one root in every bucket
        has_bucket_root = any(
            not any(
                awarding in bucket_task_ids
                for awarding in inbound_awards.get(tn.task_id, [])
            )
            for tn in bucket_tasks
        )
        if not has_bucket_root:
            errors_map[bucket_tasks[0].task_id].append(_err(
                "CHAPTER_NO_ROOT",
                f"Bucket '{bucket_id}' in group '{group_id}' has no discernible "
                f"root task.",
            ))

        # R11: main-story buckets should have an advance_chapter
        if group_id == "main":
            has_advance = any(
                ev.get("event_type") == "advance_chapter"
                for tn in bucket_tasks
                for _, ev in _iter_events(tn.task)
            )
            if not has_advance:
                errors_map[bucket_tasks[0].task_id].append(_err(
                    "CHAPTER_NO_ADVANCE",
                    f"Main-story bucket '{bucket_id}' has no advance_chapter event. "
                    f"(Warning — may be intentional for final chapters.)",
                ))

    # ── Attach errors to nodes ────────────────────────────────────────────
    task_node_map: Dict[str, TimelineTaskNode] = {tn.task_id: tn for tn in all_tasks}
    for task_id, errs in errors_map.items():
        if task_id in task_node_map:
            task_node_map[task_id].errors.extend(errs)

    # ── Summary stats ─────────────────────────────────────────────────────
    invalid_tasks  = sum(1 for tn in all_tasks if tn.errors)
    total_errors   = sum(len(tn.errors) for tn in all_tasks)
    by_code: Dict[str, int] = defaultdict(int)
    for tn in all_tasks:
        for e in tn.errors:
            by_code[e.code] += 1

    log.debug(
        "Timeline validation complete: %d tasks scanned, %d events scanned, "
        "%d invalid tasks, %d total errors",
        tasks_scanned, events_scanned, invalid_tasks, total_errors,
    )
    for code, count in sorted(by_code.items()):
        log.debug("  %s: %d", code, count)

    return {
        "tasks_scanned":  tasks_scanned,
        "events_scanned": events_scanned,
        "invalid_tasks":  invalid_tasks,
        "total_errors":   total_errors,
        "by_code":        dict(by_code),
    }