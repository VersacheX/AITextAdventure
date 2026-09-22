"""
Simulation panel for the dev data-management screen.

Lets the developer configure a party + hostile mob from seed data, then run
a CombatSimulation and inspect the round-by-round log — all without leaving
the TUI.
"""
from __future__ import annotations

from typing import Any, List, Optional

from rich.markup import escape as rich_escape
from textual import work
from textual.app import ComposeResult
from textual.containers import Horizontal, ScrollableContainer, Vertical
from textual.widgets import Button, Input, Label, ListItem, ListView, Select, Static

# ── helpers ──────────────────────────────────────────────────────────────────

_FOCUSES = ["technique", "spirit", "magic", "tech", "skill"]
_REGIONS = [
    "DESERT", "FOREST", "GRASSLAND", "MOUNTAINS", "SHALLOWS", "SNOW", "SWAMP",
]

_PARTY_SIZES  = ["1", "2", "3", "4", "5"]
_MOB_SIZES    = ["1", "2", "3", "4"]
_LEVELS       = [str(i) for i in range(1, 31)]


class SimulationPanel(Vertical):
    """Full-replacement widget for #dm-detail-panel when the Simulation tab is active."""

    DEFAULT_CSS = """
    SimulationPanel {
        width: 100%;
        height: 100%;
        padding: 1 2;
        overflow-y: auto;
    }

    #sim-config-row {
        height: auto;
        width: 100%;
        margin-bottom: 1;
    }

    #sim-party-col, #sim-hostile-col {
        width: 1fr;
        height: auto;
        border: solid $accent 30%;
        padding: 1 1;
        margin-right: 1;
    }

    #sim-hostile-col {
        margin-right: 0;
    }

    .sim-section-header {
        width: 100%;
        height: 1;
        text-style: bold;
        color: $accent;
        margin-bottom: 1;
    }

    .sim-row {
        height: auto;
        width: 100%;
        margin-bottom: 1;
        align: left middle;
    }

    .sim-label {
        width: 12;
        content-align: left middle;
        color: $text 70%;
    }

    SimulationPanel Select {
        width: 1fr;
    }

    SimulationPanel Input {
        width: 1fr;
    }

    #sim-run-btn {
        margin-top: 1;
        width: 100%;
        min-width: 12;
    }

    #sim-log-header {
        height: 1;
        text-style: bold;
        color: $accent;
        margin-top: 1;
        margin-bottom: 1;
    }

    #sim-log {
        height: 1fr;
        min-height: 12;
        border: solid $accent 20%;
        padding: 0 1;
        overflow-y: auto;
    }

    #sim-status {
        height: 1;
        color: $text 60%;
        margin-top: 1;
    }
    """

    def compose(self) -> ComposeResult:
        with Horizontal(id="sim-config-row"):
            with Vertical(id="sim-party-col"):
                yield Static("── Party ──", classes="sim-section-header")
                with Horizontal(classes="sim-row"):
                    yield Label("Size", classes="sim-label")
                    yield Select(
                        [(s, s) for s in _PARTY_SIZES],
                        value="1",
                        id="sim-party-size",
                        allow_blank=False,
                    )
                with Horizontal(classes="sim-row"):
                    yield Label("Level", classes="sim-label")
                    yield Select(
                        [(l, l) for l in _LEVELS],
                        value="10",
                        id="sim-party-level",
                        allow_blank=False,
                    )
                with Horizontal(classes="sim-row"):
                    yield Label("Focus", classes="sim-label")
                    yield Select(
                        [(f.title(), f) for f in _FOCUSES],
                        value="technique",
                        id="sim-party-focus",
                        allow_blank=False,
                    )

            with Vertical(id="sim-hostile-col"):
                yield Static("── Hostiles ──", classes="sim-section-header")
                with Horizontal(classes="sim-row"):
                    yield Label("Region", classes="sim-label")
                    yield Select(
                        [(r.title(), r) for r in _REGIONS],
                        value="FOREST",
                        id="sim-hostile-region",
                        allow_blank=False,
                    )
                with Horizontal(classes="sim-row"):
                    yield Label("Count", classes="sim-label")
                    yield Select(
                        [(s, s) for s in _MOB_SIZES],
                        value="1",
                        id="sim-hostile-count",
                        allow_blank=False,
                    )
                with Horizontal(classes="sim-row"):
                    yield Label("Level", classes="sim-label")
                    yield Select(
                        [(l, l) for l in _LEVELS],
                        value="10",
                        id="sim-hostile-level",
                        allow_blank=False,
                    )

        yield Button("▶  Run Simulation", id="sim-run-btn", variant="success")
        yield Static("── Combat Log ──", id="sim-log-header")
        yield ScrollableContainer(
            Static("Configure party and hostiles, then press Run.", id="sim-log-text"),
            id="sim-log",
        )
        yield Static("", id="sim-status")

    # ── public API ────────────────────────────────────────────────────────

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "sim-run-btn":
            event.stop()
            self._run_simulation()

    # ── internal ─────────────────────────────────────────────────────────

    def _get_select_value(self, select_id: str, fallback: str) -> str:
        try:
            sel = self.query_one(f"#{select_id}", Select)
            v = sel.value
            return str(v) if v is not None and v != Select.BLANK else fallback
        except Exception:
            return fallback

    @work(thread=True, exclusive=True)
    def _run_simulation(self) -> None:
        self.app.call_from_thread(self._set_status, "Running…")
        self.app.call_from_thread(self._set_log, "[dim]Initialising…[/dim]")
        try:
            lines = _execute_simulation(
                party_size   = int(self._get_select_value("sim-party-size",  "1")),
                party_level  = int(self._get_select_value("sim-party-level", "10")),
                party_focus  = self._get_select_value("sim-party-focus", "technique"),
                region       = self._get_select_value("sim-hostile-region", "FOREST"),
                hostile_count = int(self._get_select_value("sim-hostile-count", "1")),
                hostile_level = int(self._get_select_value("sim-hostile-level", "10")),
            )
        except Exception as exc:  # noqa: BLE001
            lines = [f"[red]Simulation error: {rich_escape(str(exc))}[/red]"]

        self.app.call_from_thread(self._set_log, "\n".join(lines))
        self.app.call_from_thread(self._set_status, "Done.")

    def _set_log(self, markup: str) -> None:
        try:
            self.query_one("#sim-log-text", Static).update(markup)
        except Exception:
            pass

    def _set_status(self, text: str) -> None:
        try:
            self.query_one("#sim-status", Static).update(f"[dim]{rich_escape(text)}[/dim]")
        except Exception:
            pass


