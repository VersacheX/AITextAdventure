from typing import List, Optional, Any
import readchar
from game.objects.npc import NPC

class NPCLogScreen:
    """Overlay that displays NPCs the player knows about.

    Shows a detailed summary for the currently selected NPC above a paged
    list of NPC entries (name). Summary contains: Name header, Known Location,
    and Description (word-wrapped).
    """

    def __init__(self, player_game: Any, width: int = 80, height: int = 16):
        self.player_game = player_game
        self.width = width
        self.height = max(6, int(height))
        self.selected_index = 0

    def _wrap_text(self, text: str, max_width: int) -> List[str]:
        if not text:
            return []
        words = text.split()
        lines: List[str] = []
        cur = ''
        for w in words:
            if not cur:
                cur = w
            elif len(cur) + 1 + len(w) <= max_width:
                cur = cur + ' ' + w
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def _format_npc_summary_full(self, npc: NPC, box_w: int) -> List[str]:
        # reserve1 space padding on left and right inside the '*' borders
        if box_w < 6:
            box_w = 6
        inner_w = box_w - 2  # width between the outer stars
        content_w = inner_w - 2  # account for one space padding on each side

        lines: List[str] = []

        # Top border and name
        lines.append('*' * box_w)
        title = f"{getattr(npc, 'name', 'NPC')}"
        # center title within content_w and surround with single-space padding
        lines.append('*' + ' ' + title.center(content_w)[:content_w] + ' ' + '*')
        lines.append('*' + ' ' * content_w + ' ' + '*')

        # LOCATION
        location_results = self.player_game.get_npc_details(npc)
        has_tasks = location_results.get('has_tasks', False)
        location_description = location_results.get('location_description', 'Unknown')
        loc_line = f"Known Location: {location_description} {npc.position} {' * ' if has_tasks else ''}"
        loc_wr = self._wrap_text(loc_line, content_w)
        for lw in loc_wr:
            lines.append('*' + ' ' + lw.ljust(content_w)[:content_w] + ' ' + '*')
            lines.append('*' + ' ' * content_w + ' ' + '*')

        # Description
        desc = getattr(npc, 'description', '') or ''
        if desc:
            desc_lines = self._wrap_text(desc, content_w)
            for dl in desc_lines:
                lines.append('*' + ' ' + dl.ljust(content_w)[:content_w] + ' ' + '*')
        else:
            lines.append('*' + ' ' + 'No description.'.ljust(content_w)[:content_w] + ' ' + '*')

        # Bottom border
        lines.append('*' * box_w)
        return lines

    def render_overlay(self, term_w: int, term_h: int, selected_player=None) -> List[str]:
        box_w = min(self.width, max(40, term_w - 10))
        box_h = min(self.height, max(6, term_h - 4))
        left = (term_w - box_w) // 2
        inner_w = box_w - 2
        content_w = inner_w - 2

        lines: List[str] = []
        lines.append(' ' * left + '*' * box_w)

        # filter to only NPCs the player has met
        known_npcs = [n for n in (self.player_game.npcs or []) if n.met]

        # ensure selected_index is within bounds for the filtered list
        if known_npcs:
            self.selected_index = max(0, min(self.selected_index, len(known_npcs) - 1))
        else:
            self.selected_index = 0

        title = f" NPC Log ({len(known_npcs)} entries) - esc:close"
        # header line with one space padding inside
        lines.append(' ' * left + '*' + ' ' + title.center(content_w)[:content_w] + ' ' + '*')
        lines.append(' ' * left + '*' + ' ' * content_w + ' ' + '*')

        sel = self.selected_index
        sel_npc = known_npcs[sel] if known_npcs else None
        summary_lines: List[str] = []
        if sel_npc is not None:
            summary_lines = self._format_npc_summary_full(sel_npc, box_w)

        for s in summary_lines:
            lines.append(' ' * left + s.ljust(box_w)[:box_w])

        lines.append(' ' * left + '*' + ' ' * (box_w - 2) + ' ' + '*')

        # List area
        list_inner_rows = max(1, box_h - 6)
        lines.append(' ' * left + '*' * box_w)

        start = max(0, min(self.selected_index, max(0, len(known_npcs) - list_inner_rows)))
        shown = known_npcs[start:start + list_inner_rows]

        for i, n in enumerate(shown, start=start):
            name = getattr(n, 'name', 'NPC')
            prefix = '>' if i == self.selected_index else ' '
            entry = f"{prefix} {name}"
            # pad entry inside content width
            lines.append(' ' * left + '*' + ' ' + entry.ljust(content_w)[:content_w] + ' ' + '*')

        remaining = list_inner_rows - len(shown)
        for _ in range(remaining):
            lines.append(' ' * left + '*' + ' ' + ' ' * content_w + ' ' + '*')

        lines.append(' ' * left + '*' * box_w)

        # pad/truncate
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

        def _is_esc(k: str) -> bool:
            return k == getattr(readchar.key, 'ESC', None) or k == '\x1b'

        known_npcs = [n for n in (self.player_game.npcs or []) if n.met]

        if _is_esc(ch):
            return {'handled': True, 'close': True}

        if _is_up(ch):
            if self.selected_index > 0:
                self.selected_index -= 1
            return {'handled': True, 'close': False}

        if _is_down(ch):
            if self.selected_index < max(0, len(known_npcs) - 1):
                self.selected_index += 1
            return {'handled': True, 'close': False}

        return {'handled': False}
