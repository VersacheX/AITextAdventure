"""
MessageDialog: centered popup for story messages, encounters, and notifications.

Mirrors the console game's dialog flow where `pg.info_dialogs` is populated
by task completion events, NPC interactions, and random encounters, then
displayed one at a time in the center of the viewport. The player presses
any key to advance to the next message.

This is a Widget (not a Screen) mounted on the "overlay" layer inside the
map panel so it floats centered over the map without covering the legend/stats.
Unlike LocationOverlay, this widget steals focus and blocks input until 
dismissed, matching the console behavior where the player must acknowledge 
each message before continuing.

Usage from OverworldScreen:
    messages = ["Line 1", "Line 2: Speaker Name", "..."]
    dialog = MessageDialog(messages)
    map_panel = self.query_one("#map-panel")
    map_panel.mount(dialog)
    # Dialog will remove itself when complete

The parent screen can watch for removal by checking `_dialog_visible()`.
"""
from __future__ import annotations

from typing import List, Optional

from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Static


class MessageDialog(Widget):
    """Centered message popup that blocks input and cycles through messages."""

    # Steal focus so WASD doesn't fire on the underlying screen
    can_focus = True
    can_focus_children = False

    BINDINGS = [
        # Any key advances to the next message
        Binding("space", "advance", "Continue", show=False),
        Binding("enter", "advance", "Continue", show=False),
        Binding("escape", "advance", "Continue", show=False),
    ]

    DEFAULT_CSS = """
    MessageDialog {
        layer: overlay;
        width: 80;
        height: auto;
        max-height: 24;
        background: $surface;
        border: thick $accent;
        offset: 50% 50%;
    }

    MessageDialog > Vertical {
        width: 100%;
        height: auto;
    }

    #msg-title {
        width: 100%;
        text-align: center;
        text-style: bold;
        background: $boost;
        color: $text;
        padding: 0 1;
        height: 1;
    }

    #msg-content {
        width: 100%;
        height: auto;
        min-height: 3;
        max-height: 18;
        padding: 1 2;
        color: $text;
        text-align: left;
        overflow-y: auto;
    }

    #msg-footer {
        width: 100%;
        height: 2;
        text-align: center;
        color: $text 50%;
        padding: 0 1;
        border-top: solid $accent 50%;
    }
    """

    current_index: reactive[int] = reactive(0)

    def __init__(self, messages: List[str], title: str = "Message") -> None:
        """Create a message dialog with a queue of messages.
        
        Args:
            messages: List of message strings to display sequentially.
            title: Dialog title (default: "Message").
        """
        super().__init__()
        self._messages = list(messages)  # defensive copy
        self._title = title

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Static(self._title, id="msg-title")
            yield Static("", id="msg-content")
            yield Static("Press any key to continue...", id="msg-footer")

    def on_mount(self) -> None:
        """Display the first message on mount, center it, and steal focus."""
        self._center_in_parent()
        self._update_display()
        self.focus()

    def _center_in_parent(self) -> None:
        """Calculate and apply styles to center the dialog in its parent container."""
        try:
            parent = self.parent
            if parent is None:
                return
            
            # Get parent size
            parent_width = parent.size.width
            parent_height = parent.size.height
            
            # Get our size (use a reasonable estimate for initial positioning)
            our_width = self.styles.width.value if hasattr(self.styles.width, 'value') else 80
            our_height = 10  # reasonable estimate for height
            
            # Calculate center position
            left = (parent_width - our_width) // 2
            top = (parent_height - our_height) // 2
            
            # Apply positioning
            self.styles.offset = (left, top)
        except Exception:
            # Fallback to default offset if calculation fails
            pass

    def action_advance(self) -> None:
        """Advance to the next message or dismiss if queue is exhausted."""
        self.current_index += 1
        if self.current_index >= len(self._messages):
            self.remove()  # auto-remove when done
        else:
            self._update_display()

    def watch_current_index(self, old_index: int, new_index: int) -> None:
        """Called when current_index changes."""
        if new_index < len(self._messages):
            self._update_display()

    def _update_display(self) -> None:
        """Render the current message in the content area."""
        if 0 <= self.current_index < len(self._messages):
            content = self._messages[self.current_index]
            self.query_one("#msg-content", Static).update(content)

    def on_key(self, event) -> None:
        """Catch any key press and advance."""
        self.action_advance()
        event.prevent_default()
        event.stop()