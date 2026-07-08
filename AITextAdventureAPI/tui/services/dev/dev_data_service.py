"""
dev_data_service: normalizes legacy `old/game` seed data into a flat,
searchable catalog for the Dev > Data Management screen.

Mirrors `monster_log_service.py`: a thin, read-only adapter that lazily
imports `game.constants` (never at module scope, matching every other
service in this package) and reshapes its seed dicts into a single, uniform
`DevRecord` per entry. Nothing under `old/` is modified.

Because `game.constants` transitively imports hundreds of region/story/
dungeon seed modules on first use, records are built once per process via
`preload()` and cached in `_CACHE` afterwards -- callers should invoke
`preload()` from a background worker (see `tui/screens/dev/data_mgmt_screen.py`)
so that first, relatively heavy import doesn't block the compositor.

The "character_dialog" category is a special case: rather than a flat list
of `DevRecord`, it's a hierarchical Act -> Chapter -> Task -> stage -> line
tree (see `DialogueActNode` and friends below), built only from
`game.constants.MAIN_STORY_SETTINGS` since Act/Chapter is a main-story-only
concept -- region/city side-quest dialogue remains browsable via the flat
"Timeline" category instead. Use `get_dialogue_tree()` / `filter_dialogue_tree()`
rather than `get_records()` / `search_records()` for this category.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

CATEGORIES: Tuple[str, ...] = (
    "character",
    "timeline",
    "item",
    "special_item",
    "equipment",
    "dungeon",
    "city",
    "npc",
    "character_dialog",
)

CATEGORY_LABELS: Dict[str, str] = {
    "character":        "Characters",
    "timeline":         "Timeline",
    "item":             "Items",
    "special_item":     "Special Items",
    "equipment":        "Equipment",
    "dungeon":          "Dungeons",
    "city":             "Cities",
    "npc":              "NPCs",
    "character_dialog": "Dialogue",
}

_CACHE: Dict[str, List["DevRecord"]] = {}
_DIALOG_TREE: List["DialogueActNode"] = []
_TIMELINE_TREE: List[TimelineGroupNode] = []


@dataclass
class DevRecord:
    """One normalized, searchable row in the dev data browser."""

    category: str
    id: str
    name: str
    subtitle: str = ""
    detail: str = ""
    image: str = ""   # filename only (e.g. "ripple1.png"); resolved at render time
    source_group: str = ""  # NPC_GROUPS key (e.g. "main_story"); empty for non-NPC records

    def matches(self, query: str) -> bool:
        if not query:
            return True
        q = query.lower()
        return (
            q in self.id.lower()
            or q in self.name.lower()
            or q in self.subtitle.lower()
            or q in self.detail.lower()
        )


@dataclass
class DialogueLine:
    """One spoken line within a task's acquire/complete stage."""

    speaker: str
    text: str


@dataclass
class DialogueStageNode:
    """Either the 'Acquired' or 'Completed' stage of a task, with its lines."""

    label: str
    lines: List[DialogueLine]


@dataclass
class DialogueTaskNode:
    """One task within a chapter, holding its non-empty acquire/complete stages."""

    task_id: str
    label: str
    stages: List[DialogueStageNode]


@dataclass
class DialogueChapterNode:
    """One main-story chapter, holding every task that has dialogue in it."""

    chapter_id: str
    label: str
    tasks: List[DialogueTaskNode]


@dataclass
class DialogueActNode:
    """Top-level grouping of chapters, per `_ACT_CHAPTER_RANGES` below."""

    label: str
    chapters: List[DialogueChapterNode]


# ── timeline tree model ───────────────────────────────────────────────────

@dataclass
class TimelineTaskNode:
    """One task leaf in the timeline tree, carrying its raw seed dict."""

    task_id: str
    label: str
    source_path: str   # e.g. "regional:desert", "extended:desert_large", "main:ch1"
    task: Dict[str, Any]


@dataclass
class TimelineBucketNode:
    """One source bucket under a timeline group (e.g. 'desert', 'ch1')."""

    bucket_id: str
    label: str
    tasks: List[TimelineTaskNode]


