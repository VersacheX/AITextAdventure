"""
Dialogue tree: builder, filter, and module-level cache.
get_dialogue_tree() lives in catalog.py to avoid circular imports.
"""
from __future__ import annotations

import re
from typing import Any, Dict, List, Tuple

from tui.services.dev.dataservices.models import (
    DialogueActNode,
    DialogueChapterNode,
    DialogueLine,
    DialogueStageNode,
    DialogueTaskNode,
)

# ── Module-level tree cache (mutated by catalog._load_all) ────────────────
_DIALOG_TREE: List[DialogueActNode] = []


# ── Act / chapter metadata ────────────────────────────────────────────────

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

_REGION_STORY_META: Dict[str, Tuple[str, str]] = {
    "desert":    ("Desert",    "Sable vs Zaruun the Sand-Sunderer"),
    "forest":    ("Forest",    "Thorn vs Elder Marrowroot"),
    "grassland": ("Grassland", "Nia vs Serene the Whisper-Thief"),
    "mountains": ("Mountains", "Bragg vs Rokhuld the Core-Breaker"),
    "shallows":  ("Shallows",  "Ripple vs Uul'thar the Tide-Wakened"),
    "snow":      ("Snow",      "Kor-in vs Lady Aeriola Frostborn"),
    "swamp":     ("Swamp",     "Grimnaw vs Lich-King Miregloom"),
}


# Act label for each STORY_GROUPS key that doesn't use chapter-range grouping
_STORY_GROUP_ACT_LABELS: Dict[str, str] = {
    "regional_stories": "Regional Hero Arcs",
    "city_stories":     "City Stories",
}


# ── Public filter API ─────────────────────────────────────────────────────

def filter_dialogue_tree(
    tree: List[DialogueActNode],
    act_query: str = "",
    chapter_query: str = "",
    task_query: str = "",
    character_query: str = "",
) -> List[DialogueActNode]:
    """Return a pruned copy of ``tree`` matching every non-empty query (AND'd)."""
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


def _label_for_story(story_id: str, group_key: str) -> str:
    """Derive a human-readable chapter label from a story_id and its group key."""
    if group_key == "regional_stories":
        region_match = re.match(r"(\w+)_primary_story", story_id)
        region_key   = region_match.group(1) if region_match else story_id
        if region_key in _REGION_STORY_META:
            region_name, arc_subtitle = _REGION_STORY_META[region_key]
            return f"{region_name} Arc - {arc_subtitle}"
        return _humanize_task_id(story_id)

    if group_key == "city_stories":
        city_match = re.match(r"(\w+)_(\w+)_city_story", story_id)
        if city_match:
            region, size = city_match.group(1), city_match.group(2)
            return f"{region.title()} {size.title()} City"
        return _humanize_task_id(story_id)

    return _humanize_task_id(story_id)


# ── Builder ───────────────────────────────────────────────────────────────

def _humanize_task_id(task_id: str) -> str:
    return task_id.replace("_", " ").strip().title()


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


def _build_dialogue_tree(const: Any) -> List[DialogueActNode]:
    """Build the dialogue tree from STORY_GROUPS (main_story, regional_stories, city_stories).

    Falls back to individual MAIN_STORY_SETTINGS / PRIMARY_STORIES list access
    if STORY_GROUPS is not present so older constants still work.
    """
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

    story_groups = getattr(const, "STORY_GROUPS", None)

    if story_groups:
        # Preferred path — driven by STORY_GROUPS in declared order
        for group_key, story_list in story_groups.items():
            if not story_list:
                continue
            for story_settings in story_list:
                if not isinstance(story_settings, dict):
                    continue
                _process_story(
                    story_settings, group_key,
                    dialog_index, name_by_id, acts,
                )
    else:
        # Fallback path — individual list access (pre-STORY_GROUPS constants)
        for chapter_settings in getattr(const, "MAIN_STORY_SETTINGS", []) or []:
            if isinstance(chapter_settings, dict):
                _process_story(chapter_settings, "main_story", dialog_index, name_by_id, acts)
        for primary_story in getattr(const, "PRIMARY_STORIES", []) or []:
            if isinstance(primary_story, dict):
                _process_story(primary_story, "regional_stories", dialog_index, name_by_id, acts)

    return [
        DialogueActNode(label=act_label, chapters=list(chapters.values()))
        for act_label, chapters in acts.items()
    ]


def _process_story(
    story_settings: Dict[str, Any],
    group_key: str,
    dialog_index: Dict[Tuple[Any, Any], List[str]],
    name_by_id: Dict[str, str],
    acts: Dict[str, Dict[str, DialogueChapterNode]],
) -> None:
    """Normalize one story settings dict into the acts accumulator."""
    task_nodes = _build_task_nodes_from_chapter(story_settings, dialog_index, name_by_id)
    if not task_nodes:
        return

    if group_key == "main_story":
        # Main story: group by act ranges derived from chapter number
        chapter_id    = str(story_settings.get("chapter_id", "?"))
        chapter_num   = _chapter_number_from_id(chapter_id)
        act_label     = _act_for_chapter(chapter_num)
        chapter_label = (
            f"Chapter {chapter_num} - {_CHAPTER_TITLES[chapter_num]}"
            if chapter_num in _CHAPTER_TITLES
            else chapter_id.replace("_", " ").title()
        )
        chapters = acts.setdefault(act_label, {})
        chapters[chapter_id] = DialogueChapterNode(
            chapter_id=chapter_id,
            label=chapter_label,
            tasks=task_nodes,
        )
    else:
        # Regional / city: flat list under a single act label
        act_label  = _STORY_GROUP_ACT_LABELS.get(group_key, group_key.replace("_", " ").title())
        story_id   = str(story_settings.get("story_id", "?"))
        chapter_label = _label_for_story(story_id, group_key)
        chapters = acts.setdefault(act_label, {})
        chapters[story_id] = DialogueChapterNode(
            chapter_id=story_id,
            label=chapter_label,
            tasks=task_nodes,
        )