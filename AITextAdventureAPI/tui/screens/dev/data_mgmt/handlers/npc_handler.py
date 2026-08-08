"""
NPC tree rebuild and validation.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from textual.widgets import Static

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen


def rebuild_npc_tree_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.screens.dev.data_mgmt.treehandlers.npc_handler import rebuild_npc_tree  # noqa: PLC0415
    from textual.widgets import Input, Tree                                           # noqa: PLC0415

    if not screen._loaded:
        return
    query = ""
    try:
        query = screen.query_one("#dm-filter", Input).value.strip()
    except Exception:
        pass

    tree = screen.query_one("#dm-npc-tree", Tree)
    total_npcs, filtered = rebuild_npc_tree(
        tree,
        query=query,
        user_expanded=screen._npc_user_expanded,
        user_collapsed=screen._npc_user_collapsed,
    )
    screen._last_npc_filtered = filtered
    screen.query_one("#dm-status", Static).update(f"{total_npcs} NPC(s)")
    screen.restore_npc_selection()


def validate_npc_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.services.dev.dataservices.npc_validator import validate_npc_tree  # noqa: PLC0415
    from tui.services.dev.dataservices import get_npc_tree                     # noqa: PLC0415
    import game.constants as const                                              # noqa: PLC0415

    tree    = get_npc_tree()
    summary = validate_npc_tree(tree, const)

    rebuild_npc_tree_for_screen(screen)

    total_errors = summary.get("total_errors", 0)
    total_info   = summary.get("total_info", 0)
    invalid      = summary.get("invalid", 0)

    if total_errors == 0 and total_info == 0:
        screen.notify("✓ NPC integrity OK — all seeds complete.", timeout=3.0)
    elif total_errors == 0:
        screen.notify(
            f"ℹ {total_info} optional field(s) unset across {invalid} NPC(s) — shown in cyan.",
            severity="information",
            timeout=5.0,
        )
    else:
        screen.notify(
            f"✗ {total_errors} error(s) across {invalid} NPC(s) — flagged in tree.",
            severity="warning",
            timeout=5.0,
        )