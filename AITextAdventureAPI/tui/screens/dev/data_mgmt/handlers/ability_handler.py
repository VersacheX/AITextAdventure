"""
Ability table population, sorting, rebuild, copy, and validation.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from rich.text import Text

from textual.widgets import DataTable, RadioSet, Static

from tui.screens.dev.data_mgmt.handlers._constants import (
    ROW_DEFAULT_STYLE,
    ROW_ERROR_STYLE,
    ROW_WARN_STYLE,
    ROW_NOTICE_STYLE,
    ROW_BLUE_STYLE,
    ROW_INFO_STYLE,
    ROW_OK_STYLE,
    fmt_elem_list as _fmt_elem_list,
    fmt_status_list as _fmt_status_list,
)
from tui.services.dev.dataservices import AbilityNode

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen

# ── Columns / sort keys ───────────────────────────────────────────────────────

_ABILITY_COLUMNS = ["Name", "ID", "Level", "Type", "Elements", "AP", "Power", "Effect", "AOE", "Statuses", "Errors"]

_ABILITY_SORT_KEYS: dict[str, str] = {
    "ability-sort-type":     "ability_type",
    "ability-sort-lv":       "level",
    "ability-sort-effect":   "effect",
    "ability-sort-name":     "name",
    "ability-sort-severity": "severity_rank",
}

_ABILITY_BLUE_NOTICE_CODES  = frozenset({"ABILITY_BALANCE_STRONG"})
_ABILITY_MGNTA_NOTICE_CODES = frozenset({"ABILITY_BALANCE_WEAK"})  # info only


# ── Row style / error cell ────────────────────────────────────────────────────

def _ability_row_style(errors: list):
    if not errors:
        return ROW_DEFAULT_STYLE
    if any(e.severity == "error"   for e in errors):
        return ROW_ERROR_STYLE
    if any(e.severity == "warning" for e in errors):
        return ROW_WARN_STYLE
    if any(e.severity == "notice" and e.code in _ABILITY_BLUE_NOTICE_CODES for e in errors):
        return ROW_BLUE_STYLE
    if any(e.severity == "notice" for e in errors):
        return ROW_NOTICE_STYLE
    if any(e.severity == "info"   for e in errors):
        return ROW_INFO_STYLE
    return ROW_DEFAULT_STYLE


def _ability_error_cell(errors: list) -> Text:
    if not errors:
        return Text("✓", style=ROW_OK_STYLE)
    has_error       = any(e.severity == "error"   for e in errors)
    has_warning     = any(e.severity == "warning" for e in errors)
    has_blue_notice = any(e.severity == "notice" and e.code in _ABILITY_BLUE_NOTICE_CODES for e in errors)
    has_notice      = any(e.severity == "notice"  for e in errors)
    has_info        = any(e.severity == "info"    for e in errors)
    count = len(errors)
    if has_error:
        return Text(f"✗ {count}", style=ROW_ERROR_STYLE)
    if has_warning:
        return Text(f"⚠ {count}", style=ROW_WARN_STYLE)
    if has_blue_notice:
        return Text(f"● {count}", style=ROW_BLUE_STYLE)
    if has_notice:
        return Text(f"● {count}", style=ROW_NOTICE_STYLE)
    if has_info:
        return Text(f"• {count}", style=ROW_INFO_STYLE)
    return Text(f"• {count}")


def _ability_severity_rank(node: AbilityNode) -> int:
    if any(e.severity == "error"   for e in node.errors):
        return 0
    if any(e.severity == "warning" for e in node.errors):
        return 1
    if any(e.severity == "notice" and e.code in _ABILITY_BLUE_NOTICE_CODES for e in node.errors):
        return 2
    if any(e.severity == "notice" for e in node.errors):
        return 3
    if any(e.severity == "info"   for e in node.errors):
        return 4
    if node.errors:
        return 5
    return 6


# ── Table population ──────────────────────────────────────────────────────────

def _populate_ability_table(screen: "DataMgmtScreen", nodes: list) -> None:
    sort_asc   = getattr(screen, "_ability_sort_asc", True)
    sort_radio = None
    try:
        sort_radio = screen.query_one("#dm-ability-sort-radio", RadioSet)
    except Exception:
        pass

    sort_key_id = ""
    if sort_radio and sort_radio.pressed_button:
        sort_key_id = sort_radio.pressed_button.id or ""
    sort_col = _ABILITY_SORT_KEYS.get(sort_key_id, "")

    def _sort_key(n: AbilityNode):
        sev = _ability_severity_rank(n)
        if sort_col == "ability_type":
            primary = n.ability_type.lower()
        elif sort_col == "level":
            primary = n.level
        elif sort_col == "effect":
            primary = str(n.record.extras.get("_seed", {}).get("effect", "") or "").lower()
        elif sort_col == "name":
            primary = n.label.lower()
        elif sort_col == "severity_rank":
            primary = sev
        else:
            primary = n.ability_type.lower()
        return (primary, sev, n.label.lower())

    valid_nodes  = [n for n in nodes if isinstance(n, AbilityNode)]
    sorted_nodes = sorted(valid_nodes, key=_sort_key, reverse=not sort_asc)
    screen._ability_flat_nodes = sorted_nodes

    table: DataTable = screen.query_one("#dm-ability-table", DataTable)
    table.clear(columns=True)
    for col in _ABILITY_COLUMNS:
        table.add_column(col, key=col)

    for idx, node in enumerate(sorted_nodes):
        seed        = node.record.extras.get("_seed") or {}
        elements    = seed.get("elements") or []
        status_keys = seed.get("status_keys") or []
        effect      = str(seed.get("effect", "") or "")
        base_power  = int(seed.get("base_power", 0) or 0)
        ap_cost     = int(seed.get("ap_cost", 0) or 0)
        can_aoe     = "✓" if seed.get("can_aoe") else ""
        errors      = node.errors or []
        row_style   = _ability_row_style(errors)
        ability_id  = node.ability_id[:20]

        table.add_row(
            Text(node.label,                     style=row_style),
            Text(ability_id,                     style=row_style),
            Text(str(node.level),                style=row_style),
            Text(node.ability_type,              style=row_style),
            Text(_fmt_elem_list(elements),       style=row_style),
            Text(str(ap_cost),                   style=row_style),
            Text(str(base_power),                style=row_style),
            Text(effect,                         style=row_style),
            Text(can_aoe,                        style=row_style),
            Text(_fmt_status_list(status_keys),  style=row_style),
            _ability_error_cell(errors),
            key=str(idx),
        )


# ── Rebuild ───────────────────────────────────────────────────────────────────

def rebuild_ability_tree_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.screens.dev.data_mgmt.treehandlers.ability_handler import rebuild_ability_tree  # noqa: PLC0415
    from tui.services.dev.dataservices.ability_service import _flat_ability_nodes             # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import get_ability_tree                        # noqa: PLC0415
    from tui.screens.dev.data_mgmt.detail_panel import update_detail_for_ability_group       # noqa: PLC0415
    from textual.widgets import Tree                                                          # noqa: PLC0415

    if not screen._loaded:
        return
    query = ""
    try:
        query = screen.query_one("#dm-ability-filter", __import__("textual.widgets", fromlist=["Input"]).Input).value.strip()
    except Exception:
        pass

    tree = screen.query_one("#dm-ability-tree", Tree)
    total, filtered = rebuild_ability_tree(
        tree,
        query=query,
        user_expanded=screen._ability_user_expanded,
        user_collapsed=screen._ability_user_collapsed,
    )
    screen._last_ability_filtered = filtered

    nodes = _flat_ability_nodes(filtered if filtered is not None else get_ability_tree())
    _populate_ability_table(screen, nodes)

    screen.query_one("#dm-status", Static).update(f"{total} ability(s)")
    update_detail_for_ability_group(screen, [])


# ── Copy ──────────────────────────────────────────────────────────────────────

def copy_abilities(screen: "DataMgmtScreen") -> str:
    nodes  = getattr(screen, "_ability_flat_nodes", [])
    header = "\t".join(_ABILITY_COLUMNS + ["Messages"])
    rows   = [header]
    for node in nodes:
        if not isinstance(node, AbilityNode):
            continue
        seed        = node.record.extras.get("_seed") or {}
        elements    = seed.get("elements") or []
        status_keys = seed.get("status_keys") or []
        effect      = str(seed.get("effect", "") or "")
        can_aoe     = "yes" if seed.get("can_aoe") else "no"
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
            node.ability_id[:20],
            str(node.level),
            node.ability_type,
            _fmt_elem_list(elements),
            effect,
            can_aoe,
            _fmt_status_list(status_keys),
            err_cell,
            messages,
        ]))
    return "\n".join(rows)


# ── Validate ──────────────────────────────────────────────────────────────────

def validate_abilities_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.services.dev.dataservices.ability_validator import validate_ability_tree  # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import get_ability_tree                 # noqa: PLC0415

    tree    = get_ability_tree()
    summary = validate_ability_tree(tree)

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