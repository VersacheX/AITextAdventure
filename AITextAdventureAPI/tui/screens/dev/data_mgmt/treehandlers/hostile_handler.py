"""
Hostile tree: widget population, filtering, and node traversal.
Operates on #dm-hostile-tree using the HostileRarityNode model.

Tree shape: Rarity (expanded) → Level bucket (collapsed) → Hostile leaf
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
    HostileNode,
    filter_hostile_tree,
    get_hostile_tree,
)

_RARITY_COLOURS: dict[str, str] = {
    "common":    "white",
    "uncommon":  "green",
    "rare":      "cyan",
    "superrare": "yellow",
    "notfound":  "red",
}


def rebuild_hostile_tree(
    tree: Tree,
    query: str,
    user_expanded: Set[str],
    user_collapsed: Set[str],
) -> tuple[int, list]:
    """Rebuild the hostile tree widget, preserving explicit user expansion state.

    Rarity nodes default to expanded; level bucket nodes default to collapsed.

    Returns:
        (total_hostiles, filtered_model)
    """
    save_user_expansion_state(tree, user_expanded, user_collapsed)
    tree.clear()

    full_tree     = get_hostile_tree()
    filtered      = filter_hostile_tree(full_tree, query=query)
    filter_active = bool(query)

    total_hostiles = 0
    for rarity_node in filtered:
        colour       = _RARITY_COLOURS.get(rarity_node.rarity_id, "white")
        rarity_label = f"[bold {colour}]{rich_escape(rarity_node.label)}[/bold {colour}]"
        rarity_branch = tree.root.add(rarity_label, expand=True)

        for bucket_node in rarity_node.level_buckets:
            count        = len(bucket_node.hostiles)
            bucket_label = f"{rich_escape(bucket_node.label)}  [dim]({count})[/dim]"
            bucket_branch = rarity_branch.add(bucket_label, expand=False)

            for hostile_node in bucket_node.hostiles:
                total_hostiles += 1
                label = _hostile_leaf_label(hostile_node)
                bucket_branch.add_leaf(label, data=hostile_node)

    restore_user_expansion_state(tree, user_expanded, user_collapsed, filter_active)
    return total_hostiles, filtered


def _hostile_leaf_label(node: HostileNode) -> str:
    """Render the Rich-markup label for a hostile leaf.

    Errors → red, warnings → yellow.
    """
    name = rich_escape(node.label)
    hid  = rich_escape(node.hostile_id)
    if node.errors:
        has_error = any(e.severity == "error"   for e in node.errors)
        colour    = "red" if has_error else "yellow"
        kind      = "error" if has_error else "warn"
        n         = len(node.errors)
        return (
            f"[{colour}]{name}[/{colour}]  "
            f"[dim {colour}]{hid}[/dim {colour}]  "
            f"[{colour}]({kind}: {n})[/{colour}]"
        )
    return f"{name}  [dim]{hid}[/dim]"


def collect_hostile_nodes_from_node(node: TreeNode) -> List[HostileNode]:
    """Recursively collect all HostileNode objects from a subtree."""
    collected: List[HostileNode] = []
    if isinstance(node.data, HostileNode):
        collected.append(node.data)
    for child in get_node_children(node):
        collected.extend(collect_hostile_nodes_from_node(child))
    return collected