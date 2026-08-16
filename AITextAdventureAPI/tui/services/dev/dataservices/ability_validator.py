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
A7  ABILITY_UNKNOWN_ELEMENT    an element in 'elements' is not in ELEMENTAL_CHAR_KEYS
A8  ABILITY_UNKNOWN_STATUS     a key in 'status_keys' is not in STATUS_EFFECTS
A9  ABILITY_STATUS_THIN        effect=status but len(status_keys) < level  (warning)

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
from typing import Any, Dict, List

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

    *const* should be the ``game.constants`` module.  When supplied, known
    elements are taken from ``const.ELEMENTAL_CHAR_KEYS`` and known statuses
    from ``const.STATUS_EFFECTS`` so the validator stays in sync with the
    game's authoritative data rather than a duplicated hardcoded set.

    Returns a summary dict::
        {"abilities_scanned": int, "invalid": int, "total_errors": int,
         "by_code": {code: count}}
    """
    from game import constants as const
    # Derive known sets from const when available; fall back to safe defaults
    known_elements: frozenset[str] = frozenset(
        str(k).lower() for k in (getattr(const, "ELEMENTAL_CHAR_KEYS", {}) or {}).keys()
    )
    known_statuses: frozenset[str] = frozenset(
        str(k).lower() for k in (getattr(const, "STATUS_EFFECTS", {}) or {}).keys()
    )

    all_nodes = _flat_nodes(tree)

    # Reset existing errors
    for node in all_nodes:
        node.errors.clear()

    by_code: Dict[str, int] = defaultdict(int)

    # ── Build balance groups ──────────────────────────────────────────────
    tv_by_group: Dict[tuple, List[float]] = defaultdict(list)
    node_group:  Dict[str, tuple]         = {}

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

        # A7 — each unknown element is a separate error
        for elem in elements:
            if str(elem).lower() not in known_elements:
                node.errors.append(_err(
                    "ABILITY_UNKNOWN_ELEMENT",
                    f"Element '{elem}' is not in ELEMENTAL_CHAR_KEYS.",
                ))
                by_code["ABILITY_UNKNOWN_ELEMENT"] += 1

        # A8 — each unknown status key is a separate error
        for sk in status_keys:
            if str(sk).lower() not in known_statuses:
                node.errors.append(_err(
                    "ABILITY_UNKNOWN_STATUS",
                    f"status_key '{sk}' is not in STATUS_EFFECTS.",
                ))
                by_code["ABILITY_UNKNOWN_STATUS"] += 1

        # A9 — status-effect abilities should have at least as many status_keys as their level
        if effect == "status" and len(status_keys) < node.level:
            node.errors.append(_err(
                "ABILITY_STATUS_THIN",
                f"Status ability at level {node.level} only has "
                f"{len(status_keys)} status_key(s) (expected ≥ {node.level}).",
                severity="warning",
            ))
            by_code["ABILITY_STATUS_THIN"] += 1

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
                        severity="info",
                    ))
                    by_code["ABILITY_BALANCE_WEAK"] += 1
                elif ratio > 1.45:
                    node.errors.append(_err(
                        "ABILITY_BALANCE_STRONG",
                        f"Total value {tv:.1f} is {ratio:.0%} of "
                        f"group average {avg:.1f} "
                        f"(type={gkey[0]}, lv={gkey[1]}, effect={gkey[2]}).",
                        severity="notice",
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


def validate_abilities_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.services.dev.dataservices.ability_validator import validate_ability_tree  # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import get_ability_tree               # noqa: PLC0415

    tree    = get_ability_tree()
    summary = validate_ability_tree(tree)

    # Repopulate table so flagged rows render in colour
    rebuild_ability_tree_for_screen(screen)

    invalid      = summary.get("invalid", 0)
    total_errors = summary.get("total_errors", 0)

    if total_errors == 0:
        screen.notify("✓ Ability integrity OK — no issues found.", timeout=3.0)
    else:
        screen.notify(
            f"✗ {total_errors} issue(s) across {invalid} ability(s) — flagged in table.",
            severity="warning",
            timeout=5.0,
        )