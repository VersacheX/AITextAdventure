"""
Flat DevRecord builders for all non-tree categories:
characters, items, special_items, equipment, dungeons, cities.
"""
from __future__ import annotations

from typing import Any, Dict, List, Tuple

from tui.services.dev.dataservices.models import DevRecord

_CITY_FIELDS: Tuple[str, ...] = ("CITY_NAME", "CITY_DESCRIPTION", "BUILDINGS")


def _build_characters(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []

    for npc in getattr(const, "PLAYER_NPCS", []) or []:
        cid      = str(npc.get("npc_id", "?"))
        name     = str(npc.get("name", cid))
        desc     = str(npc.get("description", ""))
        psych    = npc.get("psychology") or {}
        enneagram = npc.get("enneagram") or {}
        lines = [desc, ""]
        if psych:
            lines.append(f"MBTI: {psych.get('mbti', '?')}")
        if enneagram:
            lines.append(f"Enneagram: {enneagram.get('enneagram_type', '?')}")
            lines.append(f"Core fear: {enneagram.get('core_fear', '?')}")
            lines.append(f"Core desire: {enneagram.get('core_desire', '?')}")
        records.append(DevRecord(
            category="character", id=cid, name=name,
            subtitle=psych.get("mbti", ""),
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


def _build_items(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []
    for seed in getattr(const, "UTILITY_ITEM_SEEDS", []) or []:
        iid  = str(seed.get("id", "?"))
        name = str(seed.get("name", iid))
        records.append(DevRecord(
            category="item", id=iid, name=name,
            subtitle=f"value:{seed.get('value',0)}",
            detail=str(seed.get("description", "")),
        ))
    return records


def _build_special_items(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []
    for seed in getattr(const, "SPECIAL_ITEM_SEEDS", []) or []:
        iid  = str(seed.get("id", "?"))
        name = str(seed.get("name", iid))
        records.append(DevRecord(
            category="special_item", id=iid, name=name,
            subtitle="special",
            detail=str(seed.get("description", "")),
        ))
    return records


def _build_equipment(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []

    # WEAPON_SEEDS is a flat list; ARMOR_SEEDS is a dict keyed by slot.
    weapon_seeds = getattr(const, "WEAPON_SEEDS", []) or []
    if isinstance(weapon_seeds, list):
        for seed in weapon_seeds:
            iid  = str(seed.get("id", "?"))
            name = str(seed.get("name", iid))
            records.append(DevRecord(
                category="equipment", id=iid, name=name,
                subtitle="weapon",
                detail=str(seed.get("description", "")),
            ))
    elif isinstance(weapon_seeds, dict):
        for slot, seed_list in weapon_seeds.items():
            for seed in seed_list or []:
                iid  = str(seed.get("id", "?"))
                name = str(seed.get("name", iid))
                records.append(DevRecord(
                    category="equipment", id=iid, name=name,
                    subtitle=f"weapon · {slot}",
                    detail=str(seed.get("description", "")),
                ))

    armor_seeds = getattr(const, "ARMOR_SEEDS", {}) or {}
    if isinstance(armor_seeds, dict):
        for slot, seed_list in armor_seeds.items():
            for seed in seed_list or []:
                iid  = str(seed.get("id", "?"))
                name = str(seed.get("name", iid))
                records.append(DevRecord(
                    category="equipment", id=iid, name=name,
                    subtitle=f"armor · {slot}",
                    detail=str(seed.get("description", "")),
                ))
    elif isinstance(armor_seeds, list):
        for seed in armor_seeds:
            iid  = str(seed.get("id", "?"))
            name = str(seed.get("name", iid))
            records.append(DevRecord(
                category="equipment", id=iid, name=name,
                subtitle="armor",
                detail=str(seed.get("description", "")),
            ))

    return records


def _build_dungeons(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []
    for ds in getattr(const, "DUNGEON_SETTINGS", []) or []:
        did      = str(ds.get("id", "?"))
        name     = str(ds.get("display_name", did))
        hostiles = ds.get("hostile_seeds") or []
        boss     = ds.get("boss_hostiles") or []
        npcs     = ds.get("npcs") or []
        items    = ds.get("items") or []
        lines    = [str(ds.get("description", ""))]
        if hostiles:
            lines.append("")
            lines.append(f"Hostiles ({len(hostiles)}):")
            lines.extend(f"  - {h.get('name', h.get('id', '?'))}" for h in hostiles[:10] if isinstance(h, dict))
        if boss:
            lines.append("")
            lines.append("Boss:")
            lines.extend(f"  - {b.get('name', b.get('id', '?'))}" for b in boss if isinstance(b, dict))
        if npcs:
            lines.append("")
            lines.append(f"NPCs: {', '.join(str(n.get('id', '?')) for n in npcs if isinstance(n, dict))}")
        if items:
            lines.append(f"Items: {', '.join(str(i.get('id', '?')) for i in items if isinstance(i, dict))}")
        records.append(DevRecord(
            category="dungeon", id=did, name=name,
            subtitle=f"{len(hostiles)} hostiles · {len(boss)} boss",
            detail="\n".join(lines),
        ))
    return records


def _build_cities(const: Any) -> List[DevRecord]:
    """Build city DevRecords from CITY_DATA dict, falling back to the old
    per-attribute pattern when CITY_DATA is not present (e.g. older saves
    loaded without the updated constants).
    """
    records: List[DevRecord] = []

    city_data: Dict[str, Any] = getattr(const, "CITY_DATA", None) or {}

    if city_data:
        # ── fast path: use the pre-built dict ────────────────────────────────
        for city_id, entry in city_data.items():
            name        = str(entry.get("name") or city_id.replace("_", " ").title())
            description = str(entry.get("description") or "No description available.")
            buildings   = entry.get("buildings") or []
            # derive subtitle from city_id: "desert_large_city" → "Desert · Large City"
            parts       = city_id.split("_", 1)
            subtitle    = f"{parts[0].title()} · {parts[1].replace('_', ' ').title()}" if len(parts) == 2 else city_id
            lines       = [description]
            if buildings:
                lines.append("")
                lines.append(f"Buildings ({len(buildings)}):")
                lines.extend(
                    f"  - {b.get('display_name', b.get('name', '?'))} ({b.get('type', '?')})"
                    for b in buildings if isinstance(b, dict)
                )
            records.append(DevRecord(
                category="city", id=city_id, name=name,
                subtitle=subtitle,
                detail="\n".join(lines),
            ))
    else:
        # ── fallback: old getattr pattern ────────────────────────────────────
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
                    category="city", id=city_id, name=str(name),
                    subtitle=f"{region.title()} · {size.replace('_', ' ').title()}",
                    detail="\n".join(lines),
                ))

    return records