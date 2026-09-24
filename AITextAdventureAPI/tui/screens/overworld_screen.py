"""
OverworldScreen: the primary game screen shown after loading or starting a
new game.

Layout:
  ┌──────────── menu bar ─────────────────────────────┐
  │ [Inventory]  [Tasks]  [Main Menu]                 │
  ├──────── header (region – city) ───────────────────┤
  │                                      │             │
  │  MAP (fills available width/height)  │  Legend     │
  │  ┌─────────────────┐                 │  Party      │
  │  │ Actions overlay │ (if any)        │  Gold / Pos │
  │  └─────────────────┘                 │             │
  │  ┌─────────────────────────────┐     │             │
  │  │   Message Dialog (centered)  │     │             │
  │  └─────────────────────────────┘     │             │
  └────────────────────────────────────────────────────┘

The LocationOverlay widget is mounted on the "overlay" CSS layer so it
floats over the map without disrupting layout. WASD bindings remain on
this screen — the player can move while the overlay is visible.

The MessageDialog widget is mounted inside the map-panel container and
uses align: center middle to float centered over just the map area,
leaving the legend/stats visible. It steals focus to block input until
all messages are acknowledged, matching the console game's dialog flow.
"""
from __future__ import annotations

from textual import events, on, work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Footer, Static
from textual.worker import get_current_worker

from tui.screens.base_screen import BaseScreen
from tui.screens.combat_screen import CombatScreen
from tui.screens.confirm_screen import ConfirmScreen
from tui.screens.dungeon_screen import DungeonScreen
from tui.screens.location_menu_screen import LocationOverlay
from tui.screens.message_dialog import MessageDialog
from tui.screens.loading_dialog import LoadingDialog
from tui.services.encounter_service import (
    check_and_handle_encounters,
    get_boss_encounter_hostiles,
    get_random_encounter_hostiles,
)
from tui.services.location_actions import LocationAction, get_location_actions
from tui.services.movement_service import (
    check_random_encounter,
    ensure_tiles_around_sync,
    get_active_area,
    try_move,
)
from tui.services.overworld_renderer import (
    build_header,
    build_legend_lines,
    build_stats_lines,
    build_viewport_lines,
)


