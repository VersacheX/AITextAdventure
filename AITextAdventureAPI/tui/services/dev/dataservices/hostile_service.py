"""
Hostile tree: builder, filter, and module-level cache.
get_hostile_tree() lives in catalog.py to avoid circular imports.

Tree shape:  Rarity → Level bucket (1-5, 6-10, …) → Hostile leaf
"""
from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict, List

from tui.services.dev.dataservices.models import (
    DevRecord,
    HostileLevelBucketNode,
    HostileNode,
    HostileRarityNode,
)

# ── Module-level tree cache (mutated by catalog._load_all) ────────────────
_HOSTILE_TREE: List[HostileRarityNode] = []

_RARITY_ORDER = ["common", "uncommon", "rare", "superrare", "notfound"]
_RARITY_LABELS: Dict[str, str] = {
    "common":    "Common",
    "uncommon":  "Uncommon",
    "rare":      "Rare",
    "superrare": "Super Rare",
    "notfound":  "Unknown Rarity",
}
_ELEMENT_CHARS: Dict[str, str] = {
    "dark": "(D)", "light": "(L)", "earth": "(Ë)", "fire": "(F)",
    "water": "(W)", "air": "(A)", "ice": "(I)", "electric": "(É)",
}
_BUCKET_SIZE = 5  # levels per bucket

# ── Location resolution helpers ───────────────────────────────────────────

_REGION_KEYWORDS = ["desert", "forest", "grassland", "mountains", "shallows", "snow", "swamp"]

# Static overrides for dungeon_ids whose city/region cannot be inferred
# purely from the dungeon_id string prefix.
# Maps dungeon_id (lowercase) → CITY_DATA key (e.g. "swamp_small_city")
_DUNGEON_CITY_OVERRIDES: Dict[str, str] = {
    "murkchannel_run":                "swamp_small_city",
    "rotfen_hideaway":                "swamp_small_city",
    "ghost_hideaway":                 "swamp_small_city",
    "charmroot_den":                  "forest_small_city",
    "windcarve_den":                  "mountains_small_city",
    "zaruuns_sanctum":                "desert_mid_city",
    "miregloom_resurrection_pit":     "swamp_large_city",
    "uulthars_tidal_maw":             "shallows_small_city",
    "marrowroots_deep_grove":         "forest_large_city",
    "serenes_wind_vault":             "grassland_large_city",
    "aeriolass_frozen_sanctum":       "snow_large_city",
    "rokhulls_fracture_core":         "mountains_mid_city",
    "relicmire_sump":                 "shallows_small_city",
    "fogwhisper_inlet":               "shallows_small_city",
    "coveveil_passage":               "shallows_mid_city",
    "stormhollow_voice_1":            "snow_small_city",
}

# ── Primary story lair dungeon_id fragments → region display label ────────
# These dungeons are region-specific but not tied to a single city.
# Checked as a fallback in _city_from_dungeon_id when no city prefix matches.
# Ordered longest-first so more specific fragments win over shorter ones.
_PS_LAIR_FRAGMENTS: list[tuple[str, str]] = [
    # desert
    ("zaruun_lair",          "Desert"),
    ("zaruun_sanctum",       "Desert"),
    # forest
    ("marrowroot_root",      "Forest"),
    ("marrowroot_lair",      "Forest"),
    # grassland
    ("serene_whispering",    "Grassland"),
    ("serene_lair",          "Grassland"),
    # mountains
    ("rokhuld_deep",         "Mountains"),
    ("rokhuld_lair",         "Mountains"),
    # shallows
    ("uulthar_abyssal",      "Shallows"),
    ("uulthar_lair",         "Shallows"),
    # snow
    ("aeriola_glacier",      "Snow"),
    ("aeriola_lair",         "Snow"),
    # swamp
    ("miregloom_rot",        "Swamp"),
    ("miregloom_lair",       "Swamp"),
]


