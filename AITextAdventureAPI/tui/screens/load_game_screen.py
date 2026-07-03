"""
Load game screen: display saved games and load selection.
"""
from typing import Optional, Dict, Any, List
from tui.core.screen_manager import Screen, ScreenType
from tui.core.renderer import clear_screen, make_box, center_box_in_terminal
from tui.core.input_handler import InputHandler


class LoadGameScreen(Screen):
    """
    Load game selection screen.
    """

    def __init__(self, manager):
        super().__init__(manager)
        self.saves: List[Dict[str, Any]] = []

    def on_enter(self, context: Optional[Dict[str, Any]] = None) -> None:
        """Load save list when entering screen."""
        super().on_enter(context)
        self._load_saves()

    def _load_saves(self) -> None:
        """Fetch available saves."""
        try:
            from client_api_requests.load_game_service import load_player_games
            from client_api_requests.save_service_adapter import get_adapter

            adapter = get_adapter()
            self.saves = load_player_games(save_adapter=adapter) or []

        except Exception as e:
            print(f"Error loading saves: {e}")
            self.saves = []

    def render(self) -> None:
        """Render the load game screen."""
        clear_screen()

        # Title
        title = ["=== Load Game ===", ""]
        title_box = make_box(title, 80, center_content=True)

        # Saves list
        saves_content = [""]
        if not self.saves:
            saves_content.append("No saved games found.")
        else:
            for idx, save in enumerate(self.saves, start=1):
                name = save.get('name', 'Unknown')
                char = save.get('main_character', 'Unknown')
                level = save.get('level', 0)
                money = save.get('money', 0)
                updated = save.get('updated_at', 'Unknown')

                line = f"{idx}) {name} - {char} Lv.{level} ${money} ({updated})"
                saves_content.append(line)

        saves_content.append("")
        saves_content.append("Enter number to load, or ESC to cancel")

        saves_box = make_box(saves_content, 80)

        # Combine and center
        all_lines = title_box + [""] + saves_box
        centered = center_box_in_terminal(all_lines)

        for line in centered:
            print(line)

    def handle_input(self, key: Optional[str] = None) -> Optional[str]:
        """Handle load game input."""
        if key is None:
            key = InputHandler.get_key()

        if key == 'esc':
            return "pop"

        if key.isdigit() and self.saves:
            idx = int(key) - 1
            if 0 <= idx < len(self.saves):
                return self._load_save(self.saves[idx])

        return None

    def _load_save(self, save: Dict[str, Any]) -> Optional[str]:
        """Load the selected save."""
        try:
            from client_api_requests.load_game_service import load_player_game
            from client_api_requests.save_service_adapter import get_adapter

            adapter = get_adapter()
            save_id = save.get('id')

            print(f"\nLoading save {save_id}...")
            pg = load_player_game(save_id, save_adapter=adapter)

            if pg is None:
                print("Failed to load save.")
                input("Press Enter to continue...")
                return None

            print("Save loaded successfully!")
            input("Press Enter to continue...")

            # In full implementation, would transition to overworld
            # For now, return to menu
            return "pop"

        except Exception as e:
            print(f"\nError loading save: {e}")
            input("Press Enter to continue...")
            return None