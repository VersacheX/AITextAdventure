"""
DataMgmtScreen: developer data-management hub for browsing/searching every
seed-data catalog in the game -- characters, timeline, items, special
items, equipment, dungeons, cities, NPCs, and character dialogue.

Layout:
  ┌── tab bar (categories) ────────────────────────────────────────────────┐
  │ [Characters] [Timeline] [Items] [Special] [Equipment] [Dungeons] [Cities] [NPCs] [Dialogue] │
  ├── filter bar (search box, or act/chapter/task/character for Dialogue) ─┤
  │ [ search input                                                        ] │
  ├────────────────────────────────────────────────────────────────────────┤
  │  list or tree (1fr)                  │  detail panel (54 wide)         │
  │  ...                                 │  ...                            │
  └────────────────────────────────────────────────────────────────────────┘

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

The "Dialogue" tab is a special case: instead of the flat `#dm-list` /
single `#dm-filter` search box, it swaps in a `Tree` (`#dm-dialog-tree`,
Act -> Chapter -> Task -> Acquired/Completed -> line) and four filter
inputs (act / chapter / task / character), toggled by `_set_dialog_mode()`.
"""
from __future__ import annotations

from typing import List, cast

from rich.markup import escape as rich_escape
from textual import work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Input, Label, ListItem, ListView, Static, Tab, Tabs, Tree
from textual.widgets.tree import TreeNode

from tui.screens.base_screen import BaseScreen
from tui.services.dev.dev_data_service import (
    CATEGORIES,
    CATEGORY_LABELS,
    DevRecord,
    DialogueLine,
    filter_dialogue_tree,
    get_dialogue_tree,
    preload,
    search_records,
)

_DIALOG_CATEGORY = "character_dialog"


