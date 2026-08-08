"""
City/region validation.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen


def validate_city_region_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.services.dev.dataservices.city_region_validator import validate_region_for_screen  # noqa: PLC0415
    import game.constants as const  # noqa: PLC0415

    summary = validate_region_for_screen(const)

    total_errors = summary.get("total_errors", 0)
    invalid      = summary.get("invalid", 0)
    scanned      = summary.get("regions_scanned", 0)
    by_code      = summary.get("by_code", {})

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