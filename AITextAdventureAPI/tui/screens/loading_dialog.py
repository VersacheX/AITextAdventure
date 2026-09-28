"""
LoadingDialog: a small non-interactive overlay shown while a "busy" task
event (dungeon generation, intro-story completion, etc.) runs on a
background worker.

Unlike MessageDialog, this widget:
  - takes no player input and cannot be dismissed by a keypress
  - is removed programmatically by the screen once player_game.is_busy
    clears, never by the widget itself
"""
from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Static


class LoadingDialog(Container):
    """Centered "Loading..." indicator mounted inside #map-panel."""

    DEFAULT_CSS = """
    LoadingDialog {
        layer: overlay;
        width: 100%;
        height: 100%;
        align: center middle;
        background: $background 60%;
    }
    LoadingDialog .loading-box {
        width: auto;
        height: auto;
        background: $panel;
        border: round $accent;
        padding: 1 3;
        color: $text;
        text-style: bold;
        text-align: center;
    }
    """

    def __init__(self, message: str = "Loading...") -> None:
        super().__init__()
        self._message = message or "Loading..."

    def compose(self) -> ComposeResult:
        yield Static(self._message, classes="loading-box")

