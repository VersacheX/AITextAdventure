"""
Timeline tree: builder, filter, and module-level cache.
get_timeline_tree() lives in catalog.py to avoid circular imports.
"""
from __future__ import annotations

import re
from typing import Any, Dict, List, Tuple

from tui.services.dev.dataservices.models import (
    TimelineBucketNode,
    TimelineGroupNode,
    TimelineTaskNode,
)

# ── Module-level tree cache (mutated by catalog._load_all) ────────────────
_TIMELINE_TREE: List[TimelineGroupNode] = []

# ── Group/bucket labels ───────────────────────────────────────────────────

_TIMELINE_GROUP_LABELS: Dict[str, str] = {
    "main":     "Main",
    "regional": "Regional",
    "extended": "Extended",
}

_CHAPTER_TITLES: Dict[int, str] = {
    1:  "Awakening",           2:  "Black Market & Uncoupling",
    3:  "Street Justice",      4:  "Fracture Point",
    5:  "Riftwaters Crossing", 6:  "The Riftlands Unveiled",
    7:  "Seth's Airship & The Requirement",
    8:  "Glamour's City of Shattered Attention",
    9:  "Scalpel's Domain",    10: "Human Chaos",
    11: "Rapture & Revelry",   12: "Lament",
    13: "Garbage",             14: "Stigma",
    15: "Pageant & Edict",     16: "Path Without Meaning",
    17: "Paradox & Crux",      18: "Reconstructing the Self",
    19: "Cataclysm",           20: "Oracle & Reliquary",
    21: "Dominion's Gauntlet",
}


# ── City metadata lookup (chapter + continent per extended bucket) ─────────

def _build_city_metadata() -> Dict[str, Tuple[int, int]]:
    """Return a mapping of extended bucket_key → (chapter_number, continent_number).

    Derives from CHAPTER_CITY_ORDER and CONTINENT_COMPOSITION in world_constants.
    Extended bucket keys are city keys with the trailing ``_city`` stripped:
    ``"desert_large_city"`` → ``"desert_large"``.
    """
    try:
        from game.region_seeds.world_constants import (
            CHAPTER_CITY_ORDER,
            CONTINENT_COMPOSITION,
        )
    except ImportError:
        return {}

    meta: Dict[str, Tuple[int, int]] = {}
    continent     = 1
    comp_idx      = 0
    cities_left   = CONTINENT_COMPOSITION[0] if CONTINENT_COMPOSITION else 0

    for chapter_num, city_key in enumerate(CHAPTER_CITY_ORDER, start=1):
        bucket_key = city_key[:-5] if city_key.endswith("_city") else city_key
        meta[bucket_key] = (chapter_num, continent)

        cities_left -= 1
        if cities_left == 0:
            comp_idx += 1
            continent += 1
            cities_left = (
                CONTINENT_COMPOSITION[comp_idx]
                if comp_idx < len(CONTINENT_COMPOSITION)
                else 0
            )

    return meta


_CITY_METADATA: Dict[str, Tuple[int, int]] = _build_city_metadata()


# ── Public filter API ─────────────────────────────────────────────────────

def filter_timeline_tree(
    tree: List[TimelineGroupNode],
    query: str = "",
) -> List[TimelineGroupNode]:
    """Return a pruned copy of ``tree`` matching ``query`` (case-insensitive).

    Group/bucket label matches keep the full subtree.
    Otherwise individual task_id / label / source_path are matched.
    """
    if not query:
        return tree
    q = query.strip().lower()
    result: List[TimelineGroupNode] = []
    for group in tree:
        group_matches = q in group.label.lower() or q in group.group_id.lower()
        filtered_buckets: List[TimelineBucketNode] = []
        for bucket in group.buckets:
            bucket_matches = q in bucket.label.lower() or q in bucket.bucket_id.lower()
            if group_matches or bucket_matches:
                filtered_buckets.append(bucket)
            else:
                tasks = [
                    t for t in bucket.tasks
                    if q in t.task_id.lower()
                    or q in t.label.lower()
                    or q in t.source_path.lower()
                ]
                if tasks:
                    filtered_buckets.append(TimelineBucketNode(
                        bucket_id=bucket.bucket_id,
                        label=bucket.label,
                        tasks=tasks,
                    ))
        if filtered_buckets:
            result.append(TimelineGroupNode(
                group_id=group.group_id,
                label=group.label,
                buckets=filtered_buckets,
            ))
    return result


