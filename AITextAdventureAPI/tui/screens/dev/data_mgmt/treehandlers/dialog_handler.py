"""
Dialogue tree: widget population, filtering, and node traversal.
Operates on #dm-dialog-tree using the DialogueActNode model.
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
    DialogueLine,
    filter_dialogue_tree,
    get_dialogue_tree,
)


def rebuild_dialog_tree(
    tree: Tree,
    act_query: str,
    chapter_query: str,
    task_query: str,
    character_query: str,
    user_expanded: Set[str],
    user_collapsed: Set[str],
) -> tuple[int, list]:
    """Rebuild the dialogue tree widget, preserving explicit user expansion state.

    Returns:
        (total_lines, filtered_model)
    """
    save_user_expansion_state(tree, user_expanded, user_collapsed)
    tree.clear()

    full_tree = get_dialogue_tree()
    filtered  = filter_dialogue_tree(
        full_tree,
        act_query=act_query,
        chapter_query=chapter_query,
        task_query=task_query,
        character_query=character_query,
    )
    filter_active = bool(act_query or chapter_query or task_query or character_query)

    total_lines = 0
    for act_node in filtered:
        act_branch = tree.root.add(act_node.label, expand=True)
        for chapter_node in act_node.chapters:
            chapter_branch = act_branch.add(chapter_node.label, expand=False)
            for task_node in chapter_node.tasks:
                task_branch = chapter_branch.add(task_node.label, expand=False)
                for stage_node in task_node.stages:
                    stage_branch = task_branch.add(f"[dim]{stage_node.label}[/dim]", expand=False)
                    for line in stage_node.lines:
                        total_lines += 1
                        speaker      = rich_escape(line.speaker)
                        text_preview = rich_escape(
                            line.text[:60] + "..." if len(line.text) > 60 else line.text
                        )
                        stage_branch.add_leaf(f"{speaker}: {text_preview}", data=line)

    restore_user_expansion_state(tree, user_expanded, user_collapsed, filter_active)
    return total_lines, filtered


def collect_dialogue_lines_from_node(node: TreeNode) -> List[DialogueLine]:
    """Recursively collect all DialogueLine objects from a subtree."""
    collected: List[DialogueLine] = []
    if isinstance(node.data, DialogueLine):
        collected.append(node.data)
    for child in get_node_children(node):
        collected.extend(collect_dialogue_lines_from_node(child))
    return collected