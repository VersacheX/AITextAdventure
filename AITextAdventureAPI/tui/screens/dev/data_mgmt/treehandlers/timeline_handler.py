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
    """Render the Rich-markup label for a task leaf.

    Errors render in red, warnings in yellow.  If a node has both the
    highest-severity colour wins (red takes priority).
    """
    if task_node.errors:
        has_error   = any(e.severity == "error"   for e in task_node.errors)
        has_warning = any(e.severity == "warning" for e in task_node.errors)
        colour = "red" if has_error else "yellow"
        n      = len(task_node.errors)
        label  = rich_escape(task_node.label)
        tid    = rich_escape(task_node.task_id)
        return (
            f"[{colour}]{label}[/{colour}]  "
            f"[dim {colour}]{tid}[/dim {colour}]  "
            f"[{colour}]({'errors' if has_error else 'warnings'}: {n})[/{colour}]"
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