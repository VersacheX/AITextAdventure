"""
CityLogOverlay: floating visited-cities log for InventoryScreen.

Lists every city the player has visited (city.visited == True) sourced
directly from pg.get_cities(), which returns all child_city objects from
the generated regions.  The right panel shows the city's description and
the unique buildings found in its tile map.

Mirrors the structure of npc_log_overlay.py and monster_log_overlay.py.
The CSS class "inv-overlay" is added in on_mount so InventoryScreen can
remove it generically.
"""
from __future__ import annotations

from typing import Any, Callable

from rich.markup import escape as rich_escape
from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, ScrollableContainer, Vertical
from textual.widget import Widget
from textual.widgets import Label, ListItem, ListView, Static


# ── pure helpers ──────────────────────────────────────────────────────────────

def _visited_cities(pg: Any) -> list:
    """Return City objects the player has visited, sorted by display_name."""
    try:
        cities = pg.get_cities() or []
    except Exception:
        return []
    visited = [c for c in cities if getattr(c, "visited", False) is True]
    visited.sort(key=lambda c: str(getattr(c, "display_name", "") or ""))
    return visited


def _city_row_label(city: Any) -> str:
    return rich_escape(str(getattr(city, "display_name", None) or getattr(city, "city_name", "City")))


def _collect_buildings(city: Any) -> list[str]:
    """Return deduplicated building display strings from the city tile map."""
    seen: set[str] = set()
    results: list[str] = []
    tiles = getattr(city, "tiles", {}) or {}
    for tile in tiles.values():
        bdef = getattr(tile, "building", None)
        if not bdef:
            continue
        if isinstance(bdef, dict):
            bname   = bdef.get("display_name") or bdef.get("name") or ""
            bsymbol = bdef.get("symbol", "")
        else:
            bname   = str(bdef)
            bsymbol = ""
        bname = bname.strip()
        if not bname or bname in seen:
            continue
        seen.add(bname)
        entry = rich_escape(bname)
        if bsymbol:
            entry = f"{rich_escape(str(bsymbol))} {entry}"
        results.append(entry)
    return results


_DEFAULT_DESC = "No description provided."


def _build_city_detail(city: Any | None) -> str:
    if city is None:
        return "[dim]No cities visited yet.[/dim]"

    name = str(getattr(city, "display_name", None) or getattr(city, "city_name", "Unknown"))
    lines: list[str] = [
        f"[bold]{rich_escape(name)}[/bold]",
        "",
    ]

    desc = str(getattr(city, "description", "") or "").strip()
    if desc and desc != _DEFAULT_DESC:
        lines.append(rich_escape(desc))
    else:
        lines.append(f"[dim]{_DEFAULT_DESC}[/dim]")
    lines.append("")

    buildings = _collect_buildings(city)
    if buildings:
        lines.append("[dim]── Buildings ──[/dim]")
        for b in buildings[:30]:
            lines.append(f"  {b}")
    else:
        lines.append("[dim](No buildings recorded)[/dim]")

    return "\n".join(lines)


# ── list item ─────────────────────────────────────────────────────────────────

class _CityRow(ListItem):
    def __init__(self, city: Any) -> None:
        super().__init__(Label(_city_row_label(city)))
        self.city = city


# ── overlay widget ────────────────────────────────────────────────────────────

class CityLogOverlay(Widget):
    """
    Floating city log viewer docked to the bottom of InventoryScreen.

    Lists every visited city from pg.get_cities().  The right panel shows
    the city's description and known buildings.  Read-only; Escape closes.
    The CSS class "inv-overlay" lets InventoryScreen close it generically.
    """

    can_focus = True

    BINDINGS = [
        Binding("up",     "cursor_up",     "Up",    show=False),
        Binding("down",   "cursor_down",   "Down",  show=False),
        Binding("escape", "request_close", "Close", show=True),
    ]

    DEFAULT_CSS = """
    CityLogOverlay {
        layer: overlay;
        dock: bottom;
        width: 100%;
        height: 20;
        background: $surface;
        border-top: solid $accent;
        layout: vertical;
    }

    #city-header {
        height: 1;
        text-align: center;
        text-style: bold;
        background: $boost;
        padding: 0 1;
    }

    #city-main-row {
        height: 1fr;
    }

    #city-list-panel {
        width: 1fr;
        height: 100%;
    }

    #city-list {
        height: 100%;
    }

    #city-detail-panel {
        width: 65;
        height: 100%;
        padding: 0;
        border-left: solid $accent 30%;
    }

    #city-detail-text {
        height: auto;
        padding: 0 1;
    }

    #city-hint {
        height: 1;
        padding: 0 1;
        color: $text 50%;
        text-align: center;
        border-top: solid $accent 30%;
    }
    """

    def __init__(self, pg: Any, on_close: Callable[[str | None], None]) -> None:
        super().__init__()
        self._pg       = pg
        self._on_close = on_close

    # ── compose ───────────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        yield Static("── City Log ──", id="city-header")
        with Horizontal(id="city-main-row"):
            with Vertical(id="city-list-panel"):
                yield ListView(id="city-list")
            with ScrollableContainer(id="city-detail-panel"):
                yield Static("", id="city-detail-text")
        yield Static("[dim]▲▼:navigate  Esc:close[/dim]", id="city-hint")

    def on_mount(self) -> None:
        self.add_class("inv-overlay")
        self._rebuild_list()
        self.query_one("#city-list", ListView).focus()

    # ── internal ──────────────────────────────────────────────────────────────

    def _rebuild_list(self) -> None:
        lv     = self.query_one("#city-list", ListView)
        lv.clear()
        cities = _visited_cities(self._pg)
        for city in cities:
            lv.append(_CityRow(city))
        self.query_one("#city-header", Static).update(
            f"── City Log ({len(cities)} visited) ──"
        )
        self._update_detail(self._highlighted_city())

    def _highlighted_city(self) -> Any | None:
        lv    = self.query_one("#city-list", ListView)
        child = lv.highlighted_child
        return child.city if isinstance(child, _CityRow) else None

    def _update_detail(self, city: Any | None) -> None:
        self.query_one("#city-detail-text", Static).update(
            _build_city_detail(city)
        )

    # ── events ────────────────────────────────────────────────────────────────

    @on(ListView.Highlighted, "#city-list")
    def _on_highlighted(self, event: ListView.Highlighted) -> None:
        city = event.item.city if isinstance(event.item, _CityRow) else None
        self._update_detail(city)

    # ── actions ───────────────────────────────────────────────────────────────

    def action_cursor_up(self) -> None:
        self.query_one("#city-list", ListView).action_cursor_up()

    def action_cursor_down(self) -> None:
        self.query_one("#city-list", ListView).action_cursor_down()

    def action_request_close(self) -> None:
        self._on_close(None)