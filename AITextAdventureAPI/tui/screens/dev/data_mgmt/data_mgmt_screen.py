"""
DataMgmtScreen: developer data-management hub for browsing/searching every
seed-data catalog in the game.

Delegates all behavior to handlers, treehandlers, detail_panel, and utils.
"""
from __future__ import annotations

import random as _random
from pathlib import Path
from typing import Any, List, Optional, Set

from textual import work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, ScrollableContainer, Vertical
from textual.widgets import Button, Input, Label, ListView, RadioButton, RadioSet, Static, Tab, Tabs, Tree

from tui.audio import NPCMusicController
from tui.screens.base_screen import BaseScreen
from tui.screens.dev.data_mgmt.handlers import (
    handle_button_pressed,
    handle_input_changed,
    handle_list_view_highlighted,
    handle_radio_set_changed,
    handle_tab_activated,
    handle_tree_node_highlighted,
    rebuild_dialog_tree_for_screen,
    rebuild_list_for_screen,
    rebuild_npc_tree_for_screen,
    rebuild_timeline_tree_for_screen,
    set_filter_mode,
)
from tui.screens.dev.data_mgmt.npc_music_player import NpcMusicPlayerWidget
from tui.services.dev.dataservices import (
    CATEGORIES,
    CATEGORY_LABELS,
    DevRecord,
    DialogueLine,
    NpcRecordNode,
    get_npc_tree,
    preload,
)

_DIALOG_CATEGORY   = "character_dialog"
_TIMELINE_CATEGORY = "timeline"
_NPC_CATEGORY      = "npc"

_MUSIC_DIR          = Path(__file__).resolve().parents[3] / "assets" / "music"
_DETAIL_WIDTH_NORMAL = 80


