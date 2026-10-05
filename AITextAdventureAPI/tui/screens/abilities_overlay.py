"""
AbilitiesOverlay: floating ability-use panel for InventoryScreen.

Shows ALL abilities known by the selected character. Beneficial abilities
(heal / revive / cure / *_buff status) are fully selectable. Non-beneficial
abilities are shown dimmed and cannot be used.

Interaction:
  - Up / Down or mouse navigate; highlight updates the right detail panel.
  - Click a new row → highlight/preview only.
  - Enter on an already-highlighted row, or the Use button → push
    AbilityTargetScreen to pick a target (beneficial only).
  - InventoryScreen's own ◄/► propagates via on_player_changed().
  - Escape or ✕ closes.

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

def _resolve_ability_instances(player: Any) -> List[Any]:
    """Return all PlayerAbility instances from player.abilities.

    Handles both object form (after learn_ability()) and legacy id-string form.
    """
    owned = list(getattr(player, "abilities", []) or [])
    if not owned:
        return []
    result: List[Any] = []
    for item in owned:
        if hasattr(item, "_is_beneficial_ability"):
            result.append(item)
            continue
        try:
            import game.constants as const
            from game.objects.player_ability import _instantiate_from_seed
            seed = next(
                (s for s in getattr(const, "PLAYER_ABILITY_SEEDS", []) if s.get("id") == item),
                None,
            )
            if seed is not None:
                result.append(_instantiate_from_seed(seed))
        except Exception:
            pass
    return result


def _is_beneficial(ability: Any) -> bool:
    try:
        return bool(ability._is_beneficial_ability())
    except Exception:
        return False


def _ability_row_markup(ability: Any, player: Any, beneficial: bool) -> str:
    name    = rich_escape(str(getattr(ability, "name", "?")))
    ap_cost = getattr(ability, "ap_cost", 0) or 0
    cur_ap  = getattr(player,  "current_ap", 0) or 0
    level   = getattr(ability, "level", 1)
    effect  = getattr(ability, "effect", None)
    eff_val = rich_escape(effect.value if hasattr(effect, "value") else str(effect))
    can_aoe = getattr(ability, "can_aoe", False)

    aoe_str = "  [bold yellow]AOE[/bold yellow]" if can_aoe else ""

    if not beneficial:
        # Non-beneficial: render entirely dim — not usable
        return f"[dim]{name}  Lv.{level}  {eff_val}  AP:{ap_cost}{aoe_str}[/dim]"

    ap_str  = f"[dim]AP:{ap_cost}[/dim]"
    lv_str  = f"[dim]Lv.{level}[/dim]"
    eff_str = f"[dim]{eff_val}[/dim]"

    if cur_ap < ap_cost:
        # Beneficial but can't afford: name dim, rest normal
        return f"[dim]{name}[/dim]  {lv_str}  {eff_str}  {ap_str}{aoe_str}"

    return f"{name}  {lv_str}  {eff_str}  {ap_str}{aoe_str}"


def _build_ability_detail(ability: Any, player: Any, beneficial: bool) -> str:
    if ability is None:
        return "[dim]Select an ability to see details.[/dim]"

    lines: list[str] = []
    name        = rich_escape(str(getattr(ability, "name", "?")))
    description = rich_escape(str(getattr(ability, "description", "") or ""))
    ap_cost     = getattr(ability, "ap_cost", 0) or 0
    level       = getattr(ability, "level",   1)
    effect      = getattr(ability, "effect",  None)
    eff_val     = rich_escape(effect.value if hasattr(effect, "value") else str(effect))
    atype       = getattr(ability, "ability_type", None)
    atype_val   = rich_escape(atype.value if hasattr(atype, "value") else str(atype))
    elements    = getattr(ability, "elements", []) or []
    status_keys = getattr(ability, "status_keys", []) or []
    can_aoe     = getattr(ability, "can_aoe", False)
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

    lines.append(f"Type    : [cyan]{atype_val}[/cyan]")
    lines.append(f"Effect  : [green]{eff_val}[/green]")
    lines.append(f"Level   : {level}")
    lines.append(f"AP Cost : {ap_cost}  (have {cur_ap})")
    lines.append(f"Power   : {power}")

    if can_aoe:
        lines.append("[bold yellow]AOE — can target the whole party[/bold yellow]")
    if elements:
        from game.constants import fmt_element_glyphs
        elem_names = [
            (e.value if hasattr(e, "value") else str(e)) for e in elements
        ]
        lines.append("Elements: " + rich_escape(fmt_element_glyphs(elem_names)))
    if status_keys:
        from game.constants import fmt_status_glyphs
        status_names = [
            (k.value if hasattr(k, "value") else str(k)) for k in status_keys
        ]
        lines.append("Status  : " + rich_escape(fmt_status_glyphs(status_names)))

    lines.append("")
    if not beneficial:
        lines.append("[bold red]This ability cannot be used outside of combat.[/bold red]")
    elif cur_ap < ap_cost:
        lines.append(f"[bold red]Insufficient AP ({cur_ap}/{ap_cost})[/bold red]")

    return "\n".join(lines)


# ── row widget ────────────────────────────────────────────────────────────────

class _AbilityRow(ListItem):
    def __init__(self, ability: Any, player: Any, beneficial: bool) -> None:
        super().__init__(Label(_ability_row_markup(ability, player, beneficial)))
        self.ability    = ability
        self.beneficial = beneficial

    def _on_click(self, *args: Any, **kwargs: Any) -> None:
        """Clicks on non-beneficial rows are swallowed — no selection event."""
        if not self.beneficial:
            return
        super()._on_click(*args, **kwargs)


# ── overlay widget ────────────────────────────────────────────────────────────

class AbilitiesOverlay(Widget):
    """Floating ability panel — all known abilities, beneficial ones usable."""

    can_focus = True

    BINDINGS = [
        Binding("up",     "cursor_up",     "Up",    show=False),
        Binding("down",   "cursor_down",   "Down",  show=False),
        Binding("escape", "request_close", "Close", show=True),
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
        self._pg                  = player_game
        self._on_close            = on_close
        self._member_index        = selected_index
        self._highlighted_ability: Optional[Any] = None
        self._highlighted_beneficial: bool       = False

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
                yield Button("Use (Enter)", id="ab-btn-use",   variant="success")
                yield Button("✕ Close",     id="ab-btn-close", variant="default")
            yield Static(
                "[dim]↑↓:navigate  Enter/Use:pick target  Esc:close[/dim]",
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
        elif event.key == "enter":
            event.stop()
            self.action_use_ability()

    # ── public: called by InventoryScreen ◄/► ────────────────────────────

    def on_player_changed(self, player: Any) -> None:
        players = list(getattr(self._pg, "characters", []))
        try:
            self._member_index = players.index(player)
        except ValueError:
            pass
        self._highlighted_ability    = None
        self._highlighted_beneficial = False
        self._rebuild_list()

    # ── internal helpers ──────────────────────────────────────────────────

    def _current_player(self) -> Optional[Any]:
        players = list(getattr(self._pg, "characters", []))
        if not players:
            return None
        return players[max(0, min(self._member_index, len(players) - 1))]

    def _rebuild_list(self) -> None:
        player = self._current_player()
        lv     = self.query_one("#ab-list", ListView)
        lv.clear()
        self._highlighted_ability    = None
        self._highlighted_beneficial = False

        if player is None:
            self._update_header(0)
            self._update_detail(None, None, False)
            return

        abilities = _resolve_ability_instances(player)
        for ab in abilities:
            lv.append(_AbilityRow(ab, player, _is_beneficial(ab)))

        self._update_header(len(abilities))

        if abilities:
            first_beneficial = next((a for a in abilities if _is_beneficial(a)), None)
            first            = first_beneficial or abilities[0]
            self._highlighted_ability    = first
            self._highlighted_beneficial = _is_beneficial(first)
            self._update_detail(first, player, self._highlighted_beneficial)
            self.call_after_refresh(self._highlight_first_row)
        else:
            self._update_detail(None, player, False)

    def _highlight_first_row(self) -> None:
        lv = self.query_one("#ab-list", ListView)
        if len(lv) > 0:
            lv.index = 0

    def _update_header(self, count: int) -> None:
        player = self._current_player()
        name   = rich_escape(str(getattr(player, "name", "?"))) if player else "?"
        ap     = getattr(player, "current_ap", 0) if player else 0
        max_ap = getattr(player, "max_ap",     0) if player else 0
        self.query_one("#ab-header", Static).update(
            f"── Abilities ({count}) · {name}  AP {ap}/{max_ap} ──"
        )

    def _update_detail(
        self, ability: Optional[Any], player: Optional[Any], beneficial: bool
    ) -> None:
        text = (
            _build_ability_detail(ability, player, beneficial)
            if player
            else "[dim]No character.[/dim]"
        )
        self.query_one("#ab-detail", Static).update(text)

    # ── events ────────────────────────────────────────────────────────────

    @on(ListView.Highlighted, "#ab-list")
    def _on_highlighted(self, event: ListView.Highlighted) -> None:
        """Keyboard/mouse hover → update detail panel only, never use."""
        event.stop()
        player = self._current_player()
        child  = event.item
        if isinstance(child, _AbilityRow):
            self._highlighted_ability    = child.ability
            self._highlighted_beneficial = child.beneficial
            self._update_detail(child.ability, player, child.beneficial)
        else:
            self._highlighted_ability    = None
            self._highlighted_beneficial = False
            self._update_detail(None, player, False)

    @on(ListView.Selected, "#ab-list")
    def _on_list_selected(self, event: ListView.Selected) -> None:
        """ListView fires Selected for both Enter and click.
        We intercept Enter via on_key above, so by the time this fires the
        key event has already been consumed — this handler is click-only.
        Just sync highlight state and keep focus on the list."""
        event.stop()
        player = self._current_player()
        child  = event.item
        if isinstance(child, _AbilityRow):
            self._highlighted_ability    = child.ability
            self._highlighted_beneficial = child.beneficial
            self._update_detail(child.ability, player, child.beneficial)
        self.query_one("#ab-list", ListView).focus()

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

    def action_use_ability(self) -> None:
        ability     = self._highlighted_ability
        beneficial  = self._highlighted_beneficial
        player      = self._current_player()

        if ability is None:
            self.app.notify("Highlight an ability first.", title="Abilities")
            return
        if not beneficial:
            self.app.notify(
                "That ability cannot be used outside of combat.", title="Abilities",
                severity="warning",
            )
            return
        if player is None:
            self.app.notify("No character selected.", title="Abilities")
            return

        ap_cost = getattr(ability, "ap_cost", 0) or 0
        cur_ap  = getattr(player,  "current_ap", 0) or 0
        if cur_ap < ap_cost:
            self.app.notify(
                f"Not enough AP — need {ap_cost}, have {cur_ap}.",
                title="Abilities",
                severity="warning",
            )
            return

        party = list(getattr(self._pg, "characters", []))

        from tui.screens.ability_target_screen import AbilityTargetScreen

        def _handle_target(result: Any) -> None:
            if result is None:
                return
            self._execute_ability(ability, player, result, party)

        self.app.push_screen(AbilityTargetScreen(ability, party), _handle_target)

    def _execute_ability(
        self,
        ability: Any,
        caster: Any,
        result: Any,
        party: List[Any],
    ) -> None:
        try:
            if result[0] == "all":
                outcome = caster.use_ability(ability, targets=list(party))
            else:
                idx     = result[1]
                target  = party[idx] if 0 <= idx < len(party) else caster
                outcome = caster.use_ability(ability, target=target, targets=[target])
        except Exception as exc:
            self.app.notify(
                f"Error: {rich_escape(str(exc))}", title="Abilities", severity="error"
            )
            return

        if not outcome.get("used", False):
            err = outcome.get("error", "unknown")
            self.app.notify(
                f"Could not use ability ({err}).", title="Abilities", severity="warning"
            )
            return

        ab_name = rich_escape(str(getattr(ability, "name", "ability")))
        self.app.notify(f"Used {ab_name}!", title="Abilities")
        self._rebuild_list()

    def action_request_close(self) -> None:
        self._on_close(None)