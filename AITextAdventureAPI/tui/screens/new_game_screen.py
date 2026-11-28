"""
NewGameScreen: create a fresh PlayerGame and enter the overworld.

Mirrors `old/console_game_gameloop.py`'s `new_game()`: prompt for a
character name, choose a class, build a `Player` + `PlayerGame`, equip
starting gear via
`combat_balancing_simulation.player_generator.equip_player_character`, and
generate the first region at the origin with `PlayerGame.create_region_at`
-- then hand off to `OverworldScreen` exactly like `LoadGameScreen` does
after a successful load (`set_active_game()` + `goto_screen("overworld")`).

Class selection (IMPLEMENTATION_SPEC_custom_character_class.md): the hero
picks one of the five classes from `CLASS_LEVEL1_STATS` on this screen.
`apply_class_curve()` sets level-1 stats/HP/AP from that class's curve, and
`equip_player_character(..., focus=cls)` gives the matching starting gear.
The hero keeps access to every element (`elements_base` stays empty).
"""
from __future__ import annotations

from textual import work
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Button, Input, RadioButton, RadioSet, Static

from tui.screens.base_screen import BaseScreen

# One-line role description per class, shown under the picker. Kept here
# (not in game/constants) since it's presentation-only flavor text.
_CLASS_ROLES: dict[str, str] = {
    "technique": "Front line: high HP, heavy physical hits (STR / CON)",
    "spirit": "Healing, protection and revives (INT / CON)",
    "magic": "Elemental and area damage (INT)",
    "tech": "Devices and precise elemental attacks (INT / DEX)",
    "skill": "Speed and precision strikes (DEX / STR)",
}
_CLASS_LABELS: dict[str, str] = {
    "technique": "Technique",
    "spirit": "Spirit",
    "magic": "Magic",
    "tech": "Tech",
    "skill": "Skill",
}
_DEFAULT_CLASS = "technique"


def _class_order() -> list[str]:
    """Return the class ids from `CLASS_LEVEL1_STATS`, in display order."""
    from game.region_seeds.player_abilities.ability_requirements import CLASS_LEVEL1_STATS

    order = ["technique", "spirit", "magic", "tech", "skill"]
    return [c for c in order if c in CLASS_LEVEL1_STATS] or list(CLASS_LEVEL1_STATS.keys())


class NewGameScreen(BaseScreen):
    """Character name + class entry -> world generation -> Overworld handoff."""

    DEFAULT_CSS = """
    NewGameScreen {
        align: center middle;
    }

    #new-game-panel {
        width: 60;
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

    #class-label {
        margin-bottom: 1;
    }

    #char-class {
        margin-bottom: 1;
        height: auto;
    }

    #class-role {
        margin-bottom: 1;
        color: $text 70%;
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
            yield Static("Class:", id="class-label")
            with RadioSet(id="char-class"):
                for cls in _class_order():
                    yield RadioButton(
                        _CLASS_LABELS.get(cls, cls.capitalize()),
                        value=(cls == _DEFAULT_CLASS),
                        id=f"class-{cls}",
                    )
            yield Static(_CLASS_ROLES.get(_DEFAULT_CLASS, ""), id="class-role")
            yield Static("", id="new-game-status")
            with Vertical(id="new-game-buttons"):
                yield Button("Begin", id="submit", variant="primary")
                yield Button("Back", id="back")

    def on_mount(self) -> None:
        self.query_one("#char-name", Input).focus()

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        if event.radio_set.id != "char-class":
            return
        cls = self._selected_class()
        self.query_one("#class-role", Static).update(_CLASS_ROLES.get(cls, ""))

    def _selected_class(self) -> str:
        radio_set = self.query_one("#char-class", RadioSet)
        pressed = radio_set.pressed_button
        if pressed is not None and pressed.id:
            return pressed.id.removeprefix("class-")
        return _DEFAULT_CLASS

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

        cls = self._selected_class()
        status.update("Please wait - building initial region...")
        self.query_one("#submit", Button).disabled = True
        self.query_one("#char-name", Input).disabled = True
        self.query_one("#char-class", RadioSet).disabled = True
        self._build_world(name, cls)

    @work(thread=True)
    def _build_world(self, name: str, cls: str) -> None:
        """Runs off the UI thread -- see module docstring.

        Mirrors `old/console_game_gameloop.py`'s `new_game()`: build the
        `Player` + `PlayerGame`, apply the chosen class's level-1 curve,
        equip starting gear for that class, add the character to the party,
        then generate the first region at the origin.
        """
        from game.objects.player import Player, apply_class_curve
        from game.objects.player_game import PlayerGame
        from combat_balancing_simulation.player_generator import equip_player_character

        try:
            # Create player at origin (0, 0, 0, inside=False)
            player = Player(name, 0, 0, 0, False)

            # Create world state container
            pg = PlayerGame()

            # Apply the chosen class's level-1 stat/HP/AP curve.
            apply_class_curve(player, cls, 1)
            # apply_class_curve zeroes ability slots; a new character starts with 1.
            player.unused_ability_slots = 1
            # Custom hero: keep access to every element (for now).
            player.elements_base = []

            # Equip starting gear matching the chosen class
            equip_player_character(player, pg, focus=cls)

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
        self.query_one("#char-class", RadioSet).disabled = False
