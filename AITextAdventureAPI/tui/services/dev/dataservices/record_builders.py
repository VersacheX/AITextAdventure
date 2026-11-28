"""
Flat DevRecord builders for all non-tree categories:
characters, items, special_items, equipment, dungeons, cities.
"""
from __future__ import annotations

from typing import Any, Dict, List, Tuple

from tui.services.dev.dataservices.models import DevRecord
from game.constants_other import ELEMENT_SYMBOLS as _ELEMENTAL_CHARS

_CITY_FIELDS: Tuple[str, ...] = ("CITY_NAME", "CITY_DESCRIPTION", "BUILDINGS")

_RARITY_LABELS: dict[str, str] = {
    "common":    "Common",
    "uncommon":  "Uncommon",
    "rare":      "Rare",
    "superrare": "Super Rare",
}

_RARITY_ABBR: dict[str, str] = {
    "common":    "Com",
    "uncommon":  "Unc",
    "rare":      "Rar",
    "superrare": "SR ",
}

_RARITY_RANK: dict[str, int] = {
    "common": 0, "uncommon": 1, "rare": 2, "superrare": 3,
}

_TYPE_ABBR: dict[str, str] = {
    "weapon":       "WPN ",
    "armor · head": "A-HD",
    "armor · body": "A-BD",
    "armor · arms": "A-AR",
    "armor · legs": "A-LG",
    "accessory":    "ACC ",
}


def _fmt_elements(elems: Any) -> str:
    if not elems:
        return ""
    if not isinstance(elems, (list, tuple)):
        elems = [elems]
    out = ""
    for e in elems:
        key = e.get("id") or e.get("name") if isinstance(e, dict) else str(e)
        out += _ELEMENTAL_CHARS.get(str(key).lower(), f"({key})")
    return out


def _total_stat_power(seed: dict) -> int:
    """Derived stat: sum of all bonus stat buffs on an equipment seed."""
    return sum(
        int(seed.get(s, 0) or 0)
        for s in ("strength", "dexterity", "intelligence", "constitution")
    )


def _equip_stats(seed: dict, type_label: str = "") -> dict:
    """Compute all display and sort stats from an equipment seed."""
    tsp      = _total_stat_power(seed)
    damage   = int(seed.get("damage") or 0)
    defense  = int(seed.get("defense") or 0)
    crit     = float(seed.get("critical_chance", 0) or 0)
    crit_pts = int(crit * 5)
    tep      = (damage + crit_pts) if damage else defense
    tp       = tsp + tep
    level    = int(seed.get("min_spawn_level", seed.get("min_level", 0)) or 0)
    rarity   = str(seed.get("rarity", "") or "").lower()
    return {
        "type_label":  type_label,
        "level":       level,
        "rarity":      rarity,
        "rarity_rank": _RARITY_RANK.get(rarity, -1),
        "damage":      damage,
        "defense":     defense,
        "crit":        crit,
        "tsp":         tsp,
        "tep":         tep,
        "tp":          tp,
        "elements":    _fmt_elements(seed.get("elements")),
    }

def _equip_subtitle(seed: dict, type_label: str) -> str:
    """Fixed-width subtitle so all columns align across list rows."""
    s     = _equip_stats(seed)
    abbr  = _TYPE_ABBR.get(type_label, (type_label[:4].upper() if type_label else "????"))
    rar   = _RARITY_ABBR.get(s["rarity"], s["rarity"][:3].title() if s["rarity"] else "---")
    elem  = s["elements"] if s["elements"] else "   "

    dmg_s = str(s["damage"])     if s["damage"]  else "---"
    def_s = str(s["defense"])    if s["defense"] else "---"
    crt_s = f"{s['crit']:.2f}"  if s["crit"]    else "-.--"
    tsp_s = str(s["tsp"])        if s["tsp"]     else "---"
    tep_s = str(s["tep"])        if s["tep"]     else "---"
    tp_s  = str(s["tp"])         if s["tp"]      else "---"

    return (
        f"{abbr:<4} "
        f"Lv:{s['level']:<3} "
        f"{rar:<3} "
        f"{elem:<9} "
        f"DMG:{dmg_s:<5} "
        f"DEF:{def_s:<5} "
        f"CRT:{crt_s:<5} "
        f"TSP:{tsp_s:<4} "
        f"TEP:{tep_s:<4} "
        f"TP:{tp_s:<4}"
    )

_SPECIAL_ITEM_SOURCE_EVENT_TYPES = frozenset({"dungeon_add_treasure", "award_item", "remove_item"})


def _build_special_item_source_index(
    const: Any,
) -> Dict[str, List[str]]:
    """Scan TASK_GROUPS for dungeon_add_treasure, award_item, and remove_item events.

    Returns {item_id: [formatted_line, ...]} where each line describes one
    source, e.g.:
      Award   - main_story_ch_1_deliver_ornate_bracers
      Dungeon - seth_hideout (final_chamber) - main_story_ch_1_find_item_shop
      Remove  - main_story_ch_2_deliver_cursed_couplet_to_mira
    """
    index: Dict[str, List[str]] = {}
    task_groups = getattr(const, "TASK_GROUPS", None) or {}

    for family in task_groups.values():
        if not isinstance(family, dict):
            continue
        for task_list in family.values():
            for task in task_list or []:
                if not isinstance(task, dict):
                    continue
                task_id = str(task.get("task_id", "?"))
                for stage_key in ("task_acquire_events", "task_complete_events"):
                    for ev in task.get(stage_key) or []:
                        if not isinstance(ev, dict):
                            continue
                        event_type = ev.get("event_type", "")
                        if event_type not in _SPECIAL_ITEM_SOURCE_EVENT_TYPES:
                            continue
                        params  = ev.get("params") or {}
                        item_id = str(
                            params.get("item_id") or params.get("id") or ""
                        )
                        if not item_id:
                            continue

                        if event_type == "award_item":
                            line = f"  Award   - {task_id}"
                        elif event_type == "remove_item":
                            line = f"  Remove  - {task_id}"
                        else:  # dungeon_add_treasure
                            dungeon_id    = str(params.get("dungeon_id") or "?")
                            location_type = str(params.get("location") or "?")
                            line = f"  Dungeon - {dungeon_id} ({location_type}) - {task_id}"

                        index.setdefault(item_id, []).append(line)

    return index


