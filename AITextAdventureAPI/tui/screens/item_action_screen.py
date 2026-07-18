"""
ItemActionScreen: modal popup shown when the player presses Enter or clicks
an item in the Items or Equip overlays.

Displays:
  - Item name, type tag and short description.
  - For equipment (Weapon / Armor): a stat diff vs. the character's current
    item in that slot — green for improvements, red for regressions.
  - For accessories: slot availability, stat bonuses, and immunity/resistance/weakness.
  - Action buttons appropriate to the item type:
      Equip / Unequip / Use (depending on type) · Discard · Cancel

Callers push this screen with a result callback and receive an
`ItemActionResult` string: "equip", "unequip", "use", "discard", or None for cancel.
"""
from __future__ import annotations

from typing import Any

from rich.markup import escape as rich_escape
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Static

from tui.screens.base_screen import BaseScreen


ItemActionResult = str | None  # "equip" | "unequip" | "use" | "discard" | None


def _stat_diff_markup(player: Any, item: Any) -> str:
    """Build Rich markup showing the stat comparison between *item* and the
    player's currently equipped item in the same slot.

    Returns an empty string for accessories or items with no comparable stats.
    """
    lines: list[str] = []

    def _diff(label: str, nv: int | float, ov: int | float, fmt: str = "d") -> str:
        if fmt == "f":
            diff  = float(nv) - float(ov)
            diff_s = f"{diff:+.1f}"
            val_s  = f"{float(nv):.1f}"
        else:
            diff  = int(nv) - int(ov)
            diff_s = f"{int(diff):+d}"
            val_s  = str(int(nv))
        if diff > 0:
            diff_m = f"[green]{diff_s}[/green]"
        elif diff < 0:
            diff_m = f"[red]{diff_s}[/red]"
        else:
            diff_m = f"[dim]{diff_s}[/dim]"
        return f"  {label}: {val_s}  {diff_m}"

    try:
        from game.objects.weapon import Weapon
        from game.objects.armor import Armor, ArmorType
    except ImportError:
        return ""

    if isinstance(item, Weapon):
        current = getattr(player, "equipped_weapon", None)
        lines.append("[dim]vs current weapon[/dim]")
        lines.append(_diff("DMG",
            int(getattr(item,    "damage", 0) or 0),
            int(getattr(current, "damage", 0) or 0) if current else 0))
        lines.append(_diff("Crit%",
            float(getattr(item,    "critical_chance", 0.0) or 0),
            float(getattr(current, "critical_chance", 0.0) or 0) if current else 0.0,
            "f"))
        for attr, short in (("strength","STR"), ("dexterity","DEX"),
                             ("intelligence","INT"), ("constitution","CON")):
            nv = int(getattr(item,    attr, 0) or 0)
            ov = int(getattr(current, attr, 0) or 0) if current else 0
            if nv or ov:
                lines.append(_diff(short, nv, ov))

    elif isinstance(item, Armor):
        slot = getattr(item, "slot", None)
        slot_attr_map = {
            ArmorType.HEAD: ("head_armor", "HEAD"),
            ArmorType.BODY: ("body_armor", "BODY"),
            ArmorType.ARMS: ("arm_armor",  "ARMS"),
            ArmorType.LEGS: ("leg_armor",  "LEGS"),
        }
        attr_name, slot_label = slot_attr_map.get(slot, (None, "?"))
        current = getattr(player, attr_name, None) if attr_name else None
        lines.append(f"[dim]vs current {slot_label}[/dim]")
        lines.append(_diff("DEF",
            int(getattr(item,    "defense", 0) or 0),
            int(getattr(current, "defense", 0) or 0) if current else 0))
        for attr, short in (("strength","STR"), ("dexterity","DEX"),
                             ("intelligence","INT"), ("constitution","CON")):
            nv = int(getattr(item,    attr, 0) or 0)
            ov = int(getattr(current, attr, 0) or 0) if current else 0
            if nv or ov:
                lines.append(_diff(short, nv, ov))

    return "\n".join(lines)