@dataclass
class TimelineGroupNode:
    """Top-level timeline group: 'regional', 'extended', or 'main'."""

    group_id: str
    label: str
    buckets: List[TimelineBucketNode]


# Chapter -> Act grouping, mirroring
# `old/STORY DOCUMENTS FOR AI/ACT TIMELINE.mmd`. Chapters without a code
# seed yet (e.g. 21, still design-doc only) simply won't appear in the tree.
_ACT_CHAPTER_RANGES: Tuple[Tuple[str, int, int], ...] = (
    ("Act I - The World in Becoming",  1,  4),
    ("Act II - The Humanist Act",      5,  7),
    ("Act III - Fall of the Body",     8,  13),
    ("Act IV - Fall of the Heart",     14, 15),
    ("Act V.1 - Fall of the Mind",     16, 19),
    ("Act V.2 - Fall of Time",         20, 20),
    ("Act VI - Fall of Existence",     21, 21),
)

_CHAPTER_TITLES: Dict[int, str] = {
    1:  "Awakening",
    2:  "Black Market & Uncoupling",
    3:  "Street Justice",
    4:  "Fracture Point",
    5:  "Riftwaters Crossing",
    6:  "The Riftlands Unveiled",
    7:  "Seth's Airship & The Requirement",
    8:  "Glamour's City of Shattered Attention",
    9:  "Scalpel's Domain",
    10: "Human Chaos",
    11: "Rapture & Revelry",
    12: "Lament",
    13: "Garbage",
    14: "Stigma",
    15: "Pageant & Edict",
    16: "Path Without Meaning",
    17: "Paradox & Crux",
    18: "Reconstructing the Self",
    19: "Cataclysm",
    20: "Oracle & Reliquary",
    21: "Dominion's Gauntlet",
}

# Regional Primary Story metadata
_REGION_STORY_META: Dict[str, Tuple[str, str]] = {
    "desert":    ("Desert",    "Sable vs Zaruun the Sand-Sunderer"),
    "forest":    ("Forest",    "Thorn vs Elder Marrowroot"),
    "grassland": ("Grassland", "Nia vs Serene the Whisper-Thief"),
    "mountains": ("Mountains", "Bragg vs Rokhuld the Core-Breaker"),
    "shallows":  ("Shallows",  "Ripple vs Uul'thar the Tide-Wakened"),
    "snow":      ("Snow",      "Kor-in vs Lady Aeriola Frostborn"),
    "swamp":     ("Swamp",     "Grimnaw vs Lich-King Miregloom"),
}

_TIMELINE_GROUP_LABELS: Dict[str, str] = {
    "regional": "Regional",
    "extended": "Extended",
    "main":     "Main",
}


def preload() -> None:
    """Eagerly build and cache every category from `game.constants`.

    Call this once (from a background worker) before the screen needs any
    records -- see the module docstring for why.
    """
    if _CACHE:
        return
    _load_all()


def get_records(category: str) -> List[DevRecord]:
    """Return every `DevRecord` for `category`, building + caching on first use."""
    if not _CACHE:
        _load_all()
    return _CACHE.get(category, [])


def search_records(category: str, query: str) -> List[DevRecord]:
    """Return every record in `category` whose text matches `query` (case-insensitive)."""
    return [r for r in get_records(category) if r.matches(query)]


def filter_equipment_records(type_query: str = "", slot_query: str = "") -> List[DevRecord]:
    """
    Filter equipment records by type (Weapon/Armor) and armor slot.
    
    Args:
        type_query: Filter by equipment type (e.g., "Weapon", "Armor")
        slot_query: Filter by armor slot (e.g., "head", "body", "arms", "legs")
    
    Returns:
        List of matching DevRecord objects.
    """
    preload()  # ensure catalog is loaded
    
    all_equipment = _CACHE.get("equipment", [])
    if not type_query and not slot_query:
        return all_equipment
    
    type_lower = type_query.lower()
    slot_lower = slot_query.lower()
    
    filtered = []
    for record in all_equipment:
        # Check type match
        type_match = not type_query or type_lower in record.subtitle.lower()
        
        # Check slot match (only for armor)
        slot_match = True
        if slot_query:
            if "armor" in record.subtitle.lower():
                # For armor, check if slot is in detail or subtitle
                slot_match = slot_lower in record.detail.lower() or slot_lower in record.subtitle.lower()
            else:
                # For weapons, slot filter doesn't apply
                slot_match = False
        
        if type_match and slot_match:
            filtered.append(record)
    
    return filtered


