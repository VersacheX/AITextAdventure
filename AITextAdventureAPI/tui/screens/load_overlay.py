"""
LoadOverlay: floating load-game widget for InventoryScreen.

Lists the signed-in user's saves from the configured save adapter.
Selecting a save asks for confirmation then loads it in a background
worker.  On success the active game is replaced and the screen transitions
to the overworld.

The CSS class "inv-overlay" is added in on_mount so InventoryScreen's
_close_overlay() can remove it generically.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from rich.markup import escape as rich_escape
from textual import on, work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal
from textual.widget import Widget
from textual.widgets import Button, Label, ListItem, ListView, Static


# ── helpers ──────────────────────────────────────────────────────────────────

def _format_save_row(save: Dict[str, Any]) -> str:
    name      = save.get("name")          or "Unnamed Save"
    character = save.get("main_character") or "Unknown"
    level     = save.get("level")
    money     = save.get("money")
    updated   = save.get("updated_at")    or "unknown"
    level_part = f"Level {level}" if level is not None else "Level ?"
    money_part = f"${money}"      if money is not None else "$?"
    return (
        f"{rich_escape(name)} \u2014 {rich_escape(character)}\n"
        f"{level_part}   {money_part}   Updated {updated}"
    )


class _SaveRow(ListItem):
    def __init__(self, save: Dict[str, Any]) -> None:
        super().__init__(Label(_format_save_row(save)))
        self.save_id   = save.get("id")
        self.save_name = str(save.get("name") or "Unnamed Save")


# ── overlay widget ────────────────────────────────────────────────────────────

class LoadOverlay(Widget):
    """
    Floating load-game overlay for InventoryScreen.

    Fetches the save list in a background worker.  Selecting a save
    confirms via ConfirmScreen then loads it in another worker.  On success
    the active game is replaced and the screen switches to the overworld.
    The CSS class "inv-overlay" lets InventoryScreen close it generically.
    """

    can_focus = True

    BINDINGS = [
        Binding("r",      "refresh_saves", "Refresh", show=False),
        Binding("escape", "request_close", "Close",   show=True),
    ]

    DEFAULT_CSS = """
    LoadOverlay {
        layer: overlay;
        dock: bottom;
        width: 100%;
        height: 20;
        background: $surface;
        border-top: solid $accent;
        layout: vertical;
    }

    #load-header {
        height: 1;
        text-align: center;
        text-style: bold;
        background: $boost;
        padding: 0 1;
    }

    #load-btn-row {
        height: 3;
        padding: 0 2;
    }

    #load-btn-row Button {
        height: 1;
        margin-right: 1;
        border: none;
    }

    #load-status {
        height: 1;
        text-align: center;
        color: $text 60%;
        padding: 0 1;
    }

    #load-list {
        height: 1fr;
    }

    #load-hint {
        height: 1;
        text-align: center;
        color: $text 50%;
        border-top: solid $accent 30%;
        padding: 0 1;
    }
    """

    def __init__(self, on_close: Callable[[bool], None]) -> None:
        super().__init__()
        self._on_close = on_close
        self._loading  = False

    def on_mount(self) -> None:
        self.add_class("inv-overlay")
        self._fetch_saves()

    # ── compose ───────────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        yield Static("── Load Game ──", id="load-header")
        with Horizontal(id="load-btn-row"):
            yield Button("Refresh", id="load-refresh", variant="default")
            yield Button("Cancel",  id="load-cancel",  variant="default")
        yield Static("Loading saves\u2026", id="load-status")
        yield ListView(id="load-list")
        yield Static(
            "[dim]\u2191\u2193:navigate  Enter/click:load  R:refresh  Esc:close[/dim]",
            id="load-hint",
        )

    # ── fetch ─────────────────────────────────────────────────────────────────

    def _fetch_saves(self) -> None:
        lv = self.query_one("#load-list", ListView)
        lv.clear()
        lv.disabled = True
        self.query_one("#load-refresh", Button).disabled = True
        self.query_one("#load-status",  Static).update("Loading saves\u2026")
        self._fetch_worker()

    @work(thread=True)
    def _fetch_worker(self) -> None:
        from client_api_requests.save_service_adapter import get_adapter  # noqa: PLC0415

        try:
            adapter = get_adapter()
            raw     = adapter.list_saves()
            saves: List[Dict[str, Any]] = raw if isinstance(raw, list) else []
        except Exception as exc:  # noqa: BLE001
            self.app.call_from_thread(self._on_fetch_error, str(exc))
            return
        self.app.call_from_thread(self._on_fetch_success, saves)

    def _on_fetch_success(self, saves: List[Dict[str, Any]]) -> None:
        lv     = self.query_one("#load-list", ListView)
        status = self.query_one("#load-status", Static)
        lv.clear()
        if saves:
            for s in saves:
                lv.append(_SaveRow(s))
            status.update(
                f"{len(saves)} save(s) \u2014 \u2191\u2193 + Enter or click to load."
            )
            lv.focus()
        else:
            status.update("No saved games found.")
        lv.disabled = False
        self.query_one("#load-refresh", Button).disabled = False

    def _on_fetch_error(self, message: str) -> None:
        self.query_one("#load-status", Static).update(
            f"[red]Failed to fetch saves: {rich_escape(message)}[/red]"
        )
        self.query_one("#load-list",    ListView).disabled = False
        self.query_one("#load-refresh", Button).disabled   = False

    # ── select → confirm → load ───────────────────────────────────────────────

    @on(ListView.Selected, "#load-list")
    def _on_selected(self, event: ListView.Selected) -> None:
        if self._loading or not isinstance(event.item, _SaveRow):
            return
        row = event.item

        from tui.screens.confirm_screen import ConfirmScreen  # noqa: PLC0415

        def _confirmed(result: bool | None) -> None:
            if result:
                self._do_load(row.save_id, row.save_name)

        self.app.push_screen(
            ConfirmScreen(
                f"Load '{rich_escape(row.save_name)}'?\nUnsaved progress will be lost."
            ),
            _confirmed,
        )

    def _do_load(self, save_id: Any, save_name: str) -> None:
        self._loading = True
        self.query_one("#load-list",    ListView).disabled = True
        self.query_one("#load-refresh", Button).disabled   = True
        self.query_one("#load-status",  Static).update(
            f"Loading '{rich_escape(save_name)}'\u2026"
        )
        self._load_worker(save_id)

    @work(thread=True)
    def _load_worker(self, save_id: Any) -> None:
        from client_api_requests.save_service_adapter import get_adapter  # noqa: PLC0415
        from tui.services.save_transfer import load_player_game            # noqa: PLC0415

        try:
            adapter     = get_adapter()
            player_game = load_player_game(save_id, adapter)
        except Exception as exc:  # noqa: BLE001
            self.app.call_from_thread(self._on_load_error, str(exc))
            return
        if player_game is None:
            self.app.call_from_thread(self._on_load_error, "save data could not be read")
            return
        self.app.call_from_thread(self._on_load_success, player_game)

    def _on_load_success(self, player_game: Any) -> None:
        from tui.services.game_state import set_active_game  # noqa: PLC0415

        set_active_game(player_game)
        self.app.notify("Game loaded.", title="Load Game")
        self.app.goto_screen("overworld")

    def _on_load_error(self, message: str) -> None:
        self._loading = False
        self.query_one("#load-status",  Static).update(
            f"[red]Could not load save: {rich_escape(message)}[/red]"
        )
        self.query_one("#load-list",    ListView).disabled = False
        self.query_one("#load-refresh", Button).disabled   = False

    # ── buttons + actions ─────────────────────────────────────────────────────

    @on(Button.Pressed, "#load-refresh")
    def _on_refresh(self) -> None:
        if not self._loading:
            self._fetch_saves()

    @on(Button.Pressed, "#load-cancel")
    def _on_cancel(self) -> None:
        if not self._loading:
            self._on_close(False)

    def action_refresh_saves(self) -> None:
        if not self._loading:
            self._fetch_saves()

    def action_request_close(self) -> None:
        if not self._loading:
            self._on_close(False)