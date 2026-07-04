"""
MonsterLogOverlay: floating monster-log widget for InventoryScreen.

Mirrors `old/game_screens/monster_log_screen.py`, following the same
docked-list-with-detail-panel pattern already proven in `equip_overlay.py`:
  - Lists every hostile the player has slain at least once, built from
    `player_game.enemies_slain` via `tui.services.monster_log_service`.
  - Up / Down navigate the list; the detail panel always shows the
    highlighted hostile's full stat block (stats, attributes, abilities,
    drops) reusing the legacy `format_hostile_summary_full` formatter.
  - Escape closes the overlay.

This overlay is read-only — there is no equip/discard/use action, matching
the legacy screen's behavior (up/down/esc only).

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

from tui.services.monster_log_service import build_slain_hostiles


def _hostile_row_label(hostile: Any, count: int) -> str:
    name = rich_escape(str(getattr(hostile, "name", "?")))
    lvl  = getattr(hostile, "level", "?")
    return f"{name}  [dim](lvl {lvl})[/dim]  [yellow]x{count}[/yellow]"


def _build_hostile_detail(hostile: Any | None) -> str:
    if hostile is None:
        return "[dim]No hostiles slain yet.[/dim]"

    from combat_balancing_simulation.hostile_details_screen import format_hostile_summary_full

    # Reuse the legacy '*'-framed formatter and strip its border characters —
    # the Textual panel already has its own border, so plain text reads cleaner.
    try:
        raw_lines = format_hostile_summary_full(hostile, width=44)
    except Exception:
        raw_lines = []

    lines: list[str] = []
    for ln in raw_lines:
        stripped = ln.strip("*").strip()
        if not stripped or set(stripped) == {"*"}:
            continue
        lines.append(rich_escape(stripped))
    return "\n".join(lines) if lines else "[dim]No details available.[/dim]"


class _HostileRow(ListItem):
    def __init__(self, hostile: Any, count: int) -> None:
        super().__init__(Label(_hostile_row_label(hostile, count)))
        self.hostile = hostile


class MonsterLogOverlay(Widget):
    """
    Floating monster-log viewer docked to the bottom of InventoryScreen.

    Up / Down navigate the list of slain hostiles.  The right-hand panel
    always shows the full stat/ability/drop summary for the highlighted
    entry.  Escape closes the overlay.  There is no edit/action flow — this
    overlay is purely informational, matching `old/game_screens/monster_log_screen.py`.
    """

    can_focus = True

    BINDINGS = [
        Binding("up",     "cursor_up",     "Up",    show=False),
        Binding("down",   "cursor_down",   "Down",  show=False),
        Binding("escape", "request_close", "Close", show=True),
    ]

    DEFAULT_CSS = """
    MonsterLogOverlay {
        layer: overlay;
        dock: bottom;
        width: 100%;
        height: 20;
        background: $surface;
        border-top: solid $accent;
        layout: vertical;
    }

    #ml-header {
        height: 1;
        text-align: center;
        text-style: bold;
        background: $boost;
        padding: 0 1;
    }

    #ml-main-row {
        height: 1fr;
    }

    #ml-list-panel {
        width: 1fr;
        height: 100%;
    }

    #ml-list {
        height: 100%;
    }

    #ml-detail-panel {
        width: 46;
        height: 100%;
        padding: 0 1;
        overflow-y: auto;
        border-left: solid $accent 30%;
    }

    #ml-hint {
        height: 1;
        padding: 0 1;
        color: $text 50%;
        text-align: center;
        border-top: solid $accent 30%;
    }
    """

    def __init__(self, player_game: Any, on_close: Callable[[str | None], None]) -> None:
        super().__init__()
        self._pg       = player_game
        self._on_close = on_close
        self._hostiles: list[Any] = []
        self._counts: dict[str, int] = {}

    # ── compose ───────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        yield Static("── Monster Log ──", id="ml-header")
        with Horizontal(id="ml-main-row"):
            with Vertical(id="ml-list-panel"):
                yield ListView(id="ml-list")
            yield Static("", id="ml-detail-panel")
        yield Static(
            "[dim]▲▼:navigate  Esc:close[/dim]",
            id="ml-hint",
        )

    def on_mount(self) -> None:
        self.add_class("inv-overlay")
        self._hostiles, self._counts = build_slain_hostiles(self._pg)
        self._rebuild_list()
        self.query_one("#ml-list", ListView).focus()

    # ── internal ──────────────────────────────────────────────────────────

    def _rebuild_list(self) -> None:
        lv = self.query_one("#ml-list", ListView)
        lv.clear()
        for hostile in self._hostiles:
            count = self._counts.get(getattr(hostile, "id", None), 0)
            lv.append(_HostileRow(hostile, count))
        self.query_one("#ml-header", Static).update(
            f"── Monster Log ({len(self._hostiles)} entries) ──"
        )
        self._update_detail(self._highlighted_hostile())

    def _highlighted_hostile(self) -> Any | None:
        lv    = self.query_one("#ml-list", ListView)
        child = lv.highlighted_child
        return child.hostile if isinstance(child, _HostileRow) else None

    def _update_detail(self, hostile: Any | None) -> None:
        self.query_one("#ml-detail-panel", Static).update(_build_hostile_detail(hostile))

    # ── events ────────────────────────────────────────────────────────────

    @on(ListView.Highlighted, "#ml-list")
    def _on_highlighted(self, event: ListView.Highlighted) -> None:
        hostile = event.item.hostile if isinstance(event.item, _HostileRow) else None
        self._update_detail(hostile)

    # ── actions ───────────────────────────────────────────────────────────

    def action_cursor_up(self) -> None:
        self.query_one("#ml-list", ListView).action_cursor_up()

    def action_cursor_down(self) -> None:
        self.query_one("#ml-list", ListView).action_cursor_down()

    def action_request_close(self) -> None:
        self._on_close(None)