def _build_weapon_detail(seed: dict) -> str:
    lines: list[str] = []
    desc      = str(seed.get("description", "") or "")
    rarity    = str(seed.get("rarity", "") or "")
    level     = seed.get("min_spawn_level", seed.get("min_level", 0))
    dmg       = seed.get("damage", 0)
    dmg_type  = str(seed.get("damage_type", "physical") or "physical")
    crit      = seed.get("critical_chance", 0.0)
    ap_cost   = seed.get("ap_cost", 0)
    rng       = seed.get("range", 1)
    dur       = seed.get("durability", seed.get("max_durability", 0))
    max_dur   = seed.get("max_durability", dur)
    value     = seed.get("value", 0)
    elements  = seed.get("elements")
    strength  = int(seed.get("strength",     0) or 0)
    dexterity = int(seed.get("dexterity",    0) or 0)
    intel     = int(seed.get("intelligence", 0) or 0)
    con       = int(seed.get("constitution", 0) or 0)
    tsp       = strength + dexterity + intel + con

    rarity_label = _RARITY_LABELS.get(rarity.lower(), rarity)
    if desc:
        lines.append(desc)
        lines.append("")
    lines.append(f"Rarity          : {rarity_label}")
    lines.append(f"Req. Level      : {level}")
    lines.append("")
    lines.append(f"── Weapon  ·  {dmg_type} ──")
    lines.append(f"Damage          : {dmg}")
    if crit:
        lines.append(f"Crit Chance     : {float(crit):.1f}%")
    lines.append(f"AP Cost         : {ap_cost}")
    lines.append(f"Range           : {rng}")
    elem_s = _fmt_elements(elements)
    if elem_s:
        lines.append(f"Elements        : {elem_s}")
    lines.append("")
    lines.append(f"── Stat Bonuses  ·  TSP: {tsp} ──")
    for v, l in ((strength, "STR"), (dexterity, "DEX"), (intel, "INT"), (con, "CON")):
        if v:
            lines.append(f"  +{v:<4} {l}")
    if max_dur:
        lines.append("")
        lines.append(f"Durability      : {dur}/{max_dur}")
    if value:
        lines.append("")
        lines.append(f"Value           : {value}g  |  Sell: {int(int(value) * 0.5)}g")
    return "\n".join(lines)


def _build_armor_detail(seed: dict, slot: str) -> str:
    lines: list[str] = []
    desc      = str(seed.get("description", "") or "")
    rarity    = str(seed.get("rarity", "") or "")
    level     = seed.get("min_spawn_level", seed.get("min_level", 0))
    defense   = seed.get("defense", 0)
    dur       = seed.get("durability", seed.get("max_durability", 0))
    max_dur   = seed.get("max_durability", dur)
    value     = seed.get("value", 0)
    elements  = seed.get("elements")
    strength  = int(seed.get("strength",     0) or 0)
    dexterity = int(seed.get("dexterity",    0) or 0)
    intel     = int(seed.get("intelligence", 0) or 0)
    con       = int(seed.get("constitution", 0) or 0)
    tsp       = strength + dexterity + intel + con

    rarity_label = _RARITY_LABELS.get(rarity.lower(), rarity)
    if desc:
        lines.append(desc)
        lines.append("")
    lines.append(f"Rarity          : {rarity_label}")
    lines.append(f"Req. Level      : {level}")
    lines.append("")
    lines.append(f"── Armor  ·  {slot.capitalize()} ──")
    lines.append(f"Defense         : {defense}")
    elem_s = _fmt_elements(elements)
    if elem_s:
        lines.append(f"Elements        : {elem_s}")
    lines.append("")
    lines.append(f"── Stat Bonuses  ·  TSP: {tsp} ──")
    for v, l in ((strength, "STR"), (dexterity, "DEX"), (intel, "INT"), (con, "CON")):
        if v:
            lines.append(f"  +{v:<4} {l}")
    if max_dur:
        lines.append("")
        lines.append(f"Durability      : {dur}/{max_dur}")
    if value:
        lines.append("")
        lines.append(f"Value           : {value}g  |  Sell: {int(int(value) * 0.5)}g")
    return "\n".join(lines)


def _equip_subtitle(seed: dict, type_label: str) -> str:
    level        = seed.get("min_spawn_level", seed.get("min_level", 0)) or 0
    rarity       = str(seed.get("rarity", "") or "")
    rarity_label = _RARITY_LABELS.get(rarity.lower(), rarity)
    tsp          = _total_stat_power(seed)

    # Detect weapon vs armor by the presence of "damage" / "defense" keys
    damage  = seed.get("damage") or 0
    defense = seed.get("defense") or 0
    crit    = float(seed.get("critical_chance", 0) or 0)
    # TEP: damage/defense are direct; crit contributes decimal * 5
    crit_pts = int(crit * 5)
    if damage:
        tep = int(damage) + crit_pts
    elif defense:
        tep = int(defense)
    else:
        tep = 0
    tp = tsp + tep

    elements = _fmt_elements(seed.get("elements"))

    parts: list[str] = [type_label]
    if level:
        parts.append(f"Lv.{level}")
    if rarity_label:
        parts.append(rarity_label)
    if elements:
        parts.append(elements)
    if damage:
        parts.append(f"DMG:{damage}")
    if defense:
        parts.append(f"DEF:{defense}")
    if crit:
        parts.append(f"CRIT:{crit:.1f}")
    if tsp:
        parts.append(f"TSP:{tsp}")
    if tep:
        parts.append(f"TEP:{tep}")
    if tp:
        parts.append(f"TP:{tp}")
    return "  ·  ".join(parts)