def get_dialogue_tree() -> List[DialogueActNode]:
    """Return the cached Act -> Chapter -> Task -> stage -> line tree,
    building + caching (alongside every other category) on first use."""
    if not _CACHE:
        _load_all()
    return _DIALOG_TREE


def filter_dialogue_tree(
    tree: List[DialogueActNode],
    act_query: str = "",
    chapter_query: str = "",
    task_query: str = "",
    character_query: str = "",
) -> List[DialogueActNode]:
    """Return a pruned copy of `tree` containing only branches that match
    every non-empty query (case-insensitive substring match, AND'd together)."""
    aq  = act_query.strip().lower()
    cq  = chapter_query.strip().lower()
    tq  = task_query.strip().lower()
    chq = character_query.strip().lower()

    result: List[DialogueActNode] = []
    for act in tree:
        if aq and aq not in act.label.lower():
            continue
        chapters: List[DialogueChapterNode] = []
        for chapter in act.chapters:
            if cq and cq not in chapter.label.lower() and cq not in chapter.chapter_id.lower():
                continue
            tasks: List[DialogueTaskNode] = []
            for task in chapter.tasks:
                if tq and tq not in task.label.lower() and tq not in task.task_id.lower():
                    continue
                stages: List[DialogueStageNode] = []
                for stage in task.stages:
                    lines = [ln for ln in stage.lines if not chq or chq in ln.speaker.lower()]
                    if lines:
                        stages.append(DialogueStageNode(label=stage.label, lines=lines))
                if stages:
                    tasks.append(DialogueTaskNode(task_id=task.task_id, label=task.label, stages=stages))
            if tasks:
                chapters.append(DialogueChapterNode(chapter_id=chapter.chapter_id, label=chapter.label, tasks=tasks))
        if chapters:
            result.append(DialogueActNode(label=act.label, chapters=chapters))
    return result


def get_timeline_tree() -> List[TimelineGroupNode]:
    """Return the cached group → bucket → task tree, building on first use."""
    if not _CACHE:
        _load_all()
    return _TIMELINE_TREE


