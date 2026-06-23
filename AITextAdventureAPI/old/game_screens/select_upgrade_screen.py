from typing import List, Dict, Optional, Any
import readchar

from game.objects.player import Player

class SelectUpgradeScreen:
    def __init__(self, player_game: Any, width: int =60, height: int =12):
        self.player_game = player_game
        self.width = width
        self.height = max(6, int(height))
        # list entries: power -> HP/AP, stats -> STR/DEX/INT/CON
        self.entries = [
            {"key": "hp", "label": "HP"},
            {"key": "ap", "label": "AP"},
            {"key": "str", "label": "STR"},
            {"key": "dex", "label": "DEX"},
            {"key": "int", "label": "INT"},
            {"key": "con", "label": "CON"},
        ]
        self.selected_index =0
        # tentative quantity to apply for selected entry
        self.qty =0

    def render_overlay(self, term_w: int, term_h: int, selected_player: Optional[Player] = None) -> List[str]:
        box_w = min(self.width, max(40, term_w -10))
        box_h = min(self.height, max(6, term_h -4))
        left = (term_w - box_w) //2
        inner_w = box_w -2

        up_stat =0
        up_pow =0
        if selected_player is not None:
            up_stat = selected_player.unused_stat_points
            up_pow = selected_player.unused_power_points

        lines: List[str] = []
        lines.append(' ' * left + '*' * box_w)
        title = f" Upgrade Stats - Pow:{up_pow} Stat:{up_stat} - esc:cancel +/- change ent:apply"
        lines.append(' ' * left + '*' + title.center(inner_w)[:inner_w] + '*')
        lines.append(' ' * left + '*' + ' ' * inner_w + '*')

        # list entries
        for idx, e in enumerate(self.entries):
            prefix = '>' if idx == self.selected_index else ' '
            label = e['label']
            # show current player stat or power value
            right = ''
            if selected_player is not None:
                if e['key'] == 'hp':
                    right = f"MaxHP: {getattr(selected_player, 'max_hp',0)}"
                elif e['key'] == 'ap':
                    right = f"MaxAP: {getattr(selected_player, 'max_ap',0)}"
                else:
                    map_key = {'str': 'strength', 'dex': 'dexterity', 'int': 'intelligence', 'con': 'constitution'}
                    right = f"{getattr(selected_player, map_key.get(e['key']),0)}"

            left_text = f" {prefix} {label}"
            qty_text = f"+{self.qty}" if idx == self.selected_index and self.qty >0 else ''

            # build content with right column
            if right:
                # reserve one space between columns
                if qty_text:
                    right_col = (qty_text + ' ' + right).strip()
                else:
                    right_col = right
                left_part = left_text.ljust(max(0, inner_w - len(right_col)))
                content = (left_part + right_col)[:inner_w]
            else:
                content = (left_text.ljust(inner_w - len(qty_text)) + qty_text)[:inner_w]

            lines.append(' ' * left + '*' + content + '*')

        # fill remaining rows
        for _ in range(box_h -4 - len(self.entries)):
            lines.append(' ' * left + '*' + ' ' * inner_w + '*')

        lines.append(' ' * left + '*' * box_w)

        # pad/truncate to term_w
        padded: List[str] = []
        for ln in lines:
            if len(ln) < term_w:
                padded.append(ln + ' ' * (term_w - len(ln)))
            else:
                padded.append(ln[:term_w])
        return padded

    def handle_key(self, ch: str, selected_player: Optional[Player] = None) -> Dict[str, Optional[object]]:
        def _is_esc(k: str) -> bool:
            return k == readchar.key.ESC

        def _is_enter(k: str) -> bool:
            return k == readchar.key.ENTER

        def _is_up(k: str) -> bool:
            return k == readchar.key.UP

        def _is_down(k: str) -> bool:
            return k == readchar.key.DOWN

        if _is_esc(ch):
            return {'handled': True, 'close': True}

        if _is_up(ch):
            self.selected_index = max(0, self.selected_index -1)
            self.qty =0
            return {'handled': True, 'close': False}
        if _is_down(ch):
            self.selected_index = min(len(self.entries) -1, self.selected_index +1)
            self.qty =0
            return {'handled': True, 'close': False}

        # change quantity with +/-


        if ch in ('-', '+', '='):
            entry = self.entries[self.selected_index]
            if ch == '-':
                self.qty = max(0, self.qty -1)
                return {'handled': True, 'close': False}

            # increment but do not exceed available points
            if selected_player is None:
                return {'handled': False}

            if entry['key'] in ('hp', 'ap'):
                avail = selected_player.unused_power_points
            else:
                avail = selected_player.unused_stat_points

            # cannot set qty beyond avail
            if self.qty < avail:
                self.qty +=1
                return {'handled': True, 'close': False}

        # apply
        if _is_enter(ch):
            if selected_player is None:
                return {'handled': True, 'close': False, 'message': 'no player'}
            if self.qty <=0:
                return {'handled': True, 'close': False, 'message': 'no change'}

            entry = self.entries[self.selected_index]
            
            if entry['key'] in ('hp', 'ap'):
                avail = selected_player.unused_power_points
                apply_qty = min(self.qty, avail)
                if apply_qty <=0:
                    return {'handled': True, 'close': False, 'message': 'no power points'}
                # apply to appropriate field
                hp_add = apply_qty if entry['key'] == 'hp' else 0
                ap_add = apply_qty if entry['key'] == 'ap' else 0
                # apply power allocation (Player.apply_power_point_allocation will update unused_power_points)
                selected_player.apply_power_point_allocation(hp_add, ap_add)
                msg = f'Applied {apply_qty} power to {entry["label"]}'
            else:
                avail = int(getattr(selected_player, 'unused_stat_points',0) or 0)
                apply_qty = min(self.qty, avail)
                if apply_qty <=0:
                    return {'handled': True, 'close': False, 'message': 'no stat points'}
                # map key to allocate_stats args (str_inc, dex_inc, con_inc, int_inc)
                str_inc = dex_inc = con_inc = int_inc =0
                if entry['key'] == 'str':
                    str_inc = apply_qty
                elif entry['key'] == 'dex':
                    dex_inc = apply_qty
                elif entry['key'] == 'int':
                    int_inc = apply_qty
                elif entry['key'] == 'con':
                    con_inc = apply_qty
                # apply stat allocation (Player.allocate_stats will update unused_stat_points)
                selected_player.allocate_stats(str_inc, dex_inc, con_inc, int_inc)
                msg = f'Applied {apply_qty} stat to {entry["label"]}'
            
            # reset qty
            self.qty =0
            # if both pools depleted, close
            
            remaining_stat =selected_player.unused_stat_points
            remaining_pow = selected_player.unused_power_points
            

            if remaining_stat <=0 and remaining_pow <=0:
                return {'handled': True, 'close': True, 'message': msg}
            # otherwise keep open and let inventory screen update overlay render
            return {'handled': True, 'close': False, 'message': msg}

        return {'handled': False}
