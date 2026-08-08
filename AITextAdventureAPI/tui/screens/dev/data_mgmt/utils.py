"""
Utility functions for serialization, clipboard operations, and node inspection.
Shared by all tree handlers.
"""
from __future__ import annotations

from typing import Any, List, Set
import re as _re

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


def serialize_hostile_tree(filtered) -> str:
    """Serialize rarity/bucket/hostile into plain text with key stats per line."""
    out: List[str] = []
    for rarity_node in filtered:
        out.append(rarity_node.label)
        for bucket in rarity_node.level_buckets:
            out.append(f"  {bucket.label}")
            for h in bucket.hostiles:
                seed    = h.seed or {}
                htype   = seed.get("hostile_type", "?")
                role    = seed.get("role", "?")
                res     = ", ".join(seed.get("resistances") or []) or "—"
                weak    = ", ".join(seed.get("weaknesses") or []) or "—"
                imm     = ", ".join(seed.get("immunities") or []) or "—"
                hp      = seed.get("base_hp", "?")
                src     = h.source_list
                err_tag = f"  [!{len(h.errors)}]" if h.errors else ""
                out.append(
                    f"    {h.label}  [{h.hostile_id}]  "
                    f"type={htype}  role={role}  "
                    f"hp={hp}  "
                    f"res={res}  weak={weak}  imm={imm}  "
                    f"src={src}{err_tag}"
                )
    return "\n".join(out)


def serialize_timeline_tree(filtered) -> str:
    """Serialize timeline group/bucket/task into plain text (non-widget fallback)."""
    out: List[str] = []
    for group in filtered:
        out.append(group.label)
        for bucket in group.buckets:
            out.append(f"  {bucket.label}")
            for task in bucket.tasks:
                out.append(f"    {task.label}  [{task.task_id}]")
    return "\n".join(out)


