"""
AuthScreen: Login / Register / Guest menu.

Mirrors the choices offered by `old/console_game.py`'s `auth_menu()`
(Login, Register, Continue as guest), rebuilt as a `BaseScreen` with real
focusable/clickable widgets instead of a blocking `input()` loop.

By the time this screen is reached, `ServerSelectScreen` has already
configured the active save adapter (Local or Online) via
`tui.services.server_config` -- this screen only handles identity.
"""
from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Button, Static

from tui.screens.base_screen import BaseScreen


class AuthScreen(BaseScreen):
    """Menu screen offering Login, Register, or Guest access."""

    DEFAULT_CSS = """
    AuthScreen {
        align: center middle;
    }

    #auth-panel {
        width: 44;
        height: auto;
        border: round $accent;
        padding: 1 2;
    }

    #auth-title {
        text-align: center;
        text-style: bold;
        margin-bottom: 1;
    }

    #auth-panel Button {
        width: 1fr;
        margin-bottom: 1;
    }
    """

    def compose_content(self) -> ComposeResult:
        with Vertical(id="auth-panel"):
            yield Static("=== Authentication ===", id="auth-title")
            yield Button("Login", id="login", variant="primary")
            yield Button("Register", id="register")
            yield Button("Continue as Guest", id="guest")
            yield Button("Back", id="back")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "login":
            self.app.goto_screen("login")
        elif button_id == "register":
            self.app.goto_screen("register")
        elif button_id == "guest":
            self._continue_as_guest()
        elif button_id == "back":
            self.app.go_back()

    def _continue_as_guest(self) -> None:
        from tui.services.session import Session, set_session
        from tui.services.server_config import current_mode

        set_session(Session(mode=current_mode(), username=None, is_guest=True))
        self.notify("Continuing as guest.", title="Guest mode")
        self.app.goto_screen("main_menu")