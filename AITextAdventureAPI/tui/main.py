"""
Main entry point for the TUI application.
"""
from tui.core.screen_manager import ScreenManager, ScreenType
from tui.screens.server_select_screen import ServerSelectScreen
from tui.screens.auth_screen import AuthScreen
from tui.screens.main_menu_screen import MainMenuScreen
from tui.screens.new_game_screen import NewGameScreen
from tui.screens.load_game_screen import LoadGameScreen


def main():
    """Initialize and run the TUI application."""
    manager = ScreenManager()

    # Register all screens
    manager.register_screen(ScreenType.SERVER_SELECT, ServerSelectScreen)
    manager.register_screen(ScreenType.AUTH, AuthScreen)
    manager.register_screen(ScreenType.MAIN_MENU, MainMenuScreen)
    manager.register_screen(ScreenType.NEW_GAME, NewGameScreen)
    manager.register_screen(ScreenType.LOAD_GAME, LoadGameScreen)

    # Start with server selection
    try:
        manager.run(ScreenType.SERVER_SELECT)
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
    except Exception as e:
        print(f"\n\nAn error occurred: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("\nThank you for playing Fracture!")


if __name__ == "__main__":
    main()