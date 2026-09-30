"""
FastTravelOverlay: hyperway station selection overlay for OverworldScreen.

Mirrors `old/console_game_gameloop.py::handle_fast_travel_selection()`.
Cost: 100 gold per trip. Player must be standing on a hyperway tile
(`_can_travel_from_player_location`) for the action to appear.

Architecture
────────────
This is a Widget (not a pushed Screen) mounted into OverworldScreen so the
map, legend, and stats remain visible underneath.  A ConfirmScreen is pushed
before charging gold so accidental selection can be cancelled.
"""
from __future__ import annotations

from typing import Any, Callable

from rich.markup import escape as rich_escape
from textual import on
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Button, Label, ListItem, ListView, Static
from textual import events

_TRAVEL_COST = 100


def _build_hyperway_label(entry: dict) -> str:
    desc = rich_escape(str(entry.get("description") or "Unknown Location"))
    pos  = entry.get("position") or (0, 0)
    return f"{desc}  [dim]{pos}[/dim]"


class _StationItem(ListItem):
    def __init__(self, entry: dict) -> None:
        super().__init__(Label(_build_hyperway_label(entry)))
        self.entry = entry


class FastTravelOverlay(Widget):
    """Floating hyperway-selection widget overlaid on the map panel."""

    can_focus = False

    DEFAULT_CSS = """
    FastTravelOverlay {
        layer: overlay;
        width: 44;
        height: auto;
        max-height: 24;
        offset: 1 5;
        background: $surface;
        border: round $accent;
    }

    #ft-title-bar {
        height: 1;
        background: $boost;
        width: 100%;
    }

    #ft-title {
        width: 1fr;
        text-align: center;
        text-style: bold;
        padding: 0 1;
    }

    #ft-cost {
        text-align: center;
        color: $warning;
        padding: 0 1;
    }

    #ft-list {
        height: auto;
        max-height: 16;
    }

    #ft-close {
        width: 100%;
        height: 1;
        border-top: solid $accent 50%;
    }

    #ft-close-x {
        width: 3;
        min-width: 3;
        height: 1;
        border: none;
        color: $error;
        background: $boost;
    }
    """

    def __init__(
        self,
        pg: Any,
        stations: list,
        on_done: Callable[[bool], None],
    ) -> None:
        super().__init__()
        self._pg = pg
        self._stations = stations
        self._on_done = on_done

    def compose(self) -> ComposeResult:
        with Vertical():
            with Horizontal(id="ft-title-bar"):
                yield Static("── Hyperway Fast Travel ──", id="ft-title")
                yield Button("✕", id="ft-close-x", variant="default")
            yield Static(
                f"Cost: {_TRAVEL_COST} gold  |  Balance: {getattr(self._pg, 'money', 0)}",
                id="ft-cost",
            )
            with ListView(id="ft-list"):
                for entry in self._stations:
                    yield _StationItem(entry)

    @on(Button.Pressed, "#ft-close")
    def _close(self) -> None:
        self.remove()
        self._on_done(False)

    def on_key(self, event: events.Key) -> None:
        """Block overworld movement keys. Handle Escape directly."""
        _OVERWORLD_KEYS = {
            "w", "a", "s", "d",
            "up", "down", "left", "right",
            "i", "t",
        }
        if event.key == "escape":
            event.stop()
            self.action_close()
        elif event.key in _OVERWORLD_KEYS:
            event.stop()

    @on(Button.Pressed, "#ft-close-x")
    def _on_close_x(self) -> None:
        self.action_close()

    def action_close(self) -> None:
        self.remove_class("ow-overlay")
        self.remove()
        self._on_done(False)

    @on(ListView.Selected, "#ft-list")
    def _on_selected(self, event: ListView.Selected) -> None:
        if not isinstance(event.item, _StationItem):
            return
        entry = event.item.entry
        dest  = entry.get("position")
        desc  = entry.get("description") or "Unknown Location"
        money = getattr(self._pg, "money", 0)

        if money < _TRAVEL_COST:
            self.app.notify(
                f"You need {_TRAVEL_COST} gold to travel. You have {money}.",
                title="Insufficient Funds",
                severity="warning",
            )
            return

        def _on_confirmed(confirmed: bool | None) -> None:
            if confirmed:
                try:
                    self._pg.handle_fast_travel_from_player_location(dest)
                except Exception as exc:
                    self.app.notify(str(exc), title="Travel Error", severity="error")
                    self.action_close()
                    return
                self.app.notify(f"Arrived at {desc}.", title="Fast Travel", timeout=3)
                self.remove_class("ow-overlay")
                self.remove()
                self._on_done(True)
                return
            # Cancelled: ConfirmScreen returned focus to the app, not this
            # overlay. Refocus the station list so arrow/Enter navigation keeps
            # working (the overworld's structural .ow-overlay guard otherwise
            # swallows those keys, stranding the overlay until Escape/reopen).
            try:
                self.query_one("#ft-list", ListView).focus()
            except Exception:
                try:
                    self.focus()
                except Exception:
                    pass

        from tui.screens.confirm_screen import ConfirmScreen  # noqa: PLC0415
        self.app.push_screen(
            ConfirmScreen(
                f"Travel to {desc}?\nCost: {_TRAVEL_COST} gold",
                yes_label="Travel",
                no_label="Cancel",
            ),
            _on_confirmed,
        )

    def on_mount(self) -> None:
        self.add_class("ow-overlay")