"""
Hostile table population, sorting, rebuild, copy, and validation.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from rich.text import Text

from textual.widgets import DataTable, Static

from tui.screens.dev.data_mgmt.handlers._constants import (
    ROW_DEFAULT_STYLE,
    ROW_ERROR_STYLE,
    ROW_WARN_STYLE,
    ROW_NOTICE_STYLE,
    ROW_BLUE_STYLE,
    ROW_INFO_STYLE,
    ROW_OK_STYLE,
    fmt_elem_list as _fmt_elem_list,
)
from tui.services.dev.dataservices import HostileNode

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen

# ── Constants ────────────────────────────────────────────────────────────────

_HOSTILE_COLUMNS = ["Name", "ID", "Location", "Region", "Lv", "Rar", "Err"]

_HOSTILE_RARITY_ABBR: dict[str, str] = {
    "common": "Com", "uncommon": "Unc", "rare": "Rar",
    "superrare": "SR", "notfound": "Not",
}

_HOSTILE_RARITY_RANK: dict[str, int] = {
    "common": 0, "uncommon": 1, "rare": 2, "superrare": 3, "notfound": 4,
}

_MGNTA_NOTICE_CODES = frozenset({"HOSTILE_DROP_UNKNOWN_ITEM"})
_BLUE_NOTICE_CODES  = frozenset({"HOSTILE_BALANCE_STRONG", "HOSTILE_ABILITY_MISMATCH"})

_HOSTILE_SORT_KEYS: dict[str, str] = {
    "hostile-sort-lv":       "level",
    "hostile-sort-rarity":   "rarity_rank",
    "hostile-sort-dungeon":  "location_dungeon",
    "hostile-sort-region":   "location_region",
    "hostile-sort-name":     "name",
    "hostile-sort-severity": "severity_rank",
}


# ── Row style / error cell ────────────────────────────────────────────────────

def _hostile_row_style(errors: list):
    if not errors:
        return ROW_DEFAULT_STYLE
    if any(e.severity == "error"   for e in errors):
        return ROW_ERROR_STYLE
    if any(e.severity == "warning" for e in errors):
        return ROW_WARN_STYLE
    if any(e.severity == "notice" and e.code in _MGNTA_NOTICE_CODES for e in errors):
        return ROW_NOTICE_STYLE
    if any(e.severity == "notice" and e.code in _BLUE_NOTICE_CODES  for e in errors):
        return ROW_BLUE_STYLE
    if any(e.severity == "info"    for e in errors):
        return ROW_INFO_STYLE
    return ROW_DEFAULT_STYLE


def _hostile_error_cell(errors: list) -> Text:
    if not errors:
        return Text("✓", style=ROW_OK_STYLE)
    has_error          = any(e.severity == "error"   for e in errors)
    has_warning        = any(e.severity == "warning" for e in errors)
    has_magenta_notice = any(e.severity == "notice" and e.code in _MGNTA_NOTICE_CODES for e in errors)
    has_blue_notice    = any(e.severity == "notice" and e.code in _BLUE_NOTICE_CODES  for e in errors)
    has_info           = any(e.severity == "info"    for e in errors)
    count = len(errors)
    if has_error:
        return Text(f"✗ {count}", style=ROW_ERROR_STYLE)
    if has_warning:
        return Text(f"⚠ {count}", style=ROW_WARN_STYLE)
    if has_magenta_notice:
        return Text(f"● {count}", style=ROW_NOTICE_STYLE)
    if has_blue_notice:
        return Text(f"● {count}", style=ROW_BLUE_STYLE)
    if has_info:
        return Text(f"• {count}", style=ROW_INFO_STYLE)
    return Text(f"• {count}")


def _hostile_severity_rank(node: HostileNode) -> int:
    if any(e.severity == "error"   for e in node.errors):
        return 0
    if any(e.severity == "warning" for e in node.errors):
        return 1
    if any(e.severity == "notice" and e.code in _MGNTA_NOTICE_CODES for e in node.errors):
        return 2
    if any(e.severity == "notice" and e.code in _BLUE_NOTICE_CODES  for e in node.errors):
        return 3
    if any(e.severity == "info"   for e in node.errors):
        return 4
    if node.errors:
        return 5
    return 6


def get_hostile_sort_col(screen: "DataMgmtScreen") -> str:
    from textual.widgets import RadioSet  # noqa: PLC0415
    try:
        sort_radio = screen.query_one("#dm-hostile-sort-radio", RadioSet)
        pressed_id = sort_radio.pressed_button.id if sort_radio.pressed_button else "hostile-sort-lv"
        return _HOSTILE_SORT_KEYS.get(pressed_id, "level")
    except Exception:
        return "level"


# ── Table population ──────────────────────────────────────────────────────────

def _populate_hostile_table(screen: "DataMgmtScreen", nodes: list) -> None:
    sort_col = get_hostile_sort_col(screen)
    sort_asc = getattr(screen, "_hostile_sort_asc", True)

    def _sort_key(n: HostileNode):
        sev = _hostile_severity_rank(n)
        if sort_col == "level":
            primary = n.level
        elif sort_col == "rarity_rank":
            primary = _HOSTILE_RARITY_RANK.get(n.rarity, 99)
        elif sort_col == "location_dungeon":
            primary = (n.location_dungeon or "").lower()
        elif sort_col == "location_region":
            primary = (n.location_region or "").lower()
        elif sort_col == "name":
            primary = n.label.lower()
        elif sort_col == "severity_rank":
            primary = sev
        else:
            primary = n.level
        return (primary, sev, n.label.lower())

    valid_nodes  = [n for n in nodes if isinstance(n, HostileNode)]
    sorted_nodes = sorted(valid_nodes, key=_sort_key, reverse=not sort_asc)
    screen._hostile_flat_nodes = sorted_nodes

    table: DataTable = screen.query_one("#dm-hostile-table", DataTable)
    table.clear(columns=True)
    for col in _HOSTILE_COLUMNS:
        table.add_column(col, key=col)

    for idx, node in enumerate(sorted_nodes):
        rar_abbr  = _HOSTILE_RARITY_ABBR.get(node.rarity, node.rarity[:3].title())
        errors    = node.errors or []
        row_style = _hostile_row_style(errors)
        table.add_row(
            Text(node.label,                        style=row_style),
            Text(node.hostile_id,                   style=row_style),
            Text(node.location_dungeon or "Overworld", style=row_style),
            Text(node.location_region  or "—",      style=row_style),
            Text(str(node.level),                   style=row_style),
            Text(rar_abbr,                          style=row_style),
            _hostile_error_cell(errors),
            key=str(idx),
        )


# ── Rebuild ───────────────────────────────────────────────────────────────────

def rebuild_hostile_tree_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.screens.dev.data_mgmt.treehandlers.hostile_handler import rebuild_hostile_tree  # noqa: PLC0415
    from tui.services.dev.dataservices.hostile_service import flat_hostile_nodes             # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import get_hostile_tree                       # noqa: PLC0415
    from textual.widgets import Tree                                                          # noqa: PLC0415

    if not screen._loaded:
        return
    query = ""
    try:
        from textual.widgets import Input  # noqa: PLC0415
        query = screen.query_one("#dm-filter", Input).value.strip()
    except Exception:
        pass

    tree = screen.query_one("#dm-hostile-tree", Tree)
    total, filtered = rebuild_hostile_tree(
        tree,
        query=query,
        user_expanded=screen._hostile_user_expanded,
        user_collapsed=screen._hostile_user_collapsed,
    )
    screen._last_hostile_filtered = filtered

    nodes = flat_hostile_nodes(filtered if filtered is not None else get_hostile_tree())
    _populate_hostile_table(screen, nodes)

    screen.query_one("#dm-status", Static).update(f"{total} hostile(s)")


# ── Copy ──────────────────────────────────────────────────────────────────────

def copy_hostiles(screen: "DataMgmtScreen") -> str:
    nodes  = getattr(screen, "_hostile_flat_nodes", [])
    header = "\t".join(_HOSTILE_COLUMNS + ["Messages"])
    rows   = [header]
    for node in nodes:
        if not isinstance(node, HostileNode):
            continue
        rar_abbr    = _HOSTILE_RARITY_ABBR.get(node.rarity, node.rarity[:3].title())
        error_count = len(node.errors)
        has_error   = any(e.severity == "error"   for e in node.errors)
        has_warning = any(e.severity == "warning" for e in node.errors)
        if error_count == 0:
            err_cell = "✓"
        elif has_error:
            err_cell = f"✗ {error_count}"
        elif has_warning:
            err_cell = f"⚠ {error_count}"
        else:
            err_cell = f"• {error_count}"
        messages = " | ".join(
            f"[{e.severity.upper()}] {e.code}: {e.message}" for e in node.errors
        ) if node.errors else ""
        rows.append("\t".join([
            node.label,
            node.hostile_id,
            node.location_dungeon or "Overworld",
            node.location_region  or "—",
            str(node.level),
            rar_abbr,
            err_cell,
            messages,
        ]))
    return "\n".join(rows)


# ── Validate ──────────────────────────────────────────────────────────────────

def validate_hostiles_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.services.dev.dataservices.hostile_validator import validate_hostile_tree  # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import get_hostile_tree                 # noqa: PLC0415
    import game.constants as const                                                     # noqa: PLC0415

    tree    = get_hostile_tree()
    summary = validate_hostile_tree(tree, const)

    rebuild_hostile_tree_for_screen(screen)

    invalid      = summary.get("invalid", 0)
    total_errors = summary.get("total_errors", 0)

    if total_errors == 0:
        screen.notify("✓ Hostile integrity OK — no issues found.", timeout=3.0)
    else:
        screen.notify(
            f"✗ {total_errors} issue(s) across {invalid} hostile(s) — flagged in tree.",
            severity="warning",
            timeout=5.0,
        )