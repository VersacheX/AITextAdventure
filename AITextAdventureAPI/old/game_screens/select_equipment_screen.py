from typing import List, Dict, Optional, Any
import readchar

from game.objects.weapon import Weapon
from game.objects.armor import Armor, ArmorType
from game.objects.player import Player
from game_screens.select_equipment_screen_service import SelectEquipmentScreenService
from game.constants_other import ELEMENTAL_CHAR_KEYS


def _getch() -> str:
    return readchar.readkey()


class SelectEquipmentScreen:
    def __init__(self, player_game: Any, width: int = 60, height: int = 12, max_display: int = 8):
        self.player_game = player_game
        self.width = width
        self.height = max(6, int(height))
        self.service = SelectEquipmentScreenService(player_game, max_display=max_display)

        # filter options: all, weapon, head, body, arms, legs
        self.filter_options = ["all", "weapon", "head", "body", "arms", "legs"]
        self.filter_index = 0

    def _matches_filter(self, it, current_filter: str) -> bool:
        """Small helper to apply the same filter logic used in render_overlay."""
        if current_filter == "all":
            return True
        if current_filter == "weapon":
            return isinstance(it, Weapon)
        # if it's not armor we cannot match head/body/arms/legs
        if not isinstance(it, Armor):
            return False
        if current_filter == "head":
            return it.slot == ArmorType.HEAD
        if current_filter == "body":
            return it.slot == ArmorType.BODY
        if current_filter == "arms":
            return it.slot == ArmorType.ARMS
        if current_filter == "legs":
            return it.slot == ArmorType.LEGS
        return True

    def _item_stats_short(self, item) -> str:
        if item is None:
            return ""
        if isinstance(item, Weapon):
            dmg = item.damage
            crit = item.critical_chance
            s = item.strength
            dx = item.dexterity
            inte = item.intelligence
            con = item.constitution
            elems = item.elements
            elem_str = "".join([ELEMENTAL_CHAR_KEYS.get(e, "?") for e in elems]) if elems else "N/A"
            return f"Dmg:{dmg} Crt:{crit}% S:{s} D:{dx} I:{inte} C:{con} E:{elem_str}"
        if isinstance(item, Armor):
            defense = getattr(item, "defense", "")
            s = item.strength
            dx = item.dexterity
            inte = item.intelligence
            con = item.constitution
            elems = item.elements
            elem_str = "".join([ELEMENTAL_CHAR_KEYS.get(e, "?") for e in elems]) if elems else "N/A"
            return f"Def:{defense} S:{s} D:{dx} I:{inte} C:{con} E:{elem_str}"
        return ""

    def _format_left_right(self, left_text: str, right_text: str, inner_w: int) -> str:
        left_text = left_text or ""
        right_text = right_text or ""
        if not right_text:
            # simple left justfied
            return left_text.ljust(inner_w)[:inner_w]
        # truncate right_text if too long
        if len(right_text) > inner_w - 2:
            right_text = right_text[: max(0, inner_w - 4)]
        avail_left = inner_w - len(right_text)
        if avail_left <= 0:
            return right_text.rjust(inner_w)[:inner_w]
        if len(left_text) > avail_left:
            left_text = left_text[: max(0, avail_left - 1)] + "..."
        return (left_text.ljust(avail_left) + right_text)[:inner_w]

    def render_overlay(self, term_w: int, term_h: int, selected_player: Optional[Player] = None) -> List[str]:
        ctx = self.service.get_view_context()
        full_inv = ctx.get("inventory", [])
        total = int(ctx.get("total", 0) or 0)
        sel = int(ctx.get("selected_index", 0) or 0)
        off = int(ctx.get("offset", 0) or 0)
        display_n = int(ctx.get("display_n", 8) or 8)

        # geometry
        box_w = min(self.width, max(40, term_w - 10))
        box_h = min(self.height, max(6, term_h - 4))
        left = (term_w - box_w) // 2
        inner_w = box_w - 2

        # filter
        current_filter = self.filter_options[self.filter_index]

        def matches(it):
            if current_filter == "all":
                return True
            if current_filter == "weapon":
                return isinstance(it, Weapon)
            if not isinstance(it, Armor):
                return False
            if current_filter == "head":
                return it.slot == ArmorType.HEAD
            if current_filter == "body":
                return it.slot == ArmorType.BODY
            if current_filter == "arms":
                return it.slot == ArmorType.ARMS
            if current_filter == "legs":
                return it.slot == ArmorType.LEGS
            return True

        inv = [it for it in full_inv if matches(it)]
        filtered_total = len(inv)

        # map selection
        selected_item = None
        if 0 <= sel < total:
            selected_item = full_inv[sel]
            
        sel_filtered = -1
        if selected_item is not None:
            #input (f'selected item and inv: {selected_item}, {inv}')
            #get index of selected_item in filtered inv
            sel_filtered = next((i for i, it in enumerate(inv) if it is selected_item), -1)            

        lines: List[str] = []

        # top box: selected player's equipped
        lines.append(" " * left + "*" * box_w)
        title = f" Player: {selected_player.name if selected_player else 'None'} - Equipped "
        lines.append(" " * left + "*" + title.center(inner_w)[:inner_w] + "*")
        lines.append(" " * left + "*" + " " * inner_w + "*")

        if selected_player:
            w = getattr(selected_player, "equipped_weapon", None)
            left_txt = f" Weapon: {w.name if w else 'None'}"
            right_txt = self._item_stats_short(w) if w else ""
            lines.append(" " * left + "*" + self._format_left_right(left_txt, right_txt, inner_w) + "*")

            slots = [
                ("HEAD", getattr(selected_player, "head_armor", None)),
                ("BODY", getattr(selected_player, "body_armor", None)),
                ("ARMS", getattr(selected_player, "arm_armor", None)),
                ("LEGS", getattr(selected_player, "leg_armor", None)),
            ]
            for lbl, armor in slots:
                left_txt = f" {lbl}: {armor.name if armor else 'None'}"
                right_txt = self._item_stats_short(armor) if armor else ""
                lines.append(" " * left + "*" + self._format_left_right(left_txt, right_txt, inner_w) + "*")
        else:
            lines.append(" " * left + "*" + " No player selected ".center(inner_w)[:inner_w] + "*")

        lines.append(" " * left + "*" * box_w)

        # equipment header with filter
        title = f" Equipment ({off + 1}-{off + display_n} of {filtered_total}) - filter:{current_filter} - del:discard ent:equip esc:cancel"
        lines.append(" " * left + "*" + title.center(inner_w)[:inner_w] + "*")
        lines.append(" " * left + "*" + " " * inner_w + "*")

        # pagination for filtered list
        if filtered_total == 0:
            page_start = 0
        else:
            if sel_filtered >= 0:
                half = display_n // 2
                page_start = max(0, sel_filtered - half)
                page_start = min(page_start, max(0, filtered_total - display_n))
            else:
                page_start = 0

        page_items = inv[page_start: page_start + display_n]
        for item in page_items:
            name = item.name
            prefix = ">" if (selected_item is not None and item is selected_item) else " "
            left_text = f" {prefix} {name}"
            right_text = self._item_stats_short(item)
            line_content = self._format_left_right(left_text, right_text, inner_w)
            lines.append(" " * left + "*" + line_content + "*")

        # fill remaining
        for _ in range(box_h - 4 - display_n):
            lines.append(" " * left + "*" + " " * inner_w + "*")
        lines.append(" " * left + "*" * box_w)

        # pad
        padded: List[str] = []
        for ln in lines:
            if len(ln) < term_w:
                padded.append(ln + " " * (term_w - len(ln)))
            else:
                padded.append(ln[:term_w])
        return padded

    def handle_key(self, ch: str, selected_player: Optional[Player] = None) -> Dict[str, Optional[object]]:
        def _is_up(k: str) -> bool:
            return k == getattr(readchar.key, "UP", None) or k in ("\x1b[A", "\x1bOA", "\x00H", "\xe0H")

        def _is_down(k: str) -> bool:
            return k == getattr(readchar.key, "DOWN", None) or k in ("\x1b[B", "\x1bOB", "\x00P", "\xe0P")

        def _is_delete(k: str) -> bool:
            return k == getattr(readchar.key, "DELETE", None) or k in ("\x7f",)

        def _is_enter(k: str) -> bool:
            return k == getattr(readchar.key, "ENTER", None) or k in ("\r", "\n")

        def _is_esc(k: str) -> bool:
            return k == getattr(readchar.key, "ESC", None) or k == "\x1b"

        def _is_shift_left(k: str) -> bool:
            return k in ("\x1b[1;2D", "\x1b[1;2;D", "\x1b[1;2;4D", "<")

        def _is_shift_right(k: str) -> bool:
            return k in ("\x1b[1;2C", "\x1b[1;2;C", "\x1b[1;2;4C", ">")

        # cancel
        if _is_esc(ch):
            return {"handled": True, "close": True}

        # delete/discard
        if _is_delete(ch):
            removed = self.service.discard_selected()
            return {"handled": True, "close": False, "message": "discarded" if removed else "nothing"}

        # navigate
        if _is_up(ch):
            current_filter = self.filter_options[self.filter_index]
            self.service.move_up(current_filter)
            return {"handled": True, "close": False}
        if _is_down(ch):
            current_filter = self.filter_options[self.filter_index]
            self.service.move_down(current_filter)
            return {"handled": True, "close": False}

        # enter = equip
        if _is_enter(ch):
            ctx = self.service.get_view_context()
            if int(ctx.get("total", 0) or 0) == 0:
                return {"handled": True, "close": False, "message": "empty"}
            res = self.service.equip_selected(selected_player)
            if res.get("ok"):
                return {"handled": True, "close": False, "message": f"equipped {res.get('item')}"}
            else:
                return {"handled": True, "close": False, "message": f"failed: {res.get('error')}"}

        # filter change
        if _is_shift_left(ch):
            self.filter_index = (self.filter_index - 1) % len(self.filter_options)
            # map UI-filtered first item back to service index so cursor moves to first item in new filter
            current_filter = self.filter_options[self.filter_index]
            filtered_inv = [it for it in self.service.all_equipment if self._matches_filter(it, current_filter)]
            if filtered_inv:
                idx = self.service.all_equipment.index(filtered_inv[0])
                self.service.selected = idx
                self.service.offset = idx
            else:
                self.service.selected = 0
                self.service.offset = 0
            return {"handled": True, "close": False, "message": f"filter:{self.filter_options[self.filter_index]}"}

        if _is_shift_right(ch):
            self.filter_index = (self.filter_index + 1) % len(self.filter_options)
            current_filter = self.filter_options[self.filter_index]
            filtered_inv = [it for it in self.service.all_equipment if self._matches_filter(it, current_filter)]
            if filtered_inv:
                idx = self.service.all_equipment.index(filtered_inv[0])
                self.service.selected = idx
                self.service.offset = idx
            else:
                self.service.selected = 0
                self.service.offset = 0
            return {"handled": True, "close": False, "message": f"filter:{self.filter_options[self.filter_index]}"}

        # explicit +/- keys to change filter (prefer these to avoid terminal shift-arrow issues)        
        if ch == '-':
            self.filter_index = (self.filter_index - 1) % len(self.filter_options)
            current_filter = self.filter_options[self.filter_index]
            filtered_inv = [it for it in self.service.all_equipment if self._matches_filter(it, current_filter)]
            if filtered_inv:
                idx = self.service.all_equipment.index(filtered_inv[0])
                self.service.selected = idx
                self.service.offset = idx
            else:
                self.service.selected = 0
                self.service.offset = 0
            return {"handled": True, "close": False, "message": f"filter (-/+):{self.filter_options[self.filter_index]}"}

        if ch in ('+', '='):
            self.filter_index = (self.filter_index + 1) % len(self.filter_options)
            current_filter = self.filter_options[self.filter_index]
            filtered_inv = [it for it in self.service.all_equipment if self._matches_filter(it, current_filter)]
            if filtered_inv:
                idx = self.service.all_equipment.index(filtered_inv[0])
                self.service.selected = idx
                self.service.offset = idx
            else:
                self.service.selected = 0
                self.service.offset = 0
            return {"handled": True, "close": False, "message": f"filter:{self.filter_options[self.filter_index]}"}
        
        return {"handled": False}
