"""
LocationOverlay: top-left floating action widget overlaid on the map.

This is a Widget, not a Screen. It is mounted directly into OverworldScreen
on Textual's "overlay" CSS layer so the map, legend, and stats remain fully
visible underneath. Because it is not a pushed Screen, WASD bindings on
OverworldScreen fire normally — the player can move while the overlay is open.

Key implementation notes
────────────────────────
compose() vs on_mount for ListView population
    Items are yielded inside the ListView context manager in compose(), NOT
    added via lv.append() in on_mount. When a Widget is dynamically mounted
    into a running screen via self.mount(), on_mount can fire before child
    widgets are fully attached, causing query_one() to raise NoMatches.
    Yielding items in compose() is always synchronous and safe.

Loot position restore
    loot_sublocation(player_game, name) uses player_game.x/y/z as its lookup
    key. Because the player can move while the overlay is open, those coords
    may differ from where the subloc was detected. We snapshot (x, y, z) in
    location_actions.get_location_actions() and temporarily restore them
    around the loot call so the lookup always finds the right subloc record.
"""
from __future__ import annotations

from typing import Any, Callable, List

from textual import events, on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.widget import Widget
from textual.widgets import Button, Label, ListItem, ListView, Static

from tui.services.location_actions import LocationAction


class _ActionItem(ListItem):
    """Single action row carrying its LocationAction payload."""

    def __init__(self, action: LocationAction) -> None:
        super().__init__(Label(action.label))
        self.action = action