# ── simulation runner (pure logic, called from worker thread) ────────────────

def _execute_simulation(
    *,
    party_size: int,
    party_level: int,
    party_focus: str,
    region: str,
    hostile_count: int,
    hostile_level: int,
) -> List[str]:
    from combat_balancing_simulation.player_generator import generate_player  # noqa: PLC0415
    from combat_balancing_simulation.run_hostile_generator import pick_hostiles_from_region  # noqa: PLC0415
    from combat_balancing_simulation.combat_simulator import CombatSimulation  # noqa: PLC0415
    from combat_balancing_simulation.hostile_ai_service import decide_action  # noqa: PLC0415
    from game.objects.player_game import PlayerGame  # noqa: PLC0415

    _FOCUSES_CYCLE = ["technique", "spirit", "magic", "tech", "skill"]

    # ── Build party ───────────────────────────────────────────────────────
    pg = PlayerGame()
    players = []
    for i in range(max(1, party_size)):
        focus = _FOCUSES_CYCLE[i % len(_FOCUSES_CYCLE)] if i > 0 else party_focus
        p = generate_player(
            name=f"P{i + 1}_{focus[:3].title()}",
            focus=focus,
            target_level=party_level,
            player_game=pg,
        )
        players.append(p)
        pg.party.append(p)

    # ── Build hostiles ────────────────────────────────────────────────────
    hostiles = pick_hostiles_from_region(
        count=max(1, hostile_count),
        region=region,
        level=hostile_level,
    )
    if not hostiles:
        return [f"[yellow]No hostiles found for region '{region}' at level {hostile_level}.[/yellow]"]

    # ── Run simulation ────────────────────────────────────────────────────
    sim   = CombatSimulation(pg, hostiles)
    lines: List[str] = []

    # Header
    party_names  = ", ".join(rich_escape(p.name) for p in players)
    hostile_names = ", ".join(rich_escape(h.name) for h in hostiles)
    lines.append(f"[bold]Party   :[/bold]  {party_names}  (Lv.{party_level}  {party_focus.title()})")
    lines.append(f"[bold]Hostiles:[/bold]  {hostile_names}  (region: {region}  Lv.{hostile_level})")
    lines.append("")

    MAX_ROUNDS = 300
    round_num  = 0

    while round_num < MAX_ROUNDS:
        unit = sim.next_active_unit()
        if unit is None:
            break

        if not sim.is_player_annhilation() and not sim.is_hostile_annhilation():
            break
        if sim.is_player_annhilation() and not sim.is_hostile_annhilation():
            break

        entity = unit.entity
        is_player = unit._is_player()

        if is_player:
            # simple AI: basic attack the first alive hostile
            target = next((u.entity for u in sim.units if not u._is_player() and u.is_alive()), None)
            if target is None:
                break
            action = {"type": "basic_attack", "target": target}
        else:
            # hostile AI
            alive_players = [u.entity for u in sim.units if u._is_player() and u.is_alive()]
            if not alive_players:
                break
            action = decide_action(entity, alive_players, pg)

        result = sim.perform_unit_action(unit, action)
        unit.advance_schedule()
        round_num += 1

        if result:
            actor  = rich_escape(str(getattr(entity, "name", "?")))
            rtype  = str(result.get("type", ""))
            target_name = rich_escape(str(getattr(result.get("target"), "name", "?")) if result.get("target") else "?")
            dmg    = result.get("damage", 0)
            if rtype == "basic_attack":
                lines.append(f"  [cyan]R{round_num:>3}[/cyan]  {actor} → {target_name}  dmg [red]{dmg}[/red]")
            elif rtype == "ability":
                aname = rich_escape(str(result.get("ability_name", "")))
                lines.append(f"  [cyan]R{round_num:>3}[/cyan]  {actor} uses [yellow]{aname}[/yellow] → {target_name}  dmg [red]{dmg}[/red]")
            else:
                lines.append(f"  [cyan]R{round_num:>3}[/cyan]  {actor}: {rich_escape(str(result))}")

        # Check end conditions
        players_alive   = sim.is_player_annhilation()
        hostiles_alive  = sim.is_hostile_annhilation()
        if not players_alive or not hostiles_alive:
            break

    # ── Outcome ───────────────────────────────────────────────────────────
    lines.append("")
    players_alive  = sim.is_player_annhilation()
    hostiles_alive = sim.is_hostile_annhilation()

    if players_alive and not hostiles_alive:
        lines.append("[green bold]Result: PARTY WINS[/green bold]")
    elif hostiles_alive and not players_alive:
        lines.append("[red bold]Result: PARTY WIPED[/red bold]")
    elif round_num >= MAX_ROUNDS:
        lines.append("[yellow]Result: MAX ROUNDS REACHED (draw)[/yellow]")
    else:
        lines.append("[dim]Result: Combat ended[/dim]")

    lines.append(f"[dim]Rounds: {round_num}[/dim]")
    return lines