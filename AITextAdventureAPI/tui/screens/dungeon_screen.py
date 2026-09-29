"""
DungeonScreen: the in-dungeon exploration screen.

Mirrors the full behavior of `old/game_screens/dungeon_screen.run_dungeon_screen()`,
but implemented as a non-blocking Textual screen:

  - Arrow keys / WASD move the player on the Dungeon grid.
  - Space interacts with adjacent/current-tile entities (NPC meet, item pickup).
  - I opens the inventory screen.
  - U/D move up/down a floor via stairs (dz ±1).
  - Walking onto the exit tile returns to the overworld (unless locked).

Layout mirrors OverworldScreen:
  ┌── header (dungeon name – floor) ─────────────────────┐
  │  MAP (fills available width/height)  │  Stats/Legend  │
  │  ┌─────────────────────────────┐     │                │
  │  │   Message Dialog (centered)  │     │                │
  │  └─────────────────────────────┘     │                │
  └───────────────────────────────────────────────────────┘

The screen dismisses with True (player exited normally) or False (player
died / gave up), matching the modal-result pattern used by CombatScreen
and ConfirmScreen so the caller (OverworldScreen) can react cleanly.
"""
from __future__ import annotations

from typing import Any, Callable, List, Optional

from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Footer, Static

from tui.screens.base_screen import BaseScreen
from tui.screens.combat_screen import CombatScreen
from tui.screens.message_dialog import MessageDialog
from tui.screens.loading_dialog import LoadingDialog
from tui.services.dungeon_renderer import build_header, build_minimap_lines, build_stats_lines
from tui.services.dungeon_encounter_service import (
    get_boss_encounter_hostiles,
    get_random_encounter_hostiles,
)
from tui.services.combat_service import build_simulation


