"""
run_combat_sim.py — Development runner for isolated combat testing.

Boots directly into a series of `CombatScreen` encounters using the native
Textual TUI — no overworld, no auth, no save file required. The party and
hostile mob are generated from scratch using the same helpers as
`old/run_combat_simulator.py`, but rendered through the non-blocking
`tui/screens/combat_screen.py` instead of the legacy `readchar`-based loop.

Simulator loop behaviour (mirrors old/run_combat_simulator.py's
keep_going / players_won logic):
  - Party persists between fights if they won — same characters, same
    inventory, XP and levels carry forward.
  - Party is rebuilt from scratch on a loss (new seed, same CLI args).
  - After each fight a ConfirmScreen prompt asks "Fight again?" — No exits.
  - --escalate bumps the hostile level by +1 after each win so you can
    walk a party through ascending difficulty without changing CLI args.

Usage:
    python run_combat_sim.py
    python run_combat_sim.py --seed 42 --players 3 --level 5 --hostiles 4
    python run_combat_sim.py --level 10 --region DESERT --escalate
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Any, Optional

_THIS_DIR = os.path.dirname(__file__)

# Both this directory and old/ must be on sys.path so bare imports like
# `tui.app`, `game.objects.*`, and `run_combat_simulator` resolve —
# matching the bootstrap in run_dev_tui.py / run_tui.py.
sys.path.insert(0, _THIS_DIR)
sys.path.insert(0, os.path.join(_THIS_DIR, "old"))

from textual.app import App  # noqa: E402
from tui.screens.combat_screen import CombatScreen  # noqa: E402
from tui.screens.confirm_screen import ConfirmScreen  # noqa: E402
from tui.services.combat_service import (  # noqa: E402
    generate_test_hostiles,
    generate_test_party,
)

_STYLES_PATH = Path(_THIS_DIR) / "tui" / "styles" / "app.tcss"


class CombatSimApp(App):
    """Minimal Textual App that runs a looping combat simulator.

    Inherits from `App` directly — NOT `FractureApp` — so `FractureApp`'s
    `on_mount()` (which pushes `TitleScreen`) never fires. `BaseScreen`
    calls `self.app.go_back()`, so we add that one method explicitly.

    State machine
    ─────────────
    _pg           : Optional[PlayerGame]  — None forces a party rebuild
    _current_level: int                   — tracks escalating hostile level
    _fight_count  : int                   — total fights run this session

    on_mount()  → _start_encounter()
                      ↓
                  push CombatScreen
                      ↓ (dismiss)
    _on_combat_done(won)
      won  → push ConfirmScreen("Fight again?")  → _on_continue_choice
      lost → push ConfirmScreen("Defeated! Try again?") → _on_continue_choice

    _on_continue_choice(yes)
      yes, won  → if escalate, bump level → _start_encounter()
      yes, lost → rebuild party (_pg=None) → _start_encounter()
      no        → app.exit()
    """

    CSS_PATH = _STYLES_PATH

    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),
    ]

    def __init__(
        self,
        seed: int,
        num_players: int,
        level: int,
        num_hostiles: int,
        region_key: Optional[str],
        escalate: bool,
    ) -> None:
        super().__init__()
        self._seed = seed
        self._num_players = num_players
        self._base_level = level
        self._num_hostiles = num_hostiles
        self._region_key = region_key
        self._escalate = escalate

        # mutable simulator state
        self._pg: Optional[Any] = None
        self._current_level: int = level
        self._last_won: bool = False
        self._fight_count: int = 0

    # ── go_back: required by BaseScreen (and therefore CombatScreen) ─────

    def go_back(self) -> bool:
        """Pop the current screen. Returns True if a screen was popped."""
        if len(self.screen_stack) > 1:
            self.pop_screen()
            return True
        return False

    # ── lifecycle ────────────────────────────────────────────────────────

    def on_mount(self) -> None:
        self._start_encounter()

    # ── core loop ────────────────────────────────────────────────────────

    def _start_encounter(self) -> None:
        """Build or reuse the party, generate fresh hostiles, push CombatScreen."""
        if self._pg is None:
            # Offset seed by fight count so each rebuilt party is different.
            party_seed = self._seed + self._fight_count * 100
            self._pg = generate_test_party(party_seed, self._num_players, self._current_level)

        hostiles = generate_test_hostiles(
            self._current_level, self._num_hostiles, self._region_key
        )

        if not hostiles:
            self.notify(
                f"Could not generate hostiles (level={self._current_level}, "
                f"region={self._region_key!r}). Check the region key and try again.",
                severity="error",
                timeout=8,
            )
            self.set_timer(8.0, self.exit)
            return

        self._fight_count += 1
        self.push_screen(CombatScreen(self._pg, hostiles), self._on_combat_done)

    def _on_combat_done(self, players_won: bool | None) -> None:
        """Called by CombatScreen.dismiss() when the fight ends."""
        self._last_won = bool(players_won)

        if players_won:
            if self._escalate:
                self._current_level += 1
            msg = (
                f"Victory!  Fight {self._fight_count} complete."
                + (f"  Hostile level now {self._current_level}." if self._escalate else "")
                + "  Fight again?"
            )
        else:
            # Wipe the party so _start_encounter() rebuilds from scratch.
            self._pg = None
            self._current_level = self._base_level
            msg = "Defeated!  Party wiped — rebuild and try again?"

        self.push_screen(
            ConfirmScreen(msg, yes_label="Yes", no_label="Exit"),
            self._on_continue_choice,
        )

    def _on_continue_choice(self, confirmed: bool | None) -> None:
        """Called by ConfirmScreen.dismiss() with the player's yes/no choice."""
        if confirmed:
            self._start_encounter()
        else:
            self.exit()


# ── entry point ───────────────────────────────────────────────────────────────

def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fracture combat simulator — isolated TUI combat testing."
    )
    parser.add_argument(
        "--seed", type=int, default=86,
        help="RNG seed for party generation (default: 86).",
    )
    parser.add_argument(
        "--players", type=int, default=5,
        help="Number of party members to generate (default: 5).",
    )
    parser.add_argument(
        "--level", type=int, default=3,
        help="Starting level for both party and hostiles (default: 3).",
    )
    parser.add_argument(
        "--hostiles", type=int, default=3,
        help="Passed to the formation generator as the max hostile count (default: 3).",
    )
    parser.add_argument(
        "--region", type=str, default=None,
        metavar="REGION_KEY",
        help=(
            "Optional hostile-seed region key, e.g. DESERT or FOREST_SMALL_CITY. "
            "Omit to pick a random region each fight."
        ),
    )
    parser.add_argument(
        "--escalate", action="store_true", default=False,
        help="Bump hostile level by +1 after each win (simulates dungeon progression).",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    app = CombatSimApp(
        seed=args.seed,
        num_players=args.players,
        level=args.level,
        num_hostiles=args.hostiles,
        region_key=args.region,
        escalate=args.escalate,
    )
    app.run()


if __name__ == "__main__":
    main()