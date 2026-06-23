from typing import List, Dict, Any, Optional
from game.objects.weapon import Weapon
from game.objects.armor import Armor, ArmorType
from game.objects.player import Player


class SelectEquipmentScreenService:
    """Selection service for equipment overlay. Shows only Weapon and Armor items
    from the player_game.inventory. Maintains selected index and offset for pagination."""

    def __init__(self, player_game: Any, max_display: int = 8) -> None:
        self.player_game = player_game
        self.max_display = int(max_display)
        self.selected: int = 0
        self.offset: int = 0

    @property
    def all_equipment(self) -> List:
        # return a list of references to items in player_game.inventory that are Weapon or Armor
        items = []
        for it in self.player_game.inventory:
            if isinstance(it, Weapon) or isinstance(it, Armor):
                items.append(it)
        return items

    @property
    def total(self) -> int:
        return len(self.all_equipment)

    def ensure_selected_visible(self) -> None:
        if self.selected < self.offset:
            self.offset = self.selected
        if self.selected >= self.offset + self.max_display:
            self.offset = max(0, self.selected - self.max_display + 1)

    def move_up(self, ui_filter: Optional[str] = None) -> None:
        inv = self.all_equipment
        # apply optional UI filter (weapon/head/body/arms/legs)
        if ui_filter:
            f = ui_filter.lower()
            if f == "weapon":
                filtered = [it for it in inv if isinstance(it, Weapon)]
            elif f in ("head", "body", "arms", "legs"):
                slot_map = {
                    "head": ArmorType.HEAD,
                    "body": ArmorType.BODY,
                    "arms": ArmorType.ARMS,
                    "legs": ArmorType.LEGS,
                }
                slot = slot_map.get(f)
                filtered = [it for it in inv if isinstance(it, Armor) and it.slot == slot]
            else:
                filtered = inv
        else:
            filtered = inv

        total = len(filtered)
        if total == 0:
            self.selected = 0
            self.offset = 0
            return

        # map current selected (index into all_equipment) -> filtered index
        sel_filtered = 0
        if 0 <= self.selected < len(inv):
            sel_item = inv[self.selected]
            sel_filtered = filtered.index(sel_item) if sel_item in filtered else 0
        else:
            sel_filtered = 0

        new_filtered_sel = max(0, sel_filtered - 1)
        target_item = filtered[new_filtered_sel]
        self.selected = inv.index(target_item)

        # map offset similarly
        if 0 <= self.offset < len(inv):
            off_item = inv[self.offset]
            filtered_off = filtered.index(off_item) if off_item in filtered else 0
        else:
            filtered_off = 0

        if new_filtered_sel < filtered_off:
            new_filtered_off = new_filtered_sel
        elif new_filtered_sel >= filtered_off + self.max_display:
            new_filtered_off = max(0, new_filtered_sel - self.max_display + 1)
        else:
            new_filtered_off = filtered_off

        off_item = filtered[new_filtered_off]
        self.offset = inv.index(off_item)

        self.ensure_selected_visible()

    def move_down(self, ui_filter: Optional[str] = None) -> None:
        inv = self.all_equipment
        # apply optional UI filter (weapon/head/body/arms/legs)
        if ui_filter:
            f = ui_filter.lower()
            if f == "weapon":
                filtered = [it for it in inv if isinstance(it, Weapon)]
            elif f in ("head", "body", "arms", "legs"):
                slot_map = {
                    "head": ArmorType.HEAD,
                    "body": ArmorType.BODY,
                    "arms": ArmorType.ARMS,
                    "legs": ArmorType.LEGS,
                }
                slot = slot_map.get(f)
                filtered = [it for it in inv if isinstance(it, Armor) and it.slot == slot]
            else:
                filtered = inv
        else:
            filtered = inv

        total = len(filtered)
        if total == 0:
            self.selected = 0
            self.offset = 0
            return

        # map current selected (index into all_equipment) -> filtered index
        if 0 <= self.selected < len(inv):
            sel_item = inv[self.selected]
            sel_filtered = filtered.index(sel_item) if sel_item in filtered else 0
        else:
            sel_filtered = 0

        new_filtered_sel = min(total - 1, sel_filtered + 1)
        target_item = filtered[new_filtered_sel]
        self.selected = inv.index(target_item)

        # map offset similarly
        if 0 <= self.offset < len(inv):
            off_item = inv[self.offset]
            filtered_off = filtered.index(off_item) if off_item in filtered else 0
        else:
            filtered_off = 0

        if new_filtered_sel >= filtered_off + self.max_display:
            new_filtered_off = max(0, new_filtered_sel - self.max_display + 1)
        elif new_filtered_sel < filtered_off:
            new_filtered_off = new_filtered_sel
        else:
            new_filtered_off = filtered_off

        off_item = filtered[new_filtered_off]
        self.offset = inv.index(off_item)

        self.ensure_selected_visible()

    def discard_selected(self) -> bool:
        """Discard the selected equipment item from the underlying player_game.inventory."""
        if self.total == 0:
            return False
        it = self.all_equipment[self.selected]
        # remove the object from the actual player_game.inventory list
        self.player_game.inventory.remove(it)
        
        # clamp selection
        if self.selected >= max(0, self.total - 1):
            self.selected = max(0, self.total - 2)
        self.ensure_selected_visible()
        return True

    def equip_selected(self, player: Optional[Player]) -> Dict[str, Any]:
        """Equip the currently selected equipment item onto the provided player.
        Returns a dict: {'ok': bool, 'item': name or None, 'error': optional message}
        """
        if player is None:
            return {'ok': False, 'error': 'no_target_player'}
        if self.total == 0:
            return {'ok': False, 'error': 'empty'}
        it = self.all_equipment[self.selected]
        
        if isinstance(it, Weapon):
            ok = player.equip_weapon(self.player_game, it)
        elif isinstance(it, Armor):
            ok = player.equip_armor(self.player_game, it)
        else:
            return {'ok': False, 'error': 'not_equipable'}
        
        # after equip, adjust selection/offset in case inventory changed
        # the underlying equip calls may remove the item from inventory
        # so ensure selection references a valid index
        if self.selected >= self.total:
            self.selected = max(0, self.total - 1)
        self.ensure_selected_visible()
        return {'ok': bool(ok), 'item': getattr(it, 'name', None)}

    def get_view_context(self) -> Dict[str, Any]:
        inv = self.all_equipment
        total = len(inv)
        if total == 0:
            sel = 0
            off = 0
        else:
            sel = max(0, min(self.selected, total - 1))
            off = max(0, min(self.offset, total - 1))
        if sel < off:
            off = sel
        if sel >= off + self.max_display:
            off = max(0, sel - self.max_display + 1)
        remaining = max(0, total - off)
        display_n = min(self.max_display, remaining)
        return {
            "inventory": inv,
            "total": total,
            "selected_index": sel,
            "offset": off,
            "display_n": display_n,
        }