class LocationOverlay(Widget):
    """Floating action-menu widget overlaid on the map panel."""

    can_focus = True

    BINDINGS = [
        Binding("up",     "cursor_up",   "Up",    show=False),
        Binding("down",   "cursor_down", "Down",  show=False),
        Binding("enter",  "confirm",     "Select", show=False),
        Binding("escape", "close",       "Close",  show=False),
    ]

    DEFAULT_CSS = """
    LocationOverlay {
        layer: overlay;
        width: 38;
        height: auto;
        max-height: 22;
        offset: 1 5;
        background: $surface;
        border: round $accent;
    }

    #ov-title {
        text-align: center;
        text-style: bold;
        background: $boost;
        padding: 0 1;
        width: 100%;
    }

    #ov-list {
        height: auto;
        max-height: 16;
    }

    #ov-close {
        width: 100%;
        height: 1;
        border-top: solid $accent 50%;
    }
    """

    def __init__(
        self,
        pg: Any,
        active_area: Any,
        actions: List[LocationAction],
        on_action: Callable[[bool], None],
    ) -> None:
        super().__init__()
        self._pg = pg
        self._active_area = active_area
        self._actions = actions
        self._on_action = on_action

    def compose(self) -> ComposeResult:
        title = _get_location_title(self._pg, self._active_area)
        with Vertical():
            yield Static(f"── {title} ──  [dim](a) to focus[/dim]", id="ov-title", markup=True)
            with ListView(id="ov-list"):
                for action in self._actions:
                    yield _ActionItem(action)
            yield Button("✕  Close", id="ov-close", variant="default")

    def refresh_actions(
        self,
        pg: Any,
        active_area: Any,
        actions: List[LocationAction],
        on_action: Callable[[bool], None],
    ) -> None:
        """Replace the action list and callback in-place without remounting."""
        self._pg          = pg
        self._active_area = active_area
        self._actions     = actions
        self._on_action   = on_action
        try:
            lv = self.query_one("#ov-list", ListView)
            # Remember the currently highlighted action id before clearing
            prev_id: str | None = None
            try:
                highlighted = lv.highlighted_child
                if isinstance(highlighted, _ActionItem):
                    prev_id = highlighted.action.id
            except Exception:
                pass

            lv.clear()
            for action in actions:
                lv.append(_ActionItem(action))

            # Restore the highlight after the DOM settles so the blue
            # selection background repaints correctly.
            restore_index = 0
            if prev_id is not None:
                for i, action in enumerate(actions):
                    if action.id == prev_id:
                        restore_index = i
                        break

            if actions:
                def _restore(idx: int = restore_index) -> None:
                    try:
                        self.query_one("#ov-list", ListView).index = idx
                    except Exception:
                        pass
                self.call_after_refresh(_restore)

            focused = lv.has_focus
        except Exception:
            focused = False
        self._set_title_hint(focused=focused)

    # ── keyboard navigation ────────────────────────────────────────────────

    def focus_list(self) -> None:
        """Give focus to the ListView so arrow keys + Enter work."""
        try:
            self.query_one("#ov-list", ListView).focus()
        except Exception:
            self.focus()

    def _set_title_hint(self, focused: bool) -> None:
        hint = "[dim](esc) to exit[/dim]" if focused else "[dim](a) to focus[/dim]"
        try:
            title = _get_location_title(self._pg, self._active_area)
            self.query_one("#ov-title", Static).update(
                f"── {title} ──  {hint}"
            )
        except Exception:
            pass

    def on_descendant_focus(self, event: events.DescendantFocus) -> None:
        self._set_title_hint(focused=True)

    def on_descendant_blur(self, event: events.DescendantBlur) -> None:
        self._set_title_hint(focused=False)

    def action_cursor_up(self) -> None:
        try:
            lv = self.query_one("#ov-list", ListView)
            lv.action_cursor_up()
        except Exception:
            pass

    def action_cursor_down(self) -> None:
        try:
            lv = self.query_one("#ov-list", ListView)
            lv.action_cursor_down()
        except Exception:
            pass

    def action_confirm(self) -> None:
        try:
            lv = self.query_one("#ov-list", ListView)
            item = lv.highlighted_child
            if isinstance(item, _ActionItem):
                self._execute(item.action)
        except Exception:
            pass

    def action_close(self) -> None:
        """Escape while focused: release focus back to the screen."""
        try:
            lv = self.query_one("#ov-list", ListView)
            if lv.has_focus:
                self.screen.set_focus(None)
                return
        except Exception:
            pass
        self.remove()

    # ── close ─────────────────────────────────────────────────────────────

    @on(Button.Pressed, "#ov-close")
    def _close(self) -> None:
        self.remove()

    # ── selection ─────────────────────────────────────────────────────────

    @on(ListView.Selected, "#ov-list")
    def _on_selected(self, event: ListView.Selected) -> None:
        if isinstance(event.item, _ActionItem):
            self._execute(event.item.action)

    # ── dispatch ──────────────────────────────────────────────────────────

    def _execute(self, action: LocationAction) -> None:
        kind = action.kind
        if kind == "npc":
            self._do_npc(action)
        elif kind == "shop":
            self._do_shop(action)
        elif kind == "sublocation":
            self._do_sublocation(action)
        elif kind == "floor_up":
            self._do_floor("u")
        elif kind == "floor_down":
            self._do_floor("j")
        elif kind == "travel":
            self._do_fast_travel()
        elif kind == "aircraft_enter":
            self._pg.enter_aircraft()
            self._on_action(True)
        elif kind == "aircraft_land":
            self._pg.land_aircraft()
            self._on_action(True)

    def _do_npc(self, action: LocationAction) -> None:
        npc_id = (action.data or {}).get("npc_id")

        def _interact() -> None:
            try:
                self._pg.handle_npc_interaction_at_player_location(npc_id)
            except Exception:
                pass

        # handle_npc_interaction_at_player_location can fire long-running task
        # events (create_dungeon, complete_intro_story, remove_ocean) that would
        # freeze Textual's compositor if run inline. Route it through the parent
        # screen's loading worker so a LoadingDialog shows and input is blocked
        # for its duration, then continue on the compositor thread.
        screen = self.screen
        runner = getattr(screen, "run_blocking_with_loading", None)
        if callable(runner):
            runner(_interact, on_done=lambda: self._on_action(True))
        else:
            _interact()
            self._on_action(True)

    def _do_shop(self, action: LocationAction) -> None:
        from tui.screens.shop_overlay import ShopOverlay  # noqa: PLC0415

        business_def = (action.data or {}).get("business_def", {})
        screen = self.screen

        def _on_done(acted: bool) -> None:
            self._on_action(acted)

        self.remove()
        screen.mount(ShopOverlay(self._pg, business_def, self._active_area, _on_done))

    def _do_fast_travel(self) -> None:
        from tui.screens.fast_travel_overlay import FastTravelOverlay  # noqa: PLC0415

        try:
            stations = self._pg.get_all_hyperways() or []
        except Exception:
            stations = []

        if not stations:
            self.app.notify("No hyperway stations found.", title="Fast Travel", severity="warning")
            return

        screen = self.screen

        def _on_done(acted: bool) -> None:
            self._on_action(acted)

        self.remove()
        screen.mount(FastTravelOverlay(self._pg, stations, _on_done))

    def _do_sublocation(self, action: LocationAction) -> None:
        from tui.screens.confirm_screen import ConfirmScreen

        data = action.data or {}
        name = data.get("name")
        has_loot = data.get("has_loot", False)
        # snapshot position recorded when the action list was built
        stored_x = data.get("x", self._pg.x)
        stored_y = data.get("y", self._pg.y)
        stored_z = data.get("z", self._pg.z)

        if not has_loot:
            sl = data.get("subloc", {})
            prompt = sl.get("prompt") or f"You examine the {name}."
            self.app.notify(prompt, title=name or "Examine")
            self._on_action(False)
            return

        sl = data.get("subloc", {})
        item = sl.get("loot")
        money = int(sl.get("money", 0) or 0)

        parts: list[str] = []
        if item:
            parts.append(f"the {item.name}")
        if money > 0:
            parts.append(f"{money:,} gold")
        msg = f"Pick up {' and '.join(parts)}?"

        def _on_confirm(confirmed: bool | None) -> None:
            if confirmed:
                # loot_sublocation looks up the subloc by pg.x/y/z — restore
                # the tile position so it finds the right record even if the
                # player has moved since the overlay was shown.
                orig_x, orig_y, orig_z = self._pg.x, self._pg.y, self._pg.z
                self._pg.x = stored_x
                self._pg.y = stored_y
                self._pg.z = stored_z
                try:
                    result = self._active_area.loot_sublocation(self._pg, name)
                finally:
                    self._pg.x = orig_x
                    self._pg.y = orig_y
                    self._pg.z = orig_z
                if result:
                    self.app.notify(result, title="Looted")
                self._on_action(True)
            else:
                # Player chose to leave — stay put, overlay refreshes in-place
                self._on_action(False)

        self.app.push_screen(
            ConfirmScreen(msg, yes_label="Take", no_label="Leave"),
            _on_confirm,
        )

    def _do_floor(self, cmd: str) -> None:
        from services.player_movement_service import handle_floor_action

        try:
            ok = handle_floor_action(cmd, self._active_area, self._pg)
        except Exception as exc:
            self.app.notify(str(exc), title="Floor Error", severity="error")
            return

        if ok:
            self._on_action(True)
        else:
            label = "top floor" if cmd == "u" else "bottom floor"
            self.app.notify(f"Already at the {label}.", title="Floor")

def _get_location_title(pg: Any, active_area: Any) -> str:
    """Return the display name of the player's current tile, or 'Open Area'."""
    try:
        tile = (getattr(active_area, "tiles", {}) or {}).get((pg.x, pg.y))
        if tile is not None:
            building = getattr(tile, "building", None)
            if isinstance(building, dict):
                name = building.get("display_name") or building.get("name", "")
                if name:
                    return str(name)
    except Exception:
        pass
    return "Open Area"