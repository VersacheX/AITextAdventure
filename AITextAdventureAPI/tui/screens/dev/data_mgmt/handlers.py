"""
Event handlers for tab activation, input changes, list/tree highlighting, and button presses.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from textual.containers import Vertical
from textual.widgets import Button, Input, ListView, RadioSet, Static, Tabs, Tree

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
    filter_equipment_records,
    get_dialogue_tree,
    search_records,
)

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen

_DIALOG_CATEGORY = "character_dialog"
_EQUIPMENT_CATEGORY = "equipment"


def handle_tab_activated(screen: "DataMgmtScreen", event: Tabs.TabActivated) -> None:
    """Handle tab activation from the Tabs widget."""
    tab_id = event.tab.id or ""
    if tab_id.startswith("tab-"):
        category = tab_id.removeprefix("tab-")
        if category in CATEGORIES:
            screen._category = category
            is_dialog = category == _DIALOG_CATEGORY
            set_dialog_mode(screen, is_dialog)
            set_filter_mode(screen, category)
            if category == _DIALOG_CATEGORY:
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


def set_filter_mode(screen: "DataMgmtScreen", category: str) -> None:
    """Swap filter UI based on category: default search / dialogue filters / equipment filters."""
    is_dialog = category == _DIALOG_CATEGORY
    is_equipment = category == _EQUIPMENT_CATEGORY

    screen.query_one("#dm-filter", Input).display = not (is_dialog or is_equipment)
    screen.query_one("#dm-dialog-filter-row").display = is_dialog
    screen.query_one("#dm-equipment-filter-row", Vertical).display = is_equipment
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


def handle_radio_set_changed(screen: "DataMgmtScreen", event: RadioSet.Changed) -> None:
    """Handle equipment filter radio button changes."""
    if event.radio_set.id in ("dm-equipment-type-radio", "dm-equipment-slot-radio"):
        rebuild_list_for_screen(screen)


def get_equipment_type_filter(screen: "DataMgmtScreen") -> str:
    """Get the selected equipment type from radio buttons."""
    try:
        type_radio = screen.query_one("#dm-equipment-type-radio", RadioSet)
        pressed_id = type_radio.pressed_button.id if type_radio.pressed_button else "equip-type-all"
        if pressed_id == "equip-type-weapon":
            return "weapon"
        elif pressed_id == "equip-type-armor":
            return "armor"
        return ""  # "All" selected
    except Exception:
        return ""


def get_equipment_slot_filter(screen: "DataMgmtScreen") -> str:
    """Get the selected armor slot from radio buttons."""
    try:
        slot_radio = screen.query_one("#dm-equipment-slot-radio", RadioSet)
        pressed_id = slot_radio.pressed_button.id if slot_radio.pressed_button else "equip-slot-all"
        if pressed_id == "equip-slot-head":
            return "head"
        elif pressed_id == "equip-slot-body":
            return "body"
        elif pressed_id == "equip-slot-arms":
            return "arms"
        elif pressed_id == "equip-slot-legs":
            return "legs"
        return ""  # "All" selected
    except Exception:
        return ""


def handle_list_view_highlighted(screen: "DataMgmtScreen", event: ListView.Highlighted) -> None:
    """Handle list item selection."""
    record = event.item.record if isinstance(event.item, _RecordRow) else None
    update_detail_for_record(screen, record)


def handle_tree_node_highlighted(screen: "DataMgmtScreen", event: Tree.NodeHighlighted) -> None:
    """Handle tree node selection (dialogue category)."""
    if screen._category != _DIALOG_CATEGORY:
        return
    node = event.node
    data = node.data
    if isinstance(data, DialogueLine):
        update_detail_for_single_dialogue(screen, data)
    else:
        lines = collect_dialogue_lines_from_node(node)
        update_detail_for_multiple_dialogue(screen, lines)


def handle_button_pressed(screen: "DataMgmtScreen", event: Button.Pressed) -> None:
    """Handle button clicks (expand/collapse/copy)."""
    bid = event.button.id or ""
    if bid == "dm-expand":
        expand_all_nodes(screen.query_one("#dm-dialog-tree", Tree))
    elif bid == "dm-collapse":
        collapse_all_nodes(screen.query_one("#dm-dialog-tree", Tree))
    elif bid == "dm-copy":
        handle_copy_action(screen)


def rebuild_list_for_screen(screen: "DataMgmtScreen") -> None:
    """Rebuild the flat list view with filtered records."""
    if not screen._loaded:
        return

    if screen._category == _EQUIPMENT_CATEGORY:
        records = filter_equipment_records(
            type_query=get_equipment_type_filter(screen),
            slot_query=get_equipment_slot_filter(screen),
        )
    else:
        query = screen.query_one("#dm-filter", Input).value.strip()
        records = search_records(screen._category, query)

    lv = screen.query_one("#dm-list", ListView)
    lv.clear()
    for record in records:
        lv.append(_RecordRow(record))
    screen.query_one("#dm-status", Static).update(f"{len(records)} result(s)")
    update_detail_for_record(screen, records[0] if records else None)


def rebuild_dialog_tree_for_screen(screen: "DataMgmtScreen") -> None:
    """Rebuild the dialogue tree with filtered data, preserving expansion state."""
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
    update_detail_for_single_dialogue(screen, None)


def handle_copy_action(screen: "DataMgmtScreen") -> None:
    """Copy visible tree content to clipboard."""
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
            children = get_node_children(root)
            for child in children:
                lines.extend(serialize_node_visible(child, depth=0))
            text = "\n".join(lines)
        else:
            if screen._last_filtered:
                text = serialize_filtered_tree(screen._last_filtered)
            else:
                full = get_dialogue_tree()
                text = serialize_filtered_tree(full)

    copied = copy_to_clipboard(text)
    status = "Copied to clipboard" if copied else "Saved to temp file (fallback)"
    screen.query_one("#dm-status", Static).update(status)