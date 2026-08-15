"""
Equipment integrity validator.

Structural rules
----------------
E1  EQUIPMENT_NOT_FOUND_IN_TIMELINE
    The equipment item_id does not appear as the target of any award_item or
    dungeon_add_treasure event across the entire loaded timeline tree.  The
    item exists in the seed constants but is unreachable by the player through
    normal play.  Rendered as red in the equipment table.

Balance rules
-------------
B1  EQUIPMENT_TP_LOW  (warning) 
    The item's TP is below 65 % of the peer-group average for items of the
    same type and level.  Rendered as yellow/orange in the equipment table.

B2  EQUIPMENT_TP_HIGH  (info)
    The item's TP exceeds 145 % of the peer-group average for items of the
    same type and level.  Rendered as cyan in the equipment table.
"""
from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict, List, Set

from tui.services.dev.dataservices.models import EquipmentValidationError


def _err(code: str, message: str, severity: str = "error") -> EquipmentValidationError:
    return EquipmentValidationError(code=code, message=message, severity=severity)


_CHARACTER_EQUIP_SLOTS = ("arm_armor", "head_armor", "body_armor", "leg_armor", "equipped_weapon")


def _collect_awarded_item_ids(groups: list, const: Any = None) -> Set[str]:
    """Walk every event in every task across all timeline groups and collect
    item_ids referenced by award_item and dungeon_add_treasure events.
    Also collects equipment pre-equipped on ATTAINABLE_PLAYER_CHARACTERS."""
    awarded: Set[str] = set()

    # Timeline events � award_item and dungeon_add_treasure
    for group in groups:
        for bucket in group.buckets:
            for tn in bucket.tasks:
                task = tn.task
                for stage in ("task_acquire_events", "task_complete_events"):
                    for ev in (task.get(stage) or []):
                        if not isinstance(ev, dict):
                            continue
                        et     = ev.get("event_type", "")
                        params = ev.get("params") or {}
                        if et == "award_item":
                            iid = str(params.get("item_id") or "").strip()
                            if iid:
                                awarded.add(iid)
                        elif et == "dungeon_add_treasure":
                            iid = str(
                                params.get("item_id") or params.get("item") or ""
                            ).strip()
                            if iid:
                                awarded.add(iid)

    # Character starting equipment � pre-equipped items on attainable characters
    if const is not None:
        for char in (getattr(const, "ATTAINABLE_PLAYER_CHARACTERS", None) or []):
            if not isinstance(char, dict):
                continue
            for slot in _CHARACTER_EQUIP_SLOTS:
                iid = str(char.get(slot) or "").strip()
                if iid:
                    awarded.add(iid)

    return awarded


def validate_equipment(records: list, timeline_groups: list, const: Any = None) -> Dict[str, Any]:
    """Validate all equipment DevRecords against the full timeline tree and
    character starting equipment.

    Annotates each record's ``extras["_errors"]`` with a list of
    ``EquipmentValidationError`` objects and sets ``extras["_validated"] = True``.

    Returns a summary dict with ``total_errors``, ``invalid``, and
    ``by_code`` tallies.
    """
    awarded_ids = _collect_awarded_item_ids(timeline_groups, const=const)

    by_code: Dict[str, int] = {}
    total_errors = 0
    invalid      = 0

    for record in records:
        record.extras["_errors"]    = []
        record.extras["_validated"] = True

        # Only notfound-rarity items must have an explicit award source.
        # All other rarities can reach the player via RNG drops.
        if record.extras.get("rarity") != "notfound":
            continue

        if record.id not in awarded_ids:
            err = _err(
                "EQUIPMENT_NOT_FOUND_IN_TIMELINE",
                f"'{record.id}' is rarity 'notfound' but is not awarded by any "
                f"award_item or dungeon_add_treasure event in the timeline.  "
                f"The item is unreachable through normal play.",
            )
            record.extras["_errors"].append(err)
            by_code["EQUIPMENT_NOT_FOUND_IN_TIMELINE"] = (
                by_code.get("EQUIPMENT_NOT_FOUND_IN_TIMELINE", 0) + 1
            )
            total_errors += 1
            invalid      += 1

    # ── B1 / B2: TP balance checks ────────────────────────────────────────
    # Group items by (type_label, level) and compute peer-average TP.
    # Items with no TP value (0 or None) are excluded from comparison so that
    # accessories and purely defensive pieces don't skew weapon averages.
    group_tp: Dict[tuple, List[float]] = defaultdict(list)
    for record in records:
        tp  = record.extras.get("tp") or 0
        if tp <= 0:
            continue
        key = (record.extras.get("type_label", ""), record.extras.get("level", 0))
        group_tp[key].append(float(tp))

    group_avg: Dict[tuple, float] = {
        k: sum(v) / len(v) for k, v in group_tp.items() if v
    }

    for record in records:
        tp = record.extras.get("tp") or 0
        if tp <= 0:
            continue
        key = (record.extras.get("type_label", ""), record.extras.get("level", 0))
        avg = group_avg.get(key)
        if avg is None or avg == 0:
            continue
        ratio = float(tp) / avg
        type_label = key[0] or "unknown"
        level      = key[1]
        if ratio < 0.65:
            err = _err(
                "EQUIPMENT_TP_LOW",
                f"'{record.id}' TP {tp} is only {ratio:.0%} of the "
                f"{type_label} Lv {level} peer average {avg:.1f}. "
                f"Consider raising TP or verifying this is intentional.",
                severity="warning",
            )
            record.extras["_errors"].append(err)
            by_code["EQUIPMENT_TP_LOW"] = by_code.get("EQUIPMENT_TP_LOW", 0) + 1
            total_errors += 1
            invalid      += 1
        elif ratio > 1.45:
            err = _err(
                "EQUIPMENT_TP_HIGH",
                f"'{record.id}' TP {tp} is {ratio:.0%} of the "
                f"{type_label} Lv {level} peer average {avg:.1f}. "
                f"Consider lowering TP or verifying this is intentional.",
                severity="info",
            )
            record.extras["_errors"].append(err)
            by_code["EQUIPMENT_TP_HIGH"] = by_code.get("EQUIPMENT_TP_HIGH", 0) + 1
            total_errors += 1
            invalid      += 1

    return {
        "total_errors": total_errors,
        "invalid":      invalid,
        "by_code":      by_code,
    }