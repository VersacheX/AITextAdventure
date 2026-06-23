from typing import List, Dict, Optional, Any
import readchar

from game.objects.player import Player
from game_screens.select_ability_screen_service import SelectAbilityScreenService
from game.region_seeds.player_abilities.ability_requirements import ABILITY_TYPE_REQUIREMENTS
import game.constants as const


class SelectAbilityScreen:
    def __init__(self, player_game: Any, width: int =80, height: int =14, page_size: int =8):
        self.player_game = player_game
        self.width = width
        self.height = max(6, int(height))
        self.service = SelectAbilityScreenService(player_game, page_size)

        # build type filters from requirements file, keep 'all' first
        types = [entry.get('ability_type') for entry in (ABILITY_TYPE_REQUIREMENTS or []) if entry.get('ability_type')]
        self.type_filters = ['all'] + types
        self.type_index =0

    def render_overlay(self, term_w: int, term_h: int, selected_player: Optional[Player] = None) -> List[str]:
        ctx = self.service.get_view_context(selected_player, ability_type_filter=(None if self.type_filters[self.type_index] == 'all' else self.type_filters[self.type_index]))
        abilities = ctx['abilities']
        total = ctx['total']
        sel = ctx['selected_index']
        off = ctx['offset']
        display_n = ctx['display_n']

        box_w = min(self.width, max(40, term_w -10))
        box_h = min(self.height, max(6, term_h -4))
        left = (term_w - box_w) //2
        inner_w = box_w -2

        lines: List[str] = []
        # top border
        lines.append(' ' * left + '*' * box_w)
        title = f" Learn Abilities - filter:{self.type_filters[self.type_index]} ({off +1}-{min(off + display_n, total)} of {total}) - esc:cancel +/-:filter ent:learn"
        lines.append(' ' * left + '*' + title.center(inner_w)[:inner_w] + '*')
        lines.append(' ' * left + '*' + ' ' * inner_w + '*')

        for i in range(off, off + display_n):
            if i >= total:
                break
            a = abilities[i]
            prefix = '>' if i == sel else ' '
            name = getattr(a, 'name', 'Ability')
            lvl = getattr(a, 'level',1)
            
            # build right-aligned suffix: effect display, base power, ap cost, elements, status display, aoe
            # effect display mapping may be misspelled in constants; try both keys then fallback to capitalized effect
            effect_key = getattr(a, 'effect', None)
            effect_val = (getattr(effect_key, 'value', None) if effect_key is not None else str(effect_key))
            effect_map = getattr(const, 'ABILTITY_EFFECT_DISPLAY_NAME', None) or getattr(const, 'ABILITY_EFFECT_DISPLAY_NAME', None) or {}
            effect_display = (effect_map.get(effect_val) if isinstance(effect_map, dict) else None) or (str(effect_val).capitalize() if effect_val is not None else '')
            
            base_power = getattr(a, 'base_power', None)
            ap_cost = getattr(a, 'ap_cost', None)
            
            # elements: map to single-char keys
            elem_map = getattr(const, 'ELEMENTAL_CHAR_KEYS', {}) or {}
            elems = getattr(a, 'elements', []) or []
            
            elem_chars = ''.join([elem_map.get(e.value, elem_map.get(str(e).lower(), '')) for e in elems])
            
            
            # status display name
            status_keys = getattr(a, 'status_keys', None)
            status_map = getattr(const, 'ABILITY_STATUS_KEY_DISPLAY_NAMES', {}) or {}
            
            #status_display should comma seperate statuses
            status_display = ''
            if status_keys:
                status_displays = []
                for sk in status_keys:
                    sd = status_map.get(sk) if sk else None
                    if sd:
                        status_displays.append(sd)
                status_display = ','.join(status_displays) if status_displays else ''
            
            aoe = getattr(a, 'can_aoe', False)
            
            parts: List[str] = []
            if effect_display:
                parts.append(effect_display)
            if base_power is not None:
                parts.append(f"{int(base_power)}p")
            if ap_cost is not None:
                parts.append(f"{int(ap_cost)}ap")
            if elem_chars:
                parts.append(elem_chars)
            if status_display:
                parts.append(status_display)
            if aoe:
                parts.append("(aoe)")
            
            suffix = ' '.join(parts)
            
            left_text = f" {prefix} {name} (lvl {lvl})"
            # ensure suffix fits; reserve at least one space between name and suffix when possible
            max_suffix_len = max(0, inner_w -4) # leave some room
            if len(suffix) > max_suffix_len:
                suffix = suffix[:max_suffix_len]
            
            # compute spacing
            if len(left_text) +1 + len(suffix) <= inner_w:
                gap = inner_w - len(left_text) - len(suffix)
                line = left_text + (' ' * gap) + suffix
            else:
                # need to truncate left_text
                avail_left = max(0, inner_w - len(suffix) -1)
                left_text_trunc = left_text[:avail_left]
                gap = inner_w - len(left_text_trunc) - len(suffix)
                line = left_text_trunc + (' ' * gap) + suffix

            lines.append(' ' * left + '*' + line.ljust(inner_w)[:inner_w] + '*')

        # fill remaining
        remaining_rows = max(0, box_h -4 - max(0, min(display_n, total - off)))
        for _ in range(remaining_rows):
            lines.append(' ' * left + '*' + ' ' * inner_w + '*')

        # bottom border
        lines.append(' ' * left + '*' * box_w)

        # pad/truncate
        padded: List[str] = []
        for ln in lines:
            if len(ln) < term_w:
                padded.append(ln + ' ' * (term_w - len(ln)))
            else:
                padded.append(ln[:term_w])
        return padded

    def handle_key(self, ch: str, selected_player: Optional[Player] = None) -> Dict[str, Optional[object]]:
        def _is_esc(k: str) -> bool:
            return k == getattr(readchar.key, 'ESC', None) or k == '\x1b'

        def _is_enter(k: str) -> bool:
            return k == getattr(readchar.key, 'ENTER', None) or k in ('\r', '\n')

        def _is_up(k: str) -> bool:
            return k == getattr(readchar.key, 'UP', None) or k in ('\x1b[A', '\x1bOA', '\x00H', '\xe0H')

        def _is_down(k: str) -> bool:
            return k == getattr(readchar.key, 'DOWN', None) or k in ('\x1b[B', '\x1bOB', '\x00P', '\xe0P')

        # cancel
        if _is_esc(ch):
            return {'handled': True, 'close': True}

        # navigation
        if _is_up(ch):
            self.service.move_up()
            return {'handled': True, 'close': False}
        if _is_down(ch):
            self.service.move_down()
            return {'handled': True, 'close': False}

        # filter change via + / -
        if ch in ('-', '+', '='):
            if ch == '-':
                self.type_index = (self.type_index -1) % len(self.type_filters)
            else:
                self.type_index = (self.type_index +1) % len(self.type_filters)
            return {'handled': True, 'close': False, 'message': f'filter:{self.type_filters[self.type_index]}'}

        # learn
        if _is_enter(ch):
            res = self.service.learn_selected(selected_player, ability_type_filter=(None if self.type_filters[self.type_index] == 'all' else self.type_filters[self.type_index]))
            if res.get('ok'):
                ability = res.get('ability')
                # if the player has no remaining ability slots after learning, request overlay close
                remaining =0
                
                remaining = int(getattr(selected_player, 'unused_ability_slots',0) or 0)
                
                msg = f"learned {getattr(ability, 'name', '')}"
                if remaining <=0:
                    return {'handled': True, 'close': True, 'message': msg}
                # still has slots -> refresh service view so learned ability is removed from results
                
                # call get_view_context with same filter to refresh/clamp internal indices
                _ = self.service.get_view_context(selected_player, ability_type_filter=(None if self.type_filters[self.type_index] == 'all' else self.type_filters[self.type_index]))
                
                return {'handled': True, 'close': False, 'message': msg}
            return {'handled': True, 'close': False, 'message': f"failed: {res.get('error')}"}

        return {'handled': False}
