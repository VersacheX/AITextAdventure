"""
Hostile integrity validator.

Structural rules
----------------
H1  HOSTILE_UNKNOWN_RARITY         rarity not in recognised set
H2  HOSTILE_MISSING_ATTACKS        basic_attack is empty or absent
H3  HOSTILE_MISSING_BASE_STATS     base_hp or base_ap is 0 / absent
H4  HOSTILE_ABILITY_MISMATCH       ability count below expected minimum for rarity
                                   (common=0, uncommon≥1, rare≥2, superrare≥3)
H4b HOSTILE_UNKNOWN_ABILITY      player_abilities references an id that is not
                                   registered in PLAYER_ABILITY_SEEDS
H5  HOSTILE_MISSING_TYPE           hostile_type is empty or absent
H6  HOSTILE_DROP_UNKNOWN_ITEM      common_drop or rare_drop references an item
                                   id that is not registered in the game's
                                   known item constants

Balance rules  (warning, rarity-aware)
--------------------------------------
Groups are (rarity, level) — same rarity, same exact level. Never mixed.
B1  HOSTILE_BALANCE_WEAK           combat_score < 65% of peer average
B2  HOSTILE_BALANCE_STRONG         combat_score > 145% of peer average
B3  HOSTILE_RARITY_SCORE_LOW       combat_score below the expected floor for the
                                   rarity at this level (higher rarity should be
                                   strictly stronger than lower at the same level).
    Floor = group_avg(rarity-1) * 0.90 where group_avg is computed across all
    same-level nodes of the next-lower rarity.

Combat score formula (mirrors hostile_seed_engine.py)
------------------------------------------------------
    derived_hp  = base_hp + con * 2 + level * hp_per_level
    derived_dps = max(1, str*0.5 + dex*0.3 + level*0.2)
    defense     = con * 0.5
    ap_pool     = base_ap + level * ap_per_level
    ability_pot = sum(base_power * (1 + 0.2*(ability_lv-1))) for each ability
    score = (0.01*hp + 1.0*dps + 0.8*defense + 0.8*ap_pool + 1.5*ability_pot)
          * (1 + level*0.05)

Stat pools (from hostile_seed_engine.py RARITY_STAT_POOLS)
------------------------------------------------------------
    common:    start=5,  per_level=5.5, pp=8
    uncommon:  start=6,  per_level=6,   pp=10
    rare:      start=7,  per_level=6.5, pp=15
    superrare: start=8,  per_level=7,   pp=20
    notfound:  start=15, per_level=10,  pp=25
"""
from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict, List, Set

from tui.services.dev.dataservices.models import (
    HostileNode,
    HostileRarityNode,
    HostileValidationError,
)

# ── Constants mirrored from hostile_seed_engine.py ────────────────────────

_RARITY_STAT_POOLS: Dict[str, Dict[str, float]] = {
    "common":    {"start": 5,  "per_level": 5.5, "pp": 8},
    "uncommon":  {"start": 6,  "per_level": 6.0, "pp": 10},
    "rare":      {"start": 7,  "per_level": 6.5, "pp": 15},
    "superrare": {"start": 8,  "per_level": 7.0, "pp": 20},
    "notfound":  {"start": 15, "per_level": 10.0, "pp": 25},
}

_RARITY_ABILITY_COUNTS: Dict[str, int] = {
    "common":    0,
    "uncommon":  1,
    "rare":      2,
    "superrare": 3,
    "notfound":  4,
}

_RARITY_ORDER = ["common", "uncommon", "rare", "superrare"]

_KNOWN_RARITIES = set(_RARITY_STAT_POOLS.keys())

_W_HP  = 0.01
_W_DPS = 1.0
_W_DEF = 0.8
_W_AP  = 0.8
_W_AB  = 1.5


def _err(code: str, message: str, severity: str = "error") -> HostileValidationError:
    return HostileValidationError(code=code, message=message, severity=severity)


