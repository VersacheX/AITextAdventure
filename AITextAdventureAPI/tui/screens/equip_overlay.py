"""
EquipOverlay: floating equipment-management widget for InventoryScreen.

Mirrors `old/game_screens/select_equipment_screen.py`, following the same
docked/filtered-list pattern already proven in `items_overlay.py`:
  - Filters by slot: all / weapon / head / body / arms / legs.
    Tab / Shift-Tab cycle filters.
  - Up / Down navigate the list.
  - Left / Right change the selected party member without closing the overlay.
  - Click highlights a row only. Enter or the Equip button opens ItemActionScreen.
  - Delete directly discards the highlighted item.
  - Escape closes the overlay.

Right panel is split into two columns:
  - Left col: selected item stats/description.
  - Right col: selected character's current loadout, awards, statuses, and
    stat diff vs the highlighted item (green=better, red=worse, dim=no change).

The CSS class "inv-overlay" is added in on_mount so InventoryScreen can
query and remove any open overlay generically.
"""
from __future__ import annotations

from typing import Any, Callable

from rich.markup import escape as rich_escape
from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Button, Label, ListItem, ListView, Static

from tui.screens.item_action_screen import ItemActionScreen

_EQUIP_FILTERS: tuple[str, ...] = ("all", "weapon", "head", "body", "arms", "legs")
_EQUIP_FILTER_LABEL: dict[str, str] = {
    "all":    "All",
    "weapon": "Weapon",
    "head":   "Head",
    "body":   "Body",
    "arms":   "Arms",
    "legs":   "Legs",
}


# ── pure helpers ──────────────────────────────────────────────────────────────

def _apply_equip_filter(inventory: list, filter_key: str) -> list:
    try:
        from game.objects.weapon import Weapon
        from game.objects.armor import Armor, ArmorType
    except ImportError:
        return list(inventory)
    if filter_key == "all":
        return [it for it in inventory if isinstance(it, (Weapon, Armor))]
    if filter_key == "weapon":
        return [it for it in inventory if isinstance(it, Weapon)]
    slot_map: dict[str, Any] = {
        "head": ArmorType.HEAD,
        "body": ArmorType.BODY,
        "arms": ArmorType.ARMS,
        "legs": ArmorType.LEGS,
    }
    slot = slot_map.get(filter_key)
    if slot is None:
        return [it for it in inventory if isinstance(it, (Weapon, Armor))]
    return [it for it in inventory if isinstance(it, Armor) and it.slot == slot]


def _equip_item_label(item: Any) -> str:
    name  = rich_escape(str(getattr(item, "name", "?")))
    stats: list[str] = []
    try:
        from game.objects.weapon import Weapon
        from game.objects.armor import Armor
        if isinstance(item, Weapon):
            dmg  = int(getattr(item, "damage", 0) or 0)
            crit = float(getattr(item, "critical_chance", 0.0) or 0)
            stats.append(f"DMG:{dmg}")
            if crit:
                stats.append(f"Crt:{crit:.0f}%")
        elif isinstance(item, Armor):
            stats.append(f"DEF:{int(getattr(item, 'defense', 0) or 0)}")
    except Exception:
        pass
    for attr, short in (("strength","S"),("dexterity","D"),("intelligence","I"),("constitution","C")):
        try:
            v = int(getattr(item, attr, 0) or 0)
            if v:
                stats.append(f"{short}:{v}")
        except Exception:
            pass
    stat_str = "  ".join(stats)
    return f"{name}  [dim]{stat_str}[/dim]" if stat_str else name


def _diff_row(label: str, new_val: int | float, old_val: int | float, *, fmt: str = "d") -> str:
    if fmt == "f":
        val_str  = f"{float(new_val):.1f}"
        diff     = float(new_val) - float(old_val)
        diff_str = f"{diff:+.1f}"
    else:
        val_str  = str(int(new_val))
        diff     = int(new_val) - int(old_val)
        diff_str = f"{int(diff):+d}"
    if diff > 0:
        diff_markup = f"[green]{diff_str}[/green]"
    elif diff < 0:
        diff_markup = f"[red]{diff_str}[/red]"
    else:
        diff_markup = f"[dim]{diff_str}[/dim]"
    return f"{label}: {val_str}  {diff_markup}"


