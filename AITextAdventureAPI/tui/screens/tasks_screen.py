"""
TasksScreen: overlay displaying the player's active and completed tasks.

Layout:
  ┌─────────────────────────────────────────────────────────────────┐
  │                        Tasks                                     │
  ├─────────────────────────────────────────────────────────────────┤
  │  ▼ Active (3)            │  Task Details                         │
  │    Meet Seth             │                                       │
  │    Defeat Sand Guardian  │  Meet Seth                            │
  │    Fetch Ancient Relic   │                                       │
  │  ▶ Completed (12)        │  Type: Meet                           │
  │    Awakening             │  Target: NPC (seth)                   │
  │    First Steps           │                                       │
  │    ...                   │  Description:                         │
  │                          │  Travel to Bleakwatch Outpost and    │
  │                          │  speak with Seth, a resistance       │
  │                          │  contact who can help you navigate   │
  │                          │  the dangers of the Riftlands.       │
  │                          │                                       │
  │                          │  Region: riftlands                    │
  │                          │                                       │
  └─────────────────────────────────────────────────────────────────┘
  [Esc] Close
"""
from __future__ import annotations

from typing import Any

from rich.markup import escape as rich_escape
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, ScrollableContainer, Vertical, VerticalScroll
from textual.widgets import Collapsible, Label, ListItem, ListView, Static

from tui.screens.base_screen import BaseScreen


class _TaskRow(ListItem):
    """One task in the list."""

    def __init__(self, task: Any, label_text: str) -> None:
        super().__init__(Label(label_text))
        self.task_obj = task  # Renamed from 'task' to avoid conflict with ListItem


