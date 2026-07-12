"""
AbilityTargetScreen: modal target-selection popup launched from AbilitiesOverlay.

Shows all party members as selectable targets for the chosen ability.
If the ability has `can_aoe=True`, a "Use on All" button is also offered.

Caller pushes and receives a result via dismiss():
  - None            → cancelled
  - ("single", idx) → use on player at that party index
  - ("all",)        → use on the entire party (AOE)
"""
from __future__ import annotations

from typing import Any, List, Optional, Tuple, Union

from rich.markup import escape as rich_escape
from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label, ListItem, ListView, Static

from tui.screens.base_screen import BaseScreen

AbilityTargetResult = Union[Tuple[str, int], Tuple[str], None]


def _target_row_markup(player: Any) -> str:
    name   = rich_escape(str(getattr(player, "name", "?")))
    level  = getattr(player, "level", 0)
    cur_hp = getattr(player, "current_hp", 0)
    max_hp = getattr(player, "max_hp", 0)
    cur_ap = getattr(player, "current_ap", 0)
    max_ap = getattr(player, "max_ap", 0)
    return f"{name}  [dim]Lv.{level}  HP {cur_hp}/{max_hp}  AP {cur_ap}/{max_ap}[/dim]"


class _TargetRow(ListItem):
    def __init__(self, player: Any, index: int) -> None:
        super().__init__(Label(_target_row_markup(player)))
        self.player = player
        self.index  = index


class AbilityTargetScreen(BaseScreen):
    """
    Modal overlay: pick a target for a beneficial ability.

    Up / Down navigate; Enter or "Use on Target" confirms single-target use.
    "Use on All" (only shown when ability.can_aoe is True) fires AOE use.
    Escape or Cancel dismisses with None.
    """

    show_header = False
    show_footer = False

    BINDINGS = [
        Binding("up",     "cursor_up",   "Up",     show=False),
        Binding("down",   "cursor_down", "Down",   show=False),
        Binding("enter",  "confirm",     "Use",    show=True),
        Binding("escape", "cancel",      "Cancel", show=True),
    ]

    DEFAULT_CSS = """
    AbilityTargetScreen {
        align: center middle;
        background: $background 60%;
    }

    #target-panel {
        width: 60;
        height: auto;
        max-height: 30;
        border: round $accent;
        padding: 1 2;
        background: $surface;
    }

    #target-title {
        text-style: bold;
        text-align: center;
        margin-bottom: 1;
    }

    #target-subtitle {
        text-align: center;
        color: $text 60%;
        margin-bottom: 1;
    }

    #target-list {
        height: auto;
        max-height: 12;
        margin-bottom: 1;
    }

    #target-buttons {
        align: center middle;
        height: auto;
        margin-top: 1;
    }

    #target-buttons Button {
        margin: 0 1;
        min-width: 16;
    }
    """

    def __init__(self, ability: Any, party: List[Any]) -> None:
        super().__init__()
        self._ability = ability
        self._party   = list(party)

    def compose_content(self) -> ComposeResult:
        name    = rich_escape(str(getattr(self._ability, "name", "?")))
        ap_cost = getattr(self._ability, "ap_cost", 0) or 0
        can_aoe = getattr(self._ability, "can_aoe", False)
        effect  = getattr(self._ability, "effect", None)
        eff_val = rich_escape(effect.value if hasattr(effect, "value") else str(effect))

        with Vertical(id="target-panel"):
            yield Static(f"Use: [bold]{name}[/bold]", id="target-title")
            yield Static(
                f"{eff_val}  ·  AP cost: {ap_cost}  ·  Select a target",
                id="target-subtitle",
            )
            with ListView(id="target-list"):
                for i, p in enumerate(self._party):
                    yield _TargetRow(p, i)
            with Horizontal(id="target-buttons"):
                yield Button("Use on Target", id="btn-confirm", variant="success")
                if can_aoe:
                    yield Button("Use on All",    id="btn-aoe",     variant="warning")
                yield Button("Cancel",            id="btn-cancel",  variant="default")

    def on_mount(self) -> None:
        lv = self.query_one("#target-list", ListView)
        lv.focus()
        if len(lv) > 0:
            lv.index = 0

    # ── helpers ───────────────────────────────────────────────────────────

    def _highlighted_index(self) -> Optional[int]:
        lv    = self.query_one("#target-list", ListView)
        child = lv.highlighted_child
        return child.index if isinstance(child, _TargetRow) else None

    # ── events ────────────────────────────────────────────────────────────

    @on(ListView.Selected, "#target-list")
    def _on_list_selected(self, event: ListView.Selected) -> None:
        """Click selects the row only; Enter is handled by the binding."""
        event.stop()
        self.query_one("#target-list", ListView).focus()

    @on(Button.Pressed, "#btn-confirm")
    def _on_confirm(self) -> None:
        self.action_confirm()

    @on(Button.Pressed, "#btn-aoe")
    def _on_aoe(self) -> None:
        self.dismiss(("all",))

    @on(Button.Pressed, "#btn-cancel")
    def _on_cancel(self) -> None:
        self.dismiss(None)

    # ── actions ───────────────────────────────────────────────────────────

    def action_cursor_up(self) -> None:
        self.query_one("#target-list", ListView).action_cursor_up()

    def action_cursor_down(self) -> None:
        self.query_one("#target-list", ListView).action_cursor_down()

    def action_confirm(self) -> None:
        idx = self._highlighted_index()
        if idx is None:
            self.app.notify("Select a target first.", title="Abilities")
            return
        self.dismiss(("single", idx))

    def action_cancel(self) -> None:
        self.dismiss(None)