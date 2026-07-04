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

from typing import List, Any

from rich.markup import escape as rich_escape
from textual import work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, ScrollableContainer
from textual.widgets import (
    Button,
    Input,
    Label,
    ListItem,
    ListView,
    Static,
    Tab,
    Tabs,
    Tree,
)
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

    /* Make buttons readable and clickable */
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

    #dm-detail-panel {
        width: 54;
        height: 1fr;           /* Changed from 100% */
        padding: 0 1;
        border-left: solid $accent 30%;
        overflow-y: auto;      /* Explicitly force it */
    }

    #dm-detail-text {
        height: auto;          /* Let content dictate height */
        width: 1fr;
    }
    """

    def __init__(self) -> None:
        super().__init__()
        self._category: str = CATEGORIES[0]
        self._loaded: bool = False
        self._last_filtered: Any = None  # store last filtered tree nodes for copy

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
            # Expand/Collapse buttons: ++ / --
            yield Button("++", id="dm-expand", variant="default")
            yield Button("--", id="dm-collapse", variant="default")
            # Copy button
            yield Button("Copy", id="dm-copy", variant="default")
            yield Static("Loading...", id="dm-status")
        with Horizontal(id="dm-main-row"):
            with Vertical(id="dm-list-panel"):
                yield ListView(id="dm-list")
                dialog_tree: Tree[DialogueLine] = Tree("Dialogue", id="dm-dialog-tree")
                dialog_tree.show_root = False
                yield dialog_tree
            # Right detail pane: ScrollableContainer with inner Static
            with ScrollableContainer(id="dm-detail-panel"):
                yield Static("", id="dm-detail-text", expand=True)

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
        self.query_one("#dm-detail-text", Static).update(
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
        # toggle expand/collapse/copy button visibility
        self.query_one("#dm-expand", Button).display = is_dialog
        self.query_one("#dm-collapse", Button).display = is_dialog
        self.query_one("#dm-copy", Button).display = is_dialog

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
        node = event.node
        data = node.data
        if isinstance(data, DialogueLine):
            # leaf dialog line selected — show single line
            self._update_dialog_detail(data)
        else:
            # non-dialog node selected — collect all dialogue lines in subtree
            lines = self._collect_dialogue_lines(node)
            self._update_dialog_detail_multiple(lines)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        bid = event.button.id or ""
        if bid == "dm-expand":
            self._expand_all()
        elif bid == "dm-collapse":
            self._collapse_all()
        elif bid == "dm-copy":
            self._handle_copy_action()

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
        panel = self.query_one("#dm-detail-text", Static)
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

        # store for copy action (model of what's visible)
        self._last_filtered = filtered

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
        panel = self.query_one("#dm-detail-text", Static)
        if line is None:
            panel.update("[dim]← select a dialogue line from the tree[/dim]")
            return
        speaker = rich_escape(line.speaker)
        text = rich_escape(line.text)
        panel.update(f"[bold]{speaker}[/bold]\n\n{text}")

    def _update_dialog_detail_multiple(self, lines: List[DialogueLine]) -> None:
        """Render all lines (speaker + text) for a subtree selection."""
        panel = self.query_one("#dm-detail-text", Static)
        if not lines:
            panel.update("[dim]No dialogue lines under this node.[/dim]")
            return
        parts: List[str] = []
        for ln in lines:
            parts.append(f"[bold]{rich_escape(ln.speaker)}[/bold]\n\n{rich_escape(ln.text)}")
            parts.append("\n[dim]──[/dim]\n")
        # remove trailing separator
        if parts:
            parts = parts[:-1]
        panel.update("\n".join(parts))

    def _collect_dialogue_lines(self, node: TreeNode) -> List[DialogueLine]:
        """Recursively collect DialogueLine data from `node` subtree (descend all children)."""
        collected: List[DialogueLine] = []
        # If this node holds a DialogueLine directly, include it
        data = node.data
        if isinstance(data, DialogueLine):
            collected.append(data)
        # Traverse children: textual TreeNode stores children in .children (dict)
        children = getattr(node, "children", None)
        if isinstance(children, dict):
            iterable = children.values()
        else:
            iterable = list(children or [])
        for child in iterable:
            collected.extend(self._collect_dialogue_lines(child))
        return collected

    # ── expand/collapse helpers ──────────────────────────────────────────

    def _expand_all(self) -> None:
        """Recursively expand every node in the dialogue tree."""
        try:
            tree = self.query_one("#dm-dialog-tree", Tree)
        except Exception:
            return
        root = tree.root
        self._traverse_and_apply(root, expand=True)

    def _collapse_all(self) -> None:
        """Recursively collapse every node in the dialogue tree."""
        try:
            tree = self.query_one("#dm-dialog-tree", Tree)
        except Exception:
            return
        root = tree.root
        self._traverse_and_apply(root, expand=False)

    def _traverse_and_apply(self, node: TreeNode, *, expand: bool) -> None:
        """Recursive helper: call expand()/collapse() on node and its descendants."""
        try:
            if expand:
                node.expand()
            else:
                node.collapse()
        except Exception:
            # Some nodes (e.g. leaves) may not support expand/collapse; ignore.
            pass
        children = getattr(node, "children", None)
        if isinstance(children, dict):
            iterable = children.values()
        else:
            iterable = list(children or [])
        for child in iterable:
            self._traverse_and_apply(child, expand=expand)

    # ── copy tree to clipboard (respect UI visibility/expansion) ─────────

    def _handle_copy_action(self) -> None:
        """Copy currently visible tree (or selected subtree/line) to clipboard.

        Behavior:
        - If a node is highlighted: serialize that node, including children only
          if the corresponding UI nodes are expanded.
        - If no node is highlighted: serialize the whole UI tree starting at root,
          including children only when their parent node is expanded in the UI.
        - Leaf DialogueLine nodes use the full text from the model (`node.data`).
        """
        try:
            tree = self.query_one("#dm-dialog-tree", Tree)
        except Exception:
            tree = None

        text = ""
        highlighted = None
        if tree is not None:
            highlighted = getattr(tree, "highlighted_node", None) or getattr(tree, "focused_node", None)

        if highlighted and highlighted is not tree.root:
            # Serialize the highlighted node respecting UI expansion
            lines = self._serialize_node_visible(highlighted, depth=0)
            text = "\n".join(lines)
        else:
            # Serialize the UI-visible portions of the whole tree
            if tree is not None:
                lines: List[str] = []
                root = tree.root
                children = getattr(root, "children", None)
                iterable = children.values() if isinstance(children, dict) else list(children or [])
                for child in iterable:
                    lines.extend(self._serialize_node_visible(child, depth=0))
                text = "\n".join(lines)
            else:
                # Fallback to model if tree not available
                if self._last_filtered:
                    text = self._serialize_filtered_tree(self._last_filtered)
                else:
                    full = get_dialogue_tree()
                    text = self._serialize_filtered_tree(full)

        # Attempt to copy to clipboard (pyperclip -> tkinter -> write temp)
        copied = self._copy_to_clipboard(text)
        status = "Copied to clipboard" if copied else "Saved to temp file (fallback)"
        self.query_one("#dm-status", Static).update(status)

    def _serialize_node_visible(self, node: TreeNode, depth: int) -> List[str]:
        """Return list of text lines for `node` and its visible children.
        Only descend into children when the UI node is expanded.
        """
        out: List[str] = []
        # If node carries a DialogueLine (leaf), include full speaker:text
        if isinstance(getattr(node, "data", None), DialogueLine):
            ln: DialogueLine = node.data
            out.append("  " * depth + f"{ln.speaker}: {ln.text}")
            return out

        # Non-leaf node: append its label
        label = self._node_label_text(node)
        out.append("  " * depth + label)

        # Descend only if node is expanded; but always include leaf children even if collapsed? No:
        # respect UI visibility: if node is collapsed, do not include children.
        if not self._is_node_expanded(node):
            return out

        children = getattr(node, "children", None)
        iterable = children.values() if isinstance(children, dict) else list(children or [])
        for child in iterable:
            out.extend(self._serialize_node_visible(child, depth + 1))
        return out

    def _is_node_expanded(self, node: TreeNode) -> bool:
        """Robustly check whether a TreeNode is expanded/open across Textual versions."""
        # common attribute names/methods
        for attr in ("is_expanded", "expanded", "is_open", "open"):
            val = getattr(node, attr, None)
            if val is not None:
                if callable(val):
                    try:
                        return bool(val())
                    except Exception:
                        continue
                return bool(val)
        # Some Textual versions expose a private flag
        val = getattr(node, "_is_expanded", None) or getattr(node, "_expanded", None)
        if val is not None:
            return bool(val)
        # fallback: if node has no children, treat as expanded/visible leaf
        children = getattr(node, "children", None)
        return False if children else True

    # def _serialize_ui_open_nodes(self, root: TreeNode) -> str:
    #     """Serialize only the UI-visible (open/expanded) nodes starting at `root`."""
    #     out: List[str] = []

    #     def walk(node: TreeNode, depth: int) -> None:
    #         # Skip root label (tree root is hidden in this UI)
    #         if node is not root:
    #             # Attempt to obtain a textual label for the UI node
    #             lbl = self._node_label_text(node)
    #             out.append("  " * (depth - 1) + lbl)
    #         # If node is expanded, descend into children
    #         children = getattr(node, "children", None)
    #         iterable = children.values() if isinstance(children, dict) else list(children or [])
    #         if not iterable:
    #             # leaf nodes may carry DialogueLine data; include them when present
    #             if isinstance(node.data, DialogueLine):
    #                 out.append("  " * depth + f"{node.data.speaker}: {node.data.text}")
    #             return
    #         for child in iterable:
    #             if self._is_node_expanded(child) or isinstance(child.data, DialogueLine):
    #                 # include child and descend
    #                 walk(child, depth + 1)
    #             # if the child is collapsed, skip its subtree entirely

    #     # Walk top-level children
    #     for child in (root.children.values() if isinstance(root.children, dict) else list(root.children or [])):
    #         if self._is_node_expanded(child):
    #             walk(child, 0)
    #     return "\n".join(out)

    def _node_label_text(self, node: TreeNode) -> str:
        """Get a string label for a UI tree node in a best-effort way."""
        # Try common attributes that may hold the label/renderable
        for attr in ("label", "_label", "renderable", "text"):
            val = getattr(node, attr, None)
            if val is None:
                continue
            try:
                # If it's a rich/textual renderable, str() will produce something usable
                return str(val)
            except Exception:
                continue
        # Fallback: try to coerce the node itself
        try:
            return str(node)
        except Exception:
            return "<node>"

    def _format_lines_for_copy(self, lines: List[DialogueLine]) -> str:
        parts: List[str] = []
        for ln in lines:
            parts.append(f"{ln.speaker}: {ln.text}")
        return "\n\n".join(parts)

    def _serialize_filtered_tree(self, filtered) -> str:
        """Serialize the act/chapter/task/stage/lines structure into plain text (model-driven)."""
        out: List[str] = []
        for act in filtered:
            out.append(f"{act.label}")
            for chapter in act.chapters:
                out.append(f"  {chapter.label}")
                for task in chapter.tasks:
                    out.append(f"    {task.label}")
                    for stage in task.stages:
                        out.append(f"      {stage.label}")
                        for ln in stage.lines:
                            out.append(f"        {ln.speaker}: {ln.text}")
        return "\n".join(out)

    def _copy_to_clipboard(self, text: str) -> bool:
        """Try pyperclip, then tkinter, then fallback to a temp file. Return True on clipboard success."""
        if not text:
            return False
        # Try pyperclip
        try:
            import pyperclip

            pyperclip.copy(text)
            return True
        except Exception:
            pass
        # Try tkinter
        try:
            import tkinter as tk

            root = tk.Tk()
            root.withdraw()
            root.clipboard_clear()
            root.clipboard_append(text)
            root.update()  # ensure it's copied
            root.destroy()
            return True
        except Exception:
            pass
        # Fallback: write to temp file and inform user via status
        try:
            import tempfile
            import os

            fd, path = tempfile.mkstemp(prefix="dialogue_copy_", suffix=".txt")
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(text)
            # leave the file for user to open; set status to path
            self.query_one("#dm-status", Static).update(f"Saved to {path}")
            return False
        except Exception:
            return False