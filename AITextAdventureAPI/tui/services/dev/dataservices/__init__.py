"""
Public API for the dev data services package.

All consumers should import from here:
    from tui.services.dev.dataservices import DevRecord, preload, ...
"""
from __future__ import annotations

# Models
from tui.services.dev.dataservices.models import (
    DevRecord,
    DialogueActNode,
    DialogueChapterNode,
    DialogueLine,
    DialogueStageNode,
    DialogueTaskNode,
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

# Catalog (CATEGORIES, preload, get_records, tree getters …)
from tui.services.dev.dataservices.catalog import (
    CATEGORIES,
    CATEGORY_LABELS,
    filter_equipment_records,
    get_dialogue_tree,
    get_npc_tree,
    get_records,
    get_timeline_tree,
    preload,
    search_records,
)

__all__ = [
    # models
    "DevRecord", "DialogueLine", "DialogueStageNode", "DialogueTaskNode",
    "DialogueChapterNode", "DialogueActNode",
    "TimelineTaskNode", "TimelineBucketNode", "TimelineGroupNode",
    "NpcRecordNode", "NpcGroupNode",
    # catalogue
    "CATEGORIES", "CATEGORY_LABELS",
    "preload", "get_records", "search_records", "filter_equipment_records",
    # tree getters
    "get_dialogue_tree", "filter_dialogue_tree",
    "get_timeline_tree", "filter_timeline_tree",
    "get_npc_tree", "filter_npc_tree",
]