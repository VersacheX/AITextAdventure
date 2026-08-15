"""
Equipment table population, sorting, filtering, copy, and validation.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from rich.style import Style
from rich.text import Text

from textual.widgets import DataTable, RadioSet, Static

from tui.screens.dev.data_mgmt.handlers._constants import (
    ELEMENT_SYMBOLS,
    STATUS_SYMBOLS,
    EQUIPMENT_CATEGORY,
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

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen

# ── Type / rarity display maps ────────────────────────────────────────────────

_TYPE_ABBR_MAP: dict[str, str] = {
    "weapon":       "WPN",
    "armor · head": "HED",
    "armor · body": "BDY",
    "armor · arms": "ARM",
    "armor · legs": "LEG",
    "armor":        "AMR",
    "accessory":    "ACC",
}

_RARITY_ABBR_MAP: dict[str, str] = {
    "common": "Com", "uncommon": "Unc", "rare": "Rar",
    "superrare": "SR", "notfound": "Not",
}

# ── Equipment table columns ───────────────────────────────────────────────────

_EQUIP_COLUMNS = (
    "Name", "Type", "Lv", "Rarity", "Elem",
    "DMG", "DEF", "CRIT", "TSP", "TEP", "TAP", "TP",
    "Imm", "Res", "Wk", "Err",
)

# ── Balance / error styles ────────────────────────────────────────────────────

_EQUIP_ERROR_STYLE  = ROW_ERROR_STYLE
_EQUIP_NOTICE_STYLE = ROW_NOTICE_STYLE
_EQUIP_STRONG_STYLE = ROW_BLUE_STYLE
_EQUIP_WEAK_STYLE   = ROW_INFO_STYLE

_SORT_COL_MAP: dict[str, str] = {
    "equip-sort-lv":       "level",
    "equip-sort-rarity":   "rarity_rank",
    "equip-sort-dmg":      "damage",
    "equip-sort-def":      "defense",
    "equip-sort-crit":     "crit",
    "equip-sort-tsp":      "tsp",
    "equip-sort-tep":      "tep",
    "equip-sort-tap":      "tap",
    "equip-sort-tp":       "tp",
    "equip-sort-severity": "severity_rank",
}


# ── Row style / error cell helpers ────────────────────────────────────────────

def _equip_row_style(record: Any, rating: str) -> Style:
    """Row tint priority: error > notice > warning > info > balance-strong > balance-weak > default."""
    errors = (record.extras.get("_errors") or []) if record.extras else []
    if any(e.severity == "error"   for e in errors):
        return _EQUIP_ERROR_STYLE
    if any(e.severity == "notice"  for e in errors):
        return _EQUIP_NOTICE_STYLE
    if any(e.severity == "warning" for e in errors):
        return ROW_WARN_STYLE
    if any(e.severity == "info"    for e in errors):
        return ROW_INFO_STYLE
    if rating == "strong":
        return _EQUIP_STRONG_STYLE
    if rating == "weak":
        return _EQUIP_WEAK_STYLE
    return ROW_DEFAULT_STYLE


def _equip_error_cell(record: Any) -> Text:
    """Compact error indicator cell for the equipment table."""
    errors = (record.extras.get("_errors") or []) if record.extras else []
    if not errors:
        return Text("✓", style=ROW_OK_STYLE)
    has_error   = any(e.severity == "error"   for e in errors)
    has_notice  = any(e.severity == "notice"  for e in errors)
    has_warning = any(e.severity == "warning" for e in errors)
    has_info    = any(e.severity == "info"    for e in errors)
    count = len(errors)
    if has_error:
        return Text(f"✗{count}", style=_EQUIP_ERROR_STYLE)
    if has_notice:
        return Text(f"◆{count}", style=_EQUIP_NOTICE_STYLE)
    if has_warning:
        return Text(f"⚠{count}", style=ROW_WARN_STYLE)
    if has_info:
        return Text(f"i{count}", style=ROW_INFO_STYLE)
    return Text(f"⚠{count}", style=ROW_WARN_STYLE)


def _equip_severity_rank(record: Any) -> int:
    errors = (record.extras.get("_errors") or []) if record.extras else []
    if any(e.severity == "error"   for e in errors):
        return 0
    if any(e.severity == "notice"  for e in errors):
        return 1
    if any(e.severity == "warning" for e in errors):
        return 2
    if any(e.severity == "info"    for e in errors):
        return 3
    if errors:
        return 4
    return 5


# ── Filter / sort accessors ───────────────────────────────────────────────────

def get_equipment_sort_col(screen: "DataMgmtScreen") -> str:
    try:
        sort_radio = screen.query_one("#dm-equipment-sort-radio", RadioSet)
        pressed_id = sort_radio.pressed_button.id if sort_radio.pressed_button else "equip-sort-none"
        return _SORT_COL_MAP.get(pressed_id, "")
    except Exception:
        return ""


def get_equipment_type_filter(screen: "DataMgmtScreen") -> str:
    try:
        type_radio = screen.query_one("#dm-equipment-type-radio", RadioSet)
        pressed_id = type_radio.pressed_button.id if type_radio.pressed_button else "equip-type-all"
        if pressed_id == "equip-type-weapon":
            return "weapon"
        elif pressed_id == "equip-type-armor":
            return "armor"
        elif pressed_id == "equip-type-accessory":
            return "accessory"
        return ""
    except Exception:
        return ""


def get_equipment_slot_filter(screen: "DataMgmtScreen") -> str:
    try:
        slot_radio = screen.query_one("#dm-equipment-slot-radio", RadioSet)
        pressed_id = slot_radio.pressed_button.id if slot_radio.pressed_button else "equip-slot-all"
        slot_map = {
            "equip-slot-head": "head",
            "equip-slot-body": "body",
            "equip-slot-arms": "arms",
            "equip-slot-legs": "legs",
        }
        return slot_map.get(pressed_id, "")
    except Exception:
        return ""


# ── Table population ──────────────────────────────────────────────────────────

def _populate_equipment_table(screen: "DataMgmtScreen", records: list) -> None:
    table = screen.query_one("#dm-equipment-table", DataTable)
    table.clear(columns=True)
    for col in _EQUIP_COLUMNS:
        table.add_column(col, key=col)

    for idx, r in enumerate(records):
        x         = r.extras
        rarity    = x.get("rarity", "")
        rar_disp  = _RARITY_ABBR_MAP.get(rarity, rarity[:3].title() if rarity else "—")
        type_abbr = _TYPE_ABBR_MAP.get(x.get("type_label", ""), x.get("type_label", "")[:4].upper() or "—")
        dmg  = str(x["damage"])    if x.get("damage")  else "—"
        defn = str(x["defense"])   if x.get("defense") else "—"
        crit = f"{x['crit']:.1f}" if x.get("crit")    else "—"
        tsp  = str(x.get("tsp", 0))
        tep  = str(x.get("tep", 0))
        tap_val = x.get("tap", 0)
        tap  = str(tap_val) if tap_val != 0 else "—"
        tp   = str(x.get("tp",  0))
        elem = x.get("elements", "") or "—"

        imm_raw = x.get("immunities")  or []
        res_raw = x.get("resistances") or []
        wk_raw  = x.get("weaknesses")  or []

        def _fmt_mixed(items: list[str]) -> str:
            if not items:
                return "—"
            parts = []
            for item in items:
                if item in STATUS_SYMBOLS:
                    parts.append(STATUS_SYMBOLS[item])
                elif item in ELEMENT_SYMBOLS:
                    parts.append(ELEMENT_SYMBOLS[item])
                else:
                    parts.append(f"[{item[:3]}]")
            return " ".join(parts)

        imm_disp = _fmt_mixed(imm_raw)
        res_disp = _fmt_mixed(res_raw)
        wk_disp  = _fmt_mixed(wk_raw)

        rating    = (r.extras.get("_balance_rating") or "") if r.extras else ""
        row_style = _equip_row_style(r, rating)

        table.add_row(
            Text(r.name,                  style=row_style),
            Text(type_abbr,               style=row_style),
            Text(str(x.get("level", 0)), style=row_style),
            Text(rar_disp,                style=row_style),
            Text(elem,                    style=row_style),
            Text(dmg,                     style=row_style),
            Text(defn,                    style=row_style),
            Text(crit,                    style=row_style),
            Text(tsp,                     style=row_style),
            Text(tep,                     style=row_style),
            Text(tap,                     style=row_style),
            Text(tp,                      style=row_style),
            Text(imm_disp,                style=row_style),
            Text(res_disp,                style=row_style),
            Text(wk_disp,                 style=row_style),
            _equip_error_cell(r),
            key=str(idx),
        )


# ── List rebuild (equipment branch) ──────────────────────────────────────────

def rebuild_list_for_screen(screen: "DataMgmtScreen") -> None:
    """Rebuild the equipment DataTable only. Called from core.rebuild_list_for_screen."""
    from tui.services.dev.dataservices.catalog import filter_equipment_records  # noqa: PLC0415

    records  = filter_equipment_records(
        get_equipment_type_filter(screen),
        get_equipment_slot_filter(screen),
    )
    sort_col = get_equipment_sort_col(screen)
    if sort_col:
        sort_asc = getattr(screen, "_equipment_sort_asc", True)
        if sort_col == "severity_rank":
            records = sorted(
                records,
                key=lambda r: (_equip_severity_rank(r), r.name.lower()),
                reverse=not sort_asc,
            )
        else:
            records = sorted(
                records,
                key=lambda r: r.extras.get(sort_col, 0),
                reverse=not sort_asc,
            )
    screen._last_filtered = records
    _populate_equipment_table(screen, records)
    screen.query_one("#dm-status", Static).update(f"{len(records)} record(s)")


# ── Copy ──────────────────────────────────────────────────────────────────────

def copy_equipment(screen: "DataMgmtScreen") -> str:
    records = screen._last_filtered or []
    lines = []
    for r in records:
        x       = r.extras or {}
        errors  = x.get("_errors") or []
        rating  = x.get("_balance_rating") or ""
        if any(e.severity == "error"  for e in errors):
            tag = "  ·  [ERROR]"
        elif any(e.severity == "notice" for e in errors):
            tag = "  ·  [NOTICE]"
        elif any(e.severity == "warning" for e in errors):
            tag = "  ·  [WARNING]"
        elif any(e.severity == "info" for e in errors):
            tag = "  ·  [INFO]"
        elif rating == "strong":
            tag = "  ·  [STRONG]"
        elif rating == "weak":
            tag = "  ·  [WEAK]"
        else:
            tag = ""
        lines.append(f"{r.name}  {r.subtitle}{tag}")
    return "\n".join(lines)


# ── Validate ──────────────────────────────────────────────────────────────────

def validate_equipment_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.services.dev.dataservices.equipment_validator import validate_equipment  # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import (                               # noqa: PLC0415
        get_timeline_tree,
        filter_equipment_records as _fer,
    )
    import game.constants as const  # noqa: PLC0415

    all_equipment   = _fer()
    timeline_groups = get_timeline_tree()
    summary         = validate_equipment(all_equipment, timeline_groups, const=const)

    rebuild_list_for_screen(screen)

    total_errors = summary.get("total_errors", 0)
    invalid      = summary.get("invalid", 0)
    by_code      = summary.get("by_code", {})

    if total_errors == 0:
        screen.notify("✓ Equipment integrity OK — all items are reachable.", timeout=3.0)
    else:
        parts = []
        if by_code.get("EQUIPMENT_NOT_FOUND_IN_TIMELINE"):
            parts.append(f"{by_code['EQUIPMENT_NOT_FOUND_IN_TIMELINE']} unreachable")
        if by_code.get("EQUIPMENT_TP_LOW"):
            parts.append(f"{by_code['EQUIPMENT_TP_LOW']} low-TP")
        if by_code.get("EQUIPMENT_TP_HIGH"):
            parts.append(f"{by_code['EQUIPMENT_TP_HIGH']} high-TP")
        detail = ", ".join(parts) if parts else f"{invalid} issue(s)"
        screen.notify(
            f"✗ {total_errors} equipment issue(s): {detail} — flagged in table.",
            severity="warning",
            timeout=5.0,
        )