"""
State-space BFS reachability engine for the timeline validator.

``explore_reachability(tree, all_tasks)`` returns a ``ReachabilityResult``
that the rule functions in ``timeline_reachability_rules.py`` convert into
``TimelineValidationError`` instances.

Design notes
------------
- GameState is frozen/hashable so a visited-set deduplicates identical states.
- Only "relevant" items (those tested by conditions, deliver tasks, or
  remove_item events) are tracked in inventory.  All others are discarded to
  keep the state space small.
- Item counts are capped at INVENTORY_COUNT_CAP (2).  Conditions only test
  "has >= 1"; exact large counts add no discriminating power.
- BFS (not DFS) gives shortest paths naturally.

Seeding strategy
----------------
- ``main`` group: ONE seed from the very first chapter's root only.
  Inter-chapter flow is modelled by injecting an implicit out-edge from any
  task whose complete-effects have advances_chapter=True to the next
  chapter's root task.  This allows cross-chapter item flow (e.g. an item
  awarded in ch2 satisfying a deliver task pending since ch1's option branch).
- ``regional`` and ``extended`` groups: one seed per bucket (independent stories).
- Any other group: one seed per bucket (future-proofing).

Phase 1: option_dialog targets are unioned (all branches active at once).
Phase 2 will introduce exclusive branch forks via ChoicePoint.
"""
from __future__ import annotations

import logging
import re
from collections import defaultdict, deque
from dataclasses import dataclass
from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple

from tui.services.dev.dataservices.models import (
    GameState,
    ReachabilityResult,
    TaskEffects,
    TimelineBucketNode,
    TimelineGroupNode,
    TimelineTaskNode,
)
from tui.services.dev.dataservices.timeline_graph_utils import (
    condition_satisfied,
    events_for_stage,
    iter_events,
)

log = logging.getLogger(__name__)

# ── Tunables ─────────────────────────────────────────────────────────────────
_MAX_STATES:         int = 500_000   # raised — state key no longer includes active
_MAX_DEPTH:          int = 1_000
INVENTORY_COUNT_CAP: int = 2

# ── Chapter-number helper ─────────────────────────────────────────────────────

