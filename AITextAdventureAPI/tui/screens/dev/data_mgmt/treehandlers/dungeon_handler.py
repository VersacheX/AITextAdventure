"""
Dungeon tree: widget population, filtering, and node traversal.
Operates on #dm-dungeon-tree using the DungeonGroupNode / DungeonNode models.

Tree shape: Group (expanded) → Dungeon leaf
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
from tui.services.dev.dataservices.models import DungeonGroupNode, DungeonNode

_GROUP_COLOURS: dict[str, str] = {
    "main_story":    "cyan",
    "primary_story": "yellow",
    "city_regional": "green",
}


def rebuild_dungeon_tree(
    tree: Tree,
    query: str,
    user_expanded: Set[str],
    user_collapsed: Set[str],
) -> tuple[int, list]:
    """Rebuild the dungeon tree widget, preserving explicit user expansion state.

    Group nodes default to expanded; individual dungeon leaves are leaves.

    Returns:
        (total_dungeons, filtered_model)
    """
    from tui.services.dev.dataservices.catalog import get_dungeon_tree  # noqa: PLC0415
    from tui.services.dev.dataservices.dungeon_service import filter_dungeon_tree  # noqa: PLC0415

    save_user_expansion_state(tree, user_expanded, user_collapsed)
    tree.clear()

    full_tree     = get_dungeon_tree()
    filtered      = filter_dungeon_tree(full_tree, query=query)
    filter_active = bool(query)

    total_dungeons = 0
    for group_node in filtered:
        colour       = _GROUP_COLOURS.get(group_node.group_id, "white")
        count        = len(group_node.dungeons)
        group_label  = (
            f"[bold {colour}]{rich_escape(group_node.label)}[/bold {colour}]"
            f"  [dim]({count})[/dim]"
        )
        group_branch = tree.root.add(group_label, expand=True)

        for dungeon_node in group_node.dungeons:
            total_dungeons += 1
            label = _dungeon_leaf_label(dungeon_node)
            group_branch.add_leaf(label, data=dungeon_node)

    restore_user_expansion_state(tree, user_expanded, user_collapsed, filter_active)
    return total_dungeons, filtered


def _dungeon_leaf_label(node: DungeonNode) -> str:
    """Render the Rich-markup label for a dungeon leaf."""
    name = rich_escape(node.label)
    did  = rich_escape(node.dungeon_id)
    if node.errors:
        has_error = any(e.severity == "error"   for e in node.errors)
        has_warn  = any(e.severity == "warning" for e in node.errors)
        if has_error:
            colour, kind = "red", "error"
        elif has_warn:
            colour, kind = "yellow", "warn"
        else:
            colour, kind = "magenta", "notice"
        n = len(node.errors)
        return (
            f"[{colour}]{name}[/{colour}]  "
            f"[dim {colour}]{did}[/dim {colour}]  "
            f"[{colour}]({kind}: {n})[/{colour}]"
        )
    return f"{name}  [dim]{did}[/dim]"


def collect_dungeon_nodes_from_node(node: TreeNode) -> List[DungeonNode]:
    """Recursively collect all DungeonNode objects from a subtree."""
    collected: List[DungeonNode] = []
    if isinstance(node.data, DungeonNode):
        collected.append(node.data)
    for child in get_node_children(node):
        collected.extend(collect_dungeon_nodes_from_node(child))
    return collected