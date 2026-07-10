"""
ShopOverlay: buy / sell screen for weapon, armor, utility, inn, and bar shops.

Mirrors `old/game_screens/shop_menu_screen.py` and delegates to the legacy
shop services (weapon_shop_service, armor_shop_service, utility_shop_service)
plus inn_service and bar_service.

Architecture
────────────
- TabbedContent with BUY and SELL tabs (inn/bar render only BUY).
- BUY tab: list of shop stock + right-hand detail panel.
- SELL tab: list of player's sellable items with owned qty shown; the detail
  panel shows item stats, owned count, a ×qty stepper, and a Sell button.
- Selecting a buy row or pressing Sell on the sell side opens ConfirmScreen.
- Gold updates live after every transaction.
- CSS class "ow-overlay" suppresses the LocationOverlay while this is open.
"""
from __future__ import annotations

from typing import Any, Callable, List

from rich.markup import escape as rich_escape
from textual import on
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widget import Widget
from textual.widgets import Button, Label, ListItem, ListView, Static, TabbedContent, TabPane
from textual import events


# ── shop-type helpers ─────────────────────────────────────────────────────────

def _detect_shop_type(business_def: dict) -> str:
    return str(business_def.get("name", "shopitems")).lower()


def _shop_has_sell(shop_type: str) -> bool:
    return shop_type in ("shopweapons", "shoparmor", "shopitems")


# ── stock loading ─────────────────────────────────────────────────────────────

def _load_stock(shop_type: str, pg: Any, region: Any) -> List[Any]:
    level = 1
    try:
        level = pg.get_max_character_level()
    except Exception:
        pass
    try:
        if shop_type == "shopweapons":
            from services.weapon_shop_service import get_stock  # noqa: PLC0415
            return get_stock(level, region)
        if shop_type == "shoparmor":
            from services.armor_shop_service import get_stock  # noqa: PLC0415
            return get_stock(level, region)
        if shop_type == "shopitems":
            from services.utility_shop_service import get_stock  # noqa: PLC0415
            return get_stock(level, region)
        if shop_type == "inn":
            from services.inn_service import get_stock  # noqa: PLC0415
            return get_stock(level, pg, region)
        if shop_type == "bar":
            from services.bar_service import get_stock  # noqa: PLC0415
            return get_stock(level, pg, region)
    except Exception:
        pass
    return []


def _load_sell_stock(shop_type: str, pg: Any) -> List[Any]:
    """Return player inventory items that this shop will buy.
    SpecialItem instances are never sellable anywhere.
    """
    inv = list(getattr(pg, "inventory", []) or [])
    if not inv:
        return []
    try:
        from game.objects.special_item import SpecialItem  # noqa: PLC0415
        from game.objects.weapon import Weapon              # noqa: PLC0415
        from game.objects.armor import Armor                # noqa: PLC0415
        if shop_type == "shopweapons":
            return [i for i in inv if isinstance(i, Weapon) and not isinstance(i, SpecialItem)]
        if shop_type == "shoparmor":
            return [i for i in inv if isinstance(i, Armor) and not isinstance(i, SpecialItem)]
        if shop_type == "shopitems":
            return [i for i in inv if not isinstance(i, (Weapon, Armor, SpecialItem))]
    except Exception:
        pass
    return [i for i in inv if not _is_special(i)]


def _is_special(item: Any) -> bool:
    """Fallback check when SpecialItem can't be imported."""
    try:
        from game.objects.special_item import SpecialItem  # noqa: PLC0415
        return isinstance(item, SpecialItem)
    except Exception:
        return False


# ── display helpers ───────────────────────────────────────────────────────────

def _buy_label(item: Any) -> str:
    if isinstance(item, dict):
        name  = rich_escape(str(item.get("name", "?")))
        price = item.get("value", 0)
        return f"{name}  [dim]{price}g[/dim]"
    name  = rich_escape(str(getattr(item, "name", "?")))
    price = getattr(item, "value", 0)
    return f"{name}  [dim]{price}g[/dim]"


