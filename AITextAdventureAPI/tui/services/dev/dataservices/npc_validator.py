"""NPC seed completeness validator.

Rules
-----
N1  NPC_MISSING_FIELD
    A required top-level field (npc_id, name, description, image) is absent
    or blank.

N2  NPC_MISSING_SECTION
    A required section (psychology, enneagram, shadow_psychology) is absent
    or not a non-empty dict.

N3  NPC_MISSING_SECTION_KEY
    A required key within psychology / enneagram / shadow_psychology is absent
    or blank.

N4  NPC_MISSING_OPTIONAL   [severity=info]
    An optional presentation field (theme_song, song_id) is absent or blank.
    Shown in cyan — not counted as an error.
"""
from __future__ import annotations

from types import SimpleNamespace
from typing import Any, Dict, List

from tui.services.dev.dataservices.models import NpcGroupNode


# ── Required schema ───────────────────────────────────────────────────────────

_REQUIRED_TOP_LEVEL: tuple[str, ...] = ("npc_id", "name", "description", "image")
_OPTIONAL_TOP_LEVEL: tuple[str, ...] = ("theme_song", "song_id")

_REQUIRED_SECTIONS: Dict[str, tuple[str, ...]] = {
    "psychology": ("mbti", "dominant", "auxiliary", "tertiary", "inferior"),
    "enneagram": (
        "enneagram_type",
        "core_fear",
        "core_desire",
        "defense_mechanism",
        "stress_line",
        "growth_line",
        "instinctual_variant",
    ),
}


# ── Error helpers ─────────────────────────────────────────────────────────────

def _err(code: str, message: str) -> Any:
    return SimpleNamespace(code=code, message=message, severity="error")


def _info(code: str, message: str) -> Any:
    return SimpleNamespace(code=code, message=message, severity="info")


# ── Core validation logic ─────────────────────────────────────────────────────

def _validate_seed(npc: dict) -> list:
    """Return a list of error/info objects for a single NPC seed dict."""
    errors: list = []

    # N1 — required top-level fields
    for field in _REQUIRED_TOP_LEVEL:
        value = npc.get(field)
        if not value or not str(value).strip():
            errors.append(_err(
                "NPC_MISSING_FIELD",
                f"Required field '{field}' is missing or blank.",
            ))

    # N2 / N3 — required sections and their keys
    for section, keys in _REQUIRED_SECTIONS.items():
        block = npc.get(section)
        if not block or not isinstance(block, dict):
            errors.append(_err(
                "NPC_MISSING_SECTION",
                f"Required section '{section}' is missing or not a dict.",
            ))
            continue
        for key in keys:
            value = block.get(key)
            if not value or not str(value).strip():
                errors.append(_err(
                    "NPC_MISSING_SECTION_KEY",
                    f"'{section}.{key}' is missing or blank.",
                ))

    # N4 — optional presentation fields (info only)
    for field in _OPTIONAL_TOP_LEVEL:
        value = npc.get(field)
        if not value or not str(value).strip():
            errors.append(_info(
                "NPC_MISSING_OPTIONAL",
                f"Optional field '{field}' is not set.",
            ))

    return errors


# ── Public API ────────────────────────────────────────────────────────────────

def validate_npc_tree(tree: List[NpcGroupNode], const: Any) -> Dict[str, Any]:
    """Validate every NPC seed in *tree* for structural completeness.

    Annotates each ``NpcRecordNode.record.extras``:
      ``_errors``    — list of SimpleNamespace error/info objects
      ``_validated`` — True

    Returns a summary dict: ``total_errors``, ``total_info``, ``invalid``,
    ``by_code``.
    """
    # Build a flat lookup: npc_id → raw seed dict from const.NPC_GROUPS / const.NPCS
    seed_index: Dict[str, dict] = {}
    npc_groups = getattr(const, "NPC_GROUPS", None)
    if npc_groups and isinstance(npc_groups, dict):
        for npc_list in npc_groups.values():
            for npc in (npc_list or []):
                if isinstance(npc, dict):
                    nid = str(npc.get("npc_id", "")).strip()
                    if nid:
                        seed_index[nid] = npc
    else:
        for npc in (getattr(const, "NPCS", None) or []):
            if isinstance(npc, dict):
                nid = str(npc.get("npc_id", "")).strip()
                if nid:
                    seed_index[nid] = npc

    by_code:     Dict[str, int] = {}
    total_errors = 0
    total_info   = 0
    invalid      = 0

    for group in tree:
        for npc_node in group.npcs:
            record = npc_node.record
            record.extras["_errors"]    = []
            record.extras["_validated"] = True

            seed = seed_index.get(npc_node.npc_id)
            if seed is None:
                # Seed not found in const — flag as error
                err = _err("NPC_SEED_NOT_FOUND", "Raw seed not found in constants.")
                record.extras["_errors"] = [err]
                by_code["NPC_SEED_NOT_FOUND"] = by_code.get("NPC_SEED_NOT_FOUND", 0) + 1
                total_errors += 1
                invalid      += 1
                continue

            errors = _validate_seed(seed)
            record.extras["_errors"] = errors

            hard_errors = [e for e in errors if e.severity == "error"]
            info_items  = [e for e in errors if e.severity == "info"]

            if hard_errors:
                invalid += 1
            total_errors += len(hard_errors)
            total_info   += len(info_items)

            for e in errors:
                by_code[e.code] = by_code.get(e.code, 0) + 1

    return {
        "total_errors": total_errors,
        "total_info":   total_info,
        "invalid":      invalid,
        "by_code":      by_code,
    }