def _chapter_num_from_source_path(source_path: str) -> int:
    """Parse the chapter number from a source_path like 'main:ch7'.

    Returns -1 if the path does not match a main-story chapter pattern.
    """
    m = re.search(r"ch(\d+)$", source_path, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return -1


# ── Relevant-item filtering ───────────────────────────────────────────────────

def _relevant_item_ids(all_tasks: List[TimelineTaskNode]) -> FrozenSet[str]:
    """Return the set of item_ids that actually affect completability.

    Only items appearing in:
      - deliver task ``item_id`` fields
      - ``has_item`` condition params
      - ``remove_item`` event params

    are tracked in ``GameState.inventory``.  All others are irrelevant to
    reachability and excluding them is the single biggest lever against
    state explosion.
    """
    relevant: Set[str] = set()
    for tn in all_tasks:
        task = tn.task
        if str(task.get("type", "")).lower() == "deliver":
            iid = str(task.get("item_id") or "")
            if iid:
                relevant.add(iid)

        for _stage, ev in iter_events(task):
            et     = ev.get("event_type", "")
            params = ev.get("params") or {}

            if et == "remove_item":
                iid = str(params.get("item_id") or "")
                if iid:
                    relevant.add(iid)

            cond = ev.get("condition")
            if cond and isinstance(cond, dict):
                if str(cond.get("type", "")) == "has_item":
                    iid = str((cond.get("params") or {}).get("item_id") or "")
                    if iid:
                        relevant.add(iid)

    return frozenset(relevant)


# ── Task effects extraction ───────────────────────────────────────────────────

def _extract_effects(
    task: Dict[str, Any],
    stage: str,
    relevant_items: FrozenSet[str],
) -> TaskEffects:
    """Build a TaskEffects for one lifecycle stage of a task dict."""
    awards:     Dict[str, int] = defaultdict(int)
    removes:    Dict[str, int] = defaultdict(int)
    requires:   Dict[str, int] = defaultdict(int)
    advances    = False
    award_ids:  List[str] = []
    option_ids: List[str] = []

    for ev in events_for_stage(task, stage):
        et     = ev.get("event_type", "")
        params = ev.get("params") or {}

        if et == "award_item":
            iid = str(params.get("item_id") or "")
            if iid in relevant_items:
                awards[iid] += 1

        elif et == "dungeon_add_treasure":
            iid = str(params.get("item_id") or "")
            if iid in relevant_items:
                awards[iid] += 1

        elif et == "remove_item":
            iid = str(params.get("item_id") or "")
            if iid in relevant_items:
                removes[iid] += 1

        elif et == "advance_chapter":
            advances = True

        elif et == "award_task":
            tid = str(params.get("task_id") or "")
            if tid:
                award_ids.append(tid)

        elif et == "initiate_option_dialog":
            for opt in params.get("options") or []:
                if isinstance(opt, (list, tuple)) and len(opt) == 2:
                    tid = str(opt[1]).strip()
                elif isinstance(opt, dict):
                    tid = str(opt.get("task_id") or "").strip()
                else:
                    tid = ""
                if tid:
                    option_ids.append(tid)

    # deliver tasks implicitly require the item to be present at completion
    if stage == "task_complete_events":
        task_type = str(task.get("type", "")).lower()
        if task_type == "deliver":
            iid = str(task.get("item_id") or "")
            if iid in relevant_items:
                requires[iid] = max(requires.get(iid, 0), 1)

    # has_item conditions on events in this stage add requirements
    for ev in events_for_stage(task, stage):
        cond = ev.get("condition")
        if cond and isinstance(cond, dict) and str(cond.get("type", "")) == "has_item":
            iid = str((cond.get("params") or {}).get("item_id") or "")
            if iid in relevant_items:
                requires[iid] = max(requires.get(iid, 0), 1)

    return TaskEffects(
        awards_item=dict(awards),
        removes_item=dict(removes),
        requires_item=dict(requires),
        advances_chapter=advances,
        awards_task_ids=award_ids,
        option_task_ids=option_ids,
    )


# ── Inventory helpers ─────────────────────────────────────────────────────────

def _apply_inventory_delta(
    inv: Dict[str, int],
    awards: Dict[str, int],
    removes: Dict[str, int],
    relevant: FrozenSet[str],
) -> Dict[str, int]:
    result = dict(inv)
    for iid, count in awards.items():
        if iid in relevant:
            result[iid] = min(result.get(iid, 0) + count, INVENTORY_COUNT_CAP)
    for iid, count in removes.items():
        if iid in relevant:
            result[iid] = max(result.get(iid, 0) - count, 0)
    return {k: v for k, v in result.items() if v > 0}


def _freeze_inventory(inv: Dict[str, int]) -> Tuple[Tuple[str, int], ...]:
    return tuple(sorted(inv.items()))


# ── Transition model ──────────────────────────────────────────────────────────

@dataclass
class _TransitionModel:
    acquire_effects:  Dict[str, TaskEffects]   # task_id -> effects on acquire
    complete_effects: Dict[str, TaskEffects]   # task_id -> effects on complete
    out_edges:        Dict[str, List[str]]     # task_id -> tasks activated on completion
    relevant_items:   FrozenSet[str]
    known_task_ids:   FrozenSet[str]


def _build_transition_model(
    all_tasks: List[TimelineTaskNode],
) -> _TransitionModel:
    """Build per-task effect tables and outbound edge graph.

    Injected implicit edges
    -----------------------
    Two categories of cross-boundary edges have no explicit ``award_task``
    in the seed data and must be injected here:

    1. ``advance_chapter`` edges (main story only)
       Any task whose complete-effects fire ``advance_chapter`` gets an
       implicit out-edge to the next numerically ordered main-story chapter's
       root.  Seeds BFS from ch1 through ch21 as a single continuous chain.

    2. ``complete_intro_story`` edges (main → regional unlock)
       Regional story roots are gated behind ``complete_intro_story`` — they
       become available only after ch4's Catalyst defeat.  Any task whose
       complete-events fire ``complete_intro_story`` gets an implicit out-edge
       to every regional bucket root.  This means regional item flow (e.g.
       grove_lattice from ch2 still in inventory when the regional deliver
       becomes active) is correctly modelled.

    Regional tasks must be completed before ``complete_regional_quests``
    gates ch7 progression, but they share the main-story item pool from
    ch4 onward and have access to items awarded in ch5–ch7 for any tasks
    that extend past ``complete_region_quest``.
    """
    relevant = _relevant_item_ids(all_tasks)
    known    = frozenset(tn.task_id for tn in all_tasks)

    acquire_fx:  Dict[str, TaskEffects] = {}
    complete_fx: Dict[str, TaskEffects] = {}
    out_edges:   Dict[str, List[str]]   = {}

    # Track which tasks fire complete_intro_story or advance_chapter
    fires_intro_complete: Set[str] = set()
    fires_advance_chapter: Dict[str, int] = {}  # task_id -> chapter number

    for tn in all_tasks:
        tid = tn.task_id
        acquire_fx[tid]  = _extract_effects(tn.task, "task_acquire_events",  relevant)
        complete_fx[tid] = _extract_effects(tn.task, "task_complete_events", relevant)

        edges: List[str] = [
            t for t in complete_fx[tid].awards_task_ids + complete_fx[tid].option_task_ids
            if t in known
        ]
        out_edges[tid] = edges

        # Detect complete_intro_story events
        for ev in events_for_stage(tn.task, "task_complete_events"):
            if ev.get("event_type") == "complete_intro_story":
                fires_intro_complete.add(tid)

    # ── Inject advance_chapter cross-chapter edges ────────────────────────
    main_chapter_roots: Dict[int, str] = {}
    for tn in all_tasks:
        if not tn.source_path.startswith("main:"):
            continue
        ch_num = _chapter_num_from_source_path(tn.source_path)
        if ch_num < 0:
            continue
        bucket_tasks_for_ch = [t for t in all_tasks if t.source_path == tn.source_path]
        if bucket_tasks_for_ch:
            root_id = bucket_tasks_for_ch[0].task_id
            if ch_num not in main_chapter_roots:
                main_chapter_roots[ch_num] = root_id

    sorted_chapters = sorted(main_chapter_roots.keys())
    next_chapter_root: Dict[int, str] = {
        ch: main_chapter_roots[sorted_chapters[i + 1]]
        for i, ch in enumerate(sorted_chapters[:-1])
    }

    for tn in all_tasks:
        if not tn.source_path.startswith("main:"):
            continue
        ch_num = _chapter_num_from_source_path(tn.source_path)
        if ch_num < 0:
            continue
        fx = complete_fx.get(tn.task_id)
        if fx and fx.advances_chapter:
            next_root = next_chapter_root.get(ch_num)
            if next_root and next_root not in out_edges[tn.task_id]:
                out_edges[tn.task_id].append(next_root)

    # ── Inject complete_intro_story → regional root edges ─────────────────
    # Collect all regional bucket roots in stable order
    regional_roots: List[str] = []
    regional_root_set: Set[str] = set()
    for tn in all_tasks:
        if not tn.source_path.startswith("regional:"):
            continue
        # The root of each regional bucket is the first task in that bucket
        # (identified by _initialize suffix or complete_intro_story type)
        bucket_tasks = [t for t in all_tasks if t.source_path == tn.source_path]
        if bucket_tasks:
            root_id = bucket_tasks[0].task_id
            if root_id not in regional_root_set:
                regional_root_set.add(root_id)
                regional_roots.append(root_id)

    for task_id in fires_intro_complete:
        for reg_root in regional_roots:
            if reg_root not in out_edges[task_id]:
                out_edges[task_id].append(reg_root)

    return _TransitionModel(
        acquire_effects=acquire_fx,
        complete_effects=complete_fx,
        out_edges=out_edges,
        relevant_items=relevant,
        known_task_ids=known,
    )


# ── BFS state helpers ─────────────────────────────────────────────────────────

def _activate_with_cascade(
    start_id: str,
    inv: Dict[str, int],
    new_active: FrozenSet[str],
    new_completed: FrozenSet[str],
    model: _TransitionModel,
) -> Tuple[Dict[str, int], FrozenSet[str]]:
    """Activate start_id and all tasks cascaded via acquire-stage award_task events.

    Iterative BFS within the activation — handles chains like:
        task_A acquire → award_task task_B → task_B acquire → award_task task_C
    without recursion depth limits.

    Only inventory effects and active-set membership are updated here.
    Complete-stage effects fire separately in _complete_task.
    """
    queue: deque[str] = deque([start_id])
    while queue:
        tid = queue.popleft()
        if tid in new_active or tid in new_completed or tid not in model.known_task_ids:
            continue
        new_active = new_active | {tid}
        fx = model.acquire_effects.get(tid)
        if fx:
            inv = _apply_inventory_delta(
                inv, fx.awards_item, fx.removes_item, model.relevant_items
            )
            for sub_id in fx.awards_task_ids + fx.option_task_ids:
                if sub_id not in new_active and sub_id not in new_completed:
                    queue.append(sub_id)
    return inv, new_active


def _complete_task(
    task_id: str,
    state: GameState,
    model: _TransitionModel,
) -> Optional[GameState]:
    """Attempt to complete a task from *state*.

    Returns the successor GameState, or None if requirements are not met.
    """
    if task_id not in state.active:
        return None

    fx = model.complete_effects.get(task_id)
    if fx is None:
        return None

    for iid, min_count in fx.requires_item.items():
        if state.inv_count(iid) < min_count:
            return None

    inv = dict(state.inventory)
    inv = _apply_inventory_delta(inv, fx.awards_item, fx.removes_item, model.relevant_items)

    new_completed = state.completed | {task_id}
    new_active    = state.active - {task_id}
    new_chapter   = state.chapter + (1 if fx.advances_chapter else 0)

    # Activate each successor via cascade — handles acquire-stage award chains
    for next_id in model.out_edges.get(task_id, []):
        inv, new_active = _activate_with_cascade(
            next_id, inv, new_active, new_completed, model
        )

    return GameState(
        completed=new_completed,
        active=new_active,
        inventory=_freeze_inventory(inv),
        chapter=new_chapter,
    )


# ── Seed builder ──────────────────────────────────────────────────────────────

def _build_seeds(
    tree: List[TimelineGroupNode],
    model: _TransitionModel,
) -> List[GameState]:
    """Build the initial BFS frontier.

    Seeding strategy:
    - ``main`` group     → one seed from ch1 root only.
    - ``regional`` group → injected via complete_intro_story edges mid-BFS.
    - ``extended`` group → one independent seed per bucket.
    - Any other group   → one independent seed per bucket.
    """
    seeds: List[GameState] = []
    seen_seed_ids: Set[str] = set()

    # ── Main story: single seed from ch1 root ─────────────────────────────
    for group in tree:
        if group.group_id != "main":
            continue
        main_buckets = sorted(
            (b for b in group.buckets if b.tasks),
            key=lambda b: _chapter_num_from_source_path(f"main:{b.bucket_id}"),
        )
        if main_buckets:
            root_id = main_buckets[0].tasks[0].task_id
            if root_id in model.known_task_ids and root_id not in seen_seed_ids:
                seen_seed_ids.add(root_id)
                inv: Dict[str, int] = {}
                new_active: FrozenSet[str] = frozenset()
                inv, new_active = _activate_with_cascade(
                    root_id, inv, new_active, frozenset(), model
                )
                seeds.append(GameState(
                    completed=frozenset(),
                    active=new_active,
                    inventory=_freeze_inventory(inv),
                    chapter=0,
                ))
        break

    # ── Extended + any other groups: one seed per bucket ──────────────────
    for group in tree:
        if group.group_id in ("main", "regional"):
            continue
        for bucket in group.buckets:
            if not bucket.tasks:
                continue
            root_id = bucket.tasks[0].task_id
            if root_id in seen_seed_ids or root_id not in model.known_task_ids:
                continue
            seen_seed_ids.add(root_id)
            inv = {}
            new_active = frozenset()
            inv, new_active = _activate_with_cascade(
                root_id, inv, new_active, frozenset(), model
            )
            seeds.append(GameState(
                completed=frozenset(),
                active=new_active,
                inventory=_freeze_inventory(inv),
                chapter=0,
            ))

    return seeds


# ── BFS engine ────────────────────────────────────────────────────────────────

def explore_reachability(
    tree: List[TimelineGroupNode],
    all_tasks: List[TimelineTaskNode],
    max_states: int = _MAX_STATES,
    max_depth:  int = _MAX_DEPTH,
) -> ReachabilityResult:
    """BFS over all reachable GameState instances.

    Deduplication uses exact hash equality (all fields including active).
    A dominance check prunes states that are strictly worse than an already-
    visited state in every dimension — this replaces the previous approach of
    excluding ``active`` from the hash, which caused false-negative completions.
    """
    if not all_tasks:
        return ReachabilityResult(
            reachable_states=0,
            reachable_task_ids=frozenset(),
            completable_task_ids=frozenset(),
            truncated=False,
            shortest_paths={},
            failure_traces={},
        )

    model = _build_transition_model(all_tasks)
    seeds = _build_seeds(tree, model)

    if not seeds:
        return ReachabilityResult(
            reachable_states=0,
            reachable_task_ids=frozenset(),
            completable_task_ids=frozenset(),
            truncated=False,
            shortest_paths={},
            failure_traces={},
        )

    visited:          Set[GameState]                         = set()
    came_from:        Dict[GameState, Tuple[GameState, str]] = {}
    first_completion: Dict[str, GameState]                   = {}
    first_active:     Dict[str, GameState]                   = {}

    reachable_task_ids:   Set[str] = set()
    completable_task_ids: Set[str] = set()
    truncated = False

    queue: deque[Tuple[GameState, int]] = deque()

    def _is_dominated(state: GameState) -> bool:
        """Return True if any visited state dominates this one."""
        for vs in visited:
            if vs.dominates(state):
                return True
        return False

    for s in seeds:
        if s not in visited and not _is_dominated(s):
            visited.add(s)
            queue.append((s, 0))
            for tid in s.active:
                if tid not in first_active:
                    first_active[tid] = s
                reachable_task_ids.add(tid)

    while queue:
        if len(visited) >= max_states:
            truncated = True
            log.warning(
                "Reachability BFS truncated at %d states (max_states=%d).",
                len(visited), max_states,
            )
            break

        state, depth = queue.popleft()

        if depth >= max_depth:
            continue

        for task_id in list(state.active):
            try:
                successor = _complete_task(task_id, state, model)
            except Exception as exc:  # noqa: BLE001
                log.debug("BFS: exception completing task %r: %s", task_id, exc)
                continue

            if successor is None:
                continue

            if task_id not in completable_task_ids:
                completable_task_ids.add(task_id)
                first_completion[task_id] = successor

            for new_tid in successor.active - state.active:
                if new_tid not in first_active:
                    first_active[new_tid] = successor
                reachable_task_ids.add(new_tid)

            if successor not in visited and not _is_dominated(successor):
                visited.add(successor)
                came_from[successor] = (state, task_id)
                queue.append((successor, depth + 1))

    # ── Reconstruct shortest paths ────────────────────────────────────────
    shortest_paths: Dict[str, List[str]] = {}
    for task_id, end_state in first_completion.items():
        path: List[str] = []
        cur = end_state
        while cur in came_from:
            parent, completed_tid = came_from[cur]
            path.append(completed_tid)
            cur = parent
        path.reverse()
        shortest_paths[task_id] = path

    # ── Build failure traces for never-completed tasks ────────────────────
    failure_traces: Dict[str, str] = {}
    for tn in all_tasks:
        tid = tn.task_id
        if tid in completable_task_ids:
            continue
        fx = model.complete_effects.get(tid)
        if fx is None:
            failure_traces[tid] = "No complete-effects entry (internal error)."
            continue
        if tid not in first_active:
            failure_traces[tid] = f"Task '{tid}' was never activated."
            continue

        best_inv: Dict[str, int] = defaultdict(int)
        for vs in visited:
            if tid in vs.active:
                for iid, cnt in vs.inventory:
                    best_inv[iid] = max(best_inv[iid], cnt)

        blocking = [
            f"item '{iid}' never reaches count {min_count} "
            f"(best seen across all active states: {best_inv.get(iid, 0)})"
            for iid, min_count in fx.requires_item.items()
            if best_inv.get(iid, 0) < min_count
        ]
        if blocking:
            failure_traces[tid] = "; ".join(blocking)
        else:
            failure_traces[tid] = (
                f"Task '{tid}' was active but never completed — "
                f"item requirements appeared satisfiable; check event conditions."
            )

    log.debug(
        "Reachability BFS complete: %d states, %d reachable, %d completable, truncated=%s",
        len(visited), len(reachable_task_ids), len(completable_task_ids), truncated,
    )

    return ReachabilityResult(
        reachable_states=len(visited),
        reachable_task_ids=frozenset(reachable_task_ids),
        completable_task_ids=frozenset(completable_task_ids),
        truncated=truncated,
        shortest_paths=shortest_paths,
        failure_traces=failure_traces,
    )


@dataclass(frozen=True)
class GameState:
    """Immutable, hashable snapshot of simulated player progress.

    ALL fields participate in hash/equality, including ``active``.
    Excluding ``active`` caused false-negatives: two states with identical
    (completed, inventory, chapter) but different active sets would collide
    in the visited set, silently dropping reachable task completions.

    State explosion is controlled instead by dominance pruning in the BFS
    (see ``explore_reachability``).

    ``inventory`` is a sorted tuple of (item_id, count) pairs with
    zero-count entries omitted.  Counts are capped at INVENTORY_COUNT_CAP.
    Only items relevant to completability are tracked.
    """
    completed: FrozenSet[str]
    active:    FrozenSet[str]
    inventory: Tuple[Tuple[str, int], ...]
    chapter:   int

    def inv_count(self, item_id: str) -> int:
        return dict(self.inventory).get(item_id, 0)

    def dominates(self, other: "GameState") -> bool:
        """Return True if self is strictly better than other in every dimension.

        A state dominates another when it has completed at least everything
        the other has, has everything active the other has, has at least as
        much of every item, and is at least as far in the chapter sequence.
        Dominated states can be pruned from the BFS frontier safely.
        """
        return (
            self.completed >= other.completed
            and self.active >= other.active
            and self.chapter >= other.chapter
            and all(
                self.inv_count(iid) >= cnt
                for iid, cnt in other.inventory
            )
        )