"""
Utility functions for serialization, clipboard operations, and node inspection.
Shared by all tree handlers.
"""
from __future__ import annotations

from typing import List, Set

from textual.widgets import Tree
from textual.widgets.tree import TreeNode

from tui.services.dev.dataservices import DialogueLine, NpcRecordNode, TimelineTaskNode


def serialize_node_visible(node: TreeNode, depth: int) -> List[str]:
    """Return text lines for ``node`` and its visible children (expanded only)."""
    out: List[str] = []
    data = getattr(node, "data", None)

    if isinstance(data, DialogueLine):
        out.append("  " * depth + f"{data.speaker}: {data.text}")
        return out

    if isinstance(data, TimelineTaskNode):
        out.append("  " * depth + f"{data.label}  [{data.task_id}]  ({data.source_path})")
        return out

    if isinstance(data, NpcRecordNode):
        out.append("  " * depth + f"{data.label}  [{data.npc_id}]  ({data.source_group})")
        return out

    label = node_label_text(node)
    out.append("  " * depth + label)

    if not is_node_expanded(node):
        return out

    for child in get_node_children(node):
        out.extend(serialize_node_visible(child, depth + 1))
    return out


def is_node_expanded(node: TreeNode) -> bool:
    """Robustly check whether a TreeNode is expanded across Textual versions."""
    for attr in ("is_expanded", "expanded", "is_open", "open"):
        val = getattr(node, attr, None)
        if val is not None:
            if callable(val):
                try:
                    return bool(val())
                except Exception:
                    continue
            return bool(val)
    val = getattr(node, "_is_expanded", None) or getattr(node, "_expanded", None)
    if val is not None:
        return bool(val)
    children = getattr(node, "children", None)
    return False if children else True


def node_label_text(node: TreeNode) -> str:
    """Get a string label for a tree node in a best-effort way."""
    for attr in ("label", "_label", "renderable", "text"):
        val = getattr(node, attr, None)
        if val is None:
            continue
        try:
            return str(val).strip()
        except Exception:
            continue
    try:
        return str(node).strip()
    except Exception:
        return "<node>"


def get_node_children(node: TreeNode) -> List[TreeNode]:
    """Get list of children from a TreeNode (robust across Textual versions)."""
    children = getattr(node, "children", None)
    if isinstance(children, dict):
        return list(children.values())
    return list(children) if children else []


def expand_all_nodes(tree: Tree) -> None:
    """Recursively expand every node in the tree."""
    _traverse_and_apply(tree.root, expand=True)


def collapse_all_nodes(tree: Tree) -> None:
    """Recursively collapse every node in the tree."""
    _traverse_and_apply(tree.root, expand=False)


def _traverse_and_apply(node: TreeNode, *, expand: bool) -> None:
    try:
        if expand:
            node.expand()
        else:
            node.collapse()
    except Exception:
        pass
    for child in get_node_children(node):
        _traverse_and_apply(child, expand=expand)


def save_user_expansion_state(tree: Tree, user_expanded: Set[str], user_collapsed: Set[str]) -> None:
    """Snapshot current expansion state into the tracking sets."""
    root = tree.root

    def collect(node: TreeNode) -> None:
        if node is root:
            for child in get_node_children(node):
                collect(child)
            return
        label = node_label_text(node)
        if not label:
            for child in get_node_children(node):
                collect(child)
            return
        if is_node_expanded(node):
            user_collapsed.discard(label)
            user_expanded.add(label)
        else:
            user_expanded.discard(label)
            user_collapsed.add(label)
        for child in get_node_children(node):
            collect(child)

    collect(root)


def restore_user_expansion_state(
    tree: Tree,
    user_expanded: Set[str],
    user_collapsed: Set[str],
    filter_active: bool,
) -> None:
    """Restore expansion state from tracking sets; auto-expand all if filter is active."""
    root = tree.root

    def restore(node: TreeNode, ancestors_match_filter: bool = False) -> None:
        label            = node_label_text(node)
        node_has_children = bool(get_node_children(node))
        if label in user_expanded:
            try:
                node.expand()
            except Exception:
                pass
        elif label in user_collapsed:
            try:
                node.collapse()
            except Exception:
                pass
        elif filter_active and node_has_children:
            try:
                node.expand()
            except Exception:
                pass
        for child in get_node_children(node):
            restore(child, ancestors_match_filter=ancestors_match_filter or filter_active)

    restore(root)


def serialize_filtered_tree(filtered) -> str:
    """Serialize act/chapter/task/stage/lines into plain text."""
    out: List[str] = []
    for act in filtered:
        out.append(f"{act.label}")
        for chapter in act.chapters:
            out.append(f"  {chapter.label}")
            for task in chapter.tasks:
                out.append(f"    {task.label}")
                for stage in task.stages:
                    out.append(f"      {stage.label}")
                    for ln in stage.lines:
                        out.append(f"        {ln.speaker}: {ln.text}")
    return "\n".join(out)


def serialize_timeline_tree(filtered) -> str:
    """Serialize timeline group/bucket/task into plain text."""
    out: List[str] = []
    for group in filtered:
        out.append(group.label)
        for bucket in group.buckets:
            out.append(f"  {bucket.label}")
            for task in bucket.tasks:
                out.append(f"    {task.label}  [{task.task_id}]")
    return "\n".join(out)


def serialize_npc_tree(filtered) -> str:
    """Serialize NPC group/npc into plain text."""
    out: List[str] = []
    for group in filtered:
        out.append(group.label)
        for npc in group.npcs:
            out.append(f"  {npc.label}  [{npc.npc_id}]")
    return "\n".join(out)


def copy_to_clipboard(text: str) -> tuple[bool, str]:
    """Try pyperclip → tkinter → temp file. Returns (success, status_message)."""
    if not text:
        return False, "Nothing to copy"
    try:
        import pyperclip
        pyperclip.copy(text)
        return True, "Copied to clipboard"
    except Exception:
        pass
    try:
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        root.destroy()
        return True, "Copied to clipboard"
    except Exception:
        pass
    try:
        import os
        import tempfile
        fd, path = tempfile.mkstemp(prefix="dialogue_copy_", suffix=".txt")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        return False, f"Saved to {path}"
    except Exception as exc:
        return False, f"Failed: {exc}"