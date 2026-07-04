"""
ItemsOverlay: floating inventory-item widget for InventoryScreen.

Mirrors the behaviour of `old/game_screens/select_items_screen.py`:
  - Filters by item type (all / utility / weapon / armor / special).
    Tab / Shift-Tab cycle filters.
  - Up / Down navigate the list.
  - Left / Right change the selected party member without closing.
  - Enter or clicking a row opens ItemActionScreen modal (use / discard / cancel).
    Only utility items may be used; non-utility shows a modal without the Use button.
  - Delete directly discards one unit without a modal.
  - Escape closes the overlay.

The CSS class "inv-overlay" is added in on_mount so InventoryScreen can
query and remove any open overlay generically.
"""
from __future__ import annotations

from typing import Any, Callable

from rich.markup import escape as rich_escape
from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical
from textual.widget import Widget
from textual.widgets import Label, ListItem, ListView, Static

from tui.screens.item_action_screen import ItemActionScreen

_FILTERS: tuple[str, ...] = ("all", "utility", "weapon", "armor", "special")
_FILTER_LABEL: dict[str, str] = {
    "all":     "All",
    "utility": "Utility",
    "weapon":  "Weapon",
    "armor":   "Armor",
    "special": "Special",
}


def _item_label(item: Any) -> str:
    name     = rich_escape(str(getattr(item, "name", "?")))
    qty      = getattr(item, "quantity", 1)
    desc     = rich_escape(str(getattr(item, "description", "") or ""))
    qty_str  = f" [dim]x{qty}[/dim]" if qty and qty > 1 else ""
    desc_str = f"  [dim italic]{desc[:40]}[/dim italic]" if desc else ""
    return f"{name}{qty_str}{desc_str}"


def _apply_filter(inventory: list, filter_key: str) -> list:
    if filter_key == "all":
        return list(inventory)
    try:
        from game.objects.utility_item import UtilityItem
        from game.objects.weapon import Weapon
        from game.objects.armor import Armor
        from game.objects.special_item import SpecialItem
    except ImportError:
        return list(inventory)
    mapping: dict[str, type] = {
        "utility": UtilityItem,
        "weapon":  Weapon,
        "armor":   Armor,
        "special": SpecialItem,
    }
    cls = mapping.get(filter_key)
    if cls is None:
        return list(inventory)
    return [it for it in inventory if isinstance(it, cls)]


class _ItemRow(ListItem):
    def __init__(self, item: Any) -> None:
        super().__init__(Label(_item_label(item)))
        self.item = item


