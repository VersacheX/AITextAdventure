"""
NpcMusicPlayerWidget — compact player bar for the NPC tab.

Layout (left to right):
  [⏮] [⏯] [⏭]  ♪ NPC Name — song_name  [✓ Autoplay]  (● Random ○ Sequential)

Messages bubbled to DataMgmtScreen:
  - NpcMusicPlayerWidget.RequestPrev    — always sequential step back
  - NpcMusicPlayerWidget.RequestNext   — always sequential step forward
  - NpcMusicPlayerWidget.RequestTogglePause
"""
from __future__ import annotations

from textual.app import ComposeResult
from textual.message import Message
from textual.widget import Widget
from textual.widgets import Button, Checkbox, RadioButton, RadioSet, Static


class NpcMusicPlayerWidget(Widget):
    """Compact player bar displayed above the NPC tree."""

    # ── Messages ──────────────────────────────────────────────────────────
    class RequestPrev(Message):
        """User pressed the previous track button (always sequential)."""

    class RequestNext(Message):
        """User pressed the next track button (always sequential)."""

    class RequestTogglePause(Message):
        """User pressed the play/pause button."""

    # ── CSS ───────────────────────────────────────────────────────────────
    DEFAULT_CSS = """
    NpcMusicPlayerWidget {
        width: 100%;
        height: auto;
        layout: horizontal;
        background: $panel;
        border-bottom: solid $accent 30%;
        align: left middle;
        padding: 0 1;
    }
    NpcMusicPlayerWidget Button {
        height: auto;
        min-width: 4;
        padding: 0 0;
        margin-right: 1;
        background: $surface;
        border: none;
        color: $text;
    }
    NpcMusicPlayerWidget Button:hover {
        background: $surface-lighten-1;
    }
    #npc-player-label {
        width: 1fr;
        height: auto;
        content-align: left middle;
        color: $text 55%;
        padding: 0 1;
    }
    #npc-player-autoplay {
        height: auto;
        margin-right: 1;
        border: none;
        background: transparent;
        padding: 0 0;
    }
    #npc-player-mode-set {
        height: auto;
        border: none;
        background: transparent;
        layout: horizontal;
        padding: 0 0;
        margin: 0;
    }
    #npc-player-mode-set RadioButton {
        height: auto;
        border: none;
        background: transparent;
        padding: 0 1;
        margin: 0;
        min-width: 0;
    }
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        # _autoplay and _random are the canonical state; widgets are kept in sync.
        self._autoplay: bool = False
        self._random:   bool = True

    # ── Compose ───────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        yield Button("⏮", id="npc-player-prev")
        yield Button("⏯", id="npc-player-play")
        yield Button("⏭", id="npc-player-next")
        yield Static("[dim]♪  —[/dim]", id="npc-player-label")
        yield Checkbox("Autoplay", value=False, id="npc-player-autoplay")
        with RadioSet(id="npc-player-mode-set"):
            yield RadioButton("Random",     value=True,  id="npc-player-random")
            yield RadioButton("Sequential", value=False, id="npc-player-sequential")

    # ── Public API ────────────────────────────────────────────────────────

    @property
    def is_autoplay(self) -> bool:
        """True when autoplay is enabled."""
        return self._autoplay

    @property
    def is_random(self) -> bool:
        """True when mode is Random; False means Sequential."""
        return self._random

    def update_now_playing(self, npc_name: str, song_name: str) -> None:
        """Update the now-playing label."""
        try:
            label = self.query_one("#npc-player-label", Static)
            if npc_name or song_name:
                label.update(f"[dim]♪  {npc_name}  —  {song_name}[/dim]")
            else:
                label.update("[dim]♪  —[/dim]")
        except Exception:
            pass

    def set_paused(self, paused: bool) -> None:
        """Update the play/pause button icon."""
        try:
            btn = self.query_one("#npc-player-play", Button)
            btn.label = "⏸" if not paused else "▶"
        except Exception:
            pass

    # ── Widget event handling ─────────────────────────────────────────────

    def on_button_pressed(self, event: Button.Pressed) -> None:
        bid = event.button.id or ""
        event.stop()

        if bid == "npc-player-prev":
            self.post_message(self.RequestPrev())
        elif bid == "npc-player-play":
            self.post_message(self.RequestTogglePause())
        elif bid == "npc-player-next":
            self.post_message(self.RequestNext())

    def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
        if event.checkbox.id == "npc-player-autoplay":
            self._autoplay = bool(event.value)
            event.stop()

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        if event.radio_set.id == "npc-player-mode-set":
            pressed_id = event.pressed.id if event.pressed else ""
            self._random = (pressed_id == "npc-player-random")
            event.stop()