"""
Dialogue tree building, filtering, and traversal logic.
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
from tui.services.dev.dev_data_service import DialogueLine, filter_dialogue_tree, get_dialogue_tree


def rebuild_dialog_tree(
    tree: Tree,
    act_query: str,
    chapter_query: str,
    task_query: str,
    character_query: str,
    user_expanded: Set[str],
    user_collapsed: Set[str],
) -> tuple[int, list]:
    """
    Rebuild the dialogue tree widget with filtered data, preserving **explicit user expansion state**.

    **Option 3 behavior**:
    - Before rebuild: save current expansion state (updates user_expanded/user_collapsed).
    - After rebuild: restore user_expanded nodes as expanded, user_collapsed as collapsed.
    - If a filter is active, matching nodes auto-expand temporarily (without being added to user_expanded).
    - When filter is cleared, only explicitly expanded nodes remain open.

    Args:
        tree: The Tree widget to rebuild.
        act_query: Filter query for act.
        chapter_query: Filter query for chapter.
        task_query: Filter query for task.
        character_query: Filter query for character.
        user_expanded: Set of node labels the user explicitly expanded (modified in-place).
        user_collapsed: Set of node labels the user explicitly collapsed (modified in-place).

    Returns:
        (total_lines, filtered_model) where filtered_model is the list of act nodes
        used for copy operations.
    """
    # === SAVE: update user expansion state from current tree ===
    save_user_expansion_state(tree, user_expanded, user_collapsed)
    
    tree.clear()

    full_tree = get_dialogue_tree()
    filtered = filter_dialogue_tree(
        full_tree,
        act_query=act_query,
        chapter_query=chapter_query,
        task_query=task_query,
        character_query=character_query,
    )

    # Check if any filter is active
    filter_active = bool(act_query or chapter_query or task_query or character_query)

    total_lines = 0
    for act_node in filtered:
        # Acts default to expanded (always visible level)
        act_branch = tree.root.add(act_node.label, expand=True)
        for chapter_node in act_node.chapters:
            chapter_branch = act_branch.add(chapter_node.label, expand=False)
            for task_node in chapter_node.tasks:
                task_branch = chapter_branch.add(task_node.label, expand=False)
                for stage_node in task_node.stages:
                    stage_branch = task_branch.add(f"[dim]{stage_node.label}[/dim]", expand=False)
                    for line in stage_node.lines:
                        total_lines += 1
                        speaker = rich_escape(line.speaker)
                        text_preview = rich_escape(
                            line.text[:60] + "..." if len(line.text) > 60 else line.text
                        )
                        stage_branch.add_leaf(f"{speaker}: {text_preview}", data=line)

    # === RESTORE: apply user expansion state + temporary filter expansions ===
    restore_user_expansion_state(tree, user_expanded, user_collapsed, filter_active)

    return total_lines, filtered


def collect_dialogue_lines_from_node(node: TreeNode) -> List[DialogueLine]:
    """Recursively collect all DialogueLine objects from a TreeNode subtree."""
    collected: List[DialogueLine] = []
    data = node.data
    if isinstance(data, DialogueLine):
        collected.append(data)
    for child in get_node_children(node):
        collected.extend(collect_dialogue_lines_from_node(child))
    return collected


def expand_all_nodes(tree: Tree) -> None:
    """Recursively expand every node in the tree."""
    root = tree.root
    _traverse_and_apply(root, expand=True)


def collapse_all_nodes(tree: Tree) -> None:
    """Recursively collapse every node in the tree."""
    root = tree.root
    _traverse_and_apply(root, expand=False)


def _traverse_and_apply(node: TreeNode, *, expand: bool) -> None:
    """Recursive helper: call expand()/collapse() on node and descendants."""
    try:
        if expand:
            node.expand()
        else:
            node.collapse()
    except Exception:
        pass
    for child in get_node_children(node):
        _traverse_and_apply(child, expand=expand)