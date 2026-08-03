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


def _npc_leaf_label(npc_node: NpcRecordNode) -> str:
    """Build a Rich-markup label for a leaf node, with severity prefix if validated."""
    base = (
        f"{rich_escape(npc_node.label)}  "
        f"[dim]{rich_escape(npc_node.npc_id)}[/dim]"
    )
    extras = npc_node.record.extras if npc_node.record else {}
    if not extras.get("_validated"):
        return base

    errors = extras.get("_errors") or []
    hard   = [e for e in errors if e.severity == "error"]
    info   = [e for e in errors if e.severity == "info"]

    if hard:
        count = len(hard)
        return f"[red]✗[/red] {base}  [red dim]{count} err[/red dim]"
    if info:
        count = len(info)
        return f"[cyan]ℹ[/cyan] {base}  [cyan dim]{count} info[/cyan dim]"
    return f"[green]✓[/green] {base}"


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
            label = _npc_leaf_label(npc_node)
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