class TasksScreen(BaseScreen):
    """Overlay screen showing active and completed tasks."""

    show_header = True
    show_footer = True

    BINDINGS = [
        Binding("escape", "go_back", "Close", show=True),
        Binding("up", "cursor_up", "Up", show=False),
        Binding("down", "cursor_down", "Down", show=False),
        Binding("k", "cursor_up", "Up", show=False),
        Binding("j", "cursor_down", "Down", show=False),
    ]

    DEFAULT_CSS = """
    TasksScreen {
        align: center middle;
    }

    #tasks-container {
        width: 90;
        height: 35;
        background: $panel;
        border: thick $accent;
    }

    #tasks-header {
        height: 3;
        content-align: center middle;
        text-style: bold;
        background: $boost;
        border-bottom: solid $accent;
    }

    #tasks-main {
        height: 1fr;
        layout: horizontal;
    }

    #tasks-list-panel {
        width: 30;
        height: 100%;
        border-right: solid $accent 50%;
        overflow-y: auto;
    }

    #tasks-list-scroll {
        width: 100%;
        height: auto;
    }

    Collapsible {
        width: 100%;
        height: auto;
        border: none;
        background: $surface;
    }

    Collapsible > CollapsibleTitle {
        padding: 1 1;
        text-style: bold;
        color: $text 80%;
        background: $surface;
        border-bottom: solid $accent 30%;
    }

    Collapsible > CollapsibleTitle:hover {
        background: $accent 20%;
    }

    Collapsible > Contents {
        height: auto;
        padding: 0;
    }

    #tasks-active-list,
    #tasks-completed-list {
        height: auto;
        width: 100%;
    }

    #tasks-active-list ListItem,
    #tasks-completed-list ListItem {
        height: auto;
        padding: 0 1;
    }

    #tasks-active-list ListItem:hover,
    #tasks-completed-list ListItem:hover {
        background: $accent 20%;
    }

    #tasks-active-list > .--highlight,
    #tasks-completed-list > .--highlight {
        background: $accent 40%;
    }

    #tasks-detail-panel {
        width: 1fr;
        height: 100%;
        padding: 1 2;
        overflow-y: auto;
    }

    #tasks-detail-text {
        width: 100%;
        height: auto;
    }
    """

    def __init__(self) -> None:
        super().__init__()
        self._pg: Any = None

    def compose_content(self) -> ComposeResult:
        with Vertical(id="tasks-container"):
            yield Static("Tasks", id="tasks-header")
            with Horizontal(id="tasks-main"):
                with VerticalScroll(id="tasks-list-panel"):
                    with Vertical(id="tasks-list-scroll"):
                        with Collapsible(title="Active (0)", collapsed=False, id="tasks-active-collapsible"):
                            yield ListView(id="tasks-active-list")
                        with Collapsible(title="Completed (0)", collapsed=True, id="tasks-completed-collapsible"):
                            yield ListView(id="tasks-completed-list")
                with ScrollableContainer(id="tasks-detail-panel"):
                    yield Static("", id="tasks-detail-text")

    def on_mount(self) -> None:
        from tui.services.game_state import get_active_game
        self._pg = get_active_game()
        self._rebuild_lists()

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        """Update detail panel when a task is selected."""
        if isinstance(event.item, _TaskRow):
            self._update_detail(event.item.task_obj)

    def action_cursor_up(self) -> None:
        """Move selection up in the currently focused list."""
        try:
            active_list = self.query_one("#tasks-active-list", ListView)
            completed_list = self.query_one("#tasks-completed-list", ListView)
            if active_list.has_focus:
                active_list.action_cursor_up()
            elif completed_list.has_focus:
                completed_list.action_cursor_up()
            else:
                # Focus active list by default
                active_list.focus()
        except Exception:
            pass

    def action_cursor_down(self) -> None:
        """Move selection down in the currently focused list."""
        try:
            active_list = self.query_one("#tasks-active-list", ListView)
            completed_list = self.query_one("#tasks-completed-list", ListView)
            if active_list.has_focus:
                active_list.action_cursor_down()
            elif completed_list.has_focus:
                completed_list.action_cursor_down()
            else:
                # Focus active list by default
                active_list.focus()
        except Exception:
            pass

    def action_go_back(self) -> None:
        self.app.pop_screen()

    # ── internal helpers ──────────────────────────────────────────────────

    def _rebuild_lists(self) -> None:
        """Populate active and completed task lists."""
        if self._pg is None:
            return

        active_tasks = [t for t in self._pg.tasks if not t.completed]
        completed_tasks = [t for t in self._pg.tasks if t.completed]

        # Update active tasks
        active_list = self.query_one("#tasks-active-list", ListView)
        active_list.clear()
        for task in active_tasks:
            label = self._format_task_label(task)
            active_list.append(_TaskRow(task, label))

        # Update completed tasks
        completed_list = self.query_one("#tasks-completed-list", ListView)
        completed_list.clear()
        for task in completed_tasks:
            label = self._format_task_label(task)
            completed_list.append(_TaskRow(task, label))

        # Update collapsible titles with counts
        try:
            active_collapsible = self.query_one("#tasks-active-collapsible", Collapsible)
            active_collapsible.title = f"Active ({len(active_tasks)})"
            
            completed_collapsible = self.query_one("#tasks-completed-collapsible", Collapsible)
            completed_collapsible.title = f"Completed ({len(completed_tasks)})"
        except Exception:
            pass

        # Show first active task detail, or first completed if no active tasks
        if active_tasks:
            self._update_detail(active_tasks[0])
            active_list.focus()
        elif completed_tasks:
            self._update_detail(completed_tasks[0])
            completed_list.focus()
        else:
            self._update_detail(None)

    def _format_task_label(self, task: Any) -> str:
        """Format a task name for the list."""
        task_id = rich_escape(getattr(task, "task_id", "?"))
        # Humanize task_id: replace underscores with spaces, title case
        name = task_id.replace("_", " ").title()
        return name

    def _update_detail(self, task: Any | None) -> None:
        """Update the detail panel with task information."""
        panel = self.query_one("#tasks-detail-text", Static)
        
        if task is None:
            panel.update("[dim]No tasks to display.[/dim]")
            return

        # Build detail text
        task_id = rich_escape(getattr(task, "task_id", "?"))
        task_name = task_id.replace("_", " ").title()
        task_type = rich_escape(str(getattr(task, "type", "?")).replace("TaskType.", ""))
        completed = getattr(task, "completed", False)
        
        lines = [
            f"[bold]{task_name}[/bold]",
            "",
            f"Type: [cyan]{task_type}[/cyan]",
        ]

        # Add type-specific details
        if hasattr(task, "to_type"):
            to_type = rich_escape(str(task.to_type).replace("SpecialTaskToType.", ""))
            to_id = rich_escape(str(getattr(task, "to_id", "?")))
            lines.append(f"Target: {to_type} ({to_id})")

        if hasattr(task, "item_id"):
            item_id = rich_escape(str(task.item_id))
            lines.append(f"Item: {item_id}")

        if hasattr(task, "coordinates"):
            coords = task.coordinates
            lines.append(f"Location: ({coords[0]}, {coords[1]}, {coords[2]})")

        # Region where task was acquired - extract name from object
        if hasattr(task, "acquired_region") and task.acquired_region:
            region_obj = task.acquired_region
            # Try to get a readable name from the region object
            region_name = "Unknown"
            if hasattr(region_obj, "name"):
                region_name = str(region_obj.name)
            elif hasattr(region_obj, "id"):
                region_name = str(region_obj.id)
            elif hasattr(region_obj, "region_name"):
                region_name = str(region_obj.region_name)
            elif hasattr(region_obj, "__class__"):
                # Last resort: use class name
                region_name = region_obj.__class__.__name__
            
            lines.append(f"Region: {rich_escape(region_name)}")

        # Status
        status = "[green]✓ Completed[/green]" if completed else "[yellow]○ Active[/yellow]"
        lines.append("")
        lines.append(f"Status: {status}")

        # Check completion progress for active tasks
        if not completed:
            lines.append("")
            if self._pg and hasattr(task, "check_completion_terms"):
                try:
                    can_complete = task.check_completion_terms(self._pg)
                    if can_complete:
                        lines.append("[green]✓ Ready to complete![/green]")
                    else:
                        lines.append("[dim]○ In progress...[/dim]")
                except Exception:
                    lines.append("[dim]○ In progress...[/dim]")

        panel.update("\n".join(lines))