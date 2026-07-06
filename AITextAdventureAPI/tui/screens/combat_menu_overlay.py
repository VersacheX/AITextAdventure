"""
CombatMenuOverlay: bottom-docked ability/item picker for the combat screen.

Mirrors the "b" (abilities) and "u" (inventory) dropdowns in
`old/combat_balancing_simulation/combat_simulator_screen.py`: the active
player browses a filtered list (abilities they can currently afford, or
usable utility items) and picks one to use. Selecting an entry hands control
back to `CombatScreen`, which then opens `CombatTargetOverlay` to choose who
it's used on.
"""
from __future__ import annotations

from typing import Any, Callable, List, Optional, Tuple

from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.widget import Widget
from textual.widgets import Label, ListItem, ListView, Static


class _MenuItem(ListItem):
    """Single selectable row carrying an arbitrary payload."""

    def __init__(self, label: str, payload: Any) -> None:
        super().__init__(Label(label))
        self.payload = payload


class CombatMenuOverlay(Widget):
    """Bottom-docked list picker for abilities or utility items."""

    can_focus = True
    can_focus_children = False

    BINDINGS = [
        Binding("escape", "cancel", "Cancel", show=True),
    ]

    DEFAULT_CSS = """
    CombatMenuOverlay {
        layer: overlay;
        dock: bottom;
        width: 100%;
        height: 12;
        background: $surface;
        border-top: thick $accent;
    }

    #menu-title {
        width: 100%;
        text-align: center;
        text-style: bold;
        background: $boost;
        color: $text;
        padding: 0 1;
        height: 1;
    }

    #menu-list {
        width: 100%;
        height: 1fr;
        border: solid $primary;
    }
    """

    def __init__(
        self,
        title: str,
        entries: List[Tuple[str, Any]],
        on_select: Callable[[Optional[Any]], None],
    ) -> None:
        super().__init__()
        self._title = title
        self._entries = entries
        self._on_select = on_select

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Static(self._title, id="menu-title")
            with ListView(id="menu-list"):
                for label, payload in self._entries:
                    yield _MenuItem(label, payload)

    def on_mount(self) -> None:
        self.add_class("inv-overlay")
        self.focus()
        try:
            self.query_one("#menu-list", ListView).focus()
        except Exception:
            pass

    def action_cancel(self) -> None:
        self._on_select(None)
        self.remove()

    @on(ListView.Selected, "#menu-list")
    def _on_selected(self, event: ListView.Selected) -> None:
        if isinstance(event.item, _MenuItem):
            self._on_select(event.item.payload)
        else:
            self._on_select(None)
        self.remove()
