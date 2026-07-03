"""
New game screen: character creation and setup.
"""
from typing import Optional, Dict, Any
from tui.core.screen_manager import Screen, ScreenType
from tui.core.renderer import clear_screen, make_box, center_box_in_terminal
from tui.core.input_handler import InputHandler


class NewGameScreen(Screen):
    """
    New game character creation screen.
    """

    def __init__(self, manager):
        super().__init__(manager)
        self.character_name: Optional[str] = None

    def render(self) -> None:
        """Render the new game screen."""
        clear_screen()

        # Title
        title = ["=== New Game ===", ""]
        title_box = make_box(title, 60, center_content=True)

        centered = center_box_in_terminal(title_box)
        for line in centered:
            print(line)

    def handle_input(self, key: Optional[str] = None) -> Optional[str]:
        """Handle new game setup."""
        # Get character name
        print("\nCharacter Creation")
        name = InputHandler.get_text("Enter your character name: ", 
                                     validator=lambda x: len(x) > 0)

        if not name:
            print("Name cannot be empty.")
            input("Press Enter to try again...")
            return None

        print(f"\nCreating character: {name}")
        print("Please wait - Building initial world...")

        try:
            from game.objects.player import Player
            from game.objects.player_game import PlayerGame
            from combat_balancing_simulation.player_generator import equip_player_character

            # Create player
            player = Player(name, 0, 0, 0, False)

            # Create game state
            pg = PlayerGame()
            equip_player_character(player, pg, focus='technique')
            pg.add_character(player)

            # Generate initial region
            pg.create_region_at((0, 0))

            print("World created successfully!")
            input("Press Enter to begin your adventure...")

            # Transition to overworld
            context = {"player_game": pg}
            # Note: In full implementation, would push overworld screen
            # For now, return to menu
            return "pop"

        except Exception as e:
            print(f"\nError creating game: {e}")
            input("Press Enter to return...")
            return "pop"