"""
AbilitiesOverlay: floating ability-use panel for InventoryScreen.

Displays only the beneficial abilities known by the selected character
(heal / revive / cure / *_buff status abilities).  Players may:
  - Browse the list with Up / Down (or mouse).
  - Press Enter (or click a row) to select — this highlights the row and
    populates the right-hand detail panel.  It does NOT immediately use.
  - Press U or click "Use" to actually invoke the ability on the character
    (self-target).  The right panel shows AP cost, power, elements, and a
    description.
  - Left / Right cycle the active character while the overlay stays open.
  - Escape or ✕ closes.

Only abilities whose `_is_beneficial_ability()` returns True are shown.
Abilities the character lacks sufficient AP for are labelled [dim] but are
still listed (the Use action will surface the error).

The CSS class "inv-overlay" is added in on_mount so InventoryScreen can
query and remove any open overlay generically.
"""
from __future__ import annotations

from typing import Any, Callable, List, Optional

from rich.markup import escape as rich_escape
from textual import events, on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, ScrollableContainer, Vertical
from textual.widget import Widget
from textual.widgets import Button, Label, ListItem, ListView, Static


# ── helpers ───────────────────────────────────────────────────────────────────

def _get_beneficial_abilities(player: Any) -> List[Any]:
    """Return instantiated PlayerAbility objects known by *player* that are
    considered beneficial (heal / revive / cure / buff status)."""
    try:
        from game.objects.player_ability import get_player_ability_instances
    except ImportError:
        return []
    abilities = get_player_ability_instances(player)
    return [a for a in abilities if a._is_beneficial_ability()]


def _ability_row_markup(ability: Any, player: Any) -> str:
    name     = rich_escape(str(getattr(ability, "name", "?")))
    ap_cost  = getattr(ability, "ap_cost", 0) or 0
    cur_ap   = getattr(player,  "current_ap", 0) or 0
    level    = getattr(ability, "level", 1)
    effect   = getattr(ability, "effect", None)
    eff_val  = effect.value if hasattr(effect, "value") else str(effect)

    ap_str   = f"[dim]AP:{ap_cost}[/dim]"
    lv_str   = f"[dim]Lv.{level}[/dim]"
    eff_str  = f"[dim]{rich_escape(eff_val)}[/dim]"

    if cur_ap < ap_cost:
        return f"[dim]{name}[/dim]  {lv_str}  {eff_str}  {ap_str}"
    return f"{name}  {lv_str}  {eff_str}  {ap_str}"


def _build_ability_detail(ability: Any, player: Any) -> str:
    """Return Rich-markup detail text for the right panel."""
    if ability is None:
        return "[dim]Select an ability to see details.[/dim]"

    lines: list[str] = []
    name        = rich_escape(str(getattr(ability, "name", "?")))
    description = rich_escape(str(getattr(ability, "description", "") or ""))
    ap_cost     = getattr(ability, "ap_cost", 0) or 0
    level       = getattr(ability, "level",   1)
    effect      = getattr(ability, "effect",  None)
    eff_val     = effect.value if hasattr(effect, "value") else str(effect)
    atype       = getattr(ability, "ability_type", None)
    atype_val   = atype.value  if hasattr(atype,   "value") else str(atype)
    elements    = getattr(ability, "elements", []) or []
    status_keys = getattr(ability, "status_keys", []) or []
    cur_ap      = getattr(player, "current_ap", 0) or 0

    try:
        power = ability.compute_power_with_owner(player)
    except Exception:
        power = ability.compute_power()

    lines.append(f"[bold]{name}[/bold]")
    lines.append("")
    if description:
        lines.append(description)
        lines.append("")

    lines.append(f"Type    : [cyan]{rich_escape(atype_val)}[/cyan]")
    lines.append(f"Effect  : [green]{rich_escape(eff_val)}[/green]")
    lines.append(f"Level   : {level}")
    lines.append(f"AP Cost : {ap_cost}  (have {cur_ap})")
    lines.append(f"Power   : {power}")

    if elements:
        elem_str = ", ".join(
            rich_escape(e.value if hasattr(e, "value") else str(e))
            for e in elements
        )
        lines.append(f"Elements: {elem_str}")

    if status_keys:
        sk_str = ", ".join(rich_escape(str(k)) for k in status_keys)
        lines.append(f"Status  : {sk_str}")

    if cur_ap < ap_cost:
        lines.append("")
        lines.append(f"[bold red]Insufficient AP ({cur_ap}/{ap_cost})[/bold red]")

    return "\n".join(lines)