def _format_status(status: dict) -> str:
    """One-line display for a status descriptor, e.g. 'Attack Buff (F) (3t)'."""
    try:
        from game.constants_other import ELEMENTAL_CHAR_KEYS
    except ImportError:
        ELEMENTAL_CHAR_KEYS = {}
    name  = rich_escape(str(status.get("name") or status.get("id") or "Status"))
    elems = status.get("elements") or []
    elem_str = "".join(ELEMENTAL_CHAR_KEYS.get(str(e), "") for e in elems)
    turns = status.get("turns_remaining", status.get("duration", 1))
    try:
        turns = int(turns)
    except (TypeError, ValueError):
        turns = 1
    dur_str = "perm" if turns == -1 else f"{turns}t"
    suffix  = f" {elem_str}" if elem_str else ""
    return f"{name}{suffix} [dim]({dur_str})[/dim]"


def _build_item_info(item: Any | None) -> str:
    """Left column: item name, description, and all stats."""
    if item is None:
        return "[dim]← Select an item[/dim]"

    lines: list[str] = []
    iname = rich_escape(str(getattr(item, "name", "?")))
    lines.append(f"[bold]{iname}[/bold]")

    desc = getattr(item, "description", "") or getattr(item, "desc", "")
    if desc:
        lines.append(rich_escape(str(desc)))

    lines.append("")

    try:
        from game.objects.weapon import Weapon
        from game.objects.armor import Armor, ArmorType
        if isinstance(item, Weapon):
            lines.append("[dim]── Weapon ──[/dim]")
            dmg  = int(getattr(item, "damage", 0) or 0)
            crit = float(getattr(item, "critical_chance", 0.0) or 0)
            lines.append(f"DMG:   {dmg}")
            if crit:
                lines.append(f"CRIT%: {crit:.1f}")
        elif isinstance(item, Armor):
            slot = getattr(item, "slot", None)
            slot_label = slot.name if hasattr(slot, "name") else str(slot or "?")
            lines.append(f"[dim]── Armor · {slot_label} ──[/dim]")
            lines.append(f"DEF:   {int(getattr(item, 'defense', 0) or 0)}")
    except Exception:
        pass

    for attr, lbl in (
        ("strength",     "STR"),
        ("dexterity",    "DEX"),
        ("intelligence", "INT"),
        ("constitution", "CON"),
        ("durability",   "DUR"),
    ):
        v = int(getattr(item, attr, 0) or 0)
        if v:
            lines.append(f"{lbl}:   {v}")

    value = getattr(item, "value", None)
    if value:
        lines.append("")
        lines.append(f"[dim]Value: {value}g  |  Sell: {int(value * 0.5)}g[/dim]")

    return "\n".join(lines)


