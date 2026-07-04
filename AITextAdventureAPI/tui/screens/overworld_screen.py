"""
OverworldScreen: the primary game screen shown after loading or starting a
new game.

Layout:
  ┌──────────── menu bar ─────────────────────────────┐
  │ [Save]  [Inventory]  [Tasks]  [Main Menu]         │
  ├──────── header (region – city) ───────────────────┤
  │                                      │             │
  │  MAP (fills available width/height)  │  Legend     │
  │  ┌─────────────────┐                 │  Party      │
  │  │ Actions overlay │ (if any)        │  Gold / Pos │
  │  └─────────────────┘                 │             │
  └────────────────────────────────────────────────────┘

The LocationOverlay widget is mounted on the "overlay" CSS layer so it
floats over the map without disrupting layout. WASD bindings remain on
this screen — the player can move while the overlay is visible.
"""
from __future__ import annotations

from textual import events, on, work
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Footer, Static

from tui.screens.base_screen import BaseScreen
from tui.screens.confirm_screen import ConfirmScreen
from tui.screens.location_menu_screen import LocationOverlay
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

    LAYERS = ("default", "overlay")

    show_header = False
    show_footer = True

    BINDINGS = [
        Binding("w", "move_north", "North", show=False),
        Binding("up", "move_north", "North", show=False),
        Binding("s", "move_south", "South", show=False),
        Binding("down", "move_south", "South", show=False),
        Binding("a", "move_west", "West", show=False),
        Binding("left", "move_west", "West", show=False),
        Binding("d", "move_east", "East", show=False),
        Binding("right", "move_east", "East", show=False),
        Binding("e", "interact", "Interact", show=True),
        Binding("escape", "go_back", "Menu", show=True),
    ]

    DEFAULT_CSS = """
    OverworldScreen {
        layout: vertical;
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
            yield Button("Save", id="btn-save", variant="default")
            yield Button("Inventory", id="btn-inventory", variant="default")
            yield Button("Tasks", id="btn-tasks", variant="default")
            yield Button("Main Menu", id="btn-mainmenu", variant="default")

        yield Static("", id="location-header")

        with Horizontal(id="content-row"):
            with Vertical(id="map-panel"):
                yield Static("", id="map-content")
            with Vertical(id="side-panel"):
                yield Static("", id="legend-panel")
                yield Static("", id="stats-panel")

        yield Footer()

    def on_mount(self) -> None:
        self.call_after_refresh(self._ensure_and_render)

    def on_resize(self, event: events.Resize) -> None:
        self._refresh_all()

    # ── movement actions ──────────────────────────────────────────────────

    def action_move_north(self) -> None:
        self._handle_move("w")

    def action_move_south(self) -> None:
        self._handle_move("s")

    def action_move_west(self) -> None:
        self._handle_move("a")

    def action_move_east(self) -> None:
        self._handle_move("d")

    def action_interact(self) -> None:
        """E key: toggle the location overlay."""
        if self._overlay_visible():
            self._remove_overlay()
        else:
            pg = self._player_game()
            if pg is None:
                return
            self._update_overlay(pg, get_active_area(pg))

    def action_go_back(self) -> None:
        def _handle(confirmed: bool | None) -> None:
            if confirmed:
                from tui.services.game_state import set_active_game
                set_active_game(None)
                self.app.goto_screen("main_menu")

        self.app.push_screen(ConfirmScreen("Return to Main Menu?"), _handle)

    # ── button handlers ───────────────────────────────────────────────────

    @on(Button.Pressed, "#btn-save")
    def _on_save(self) -> None:
        self.notify("Save not yet implemented.", title="Save Game")

    @on(Button.Pressed, "#btn-inventory")
    def _on_inventory(self) -> None:
        self.notify("Inventory not yet implemented.", title="Inventory")

    @on(Button.Pressed, "#btn-tasks")
    def _on_tasks(self) -> None:
        self.notify("Tasks not yet implemented.", title="Tasks")

    @on(Button.Pressed, "#btn-mainmenu")
    def _on_mainmenu(self) -> None:
        self.action_go_back()

    # ── movement ──────────────────────────────────────────────────────────

    def _handle_move(self, cmd: str) -> None:
        pg = self._player_game()
        if pg is None:
            return

        moved, _reason = try_move(cmd, pg)
        if not moved:
            return

        active_area = get_active_area(pg)
        if active_area is not None:
            check_random_encounter(pg, active_area)

        self._update_overlay(pg, active_area)
        self._ensure_and_render()

    # ── overlay management ────────────────────────────────────────────────

    def _overlay_visible(self) -> bool:
        return bool(self.query(LocationOverlay))

    def _remove_overlay(self) -> None:
        for w in self.query(LocationOverlay):
            w.remove()

    def _update_overlay(self, pg: object, active_area: object | None) -> None:
        """Replace the overlay with one matching the current tile's actions.
        Removes it entirely when there are no actions available here.
        """
        self._remove_overlay()
        if active_area is None:
            return
        actions: list[LocationAction] = get_location_actions(pg, active_area)
        if not actions:
            return
        self.mount(LocationOverlay(pg, active_area, actions, self._on_action_taken))

    def _on_action_taken(self, changed: bool) -> None:
        """Called by LocationOverlay after any action execution.

        Refreshes the map/side panel when state changed, then rebuilds
        the overlay so the action list reflects the new tile state
        (e.g. a looted subloc switches from 'Loot: x' to 'Search: x (empty)').
        """
        if changed:
            self._refresh_all()
            pg = self._player_game()
            if pg is not None:
                self._update_overlay(pg, get_active_area(pg))

        # drain any queued NPC / story dialog lines as notifications
        pg = self._player_game()
        if pg is None:
            return
        try:
            while pg.info_dialogs:
                line = pg.pop_dialog()
                if line:
                    self.notify(line, title="", timeout=6)
        except Exception:
            pass

    # ── tile generation + render ──────────────────────────────────────────

    def _ensure_and_render(self) -> None:
        pg = self._player_game()
        if pg is None:
            self._refresh_all()
            return
        self._ensure_tiles_worker(pg)

    @work(thread=True)
    def _ensure_tiles_worker(self, pg: object) -> None:
        ensure_tiles_around_sync(pg)
        self.app.call_from_thread(self._refresh_all)

    # ── rendering ─────────────────────────────────────────────────────────

    def _player_game(self) -> object | None:
        from tui.services.game_state import get_active_game
        return get_active_game()

    def _map_dimensions(self) -> tuple[int, int]:
        try:
            panel = self.query_one("#map-panel")
            w = max(10, panel.content_size.width)
            h = max(5, panel.content_size.height - 1)
            return w, h
        except Exception:
            return 40, 20

    def _refresh_all(self) -> None:
        self._refresh_map()
        self._refresh_side()

    def _refresh_map(self) -> None:
        pg = self._player_game()
        map_widget = self.query_one("#map-content", Static)
        header_widget = self.query_one("#location-header", Static)

        if pg is None:
            map_widget.update("No game loaded.")
            header_widget.update("")
            return

        view_w, view_h = self._map_dimensions()
        try:
            lines = build_viewport_lines(pg, view_w, view_h)
            map_widget.update("\n".join(lines))
            header_widget.update(build_header(pg))
        except Exception as exc:
            map_widget.update(f"Map error: {exc}")

    def _refresh_side(self) -> None:
        pg = self._player_game()
        legend_widget = self.query_one("#legend-panel", Static)
        stats_widget = self.query_one("#stats-panel", Static)

        if pg is None:
            legend_widget.update("")
            stats_widget.update("")
            return

        try:
            _, cur_area = pg.get_region_and_active_area_for_position()
            legend_widget.update("\n".join(build_legend_lines(cur_area)))
        except Exception:
            legend_widget.update("")

        try:
            stats_widget.update("\n".join(build_stats_lines(pg)))
        except Exception:
            stats_widget.update("")