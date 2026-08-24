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

R4  REGION_HOSTILE_RARITY_GAP
    A 5-level window (the band the normal encounter selector inspects) is
    missing at least one seed of a required rarity (common, uncommon, rare,
    superrare). Reported per zone, per window, per missing rarity.
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

# Rarity coverage: normal encounter selection (`pick_seeds_for_rarity`) inspects
# seeds whose min_spawn_level falls within a 5-level window of the party level,
# so every such window must contain at least one seed of each required rarity.
_RARITY_WINDOW    = 5
_REQUIRED_RARITIES = ("common", "uncommon", "rare", "superrare")

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
    rarity:   str = ""


@dataclass
class RegionNode:
    """One validated region (e.g. 'desert')."""
    region_id: str          # e.g. "desert"
    label:     str          # display label e.g. "Desert"
    data:      Dict[str, Any] = field(default_factory=dict)
    errors:    List[RegionValidationError] = field(default_factory=list)


def _band_label(band_min: int, band_max: int) -> str:
    return f"Lv {band_min}–{band_max}"


def _minimal_rarity_additions(
    present_levels: set,
    uncovered_starts: List[int],
) -> List[int]:
    """Return the fewest seed levels that cover every uncovered sliding window.

    Interval point-cover: an uncovered window ``[s, s+4]`` is closed by any seed
    whose level lies in that range.  Processing uncovered windows left-to-right
    and placing each new seed at the *right edge* (``s + _RARITY_WINDOW - 1``) of
    the earliest still-open window maximises how many later, overlapping windows
    the same seed also closes — the greedy optimum for covering intervals by
    points.
    """
    additions: List[int] = []
    ordered = sorted(uncovered_starts)
    idx = 0
    while idx < len(ordered):
        start = ordered[idx]
        # Place the seed as late as possible while still covering this window,
        # so it also covers the maximum number of following overlapping windows.
        level = min(start + _RARITY_WINDOW - 1, _LEVEL_MAX)
        additions.append(level)
        # Skip every remaining window this seed now covers (start within
        # [level - 4, level] — all such starts are >= this start and <= level).
        idx += 1
        while idx < len(ordered) and ordered[idx] <= level:
            idx += 1
    return additions


def _validate_rarity_coverage(
    seeds: List[Dict[str, Any]],
    zone_key: str,
    zone_label: str,
) -> List[RegionValidationError]:
    """Ensure every *sliding* 5-level window has each required rarity, then
    recommend the minimum set of seed additions that closes all gaps.

    Mirrors `pick_seeds_for_rarity`, which considers seeds whose min_spawn_level
    is within `_RARITY_WINDOW` levels of the party level.  Because the windows
    slide (1–5, 2–6, 3–7, …) a single missing rarity spans several overlapping
    windows; rather than reporting each window, we compute the fewest seed levels
    that would cover them all and emit one actionable error per addition.
    """
    errors: List[RegionValidationError] = []

    # Levels at which each rarity is present (within the valid range).
    levels_by_rarity: Dict[str, set] = defaultdict(set)
    for seed in seeds:
        if not isinstance(seed, dict):
            continue
        lv = int(seed.get("min_spawn_level", 0) or 0)
        if lv < _LEVEL_MIN or lv > _LEVEL_MAX:
            continue
        rarity = str(seed.get("rarity", "common") or "common").lower()
        levels_by_rarity[rarity].add(lv)

    # Sliding window starts: 1–5, 2–6, … up to the last full 5-level window.
    window_starts = range(_LEVEL_MIN, _LEVEL_MAX - _RARITY_WINDOW + 2)

    for rarity in _REQUIRED_RARITIES:
        present = levels_by_rarity.get(rarity, set())

        uncovered_starts = [
            start for start in window_starts
            if not any(
                start <= lv <= start + _RARITY_WINDOW - 1
                for lv in present
            )
        ]
        if not uncovered_starts:
            continue

        additions = _minimal_rarity_additions(present, uncovered_starts)
        for level in additions:
            band_min = max(_LEVEL_MIN, level - _RARITY_WINDOW + 1)
            band_max = level
            errors.append(RegionValidationError(
                code="REGION_HOSTILE_RARITY_GAP",
                message=(
                    f"{zone_label}: add a '{rarity}' hostile seed at "
                    f"Lv {level} (covers the missing '{rarity}' 5-level "
                    f"windows around Lv {band_min}–{band_max})."
                ),
                severity="error",
                zone=zone_key,
                band_min=band_min,
                band_max=band_max,
                rarity=rarity,
            ))

    return errors


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

    # R4: rarity coverage per 5-level window
    errors.extend(_validate_rarity_coverage(seeds, zone_key, zone_label))

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
