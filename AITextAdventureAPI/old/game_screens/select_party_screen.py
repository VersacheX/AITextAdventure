from typing import List, Optional, Any
import readchar


class SelectPartyScreen:
    """Overlay to select which characters are in the active party.

    Displays small boxes for characters currently in the active party above
    a selectable list of all characters. Characters in the active party have
    a '*' shown next to their name in the list. Press Enter to toggle a
    character in/out of the active party. Esc closes the overlay.
    """

    def __init__(self, player_game: Any, width: int =80, height: int =16, party_mode: bool = False):
        self.player_game = player_game
        self.width = width
        self.height = max(6, int(height))
        self.selected_index =0
        self.party_mode = party_mode

    def _wrap_text(self, text: str, max_width: int) -> List[str]:
        if not text:
            return []
        words = text.split()
        lines: List[str] = []
        cur = ''
        for w in words:
            if not cur:
                cur = w
            elif len(cur) +1 + len(w) <= max_width:
                cur = cur + ' ' + w
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def render_overlay(self, term_w: int, term_h: int, selected_player=None) -> List[str]:
        box_w = min(self.width, max(40, term_w -10))
        box_h = min(self.height, max(6, term_h -4))
        left = (term_w - box_w) //2
        inner_w = box_w -2
        content_w = inner_w -2

        lines: List[str] = []
        # top border and title
        lines.append(' ' * left + '*' * box_w)
        title = f" Select Party ({len(self.player_game.get_all_characters() or [])} chars) - esc:close"
        lines.append(' ' * left + '*' + ' ' + title.center(content_w)[:content_w] + ' ' + '*')
        lines.append(' ' * left + '*' + ' ' * content_w + ' ' + '*')

        # Active party small boxes row
        active = self.player_game.get_active_party() or []
        if active:
            # compute small box width per member to fit in box_w
            max_name = max((len(getattr(a, 'name', '')) for a in active), default=0)
            per_box = max(8, min(max_name +4, (content_w +1) // len(active) -1)) if len(active) >0 else max_name +4
            total_boxes_w = len(active) * per_box + max(0, len(active) -1)
            start_left = max(0, (content_w - total_boxes_w) //2)

            # top border of boxes
            top = ' ' * start_left
            for a in active:
                top += '+' + '-' * (per_box -2) + '+' + ' '
            top = top.rstrip()
            lines.append(' ' * left + '*' + ' ' + top.ljust(content_w)[:content_w] + ' ' + '*')

            # name row
            name_row = ' ' * start_left
            for a in active:
                name = getattr(a, 'name', 'Char')
                name_row += '|' + name.center(per_box -2)[:per_box -2] + '|' + ' '
            name_row = name_row.rstrip()
            lines.append(' ' * left + '*' + ' ' + name_row.ljust(content_w)[:content_w] + ' ' + '*')

            # bottom border of boxes
            bot = ' ' * start_left
            for a in active:
                bot += '+' + '-' * (per_box -2) + '+' + ' '
            bot = bot.rstrip()
            lines.append(' ' * left + '*' + ' ' + bot.ljust(content_w)[:content_w] + ' ' + '*')
        else:
            lines.append(' ' * left + '*' + ' ' + 'No active party members'.center(content_w)[:content_w] + ' ' + '*')
            lines.append(' ' * left + '*' + ' ' * content_w + ' ' + '*')

        # spacer
        lines.append(' ' * left + '*' + ' ' * content_w + ' ' + '*')

        # List header
        lines.append(' ' * left + '*' * box_w)

        # List area
        all_chars = self.player_game.get_all_characters() or []
        # calculate remaining rows available for listing
        used_rows = len(lines) +3 # approximate rows already used plus bottom border and pad
        list_inner_rows = max(1, box_h - used_rows)

        # ensure selected index in range
        sel = max(0, min(self.selected_index, max(0, len(all_chars) -1)))
        start = max(0, min(sel, max(0, len(all_chars) - list_inner_rows)))
        shown = all_chars[start:start + list_inner_rows]

        for i, ch in enumerate(shown, start=start):
            name = getattr(ch, 'name', 'Character')
            is_active = any(getattr(ac, '_uuid', None) == getattr(ch, '_uuid', None) for ac in active)
            prefix = '>' if i == self.selected_index else ' '
            star = '*' if is_active else ' '
            entry = f"{prefix} {star} {name}"
            lines.append(' ' * left + '*' + ' ' + entry.ljust(content_w)[:content_w] + ' ' + '*')

        remaining = list_inner_rows - len(shown)
        for _ in range(remaining):
            lines.append(' ' * left + '*' + ' ' + ' ' * content_w + ' ' + '*')

        lines.append(' ' * left + '*' * box_w)

        # pad/truncate to terminal width
        padded: List[str] = []
        for ln in lines:
            if len(ln) < term_w:
                padded.append(ln + ' ' * (term_w - len(ln)))
            else:
                padded.append(ln[:term_w])
        return padded

    def handle_key(self, ch: str, selected_player: Optional[object] = None):
        def _is_up(k: str) -> bool:
            return k == getattr(readchar.key, 'UP', None) or k in ('\x1b[A', '\x1bOA', '\x00H', '\xe0H')

        def _is_down(k: str) -> bool:
            return k == getattr(readchar.key, 'DOWN', None) or k in ('\x1b[B', '\x1bOB', '\x00P', '\xe0P')

        def _is_enter(k: str) -> bool:
            return k == getattr(readchar.key, 'ENTER', None) or k == '\r' or k == '\n'

        def _is_esc(k: str) -> bool:
            return k == getattr(readchar.key, 'ESC', None) or k == '\x1b'

        all_chars = self.player_game.get_all_characters() or []

        if _is_esc(ch):
            return {'handled': True, 'close': True}

        if _is_up(ch):
            if self.selected_index >0:
                self.selected_index -=1
            return {'handled': True, 'close': False}

        if _is_down(ch):
            if self.selected_index < max(0, len(all_chars) -1):
                self.selected_index +=1
            return {'handled': True, 'close': False}

        if _is_enter(ch):
            if 0 <= self.selected_index < len(all_chars):
                sel_char = all_chars[self.selected_index]
                active_uuids = [getattr(a, '_uuid', None) for a in self.player_game.get_active_party() or []]
                if getattr(sel_char, '_uuid', None) in active_uuids:
                    # remove from active party                    
                    self.player_game.remove_character_from_active_party(sel_char)
                    
                    return {'handled': True, 'message': f'Removed {getattr(sel_char, "name", "char")} from party', 'close': False}
                else:
                    # add to active party if room
                    if len(self.player_game.get_active_party() or []) >= getattr(self.player_game, 'max_party_count',5):
                        return {'handled': True, 'message': 'Party is full', 'close': False}
                    self.player_game.add_character_to_active_party(sel_char)

                    return {'handled': True, 'message': f'Added {getattr(sel_char, "name", "char")} to party', 'close': False}

            return {'handled': False}

        return {'handled': False}
