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

    Severity is informational — warnings (e.g. dynamic NPC references) and
    hard errors share the same type; callers may inspect ``code`` to
    distinguish them.

    Attributes:
        code:              Machine-readable error code (e.g. ``ITEM_REMOVE_WITHOUT_SOURCE``).
        message:           Human-readable description.
        event_type:        The event_type string that triggered the error, if applicable.
        related_task_id:   A secondary task id referenced by the error, if any.
        related_entity_id: An NPC id, item id, or dungeon id involved, if any.
    """
    code: str
    message: str
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


@dataclass
class NpcGroupNode:
    """Top-level NPC group: 'regional_story', 'extended', or 'main_story'."""
    group_id: str
    label: str
    npcs: List[NpcRecordNode]