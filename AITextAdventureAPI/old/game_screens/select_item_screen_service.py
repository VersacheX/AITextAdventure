from typing import List, Dict, Any, Optional
from game.objects.item import Item
from game.objects.utility_item import UtilityItem
from game.objects.weapon import Weapon
from game.objects.armor import Armor
from game.objects.special_item import SpecialItem


class SelectItemScreenService:
    """Lightweight selection service for the item selection overlay.

    Tracks a selected index and viewport offset for the player's inventory list.
    Provides simple navigation and a discard operation. The UI layer handles use/targeting.
    """

    def __init__(self, player_game: Any, max_display: int = 8) -> None:
        self.player_game = player_game
        self.max_display = int(max_display)
        # self.selected and self.offset are maintained as indices into the full inventory list.
        self.selected: int = 0
        self.offset: int = 0

    @property
    def inventory(self) -> List:
        return list(self.player_game.inventory)

    @property
    def total(self) -> int:
        return len(self.inventory)

    def ensure_selected_visible(self) -> None:
        if self.selected < self.offset:
            self.offset = self.selected
        if self.selected >= self.offset + self.max_display:
            self.offset = max(0, self.selected - self.max_display + 1)

    def move_up(self, item_type_filter: Optional[str] = None) -> None:
        # Operate on the filtered view, then map back to full-inventory indices.
        ctx = self.get_view_context(item_type_filter=item_type_filter)
        total = ctx["total"]
        if total == 0:
            self.selected = 0
            self.offset = 0
            return

        filtered_sel = ctx["selected_index"]
        filtered_off = ctx["offset"]

        new_filtered_sel = max(0, filtered_sel - 1)

        # map filtered selected back to full inventory index
        full_inv = list(self.player_game.inventory)
        target_item = ctx["inventory"][new_filtered_sel]
        self.selected = full_inv.index(target_item)

        # compute new filtered offset and map back to full index
        if new_filtered_sel < filtered_off:
            new_filtered_off = new_filtered_sel
        elif new_filtered_sel >= filtered_off + self.max_display:
            new_filtered_off = max(0, new_filtered_sel - self.max_display + 1)
        else:
            new_filtered_off = filtered_off

        off_item = ctx["inventory"][new_filtered_off]
        self.offset = full_inv.index(off_item)

        # keep consistency guard
        self.ensure_selected_visible()

    def move_down(self, item_type_filter: Optional[str] = None) -> None:
        # Operate on the filtered view, then map back to full-inventory indices.
        ctx = self.get_view_context(item_type_filter=item_type_filter)
        total = ctx["total"]
        if total == 0:
            self.selected = 0
            self.offset = 0
            return

        filtered_sel = ctx["selected_index"]
        filtered_off = ctx["offset"]

        new_filtered_sel = min(max(0, total - 1), filtered_sel + 1)

        # map filtered selected back to full inventory index
        full_inv = list(self.player_game.inventory)
        target_item = ctx["inventory"][new_filtered_sel]
        self.selected = full_inv.index(target_item)

        # compute new filtered offset and map back to full index
        if new_filtered_sel >= filtered_off + self.max_display:
            new_filtered_off = max(0, new_filtered_sel - self.max_display + 1)
        elif new_filtered_sel < filtered_off:
            new_filtered_off = new_filtered_sel
        else:
            new_filtered_off = filtered_off

        off_item = ctx["inventory"][new_filtered_off]
        self.offset = full_inv.index(off_item)

        # keep consistency guard
        self.ensure_selected_visible()

    def discard_selected(self, item_type_filter: Optional[str] = None) -> bool:
        """Discard one unit of the selected inventory item. Returns True if an
        item was removed, False otherwise.

        If a filter is supplied, operate on the filtered view.
        """
        ctx = self.get_view_context(item_type_filter=item_type_filter)
        if ctx["total"] == 0:
            return False
        idx = ctx["selected_index"]
        item = ctx["inventory"][idx]
        # Use central removal so inventory indices and stacks are managed consistently
        removed = self.player_game.remove_single_item_unit(item)

        # After removal, map the new filtered selection/offset back to full inventory indices
        new_ctx = self.get_view_context(item_type_filter=item_type_filter)
        if new_ctx["total"] == 0:
            self.selected = 0
            self.offset = 0
            return removed

        full_inv = list(self.player_game.inventory)

        new_filtered_sel = new_ctx["selected_index"]
        sel_item = new_ctx["inventory"][new_filtered_sel]
        self.selected = full_inv.index(sel_item)

        new_filtered_off = new_ctx["offset"]
        off_item = new_ctx["inventory"][new_filtered_off]
        self.offset = full_inv.index(off_item)

        return removed

    def get_view_context(self, item_type_filter: Optional[str] = None) -> Dict[str, Any]:
        """
        Return a view context dict similar to SelectAbilityScreenService.
        If item_type_filter is provided (string), inventory is filtered to items
        matching that type. Supported filters: 'utility','weapon','armor','special','item'.
        Pass None to get full inventory.

        NOTE: selection and offset are preserved across filters by mapping the
        current numeric selected/offset (which reference the full inventory)
        to positions within the filtered inventory when possible. This prevents
        the cursor jumping to unexpected positions when a filter is applied.
        """
        full_inv = list(self.player_game.inventory)

        # Start with full inventory, then apply filter if requested
        inv = list(full_inv)
        if item_type_filter:
            filt = item_type_filter.lower()
            filtered: List = []
            for it in full_inv:
                if filt == "utility" and isinstance(it, UtilityItem):
                    filtered.append(it)
                elif filt == "weapon" and isinstance(it, Weapon):
                    filtered.append(it)
                elif filt == "armor" and isinstance(it, Armor):
                    filtered.append(it)
                elif filt == "special" and isinstance(it, SpecialItem):
                    filtered.append(it)
                # elif filt == "item" and type(it) is Item:
                #     filtered.append(it)
            inv = filtered

        total = len(inv)

        # If no items in view, reset indices
        if total == 0:
            sel = 0
            off = 0
            display_n = 0
            return {
                "inventory": inv,
                "total": total,
                "selected_index": sel,
                "offset": off,
                "display_n": display_n,
            }

        # Map current selected (which should be an index into full_inv) to index in filtered inv
        sel = 0
        if 0 <= self.selected < len(full_inv):
            sel_item = full_inv[self.selected]
            if sel_item in inv:
                sel = inv.index(sel_item)
            else:
                # fallback: clamp numeric selected into filtered range
                sel = max(0, min(self.selected, total - 1))
        else:
            sel = min(self.selected, total - 1)

        # Map offset similarly so viewport tracks the same region when possible
        if 0 <= self.offset < len(full_inv):
            off_item = full_inv[self.offset]
            if off_item in inv:
                off = inv.index(off_item)
            else:
                off = max(0, min(self.offset, total - 1))
        else:
            off = max(0, min(self.offset, total - 1))

        # Ensure selection is within offset/view bounds
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