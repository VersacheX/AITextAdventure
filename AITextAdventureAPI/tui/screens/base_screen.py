"""
BaseScreen: shared base class for every Fracture TUI screen.

All concrete screens must inherit from `BaseScreen` rather than Textual's
`Screen` directly. This keeps common chrome (header/footer) and navigation
bindings consistent across the app, and gives us one place to add
cross-cutting behavior later (e.g. global error handling).
"""
from __future__ import annotations

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer, Header


class BaseScreen(Screen):
    """Common base class for all screens in the Fracture TUI.

    Subclasses should override `compose_content()` instead of `compose()`
    so the shared header/footer stay consistent. A subclass that needs a
    fully custom layout (rare) can override `compose()` directly instead.
    """

    BINDINGS = [
        ("escape", "go_back", "Back"),
    ]

    show_header: bool = True
    show_footer: bool = True

    def compose(self) -> ComposeResult:
        if self.show_header:
            yield Header()
        yield from self.compose_content()
        if self.show_footer:
            yield Footer()

    def compose_content(self) -> ComposeResult:
        """Override in subclasses to yield the screen's widgets."""
        return
        yield  # pragma: no cover - keeps this a generator function

    def action_go_back(self) -> None:
        self.app.go_back()