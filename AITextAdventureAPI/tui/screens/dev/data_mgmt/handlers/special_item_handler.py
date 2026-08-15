"""
Special-item table population, row coloring, copy, and validation.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from rich.style import Style
from rich.text import Text

from textual.widgets import DataTable, Static

from tui.screens.dev.data_mgmt.handlers._constants import (
    ROW_DEFAULT_STYLE,
    ROW_ERROR_STYLE,
    ROW_INFO_STYLE,
    ROW_OK_STYLE,
)

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen


# ── Table columns ─────────────────────────────────────────────────────────────

_SI_COLUMNS = ("Name", "ID", "Err")


# ── Row style / error cell helpers ────────────────────────────────────────────

def _si_row_style(record: Any) -> Style:
    """Row tint priority: error > info > default."""
    errors = (record.extras.get("_errors") or []) if record.extras else []
    if any(e.severity == "error" for e in errors):
        return ROW_ERROR_STYLE
    if any(e.severity == "info" for e in errors):
        return ROW_INFO_STYLE
    return ROW_DEFAULT_STYLE


def _si_error_cell(record: Any) -> Text:
    """Compact error indicator cell for the special-item table."""
    errors = (record.extras.get("_errors") or []) if record.extras else []
    if not errors:
        return Text("✓", style=ROW_OK_STYLE)
    count     = len(errors)
    has_error = any(e.severity == "error" for e in errors)
    has_info  = any(e.severity == "info"  for e in errors)
    if has_error:
        return Text(f"✗{count}", style=ROW_ERROR_STYLE)
    if has_info:
        return Text(f"i{count}", style=ROW_INFO_STYLE)
    return Text(f"?{count}", style=ROW_DEFAULT_STYLE)


def _si_severity_rank(record: Any) -> int:
    errors = (record.extras.get("_errors") or []) if record.extras else []
    if any(e.severity == "error" for e in errors):
        return 0
    if any(e.severity == "info"  for e in errors):
        return 1
    if errors:
        return 2
    return 3


# ── Table population ──────────────────────────────────────────────────────────

def _populate_special_item_table(screen: "DataMgmtScreen", records: list) -> None:
    table = screen.query_one("#dm-special-item-table", DataTable)
    table.clear(columns=True)
    for col in _SI_COLUMNS:
        table.add_column(col, key=col)

    for idx, r in enumerate(records):
        row_style = _si_row_style(r)
        table.add_row(
            Text(r.name, style=row_style),
            Text(r.id,   style=row_style),
            _si_error_cell(r),
            key=str(idx),
        )


# ── List rebuild ──────────────────────────────────────────────────────────────

def rebuild_list_for_screen(screen: "DataMgmtScreen") -> None:
    """Rebuild the special-item DataTable. Called from core.rebuild_list_for_screen."""
    from tui.services.dev.dataservices.catalog import get_records  # noqa: PLC0415

    records = get_records("special_item")
    records = sorted(records, key=lambda r: (_si_severity_rank(r), r.name.lower()))
    screen._last_filtered = records
    _populate_special_item_table(screen, records)
    screen.query_one("#dm-status", Static).update(f"{len(records)} record(s)")


# ── Copy ──────────────────────────────────────────────────────────────────────

def copy_special_items(screen: "DataMgmtScreen") -> str:
    records = screen._last_filtered or []
    lines = []
    for r in records:
        errors = (r.extras.get("_errors") or []) if r.extras else []
        if any(e.severity == "error" for e in errors):
            tag = "  ·  [ERROR]"
        elif any(e.severity == "info" for e in errors):
            tag = "  ·  [INFO]"
        else:
            tag = ""
        lines.append(f"{r.name}  ({r.id}){tag}")
    return "\n".join(lines)


# ── Validate ──────────────────────────────────────────────────────────────────

def validate_special_items_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.services.dev.dataservices.special_item_validator import validate_special_items  # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import get_records, get_timeline_tree         # noqa: PLC0415

    all_records     = get_records("special_item")
    timeline_groups = get_timeline_tree()
    summary         = validate_special_items(all_records, timeline_groups)

    rebuild_list_for_screen(screen)

    total_errors = summary.get("total_errors", 0)
    invalid      = summary.get("invalid", 0)
    by_code      = summary.get("by_code", {})

    if total_errors == 0:
        screen.notify("✓ Special items OK — all items are reachable and counts are valid.", timeout=3.0)
        return

    parts: list[str] = []
    no_src  = by_code.get("SPECIAL_ITEM_NO_SOURCE", 0)
    imp_cnt = by_code.get("SPECIAL_ITEM_IMPOSSIBLE_COUNTS", 0)
    no_rem  = by_code.get("SPECIAL_ITEM_NEVER_REMOVED", 0)
    if no_src:
        parts.append(f"{no_src} unreachable")
    if imp_cnt:
        parts.append(f"{imp_cnt} impossible give/remove")
    if no_rem:
        parts.append(f"{no_rem} never-removed (info)")

    screen.notify(
        f"Special items: {invalid} error(s) — {', '.join(parts)}",
        severity="warning",
        timeout=6.0,
    )