class OverworldScreen(BaseScreen):
    """Main overworld / world-map screen."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        # Callbacks queued while a dialog chain is already active (see
        # _check_dialogs_and_refresh) so deferred pending-combat checks are
        # never dropped.
        self._deferred_on_cleared: list = []
        # True while a background tile-generation pass is running; keeps the
        # busy watcher polling for the whole duration.
        self._generation_active = False
        # Monotonic id of the current tile-generation pass. A stale (cancelled)
        # worker uses its captured token to avoid stopping a newer pass's watcher.
        self._generation_token = 0
        # True while combat is on-screen; suppresses the tile worker's
        # combat callback so we can't stack two CombatScreens.
        self._combat_active = False

    LAYERS = ("default", "overlay")

    show_header = False
    show_footer = True

    BINDINGS = [
        Binding("w", "move_north", "North", show=False),
        Binding("up", "move_north", "North", show=False),
        Binding("s", "move_south", "South", show=False),
        Binding("down", "move_south", "South", show=False),
        Binding("a", "move_or_focus", "West", show=False),
        Binding("left", "move_west", "West", show=False),
        Binding("d", "move_east", "East", show=False),
        Binding("right", "move_east", "East", show=False),
        Binding("i", "open_inventory", "Inventory", show=True),
        Binding("t", "open_tasks", "Tasks", show=True),
        Binding("escape", "go_back", "Menu", show=True),
    ]

    DEFAULT_CSS = """
    OverworldScreen {
        layout: vertical;
        layers: base overlay;
    }

    #menu-bar {
        height: 3;
        background: $panel;
        border-bottom: solid $accent;
        padding: 0 1;
    }

    #menu-bar Button {
        height: 1;
        min-width: 14;
        margin-right: 1;
        border: none;
    }

    #location-header {
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
        width: 42;
        height: 1fr;
        layout: vertical;
        border-left: solid $accent;
    }

    #legend-panel {
        height: 1fr;
        border-bottom: solid $accent 50%;
        padding: 1;
        color: $text 80%;
    }

    #stats-panel {
        height: auto;
        padding: 1;
        color: $text 80%;
    }

    Footer {
        height: 1;
    }
    """

    def compose_content(self) -> ComposeResult:
        with Horizontal(id="menu-bar"):
            yield Button("(I)nventory", id="btn-inventory", variant="default")
            yield Button("(T)asks", id="btn-tasks", variant="default")
            yield Button("(Esc) Main Menu", id="btn-mainmenu", variant="default")

        yield Static("", id="location-header")

        with Horizontal(id="content-row"):
            with Vertical(id="map-panel"):
                yield Static("", id="map-content", markup=True)
            with Vertical(id="side-panel"):
                yield Static("", id="legend-panel")
                yield Static("", id="stats-panel")

        yield Footer()

    def on_mount(self) -> None:
        self.call_after_refresh(self._ensure_and_render)

    def on_screen_resume(self) -> None:
        """Called when returning from inventory/tasks/dungeon screens."""
        self._check_dialogs_and_refresh()
        self._update_overlay()

    def on_resize(self, event: events.Resize) -> None:
        self._refresh_all()

    # ── movement actions ──────────────────────────────────────────────────

    def _overlay_list_focused(self) -> bool:
        """Return True if the LocationOverlay's list currently has focus."""
        try:
            from textual.widgets import ListView  # noqa: PLC0415
            lv = self.query_one(LocationOverlay).query_one("#ov-list", ListView)
            return lv.has_focus
        except Exception:
            return False

    def action_move_north(self) -> None:
        if self._overlay_list_focused():
            return
        self._handle_move("w")

    def action_move_south(self) -> None:
        if self._overlay_list_focused():
            return
        self._handle_move("s")

    def action_move_west(self) -> None:
        if self._overlay_list_focused():
            return
        self._handle_move("a")

    def action_move_or_focus(self) -> None:
        """'a' key: focus the location overlay if visible, otherwise move west."""
        if self._overlay_list_focused():
            return
        if self._blocked():
            return
        try:
            overlay = self.query_one(LocationOverlay)
            overlay.focus_list()
            return
        except Exception:
            pass
        self._handle_move("a")

    def action_move_east(self) -> None:
        if self._overlay_list_focused():
            return
        self._handle_move("d")

    def action_open_inventory(self) -> None:
        """I key: open inventory screen."""
        if self._blocked():
            return
        self.app.push_screen("inventory")

    def action_open_tasks(self) -> None:
        """T key: open tasks screen."""
        if self._blocked():
            return
        self.app.push_screen("tasks")

    def action_interact(self) -> None:
        """E key: toggle the location overlay."""
        if self._blocked():
            return
        if self._overlay_visible():
            self._remove_overlay()
        else:
            pg = self._player_game()
            if pg is None:
                return
            self._update_overlay(pg, get_active_area(pg))

    def action_go_back(self) -> None:
        # Block navigation while a generation/task worker or dialog is active —
        # its deferred call_from_thread/on_done callbacks would otherwise refresh
        # or push combat onto an inactive screen after we've navigated away.
        if self._blocked():
            return

        def _handle(confirmed: bool | None) -> None:
            if confirmed:
                from tui.services.game_state import set_active_game
                set_active_game(None)
                self.app.goto_screen("main_menu")

        self.app.push_screen(
            ConfirmScreen("Return to main menu? (Unsaved progress will be lost)"),
            _handle,
        )

    # ── dialog and message handling ───────────────────────────────────────

    def _check_dialogs_and_refresh(self, on_cleared: "Callable[[], None] | None" = None) -> None:
        """Check for pending dialogs and display them, then refresh the view.

        If `on_cleared` is given it runs once the *entire* dialog chain (all
        info dialogs and any pending option dialog) has been resolved — used to
        defer combat/encounter checks until the player has read everything.
        """
        pg = self._player_game()
        if pg is None:
            self._refresh_all()
            if on_cleared is not None:
                on_cleared()
            return

        # Block re-entrancy — if a dialog or option dialog is already visible,
        # don't start a second chain. We must NOT drop `on_cleared` though: a
        # worker/combat completion arriving mid-dialog would otherwise lose its
        # deferred pending-combat check. Queue it so it runs when the active
        # chain resolves and re-enters this method.
        if self._dialog_visible():
            if on_cleared is not None:
                self._deferred_on_cleared.append(on_cleared)
            return

        # Info dialogs drain first — conversation lines before the choice appears
        if hasattr(pg, "info_dialogs") and pg.info_dialogs:
            messages = []
            while pg.info_dialogs:
                messages.append(pg.pop_dialog())
            if messages:
                self._show_dialog(messages, "Story", on_cleared=on_cleared)
                return

        # Option dialog follows once all preceding lines have been acknowledged
        if getattr(pg, "option_dialog", None):
            self._show_option_dialog(pg.option_dialog, on_cleared=on_cleared)
            return

        self._refresh_all()
        if on_cleared is not None:
            on_cleared()
        self._run_deferred_on_cleared()

    def _run_deferred_on_cleared(self) -> None:
        """Fire any callbacks queued while a dialog chain was already active."""
        queued = self._deferred_on_cleared
        if not queued:
            return
        self._deferred_on_cleared = []
        for cb in queued:
            cb()

    def _show_option_dialog(self, option_dialog: dict, on_cleared: "Callable[[], None] | None" = None) -> None:
        """Mount an OptionDialogWidget for the pending choice prompt.

        `on_cleared` is stashed and re-invoked after the player picks an option
        (and any resulting info dialogs drain), so a combat task awarded by a
        chosen option is still picked up.
        """
        from tui.screens.option_dialog import OptionDialogWidget  # noqa: PLC0415
        self._remove_option_dialog()
        self._pending_on_cleared = on_cleared
        try:
            map_panel = self.query_one("#map-panel")
            widget = OptionDialogWidget(option_dialog)
            map_panel.mount(widget)
        except Exception as e:
            self.notify(f"Could not show option dialog: {e}", severity="error")
            self._refresh_all()
            self._pending_on_cleared = None
            if on_cleared is not None:
                on_cleared()

    def _remove_option_dialog(self) -> None:
        from tui.screens.option_dialog import OptionDialogWidget  # noqa: PLC0415
        try:
            self.query_one("#map-panel").query_one(OptionDialogWidget).remove()
        except Exception:
            pass

    def on_option_dialog_widget_option_chosen(
        self, event: "OptionDialogWidget.OptionChosen"
    ) -> None:
        """Award the chosen task, clear the pending dialog, and continue."""
        from tui.screens.option_dialog import OptionDialogWidget  # noqa: PLC0415
        from services.task_completion_service import award_task_to_player_game  # noqa: PLC0415
        pg = self._player_game()
        self._remove_option_dialog()
        # Preserve any deferred callback across the option resolution so a
        # combat task awarded by the chosen option is still handled.
        on_cleared = getattr(self, "_pending_on_cleared", None)
        self._pending_on_cleared = None

        def _continue() -> None:
            # Defer until after Textual has processed the widget removal so that
            # _dialog_visible() returns False and the acquire info_dialogs surface.
            self.call_after_refresh(
                lambda: self._check_dialogs_and_refresh(on_cleared=on_cleared)
            )

        if pg is not None:
            pg.option_dialog = None
            # Awarding a task can fire long-running acquire events (e.g. an
            # option that starts the next chapter → world generation). Run it
            # off the compositor thread behind a loading overlay so the UI
            # stays responsive, then continue the dialog chain.
            self.run_blocking_with_loading(
                lambda: award_task_to_player_game(event.target_task_id, pg, None),
                on_done=_continue,
            )
        else:
            _continue()
        event.stop()

    def _show_dialog(self, messages: list[str], title: str = "Message", on_cleared: "Callable[[], None] | None" = None) -> None:
        """Display a centered message dialog with the given messages.

        The dialog will cycle through all messages sequentially and
        auto-remove when the queue is exhausted, then refresh the screen.

        Dialog is mounted inside the map panel so it centers over the map
        area without covering the legend/stats sidebar.
        """
        if not messages:
            self._refresh_all()
            if on_cleared is not None:
                on_cleared()
            return

        # Remove any existing dialog first
        self._remove_dialog()

        # Mount the dialog inside the map panel (not the screen root)
        try:
            map_panel = self.query_one("#map-panel")
            dialog = MessageDialog(messages, title)
            map_panel.mount(dialog)

            # Schedule periodic checks to refresh when dialog is removed
            self._schedule_dialog_check(on_cleared=on_cleared)
        except Exception as e:
            # Fallback: if mounting fails, just refresh
            self.notify(f"Could not show dialog: {e}", severity="error")
            self._refresh_all()
            if on_cleared is not None:
                on_cleared()

    def _schedule_dialog_check(self, on_cleared: "Callable[[], None] | None" = None) -> None:
        """Schedule a check to see if the dialog has been dismissed."""
        def _check_and_refresh() -> None:
            if not self._dialog_visible():
                # Re-enter the full dialog/option check so any queued
                # option_dialog surfaces immediately after info lines drain.
                # on_cleared is forwarded so it fires only once the entire
                # chain (including a following option dialog) is resolved.
                self._check_dialogs_and_refresh(on_cleared=on_cleared)
            else:
                self.set_timer(0.2, _check_and_refresh)

        self.set_timer(0.1, _check_and_refresh)

    def _dialog_visible(self) -> bool:
        """Check if a MessageDialog or OptionDialogWidget is currently mounted."""
        from tui.screens.option_dialog import OptionDialogWidget  # noqa: PLC0415
        try:
            map_panel = self.query_one("#map-panel")
            try:
                map_panel.query_one(MessageDialog)
                return True
            except Exception:
                pass
            try:
                map_panel.query_one(OptionDialogWidget)
                return True
            except Exception:
                pass
        except Exception:
            pass
        return False

    def _remove_dialog(self) -> None:
        """Remove the message dialog if present in the map panel."""
        try:
            map_panel = self.query_one("#map-panel")
            dialog = map_panel.query_one(MessageDialog)
            dialog.remove()
        except Exception:
            pass

    # ── busy / loading overlay ────────────────────────────────────────────

    def run_blocking_with_loading(
        self,
        fn: "Callable[[], None]",
        on_done: "Callable[[], None] | None" = None,
        message: str = "Loading...",
    ) -> None:
        """Run a blocking task chain off the compositor thread with a loading
        overlay so long-running task events (world generation, dungeon build,
        intro-story completion) can't freeze the UI.

        `fn` runs on a worker thread; `on_done` runs back on the compositor
        thread once it finishes. Callers that mutate shared game state through
        `handle_task_event` (NPC interactions, awarded option tasks) route
        through here so `pg.is_busy` has somewhere to surface a loading state.
        """
        self._show_loading(message)

        def _runner() -> None:
            try:
                fn()
            finally:
                def _finish() -> None:
                    self._hide_loading()
                    if on_done is not None:
                        on_done()
                self.app.call_from_thread(_finish)

        # Use the screen's worker API directly. A locally-defined @work function
        # is a plain callable, not a bound method, so the decorator's expected
        # `self` widget argument would be missing — run_worker sidesteps that.
        self.run_worker(_runner, thread=True, group="blocking_task", exclusive=False)

    def _busy(self) -> bool:
        """True while a long-running task event (dungeon build, etc.) runs."""
        pg = self._player_game()
        return bool(getattr(pg, "is_busy", False)) or self._loading_visible()

    def _blocked(self) -> bool:
        """Single guard for all input handlers: dialogs OR busy overlay."""
        return self._dialog_visible() or self._busy()

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
        # Mounting the LoadingDialog inside #map-panel does NOT make the screen
        # modal — the screen-level LocationOverlay (and any shop/travel overlay)
        # stay interactive and their Enter/click handlers could mutate the same
        # PlayerGame while the worker runs. Disable every interactive overlay
        # for the loading lifetime so no second action can race the worker.
        self._set_overlays_disabled(True)

    def _hide_loading(self) -> None:
        try:
            self.query_one("#map-panel").query_one(LoadingDialog).remove()
        except Exception:
            pass
        self._set_overlays_disabled(False)

    def _set_overlays_disabled(self, disabled: bool) -> None:
        """Disable/enable all interactive overlays (location menu, shop, travel)
        so they can't process input while a loading overlay is up."""
        try:
            for overlay in self.query(LocationOverlay):
                overlay.disabled = disabled
        except Exception:
            pass
        try:
            for overlay in self.query(".ow-overlay"):
                overlay.disabled = disabled
        except Exception:
            pass

    def _check_pending_combat(self) -> None:
        """Trigger combat if a task event set a pending boss fight.

        Mirrors DungeonScreen._check_encounters but overworld-flavored: only
        the priority boss fight is checked (random encounters here are driven
        by movement, not location actions).
        """
        pg = self._player_game()
        if pg is None:
            return
        if getattr(pg, "pending_fight_mob_id", None):
            self._trigger_combat(pg, get_active_area(pg))

    def _start_busy_watch(self) -> int:
        """Poll pg.is_busy for the whole generation pass; mirror the overlay.

        The watcher must stay alive until `_stop_busy_watch` is called by the
        generation worker — it can't stop on the first `is_busy == False` read
        because a long-running event (create_dungeon, complete_intro_story,
        remove_ocean) may not have flipped the flag yet when generation starts.

        Returns a token identifying this watch pass; the caller must pass it
        back to `_stop_busy_watch` so a stale/cancelled worker can't stop a
        newer pass's watcher.
        """
        self._generation_token += 1
        token = self._generation_token
        self._generation_active = True

        def _tick() -> None:
            # A newer pass superseded this one — stop ticking silently.
            if self._generation_token != token:
                return
            pg = self._player_game()
            if getattr(pg, "is_busy", False):
                self._show_loading()
            else:
                # Busy flag not (yet) set — hide the overlay but keep polling
                # until generation completes so a later long-running event is
                # still reflected. Do NOT run dialog checks here; the worker's
                # completion handler surfaces combat/dialogs exactly once.
                self._hide_loading()
            if getattr(self, "_generation_active", False):
                self.set_timer(0.1, _tick)

        _tick()
        return token

    def _stop_busy_watch(self, token: int | None = None) -> None:
        # Only the pass that owns the current token may stop the watcher; a
        # stale worker finishing after a newer pass started must be ignored.
        if token is not None and token != self._generation_token:
            return
        self._generation_active = False
        self._hide_loading()

    # ── movement handling ─────────────────────────────────────────────────

    def _handle_move(self, key: str) -> None:
        pg = self._player_game()
        if pg is None:
            return

        if self._blocked():
            return

        moved, reason = try_move(key, pg)
        if not moved:
            if reason:
                self.notify(reason, severity="warning", timeout=2)
            return

        self._refresh_all()
        self._update_overlay()

        dungeon = pg.get_dungeon_at_position()
        if dungeon is not None:
            self._enter_dungeon(pg, dungeon)
            return

        active_area = get_active_area(pg)
        encounter_messages = check_and_handle_encounters(pg, active_area)

        # Wait for any encounter/narrative dialogs to be dismissed before
        # starting combat so the player can read them first. A pending boss
        # fight (set via begin_combat during a task completion) or a random
        # encounter both defer to this point. Tile generation is deferred until
        # after any combat resolves so its own combat callback can't stack a
        # second CombatScreen on top of the active one.
        def _after_move_dialogs_cleared() -> None:
            if getattr(pg, "pending_fight_mob_id", None) or encounter_messages:
                self._trigger_combat(pg, active_area)
            else:
                self._ensure_tiles_worker(pg)

        self._check_dialogs_and_refresh(on_cleared=_after_move_dialogs_cleared)

    # ── dungeon entry ─────────────────────────────────────────────────────

    def _enter_dungeon(self, pg: Any, dungeon: Any) -> None:
        """Push DungeonScreen for the given dungeon, then handle the result."""
        # Place the player at the dungeon entrance location
        from game.objects.dungeon import DungeonTileType  # noqa: PLC0415

        if dungeon.player_pos is None:
            dungeon.place_player_at_location(DungeonTileType.ENTRANCE)

        def _on_dungeon_done(exited_normally: bool | None) -> None:
            # Player either walked out or was defeated
            if not exited_normally:
                self._show_dialog(["Your party was defeated in the dungeon..."], "Game Over")
                self.set_timer(2.0, lambda: self.action_go_back())
            else:
                self._check_dialogs_and_refresh()

        self.app.push_screen(DungeonScreen(dungeon, pg), _on_dungeon_done)

    def _trigger_combat(self, pg: Any, active_area: Any) -> None:
        """Trigger combat after encounter messages are displayed.

        Generates the hostile list via `tui/services/encounter_service.py`
        (which delegates to `tui/services/combat_service.py`), then pushes
        `CombatScreen` — a native Textual screen driven by the pure
        `CombatSimulation` engine from `old/combat_balancing_simulation/
        combat_simulator.py` — instead of running the legacy blocking
        `readchar`-based `CombatScreen.run()` loop. The result (win/loss)
        arrives through the `push_screen` callback, the same modal-result
        pattern used by `ConfirmScreen`.
        """
        if getattr(pg, "pending_fight_mob_id", None):
            hostiles = get_boss_encounter_hostiles(pg)
            is_boss = True
        else:
            hostiles = get_random_encounter_hostiles(pg, active_area)
            is_boss = False

        if not hostiles:
            self._refresh_all()
            return

        # Guard against stacking a second CombatScreen. The tile-generation
        # worker can independently queue a pending fight and call
        # _check_pending_combat while a battle is already on-screen; ignore
        # that until the current fight resolves.
        if self._combat_active:
            return
        self._combat_active = True
        # Snapshot the boss id now — get_boss_encounter_hostiles leaves
        # pending_fight_mob_id set, so we must clear it via check_complete_boss_mob
        # after the win instead of assuming it changed.
        boss_mob_id = getattr(pg, "pending_fight_mob_id", None) if is_boss else None

        def _on_combat_done(players_won: bool | None) -> None:
            self._combat_active = False
            if not players_won:
                # Player lost → return to main menu
                self._show_dialog(["You have been defeated..."], "Game Over")
                self.set_timer(2.0, lambda: self.action_go_back())
                return

            # Player won → complete the boss mob first (its completion events
            # can be long-running, so route through the loading worker), then
            # surface any queued dialogs and only afterwards re-check for a
            # freshly-awarded pending fight. Tile generation (deferred from the
            # move that started this fight) runs only once no further combat is
            # pending, so it can't stack another CombatScreen.
            def _after_combat_dialogs() -> None:
                if getattr(pg, "pending_fight_mob_id", None):
                    self._check_pending_combat()
                else:
                    self._ensure_tiles_worker(pg)

            def _surface() -> None:
                self._check_dialogs_and_refresh(on_cleared=_after_combat_dialogs)

            if boss_mob_id:
                self.run_blocking_with_loading(
                    lambda: pg.check_complete_boss_mob(boss_mob_id),
                    on_done=_surface,
                )
            else:
                _surface()

        self.app.push_screen(CombatScreen(pg, hostiles), _on_combat_done)

    # ── location overlay handling ─────────────────────────────────────────

    def _overlay_visible(self) -> bool:
        try:
            self.query_one(LocationOverlay)
            return True
        except Exception:
            return False

    def _remove_overlay(self) -> None:
        try:
            self.query_one(LocationOverlay).remove()
        except Exception:
            pass

    def _update_overlay(self) -> None:
        """Refresh the location overlay for the player's current tile.

        - If an overlay is already mounted, updates its action list in-place.
        - If no overlay exists, mounts a new one.
        - If there are no actions, removes any existing overlay.
        - Does nothing while a shop / travel / other .ow-overlay is open.
        """
        if self.query(".ow-overlay"):
            return

        pg = self._player_game()
        if pg is None:
            self._remove_overlay()
            return

        active_area = get_active_area(pg)
        actions     = get_location_actions(pg, active_area)

        if not actions:
            self._remove_overlay()
            return

        def _on_action_complete(took_action: bool) -> None:
            if took_action:
                # A location action (e.g. talking to an NPC) can complete a
                # task that queues dialogs and sets a pending fight. Defer the
                # combat check until the dialog chain clears so the player can
                # read the narrative before battle begins.
                self._check_dialogs_and_refresh(on_cleared=self._check_pending_combat)
            else:
                self._refresh_all()
            # Refresh the overlay in-place for the (possibly updated) tile
            self._update_overlay()

        # Re-use existing overlay instead of remove+remount to avoid flicker
        # and duplicate overlays when _update_overlay is called multiple times.
        try:
            existing = self.query_one(LocationOverlay)
            existing.refresh_actions(pg, active_area, actions, _on_action_complete)
            return
        except Exception:
            pass

        self.mount(LocationOverlay(pg, active_area, actions, _on_action_complete))

    # ── rendering ─────────────────────────────────────────────────────────

    @work(thread=True, exclusive=True, group="ensure_tiles")
    def _ensure_tiles_worker(self, pg: Any) -> None:
        """Background worker to ensure tiles around the player exist.

        Region generation runs here, and `create_region_at` → `acquire_task`
        can enqueue narrator/info dialogs (e.g. the start of the next chapter's
        task chain) and/or set `pg.option_dialog`. Those must be surfaced once
        generation finishes, so we hop back to the compositor thread and run the
        normal dialog-drain + refresh. Without this the chapter dialog silently
        sits in `pg.info_dialogs` until some unrelated event triggers a check.

        Marked exclusive + grouped so rapid movement can't spawn two concurrent
        generation passes racing on world_tiles / regions.
        """
        # Never run generation while a fight is on-screen. pending_fight_mob_id
        # is a single shared slot; if generation set it to mob B while boss A is
        # being fought, A's win path (check_complete_boss_mob) would clear B and
        # lose it. Deferring until combat resolves keeps the slot stable — the
        # move/combat flow re-invokes this worker once the fight ends.
        if self._combat_active:
            return

        # Snapshot queue state so we only force a dialog check when generation
        # actually produced new dialogs (avoids needless refresh churn on the
        # common no-op path where all nearby tiles already exist).
        had_dialogs_before = bool(getattr(pg, "info_dialogs", None)) or bool(
            getattr(pg, "option_dialog", None)
        )
        had_fight_before = bool(getattr(pg, "pending_fight_mob_id", None))

        # Region generation can fire long-running task events (create_dungeon,
        # complete_intro_story, remove_ocean) that flip pg.is_busy. Start the
        # busy watcher on the UI thread so the LoadingDialog overlay appears
        # and input stays blocked for their duration. Capture the token so this
        # (possibly-cancelled) pass only stops the watcher it actually started.
        token = self.app.call_from_thread(self._start_busy_watch)

        ensure_tiles_around_sync(pg, check_rad=4)

        has_dialogs_after = bool(getattr(pg, "info_dialogs", None)) or bool(
            getattr(pg, "option_dialog", None)
        )
        has_fight_after = bool(getattr(pg, "pending_fight_mob_id", None))

        # Clear the overlay once generation completes — but only if a newer
        # pass hasn't superseded this one (rapid movement cancels older passes;
        # ensure_tiles_around_sync is synchronous and can't check cancellation).
        self.app.call_from_thread(lambda: self._stop_busy_watch(token))

        new_dialogs = has_dialogs_after and not had_dialogs_before
        new_fight = has_fight_after and not had_fight_before

        if new_dialogs or new_fight:
            # New dialogs and/or a pending fight were queued during generation —
            # surface them on the compositor thread (widget access must not
            # happen off-thread). Defer any combat until the dialog chain
            # clears so the player can read narrative first.
            self.app.call_from_thread(
                lambda: self._check_dialogs_and_refresh(
                    on_cleared=self._check_pending_combat
                )
            )

    @work(thread=True, exclusive=True)
    def _refresh_all(self) -> None:
        """Rebuild map/legend/stats on a background thread and push to widgets."""
        pg = self._player_game()
        if pg is None:
            return

        worker = get_current_worker()

        # Build all text off the main thread
        header_text = build_header(pg)
        if worker.is_cancelled:
            return

        map_widget = self.query_one("#map-content", Static)
        map_width = map_widget.size.width or 75
        map_height = map_widget.size.height or 25
        viewport_lines = build_viewport_lines(pg, map_width, map_height)
        if worker.is_cancelled:
            return

        try:
            _, active_area = pg.get_region_and_active_area_for_position()
        except Exception:
            active_area = None
        legend_lines = build_legend_lines(active_area)
        from tui.services.location_actions import get_location_actions  # noqa: PLC0415
        from tui.services.movement_service import get_active_area as _gaa  # noqa: PLC0415
        try:
            _area = _gaa(pg)
            _has_actions = bool(get_location_actions(pg, _area))
        except Exception:
            _has_actions = False
        stats_lines = build_stats_lines(pg, has_actions=_has_actions)

        if worker.is_cancelled:
            return

        # Push results back to the compositor thread
        map_text = "\n".join(viewport_lines)
        legend_text = "\n".join(legend_lines)
        stats_text = "\n".join(stats_lines)

        self.app.call_from_thread(self.query_one("#location-header", Static).update, header_text)
        self.app.call_from_thread(self.query_one("#map-content", Static).update, map_text)
        self.app.call_from_thread(self.query_one("#legend-panel", Static).update, legend_text)
        self.app.call_from_thread(self.query_one("#stats-panel", Static).update, stats_text)

    def _ensure_and_render(self) -> None:
        """Ensure tiles exist around player and render initial view."""
        pg = self._player_game()
        if pg is None:
            return
        self._ensure_tiles_worker(pg)
        # Use _check_dialogs_and_refresh so any info_dialogs or option_dialog
        # set by task acquire events during world setup are shown immediately
        # rather than being silently skipped on the first render.
        self._check_dialogs_and_refresh()
        self._update_overlay()

    def _player_game(self) -> Any:
        from tui.services.game_state import get_active_game  # noqa: PLC0415
        return get_active_game()