def _sell_label(item: Any) -> str:
    name       = rich_escape(str(getattr(item, "name", "?")))
    sell_price = int(getattr(item, "value", 0) * 0.5)
    owned      = int(getattr(item, "quantity", 1) or 1)
    qty_str    = f" ×{owned}" if owned > 1 else ""
    return f"{name}{qty_str}  [dim]+{sell_price}g ea[/dim]"


def _item_detail(item: Any) -> str:
    if item is None:
        return "[dim]Select an item.[/dim]"
    if isinstance(item, dict):
        lines = [f"[bold]{rich_escape(str(item.get('name', '?')))}[/bold]"]
        desc  = item.get("description") or item.get("desc", "")
        if desc:
            lines.append(rich_escape(str(desc)))
        lines.append(f"Cost: {item.get('value', 0)}g")
        frac = item.get("heal_fraction") or item.get("hp_fraction")
        if frac:
            lines.append(f"Restores {int(float(frac)*100)}% HP")
        ap_frac = item.get("ap_fraction")
        if ap_frac:
            lines.append(f"Restores {int(float(ap_frac)*100)}% AP")
        return "\n".join(lines)

    lines = [f"[bold]{rich_escape(str(getattr(item, 'name', '?')))}[/bold]"]
    desc  = getattr(item, "description", "") or getattr(item, "desc", "")
    if desc:
        lines.append(rich_escape(str(desc)))
    price = getattr(item, "value", 0)
    lines.append(f"Cost: {price}g  |  Sell: {int(price * 0.5)}g ea")
    for attr, lbl in (
        ("damage",          "DMG"),
        ("critical_chance", "CRIT%"),
        ("defense",         "DEF"),
        ("strength",        "STR"),
        ("dexterity",       "DEX"),
        ("intelligence",    "INT"),
        ("constitution",    "CON"),
        ("durability",      "DUR"),
    ):
        v = getattr(item, attr, None)
        if v:
            lines.append(f"{lbl}: {v}")
    slot = getattr(item, "slot", None)
    if slot:
        lines.append(f"Slot: {slot.name if hasattr(slot, 'name') else slot}")
    return "\n".join(lines)


# ── party stat comparison ─────────────────────────────────────────────────────

_COMPARE_ATTRS = [
    ("damage",          "DMG"),
    ("defense",         "DEF"),
    ("strength",        "STR"),
    ("dexterity",       "DEX"),
    ("intelligence",    "INT"),
    ("constitution",    "CON"),
    ("critical_chance", "CRIT%"),
    ("durability",      "DUR"),
]


def _get_equipped_stat(char: Any, slot: Any, attr: str) -> int:
    """Return the value of `attr` on the item currently equipped in `slot`."""
    try:
        equipped = None
        # Try equipment dict first, then individual slot attributes
        equipment = getattr(char, "equipment", None)
        if isinstance(equipment, dict):
            slot_key = slot.name if hasattr(slot, "name") else str(slot)
            equipped = equipment.get(slot_key)
        if equipped is None:
            slot_key = slot.name if hasattr(slot, "name") else str(slot)
            equipped = getattr(char, slot_key.lower(), None)
        if equipped is None:
            return 0
        return int(getattr(equipped, attr, 0) or 0)
    except Exception:
        return 0


def _party_stat_comparison(item: Any, pg: Any) -> str:
    """Return a Rich-markup string showing per-character stat deltas."""
    if item is None or isinstance(item, dict):
        return ""
    slot = getattr(item, "slot", None)
    if slot is None:
        return ""

    try:
        party = pg.get_active_party()
    except Exception:
        return ""
    if not party:
        return ""

    # Collect which attrs this item actually has values for
    relevant = [(attr, lbl) for attr, lbl in _COMPARE_ATTRS if getattr(item, attr, None)]
    if not relevant:
        return ""

    lines: List[str] = ["[dim]─ Party comparison ─[/dim]"]
    for char in party:
        name = rich_escape(str(getattr(char, "name", "?")))
        delta_parts: List[str] = []
        for attr, lbl in relevant:
            new_val = int(getattr(item, attr, 0) or 0)
            cur_val = _get_equipped_stat(char, slot, attr)
            diff = new_val - cur_val
            if diff > 0:
                delta_parts.append(f"[green]+{diff} {lbl}[/green]")
            elif diff < 0:
                delta_parts.append(f"[red]{diff} {lbl}[/red]")
            else:
                delta_parts.append(f"[dim]±0 {lbl}[/dim]")
        lines.append(f"[bold]{name}[/bold]: " + "  ".join(delta_parts))

    return "\n".join(lines)