# ── Ability sorting (mirrors tui.services.combat_renderer.ability_sort_key) ──
# Effect ordering: damage, heal, cure, revive, then status (beneficial
# statuses before detrimental ones). Within each bucket, sort by level.
_ABILITY_EFFECT_ORDER: dict[str, int] = {
    "damage": 0,
    "heal": 1,
    "cure": 2,
    "revive": 3,
    "status": 4,
}


def _ability_is_beneficial(seed: dict) -> bool:
    """Mirror PlayerAbility._is_beneficial_ability() for a raw seed dict."""
    import fnmatch
    from game.constants_other import BENEFICIAL_PLAYER_ABILITY_EFFECTS

    effect = str(seed.get("effect", "") or "").lower()
    if effect != "status":
        non_status_patterns = [
            p for p in BENEFICIAL_PLAYER_ABILITY_EFFECTS if str(p).lower() != "status"
        ]
        return any(fnmatch.fnmatch(effect, str(p).lower()) for p in non_status_patterns)
    keys = [str(k).lower() for k in (seed.get("status_keys") or [])]
    buff_patterns = [p for p in BENEFICIAL_PLAYER_ABILITY_EFFECTS if "_buff" in str(p)] + ["regen"]
    return bool(keys) and all(
        any(fnmatch.fnmatch(k, str(p).lower()) for p in buff_patterns) for k in keys
    )


def _ability_sort_key(seed: dict) -> Tuple[int, int, int, int]:
    """Sort key: ability level first (low to high), then ability type
    (technique/spirit/magic/tech/skill order), then effect bucket, then
    beneficial/harmful status ordering."""
    from tui.services.dev.dataservices.ability_service import _TYPE_ORDER

    level = int(seed.get("level", 1) or 1)
    atype = str(seed.get("ability_type", "") or "").lower()
    type_rank = _TYPE_ORDER.index(atype) if atype in _TYPE_ORDER else len(_TYPE_ORDER)
    effect = str(seed.get("effect", "") or "").lower()
    bucket = _ABILITY_EFFECT_ORDER.get(effect, len(_ABILITY_EFFECT_ORDER))
    status_rank = 0
    if effect == "status":
        status_rank = 0 if _ability_is_beneficial(seed) else 1
    return (level, type_rank, bucket, status_rank)


# ── Effect label colors ──────────────────────────────────────────────────────
# damage=red, heal=green, cure=teal, revive=white, status buff=vibrant
# magenta, status debuff=dim orange. Hex values used directly (Rich supports
# "#rrggbb" markup) so colors render consistently regardless of named-color
# availability/ambiguity across terminals.
_EFFECT_COLORS: dict[str, str] = {
    "damage": "#ff5252",
    "heal":   "#66bb6a",
    "cure":   "#26c6da",
    "revive": "#eeeeee",
}
_STATUS_BUFF_COLOR   = "#e040fb"
_STATUS_DEBUFF_COLOR = "#ff9e4d"


def _effect_color(seed: dict) -> str:
    """Resolve the hex color for an ability's effect label."""
    effect = str(seed.get("effect", "") or "").lower()
    if effect == "status":
        return _STATUS_BUFF_COLOR if _ability_is_beneficial(seed) else _STATUS_DEBUFF_COLOR
    return _EFFECT_COLORS.get(effect, "#ffffff")


# ── Per-level count breakdown ────────────────────────────────────────────────
_COUNT_BREAKDOWN_LABELS: dict[str, str] = {
    "damage":        "DMG",
    "heal":          "HL",
    "cure":          "CUR",
    "revive":        "REV",
    "status_buff":   "BUF",
    "status_debuff": "DEB",
}
_COUNT_BREAKDOWN_ORDER: tuple[str, ...] = (
    "damage", "heal", "cure", "revive", "status_buff", "status_debuff",
)


def _ability_effect_bucket(seed: dict) -> str:
    """Resolve the count-breakdown bucket key (splits status into buff/debuff)."""
    effect = str(seed.get("effect", "") or "").lower()
    if effect == "status":
        return "status_buff" if _ability_is_beneficial(seed) else "status_debuff"
    return effect


def _ability_count_breakdown(seeds: List[dict]) -> str:
    """Colored, space-separated count-by-effect-type summary (e.g. '5 DMG  2 BUF'),
    in fixed damage/heal/cure/revive/buff/debuff order, color-coded to match
    `_ability_line`'s effect-label colors. Empty buckets are omitted."""
    counts: dict[str, int] = {}
    for s in seeds:
        key = _ability_effect_bucket(s)
        counts[key] = counts.get(key, 0) + 1

    colors = {
        "damage": _EFFECT_COLORS["damage"],
        "heal": _EFFECT_COLORS["heal"],
        "cure": _EFFECT_COLORS["cure"],
        "revive": _EFFECT_COLORS["revive"],
        "status_buff": _STATUS_BUFF_COLOR,
        "status_debuff": _STATUS_DEBUFF_COLOR,
    }
    parts: list[str] = []
    for key in _COUNT_BREAKDOWN_ORDER:
        n = counts.get(key, 0)
        if not n:
            continue
        color = colors[key]
        label = _COUNT_BREAKDOWN_LABELS[key]
        parts.append(f"[{color}]{n} {label}[/{color}]")
    return "  ".join(parts)


def _build_ability_tier_lines(tier_label: str, seeds: List[dict]) -> List[str]:
    """Build the header + per-level sub-sections for one ability tier
    ('Signature', 'Learnable Now', 'Learnable Later'). Seeds must already be
    sorted by `_ability_sort_key` (level first). Each level sub-section gets
    its own count and a colored effect-type count breakdown."""
    from itertools import groupby

    lines: List[str] = [f"Abilities — {tier_label} ({len(seeds)}):"]
    for level, group in groupby(seeds, key=lambda s: int(s.get("level", 1) or 1)):
        group_seeds = list(group)
        breakdown = _ability_count_breakdown(group_seeds)
        header = f"  Level {level} ({len(group_seeds)}):"
        if breakdown:
            header = f"{header}  {breakdown}"
        lines.append(header)
        lines.extend(f"    {_ability_line(s)}" for s in group_seeds)
    return lines


