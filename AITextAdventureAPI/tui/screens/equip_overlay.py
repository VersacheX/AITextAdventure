"""
EquipOverlay: floating equipment-management widget for InventoryScreen.

  - Filters by slot: all / weapon / head / body / arms / legs.
    Tab / Shift-Tab cycle filters.
  - List is sorted: level → total stat points → primary stat (DMG or DEF) → crit.
  - Up / Down navigate the list; Left / Right change party member.
  - Click highlights only. Enter or the Equip button opens ItemActionScreen.
  - Delete discards directly.
  - Escape closes.

Right panel — two columns:
  Left col : full item detail (name, description, type, elements, rarity,
             level, all stats, durability, value).
  Right col: selected character's equipped gear + colour-coded stat diff
             vs the highlighted item (green=better, red=worse, dim=no change).

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

_EQUIP_FILTERS: tuple[str, ...] = ("all", "weapon", "head", "body", "arms", "legs", "accessory")
_EQUIP_FILTER_LABEL: dict[str, str] = {
    "all":       "All",
    "weapon":    "Weapon",
    "head":      "Head",
    "body":      "Body",
    "arms":      "Arms",
    "legs":      "Legs",
    "accessory": "Accessory",
}

_RARITY_MARKUP: dict[str, str] = {
    "common":    "[dim]Common[/dim]",
    "uncommon":  "[cyan]Uncommon[/cyan]",
    "rare":      "[blue]Rare[/blue]",
    "superrare": "[bold magenta]Super Rare[/bold magenta]",
    "notfound":  "[dim]?[/dim]",
}


# ── sorting ───────────────────────────────────────────────────────────────────

def _total_stat_power(item: Any) -> int:
    """Derived stat: sum of all bonus stat buffs on an equipment object."""
    return sum(
        int(getattr(item, s, 0) or 0)
        for s in ("strength", "dexterity", "intelligence", "constitution")
    )


def _item_sort_key(item: Any) -> tuple:
    """Sort: level asc, TSP desc, primary stat desc (DMG or DEF), crit desc."""
    level = int(getattr(item, "min_spawn_level", 0) or 0)
    tsp   = _total_stat_power(item)
    try:
        from game.objects.weapon import Weapon
        primary = int(getattr(item, "damage",   0) or 0) if isinstance(item, Weapon) \
                  else int(getattr(item, "defense", 0) or 0)
    except Exception:
        primary = 0
    crit = float(getattr(item, "critical_chance", 0.0) or 0.0)
    return (level, -tsp, -primary, -crit)


# ── element formatting (mirrors legacy shop_menu_screen._format_elements) ─────

def _format_elements(elems: Any) -> str:
    try:
        from game.constants_other import ELEMENTAL_CHAR_KEYS
    except ImportError:
        ELEMENTAL_CHAR_KEYS = {}
    if not elems:
        return ""
    if not isinstance(elems, (list, tuple)):
        elems = [elems]
    out = ""
    for e in elems:
        if isinstance(e, dict):
            key = e.get("id") or e.get("name") or ""
        elif isinstance(e, str):
            key = e
        else:
            key = str(getattr(e, "id", getattr(e, "value", "")))
        out += ELEMENTAL_CHAR_KEYS.get(str(key).lower(), f"({key})")
    return out


# ── filter + sort ─────────────────────────────────────────────────────────────

def _apply_equip_filter(inventory: list, filter_key: str) -> list:
    try:
        from game.objects.weapon import Weapon
        from game.objects.armor import Armor, ArmorType
        from game.objects.accessory import Accessory
    except ImportError:
        return list(inventory)
    if filter_key == "all":
        items = [it for it in inventory if isinstance(it, (Weapon, Armor, Accessory))]
    elif filter_key == "weapon":
        items = [it for it in inventory if isinstance(it, Weapon)]
    elif filter_key == "accessory":
        items = [it for it in inventory if isinstance(it, Accessory)]
    else:
        slot_map: dict[str, Any] = {
            "head": ArmorType.HEAD,
            "body": ArmorType.BODY,
            "arms": ArmorType.ARMS,
            "legs": ArmorType.LEGS,
        }
        slot  = slot_map.get(filter_key)
        items = [it for it in inventory if isinstance(it, Armor) and it.slot == slot] \
                if slot else [it for it in inventory if isinstance(it, (Weapon, Armor, Accessory))]
    items.sort(key=_item_sort_key)
    return items


# ── list-row label ────────────────────────────────────────────────────────────

def _equip_item_label(item: Any) -> str:
    name       = rich_escape(str(getattr(item, "name", "?")))
    level      = int(getattr(item, "min_spawn_level", getattr(item, "min_level", 0)) or 0)
    rarity     = str(getattr(item, "rarity", "") or "")
    rarity_val = rarity.value if hasattr(rarity, "value") else str(rarity)
    elems      = getattr(item, "elements", None)
    elem_s     = _format_elements(elems)
    tsp        = _total_stat_power(item)

    stats: list[str] = []
    try:
        from game.objects.weapon import Weapon
        from game.objects.armor import Armor
        from game.objects.accessory import Accessory
        if isinstance(item, Weapon):
            dmg  = int(getattr(item, "damage", 0) or 0)
            crit = float(getattr(item, "critical_chance", 0.0) or 0)
            stats.append(f"DMG:{dmg}")
            if crit:
                stats.append(f"Crt:{crit:.0f}%")
        elif isinstance(item, Armor):
            stats.append(f"DEF:{int(getattr(item, 'defense', 0) or 0)}")
        elif isinstance(item, Accessory):
            imm = list(getattr(item, "immunities",  []) or [])
            res = list(getattr(item, "resistances", []) or [])
            wk  = list(getattr(item, "weaknesses",  []) or [])
            if imm:
                stats.append(f"Imm:{len(imm)}")
            if res:
                stats.append(f"Res:{len(res)}")
            if wk:
                stats.append(f"Wk:{len(wk)}")
            dmg_b = int(getattr(item, "damage_bonus", 0) or 0)
            crit_b = float(getattr(item, "crit_bonus", 0.0) or 0)
            if dmg_b:
                stats.append(f"+DMG:{dmg_b}")
            if crit_b:
                stats.append(f"+Crt:{crit_b:.0f}%")
    except Exception:
        pass
    if tsp:
        stats.append(f"TSP:{tsp}")

    lv_s   = f"[dim]Lv.{level}[/dim]" if level else ""
    stat_s = f"[dim]  {'  '.join(stats)}[/dim]" if stats else ""
    elem_m = f"  [yellow]{rich_escape(elem_s)}[/yellow]" if elem_s else ""

    rarity_colors = {
        "common": "", "uncommon": "cyan", "rare": "blue",
        "superrare": "magenta", "notfound": "",
    }
    color  = rarity_colors.get(rarity_val.lower(), "")
    name_m = f"[{color}]{name}[/{color}]" if color else name

    return f"{name_m}  {lv_s}{stat_s}{elem_m}"


# ── detail panels ─────────────────────────────────────────────────────────────

def _build_item_info(item: Any | None) -> str:
    """Left column: full in-game style item card."""
    if item is None:
        return "[dim]← Select an item[/dim]"

    lines: list[str] = []

    iname      = rich_escape(str(getattr(item, "name", "?")))
    rarity_raw = getattr(item, "rarity", None)
    rarity_val = rarity_raw.value if hasattr(rarity_raw, "value") else str(rarity_raw or "")
    rarity_m   = _RARITY_MARKUP.get(rarity_val.lower(), rich_escape(rarity_val))
    lines.append(f"[bold]{iname}[/bold]")
    lines.append(rarity_m)

    desc = str(getattr(item, "description", "") or getattr(item, "desc", "") or "")
    if desc:
        lines.append("")
        lines.append(f"[dim]{rich_escape(desc)}[/dim]")

    lines.append("")

    try:
        from game.objects.weapon import Weapon
        from game.objects.armor import Armor, ArmorType
        from game.objects.accessory import Accessory
        if isinstance(item, Weapon):
            dmg_type = rich_escape(str(getattr(item, "damage_type", "physical") or "physical"))
            dmg      = int(getattr(item, "damage", 0) or 0)
            crit     = float(getattr(item, "critical_chance", 0.0) or 0)
            ap_cost  = int(getattr(item, "ap_cost", 0) or 0)
            rng      = int(getattr(item, "range", 1) or 1)
            lines.append(f"[dim]── Weapon  ·  {dmg_type} ──[/dim]")
            lines.append(f"Damage      : [bold]{dmg}[/bold]")
            if crit:
                lines.append(f"Crit Chance : [yellow]{crit:.1f}%[/yellow]")
            lines.append(f"AP Cost     : {ap_cost}")
            lines.append(f"Range       : {rng}")
        elif isinstance(item, Armor):
            slot       = getattr(item, "slot", None)
            slot_label = slot.name.capitalize() if hasattr(slot, "name") else str(slot or "?")
            defense    = int(getattr(item, "defense", 0) or 0)
            lines.append(f"[dim]── Armor  ·  {slot_label} ──[/dim]")
            lines.append(f"Defense     : [bold]{defense}[/bold]")
        elif isinstance(item, Accessory):
            dmg_b  = int(getattr(item, "damage_bonus", 0) or 0)
            crit_b = float(getattr(item, "crit_bonus", 0.0) or 0)
            lines.append("[dim]── Accessory ──[/dim]")
            if dmg_b:
                lines.append(f"Damage Bonus: [bold]+{dmg_b}[/bold]")
            if crit_b:
                lines.append(f"Crit Bonus  : [yellow]+{crit_b:.1f}%[/yellow]")
            # immunities / resistances / weaknesses
            imm = list(getattr(item, "immunities",  []) or [])
            res = list(getattr(item, "resistances", []) or [])
            wk  = list(getattr(item, "weaknesses",  []) or [])
            if imm:
                lines.append(f"Immune      : [bold green]{', '.join(rich_escape(s) for s in imm)}[/bold green]")
            if res:
                lines.append(f"Resist      : [cyan]{', '.join(rich_escape(s) for s in res)}[/cyan]")
            if wk:
                lines.append(f"Weakness    : [red]{', '.join(rich_escape(s) for s in wk)}[/red]")
    except Exception:
        pass

    level = int(getattr(item, "min_spawn_level", getattr(item, "min_level", 0)) or 0)
    if level:
        lines.append(f"Req. Level  : {level}")

    # ── elements ──
    elems  = getattr(item, "elements", None)
    elem_s = _format_elements(elems)
    if elem_s:
        lines.append(f"Elements    : [yellow]{rich_escape(elem_s)}[/yellow]")

    # ── stat bonuses + TSP ──
    strength  = int(getattr(item, "strength",     0) or 0)
    dexterity = int(getattr(item, "dexterity",    0) or 0)
    intel     = int(getattr(item, "intelligence", 0) or 0)
    con       = int(getattr(item, "constitution", 0) or 0)
    tsp       = strength + dexterity + intel + con
    bonus_pairs = [(v, l) for v, l in
                   ((strength, "STR"), (dexterity, "DEX"), (intel, "INT"), (con, "CON")) if v]
    if bonus_pairs or tsp:
        lines.append("")
        lines.append(f"[dim]── Stat Bonuses  ·  [bold]TSP: {tsp}[/bold] ──[/dim]")
        for v, l in bonus_pairs:
            lines.append(f"  +{v:<4} {l}")

    # ── durability (weapons/armor only) ──
    dur     = int(getattr(item, "durability",     0) or 0)
    max_dur = int(getattr(item, "max_durability", 0) or 0)
    if max_dur:
        dur_color = "green" if dur >= max_dur * 0.6 else ("yellow" if dur >= max_dur * 0.3 else "red")
        lines.append("")
        lines.append(f"Durability  : [{dur_color}]{dur}/{max_dur}[/{dur_color}]")

    value = getattr(item, "value", None)
    if value:
        lines.append("")
        lines.append(f"[dim]Value: {value}g  |  Sell: {int(int(value) * 0.5)}g[/dim]")

    return "\n".join(lines)


def _diff_row(label: str, new_val: int | float, old_val: int | float, *,
              fmt: str = "d", higher_is_better: bool = True) -> str:
    if fmt == "f":
        val_str  = f"{float(new_val):.1f}"
        diff     = float(new_val) - float(old_val)
        diff_str = f"{diff:+.1f}"
    else:
        val_str  = str(int(new_val))
        diff     = int(new_val) - int(old_val)
        diff_str = f"{int(diff):+d}"
    if diff == 0:
        diff_markup = f"[dim]{diff_str}[/dim]"
    elif (diff > 0) == higher_is_better:
        diff_markup = f"[green]{diff_str}[/green]"
    else:
        diff_markup = f"[red]{diff_str}[/red]"
    return f"  {label}: {val_str}  {diff_markup}"


def _format_status(status: dict) -> str:
    try:
        from game.constants_other import ELEMENTAL_CHAR_KEYS
    except ImportError:
        ELEMENTAL_CHAR_KEYS = {}
    name     = rich_escape(str(status.get("name") or status.get("id") or "Status"))
    elems    = status.get("elements") or []
    elem_str = "".join(ELEMENTAL_CHAR_KEYS.get(str(e), "") for e in elems)
    turns    = status.get("turns_remaining", status.get("duration", 1))
    try:
        turns = int(turns)
    except (TypeError, ValueError):
        turns = 1
    dur_str = "perm" if turns == -1 else f"{turns}t"
    suffix  = f" {elem_str}" if elem_str else ""
    return f"{name}{suffix} [dim]({dur_str})[/dim]"


def _build_char_detail(player: Any, item: Any | None) -> str:
    """Right column: character loadout + colour-coded stat diff vs item."""
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
    accessories    = list(getattr(player, "accessories",        []) or [])
    max_acc_slots  = int(getattr(player, "max_accessory_slots", 3) or 3)

    lines.append("[dim]── Equipped ──[/dim]")
    lines.append(f"WPN:  {rich_escape(w.name    if w    else 'None')}")
    lines.append(f"HEAD: {rich_escape(head.name if head else 'None')}")
    lines.append(f"BODY: {rich_escape(body.name if body else 'None')}")
    lines.append(f"ARMS: {rich_escape(arms.name if arms else 'None')}")
    lines.append(f"LEGS: {rich_escape(legs.name if legs else 'None')}")
    # accessories
    lines.append(f"[dim]── Accessories ({len(accessories)}/{max_acc_slots}) ──[/dim]")
    if accessories:
        for acc in accessories:
            acc_name = rich_escape(str(getattr(acc, "name", "?")))
            imm_c    = len(getattr(acc, "immunities",  []) or [])
            res_c    = len(getattr(acc, "resistances", []) or [])
            wk_c     = len(getattr(acc, "weaknesses",  []) or [])
            tags: list[str] = []
            if imm_c: tags.append(f"[green]Imm:{imm_c}[/green]")
            if res_c: tags.append(f"[cyan]Res:{res_c}[/cyan]")
            if wk_c:  tags.append(f"[red]Wk:{wk_c}[/red]")
            tag_s = "  " + "  ".join(tags) if tags else ""
            lines.append(f"  ◈ {acc_name}{tag_s}  [dim](Equip→Unequip)[/dim]")
    else:
        lines.append("  [dim]None[/dim]")

    # pending points
    up_abil = int(getattr(player, "unused_ability_slots", 0) or 0)
    up_stat = int(getattr(player, "unused_stat_points",   0) or 0)
    up_pow  = int(getattr(player, "unused_power_points",  0) or 0)
    awards: list[str] = []
    if up_abil: awards.append(f"S:{up_abil}")
    if up_stat: awards.append(f"SP:{up_stat}")
    if up_pow:  awards.append(f"PP:{up_pow}")
    if awards:
        lines.append("")
        lines.append(f"[yellow]★ {'  '.join(awards)}[/yellow]")

    # statuses
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
        from game.objects.accessory import Accessory
    except ImportError:
        return "\n".join(lines)

    # ── comparison block ──
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
        lines.append(_diff_row("AP Cost",
            int(getattr(item, "ap_cost", 0) or 0),
            int(getattr(current, "ap_cost", 0) or 0) if current else 0,
            higher_is_better=False))
        for attr, short in (("strength","STR"), ("dexterity","DEX"),
                             ("intelligence","INT"), ("constitution","CON")):
            nv = int(getattr(item,    attr, 0) or 0)
            ov = int(getattr(current, attr, 0) or 0) if current else 0
            if nv or ov:
                lines.append(_diff_row(short, nv, ov))
        new_e = _format_elements(getattr(item,    "elements", None))
        old_e = _format_elements(getattr(current, "elements", None) if current else None)
        if new_e or old_e:
            lines.append(f"  Elem: [yellow]{rich_escape(new_e or '—')}[/yellow]"
                         f"  (was [dim]{rich_escape(old_e or '—')}[/dim])")

    elif isinstance(item, Armor):
        slot      = getattr(item, "slot", None)
        _slot_map: dict[Any, tuple[Any, str]] = {
            ArmorType.HEAD: (head, "HEAD"),
            ArmorType.BODY: (body, "BODY"),
            ArmorType.ARMS: (arms, "ARMS"),
            ArmorType.LEGS: (legs, "LEGS"),
        }
        current, slot_label = _slot_map.get(slot, (None, "?"))
        lines.append(f"  [dim]Slot: {slot_label}[/dim]")
        lines.append(_diff_row("DEF",
            int(getattr(item, "defense", 0) or 0),
            int(getattr(current, "defense", 0) or 0) if current else 0))
        for attr, short in (("strength","STR"), ("dexterity","DEX"),
                             ("intelligence","INT"), ("constitution","CON")):
            nv = int(getattr(item,    attr, 0) or 0)
            ov = int(getattr(current, attr, 0) or 0) if current else 0
            if nv or ov:
                lines.append(_diff_row(short, nv, ov))
        new_e = _format_elements(getattr(item,    "elements", None))
        old_e = _format_elements(getattr(current, "elements", None) if current else None)
        if new_e or old_e:
            lines.append(f"  Elem: [yellow]{rich_escape(new_e or '—')}[/yellow]"
                         f"  (was [dim]{rich_escape(old_e or '—')}[/dim])")

    elif isinstance(item, Accessory):
        slots_used = len(accessories)
        slots_free = max_acc_slots - slots_used
        already_eq = item in accessories
        if already_eq:
            lines.append("  [yellow]Equipped — press Equip to unequip[/yellow]")
        elif slots_free <= 0:
            lines.append(f"  [red]No free slots ({slots_used}/{max_acc_slots})[/red]")
        else:
            lines.append(f"  [green]Slot available ({slots_used}/{max_acc_slots}) — press Equip[/green]")
    else:
        lines.append("[dim]Not equippable[/dim]")

    return "\n".join(lines)


# ── list row ──────────────────────────────────────────────────────────────────

class _EquipRow(ListItem):
    def __init__(self, item: Any) -> None:
        super().__init__(Label(_equip_item_label(item)))
        self.item = item


# ── overlay widget ────────────────────────────────────────────────────────────

class EquipOverlay(Widget):
    """
    Floating equipment picker docked to the bottom of InventoryScreen.

    Tab / Shift-Tab cycle slot filters. List sorted by level → stats → primary → crit.
    Left / Right change party member. Click highlights; Enter/Equip opens modal.
    Delete discards. Escape closes.
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
                    yield Button("Equip",   id="eq-btn-equip",   variant="primary", disabled=True)
                    yield Button("Discard", id="eq-btn-discard", variant="error",   disabled=True)
        yield Static(
            "[dim]Enter/Equip:equip  Del/Discard:discard  Tab/⇧Tab:filter  ◄►:member  Esc:close[/dim]",
            id="eq-hint",
        )

    def on_mount(self) -> None:
        self.add_class("inv-overlay")
        self._rebuild_list()
        self.query_one("#eq-list", ListView).focus()

    # ── public API called by InventoryScreen ──────────────────────────────

    def on_player_changed(self, player: Any) -> None:
        self._update_detail(self._highlighted_item())

    # ── filter helpers ────────────────────────────────────────────────────

    @property
    def _current_filter(self) -> str:
        return _EQUIP_FILTERS[self._filter_idx]

    def _filter_bar_text(self) -> str:
        parts: list[str] = []
        for i, key in enumerate(_EQUIP_FILTERS):
            label = _EQUIP_FILTER_LABEL[key]
            parts.append(
                f"[bold reverse] {label} [/bold reverse]"
                if i == self._filter_idx
                else f"[dim] {label} [/dim]"
            )
        return "  ".join(parts)

    def _filtered_equipment(self) -> list:
        inv = list(getattr(self._pg, "inventory", []) or [])
        return _apply_equip_filter(inv, self._current_filter)

    def _rebuild_list(self) -> None:
        lv    = self.query_one("#eq-list", ListView)
        lv.clear()
        items = self._filtered_equipment()
        for item in items:
            lv.append(_EquipRow(item))
        self.query_one("#eq-filter-bar", Static).update(self._filter_bar_text())
        filt  = _EQUIP_FILTER_LABEL[self._current_filter]
        self.query_one("#eq-header", Static).update(
            f"── Equip ({len(items)}) · sorted: level/stats/primary/crit · filter: {filt} ──"
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
        """Mouse click — highlight only, do not open modal.
        Keyboard Enter is handled by action_open_action (bound via BINDINGS).
        """
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
            elif result == "unequip":
                self._do_unequip_accessory(item, player)
            elif result == "discard":
                self._do_discard(item)

        self.app.push_screen(ItemActionScreen(item, player, self._pg), _handle)

    # ── internal: actions ─────────────────────────────────────────────────

    def _do_equip(self, item: Any, player: Any) -> None:
        try:
            from game.objects.weapon import Weapon
            from game.objects.armor import Armor
            from game.objects.accessory import Accessory
            if isinstance(item, Weapon):
                ok = player.equip_weapon(self._pg, item)
            elif isinstance(item, Armor):
                ok = player.equip_armor(self._pg, item)
            elif isinstance(item, Accessory):
                # Push slot-picker — it handles replace confirmation internally
                from tui.screens.accessory_slot_screen import AccessorySlotScreen  # noqa: PLC0415

                def _on_slot_chosen(slot_index: int | None) -> None:
                    if slot_index is None:
                        return
                    ok = player.equip_accessory(self._pg, item)
                    if ok:
                        iname = rich_escape(str(getattr(item,   "name", "item")))
                        pname = rich_escape(str(getattr(player, "name", "?")))
                        self.app.notify(f"{pname} equipped {iname}.", title="Equip")
                    else:
                        self.app.notify("Could not equip accessory.", title="Equip")
                    self._rebuild_list()

                self.app.push_screen(
                    AccessorySlotScreen(item, player, self._pg),
                    _on_slot_chosen,
                )
                return
            else:
                ok = None
            if ok is None:
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

    def _do_unequip_accessory(self, item: Any, player: Any) -> None:
        """Remove an equipped accessory back to the shared inventory."""
        try:
            ok = player.unequip_accessory(self._pg, item)
        except Exception as exc:
            self.app.notify(f"Error unequipping: {rich_escape(str(exc))}", title="Equip")
            return
        iname = rich_escape(str(getattr(item,   "name", "item")))
        pname = rich_escape(str(getattr(player, "name", "?")))
        self.app.notify(
            f"{pname} unequipped {iname}." if ok else f"Could not unequip {iname}.",
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
        try:
            from tui.screens.inventory_screen import InventoryScreen
            screen = self.app.screen
            if not isinstance(screen, InventoryScreen):
                return
            total   = len(list(getattr(self._pg, "characters", [])))
            if total == 0:
                return
            new_sel = max(0, min(screen._selected + delta, total - 1))
            if new_sel == screen._selected:
                return
            screen._selected = new_sel
            if screen._selected < screen._offset:
                screen._offset = screen._selected
            if screen._selected >= screen._offset + 5:
                screen._offset = screen._selected - 4
            screen._refresh_cards()
        except Exception:
            return
        self._update_detail(self._highlighted_item())

    def _resolve_player(self) -> Any | None:
        try:
            from tui.screens.inventory_screen import InventoryScreen
            screen  = self.app.screen
            if not isinstance(screen, InventoryScreen):
                return None
            players = list(getattr(self._pg, "characters", []))
            idx     = screen._selected
            return players[idx] if 0 <= idx < len(players) else None
        except Exception:
            return None