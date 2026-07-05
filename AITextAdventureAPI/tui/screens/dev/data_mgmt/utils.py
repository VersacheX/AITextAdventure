"""
Utility functions for serialization, clipboard operations, and node inspection.
"""
from __future__ import annotations

from typing import List, Set

from textual.widgets import Tree
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

    children = get_node_children(node)
    for child in children:
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
            # Convert to string and strip any rich markup/ANSI codes for comparison
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


def save_user_expansion_state(tree: Tree, user_expanded: Set[str], user_collapsed: Set[str]) -> None:
    """
    Save the **current** expansion state by comparing it to known user actions.
    
    This updates user_expanded/user_collapsed to reflect any changes the user
    made during the current tree view (e.g., manually expanding or collapsing nodes).
    
    This is called before tree rebuild to preserve user intent across filter changes.
    
    Args:
        tree: The Tree widget to inspect.
        user_expanded: Set tracking nodes the user explicitly expanded (modified in-place).
        user_collapsed: Set tracking nodes the user explicitly collapsed (modified in-place).
    """
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
        
        expanded = is_node_expanded(node)
        
        # Update tracking based on current state
        if expanded:
            # Node is expanded: remove from collapsed set (if present), ensure in expanded set
            user_collapsed.discard(label)
            user_expanded.add(label)
        else:
            # Node is collapsed: remove from expanded set (if present), ensure in collapsed set
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
    """
    Restore expansion state based on explicit user actions and active filters.
    
    **Option 3 behavior**: 
    - Nodes in `user_expanded` are always expanded (user explicitly opened them).
    - Nodes in `user_collapsed` are always collapsed (user explicitly closed them).
    - If a filter is active, matching nodes and their ancestors auto-expand **temporarily**
      (this expansion does NOT add them to user_expanded).
    - When the filter is cleared, only user_expanded nodes remain open.
    
    Args:
        tree: The Tree widget to restore expansion state to.
        user_expanded: Set of labels the user explicitly expanded.
        user_collapsed: Set of labels the user explicitly collapsed.
        filter_active: True if any filter query is active.
    """
    root = tree.root
    
    def restore(node: TreeNode, ancestors_match_filter: bool = False) -> None:
        label = node_label_text(node)
        
        # Determine if this node or its children match the filter
        node_has_children = bool(get_node_children(node))
        
        # User intent takes precedence
        if label in user_expanded:
            # User explicitly expanded this node
            try:
                node.expand()
            except Exception:
                pass
        elif label in user_collapsed:
            # User explicitly collapsed this node
            try:
                node.collapse()
            except Exception:
                pass
        elif filter_active and node_has_children:
            # No explicit user action: if filter is active and this node has children,
            # we expand it temporarily to reveal matches (but don't track it as user action)
            try:
                node.expand()
            except Exception:
                pass
        # else: leave at default state (collapsed for non-acts)
        
        # Recurse into children
        for child in get_node_children(node):
            restore(child, ancestors_match_filter=ancestors_match_filter or filter_active)
    
    restore(root)


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
    except Exception as exc:
        return False, f"Failed: {exc}"