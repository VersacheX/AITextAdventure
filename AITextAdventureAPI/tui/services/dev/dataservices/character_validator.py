"""Character equipment integrity validator.

Rules
-----
C1  CHARACTER_EQUIP_UNKNOWN_WEAPON
    equipped_weapon references an item id that is not registered in any weapon
    seed list (WEAPON_SEEDS).

C2  CHARACTER_EQUIP_UNKNOWN_ARMOR
    arm_armor, head_armor, body_armor, or leg_armor references an item id that
    is not registered in any armor seed list (ARMOR_SEEDS).

C3  CHARACTER_EQUIP_UNKNOWN_ACCESSORY
    equipped_accessory references an item id that is not registered in
    ACCESSORY_SEEDS.  (Slot is optional — only checked when present.)

C4  CHARACTER_UNKNOWN_ABILITY
    An ability id in the abilities list is not registered in PLAYER_ABILITY_SEEDS.

C5  CHARACTER_SHORT_DESCRIPTION  (warning)
    The NPC seed's description field is shorter than the minimum acceptable
    length, benchmarked against Lyren Vale's reference description.
"""
from __future__ import annotations

from types import SimpleNamespace
from typing import Any, Dict, List, Set

from tui.services.dev.dataservices.models import DevRecord


_ARMOR_SLOTS: tuple[str, ...] = ("arm_armor", "head_armor", "body_armor", "leg_armor")

# Minimum acceptable description length, benchmarked against Lyren Vale's reference.
_MIN_DESCRIPTION_LENGTH: int = len(
    "A gentle wayfarer attuned to the emotional undercurrents of the world. "
    "Lyren feels the Riftwaters long before she sees them."
    "The way light bends, the way people's hearts tighten. "
    "She speaks softly, moves quietly, and heals instinctively, "
    "as if guided by something older than memory."
)


def _err(code: str, message: str) -> Any:
    return SimpleNamespace(code=code, message=message, severity="error")


def _warn(code: str, message: str) -> Any:
    return SimpleNamespace(code=code, message=message, severity="warning")


def _build_weapon_ids(const: Any) -> Set[str]:
    ids: Set[str] = set()
    seeds = getattr(const, "WEAPON_SEEDS", None) or []
    if isinstance(seeds, list):
        for s in seeds:
            iid = str(s.get("id", "") or "").strip()
            if iid:
                ids.add(iid)
    elif isinstance(seeds, dict):
        for seed_list in seeds.values():
            for s in (seed_list or []):
                iid = str(s.get("id", "") or "").strip()
                if iid:
                    ids.add(iid)
    return ids


def _build_armor_ids(const: Any) -> Set[str]:
    ids: Set[str] = set()
    seeds = getattr(const, "ARMOR_SEEDS", None) or {}
    if isinstance(seeds, dict):
        for seed_list in seeds.values():
            for s in (seed_list or []):
                iid = str(s.get("id", "") or "").strip()
                if iid:
                    ids.add(iid)
    elif isinstance(seeds, list):
        for s in seeds:
            iid = str(s.get("id", "") or "").strip()
            if iid:
                ids.add(iid)
    return ids


def _build_accessory_ids(const: Any) -> Set[str]:
    ids: Set[str] = set()
    for s in (getattr(const, "ACCESSORY_SEEDS", None) or []):
        iid = str(s.get("id", "") or "").strip()
        if iid:
            ids.add(iid)
    return ids


def _build_ability_ids(const: Any) -> Set[str]:
    ids: Set[str] = set()
    for s in (getattr(const, "PLAYER_ABILITY_SEEDS", None) or []):
        iid = str(s.get("id", "") or "").strip()
        if iid:
            ids.add(iid)
    return ids


def _build_player_npc_lookup(const: Any) -> Dict[str, dict]:
    """Return a mapping of npc_id → NPC seed dict.

    Searches both PLAYER_NPCS and NPCS, mirroring the cross-reference logic
    in record_builders._build_characters.  Attainable (unlockable) characters
    store their description in NPCS, not PLAYER_NPCS.
    """
    lookup: Dict[str, dict] = {}
    for source in ("NPCS", "PLAYER_NPCS"):
        for npc in (getattr(const, source, None) or []):
            nid = str(npc.get("npc_id", "") or "").strip()
            if nid:
                lookup[nid] = npc
    return lookup


