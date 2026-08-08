"""
Dungeon tree rebuild and validation.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from textual.widgets import Static

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen


def rebuild_dungeon_tree_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.screens.dev.data_mgmt.treehandlers.dungeon_handler import rebuild_dungeon_tree  # noqa: PLC0415
    from tui.screens.dev.data_mgmt.detail_panel import update_detail_for_dungeon_group       # noqa: PLC0415
    from textual.widgets import Input, Tree                                                   # noqa: PLC0415

    if not screen._loaded:
        return
    query = ""
    try:
        query = screen.query_one("#dm-filter", Input).value.strip()
    except Exception:
        pass

    tree = screen.query_one("#dm-dungeon-tree", Tree)
    total, filtered = rebuild_dungeon_tree(
        tree,
        query=query,
        user_expanded=screen._dungeon_user_expanded,
        user_collapsed=screen._dungeon_user_collapsed,
    )
    screen._last_dungeon_filtered = filtered
    screen.query_one("#dm-status", Static).update(f"{total} dungeon(s)")
    update_detail_for_dungeon_group(screen, [])


def validate_dungeons_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.services.dev.dataservices.dungeon_validator import validate_dungeon_tree  # noqa: PLC0415
    from tui.services.dev.dataservices.catalog import get_dungeon_tree                 # noqa: PLC0415
    import game.constants as const                                                     # noqa: PLC0415

    tree    = get_dungeon_tree()
    summary = validate_dungeon_tree(tree, const)

    rebuild_dungeon_tree_for_screen(screen)

    invalid      = summary.get("invalid", 0)
    total_errors = summary.get("total_errors", 0)

    if total_errors == 0:
        screen.notify("✓ Dungeon integrity OK — no issues found.", timeout=3.0)
    else:
        screen.notify(
            f"✗ {total_errors} issue(s) across {invalid} dungeon(s) — flagged in tree.",
            severity="warning",
            timeout=5.0,
        )