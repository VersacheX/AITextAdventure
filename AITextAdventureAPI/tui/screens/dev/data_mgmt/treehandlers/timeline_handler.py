"""
Timeline tree: widget population, filtering, and node traversal.
Operates on #dm-timeline-tree using the TimelineGroupNode model.
"""
from __future__ import annotations

from typing import List, Set

from rich.markup import escape as rich_escape
from textual.widgets import Tree
from textual.widgets.tree import TreeNode

from tui.screens.dev.data_mgmt.utils import (
    get_node_children,
    restore_user_expansion_state,
    save_user_expansion_state,
)
from tui.services.dev.dataservices import (
    TimelineTaskNode,
    filter_timeline_tree,
    get_timeline_tree,
)


def rebuild_timeline_tree(
    tree: Tree,
    query: str,
    user_expanded: Set[str],
    user_collapsed: Set[str],
) -> tuple[int, list]:
    """Rebuild the NPC tree widget, preserving explicit user expansion state.

    Group nodes default to expanded; bucket nodes default to collapsed.

    Returns:
        (total_tasks, filtered_model)
    """
    save_user_expansion_state(tree, user_expanded, user_collapsed)
    tree.clear()

    full_tree     = get_timeline_tree()
    filtered      = filter_timeline_tree(full_tree, query=query)
    filter_active = bool(query)

    total_tasks = 0
    for group_node in filtered:
        group_branch = tree.root.add(group_node.label, expand=True)
        for bucket_node in group_node.buckets:
            bucket_branch = group_branch.add(bucket_node.label, expand=False)
            for task_node in bucket_node.tasks:
                total_tasks += 1
                label = _task_label(task_node)
                bucket_branch.add_leaf(label, data=task_node)

    restore_user_expansion_state(tree, user_expanded, user_collapsed, filter_active)
    return total_tasks, filtered


def _task_label(task_node: TimelineTaskNode) -> str:
    if task_node.errors:
        has_error       = any(e.severity == "error"     for e in task_node.errors)
        has_warning     = any(e.severity == "warning"   for e in task_node.errors)
        has_duplicate   = any(e.severity == "duplicate" for e in task_node.errors)
        has_notice      = any(e.severity == "notice" and e.code != "MEET_DELIVER_NO_CHARACTER_DIALOG" for e in task_node.errors)
        has_blue_notice = any(e.severity == "notice" and e.code == "MEET_DELIVER_NO_CHARACTER_DIALOG" for e in task_node.errors)
        has_info        = any(e.severity == "info"      for e in task_node.errors)

        import logging
        logging.getLogger(__name__).debug(
            "_task_label %s → severities=%s",
            task_node.task_id,
            [e.severity for e in task_node.errors],
        )

        label = rich_escape(task_node.label)
        tid   = rich_escape(task_node.task_id)

        if has_error:
            n = sum(1 for e in task_node.errors if e.severity == "error")
            return (
                f"[red]{label}[/red]  "
                f"[dim red]{tid}[/dim red]  "
                f"[red](errors: {n})[/red]"
            )
        if has_warning:
            n = sum(1 for e in task_node.errors if e.severity == "warning")
            return (
                f"[yellow]{label}[/yellow]  "
                f"[dim yellow]{tid}[/dim yellow]  "
                f"[yellow](warnings: {n})[/yellow]"
            )
        if has_duplicate:
            n = sum(1 for e in task_node.errors if e.severity == "duplicate")
            return (
                f"[#c084fc]{label}[/#c084fc]  "
                f"[dim #c084fc]{tid}[/dim #c084fc]  "
                f"[#c084fc](duplicates: {n})[/#c084fc]"
            )
        if has_notice:
            n = sum(1 for e in task_node.errors if e.severity == "notice" and e.code != "MEET_DELIVER_NO_CHARACTER_DIALOG")
            return (
                f"[#e040fb]{label}[/#e040fb]  "
                f"[dim #e040fb]{tid}[/dim #e040fb]  "
                f"[#e040fb](notice: {n})[/#e040fb]"
            )
        if has_blue_notice:
            n = sum(1 for e in task_node.errors if e.severity == "notice" and e.code == "MEET_DELIVER_NO_CHARACTER_DIALOG")
            return (
                f"[#2323ff]{label}[/#2323ff]  "
                f"[dim #2323ff]{tid}[/dim #2323ff]  "
                f"[#2323ff](notice: {n})[/#2323ff]"
            )
        if has_info:
            return (
                f"[cyan]{label}[/cyan]  "
                f"[dim cyan]{tid}[/dim cyan]"
            )

    return (
        f"{rich_escape(task_node.label)}  "
        f"[dim]{rich_escape(task_node.task_id)}[/dim]"
    )


def collect_timeline_tasks_from_node(node: TreeNode) -> List[TimelineTaskNode]:
    """Recursively collect all TimelineTaskNode objects from a subtree."""
    collected: List[TimelineTaskNode] = []
    if isinstance(node.data, TimelineTaskNode):
        collected.append(node.data)
    for child in get_node_children(node):
        collected.extend(collect_timeline_tasks_from_node(child))
    return collected