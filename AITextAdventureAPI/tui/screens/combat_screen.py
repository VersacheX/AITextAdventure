"""
CombatScreen: native Textual combat screen driven by the pure
`CombatSimulation` engine.

Replaces the legacy blocking `readchar`-based loop in
`old/combat_balancing_simulation/combat_simulator_screen.py`'s
`CombatScreen.run()`. That engine (`old/combat_balancing_simulation/
combat_simulator.py`) stays exactly as-is and is the source of truth for
combat rules — this screen only replaces *how* turns are stepped through and
rendered:

  - The legacy loop called `time.sleep()` between messages and blocked on
    `readchar.readkey()` for player input. Here, turns advance through
    `set_timer()` callbacks and player input arrives through normal Textual
    bindings/button presses, so the compositor never stalls.
  - Target/ability/item selection (`_select_target()`, the 'b'/'u' dropdowns)
    is replaced by `CombatTargetOverlay` / `CombatMenuOverlay`, mounted on the
    "overlay" layer exactly like `LocationOverlay` / `LearnOverlay`.

Flow per turn (mirrors the legacy inner loop in `CombatScreen.run()`):
  1. `_advance_turn()` checks for combat-over, then asks the simulation for
     the next ready unit.
  2. A blocked (petrify/stun/sleep/paralyze) or confused unit auto-resolves
     its turn and immediately chains into `_advance_turn()` again.
  3. A hostile unit acts automatically and chains onward the same way.
  4. A player unit sets `_awaiting_player_input = True` and waits for an
     Attack/Ability/Item/Flee action from the key bindings or action bar.
Once combat ends, the screen calls `self.dismiss(players_won)` — the same
modal-result pattern `ConfirmScreen` uses — so callers (e.g.
`OverworldScreen._trigger_combat`) react via a `push_screen(..., callback)`.
"""
from __future__ import annotations

from typing import Any, List, Optional

from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Static

from tui.screens.base_screen import BaseScreen
from tui.screens.combat_menu_overlay import CombatMenuOverlay
from tui.screens.combat_target_overlay import CombatTargetOverlay
from tui.services.combat_renderer import (
    build_hostile_card_text,
    build_player_card_text,
    build_turn_order_text,
)
from tui.services.combat_service import (
    build_simulation,
    check_combat_over,
    distribute_rewards,
    get_blocking_status_result,
    get_next_ready_unit,
    get_targets,
    is_beneficial_ability,
    is_beneficial_item,
    is_confused,
    is_silenced,
    is_unit_player,
    perform_auto_skip,
    perform_confused_action,
    perform_hostile_auto_action,
    perform_player_ability,
    perform_player_attack,
    perform_player_escape,
    perform_player_item,
)


