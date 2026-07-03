"""
TitleScreen: the opening / splash screen shown when the TUI starts.

This is the first screen pushed by `FractureApp.on_mount()`. It shows the
game banner and advances on any (unmodified) keypress or a mouse click —
classic "press any key to continue" behavior. Advancing goes to the "auth"
screen (Login/Register/Guest). Once Server Selection is built, it will be
inserted between this screen and "auth" (see `tui/README.md` roadmap).
"""
from __future__ import annotations

from textual import events
from textual.app import ComposeResult
from textual.widgets import Static

from tui.screens.base_screen import BaseScreen


def _build_banner(title: str, width: int = 39) -> str:
    """Build a simple boxed banner, computed (not hand-aligned) to avoid
    any risk of misaligned ASCII art."""
    inner = width - 2
    spaced = " ".join(title)
    top = "╔" + "═" * inner + "╗"
    blank = "║" + " " * inner + "║"
    middle = "║" + spaced.center(inner) + "║"
    bottom = "╚" + "═" * inner + "╝"
    return "\n".join([top, blank, middle, blank, bottom])


_BANNER = _build_banner("FRACTURE")
_TAGLINE = "An AI-Driven Text Adventure"


class TitleScreen(BaseScreen):
    """Opening splash screen: banner + 'press any key to continue' prompt."""

    show_header = False
    show_footer = True

    BINDINGS = [
        ("enter", "continue", "Continue"),
    ]

    DEFAULT_CSS = """
    TitleScreen {
        align: center middle;
    }

    #banner {
        color: $accent;
        text-style: bold;
        text-align: center;
        margin-bottom: 1;
    }

    #tagline {
        text-align: center;
        margin-bottom: 3;
    }

    #prompt {
        text-align: center;
    }

    #prompt.dim {
        color: grey;
    }
    """

    def compose_content(self) -> ComposeResult:
        yield Static(_BANNER, id="banner")
        yield Static(_TAGLINE, id="tagline")
        yield Static("Press any key or click to continue", id="prompt")

    def on_mount(self) -> None:
        self._blink_on = True
        self.set_interval(0.6, self._blink_prompt)

    def _blink_prompt(self) -> None:
        self._blink_on = not self._blink_on
        self.query_one("#prompt", Static).set_class(not self._blink_on, "dim")

    def action_continue(self) -> None:
        self.app.goto_screen("auth")

    def on_key(self, event: events.Key) -> None:
        key = event.key
        # "enter"/"escape" have their own bindings; anything with "+" is a
        # modified combo (ctrl+q, etc.) and must not be swallowed here.
        if key in ("enter", "escape") or "+" in key:
            return
        event.stop()
        self.app.goto_screen("auth")

    def on_click(self) -> None:
        self.app.goto_screen("auth")