def _accessory_detail_markup(player: Any, item: Any) -> str:
    """Build Rich markup showing accessory slot state, stat bonuses, and
    elemental/status effects for the detail panel."""
    lines: list[str] = []

    accessories = list(getattr(player, "accessories",        []) or [])
    max_slots   = int(getattr(player, "max_accessory_slots", 3) or 3)
    slots_used  = len(accessories)

    if slots_used >= max_slots:
        lines.append(f"[yellow]All slots full  ({slots_used}/{max_slots}) — equip to replace[/yellow]")
    else:
        lines.append(f"[green]Slot available  ({slots_used}/{max_slots} used)[/green]")

    lines.append("")

    for attr, label in (("strength","STR"), ("dexterity","DEX"),
                         ("intelligence","INT"), ("constitution","CON")):
        v = int(getattr(item, attr, 0) or 0)
        if v:
            lines.append(f"  [green]+{v}[/green] {label}")

    dmg_b  = int(getattr(item, "damage_bonus", 0) or 0)
    crit_b = float(getattr(item, "crit_bonus", 0.0) or 0)
    if dmg_b:
        lines.append(f"  [green]+{dmg_b}[/green] Damage")
    if crit_b:
        lines.append(f"  [green]+{crit_b:.1f}%[/green] Crit")

    imm = list(getattr(item, "immunities",  []) or [])
    res = list(getattr(item, "resistances", []) or [])
    wk  = list(getattr(item, "weaknesses",  []) or [])
    if imm:
        lines.append(f"  Immune : [bold green]{', '.join(rich_escape(s) for s in imm)}[/bold green]")
    if res:
        lines.append(f"  Resist : [cyan]{', '.join(rich_escape(s) for s in res)}[/cyan]")
    if wk:
        lines.append(f"  Weak   : [red]{', '.join(rich_escape(s) for s in wk)}[/red]")

    return "\n".join(lines)


def _item_type_tag(item: Any) -> str:
    try:
        from game.objects.weapon import Weapon
        from game.objects.armor import Armor, ArmorType
        from game.objects.utility_item import UtilityItem
        from game.objects.special_item import SpecialItem
        from game.objects.accessory import Accessory
        if isinstance(item, Weapon):
            return "Weapon"
        if isinstance(item, Armor):
            slot = getattr(item, "slot", None)
            names = {
                ArmorType.HEAD: "Head Armor",
                ArmorType.BODY: "Body Armor",
                ArmorType.ARMS: "Arms Armor",
                ArmorType.LEGS: "Legs Armor",
            }
            return names.get(slot, "Armor")
        if isinstance(item, Accessory):
            rarity_raw = getattr(item, "rarity", "")
            rarity_val = rarity_raw.value if hasattr(rarity_raw, "value") else str(rarity_raw or "")
            return f"Accessory  [{rarity_val.capitalize()}]" if rarity_val else "Accessory"
        if isinstance(item, UtilityItem):
            eff = getattr(item, "effect", None)
            return f"Utility  [{eff}]" if eff else "Utility"
        if isinstance(item, SpecialItem):
            return "Special"
    except Exception:
        pass
    return "Item"


def _is_accessory(item: Any) -> bool:
    """Return True if item is an Accessory instance without raising."""
    try:
        from game.objects.accessory import Accessory
        return isinstance(item, Accessory)
    except Exception:
        return False