# ── party stat comparison ─────────────────────────────────────────────────────

_COMPARE_ATTRS = [
    ("damage",          "DMG"),
    ("defense",         "DEF"),
    ("strength",        "STR"),
    ("dexterity",       "DEX"),
    ("intelligence",    "INT"),
    ("constitution",    "CON"),
    ("critical_chance", "CRIT%"),
    ("durability",      "DUR"),
]


def _get_equipped_stat(char: Any, slot: Any, attr: str) -> int:
    """Return the value of `attr` on the item currently equipped in `slot`."""
    try:
        equipped = None
        # Try equipment dict first, then individual slot attributes
        equipment = getattr(char, "equipment", None)
        if isinstance(equipment, dict):
            slot_key = slot.name if hasattr(slot, "name") else str(slot)
            equipped = equipment.get(slot_key)
        if equipped is None:
            slot_key = slot.name if hasattr(slot, "name") else str(slot)
            equipped = getattr(char, slot_key.lower(), None)
        if equipped is None:
            return 0
        return int(getattr(equipped, attr, 0) or 0)
    except Exception:
        return 0


def _party_stat_comparison(item: Any, pg: Any) -> str:
    """Return a Rich-markup string showing per-character stat deltas."""
    if item is None or isinstance(item, dict):
        return ""
    slot = getattr(item, "slot", None)
    if slot is None:
        return ""

    try:
        party = pg.get_active_party()
    except Exception:
        return ""
    if not party:
        return ""

    # Collect which attrs this item actually has values for
    relevant = [(attr, lbl) for attr, lbl in _COMPARE_ATTRS if getattr(item, attr, None)]
    if not relevant:
        return ""

    lines: List[str] = ["[dim]─ Party comparison ─[/dim]"]
    for char in party:
        name = rich_escape(str(getattr(char, "name", "?")))
        delta_parts: List[str] = []
        for attr, lbl in relevant:
            new_val = int(getattr(item, attr, 0) or 0)
            cur_val = _get_equipped_stat(char, slot, attr)
            diff = new_val - cur_val
            if diff > 0:
                delta_parts.append(f"[green]+{diff} {lbl}[/green]")
            elif diff < 0:
                delta_parts.append(f"[red]{diff} {lbl}[/red]")
            else:
                delta_parts.append(f"[dim]±0 {lbl}[/dim]")
        lines.append(f"[bold]{name}[/bold]: " + "  ".join(delta_parts))

    return "\n".join(lines)


# ── list-item widget ──────────────────────────────────────────────────────────

class _ShopItem(ListItem):
    def __init__(self, item: Any, *, selling: bool = False) -> None:
        label = _sell_label(item) if selling else _buy_label(item)
        super().__init__(Label(label))
        self.item    = item
        self.selling = selling


# ── overlay ───────────────────────────────────────────────────────────────────

