from typing import List, Dict, Optional, Any
import readchar

from game.objects.utility_item import UtilityItem
from game_screens.select_item_screen_service import SelectItemScreenService
from game.objects.player import Player


def _getch() -> str:
    
    ch = readchar.readkey()
    return ch
    


class SelectItemsScreen:
    """UI overlay for selecting/using/discarding inventory items.

    This class is stateful and owns a SelectItemScreenService instance that
    controls pagination and back-end item operations. The InventoryScreen is
    expected to create one instance per `run` and call `render_overlay` from
    its own `render` method, and forward keystrokes to `handle_key` while the
    overlay is active. The overlay does not manage the main input loop.
    """

    def __init__(self, player_game: Any, width: int =60, height: int =12, max_display: int =8):
        self.player_game = player_game
        self.width = width
        # fixed box height in rows (including borders)
        self.height = max(6, int(height))
        # service controls which inventory slice is shown; keep its max_display in sync
        self.service = SelectItemScreenService(player_game, max_display=max_display)

        # item type filters (mimic select_ability_screen behaviour)
        self.type_filters = ['all', 'utility', 'weapon', 'armor', 'special']#, 'item'
        self.type_index =0

    def render_overlay(self, term_w: int, term_h: int, selected_player) -> List[str]:
        """Return a list of strings representing the centered-bottom framed overlay.

        The caller (InventoryScreen.render) will print these lines so the overlay
        is composed within the same frame. Borders use '*' to match the inventory frame.
        Each returned line is padded/truncated to `term_w` columns.
        This overlay uses a fixed height (`self.height`) clamped to available terminal rows.
        """
        # fixed box width but constrained by terminal
        box_w = min(self.width, max(40, term_w -10))
        # fixed box height but ensure it fits in terminal (leave at least1 row margin)
        box_h = min(self.height, max(6, term_h -4))
        left = (term_w - box_w) //2

        inner_w = box_w -2
        # compute how many item rows fit (border + title + padding take3 rows)
        available_item_rows = max(1, box_h -4)

        # ensure service pagination matches UI available rows so offset/visibility logic aligns
        self.service.max_display = available_item_rows

        # pass filter into service
        current_filter = None if self.type_filters[self.type_index] == 'all' else self.type_filters[self.type_index]
        ctx = self.service.get_view_context(item_type_filter=current_filter)
        inv = ctx['inventory']
        total = ctx['total']
        sel = ctx['selected_index']
        off = ctx['offset']
        svc_display_n = ctx['display_n']

        display_n = min(svc_display_n, available_item_rows)

        lines: List[str] = []
        # top border
        lines.append(' ' * left + '*' * box_w)
        # title (include filter like select_ability_screen)
        title = f" Inventory Items - filter:{self.type_filters[self.type_index]} ({off +1}-{off + display_n} of {total}) - del:discard +/-:filter ent:use esc:cancel"
        lines.append(' ' * left + '*' + title.center(inner_w)[:inner_w] + '*')
        lines.append(' ' * left + '*' + ' ' * inner_w + '*')

        # item lines according to available rows
        for i in range(off, off + display_n):
            if i >= total:
                break
            item = inv[i]
            q = f" x{item.quantity}" 
            name = f"{item.name}{q}"
            prefix = '>' if i == sel else ' '
            line = f" {prefix} {name}"
            lines.append(' ' * left + '*' + line.ljust(inner_w)[: inner_w] + '*')

        # fill remaining item rows if inventory shorter than space
        filled = max(0, display_n - max(0, min(display_n, total - off)))
        for _ in range(filled):
            lines.append(' ' * left + '*' + ' ' * inner_w + '*')

        # ensure total inner content rows match available_item_rows
        current_item_rows = sum(1 for ln in lines if ln.strip().startswith('*') and ln.strip().endswith('*')) -3
        # (above calculation rough; simpler to append empty lines until we reach box_h -2)
        while len(lines) < box_h -1:
            lines.append(' ' * left + '*' + ' ' * inner_w + '*')

        # bottom border
        lines.append(' ' * left + '*' * box_w)

        # pad/truncate each line to terminal width so it cleanly overwrites existing content
        padded: List[str] = []
        for ln in lines:
            if len(ln) < term_w:
                padded.append(ln + ' ' * (term_w - len(ln)))
            else:
                padded.append(ln[:term_w])
        return padded

    def handle_key(self, ch: str, selected_player: Optional[Player] = None) -> Dict[str, Optional[object]]:
        """Handle a keypress forwarded from InventoryScreen.run.

        Returns a dict with optional keys:
        - 'handled': bool (True if overlay consumed key)
        - 'close': bool (True if overlay should be closed)
        - 'message': Optional[str] (message to show after action)
        """
        def _is_up(k: str) -> bool:
            return k == getattr(readchar.key, 'UP', None) or k in ('\x1b[A', '\x1bOA', '\x00H', '\xe0H')

        def _is_down(k: str) -> bool:
            return k == getattr(readchar.key, 'DOWN', None) or k in ('\x1b[B', '\x1bOB', '\x00P', '\xe0P')

        def _is_delete(k: str) -> bool:
            return k == getattr(readchar.key, 'DELETE', None) or k in ('\x7f', )

        def _is_enter(k: str) -> bool:
            return k == getattr(readchar.key, 'ENTER', None) or k in ('\r', '\n')

        def _is_esc(k: str) -> bool:
            return k == getattr(readchar.key, 'ESC', None) or k == '\x1b'

        # cancel
        if _is_esc(ch):
            return {'handled': True, 'close': True}

        # change filter via +/- like SelectAbilityScreen
        if ch in ('-', '+', '='):
            if ch == '-':
                self.type_index = (self.type_index -1) % len(self.type_filters)
            else:
                self.type_index = (self.type_index +1) % len(self.type_filters)
            return {'handled': True, 'close': False, 'message': f'filter:{self.type_filters[self.type_index]}'}

        # delete/discard — pass current filter so the selected index maps to filtered view
        if _is_delete(ch):
            current_filter = None if self.type_filters[self.type_index] == 'all' else self.type_filters[self.type_index]
            removed = self.service.discard_selected(item_type_filter=current_filter)
            return {'handled': True, 'close': False, 'message': 'discarded' if removed else 'nothing'}

        # navigate up
        if _is_up(ch):
            current_filter = None if self.type_filters[self.type_index] == 'all' else self.type_filters[self.type_index]
            self.service.move_up(item_type_filter=current_filter)
            return {'handled': True, 'close': False}

        # navigate down
        if _is_down(ch):
            current_filter = None if self.type_filters[self.type_index] == 'all' else self.type_filters[self.type_index]
            self.service.move_down(item_type_filter=current_filter)
            return {'handled': True, 'close': False}

        # use/enter
        if _is_enter(ch):
            current_filter = None if self.type_filters[self.type_index] == 'all' else self.type_filters[self.type_index]
            ctx = self.service.get_view_context(item_type_filter=current_filter)
            if ctx['total'] ==0:
                return {'handled': True, 'close': False, 'message': 'empty'}
            inv_idx = ctx['selected_index']
            item = ctx['inventory'][inv_idx]

            # If utility item, apply to selected_player via Player.use_item()
            if isinstance(item, UtilityItem):
                if selected_player is None:
                    return {'handled': True, 'close': False, 'message': 'no_target_player'}
                
                full_inv = list(self.player_game.inventory)
                full_idx = full_inv.index(item)
                res = selected_player.use_item(full_idx, self.player_game)
                
                return {'handled': True, 'close': False, 'message': f'{selected_player.name} used {item.name}, {res["note"]}'}

            # non-utility: no-op
            return {'handled': True, 'close': False, 'message': f"Cannot 'use' {item.name} here."}

        # unhandled: ignore other keys
        return {'handled': False}
