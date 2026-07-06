"""
CombatTargetOverlay: centered target-selection widget for the combat screen.

Mirrors `old/combat_balancing_simulation/combat_simulator_screen.py`'s
`_select_target()` helper: the player picks a unit to attack, heal, or apply
an ability/item to, with Left/Right toggling between the hostile and
friendly rosters. Unlike the legacy blocking version, this is a Textual
`Widget` that reports the choice back through a callback instead of
stealing the whole terminal via a `readchar` + redraw loop.

If `allow_multi` is True, pressing "a" selects every currently-listed unit
(used for AoE abilities), mirroring the legacy 'a' shortcut.
"""
from __future__ import annotations

from typing import Any, Callable, List, Optional

from rich.markup import escape as rich_escape
from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.widget import Widget
from textual.widgets import Label, ListItem, ListView, Static


class _TargetItem(ListItem):
    """Single selectable row carrying its Unit payload."""

    def __init__(self, unit: Any) -> None:
        name = rich_escape(str(getattr(unit.entity, "name", "?")))
        cur_hp = getattr(unit.entity, "current_hp", 0)
        max_hp = getattr(unit.entity, "max_hp", 0)
        super().__init__(Label(f"{name}  ({cur_hp}/{max_hp} HP)"))
        self.unit = unit


class CombatTargetOverlay(Widget):
    """Centered target picker; reports the selection via `on_select` callback."""

    can_focus = True
    can_focus_children = False

    BINDINGS = [
        Binding("left", "toggle_side", "Switch side", show=True),
        Binding("right", "toggle_side", "Switch side", show=True),
        Binding("a", "select_all", "Select All", show=False),
        Binding("escape", "cancel", "Cancel", show=True),
    ]

    DEFAULT_CSS = """
    CombatTargetOverlay {
        layer: overlay;
        width: 50;
        height: auto;
        max-height: 20;
        background: $surface;
        border: thick $accent;
        offset: 50% 50%;
    }

    #tgt-title {
        width: 100%;
        text-align: center;
        text-style: bold;
        background: $boost;
        color: $text;
        padding: 0 1;
        height: 1;
    }

    #tgt-list {
        width: 100%;
        height: auto;
        max-height: 14;
    }

    #tgt-footer {
        width: 100%;
        height: 1;
        text-align: center;
        color: $text 50%;
        border-top: solid $accent 50%;
    }
    """

    def __init__(
        self,
        hostiles: List[Any],
        allies: List[Any],
        on_select: Callable[[Optional[List[Any]]], None],
        *,
        title: str = "Select target",
        prefer_hostiles: bool = True,
        allow_multi: bool = False,
    ) -> None:
        super().__init__()
        self._hostiles = hostiles
        self._allies = allies
        self._on_select = on_select
        self._title = title
        self._allow_multi = allow_multi

        if prefer_hostiles and hostiles:
            self._showing_hostiles = True
        elif not prefer_hostiles and allies:
            self._showing_hostiles = False
        else:
            self._showing_hostiles = bool(hostiles)

    def _current_list(self) -> List[Any]:
        return self._hostiles if self._showing_hostiles else self._allies

    def compose(self) -> ComposeResult:
        footer_parts: List[str] = []
        if self._hostiles and self._allies:
            footer_parts.append("<-/-> switch side")
        if self._allow_multi:
            footer_parts.append("(a) select all")
        footer_parts.append("Esc cancel")

        with Vertical():
            yield Static(self._title, id="tgt-title")
            with ListView(id="tgt-list"):
                for unit in self._current_list():
                    yield _TargetItem(unit)
            yield Static("   ".join(footer_parts), id="tgt-footer")

    def on_mount(self) -> None:
        self.add_class("inv-overlay")
        self.focus()
        try:
            self.query_one("#tgt-list", ListView).focus()
        except Exception:
            pass

    # ── helpers ──────────────────────────────────────────────────────────

    def _rebuild_list(self) -> None:
        try:
            list_view = self.query_one("#tgt-list", ListView)
            list_view.clear()
            for unit in self._current_list():
                list_view.append(_TargetItem(unit))
        except Exception:
            pass

    # ── actions ──────────────────────────────────────────────────────────

    def action_toggle_side(self) -> None:
        if not self._hostiles or not self._allies:
            return
        self._showing_hostiles = not self._showing_hostiles
        self._rebuild_list()

    def action_select_all(self) -> None:
        if not self._allow_multi:
            return
        targets = list(self._current_list())
        self._on_select(targets if targets else None)
        self.remove()

    def action_cancel(self) -> None:
        self._on_select(None)
        self.remove()

    @on(ListView.Selected, "#tgt-list")
    def _on_selected(self, event: ListView.Selected) -> None:
        if isinstance(event.item, _TargetItem):
            self._on_select([event.item.unit])
        else:
            self._on_select(None)
        self.remove()