"""
Dialogue tree building, filtering, and traversal logic.
"""
from __future__ import annotations

from typing import List, Set

from rich.markup import escape as rich_escape
from textual.widgets import Tree
from textual.widgets.tree import TreeNode

from tui.screens.dev.data_mgmt.utils import collect_expanded_paths, is_node_expanded
from tui.services.dev.dev_data_service import DialogueLine, filter_dialogue_tree, get_dialogue_tree


def rebuild_dialog_tree(
    tree: Tree,
    act_query: str,
    chapter_query: str,
    task_query: str,
    character_query: str,
    expanded_paths: Set[str] | None = None,
) -> tuple[int, list]:
    """
    Rebuild the dialogue tree widget with filtered data.

    Args:
        tree: The Tree widget to rebuild.
        act_query: Filter query for act.
        chapter_query: Filter query for chapter.
        task_query: Filter query for task.
        character_query: Filter query for character.
        expanded_paths: Set of node paths that were expanded before rebuild.
                       If provided, these paths will be re-expanded in the new tree.

    Returns:
        (total_lines, filtered_model) where filtered_model is the list of act nodes
        used for copy operations.
    """
    # Capture current expansion state before clearing if not provided
    if expanded_paths is None:
        expanded_paths = collect_expanded_paths(tree.root)
    
    tree.clear()

    full_tree = get_dialogue_tree()
    filtered = filter_dialogue_tree(
        full_tree,
        act_query=act_query,
        chapter_query=chapter_query,
        task_query=task_query,
        character_query=character_query,
    )

    total_lines = 0
    for act_node in filtered:
        act_path = act_node.label
        act_should_expand = act_path in expanded_paths
        act_branch = tree.root.add(act_node.label, expand=act_should_expand)
        
        for chapter_node in act_node.chapters:
            chapter_path = f"{act_path}/{chapter_node.label}"
            chapter_should_expand = chapter_path in expanded_paths
            chapter_branch = act_branch.add(chapter_node.label, expand=chapter_should_expand)
            
            for task_node in chapter_node.tasks:
                task_path = f"{chapter_path}/{task_node.label}"
                task_should_expand = task_path in expanded_paths
                task_branch = chapter_branch.add(task_node.label, expand=task_should_expand)
                
                for stage_node in task_node.stages:
                    stage_path = f"{task_path}/{stage_node.label}"
                    stage_should_expand = stage_path in expanded_paths
                    stage_branch = task_branch.add(
                        f"[dim]{stage_node.label}[/dim]", expand=stage_should_expand
                    )
                    
                    for line in stage_node.lines:
                        total_lines += 1
                        speaker = rich_escape(line.speaker)
                        text_preview = rich_escape(
                            line.text[:60] + "..." if len(line.text) > 60 else line.text
                        )
                        stage_branch.add_leaf(f"{speaker}: {text_preview}", data=line)

    return total_lines, filtered


def collect_dialogue_lines_from_node(node: TreeNode) -> List[DialogueLine]:
    """Recursively collect all DialogueLine objects from a TreeNode subtree."""
    collected: List[DialogueLine] = []
    data = node.data
    if isinstance(data, DialogueLine):
        collected.append(data)
    children = getattr(node, "children", None)
    if isinstance(children, dict):
        iterable = children.values()
    else:
        iterable = list(children or [])
    for child in iterable:
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
    children = getattr(node, "children", None)
    if isinstance(children, dict):
        iterable = children.values()
    else:
        iterable = list(children or [])
    for child in iterable:
        _traverse_and_apply(child, expand=expand)