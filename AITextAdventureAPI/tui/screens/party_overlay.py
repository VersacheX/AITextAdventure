"""
PartyOverlay: floating party-management widget for InventoryScreen.

Mirrors `old/game_screens/select_party_screen.py`.

Layout
──────
  ┌──────────────── Party ──────────────────┐
  │  Active party boxes: [Name] [Name]      │
  ├─────────────────────────────────────────┤
  │  ★ Alice        Lv.5  HP:80/80         │  ← in party
  │    Bob          Lv.3  HP:60/60         │
  │  > ★ Carol      Lv.4  HP:70/70 ◄      │  ← selected
  └─────────────────────────────────────────┘

Enter / click toggles the highlighted character into/out of the active party.
Escape closes.

The CSS class "inv-overlay" is added in on_mount so InventoryScreen's
_close_overlay() removes it generically.
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


# ── helpers ──────────────────────────────────────────────────────────────────

def _is_in_party(pg: Any, char: Any) -> bool:
    try:
        active = pg.get_active_party() or []
        char_uuid = getattr(char, "_uuid", None)
        return any(getattr(a, "_uuid", None) == char_uuid for a in active)
    except Exception:
        return False


def _char_label(pg: Any, char: Any) -> str:
    name    = rich_escape(str(getattr(char, "name", "Character")))
    level   = getattr(char, "level", 0)
    cur_hp  = getattr(char, "current_hp", 0)
    max_hp  = getattr(char, "max_hp", 0)
    star    = "[yellow]★[/yellow] " if _is_in_party(pg, char) else "  "
    return f"{star}{name}  [dim]Lv.{level}  HP:{cur_hp}/{max_hp}[/dim]"


def _build_active_boxes(pg: Any) -> str:
    try:
        active = pg.get_active_party() or []
    except Exception:
        active = []
    if not active:
        return "[dim](No active party members)[/dim]"
    parts = [
        f"\\[[bold]{rich_escape(str(getattr(a, 'name', '?')))}[/bold]]"
        for a in active
    ]
    return "  ".join(parts)


# ── list item ─────────────────────────────────────────────────────────────────

class _CharRow(ListItem):
    def __init__(self, pg: Any, char: Any) -> None:
        super().__init__(Label(_char_label(pg, char)))
        self.char = char
        self._pg  = pg

    def refresh_label(self) -> None:
        try:
            self.query_one(Label).update(_char_label(self._pg, self.char))
        except Exception:
            pass


# ── overlay widget ────────────────────────────────────────────────────────────

class PartyOverlay(Widget):
    """
    Floating party management overlay for InventoryScreen.

    Enter or clicking a row toggles that character in/out of the active party.
    Escape closes.  The CSS class "inv-overlay" lets InventoryScreen close it
    generically.
    """

    can_focus = True

    BINDINGS = [
        Binding("escape", "request_close", "Close", show=True),
    ]

    DEFAULT_CSS = """
    PartyOverlay {
        layer: overlay;
        dock: bottom;
        width: 100%;
        height: 22;
        background: $surface;
        border-top: solid $accent;
        layout: vertical;
    }

    #party-header {
        height: 1;
        text-align: center;
        text-style: bold;
        background: $boost;
    }

    #party-active-row {
        height: 3;
        padding: 0 2;
        border-bottom: solid $accent 30%;
        content-align: left middle;
    }

    #party-main-row {
        height: 1fr;
    }

    #party-list {
        width: 1fr;
        height: 100%;
    }

    #party-detail {
        width: 30;
        height: 100%;
        border-left: solid $accent 30%;
        padding: 1;
    }

    #party-hint {
        height: 1;
        text-align: center;
        background: $panel;
        color: $text 60%;
        padding: 0 1;
    }
    """

    def __init__(self, pg: Any, on_close: Callable[[str | None], None]) -> None:
        super().__init__()
        self._pg       = pg
        self._on_close = on_close

    def on_mount(self) -> None:
        self.add_class("inv-overlay")

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Static("── Party Management ──", id="party-header")
            yield Static(_build_active_boxes(self._pg), id="party-active-row")
            with Horizontal(id="party-main-row"):
                with ListView(id="party-list"):
                    for char in (getattr(self._pg, "characters", []) or []):
                        yield _CharRow(self._pg, char)
                yield Static("[dim]Select a character\nto toggle them\ninto or out of\nthe active party.\n\nEnter or click.", id="party-detail")
            yield Static("Enter: toggle party  |  Esc: close", id="party-hint")

    # ── selection ─────────────────────────────────────────────────────────────

    @on(ListView.Selected, "#party-list")
    def _on_selected(self, event: ListView.Selected) -> None:
        if isinstance(event.item, _CharRow):
            self._toggle(event.item)

    def _toggle(self, row: "_CharRow") -> None:
        char = row.char
        pg   = self._pg
        try:
            if _is_in_party(pg, char):
                active = pg.get_active_party() or []
                if len(active) <= 1:
                    self.app.notify("Cannot remove the last party member.", severity="warning")
                    return
                pg.remove_character_from_active_party(char)
                msg = f"Removed {getattr(char,'name','character')} from party."
            else:
                max_count = getattr(pg, "max_party_count", 5)
                active    = pg.get_active_party() or []
                if len(active) >= max_count:
                    self.app.notify(f"Party is full ({max_count} members).", severity="warning")
                    return
                pg.add_character_to_active_party(char)
                msg = f"Added {getattr(char,'name','character')} to party."
        except Exception as exc:
            self.app.notify(str(exc), severity="error")
            return

        self.app.notify(msg, timeout=2)
        self._refresh_all_rows()
        self._refresh_active_boxes()

    def _refresh_all_rows(self) -> None:
        for row in self.query(_CharRow):
            row.refresh_label()

    def _refresh_active_boxes(self) -> None:
        try:
            self.query_one("#party-active-row", Static).update(
                _build_active_boxes(self._pg)
            )
        except Exception:
            pass

    # ── close ─────────────────────────────────────────────────────────────────

    def action_request_close(self) -> None:
        self.remove()
        self._on_close(None)