def _build_ability_total_lines(all_tier_seeds: List[dict]) -> List[str]:
    """Build the 'Total Abilities' summary block from every seed across all
    tiers (Signature + Learnable Now + Learnable Later): a grand total, then
    a Lv.1–5 per-level total line, used right under Theme Song so pool size
    is visible without expanding the full ability breakdown."""
    if not all_tier_seeds:
        return []

    level_counts: dict[int, int] = {}
    for s in all_tier_seeds:
        level = int(s.get("level", 1) or 1)
        level_counts[level] = level_counts.get(level, 0) + 1

    lines: List[str] = [f"Total Abilities: {len(all_tier_seeds)}"]
    level_parts = [
        f"Lv.{lvl}: {level_counts[lvl]}"
        for lvl in sorted(level_counts.keys())
    ]
    lines.append("  " + "  ".join(level_parts))
    return lines


def _ability_line(seed: dict) -> str:
    """One-line summary for an ability seed, with the effect label wrapped
    in Rich markup colored by effect type (damage/heal/cure/revive/status
    buff/status debuff). Callers that render this through plain-text paths
    must NOT re-escape it — see `_render_character_detail`'s ability-section
    handling, which renders these lines unescaped.

    Elements and statuses are rendered via the canonical `fmt_element_glyphs`/
    `fmt_status_glyphs` helpers so wide-rendering glyphs (fire, ice, earth,
    continuous_damage, regen, …) get the same spacer compensation used
    everywhere else in the game (WIDE_SYMBOL_KEYS), instead of raw lookups
    that would visually collide with the next character.
    """
    from tui.services.dev.dataservices.ability_service import _TYPE_LABELS, _EFFECT_LABELS
    from game.constants_other import fmt_element_glyphs, fmt_status_glyphs

    name    = str(seed.get("name", seed.get("id", "?")))
    level   = int(seed.get("level", 1) or 1)
    atype   = str(seed.get("ability_type", "") or "")
    effect  = str(seed.get("effect", "") or "")
    ap_cost = seed.get("ap_cost", 0)
    elements = seed.get("elements") or []
    status_keys = seed.get("status_keys") or []
    elem_str = fmt_element_glyphs(elements) if elements else ""
    status_str = fmt_status_glyphs(status_keys) if status_keys else ""
    type_label   = _TYPE_LABELS.get(atype, atype.title())
    effect_label = _EFFECT_LABELS.get(effect, effect.title())
    color = _effect_color(seed)
    effect_markup = f"[{color}]{effect_label}[/{color}]"
    aoe = "  ◆AOE" if seed.get("can_aoe") else ""
    glyphs = elem_str
    if status_str:
        glyphs = f"{glyphs}  {status_str}" if glyphs else status_str
    return f"{name}  Lv.{level}  {type_label}  {effect_markup}  AP{ap_cost}  {glyphs}{aoe}"


def _build_character_ability_lines(
    cid: str,
    const: Any,
    hardcoded_ids: List[str] | None = None,
    stats: Dict[str, int] | None = None,
) -> Tuple[List[str], List[str]]:
    """Build the 'Abilities' detail block for any character id (core-five
    PLAYER_NPCS or ATTAINABLE_PLAYER_CHARACTERS alike).

    Hand-written/signature ability ids (if any) are listed first (sorted
    combat-style). Beneath them, every other ability this character could
    ever learn from the shared pool — filtered only by class + element
    (ignoring stat requirements, so the full tree is visible regardless of
    current level) — is listed in two tiers, both sorted combat-style:

      "Learnable Now"   — also passes the real stat requirements at the
                          character's current/starting stats.
      "Learnable Later" — class/element-eligible but needs higher stats
                          (i.e. more levels) than the character has now.

    `stats` lets callers supply known strength/dexterity/constitution/
    intelligence (e.g. from an ATTAINABLE_PLAYER_CHARACTERS entry); when
    omitted (core-five PLAYER_NPCS carry no stat block), the class's
    level-1 curve stats are used.

    Returns a ``(total_lines, ability_lines)`` tuple: ``total_lines`` is the
    short 'Total Abilities: N' + per-level breakdown summary (meant to sit
    right under Theme Song), and ``ability_lines`` is the full Signature/
    Learnable Now/Learnable Later breakdown.
    """
    from game.objects.player_ability import can_learn
    from game.region_seeds.player_abilities.ability_requirements import CLASS_LEVEL1_STATS

    all_seeds = getattr(const, "PLAYER_ABILITY_SEEDS", []) or []
    seed_map = {s.get("id"): s for s in all_seeds if isinstance(s, dict)}

    hardcoded_ids = list(hardcoded_ids or [])

    class _StubPlayer:
        pass

    stub = _StubPlayer()
    char_class = (getattr(const, "CHARACTER_NPC_CLASS_MAP", {}) or {}).get(cid)
    stub.character_class = char_class
    stub.npc_id = cid
    stub.id = cid
    stub.elements_base = list(
        (getattr(const, "CHARACTER_NPC_ELEMENT_MAP", {}) or {}).get(cid, []) or []
    )

    if stats:
        stub.strength = int(stats.get("strength", 0) or 0)
        stub.dexterity = int(stats.get("dexterity", 0) or 0)
        stub.constitution = int(stats.get("constitution", 0) or 0)
        stub.intelligence = int(stats.get("intelligence", 0) or 0)
    else:
        base = CLASS_LEVEL1_STATS.get(str(char_class or "").lower(), (8, 8, 8, 8))
        stub.strength, stub.dexterity, stub.constitution, stub.intelligence = base

    hardcoded_seeds = [seed_map[aid] for aid in hardcoded_ids if aid in seed_map]
    hardcoded_seeds.sort(key=_ability_sort_key)

    # Full class/element-eligible universe, ignoring stat requirements
    # entirely (check_stats=False) so the whole learnable tree is visible
    # regardless of the character's current level.
    universe_seeds = [
        s for s in all_seeds
        if isinstance(s, dict)
        and s.get("id") not in hardcoded_ids
        and not s.get("non_player_ability")
        and can_learn(stub, s, check_stats=False)
    ]

    now_seeds = [s for s in universe_seeds if can_learn(stub, s, check_stats=True)]
    now_ids = {s.get("id") for s in now_seeds}
    later_seeds = [s for s in universe_seeds if s.get("id") not in now_ids]

    now_seeds.sort(key=_ability_sort_key)
    later_seeds.sort(key=_ability_sort_key)

    lines: List[str] = []
    if hardcoded_seeds:
        lines.extend(_build_ability_tier_lines("Signature", hardcoded_seeds))
    if now_seeds:
        if lines:
            lines.append("")
        lines.extend(_build_ability_tier_lines("Learnable Now", now_seeds))
    if later_seeds:
        if lines:
            lines.append("")
        lines.extend(_build_ability_tier_lines("Learnable Later", later_seeds))

    total_lines = _build_ability_total_lines(hardcoded_seeds + now_seeds + later_seeds)
    return total_lines, lines


