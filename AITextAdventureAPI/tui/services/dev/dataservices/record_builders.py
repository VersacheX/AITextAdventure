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


def _build_items(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []
    for seed in getattr(const, "UTILITY_ITEM_SEEDS", []) or []:
        rid    = str(seed.get("id", "?"))
        name   = str(seed.get("name", rid))
        rarity = str(seed.get("rarity", "?"))
        lvl    = seed.get("min_spawn_level", "?")
        lines = [
            str(seed.get("description", "")), "",
            f"Effect: {seed.get('effect', '?')}",
            f"Value: {seed.get('value', 0)}   Uses: {seed.get('uses', 1)}",
            f"Rarity: {rarity}   Min level: {lvl}",
        ]
        records.append(DevRecord(
            category="item", id=rid, name=name,
            subtitle=f"{rarity} · Lv.{lvl}", detail="\n".join(lines),
        ))
    return records


def _build_special_items(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []
    for seed in getattr(const, "SPECIAL_ITEM_SEEDS", []) or []:
        rid    = str(seed.get("id", "?"))
        name   = str(seed.get("name", rid))
        rarity = str(seed.get("rarity", "?"))
        lines  = [str(seed.get("description", ""))]
        effect_desc = seed.get("effect_description")
        if effect_desc:
            lines.append("")
            lines.append(f"Effect: {effect_desc}")
        records.append(DevRecord(
            category="special_item", id=rid, name=name,
            subtitle=rarity, detail="\n".join(lines),
        ))
    return records


def _build_equipment(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []
    for seed in getattr(const, "WEAPON_SEEDS", []) or []:
        rid    = str(seed.get("id", "?"))
        name   = str(seed.get("name", rid))
        rarity = str(seed.get("rarity", "?"))
        lvl    = seed.get("min_spawn_level", "?")
        lines = [
            str(seed.get("description", "")), "",
            f"Damage: {seed.get('damage', 0)} ({seed.get('damage_type', '?')})   "
            f"Crit: {seed.get('critical_chance', 0)}%",
            f"STR {seed.get('strength', 0)}  DEX {seed.get('dexterity', 0)}  "
            f"INT {seed.get('intelligence', 0)}",
            f"Value: {seed.get('value', 0)}   Rarity: {rarity}   Min level: {lvl}",
        ]
        records.append(DevRecord(
            category="equipment", id=rid, name=name,
            subtitle=f"Weapon · {rarity} · Lv.{lvl}", detail="\n".join(lines),
        ))
    armor_seeds = getattr(const, "ARMOR_SEEDS", {}) or {}
    for slot, seeds in armor_seeds.items():
        for seed in seeds or []:
            rid    = str(seed.get("id", "?"))
            name   = str(seed.get("name", rid))
            rarity = str(seed.get("rarity", "?"))
            lvl    = seed.get("min_spawn_level", "?")
            lines = [
                str(seed.get("description", "")), "",
                f"Defense: {seed.get('defense', 0)}   Slot: {slot}",
                f"STR {seed.get('strength', 0)}  DEX {seed.get('dexterity', 0)}  "
                f"INT {seed.get('intelligence', 0)}  CON {seed.get('constitution', 0)}",
                f"Value: {seed.get('value', 0)}   Rarity: {rarity}   Min level: {lvl}",
            ]
            records.append(DevRecord(
                category="equipment", id=rid, name=name,
                subtitle=f"Armor ({slot}) · {rarity} · Lv.{lvl}", detail="\n".join(lines),
            ))
    return records


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
            lines.extend(f"  - {h.get('name', h.get('id', '?'))}" for h in hostiles if isinstance(h, dict))
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
                category="city", id=city_id, name=str(name),
                subtitle=f"{region.title()} · {size.replace('_', ' ').title()}",
                detail="\n".join(lines),
            ))
    return records