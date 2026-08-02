"""City and Region integrity validator.

Validates hostile level coverage for all regions and their associated cities.

Rules
-----
R1  REGION_HOSTILE_COVERAGE_GAP
    A region zone (overworld, large_city, mid_city, small_city) has no hostile
    seeds covering a 10-level band within the expected 1–100 range.
    Reported per zone, per gap band.

R2  REGION_HOSTILE_COVERAGE_SPARSE
    A 10-level band has fewer than 2 distinct hostile seeds (warning — low
    variety, not a hard gap).

R3  REGION_HOSTILE_NO_SEEDS
    A zone has no hostile seeds at all.
"""
from __future__ import annotations

import logging
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

log = logging.getLogger(__name__)

_LEVEL_MIN  = 1
_LEVEL_MAX  = 100
_BAND_SIZE  = 10
_SPARSE_MIN = 2   # seeds per band below this → sparse warning

_ZONE_LABELS: Dict[str, str] = {
    "region_hostile_seeds":     "Overworld",
    "large_city_hostile_seeds": "Large City",
    "mid_city_hostile_seeds":   "Mid City",
    "small_city_hostile_seeds": "Small City",
}


@dataclass
class RegionValidationError:
    code:     str
    message:  str
    severity: str = "error"   # "error" | "warning" | "info"
    zone:     str = ""
    band_min: int = 0
    band_max: int = 0


@dataclass
class RegionNode:
    """One validated region (e.g. 'desert')."""
    region_id: str          # e.g. "desert"
    label:     str          # display label e.g. "Desert"
    data:      Dict[str, Any] = field(default_factory=dict)
    errors:    List[RegionValidationError] = field(default_factory=list)


def _band_label(band_min: int, band_max: int) -> str:
    return f"Lv {band_min}–{band_max}"


def _validate_zone(
    seeds: List[Dict[str, Any]],
    zone_key: str,
    zone_label: str,
) -> List[RegionValidationError]:
    errors: List[RegionValidationError] = []

    if not seeds:
        errors.append(RegionValidationError(
            code="REGION_HOSTILE_NO_SEEDS",
            message=f"{zone_label}: no hostile seeds defined.",
            severity="error",
            zone=zone_key,
        ))
        return errors

    # Build per-band counts
    band_counts: Dict[int, int] = defaultdict(int)
    for seed in seeds:
        if not isinstance(seed, dict):
            continue
        lv = int(seed.get("min_spawn_level", 0) or 0)
        if lv < _LEVEL_MIN or lv > _LEVEL_MAX:
            continue
        band = ((lv - 1) // _BAND_SIZE) * _BAND_SIZE + 1
        band_counts[band] += 1

    # Check every band in 1–100
    for band_start in range(_LEVEL_MIN, _LEVEL_MAX, _BAND_SIZE):
        band_end   = band_start + _BAND_SIZE - 1
        band_label = _band_label(band_start, band_end)
        count      = band_counts.get(band_start, 0)

        if count == 0:
            errors.append(RegionValidationError(
                code="REGION_HOSTILE_COVERAGE_GAP",
                message=f"{zone_label} {band_label}: no hostile seeds in this level band.",
                severity="error",
                zone=zone_key,
                band_min=band_start,
                band_max=band_end,
            ))
        elif count < _SPARSE_MIN:
            errors.append(RegionValidationError(
                code="REGION_HOSTILE_COVERAGE_SPARSE",
                message=(
                    f"{zone_label} {band_label}: only {count} hostile seed(s) "
                    f"— consider adding more variety (minimum {_SPARSE_MIN} recommended)."
                ),
                severity="warning",
                zone=zone_key,
                band_min=band_start,
                band_max=band_end,
            ))

    return errors


def validate_region_data(region_data: Dict[str, Any]) -> List[RegionNode]:
    """Validate all regions in REGION_DATA and return annotated RegionNode list."""
    nodes: List[RegionNode] = []
    for region_name, entry in region_data.items():
        node = RegionNode(
            region_id=region_name,
            label=region_name.replace("_", " ").title(),
            data=entry,
        )
        for zone_key, zone_label in _ZONE_LABELS.items():
            seeds = entry.get(zone_key) or []
            node.errors.extend(_validate_zone(seeds, zone_key, zone_label))
        nodes.append(node)

    invalid      = sum(1 for n in nodes if n.errors)
    total_errors = sum(len(n.errors) for n in nodes)
    log.debug(
        "City/region validation: %d regions, %d with issues, %d total issues",
        len(nodes), invalid, total_errors,
    )
    return nodes


def validate_region_for_screen(const: Any) -> Dict[str, Any]:
    """Entry point called from the UI handler.  Returns a summary dict."""
    region_data: Dict[str, Any] = getattr(const, "REGION_DATA", None) or {}
    if not region_data:
        return {"regions_scanned": 0, "invalid": 0, "total_errors": 0, "nodes": []}

    nodes = validate_region_data(region_data)
    invalid      = sum(1 for n in nodes if n.errors)
    total_errors = sum(len(n.errors) for n in nodes)
    by_code: Dict[str, int] = defaultdict(int)
    for n in nodes:
        for e in n.errors:
            by_code[e.code] += 1

    return {
        "regions_scanned": len(nodes),
        "invalid":         invalid,
        "total_errors":    total_errors,
        "by_code":         dict(by_code),
        "nodes":           nodes,
    }
