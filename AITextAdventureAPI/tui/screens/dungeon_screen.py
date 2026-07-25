"""
DungeonScreen: the in-dungeon exploration screen.

Mirrors the full behavior of `old/game_screens/dungeon_screen.run_dungeon_screen()`,
but implemented as a non-blocking Textual screen:

  - Arrow keys / WASD move the player on the Dungeon grid.
  - Space interacts with adjacent/current-tile entities (NPC meet, item pickup).
  - I opens the inventory screen.
  - U/D move up/down a floor via stairs (dz ±1).
  - Escape dismisses the dungeon and returns to the overworld.

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

from typing import Any, List, Optional

from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Footer, Static

from tui.screens.base_screen import BaseScreen
from tui.screens.combat_screen import CombatScreen
from tui.screens.message_dialog import MessageDialog
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
        Binding("w", "move_north", "North", show=False),
        Binding("up", "move_north", "North", show=False),
        Binding("s", "move_south", "South", show=False),
        Binding("down", "move_south", "South", show=False),
        Binding("a", "move_west", "West", show=False),
        Binding("left", "move_west", "West", show=False),
        Binding("d", "move_east", "East", show=False),
        Binding("right", "move_east", "East", show=False),
        Binding("u", "floor_up", "Up", show=True),
        Binding("shift+d", "floor_down", "Down", show=True),
        Binding("space", "interact", "Interact", show=True),
        Binding("i", "open_inventory", "Inventory", show=True),
        Binding("escape", "go_back", "Exit", show=True),
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
        self.app._active_dungeon = self._dungeon
        self._check_dialogs_and_refresh()

    # ── movement bindings ─────────────────────────────────────────────────

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
        self.app.push_screen("inventory")

    def action_interact(self) -> None:
        """Space: interact with entities on or adjacent to the player's tile."""
        if self._dialog_visible():
            return
        self._interact()

    def on_dismiss(self, result: bool | None = None) -> None:
        """Clear the active dungeon reference whenever this screen is removed,
        regardless of which code path triggered the dismiss."""
        self.app._active_dungeon = None

    def action_go_back(self) -> None:
        """Escape: leave the dungeon and return to the overworld."""
        self.dismiss(True)

    # ── movement ──────────────────────────────────────────────────────────

    def _handle_move(self, dx: int, dy: int, dz: int) -> None:
        if self._dialog_visible():
            return

        dungeon = self._dungeon
        player_pos = dungeon.get_player_pos()
        if player_pos is None:
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
            self.dismiss(True)
            return

        # check for pending dialogs from the move
        self._check_dialogs_and_refresh()

        # encounter checks (boss first, then random countdown)
        self._check_encounters(after_action=True)

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

        for ddx, ddy in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
            tx, ty, tz = px + ddx, py + ddy, pz
            adj_tile = dungeon.get_tile(tx, ty, tz)
            if not adj_tile or not adj_tile.entities:
                continue

            for ent in list(adj_tile.entities):
                if isinstance(ent, dict) and ent.get("type") == "npc":
                    npc_id = ent.get("npc_id")
                    if npc_id:
                        self._pg.check_meet_npc_dungeon(npc_id)
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
            self._check_dialogs_and_refresh()
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

        def _on_combat_done(players_won: bool | None) -> None:
            if not players_won:
                self._show_dialog(["You have been defeated..."], "Game Over")
                self.set_timer(2.0, lambda: self.dismiss(False))
                return

            if is_boss:
                mob_id = getattr(pg, "pending_fight_mob_id", None)
                if mob_id:
                    pg.check_complete_boss_mob(mob_id)

            self._check_dialogs_and_refresh()

        self.app.push_screen(CombatScreen(pg, hostiles), _on_combat_done)

    # ── dialog helpers ────────────────────────────────────────────────────

    def _check_dialogs_and_refresh(self) -> None:
        pg = self._pg
        if hasattr(pg, "info_dialogs") and pg.info_dialogs:
            messages: List[str] = []
            while pg.info_dialogs:
                messages.append(pg.pop_dialog())
            if messages:
                self._show_dialog(messages, "Message")
                return
        self._refresh_all()

    def _show_dialog(self, messages: List[str], title: str = "Message") -> None:
        if not messages:
            self._refresh_all()
            return

        self._remove_dialog()
        try:
            map_panel = self.query_one("#map-panel")
            dialog = MessageDialog(messages, title)
            map_panel.mount(dialog)
            self._schedule_dialog_check()
        except Exception as e:
            self.notify(f"Could not show dialog: {e}", severity="error")
            self._refresh_all()

    def _schedule_dialog_check(self) -> None:
        def _check() -> None:
            if not self._dialog_visible():
                self._refresh_all()
            else:
                self.set_timer(0.2, _check)

        self.set_timer(0.1, _check)

    def _dialog_visible(self) -> bool:
        try:
            self.query_one("#map-panel").query_one(MessageDialog)
            return True
        except Exception:
            return False

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