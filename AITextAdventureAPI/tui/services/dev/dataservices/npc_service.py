"""
NPC tree: builder, filter, and module-level cache.
get_npc_tree() lives in catalog.py to avoid circular imports.
"""
from __future__ import annotations

from typing import Any, Dict, List

from tui.services.dev.dataservices.models import DevRecord, NpcGroupNode, NpcRecordNode

# ── Module-level tree cache (mutated by catalog._load_all) ────────────────
_NPC_TREE: List[NpcGroupNode] = []

# ── Group labels ──────────────────────────────────────────────────────────

_NPC_GROUP_LABELS: Dict[str, str] = {
    "regional_story": "Regional Story",
    "main_story":     "Main Story",
    "extended":       "Extended",
}


# ── Public filter API ─────────────────────────────────────────────────────

def filter_npc_tree(
    tree: List[NpcGroupNode],
    query: str = "",
) -> List[NpcGroupNode]:
    """Return a pruned copy of ``tree`` matching ``query`` (case-insensitive).

    Group label match keeps the full group.
    Otherwise individual npc_id / name / detail are matched.
    """
    if not query:
        return tree
    q = query.strip().lower()
    result: List[NpcGroupNode] = []
    for group in tree:
        group_matches = q in group.label.lower() or q in group.group_id.lower()
        if group_matches:
            result.append(group)
        else:
            npcs = [
                n for n in group.npcs
                if q in n.npc_id.lower()
                or q in n.label.lower()
                or q in n.record.detail.lower()
            ]
            if npcs:
                result.append(NpcGroupNode(
                    group_id=group.group_id,
                    label=group.label,
                    npcs=npcs,
                ))
    return result


# ── Builder ───────────────────────────────────────────────────────────────

def _make_npc_record(npc: Dict[str, Any], subtitle: str, source_group: str) -> DevRecord:
    """Normalize a raw NPC seed dict into a DevRecord."""
    cid        = str(npc.get("npc_id", "?"))
    name       = str(npc.get("name", cid))
    desc       = str(npc.get("description", ""))
    theme_song = str(npc.get("theme_song", ""))
    image      = str(npc.get("image", ""))

    psych  = npc.get("psychology") or {}
    ennea  = npc.get("enneagram") or {}
    shadow = npc.get("shadow_psychology") or {}

    group_label = _NPC_GROUP_LABELS.get(source_group, source_group.replace("_", " ").title())

    lines: List[str] = []
    if source_group:
        lines.append(f"Source: {group_label}")
        lines.append("")
    lines.append(desc)
    lines.append("")
    if theme_song:
        lines.append(f"Theme: {theme_song}")
        lines.append("")
    if psych:
        lines.append(f"MBTI: {psych.get('mbti', '?')}")
        lines.append(f"Dominant: {psych.get('dominant', '?')}")
        lines.append(f"Auxiliary: {psych.get('auxiliary', '?')}")
        lines.append(f"Tertiary: {psych.get('tertiary', '?')}")
        lines.append(f"Inferior: {psych.get('inferior', '?')}")
    if ennea:
        lines.append("")
        lines.append(f"Enneagram: {ennea.get('enneagram_type', '?')}")
        lines.append(f"Core fear: {ennea.get('core_fear', '?')}")
        lines.append(f"Core desire: {ennea.get('core_desire', '?')}")
        lines.append(f"Defense mechanism: {ennea.get('defense_mechanism', '?')}")
        lines.append(f"Stress line: {ennea.get('stress_line', '?')}")
        lines.append(f"Growth line: {ennea.get('growth_line', '?')}")
        lines.append(f"Instinctual variant: {ennea.get('instinctual_variant', '?')}")
    if shadow:
        lines.append("")
        lines.append(f"Shadow MBTI: {shadow.get('mbti', '?')}")
        lines.append(f"Shadow Dominant: {shadow.get('dominant', '?')}")
        lines.append(f"Shadow Auxiliary: {shadow.get('auxiliary', '?')}")
        lines.append(f"Shadow Tertiary: {shadow.get('tertiary', '?')}")
        lines.append(f"Shadow Inferior: {shadow.get('inferior', '?')}")

    return DevRecord(
        category="npc",
        id=cid,
        name=name,
        subtitle=subtitle,
        detail="\n".join(lines),
        image=image,
        source_group=source_group,
    )


def _build_npc_tree(const: Any) -> List[NpcGroupNode]:
    """Build the group → NPC tree from ``const.NPC_GROUPS``.

    Priority order: regional_story → extended → main_story.
    Raises ValueError immediately if a duplicate npc_id is detected.
    Falls back to flat ``const.NPCS`` if NPC_GROUPS is absent.
    """
    npc_groups = getattr(const, "NPC_GROUPS", None)
    if not npc_groups:
        npcs = []
        for npc in getattr(const, "NPCS", []) or []:
            if not isinstance(npc, dict):
                continue
            cid    = str(npc.get("npc_id", "?"))
            record = _make_npc_record(npc, "NPC", "")
            npcs.append(NpcRecordNode(
                npc_id=cid,
                label=str(npc.get("name", cid)),
                group_id="all",
                source_group="",
                record=record,
            ))
        if not npcs:
            return []
        return [NpcGroupNode(group_id="all", label="All", npcs=npcs)]

    seen_ids: Dict[str, str] = {}   # npc_id → first-seen group_id
    result: List[NpcGroupNode] = []

    for group_key, npc_list in npc_groups.items():
        group_label = _NPC_GROUP_LABELS.get(group_key, group_key.replace("_", " ").title())
        subtitle    = f"NPC · {group_label}"
        npc_nodes: List[NpcRecordNode] = []

        for npc in npc_list or []:
            if not isinstance(npc, dict):
                continue
            cid = str(npc.get("npc_id", "?"))
            if cid in seen_ids:
                raise ValueError(
                    f"Duplicate npc_id detected: '{cid}' "
                    f"(first seen in group '{seen_ids[cid]}', also found in group '{group_key}')"
                )
            seen_ids[cid] = group_key
            record = _make_npc_record(npc, subtitle, group_key)
            npc_nodes.append(NpcRecordNode(
                npc_id=cid,
                label=str(npc.get("name", cid)),
                group_id=group_key,
                source_group=group_label,
                record=record,
            ))

        if npc_nodes:
            result.append(NpcGroupNode(
                group_id=group_key,
                label=group_label,
                npcs=npc_nodes,
            ))

    return result