"""
Character list copy and validation.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from tui.screens.dev.data_mgmt.handlers._constants import CHARACTER_CATEGORY

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen


def copy_characters(screen: "DataMgmtScreen") -> str:
    records = screen._last_filtered or []
    lines = []
    for r in records:
        errors = (r.extras or {}).get("_errors") or []
        if any(e.severity == "error" for e in errors):
            messages = "  ·  [ERROR] " + " | ".join(
                f"{e.code}: {e.message}" for e in errors if e.severity == "error"
            )
        else:
            messages = ""
        lines.append(f"{r.name}  {r.subtitle}{messages}")
    return "\n".join(lines)


def validate_characters_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.services.dev.dataservices.character_validator import validate_characters  # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import get_records                      # noqa: PLC0415
    import game.constants as const                                                      # noqa: PLC0415

    from tui.screens.dev.data_mgmt.handlers.core import rebuild_list_for_screen        # noqa: PLC0415

    records = get_records(CHARACTER_CATEGORY)
    summary = validate_characters(records, const)

    rebuild_list_for_screen(screen)

    total_errors = summary.get("total_errors", 0)
    invalid      = summary.get("invalid", 0)

    if total_errors == 0:
        screen.notify("✓ Character integrity OK — no issues found.", timeout=3.0)
    else:
        screen.notify(
            f"✗ {total_errors} issue(s) across {invalid} character(s) — flagged in list.",
            severity="warning",
            timeout=5.0,
        )