class ShopOverlay(Widget):
    """Floating shop widget with Buy / Sell tabs overlaid on the map."""

    can_focus = True

    BINDINGS = [
        Binding("escape", "close", "Close", show=True),
    ]

    DEFAULT_CSS = """
    ShopOverlay {
        layer: overlay;
        width: 72;
        height: auto;
        max-height: 34;
        offset: 2 2;
        background: $surface;
        border: round $accent;
    }

    #shop-title-bar {
        height: 1;
        background: $boost;
        width: 100%;
    }

    #shop-title {
        width: 1fr;
        text-align: center;
        text-style: bold;
        padding: 0 1;
    }

    #shop-close-x {
        width: 3;
        min-width: 3;
        height: 1;
        border: none;
        color: $error;
        background: $boost;
    }

    #shop-gold {
        text-align: center;
        color: $success;
        padding: 0 1;
    }

    #shop-tabs {
        height: auto;
        max-height: 28;
    }

    ShopOverlay TabPane {
        padding: 0;
    }

    #shop-buy-row, #shop-sell-row {
        height: auto;
        max-height: 22;
    }

    #buy-list-col, #sell-list-col {
        width: 1fr;
        height: auto;
        max-height: 22;
    }

    #buy-list, #sell-list {
        height: auto;
        max-height: 18;
    }

    #buy-detail-col, #sell-detail-col {
        width: 30;
        height: auto;
        max-height: 22;
        border-left: solid $accent 30%;
        padding: 1;
    }

    #buy-detail, #sell-detail {
        height: auto;
    }

    #sell-owned {
        height: 1;
        margin-top: 1;
        color: $text 60%;
    }

    #sell-qty-row {
        height: 3;
        margin-top: 1;
        align: left middle;
    }

    #sell-qty-dec, #sell-qty-inc {
        min-width: 3;
        width: 3;
        height: 1;
        border: none;
    }

    #sell-qty-display {
        width: 4;
        text-align: center;
        content-align: center middle;
    }

    #sell-btn {
        width: 100%;
        margin-top: 1;
    }

    #shop-close {
        width: 100%;
        height: 1;
        border-top: solid $accent 50%;
    }
    """

    def __init__(
        self,
        pg: Any,
        business_def: dict,
        region: Any,
        on_done: Callable[[bool], None],
    ) -> None:
        super().__init__()
        self._pg           = pg
        self._business_def = business_def
        self._region       = region
        self._on_done      = on_done
        self._shop_type    = _detect_shop_type(business_def)
        self._stock:       List[Any] = []
        self._sell_stock:  List[Any] = []
        self._acted        = False
        self._sell_item:   Any | None = None
        self._sell_qty:    int = 1

    # ── compose ───────────────────────────────────────────────────────────────

    def compose(self) -> ComposeResult:
        name     = self._business_def.get("display_name") or self._business_def.get("name", "Shop")
        has_sell = _shop_has_sell(self._shop_type)

        with Vertical():
            with Horizontal(id="shop-title-bar"):
                yield Static(f"── {rich_escape(str(name))} ──", id="shop-title")
                yield Button("✕", id="shop-close-x", variant="default")
            yield Static(f"Gold: {getattr(self._pg, 'money', 0)}", id="shop-gold")
            with TabbedContent(id="shop-tabs"):
                with TabPane("Buy", id="tab-buy"):
                    with Horizontal(id="shop-buy-row"):
                        with Vertical(id="buy-list-col"):
                            yield ListView(id="buy-list")
                        with Vertical(id="buy-detail-col"):
                            yield Static("[dim]Select an item.[/dim]", id="buy-detail")
                if has_sell:
                    with TabPane("Sell", id="tab-sell"):
                        with Horizontal(id="shop-sell-row"):
                            with Vertical(id="sell-list-col"):
                                yield ListView(id="sell-list")
                            with Vertical(id="sell-detail-col"):
                                yield Static("[dim]Select an item to sell.[/dim]", id="sell-detail")
                                yield Static("", id="sell-owned")
                                with Horizontal(id="sell-qty-row"):
                                    yield Button("−", id="sell-qty-dec", variant="default")
                                    yield Static("1", id="sell-qty-display")
                                    yield Button("+", id="sell-qty-inc", variant="default")
                                yield Button("Sell", id="sell-btn", variant="primary", disabled=True)

    def on_mount(self) -> None:
        self.add_class("ow-overlay")
        self.focus()
        self._stock      = _load_stock(self._shop_type, self._pg, self._region)
        self._sell_stock = _load_sell_stock(self._shop_type, self._pg) if _shop_has_sell(self._shop_type) else []
        self._rebuild_buy_list()
        self._rebuild_sell_list()

    def on_key(self, event: events.Key) -> None:
        """Block overworld movement keys. Handle Escape directly.
        All other keys (Tab, Enter, etc.) pass through to child widgets.
        """
        _OVERWORLD_KEYS = {
            "w", "a", "s", "d",
            "up", "down", "left", "right",
            "i", "t",
        }
        if event.key == "escape":
            event.stop()
            self.action_close()
        elif event.key in _OVERWORLD_KEYS:
            event.stop()

    @on(Button.Pressed, "#shop-close-x")
    def _on_close_x(self) -> None:
        self.action_close()

    def action_close(self) -> None:
        self.remove_class("ow-overlay")
        self.remove()
        self._on_done(self._acted)

    # ── list population ───────────────────────────────────────────────────────

    def _rebuild_buy_list(self) -> None:
        try:
            lv = self.query_one("#buy-list", ListView)
            lv.clear()
            for item in self._stock:
                lv.append(_ShopItem(item, selling=False))
        except Exception:
            pass

    def _rebuild_sell_list(self) -> None:
        try:
            lv = self.query_one("#sell-list", ListView)
            lv.clear()
            for item in self._sell_stock:
                lv.append(_ShopItem(item, selling=True))
        except Exception:
            pass

    # ── gold display ──────────────────────────────────────────────────────────

    def _refresh_gold(self) -> None:
        try:
            self.query_one("#shop-gold", Static).update(
                f"Gold: {getattr(self._pg, 'money', 0)}"
            )
        except Exception:
            pass

    # ── buy detail ────────────────────────────────────────────────────────────

    @on(ListView.Highlighted, "#buy-list")
    def _on_buy_highlighted(self, event: ListView.Highlighted) -> None:
        item = event.item.item if isinstance(event.item, _ShopItem) else None
        try:
            self.query_one("#buy-detail", Static).update(_item_detail(item))
        except Exception:
            pass

    # ── sell detail + qty stepper ─────────────────────────────────────────────

    @on(ListView.Highlighted, "#sell-list")
    def _on_sell_highlighted(self, event: ListView.Highlighted) -> None:
        self._sell_item = event.item.item if isinstance(event.item, _ShopItem) else None
        self._sell_qty  = 1
        self._refresh_sell_panel()

    def _refresh_sell_panel(self) -> None:
        item = self._sell_item
        try:
            self.query_one("#sell-detail", Static).update(_item_detail(item))
        except Exception:
            pass
        try:
            if item is not None:
                owned = int(getattr(item, "quantity", 1) or 1)
                self.query_one("#sell-owned",       Static).update(f"Owned: {owned}")
                self.query_one("#sell-qty-display", Static).update(str(self._sell_qty))
                self.query_one("#sell-qty-dec",  Button).disabled = (self._sell_qty <= 1)
                self.query_one("#sell-qty-inc",  Button).disabled = (self._sell_qty >= owned)
                self.query_one("#sell-btn",      Button).disabled = False
            else:
                self.query_one("#sell-owned",       Static).update("")
                self.query_one("#sell-qty-display", Static).update("1")
                self.query_one("#sell-qty-dec",  Button).disabled = True
                self.query_one("#sell-qty-inc",  Button).disabled = True
                self.query_one("#sell-btn",      Button).disabled = True
        except Exception:
            pass

    @on(Button.Pressed, "#sell-qty-dec")
    def _on_qty_dec(self) -> None:
        if self._sell_item is None or self._sell_qty <= 1:
            return
        self._sell_qty -= 1
        self._refresh_sell_panel()

    @on(Button.Pressed, "#sell-qty-inc")
    def _on_qty_inc(self) -> None:
        if self._sell_item is None:
            return
        owned = int(getattr(self._sell_item, "quantity", 1) or 1)
        if self._sell_qty >= owned:
            return
        self._sell_qty += 1
        self._refresh_sell_panel()

    @on(Button.Pressed, "#sell-btn")
    def _on_sell_btn(self) -> None:
        if self._sell_item is not None:
            self._do_sell(self._sell_item, self._sell_qty)

    # ── buy flow ──────────────────────────────────────────────────────────────

    @on(ListView.Selected, "#buy-list")
    def _on_buy_selected(self, event: ListView.Selected) -> None:
        if isinstance(event.item, _ShopItem):
            self._do_buy(event.item.item)

    def _do_buy(self, item: Any) -> None:
        price = item.get("value", 0) if isinstance(item, dict) else getattr(item, "value", 0)
        name  = item.get("name", "?") if isinstance(item, dict) else getattr(item, "name", "?")
        money = getattr(self._pg, "money", 0)

        if money < price:
            self.app.notify(
                f"You need {price}g. You have {money}g.",
                title="Insufficient Funds",
                severity="warning",
            )
            return

        def _on_confirmed(confirmed: bool | None) -> None:
            if not confirmed:
                return
            try:
                result = self._execute_buy(item)
            except Exception as exc:
                self.app.notify(str(exc), title="Purchase Error", severity="error")
                return
            if result.get("success"):
                self._acted = True
                self.app.notify(f"Bought {rich_escape(str(name))}!", title="Purchased", timeout=2)
                self._refresh_gold()
                if _shop_has_sell(self._shop_type):
                    self._sell_stock = _load_sell_stock(self._shop_type, self._pg)
                    self._rebuild_sell_list()
            else:
                err = result.get("error", "unknown_error")
                if err == "insufficient_funds":
                    self.app.notify("Not enough gold.", title="Purchase Failed", severity="warning")
                elif err == "inventory_full":
                    self.app.notify("Your inventory is full.", title="Purchase Failed", severity="warning")
                else:
                    self.app.notify(f"Purchase failed: {err}", severity="error")

        from tui.screens.confirm_screen import ConfirmScreen  # noqa: PLC0415
        self.app.push_screen(
            ConfirmScreen(
                f"Buy {rich_escape(str(name))} for {price}g?",
                yes_label="Buy",
                no_label="Cancel",
            ),
            _on_confirmed,
        )

    def _execute_buy(self, item: Any) -> dict:
        try:
            if self._shop_type == "shopweapons":
                from services.weapon_shop_service import buy  # noqa: PLC0415
                return buy(self._pg, item)
            if self._shop_type == "shoparmor":
                from services.armor_shop_service import buy  # noqa: PLC0415
                return buy(self._pg, item)
            if self._shop_type == "shopitems":
                from services.utility_shop_service import buy  # noqa: PLC0415
                return buy(self._pg, item)
            if self._shop_type == "inn":
                from services.inn_service import buy  # noqa: PLC0415
                return buy(self._pg, item)
            if self._shop_type == "bar":
                from services.bar_service import buy  # noqa: PLC0415
                return buy(self._pg, item)
        except Exception as exc:
            return {"success": False, "error": str(exc)}
        return {"success": False, "error": "unsupported_shop_type"}

    # ── sell flow ─────────────────────────────────────────────────────────────

    def _do_sell(self, item: Any, qty: int = 1) -> None:
        name       = rich_escape(str(getattr(item, "name", "?")))
        unit_price = int(getattr(item, "value", 0) * 0.5)
        total      = unit_price * qty
        qty_str    = f"{qty}× " if qty > 1 else ""

        def _on_confirmed(confirmed: bool | None) -> None:
            if not confirmed:
                return
            success_count = 0
            for _ in range(qty):
                try:
                    if self._shop_type == "shopweapons":
                        from services.weapon_shop_service import sell  # noqa: PLC0415
                        result = sell(self._pg, item)
                    elif self._shop_type == "shoparmor":
                        from services.armor_shop_service import sell  # noqa: PLC0415
                        result = sell(self._pg, item)
                    else:
                        from services.utility_shop_service import sell  # noqa: PLC0415
                        result = sell(self._pg, item)
                    if result.get("success"):
                        success_count += 1
                    else:
                        break
                except Exception:
                    break

            if success_count > 0:
                self._acted = True
                earned = unit_price * success_count
                self.app.notify(
                    f"Sold {qty_str}{name} for {earned}g.",
                    title="Sold",
                    timeout=2,
                )
                self._sell_stock = _load_sell_stock(self._shop_type, self._pg)
                self._sell_item  = None
                self._sell_qty   = 1
                self._rebuild_sell_list()
                self._refresh_sell_panel()
                self._refresh_gold()
            else:
                self.app.notify("Could not sell that item.", severity="warning")

        from tui.screens.confirm_screen import ConfirmScreen  # noqa: PLC0415
        self.app.push_screen(
            ConfirmScreen(
                f"Sell {qty_str}{name} for {total}g?",
                yes_label="Sell",
                no_label="Cancel",
            ),
            _on_confirmed,
        )

    # ── close ─────────────────────────────────────────────────────────────────

    @on(Button.Pressed, "#shop-close")
    def _on_close_btn(self) -> None:
        self.action_close()

    def action_close(self) -> None:
        self.remove_class("ow-overlay")
        self.remove()
        self._on_done(self._acted)