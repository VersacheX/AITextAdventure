"""
Utility functions for serialization, clipboard operations, and node inspection.
"""
from __future__ import annotations

from typing import List, Set

from textual.widgets.tree import TreeNode

from tui.services.dev.dev_data_service import DialogueLine


def serialize_node_visible(node: TreeNode, depth: int) -> List[str]:
    """
    Return list of text lines for `node` and its visible children.
    Only descend into children when the UI node is expanded.
    """
    out: List[str] = []
    # If node carries a DialogueLine (leaf), include full speaker:text
    if isinstance(getattr(node, "data", None), DialogueLine):
        ln: DialogueLine = node.data
        out.append("  " * depth + f"{ln.speaker}: {ln.text}")
        return out

    # Non-leaf node: append its label
    label = node_label_text(node)
    out.append("  " * depth + label)

    # Descend only if node is expanded
    if not is_node_expanded(node):
        return out

    children = getattr(node, "children", None)
    iterable = children.values() if isinstance(children, dict) else list(children or [])
    for child in iterable:
        out.extend(serialize_node_visible(child, depth + 1))
    return out


def is_node_expanded(node: TreeNode) -> bool:
    """Robustly check whether a TreeNode is expanded/open across Textual versions."""
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
    """Get a string label for a UI tree node in a best-effort way."""
    for attr in ("label", "_label", "renderable", "text"):
        val = getattr(node, attr, None)
        if val is None:
            continue
        try:
            return str(val)
        except Exception:
            continue
    try:
        return str(node)
    except Exception:
        return "<node>"


def collect_expanded_paths(node: TreeNode, current_path: str = "") -> Set[str]:
    """
    Recursively collect paths (label chains) of all expanded nodes.

    Returns a set of path strings like "Act I/Chapter 2/Task Name/Stage".
    """
    expanded_paths: Set[str] = set()

    # Get label for current node
    label = node_label_text(node)
    path = f"{current_path}/{label}" if current_path else label

    # If this node is expanded, record its path
    if is_node_expanded(node):
        expanded_paths.add(path)

    # Recurse into children
    children = getattr(node, "children", None)
    if children:
        iterable = children.values() if isinstance(children, dict) else list(children)
        for child in iterable:
            expanded_paths.update(collect_expanded_paths(child, path))

    return expanded_paths


def serialize_filtered_tree(filtered) -> str:
    """Serialize the act/chapter/task/stage/lines structure into plain text (model-driven)."""
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


def copy_to_clipboard(text: str) -> tuple[bool, str]:
    """
    Try to copy text to clipboard using pyperclip, then tkinter, then fallback to temp file.

    Returns:
        (success, status_message) where success is True if copied to clipboard.
    """
    if not text:
        return False, "Nothing to copy"

    # Try pyperclip
    try:
        import pyperclip

        pyperclip.copy(text)
        return True, "Copied to clipboard"
    except Exception:
        pass

    # Try tkinter
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

    # Fallback: write to temp file
    try:
        import os
        import tempfile

        fd, path = tempfile.mkstemp(prefix="dialogue_copy_", suffix=".txt")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        return False, f"Saved to {path}"
    except Exception:
        return False, "Copy failed"