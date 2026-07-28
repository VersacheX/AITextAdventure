"""
Public API for the dev data services package.
"""
from __future__ import annotations

# Models
from tui.services.dev.dataservices.models import (
    AbilityLevelNode,
    AbilityNode,
    AbilityTypeNode,
    AbilityValidationError,
    DevRecord,
    DialogueActNode,
    DialogueChapterNode,
    DialogueLine,
    DialogueStageNode,
    DialogueTaskNode,
    DungeonGroupNode,
    DungeonNode,
    DungeonValidationError,
    HostileLevelBucketNode,
    HostileNode,
    HostileRarityNode,
    HostileValidationError,
    NpcGroupNode,
    NpcRecordNode,
    TimelineBucketNode,
    TimelineGroupNode,
    TimelineTaskNode,
)

# Dialogue
from tui.services.dev.dataservices.dialogue_service import filter_dialogue_tree

# Timeline
from tui.services.dev.dataservices.timeline_service import filter_timeline_tree

# NPC
from tui.services.dev.dataservices.npc_service import filter_npc_tree

# ABILITY
from tui.services.dev.dataservices.ability_service import filter_ability_tree

# HOSTILE
from tui.services.dev.dataservices.hostile_service import filter_hostile_tree

# DUNGEON
from tui.services.dev.dataservices.dungeon_service import filter_dungeon_tree

# Catalog (CATEGORIES, preload, get_records, tree getters)
from tui.services.dev.dataservices.catalog import (
    CATEGORIES,
    CATEGORY_LABELS,
    filter_equipment_records,
    get_ability_tree,
    get_dialog_index,
    get_dialogue_tree,
    get_dungeon_tree,
    get_hostile_tree,
    get_npc_names,
    get_npc_tree,
    get_records,
    get_timeline_tree,
    preload,
    search_records,
)

__all__ = [
    # models
    "DevRecord",
    "DialogueLine", "DialogueStageNode", "DialogueTaskNode",
    "DialogueChapterNode", "DialogueActNode",
    "TimelineTaskNode", "TimelineBucketNode", "TimelineGroupNode",
    "NpcRecordNode", "NpcGroupNode",
    "AbilityNode", "AbilityLevelNode", "AbilityTypeNode", "AbilityValidationError",
    "HostileNode", "HostileLevelBucketNode", "HostileRarityNode", "HostileValidationError",
    "DungeonNode", "DungeonGroupNode", "DungeonValidationError",
    # catalogue
    "CATEGORIES", "CATEGORY_LABELS",
    "preload", "get_records", "search_records", "filter_equipment_records",
    # tree getters
    "get_dialogue_tree", "filter_dialogue_tree",
    "get_timeline_tree", "filter_timeline_tree",
    "get_npc_tree", "filter_npc_tree",
    "get_ability_tree", "filter_ability_tree",
    "get_hostile_tree", "filter_hostile_tree",
    "get_dungeon_tree", "filter_dungeon_tree",
]