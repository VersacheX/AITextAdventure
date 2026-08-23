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
  2. A blocked (petrify/stun/sleep) or confused unit auto-resolves
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

from textual import events, on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Static

from tui.screens.base_screen import BaseScreen
from tui.screens.combat_menu_overlay import CombatMenuOverlay, build_ability_detail, build_item_detail
from tui.screens.combat_target_overlay import CombatTargetOverlay
from tui.services.combat_renderer import (
    build_hostile_card_text,
    build_player_card_text,
    build_timeline_rows,
)
from tui.services.combat_service import (
    build_simulation,
    check_combat_over,
    distribute_rewards,
    get_blocking_status_result,
    get_dead_allies,
    get_next_ready_unit,
    get_targets,
    is_beneficial_ability,
    is_beneficial_item,
    is_confused,
    is_revive_item,
    is_silenced,
    is_unit_player,
    perform_auto_skip,
    perform_confused_action,
    perform_hostile_auto_action,
    perform_player_ability,
    perform_player_attack,
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
        Binding("a", "attack", "Attack", show=False),
        Binding("b", "ability", "A(b)ility", show=False),
        Binding("u", "item", "Item", show=False),
        Binding("up", "menu_up", "Up", show=False),
        Binding("down", "menu_down", "Down", show=False),
        Binding("enter", "menu_confirm", "Confirm", show=False),
        Binding("escape", "noop", "", show=False),  # disable base-class go_back in combat
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
        width: 26;
        height: 100%;
        border-right: solid $accent 40%;
        padding: 1;
        overflow-y: auto;
    }

    #actions-col {
        width: 18;
        height: 100%;
        border-right: solid $accent;
        padding: 1 0;
        background: $surface;
    }

    #actions-title {
        width: 100%;
        text-align: center;
        text-style: bold;
        color: $accent;
        padding: 0 1;
        margin-bottom: 1;
        border-bottom: solid $accent 40%;
    }

    .action-item {
        width: 100%;
        height: 1;
        padding: 0 2;
        color: $text;
    }

    .action-item.action-selected {
        background: $accent;
        color: $text;
        text-style: bold;
    }

    #hostiles-col {
        width: 26;
        height: 100%;
        border-left: solid $accent 40%;
        padding: 1;
        overflow-y: auto;
    }

    #center-col {
        width: 1fr;
        height: 100%;
        padding: 1;
        layout: vertical;
    }

    #combat-log {
        width: 100%;
        height: 1fr;
        overflow-y: auto;
    }

    #timeline {
        width: 100%;
        height: auto;
        border-top: solid $accent 40%;
        padding: 1 0 0 0;
        color: $text-muted;
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
        # Action panel state: display label (hotkey embedded in label text)
        self._ACTION_ENTRIES = [
            "Attack  (a)",
            "A(b)ility",
            "(U)se Item",
        ]
        self._action_index = 0  # currently highlighted row

    # ── compose ──────────────────────────────────────────────────────────

    def compose_content(self) -> ComposeResult:
        players = [u for u in self._sim.units if is_unit_player(u)]
        hostiles = [u for u in self._sim.units if not is_unit_player(u)]

        with Horizontal(id="combat-row"):
            with Vertical(id="players-col"):
                for u in players:
                    yield Static("", id=f"card-{u.entity._uuid}", classes="combat-card")
            with Vertical(id="actions-col"):
                yield Static("Actions", id="actions-title")
                for i, label in enumerate(self._ACTION_ENTRIES):
                    yield Static(
                        label,
                        id=f"action-row-{i}",
                        classes="action-item" + (" action-selected" if i == 0 else ""),
                    )
            with Vertical(id="center-col"):
                yield Static("", id="combat-log")
                yield Static("", id="timeline", markup=True)
            with Vertical(id="hostiles-col"):
                for u in hostiles:
                    yield Static("", id=f"card-{u.entity._uuid}", classes="combat-card")


    def on_mount(self) -> None:
        self._refresh_cards()
        self._refresh_action_panel()
        self._update_log()
        self._refresh_timeline()
        self.set_timer(0.4, self._advance_turn)

    # ── turn loop ────────────────────────────────────────────────────────

    def action_noop(self) -> None:
        """Intentional no-op — swallows escape so combat cannot be quit."""

    def _advance_turn(self) -> None:
        outcome = check_combat_over(self._sim)
        if outcome is not None:
            self._finish_combat(outcome)
            return

        unit = get_next_ready_unit(self._sim)
        if unit is None:
            self.set_timer(0.05, self._advance_turn)
            return

        # Timer normalisation has just run inside next_active_unit(), so
        # refresh the timeline now — values are correct for this moment.
        self._active_unit = unit
        self._refresh_cards()
        self._refresh_timeline()

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
            self._refresh_action_panel()
        else:
            res = perform_hostile_auto_action(self._sim, unit)
            self._show_messages_then(res.get("messages", []), self._advance_turn)

    def _finish_combat(self, players_won: bool) -> None:
        self._awaiting_player_input = False
        self._refresh_action_panel()
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
        try:
            self.query_one("#combat-log", Static).update("\n".join(lines))
        except Exception:
            pass

    def _refresh_timeline(self) -> None:
        """Rebuild the timeline inset — called after each full turn completes,
        not during per-message pacing, so values reflect post-advance_schedule
        state."""
        try:
            tl_widget = self.query_one("#timeline", Static)
            tl_width  = max(20, (tl_widget.size.width or 40) - 2)
            tl_lines  = build_timeline_rows(self._sim, tl_width)
            tl_widget.update("\n".join(tl_lines))
        except Exception:
            pass

    # ── action panel ─────────────────────────────────────────────────────

    def _refresh_action_panel(self) -> None:
        """Highlight the currently selected action row."""
        for i, label in enumerate(self._ACTION_ENTRIES):
            try:
                w = self.query_one(f"#action-row-{i}", Static)
                if i == self._action_index and self._awaiting_player_input:
                    w.update(f"[bold]▶ {label}[/bold]")
                    w.add_class("action-selected")
                else:
                    w.update(f"  {label}")
                    w.remove_class("action-selected")
            except Exception:
                pass

    def action_menu_up(self) -> None:
        if not self._awaiting_player_input or self._overlay_open():
            return
        self._action_index = (self._action_index - 1) % len(self._ACTION_ENTRIES)
        self._refresh_action_panel()

    def action_menu_down(self) -> None:
        if not self._awaiting_player_input or self._overlay_open():
            return
        self._action_index = (self._action_index + 1) % len(self._ACTION_ENTRIES)
        self._refresh_action_panel()

    def action_menu_confirm(self) -> None:
        if not self._awaiting_player_input or self._overlay_open():
            return
        _dispatch = [
            self.action_attack,
            self.action_ability,
            self.action_item,
        ]
        _dispatch[self._action_index]()

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
            self._refresh_action_panel()
            res = perform_player_attack(self._sim, unit, targets)
            self._refresh_timeline()
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
        cur_ap  = getattr(unit.entity, "current_ap", 0)
        entries = [(a.name, a) for a in abilities]

        def _on_menu_result(ability: Optional[Any]) -> None:
            if ability is None:
                return
            self._on_ability_chosen(ability)

        self.mount(CombatMenuOverlay(
            "Choose Ability",
            entries,
            _on_menu_result,
            detail_fn=lambda a: build_ability_detail(a, cur_ap),
        ))

    def _on_ability_chosen(self, ability: Any) -> None:
        unit = self._active_unit
        hostiles = get_targets(self._sim, unit, want_enemies=True)
        allies = get_targets(self._sim, unit, want_enemies=False)
        prefer_hostiles = not is_beneficial_ability(ability)

        def _on_result(targets: Optional[List[Any]]) -> None:
            if not targets:
                return
            self._awaiting_player_input = False
            self._refresh_action_panel()
            res = perform_player_ability(self._sim, unit, ability, targets)
            self._refresh_timeline()
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

        self.mount(CombatMenuOverlay(
            "Use Item",
            menu_entries,
            _on_menu_result,
            detail_fn=lambda p: build_item_detail(p[1]),
        ))

    def _on_item_chosen(self, payload: Any) -> None:
        idx, item = payload
        unit = self._active_unit

        # Revive items are friendly and may only target *fallen* allies, so
        # they bypass the normal alive-target roster entirely.
        if is_revive_item(item):
            dead_allies = get_dead_allies(self._sim, unit)
            if not dead_allies:
                self.notify("No fallen allies to revive.", severity="warning")
                return

            def _on_revive_result(targets: Optional[List[Any]]) -> None:
                if not targets:
                    return
                self._awaiting_player_input = False
                self._refresh_action_panel()
                res = perform_player_item(self._sim, unit, idx, targets)
                self._refresh_timeline()
                self._show_messages_then(res.get("messages", []), self._advance_turn)

            self._prompt_target(
                [],
                dead_allies,
                _on_revive_result,
                title=f"Revive who with {item.name}?",
                prefer_hostiles=False,
            )
            return

        hostiles = get_targets(self._sim, unit, want_enemies=True)
        allies = get_targets(self._sim, unit, want_enemies=False)
        prefer_hostiles = not is_beneficial_item(item)

        def _on_result(targets: Optional[List[Any]]) -> None:
            if not targets:
                return
            self._awaiting_player_input = False
            self._refresh_action_panel()
            res = perform_player_item(self._sim, unit, idx, targets)
            self._refresh_timeline()
            self._show_messages_then(res.get("messages", []), self._advance_turn)

        self._prompt_target(
            hostiles, allies, _on_result, title=f"Use {item.name} on?", prefer_hostiles=prefer_hostiles
        )