def _build_known_item_ids(const: Any) -> Set[str]:
    """Collect every valid item id from the game constants."""
    ids: Set[str] = set()
    for attr in (
        "SEED_UTILITY_IDS",
        "SEED_SPECIAL_IDS",
        "SEED_WEAPON_IDS",
        "SEED_ACCESSORY_IDS",
    ):
        val = getattr(const, attr, None)
        if isinstance(val, list):
            ids.update(str(i) for i in val if i)
    armor_ids = getattr(const, "SEED_ARMOR_IDS", None)
    if isinstance(armor_ids, dict):
        for slot_list in armor_ids.values():
            if isinstance(slot_list, list):
                ids.update(str(i) for i in slot_list if i)
    return ids


def _estimate_combat_score(seed: dict, ability_index: Dict[str, dict]) -> float:
    """Estimate combat score for *seed* without mutating it.

    Mirrors the derivation in hostile_seed_engine.estimate_stats_from_seed +
    compute_combat_score, but avoids all the print() calls and side-effects
    in that function.
    """
    rarity = str(seed.get("rarity", "common") or "common").lower()
    pool   = _RARITY_STAT_POOLS.get(rarity, _RARITY_STAT_POOLS["common"])
    level  = int(seed.get("min_spawn_level", 1) or 1)

    start    = pool["start"]
    per_lv   = pool["per_level"]
    pp       = pool["pp"]

    # Per-stat scaling ratios (seed provides relative weights via per_level fields)
    str_pl = float(seed.get("str_per_level", 0) or 0) + 1.0
    dex_pl = float(seed.get("dex_per_level", 0) or 0) + 1.0
    con_pl = float(seed.get("con_per_level", 0) or 0) + 1.0
    int_pl = float(seed.get("int_per_level", 0) or 0) + 1.0
    total_pl = str_pl + dex_pl + con_pl + int_pl or 1.0

    str_pl = (str_pl / total_pl) * per_lv
    dex_pl = (dex_pl / total_pl) * per_lv
    con_pl = (con_pl / total_pl) * per_lv

    strength     = start + str_pl * level
    dexterity    = start + dex_pl * level
    constitution = start + con_pl * level

    abil_count  = max(len(seed.get("player_abilities") or []),
                      _RARITY_ABILITY_COUNTS.get(rarity, 0))
    hp_dist     = 1.0 - abil_count * 0.05
    hp_per_lv   = pp * hp_dist
    ap_per_lv   = pp * (1.0 - hp_dist)

    base_hp = seed.get("base_hp") or (pool["start"] * 2 + int(hp_per_lv * level))
    base_ap = seed.get("base_ap") or (pool["start"] * 2 + int(ap_per_lv * level))

    hp      = float(base_hp) + constitution * 2.0 + level * hp_per_lv
    ap_pool = float(base_ap) + level * ap_per_lv
    dps     = max(1.0, strength * 0.5 + dexterity * 0.3 + level * 0.2)
    defense = constitution * 0.5

    # Ability potential
    ab_pot = 0.0
    abilities = seed.get("player_abilities") or []
    if isinstance(abilities, list):
        for aid in abilities:
            a = ability_index.get(str(aid))
            if a:
                lv = int(a.get("level", 1) or 1)
                bp = float(a.get("base_power", 10) or 10)
                ab_pot += bp * (1.0 + 0.2 * (lv - 1))

    raw         = _W_HP * hp + _W_DPS * dps + _W_DEF * defense + _W_AP * ap_pool + _W_AB * ab_pot
    level_scale = 1.0 + level * 0.05
    return raw * level_scale


def _flat_nodes(tree: List[HostileRarityNode]) -> List[HostileNode]:
    out: List[HostileNode] = []
    for rarity_node in tree:
        for bucket in rarity_node.level_buckets:
            out.extend(bucket.hostiles)
    return out


