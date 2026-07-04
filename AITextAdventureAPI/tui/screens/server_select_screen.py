"""
ServerSelectScreen: choose Local (SQLite) or Online (API server) play mode.

This is the screen `old/console_game.py`'s `auth_menu()` prompted for
inline ("1) Play Local" / "2) Play Online") before showing Login/Register.
It is now its own step in the navigation stack, pushed by `TitleScreen`
before "auth", and is solely responsible for calling
`tui.services.server_config` to configure the save adapter --
`AuthScreen`/`LoginScreen` no longer default to a local adapter themselves.

Choosing "Play Local" configures and proceeds immediately. Choosing
"Play Online" verifies the server is reachable (in a background worker,
per project convention) before proceeding, so a typo'd/unreachable URL is
caught here with a clear message instead of surfacing as a confusing
failure on the Login screen.
"""
from __future__ import annotations

from textual import work
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Input, Static

from tui.screens.base_screen import BaseScreen
from tui.services.server_config import (
    DEFAULT_ONLINE_BASE_URL,
    configure_local,
    configure_online,
    test_online_connection,
)


class ServerSelectScreen(BaseScreen):
    """Local vs. Online play-mode selection."""

    DEFAULT_CSS = """
    ServerSelectScreen {
        align: center middle;
    }

    #server-panel {
        width: 56;
        height: auto;
        border: round $accent;
        padding: 1 2;
    }

    #server-title {
        text-align: center;
        text-style: bold;
        margin-bottom: 1;
    }

    #server-subtitle {
        text-align: center;
        color: $text 60%;
        margin-bottom: 1;
    }

    #mode-buttons {
        height: auto;
        margin-bottom: 1;
    }

    #mode-buttons Button {
        width: 1fr;
        margin-right: 1;
    }

    #online-url {
        margin-bottom: 1;
    }

    #server-status {
        margin-bottom: 1;
        color: $error;
        text-align: center;
    }
    """

    def compose_content(self) -> ComposeResult:
        with Vertical(id="server-panel"):
            yield Static("=== Server Selection ===", id="server-title")
            yield Static("Play using a local save file, or connect to a server.", id="server-subtitle")
            with Horizontal(id="mode-buttons"):
                yield Button("Play Local", id="local", variant="primary")
                yield Button("Play Online", id="online")
            yield Input(value=DEFAULT_ONLINE_BASE_URL, placeholder="Server URL", id="online-url")
            yield Static("", id="server-status")
            yield Button("Back", id="back")

    def on_mount(self) -> None:
        self.query_one("#local", Button).focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == "local":
            self._choose_local()
        elif button_id == "online":
            self._choose_online()
        elif button_id == "back":
            self.app.go_back()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id == "online-url":
            self._choose_online()

    def _set_controls_disabled(self, disabled: bool) -> None:
        self.query_one("#local", Button).disabled = disabled
        self.query_one("#online", Button).disabled = disabled
        self.query_one("#online-url", Input).disabled = disabled

    def _choose_local(self) -> None:
        configure_local()
        self.notify("Local save mode configured.", title="Server Selection")
        self.app.goto_screen("auth")

    def _choose_online(self) -> None:
        url = self.query_one("#online-url", Input).value.strip() or DEFAULT_ONLINE_BASE_URL
        self.query_one("#server-status", Static).update("Connecting...")
        self._set_controls_disabled(True)
        self._connect_online(url)

    @work(thread=True)
    def _connect_online(self, url: str) -> None:
        """Runs off the UI thread -- see `tui/screens/login_screen.py` for
        the reference pattern this follows."""
        ok, message = test_online_connection(url)
        if not ok:
            self.app.call_from_thread(self._on_connect_error, message)
            return

        configure_online(url)
        self.app.call_from_thread(self._on_connect_success)

    def _on_connect_success(self) -> None:
        self.notify("Connected to server.", title="Server Selection")
        self.app.goto_screen("auth")

    def _on_connect_error(self, message: str) -> None:
        self.query_one("#server-status", Static).update(f"Could not reach server: {message}")
        self._set_controls_disabled(False)