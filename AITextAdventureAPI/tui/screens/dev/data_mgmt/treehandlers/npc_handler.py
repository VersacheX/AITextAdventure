"""
NPC tree: widget population, filtering, and node traversal.
Operates on #dm-npc-tree using the NpcGroupNode model.
NPC leaf selection passes node.data.record (a DevRecord) to the existing
NpcDetailPanel — portrait rendering is fully preserved.
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
    NpcRecordNode,
    filter_npc_tree,
    get_npc_tree,
)


def rebuild_npc_tree(
    tree: Tree,
    query: str,
    user_expanded: Set[str],
    user_collapsed: Set[str],
) -> tuple[int, list]:
    """Rebuild the NPC tree widget, preserving explicit user expansion state.

    Group nodes default to expanded; NPC leaves are direct children.

    Returns:
        (total_npcs, filtered_model)
    """
    save_user_expansion_state(tree, user_expanded, user_collapsed)
    tree.clear()

    full_tree     = get_npc_tree()
    filtered      = filter_npc_tree(full_tree, query=query)
    filter_active = bool(query)

    total_npcs = 0
    for group_node in filtered:
        group_branch = tree.root.add(group_node.label, expand=True)
        for npc_node in group_node.npcs:
            total_npcs += 1
            label = (
                f"{rich_escape(npc_node.label)}  "
                f"[dim]{rich_escape(npc_node.npc_id)}[/dim]"
            )
            group_branch.add_leaf(label, data=npc_node)

    restore_user_expansion_state(tree, user_expanded, user_collapsed, filter_active)
    return total_npcs, filtered


def collect_npc_records_from_node(node: TreeNode) -> List[NpcRecordNode]:
    """Recursively collect all NpcRecordNode objects from a subtree."""
    collected: List[NpcRecordNode] = []
    if isinstance(node.data, NpcRecordNode):
        collected.append(node.data)
    for child in get_node_children(node):
        collected.extend(collect_npc_records_from_node(child))
    return collected