def _city_from_dungeon_id(dungeon_id: str, city_data: Dict[str, Any]) -> str:
    """Return the city display name for a dungeon, or the region name as fallback."""
    did_lower = dungeon_id.lower()

    # 1. Static overrides (city dungeons)
    override_key = _DUNGEON_CITY_OVERRIDES.get(did_lower)
    if override_key and override_key in city_data:
        return city_data[override_key].get("name", override_key)

    # 2. Prefix match against CITY_DATA keys: "swamp_small_city" → prefix "swamp_small"
    best_len  = 0
    best_name = ""
    for city_key, city_info in city_data.items():
        parts = city_key.split("_")
        if len(parts) >= 3 and parts[-1] == "city":
            prefix = "_".join(parts[:-1])
            if did_lower.startswith(prefix) and len(prefix) > best_len:
                best_len  = len(prefix)
                best_name = city_info.get("name", city_key)
    if best_name:
        return best_name

    # 3. Region-only prefix fallback (open-world region hostiles)
    for region in _REGION_KEYWORDS:
        if did_lower.startswith(region):
            return region.title()

    # 4. Primary story lair fragments (region-bound, no specific city)
    for fragment, region_label in _PS_LAIR_FRAGMENTS:
        if fragment in did_lower:
            return region_label

    return "—"


def _resolve_hostile_location(
    source_attr: str,
    dungeon_display_map: Dict[str, str],
    city_data: Dict[str, Any],
    chapter_city_order: list,
) -> tuple[str, str]:
    """Return (location_dungeon, location_region) for a hostile source attribute."""

    # ── Dungeon node: "dungeon_id.hostile_seeds" or "dungeon_id.boss_hostiles" ──
    if "." in source_attr:
        dungeon_id   = source_attr.split(".")[0]
        dungeon_name = dungeon_display_map.get(
            dungeon_id,
            dungeon_id.replace("_", " ").title(),
        )
        region_label = _city_from_dungeon_id(dungeon_id, city_data)

        # Fallback: main story dungeon → look up chapter → CHAPTER_CITY_ORDER
        if region_label == "—":
            did_lower = dungeon_id.lower()
            chapter   = None
            for key, ch in _MAIN_STORY_DUNGEON_CHAPTER.items():
                if key in did_lower:
                    chapter = ch
                    break
            if chapter is not None and 1 <= chapter <= len(chapter_city_order):
                city_key  = chapter_city_order[chapter - 1]
                city_info = city_data.get(city_key, {})
                region_label = city_info.get("name", city_key.replace("_", " ").title())

        return (dungeon_name, region_label)

    # ── World hostiles ──────────────────────────────────────────────────────
    if source_attr == "WORLD_HOSTILES":
        return ("Overworld", "—")

    src_lower = source_attr.lower()

    # ── City random hostile seeds ────────────────────────────────────────────
    for city_key, city_info in city_data.items():
        parts = city_key.split("_")
        if len(parts) >= 3 and parts[-1] == "city":
            pattern = city_key + "_random_hostile"
            if pattern in src_lower:
                return ("Overworld", city_info.get("name", city_key))

    # ── Region random hostile seeds ──────────────────────────────────────────
    for region in _REGION_KEYWORDS:
        if src_lower.startswith(region + "_random"):
            return ("Overworld", region.title())

    return ("Overworld", source_attr)


