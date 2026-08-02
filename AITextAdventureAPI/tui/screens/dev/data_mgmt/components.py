"""
Custom widgets and components for the data management screen.
"""
from __future__ import annotations

from rich.markup import escape as rich_escape
from textual.widgets import Label, ListItem

from tui.services.dev.dataservices import DevRecord


class _RecordRow(ListItem):
    """ListView item that displays a DevRecord with name and subtitle.

    When the record's extras contain ``_errors`` (a list of validation error
    objects with a ``severity`` attribute), the row name is coloured:
      error   ? red
      warning ? yellow
      notice  ? #e040fb (magenta)
      info    ? cyan
    """

    def __init__(self, record: DevRecord) -> None:
        errors   = (record.extras or {}).get("_errors") or []
        name_raw = rich_escape(record.name)
        sub      = rich_escape(record.subtitle)

        if errors:
            has_error   = any(getattr(e, "severity", "") == "error"   for e in errors)
            has_warning = any(getattr(e, "severity", "") == "warning" for e in errors)
            has_notice  = any(getattr(e, "severity", "") == "notice"  for e in errors)
            if has_error:
                colour = "red"
            elif has_warning:
                colour = "yellow"
            elif has_notice:
                colour = "#e040fb"
            else:
                colour = "cyan"
            name_markup = f"[{colour}]{name_raw}[/{colour}]"
        else:
            name_markup = name_raw

        label = f"{name_markup}  [dim]{sub}[/dim]" if sub else name_markup
        super().__init__(Label(label, markup=True))
        self.record = record