class CombatScreen(BaseScreen):
    """Turn-based combat screen. Push with a result callback:

        self.app.push_screen(CombatScreen(pg, hostiles), on_done)

        def on_done(players_won: bool | None) -> None:
            ...

    Not registered in `FractureApp.SCREENS` — like `ConfirmScreen`, it needs
    constructor arguments (`pg`, `hostiles`), so it's always pushed as an
    already-constructed instance rather than looked up by name.
    """

    LAYERS = ("default", "overlay")
    show_header = False

    BINDINGS = [
        Binding("a", "attack", "Attack", show=True),
        Binding("b", "ability", "Ability", show=True),
        Binding("u", "item", "Item", show=True),
        Binding("r", "flee", "Flee", show=True),
        Binding("escape", "go_back", "Forfeit disabled", show=False),
    ]

    DEFAULT_CSS = """
    CombatScreen {
        layout: vertical;
        layers: base overlay;
    }

    #combat-row {
        height: 1fr;
        layout: horizontal;
    }

    #players-col {
        width: 30;
        height: 100%;
        border-right: solid $accent;
        padding: 1;
        overflow-y: auto;
    }

    #hostiles-col {
        width: 30;
        height: 100%;
        border-left: solid $accent;
        padding: 1;
        overflow-y: auto;
    }

    #center-col {
        width: 1fr;
        height: 100%;
        padding: 1;
    }

    #combat-log {
        width: 100%;
        height: 100%;
        overflow-y: auto;
    }

    .combat-card {
        width: 100%;
        height: auto;
        border: solid $primary;
        padding: 0 1;
        margin-bottom: 1;
    }

    .combat-card.active-card {
        border: double $accent;
        background: $surface-lighten-1;
    }

    #action-bar {
        height: 3;
        background: $panel;
        border-top: solid $accent;
        padding: 0 1;
    }

    #action-bar Button {
        height: 1;
        min-width: 14;
        margin-right: 1;
        border: none;
    }

    Footer {
        height: 1;
    }
    """

    def __init__(self, pg: Any, hostiles: List[Any]) -> None:
        super().__init__()
        self._pg = pg
        # CombatSimulation.__init__ is pure computation (unit wrapping +
        # initial scheduling) — safe to build eagerly so compose_content()
        # already knows the unit roster.
        self._sim = build_simulation(pg, hostiles)
        self._active_unit: Optional[Any] = None
        self._message_log: List[str] = []
        self._awaiting_player_input = False

    # ── compose ──────────────────────────────────────────────────────────

    def compose_content(self) -> ComposeResult:
        players = [u for u in self._sim.units if is_unit_player(u)]
        hostiles = [u for u in self._sim.units if not is_unit_player(u)]

        with Horizontal(id="combat-row"):
            with Vertical(id="players-col"):
                for u in players:
                    yield Static("", id=f"card-{u.entity._uuid}", classes="combat-card")
            with Vertical(id="center-col"):
                yield Static("", id="combat-log")
            with Vertical(id="hostiles-col"):
                for u in hostiles:
                    yield Static("", id=f"card-{u.entity._uuid}", classes="combat-card")

        with Horizontal(id="action-bar"):
            yield Button("Attack (a)", id="btn-attack", variant="default")
            yield Button("Ability (b)", id="btn-ability", variant="default")
            yield Button("Item (u)", id="btn-item", variant="default")
            yield Button("Flee (r)", id="btn-flee", variant="default")

    def on_mount(self) -> None:
        self._refresh_cards()
        self._update_log()
        self.set_timer(0.4, self._advance_turn)

    # ── escape is intentionally not "go back" mid-combat ───────────────────

    def action_go_back(self) -> None:
        self.notify("You can't leave combat. Use Flee (r) to attempt an escape.", severity="warning")

    # ── turn loop ────────────────────────────────────────────────────────

    def _advance_turn(self) -> None:
        outcome = check_combat_over(self._sim)
        if outcome is not None:
            self._finish_combat(outcome)
            return

        unit = get_next_ready_unit(self._sim)
        if unit is None:
            # Defensive only: next_active_unit() should always return a unit
            # when alive units remain, since check_combat_over() already
            # guarded against an empty roster above.
            self.set_timer(0.05, self._advance_turn)
            return

        self._active_unit = unit
        self._refresh_cards()

        blocking = get_blocking_status_result(unit)
        if blocking is not None:
            res = perform_auto_skip(self._sim, unit, blocking)
            self._show_messages_then(res.get("messages", []), self._advance_turn)
            return

        if is_confused(unit):
            res = perform_confused_action(self._sim, unit)
            self._show_messages_then(res.get("messages", []), self._advance_turn)
            return

        if is_unit_player(unit):
            self._awaiting_player_input = True
            self._update_log(prompt=f"{unit.entity.name}'s turn — choose an action.")
        else:
            res = perform_hostile_auto_action(self._sim, unit)
            self._show_messages_then(res.get("messages", []), self._advance_turn)

    def _finish_combat(self, players_won: bool) -> None:
        self._awaiting_player_input = False
        if players_won:
            messages = distribute_rewards(self._sim) or ["Victory!"]
            self._show_messages_then(messages, lambda: self.dismiss(True))
        else:
            self._show_messages_then(["You have been defeated..."], lambda: self.dismiss(False))

    def _show_messages_then(self, messages: List[str], callback) -> None:
        """Reveal `messages` one at a time (mirrors the legacy `time.sleep(1)`
        pacing) via chained `set_timer()` calls, then invoke `callback`."""

        def _step(index: int) -> None:
            if index >= len(messages):
                callback()
                return
            self._message_log.append(messages[index])
            if len(self._message_log) > 200:
                self._message_log.pop(0)
            self._update_log()
            self._refresh_cards()
            self.set_timer(0.9, lambda: _step(index + 1))

        if not messages:
            callback()
            return
        _step(0)

    # ── rendering ────────────────────────────────────────────────────────

    def _refresh_cards(self) -> None:
        for u in self._sim.units:
            try:
                card = self.query_one(f"#card-{u.entity._uuid}", Static)
            except Exception:
                continue
            is_active = u is self._active_unit
            if is_unit_player(u):
                card.update(build_player_card_text(u, is_active=is_active))
            else:
                card.update(build_hostile_card_text(u, is_active=is_active))
            card.set_class(is_active, "active-card")

    def _update_log(self, *, prompt: Optional[str] = None) -> None:
        lines = list(self._message_log[-12:])
        if prompt:
            lines.append("")
            lines.append(f"[bold cyan]{prompt}[/bold cyan]")
        turn_order = build_turn_order_text(self._sim)
        if turn_order:
            lines.append("")
            lines.append(f"[dim]{turn_order}[/dim]")
        try:
            self.query_one("#combat-log", Static).update("\n".join(lines))
        except Exception:
            pass

    # ── overlay guard ────────────────────────────────────────────────────

    def _overlay_open(self) -> bool:
        return bool(self.query(".inv-overlay"))

    def _prompt_target(
        self,
        hostiles: List[Any],
        allies: List[Any],
        on_result,
        *,
        title: str,
        prefer_hostiles: bool,
        allow_multi: bool = False,
    ) -> None:
        if not hostiles and not allies:
            self.notify("No valid targets.", severity="warning")
            return
        self.mount(
            CombatTargetOverlay(
                hostiles,
                allies,
                on_result,
                title=title,
                prefer_hostiles=prefer_hostiles,
                allow_multi=allow_multi,
            )
        )

    # ── player actions: attack ───────────────────────────────────────────

    def action_attack(self) -> None:
        if not self._awaiting_player_input or self._overlay_open():
            return
        unit = self._active_unit
        hostiles = get_targets(self._sim, unit, want_enemies=True)
        allies = get_targets(self._sim, unit, want_enemies=False)

        def _on_result(targets: Optional[List[Any]]) -> None:
            if not targets:
                return
            self._awaiting_player_input = False
            res = perform_player_attack(self._sim, unit, targets)
            self._show_messages_then(res.get("messages", []), self._advance_turn)

        self._prompt_target(hostiles, allies, _on_result, title="Attack who?", prefer_hostiles=True)

    # ── player actions: ability ──────────────────────────────────────────

    def action_ability(self) -> None:
        if not self._awaiting_player_input or self._overlay_open():
            return
        unit = self._active_unit
        if is_silenced(unit):
            self.notify("Silenced — cannot use abilities.", severity="warning")
            return
        abilities = [a for a in (unit.entity.abilities or []) if a.ap_cost <= unit.entity.current_ap]
        if not abilities:
            self.notify("No usable abilities (check AP).", severity="warning")
            return
        entries = [(f"{a.name}  (cost {a.ap_cost} AP)", a) for a in abilities]

        def _on_menu_result(ability: Optional[Any]) -> None:
            if ability is None:
                return
            self._on_ability_chosen(ability)

        self.mount(CombatMenuOverlay("Choose ability", entries, _on_menu_result))

    def _on_ability_chosen(self, ability: Any) -> None:
        unit = self._active_unit
        hostiles = get_targets(self._sim, unit, want_enemies=True)
        allies = get_targets(self._sim, unit, want_enemies=False)
        prefer_hostiles = not is_beneficial_ability(ability)

        def _on_result(targets: Optional[List[Any]]) -> None:
            if not targets:
                return
            self._awaiting_player_input = False
            res = perform_player_ability(self._sim, unit, ability, targets)
            self._show_messages_then(res.get("messages", []), self._advance_turn)

        self._prompt_target(
            hostiles,
            allies,
            _on_result,
            title=f"Use {ability.name} on?",
            prefer_hostiles=prefer_hostiles,
            allow_multi=ability.can_aoe,
        )

    # ── player actions: item ─────────────────────────────────────────────

    def action_item(self) -> None:
        if not self._awaiting_player_input or self._overlay_open():
            return
        from game.objects.utility_item import UtilityItem  # noqa: PLC0415

        entries = [(idx, it) for idx, it in enumerate(self._pg.inventory) if isinstance(it, UtilityItem)]
        if not entries:
            self.notify("No usable items.", severity="warning")
            return
        menu_entries = [(f"{it.name} x{it.quantity}", (idx, it)) for idx, it in entries]

        def _on_menu_result(payload: Optional[Any]) -> None:
            if payload is None:
                return
            self._on_item_chosen(payload)

        self.mount(CombatMenuOverlay("Choose item", menu_entries, _on_menu_result))

    def _on_item_chosen(self, payload: Any) -> None:
        idx, item = payload
        unit = self._active_unit
        hostiles = get_targets(self._sim, unit, want_enemies=True)
        allies = get_targets(self._sim, unit, want_enemies=False)
        prefer_hostiles = not is_beneficial_item(item)

        def _on_result(targets: Optional[List[Any]]) -> None:
            if not targets:
                return
            self._awaiting_player_input = False
            res = perform_player_item(self._sim, unit, idx, targets)
            self._show_messages_then(res.get("messages", []), self._advance_turn)

        self._prompt_target(
            hostiles, allies, _on_result, title=f"Use {item.name} on?", prefer_hostiles=prefer_hostiles
        )

    # ── player actions: flee ─────────────────────────────────────────────

    def action_flee(self) -> None:
        if not self._awaiting_player_input or self._overlay_open():
            return
        unit = self._active_unit
        self._awaiting_player_input = False
        res = perform_player_escape(self._sim, unit)
        self._show_messages_then(res.get("messages", []), self._advance_turn)

    # ── action-bar button wiring (mouse support) ────────────────────────

    @on(Button.Pressed, "#btn-attack")
    def _btn_attack(self) -> None:
        self.action_attack()

    @on(Button.Pressed, "#btn-ability")
    def _btn_ability(self) -> None:
        self.action_ability()

    @on(Button.Pressed, "#btn-item")
    def _btn_item(self) -> None:
        self.action_item()

    @on(Button.Pressed, "#btn-flee")
    def _btn_flee(self) -> None:
        self.action_flee()