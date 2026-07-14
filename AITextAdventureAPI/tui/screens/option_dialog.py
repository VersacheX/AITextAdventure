"""
OptionDialogWidget: centered choice-prompt popup.

Mirrors MessageDialog but instead of advancing through a queue of lines,
it presents a single prompt with a list of labelled options.  The player
selects one with arrow keys / mouse click and confirms with Enter or by
clicking the option button.  Escape is intentionally NOT bound — the player
must make a choice.

The widget is mounted inside the map panel (same layer strategy as
MessageDialog) and emits ``OptionChosen`` with the ``target_task_id`` of
the selected option so the parent screen can award the task and remove the
widget.

Usage from OverworldScreen / DungeonScreen:
    dialog = OptionDialogWidget(option_dialog)   # OptionDialog TypedDict
    map_panel.mount(dialog)
    # listen for OptionDialogWidget.OptionChosen
"""
from __future__ import annotations

from typing import List, Tuple

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.message import Message
from textual.widget import Widget
from textual.widgets import Button, Static


class OptionDialogWidget(Widget):
    """Centered choice-prompt popup that blocks input until a selection is made."""

    can_focus = True
    can_focus_children = True

    # No escape binding — player must choose
    BINDINGS = [
        Binding("up",   "focus_previous", "Up",   show=False),
        Binding("down", "focus_next",     "Down", show=False),
    ]

    DEFAULT_CSS = """
    OptionDialogWidget {
        layer: overlay;
        width: 80;
        height: auto;
        max-height: 30;
        background: $surface;
        border: thick $accent;
        offset: 50% 50%;
    }

    OptionDialogWidget > Vertical {
        width: 100%;
        height: auto;
    }

    #opt-title {
        width: 100%;
        text-align: center;
        text-style: bold;
        background: $boost;
        color: $text;
        padding: 0 1;
        height: 1;
    }

    #opt-message {
        width: 100%;
        height: auto;
        min-height: 2;
        padding: 1 2;
        color: $text;
        text-align: left;
    }

    #opt-buttons {
        width: 100%;
        height: auto;
        padding: 0 2 1 2;
        layout: vertical;
    }

    #opt-buttons Button {
        width: 100%;
        margin-bottom: 1;
    }
    """

    class OptionChosen(Message):
        """Emitted when the player selects an option."""

        def __init__(self, target_task_id: str) -> None:
            super().__init__()
            self.target_task_id = target_task_id

    def __init__(self, option_dialog: dict) -> None:
        """Create the widget from an ``OptionDialog`` TypedDict.

        Args:
            option_dialog: Dict with ``message`` (str) and
                ``options`` (list of (display_text, target_task_id) tuples).
        """
        super().__init__()
        self._message: str = option_dialog.get("message", "")
        self._options: List[Tuple[str, str]] = list(option_dialog.get("options") or [])

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Static("Choose", id="opt-title")
            yield Static(self._message, id="opt-message")
            with Vertical(id="opt-buttons"):
                for i, (label, task_id) in enumerate(self._options):
                    yield Button(label, id=f"opt-btn-{i}", variant="default")

    def on_mount(self) -> None:
        self._center_in_parent()
        # Focus the first button
        try:
            self.query_one("#opt-btn-0", Button).focus()
        except Exception:
            self.focus()

    def _center_in_parent(self) -> None:
        try:
            parent = self.parent
            if parent is None:
                return
            parent_width = parent.size.width
            parent_height = parent.size.height
            our_width = 80
            our_height = 4 + len(self._options) * 2
            left = (parent_width - our_width) // 2
            top = (parent_height - our_height) // 2
            self.styles.offset = (left, top)
        except Exception:
            pass

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Map button id back to the option index and emit OptionChosen."""
        btn_id: str = event.button.id or ""
        if btn_id.startswith("opt-btn-"):
            try:
                idx = int(btn_id.removeprefix("opt-btn-"))
                _, task_id = self._options[idx]
                self.post_message(self.OptionChosen(task_id))
            except (ValueError, IndexError):
                pass
        event.stop()