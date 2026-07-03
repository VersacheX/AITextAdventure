"""
GameState: process-wide singleton holding the currently active PlayerGame.

Populated by `LoadGameScreen` after successfully loading + unpickling a
save (and, later, by New Game / Character Creation once implemented).
Downstream screens that don't exist yet (Overworld, Combat, Inventory)
will read the active game from here instead of having a `PlayerGame`
threaded through every `push_screen()` call in the stack.
"""
from __future__ import annotations

from typing import Any, Optional

_active_game: Optional[Any] = None  # Optional[PlayerGame]


def set_active_game(player_game: Optional[Any]) -> None:
    """Set (or clear, with None) the currently active PlayerGame."""
    global _active_game
    _active_game = player_game


def get_active_game() -> Optional[Any]:
    """Return the currently active PlayerGame, or None if none is loaded."""
    return _active_game