class DataMgmtScreen(BaseScreen):
    """Dev-only browser for every seed-data catalog in the game."""

    BINDINGS = [
        Binding("escape", "go_back", "Back", show=True),
    ]

    DEFAULT_CSS = """
    DataMgmtScreen {
        layout: vertical;
    }

    #dm-tabs {
        height: 3;
        background: $panel;
        border-bottom: solid $accent;
    }

    #dm-filter-row {
        height: auto;
        min-height: 3;
        padding: 0 1;
        border-bottom: solid $accent 30%;
    }

    #dm-filter {
        width: 1fr;
    }

    #dm-dialog-filter-row {
        width: 1fr;
        height: 3;
        display: none;
    }

    #dm-dialog-filter-row Input {
        width: 1fr;
        margin-right: 1;
    }

    #dm-equipment-filter-row {
        width: 1fr;
        height: auto;
        display: none;
        padding: 1 0;
    }

    #dm-equipment-filter-row Label {
        width: auto;
        padding: 0 1;
        content-align: left middle;
    }

    #dm-equipment-filter-row Horizontal {
        height: auto;
        width: 1fr;
        align: left middle;
    }

    #dm-equipment-type-radio,
    #dm-equipment-slot-radio {
        width: 1fr;
        height: auto;
        layout: horizontal;
        border: none;
        background: transparent;
    }

    #dm-equipment-type-radio RadioButton,
    #dm-equipment-slot-radio RadioButton {
        width: auto;
        min-width: 8;
        margin-right: 1;
    }

    RadioButton {
        border: tall $accent 50%;
        background: $surface;
        color: $text;
        padding: 0 1;
    }

    RadioButton:hover {
        background: $surface-lighten-1;
    }

    RadioButton.-selected {
        background: $accent;
        color: $text;
    }

    #dm-expand, #dm-collapse, #dm-copy {
        display: none;
        margin-left: 1;
        padding: 0 1;
        min-width: 3;
        height: auto;
        color: $text;
        background: $surface;
        border: solid $accent 30%;
    }

    #dm-detail-expand {
        margin-left: 1;
        padding: 0 1;
        min-width: 3;
        height: auto;
        color: $text;
        background: $surface;
        border: solid $accent 30%;
    }

    #dm-status {
        width: auto;
        min-width: 14;
        content-align: right middle;
        color: $text 60%;
        padding: 0 1;
    }

    #dm-main-row {
        height: 1fr;
    }

    #dm-list-panel {
        width: 1fr;
        height: 100%;
    }

    #dm-list {
        height: 1fr;
    }

    #dm-dialog-tree {
        height: 1fr;
        display: none;
    }

    #dm-timeline-tree {
        height: 1fr;
        display: none;
    }

    #dm-npc-tree {
        height: 1fr;
        display: none;
    }

    #dm-detail-panel {
        width: 80;
        height: 100%;
        padding: 0;
        border-left: solid $accent 30%;
    }

    #dm-detail-text {
        height: 100%;
        padding: 0 1;
    }
    """

    def __init__(self) -> None:
        super().__init__()
        self._category: str = CATEGORIES[0]
        self._loaded: bool  = False
        self._detail_maximised: bool = False

        # Per-tree filtered model caches (for copy-to-clipboard fallback)
        self._last_filtered: Any           = None
        self._last_timeline_filtered: Any  = None
        self._last_npc_filtered: Any       = None

        # Independent expansion state per tree so switching tabs doesn't clobber state
        self._user_expanded: Set[str]          = set()
        self._user_collapsed: Set[str]         = set()
        self._timeline_user_expanded: Set[str] = set()
        self._timeline_user_collapsed: Set[str] = set()
        self._npc_user_expanded: Set[str]      = set()
        self._npc_user_collapsed: Set[str]     = set()

        # NPC selection and playlist state
        self._last_selected_npc_record: Optional[DevRecord] = None
        self._npc_playlist: List[DevRecord] = []
        self._npc_playlist_index: int = 0

        # NPC theme-music controller — active for the lifetime of this screen.
        self._npc_music = NPCMusicController(
            music_dir=_MUSIC_DIR,
            fadeout_ms=700,
            volume=0.7,
        )

    # ── Compose ───────────────────────────────────────────────────────────

    def compose_content(self) -> ComposeResult:
        yield Tabs(
            *[Tab(CATEGORY_LABELS[category], id=f"tab-{category}") for category in CATEGORIES],
            id="dm-tabs",
        )
        with Horizontal(id="dm-filter-row"):
            yield Input(placeholder="Filter by name, id, or description...", id="dm-filter")
            with Horizontal(id="dm-dialog-filter-row"):
                yield Input(placeholder="Act...", id="dm-filter-act")
                yield Input(placeholder="Chapter...", id="dm-filter-chapter")
                yield Input(placeholder="Task...", id="dm-filter-task")
                yield Input(placeholder="Character...", id="dm-filter-character")
            with Vertical(id="dm-equipment-filter-row"):
                with Horizontal():
                    yield Label("Type:")
                    with RadioSet(id="dm-equipment-type-radio"):
                        yield RadioButton("All", value=True, id="equip-type-all")
                        yield RadioButton("Weapon", id="equip-type-weapon")
                        yield RadioButton("Armor", id="equip-type-armor")
                with Horizontal():
                    yield Label("Slot:")
                    with RadioSet(id="dm-equipment-slot-radio"):
                        yield RadioButton("All", value=True, id="equip-slot-all")
                        yield RadioButton("Head", id="equip-slot-head")
                        yield RadioButton("Body", id="equip-slot-body")
                        yield RadioButton("Arms", id="equip-slot-arms")
                        yield RadioButton("Legs", id="equip-slot-legs")
            yield Button("++", id="dm-expand", variant="default")
            yield Button("--", id="dm-collapse", variant="default")
            yield Button("Copy", id="dm-copy", variant="default")
            yield Button("⤢", id="dm-detail-expand", variant="default")
            yield Static("Loading...", id="dm-status")
        with Horizontal(id="dm-main-row"):
            with Vertical(id="dm-list-panel"):
                # NPC player bar — hidden on non-NPC tabs via set_filter_mode
                yield NpcMusicPlayerWidget(id="npc-player")
                yield ListView(id="dm-list")
                dialog_tree: Tree[DialogueLine] = Tree("Dialogue", id="dm-dialog-tree")
                dialog_tree.show_root = False
                yield dialog_tree
                timeline_tree: Tree = Tree("Timeline", id="dm-timeline-tree")
                timeline_tree.show_root = False
                yield timeline_tree
                npc_tree: Tree = Tree("NPCs", id="dm-npc-tree")
                npc_tree.show_root = False
                yield npc_tree
            with ScrollableContainer(id="dm-detail-panel"):
                yield Static("", id="dm-detail-text")

    # ── Lifecycle ─────────────────────────────────────────────────────────

    def on_mount(self) -> None:
        # Hide player until NPC tab is active
        self.query_one(NpcMusicPlayerWidget).display = False
        self._load_catalog()
        # Poll for song-end every 500ms to drive autoplay/loop regardless of tab
        self.set_interval(0.5, self._on_music_poll)

    def on_unmount(self) -> None:
        self._npc_music.shutdown()

    def on_screen_resume(self) -> None:
        """Called when this screen returns to the top of the stack (e.g. after
        portrait fullscreen or any other pushed screen is dismissed).

        If a track was playing before the sub-screen appeared and has since
        ended naturally while suspended, restart it so music continues."""
        if self._last_selected_npc_record is None:
            return
        if self._npc_music.is_playing():
            return
        # Track ended or was never running — resume from where we left off
        record = self._last_selected_npc_record
        self._npc_music.play_record(record.id, record.song_id, force=True)
        self._update_player_label(record)

    # ── Data loading ──────────────────────────────────────────────────────

    @work(thread=True)
    def _load_catalog(self) -> None:
        """Runs off the UI thread — imports hundreds of seed modules."""
        try:
            preload()
        except Exception as exc:  # noqa: BLE001
            self.app.call_from_thread(self._on_load_error, str(exc))
            return
        self.app.call_from_thread(self._on_load_success)

    def _on_load_success(self) -> None:
        self._loaded = True
        tabs = self.query_one("#dm-tabs", Tabs)
        tabs.active = f"tab-{self._category}"
        set_filter_mode(self, self._category)
        if self._category == _DIALOG_CATEGORY:
            rebuild_dialog_tree_for_screen(self)
        elif self._category == _TIMELINE_CATEGORY:
            rebuild_timeline_tree_for_screen(self)
        elif self._category == _NPC_CATEGORY:
            rebuild_npc_tree_for_screen(self)
        else:
            rebuild_list_for_screen(self)
        self.query_one("#dm-filter", Input).focus()

    def _on_load_error(self, message: str) -> None:
        from rich.markup import escape as rich_escape  # noqa: PLC0415
        self.query_one("#dm-status", Static).update("Load failed")
        self.query_one("#dm-detail-text", Static).update(
            f"[red]Failed to load seed data:[/red]\n{rich_escape(message)}"
        )

    # ── NPC selection / playlist ──────────────────────────────────────────

    def rebuild_npc_playlist(self) -> None:
        """Collect every NPC with a resolvable audio file into the playlist."""
        playlist: List[DevRecord] = []
        for group in get_npc_tree():
            for npc_node in group.npcs:
                r = npc_node.record
                if r.song_id and self._npc_music.resolve_song(r.song_id) is not None:
                    playlist.append(r)
        self._npc_playlist = playlist
        # Keep index pointing at the currently playing NPC if possible
        if self._last_selected_npc_record and playlist:
            try:
                self._npc_playlist_index = next(
                    i for i, r in enumerate(playlist)
                    if r.id == self._last_selected_npc_record.id
                )
            except StopIteration:
                self._npc_playlist_index = 0

    def select_npc_record(self, record: DevRecord, *, start_music: bool = True) -> None:
        """Update detail panel and optionally start music for *record*.

        Used both by tree selection events and by the player widget.
        """
        from tui.screens.dev.data_mgmt.detail_panel import update_detail_for_record  # noqa: PLC0415

        self._last_selected_npc_record = record

        # Update playlist index to match
        for i, r in enumerate(self._npc_playlist):
            if r.id == record.id:
                self._npc_playlist_index = i
                break

        update_detail_for_record(self, record)

        if start_music:
            started = self._npc_music.play_record(
                record.id, record.song_id, force=True
            )
            if started:
                self._update_player_label(record)

    def restore_npc_selection(self) -> None:
        """Called when the NPC tab gains focus.

        - If a previous NPC is remembered: repopulate the detail panel
          (portrait re-renders) WITHOUT restarting music.
        - If no previous selection: pick a random NPC with a song and play it.
        """
        from tui.screens.dev.data_mgmt.detail_panel import update_detail_for_record  # noqa: PLC0415

        self.rebuild_npc_playlist()

        if self._last_selected_npc_record is not None:
            # Restore detail — do NOT call on_npc_changed, music keeps playing
            update_detail_for_record(self, self._last_selected_npc_record)
            self._update_player_label(self._last_selected_npc_record)
            return

        # No previous selection — pick a random NPC with a song
        if not self._npc_playlist:
            return

        record = _random.choice(self._npc_playlist)
        self._npc_playlist_index = self._npc_playlist.index(record)
        self._last_selected_npc_record = record
        update_detail_for_record(self, record)
        self._npc_music.play_record(record.id, record.song_id, force=True)
        self._update_player_label(record)

    def _update_player_label(self, record: DevRecord) -> None:
        try:
            player = self.query_one(NpcMusicPlayerWidget)
            player.update_now_playing(record.name, record.song_id)
            player.set_paused(self._npc_music.is_paused)
        except Exception:
            pass

    # ── Music poll timer ──────────────────────────────────────────────────

    def _on_music_poll(self) -> None:
        """Called every 500ms to detect end-of-track and drive autoplay/loop.

        Runs regardless of the active tab — music should continue playing when
        the user switches to dialog, timeline, or any other tab.
        """
        if not self._npc_music.poll_song_ended():
            return

        try:
            player = self.query_one(NpcMusicPlayerWidget)
        except Exception:
            return

        if not player.is_autoplay:
            # Autoplay off — loop the same track
            if self._last_selected_npc_record:
                self._npc_music.play_record(
                    self._last_selected_npc_record.id,
                    self._last_selected_npc_record.song_id,
                    force=True,
                )
            return

        # Autoplay on — advance to next track
        self._advance_playlist(forward=True, random_mode=player.is_random)

    def _advance_playlist(self, *, forward: bool, random_mode: bool) -> None:
        """Move to the next or previous track in the playlist."""
        if not self._npc_playlist:
            return

        if random_mode:
            # Pick a random track that isn't the current one (if possible)
            if len(self._npc_playlist) > 1:
                current_id = self._last_selected_npc_record.id if self._last_selected_npc_record else ""
                candidates = [r for r in self._npc_playlist if r.id != current_id]
                record = _random.choice(candidates)
            else:
                record = self._npc_playlist[0]
        else:
            step   = 1 if forward else -1
            self._npc_playlist_index = (self._npc_playlist_index + step) % len(self._npc_playlist)
            record = self._npc_playlist[self._npc_playlist_index]

        self.select_npc_record(record, start_music=True)

    # ── Player widget messages ────────────────────────────────────────────

    def on_npc_music_player_widget_request_prev(
        self, _: NpcMusicPlayerWidget.RequestPrev
    ) -> None:
        # Prev/next buttons are always sequential — random mode only applies to autoplay.
        self._advance_playlist(forward=False, random_mode=False)

    def on_npc_music_player_widget_request_next(
        self, _: NpcMusicPlayerWidget.RequestNext
    ) -> None:
        # Prev/next buttons are always sequential — random mode only applies to autoplay.
        self._advance_playlist(forward=True, random_mode=False)

    def on_npc_music_player_widget_request_toggle_pause(
        self, _: NpcMusicPlayerWidget.RequestTogglePause
    ) -> None:
        paused = self._npc_music.toggle_pause()
        try:
            self.query_one(NpcMusicPlayerWidget).set_paused(paused)
        except Exception:
            pass

    # ── Detail panel toggle ───────────────────────────────────────────────

    def _toggle_detail_panel(self) -> None:
        """Swap the detail panel between fixed-width and full-width."""
        self._detail_maximised = not self._detail_maximised
        detail_panel = self.query_one("#dm-detail-panel")
        list_panel   = self.query_one("#dm-list-panel")
        btn          = self.query_one("#dm-detail-expand", Button)
        if self._detail_maximised:
            detail_panel.styles.width = "1fr"
            list_panel.display        = False
            btn.label                 = "⤡"
        else:
            detail_panel.styles.width = str(_DETAIL_WIDTH_NORMAL)
            list_panel.display        = True
            btn.label                 = "⤢"

    # ── Textual event routing ─────────────────────────────────────────────

    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        handle_tab_activated(self, event)

    def on_input_changed(self, event: Input.Changed) -> None:
        handle_input_changed(self, event)

    def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
        handle_radio_set_changed(self, event)

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        handle_list_view_highlighted(self, event)

    def on_tree_node_highlighted(self, event: Tree.NodeHighlighted) -> None:
        handle_tree_node_highlighted(self, event)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "dm-detail-expand":
            self._toggle_detail_panel()
            return
        handle_button_pressed(self, event)