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

    # Collect every list attribute that looks like hostile seeds
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

    # Also pull WORLD_HOSTILES / WORLD_BOSS_MOBS
    for attr in ("WORLD_HOSTILES", "WORLD_BOSS_MOBS"):
        val = getattr(const, attr, None)
        if isinstance(val, list):
            for s in val:
                if isinstance(s, dict):
                    all_seeds.append((attr, s))

    # Group by (rarity, level_bucket)
    # rarity → bucket_id → [HostileNode]
    by_rarity_bucket: Dict[str, Dict[str, List[HostileNode]]] = {
        r: defaultdict(list) for r in _RARITY_ORDER
    }

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
                hostiles = [
                    h for h in bucket_node.hostiles
                    if q in h.hostile_id.lower()
                    or q in h.label.lower()
                    or q in h.record.detail.lower()
                    or q in h.source_list.lower()
                ]
                if hostiles:
                    filtered_buckets.append(HostileLevelBucketNode(
                        bucket_id=bucket_node.bucket_id,
                        label=bucket_node.label,
                        level_min=bucket_node.level_min,
                        level_max=bucket_node.level_max,
                        hostiles=hostiles,
                    ))
        if filtered_buckets:
            result.append(HostileRarityNode(
                rarity_id=rarity_node.rarity_id,
                label=rarity_node.label,
                level_buckets=filtered_buckets,
            ))
    return result