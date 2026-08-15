"""
All dataclasses shared across the dev data services.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class DevRecord:
    """One normalized, searchable row in the dev data browser."""

    category: str
    id: str
    name: str
    subtitle: str = ""
    detail: str = ""
    image: str = ""        # filename only (e.g. "ripple1.png"); resolved at render time
    source_group: str = "" # NPC_GROUPS key (e.g. "main_story"); empty for non-NPC records
    song_id: str = ""      # audio track reference key (e.g. "hero_instrumental_skillet")
    extras: Dict[str, Any] = field(default_factory=dict)  # raw numeric stats for sorting

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


# ── Dialogue tree model ───────────────────────────────────────────────────

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
    """Top-level grouping of chapters, per _ACT_CHAPTER_RANGES."""
    label: str
    chapters: List[DialogueChapterNode]


# ── Timeline validation model ─────────────────────────────────────────────

@dataclass
class TimelineValidationError:
    """One integrity error attached to a TimelineTaskNode.

    Attributes:
        code:              Machine-readable error code.
        message:           Human-readable description.
        severity:          ``"error"`` (red), ``"warning"`` (yellow),
                           ``"info"`` (cyan — informational, not a fault),
                           ``"notice"`` (magenta — deterministic authoring hint),
                           or ``"duplicate"`` (light violet — duplicate award).
        event_type:        The event_type string that triggered the error, if applicable.
        related_task_id:   A secondary task id referenced by the error, if any.
        related_entity_id: An NPC id, item id, or dungeon id involved, if any.
    """
    code: str
    message: str
    severity: str = "error"   # "error" | "warning" | "info" | "notice" | "duplicate"
    event_type: str = ""
    related_task_id: str = ""
    related_entity_id: str = ""


# ── Timeline tree model ───────────────────────────────────────────────────

@dataclass
class TimelineTaskNode:
    """One task leaf in the timeline tree, carrying its raw seed dict."""
    task_id: str
    label: str
    source_path: str   # e.g. "regional:desert", "extended:desert_large", "main:ch1"
    task: Dict[str, Any]
    # Validation errors — empty until validate_timeline_integrity() is called
    errors: List[TimelineValidationError] = field(default_factory=list)


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


# ── NPC tree model ────────────────────────────────────────────────────────

@dataclass
class NpcRecordNode:
    """One NPC leaf in the NPC tree, carrying its pre-built DevRecord."""
    npc_id: str
    label: str          # NPC display name
    group_id: str       # "regional_story", "extended", "main_story"
    source_group: str   # Humanized group label, e.g. "Regional Story"
    record: DevRecord   # Full DevRecord (includes image, detail, psychology …)
    mbti: str = ""      # e.g. "INTJ"
    enneagram: str = "" # e.g. "5w4"


@dataclass
class NpcGroupNode:
    group_id: str
    label: str
    npcs: List[NpcRecordNode]


# ── Ability tree model ────────────────────────────────────────────────────

@dataclass
class AbilityValidationError:
    """One validation error attached to an AbilityNode."""
    code: str
    message: str
    severity: str = "error"   # "error" | "warning"


@dataclass
class AbilityNode:
    """One ability leaf in the ability tree."""
    ability_id: str
    label: str
    ability_type: str   # "technique" | "faith" | "magic" | "tech" | "skill"
    level: int
    record: DevRecord
    errors: List[AbilityValidationError] = field(default_factory=list)


@dataclass
class AbilityLevelNode:
    """A level bucket under an ability-type group."""
    level: int
    label: str          # e.g. "Level 1"
    abilities: List[AbilityNode]


@dataclass
class AbilityTypeNode:
    type_id: str
    label: str
    level_buckets: List[AbilityLevelNode]


# ── Hostile tree model ────────────────────────────────────────────────────

@dataclass
class HostileValidationError:
    code: str
    message: str
    severity: str = "error"   # "error" | "warning"


@dataclass
class HostileNode:
    """One hostile leaf in the hostile tree."""
    hostile_id: str
    label: str
    rarity: str     # "common" | "uncommon" | "rare" | "superrare" | "notfound"
    level: int
    source_list: str    # attribute name the seed came from, e.g. "FOREST_RANDOM_HOSTILE_SEEDS"
    record: DevRecord
    seed: Dict[str, Any] = field(default_factory=dict)
    errors: List[HostileValidationError] = field(default_factory=list)
    location_dungeon: str = ""   # Dungeon display name, or "Overworld"
    location_region: str = ""    # Region name or city name


@dataclass
class HostileLevelBucketNode:
    """A level-range bucket under a rarity group, e.g. 'Lv 1–5'."""
    bucket_id: str      # e.g. "lv_01_05"
    label: str          # e.g. "Lv 1–5"
    level_min: int
    level_max: int
    hostiles: List[HostileNode]


@dataclass
class HostileRarityNode:
    """Top-level rarity group: Common, Uncommon, Rare, Super Rare."""
    rarity_id: str      # "common" | "uncommon" | "rare" | "superrare" | "notfound"
    label: str
    level_buckets: List[HostileLevelBucketNode]


# ── Dungeon tree model ────────────────────────────────────────────────────

@dataclass
class DungeonValidationError:
    """One validation error attached to a DungeonNode."""
    code: str
    message: str
    severity: str = "error"   # "error" | "warning" | "notice"


@dataclass
class DungeonNode:
    """One dungeon leaf in the dungeon tree."""
    dungeon_id: str
    label: str          # display_name
    group_id: str       # "main_story" | "primary_story" | "city_regional"
    record: DevRecord
    settings: Dict[str, Any] = field(default_factory=dict)
    errors: List[DungeonValidationError] = field(default_factory=list)


@dataclass
class DungeonGroupNode:
    """Top-level dungeon source group."""
    group_id: str       # "main_story" | "primary_story" | "city_regional"
    label: str
    dungeons: List[DungeonNode]


# ── Special item validation model ───────────────────────────────────────

@dataclass
class SpecialItemValidationError:
    """One validation error attached to a special-item DevRecord."""
    code: str
    message: str
    severity: str = "error"   # "error" | "info"


# ── Equipment validation model ────────────────────────────────────────────

@dataclass
class EquipmentValidationError:
    """One validation error attached to an equipment DevRecord."""
    code: str
    message: str
    severity: str = "error"   # "error" | "warning" | "info"