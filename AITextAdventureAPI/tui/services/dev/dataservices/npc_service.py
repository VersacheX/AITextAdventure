"""
NPC tree: builder, filter, and module-level cache.
get_npc_tree() lives in catalog.py to avoid circular imports.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

from tui.services.dev.dataservices.models import DevRecord, NpcGroupNode, NpcRecordNode
from tui.services.dev.dataservices.timeline_service import _CITY_METADATA

# ── Module-level tree cache (mutated by catalog._load_all) ────────────────
_NPC_TREE: List[NpcGroupNode] = []

# ── Group labels ──────────────────────────────────────────────────────────

_NPC_GROUP_LABELS: Dict[str, str] = {
    "regional_story": "Regional Story",
    "main_story":     "Main Story",
    "extended":       "Extended",
}

# ── Event types that affect NPC placement ─────────────────────────────────

_PLACEMENT_EVENT_TYPES = frozenset({"create_npc", "show_npc", "hide_npc"})

# ── Human-readable building type labels ───────────────────────────────────

_BUILDING_TYPE_LABELS: Dict[str, str] = {
    "bar":            "bar",
    "inn":            "inn",
    "shopweapons":    "weapon shop",
    "shopitems":      "item shop",
    "shoparmor":      "armor shop",
    "residencelarge": "large residence",
    "residencesmall": "small residence",
    "businesslarge":  "large business",
    "businesssmall":  "small business",
    "hyperway":       "hyperway",
    "other1":         "other",
    "other2":         "other",
}

# ── Event action labels ───────────────────────────────────────────────────

_EVENT_ACTION_LABELS: Dict[str, str] = {
    "create_npc": "Create",
    "show_npc":   "Show",
    "hide_npc":   "Hide",
}

# ── Chapter → city bucket map (derived from world_constants) ─────────────

def _build_chapter_to_city_bucket() -> Dict[int, str]:
    """Return {chapter_number: bucket_key} e.g. {2: 'forest_mid'}."""
    try:
        from game.region_seeds.world_constants import CHAPTER_CITY_ORDER
    except ImportError:
        return {}
    return {
        ch: key[:-5] if key.endswith("_city") else key
        for ch, key in enumerate(CHAPTER_CITY_ORDER, start=1)
    }


_CHAPTER_TO_CITY_BUCKET: Dict[int, str] = _build_chapter_to_city_bucket()


# ── City info index (name + building display-name lookup per city) ─────────

def _build_city_info_index(const: Any) -> Dict[str, Dict[str, Any]]:
    """Return {bucket_key: {name, ch_num, cont_num, buildings: {name: display_name}}}.

    ``bucket_key`` matches the TASK_GROUPS extended keys and _CITY_METADATA keys,
    e.g. ``"forest_mid"``, ``"desert_large"``.

    City names and buildings are loaded from the const attributes that
    constants.py aggregates, e.g. FOREST_MID_CITY_CITY_NAME / FOREST_MID_CITY_BUILDINGS.
    """
    index: Dict[str, Dict[str, Any]] = {}
    for bucket_key, (ch_num, cont_num) in _CITY_METADATA.items():
        const_prefix    = f"{bucket_key.upper()}_CITY"
        city_name       = getattr(const, f"{const_prefix}_CITY_NAME", bucket_key.replace("_", " ").title())
        buildings_list  = getattr(const, f"{const_prefix}_BUILDINGS", []) or []
        buildings_by_name: Dict[str, str] = {
            b["name"]: b.get("display_name", b["name"])
            for b in buildings_list
            if isinstance(b, dict) and b.get("name")
        }
        index[bucket_key] = {
            "name":      city_name,
            "ch_num":    ch_num,
            "cont_num":  cont_num,
            "buildings": buildings_by_name,
        }
    return index


# ── Placement formatting helpers ──────────────────────────────────────────

def _resolve_city_bucket(group_key: str, bucket_key: str) -> Optional[str]:
    """Map a TASK_GROUPS group/bucket pair to a city bucket_key, or None."""
    if group_key == "extended":
        return bucket_key if bucket_key in _CITY_METADATA else None
    if group_key == "main":
        import re
        ch_match = re.match(r"^ch(\d+)$", bucket_key)
        if ch_match:
            return _CHAPTER_TO_CITY_BUCKET.get(int(ch_match.group(1)))
    return None


def _parse_building_from_location(
    location: str,
    city_info: Optional[Dict[str, Any]],
) -> str:
    """Extract a building hint string from a raw location param.

    Examples::

        "region_city_bar"         → "The Iron Maw (bar)"
        "region_city_shopweapons" → "Scrap & Spike (weapon shop)"
        "region_city_center"      → "city center"
        "region_city_open_area"   → "city open area"
        "region_open_area"        → "open area (wilderness)"
        "(no location)"           → "(unplaced)"
    """
    loc = location or ""
    if not loc or loc == "(no location)":
        return "(unplaced)"

    city_prefix = "region_city_"
    region_prefix = "region_"

    if loc.startswith(city_prefix):
        btype = loc[len(city_prefix):]
        if city_info:
            display = city_info["buildings"].get(btype)
            if display:
                type_label = _BUILDING_TYPE_LABELS.get(btype, btype)
                return f"{display} ({type_label})"
        # No building lookup available — humanize the type
        return btype.replace("_", " ")

    if loc.startswith(region_prefix):
        area = loc[len(region_prefix):].replace("_", " ")
        return f"{area} (wilderness)"

    return loc


def _format_placement_line(
    event_type: str,
    task_id: str,
    location: str,
    group_key: str,
    bucket_key: str,
    city_info_index: Dict[str, Dict[str, Any]],
) -> str:
    """Render one placement event as a single display line."""
    action       = _EVENT_ACTION_LABELS.get(event_type, event_type)
    city_bucket  = _resolve_city_bucket(group_key, bucket_key)
    city_info    = city_info_index.get(city_bucket) if city_bucket else None

    if city_info:
        city_part = (
            f"{city_info['name']} - "
            f"Ch.{city_info['ch_num']} - "
            f"Cont.{city_info['cont_num']}"
        )
    else:
        city_part = None

    if event_type == "hide_npc":
        return f"  {action} - {city_part + ' - ' if city_part else ''}{task_id}"

    building_hint = _parse_building_from_location(location, city_info)
    if city_part:
        return f"  {action} - {city_part} - {building_hint} - {task_id}"
    return f"  {action} - {building_hint} - {task_id}"


# ── Location index builder ────────────────────────────────────────────────

def _build_npc_location_index(
    const: Any,
) -> Dict[str, List[Tuple[str, str, str, str, str]]]:
    """Scan every task event in TASK_GROUPS for NPC placement events.

    Returns::

        {npc_id: [(event_type, task_id, location, group_key, bucket_key), ...]}
    """
    index: Dict[str, List[Tuple[str, str, str, str, str]]] = {}
    task_groups = getattr(const, "TASK_GROUPS", None) or {}

    for group_key, family in task_groups.items():
        if not isinstance(family, dict):
            continue
        for bucket_key, task_list in family.items():
            for task in task_list or []:
                if not isinstance(task, dict):
                    continue
                task_id = str(task.get("task_id", "?"))
                for stage_key in ("task_acquire_events", "task_complete_events"):
                    for ev in task.get(stage_key) or []:
                        if not isinstance(ev, dict):
                            continue
                        event_type = ev.get("event_type", "")
                        if event_type not in _PLACEMENT_EVENT_TYPES:
                            continue
                        params   = ev.get("params") or {}
                        npc_id   = str(params.get("npc_id") or params.get("id") or "")
                        if not npc_id:
                            continue
                        location = str(params.get("location") or "(no location)")
                        index.setdefault(npc_id, []).append(
                            (event_type, task_id, location, group_key, bucket_key)
                        )

    return index


# ── Builder ───────────────────────────────────────────────────────────────

def _make_npc_record(
    npc: Dict[str, Any],
    subtitle: str,
    source_group: str,
    location_index: Dict[str, List[Tuple[str, str, str, str, str]]],
    city_info_index: Dict[str, Dict[str, Any]],
) -> DevRecord:
    """Normalize a raw NPC seed dict into a DevRecord."""
    cid        = str(npc.get("npc_id", "?"))
    name       = str(npc.get("name", cid))
    desc       = str(npc.get("description", ""))
    theme_song = str(npc.get("theme_song", ""))
    image      = str(npc.get("image", ""))
    song_id    = str(npc.get("song_id", ""))

    psych  = npc.get("psychology") or {}
    ennea  = npc.get("enneagram") or {}
    shadow = npc.get("shadow_psychology") or {}

    group_label = _NPC_GROUP_LABELS.get(source_group, source_group.replace("_", " ").title())

    lines: List[str] = []
    if source_group:
        lines.append(f"Source: {group_label}")
        lines.append("")

    # ── Locations section ─────────────────────────────────────────────────
    placements = location_index.get(cid, [])
    lines.append("Locations:")
    if placements:
        for event_type, task_id, location, group_key, bucket_key in placements:
            lines.append(_format_placement_line(
                event_type, task_id, location,
                group_key, bucket_key, city_info_index,
            ))
    else:
        lines.append("  None")
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
        song_id=song_id,
    )

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
            continue
        matched_npcs = [
            npc for npc in group.npcs
            if q in npc.npc_id.lower()
            or q in npc.label.lower()
            or q in npc.record.detail.lower()
        ]
        if matched_npcs:
            result.append(NpcGroupNode(
                group_id=group.group_id,
                label=group.label,
                npcs=matched_npcs,
            ))
    return result

def _build_npc_tree(const: Any) -> List[NpcGroupNode]:
    """Build the group → NPC tree from ``const.NPC_GROUPS``.

    Priority order: regional_story → extended → main_story.
    Raises ValueError immediately if a duplicate npc_id is detected.
    Falls back to flat ``const.NPCS`` if NPC_GROUPS is absent.
    """
    location_index  = _build_npc_location_index(const)
    city_info_index = _build_city_info_index(const)

    npc_groups = getattr(const, "NPC_GROUPS", None)
    if not npc_groups:
        npcs = []
        for npc in getattr(const, "NPCS", []) or []:
            if not isinstance(npc, dict):
                continue
            cid    = str(npc.get("npc_id", "?"))
            record = _make_npc_record(npc, "NPC", "", location_index, city_info_index)
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
            record = _make_npc_record(npc, subtitle, group_key, location_index, city_info_index)
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