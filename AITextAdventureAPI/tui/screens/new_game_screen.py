"""
NewGameScreen: create a fresh PlayerGame and enter the overworld.

Mirrors `old/console_game_gameloop.py`'s `new_game()`: prompt for a
character name, build a `Player` + `PlayerGame`, equip starting gear via
`combat_balancing_simulation.player_generator.equip_player_character`, and
generate the first region at the origin with `PlayerGame.create_region_at`
-- then hand off to `OverworldScreen` exactly like `LoadGameScreen` does
after a successful load (`set_active_game()` + `goto_screen("overworld")`).

Full Character Creation (class/focus selection) is a later roadmap item
(see `tui/screens/main_menu_screen.py`'s docstring) -- for now the starting
`ability_type_focus` matches the legacy hardcoded default ('technique').

Building the first region is procedural generation and can be slow, so it
runs in a background worker per project convention (see
`tui/screens/login_screen.py` / `tui/screens/load_game_screen.py`).
"""
from __future__ import annotations

from textual import work
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Button, Input, Static

from tui.screens.base_screen import BaseScreen


class NewGameScreen(BaseScreen):
    """Character name entry -> world generation -> Overworld handoff."""

    DEFAULT_CSS = """
    NewGameScreen {
        align: center middle;
    }

    #new-game-panel {
        width: 48;
        height: auto;
        border: round $accent;
        padding: 1 2;
    }

    #new-game-title {
        text-align: center;
        text-style: bold;
        margin-bottom: 1;
    }

    #new-game-panel Input {
        margin-bottom: 1;
    }

    #new-game-status {
        margin-bottom: 1;
        color: $text 60%;
        text-align: center;
    }

    #new-game-buttons {
        layout: horizontal;
    }

    #new-game-buttons Button {
        width: 1fr;
        margin-right: 1;
    }

    #new-game-buttons Button:last-child {
        margin-right: 0;
    }
    """

    def compose_content(self) -> ComposeResult:
        with Vertical(id="new-game-panel"):
            yield Static("=== New Game ===", id="new-game-title")
            yield Input(placeholder="Character name", id="char-name")
            yield Static("", id="new-game-status")
            with Vertical(id="new-game-buttons"):
                yield Button("Begin", id="submit", variant="primary")
                yield Button("Back", id="back")

    def on_mount(self) -> None:
        self.query_one("#char-name", Input).focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "submit":
            self._submit()
        elif event.button.id == "back":
            self.app.go_back()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id == "char-name":
            self._submit()

    def _submit(self) -> None:
        name = self.query_one("#char-name", Input).value.strip()
        status = self.query_one("#new-game-status", Static)
        if not name:
            status.update("Name cannot be empty.")
            return

        status.update("Please wait - building initial region...")
        self.query_one("#submit", Button).disabled = True
        self.query_one("#char-name", Input).disabled = True
        self._build_world(name)

    @work(thread=True)
    def _build_world(self, name: str) -> None:
        """Runs off the UI thread -- see module docstring.

        Mirrors `old/console_game_gameloop.py`'s `new_game()`: build the
        `Player` + `PlayerGame`, equip starting gear, add the character to
        the party, then generate the first region at the origin.
        """
        from game.objects.player import Player
        from game.objects.player_game import PlayerGame
        from combat_balancing_simulation.player_generator import equip_player_character

        try:
            # Create player at origin (0, 0, 0, inside=False)
            player = Player(name, 0, 0, 0, False)
            
            # Create world state container
            pg = PlayerGame()
            
            # Equip starting gear with 'technique' focus (hardcoded default)
            equip_player_character(player, pg, focus="technique")
            
            # Add character to the game (also adds to active party automatically)
            pg.add_character(player)
            
            # Build first region at origin (0,0)
            # This chooses a random initial region type and generates tiles
            pg.create_region_at((0, 0))
            
        except Exception as exc:  # noqa: BLE001 - surfaced to the user below
            self.app.call_from_thread(self._on_build_error, str(exc))
            return

        self.app.call_from_thread(self._on_build_success, pg)

    def _on_build_success(self, pg: object) -> None:
        """Called on the main thread after world generation completes.
        
        Sets the active game state and transitions to the overworld screen,
        matching the console game's flow after `new_game()` completes.
        """
        from tui.services.game_state import set_active_game

        set_active_game(pg)
        self.notify("World created. Welcome to Fracture.", title="New Game")
        self.app.goto_screen("overworld")

    def _on_build_error(self, message: str) -> None:
        """Called on the main thread if world generation fails."""
        self.notify(
            f"Could not create world: {message}",
            title="New Game",
            severity="error"
        )
        self.query_one("#new-game-status", Static).update(
            "An error occurred. Please try again."
        )
        self.query_one("#submit", Button).disabled = False
        self.query_one("#char-name", Input).disabled = False