def _build_npc_profile_lines(npc: dict) -> list[str]:
    """Render the full character profile block from an NPC seed dict.

    Produces: description → MBTI + cognitive functions → Enneagram (all
    fields) → Shadow Psychology → Theme Song.  Returns a list of strings
    ready to be joined with newlines.
    """
    lines: list[str] = []

    desc = str(npc.get("description", "") or "")
    if desc:
        lines.append(desc)
        lines.append("")

    psych = npc.get("psychology") or {}
    if psych:
        lines.append(f"── Psychology ──────────────────────────────")
        lines.append(f"MBTI: {psych.get('mbti', '?')}")
        for key in ("dominant", "auxiliary", "tertiary", "inferior"):
            val = psych.get(key)
            if val:
                lines.append(f"  {key.capitalize()}: {val}")
        lines.append("")

    enneagram = npc.get("enneagram") or {}
    if enneagram:
        lines.append(f"── Enneagram ────────────────────────────────")
        lines.append(f"Enneagram: {enneagram.get('enneagram_type', '?')}")
        for key, label in (
            ("core_fear",           "Core Fear"),
            ("core_desire",         "Core Desire"),
            ("defense_mechanism",   "Defense"),
            ("stress_line",         "Stress"),
            ("growth_line",         "Growth"),
            ("instinctual_variant", "Instinct"),
        ):
            val = enneagram.get(key)
            if val:
                lines.append(f"  {label}: {val}")
        lines.append("")

    shadow = npc.get("shadow_psychology") or {}
    if shadow:
        lines.append(f"── Shadow Psychology ────────────────────────")
        lines.append(f"Shadow MBTI: {shadow.get('mbti', '?')}")
        for key in ("dominant", "auxiliary", "tertiary", "inferior"):
            val = shadow.get(key)
            if val:
                lines.append(f"  {key.capitalize()}: {val}")
        lines.append("")

    theme = str(npc.get("theme_song", "") or "")
    if theme:
        lines.append(f"Theme Song: {theme}")

    return lines


