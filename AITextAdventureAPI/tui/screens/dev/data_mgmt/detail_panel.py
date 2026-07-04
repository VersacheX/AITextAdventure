"""
Detail panel rendering logic for displaying DevRecord and DialogueLine data.
"""
from __future__ import annotations

from typing import List

from rich.markup import escape as rich_escape
from textual.widgets import Static

from tui.services.dev.dev_data_service import DevRecord, DialogueLine


def update_detail_for_record(panel: Static, record: DevRecord | None) -> None:
    """Update detail panel with a DevRecord."""
    if record is None:
        panel.update("[dim]No matching records.[/dim]")
        return
    name = rich_escape(record.name)
    sub = rich_escape(record.subtitle)
    detail = rich_escape(record.detail)
    header = f"[bold]{name}[/bold]"
    if sub:
        header += f"\n[dim]{sub}[/dim]"
    panel.update(f"{header}\n\n{detail}")


def update_detail_for_single_dialogue(panel: Static, line: DialogueLine | None) -> None:
    """Update detail panel with a single DialogueLine."""
    if line is None:
        panel.update("[dim]← select a dialogue line from the tree[/dim]")
        return
    speaker = rich_escape(line.speaker)
    text = rich_escape(line.text)
    panel.update(f"[bold]{speaker}[/bold]\n\n{text}")


def update_detail_for_multiple_dialogue(panel: Static, lines: List[DialogueLine]) -> None:
    """Update detail panel with multiple DialogueLines (subtree selection)."""
    if not lines:
        panel.update("[dim]No dialogue lines under this node.[/dim]")
        return
    parts: List[str] = []
    for ln in lines:
        parts.append(f"[bold]{rich_escape(ln.speaker)}[/bold]\n\n{rich_escape(ln.text)}")
        parts.append("\n[dim]──[/dim]\n")
    # remove trailing separator
    if parts:
        parts = parts[:-1]
    panel.update("\n".join(parts))