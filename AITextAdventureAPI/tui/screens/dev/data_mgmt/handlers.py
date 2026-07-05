"""
Event handlers for tab activation, input changes, list/tree highlighting, and button presses.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from textual.widgets import Button, Input, ListView, Static, Tabs, Tree

from tui.screens.dev.data_mgmt.components import _RecordRow
from tui.screens.dev.data_mgmt.detail_panel import (
    update_detail_for_multiple_dialogue,
    update_detail_for_record,
    update_detail_for_single_dialogue,
)
from tui.screens.dev.data_mgmt.dialog_tree import (
    collect_dialogue_lines_from_node,
    collapse_all_nodes,
    expand_all_nodes,
    rebuild_dialog_tree,
)
from tui.screens.dev.data_mgmt.utils import (
    copy_to_clipboard,
    get_node_children,
    is_node_expanded,
    node_label_text,
    serialize_filtered_tree,
    serialize_node_visible,
)
from tui.services.dev.dev_data_service import (
    CATEGORIES,
    DialogueLine,
    get_dialogue_tree,
    search_records,
)

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen

_DIALOG_CATEGORY = "character_dialog"


def handle_tab_activated(screen: "DataMgmtScreen", event: Tabs.TabActivated) -> None:
    """Handle tab activation from the Tabs widget."""
    tab_id = event.tab.id or ""
    if tab_id.startswith("tab-"):
        category = tab_id.removeprefix("tab-")
        if category in CATEGORIES:
            screen._category = category
            is_dialog = category == _DIALOG_CATEGORY
            set_dialog_mode(screen, is_dialog)
            if is_dialog:
                rebuild_dialog_tree_for_screen(screen)
            else:
                rebuild_list_for_screen(screen)


def set_dialog_mode(screen: "DataMgmtScreen", is_dialog: bool) -> None:
    """Swap the flat list + single search box for the dialogue tree + filters."""
    screen.query_one("#dm-filter", Input).display = not is_dialog
    screen.query_one("#dm-dialog-filter-row").display = is_dialog
    screen.query_one("#dm-list", ListView).display = not is_dialog
    screen.query_one("#dm-dialog-tree", Tree).display = is_dialog
    screen.query_one("#dm-expand", Button).display = is_dialog
    screen.query_one("#dm-collapse", Button).display = is_dialog
    screen.query_one("#dm-copy", Button).display = is_dialog


def handle_input_changed(screen: "DataMgmtScreen", event: Input.Changed) -> None:
    """Handle filter input changes."""
    input_id = event.input.id
    if input_id == "dm-filter":
        rebuild_list_for_screen(screen)
    elif input_id in ("dm-filter-act", "dm-filter-chapter", "dm-filter-task", "dm-filter-character"):
        rebuild_dialog_tree_for_screen(screen)


def handle_list_view_highlighted(screen: "DataMgmtScreen", event: ListView.Highlighted) -> None:
    """Handle list item highlighting."""
    record = event.item.record if isinstance(event.item, _RecordRow) else None
    panel = screen.query_one("#dm-detail-text", Static)
    update_detail_for_record(panel, record)


def handle_tree_node_highlighted(screen: "DataMgmtScreen", event: Tree.NodeHighlighted) -> None:
    """Handle tree node highlighting."""
    if screen._category != _DIALOG_CATEGORY:
        return
    node = event.node
    data = node.data
    panel = screen.query_one("#dm-detail-text", Static)
    if isinstance(data, DialogueLine):
        update_detail_for_single_dialogue(panel, data)
    else:
        lines = collect_dialogue_lines_from_node(node)
        update_detail_for_multiple_dialogue(panel, lines)


def handle_button_pressed(screen: "DataMgmtScreen", event: Button.Pressed) -> None:
    """Handle button presses."""
    bid = event.button.id or ""
    if bid == "dm-expand":
        try:
            tree = screen.query_one("#dm-dialog-tree", Tree)
            expand_all_nodes(tree)
            # Mark all expanded nodes as explicitly expanded by user
            _mark_all_as_user_expanded(screen, tree)
        except Exception:
            pass
    elif bid == "dm-collapse":
        try:
            tree = screen.query_one("#dm-dialog-tree", Tree)
            collapse_all_nodes(tree)
            # Mark all collapsed nodes as explicitly collapsed by user
            _mark_all_as_user_collapsed(screen, tree)
        except Exception:
            pass
    elif bid == "dm-copy":
        handle_copy_action(screen)


def _mark_all_as_user_expanded(screen: "DataMgmtScreen", tree: Tree) -> None:
    """Mark all currently expanded nodes as explicitly expanded by the user."""
    def visit(node) -> None:
        if node is tree.root:
            for child in get_node_children(node):
                visit(child)
            return
        label = node_label_text(node)
        if label and is_node_expanded(node):
            screen._user_expanded.add(label)
            screen._user_collapsed.discard(label)
        for child in get_node_children(node):
            visit(child)
    visit(tree.root)


def _mark_all_as_user_collapsed(screen: "DataMgmtScreen", tree: Tree) -> None:
    """Mark all currently collapsed nodes as explicitly collapsed by the user."""
    def visit(node) -> None:
        if node is tree.root:
            for child in get_node_children(node):
                visit(child)
            return
        label = node_label_text(node)
        if label and not is_node_expanded(node):
            screen._user_collapsed.add(label)
            screen._user_expanded.discard(label)
        for child in get_node_children(node):
            visit(child)
    visit(tree.root)


def handle_copy_action(screen: "DataMgmtScreen") -> None:
    """Copy currently visible tree (or selected subtree/line) to clipboard."""
    try:
        tree = screen.query_one("#dm-dialog-tree", Tree)
    except Exception:
        tree = None

    text = ""
    highlighted = None
    if tree is not None:
        highlighted = getattr(tree, "highlighted_node", None) or getattr(tree, "focused_node", None)

    if highlighted and highlighted is not tree.root:
        lines = serialize_node_visible(highlighted, depth=0)
        text = "\n".join(lines)
    else:
        if tree is not None:
            lines = []
            root = tree.root
            children = getattr(root, "children", None)
            iterable = children.values() if isinstance(children, dict) else list(children or [])
            for child in iterable:
                lines.extend(serialize_node_visible(child, depth=0))
            text = "\n".join(lines)
        else:
            if screen._last_filtered:
                text = serialize_filtered_tree(screen._last_filtered)
            else:
                full = get_dialogue_tree()
                text = serialize_filtered_tree(full)

    success, status = copy_to_clipboard(text)
    screen.query_one("#dm-status", Static).update(status)


def rebuild_list_for_screen(screen: "DataMgmtScreen") -> None:
    """Rebuild the flat list view with filtered records."""
    if not screen._loaded:
        return
    query = screen.query_one("#dm-filter", Input).value.strip()
    lv = screen.query_one("#dm-list", ListView)
    lv.clear()
    records = search_records(screen._category, query)
    for record in records:
        lv.append(_RecordRow(record))
    screen.query_one("#dm-status", Static).update(f"{len(records)} result(s)")
    panel = screen.query_one("#dm-detail-text", Static)
    update_detail_for_record(panel, records[0] if records else None)


def rebuild_dialog_tree_for_screen(screen: "DataMgmtScreen") -> None:
    """Rebuild the dialogue tree with filtered data, preserving explicit user expansion state."""
    if not screen._loaded:
        return
    
    tree = screen.query_one("#dm-dialog-tree", Tree)
    
    total_lines, filtered = rebuild_dialog_tree(
        tree,
        act_query=screen.query_one("#dm-filter-act", Input).value.strip(),
        chapter_query=screen.query_one("#dm-filter-chapter", Input).value.strip(),
        task_query=screen.query_one("#dm-filter-task", Input).value.strip(),
        character_query=screen.query_one("#dm-filter-character", Input).value.strip(),
        user_expanded=screen._user_expanded,
        user_collapsed=screen._user_collapsed,
    )
    screen._last_filtered = filtered
    screen.query_one("#dm-status", Static).update(f"{total_lines} line(s)")
    panel = screen.query_one("#dm-detail-text", Static)
    update_detail_for_single_dialogue(panel, None)