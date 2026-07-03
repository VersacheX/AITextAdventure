"""
Main menu screen: new game, load game, logout, exit.
"""
from typing import Optional, Dict, Any
from tui.core.screen_manager import Screen, ScreenType
from tui.core.renderer import clear_screen, make_box, center_box_in_terminal
from tui.core.input_handler import InputHandler


class MainMenuScreen(Screen):
    """
    Main menu after authentication.
    """

    def __init__(self, manager):
        super().__init__(manager)
        self.options = [
            ("1", "New Game", "new_game"),
            ("2", "Load Game", "load_game"),
            ("3", "Logout", "logout"),
            ("Q", "Exit", "exit")
        ]

    def render(self) -> None:
        """Render the main menu."""
        clear_screen()

        # Title
        title = ["=== Fracture ===", "", "Main Menu:"]
        title_box = make_box(title, 60, center_content=True)

        # Options
        options_content = [""]
        for key, label, _ in self.options:
            options_content.append(f"{key}) {label}")
        options_content.append("")

        options_box = make_box(options_content, 60)

        # Combine and center
        all_lines = title_box + [""] + options_box
        centered = center_box_in_terminal(all_lines)

        for line in centered:
            print(line)

    def handle_input(self, key: Optional[str] = None) -> Optional[str]:
        """Handle main menu input."""
        if key is None:
            key = InputHandler.get_key()

        for opt_key, label, action in self.options:
            if key == opt_key.lower():
                if action == "exit":
                    if InputHandler.get_confirmation("Exit game? (y/n): "):
                        self.manager.quit()
                    return None

                elif action == "logout":
                    print("\nLogging out...")
                    input("Press Enter to continue...")
                    return "replace:auth"

                elif action == "new_game":
                    return "push:new_game"

                elif action == "load_game":
                    return "push:load_game"

        return None