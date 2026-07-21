"""
Ability tree: widget population, filtering, and node traversal.
Operates on #dm-ability-tree using the AbilityTypeNode / AbilityLevelNode model.
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
    AbilityNode,
    filter_ability_tree,
    get_ability_tree,
)


def rebuild_ability_tree(
    tree: Tree,
    query: str,
    user_expanded: Set[str],
    user_collapsed: Set[str],
) -> tuple[int, list]:
    """Rebuild the ability tree widget, preserving explicit user expansion state.

    Type nodes default to expanded; level bucket nodes default to collapsed.

    Returns:
        (total_abilities, filtered_model)
    """
    save_user_expansion_state(tree, user_expanded, user_collapsed)
    tree.clear()

    full_tree     = get_ability_tree()
    filtered      = filter_ability_tree(full_tree, query=query)
    filter_active = bool(query)

    total_abilities = 0
    for type_node in filtered:
        type_branch = tree.root.add(
            f"[bold]{rich_escape(type_node.label)}[/bold]",
            expand=True,
        )
        for level_node in type_node.level_buckets:
            count        = len(level_node.abilities)
            level_label  = f"{rich_escape(level_node.label)}  [dim]({count})[/dim]"
            level_branch = type_branch.add(level_label, expand=False)
            for ability_node in level_node.abilities:
                total_abilities += 1
                label = _ability_leaf_label(ability_node)
                level_branch.add_leaf(label, data=ability_node)

    restore_user_expansion_state(tree, user_expanded, user_collapsed, filter_active)
    return total_abilities, filtered


def _ability_leaf_label(node: AbilityNode) -> str:
    """Render the Rich-markup label for an ability leaf.

    Errors render in red, warnings in yellow.
    """
    name = rich_escape(node.label)
    if node.errors:
        has_error   = any(e.severity == "error"   for e in node.errors)
        has_warning = any(e.severity == "warning" for e in node.errors)
        colour = "red" if has_error else "yellow"
        n      = len(node.errors)
        kind   = "error" if has_error else "warn"
        return (
            f"[{colour}]{name}[/{colour}]  "
            f"[dim {colour}]{rich_escape(node.ability_id)}[/dim {colour}]  "
            f"[{colour}]({kind}: {n})[/{colour}]"
        )
    return f"{name}  [dim]{rich_escape(node.ability_id)}[/dim]"


def collect_ability_nodes_from_node(node: TreeNode) -> List[AbilityNode]:
    """Recursively collect all AbilityNode objects from a subtree."""
    collected: List[AbilityNode] = []
    if isinstance(node.data, AbilityNode):
        collected.append(node.data)
    for child in get_node_children(node):
        collected.extend(collect_ability_nodes_from_node(child))
    return collected