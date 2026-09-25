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
from textual.containers import Center
from textual.widgets import Static


class LoadingDialog(Static):
    """Centered "Loading..." indicator mounted inside #map-panel."""

    DEFAULT_CSS = """
    LoadingDialog {
        layer: overlay;
        width: 100%;
        height: 100%;
        align: center middle;
        background: $background 60%;
    }
    LoadingDialog > Center {
        width: auto;
        height: auto;
    }
    LoadingDialog .loading-box {
        background: $panel;
        border: round $accent;
        padding: 1 3;
        color: $text;
        text-style: bold;
    }
    """

    def __init__(self, message: str = "Loading...") -> None:
        super().__init__()
        self._message = message

    def compose(self) -> ComposeResult:
        with Center():
            yield Static(self._message, classes="loading-box")
