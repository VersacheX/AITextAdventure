"""
LoadGameScreen: scrollable list of the signed-in user's saves.

Replaces `old/console_game.py`'s `load_game_menu()`, which printed a fixed,
non-scrolling numbered list and read a line of text input. This version
uses Textual's `ListView`, which is natively scrollable (mouse wheel and
keyboard) and already turns arrow-key+Enter or a mouse click into a single
`ListView.Selected` message -- no custom pagination or key handling needed.

Fetching the save list and loading a selected save's blob are both
blocking I/O calls (HTTP via `APISaveService`, or SQLite via
`LocalSaveService`) and run in background workers per project convention
(see `tui/screens/login_screen.py`).

Note: this deliberately avoids `client_api_requests.load_game_service`
entirely (for both listing and loading) -- that module imports `ClientAPI`
at module scope, which eagerly imports `requests`, and its list-saves
helper's `except` branch also calls a bare `input(...)` that would hang a
background worker thread indefinitely under Textual. Listing calls
`SaveService.list_saves()` directly; loading a specific save uses
`tui.services.save_transfer.load_player_game()`, a small adapter-only
reimplementation -- see that module's docstring for details.
"""
from __future__ import annotations

from typing import Any, Dict, List

from textual import work
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Label, ListItem, ListView, Static

from tui.screens.base_screen import BaseScreen


def _format_save_row(save: Dict[str, Any]) -> str:
    name = save.get("name") or "Unnamed Save"
    character = save.get("main_character") or "Unknown"
    level = save.get("level")
    money = save.get("money")
    updated = save.get("updated_at") or "unknown"
    level_part = f"Level {level}" if level is not None else "Level ?"
    money_part = f"${money}" if money is not None else "$?"
    return f"{name} \u2014 {character}\n{level_part}   {money_part}   Updated {updated}"


class SaveListItem(ListItem):
    """A single save entry in the scrollable list, carrying its save id."""

    def __init__(self, save: Dict[str, Any]) -> None:
        super().__init__(Label(_format_save_row(save)))
        self.save_id = save.get("id")


class LoadGameScreen(BaseScreen):
    """Scrollable save-selection screen."""

    DEFAULT_CSS = """
    LoadGameScreen {
        align: center middle;
    }

    #load-panel {
        width: 70;
        height: 28;
        border: round $accent;
        padding: 1 2;
    }

    #load-title {
        text-align: center;
        text-style: bold;
        margin-bottom: 1;
    }

    #load-status {
        text-align: center;
        color: $text 60%;
        margin-bottom: 1;
    }

    #save-list {
        height: 1fr;
        border: round $primary;
    }

    SaveListItem Label {
        padding: 0 1;
    }

    #load-buttons {
        height: auto;
        margin-top: 1;
    }

    #load-buttons Button {
        margin-right: 1;
    }
    """

    def compose_content(self) -> ComposeResult:
        with Vertical(id="load-panel"):
            yield Static("=== Load Game ===", id="load-title")
            yield Static("Loading saves...", id="load-status")
            yield ListView(id="save-list")
            with Horizontal(id="load-buttons"):
                yield Button("Refresh", id="refresh")
                yield Button("Back", id="back")

    def on_mount(self) -> None:
        self._refresh_saves()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "refresh":
            self._refresh_saves()
        elif event.button.id == "back":
            self.app.go_back()

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        item = event.item
        if isinstance(item, SaveListItem) and item.save_id is not None:
            self._load_save(item.save_id)

    def _refresh_saves(self) -> None:
        self.query_one("#load-status", Static).update("Loading saves...")
        list_view = self.query_one("#save-list", ListView)
        list_view.clear()
        list_view.disabled = True
        self.query_one("#refresh", Button).disabled = True
        self._fetch_saves()

    @work(thread=True)
    def _fetch_saves(self) -> None:
        from client_api_requests.save_service_adapter import get_adapter

        try:
            adapter = get_adapter()
            raw = adapter.list_saves()
            saves = raw if isinstance(raw, list) else []
        except Exception as exc:  # noqa: BLE001 - surfaced to the user below
            self.app.call_from_thread(self._on_fetch_error, str(exc))
            return

        self.app.call_from_thread(self._on_fetch_success, saves)

    def _on_fetch_success(self, saves: List[Dict[str, Any]]) -> None:
        list_view = self.query_one("#save-list", ListView)
        status = self.query_one("#load-status", Static)

        list_view.clear()
        if not saves:
            status.update("No saved games found.")
        else:
            for save in saves:
                list_view.append(SaveListItem(save))
            status.update(f"{len(saves)} save(s). Use \u2191/\u2193 + Enter, or click, to load.")
            list_view.focus()

        list_view.disabled = False
        self.query_one("#refresh", Button).disabled = False

    def _on_fetch_error(self, message: str) -> None:
        self.query_one("#load-status", Static).update(f"Failed to load saves: {message}")
        self.query_one("#save-list", ListView).disabled = False
        self.query_one("#refresh", Button).disabled = False

    def _load_save(self, save_id: Any) -> None:
        self.query_one("#load-status", Static).update("Loading save...")
        self.query_one("#save-list", ListView).disabled = True
        self.query_one("#refresh", Button).disabled = True
        self._fetch_and_apply_save(save_id)

    @work(thread=True)
    def _fetch_and_apply_save(self, save_id: Any) -> None:
        from client_api_requests.save_service_adapter import get_adapter
        from tui.services.save_transfer import load_player_game

        try:
            adapter = get_adapter()
            player_game = load_player_game(save_id, adapter)
        except Exception as exc:  # noqa: BLE001 - surfaced to the user below
            self.app.call_from_thread(self._on_load_error, str(exc))
            return

        if player_game is None:
            self.app.call_from_thread(self._on_load_error, "save data could not be read")
            return

        self.app.call_from_thread(self._on_load_success, player_game)

    def _on_load_success(self, player_game: Any) -> None:
        from tui.services.game_state import set_active_game

        set_active_game(player_game)
        self.notify("Save loaded.", title="Load Game")
        self.app.goto_screen("overworld")

    def _on_load_error(self, message: str) -> None:
        self.notify(f"Could not load save: {message}", title="Load Game", severity="error")
        self.query_one("#load-status", Static).update("Select a save to load.")
        self.query_one("#save-list", ListView).disabled = False
        self.query_one("#refresh", Button).disabled = False