class ItemsOverlay(Widget):
    """
    Floating inventory-item picker docked to the bottom of InventoryScreen.

    Tab / Shift-Tab cycle item-type filters.
    Left / Right change the active party member while the overlay stays open.
    Enter (or click) opens ItemActionScreen — use (utility only) / discard / cancel.
    Delete discards one unit directly.
    Escape closes.
    """

    can_focus = True

    BINDINGS = [
        Binding("up",        "cursor_up",     "Up",       show=False),
        Binding("down",      "cursor_down",   "Down",     show=False),
        Binding("left",      "prev_member",   "◄ Member", show=True),
        Binding("right",     "next_member",   "Member ►", show=True),
        Binding("enter",     "open_action",   "Action",   show=True),
        Binding("delete",    "discard_item",  "Discard",  show=True),
        Binding("tab",       "next_filter",   "Filter→",  show=True),
        Binding("shift+tab", "prev_filter",   "←Filter",  show=True),
        Binding("escape",    "request_close", "Close",    show=True),
    ]

    DEFAULT_CSS = """
    ItemsOverlay {
        layer: overlay;
        dock: bottom;
        width: 100%;
        height: 16;
        background: $surface;
        border-top: solid $accent;
    }

    ItemsOverlay > Vertical {
        height: 100%;
    }

    #ov-header {
        height: 1;
        text-align: center;
        text-style: bold;
        background: $boost;
        padding: 0 1;
    }

    #ov-filter-bar {
        height: 1;
        padding: 0 1;
        color: $text 70%;
    }

    #ov-list {
        height: 1fr;
    }

    #ov-hint {
        height: 1;
        padding: 0 1;
        color: $text 50%;
        text-align: center;
        border-top: solid $accent 30%;
    }
    """

    def __init__(self, player_game: Any, on_close: Callable[[str | None], None]) -> None:
        super().__init__()
        self._pg         = player_game
        self._on_close   = on_close
        self._filter_idx = 0

    # ── compose ──────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Static("── Items ──", id="ov-header")
            yield Static(self._filter_bar_text(), id="ov-filter-bar")
            yield ListView(id="ov-list")
            yield Static(
                "[dim]Enter/click:action  Del:discard  Tab/Shift-Tab:filter  ◄►:member  Esc:close[/dim]",
                id="ov-hint",
            )

    def on_mount(self) -> None:
        self.add_class("inv-overlay")
        self._rebuild_list()
        self.query_one("#ov-list", ListView).focus()

    # ── filter helpers ────────────────────────────────────────────────────

    @property
    def _current_filter(self) -> str:
        return _FILTERS[self._filter_idx]

    def _filter_bar_text(self) -> str:
        parts: list[str] = []
        for i, key in enumerate(_FILTERS):
            label = _FILTER_LABEL[key]
            if i == self._filter_idx:
                parts.append(f"[bold reverse] {label} [/bold reverse]")
            else:
                parts.append(f"[dim] {label} [/dim]")
        return "  ".join(parts)

    def _filtered_inventory(self) -> list:
        inv = list(getattr(self._pg, "inventory", []) or [])
        return _apply_filter(inv, self._current_filter)

    def _rebuild_list(self) -> None:
        lv = self.query_one("#ov-list", ListView)
        lv.clear()
        items = self._filtered_inventory()
        for item in items:
            lv.append(_ItemRow(item))
        self.query_one("#ov-filter-bar", Static).update(self._filter_bar_text())
        total = len(items)
        filt  = _FILTER_LABEL[self._current_filter]
        self.query_one("#ov-header", Static).update(
            f"── Items ({total}) · Tab to cycle filter · current: {filt} ──"
        )

    def _selected_item(self) -> Any | None:
        lv    = self.query_one("#ov-list", ListView)
        child = lv.highlighted_child
        return child.item if isinstance(child, _ItemRow) else None

    # ── events ────────────────────────────────────────────────────────────

    @on(ListView.Selected, "#ov-list")
    def _on_selected(self, event: ListView.Selected) -> None:
        event.stop()
        self._open_action_modal()

    # ── actions ───────────────────────────────────────────────────────────

    def action_cursor_up(self) -> None:
        self.query_one("#ov-list", ListView).action_cursor_up()

    def action_cursor_down(self) -> None:
        self.query_one("#ov-list", ListView).action_cursor_down()

    def action_prev_member(self) -> None:
        self._shift_member(-1)

    def action_next_member(self) -> None:
        self._shift_member(+1)

    def action_next_filter(self) -> None:
        self._filter_idx = (self._filter_idx + 1) % len(_FILTERS)
        self._rebuild_list()

    def action_prev_filter(self) -> None:
        self._filter_idx = (self._filter_idx - 1) % len(_FILTERS)
        self._rebuild_list()

    def action_open_action(self) -> None:
        self._open_action_modal()

    def action_discard_item(self) -> None:
        item = self._selected_item()
        if item is None:
            self.app.notify("Nothing selected.", title="Items")
            return
        try:
            removed = self._pg.remove_single_item_unit(item)
        except Exception as exc:
            self.app.notify(f"Could not discard: {rich_escape(str(exc))}", title="Items")
            return
        iname = rich_escape(str(getattr(item, "name", "item")))
        self.app.notify(
            f"Discarded {iname}." if removed else "Nothing was discarded.",
            title="Items",
        )
        self._rebuild_list()

    def action_request_close(self) -> None:
        self._on_close(None)

    # ── internal: modal ───────────────────────────────────────────────────

    def _open_action_modal(self) -> None:
        item   = self._selected_item()
        player = self._resolve_player()
        if item is None:
            self.app.notify("Nothing selected.", title="Items")
            return
        if player is None:
            self.app.notify("No character selected.", title="Items")
            return

        def _handle(result: str | None) -> None:
            if result == "use":
                self._do_use(item, player)
            elif result == "discard":
                self._do_discard(item)

        self.app.push_screen(ItemActionScreen(item, player, self._pg), _handle)

    def _do_use(self, item: Any, player: Any) -> None:
        try:
            from game.objects.utility_item import UtilityItem
            if not isinstance(item, UtilityItem):
                self.app.notify(
                    f"Cannot use {rich_escape(str(getattr(item, 'name', 'item')))} here.",
                    title="Items",
                )
                return
            full_inv = list(self._pg.inventory)
            full_idx = full_inv.index(item)
            res      = player.use_item(full_idx, self._pg)
            note  = res.get("note", "used") if isinstance(res, dict) else str(res)
            iname = rich_escape(str(getattr(item,   "name", "item")))
            pname = rich_escape(str(getattr(player, "name", "?")))
            self.app.notify(f"{pname} used {iname} — {note}", title="Items")
        except Exception as exc:
            self.app.notify(f"Error: {rich_escape(str(exc))}", title="Items")
        self._rebuild_list()

    def _do_discard(self, item: Any) -> None:
        try:
            removed = self._pg.remove_single_item_unit(item)
        except Exception as exc:
            self.app.notify(f"Could not discard: {rich_escape(str(exc))}", title="Items")
            return
        iname = rich_escape(str(getattr(item, "name", "item")))
        self.app.notify(
            f"Discarded {iname}." if removed else "Nothing was discarded.",
            title="Items",
        )
        self._rebuild_list()

    # ── internal: party navigation ────────────────────────────────────────

    def _shift_member(self, delta: int) -> None:
        try:
            from tui.screens.inventory_screen import InventoryScreen
            screen = self.app.screen
            if not isinstance(screen, InventoryScreen):
                return
            total = len(list(getattr(self._pg, "characters", [])))
            if total == 0:
                return
            new_sel = max(0, min(screen._selected + delta, total - 1))
            if new_sel == screen._selected:
                return
            screen._selected = new_sel
            if screen._selected < screen._offset:
                screen._offset = screen._selected
            if screen._selected >= screen._offset + 5:   # _MAX_DISPLAY = 5
                screen._offset = screen._selected - 4
            screen._refresh_cards()
        except Exception:
            return

    # ── helpers ───────────────────────────────────────────────────────────

    def _resolve_player(self) -> Any | None:
        try:
            from tui.screens.inventory_screen import InventoryScreen
            screen = self.app.screen
            if not isinstance(screen, InventoryScreen):
                return None
            players = list(getattr(self._pg, "characters", []))
            idx = screen._selected
            return players[idx] if 0 <= idx < len(players) else None
        except Exception:
            return None