def serialize_timeline_tree_visible(tree_widget: "Any", groups: "Any", screen: "Any" = None) -> str:
    """Serialize only the visible (user-expanded) buckets of the timeline tree.

    Uses the screen's _timeline_user_expanded / _timeline_user_collapsed sets
    as the authoritative expansion state — the same sets that drive the widget.

    Bucket default: collapsed.  Group default: expanded.
    Full task detail is written for every task inside an expanded bucket.
    """
    from tui.services.dev.dataservices import get_dialog_index, get_npc_names  # noqa: PLC0415
    from tui.screens.dev.data_mgmt.detail_panel import _format_event_lines     # noqa: PLC0415

    dialog_index = get_dialog_index()
    name_map     = get_npc_names()

    # Expansion sets from the screen — fall back to empty if not provided
    user_expanded  = getattr(screen, "_timeline_user_expanded",  set()) if screen else set()
    user_collapsed = getattr(screen, "_timeline_user_collapsed", set()) if screen else set()

    def _group_expanded(label: str) -> bool:
        if label in user_collapsed:
            return False
        if label in user_expanded:
            return True
        return True  # groups default open on first load

    def _bucket_expanded(label: str) -> bool:
        # Buckets only appear if the user explicitly expanded them
        return label in user_expanded and label not in user_collapsed

    def _task_detail_lines(node: "TimelineTaskNode", indent: str) -> List[str]:
        task     = node.task
        task_id  = node.task_id
        ttype    = str(task.get("type", "?"))
        to_type  = task.get("to_type")
        to_id    = task.get("to_id")
        acquire  = [e for e in (task.get("task_acquire_events") or []) if isinstance(e, dict)]
        complete = [e for e in (task.get("task_complete_events") or []) if isinstance(e, dict)]

        lines: List[str] = []
        lines.append(f"{indent}{node.label}")
        lines.append(f"{indent}{task_id}")
        lines.append(f"{indent}")
        lines.append(f"{indent}Source:  {node.source_path}")
        lines.append(f"{indent}Type:    {ttype}")
        if to_type or to_id:
            lines.append(f"{indent}Target:  {to_type or '?'} → {to_id or '?'}")
        if task.get("item_id"):
            lines.append(f"{indent}Item:    {task['item_id']}")
        if task.get("coordinates"):
            lines.append(f"{indent}Coords:  {task['coordinates']}")
        lines.append(f"{indent}")

        errors = node.errors or []
        if not errors:
            lines.append(f"{indent}Integrity: OK")
        else:
            ec = sum(1 for e in errors if e.severity == "error")
            wc = sum(1 for e in errors if e.severity == "warning")
            ic = sum(1 for e in errors if e.severity == "info")
            nc = sum(1 for e in errors if e.severity == "notice")
            dc = sum(1 for e in errors if e.severity == "duplicate")
            if ec or wc:
                parts = (
                    ([f"{ec} error(s)"]     if ec else []) +
                    ([f"{wc} warning(s)"]   if wc else []) +
                    ([f"{ic} info"]         if ic else []) +
                    ([f"{nc} notice(s)"]    if nc else []) +
                    ([f"{dc} duplicate(s)"] if dc else [])
                )
                lines.append(f"{indent}Integrity: FAIL  ({', '.join(parts)})")
            elif nc or dc:
                parts = (
                    ([f"{nc} notice(s)"]    if nc else []) +
                    ([f"{dc} duplicate(s)"] if dc else [])
                )
                lines.append(f"{indent}Integrity: NOTICE  ({', '.join(parts)})")
            else:
                lines.append(f"{indent}Integrity: INFO  ({ic} note(s))")
            for err in errors:
                extra = ""
                if err.event_type:        extra += f"  event={err.event_type}"
                if err.related_task_id:   extra += f"  task={err.related_task_id}"
                if err.related_entity_id: extra += f"  entity={err.related_entity_id}"
                lines.append(f"{indent}  {err.code}  {err.message}{extra}")

        lines.append(f"{indent}")
        lines.append(f"{indent}Acquired  ({len(acquire)})")
        if acquire:
            for ev in acquire:
                for raw in _format_event_lines(ev, dialog_index, name_map, set()):
                    lines.append(indent + _strip_markup(raw))
        else:
            lines.append(f"{indent}  (none)")
        lines.append(f"{indent}")
        lines.append(f"{indent}Completed  ({len(complete)})")
        if complete:
            for ev in complete:
                for raw in _format_event_lines(ev, dialog_index, name_map, set()):
                    lines.append(indent + _strip_markup(raw))
        else:
            lines.append(f"{indent}  (none)")
        return lines

    out: List[str] = []
    for group in (groups or []):
        if not _group_expanded(group.label):
            continue
        out.append(group.label)
        for bucket in group.buckets:
            if not _bucket_expanded(bucket.label):
                continue
            out.append(f"  {bucket.label}")
            for task_node in bucket.tasks:
                out.extend(_task_detail_lines(task_node, indent="    "))
                out.append("")
    return "\n".join(out)


def serialize_dialog_tree_visible(acts: "Any", screen: "Any" = None) -> str:
    """Serialize only the visible (user-expanded) chapters of the dialog tree.

    Uses the screen's _dialog_user_expanded / _dialog_user_collapsed sets
    as the authoritative expansion state — the same sets that drive the widget.

    Act default: expanded.  Chapter default: collapsed.
    Full stage/line content is written for every task inside an expanded chapter.
    """
    user_expanded  = getattr(screen, "_dialog_user_expanded",  set()) if screen else set()
    user_collapsed = getattr(screen, "_dialog_user_collapsed", set()) if screen else set()

    def _act_expanded(label: str) -> bool:
        if label in user_collapsed:
            return False
        return True  # acts default open

    def _chapter_expanded(label: str) -> bool:
        return label in user_expanded and label not in user_collapsed

    def _task_detail_lines(task_node: "Any", indent: str) -> List[str]:
        lines: List[str] = []
        lines.append(f"{indent}{task_node.label}")
        lines.append(f"{indent}{task_node.task_id}")
        for stage in task_node.stages:
            lines.append(f"{indent}")
            lines.append(f"{indent}{stage.label}  ({len(stage.lines)})")
            if stage.lines:
                for ln in stage.lines:
                    lines.append(f"{indent}  {ln.speaker}")
                    lines.append(f'{indent}    "{ln.text}"')
            else:
                lines.append(f"{indent}  (none)")
        return lines

    out: List[str] = []
    for act in (acts or []):
        if not _act_expanded(act.label):
            continue
        out.append(act.label)
        for chapter in act.chapters:
            if not _chapter_expanded(chapter.label):
                continue
            out.append(f"  {chapter.label}")
            for task_node in chapter.tasks:
                out.extend(_task_detail_lines(task_node, indent="    "))
                out.append("")
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


