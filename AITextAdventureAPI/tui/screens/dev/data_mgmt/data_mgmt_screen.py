"""
DataMgmtScreen: developer data-management hub for browsing/searching every
seed-data catalog in the game.

Delegates all behavior to handlers, treehandlers, detail_panel, and utils.
"""
from __future__ import annotations

from typing import Any, Set

from textual import work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, ScrollableContainer, Vertical
from textual.widgets import Button, Input, Label, ListView, RadioButton, RadioSet, Static, Tab, Tabs, Tree

from tui.screens.base_screen import BaseScreen
from tui.screens.dev.data_mgmt.handlers import (
    handle_button_pressed,
    handle_input_changed,
    handle_list_view_highlighted,
    handle_radio_set_changed,
    handle_tab_activated,
    handle_tree_node_highlighted,
    rebuild_dialog_tree_for_screen,
    rebuild_list_for_screen,
    rebuild_npc_tree_for_screen,
    rebuild_timeline_tree_for_screen,
    set_filter_mode,
)
from tui.services.dev.dataservices import CATEGORIES, CATEGORY_LABELS, DialogueLine, preload

_DIALOG_CATEGORY   = "character_dialog"
_TIMELINE_CATEGORY = "timeline"
_NPC_CATEGORY      = "npc"


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
        height: auto;
        min-height: 3;
        padding: 0 1;
        border-bottom: solid $accent 30%;
    }

    #dm-filter {
        width: 1fr;
    }

    #dm-dialog-filter-row {
        width: 1fr;
        height: 3;
        display: none;
    }

    #dm-dialog-filter-row Input {
        width: 1fr;
        margin-right: 1;
    }

    #dm-equipment-filter-row {
        width: 1fr;
        height: auto;
        display: none;
        padding: 1 0;
    }

    #dm-equipment-filter-row Label {
        width: auto;
        padding: 0 1;
        content-align: left middle;
    }

    #dm-equipment-filter-row Horizontal {
        height: auto;
        width: 1fr;
        align: left middle;
    }

    #dm-equipment-type-radio,
    #dm-equipment-slot-radio {
        width: 1fr;
        height: auto;
        layout: horizontal;
        border: none;
        background: transparent;
    }

    #dm-equipment-type-radio RadioButton,
    #dm-equipment-slot-radio RadioButton {
        width: auto;
        min-width: 8;
        margin-right: 1;
    }

    RadioButton {
        border: tall $accent 50%;
        background: $surface;
        color: $text;
        padding: 0 1;
    }

    RadioButton:hover {
        background: $surface-lighten-1;
    }

    RadioButton.-selected {
        background: $accent;
        color: $text;
    }

    #dm-expand, #dm-collapse, #dm-copy {
        display: none;
        margin-left: 1;
        padding: 0 1;
        min-width: 3;
        height: auto;
        color: $text;
        background: $surface;
        border: solid $accent 30%;
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

    #dm-dialog-tree {
        height: 100%;
        display: none;
    }

    #dm-timeline-tree {
        height: 100%;
        display: none;
    }

    #dm-npc-tree {
        height: 100%;
        display: none;
    }

    #dm-detail-panel {
        width: 80;
        height: 100%;
        padding: 0;
        border-left: solid $accent 30%;
    }

    #dm-detail-text {
        height: 100%;
        padding: 0 1;
    }
    """

    def __init__(self) -> None:
        super().__init__()
        self._category: str = CATEGORIES[0]
        self._loaded: bool  = False

        # Per-tree filtered model caches (for copy-to-clipboard fallback)
        self._last_filtered: Any           = None
        self._last_timeline_filtered: Any  = None
        self._last_npc_filtered: Any       = None

        # Independent expansion state per tree so switching tabs doesn't clobber state
        self._user_expanded: Set[str]          = set()
        self._user_collapsed: Set[str]         = set()
        self._timeline_user_expanded: Set[str] = set()
        self._timeline_user_collapsed: Set[str] = set()
        self._npc_user_expanded: Set[str]      = set()
        self._npc_user_collapsed: Set[str]     = set()

    def compose_content(self) -> ComposeResult:
        yield Tabs(
            *[Tab(CATEGORY_LABELS[category], id=f"tab-{category}") for category in CATEGORIES],
            id="dm-tabs",
        )
        with Horizontal(id="dm-filter-row"):
            yield Input(placeholder="Filter by name, id, or description...", id="dm-filter")
            with Horizontal(id="dm-dialog-filter-row"):
                yield Input(placeholder="Act...", id="dm-filter-act")
                yield Input(placeholder="Chapter...", id="dm-filter-chapter")
                yield Input(placeholder="Task...", id="dm-filter-task")
                yield Input(placeholder="Character...", id="dm-filter-character")
            with Vertical(id="dm-equipment-filter-row"):
                with Horizontal():
                    yield Label("Type:")
                    with RadioSet(id="dm-equipment-type-radio"):
                        yield RadioButton("All", value=True, id="equip-type-all")
                        yield RadioButton("Weapon", id="equip-type-weapon")
                        yield RadioButton("Armor", id="equip-type-armor")
                with Horizontal():
                    yield Label("Slot:")
                    with RadioSet(id="dm-equipment-slot-radio"):
                        yield RadioButton("All", value=True, id="equip-slot-all")
                        yield RadioButton("Head", id="equip-slot-head")
                        yield RadioButton("Body", id="equip-slot-body")
                        yield RadioButton("Arms", id="equip-slot-arms")
                        yield RadioButton("Legs", id="equip-slot-legs")
            yield Button("++", id="dm-expand", variant="default")
            yield Button("--", id="dm-collapse", variant="default")
            yield Button("Copy", id="dm-copy", variant="default")
            yield Static("Loading...", id="dm-status")
        with Horizontal(id="dm-main-row"):
            with Vertical(id="dm-list-panel"):
                yield ListView(id="dm-list")
                dialog_tree: Tree[DialogueLine] = Tree("Dialogue", id="dm-dialog-tree")
                dialog_tree.show_root = False
                yield dialog_tree
                timeline_tree: Tree = Tree("Timeline", id="dm-timeline-tree")
                timeline_tree.show_root = False
                yield timeline_tree
                npc_tree: Tree = Tree("NPCs", id="dm-npc-tree")
                npc_tree.show_root = False
                yield npc_tree
            with ScrollableContainer(id="dm-detail-panel"):
                yield Static("", id="dm-detail-text")

    def on_mount(self) -> None:
        self._load_catalog()

    @work(thread=True)
    def _load_catalog(self) -> None:
        """Runs off the UI thread — imports hundreds of seed modules."""
        try:
            preload()
        except Exception as exc:  # noqa: BLE001
            self.app.call_from_thread(self._on_load_error, str(exc))
            return
        self.app.call_from_thread(self._on_load_success)

    def _on_load_success(self) -> None:
        self._loaded = True
        tabs = self.query_one("#dm-tabs", Tabs)
        tabs.active = f"tab-{self._category}"
        set_filter_mode(self, self._category)
        if self._category == _DIALOG_CATEGORY:
            rebuild_dialog_tree_for_screen(self)
        elif self._category == _TIMELINE_CATEGORY:
            rebuild_timeline_tree_for_screen(self)
        elif self._category == _NPC_CATEGORY:
            rebuild_npc_tree_for_screen(self)
        else:
            rebuild_list_for_screen(self)
        self.query_one("#dm-filter", Input).focus()

    def _on_load_error(self, message: str) -> None:
        from rich.markup import escape as rich_escape
        self.query_one("#dm-status", Static).update("Load failed")
        self.query_one("#dm-detail-text", Static).update(
            f"[red]Failed to load seed data:[/red]\n{rich_escape(message)}"
        )

    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        handle_tab_activated(self, event)

    def on_input_changed(self, event: Input.Changed) -> None:
        handle_input_changed(self, event)

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        handle_radio_set_changed(self, event)

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        handle_list_view_highlighted(self, event)

    def on_tree_node_highlighted(self, event: Tree.NodeHighlighted) -> None:
        handle_tree_node_highlighted(self, event)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        handle_button_pressed(self, event)