def _build_characters(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []

    # Build a lookup from npc_id → npc seed for all NPCS so attainable
    # player characters can resolve their profile data.
    npc_lookup: dict[str, dict] = {}
    for npc in getattr(const, "NPCS", []) or []:
        nid = str(npc.get("npc_id", ""))
        if nid:
            npc_lookup[nid] = npc

    class_map   = getattr(const, "CHARACTER_NPC_CLASS_MAP", {}) or {}
    element_map = getattr(const, "CHARACTER_NPC_ELEMENT_MAP", {}) or {}

    def _class_elements_suffix(cid: str) -> str:
        parts: list[str] = []
        cls = class_map.get(cid)
        if cls:
            parts.append(str(cls).title())
        elements = element_map.get(cid) or []
        if elements:
            parts.append("/".join(str(e).title() for e in elements))
        return " · ".join(parts)

    for npc in getattr(const, "PLAYER_NPCS", []) or []:
        cid   = str(npc.get("npc_id", "?"))
        name  = str(npc.get("name", cid))
        psych = npc.get("psychology") or {}
        lines = _build_npc_profile_lines(npc)
        total_lines, ability_lines = _build_character_ability_lines(cid, const)
        if total_lines:
            lines.extend(total_lines)
            lines.append("")
        if ability_lines:
            lines.extend(ability_lines)
        subtitle_parts = [p for p in (psych.get("mbti", ""), _class_elements_suffix(cid)) if p]
        records.append(DevRecord(
            category="character", id=cid, name=name,
            subtitle=" · ".join(subtitle_parts),
            detail="\n".join(lines),
            image=str(npc.get("image", "") or ""),
        ))

    for pc in getattr(const, "ATTAINABLE_PLAYER_CHARACTERS", []) or []:
        cid      = str(pc.get("id", "?"))
        name     = str(pc.get("name", cid))
        level    = pc.get("level", "?")

        # Profile block from the matching NPC seed (cross-referenced by id)
        npc_seed = npc_lookup.get(cid, {})
        psych    = npc_seed.get("psychology") or {}
        profile_lines = _build_npc_profile_lines(npc_seed) if npc_seed else []

        # Stat block
        stat_lines = [
            "── Stats ────────────────────────────────────",
            f"Level {level}",
            f"HP  {pc.get('current_hp', '?')}/{pc.get('max_hp', '?')}   "
            f"AP  {pc.get('current_ap', '?')}/{pc.get('max_ap', '?')}",
            f"STR {pc.get('strength', 0)}  DEX {pc.get('dexterity', 0)}  "
            f"INT {pc.get('intelligence', 0)}  CON {pc.get('constitution', 0)}",
            "",
            f"Weapon : {pc.get('equipped_weapon', 'None')}",
            f"Head   : {pc.get('head_armor', 'None')}",
            f"Body   : {pc.get('body_armor', 'None')}",
            f"Arms   : {pc.get('arm_armor', 'None')}",
            f"Legs   : {pc.get('leg_armor', 'None')}",
        ]
        total_lines, ability_lines = _build_character_ability_lines(
            cid,
            const,
            hardcoded_ids=pc.get("abilities") or [],
            stats={
                "strength": pc.get("strength", 0),
                "dexterity": pc.get("dexterity", 0),
                "constitution": pc.get("constitution", 0),
                "intelligence": pc.get("intelligence", 0),
            },
        )
        if total_lines:
            profile_lines.extend(total_lines)
        if ability_lines:
            stat_lines.append("")
            stat_lines.extend(ability_lines)

        all_lines = profile_lines + ([""] if profile_lines else []) + stat_lines

        subtitle_parts = [f"Unlockable · Lv.{level}"]
        if psych.get("mbti"):
            subtitle_parts.append(psych.get("mbti", ""))
        class_elements = _class_elements_suffix(cid)
        if class_elements:
            subtitle_parts.append(class_elements)

        records.append(DevRecord(
            category="character",
            id=cid,
            name=name,
            subtitle=" · ".join(subtitle_parts),
            detail="\n".join(all_lines),
            image=str(npc_seed.get("image", "") or ""),
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
    source_index = _build_special_item_source_index(const)
    records: List[DevRecord] = []

    for seed in getattr(const, "SPECIAL_ITEM_SEEDS", []) or []:
        iid  = str(seed.get("id", "?"))
        name = str(seed.get("name", iid))
        desc = str(seed.get("description", ""))

        sources = source_index.get(iid, [])
        if sources:
            source_block = "Sources:\n" + "\n".join(sources)
        else:
            source_block = "Sources:\n  [red]None[/red]"

        detail = f"{desc}\n\n{source_block}" if desc else source_block

        records.append(DevRecord(
            category="special_item",
            id=iid,
            name=name,
            subtitle="special",
            detail=detail,
        ))

    return records


def _build_equipment(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []

    weapon_seeds = getattr(const, "WEAPON_SEEDS", []) or []
    if isinstance(weapon_seeds, list):
        for seed in weapon_seeds:
            iid  = str(seed.get("id", "?"))
            name = str(seed.get("name", iid))
            stats = _equip_stats(seed, "weapon")
            records.append(DevRecord(
                category="equipment", id=iid, name=name,
                subtitle=_equip_subtitle(seed, "weapon"),
                detail=_build_weapon_detail(seed),
                extras=stats,
            ))
    elif isinstance(weapon_seeds, dict):
        for slot, seed_list in weapon_seeds.items():
            for seed in seed_list or []:
                iid  = str(seed.get("id", "?"))
                name = str(seed.get("name", iid))
                label = f"weapon · {slot}"
                stats = _equip_stats(seed, label)
                records.append(DevRecord(
                    category="equipment", id=iid, name=name,
                    subtitle=_equip_subtitle(seed, label),
                    detail=_build_weapon_detail(seed),
                    extras=stats,
                ))

    armor_seeds = getattr(const, "ARMOR_SEEDS", {}) or {}
    if isinstance(armor_seeds, dict):
        for slot, seed_list in armor_seeds.items():
            for seed in seed_list or []:
                iid  = str(seed.get("id", "?"))
                name = str(seed.get("name", iid))
                label = f"armor · {slot}"
                stats = _equip_stats(seed, label)
                records.append(DevRecord(
                    category="equipment", id=iid, name=name,
                    subtitle=_equip_subtitle(seed, label),
                    detail=_build_armor_detail(seed, slot),
                    extras=stats,
                ))
    elif isinstance(armor_seeds, list):
        for seed in armor_seeds:
            iid  = str(seed.get("id", "?"))
            name = str(seed.get("name", iid))
            slot = str(seed.get("slot", "armor"))
            label = f"armor · {slot}"
            stats = _equip_stats(seed, label)
            records.append(DevRecord(
                category="equipment", id=iid, name=name,
                subtitle=_equip_subtitle(seed, label),
                detail=_build_armor_detail(seed, slot),
                extras=stats,
            ))

    return records


def _build_dungeons(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []
    for ds in getattr(const, "DUNGEON_SETTINGS", []) or []:
        did      = str(ds.get("dungeon_id") or ds.get("id") or "?")
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
            extras={
                "open_area_tile":  ds.get("open_area_tile",  "."),
                "impassable_tile": ds.get("impassable_tile", "#"),
                "border_tile":     ds.get("border_tile",     "*"),
                "open_area_color": ds.get("open_area_color"),
                "impassable_color":ds.get("impassable_color"),
                "border_color":    ds.get("border_color"),
                "floors":          ds.get("floor_count", 1),
                "rooms":           ds.get("rooms_per_floor", "?"),
                "visible_distance":ds.get("visible_distance", 5),
            },
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

    # ── Region records from REGION_DATA ──────────────────────────────────────
    region_data: Dict[str, Any] = getattr(const, "REGION_DATA", None) or {}
    _REGION_SIZE_LABELS = {
        "region_hostile_seeds":     "Overworld",
        "large_city_hostile_seeds": "Large City",
        "mid_city_hostile_seeds":   "Mid City",
        "small_city_hostile_seeds": "Small City",
    }
    for region_name, entry in region_data.items():
        region_id = f"region_{region_name}"
        lines = [f"Region: {region_name.title()}"]
        lines.append("")
        total = 0
        for key, label in _REGION_SIZE_LABELS.items():
            seeds = entry.get(key) or []
            total += len(seeds)
            lines.append(f"{label} ({len(seeds)} hostiles):")
            if seeds:
                min_lv = min((s.get("min_spawn_level", 0) for s in seeds if isinstance(s, dict)), default=0)
                max_lv = max((s.get("min_spawn_level", 0) for s in seeds if isinstance(s, dict)), default=0)
                lines.append(f"  Lv range: {min_lv}–{max_lv}")
            else:
                lines.append("  (none)")
        records.append(DevRecord(
            category="city", id=region_id, name=region_name.title(),
            subtitle=f"Region · {total} total hostiles",
            detail="\n".join(lines),
            extras={"region_data": entry, "region_name": region_name},
        ))

    return records


def _build_accessories(const: Any) -> List[DevRecord]:
    """Build equipment DevRecords from ACCESSORY_SEEDS in constants_accesories."""
    records: List[DevRecord] = []
    try:
        from game.constants_accesories import ACCESSORY_SEEDS  # noqa: PLC0415
    except ImportError:
        return records

    for seed in ACCESSORY_SEEDS or []:
        iid    = str(seed.get('id', '?'))
        name   = str(seed.get('name', iid))
        rarity = str(seed.get('rarity', '') or '').lower()
        level  = int(seed.get('min_level', 0) or 0)
        str_   = int(seed.get('strength', 0) or 0)
        dex    = int(seed.get('dexterity', 0) or 0)
        intel  = int(seed.get('intelligence', 0) or 0)
        con    = int(seed.get('constitution', 0) or 0)
        tsp    = str_ + dex + intel + con
        crit   = float(seed.get('crit_bonus', 0.0) or 0.0)
        dmg    = int(seed.get('damage_bonus', 0) or 0)
        tep    = dmg + int(crit * 5)
        imm    = list(seed.get('immunities') or [])
        res    = list(seed.get('resistances') or [])
        wk     = list(seed.get('weaknesses') or [])
        tap    = len(imm) * 2 + len(res) * 1 + len(wk) * -1
        tp     = tsp + tep + tap
        special = str(seed.get('special_effect', '') or '')

        detail_lines = [str(seed.get('description', ''))]
        detail_lines.append("")
        if imm:
            detail_lines.append(f"Immunity:    {', '.join(imm)}")
        if res:
            detail_lines.append(f"Resistance:  {', '.join(res)}")
        if wk:
            detail_lines.append(f"Weakness:    {', '.join(wk)}")
        detail_lines.append("")
        detail_lines.append(f"── Stats  ·  TSP: {tsp} ──")
        for v, l in ((str_, "STR"), (dex, "DEX"), (intel, "INT"), (con, "CON")):
            if v:
                detail_lines.append(f"  +{v:<4} {l}")
        if dmg or crit:
            detail_lines.append("")
            detail_lines.append("── Combat Bonus ──")
            if dmg:
                detail_lines.append(f"  Damage Bonus : +{dmg}")
            if crit:
                detail_lines.append(f"  Crit Bonus   : +{crit:.1f}%")
        if special:
            detail_lines.append("")
            detail_lines.append(f"Special: {special}")
        if seed.get('value'):
            detail_lines.append(f"\nValue: {seed['value']}g  |  Sell: {int(seed['value'] * 0.5)}g")

        extras = {
            "type_label":  "accessory",
            "level":       level,
            "rarity":      rarity,
            "rarity_rank": _RARITY_RANK.get(rarity, -1),
            "damage":      dmg,
            "defense":     0,
            "crit":        crit,
            "tsp":         tsp,
            "tep":         tep,
            "tap":         tap,
            "tp":          tp,
            "elements":    "",
            "immunities":  imm,
            "resistances": res,
            "weaknesses":  wk,
        }

        records.append(DevRecord(
            category="equipment",
            id=iid,
            name=name,
            subtitle=_equip_subtitle_from_extras(extras),
            detail="\n".join(detail_lines),
            extras=extras,
        ))
    return records


def _equip_subtitle_from_extras(x: dict) -> str:
    """Build a fixed-width subtitle from a pre-computed extras dict."""
    rarity   = x.get("rarity", "")
    rar      = _RARITY_ABBR.get(rarity, rarity[:3].title() if rarity else "---")
    type_abbr = _TYPE_ABBR.get(x.get("type_label", ""), "ACC ")
    elem     = x.get("elements", "") or "   "
    dmg_s    = str(x["damage"])      if x.get("damage")  else "---"
    def_s    = str(x["defense"])     if x.get("defense") else "---"
    crt_s    = f"{x['crit']:.2f}"   if x.get("crit")    else "-.--"
    tsp_s    = str(x.get("tsp", 0))
    tep_s    = str(x.get("tep", 0))
    tp_s     = str(x.get("tp",  0))
    return (
        f"{type_abbr:<4} "
        f"Lv:{x.get('level', 0):<3} "
        f"{rar:<3} "
        f"{elem:<9} "
        f"DMG:{dmg_s:<5} "
        f"DEF:{def_s:<5} "
        f"CRT:{crt_s:<5} "
        f"TSP:{tsp_s:<4} "
        f"TEP:{tep_s:<4} "
        f"TP:{tp_s:<4}"
    )

_EFFECT_LABELS: dict[str, str] = {
    "damage": "Damage",
    "heal":   "Heal",
    "status": "Status",
    "revive": "Revive",
    "cure":   "Cure",
}

_ABILITY_TYPE_LABELS: dict[str, str] = {
    "technique": "Technique",
    "spirit":     "Spirit",
    "magic":     "Magic",
    "tech":      "Tech",
    "skill":     "Skill",
}


def _build_ability_detail(seed: dict) -> str:
    lines: list[str] = []
    desc      = str(seed.get("description", "") or "")
    atype     = str(seed.get("ability_type", "") or "")
    level     = seed.get("level", 1)
    elements  = seed.get("elements") or []
    base_power = seed.get("base_power", 0)
    ap_cost   = seed.get("ap_cost", 0)
    effect    = str(seed.get("effect", "") or "")
    status_keys = seed.get("status_keys") or []
    can_aoe   = seed.get("can_aoe", False)

    if desc:
        lines.append(desc)
        lines.append("")

    lines.append(f"Type     : {_ABILITY_TYPE_LABELS.get(atype, atype.title())}")
    lines.append(f"Level    : {level}")
    lines.append(f"Effect   : {_EFFECT_LABELS.get(effect, effect.title())}")
    lines.append(f"AP Cost  : {ap_cost}")
    if base_power:
        lines.append(f"Power    : {base_power}")
    if elements:
        elem_str = "  ".join(_ELEMENTAL_CHARS.get(str(e).lower(), f"({e})") for e in elements)
        lines.append(f"Elements : {elem_str}")
    if status_keys:
        lines.append(f"Statuses : {', '.join(status_keys)}")
    lines.append(f"AOE      : {'Yes' if can_aoe else 'No'}")
    return "\n".join(lines)


def _build_abilities(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []
    for seed in getattr(const, "PLAYER_ABILITY_SEEDS", []) or []:
        aid    = str(seed.get("id", "?"))
        name   = str(seed.get("name", aid))
        atype  = str(seed.get("ability_type", "") or "")
        level  = seed.get("level", 1)
        effect = str(seed.get("effect", "") or "")
        elements = seed.get("elements") or []
        elem_str = "".join(_ELEMENTAL_CHARS.get(str(e).lower(), "") for e in elements)
        subtitle = (
            f"Lv.{level}  "
            f"{_ABILITY_TYPE_LABELS.get(atype, atype.title()):<10}  "
            f"{_EFFECT_LABELS.get(effect, effect.title()):<8}  "
            f"{elem_str}"
        )
        records.append(DevRecord(
            category="ability",
            id=aid,
            name=name,
            subtitle=subtitle,
            detail=_build_ability_detail(seed),
            extras={
                "level":        int(level),
                "ability_type": atype,
                "effect":       effect,
                "ap_cost":      int(seed.get("ap_cost", 0) or 0),
                "base_power":   int(seed.get("base_power", 0) or 0),
            },
        ))
    return records


def _build_hostile_detail(seed: dict) -> str:
    lines: list[str] = []
    desc      = str(seed.get("description", "") or "")
    htype     = str(seed.get("hostile_type", "creature") or "creature")
    role      = str(seed.get("role", "") or "")
    level     = seed.get("min_spawn_level", 1)
    rarity    = str(seed.get("rarity", "common") or "common")
    base_xp   = seed.get("base_xp", 0)
    money     = seed.get("money_range")
    basic_atk = str(seed.get("basic_attack", "") or "")
    strong_atk = str(seed.get("strong_attack", "") or "")
    weaknesses  = seed.get("weaknesses") or []
    resistances = seed.get("resistances") or []
    immunities  = seed.get("immunities") or []
    common_drop = seed.get("common_drop") or ""
    rare_drop   = seed.get("rare_drop") or ""

    if desc:
        lines.append(desc)
        lines.append("")

    lines.append(f"Type     : {htype.title()}  ·  {role.title() if role else '—'}")
    lines.append(f"Min Lv.  : {level}")
    lines.append(f"Rarity   : {_RARITY_LABELS.get(rarity.lower(), rarity.title())}")
    lines.append(f"XP       : {base_xp}")
    if money:
        lines.append(f"Money    : {money[0]}–{money[1]}")
    lines.append("")
    if basic_atk:
        lines.append(f"Basic    : {basic_atk}")
    if strong_atk:
        lines.append(f"Strong   : {strong_atk}")
    if weaknesses or resistances or immunities:
        lines.append("")
        def _fmt_aff(lst: list) -> str:
            return "  ".join(_ELEMENTAL_CHARS.get(str(e).lower(), f"({e})") for e in lst) or "—"
        lines.append(f"Weak     : {_fmt_aff(weaknesses)}")
        lines.append(f"Resist   : {_fmt_aff(resistances)}")
        lines.append(f"Immune   : {_fmt_aff(immunities)}")
    if common_drop or rare_drop:
        lines.append("")
        lines.append(f"Drop (C) : {common_drop or '—'}")
        lines.append(f"Drop (R) : {rare_drop or '—'}")

    return "\n".join(lines)


def _build_hostiles(const: Any) -> List[DevRecord]:
    records: List[DevRecord] = []
    seen: set[str] = set()

    # Collect from every regional and dungeon hostile seed list
    all_seed_lists: list[Any] = []
    for attr in dir(const):
        if "HOSTILE_SEEDS" in attr or "BOSS_HOSTILES" in attr or "RANDOM_HOSTILE" in attr:
            val = getattr(const, attr, None)
            if isinstance(val, list):
                all_seed_lists.append(val)
    # Also pull WORLD_HOSTILES / WORLD_BOSS_MOBS if present
    for attr in ("WORLD_HOSTILES", "WORLD_BOSS_MOBS"):
        val = getattr(const, attr, None)
        if isinstance(val, list):
            all_seed_lists.append(val)

    for seed_list in all_seed_lists:
        for seed in seed_list:
            if not isinstance(seed, dict):
                continue
            hid = str(seed.get("id", ""))
            if not hid or hid in seen:
                continue
            seen.add(hid)
            name    = str(seed.get("name", hid))
            level   = int(seed.get("min_spawn_level", 1) or 1)
            rarity  = str(seed.get("rarity", "common") or "common")
            htype   = str(seed.get("hostile_type", "creature") or "creature")
            role    = str(seed.get("role", "") or "")
            rar_abbr = _RARITY_ABBR.get(rarity.lower(), rarity[:3].title())
            subtitle = f"Lv.{level:<3}  {rar_abbr}  {htype.title():<10}  {role.title() if role else ''}"
            records.append(DevRecord(
                category="hostile",
                id=hid,
                name=name,
                subtitle=subtitle,
                detail=_build_hostile_detail(seed),
                extras={
                    "level":  level,
                    "rarity": rarity,
                    "rarity_rank": _RARITY_RANK.get(rarity.lower(), -1),
                    "hostile_type": htype,
                },
            ))

    records.sort(key=lambda r: (r.extras.get("level", 0), r.name))
    return records