class ItemActionScreen(BaseScreen):
    """
    Modal that presents equip / unequip / use / discard options for a single item.

    Push with a result callback:

        def _handle(result: ItemActionResult) -> None:
            if result == "equip":    ...
            elif result == "unequip": ...
            elif result == "use":    ...
            elif result == "discard": ...

        self.app.push_screen(ItemActionScreen(item, player, player_game), _handle)
    """

    show_header = False
    show_footer = False

    DEFAULT_CSS = """
    ItemActionScreen {
        align: center middle;
        background: $background 60%;
    }

    #action-panel {
        width: 60;
        height: auto;
        max-height: 34;
        border: round $accent;
        padding: 1 2;
        background: $surface;
    }

    #item-name {
        text-style: bold;
        text-align: center;
    }

    #item-tag {
        text-align: center;
        color: $text 60%;
        margin-bottom: 1;
    }

    #item-desc {
        color: $text 70%;
        margin-bottom: 1;
    }

    #item-diff {
        margin-bottom: 1;
    }

    #item-acc-detail {
        margin-bottom: 1;
    }

    #action-buttons {
        align: center middle;
        height: auto;
        margin-top: 1;
    }

    #action-buttons Button {
        margin: 0 1;
        min-width: 12;
    }
    """

    def __init__(self, item: Any, player: Any, player_game: Any) -> None:
        super().__init__()
        self._item        = item
        self._player      = player
        self._player_game = player_game

    def compose_content(self) -> ComposeResult:
        item   = self._item
        player = self._player

        iname = rich_escape(str(getattr(item, "name", "?")))
        itag  = _item_type_tag(item)
        idesc = rich_escape(str(getattr(item, "description", "") or ""))
        qty   = getattr(item, "quantity", 1)
        qty_s = f"  ×{qty}" if qty and qty > 1 else ""

        acc = _is_accessory(item)

        can_equip = False
        can_use   = False
        try:
            from game.objects.weapon import Weapon
            from game.objects.armor import Armor
            from game.objects.utility_item import UtilityItem
            can_equip = isinstance(item, (Weapon, Armor))
            can_use   = isinstance(item, UtilityItem)
        except Exception:
            pass

        accessories = list(getattr(player, "accessories",        []) or [])
        max_slots   = int(getattr(player, "max_accessory_slots", 3) or 3)
        # Accessories always show Equip — the slot picker handles both free
        # slots and replacing a full slot, so there is no reason to hide it.
        acc_can_equip = acc

        diff_text = _stat_diff_markup(player, item) if not acc else ""
        acc_text  = _accessory_detail_markup(player, item) if acc else ""

        with Vertical(id="action-panel"):
            yield Static(f"{iname}{qty_s}", id="item-name")
            yield Static(itag, id="item-tag")
            if idesc:
                yield Static(idesc, id="item-desc")
            if diff_text:
                yield Static(diff_text, id="item-diff")
            if acc_text:
                yield Static(acc_text, id="item-acc-detail")
            with Horizontal(id="action-buttons"):
                if can_equip:
                    yield Button("Equip",   id="btn-equip",   variant="primary")
                if acc_can_equip:
                    yield Button("Equip",   id="btn-equip",   variant="primary")
                if can_use:
                    yield Button("Use",     id="btn-use",     variant="primary")
                yield Button("Discard",     id="btn-discard", variant="error")
                yield Button("Cancel",      id="btn-cancel")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        mapping = {
            "btn-equip":   "equip",
            "btn-use":     "use",
            "btn-discard": "discard",
            "btn-cancel":  None,
        }
        self.dismiss(mapping.get(event.button.id, None))

    def equip_accessory(self, player_game, accessory: Any) -> bool:
        """Equip an accessory into the accessory array if a slot is free.

        Returns True on success, False if no slots are available.
        The same accessory type may be equipped in multiple slots.
        """
        if accessory is None:
            return False
        if len(self.accessories) >= self.max_accessory_slots:
            return False
        self.accessories.append(accessory)
        if player_game is not None and accessory in player_game.inventory:
            player_game.remove_single_item_unit(accessory)
        return True

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
        accessories   = list(getattr(player, "accessories",        []) or [])
        max_acc_slots = int(getattr(player, "max_accessory_slots", 3) or 3)

        lines.append("[dim]── Equipped ──[/dim]")
        lines.append(f"WPN:  {rich_escape(w.name    if w    else 'None')}")
        lines.append(f"HEAD: {rich_escape(head.name if head else 'None')}")
        lines.append(f"BODY: {rich_escape(body.name if body else 'None')}")
        lines.append(f"ARMS: {rich_escape(arms.name if arms else 'None')}")
        lines.append(f"LEGS: {rich_escape(legs.name if legs else 'None')}")

        # Accessories sit directly under Legs
        lines.append(f"[dim]── Accessories ({len(accessories)}/{max_acc_slots}) ──[/dim]")
        for i in range(max_acc_slots):
            if i < len(accessories):
                acc      = accessories[i]
                acc_name = rich_escape(str(getattr(acc, "name", "?")))
                imm_c = len(getattr(acc, "immunities",  []) or [])
                res_c = len(getattr(acc, "resistances", []) or [])
                wk_c  = len(getattr(acc, "weaknesses",  []) or [])
                tags: list[str] = []
                if imm_c: tags.append(f"[green]Imm:{imm_c}[/green]")
                if res_c: tags.append(f"[cyan]Res:{res_c}[/cyan]")
                if wk_c:  tags.append(f"[red]Wk:{wk_c}[/red]")
                tag_s = "  " + "  ".join(tags) if tags else ""
                lines.append(f"  ◈ {i + 1}. {acc_name}{tag_s}")
            else:
                lines.append(f"  [dim]◈ {i + 1}. [Empty][/dim]")

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