def validate_hostile_tree(
    tree: List[HostileRarityNode],
    const: Any,
) -> Dict[str, int]:
    """Validate every HostileNode in *tree*, annotating .errors in-place.

    Returns summary dict::
        {"hostiles_scanned": int, "invalid": int, "total_errors": int,
         "by_code": {code: count}}
    """
    all_nodes = _flat_nodes(tree)
    for node in all_nodes:
        node.errors.clear()

    by_code: Dict[str, int] = defaultdict(int)

    # Build ability lookup for score estimation
    ability_index: Dict[str, dict] = {}
    for a in getattr(const, "PLAYER_ABILITY_SEEDS", []) or []:
        if isinstance(a, dict) and a.get("id"):
            ability_index[str(a["id"])] = a

    # Build known item id set for H6
    known_item_ids = _build_known_item_ids(const)

    # ── Pre-compute combat scores ─────────────────────────────────────────
    scores: Dict[str, float] = {}
    for node in all_nodes:
        scores[node.hostile_id] = _estimate_combat_score(node.seed, ability_index)

    # ── Build balance groups: (rarity, level) → [score] ─────────────────
    # Groups are STRICTLY same-rarity and same-level — pure peers only.
    score_by_group: Dict[tuple, List[float]] = defaultdict(list)
    node_group:     Dict[str, tuple]         = {}

    for rarity_node in tree:
        for bucket in rarity_node.level_buckets:
            for node in bucket.hostiles:
                level = int(node.seed.get("min_spawn_level", 1) or 1)
                gkey  = (rarity_node.rarity_id, level)
                score_by_group[gkey].append(scores[node.hostile_id])
                node_group[node.hostile_id] = gkey

    group_avg: Dict[tuple, float] = {
        k: sum(v) / len(v)
        for k, v in score_by_group.items()
        if len(v) > 1
    }

    # ── Build cross-rarity floor: for each level, the avg of the rarity below ──
    # Used for B3: a rare's score should be ≥ 90% of the uncommon avg at the same level.
    rarity_bucket_avg: Dict[tuple, float] = dict(group_avg)  # (rarity, level) → avg

    # ── Per-node structural checks ────────────────────────────────────────
    for node in all_nodes:
        seed   = node.seed
        rarity = node.rarity

        # H1
        if rarity not in _KNOWN_RARITIES:
            node.errors.append(_err(
                "HOSTILE_UNKNOWN_RARITY",
                f"Rarity '{rarity}' is not a recognised value.",
            ))
            by_code["HOSTILE_UNKNOWN_RARITY"] += 1

        # H2
        if not str(seed.get("basic_attack", "") or "").strip():
            node.errors.append(_err(
                "HOSTILE_MISSING_ATTACKS",
                "basic_attack is empty or absent.",
            ))
            by_code["HOSTILE_MISSING_ATTACKS"] += 1

        # H3
        base_hp = int(seed.get("base_hp", 0) or 0)
        base_ap = int(seed.get("base_ap", 0) or 0)
        if base_hp == 0:
            node.errors.append(_err(
                "HOSTILE_MISSING_BASE_STATS",
                "base_hp is 0 or absent — hostile will have no health pool.",
            ))
            by_code["HOSTILE_MISSING_BASE_STATS"] += 1
        if base_ap == 0:
            node.errors.append(_err(
                "HOSTILE_MISSING_BASE_STATS",
                "base_ap is 0 or absent — hostile cannot use abilities.",
                severity="warning",
            ))
            by_code["HOSTILE_MISSING_BASE_STATS"] += 1

        # H4 — ability count check (rarity sets a minimum, not a maximum)
        expected_min = _RARITY_ABILITY_COUNTS.get(rarity, 0)
        abilities    = seed.get("player_abilities") or []
        actual_count = len([a for a in abilities if a]) if isinstance(abilities, list) else 0
        if expected_min > 0 and actual_count < expected_min:
            node.errors.append(_err(
                "HOSTILE_ABILITY_MISMATCH",
                f"Rarity '{rarity}' expects at least {expected_min} ability(s); "
                f"has {actual_count}.",
                severity="notice",
            ))
            by_code["HOSTILE_ABILITY_MISMATCH"] += 1

        # H4b — unknown ability id cross-reference
        if isinstance(abilities, list):
            for aid in abilities:
                if not aid:
                    continue
                if str(aid) not in ability_index:
                    node.errors.append(_err(
                        "HOSTILE_UNKNOWN_ABILITY",
                        f"player_abilities references '{aid}' which is not registered "
                        "in PLAYER_ABILITY_SEEDS.",
                    ))
                    by_code["HOSTILE_UNKNOWN_ABILITY"] += 1

        # H5
        if not str(seed.get("hostile_type", "") or "").strip():
            node.errors.append(_err(
                "HOSTILE_MISSING_TYPE",
                "hostile_type is empty or absent.",
                severity="warning",
            ))
            by_code["HOSTILE_MISSING_TYPE"] += 1

        # H6 — drop item cross-reference
        for drop_field in ("common_drop", "rare_drop"):
            drop_val = seed.get(drop_field)
            if not drop_val:
                continue
            drop_id = str(drop_val)
            if drop_id not in known_item_ids:
                node.errors.append(_err(
                    "HOSTILE_DROP_UNKNOWN_ITEM",
                    f"{drop_field} '{drop_id}' is not registered in any item "
                    "constant (SEED_UTILITY_IDS, SEED_SPECIAL_IDS, "
                    "SEED_WEAPON_IDS, SEED_ARMOR_IDS, SEED_ACCESSORY_IDS).",
                ))
                by_code["HOSTILE_DROP_UNKNOWN_ITEM"] += 1

        # ── Balance checks ────────────────────────────────────────────────
        score = scores[node.hostile_id]
        gkey  = node_group.get(node.hostile_id)

        # B1 / B2 — within same rarity + level
        if gkey and gkey in group_avg:
            avg   = group_avg[gkey]
            ratio = score / avg if avg else 1.0
            level_val = gkey[1]
            if ratio < 0.65:
                node.errors.append(_err(
                    "HOSTILE_BALANCE_WEAK",
                    f"Combat score {score:.1f} is only {ratio:.0%} of the "
                    f"{_rarity_label(gkey[0])} Lv {level_val} "
                    f"peer average {avg:.1f}.",
                    severity="info",
                ))
                by_code["HOSTILE_BALANCE_WEAK"] += 1
            elif ratio > 1.45:
                node.errors.append(_err(
                    "HOSTILE_BALANCE_STRONG",
                    f"Combat score {score:.1f} is {ratio:.0%} of the "
                    f"{_rarity_label(gkey[0])} Lv {level_val} "
                    f"peer average {avg:.1f}.",
                    severity="notice",
                ))
                by_code["HOSTILE_BALANCE_STRONG"] += 1

        # B3 — rarity floor: this rarity's score vs the avg of the rarity below
        rarity_idx = _RARITY_ORDER.index(rarity) if rarity in _RARITY_ORDER else -1
        if rarity_idx > 0 and gkey:
            lower_rarity = _RARITY_ORDER[rarity_idx - 1]
            lower_gkey   = (lower_rarity, gkey[1])
            lower_avg    = rarity_bucket_avg.get(lower_gkey)
            if lower_avg is not None:
                floor = lower_avg * 0.90
                if score < floor:
                    node.errors.append(_err(
                        "HOSTILE_RARITY_SCORE_LOW",
                        f"{_rarity_label(rarity)} hostile score {score:.1f} is below "
                        f"90% of the {_rarity_label(lower_rarity)} average "
                        f"{lower_avg:.1f} at Lv {gkey[1]}. "
                        f"Higher rarity should generally be stronger.",
                        severity="warning",
                    ))
                    by_code["HOSTILE_RARITY_SCORE_LOW"] += 1

    invalid      = sum(1 for n in all_nodes if n.errors)
    total_errors = sum(len(n.errors) for n in all_nodes)

    return {
        "hostiles_scanned": len(all_nodes),
        "invalid":          invalid,
        "total_errors":     total_errors,
        "by_code":          dict(by_code),
    }


def _rarity_label(rarity_id: str) -> str:
    return {
        "common": "Common", "uncommon": "Uncommon",
        "rare": "Rare", "superrare": "Super Rare",
    }.get(rarity_id, rarity_id.title())


def _bucket_label(bucket_id: str) -> str:
    # bucket_id e.g. "lv_01_05" → "Lv 1–5"
    parts = bucket_id.replace("lv_", "").split("_")
    if len(parts) == 2:
        return f"Lv {int(parts[0])}–{int(parts[1])}"
    return bucket_id