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
        # Reference count of in-flight tile-generation passes. The busy watcher
        # runs while this is > 0 and only tears down at 0, so a skipped/cancelled
        # pass's balanced start/stop can't hide loading state that a still-running
        # older pass owns.
        self._generation_refcount = 0
        # True while the busy watcher's poll loop is active.
        self._generation_active = False
        # True while combat is on-screen; suppresses the tile worker's
        # combat callback so we can't stack two CombatScreens.
        self._combat_active = False
        # Set when a location action's overlay refocus must be deferred because
        # _check_pending_combat opened an encounter dialog / started combat. The
        # combat completion path consumes it and refocuses the location list
        # once the dialog/battle is fully cleaned up.
        self._pending_overlay_refocus = False
        # True while the overlay-refocus watcher poll loop is running, so a
        # second location action can't stack a duplicate watcher.
        self._refocus_watch_active = False

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
        # A task (e.g. a story beat that seals the player into a rift) can place
        # the player inside a dungeon while the overworld was the active screen.
        # The authoritative pg.active_dungeon flag is set by that placement; open
        # the dungeon screen here so the player is actually taken inside. Guard
        # against re-opening the one we just exited (its own dismiss clears the
        # flag before this resumes).
        pg = self._player_game()
        active_dungeon = pg.get_active_dungeon() if pg is not None else None
        if active_dungeon is not None:
            self._enter_dungeon(pg, active_dungeon)
            return
        # A resumed screen can already carry a pending fight (e.g. from a load
        # or a task completed on another screen); start it once dialogs clear.
        self._check_dialogs_and_refresh(on_cleared=self._check_pending_combat)
        self._update_overlay()

    def on_resize(self, event: events.Resize) -> None:
        self._refresh_all()

    # ── movement actions ──────────────────────────────────────────────────

    def check_action(self, action: str, parameters: tuple) -> bool | None:
        """Disable gameplay bindings while a dialog or loading overlay is open.

        A key press that dismisses a MessageDialog (e.g. an encounter's
        "something approaches" prompt) must not also fire the screen-level
        binding for the same key — otherwise the dismiss press leaks through as
        a movement/interaction. Returning False makes Textual treat these
        actions as unavailable so the key is consumed only by the dialog.
        """
        gameplay_actions = {
            "move_north", "move_south", "move_west", "move_east",
            "move_or_focus", "open_inventory", "open_tasks", "interact",
            # Escape is bound to go_back; disable it while blocked so the dismiss
            # key falls through to the focused MessageDialog instead of being
            # swallowed by the screen binding.
            "go_back",
        }
        if action in gameplay_actions and self._blocked():
            return False
        # Structural guard: a blocking overlay (shop / fast-travel — anything on
        # the .ow-overlay layer) must swallow gameplay keys even if it has lost
        # ambient focus (e.g. after a ListView rebuild dropped focus). Without
        # this the screen's own WASD bindings would fire and move the player
        # "behind" the open overlay. Movement/focus keys stay handled by the
        # overlay itself while it has focus; this only closes the focus-loss hole.
        #
        # Escape (go_back) is deliberately exempt: in the same focus-loss state
        # the overlay never receives its own Escape handler, so blocking the
        # screen action too would strand the overlay with no keyboard close
        # path. action_go_back detects the open overlay and closes it instead.
        if action == "go_back" and self.query(".ow-overlay"):
            return True
        if action in gameplay_actions and self.query(".ow-overlay"):
            return False
        return True

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

        # A blocking overlay (shop / fast-travel) may have lost ambient focus so
        # its own Escape handler never fires. Route Escape to it here so it can
        # still be closed from the keyboard instead of opening the main-menu
        # confirm behind it.
        if self._close_active_overlay():
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

    def _leave_to_main_menu(self) -> None:
        """Unconditionally return to the main menu (no confirm, no busy guard).

        Used by game-over paths: they mount a "Game Over" MessageDialog and then
        navigate after a short delay, so the general `_blocked()` dialog guard in
        `action_go_back` must NOT apply here — otherwise the still-mounted dialog
        would suppress the navigation and strand the player on the overworld.
        """
        from tui.services.game_state import set_active_game  # noqa: PLC0415
        set_active_game(None)
        self.app.goto_screen("main_menu")

    def _close_active_overlay(self) -> bool:
        """Close an open .ow-overlay from the keyboard.

        Overlays normally handle Escape in their own on_key, but if the overlay
        has lost ambient focus (e.g. a ListView rebuild dropped focus) that key
        never reaches it. Called from action_go_back to guarantee a keyboard
        close path. Returns True if an overlay was found and closed.
        """
        overlays = self.query(".ow-overlay")
        if not overlays:
            return False
        overlay = overlays.last()
        closer = getattr(overlay, "action_close", None)
        try:
            if callable(closer):
                closer()
            else:
                overlay.remove()
        except Exception:
            return False
        return True

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
        """Fire callbacks queued while a dialog chain was already active.

        A callback can itself mount a new dialog (e.g. _check_pending_combat
        shows the encounter dialog). If it does, we must STOP draining and keep
        the remaining callbacks queued — otherwise a following callback would
        remove/replace the just-mounted dialog before its own on_cleared runs,
        stranding the pending fight or losing the first callback. The retained
        callbacks re-run when the active dialog clears and re-enters
        _check_dialogs_and_refresh → _run_deferred_on_cleared.
        """
        queued = self._deferred_on_cleared
        if not queued:
            return
        # Reset the queue; process one at a time so a callback that mounts a
        # dialog can pause draining with the rest preserved.
        self._deferred_on_cleared = []
        while queued:
            cb = queued.pop(0)
            cb()
            if self._dialog_visible():
                # This callback opened a dialog — preserve the not-yet-run
                # callbacks (prepended) for the next dialog-chain re-entry.
                self._deferred_on_cleared = queued + self._deferred_on_cleared
                return

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

        # Stream world-generation / long-task progress into the loading overlay
        # so the player can see what it's currently doing instead of a frozen
        # "Loading..." box. Lines are emitted on the worker thread, so marshal
        # each onto the compositor thread before touching the widget.
        try:
            from game.services import world_gen_progress as _progress  # noqa: PLC0415
        except Exception:  # noqa: BLE001
            _progress = None

        progress_token = None
        if _progress is not None:
            def _on_progress(line: str) -> None:
                def _apply(text: str = line) -> None:
                    self._update_loading_message(text)
                try:
                    self.app.call_from_thread(_apply)
                except Exception:  # noqa: BLE001
                    pass

            try:
                progress_token = _progress.subscribe(_on_progress)
            except Exception:  # noqa: BLE001
                progress_token = None

        # Prefer the short, PLAYER-FACING status channel for the overlay headline
        # when it's available (e.g. world generation phases / connectivity
        # passes). These are reassuring, human-readable lines rather than the raw
        # diagnostic stream above.
        status_token = None
        if _progress is not None and hasattr(_progress, "subscribe_status"):
            def _on_status(line: str) -> None:
                def _apply(text: str = line) -> None:
                    self._update_loading_message(text)
                try:
                    self.app.call_from_thread(_apply)
                except Exception:  # noqa: BLE001
                    pass

            try:
                status_token = _progress.subscribe_status(_on_status)
            except Exception:  # noqa: BLE001
                status_token = None

        def _runner() -> None:
            succeeded = False
            try:
                fn()
                succeeded = True
            finally:
                if progress_token is not None and _progress is not None:
                    try:
                        _progress.unsubscribe(progress_token)
                    except Exception:  # noqa: BLE001
                        pass
                if status_token is not None and _progress is not None:
                    try:
                        _progress.unsubscribe_status(status_token)
                    except Exception:  # noqa: BLE001
                        pass

                def _finish(ok: bool = succeeded) -> None:
                    # Always clear the loading overlay, but only continue into
                    # dialog/combat handling when fn() actually succeeded — a
                    # failed task completion must not be treated as successful
                    # (it would advance with partially-mutated state).
                    self._hide_loading()
                    if ok and on_done is not None:
                        on_done()
                self.app.call_from_thread(_finish)

        # Use the screen's worker API directly. A locally-defined @work function
        # is a plain callable, not a bound method, so the decorator's expected
        # `self` widget argument would be missing — run_worker sidesteps that.
        self.run_worker(_runner, thread=True, group="blocking_task", exclusive=False)

    def _busy(self) -> bool:
        """True while a long-running task event (dungeon build, etc.) runs."""
        pg = self._player_game()
        # _generation_refcount > 0 covers ordinary/no-op tile-generation passes
        # too: _start_busy_watch hides the loading widget when pg.is_busy is
        # false, so without the refcount _blocked() could go false while an
        # ensure worker is still in flight, letting Esc/another action navigate
        # away or mutate the same PlayerGame before its deferred callbacks run.
        return (
            bool(getattr(pg, "is_busy", False))
            or self._loading_visible()
            or self._generation_refcount > 0
        )

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
        self._refresh_overlays_disabled()

    def _update_loading_message(self, message: str) -> None:
        """Push a live progress line into the loading overlay, if shown."""
        try:
            self.query_one("#map-panel").query_one(LoadingDialog).update_message(message)
        except Exception:
            pass

    def _refresh_overlays_disabled(self) -> None:
        """Re-evaluate whether interactive overlays should stay disabled.

        Overlays must remain disabled while ANY generation pass is in flight
        (`_generation_refcount > 0`) even when the LoadingDialog widget is
        momentarily hidden (an ordinary/no-op pass hides it before pg.is_busy
        ever flips). Otherwise a location/shop/travel handler could mutate the
        shared PlayerGame concurrently with tile generation. Only re-enable
        once no pass is still running and no loading widget is up.
        """
        still_busy = self._generation_refcount > 0 or self._loading_visible()
        self._set_overlays_disabled(still_busy)
        # Overlays just re-enabled — retry any refocus request that was held
        # pending while generation ran so the location list regains focus.
        if not still_busy and self._pending_overlay_refocus:
            self._consume_pending_overlay_refocus()

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
        by movement, not location actions). The boss encounter narrative lines
        returned by check_and_handle_encounters are displayed first, and combat
        starts only once the player dismisses them.
        """
        pg = self._player_game()
        if pg is None:
            return
        if not getattr(pg, "pending_fight_mob_id", None):
            return
        active_area = get_active_area(pg)
        messages = check_and_handle_encounters(pg, active_area)
        if messages:
            self._show_dialog(
                messages, "Encounter",
                on_cleared=lambda: self._trigger_combat(pg, active_area),
            )
        else:
            self._trigger_combat(pg, active_area)

    def _start_busy_watch(self) -> None:
        """Register an in-flight generation pass and (re)start the poll loop.

        Uses a reference count: every `_begin_tile_generation` call registers a
        pass here and the matching worker retires it via `_stop_busy_watch`. The
        overlay/poll loop stays alive while the count is > 0, so a pass that was
        skipped (module lock held by another) or cancelled can safely retire its
        own registration without tearing down a still-running older pass's watch.
        """
        self._generation_refcount += 1
        # Disable interactive overlays for the whole generation lifetime, even
        # before pg.is_busy flips / the LoadingDialog appears, so a no-op pass
        # can't leave overlays interactive while a worker still runs.
        self._set_overlays_disabled(True)
        if self._generation_active:
            return
        self._generation_active = True

        def _tick() -> None:
            if self._generation_refcount <= 0:
                self._generation_active = False
                self._hide_loading()
                return
            pg = self._player_game()
            if getattr(pg, "is_busy", False):
                self._show_loading()
            else:
                # Busy flag not (yet) set — hide the overlay but keep polling
                # until all passes complete so a later long-running event is
                # still reflected. Do NOT run dialog checks here; the worker's
                # completion handler surfaces combat/dialogs exactly once.
                self._hide_loading()
            self.set_timer(0.1, _tick)

        _tick()

    def _stop_busy_watch(self) -> None:
        # Retire one in-flight pass. The poll loop tears down the overlay once
        # the count reaches zero (no pass is still generating).
        if self._generation_refcount > 0:
            self._generation_refcount -= 1
        if self._generation_refcount <= 0:
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

        # Wait for any narrative dialogs to be dismissed before starting combat
        # so the player can read them first. A pending boss fight (set via
        # begin_combat during a task completion) or a random encounter both
        # defer to this point. Tile generation is deferred until after any
        # combat resolves so its own combat callback can't stack a second
        # CombatScreen on top of the active one.
        def _start_combat_or_generate() -> None:
            if getattr(pg, "pending_fight_mob_id", None) or encounter_messages:
                self._trigger_combat(pg, active_area)
            else:
                self._begin_tile_generation(pg)

        def _after_move_dialogs_cleared() -> None:
            # check_and_handle_encounters returns the encounter narrative lines
            # ("You sense danger...", "An enemy appears!") for the caller to
            # display — they are NOT queued in pg.info_dialogs, so show them
            # here and only start combat once the player dismisses them.
            if encounter_messages:
                self._show_dialog(
                    encounter_messages, "Encounter", on_cleared=_start_combat_or_generate
                )
            else:
                _start_combat_or_generate()

        self._check_dialogs_and_refresh(on_cleared=_after_move_dialogs_cleared)

    # ── dungeon entry ─────────────────────────────────────────────────────

    def _enter_dungeon(self, pg: Any, dungeon: Any) -> None:
        """Push DungeonScreen for the given dungeon, then handle the result."""
        # Place the player at the dungeon entrance location
        from game.objects.dungeon import DungeonTileType  # noqa: PLC0415

        if dungeon.player_pos is None:
            # place_player_at_location() returns False when no valid entrance
            # tile exists. Don't mark the dungeon active or open an inert screen
            # with no player position — surface the failure and bail instead.
            if not dungeon.place_player_at_location(DungeonTileType.ENTRANCE):
                # A task placement may have already marked this dungeon active
                # before we got here. Clear it so on_screen_resume /
                # _ensure_and_render don't immediately re-enter this broken
                # dungeon on every resume and soft-lock the player.
                if getattr(pg, "active_dungeon", None) is dungeon:
                    pg.active_dungeon = None
                self._show_dialog(
                    ["You cannot find a way into the dungeon."], "Dungeon"
                )
                return

        # Mark this as the active dungeon (authoritative presence flag). A task
        # placement sets this already; setting it here covers manual walk-in
        # entry so both paths converge on the same state. Only reached once the
        # player has a valid placement.
        pg.active_dungeon = dungeon

        def _on_dungeon_done(exited_normally: DungeonResult) -> None:
            # Player either walked out or was defeated
            from tui.screens.dungeon_screen import (  # noqa: PLC0415
                DUNGEON_DEFEAT_HANDLED,
                DungeonResult,
            )

            if exited_normally == DUNGEON_DEFEAT_HANDLED:
                # DungeonScreen already showed its own defeat dialog and ran the
                # post-defeat delay; go straight to the main menu without
                # showing a second overlapping message or a second timer.
                self._leave_to_main_menu()
            elif not exited_normally:
                self._show_dialog(["Your party was defeated in the dungeon..."], "Game Over")
                self.set_timer(2.0, self._leave_to_main_menu)
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
            # An unresolvable boss id can be cleared by get_boss_encounter_hostiles
            # so no combat starts. No combat completion will fire, so consume any
            # pending overlay refocus here to avoid stranding the location list.
            self._refresh_all()
            self._consume_pending_overlay_refocus()
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
                self.set_timer(2.0, self._leave_to_main_menu)
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
                    self._begin_tile_generation(pg)
                self._consume_pending_overlay_refocus()

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

    def _consume_pending_overlay_refocus(self) -> None:
        """Refocus the location list after a pending combat/dialog opened by an
        NPC action has fully cleaned up.

        A location action can queue a fight; _after_pending_combat sets
        `_pending_overlay_refocus` instead of stealing focus from the encounter
        prompt. Once the fight/dialog resolves this restores the overlay's list
        focus so keyboard nav works again, but only if nothing new opened and
        the overlay is still present.
        """
        if not self._pending_overlay_refocus:
            return
        # Keep the request pending while another encounter dialog or chained
        # combat is still active (e.g. a boss win that immediately starts the
        # next pending fight). Clearing the flag here would leave that fight's
        # completion with nothing to consume, stranding the location list
        # unfocused after back-to-back fights.
        if self._dialog_visible() or self._combat_active:
            return
        # Also keep it pending while a tile-generation pass is in flight: the
        # LocationOverlay is disabled for the generation lifetime, so focusing
        # its list now would be a no-op. _refresh_overlays_disabled retries this
        # consume once overlays are re-enabled.
        if self._generation_refcount > 0 or self._loading_visible():
            return
        self._pending_overlay_refocus = False
        # Hand off to the feed watcher instead of a one-shot refocus: a trailing
        # info-dialog chain surfaced after combat can otherwise steal focus back
        # when Textual removes the last MessageDialog.
        self._start_overlay_refocus_watch()

    def _start_overlay_refocus_watch(self) -> None:
        """Poll the dialog/loading feed and refocus the location list once the
        player regains control.

        A single NPC interaction can throw up several info dialogs in a row.
        Firing a one-shot refocus the moment the chain *appears* cleared is
        unreliable: Textual reassigns focus after it removes the last focused
        MessageDialog, stealing focus back from the overlay. Instead we watch
        the two things that actually hold up player control — a loading overlay
        (long-running task events) and the player's `info_dialogs`/option feed —
        and only refocus once BOTH have fully drained and no combat is running.
        """
        if self._refocus_watch_active:
            return
        self._refocus_watch_active = True

        def _still_blocked() -> bool:
            pg = self._player_game()
            if pg is None:
                return False
            if self._dialog_visible() or self._combat_active:
                return True
            # Long-running task event (dungeon build, transport, world mutation)
            # still running — the overlay is disabled for its lifetime.
            if self._generation_refcount > 0 or self._loading_visible():
                return True
            # The feed itself: queued narrator lines or a pending choice prompt
            # that haven't been surfaced as a visible dialog yet.
            if getattr(pg, "info_dialogs", None):
                return True
            if getattr(pg, "option_dialog", None):
                return True
            # A queued boss fight that hasn't opened its encounter dialog /
            # CombatScreen yet — refocusing now would hand control back right
            # before the battle starts.
            if getattr(pg, "pending_fight_mob_id", None):
                return True
            return False

        def _tick() -> None:
            # The overlay may have been torn down (player transported / no
            # actions at the new tile) — stop watching rather than spin forever.
            if not self._overlay_visible():
                self._refocus_watch_active = False
                return
            if _still_blocked():
                self.set_timer(0.15, _tick)
                return
            self._refocus_watch_active = False

            def _refocus() -> None:
                try:
                    overlay = self.query_one(LocationOverlay)
                except Exception:
                    return
                # Nothing is blocking anymore (checked above), but the overlay
                # can be left in a stale disabled state if an NPC interaction
                # chained a loading pass plus tile generation — the disable/
                # enable bookkeeping races and never flips it back. Focusing a
                # *disabled* ListView is a silent no-op in Textual, which is why
                # the menu stayed greyed until the player moved (rebuilding it
                # fresh). Force it enabled before focusing so control returns.
                try:
                    overlay.disabled = False
                except Exception:
                    pass
                overlay.focus_list()

            self.call_after_refresh(_refocus)

        self.set_timer(0.15, _tick)

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
                def _after_pending_combat() -> None:
                    # An NPC interaction can run a task event (e.g. Kirn's
                    # create_dungeon in Ch4) that builds a dungeon and places the
                    # player inside it. That path sets pg.active_dungeon but does
                    # NOT push DungeonScreen — only on_screen_resume / movement /
                    # _ensure_and_render do. Since none of those fire after an
                    # in-overworld NPC dialog, check here first so the player is
                    # actually taken inside rather than left standing on the
                    # dungeon's overworld tile.
                    pg_now = self._player_game()
                    active_dungeon = (
                        pg_now.get_active_dungeon() if pg_now is not None else None
                    )
                    if active_dungeon is not None:
                        self._enter_dungeon(pg_now, active_dungeon)
                        return
                    # _check_pending_combat may mount an encounter MessageDialog
                    # (or start combat) that owns focus. The feed watcher below
                    # already waits for any such dialog/combat to drain before
                    # refocusing, so just run the combat check here.
                    self._check_pending_combat()

                self._check_dialogs_and_refresh(on_cleared=_after_pending_combat)
                # Start the refocus watcher unconditionally — NOT only inside
                # on_cleared. _check_dialogs_and_refresh may defer (or, under
                # re-entrancy, drop) on_cleared when a dialog is already visible,
                # which previously meant the watcher never started and the menu
                # stayed greyed. The watcher polls the whole feed (visible
                # dialogs, loading overlay, pending generation, and the player's
                # info_dialogs/option queue) and only refocuses once everything
                # has fully drained, so starting it now is always safe.
                self._start_overlay_refocus_watch()
            else:
                self._refresh_all()
            # Refresh the overlay in-place for the (possibly updated) tile
            self._update_overlay()

        # Re-use existing overlay instead of remove+remount to avoid flicker
        # and duplicate overlays when _update_overlay is called multiple times.
        try:
            existing = self.query_one(LocationOverlay)
            existing.refresh_actions(pg, active_area, actions, _on_action_complete)
            self._refresh_overlays_disabled()
            return
        except Exception:
            pass

        self.mount(LocationOverlay(pg, active_area, actions, _on_action_complete))
        # A generation pass may already be in flight (e.g. the initial render
        # starts the busy watch before this overlay is mounted). _start_busy_watch
        # can only disable overlays that already exist, so re-apply the disabled
        # state after the mount settles — otherwise the freshly-mounted menu
        # would stay interactive and could mutate the shared PlayerGame during
        # generation.
        self.call_after_refresh(self._refresh_overlays_disabled)

    # ── rendering ─────────────────────────────────────────────────────────

    def _begin_tile_generation(self, pg: Any) -> None:
        """Kick off a tile-generation pass from the UI thread.

        Registers the pass with the busy watcher (reference-counted) on the
        compositor thread *before* scheduling the worker. Every registration is
        balanced by exactly one `_stop_busy_watch` from the worker, so the
        overlay is only torn down when no pass is still generating — regardless
        of how `@work(exclusive=True)` cancellation and the module-level tile
        lock interleave concurrent passes.
        """
        if self._combat_active:
            return
        self._start_busy_watch()
        self._ensure_tiles_worker(pg)

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

        This worker always retires exactly one busy-watch registration (via
        `_stop_busy_watch`) on every exit path — the retirement is wrapped in a
        try/finally so even a cancelled pass (this worker is `exclusive=True`,
        so scheduling a newer pass cancels this one) can't leak its registration
        and leave `_generation_refcount` permanently positive (which would block
        all input and keep overlays disabled forever).
        """
        worker = get_current_worker()
        try:
            # Never run generation while a fight is on-screen. pending_fight_mob_id
            # is a single shared slot; if generation set it to mob B while boss A
            # is being fought, A's win path (check_complete_boss_mob) would clear
            # B and lose it. Deferring until combat resolves keeps the slot stable
            # — the move/combat flow re-invokes this worker once the fight ends.
            if self._combat_active or worker.is_cancelled:
                return

            # Snapshot queue state so we only force a dialog check when generation
            # actually produced new dialogs (avoids needless refresh churn on the
            # common no-op path where all nearby tiles already exist).
            had_dialogs_before = bool(getattr(pg, "info_dialogs", None)) or bool(
                getattr(pg, "option_dialog", None)
            )
            had_fight_before = bool(getattr(pg, "pending_fight_mob_id", None))

            # ensure_tiles_around_sync returns True only if THIS pass acquired
            # the module lock and actually ran generation (False if it skipped
            # because another pass held the lock).
            ran_generation = ensure_tiles_around_sync(pg, check_rad=4)

            has_dialogs_after = bool(getattr(pg, "info_dialogs", None)) or bool(
                getattr(pg, "option_dialog", None)
            )
            has_fight_after = bool(getattr(pg, "pending_fight_mob_id", None))

            new_dialogs = has_dialogs_after and not had_dialogs_before
            new_fight = has_fight_after and not had_fight_before

            # Surface newly-queued dialogs/combat when this pass produced them.
            # Normally a cancelled pass suppresses its callback (a newer pass
            # will surface state). But if THIS pass owned the lock and actually
            # created the state, we must surface it even when cancelled — the
            # replacement pass will skip on the lock and emit nothing, so the
            # dialogs/fight would otherwise stay queued indefinitely.
            should_surface = (new_dialogs or new_fight) and (
                not worker.is_cancelled or ran_generation
            )
            if should_surface:
                # New dialogs and/or a pending fight were queued during
                # generation — surface them on the compositor thread (widget
                # access must not happen off-thread). Defer any combat until the
                # dialog chain clears so the player can read narrative first.
                self.app.call_from_thread(
                    lambda: self._check_dialogs_and_refresh(
                        on_cleared=self._check_pending_combat
                    )
                )
        finally:
            # Retire this pass's busy-watch registration unconditionally. The
            # reference-counted watcher keeps loading state up while any other
            # pass is still running, so a skipped/cancelled pass retiring its own
            # registration won't hide an older pass's overlay prematurely.
            self.app.call_from_thread(self._stop_busy_watch)

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
        active_dungeon = pg.get_active_dungeon()
        if active_dungeon is not None:
            self._enter_dungeon(pg, active_dungeon)
            return

        self._update_overlay()

        # A save/resume can already carry pending_fight_mob_id. Resolve that
        # fight BEFORE starting tile generation: otherwise generation could run
        # concurrently with the boss-win cleanup and mutate/clear the shared
        # pending-fight slot. Only kick off generation once the startup dialog
        # chain (and any saved fight) has been fully handled.
        def _after_startup_dialogs() -> None:
            if getattr(pg, "pending_fight_mob_id", None):
                # _check_pending_combat starts the fight; tile generation is
                # resumed from the combat-done flow, keeping the slot stable.
                self._check_pending_combat()
            else:
                self._begin_tile_generation(pg)

        # Use _check_dialogs_and_refresh so any info_dialogs or option_dialog
        # set by task acquire events during world setup are shown immediately
        # rather than being silently skipped on the first render.
        self._check_dialogs_and_refresh(on_cleared=_after_startup_dialogs)

    def _player_game(self) -> Any:
        from tui.services.game_state import get_active_game  # noqa: PLC0415
        return get_active_game()