"""
Timeline tree building, filtering, and traversal logic.

Mirrors dialog_tree.py but operates on the independent
TimelineGroupNode → TimelineBucketNode → TimelineTaskNode model built by
dev_data_service._build_timeline_tree().  Has no relation to the dialogue tree.
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
from tui.services.dev.dev_data_service import (
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
    """Rebuild the timeline tree widget with filtered data, preserving explicit user expansion state.

    Group nodes default to expanded; bucket nodes default to collapsed.
    An active filter auto-expands all branches temporarily.

    Returns:
        (total_tasks, filtered_model) where filtered_model is the list of TimelineGroupNode
        used for copy operations.
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
                label = (
                    f"{rich_escape(task_node.label)}  "
                    f"[dim]{rich_escape(task_node.task_id)}[/dim]"
                )
                bucket_branch.add_leaf(label, data=task_node)

    restore_user_expansion_state(tree, user_expanded, user_collapsed, filter_active)
    return total_tasks, filtered


def collect_timeline_tasks_from_node(node: TreeNode) -> List[TimelineTaskNode]:
    """Recursively collect all TimelineTaskNode objects from a subtree."""
    collected: List[TimelineTaskNode] = []
    data = node.data
    if isinstance(data, TimelineTaskNode):
        collected.append(data)
    for child in get_node_children(node):
        collected.extend(collect_timeline_tasks_from_node(child))
    return collected