def _build_char_detail(player: Any, item: Any | None) -> str:
    """Right column: character loadout + stat diff vs highlighted item."""
    lines: list[str] = []
    pname = rich_escape(str(getattr(player, "name", "?")))
    lvl   = getattr(player, "level", 0)
    lines.append(f"[bold]{pname}[/bold]  Lv.{lvl}")
    lines.append("")

    w    = getattr(player, "equipped_weapon", None)
    head = getattr(player, "head_armor",      None)
    body = getattr(player, "body_armor",      None)
    arms = getattr(player, "arm_armor",       None)
    legs = getattr(player, "leg_armor",       None)

    lines.append("[dim]── Equipped ──[/dim]")
    lines.append(f"WPN:  {rich_escape(w.name    if w    else 'None')}")
    lines.append(f"HEAD: {rich_escape(head.name if head else 'None')}")
    lines.append(f"BODY: {rich_escape(body.name if body else 'None')}")
    lines.append(f"ARMS: {rich_escape(arms.name if arms else 'None')}")
    lines.append(f"LEGS: {rich_escape(legs.name if legs else 'None')}")

    up_abil = int(getattr(player, "unused_ability_slots", 0) or 0)
    up_stat = int(getattr(player, "unused_stat_points",   0) or 0)
    up_pow  = int(getattr(player, "unused_power_points",  0) or 0)
    awards: list[str] = []
    if up_abil:
        awards.append(f"S:{up_abil}")
    if up_stat:
        awards.append(f"SP:{up_stat}")
    if up_pow:
        awards.append(f"PP:{up_pow}")
    if awards:
        lines.append("")
        lines.append(f"[yellow]★ {'  '.join(awards)}[/yellow]")

    statuses = list(getattr(player, "statuses", []) or [])
    if statuses:
        lines.append("")
        lines.append("[dim]── Statuses ──[/dim]")
        for st in statuses:
            if isinstance(st, dict):
                lines.append(f"  {_format_status(st)}")

    if item is None:
        return "\n".join(lines)

    try:
        from game.objects.weapon import Weapon
        from game.objects.armor import Armor, ArmorType
    except ImportError:
        return "\n".join(lines)

    lines.append("")
    iname = rich_escape(str(getattr(item, "name", "?")))
    lines.append(f"[bold]── vs {iname} ──[/bold]")

    if isinstance(item, Weapon):
        current = w
        lines.append(_diff_row("DMG",
            int(getattr(item, "damage", 0) or 0),
            int(getattr(current, "damage", 0) or 0) if current else 0))
        lines.append(_diff_row("Crit%",
            float(getattr(item, "critical_chance", 0.0) or 0),
            float(getattr(current, "critical_chance", 0.0) or 0) if current else 0.0,
            fmt="f"))
        for attr, short in (("strength","STR"),("dexterity","DEX"),
                             ("intelligence","INT"),("constitution","CON")):
            nv = int(getattr(item,    attr, 0) or 0)
            ov = int(getattr(current, attr, 0) or 0) if current else 0
            if nv or ov:
                lines.append(_diff_row(short, nv, ov))

    elif isinstance(item, Armor):
        slot = getattr(item, "slot", None)
        _slot_map: dict[Any, tuple[Any, str]] = {
            ArmorType.HEAD: (head, "HEAD"),
            ArmorType.BODY: (body, "BODY"),
            ArmorType.ARMS: (arms, "ARMS"),
            ArmorType.LEGS: (legs, "LEGS"),
        }
        current, slot_label = _slot_map.get(slot, (None, "?"))
        lines.append(f"[dim]Slot: {slot_label}[/dim]")
        lines.append(_diff_row("DEF",
            int(getattr(item, "defense", 0) or 0),
            int(getattr(current, "defense", 0) or 0) if current else 0))
        for attr, short in (("strength","STR"),("dexterity","DEX"),
                             ("intelligence","INT"),("constitution","CON")):
            nv = int(getattr(item,    attr, 0) or 0)
            ov = int(getattr(current, attr, 0) or 0) if current else 0
            if nv or ov:
                lines.append(_diff_row(short, nv, ov))
    else:
        lines.append("[dim]Not equipable[/dim]")

    return "\n".join(lines)


# ── Widget ────────────────────────────────────────────────────────────────────

class _EquipRow(ListItem):
    def __init__(self, item: Any) -> None:
        super().__init__(Label(_equip_item_label(item)))
        self.item = item


