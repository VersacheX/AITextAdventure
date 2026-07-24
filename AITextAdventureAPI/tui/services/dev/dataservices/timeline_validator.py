"""Timeline integrity validator.

Call ``validate_timeline_integrity(tree, const)`` to run all rules against
the current timeline tree and annotate each ``TimelineTaskNode.errors``.

Traversal order
---------------
Checks that depend on prior-task state (item stock, NPC lifecycle, etc.) use
story-chronological order:

    main ch 1–7  →  regional stories  →  main ch 8–21  →  extended city stories

This matches the in-game unlock sequence.  ``_flat_tasks_story_order()`` builds
the ordered flat list; all stateful rules consume it instead of raw tree order.

Rules
-----
R1  ITEM_REMOVE_WITHOUT_SOURCE
    remove_item with no prior award_item / dungeon_add_treasure for the same
    item_id in story-chronological order.
    ITEM_REMOVE_EXCESS_COUNT (warning)
    remove_item count exceeds the running award/dungeon source total.

R2  MEET_NPC_WITHOUT_CREATE / MEET_NPC_DYNAMIC_REFERENCE
    meet task targeting a static NPC id with no prior create_npc in chronological
    order.  Dynamic slot ids (``pending_character``, archetype placeholders) emit a
    warning (MEET_NPC_DYNAMIC_REFERENCE) instead of an error.
    Self-create exemption: if the meet task itself contains create_npc for the same
    id in its own acquire events it is considered the authoritative creation point
    and is not flagged.
    Root-task exemption: the first task of each story bucket may freely reference
    NPCs not yet seen (they are assumed pre-placed by world setup).
    MEET_NPC_STANDING_TEXT_ON_ACQUIRE (warning)
    A set_npc_standing_text event targeting the meet's to_id appears in
    task_acquire_events. It fires before the meet interaction and the change
    is almost certainly overwritten — it should be in task_complete_events.

R3  AWARD_TASK_TARGET_MISSING
    award_task referencing a task_id that does not exist anywhere in the known set.

R4  TASK_UNREACHABLE_NO_INBOUND_AWARD
    Non-root task with zero inbound award_task edges.
    Root-task exemption: the first task of each story bucket is never flagged here.

R5  TASK_ID_DUPLICATE
    Same task_id appears more than once across all stories.

R6  DIALOG_REF_MISSING
    initiate_dialog / initiate_character_dialog references an (npc_id, dialog_id)
    pair not present in the dialog index.

R7  DIALOG_NPC_UNKNOWN
    npc_id used in a dialog event is not in the known static NPC set.
    Narrator and dynamic slot ids (pending_character, archetype ids) are exempted.

    create_character_npc coverage check (warning):
    When a task uses create_character_npc or references pending_character, the
    validator verifies that dialog coverage exists for every player-character
    archetype id (technique / tech / magic / faith / skill).  Missing coverage is
    reported as DIALOG_REF_MISSING warnings on the task.

R8  TASK_SCHEMA_INVALID
    meet    → must have to_type + to_id
    deliver → must have item_id + to_type + to_id
    defeat  → must have to_type == "mob" and to_id

    DEFEAT_NO_BEGIN_COMBAT
    defeat  → task_acquire_events must contain at least one begin_combat event.

R9  AWARD_GRAPH_CYCLE
    Cycle detected in the award_task directed graph.
    Shuttle-pair exemption: a pair of tasks that mutually award each other
    (A awards B, B awards A) AND where each task also contains remove_task
    for the other is treated as an intentional bidirectional toggle and is
    not flagged as a cycle.
    Self-cleaning replay exemption: a back-edge X → Y is exempt when X
    contains a remove_task targeting Y.  This covers intentional retry loops
    where the wrong-answer task deletes the puzzle task before re-awarding it,
    guaranteeing a fresh task instance on each attempt with no runaway cycle
    at runtime (e.g. option-dialog puzzle wrong-answer → remove → re-award).

R10 CHAPTER_NO_ROOT
    A story bucket has no root task — i.e. no task that is either the first task
    of its bucket or has an inbound award_task from outside the bucket.

R11 CHAPTER_NO_ADVANCE
    A main-story chapter bucket has no advance_chapter event anywhere in its tasks.
    Warning level only.
    Final-chapter exemption: the last chapter in the main-story sequence is not
    required to carry advance_chapter (there is no next chapter to advance to).

R12 NPC_LIFECYCLE_INVALID
    show_npc / hide_npc / set_npc_standing_text / character_join reference an
    NPC id that was never introduced by create_npc and is not in the static NPC
    list at the point it is referenced (chronological order).

R13 DUNGEON_EVENT_UNKNOWN_DUNGEON
    dungeon_add_treasure / dungeon_add_npc / set_player_in_dungeon /
    remove_player_from_dungeon / lock_dungeon / unlock_dungeon reference a
    dungeon_id that was never created by a prior create_dungeon event.

R14 REMOVE_TASK_TARGET_MISSING
    remove_task / cancel_task referencing a task_id that does not exist anywhere
    in the known set.

R15 CONDITION_PAYLOAD_INVALID
    Condition block present but missing required fields for its condition type,
    or a type-specific value is malformed (e.g. negative amount/chapter).
    Unknown condition types are also flagged here.

    CONDITION_REF_INVALID
    Condition param references an entity that does not exist in the known set:
    - is_task_completed / is_task_active / is_task_not_active → task_id must
      exist in the known task set.
    - is_npc_met / is_npc_not_met → npc_id must be a known static or dynamic
      NPC id (pending_character / final_character / twisted_character are
      always exempted as they resolve at runtime).
    Note: has_item is intentionally not cross-referenced here because the item
    set is not loaded into the validator's const context.

R16 OPTION_DIALOG_OPTION_TARGET_MISSING
    Each option in an initiate_option_dialog params.options list is a
    (display_text, task_id) pair.  Every task_id must exist in the known
    task set.  A missing message or empty options list is also flagged.
    OPTION_DIALOG_NO_MESSAGE  — params.message is absent or empty.
    OPTION_DIALOG_NO_OPTIONS  — params.options is absent or empty.
    OPTION_DIALOG_OPTION_TARGET_MISSING — an option task_id is not in the
    known task set.

R17 DELIVER_ITEM_NOT_REMOVED  (warning)
    A deliver task has an item_id but its complete events contain no
    remove_item for that item.  Most deliver tasks consume the item on
    hand-off; missing removal is flagged as a warning.  Suppress by
    adding remove_item to task_complete_events, or ignore if the NPC
    is designed to inspect and return the item.

R18 NPC_OPEN_AREA_PLACEMENT  (warning)
    create_npc or show_npc places an NPC at ``region_open_area`` or
    ``region_city_open_area``.  These are valid locations but broad — flag as a
    reminder to confirm the placement is intentional and not a placeholder.

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

# Dynamic NPC slot ids — their existence depends on runtime character assignment
_DYNAMIC_NPC_IDS: FrozenSet[str] = frozenset({
    "pending_character", "final_character", "twisted_character",
})

# The five player-character archetype ids used as npc_id proxies in dialog
# seeds that target a dynamic character slot (pending_character etc.).
# A dialog_id is considered "covered" for a dynamic slot when ALL five
# archetypes carry that dialog_id.
_PLAYER_CHARACTER_TYPES: FrozenSet[str] = frozenset({
    "technique", "tech", "magic", "faith", "skill",
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

def _chapter_number(bucket_id: str) -> int:
    """Parse the chapter number from a main-story bucket id like 'ch7'.

    Returns 0 for non-chapter bucket ids so they sort before everything else
    if unexpectedly encountered.
    """
    stripped = bucket_id.lower().lstrip("ch")
    try:
        return int(stripped)
    except ValueError:
        return 0


def _flat_tasks_story_order(tree: List[TimelineGroupNode]) -> List[TimelineTaskNode]:
    """Return all task nodes in canonical story-chronological order:

        main ch1–7  →  regional  →  main ch8–21  →  extended (city stories)

    This ordering is used for all traversal-dependent validation rules so that
    NPC creation, item economy, and dungeon tracking reflect actual play order.
    """
    # Index groups by id for easy lookup
    groups_by_id: Dict[str, TimelineGroupNode] = {g.group_id: g for g in tree}

    out: List[TimelineTaskNode] = []

    # ── 1. Main story chapters 1–7 ────────────────────────────────────────
    main_group = groups_by_id.get("main")
    if main_group:
        early_buckets = sorted(
            (b for b in main_group.buckets if _chapter_number(b.bucket_id) <= 7),
            key=lambda b: _chapter_number(b.bucket_id),
        )
        for bucket in early_buckets:
            out.extend(bucket.tasks)

    # ── 2. Regional stories ───────────────────────────────────────────────
    regional_group = groups_by_id.get("regional")
    if regional_group:
        for bucket in regional_group.buckets:
            out.extend(bucket.tasks)

    # ── 3. Main story chapters 8–21 ───────────────────────────────────────
    if main_group:
        late_buckets = sorted(
            (b for b in main_group.buckets if _chapter_number(b.bucket_id) >= 8),
            key=lambda b: _chapter_number(b.bucket_id),
        )
        for bucket in late_buckets:
            out.extend(bucket.tasks)

    # ── 4. Extended city stories ──────────────────────────────────────────
    extended_group = groups_by_id.get("extended")
    if extended_group:
        for bucket in extended_group.buckets:
            out.extend(bucket.tasks)

    # ── Fallback: any groups not covered above (future-proofing) ──────────
    known_group_ids = {"main", "regional", "extended"}
    for group in tree:
        if group.group_id not in known_group_ids:
            for bucket in group.buckets:
                out.extend(bucket.tasks)

    return out

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
    severity: str = "error",
) -> TimelineValidationError:
    return TimelineValidationError(
        code=code,
        message=message,
        severity=severity,
        event_type=event_type,
        related_task_id=related_task_id,
        related_entity_id=related_entity_id,
    )


def _is_root(task: Dict[str, Any], task_id: str, story_root_ids: FrozenSet[str]) -> bool:
    """Return True if this task is exempt from the inbound-award requirement."""
    if task_id in _ROOT_TASK_ALLOWLIST:
        return True
    for suffix in _ROOT_TASK_ID_SUFFIXES:
        if task_id.endswith(suffix):
            return True
    ttype = str(task.get("type", "")).lower()
    return ttype in _ROOT_TASK_TYPES or task_id in story_root_ids


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
    all_tasks = _flat_tasks_story_order(tree)
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

    # ── Identify story-root tasks ──────────────────────────────────────────
    # The first task of every story bucket is awarded automatically when the
    # story unlocks (primary region, city, or chapter).  It will never have
    # an inbound award_task edge and must not be flagged as unreachable.
    story_root_ids: FrozenSet[str] = frozenset(
        bucket.tasks[0].task_id
        for group in tree
        for bucket in group.buckets
        if bucket.tasks
    )

    # ── R5: Duplicate task ids ────────────────────────────────────────────
    seen_ids: Dict[str, str] = {}
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
    item_source_counts:  Dict[str, int] = defaultdict(int)
    item_remove_counts:  Dict[str, int] = defaultdict(int)
    created_dungeon_ids: Set[str]       = set()
    character_npc_slots: int            = 0   # incremented by create_character_npc events

    # Pre-populate created_npc_ids from ALL complete_intro_story acquire events.
    # These tasks are story-initialization roots that fire before any meet tasks
    # can be reached, regardless of which group/bucket they live in.  This means
    # an NPC created in one story's initialize task (e.g. mara in
    # desert_large_city_initialize) is correctly visible to meet tasks in other
    # stories (e.g. the regional desert primary story) even when traversal order
    # would place the creating bucket after the referencing one.
    created_npc_ids: Set[str] = set()
    for _tn in all_tasks:
        if str(_tn.task.get("type", "")).lower() == "complete_intro_story":
            for _ev in _events(_tn.task, "task_acquire_events"):
                if _ev.get("event_type") == "create_npc":
                    _npc_id = str(_ev.get("params", {}).get("npc_id") or "")
                    if _npc_id:
                        created_npc_ids.add(_npc_id)

    # Build the node map early — needed by shuttle-pair detection and error attachment
    task_node_map: Dict[str, TimelineTaskNode] = {tn.task_id: tn for tn in all_tasks}

    inbound_awards: Dict[str, List[str]] = defaultdict(list)
    award_edges:    Dict[str, List[str]] = defaultdict(list)

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
            has_begin_combat = any(
                ev.get("event_type") == "begin_combat"
                for ev in _events(task, "task_acquire_events")
            )
            if not has_begin_combat:
                errors_map[task_id].append(_err(
                    "DEFEAT_NO_BEGIN_COMBAT",
                    f"'defeat' task '{task_id}' has no begin_combat event in "
                    f"task_acquire_events.",
                ))

        # ── R2: meet-NPC check ────────────────────────────────────────
        # A meet task may create its own target NPC inside task_acquire_events
        # (the NPC is placed just before the player interacts with it).
        # If the NPC appears in the task's own acquire events it is considered
        # pre-created and must not be flagged.
        if task_type == "meet" and str(task.get("to_type", "")).lower() == "npc":
            to_id = str(task.get("to_id", ""))
            own_creates: Set[str] = {
                str(ev.get("params", {}).get("npc_id") or "")
                for ev in _events(task, "task_acquire_events")
                if ev.get("event_type") in ("create_npc", "create_character_npc")
            }
            if to_id in own_creates:
                pass  # Valid — NPC spawned by this task's own acquire events
            elif to_id in _DYNAMIC_NPC_IDS:
                if character_npc_slots == 0:
                    errors_map[task_id].append(_err(
                        "MEET_NPC_DYNAMIC_REFERENCE",
                        f"meet targets dynamic NPC id '{to_id}' but no prior "
                        f"create_character_npc event was found.",
                        related_entity_id=to_id,
                    ))
            elif to_id and to_id not in created_npc_ids:
                errors_map[task_id].append(_err(
                    "MEET_NPC_WITHOUT_CREATE",
                    f"No prior create_npc for NPC '{to_id}' before meet task.",
                    related_entity_id=to_id,
                ))

            # Warn when acquire events mutate the NPC's standing text — this
            # runs before the player has interacted with them and the text
            # change will almost certainly be overwritten by the meet sequence.
            standing_text_on_acquire = any(
                ev.get("event_type") == "set_npc_standing_text"
                and str((ev.get("params") or {}).get("npc_id") or "") == to_id
                for ev in _events(task, "task_acquire_events")
            )
            if standing_text_on_acquire:
                errors_map[task_id].append(_err(
                    "MEET_NPC_STANDING_TEXT_ON_ACQUIRE",
                    f"'meet' task '{task_id}' sets standing text for NPC '{to_id}' "
                    f"in task_acquire_events. This fires before the meet interaction "
                    f"and is likely unintentional — move it to task_complete_events.",
                    event_type="set_npc_standing_text",
                    related_entity_id=to_id,
                    severity="warning",
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
                    # R15a: required param keys present
                    for req_key in required:
                        if req_key not in cparams:
                            errors_map[task_id].append(_err(
                                "CONDITION_PAYLOAD_INVALID",
                                f"Condition '{ctype}' missing required param '{req_key}'.",
                                event_type=raw_type,
                            ))

                    # R15b: cross-reference param values against known entity sets
                    if ctype in ("is_task_completed", "is_task_active", "is_task_not_active"):
                        ref_id = str(cparams.get("task_id") or "")
                        if ref_id and ref_id not in known_task_ids:
                            errors_map[task_id].append(_err(
                                "CONDITION_REF_INVALID",
                                f"Condition '{ctype}' references unknown task_id '{ref_id}'.",
                                event_type=raw_type,
                                related_task_id=ref_id,
                            ))

                    elif ctype in ("is_npc_met", "is_npc_not_met"):
                        ref_id = str(cparams.get("npc_id") or "")
                        if ref_id and ref_id not in _DYNAMIC_NPC_IDS:
                            if ref_id not in created_npc_ids and ref_id not in known_npc_ids:
                                errors_map[task_id].append(_err(
                                    "CONDITION_REF_INVALID",
                                    f"Condition '{ctype}' references unknown npc_id '{ref_id}'.",
                                    event_type=raw_type,
                                    related_entity_id=ref_id,
                            ))

                    elif ctype == "has_money":
                        amount = cparams.get("amount")
                        if amount is not None:
                            try:
                                if int(amount) < 0:
                                    errors_map[task_id].append(_err(
                                        "CONDITION_PAYLOAD_INVALID",
                                        f"Condition 'has_money' has negative amount {amount!r}.",
                                        event_type=raw_type,
                                    ))
                            except (TypeError, ValueError):
                                errors_map[task_id].append(_err(
                                    "CONDITION_PAYLOAD_INVALID",
                                    f"Condition 'has_money' amount {amount!r} is not an integer.",
                                    event_type=raw_type,
                                ))

                    elif ctype in ("is_chapter_gte", "is_chapter_lte"):
                        chapter = cparams.get("chapter")
                        if chapter is not None:
                            try:
                                if int(chapter) < 0:
                                    errors_map[task_id].append(_err(
                                        "CONDITION_PAYLOAD_INVALID",
                                        f"Condition '{ctype}' has negative chapter {chapter!r}.",
                                        event_type=raw_type,
                                    ))
                            except (TypeError, ValueError):
                                errors_map[task_id].append(_err(
                                    "CONDITION_PAYLOAD_INVALID",
                                    f"Condition '{ctype}' chapter {chapter!r} is not an integer.",
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
                            f"dungeon_add_treasure in traversal order — "
                            f"item may be awarded in a regional or city story.",
                            event_type=raw_type,
                            related_entity_id=item_id,
                            severity="info",
                        ))
                    item_remove_counts[item_id] += 1
                    if item_remove_counts[item_id] > item_source_counts[item_id]:
                        errors_map[task_id].append(_err(
                            "ITEM_REMOVE_EXCESS_COUNT",
                            f"remove_item for '{item_id}' exceeds known source count "
                            f"({item_remove_counts[item_id]} removes vs "
                            f"{item_source_counts[item_id]} sources) — "
                            f"item may be awarded in a regional or city story.",
                            event_type=raw_type,
                            related_entity_id=item_id,
                            severity="info",
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
            elif raw_type == "create_npc":
                npc_id = str(params.get("npc_id") or params.get("id") or "")
                if npc_id:
                    created_npc_ids.add(npc_id)
                location = str(params.get("location") or "")
                if location in ("region_open_area", "region_city_open_area"):
                    errors_map[task_id].append(_err(
                        "NPC_OPEN_AREA_PLACEMENT",
                        f"create_npc for '{npc_id or '?'}' uses broad location "
                        f"'{location}' — confirm this is intentional and not a placeholder.",
                        event_type=raw_type,
                        related_entity_id=npc_id,
                        severity="warning",
                    ))

            elif raw_type == "create_character_npc":
                # Fills a dynamic character slot (pending/final/twisted).
                # No npc_id param — the slot identity is resolved at runtime.
                character_npc_slots += 1

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
                # R18: broad open-area placement on show_npc
                if raw_type == "show_npc":
                    location = str(params.get("location") or "")
                    if location in ("region_open_area", "region_city_open_area"):
                        errors_map[task_id].append(_err(
                            "NPC_OPEN_AREA_PLACEMENT",
                            f"show_npc for '{npc_id or '?'}' uses broad location "
                            f"'{location}' — confirm this is intentional and not a placeholder.",
                            event_type=raw_type,
                            related_entity_id=npc_id,
                            severity="warning",
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

                if npc_id is not None and str(npc_id) in _DYNAMIC_NPC_IDS:
                    # Dynamic slot dialogs are stored once per player-character
                    # archetype (technique / tech / magic / faith / skill).
                    # The dialog is valid when ALL five archetypes carry it.
                    missing_archetypes = [
                        pc for pc in sorted(_PLAYER_CHARACTER_TYPES)
                        if (pc, dialog_id) not in known_dialog_pairs
                    ]
                    if missing_archetypes:
                        errors_map[task_id].append(_err(
                            "DIALOG_REF_MISSING",
                            f"'{raw_type}' uses dynamic npc_id '{npc_id}' with "
                            f"dialog_id={dialog_id!r} but the following player-character "
                            f"archetypes are missing that dialog: "
                            f"{', '.join(missing_archetypes)}.",
                            event_type=raw_type,
                            related_entity_id=str(npc_id),
                        ))
                else:
                    pair = (npc_id, dialog_id)
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

            # ── R16: Option dialog validation ─────────────────────────
            elif raw_type == "initiate_option_dialog":
                message = params.get("message", "")
                options = params.get("options") or []
                if not message:
                    errors_map[task_id].append(_err(
                        "OPTION_DIALOG_NO_MESSAGE",
                        "initiate_option_dialog event has no message.",
                        event_type=raw_type,
                    ))
                if not options:
                    errors_map[task_id].append(_err(
                        "OPTION_DIALOG_NO_OPTIONS",
                        "initiate_option_dialog event has an empty options list.",
                        event_type=raw_type,
                    ))
                else:
                    for opt in options:
                        if isinstance(opt, (list, tuple)) and len(opt) == 2:
                            opt_task_id = str(opt[1]).strip()
                        elif isinstance(opt, dict):
                            opt_task_id = str(opt.get("task_id") or "").strip()
                        else:
                            opt_task_id = ""
                        if not opt_task_id:
                            continue
                        if opt_task_id not in known_task_ids:
                            errors_map[task_id].append(_err(
                                "OPTION_DIALOG_OPTION_TARGET_MISSING",
                                f"initiate_option_dialog option references unknown "
                                f"task_id '{opt_task_id}'.",
                                event_type=raw_type,
                                related_task_id=opt_task_id,
                            ))
                        else:
                            # Option tasks are awarded through player choice, not
                            # award_task edges.  Register them as inbound so R4
                            # (TASK_UNREACHABLE_NO_INBOUND_AWARD) does not flag them.
                            inbound_awards[opt_task_id].append(task_id)
                            award_edges[task_id].append(opt_task_id)

            # ── R12 extension: set_npc_met references known NPC ───────
            elif raw_type == "set_npc_met":
                npc_id = str(params.get("npc_id") or "")
                if npc_id and npc_id not in _DYNAMIC_NPC_IDS:
                    if npc_id not in created_npc_ids and npc_id not in known_npc_ids:
                        errors_map[task_id].append(_err(
                            "NPC_LIFECYCLE_INVALID",
                            f"set_npc_met references NPC '{npc_id}' which was never "
                            f"created or statically defined.",
                            event_type=raw_type,
                            related_entity_id=npc_id,
                        ))

    # ── R4: Unreachable tasks (no inbound award) ──────────────────────────
    for tn in all_tasks:
        if _is_root(tn.task, tn.task_id, story_root_ids):
            continue
        if not inbound_awards.get(tn.task_id):
            errors_map[tn.task_id].append(_err(
                "TASK_UNREACHABLE_NO_INBOUND_AWARD",
                f"Task '{tn.task_id}' has no inbound award_task and is not a root task.",
                related_task_id=tn.task_id,
            ))

    # ── R17: Deliver task missing remove_item (warning) ───────────────────
    for tn in all_tasks:
        task      = tn.task
        task_type = str(task.get("type", "")).lower()
        if task_type != "deliver":
            continue
        item_id = str(task.get("item_id") or "")
        if not item_id:
            continue
        has_remove = any(
            ev.get("event_type") == "remove_item"
            and str((ev.get("params") or {}).get("item_id") or "") == item_id
            for _, ev in _iter_events(task)
        )
        if not has_remove:
            errors_map[tn.task_id].append(_err(
                "DELIVER_ITEM_NOT_REMOVED",
                f"Deliver task requires item '{item_id}' but no remove_item "
                f"for that item exists in its complete events. "
                f"If this is intentional (item returned to player) this warning can be ignored.",
                event_type="deliver",
                related_entity_id=item_id,
                severity="warning",
            ))

    # ── R9: Cycle detection (DFS on award graph) ──────────────────────────
    # Build a shuttle-pair exemption set first.
    # A shuttle pair is two tasks that mutually award AND mutually remove_task
    # each other — this is an intentional bidirectional toggle, not a bug.
    shuttle_pairs: Set[FrozenSet[str]] = set()
    for tn in all_tasks:
        for _, ev in _iter_events(tn.task):
            if ev.get("event_type") != "award_task":
                continue
            target = str((ev.get("params") or {}).get("task_id") or "")
            if not target:
                continue
            # Check whether target also awards tn.task_id back
            target_node = task_node_map.get(target)
            if not target_node:
                continue
            target_awards_back = any(
                str((e.get("params") or {}).get("task_id") or "") == tn.task_id
                for _, e in _iter_events(target_node.task)
                if e.get("event_type") == "award_task"
            )
            # Check mutual remove_task — each removes the other
            own_removes = {
                str((e.get("params") or {}).get("task_id") or "")
                for _, e in _iter_events(tn.task)
                if e.get("event_type") in ("remove_task", "cancel_task")
            }
            target_removes = {
                str((e.get("params") or {}).get("task_id") or "")
                for _, e in _iter_events(target_node.task)
                if e.get("event_type") in ("remove_task", "cancel_task")
            }
            if (
                target_awards_back
                and tn.task_id in target_removes
                and target in own_removes
            ):
                shuttle_pairs.add(frozenset({tn.task_id, target}))

    visited:   Set[str] = set()
    rec_stack: Set[str] = set()

    def _dfs_cycle(node: str) -> bool:
        visited.add(node)
        rec_stack.add(node)
        for neighbour in award_edges.get(node, []):
            # Skip edges that are part of a known shuttle pair
            if frozenset({node, neighbour}) in shuttle_pairs:
                continue
            if neighbour not in visited:
                if _dfs_cycle(neighbour):
                    return True
            elif neighbour in rec_stack:
                # Self-cleaning replay loop exemption: if the source task
                # removes the back-edge target before re-awarding it, the
                # cycle is intentional — both tasks are destroyed at runtime
                # before the target is freshly re-created, so no runaway loop
                # exists.  This covers option-dialog puzzle retry patterns
                # where the wrong-answer task cleans up then replays the round.
                node_task = task_node_map.get(node)
                if node_task:
                    removes_target = any(
                        str((e.get("params") or {}).get("task_id") or "") == neighbour
                        for _, e in _iter_events(node_task.task)
                        if e.get("event_type") in ("remove_task", "cancel_task")
                    )
                    if removes_target:
                        continue
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
    # Determine the highest chapter number in the main group so R11 can
    # exempt it — the final chapter intentionally has no advance_chapter.
    main_buckets_in_tree = [
        b for g in tree if g.group_id == "main" for b in g.buckets
    ]
    final_chapter_num = max(
        (_chapter_number(b.bucket_id) for b in main_buckets_in_tree),
        default=0,
    )

    for group_id, bucket_id, bucket_tasks in _flat_tasks_by_bucket(tree):
        if not bucket_tasks:
            continue

        bucket_task_ids = {tn.task_id for tn in bucket_tasks}

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

        # R11: main-story buckets should have an advance_chapter — except the
        # final chapter, which ends the story and never advances further.
        if group_id == "main":
            is_final_chapter = _chapter_number(bucket_id) == final_chapter_num
            if not is_final_chapter:
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
    # task_node_map is built earlier — do not reassign here
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