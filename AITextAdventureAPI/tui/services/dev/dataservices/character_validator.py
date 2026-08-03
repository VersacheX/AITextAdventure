"""
Character equipment integrity validator.

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
"""
from __future__ import annotations

from types import SimpleNamespace
from typing import Any, Dict, List, Set

from tui.services.dev.dataservices.models import DevRecord


_ARMOR_SLOTS: tuple[str, ...] = ("arm_armor", "head_armor", "body_armor", "leg_armor")


def _err(code: str, message: str) -> Any:
    return SimpleNamespace(code=code, message=message, severity="error")


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


def validate_characters(records: List[DevRecord], const: Any) -> Dict[str, Any]:
    """Validate equipment slots and abilities on every character DevRecord.

    Only records whose id appears in ``ATTAINABLE_PLAYER_CHARACTERS`` carry
    equipment/ability slots — ``PLAYER_NPCS`` entries are skipped silently.

    Annotates each record's ``extras``:
      ``_errors``         — list of SimpleNamespace error objects
      ``_validated``      — True
      ``_invalid_equip``  — set of item ids that failed validation
      ``_invalid_abilities`` — set of ability ids that failed validation

    Returns a summary dict: ``total_errors``, ``invalid``, ``by_code``.
    """
    weapon_ids    = _build_weapon_ids(const)
    armor_ids     = _build_armor_ids(const)
    accessory_ids = _build_accessory_ids(const)
    ability_ids   = _build_ability_ids(const)

    pc_index: Dict[str, dict] = {
        str(pc.get("id", "")): pc
        for pc in (getattr(const, "ATTAINABLE_PLAYER_CHARACTERS", None) or [])
        if isinstance(pc, dict) and pc.get("id")
    }

    by_code:     Dict[str, int] = {}
    total_errors = 0
    invalid      = 0

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

        if errors:
            record.extras["_errors"] = errors
            total_errors += len(errors)
            invalid      += 1

    return {
        "total_errors": total_errors,
        "invalid":      invalid,
        "by_code":      by_code,
    }