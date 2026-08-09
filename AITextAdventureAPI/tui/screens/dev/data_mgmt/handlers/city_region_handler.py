"""
City/region validation.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen


# Maps zone_key → the city record id suffix for that zone
_ZONE_TO_CITY_SUFFIX = {
    "large_city_hostile_seeds": "large_city",
    "mid_city_hostile_seeds":   "mid_city",
    "small_city_hostile_seeds": "small_city",
}


def validate_city_region_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.services.dev.dataservices.city_region_validator import validate_region_for_screen  # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import get_records                               # noqa: PLC0415
    from tui.screens.dev.data_mgmt.handlers.core import rebuild_list_for_screen                 # noqa: PLC0415
    import game.constants as const                                                              # noqa: PLC0415

    summary = validate_region_for_screen(const)

    total_errors = summary.get("total_errors", 0)
    invalid      = summary.get("invalid", 0)
    scanned      = summary.get("regions_scanned", 0)
    by_code      = summary.get("by_code", {})
    nodes        = summary.get("nodes", [])

    # ── Annotate DevRecords so the list rows pick up error colours ────────
    city_records = {r.id: r for r in get_records("city")}

    for node in nodes:
        # 1. Annotate the region record itself (e.g. "region_desert")
        region_record = city_records.get(f"region_{node.region_id}")
        if region_record is not None:
            if region_record.extras is None:
                region_record.extras = {}
            region_record.extras["_errors"]    = node.errors
            region_record.extras["_validated"] = True

        # 2. Annotate each city-size record with its zone-specific errors
        #    e.g. "desert_large_city" gets only the large_city_hostile_seeds errors
        errors_by_zone: dict[str, list] = {}
        for err in node.errors:
            zone = getattr(err, "zone", "")
            errors_by_zone.setdefault(zone, []).append(err)

        for zone_key, city_suffix in _ZONE_TO_CITY_SUFFIX.items():
            city_id     = f"{node.region_id}_{city_suffix}"
            city_record = city_records.get(city_id)
            if city_record is None:
                continue
            if city_record.extras is None:
                city_record.extras = {}
            zone_errors = errors_by_zone.get(zone_key, [])
            city_record.extras["_errors"]    = zone_errors
            city_record.extras["_validated"] = True

    # Rebuild the list so row colours are applied immediately
    if screen._category == "city":
        rebuild_list_for_screen(screen)

    gaps     = by_code.get("REGION_HOSTILE_COVERAGE_GAP", 0)
    sparse   = by_code.get("REGION_HOSTILE_COVERAGE_SPARSE", 0)
    no_seeds = by_code.get("REGION_HOSTILE_NO_SEEDS", 0)

    if total_errors == 0:
        screen.notify(f"✓ All {scanned} regions have full Lv 1–100 hostile coverage.", timeout=3.0)
    else:
        parts = []
        if no_seeds:
            parts.append(f"{no_seeds} zone(s) empty")
        if gaps:
            parts.append(f"{gaps} coverage gap(s)")
        if sparse:
            parts.append(f"{sparse} sparse band(s)")
        screen.notify(
            f"✗ {invalid}/{scanned} region(s) have issues — {', '.join(parts)}.",
            severity="warning",
            timeout=6.0,
        )