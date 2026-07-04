"""
NPCLogOverlay: floating NPC-log widget for InventoryScreen.

Mirrors `old/game_screens/npc_log_screen.py`, following the same
docked-list-with-detail-panel pattern already proven in `equip_overlay.py`
and `monster_log_overlay.py`:
  - Lists every NPC the player has met (`npc.met`), from `player_game.npcs`.
  - Up / Down navigate the list; the detail panel shows the highlighted
    NPC's known location (via `player_game.get_npc_details()`) and
    word-wrapped description, with a task-indicator marker when the NPC
    has an associated incomplete Meet/Deliver task.
  - Escape closes the overlay.

This overlay is read-only, matching the legacy screen's up/down/esc-only
interaction model. Callers must only open this overlay when
`not player_game.npc_log_locked` — see `InventoryScreen._open_npc_log_overlay`.

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


def _known_npcs(player_game: Any) -> list:
    return [n for n in (getattr(player_game, "npcs", None) or []) if getattr(n, "met", False)]


def _npc_row_label(npc: Any, has_tasks: bool) -> str:
    name = rich_escape(str(getattr(npc, "name", "NPC")))
    marker = "  [yellow]★[/yellow]" if has_tasks else ""
    return f"{name}{marker}"


def _build_npc_detail(player_game: Any, npc: Any | None) -> str:
    if npc is None:
        return "[dim]No NPCs met yet.[/dim]"

    lines: list[str] = []
    name = rich_escape(str(getattr(npc, "name", "NPC")))
    lines.append(f"[bold]{name}[/bold]")
    lines.append("")

    try:
        details = player_game.get_npc_details(npc) or {}
    except Exception:
        details = {}
    has_tasks = bool(details.get("has_tasks", False))
    location_description = details.get("location_description", "Unknown")
    position = getattr(npc, "position", None)
    loc_line = f"Known Location: {rich_escape(str(location_description))}"
    if position:
        loc_line += f" {rich_escape(str(position))}"
    if has_tasks:
        loc_line += "  [yellow]★ has task[/yellow]"
    lines.append(loc_line)
    lines.append("")

    desc = rich_escape(str(getattr(npc, "description", "") or ""))
    lines.append("[dim]── Description ──[/dim]")
    lines.append(desc if desc else "[dim]No description.[/dim]")

    return "\n".join(lines)


class _NPCRow(ListItem):
    def __init__(self, npc: Any, has_tasks: bool) -> None:
        super().__init__(Label(_npc_row_label(npc, has_tasks)))
        self.npc = npc


class NPCLogOverlay(Widget):
    """
    Floating NPC-log viewer docked to the bottom of InventoryScreen.

    Up / Down navigate the list of met NPCs.  The right-hand panel shows
    the highlighted NPC's known location and description.  Escape closes
    the overlay.  Purely informational — no edit/action flow, matching
    `old/game_screens/npc_log_screen.py`.

    Only open this overlay when `not player_game.npc_log_locked`.
    """

    can_focus = True

    BINDINGS = [
        Binding("up",     "cursor_up",     "Up",    show=False),
        Binding("down",   "cursor_down",   "Down",  show=False),
        Binding("escape", "request_close", "Close", show=True),
    ]

    DEFAULT_CSS = """
    NPCLogOverlay {
        layer: overlay;
        dock: bottom;
        width: 100%;
        height: 20;
        background: $surface;
        border-top: solid $accent;
        layout: vertical;
    }

    #npc-header {
        height: 1;
        text-align: center;
        text-style: bold;
        background: $boost;
        padding: 0 1;
    }

    #npc-main-row {
        height: 1fr;
    }

    #npc-list-panel {
        width: 1fr;
        height: 100%;
    }

    #npc-list {
        height: 100%;
    }

    #npc-detail-panel {
        width: 46;
        height: 100%;
        padding: 0 1;
        overflow-y: auto;
        border-left: solid $accent 30%;
    }

    #npc-hint {
        height: 1;
        padding: 0 1;
        color: $text 50%;
        text-align: center;
        border-top: solid $accent 30%;
    }
    """

    def __init__(self, player_game: Any, on_close: Callable[[str | None], None]) -> None:
        super().__init__()
        self._pg = player_game
        self._on_close = on_close

    # ── compose ───────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        yield Static("── NPC Log ──", id="npc-header")
        with Horizontal(id="npc-main-row"):
            with Vertical(id="npc-list-panel"):
                yield ListView(id="npc-list")
            yield Static("", id="npc-detail-panel")
        yield Static(
            "[dim]▲▼:navigate  Esc:close[/dim]",
            id="npc-hint",
        )

    def on_mount(self) -> None:
        self.add_class("inv-overlay")
        self._rebuild_list()
        self.query_one("#npc-list", ListView).focus()

    # ── internal ──────────────────────────────────────────────────────────

    def _rebuild_list(self) -> None:
        lv = self.query_one("#npc-list", ListView)
        lv.clear()
        known = _known_npcs(self._pg)
        for npc in known:
            try:
                has_tasks = bool((self._pg.get_npc_details(npc) or {}).get("has_tasks", False))
            except Exception:
                has_tasks = False
            lv.append(_NPCRow(npc, has_tasks))
        self.query_one("#npc-header", Static).update(f"── NPC Log ({len(known)} entries) ──")
        self._update_detail(self._highlighted_npc())

    def _highlighted_npc(self) -> Any | None:
        lv    = self.query_one("#npc-list", ListView)
        child = lv.highlighted_child
        return child.npc if isinstance(child, _NPCRow) else None

    def _update_detail(self, npc: Any | None) -> None:
        self.query_one("#npc-detail-panel", Static).update(_build_npc_detail(self._pg, npc))

    # ── events ────────────────────────────────────────────────────────────

    @on(ListView.Highlighted, "#npc-list")
    def _on_highlighted(self, event: ListView.Highlighted) -> None:
        npc = event.item.npc if isinstance(event.item, _NPCRow) else None
        self._update_detail(npc)

    # ── actions ───────────────────────────────────────────────────────────

    def action_cursor_up(self) -> None:
        self.query_one("#npc-list", ListView).action_cursor_up()

    def action_cursor_down(self) -> None:
        self.query_one("#npc-list", ListView).action_cursor_down()

    def action_request_close(self) -> None:
        self._on_close(None)