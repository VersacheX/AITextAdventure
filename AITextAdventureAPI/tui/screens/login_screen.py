"""
LoginScreen / RegisterScreen: username+password form used for both signing
in and creating a new account.

Both screens share this single implementation (`RegisterScreen` just sets
`MODE = "register"`) since the form shape is identical — only the title,
button label, and which `SaveService` method gets called differ.

The actual `adapter.login()` / `adapter.register()` call is blocking I/O
(HTTP request or local SQLite access, depending on which adapter is
configured — see `client_api_requests.save_services`). Per project
convention, that call runs in a background worker (`@work(thread=True)`)
so a slow/unreachable server cannot freeze the compositor; the result is
marshaled back to the UI thread with `self.app.call_from_thread(...)`.
"""
from __future__ import annotations

from textual import work
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Button, Input, Static

from tui.screens.base_screen import BaseScreen
from tui.services.adapter_bootstrap import current_adapter_mode, ensure_default_local_adapter


class LoginScreen(BaseScreen):
    """Username/password form. Set `MODE = "register"` on a subclass to
    reuse this as the registration form instead."""

    MODE: str = "login"

    DEFAULT_CSS = """
    LoginScreen {
        align: center middle;
    }

    #form-panel {
        width: 48;
        height: auto;
        border: round $accent;
        padding: 1 2;
    }

    #form-title {
        text-align: center;
        text-style: bold;
        margin-bottom: 1;
    }

    #form-panel Input {
        margin-bottom: 1;
    }

    #form-status {
        margin-bottom: 1;
        color: $error;
        text-align: center;
    }

    #form-buttons Button {
        width: 1fr;
        margin-right: 1;
    }
    """

    def compose_content(self) -> ComposeResult:
        title = "=== Login ===" if self.MODE == "login" else "=== Register ==="
        submit_label = "Login" if self.MODE == "login" else "Register"

        with Vertical(id="form-panel"):
            yield Static(title, id="form-title")
            yield Input(placeholder="Username", id="username")
            yield Input(placeholder="Password", password=True, id="password")
            yield Static("", id="form-status")
            with Vertical(id="form-buttons"):
                yield Button(submit_label, id="submit", variant="primary")
                yield Button("Back", id="back")

    def on_mount(self) -> None:
        # TEMPORARY: see tui/services/adapter_bootstrap.py.
        ensure_default_local_adapter()
        self.query_one("#username", Input).focus()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "submit":
            self._submit()
        elif event.button.id == "back":
            self.app.go_back()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        # Enter in the username field moves to password; Enter in password submits.
        if event.input.id == "username":
            self.query_one("#password", Input).focus()
        elif event.input.id == "password":
            self._submit()

    def _submit(self) -> None:
        username = self.query_one("#username", Input).value.strip()
        password = self.query_one("#password", Input).value

        status = self.query_one("#form-status", Static)
        if not username or not password:
            status.update("Username and password are required.")
            return

        status.update("Working...")
        self.query_one("#submit", Button).disabled = True
        self._do_submit(username, password)

    @work(thread=True)
    def _do_submit(self, username: str, password: str) -> None:
        """Runs off the UI thread — see module docstring."""
        from client_api_requests.save_service_adapter import get_adapter

        try:
            adapter = get_adapter()
            if self.MODE == "register":
                adapter.register(username, password)
            adapter.login(username, password)
        except Exception as exc:  # noqa: BLE001 - surfaced to the user below
            self.app.call_from_thread(self._on_submit_error, str(exc))
            return

        self.app.call_from_thread(self._on_submit_success, username)

    def _on_submit_success(self, username: str) -> None:
        from tui.services.session import Session, set_session

        set_session(Session(mode=current_adapter_mode(), username=username, is_guest=False))
        verb = "Logged in" if self.MODE == "login" else "Registered and logged in"
        self.notify(f"{verb} as {username}.", title="Success")
        self.app.goto_screen("main_menu")

    def _on_submit_error(self, message: str) -> None:
        verb = "Login" if self.MODE == "login" else "Registration"
        self.query_one("#form-status", Static).update(f"{verb} failed: {message}")
        self.query_one("#submit", Button).disabled = False


class RegisterScreen(LoginScreen):
    """Registration form — identical to `LoginScreen` except for `MODE`."""

    MODE = "register"