def _strip_markup(s: str) -> str:
    """Remove Rich markup tags from a string for plain-text output."""
    return _re.sub(r'\[/?[^\]]*\]', '', s)


def serialize_timeline_task_detail(
    task_node: Any,
    groups: Any,
) -> str:
    """Serialize a single TimelineTaskNode to the same content shown in the detail panel.

    Output mirrors TimelineDetailPanel exactly:
      {group label} {bucket label} {task label}
      {task_id}

      Source:  …
      Type:    …
      Target:  … → …
      Integrity: FAIL / OK  (counts)
        CODE  message  event=…  entity=…
      Acquired  (N)
        Event lines…
      Completed  (N)
        Event lines…
    """
    from tui.services.dev.dataservices import get_dialog_index, get_npc_names  # noqa: PLC0415
    from tui.screens.dev.data_mgmt.detail_panel import _format_event_lines  # noqa: PLC0415

    task     = task_node.task
    task_id  = task_node.task_id
    ttype    = str(task.get("type", "?"))
    to_type  = task.get("to_type")
    to_id    = task.get("to_id")
    acquire  = [e for e in (task.get("task_acquire_events") or []) if isinstance(e, dict)]
    complete = [e for e in (task.get("task_complete_events") or []) if isinstance(e, dict)]

    dialog_index = get_dialog_index()
    name_map     = get_npc_names()

    # ── Resolve tree path (group label  bucket label) ─────────────────────
    group_label  = ""
    bucket_label = ""
    for g in (groups or []):
        for b in g.buckets:
            for t in b.tasks:
                if t.task_id == task_id:
                    group_label  = g.label
                    bucket_label = b.label
                    break
            if group_label:
                break
        if group_label:
            break

    out: List[str] = []

    # ── Tree-path header ───────────────────────────────────────────────────
    path_parts = [p for p in (group_label, bucket_label, task_node.label) if p]
    out.append(" ".join(path_parts))
    out.append(task_id)
    out.append("")

    # ── Source / Type / Target ─────────────────────────────────────────────
    out.append(f"Source:  {task_node.source_path}")
    out.append(f"Type:    {ttype}")
    if to_type or to_id:
        out.append(f"Target:  {to_type or '?'} → {to_id or '?'}")
    if task.get("item_id"):
        out.append(f"Item:    {task['item_id']}")
    if task.get("coordinates"):
        out.append(f"Coords:  {task['coordinates']}")
    out.append("")

    # ── Integrity ──────────────────────────────────────────────────────────
    errors = task_node.errors or []
    if not errors:
        out.append("Integrity: OK")
    else:
        error_count     = sum(1 for e in errors if e.severity == "error")
        warning_count   = sum(1 for e in errors if e.severity == "warning")
        info_count      = sum(1 for e in errors if e.severity == "info")
        notice_count    = sum(1 for e in errors if e.severity == "notice")
        duplicate_count = sum(1 for e in errors if e.severity == "duplicate")

        has_error   = error_count > 0
        has_warning = warning_count > 0
        has_notice  = notice_count > 0 or duplicate_count > 0

        if has_error or has_warning:
            parts = []
            if error_count:
                parts.append(f"{error_count} error(s)")
            if warning_count:
                parts.append(f"{warning_count} warning(s)")
            if info_count:
                parts.append(f"{info_count} info")
            if notice_count:
                parts.append(f"{notice_count} notice(s)")
            if duplicate_count:
                parts.append(f"{duplicate_count} duplicate(s)")
            out.append(f"Integrity: FAIL  ({', '.join(parts)})")
        elif has_notice:
            parts = []
            if notice_count:
                parts.append(f"{notice_count} notice(s)")
            if duplicate_count:
                parts.append(f"{duplicate_count} duplicate(s)")
            out.append(f"Integrity: NOTICE  ({', '.join(parts)})")
        else:
            out.append(f"Integrity: INFO  ({info_count} note(s))")

        for err in errors:
            extra = ""
            if err.event_type:
                extra += f"  event={err.event_type}"
            if err.related_task_id:
                extra += f"  task={err.related_task_id}"
            if err.related_entity_id:
                extra += f"  entity={err.related_entity_id}"
            out.append(f"  {err.code}  {err.message}{extra}")

    out.append("")

    # ── Acquired events ────────────────────────────────────────────────────
    out.append(f"Acquired  ({len(acquire)})")
    if acquire:
        for ev in acquire:
            for line in _format_event_lines(ev, dialog_index, name_map, set()):
                out.append(_strip_markup(line))
    else:
        out.append("  (none)")

    out.append("")

    # ── Completed events ───────────────────────────────────────────────────
    out.append(f"Completed  ({len(complete)})")
    if complete:
        for ev in complete:
            for line in _format_event_lines(ev, dialog_index, name_map, set()):
                out.append(_strip_markup(line))
    else:
        out.append("  (none)")

    return "\n".join(out)

