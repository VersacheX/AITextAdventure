"""
Dungeon integrity validator.

Structural rules
----------------
D1  DUNGEON_MISSING_DISPLAY_NAME     display_name is absent or empty
D2  DUNGEON_MISSING_HOSTILE_SEEDS    hostile_seeds is empty (notice — some
                                     dungeons are NPC-only arenas with no
                                     random encounters)
D3  DUNGEON_FLOOR_HOSTILE_UNDEFINED  floor_hostiles references an id not
                                     present in hostile_seeds
D4  DUNGEON_BOSS_MOB_HOSTILE_MISSING boss_mob.hostiles contains an id not
                                     present in boss_hostiles
D5  DUNGEON_BOSS_HOSTILES_ORPHANED   boss_hostiles is non-empty but boss_mob
                                     is None / missing the 'hostiles' list
D6  DUNGEON_ITEM_UNDEFINED           an item in the 'items' list has an id
                                     that is not registered in the game's
                                     known item constants (error)
D7  DUNGEON_RARITY_COVERAGE          a dungeon floor does not have at least
                                     one hostile of each rarity: common,
                                     uncommon, rare, superrare (notice)
D8  DUNGEON_MISSING_ITEMS            items list is empty (notice)
D9  DUNGEON_NPC_NO_LOCATION          an NPC in the 'npcs' list has location
                                     set to None (notice)
"""
from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict, List, Set

from tui.services.dev.dataservices.models import DungeonNode, DungeonValidationError

_EXPECTED_RARITIES = {"common", "uncommon", "rare", "superrare"}


def _err(
    code: str,
    message: str,
    severity: str = "error",
) -> DungeonValidationError:
    return DungeonValidationError(code=code, message=message, severity=severity)


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

    # SEED_ARMOR_IDS is a dict of slot → [id, ...]
    armor_ids = getattr(const, "SEED_ARMOR_IDS", None)
    if isinstance(armor_ids, dict):
        for slot_list in armor_ids.values():
            if isinstance(slot_list, list):
                ids.update(str(i) for i in slot_list if i)

    return ids


