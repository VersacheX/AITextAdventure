"""
DataMgmtScreen: developer data-management hub for browsing/searching every
seed-data catalog in the game -- characters, timeline, items, special
items, equipment, dungeons, and cities.

Layout:
  ┌── tab bar (categories) ────────────────────────────────────────┐
  │ [Characters] [Timeline] [Items] [Special] [Equipment] [Dungeons] [Cities] │
  ├── filter bar (type to search) ──────────────────────────────────┤
  │ [ search input                                                ] │
  ├──────────────────────────────────────────────────────────────────┤
  │  list (1fr)                          │  detail panel (46 wide)  │
  │  ...                                 │  ...                     │
  └──────────────────────────────────────────────────────────────────┘

Follows the same docked-list-with-detail-panel pattern already proven in
`equip_overlay.py` / `monster_log_overlay.py`, but as a full `BaseScreen`
(like `overworld_screen.py`) since this needs its own tab bar and filter
input rather than floating over another screen.

`tui.services.dev_data_service` normalizes the legacy `old/game/constants.py`
seed data into a uniform `DevRecord` per catalog entry. Building that catalog
imports hundreds of region/story/dungeon seed modules on first use, so it
counts as blocking I/O per project convention -- it runs in a background
worker (`@work(thread=True)`) with the result marshaled back via
`self.app.call_from_thread(...)`, matching `tui/screens/login_screen.py`.
"""
from __future__ import annotations

from typing import Any, List

from rich.markup import escape as rich_escape
from textual import on, work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Input, Label, ListItem, ListView, Static, Tab, Tabs

from tui.screens.base_screen import BaseScreen
from tui.services.dev.dev_data_service import (
    CATEGORIES,
    CATEGORY_LABELS,
    DevRecord,
    preload,
    search_records,
)


class _RecordRow(ListItem):
    def __init__(self, record: DevRecord) -> None:
        name = rich_escape(record.name)
        sub  = rich_escape(record.subtitle)
        label = f"{name}  [dim]{sub}[/dim]" if sub else name
        super().__init__(Label(label))
        self.record = record


class DataMgmtScreen(BaseScreen):
    """Dev-only browser for every seed-data catalog in the game."""

    BINDINGS = [
        Binding("escape", "go_back", "Back", show=True),
    ]

    DEFAULT_CSS = """
    DataMgmtScreen {
        layout: vertical;
    }

    #dm-tabs {
        height: 3;
        background: $panel;
        border-bottom: solid $accent;
    }

    #dm-filter-row {
        height: 3;
        padding: 0 1;
        border-bottom: solid $accent 30%;
    }

    #dm-filter {
        width: 1fr;
    }

    #dm-status {
        width: auto;
        min-width: 14;
        content-align: right middle;
        color: $text 60%;
        padding: 0 1;
    }

    #dm-main-row {
        height: 1fr;
    }

    #dm-list-panel {
        width: 1fr;
        height: 100%;
    }

    #dm-list {
        height: 100%;
    }

    #dm-detail-panel {
        width: 54;
        height: 100%;
        padding: 0 1;
        overflow-y: auto;
        border-left: solid $accent 30%;
    }
    """

    def __init__(self) -> None:
        super().__init__()
        self._category: str = CATEGORIES[0]
        self._loaded: bool = False

    # ── compose ───────────────────────────────────────────────────────────

    def compose_content(self) -> ComposeResult:
        with Tabs(id="dm-tabs"):
            for category in CATEGORIES:
                yield Tab(CATEGORY_LABELS[category], id=f"tab-{category}")
        with Horizontal(id="dm-filter-row"):
            yield Input(placeholder="Filter by name, id, or description...", id="dm-filter")
            yield Static("Loading...", id="dm-status")
        with Horizontal(id="dm-main-row"):
            with Vertical(id="dm-list-panel"):
                yield ListView(id="dm-list")
            yield Static("", id="dm-detail-panel")

    def on_mount(self) -> None:
        self._load_catalog()

    # ── background loading ───────────────────────────────────────────────

    @work(thread=True)
    def _load_catalog(self) -> None:
        """Runs off the UI thread -- building the catalog imports hundreds
        of seed modules on first use (see module docstring)."""
        try:
            preload()
        except Exception as exc:  # noqa: BLE001 - surfaced to the user below
            self.app.call_from_thread(self._on_load_error, str(exc))
            return
        self.app.call_from_thread(self._on_load_success)

    def _on_load_success(self) -> None:
        self._loaded = True
        self._rebuild_list()
        self.query_one("#dm-filter", Input).focus()

    def _on_load_error(self, message: str) -> None:
        self.query_one("#dm-status", Static).update("Load failed")
        self.query_one("#dm-detail-panel", Static).update(
            f"[red]Failed to load seed data:[/red]\n{rich_escape(message)}"
        )

    # ── tab / filter events ───────────────────────────────────────────────

    @on(Tabs.TabActivated, "#dm-tabs")
    def _on_tab_activated(self, event: Tabs.TabActivated) -> None:
        tab_id = event.tab.id or ""
        category = tab_id.removeprefix("tab-")
        if category in CATEGORIES:
            self._category = category
            self._rebuild_list()

    @on(Input.Changed, "#dm-filter")
    def _on_filter_changed(self, event: Input.Changed) -> None:
        self._rebuild_list()

    @on(ListView.Highlighted, "#dm-list")
    def _on_highlighted(self, event: ListView.Highlighted) -> None:
        record = event.item.record if isinstance(event.item, _RecordRow) else None
        self._update_detail(record)

    # ── internal ──────────────────────────────────────────────────────────

    def _rebuild_list(self) -> None:
        if not self._loaded:
            return
        query  = self.query_one("#dm-filter", Input).value.strip()
        lv     = self.query_one("#dm-list", ListView)
        lv.clear()
        records: List[DevRecord] = search_records(self._category, query)
        for record in records:
            lv.append(_RecordRow(record))
        self.query_one("#dm-status", Static).update(f"{len(records)} result(s)")
        self._update_detail(records[0] if records else None)

    def _highlighted_record(self) -> DevRecord | None:
        lv    = self.query_one("#dm-list", ListView)
        child = lv.highlighted_child
        return child.record if isinstance(child, _RecordRow) else None

    def _update_detail(self, record: DevRecord | None) -> None:
        panel = self.query_one("#dm-detail-panel", Static)
        if record is None:
            panel.update("[dim]No matching records.[/dim]")
            return
        name = rich_escape(record.name)
        sub  = rich_escape(record.subtitle)
        detail = rich_escape(record.detail)
        header = f"[bold]{name}[/bold]"
        if sub:
            header += f"\n[dim]{sub}[/dim]"
        panel.update(f"{header}\n\n{detail}")