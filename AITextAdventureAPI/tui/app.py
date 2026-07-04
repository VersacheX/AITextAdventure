"""
FractureApp: the root Textual application and screen manager for the
Fracture TUI.

Textual's `App` already implements a stack-based screen manager
(`push_screen` / `pop_screen` / `switch_screen`) backed by a compositor that
only repaints the cells that actually changed between frames. That is what
gives us flicker-free rendering without any manual clear/redraw code.

`FractureApp` *is* that screen manager: it registers named screens in
`SCREENS` and exposes two small, explicit wrapper methods — `goto_screen()`
and `go_back()` — so screens have one obvious, discoverable navigation API
instead of re-implementing "is this screen registered yet" checks
everywhere. This also lets in-progress screens link forward to screens that
don't exist yet during incremental development, without crashing.
"""
from __future__ import annotations

from pathlib import Path

from textual.app import App

from tui.screens.title_screen import TitleScreen
from tui.screens.server_select_screen import ServerSelectScreen
from tui.screens.auth_screen import AuthScreen
from tui.screens.login_screen import LoginScreen, RegisterScreen
from tui.screens.main_menu_screen import MainMenuScreen
from tui.screens.load_game_screen import LoadGameScreen
from tui.screens.overworld_screen import OverworldScreen
from tui.screens.inventory_screen import InventoryScreen

_STYLES_PATH = Path(__file__).parent / "styles" / "app.tcss"


class FractureApp(App):
    """Root application and screen manager for the Fracture TUI.

    Screens are registered by name below and navigated to with
    `self.app.goto_screen("<name>")` from within any `BaseScreen` subclass.
    """

    TITLE = "Fracture"
    CSS_PATH = _STYLES_PATH

    SCREENS = {
        "title": TitleScreen,
        "server_select": ServerSelectScreen,
        "auth": AuthScreen,
        "login": LoginScreen,
        "register": RegisterScreen,
        "main_menu": MainMenuScreen,
        "load_game": LoadGameScreen,
        "overworld": OverworldScreen,
        "inventory": InventoryScreen,
        # Registered incrementally as each screen is built:
        # "new_game": NewGameScreen,
    }

    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),
    ]

    def on_mount(self) -> None:
        self.goto_screen("title")

    def goto_screen(self, name: str) -> bool:
        """Push the named screen onto the stack.

        Returns True if `name` was registered and pushed. If it isn't
        registered yet, shows a friendly toast instead of raising — this is
        what lets screens built now link forward to screens that don't exist
        yet without erroring.
        """
        if name not in self.SCREENS:
            self.notify(
                f"Screen '{name}' isn't implemented yet.",
                title="Coming soon",
                severity="information",
            )
            return False
        self.push_screen(name)
        return True

    def go_back(self) -> None:
        """Pop the current screen, if there is somewhere to go back to."""
        if len(self.screen_stack) > 1:
            self.pop_screen()


def run() -> None:
    """Entry point used by `run_tui.py`."""
    FractureApp().run()


if __name__ == "__main__":
    run()