def serialize_npc_tree(filtered) -> str:
    """Serialize NPC group/npc into plain text.

    When the NPC validator has run (records carry ``extras["_errors"]``), each
    NPC's integrity status and every error/info code+message is included so the
    copied text is directly actionable.
    """
    out: List[str] = []
    for group in filtered:
        out.append(group.label)
        for npc in group.npcs:
            out.append(f"  {npc.label}  [{npc.npc_id}]")

            record = getattr(npc, "record", None)
            extras = getattr(record, "extras", None) or {}
            errors = extras.get("_errors")
            if errors is None:
                continue  # validator hasn't run — keep bare listing

            hard_errors = [e for e in errors if getattr(e, "severity", "error") == "error"]
            info_items  = [e for e in errors if getattr(e, "severity", "") == "info"]

            if not hard_errors and not info_items:
                out.append("    Integrity: OK")
                continue

            if hard_errors:
                summary = f"{len(hard_errors)} error(s)"
                if info_items:
                    summary += f", {len(info_items)} info"
                out.append(f"    Integrity: FAIL  ({summary})")
            else:
                out.append(f"    Integrity: INFO  ({len(info_items)} note(s))")

            for e in errors:
                sev = getattr(e, "severity", "error").upper()
                out.append(f"      [{sev}] {e.code}: {e.message}")
    return "\n".join(out)

def serialize_dialog_tree_from_widget(tree_widget: "Tree") -> str:
    """Serialize visible dialog branches by reading live widget expansion state.

    Walks the actual widget hierarchy:
      root → act → chapter → task → stage → leaf(DialogueLine)

    Acts output if expanded. Chapters output if expanded. Tasks, stages, and
    lines are always fully rendered once their chapter is visible — matching the
    timeline bucket→task pattern. Full line text is read from node.data, not
    the truncated preview label.
    """
    root = tree_widget.root
    out: List[str] = []

    for act_node in get_node_children(root):
        if not is_node_expanded(act_node):
            continue
        out.append(_strip_markup(node_label_text(act_node)))

        for chapter_node in get_node_children(act_node):
            if not is_node_expanded(chapter_node):
                continue
            out.append(f"  {_strip_markup(node_label_text(chapter_node))}")

            for task_node in get_node_children(chapter_node):
                out.append(f"    {_strip_markup(node_label_text(task_node))}")

                for stage_node in get_node_children(task_node):
                    out.append(f"      {_strip_markup(node_label_text(stage_node))}")

                    for line_node in get_node_children(stage_node):
                        line_data = getattr(line_node, "data", None)
                        if isinstance(line_data, DialogueLine):
                            out.append(f"        {line_data.speaker}")
                            out.append(f'          "{line_data.text}"')
                        else:
                            out.append(f"        {_strip_markup(node_label_text(line_node))}")

                out.append("")

    return "\n".join(out)