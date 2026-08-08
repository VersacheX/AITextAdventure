"""
Dialog tree rebuild.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from textual.widgets import Static

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen


def rebuild_dialog_tree_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.screens.dev.data_mgmt.treehandlers.dialog_handler import rebuild_dialog_tree  # noqa: PLC0415
    from tui.screens.dev.data_mgmt.detail_panel import update_detail_for_single_dialogue   # noqa: PLC0415
    from textual.widgets import Input, Tree                                                 # noqa: PLC0415

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