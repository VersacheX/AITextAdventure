"""
ItemActionScreen: modal popup shown when the player presses Enter or clicks
an item in the Items or Equip overlays.

Displays:
  - Item name, type tag and short description.
  - For equipment (Weapon / Armor): a stat diff vs. the character's current
    item in that slot — green for improvements, red for regressions.
  - Action buttons appropriate to the item type:
      Equip / Use (depending on type) · Discard · Cancel

Callers push this screen with a result callback and receive an
`ItemActionResult` string: "equip", "use", "discard", or None for cancel.
"""
from __future__ import annotations

from typing import Any

from rich.markup import escape as rich_escape
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Static

from tui.screens.base_screen import BaseScreen


ItemActionResult = str | None  # "equip" | "use" | "discard" | None


def _stat_diff_markup(player: Any, item: Any) -> str:
    """
    Build Rich markup showing the stat comparison between *item* and whatever
    the player currently has equipped in the same slot.

    Returns an empty string when the item carries no comparable stats.
    """
    lines: list[str] = []

    def _diff(label: str, nv: int | float, ov: int | float, fmt: str = "d") -> str:
        if fmt == "f":
            diff = float(nv) - float(ov)
            diff_s = f"{diff:+.1f}"
            val_s  = f"{float(nv):.1f}"
        else:
            diff = int(nv) - int(ov)
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
            int(getattr(item, "damage", 0) or 0),
            int(getattr(current, "damage", 0) or 0) if current else 0))
        lines.append(_diff("Crit%",
            float(getattr(item, "critical_chance", 0.0) or 0),
            float(getattr(current, "critical_chance", 0.0) or 0) if current else 0.0,
            "f"))
        for attr, short in (("strength","STR"),("dexterity","DEX"),
                             ("intelligence","INT"),("constitution","CON")):
            nv = int(getattr(item, attr, 0) or 0)
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
            int(getattr(item, "defense", 0) or 0),
            int(getattr(current, "defense", 0) or 0) if current else 0))
        for attr, short in (("strength","STR"),("dexterity","DEX"),
                             ("intelligence","INT"),("constitution","CON")):
            nv = int(getattr(item, attr, 0) or 0)
            ov = int(getattr(current, attr, 0) or 0) if current else 0
            if nv or ov:
                lines.append(_diff(short, nv, ov))

    return "\n".join(lines)


def _item_type_tag(item: Any) -> str:
    try:
        from game.objects.weapon import Weapon
        from game.objects.armor import Armor, ArmorType
        from game.objects.utility_item import UtilityItem
        from game.objects.special_item import SpecialItem
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
        if isinstance(item, UtilityItem):
            eff = getattr(item, "effect", None)
            return f"Utility  [{eff}]" if eff else "Utility"
        if isinstance(item, SpecialItem):
            return "Special"
    except Exception:
        pass
    return "Item"


class ItemActionScreen(BaseScreen):
    """
    Modal that presents equip / use / discard options for a single item.

    Push with a result callback:

        def _handle(result: ItemActionResult) -> None:
            if result == "equip":   ...
            elif result == "use":   ...
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
        width: 58;
        height: auto;
        max-height: 30;
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

        iname  = rich_escape(str(getattr(item, "name", "?")))
        itag   = _item_type_tag(item)
        idesc  = rich_escape(str(getattr(item, "description", "") or ""))
        qty    = getattr(item, "quantity", 1)
        qty_s  = f"  ×{qty}" if qty and qty > 1 else ""

        diff_text = _stat_diff_markup(player, item)

        # Determine which primary action button to show
        try:
            from game.objects.weapon import Weapon
            from game.objects.armor import Armor
            from game.objects.utility_item import UtilityItem
            can_equip = isinstance(item, (Weapon, Armor))
            can_use   = isinstance(item, UtilityItem)
        except Exception:
            can_equip = False
            can_use   = False

        with Vertical(id="action-panel"):
            yield Static(f"{iname}{qty_s}", id="item-name")
            yield Static(itag, id="item-tag")
            if idesc:
                yield Static(idesc, id="item-desc")
            if diff_text:
                yield Static(diff_text, id="item-diff")
            with Horizontal(id="action-buttons"):
                if can_equip:
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