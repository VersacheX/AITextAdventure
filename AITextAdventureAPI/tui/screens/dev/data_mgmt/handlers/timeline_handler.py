"""
Timeline tree rebuild and validation.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from textual.widgets import Static

from tui.services.dev.dataservices import get_timeline_tree
from tui.services.dev.dataservices.timeline_validator import validate_timeline_integrity

if TYPE_CHECKING:
    from tui.screens.dev.data_mgmt.data_mgmt_screen import DataMgmtScreen


def rebuild_timeline_tree_for_screen(screen: "DataMgmtScreen") -> None:
    from tui.screens.dev.data_mgmt.treehandlers.timeline_handler import rebuild_timeline_tree  # noqa: PLC0415
    from tui.screens.dev.data_mgmt.detail_panel import update_detail_for_timeline_subtree      # noqa: PLC0415
    from textual.widgets import Input, Tree                                                     # noqa: PLC0415

    if not screen._loaded:
        return
    query = ""
    try:
        query = screen.query_one("#dm-filter", Input).value.strip()
    except Exception:
        pass

    tree = screen.query_one("#dm-timeline-tree", Tree)
    total_tasks, filtered = rebuild_timeline_tree(
        tree,
        query=query,
        user_expanded=screen._timeline_user_expanded,
        user_collapsed=screen._timeline_user_collapsed,
    )
    screen._last_timeline_filtered = filtered
    screen.query_one("#dm-status", Static).update(f"{total_tasks} task(s)")
    update_detail_for_timeline_subtree(screen, [])


def validate_timeline_for_screen(screen: "DataMgmtScreen") -> None:
    import game.constants as const  # noqa: PLC0415

    groups = get_timeline_tree()
    validate_timeline_integrity(groups, const)

    rebuild_timeline_tree_for_screen(screen)

    error_tasks = warning_tasks = duplicate_tasks = notice_tasks = 0
    for group in groups:
        for bucket in group.buckets:
            for tn in bucket.tasks:
                if any(e.severity == "error"     for e in tn.errors):
                    error_tasks += 1
                if any(e.severity == "warning"   for e in tn.errors):
                    warning_tasks += 1
                if any(e.severity == "duplicate" for e in tn.errors):
                    duplicate_tasks += 1
                if any(e.severity == "notice"    for e in tn.errors):
                    notice_tasks += 1

    total_tasks = error_tasks + warning_tasks + duplicate_tasks + notice_tasks

    if total_tasks == 0:
        screen.notify("✓ Timeline integrity OK — no errors found.", timeout=3.0)
    else:
        parts = []
        if error_tasks:
            parts.append(f"{error_tasks} error task(s)")
        if warning_tasks:
            parts.append(f"{warning_tasks} warning task(s)")
        if duplicate_tasks:
            parts.append(f"{duplicate_tasks} duplicate task(s)")
        if notice_tasks:
            parts.append(f"{notice_tasks} notice task(s)")
        screen.notify(
            f"✗ {total_tasks} total affected task(s): {', '.join(parts)}.",
            severity="warning",
            timeout=5.0,
        )