def validate_dungeon_tree(
    tree: List["DungeonGroupNode"],  # type: ignore[name-defined]
    const: Any,
) -> Dict[str, int]:
    """Validate every DungeonNode in *tree*, annotating .errors in-place.

    Returns summary dict::
        {"dungeons_scanned": int, "invalid": int, "total_errors": int,
         "by_code": {code: count}}
    """
    known_item_ids = _build_known_item_ids(const)
    by_code: Dict[str, int] = defaultdict(int)

    all_nodes: List[DungeonNode] = [
        d for group in tree for d in group.dungeons
    ]
    for node in all_nodes:
        node.errors.clear()

    for node in all_nodes:
        ds = node.settings

        # ── D1 DUNGEON_MISSING_DISPLAY_NAME ──────────────────────────────
        if not str(ds.get("display_name", "") or "").strip():
            node.errors.append(_err(
                "DUNGEON_MISSING_DISPLAY_NAME",
                "display_name is absent or empty.",
            ))
            by_code["DUNGEON_MISSING_DISPLAY_NAME"] += 1

        # ── Build lookup sets ─────────────────────────────────────────────
        hostile_seeds: List[dict] = ds.get("hostile_seeds") or []
        boss_hostiles: List[dict] = ds.get("boss_hostiles") or []
        hostile_seed_ids: Set[str] = {
            str(h.get("id", "")) for h in hostile_seeds if isinstance(h, dict)
        }
        boss_hostile_ids: Set[str] = {
            str(b.get("id", "")) for b in boss_hostiles if isinstance(b, dict)
        }
        hostile_rarity_by_id: Dict[str, str] = {
            str(h.get("id", "")): str(h.get("rarity", "")).lower()
            for h in hostile_seeds if isinstance(h, dict)
        }

        # ── D2 DUNGEON_MISSING_HOSTILE_SEEDS ─────────────────────────────
        if not hostile_seed_ids:
            node.errors.append(_err(
                "DUNGEON_MISSING_HOSTILE_SEEDS",
                "hostile_seeds is empty — no random encounters will spawn.",
                severity="notice",
            ))
            by_code["DUNGEON_MISSING_HOSTILE_SEEDS"] += 1

        # ── D3 DUNGEON_FLOOR_HOSTILE_UNDEFINED ───────────────────────────
        floor_hostiles: Dict[int, List[str]] = ds.get("floor_hostiles") or {}
        for floor_num, floor_ids in floor_hostiles.items():
            if not isinstance(floor_ids, list):
                continue
            for hid in floor_ids:
                if str(hid) not in hostile_seed_ids:
                    node.errors.append(_err(
                        "DUNGEON_FLOOR_HOSTILE_UNDEFINED",
                        f"Floor {floor_num} references hostile '{hid}' "
                        f"which is not defined in hostile_seeds.",
                    ))
                    by_code["DUNGEON_FLOOR_HOSTILE_UNDEFINED"] += 1

        # ── D4 DUNGEON_BOSS_MOB_HOSTILE_MISSING ──────────────────────────
        boss_mob: Any = ds.get("boss_mob")
        if boss_mob and isinstance(boss_mob, dict):
            mob_hostile_refs: List[str] = boss_mob.get("hostiles") or []
            for ref in mob_hostile_refs:
                if str(ref) not in boss_hostile_ids:
                    node.errors.append(_err(
                        "DUNGEON_BOSS_MOB_HOSTILE_MISSING",
                        f"boss_mob.hostiles references '{ref}' "
                        f"which is not defined in boss_hostiles.",
                        severity="warning",
                    ))
                    by_code["DUNGEON_BOSS_MOB_HOSTILE_MISSING"] += 1

        # ── D5 DUNGEON_BOSS_HOSTILES_ORPHANED ────────────────────────────
        if boss_hostiles and not boss_mob:
            node.errors.append(_err(
                "DUNGEON_BOSS_HOSTILES_ORPHANED",
                f"{len(boss_hostiles)} boss_hostile(s) defined but boss_mob is "
                "None or absent — the boss will never be triggered.",
                severity="warning",
            ))
            by_code["DUNGEON_BOSS_HOSTILES_ORPHANED"] += 1

        # ── D6 DUNGEON_ITEM_UNDEFINED ─────────────────────────────────────
        items: List[dict] = ds.get("items") or []
        for item in items:
            if not isinstance(item, dict):
                continue
            iid = str(item.get("id", "") or "")
            if iid and iid not in known_item_ids:
                node.errors.append(_err(
                    "DUNGEON_ITEM_UNDEFINED",
                    f"Item '{iid}' is not registered in any item constant "
                    "(SEED_UTILITY_IDS, SEED_SPECIAL_IDS, SEED_WEAPON_IDS, SEED_ARMOR_IDS).",
                ))
                by_code["DUNGEON_ITEM_UNDEFINED"] += 1

        # ── D7 DUNGEON_RARITY_COVERAGE ────────────────────────────────────
        if hostile_seed_ids and floor_hostiles:
            for floor_num, floor_ids in floor_hostiles.items():
                if not isinstance(floor_ids, list):
                    continue
                present_rarities = {
                    hostile_rarity_by_id.get(str(hid), "")
                    for hid in floor_ids
                    if str(hid) in hostile_rarity_by_id
                }
                missing = _EXPECTED_RARITIES - present_rarities
                if missing:
                    node.errors.append(_err(
                        "DUNGEON_RARITY_COVERAGE",
                        f"Floor {floor_num} is missing rarity coverage: "
                        f"{', '.join(sorted(missing))}. "
                        "Each floor should have at least one common, uncommon, "
                        "rare, and superrare hostile.",
                        severity="notice",
                    ))
                    by_code["DUNGEON_RARITY_COVERAGE"] += 1

        # ── D8 DUNGEON_MISSING_ITEMS ──────────────────────────────────────
        if not items:
            node.errors.append(_err(
                "DUNGEON_MISSING_ITEMS",
                "items list is empty — the dungeon has no loot.",
                severity="notice",
            ))
            by_code["DUNGEON_MISSING_ITEMS"] += 1

        # ── D9 DUNGEON_NPC_NO_LOCATION ────────────────────────────────────
        npcs: List[dict] = ds.get("npcs") or []
        for npc in npcs:
            if not isinstance(npc, dict):
                continue
            if npc.get("location") is None:
                nid = str(npc.get("id", "?"))
                node.errors.append(_err(
                    "DUNGEON_NPC_NO_LOCATION",
                    f"NPC '{nid}' has location=None — it will not be placed "
                    "unless a create_npc event sets a location at runtime.",
                    severity="notice",
                ))
                by_code["DUNGEON_NPC_NO_LOCATION"] += 1

    invalid      = sum(1 for n in all_nodes if n.errors)
    total_errors = sum(len(n.errors) for n in all_nodes)

    return {
        "dungeons_scanned": len(all_nodes),
        "invalid":          invalid,
        "total_errors":     total_errors,
        "by_code":          dict(by_code),
    }