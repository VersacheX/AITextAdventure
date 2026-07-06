"""
MainMenuScreen: New Game / Load Game / Logout / Exit.

Mirrors `old/console_game.py`'s `main_menu()` choices, rebuilt as a
`BaseScreen` with real buttons instead of a blocking `input()` loop.
"New Game" links to `tui/screens/new_game_screen.py`, which mirrors
`old/console_game_gameloop.py`'s `new_game()` (full Character Creation
with class/focus selection is later on the roadmap); "Load Game" is fully
implemented in `tui/screens/load_game_screen.py` with a live, scrollable
save list.
"""
from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Button, Static

from tui.screens.base_screen import BaseScreen
from tui.screens.confirm_screen import ConfirmScreen
from tui.services.session import get_session


class MainMenuScreen(BaseScreen):
    """Main menu shown after authentication."""

    DEFAULT_CSS = """
    MainMenuScreen {
        align: center middle;
    }

    #menu-panel {
        width: 44;
        height: auto;
        border: round $accent;
        padding: 1 2;
    }

    #menu-title {
        text-align: center;
        text-style: bold;
    }

    #menu-identity {
        text-align: center;
        color: $text 60%;
        margin-bottom: 1;
    }

    #menu-panel Button {
        width: 1fr;
        margin-bottom: 1;
    }
    """

    def compose_content(self) -> ComposeResult:
        with Vertical(id="menu-panel"):
            yield Static("=== Fracture ===", id="menu-title")
            yield Static(self._identity_label(), id="menu-identity")
            yield Button("New Game", id="new_game", variant="primary")
            yield Button("Load Game", id="load_game")
            yield Button("Logout", id="logout")
            yield Button("Exit", id="exit")

    def on_screen_resume(self) -> None:
        # Refresh the identity label whenever this screen becomes active
        # again (e.g. after logging out and back in as someone else), not
        # just on first mount.
        self.query_one("#menu-identity", Static).update(self._identity_label())

    @staticmethod
    def _identity_label() -> str:
        session = get_session()
        if session is None:
            return "Not signed in"
        if session.is_guest:
            return f"Guest ({session.mode})"
        return f"{session.username} ({session.mode})"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "new_game":
            self.app.goto_screen("new_game")
        elif button_id == "load_game":
            self.app.goto_screen("load_game")
        elif button_id == "logout":
            self._logout()
        elif button_id == "exit":
            self._confirm_exit()

    def _logout(self) -> None:
        from client_api_requests.save_service_adapter import get_adapter
        from tui.services.game_state import set_active_game
        from tui.services.session import set_session

        try:
            get_adapter().logout()
        except RuntimeError:
            pass  # no adapter configured yet -- nothing to log out of

        set_session(None)
        set_active_game(None)
        self.notify("Logged out.", title="Logout")
        self.app.goto_screen("auth")

    def _confirm_exit(self) -> None:
        def handle_result(confirmed: bool | None) -> None:
            if confirmed:
                self.app.exit()

        self.app.push_screen(ConfirmScreen("Exit Fracture?"), handle_result)