class DungeonScreen(BaseScreen):
    """In-dungeon exploration and combat screen."""

    show_header = False
    show_footer = True

    BINDINGS = [
        Binding("up",     "move_north", "North", show=False),
        Binding("down",   "move_south", "South", show=False),
        Binding("left",   "move_west",  "West",  show=False),
        Binding("right",  "move_east",  "East",  show=False),
        Binding("u",      "floor_up",   "Up",    show=True),
        Binding("j",      "floor_down", "Down",  show=True),
        Binding("space",  "interact",   "Interact", show=True),
        Binding("i",      "open_inventory", "Inventory", show=True),
        Binding("escape", "noop", "", show=False),  # disable base-class go_back in dungeon
    ]

    DEFAULT_CSS = """
    DungeonScreen {
        layout: vertical;
    }

    #dungeon-header {
        height: 1;
        background: $boost;
        color: $text;
        text-align: center;
        text-style: bold;
        padding: 0 1;
    }

    #content-row {
        height: 1fr;
        layout: horizontal;
    }

    #map-panel {
        width: 1fr;
        height: 1fr;
        border: solid $primary;
        overflow: hidden;
        layers: base overlay;
    }

    #map-content {
        width: 100%;
        height: 100%;
        padding: 0 0;
    }

    #side-panel {
        width: 28;
        height: 1fr;
        layout: vertical;
        border-left: solid $accent;
    }

    #stats-panel {
        height: 1fr;
        padding: 1;
        color: $text 80%;
    }

    Footer {
        height: 1;
    }
    """

    def __init__(self, dungeon: Any, pg: Any) -> None:
        super().__init__()
        self._dungeon = dungeon
        self._pg = pg
        # True while a CombatScreen is on-screen; prevents stacking a second
        # combat push if an encounter re-check fires before the first resolves.
        self._combat_active = False

    # ── lifecycle ─────────────────────────────────────────────────────────

    def compose_content(self) -> ComposeResult:
        yield Static("", id="dungeon-header")
        with Horizontal(id="content-row"):
            with Vertical(id="map-panel"):
                yield Static("", id="map-content")
            with Vertical(id="side-panel"):
                yield Static("", id="stats-panel")
        yield Footer()

    def on_mount(self) -> None:
        self._dungeon.reveal_tiles_to_player()
        self.app._active_dungeon = self._dungeon
        self.call_after_refresh(self._refresh_all)

    def on_screen_resume(self) -> None:
        """Called when returning from inventory screen."""
        if self._presence_cleared():
            self.dismiss(True)
            return
        self.app._active_dungeon = self._dungeon
        self._check_dialogs_and_refresh()

    # ── movement bindings ─────────────────────────────────────────────────

    def check_action(self, action: str, parameters: tuple) -> bool | None:
        """Disable gameplay bindings while a dialog or loading overlay is open.

        A key press that dismisses a MessageDialog must not also fire the
        screen-level binding for the same key (e.g. space -> interact would
        re-trigger the NPC and append their standing text after their story;
        arrows -> move would step the player). Returning False here makes
        Textual treat these actions as unavailable so the dismiss key is
        consumed only by the dialog. Navigation actions stay enabled so the
        dialog's own dismissal is never blocked.
        """
        gameplay_actions = {
            "move_north", "move_south", "move_west", "move_east",
            "floor_up", "floor_down", "interact", "open_inventory",
            # Escape is bound to noop; disable it while blocked so the dismiss
            # key falls through to the focused MessageDialog instead of being
            # swallowed by the screen binding.
            "noop",
        }
        if action in gameplay_actions and self._blocked():
            return False
        return True

    def action_move_north(self) -> None:
        self._handle_move(0, -1, 0)

    def action_move_south(self) -> None:
        self._handle_move(0, 1, 0)

    def action_move_west(self) -> None:
        self._handle_move(-1, 0, 0)

    def action_move_east(self) -> None:
        self._handle_move(1, 0, 0)

    def action_floor_up(self) -> None:
        """Move up a floor (toward surface) — dz = -1."""
        self._handle_move(0, 0, -1)

    def action_floor_down(self) -> None:
        """Move down a floor (deeper) — dz = +1."""
        self._handle_move(0, 0, 1)

    def action_open_inventory(self) -> None:
        if self._blocked():
            return
        self.app.push_screen("inventory")

    def action_interact(self) -> None:
        """Space: interact with entities on or adjacent to the player's tile."""
        if self._blocked():
            return
        self._interact()

    def dismiss(self, result: bool | None = None) -> None:
        """Clear the active dungeon reference whenever this screen is removed,
        regardless of which code path triggered the dismiss."""
        self.app._active_dungeon = None
        # Clear the authoritative presence flag so the overworld doesn't
        # immediately re-open this dungeon on resume. Only reached on a real
        # dismiss (exit tile or defeat) — pushing the inventory screen pauses
        # this screen without dismissing it.
        if getattr(self._pg, "active_dungeon", None) is self._dungeon:
            self._pg.active_dungeon = None
        super().dismiss(result)

    def action_noop(self) -> None:
        """Swallow Escape while the player is still inside this dungeon."""
        if self._presence_cleared():
            self.dismiss(True)

    def _presence_cleared(self) -> bool:
        return (
            getattr(self._pg, "active_dungeon", None) is not self._dungeon
            or self._dungeon.get_player_pos() is None
        )

    def _try_leave_dungeon(self) -> bool:
        """Attempt to leave the dungeon. A locked dungeon traps the player:
        surface its locked_text (or a generic line) through the message feed
        instead of dismissing. Returns True if the dungeon was left."""
        dungeon = self._dungeon
        if dungeon is not None and dungeon.is_locked():
            pg = self._pg
            if getattr(dungeon, "locked_text", None):
                pg.add_dungeon_standing_text(dungeon)
            else:
                pg.add_info_dialog_line(dungeon.display_name, "You can't get out!")
            self._check_dialogs_and_refresh()
            return False
        self.dismiss(True)
        return True

    # ── movement ──────────────────────────────────────────────────────────

    def _handle_move(self, dx: int, dy: int, dz: int) -> None:
        if self._blocked():
            return

        dungeon = self._dungeon
        player_pos = dungeon.get_player_pos()
        if player_pos is None:
            self.dismiss(True)
            return

        px, py, pz = player_pos
        nx, ny, nz = px + dx, py + dy, pz + dz

        if not dungeon.in_bounds(nx, ny, nz):
            self.notify("Can't go that way.", severity="warning", timeout=1)
            return

        nt = dungeon.get_tile(nx, ny, nz)
        if not nt or not nt.passable:
            self.notify("Blocked.", severity="warning", timeout=1)
            return

        if nt.entities and len(nt.entities) > 0:
            self.notify("Something is in the way.", severity="warning", timeout=1)
            return

        dungeon.move_player(dx, dy, dz)
        self._refresh_all()

        # check exit
        if dungeon.is_player_at_exit():
            # A locked dungeon traps the player: don't leave (the shared helper
            # surfaces the locked_text message); otherwise dismiss the screen.
            self._try_leave_dungeon()
            return

        # Wait for any pending dialogs from the move to be dismissed before
        # checking encounters, so a boss ambush on a tile can't start combat
        # while the message dialog is still open/being read.
        self._check_dialogs_and_refresh(
            on_cleared=lambda: self._check_encounters(after_action=True)
        )

    # ── interaction ───────────────────────────────────────────────────────

    def _interact(self) -> None:
        """Check the player's tile and all 4 adjacent tiles for entities."""
        from game.objects.player import ItemType  # noqa: PLC0415

        dungeon = self._dungeon
        player_pos = dungeon.get_player_pos()
        if player_pos is None:
            return

        px, py, pz = player_pos
        any_interacted = False
        met_npc_ids: List[str] = []

        for ddx, ddy in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
            tx, ty, tz = px + ddx, py + ddy, pz
            adj_tile = dungeon.get_tile(tx, ty, tz)
            if not adj_tile or not adj_tile.entities:
                continue

            for ent in list(adj_tile.entities):
                if isinstance(ent, dict) and ent.get("type") == "npc":
                    npc_id = ent.get("npc_id")
                    if npc_id:
                        met_npc_ids.append(npc_id)
                    any_interacted = True

                elif isinstance(ent, ItemType):
                    picked = self._pg.pick_up_item(ent)
                    if picked:
                        adj_tile.entities.remove(ent)
                        name = getattr(ent, "name", getattr(ent, "id", "an item"))
                        self._pg.add_info_dialog_line(None, f"Picked up {name}.")
                    else:
                        name = getattr(ent, "name", getattr(ent, "id", "item"))
                        self._pg.add_info_dialog_line(None, f"Cannot pick up {name}: inventory full.")
                    any_interacted = True

        if any_interacted:
            # An interaction (meeting a boss NPC) can complete a task whose
            # events set a pending fight via begin_combat. We must wait for the
            # dialog chain to be dismissed before starting combat so the player
            # can read it first, so defer the encounter check until dialogs clear.
            def _after_meet() -> None:
                self._check_dialogs_and_refresh(
                    on_cleared=lambda: self._check_encounters(after_action=False)
                )

            if met_npc_ids:
                # check_meet_npc_dungeon → task completion executes events inline
                # and can fire long-running events (create_dungeon, etc.). Run it
                # through the loading worker so the dungeon compositor stays
                # responsive and input is blocked during the mutation.
                def _meet() -> None:
                    for npc_id in met_npc_ids:
                        self._pg.check_meet_npc_dungeon(npc_id)

                self.run_blocking_with_loading(_meet, on_done=_after_meet)
            else:
                _after_meet()
        else:
            self.notify("Nothing to interact with here.", timeout=2)

    # ── encounter handling ────────────────────────────────────────────────

    def _check_encounters(self, after_action: bool = False) -> None:
        """Check boss then random encounters; trigger combat if needed."""
        pg = self._pg
        dungeon = self._dungeon

        # boss mob takes priority
        if getattr(pg, "pending_fight_mob_id", None):
            hostiles = get_boss_encounter_hostiles(dungeon, pg)
            if hostiles:
                self._trigger_combat(hostiles, is_boss=True)
                return

        # random encounter via countdown timer
        if after_action:
            is_encounter = pg.countdown_random_encounter_timer()
            if is_encounter:
                hostiles = get_random_encounter_hostiles(dungeon, pg, force=True)
                if hostiles:
                    self._trigger_combat(hostiles, is_boss=False)

    def _trigger_combat(self, hostiles: List[Any], is_boss: bool = False) -> None:
        """Push the combat screen with the prepared hostile list."""
        pg = self._pg

        # Guard against stacking a second CombatScreen if an encounter re-check
        # fires while a battle is already on-screen.
        if self._combat_active:
            return
        self._combat_active = True

        def _on_combat_done(players_won: bool | None) -> None:
            self._combat_active = False
            if not players_won:
                self._show_dialog(["You have been defeated..."], "Game Over")
                self.set_timer(2.0, lambda: self.dismiss(False))
                return

            # A post-fight task completion can award another defeat task whose
            # acquire events set a fresh pending_fight_mob_id (back-to-back
            # fights). Re-check encounters once these dialogs are dismissed so
            # the next fight starts only after the player reads the dialog.
            def _after_completion() -> None:
                self._check_dialogs_and_refresh(
                    on_cleared=lambda: self._check_encounters(after_action=False)
                )

            if is_boss:
                mob_id = getattr(pg, "pending_fight_mob_id", None)
                if mob_id:
                    # check_complete_boss_mob → complete_task executes every
                    # completion event inline; a boss whose completion fires
                    # create_dungeon/complete_intro_story/remove_ocean would
                    # freeze the dungeon compositor. Run it through the loading
                    # worker so a LoadingDialog shows and input is blocked for
                    # its duration, then surface dialogs/encounters afterward.
                    self.run_blocking_with_loading(
                        lambda: pg.check_complete_boss_mob(mob_id),
                        on_done=_after_completion,
                    )
                    return

            _after_completion()

        self.app.push_screen(CombatScreen(pg, hostiles), _on_combat_done)

    # ── dialog helpers ────────────────────────────────────────────────────

    def _check_dialogs_and_refresh(self, on_cleared: Optional[Callable[[], None]] = None) -> None:
        pg = self._pg
        if self._presence_cleared():
            self.dismiss(True)
            return
        if hasattr(pg, "info_dialogs") and pg.info_dialogs:
            messages: List[str] = []
            while pg.info_dialogs:
                messages.append(pg.pop_dialog())
            if messages:
                self._show_dialog(messages, "Message", on_cleared=on_cleared)
                return
        self._refresh_all()
        if on_cleared is not None:
            on_cleared()

    def _show_dialog(
        self,
        messages: List[str],
        title: str = "Message",
        on_cleared: Optional[Callable[[], None]] = None,
    ) -> None:
        if not messages:
            self._refresh_all()
            if on_cleared is not None:
                on_cleared()
            return

        self._remove_dialog()
        try:
            map_panel = self.query_one("#map-panel")
            dialog = MessageDialog(messages, title)
            map_panel.mount(dialog)
            self._schedule_dialog_check(on_cleared=on_cleared)
        except Exception as e:
            self.notify(f"Could not show dialog: {e}", severity="error")
            self._refresh_all()
            if on_cleared is not None:
                on_cleared()

    def _schedule_dialog_check(self, on_cleared: Optional[Callable[[], None]] = None) -> None:
        def _check() -> None:
            if not self._dialog_visible():
                self._refresh_all()
                if on_cleared is not None:
                    on_cleared()
            else:
                self.set_timer(0.2, _check)

        self.set_timer(0.1, _check)

    def _dialog_visible(self) -> bool:
        try:
            self.query_one("#map-panel").query_one(MessageDialog)
            return True
        except Exception:
            return False

    def _blocked(self) -> bool:
        """Single guard for input handlers: a dialog is open OR a long-running
        task event (dungeon build, etc.) is mutating shared state."""
        return (
            self._dialog_visible()
            or self._loading_visible()
            or bool(getattr(self._pg, "is_busy", False))
        )

    # ── loading overlay ───────────────────────────────────────────────────

    def _loading_visible(self) -> bool:
        try:
            self.query_one("#map-panel").query_one(LoadingDialog)
            return True
        except Exception:
            return False

    def _show_loading(self, message: str = "Loading...") -> None:
        if self._loading_visible():
            return
        try:
            self.query_one("#map-panel").mount(LoadingDialog(message))
        except Exception:
            pass

    def _hide_loading(self) -> None:
        try:
            self.query_one("#map-panel").query_one(LoadingDialog).remove()
        except Exception:
            pass

    def run_blocking_with_loading(
        self,
        fn: Callable[[], None],
        on_done: Optional[Callable[[], None]] = None,
        message: str = "Loading...",
    ) -> None:
        """Run a blocking task chain off the compositor thread with a loading
        overlay so long-running task events (dungeon build, intro-story
        completion, ocean removal) fired by e.g. boss completion can't freeze
        the dungeon compositor. `fn` runs on a worker thread; `on_done` runs
        back on the compositor thread once it finishes.
        """
        self._show_loading(message)

        def _runner() -> None:
            succeeded = False
            try:
                fn()
                succeeded = True
            finally:
                def _finish(ok: bool = succeeded) -> None:
                    # Always clear the loading overlay, but only continue into
                    # encounter/dialog handling when fn() actually succeeded — a
                    # failed task completion must not advance with partially-
                    # mutated state.
                    self._hide_loading()
                    if ok and on_done is not None:
                        on_done()
                self.app.call_from_thread(_finish)

        self.run_worker(_runner, thread=True, group="dungeon_blocking", exclusive=False)

    def _remove_dialog(self) -> None:
        try:
            self.query_one("#map-panel").query_one(MessageDialog).remove()
        except Exception:
            pass

    # ── rendering ─────────────────────────────────────────────────────────

    def _refresh_all(self) -> None:
        dungeon = self._dungeon
        pg = self._pg

        header_text = build_header(dungeon)
        self.query_one("#dungeon-header", Static).update(header_text)

        map_widget = self.query_one("#map-content", Static)
        map_w = map_widget.size.width or 72
        map_h = map_widget.size.height or 23
        lines = build_minimap_lines(dungeon, view_w=map_w, view_h=map_h)
        map_widget.update("\n".join(lines))

        stats_lines = build_stats_lines(dungeon, pg)
        self.query_one("#stats-panel", Static).update("\n".join(stats_lines))