"""
AreaLogOverlay: floating area / city log for InventoryScreen.

Shows every visited region/city the player has seen, with its description
and a list of notable buildings (name + symbol).  Mirrors the pattern from
npc_log_overlay.py and monster_log_overlay.py.

The old `area_log_screen.py` was never implemented (0 bytes).  This is the
first implementation.

Data source
───────────
`player_game.world_tiles` contains all generated tiles.  Each unique
(region, city) pair that has `area.visited == True` is surfaced here.
Building names and symbols come from the building definition dict stored on
the tile.  We iterate the unique active areas via
`player_game.get_region_and_active_area_for_position()`.

The CSS class "inv-overlay" is added in on_mount so InventoryScreen can
query and remove any open overlay generically.
"""
from __future__ import annotations

from typing import Any, Callable

from rich.markup import escape as rich_escape
from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Label, ListItem, ListView, Static


# ── pure data helpers ─────────────────────────────────────────────────────────

def _collect_visited_areas(pg: Any) -> list[dict]:
    """Return a list of area info dicts for every unique visited area."""
    seen_ids: set[str] = set()
    results: list[dict] = []

    world_tiles = getattr(pg, "world_tiles", {}) or {}
    for (x, y) in world_tiles:
        try:
            region, area = pg.get_region_and_active_area_for_position((x, y))
        except Exception:
            continue
        if area is None:
            continue
        if not getattr(area, "visited", False):
            continue

        # Deduplicate by a stable area id string
        try:
            area_id = str(getattr(area, "city_name", None) or getattr(area, "region_name", id(area)))
            region_id = str(getattr(region, "region_name", "")) if region else ""
            uid = f"{region_id}::{area_id}"
        except Exception:
            uid = str(id(area))

        if uid in seen_ids:
            continue
        seen_ids.add(uid)

        name        = getattr(area, "display_name", None) or getattr(area, "city_name", None) or getattr(area, "region_name", "Unknown")
        description = getattr(area, "description", "") or ""
        is_city     = callable(getattr(area, "isCity", None)) and area.isCity()
        area_type   = "City" if is_city else "Region"

        # Collect unique building names/symbols from tiles
        buildings: list[str] = []
        seen_bldgs: set[str] = set()
        tiles = getattr(area, "tiles", {}) or {}
        for tile in tiles.values():
            bdef = getattr(tile, "building", None)
            if not bdef:
                continue
            if isinstance(bdef, dict):
                bname   = bdef.get("display_name") or bdef.get("name", "")
                bsymbol = bdef.get("symbol", "")
            else:
                bname   = str(bdef)
                bsymbol = ""
            if bname and bname not in seen_bldgs:
                seen_bldgs.add(bname)
                entry = rich_escape(str(bname))
                if bsymbol:
                    entry = f"{rich_escape(str(bsymbol))} {entry}"
                buildings.append(entry)

        results.append({
            "uid":         uid,
            "name":        str(name),
            "type":        area_type,
            "description": str(description),
            "buildings":   buildings,
        })

    results.sort(key=lambda r: r["name"])
    return results


def _build_area_detail(entry: dict | None) -> str:
    if entry is None:
        return "[dim]No areas visited yet.[/dim]"
    lines: list[str] = [
        f"[bold]{rich_escape(entry['name'])}[/bold]  [dim]({entry['type']})[/dim]",
        "",
    ]
    desc = entry.get("description", "").strip()
    if desc:
        lines.append(rich_escape(desc))
        lines.append("")
    buildings = entry.get("buildings") or []
    if buildings:
        lines.append("[dim]── Buildings ──[/dim]")
        for b in buildings[:20]:
            lines.append(f"  {b}")
    else:
        lines.append("[dim](No buildings recorded)[/dim]")
    return "\n".join(lines)


# ── list item ─────────────────────────────────────────────────────────────────

class _AreaRow(ListItem):
    def __init__(self, entry: dict) -> None:
        label = f"{rich_escape(entry['name'])}  [dim]{entry['type']}[/dim]"
        super().__init__(Label(label))
        self.entry = entry


# ── overlay widget ────────────────────────────────────────────────────────────

class AreaLogOverlay(Widget):
    """
    Floating area/city log viewer docked to the bottom of InventoryScreen.

    Lists every visited region/city.  The right panel shows the area's
    description and known buildings.  Read-only; Escape closes.
    """

    can_focus = True

    BINDINGS = [
        Binding("up",     "cursor_up",     "Up",    show=False),
        Binding("down",   "cursor_down",   "Down",  show=False),
        Binding("escape", "request_close", "Close", show=True),
    ]

    DEFAULT_CSS = """
    AreaLogOverlay {
        layer: overlay;
        dock: bottom;
        width: 100%;
        height: 20;
        background: $surface;
        border-top: solid $accent;
        layout: vertical;
    }

    #area-header {
        height: 1;
        text-align: center;
        text-style: bold;
        background: $boost;
        padding: 0 1;
    }

    #area-main-row {
        height: 1fr;
    }

    #area-list {
        width: 1fr;
        height: 100%;
        border-right: solid $accent 30%;
    }

    #area-detail {
        width: 2fr;
        height: 100%;
        padding: 1;
        overflow-y: auto;
    }
    """

    def __init__(self, pg: Any, on_close: Callable[[str | None], None]) -> None:
        super().__init__()
        self._pg       = pg
        self._on_close = on_close
        self._areas: list[dict] = []

    def on_mount(self) -> None:
        self.add_class("inv-overlay")
        self._areas = _collect_visited_areas(self._pg)
        lv = self.query_one("#area-list", ListView)
        for entry in self._areas:
            lv.append(_AreaRow(entry))
        if self._areas:
            self._update_detail(self._areas[0])

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Static("── Area Log ──", id="area-header")
            with Horizontal(id="area-main-row"):
                yield ListView(id="area-list")
                yield Static("[dim]Loading…[/dim]", id="area-detail")

    # ── navigation ────────────────────────────────────────────────────────────

    def action_cursor_up(self) -> None:
        try:
            self.query_one("#area-list", ListView).action_scroll_up()
        except Exception:
            pass

    def action_cursor_down(self) -> None:
        try:
            self.query_one("#area-list", ListView).action_scroll_down()
        except Exception:
            pass

    @on(ListView.Highlighted, "#area-list")
    def _on_highlighted(self, event: ListView.Highlighted) -> None:
        if isinstance(event.item, _AreaRow):
            self._update_detail(event.item.entry)

    def _update_detail(self, entry: dict | None) -> None:
        try:
            self.query_one("#area-detail", Static).update(_build_area_detail(entry))
        except Exception:
            pass

    # ── close ─────────────────────────────────────────────────────────────────

    def action_request_close(self) -> None:
        self.remove()
        self._on_close(None)