class _RecordRow(ListItem):
    def __init__(self, record: DevRecord) -> None:
        name = rich_escape(record.name)
        sub = rich_escape(record.subtitle)
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

    #dm-dialog-filter-row {
        width: 1fr;
        height: 3;
        display: none;
    }

    #dm-dialog-filter-row Input {
        width: 1fr;
        margin-right: 1;
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
        # Textual's Tabs widget drives the category bar.
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
            yield Static("Loading...", id="dm-status")
        with Horizontal(id="dm-main-row"):
            with Vertical(id="dm-list-panel"):
                yield ListView(id="dm-list")
                dialog_tree: Tree[DialogueLine] = Tree("Dialogue", id="dm-dialog-tree")
                dialog_tree.show_root = False
                yield dialog_tree
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
        tabs = self.query_one("#dm-tabs", Tabs)
        tabs.active = f"tab-{self._category}"
        self._set_dialog_mode(self._category == _DIALOG_CATEGORY)
        if self._category == _DIALOG_CATEGORY:
            self._rebuild_dialog_tree()
        else:
            self._rebuild_list()
        self.query_one("#dm-filter", Input).focus()

    def _on_load_error(self, message: str) -> None:
        self.query_one("#dm-status", Static).update("Load failed")
        self.query_one("#dm-detail-panel", Static).update(
            f"[red]Failed to load seed data:[/red]\n{rich_escape(message)}"
        )

    # ── tab / filter events ───────────────────────────────────────────────

    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        """Handle tab activation from the Tabs widget."""
        tab_id = event.tab.id or ""
        if tab_id.startswith("tab-"):
            category = tab_id.removeprefix("tab-")
            if category in CATEGORIES:
                self._category = category
                is_dialog = category == _DIALOG_CATEGORY
                self._set_dialog_mode(is_dialog)
                if is_dialog:
                    self._rebuild_dialog_tree()
                else:
                    self._rebuild_list()

    def _set_dialog_mode(self, is_dialog: bool) -> None:
        """Swap the flat list + single search box for the dialogue tree +
        act/chapter/task/character filters, or vice versa."""
        self.query_one("#dm-filter", Input).display = not is_dialog
        self.query_one("#dm-dialog-filter-row", Horizontal).display = is_dialog
        self.query_one("#dm-list", ListView).display = not is_dialog
        self.query_one("#dm-dialog-tree", Tree).display = is_dialog

    def on_input_changed(self, event: Input.Changed) -> None:
        input_id = event.input.id
        if input_id == "dm-filter":
            self._rebuild_list()
        elif input_id in ("dm-filter-act", "dm-filter-chapter", "dm-filter-task", "dm-filter-character"):
            self._rebuild_dialog_tree()

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        record = event.item.record if isinstance(event.item, _RecordRow) else None
        self._update_detail(record)

    def on_tree_node_highlighted(self, event: Tree.NodeHighlighted) -> None:
        if self._category != _DIALOG_CATEGORY:
            return
        data = event.node.data
        self._update_dialog_detail(data if isinstance(data, DialogueLine) else None)

    # ── internal: flat list categories ───────────────────────────────────

    def _rebuild_list(self) -> None:
        if not self._loaded:
            return
        query = self.query_one("#dm-filter", Input).value.strip()
        lv = self.query_one("#dm-list", ListView)
        lv.clear()
        records: List[DevRecord] = search_records(self._category, query)
        for record in records:
            lv.append(_RecordRow(record))
        self.query_one("#dm-status", Static).update(f"{len(records)} result(s)")
        self._update_detail(records[0] if records else None)

    def _highlighted_record(self) -> DevRecord | None:
        lv = self.query_one("#dm-list", ListView)
        child = lv.highlighted_child
        return child.record if isinstance(child, _RecordRow) else None

    def _update_detail(self, record: DevRecord | None) -> None:
        panel = self.query_one("#dm-detail-panel", Static)
        if record is None:
            panel.update("[dim]No matching records.[/dim]")
            return
        name = rich_escape(record.name)
        sub = rich_escape(record.subtitle)
        detail = rich_escape(record.detail)
        header = f"[bold]{name}[/bold]"
        if sub:
            header += f"\n[dim]{sub}[/dim]"
        panel.update(f"{header}\n\n{detail}")

    # ── internal: dialogue tree category ─────────────────────────────────

    def _rebuild_dialog_tree(self) -> None:
        if not self._loaded:
            return
        tree = self.query_one("#dm-dialog-tree", Tree)
        tree.clear()

        full_tree = get_dialogue_tree()
        filtered = filter_dialogue_tree(
            full_tree,
            act_query=self.query_one("#dm-filter-act", Input).value.strip(),
            chapter_query=self.query_one("#dm-filter-chapter", Input).value.strip(),
            task_query=self.query_one("#dm-filter-task", Input).value.strip(),
            character_query=self.query_one("#dm-filter-character", Input).value.strip(),
        )

        total_lines = 0
        for act_node in filtered:
            act_branch = tree.root.add(act_node.label, expand=True)
            for chapter_node in act_node.chapters:
                chapter_branch = act_branch.add(chapter_node.label, expand=False)
                for task_node in chapter_node.tasks:
                    task_branch = chapter_branch.add(task_node.label, expand=False)
                    for stage_node in task_node.stages:
                        stage_branch = task_branch.add(f"[dim]{stage_node.label}[/dim]", expand=False)
                        for line in stage_node.lines:
                            total_lines += 1
                            speaker = rich_escape(line.speaker)
                            text_preview = rich_escape(line.text[:60] + "..." if len(line.text) > 60 else line.text)
                            stage_branch.add_leaf(f"{speaker}: {text_preview}", data=line)

        self.query_one("#dm-status", Static).update(f"{total_lines} line(s)")
        self._update_dialog_detail(None)

    def _update_dialog_detail(self, line: DialogueLine | None) -> None:
        panel = self.query_one("#dm-detail-panel", Static)
        if line is None:
            panel.update("[dim]← select a dialogue line from the tree[/dim]")
            return
        speaker = rich_escape(line.speaker)
        text = rich_escape(line.text)
        panel.update(f"[bold]{speaker}[/bold]\n\n{text}")