# ── Builder ───────────────────────────────────────────────────────────────

def _humanize_task_id(task_id: str) -> str:
    return task_id.replace("_", " ").strip().title()


def _humanize_bucket_label(bucket_id: str) -> str:
    """Format a bucket_id as a human-readable label.

    - ``ch1`` → ``Chapter 1 - Awakening``
    - ``desert_large`` (extended city) → ``Desert Large City  Ch.1  Cont.1``
    - anything else → title-cased words
    """
    ch_match = re.match(r"^ch(\d+)$", bucket_id)
    if ch_match:
        ch_num = int(ch_match.group(1))
        title  = _CHAPTER_TITLES.get(ch_num, "")
        return f"Chapter {ch_num}{' - ' + title if title else ''}"

    city_meta = _CITY_METADATA.get(bucket_id)
    if city_meta:
        ch_num, cont_num = city_meta
        base = bucket_id.replace("_", " ").title() + " City"
        return f"{base}  Ch.{ch_num}  Cont.{cont_num}"

    return bucket_id.replace("_", " ").title()


def _build_timeline_tree(const: Any) -> List[TimelineGroupNode]:
    """Build the group → bucket → task tree from ``const.TASK_GROUPS``.

    Deduplicates tasks by task_id; first-seen group/bucket wins
    (iteration order: regional → extended → main).
    Falls back to a flat ``const.TASKS`` wrap if TASK_GROUPS is absent.
    """
    task_groups = getattr(const, "TASK_GROUPS", None)
    if not task_groups:
        tasks = [
            TimelineTaskNode(
                task_id=str(t.get("task_id", "?")),
                label=_humanize_task_id(str(t.get("task_id", "?"))),
                source_path="all",
                task=t,
            )
            for t in getattr(const, "TASKS", []) or []
            if isinstance(t, dict)
        ]
        if not tasks:
            return []
        return [TimelineGroupNode(
            group_id="all",
            label="All",
            buckets=[TimelineBucketNode(bucket_id="all", label="All", tasks=tasks)],
        )]

    seen_ids: Dict[str, str] = {}
    result: List[TimelineGroupNode] = []

    for group_key, family in task_groups.items():
        if not isinstance(family, dict):
            continue
        group_label  = _TIMELINE_GROUP_LABELS.get(group_key, group_key.replace("_", " ").title())
        bucket_nodes: List[TimelineBucketNode] = []

        for bucket_key, task_list in family.items():
            bucket_label = _humanize_bucket_label(bucket_key)
            source_path  = f"{group_key}:{bucket_key}"
            task_nodes: List[TimelineTaskNode] = []

            for task in task_list or []:
                if not isinstance(task, dict):
                    continue
                task_id = str(task.get("task_id", "?"))
                if task_id in seen_ids:
                    continue
                seen_ids[task_id] = source_path
                task_nodes.append(TimelineTaskNode(
                    task_id=task_id,
                    label=_humanize_task_id(task_id),
                    source_path=source_path,
                    task=task,
                ))

            if task_nodes:
                bucket_nodes.append(TimelineBucketNode(
                    bucket_id=bucket_key,
                    label=bucket_label,
                    tasks=task_nodes,
                ))

        if bucket_nodes:
            result.append(TimelineGroupNode(
                group_id=group_key,
                label=group_label,
                buckets=bucket_nodes,
            ))

    return result