"""
SaveOverlay: floating save-game widget for InventoryScreen.

Behaviour:
  - Pre-fills the Input with the current ``pg.name``.
  - If the user leaves the name unchanged (or clears it) → overwrites the
    existing save slot (``pg.save_id``).
  - If the user types a different name → creates a new save slot.
  - The actual write runs in a ``@work(thread=True)`` worker so the UI stays
    responsive during the blocking serialise + SQLite/HTTP call.
  - On success the overlay auto-closes after a short confirmation pause;
    on failure the controls re-enable so the user can retry.

The CSS class ``"inv-overlay"`` is added in ``on_mount`` so
``InventoryScreen._close_overlay()`` can remove it generically.
"""
from __future__ import annotations

from typing import Any, Callable

from textual import on, work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal
from textual.widget import Widget
from textual.widgets import Button, Input, Static


class SaveOverlay(Widget):
    """Docked save-game input panel."""

    can_focus = True

    BINDINGS = [
        Binding("escape", "request_close", "Cancel", show=True),
    ]

    DEFAULT_CSS = """
    SaveOverlay {
        layer: overlay;
        dock: bottom;
        width: 100%;
        height: 8;
        background: $surface;
        border-top: solid $accent;
        padding: 1 2;
        layout: vertical;
    }

    #save-header {
        height: 1;
        text-align: center;
        text-style: bold;
        background: $boost;
        color: $text;
        margin-bottom: 1;
    }

    #save-input-row {
        height: 3;
        layout: horizontal;
    }

    #save-name {
        width: 1fr;
        margin-right: 1;
    }

    #save-btn {
        width: 14;
        margin-right: 1;
    }

    #save-cancel {
        width: 12;
    }

    #save-status {
        height: 1;
        color: $text 60%;
        text-align: center;
        margin-top: 1;
    }
    """

    def __init__(self, pg: Any, on_close: Callable[[bool], None]) -> None:
        super().__init__()
        self._pg = pg
        self._on_close = on_close
        self._saving = False

    def on_mount(self) -> None:
        self.add_class("inv-overlay")
        self.query_one("#save-name", Input).focus()

    def compose(self) -> ComposeResult:
        current_name = getattr(self._pg, "name", "") or ""

        yield Static("── Save Game ──", id="save-header")
        with Horizontal(id="save-input-row"):
            yield Input(
                value=current_name,
                placeholder="Save name  (leave unchanged to overwrite current slot)",
                id="save-name",
            )
            yield Button("Save  [S]", id="save-btn", variant="primary")
            yield Button("Cancel", id="save-cancel", variant="default")
        yield Static(
            "Type a new name to create a new slot, or press Save to overwrite.",
            id="save-status",
        )

    # ── events ────────────────────────────────────────────────────────────

    @on(Button.Pressed, "#save-btn")
    def _on_save_pressed(self) -> None:
        self._do_save()

    @on(Button.Pressed, "#save-cancel")
    def _on_cancel_pressed(self) -> None:
        self._on_close(False)

    @on(Input.Submitted, "#save-name")
    def _on_input_submitted(self, _: Input.Submitted) -> None:
        self._do_save()

    def action_request_close(self) -> None:
        if not self._saving:
            self._on_close(False)

    # ── save logic ────────────────────────────────────────────────────────

    def _do_save(self) -> None:
        if self._saving:
            return
        self._saving = True

        name_input = self.query_one("#save-name", Input)
        typed = name_input.value.strip()
        current_name = getattr(self._pg, "name", "") or ""

        # Pass typed name only if the user actually changed it;
        # passing None signals "overwrite current slot" to save_service.
        save_name = typed if typed and typed != current_name else None

        self.query_one("#save-status", Static).update("Saving…")
        self.query_one("#save-btn", Button).disabled = True
        self.query_one("#save-cancel", Button).disabled = True
        name_input.disabled = True

        self._save_worker(save_name)

    @work(thread=True)
    def _save_worker(self, name: str | None) -> None:
        from tui.services.save_service import save_player_game  # noqa: PLC0415

        success, message = save_player_game(self._pg, name=name)
        self.app.call_from_thread(self._on_save_done, success, message)

    def _on_save_done(self, success: bool, message: str) -> None:
        status = self.query_one("#save-status", Static)
        if success:
            status.update(f"[green]{message}[/green]")
            # Brief pause so the user sees the confirmation, then close
            self.set_timer(1.2, lambda: self._on_close(True))
        else:
            status.update(f"[red]{message}[/red]")
            # Re-enable controls so the user can retry
            self._saving = False
            self.query_one("#save-btn", Button).disabled = False
            self.query_one("#save-cancel", Button).disabled = False
            self.query_one("#save-name", Input).disabled = False