def filter_timeline_tree(
    tree: List[TimelineGroupNode],
    query: str = "",
) -> List[TimelineGroupNode]:
    """Return a pruned copy of ``tree`` matching ``query`` (case-insensitive substring).

    When a group or bucket label itself matches, all its children are kept.
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


def _load_all() -> None:
    """Build and cache records for every category from `game.constants`."""
    import game.constants as const

    _CACHE["character"]        = _build_characters(const)
    _CACHE["timeline"]         = []  # tree category; use get_timeline_tree() instead
    _CACHE["item"]             = _build_items(const)
    _CACHE["special_item"]     = _build_special_items(const)
    _CACHE["equipment"]        = _build_equipment(const)
    _CACHE["dungeon"]          = _build_dungeons(const)
    _CACHE["city"]             = _build_cities(const)
    _CACHE["npc"]              = _build_npcs(const)
    _CACHE["character_dialog"] = []  # tree category; see get_dialogue_tree() instead

    _DIALOG_TREE.clear()
    _DIALOG_TREE.extend(_build_dialogue_tree(const))

    _TIMELINE_TREE.clear()
    _TIMELINE_TREE.extend(_build_timeline_tree(const))

# ── npcs ───────────────────────────────────────────────────────────

def _build_npcs(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []

    for npc in getattr(const, "NPCS", []) or []:
        cid   = str(npc.get("npc_id", "?"))
        name  = str(npc.get("name", cid))
        desc  = str(npc.get("description", ""))
        theme_song = str(npc.get("theme_song", ""))
        image = str(npc.get("image", ""))

        psych = npc.get("psychology") or {}
        enneagram = npc.get("enneagram") or {}
        shadow_psychology = npc.get("shadow_psychology") or {}

        lines = [desc, ""]
        if theme_song:
            lines.append(f"Theme: {theme_song}")
            lines.append("")
        if psych:
            lines.append(f"MBTI: {psych.get('mbti', '?')}")
            lines.append(f"Dominant: {psych.get('dominant', '?')}")
            lines.append(f"Auxiliary: {psych.get('auxiliary', '?')}")
            lines.append(f"Tertiary: {psych.get('tertiary', '?')}")
            lines.append(f"Inferior: {psych.get('inferior', '?')}")
        if enneagram:
            lines.append("")
            lines.append(f"Enneagram: {enneagram.get('enneagram_type', '?')}")
            lines.append(f"Core fear: {enneagram.get('core_fear', '?')}")
            lines.append(f"Core desire: {enneagram.get('core_desire', '?')}")
            lines.append(f"Defense mechanism: {enneagram.get('defense_mechanism', '?')}")
            lines.append(f"Stress line: {enneagram.get('stress_line', '?')}")
            lines.append(f"Growth line: {enneagram.get('growth_line', '?')}")
            lines.append(f"Instinctual variant: {enneagram.get('instinctual_variant', '?')}")
        if shadow_psychology:
            lines.append("")
            lines.append(f"Shadow MBTI: {shadow_psychology.get('mbti', '?')}")
            lines.append(f"Shadow Dominant: {shadow_psychology.get('dominant', '?')}")
            lines.append(f"Shadow Auxiliary: {shadow_psychology.get('auxiliary', '?')}")
            lines.append(f"Shadow Tertiary: {shadow_psychology.get('tertiary', '?')}")
            lines.append(f"Shadow Inferior: {shadow_psychology.get('inferior', '?')}")

        records.append(DevRecord(
            category="npc",
            id=cid,
            name=name,
            subtitle="NPC",
            detail="\n".join(lines),
            image=image,
        ))

    return records


# ── characters ───────────────────────────────────────────────────────────

def _build_characters(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []

    for npc in getattr(const, "PLAYER_NPCS", []) or []:
        cid   = str(npc.get("npc_id", "?"))
        name  = str(npc.get("name", cid))
        desc  = str(npc.get("description", ""))
        psych = npc.get("psychology") or {}
        enneagram = npc.get("enneagram") or {}

        lines = [desc, ""]
        if psych:
            lines.append(f"MBTI: {psych.get('mbti', '?')}")
        if enneagram:
            lines.append(f"Enneagram: {enneagram.get('enneagram_type', '?')}")
            lines.append(f"Core fear: {enneagram.get('core_fear', '?')}")
            lines.append(f"Core desire: {enneagram.get('core_desire', '?')}")

        records.append(DevRecord(
            category="character",
            id=cid,
            name=name,
            subtitle="Origin party member",
            detail="\n".join(lines),
        ))

    for pc in getattr(const, "ATTAINABLE_PLAYER_CHARACTERS", []) or []:
        cid       = str(pc.get("id", "?"))
        name      = str(pc.get("name", cid))
        level     = pc.get("level", "?")
        abilities = pc.get("abilities", []) or []

        lines = [
            f"Level {level}",
            f"HP {pc.get('current_hp', '?')}/{pc.get('max_hp', '?')}   "
            f"AP {pc.get('current_ap', '?')}/{pc.get('max_ap', '?')}",
            f"STR {pc.get('strength', 0)}  DEX {pc.get('dexterity', 0)}  "
            f"INT {pc.get('intelligence', 0)}  CON {pc.get('constitution', 0)}",
            "",
            f"Weapon: {pc.get('equipped_weapon', 'None')}",
            f"Head:   {pc.get('head_armor', 'None')}",
            f"Body:   {pc.get('body_armor', 'None')}",
            f"Arms:   {pc.get('arm_armor', 'None')}",
            f"Legs:   {pc.get('leg_armor', 'None')}",
        ]
        if abilities:
            lines.append("")
            lines.append("Abilities:")
            lines.extend(f"  {a}" for a in abilities)

        records.append(DevRecord(
            category="character",
            id=cid,
            name=name,
            subtitle=f"Unlockable · Lv.{level}",
            detail="\n".join(lines),
        ))

    return records


# ── timeline (tasks) ─────────────────────────────────────────────────────

def _humanize_task_id(task_id: str) -> str:
    return task_id.replace("_", " ").strip().title()


# ── timeline tree builder ─────────────────────────────────────────────────

def _humanize_bucket_label(bucket_id: str) -> str:
    """Human-readable label for a TASK_GROUPS bucket key.

    ``ch1`` → ``Chapter 1 - Awakening``, ``desert_large`` → ``Desert Large``.
    """
    ch_match = re.match(r"^ch(\d+)$", bucket_id)
    if ch_match:
        ch_num = int(ch_match.group(1))
        title  = _CHAPTER_TITLES.get(ch_num, "")
        return f"Chapter {ch_num}{' - ' + title if title else ''}"
    return bucket_id.replace("_", " ").title()


def _build_timeline_tree(const: Any) -> List[TimelineGroupNode]:
    """Build the group → bucket → task tree from ``const.TASK_GROUPS``.

    Deduplicates tasks by task_id; first-seen group/bucket wins
    (iteration order: regional → extended → main).
    Falls back to flat ``const.TASKS`` wrapped in a single synthetic group
    if TASK_GROUPS is absent, so the screen never breaks.
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

    seen_ids: Dict[str, str] = {}   # task_id → first-seen source_path
    result: List[TimelineGroupNode] = []

    for group_key, family in task_groups.items():
        if not isinstance(family, dict):
            continue
        group_label   = _TIMELINE_GROUP_LABELS.get(group_key, group_key.replace("_", " ").title())
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
                    continue  # dedupe: first-seen group/bucket wins
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
def _build_timeline(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []

    for task in getattr(const, "TASKS", []) or []:
        if not isinstance(task, dict):
            continue
        task_id  = str(task.get("task_id", "?"))
        ttype    = str(task.get("type", "?"))
        to_type  = task.get("to_type")
        to_id    = task.get("to_id")
        acquire  = task.get("task_acquire_events", []) or []
        complete = task.get("task_complete_events", []) or []

        lines = [f"Type: {ttype}"]
        if to_type or to_id:
            lines.append(f"Target: {to_type or '?'} → {to_id or '?'}")
        if task.get("item_id"):
            lines.append(f"Item: {task['item_id']}")
        if task.get("coordinates"):
            lines.append(f"Coordinates: {task['coordinates']}")

        lines.append("")
        lines.append(f"Acquire events ({len(acquire)}):")
        for ev in acquire:
            if isinstance(ev, dict):
                lines.append(f"  - {ev.get('event_type', '?')}  {ev.get('params', {})}")

        lines.append("")
        lines.append(f"Complete events ({len(complete)}):")
        for ev in complete:
            if isinstance(ev, dict):
                lines.append(f"  - {ev.get('event_type', '?')}  {ev.get('params', {})}")

        records.append(DevRecord(
            category="timeline",
            id=task_id,
            name=_humanize_task_id(task_id),
            subtitle=ttype,
            detail="\n".join(lines),
        ))

    return records


# ── character dialogue (Act → Chapter → Task → stage → line) ────────────
# Only `game.constants.MAIN_STORY_SETTINGS` (main-story chapters) is used
# here, since Act/Chapter is a main-story-only concept -- region/city
# side-quest dialogue is still fully browsable via the flat "Timeline" tab.

def _chapter_number_from_id(chapter_id: str) -> int | None:
    match = re.search(r"(\d+)$", chapter_id or "")
    return int(match.group(1)) if match else None


def _act_for_chapter(chapter_num: int | None) -> str:
    if chapter_num is not None:
        for label, start, end in _ACT_CHAPTER_RANGES:
            if start <= chapter_num <= end:
                return label
    return "Other"


def _speaker_name(npc_id: Any, name_by_id: Dict[str, str]) -> str:
    if npc_id is None:
        return "Narrator"
    npc_id = str(npc_id)
    if npc_id in name_by_id:
        return name_by_id[npc_id]
    if npc_id in ("pending_character", "final_character", "twisted_character"):
        return f"({npc_id.replace('_', ' ').title()})"
    return npc_id.replace("_", " ").title()


def _build_dialogue_tree(const: Any) -> List[DialogueActNode]:
    """Build the dialogue tree from both MAIN_STORY_SETTINGS and PRIMARY_STORIES."""
    dialog_index: Dict[Tuple[Any, Any], List[str]] = {}
    for dlg in getattr(const, "NPC_DIALOG", []) or []:
        if not isinstance(dlg, dict):
            continue
        key = (dlg.get("npc_id"), dlg.get("dialog_id"))
        dialog_index[key] = list(dlg.get("dialog") or [])

    name_by_id: Dict[str, str] = {}
    for npc in list(getattr(const, "NPCS", []) or []) + list(getattr(const, "PLAYER_NPCS", []) or []):
        if isinstance(npc, dict) and npc.get("npc_id"):
            name_by_id[str(npc["npc_id"])] = str(npc.get("name", npc["npc_id"]))

    acts: Dict[str, Dict[str, DialogueChapterNode]] = {}

    # Build main story chapters
    for chapter_settings in getattr(const, "MAIN_STORY_SETTINGS", []) or []:
        if not isinstance(chapter_settings, dict):
            continue
        chapter_id    = str(chapter_settings.get("chapter_id", "?"))
        chapter_num   = _chapter_number_from_id(chapter_id)
        act_label     = _act_for_chapter(chapter_num)
        chapter_label = (
            f"Chapter {chapter_num} - {_CHAPTER_TITLES[chapter_num]}"
            if chapter_num in _CHAPTER_TITLES
            else chapter_id.replace("_", " ").title()
        )

        task_nodes = _build_task_nodes_from_chapter(chapter_settings, dialog_index, name_by_id)

        if not task_nodes:
            continue

        chapters = acts.setdefault(act_label, {})
        chapters[chapter_id] = DialogueChapterNode(
            chapter_id=chapter_id,
            label=chapter_label,
            tasks=task_nodes,
        )

    # Build regional primary stories as a separate "act"
    regional_act_label = "Regional Hero Arcs"
    regional_chapters: Dict[str, DialogueChapterNode] = {}

    for primary_story in getattr(const, "PRIMARY_STORIES", []) or []:
        if not isinstance(primary_story, dict):
            continue
        
        story_id = str(primary_story.get("story_id", "?"))
        # Extract region name from story_id (e.g., "desert_primary_story" -> "desert")
        region_match = re.match(r"(\w+)_primary_story", story_id)
        region_key = region_match.group(1) if region_match else story_id
        
        if region_key in _REGION_STORY_META:
            region_name, arc_subtitle = _REGION_STORY_META[region_key]
            chapter_label = f"{region_name} Arc - {arc_subtitle}"
        else:
            chapter_label = _humanize_task_id(story_id)

        # Build task nodes from the primary story's tasks
        task_nodes = _build_task_nodes_from_chapter(primary_story, dialog_index, name_by_id)

        if task_nodes:
            regional_chapters[story_id] = DialogueChapterNode(
                chapter_id=story_id,
                label=chapter_label,
                tasks=task_nodes,
            )

    if regional_chapters:
        acts[regional_act_label] = regional_chapters

    return [
        DialogueActNode(label=act_label, chapters=list(chapters.values()))
        for act_label, chapters in acts.items()
    ]


def _build_task_nodes_from_chapter(
    chapter_or_story: Dict[str, Any],
    dialog_index: Dict[Tuple[Any, Any], List[str]],
    name_by_id: Dict[str, str],
) -> List[DialogueTaskNode]:
    """Extract task nodes with dialogue from a chapter or primary story settings dict."""
    task_nodes: List[DialogueTaskNode] = []
    
    for task in chapter_or_story.get("tasks", []) or []:
        if not isinstance(task, dict):
            continue
        task_id = str(task.get("task_id", "?"))

        stages: List[DialogueStageNode] = []
        for stage_key, stage_label in (("task_acquire_events", "Acquired"), ("task_complete_events", "Completed")):
            lines: List[DialogueLine] = []
            for ev in task.get(stage_key) or []:
                if not isinstance(ev, dict):
                    continue
                if ev.get("event_type") not in ("initiate_dialog", "initiate_character_dialog"):
                    continue
                params    = ev.get("params") or {}
                dlg_lines = dialog_index.get((params.get("npc_id"), params.get("dialog_id")))
                if not dlg_lines:
                    continue
                speaker = _speaker_name(params.get("npc_id"), name_by_id)
                lines.extend(DialogueLine(speaker=speaker, text=str(t)) for t in dlg_lines)
            if lines:
                stages.append(DialogueStageNode(label=stage_label, lines=lines))

        if stages:
            task_nodes.append(DialogueTaskNode(
                task_id=task_id,
                label=_humanize_task_id(task_id),
                stages=stages,
            ))
    
    return task_nodes


# ── items / special items ───────────────────────────────────────────────

def _build_items(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []

    for seed in getattr(const, "UTILITY_ITEM_SEEDS", []) or []:
        rid    = str(seed.get("id", "?"))
        name   = str(seed.get("name", rid))
        rarity = str(seed.get("rarity", "?"))
        lvl    = seed.get("min_spawn_level", "?")

        lines = [
            str(seed.get("description", "")),
            "",
            f"Effect: {seed.get('effect', '?')}",
            f"Value: {seed.get('value', 0)}   Uses: {seed.get('uses', 1)}",
            f"Rarity: {rarity}   Min level: {lvl}",
        ]
        records.append(DevRecord(
            category="item",
            id=rid,
            name=name,
            subtitle=f"{rarity} · Lv.{lvl}",
            detail="\n".join(lines),
        ))

    return records


def _build_special_items(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []

    for seed in getattr(const, "SPECIAL_ITEM_SEEDS", []) or []:
        rid    = str(seed.get("id", "?"))
        name   = str(seed.get("name", rid))
        rarity = str(seed.get("rarity", "?"))

        lines = [str(seed.get("description", ""))]
        effect_desc = seed.get("effect_description")
        if effect_desc:
            lines.append("")
            lines.append(f"Effect: {effect_desc}")

        records.append(DevRecord(
            category="special_item",
            id=rid,
            name=name,
            subtitle=rarity,
            detail="\n".join(lines),
        ))

    return records


# ── equipment (weapons + armor) ──────────────────────────────────────────

def _build_equipment(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []

    for seed in getattr(const, "WEAPON_SEEDS", []) or []:
        rid    = str(seed.get("id", "?"))
        name   = str(seed.get("name", rid))
        rarity = str(seed.get("rarity", "?"))
        lvl    = seed.get("min_spawn_level", "?")

        lines = [
            str(seed.get("description", "")),
            "",
            f"Damage: {seed.get('damage', 0)} ({seed.get('damage_type', '?')})   "
            f"Crit: {seed.get('critical_chance', 0)}%",
            f"STR {seed.get('strength', 0)}  DEX {seed.get('dexterity', 0)}  "
            f"INT {seed.get('intelligence', 0)}",
            f"Value: {seed.get('value', 0)}   Rarity: {rarity}   Min level: {lvl}",
        ]
        records.append(DevRecord(
            category="equipment",
            id=rid,
            name=name,
            subtitle=f"Weapon · {rarity} · Lv.{lvl}",
            detail="\n".join(lines),
        ))

    armor_seeds = getattr(const, "ARMOR_SEEDS", {}) or {}
    for slot, seeds in armor_seeds.items():
        for seed in seeds or []:
            rid    = str(seed.get("id", "?"))
            name   = str(seed.get("name", rid))
            rarity = str(seed.get("rarity", "?"))
            lvl    = seed.get("min_spawn_level", "?")

            lines = [
                str(seed.get("description", "")),
                "",
                f"Defense: {seed.get('defense', 0)}   Slot: {slot}",
                f"STR {seed.get('strength', 0)}  DEX {seed.get('dexterity', 0)}  "
                f"INT {seed.get('intelligence', 0)}  CON {seed.get('constitution', 0)}",
                f"Value: {seed.get('value', 0)}   Rarity: {rarity}   Min level: {lvl}",
            ]
            records.append(DevRecord(
                category="equipment",
                id=rid,
                name=name,
                subtitle=f"Armor ({slot}) · {rarity} · Lv.{lvl}",
                detail="\n".join(lines),
            ))

    return records


# ── dungeons ─────────────────────────────────────────────────────────────

def _build_dungeons(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []

    for seed in getattr(const, "DUNGEON_SETTINGS", []) or []:
        if not isinstance(seed, dict):
            continue
        did      = str(seed.get("dungeon_id", "?"))
        name     = str(seed.get("display_name", did))
        hostiles = seed.get("hostile_seeds", []) or []
        boss     = seed.get("boss_hostiles", []) or []
        npcs     = seed.get("npcs", []) or []
        items    = seed.get("items", []) or []

        lines = [
            f"Floors: {seed.get('floor_count', '?')}   Rooms/floor: {seed.get('rooms_per_floor', '?')}",
            f"Hostiles: {len(hostiles)}   Boss hostiles: {len(boss)}",
        ]
        if hostiles:
            lines.append("")
            lines.append("Hostiles:")
            lines.extend(
                f"  - {h.get('name', h.get('id', '?'))}" for h in hostiles if isinstance(h, dict)
            )
        if boss:
            lines.append("")
            lines.append("Boss:")
            lines.extend(
                f"  - {b.get('name', b.get('id', '?'))}" for b in boss if isinstance(b, dict)
            )
        if npcs:
            lines.append("")
            lines.append(f"NPCs: {', '.join(str(n.get('id', '?')) for n in npcs if isinstance(n, dict))}")
        if items:
            lines.append(f"Items: {', '.join(str(i.get('id', '?')) for i in items if isinstance(i, dict))}")

        records.append(DevRecord(
            category="dungeon",
            id=did,
            name=name,
            subtitle=f"{len(hostiles)} hostiles · {len(boss)} boss",
            detail="\n".join(lines),
        ))

    return records


# ── cities ───────────────────────────────────────────────────────────────
# City data has no single aggregate list -- it's exported as separate
# per-region/per-size constants (e.g. `DESERT_LARGE_CITY_CITY_NAME`,
# `DESERT_LARGE_CITY_BUILDINGS`, ...). Rather than hardcode all
# 7 regions x 3 sizes x N fields worth of aliases, look them up reflectively
# from the naming convention `game.constants` already follows. Some aliases
# have small typos upstream (e.g. one city's `_CITY_DESCRIPTION`) -- `getattr`
# with a default tolerates that gracefully instead of crashing the browser.

_CITY_FIELDS: Tuple[str, ...] = ("CITY_NAME", "CITY_DESCRIPTION", "BUILDINGS")


def _build_cities(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []
    regions = getattr(const, "AVAILABLE_REGIONS", []) or []
    sizes   = getattr(const, "AVAILABLE_CITIES", []) or []

    for region in regions:
        for size in sizes:
            prefix  = f"{region.upper()}_{size.upper()}"
            city_id = f"{region}_{size}"
            fields: Dict[str, Any] = {
                f: getattr(const, f"{prefix}_{f}", None) for f in _CITY_FIELDS
            }

            name        = fields.get("CITY_NAME") or city_id.replace("_", " ").title()
            description = fields.get("CITY_DESCRIPTION") or "No description available."
            buildings   = fields.get("BUILDINGS") or []

            lines = [str(description)]
            if buildings:
                lines.append("")
                lines.append(f"Buildings ({len(buildings)}):")
                lines.extend(
                    f"  - {b.get('display_name', b.get('name', '?'))} ({b.get('type', '?')})"
                    for b in buildings if isinstance(b, dict)
                )

            records.append(DevRecord(
                category="city",
                id=city_id,
                name=str(name),
                subtitle=f"{region.title()} · {size.replace('_', ' ').title()}",
                detail="\n".join(lines),
            ))

    return records