def validate_characters(records: List[DevRecord], const: Any) -> Dict[str, Any]:
    """Validate equipment slots, abilities, and description quality on every
    character DevRecord.

    Only records whose id appears in ``ATTAINABLE_PLAYER_CHARACTERS`` carry
    equipment/ability slots — ``PLAYER_NPCS`` entries are skipped silently.

    Annotates each record's ``extras``:
      ``_errors``         — list of SimpleNamespace error/warning objects
      ``_validated``      — True
      ``_invalid_equip``  — set of item ids that failed validation
      ``_invalid_abilities`` — set of ability ids that failed validation

    Returns a summary dict: ``total_errors``, ``invalid``, ``by_code``,
    ``total_warnings``, ``warned``.
    """
    weapon_ids    = _build_weapon_ids(const)
    armor_ids     = _build_armor_ids(const)
    accessory_ids = _build_accessory_ids(const)
    ability_ids   = _build_ability_ids(const)
    npc_lookup    = _build_player_npc_lookup(const)

    pc_index: Dict[str, dict] = {
        str(pc.get("id", "")): pc
        for pc in (getattr(const, "ATTAINABLE_PLAYER_CHARACTERS", None) or [])
        if isinstance(pc, dict) and pc.get("id")
    }

    by_code:       Dict[str, int] = {}
    total_errors   = 0
    invalid        = 0
    total_warnings = 0
    warned         = 0

    for record in records:
        record.extras["_errors"]           = []
        record.extras["_validated"]        = True
        record.extras["_invalid_equip"]    = set()
        record.extras["_invalid_abilities"] = set()

        pc = pc_index.get(record.id)
        if pc is None:
            continue

        errors: list = []

        # C1 — weapon
        weapon_id = str(pc.get("equipped_weapon") or "").strip()
        if weapon_id and weapon_id not in weapon_ids:
            errors.append(_err(
                "CHARACTER_EQUIP_UNKNOWN_WEAPON",
                f"equipped_weapon '{weapon_id}' is not registered in WEAPON_SEEDS.",
            ))
            record.extras["_invalid_equip"].add(weapon_id)
            by_code["CHARACTER_EQUIP_UNKNOWN_WEAPON"] = (
                by_code.get("CHARACTER_EQUIP_UNKNOWN_WEAPON", 0) + 1
            )

        # C2 — armor slots
        for slot in _ARMOR_SLOTS:
            armor_id = str(pc.get(slot) or "").strip()
            if armor_id and armor_id not in armor_ids:
                errors.append(_err(
                    "CHARACTER_EQUIP_UNKNOWN_ARMOR",
                    f"{slot} '{armor_id}' is not registered in ARMOR_SEEDS.",
                ))
                record.extras["_invalid_equip"].add(armor_id)
                by_code["CHARACTER_EQUIP_UNKNOWN_ARMOR"] = (
                    by_code.get("CHARACTER_EQUIP_UNKNOWN_ARMOR", 0) + 1
                )

        # C3 — accessory (optional slot)
        acc_id = str(pc.get("equipped_accessory") or "").strip()
        if acc_id and acc_id not in accessory_ids:
            errors.append(_err(
                "CHARACTER_EQUIP_UNKNOWN_ACCESSORY",
                f"equipped_accessory '{acc_id}' is not registered in ACCESSORY_SEEDS.",
            ))
            record.extras["_invalid_equip"].add(acc_id)
            by_code["CHARACTER_EQUIP_UNKNOWN_ACCESSORY"] = (
                by_code.get("CHARACTER_EQUIP_UNKNOWN_ACCESSORY", 0) + 1
            )

        # C4 — abilities
        for ability_id in (pc.get("abilities") or []):
            aid = str(ability_id or "").strip()
            if aid and aid not in ability_ids:
                errors.append(_err(
                    "CHARACTER_UNKNOWN_ABILITY",
                    f"ability '{aid}' is not registered in PLAYER_ABILITY_SEEDS.",
                ))
                record.extras["_invalid_abilities"].add(aid)
                by_code["CHARACTER_UNKNOWN_ABILITY"] = (
                    by_code.get("CHARACTER_UNKNOWN_ABILITY", 0) + 1
                )

        # C5 — description length (warning)
        npc_seed = npc_lookup.get(record.id, {})
        desc = str(npc_seed.get("description", "") or "").strip()
        if len(desc) < _MIN_DESCRIPTION_LENGTH:
            errors.append(_warn(
                "CHARACTER_SHORT_DESCRIPTION",
                f"description is {len(desc)} chars "
                f"(minimum {_MIN_DESCRIPTION_LENGTH}). "
                "Expand to match Lyren Vale's reference length.",
            ))
            by_code["CHARACTER_SHORT_DESCRIPTION"] = (
                by_code.get("CHARACTER_SHORT_DESCRIPTION", 0) + 1
            )

        hard_errors   = [e for e in errors if e.severity == "error"]
        soft_warnings = [e for e in errors if e.severity == "warning"]

        if errors:
            record.extras["_errors"] = errors

        if hard_errors:
            total_errors += len(hard_errors)
            invalid      += 1

        if soft_warnings:
            total_warnings += len(soft_warnings)
            warned         += 1

    return {
        "total_errors":   total_errors,
        "invalid":        invalid,
        "by_code":        by_code,
        "total_warnings": total_warnings,
        "warned":         warned,
    }