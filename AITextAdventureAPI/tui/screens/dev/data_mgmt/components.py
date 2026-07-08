"""
Custom widgets and components for the data management screen.
"""
from __future__ import annotations

from rich.markup import escape as rich_escape
from textual.widgets import Label, ListItem

from tui.services.dev.dataservices import DevRecord


class _RecordRow(ListItem):
    """ListView item that displays a DevRecord with name and subtitle."""

    def __init__(self, record: DevRecord) -> None:
        name = rich_escape(record.name)
        sub = rich_escape(record.subtitle)
        label = f"{name}  [dim]{sub}[/dim]" if sub else name
        super().__init__(Label(label))
        self.record = record