class EquipOverlay(Widget):
    """
    Floating equipment picker docked to the bottom of InventoryScreen.

    Tab / Shift-Tab cycle equipment-slot filters (all/weapon/head/body/arms/legs).
    Left / Right change the active party member while the overlay stays open.
    Click highlights a row only. Enter or the Equip button opens the action modal.
    Delete directly discards without a modal.
    Escape closes the overlay.
    """

    can_focus = True

    BINDINGS = [
        Binding("up",        "cursor_up",     "Up",       show=False),
        Binding("down",      "cursor_down",   "Down",     show=False),
        Binding("left",      "prev_member",   "◄ Member", show=True),
        Binding("right",     "next_member",   "Member ►", show=True),
        Binding("enter",     "open_action",   "Equip",    show=True),
        Binding("delete",    "discard_item",  "Discard",  show=True),
        Binding("tab",       "next_filter",   "Filter→",  show=True),
        Binding("shift+tab", "prev_filter",   "←Filter",  show=True),
        Binding("escape",    "request_close", "Close",    show=True),
    ]

    DEFAULT_CSS = """
    EquipOverlay {
        layer: overlay;
        dock: bottom;
        width: 100%;
        height: 26;
        background: $surface;
        border-top: solid $accent;
        layout: vertical;
    }

    #eq-header {
        height: 1;
        text-align: center;
        text-style: bold;
        background: $boost;
        padding: 0 1;
    }

    #eq-filter-bar {
        height: 1;
        padding: 0 1;
        color: $text 70%;
        border-bottom: solid $accent 20%;
    }

    #eq-main-row {
        height: 1fr;
    }

    #eq-list-panel {
        width: 1fr;
        height: 100%;
    }

    #eq-list {
        height: 100%;
    }

    #eq-detail-panel {
        width: 66;
        height: 100%;
        border-left: solid $accent 30%;
        layout: vertical;
    }

    #eq-detail-cols {
        height: 1fr;
    }

    #eq-item-col {
        width: 1fr;
        height: 100%;
        padding: 0 1;
        overflow-y: auto;
        border-right: solid $accent 20%;
    }

    #eq-char-col {
        width: 1fr;
        height: 100%;
        padding: 0 1;
        overflow-y: auto;
    }

    #eq-action-row {
        height: 3;
        padding: 0 1;
        align: left middle;
        border-top: solid $accent 20%;
    }

    #eq-btn-equip {
        width: 12;
        margin-right: 1;
    }

    #eq-btn-discard {
        width: 12;
    }

    #eq-hint {
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

    # ── compose ───────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        yield Static("── Equip ──", id="eq-header")
        yield Static(self._filter_bar_text(), id="eq-filter-bar")
        with Horizontal(id="eq-main-row"):
            with Vertical(id="eq-list-panel"):
                yield ListView(id="eq-list")
            with Vertical(id="eq-detail-panel"):
                with Horizontal(id="eq-detail-cols"):
                    yield Static("[dim]← Select an item[/dim]", id="eq-item-col")
                    yield Static("[dim]No character selected[/dim]", id="eq-char-col")
                with Horizontal(id="eq-action-row"):
                    yield Button("Equip", id="eq-btn-equip", variant="primary", disabled=True)
                    yield Button("Discard", id="eq-btn-discard", variant="error", disabled=True)
        yield Static(
            "[dim]Enter/Equip btn:equip  Del/Discard btn:discard  Tab/Shift-Tab:filter  ◄►:member  Esc:close[/dim]",
            id="eq-hint",
        )

    def on_mount(self) -> None:
        self.add_class("inv-overlay")
        self._rebuild_list()
        self.query_one("#eq-list", ListView).focus()

    # ── public API called by InventoryScreen ──────────────────────────────

    def on_player_changed(self) -> None:
        """Called by InventoryScreen after the selected character changes."""
        self._update_detail(self._highlighted_item())

    # ── filter helpers ────────────────────────────────────────────────────

    @property
    def _current_filter(self) -> str:
        return _EQUIP_FILTERS[self._filter_idx]

    def _filter_bar_text(self) -> str:
        parts: list[str] = []
        for i, key in enumerate(_EQUIP_FILTERS):
            label = _EQUIP_FILTER_LABEL[key]
            if i == self._filter_idx:
                parts.append(f"[bold reverse] {label} [/bold reverse]")
            else:
                parts.append(f"[dim] {label} [/dim]")
        return "  ".join(parts)

    def _filtered_equipment(self) -> list:
        inv = list(getattr(self._pg, "inventory", []) or [])
        return _apply_equip_filter(inv, self._current_filter)

    def _rebuild_list(self) -> None:
        lv = self.query_one("#eq-list", ListView)
        lv.clear()
        items = self._filtered_equipment()
        for item in items:
            lv.append(_EquipRow(item))
        self.query_one("#eq-filter-bar", Static).update(self._filter_bar_text())
        total = len(items)
        filt  = _EQUIP_FILTER_LABEL[self._current_filter]
        self.query_one("#eq-header", Static).update(
            f"── Equip ({total}) · Tab to cycle filter · current: {filt} ──"
        )
        self._update_detail(None)

    def _highlighted_item(self) -> Any | None:
        lv    = self.query_one("#eq-list", ListView)
        child = lv.highlighted_child
        return child.item if isinstance(child, _EquipRow) else None

    def _update_detail(self, item: Any | None) -> None:
        player = self._resolve_player()

        try:
            self.query_one("#eq-item-col", Static).update(_build_item_info(item))
        except Exception:
            pass

        try:
            char_text = (
                _build_char_detail(player, item)
                if player is not None
                else "[dim]No character selected[/dim]"
            )
            self.query_one("#eq-char-col", Static).update(char_text)
        except Exception:
            pass

        has_item = item is not None
        try:
            self.query_one("#eq-btn-equip",   Button).disabled = not has_item
            self.query_one("#eq-btn-discard", Button).disabled = not has_item
        except Exception:
            pass

    # ── events ────────────────────────────────────────────────────────────

    @on(ListView.Highlighted, "#eq-list")
    def _on_highlighted(self, event: ListView.Highlighted) -> None:
        item = event.item.item if isinstance(event.item, _EquipRow) else None
        self._update_detail(item)

    @on(ListView.Selected, "#eq-list")
    def _on_selected(self, event: ListView.Selected) -> None:
        """Click only highlights the row — use Enter or the Equip button to act."""
        event.stop()

    @on(Button.Pressed, "#eq-btn-equip")
    def _on_equip_btn(self) -> None:
        self._open_action_modal()

    @on(Button.Pressed, "#eq-btn-discard")
    def _on_discard_btn(self) -> None:
        item = self._highlighted_item()
        if item is not None:
            self._do_discard(item)

    # ── actions ───────────────────────────────────────────────────────────

    def action_cursor_up(self) -> None:
        self.query_one("#eq-list", ListView).action_cursor_up()

    def action_cursor_down(self) -> None:
        self.query_one("#eq-list", ListView).action_cursor_down()

    def action_prev_member(self) -> None:
        self._shift_member(-1)

    def action_next_member(self) -> None:
        self._shift_member(+1)

    def action_next_filter(self) -> None:
        self._filter_idx = (self._filter_idx + 1) % len(_EQUIP_FILTERS)
        self._rebuild_list()

    def action_prev_filter(self) -> None:
        self._filter_idx = (self._filter_idx - 1) % len(_EQUIP_FILTERS)
        self._rebuild_list()

    def action_open_action(self) -> None:
        self._open_action_modal()

    def action_discard_item(self) -> None:
        item = self._highlighted_item()
        if item is None:
            self.app.notify("Nothing selected.", title="Equip")
            return
        self._do_discard(item)

    def action_request_close(self) -> None:
        self._on_close(None)

    # ── internal: modal ───────────────────────────────────────────────────

    def _open_action_modal(self) -> None:
        item   = self._highlighted_item()
        player = self._resolve_player()
        if item is None:
            self.app.notify("Nothing selected.", title="Equip")
            return
        if player is None:
            self.app.notify("No character selected.", title="Equip")
            return

        def _handle(result: str | None) -> None:
            if result == "equip":
                self._do_equip(item, player)
            elif result == "discard":
                self._do_discard(item)

        self.app.push_screen(ItemActionScreen(item, player, self._pg), _handle)

    # ── internal: actions ─────────────────────────────────────────────────

    def _do_equip(self, item: Any, player: Any) -> None:
        try:
            from game.objects.weapon import Weapon
            from game.objects.armor import Armor
            if isinstance(item, Weapon):
                ok = player.equip_weapon(self._pg, item)
            elif isinstance(item, Armor):
                ok = player.equip_armor(self._pg, item)
            else:
                self.app.notify(
                    f"Cannot equip {rich_escape(str(getattr(item, 'name', 'item')))}.",
                    title="Equip",
                )
                return
        except Exception as exc:
            self.app.notify(f"Error: {rich_escape(str(exc))}", title="Equip")
            return
        iname = rich_escape(str(getattr(item,   "name", "item")))
        pname = rich_escape(str(getattr(player, "name", "?")))
        self.app.notify(
            f"{pname} equipped {iname}." if ok else f"Could not equip {iname}.",
            title="Equip",
        )
        self._rebuild_list()

    def _do_discard(self, item: Any) -> None:
        try:
            try:
                self._pg.inventory.remove(item)
                removed = True
            except (ValueError, AttributeError):
                removed = bool(self._pg.remove_single_item_unit(item))
        except Exception as exc:
            self.app.notify(f"Could not discard: {rich_escape(str(exc))}", title="Equip")
            return
        iname = rich_escape(str(getattr(item, "name", "item")))
        self.app.notify(
            f"Discarded {iname}." if removed else "Nothing was discarded.",
            title="Equip",
        )
        self._rebuild_list()

    # ── internal: party navigation ────────────────────────────────────────

    def _shift_member(self, delta: int) -> None:
        """Move the selected character index by delta, then refresh the detail panel."""
        try:
            from tui.screens.inventory_screen import InventoryScreen
            screen = self.app.screen
            if not isinstance(screen, InventoryScreen):
                return
            pg     = self._pg
            total  = len(list(getattr(pg, "characters", [])))
            if total == 0:
                return
            new_sel = max(0, min(screen._selected + delta, total - 1))
            if new_sel == screen._selected:
                return
            screen._selected = new_sel
            # keep viewport in sync
            if screen._selected < screen._offset:
                screen._offset = screen._selected
            if screen._selected >= screen._offset + 5:   # _MAX_DISPLAY = 5
                screen._offset = screen._selected - 4
            screen._refresh_cards()
        except Exception:
            return
        self._update_detail(self._highlighted_item())

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