def _level_bucket_id(level: int) -> str:
    lo = ((level - 1) // _BUCKET_SIZE) * _BUCKET_SIZE + 1
    hi = lo + _BUCKET_SIZE - 1
    return f"lv_{lo:02d}_{hi:02d}"


def _level_bucket_label(level: int) -> str:
    lo = ((level - 1) // _BUCKET_SIZE) * _BUCKET_SIZE + 1
    hi = lo + _BUCKET_SIZE - 1
    return f"Lv {lo}–{hi}"


def _level_bucket_range(level: int):
    lo = ((level - 1) // _BUCKET_SIZE) * _BUCKET_SIZE + 1
    hi = lo + _BUCKET_SIZE - 1
    return lo, hi


def _hostile_detail(seed: dict) -> str:
    lines: list[str] = []
    desc       = str(seed.get("description", "") or "")
    htype      = str(seed.get("hostile_type", "creature") or "creature")
    role       = str(seed.get("role", "") or "")
    level      = seed.get("min_spawn_level", 1)
    rarity     = str(seed.get("rarity", "common") or "common")
    base_xp    = seed.get("base_xp", 0)
    money      = seed.get("money_range")
    basic_atk  = str(seed.get("basic_attack", "") or "")
    strong_atk = str(seed.get("strong_attack", "") or "")
    abilities  = seed.get("player_abilities") or []
    weaknesses  = seed.get("weaknesses") or []
    resistances = seed.get("resistances") or []
    immunities  = seed.get("immunities") or []
    common_drop = seed.get("common_drop") or ""
    rare_drop   = seed.get("rare_drop") or ""

    base_str = seed.get("base_str", 0)
    base_dex = seed.get("base_dex", 0)
    base_con = seed.get("base_con", 0)
    base_int = seed.get("base_int", 0)
    base_hp  = seed.get("base_hp", 0)
    base_ap  = seed.get("base_ap", 0)
    str_pl   = seed.get("str_per_level", 0)
    dex_pl   = seed.get("dex_per_level", 0)
    con_pl   = seed.get("con_per_level", 0)
    int_pl   = seed.get("int_per_level", 0)

    if desc:
        lines.append(desc)
        lines.append("")

    lines.append(f"Type      : {htype.title()}  ·  {role.title() if role else '—'}")
    lines.append(f"Min Lv.   : {level}")
    lines.append(f"Rarity    : {_RARITY_LABELS.get(rarity.lower(), rarity.title())}")
    lines.append(f"XP        : {base_xp}")
    if money:
        lines.append(f"Money     : {money[0]}–{money[1]}")
    lines.append("")
    lines.append("── Base Stats ──")
    lines.append(f"STR {base_str}  DEX {base_dex}  CON {base_con}  INT {base_int}")
    lines.append(f"HP  {base_hp}  AP  {base_ap}")
    lines.append(f"+/lv  STR {str_pl:.2f}  DEX {dex_pl:.2f}  CON {con_pl:.2f}  INT {int_pl:.2f}")
    if basic_atk:
        lines.append("")
        lines.append(f"Basic     : {basic_atk}")
    if strong_atk:
        lines.append(f"Strong    : {strong_atk}")
    if abilities:
        lines.append("")
        lines.append(f"Abilities : {', '.join(str(a) for a in abilities)}")

    def _fmt_aff(lst: list) -> str:
        return "  ".join(_ELEMENT_CHARS.get(str(e).lower(), f"({e})") for e in lst) or "—"

    if weaknesses or resistances or immunities:
        lines.append("")
        lines.append(f"Weak      : {_fmt_aff(weaknesses)}")
        lines.append(f"Resist    : {_fmt_aff(resistances)}")
        lines.append(f"Immune    : {_fmt_aff(immunities)}")

    if common_drop or rare_drop:
        lines.append("")
        lines.append(f"Drop (C)  : {common_drop or '—'}")
        lines.append(f"Drop (R)  : {rare_drop or '—'}")

    return "\n".join(lines)


def _hostile_subtitle(seed: dict) -> str:
    level   = int(seed.get("min_spawn_level", 1) or 1)
    rarity  = str(seed.get("rarity", "common") or "common")
    htype   = str(seed.get("hostile_type", "creature") or "creature")
    role    = str(seed.get("role", "") or "")
    rar_abbr = {"common": "Com", "uncommon": "Unc", "rare": "Rar",
                "superrare": "SR ", "notfound": "?  "}.get(rarity.lower(), rarity[:3].title())
    return f"Lv.{level:<3}  {rar_abbr}  {htype.title():<12}  {role.title() if role else ''}"


def _build_hostile_tree(const: Any) -> None:
    """Rebuild _HOSTILE_TREE from all hostile seed lists on const."""
    global _HOSTILE_TREE
    _HOSTILE_TREE.clear()

    seen: set[str] = set()

    # ── Build dungeon display-name lookup ─────────────────────────────────
    dungeon_display_map: Dict[str, str] = {}
    dungeon_settings_list = getattr(const, "DUNGEON_SETTINGS", None)
    if isinstance(dungeon_settings_list, list):
        for ds in dungeon_settings_list:
            if not isinstance(ds, dict):
                continue
            did = str(ds.get("dungeon_id", "") or "")
            if did:
                dungeon_display_map[did] = str(
                    ds.get("display_name", did.replace("_", " ").title()) or did
                )

    city_data: Dict[str, Any] = getattr(const, "CITY_DATA", {}) or {}

    # ── Collect every list attribute that looks like hostile seeds ────────
    all_seeds: List[tuple[str, dict]] = []  # (source_attr_name, seed)
    for attr in dir(const):
        upper = attr.upper()
        if "HOSTILE_SEEDS" in upper or "BOSS_HOSTILES" in upper or (
            "RANDOM_HOSTILE" in upper and not attr.startswith("_")
        ):
            val = getattr(const, attr, None)
            if isinstance(val, list):
                for s in val:
                    if isinstance(s, dict):
                        all_seeds.append((attr, s))

    # Also pull WORLD_HOSTILES only — WORLD_BOSS_MOBS are mob group
    # definitions (id + hostiles list), not hostile seed dicts, and must
    # not be loaded into the hostile tree.
    for attr in ("WORLD_HOSTILES",):
        val = getattr(const, attr, None)
        if isinstance(val, list):
            for s in val:
                if isinstance(s, dict):
                    all_seeds.append((attr, s))

    # Pull hostile_seeds and boss_hostiles from every DUNGEON_SETTINGS entry
    if isinstance(dungeon_settings_list, list):
        for ds in dungeon_settings_list:
            if not isinstance(ds, dict):
                continue
            dungeon_id = ds.get("dungeon_id") or ds.get("display_name") or "unknown_dungeon"
            for key in ("hostile_seeds", "boss_hostiles"):
                for s in (ds.get(key) or []):
                    if isinstance(s, dict):
                        all_seeds.append((f"{dungeon_id}.{key}", s))

    # ── Group by (rarity, level_bucket) ──────────────────────────────────
    by_rarity_bucket: Dict[str, Dict[str, List[HostileNode]]] = {
        r: defaultdict(list) for r in _RARITY_ORDER
    }
    
    chapter_city_order: list = getattr(const, "CHAPTER_CITY_ORDER", []) or []
    for source_attr, seed in all_seeds:
        hid = str(seed.get("id", ""))
        if not hid or hid in seen:
            continue
        seen.add(hid)

        name    = str(seed.get("name", hid))
        level   = int(seed.get("min_spawn_level", 1) or 1)
        rarity  = str(seed.get("rarity", "common") or "common").lower()
        if rarity not in _RARITY_ORDER:
            rarity = "notfound"
        
        loc_dungeon, loc_region = _resolve_hostile_location(
            source_attr, dungeon_display_map, city_data, chapter_city_order
        )

        record = DevRecord(
            category="hostile",
            id=hid,
            name=name,
            subtitle=_hostile_subtitle(seed),
            detail=_hostile_detail(seed),
            extras={
                "level":        level,
                "rarity":       rarity,
                "hostile_type": str(seed.get("hostile_type", "") or ""),
                "role":         str(seed.get("role", "") or ""),
                "_seed":        seed,
            },
        )
        node = HostileNode(
            hostile_id=hid,
            label=name,
            rarity=rarity,
            level=level,
            source_list=source_attr,
            record=record,
            seed=seed,
            location_dungeon=loc_dungeon,
            location_region=loc_region,
        )
        bucket_id = _level_bucket_id(level)
        by_rarity_bucket[rarity][bucket_id].append(node)

    for rarity_id in _RARITY_ORDER:
        bucket_map = by_rarity_bucket[rarity_id]
        if not bucket_map:
            continue

        level_buckets: List[HostileLevelBucketNode] = []
        for bucket_id in sorted(bucket_map.keys()):
            nodes = sorted(bucket_map[bucket_id], key=lambda n: (n.level, n.label))
            lo, hi = _level_bucket_range(nodes[0].level)
            level_buckets.append(HostileLevelBucketNode(
                bucket_id=bucket_id,
                label=_level_bucket_label(nodes[0].level),
                level_min=lo,
                level_max=hi,
                hostiles=nodes,
            ))

        _HOSTILE_TREE.append(HostileRarityNode(
            rarity_id=rarity_id,
            label=_RARITY_LABELS.get(rarity_id, rarity_id.title()),
            level_buckets=level_buckets,
        ))


def filter_hostile_tree(
    tree: List[HostileRarityNode],
    query: str = "",
) -> List[HostileRarityNode]:
    """Return a pruned copy of *tree* matching *query* (case-insensitive)."""
    if not query:
        return tree
    q = query.strip().lower()
    result: List[HostileRarityNode] = []
    for rarity_node in tree:
        rarity_matches = q in rarity_node.label.lower() or q in rarity_node.rarity_id.lower()
        filtered_buckets: List[HostileLevelBucketNode] = []
        for bucket_node in rarity_node.level_buckets:
            bucket_matches = q in bucket_node.label.lower()
            if rarity_matches or bucket_matches:
                filtered_buckets.append(bucket_node)
            else:
                matched_hostiles = [
                    n for n in bucket_node.hostiles
                    if q in n.label.lower()
                    or q in n.hostile_id.lower()
                    or q in n.rarity.lower()
                    or q in n.location_dungeon.lower()
                    or q in n.location_region.lower()
                ]
                if matched_hostiles:
                    filtered_buckets.append(HostileLevelBucketNode(
                        bucket_id=bucket_node.bucket_id,
                        label=bucket_node.label,
                        level_min=bucket_node.level_min,
                        level_max=bucket_node.level_max,
                        hostiles=matched_hostiles,
                    ))
        if filtered_buckets:
            result.append(HostileRarityNode(
                rarity_id=rarity_node.rarity_id,
                label=rarity_node.label,
                level_buckets=filtered_buckets,
            ))
    return result


def flat_hostile_nodes(tree: List[HostileRarityNode]) -> List[HostileNode]:
    """Return every HostileNode from *tree* in rarity → bucket → hostile order."""
    out: List[HostileNode] = []
    for rarity_node in tree:
        for bucket in rarity_node.level_buckets:
            out.extend(bucket.hostiles)
    return out


def get_hostile_tree_module() -> List[HostileRarityNode]:
    return _HOSTILE_TREE

# Maps main-story dungeon_id (lowercase) → chapter number (1-based).
# Used to resolve the city the dungeon appears in via CHAPTER_CITY_ORDER.
_MAIN_STORY_DUNGEON_CHAPTER: Dict[str, int] = {
    "seth_hideout":                 1,
    "abandoned_ruin_ch2":           2,
    "nobles_mansion":               3,
    "seth_hideout_ch3":             3,
    "rift_dungeon":                 4,
    "stormglass_alley":             5,
    "tempest_bunker":               6,
    "riftland_breach":              7,
    "rift_dungeon_outskirts":       7,
    "theatre_of_echoed_faces":      8,
    "theatre_echoed_faces":         8,
    "bloodspark_arena":             9,
    "festival_of_delight":          11,
    "nihilist_camp":                11,
    "grand_mausoleum":              13,
    "edicts_prison":                15,
    "velvet_veil":                  15,
    "the_citadel":                  15,
    "origin_spire":                 16,
    "temporal_echoes":              16,
    "mountain_ruin":                17,
    "punishment_engines":           17,
    "collapsing_spire":             18,
    "rotwood":                      19,
    "seraphine_glade":              19,
    "memory_museum":                20,
    "trial_1":                      21,
    "trial_2":                      21,
    "trial_3":                      21,
    "trial_4":                      21,
    "trial_5":                      21,
}