"""
Ability integrity validator.

Structural rules
----------------
A1  ABILITY_UNKNOWN_TYPE       ability_type not in recognised set
A2  ABILITY_UNKNOWN_EFFECT     effect not in recognised set
A3  ABILITY_DAMAGE_NO_POWER    effect=damage but base_power == 0
A4  ABILITY_HEAL_NO_POWER      effect=heal but base_power == 0
A5  ABILITY_STATUS_NO_KEYS     effect=status/cure but status_keys is empty
A6  ABILITY_NO_ELEMENTS        damage/status/heal ability has no elements  (warning)

Balance rules  (warning — mirrors equipment TP balance check)
---------------
B1  ABILITY_BALANCE_WEAK       total_value < 65% of group average
B2  ABILITY_BALANCE_STRONG     total_value > 145% of group average
    Groups are (ability_type, level, effect).  Groups with a single member
    are not balance-checked (no meaningful average).

total_value formula
-------------------
    tv = base_power
       + len(status_keys) * 8
       + (4 if can_aoe else 0)
       - ap_cost
"""
from __future__ import annotations

from collections import defaultdict
from typing import Dict, List, Any

from tui.services.dev.dataservices.models import (
    AbilityNode,
    AbilityTypeNode,
    AbilityValidationError,
)

_KNOWN_TYPES   = {"technique", "faith", "magic", "tech", "skill"}
_KNOWN_EFFECTS = {"damage", "heal", "status", "revive", "cure"}


def _err(code: str, message: str, severity: str = "error") -> AbilityValidationError:
    return AbilityValidationError(code=code, message=message, severity=severity)


def _total_value(seed: dict) -> float:
    bp          = float(seed.get("base_power", 0) or 0)
    ap          = float(seed.get("ap_cost",    0) or 0)
    status_keys = seed.get("status_keys") or []
    can_aoe     = bool(seed.get("can_aoe", False))
    return bp + len(status_keys) * 8.0 + (4.0 if can_aoe else 0.0) - ap


def _flat_nodes(tree: List[AbilityTypeNode]) -> List[AbilityNode]:
    out: List[AbilityNode] = []
    for type_node in tree:
        for level_node in type_node.level_buckets:
            out.extend(level_node.abilities)
    return out


def validate_ability_tree(tree: List[AbilityTypeNode]) -> Dict[str, int]:
    """Validate every AbilityNode in *tree*, annotating .errors in-place.

    Returns a summary dict::
        {"abilities_scanned": int, "invalid": int, "total_errors": int,
         "by_code": {code: count}}
    """
    all_nodes = _flat_nodes(tree)

    # Reset existing errors
    for node in all_nodes:
        node.errors.clear()

    by_code: Dict[str, int] = defaultdict(int)

    # ── Build balance groups ──────────────────────────────────────────────
    # group key: (ability_type, level, effect)
    tv_by_group: Dict[tuple, List[float]] = defaultdict(list)
    node_group:  Dict[str, tuple]         = {}   # ability_id → group key

    for node in all_nodes:
        seed   = node.record.extras.get("_seed") or {}
        atype  = str(seed.get("ability_type", "") or "").lower()
        level  = int(seed.get("level", 1) or 1)
        effect = str(seed.get("effect", "") or "").lower()
        gkey   = (atype, level, effect)
        tv     = _total_value(seed)
        tv_by_group[gkey].append(tv)
        node_group[node.ability_id] = gkey

    group_avg: Dict[tuple, float] = {
        k: sum(v) / len(v)
        for k, v in tv_by_group.items()
        if len(v) > 1
    }

    # ── Per-node checks ───────────────────────────────────────────────────
    for node in all_nodes:
        seed        = node.record.extras.get("_seed") or {}
        atype       = str(seed.get("ability_type", "") or "").lower()
        effect      = str(seed.get("effect", "") or "").lower()
        base_power  = int(seed.get("base_power", 0) or 0)
        status_keys = seed.get("status_keys") or []
        elements    = seed.get("elements") or []

        # A1
        if atype not in _KNOWN_TYPES:
            node.errors.append(_err(
                "ABILITY_UNKNOWN_TYPE",
                f"ability_type '{atype}' is not a recognised type.",
            ))
            by_code["ABILITY_UNKNOWN_TYPE"] += 1

        # A2
        if effect not in _KNOWN_EFFECTS:
            node.errors.append(_err(
                "ABILITY_UNKNOWN_EFFECT",
                f"effect '{effect}' is not a recognised effect.",
            ))
            by_code["ABILITY_UNKNOWN_EFFECT"] += 1

        # A3
        if effect == "damage" and base_power == 0:
            node.errors.append(_err(
                "ABILITY_DAMAGE_NO_POWER",
                "Damage ability has base_power of 0.",
            ))
            by_code["ABILITY_DAMAGE_NO_POWER"] += 1

        # A4
        if effect == "heal" and base_power == 0:
            node.errors.append(_err(
                "ABILITY_HEAL_NO_POWER",
                "Heal ability has base_power of 0.",
            ))
            by_code["ABILITY_HEAL_NO_POWER"] += 1

        # A5
        if effect in ("status", "cure") and not status_keys:
            node.errors.append(_err(
                "ABILITY_STATUS_NO_KEYS",
                f"Effect '{effect}' ability has no status_keys.",
            ))
            by_code["ABILITY_STATUS_NO_KEYS"] += 1

        # A6
        if effect in ("damage", "status", "heal") and not elements:
            node.errors.append(_err(
                "ABILITY_NO_ELEMENTS",
                "Ability has no elements defined.",
                severity="warning",
            ))
            by_code["ABILITY_NO_ELEMENTS"] += 1

        # B1 / B2
        gkey = node_group.get(node.ability_id)
        if gkey and gkey in group_avg:
            avg = group_avg[gkey]
            tv  = _total_value(seed)
            if avg != 0:
                ratio = tv / avg
                if ratio < 0.65:
                    node.errors.append(_err(
                        "ABILITY_BALANCE_WEAK",
                        f"Total value {tv:.1f} is only {ratio:.0%} of "
                        f"group average {avg:.1f} "
                        f"(type={gkey[0]}, lv={gkey[1]}, effect={gkey[2]}).",
                        severity="warning",
                    ))
                    by_code["ABILITY_BALANCE_WEAK"] += 1
                elif ratio > 1.45:
                    node.errors.append(_err(
                        "ABILITY_BALANCE_STRONG",
                        f"Total value {tv:.1f} is {ratio:.0%} of "
                        f"group average {avg:.1f} "
                        f"(type={gkey[0]}, lv={gkey[1]}, effect={gkey[2]}).",
                        severity="warning",
                    ))
                    by_code["ABILITY_BALANCE_STRONG"] += 1

    invalid      = sum(1 for n in all_nodes if n.errors)
    total_errors = sum(len(n.errors) for n in all_nodes)

    return {
        "abilities_scanned": len(all_nodes),
        "invalid":           invalid,
        "total_errors":      total_errors,
        "by_code":           dict(by_code),
    }