# ── row widget ────────────────────────────────────────────────────────────────

class _AbilityRow(ListItem):
    def __init__(self, ability: Any, player: Any) -> None:
        super().__init__(Label(_ability_row_markup(ability, player)))
        self.ability = ability


# ── overlay widget ────────────────────────────────────────────────────────────

class AbilitiesOverlay(Widget):
    """
    Floating beneficial-ability panel docked to the bottom of InventoryScreen.

    Up / Down navigate the list; Enter/click selects (populates detail panel).
    U or the Use button invokes the ability on the current character (self-target).
    Left / Right change the active party member.
    Escape or ✕ closes the overlay.
    """

    can_focus = True

    BINDINGS = [
        Binding("up",     "cursor_up",     "Up",       show=False),
        Binding("down",   "cursor_down",   "Down",     show=False),
        Binding("left",   "prev_member",   "◄ Member", show=True),
        Binding("right",  "next_member",   "Member ►", show=True),
        Binding("u",      "use_ability",   "Use",      show=True),
        Binding("escape", "request_close", "Close",    show=True),
    ]

    DEFAULT_CSS = """
    AbilitiesOverlay {
        layer: overlay;
        dock: bottom;
        width: 100%;
        height: 20;
        background: $surface;
        border-top: solid $accent;
    }

    AbilitiesOverlay > Vertical {
        height: 100%;
    }

    #ab-title-bar {
        height: 1;
        background: $boost;
    }

    #ab-header {
        width: 1fr;
        text-align: center;
        text-style: bold;
        padding: 0 1;
    }

    #ab-close-x {
        width: 3;
        min-width: 3;
        height: 1;
        border: none;
        color: $error;
        background: $boost;
    }

    #ab-body {
        height: 1fr;
        layout: horizontal;
    }

    #ab-list {
        width: 1fr;
        height: 100%;
        border-right: solid $accent 40%;
    }

    #ab-detail-scroll {
        width: 1fr;
        height: 100%;
        padding: 0 1;
    }

    #ab-detail {
        width: 100%;
    }

    #ab-action-bar {
        height: 3;
        background: $panel;
        border-top: solid $accent 40%;
        padding: 0 1;
        layout: horizontal;
    }

    #ab-action-bar Button {
        height: 1;
        min-width: 10;
        margin-right: 1;
        border: none;
    }

    #ab-hint {
        height: 1;
        padding: 0 1;
        color: $text 50%;
        text-align: center;
    }
    """

    def __init__(
        self,
        player_game: Any,
        on_close: Callable[[str | None], None],
        selected_index: int = 0,
    ) -> None:
        super().__init__()
        self._pg             = player_game
        self._on_close       = on_close
        self._member_index   = selected_index
        self._selected_ability: Optional[Any] = None

    # ── compose ───────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        with Vertical():
            with Horizontal(id="ab-title-bar"):
                yield Static("── Abilities ──", id="ab-header")
                yield Button("✕", id="ab-close-x", variant="default")
            with Horizontal(id="ab-body"):
                yield ListView(id="ab-list")
                with ScrollableContainer(id="ab-detail-scroll"):
                    yield Static(
                        "[dim]Select an ability to see details.[/dim]",
                        id="ab-detail",
                    )
            with Horizontal(id="ab-action-bar"):
                yield Button("Use (u)", id="ab-btn-use",   variant="success")
                yield Button("✕ Close", id="ab-btn-close", variant="default")
            yield Static(
                "[dim]Enter/click:select  U:use  ◄►:member  Esc:close[/dim]",
                id="ab-hint",
            )

    def on_mount(self) -> None:
        self.add_class("inv-overlay")
        self._rebuild_list()
        self.query_one("#ab-list", ListView).focus()

    def on_key(self, event: events.Key) -> None:
        if event.key == "escape":
            event.stop()
            self.action_request_close()

    # ── public: called by InventoryScreen on ◄/► ──────────────────────────

    def on_player_changed(self, player: Any) -> None:
        players = list(getattr(self._pg, "characters", []))
        try:
            self._member_index = players.index(player)
        except ValueError:
            pass
        self._selected_ability = None
        self._rebuild_list()

    # ── helpers ───────────────────────────────────────────────────────────

    def _current_player(self) -> Optional[Any]:
        players = list(getattr(self._pg, "characters", []))
        if not players:
            return None
        idx = max(0, min(self._member_index, len(players) - 1))
        return players[idx]

    def _rebuild_list(self) -> None:
        player    = self._current_player()
        lv        = self.query_one("#ab-list", ListView)
        lv.clear()
        self._selected_ability = None

        if player is None:
            self._update_header(0)
            self._update_detail(None, None)
            return

        abilities = _get_beneficial_abilities(player)
        for ab in abilities:
            lv.append(_AbilityRow(ab, player))

        self._update_header(len(abilities))
        self._update_detail(None, player)

    def _update_header(self, count: int) -> None:
        player = self._current_player()
        name   = rich_escape(str(getattr(player, "name", "?"))) if player else "?"
        ap     = getattr(player, "current_ap", 0) if player else 0
        max_ap = getattr(player, "max_ap", 0)     if player else 0
        self.query_one("#ab-header", Static).update(
            f"── Abilities ({count}) · {name}  AP {ap}/{max_ap} ──"
        )

    def _update_detail(self, ability: Optional[Any], player: Optional[Any]) -> None:
        text = _build_ability_detail(ability, player) if player else "[dim]No character.[/dim]"
        self.query_one("#ab-detail", Static).update(text)

    def _highlighted_ability(self) -> Optional[Any]:
        lv    = self.query_one("#ab-list", ListView)
        child = lv.highlighted_child
        return child.ability if isinstance(child, _AbilityRow) else None

    # ── events ────────────────────────────────────────────────────────────

    @on(ListView.Highlighted, "#ab-list")
    def _on_highlighted(self, event: ListView.Highlighted) -> None:
        event.stop()
        player = self._current_player()
        child  = event.item
        ab     = child.ability if isinstance(child, _AbilityRow) else None
        self._selected_ability = ab
        self._update_detail(ab, player)

    @on(ListView.Selected, "#ab-list")
    def _on_list_selected(self, event: ListView.Selected) -> None:
        """Click/Enter on a row selects it (populates detail); does not use."""
        event.stop()
        player = self._current_player()
        child  = event.item
        ab     = child.ability if isinstance(child, _AbilityRow) else None
        self._selected_ability = ab
        self._update_detail(ab, player)

    @on(Button.Pressed, "#ab-close-x")
    @on(Button.Pressed, "#ab-btn-close")
    def _on_close_btn(self) -> None:
        self.action_request_close()

    @on(Button.Pressed, "#ab-btn-use")
    def _on_use_btn(self) -> None:
        self.action_use_ability()

    # ── actions ───────────────────────────────────────────────────────────

    def action_cursor_up(self) -> None:
        self.query_one("#ab-list", ListView).action_cursor_up()

    def action_cursor_down(self) -> None:
        self.query_one("#ab-list", ListView).action_cursor_down()

    def action_prev_member(self) -> None:
        self._shift_member(-1)

    def action_next_member(self) -> None:
        self._shift_member(+1)

    def action_use_ability(self) -> None:
        ability = self._selected_ability or self._highlighted_ability()
        player  = self._current_player()

        if ability is None:
            self.app.notify("Select an ability first.", title="Abilities")
            return
        if player is None:
            self.app.notify("No character selected.", title="Abilities")
            return

        # self-target: beneficial abilities apply to the user
        try:
            result = player.use_ability(ability, target=player, targets=[player])
        except Exception as exc:
            self.app.notify(
                f"Error: {rich_escape(str(exc))}", title="Abilities", severity="error"
            )
            return

        if not result.get("used", False):
            err = result.get("error", "unknown")
            if err == "insufficient_ap":
                ap    = getattr(player, "current_ap", 0)
                cost  = getattr(ability, "ap_cost", 0)
                self.app.notify(
                    f"Not enough AP — need {cost}, have {ap}.",
                    title="Abilities",
                    severity="warning",
                )
            else:
                self.app.notify(
                    f"Could not use ability ({err}).",
                    title="Abilities",
                    severity="warning",
                )
            return

        ab_name = rich_escape(str(getattr(ability, "name", "ability")))
        self.app.notify(f"Used {ab_name}!", title="Abilities")
        # refresh list and detail (AP / HP values have changed)
        self._rebuild_list()
        self._update_header(len(_get_beneficial_abilities(player)))

    def action_request_close(self) -> None:
        self._on_close(None)

    # ── member cycling ────────────────────────────────────────────────────

    def _shift_member(self, delta: int) -> None:
        players = list(getattr(self._pg, "characters", []))
        if not players:
            return
        self._member_index = (self._member_index + delta) % len(players)
        self._selected_ability = None
        self._rebuild_list()