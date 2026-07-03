"""
ConfirmScreen: reusable Yes/No confirmation dialog.

Push it with a result callback, Textual's standard modal-result pattern:

    def handle_result(confirmed: bool | None) -> None:
        if confirmed:
            ...

    self.app.push_screen(ConfirmScreen("Exit Fracture?"), handle_result)

The Yes/No buttons call `self.dismiss(True/False)` directly. Pressing
Escape falls through to `BaseScreen`'s inherited `go_back` binding, which
pops this screen with no explicit result (`None`) — callers should treat
any falsy result as "cancelled".
"""
from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Static

from tui.screens.base_screen import BaseScreen


class ConfirmScreen(BaseScreen):
    """Modal-style Yes/No confirmation dialog."""

    show_header = False
    show_footer = False

    DEFAULT_CSS = """
    ConfirmScreen {
        align: center middle;
        background: $background 60%;
    }

    #confirm-panel {
        width: 50;
        height: auto;
        border: round $accent;
        padding: 1 2;
        background: $surface;
    }

    #confirm-message {
        text-align: center;
        margin-bottom: 1;
    }

    #confirm-buttons {
        align: center middle;
        height: auto;
    }

    #confirm-buttons Button {
        margin: 0 1;
    }
    """

    def __init__(self, message: str, *, yes_label: str = "Yes", no_label: str = "No") -> None:
        super().__init__()
        self._message = message
        self._yes_label = yes_label
        self._no_label = no_label

    def compose_content(self) -> ComposeResult:
        with Vertical(id="confirm-panel"):
            yield Static(self._message, id="confirm-message")
            with Horizontal(id="confirm-buttons"):
                yield Button(self._yes_label, id="yes", variant="primary")
                yield Button(self._no_label, id="no")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id == "yes")