"""
Enhanced terminal combat screen with fixed character-frame approximating640x480 and strict '*' framing.
- Frame defaults to160x60 characters (approx640x480 pixels at4px per char)
- Left column reserved for4 player slots; placeholders shown if fewer players
- Right column for stacked hostiles
- Center column for pull-out menus, instructions and popups
- Every content row is bordered with '*' on left/right and full-star top/bottom borders
"""
from typing import List, Dict, Any, Optional
import math
import time
import sys
import os
import fnmatch

# try to use readchar for single-key input
import readchar

from combat_balancing_simulation.combat_simulator import Unit, CombatSimulation
from combat_balancing_simulation.player_details_screen import format_player_summary, format_player_sections, highlight_box as _highlight_player_box
from combat_balancing_simulation.hostile_details_screen import format_hostile_summary_compact, highlight_box as _highlight_hostile_box
from game.objects.random_hostile import RandomHostile
from game.objects.utility_item import UtilityItem
#import game.constants_other as const_other
import game.status_utils as status_utils


def clear_screen() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def _getch(prompt: str = "") -> str:   # SCREENS NEED INPUT - SHOULD BY IN IO FILE
    """Read a single key (or fallback to input())."""
    sys.stdout.write(prompt)
    sys.stdout.flush()
    ch = readchar.readkey()
    # map arrows to simple markers
    if ch == readchar.key.LEFT:
        return '<'
    if ch == readchar.key.RIGHT:
        return '>'
    if ch == readchar.key.ESC:
        return 'esc'

    return ch


class MenuState:
    def __init__(self, items: List[Dict[str, Any]], title: str = "Menu"):
        self.items = items or []
        self.title = title
        self.page =0
        self.page_size =5

    @property
    def total_pages(self) -> int:
        return max(1, math.ceil(len(self.items) / self.page_size))

    def current_page_items(self) -> List[Dict[str, Any]]:
        start = self.page * self.page_size
        return self.items[start: start + self.page_size]


class CombatScreen:
    def __init__(self, width: int =140, height: int =60): #320 ascii characters wide x240 rows high
        # width ~320 cols (approx1280 px), height ~240 rows (approx960 px)
        self.width = width
        self.height = height
        # configurable per-window widths (caller may override)
        # if left/right are not provided, they'll be derived at render time
        self.player_w: Optional[int] = None
        self.hostile_w: Optional[int] = None
        # internal working widths used by render/_make_player_box
        self.left_w: int = max(20, (self.width //6))
        self.right_w: int = max(20, (self.width //6))
        self.mid_w: int = max(10, self.width - self.left_w - self.right_w -4)
        # UI state
        self.dropdown_state: Dict[int, Dict[str, Any]] = {} # player_id -> {'type': 'ability'|'inventory', 'page':0}
        # message log: chronological list of event strings (oldest first)
        self.message_queue: List[str] = []
        # track active player to reset page when changed
        self.current_active_player_key: Optional[str] = None

    def clear(self) -> None:
        print(chr(27) + "[2J" + chr(27) + "[H", end="")

    def _hp_bar(self, cur: int, mx: int, width: int =20) -> str:
        if mx <=0:
            return '[No HP]'
        filled = int(round((cur / mx) * width))
        filled = max(0, min(width, filled))
        return '[' + '#' * filled + '-' * (width - filled) + f'] {cur}/{mx}'

    def _select_target(self, sim: CombatSimulation, unit: Unit, header_text: Optional[str] = None, prefer_friendlies: Optional[bool] = None, allow_multi: bool = False) -> Optional[Unit]:
        """Display a centered target selection dialog and return the selected Unit or None.

        The modal lists either hostiles or friendlies (toggle with left/right). If
        `prefer_friendlies` is provided it selects the initial list accordingly.
        Width is computed from the longest visible line + padding and clamped to
        the center column width so the box no longer mis-sizes.
        """
        # gather alive units and split allies/hostiles relative to the acting unit
        all_units = [u for u in sim.units if u.is_alive()]
        if not all_units:
            return None
        allies = [u for u in all_units if u._is_player() == unit._is_player()]
        hostiles = [u for u in all_units if u._is_player() != unit._is_player()]

        # initial mode selection
        if prefer_friendlies is True:
            mode = 'friendlies'
        elif prefer_friendlies is False:
            mode = 'hostiles'
        else:
            mode = 'hostiles' if hostiles else 'friendlies'

        def get_list_for_mode(m: str):
            lst = hostiles if m == 'hostiles' else allies
            names = [u.entity.name for u in lst]
            return lst, names

        base_prompt = header_text or 'select a number or esc'

        def build_box(m: str):
            visible_units, visible_names = get_list_for_mode(m)
            prompt = f"{base_prompt} ({'hostiles' if m == 'hostiles' else 'friendlies'})"
            # compute inner content width from prompt and option lines
            option_lines = [f"{i}) {n}" for i, n in enumerate(visible_names, start=1)] if visible_names else ['None']
            inner_max = max([len(prompt)] + [len(x) for x in option_lines])
            # clamp inner_max to available inner width inside the center column
            # available inner width = (self.mid_w -4) (accounting for box border)
            avail_inner = max(6, (getattr(self, 'mid_w', max(20, self.width -40)) -4))
            if inner_max > avail_inner:
                inner_max = avail_inner
            # inner content area includes2 padding spaces (left/right)
            content_area = inner_max +2
            # box width must fit inside center column (self.mid_w)
            box_w = min(self.mid_w, max(20, content_area +4))
            inner_w = box_w -4

            border = '*' * box_w
            lines: List[str] = [border, f"*{prompt.center(box_w -2)}*", border]
            if allow_multi:
                lines.append(f"* {'Press (a) to select ALL targets'.center(inner_w)} *")
                lines.append(border)
            if not visible_names:
                lines.append(f"* {'None'.ljust(inner_w)} *")
                lines.append(border)
                return lines, visible_units
            for idx, name in enumerate(visible_names, start=1):
                label = f"{idx}) {name}"
                for i in range(0, len(label), inner_w):
                    chunk = label[i:i+inner_w]
                    lines.append(f"* {chunk.ljust(inner_w)} *")
            lines.append(border)
            return lines, visible_units

        # Build initial box
        box_lines, visible_units = build_box(mode)
        box_w = len(box_lines[0]) if box_lines else max(20, min(self.mid_w,40))

        # Fallback clear-screen mode (no cached columns)
        if not hasattr(self, '_last_center_lines'):
            term = os.get_terminal_size()
            term_w = term.columns

            left_pad = max(0, (term_w - box_w) //2)
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')

            # draw initial
            box_lines, visible_units = build_box(mode)
            for ln in box_lines:
                print(' ' * left_pad + ln)

            # input loop
            while True:
                ch = _getch()
                if not ch:
                    continue
                if ch == 'esc' or (isinstance(ch, str) and ch.lower() == 'q'):
                    return None
                # allow choosing all targets when requested (press 'a')
                if allow_multi and (ch == 'a' or ch == 'A'):
                    # return the underlying visible_units list to indicate 'all'
                    return visible_units
                if ch == '<' or ch == '>':
                    mode = 'friendlies' if mode == 'hostiles' else 'hostiles'
                    box_lines, visible_units = build_box(mode)
                    if os.name == 'nt':
                        os.system('cls')
                    else:
                        os.system('clear')
                    for ln in box_lines:
                        print(' ' * left_pad + ln)
                    continue
                s = str(ch).strip()
                if s.isdigit():
                    val = int(s)
                    if 1 <= val <= len(visible_units):
                        # always return a list of targets (single selection -> single-entry list)
                        return [visible_units[val -1]]
                    continue

        # Overlay mode using cached composed columns
        left_lines = list(self._last_left_lines)
        center_lines = list(self._last_center_lines)
        right_lines = list(self._last_right_lines)
        content_rows = int(self._last_content_rows)

        overlay_center = [' ' * self.mid_w for _ in range(content_rows)]

        box_lines, visible_units = build_box(mode)
        start_row = max(0, (content_rows - len(box_lines)) //2)
        for i, bl in enumerate(box_lines):
            if start_row + i >= content_rows:
                break
            overlay_center[start_row + i] = bl.center(self.mid_w)[:self.mid_w]

        # render overlay
        clear_screen()
        self.clear()
        print('*' * self.width)
        title = f" {header_text or 'TARGET SELECTION'} "
        print('*' + title.center(self.width -2) + '*')
        print('*' * self.width)
        self.render_screen(left_lines, overlay_center, right_lines, self._last_player_box_w, self._last_hostile_box_w, content_rows, getattr(self, '_last_queue', []))

        # input loop overlayed
        while True:
            ch = _getch()
            if not ch:
                continue
            if ch == 'esc' or (isinstance(ch, str) and ch.lower() == 'q'):
                self.render(sim, active_unit=unit)
                return None
            # allow choosing all targets when requested (press 'a' or 'A')
            if allow_multi and (ch == 'a' or ch == 'A'):
                self.render(sim, active_unit=unit)
                return visible_units
            if ch == '<' or ch == '>':
                mode = 'friendlies' if mode == 'hostiles' else 'hostiles'
                box_lines, visible_units = build_box(mode)
                overlay_center = [' ' * self.mid_w for _ in range(content_rows)]
                start_row = max(0, (content_rows - len(box_lines)) //2)
                for i, bl in enumerate(box_lines):
                    if start_row + i >= content_rows:
                        break
                    overlay_center[start_row + i] = bl.center(self.mid_w)[:self.mid_w]
                clear_screen()
                self.clear()
                print('*' * self.width)
                print('*' + title.center(self.width -2) + '*')
                print('*' * self.width)
                self.render_screen(left_lines, overlay_center, right_lines, self._last_player_box_w, self._last_hostile_box_w, content_rows, getattr(self, '_last_queue', []))
                continue
            s = str(ch).strip()
            if s.isdigit():
                val = int(s)
                if 1 <= val <= len(visible_units):
                    self.render(sim, active_unit=unit)
                    # single selection: return as single-entry list
                    return [visible_units[val -1]]
            continue

    def render(self, sim: CombatSimulation, active_unit: Optional[Unit] = None, menu_open: Optional[Dict[str, Any]] = None) -> None:

        players = [u for u in sim.units if u._is_player()]
        hostiles = [u for u in sim.units if not u._is_player()]
        # sort by remaining countdown
        queue = sorted([u for u in sim.units if u.is_alive()], key=lambda u: u.next_action_in)

        # compute column widths dynamically so caller can control player/hostile window sizes
        # if specific widths supplied use them, otherwise derive reasonable defaults
        if getattr(self, 'player_w', None):
            self.left_w = max(20, int(self.player_w))
        else:
            # default left width: approx1/6 of total width
            self.left_w = max(20, self.width //6)
        if getattr(self, 'hostile_w', None):
            self.right_w = max(20, int(self.hostile_w))
        else:
            # default right width: match left
            self.right_w = max(20, self.width //6)
        # center width must be what's left inside the frame (subtract2 for spaces between columns)
        self.mid_w = max(10, self.width - self.left_w - self.right_w -4)

        # ensure we always show4 player slots
        player_slots: List[Optional[Unit]] = []
        for i in range(len(players)):
            player_slots.append(players[i] if i < len(players) else None)

        # Build boxed player summaries using formatter (preserves their internal '*' borders)
        player_box_w = max(20, int(self.player_w or (self.width //6)))
        hostile_box_w = max(20, int(self.hostile_w or (self.width //6)))

        player_boxes: List[List[str]] = []
        
        # the player box has a state based on the players game actions; 
        # the abilities, inventory and attributes_equipment boxes can be opened individually for only the active player
        # always default all boxes to collapsed.

        abl_pmt = "a(b)ility" if active_unit is None or 'silence' not in [s.get('id') for s in (active_unit.entity.statuses or [])] else "(silence)"
        action_box = [
            f"***************",
            f"*  a)ttack    *",
            f"*  {abl_pmt}  *",
            f"*  u)tility   *",
            f"***************"
        ]
        collapse_dropdowns = True #player_box_w <40 or self.width < (self.left_w + self.right_w +40)
        for ps in player_slots:
            if ps is None:
                # minimal empty boxed representation
                empty = ['*' + ' ' * (player_box_w -2) + '*'] *3
                player_boxes.append(empty)
            else:
                player_obj = ps.entity
                # when collapsing dropdowns we still want to honor explicit dropdown_state
                # so format_player_sections will render either collapsed header or the expanded menu
                # use player name as dropdown_state key to avoid relying on Unit.id
                player_key = getattr(player_obj, 'name', None)
                ds = self.dropdown_state.get(player_key) or {'type': None, 'page':1}

                current_page = ds.get('page',1)
                sections = format_player_sections(player_obj, sim.player_game, player_box_w, is_selection_window=True, page_size=5, current_page=current_page)
                lines: List[str] = []
                # If ds exists but has explicit None type, only show the header section
                lines.extend(sections.get('header', []))
                lines.extend(sections.get('stats', []))
                if ds.get('type') == 'abilities':
                    lines.extend(sections.get('abilities', []))
                elif ds.get('type') == 'inventory':
                    lines.extend(sections.get('inventory', []))
                elif ds.get('type') == 'attributes':
                    lines.extend(sections.get('attributes_equipment', []))

                # Only append the action_box popup to the active player's box
                if active_unit is not None and ps.entity == active_unit.entity:
                    for i in range(len(lines)):
                        if i < len(action_box):
                            lines[i] = lines[i] + ' ' + action_box[i]

                player_boxes.append(lines)

        # Hostile boxes: stack per hostile
        hostile_boxes: List[List[str]] = []
        for h in hostiles:
            ent = getattr(h, 'entity', None)
            # Strict: expect a RandomHostile instance. Let it raise if not.
            if not isinstance(ent, RandomHostile):
                raise TypeError('hostile entity must be a RandomHostile instance')
            hostile_boxes.append(format_hostile_summary_compact(ent, hostile_box_w))

        # Mark dead hostiles' boxes with 'X' borders
        for i, h in enumerate(hostiles):
            if not h.is_alive():
                hostile_boxes[i] = [ln.replace('*', 'X') for ln in hostile_boxes[i]]

        # Highlight active player's box ... replace every star in their box with #
        active_player_idx = None
        if active_unit is not None and active_unit._is_player():
            for idx, ps in enumerate(player_slots):
                if ps is not None and ps.entity == active_unit.entity:
                    active_player_idx = idx
                    break
        if active_player_idx is not None:
            # Mark dead player boxes with 'X' borders (do this before active highlight)
            for idx, ps in enumerate(player_slots):
                if ps is not None and not ps.is_alive():
                    player_boxes[idx] = [ln.replace('*', 'X') for ln in player_boxes[idx]]
            
            if active_player_idx is not None:
                # Only replace remaining '*' with '#' for the active (alive) player
                player_boxes[active_player_idx] = [
                    line.replace('*', '#') for line in player_boxes[active_player_idx]
                ]

        # Compose left column by concatenating the4 player boxes vertically
        left_col_lines: List[str] = []
        for b in player_boxes:
            left_col_lines.extend(b)
        # Determine left padding width to avoid truncating appended action popups
        left_pad_w = max(player_box_w, max((len(ln) for ln in left_col_lines), default=player_box_w))

        # Compose right column by concatenating hostile boxes vertically
        right_col_lines: List[str] = []
        for b in hostile_boxes:
            right_col_lines.extend(b)


        # merge any queued messages at top of center area (show most recent first)
        center_msgs: List[str] = []
        if self.message_queue:
            # Build event blocks for each logged message. Each event uses3 lines:
            # header '****', the centered message, footer '****'.
            # Determine base content rows not counting center events (we'll fit events into this space)
            min_content_rows = max(len(left_col_lines), len(right_col_lines), self.height -6)

            # Each logged event consumes3 lines. Calculate how many events fit into the available rows.
            max_events_fit = max(0, min_content_rows //3)

            # Select the most recent events that will fit (avoid slicing mid-event lines)
            events_to_show = self.message_queue[-max_events_fit:] if max_events_fit >0 else []

            event_lines: List[str] = []
            for ev in events_to_show:
                header = '****'.center(self.mid_w)[:self.mid_w]
                msgline = str(ev).center(self.mid_w)[:self.mid_w]
                footer = header
                event_lines.extend([header, msgline, footer])
            
            # Determine total content height (available rows inside frame)
            content_rows = max(len(left_col_lines), len(right_col_lines), len(event_lines), self.height -6)

            # Use the built event_lines (already limited to whole events)
            center_lines = event_lines

            # Pad columns to content_rows
            def pad(col: List[str], w: int) -> List[str]:
                out = [ln.ljust(w)[:w] for ln in col]
                if len(out) < content_rows:
                    out.extend([' ' * w for _ in range(content_rows - len(out))])
                return out[:content_rows]

            left_lines = pad(left_col_lines, left_pad_w)
            right_lines = pad(right_col_lines, hostile_box_w)
            center_lines = pad(center_lines, self.mid_w)

            # --- ACTION POPUP: render a small starred box next to the active player's name bar ---
            # popup will be aligned vertically to the header line of the player's boxed summary
            action_box_offset = 0
            if active_player_idx is not None and active_unit is not None and active_unit._is_player():
                # compute header row index in left_lines
                header_row =0
                for j in range(active_player_idx):
                    header_row += len(player_boxes[j])
                # header_row is now the index of the active players name in left_lines
                # insert a small popped-up box to the right of their name
                # action box is positioned relative to header row
                action_box_offset = header_row
                for ai, action_line in enumerate(action_box):
                    if ai >= content_rows:
                        break
                    # markup active player row with '*'
                    left_lines[action_box_offset + ai] = left_lines[action_box_offset + ai][:left_pad_w] + '*' + left_lines[action_box_offset + ai][left_pad_w+1:]
                center_lines = center_lines[:content_rows]

        else:
            # default center help lines when no messages are queued
            center_lines_raw = [
                f"Currently active: {getattr(active_unit.entity, 'name', '(unit)') if active_unit else '(none)'}"
            ]
            center_lines = [ln.center(self.mid_w)[:self.mid_w] for ln in center_lines_raw]
            content_rows = max(len(left_col_lines), len(right_col_lines), len(center_lines), self.height -6)
            
            # helper to pad any column to content_rows
            def pad(col: List[str], w: int) -> List[str]:
                out = [ln.ljust(w)[:w] for ln in col]
                if len(out) < content_rows:
                    out.extend([' ' * w for _ in range(content_rows - len(out))])
                return out[:content_rows]

            left_lines = pad(left_col_lines, left_pad_w)
            right_lines = pad(right_col_lines, hostile_box_w)
            # center needs to be fixed-width too
            center_lines = pad(center_lines, self.mid_w)

        # draw full framed output
        clear_screen()
        self.clear()
        print('*' * self.width)
        title = f" Combat - Time: {sim.time:.2f} "
        print('*' + title.center(self.width -2) + '*')
        print('*' * self.width)

        # delegate actual row rendering to helper which supports center overlay
        # pass left_pad_w so render_screen knows the actual left column width
        # Cache the last-composed columns so selection dialogs can overlay without clearing terminal
        self._last_left_lines = left_lines
        self._last_center_lines = center_lines
        self._last_right_lines = right_lines
        self._last_player_box_w = left_pad_w
        self._last_hostile_box_w = hostile_box_w
        self._last_content_rows = content_rows
        self._last_queue = queue

        self.render_screen(left_lines, center_lines, right_lines, player_box_w, hostile_box_w, content_rows, queue)

    def render_screen(self, left_lines: List[str], center_lines: List[str], right_lines: List[str], player_box_w: int, hostile_box_w: int, content_rows: int, queue: List[Unit]) -> None:
        # Optionally overlay a centered queue box into the center column so it appears
        # as part of the main content (instead of printed below the border).

        # make a mutable copy
        center_overlay = list(center_lines)
        # build queue display names (limit to8 like the prior helper)
        disp = [getattr(u.entity, 'name', '(unit)') for u in queue[:8]]
        # determine box width to fit inside center column
        box_w = min(self.mid_w -2, max(10, max((len(s) for s in disp), default=0) +4)) if self.mid_w >8 else self.mid_w
        inner_w = box_w -2

        # build box lines (local, no global printing)
        q_lines: List[str] = []
        border = '*' * box_w
        q_lines.append(border)
        for i, n in enumerate(disp):
            marker = '#' if i ==0 else ' '
            line = f"{marker} {n}"
            q_lines.append('*' + line.ljust(inner_w) + '*')
        q_lines.append(border)

        # place the queue box at the bottom of the center column (just above the bottom border)
        start_row = max(0, content_rows - len(q_lines))
        # If the queue box would overlap non-empty center content (e.g. recent messages),
        # shift the center content up by the height of the queue box so messages remain visible.
        qh = len(q_lines)
        if qh >0:
            overlap_start = max(0, content_rows - qh)
                
            overlap_nonspace = any(center_overlay[r].strip() != '' for r in range(overlap_start, content_rows))
                
            if overlap_nonspace:
                # shift everything up by qh lines; drop top-most lines if necessary
                center_overlay = center_overlay[qh:] + [' ' * self.mid_w for _ in range(qh)]
                # recompute start_row (should now be content_rows - qh still)
                start_row = max(0, content_rows - qh)

        for i, ql in enumerate(q_lines):
            row_idx = start_row + i
            if row_idx >= content_rows:
                break
            # place ql centered inside the center column width (self.mid_w)
            if len(ql) >= self.mid_w:
                placed = ql[:self.mid_w]
            else:
                left_pad = (self.mid_w - len(ql)) //2
                placed = ' ' * left_pad + ql + ' ' * (self.mid_w - left_pad - len(ql))
            center_overlay[row_idx] = placed
        center_lines = center_overlay

        # Compose rows and then print with framing
        rows = self.compose_rows(left_lines, center_lines, right_lines, content_rows)
        for row in rows:
            print('*' + row + '*')

        # bottom border
        print('*' * self.width)

    def compose_rows(self, left_lines: List[str], center_lines: List[str], right_lines: List[str], content_rows: int) -> List[str]:
        """Compose each inner row string by placing left at left edge, right at right edge,
        then overlaying center content centered across the available width. Center content
        takes precedence and overwrites characters where it appears.
        """
        inner_w = self.width -2
        out_rows: List[str] = []
        for i in range(content_rows):
            left_raw = left_lines[i] if i < len(left_lines) else ''
            center_raw = center_lines[i] if i < len(center_lines) else ''
            right_raw = right_lines[i] if i < len(right_lines) else ''

            canvas = [' '] * inner_w

            # place left content
            for j, ch in enumerate(left_raw):
                if j >= inner_w:
                    break
                canvas[j] = ch

            # place right content aligned to the right
            if right_raw:
                start_r = max(0, inner_w - len(right_raw))
                for j, ch in enumerate(right_raw):
                    pos = start_r + j
                    if 0 <= pos < inner_w:
                        canvas[pos] = ch

            # overlay center content centered across inner width
            if center_raw:
                if len(center_raw) >= inner_w:
                    center_s = center_raw[:inner_w]
                    start_c =0
                else:
                    center_s = center_raw
                    start_c = (inner_w - len(center_s)) //2
                for j, ch in enumerate(center_s):
                    if ch != ' ':
                        pos = start_c + j
                        if 0 <= pos < inner_w:
                            canvas[pos] = ch

            out_rows.append(''.join(canvas))
        return out_rows

    def _render_queue_box_centered(self, queue: List[Unit]) -> None:
        # Build display names for queue
        disp = [getattr(u.entity, 'name', '(unit)') for u in queue[:8]]
        box_w = min(self.width -10, max(20, max((len(s) for s in disp), default=10) +4))

        inner_w = self.width -2
        left_space = max(0, (inner_w - box_w) //2)
        right_space = inner_w - box_w - left_space

        border = '*' * box_w
        # top border of inner box
        inner = ' ' * left_space + border + ' ' * right_space
        print('*' + inner + '*')
        for i, n in enumerate(disp):
            marker = '#' if i ==0 else ' '
            line = f"{marker} {n}"
            # content line with '*' border inside
            inner = ' ' * left_space + '*' + line.ljust(box_w -2) + '*' + ' ' * right_space
            print('*' + inner + '*')
        # bottom border of inner box
        inner = ' ' * left_space + border + ' ' * right_space
        print('*' + inner + '*')

    def run(self, sim: CombatSimulation) -> bool:
        menu_state: Optional[MenuState] = None
        menu_open: Optional[Dict[str, Any]] = None

        # continue cycling until one side has no living units
        while True:
            # check termination: any players and any hostiles alive?
            players_alive =sim.is_player_annhilation() # any(u._is_player() and u.is_alive() for u in sim.units)
            hostiles_alive = sim.is_hostile_annhilation() # any((not u._is_player()) and u.is_alive() for u in sim.units)
            if not players_alive or not hostiles_alive:
                # delegate win/lose handling
                return self.handle_players_win(sim, players_alive)

            while True:
                unit = sim.next_active_unit()
                if not unit:
                    print('No units in simulation')
                    break

                status_res = status_utils.get_blocking_status(unit.entity)
                if status_res is not None:
                    # unit cannot act this turn, skip to next
                    action_results = sim.perform_unit_action(unit, {'type': 'auto_skip', 'reason': status_res})
                    #process action results as messages to show in center area
                    if action_results:
                        for msg in action_results.get('messages', []):
                            # append to chronological log (oldest first). Do not drop until display limit.
                            self.message_queue.append(msg)
                            # keep an upper bound to avoid unbounded memory growth
                            if len(self.message_queue) >1000:
                                self.message_queue.pop(0)
                            # small delay to allow user to see action results before next turn
                            self.render(sim, active_unit=unit, menu_open=menu_open)
                            time.sleep(1)
                    continue                
                
                if 'confuse'  in [s.get('id') for s in (unit.entity.statuses or [])]:
                    # unit is confused: perform a backend-randomized confused action
                    #input(f"Unit {unit.entity.name} is confused. Press Enter to continue...")
                    action_results = sim.perform_unit_action(unit, {'type': 'confused'})
                    #input(f"Unit {unit.entity.name} completed confused action. Press Enter to continue...")
                    # process action results as messages to show in center area
                    if action_results:
                        for msg in action_results.get('messages', []):
                            self.message_queue.append(msg)
                            if len(self.message_queue) >1000:
                                self.message_queue.pop(0)
                            self.render(sim, active_unit=unit, menu_open=menu_open)
                            time.sleep(1)
                    # continue to next unit
                    continue

                if status_res is None:
                    # render screen
                    self.render(sim, active_unit=unit, menu_open=menu_open)
                    break

                # render screen
                self.render(sim, active_unit=unit, menu_open=menu_open)

            action_results: Optional[Dict[str, Any]] = None
            if unit._is_player():
                # simple single-key loop for player
                menu_open = None
                while True:
                    ch = _getch()
                    if not ch:
                        continue
                    if ch.lower() == 'a':
                        action_results = self.handle_player_attack(sim, unit, menu_open)
                        break
                    if ch.lower() == 'r':
                        action_results = sim.perform_unit_action(unit, {'type': 'escape'})
                        pk = getattr(unit.entity, 'name', None)
                        if pk in self.dropdown_state:
                            self.dropdown_state[pk] = {'type': None, 'page':1}

                        break
                    if ch.lower() in ('b','u'):
                        #if physical == True and 'sleep' in [s.get('id') for s in self.statuses]:
                        if ch.lower() != 'b' or  (ch.lower() == 'b' and 'silence' not in [s.get('id') for s in unit.entity.statuses]):
                            # toggle the corresponding menu for this player
                            self.handle_player_item_and_ability(sim, unit, ch, menu_open)
                            continue
                    # page left/right while menu open
                    if ch in ('<', '>'):
                        self.switch_page_ability_item_menu(unit, ch, sim)
                        continue
                    # numeric selection when dropdown open -> choose ability/item
                    if isinstance(ch, str) and ch.isdigit():
                        action_results = self.select_item_or_ability_from_menu(sim, unit, ch, menu_open)
                        if action_results is not None:
                            break
                    if ch == 'esc' or ch.lower() == 'q':
                        # clear any open dropdown for the active player
                        player_key = getattr(unit.entity, 'name', None)
                        if player_key is not None and player_key in self.dropdown_state:
                            # set to closed state and reset page
                            self.dropdown_state[player_key] = {'type': None, 'page':1}
                        menu_open = None
                        self.render(sim, active_unit=unit, menu_open=None)
                        continue
                    # otherwise loop

            else:
                # hostile automatic action
                action_results = sim.perform_unit_action(unit, {'type': 'auto'})

            #process action results as messages to show in center area
            if action_results:
                for msg in action_results.get('messages', []):
                    # append to chronological log (oldest first). Do not drop until display limit.
                    self.message_queue.append(msg)
                    # keep an upper bound to avoid unbounded memory growth
                    if len(self.message_queue) >1000:
                        self.message_queue.pop(0)
                    # small delay to allow user to see action results before next turn
                    self.render(sim, active_unit=unit, menu_open=menu_open)
                    time.sleep(1)


        print('Simulation finished')
        
    # --- Extracted helpers ---
    def handle_players_win(self, sim: CombatSimulation, players_alive: bool) -> bool:
        """Handle end-of-combat when players have won (or lost). Returns True if players won."""
        if not players_alive:
            return False

        rewards = sim.distribute_rewards()
        
        # If rewards is a flat list of messages (new behavior), display each message slowly
        self.message_queue.clear()

        for msg in rewards:
            # append to chronological log (oldest first)
            self.message_queue.append(msg)
            if len(self.message_queue) >1000:
                self.message_queue.pop(0)
            self.render(sim, active_unit=None, menu_open=None)

            time.sleep(1.5)
        return True
    
    def handle_player_attack(self, sim: CombatSimulation, unit: Unit, menu_open: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """Handle player attack keypress flow and return action_results or None."""
        targets = self._select_target(sim, unit, header_text='select target to attack', prefer_friendlies=False)
        if targets is None or len(targets) == 0:
            # cancelled, re-render and continue input loop
            self.render(sim, active_unit=unit, menu_open=menu_open)
            return None
        sel = targets
        action_results = sim.perform_unit_action(unit, {'type': 'attack', 'targets': sel})
        # close any open dropdown for this player after taking action
        pk = unit.entity.name
        if pk in self.dropdown_state:
            self.dropdown_state[pk] = {'type': None, 'page':1}

        return action_results
    
    def handle_player_item_and_ability(self, sim: CombatSimulation, unit: Unit, ch: str, menu_open: Optional[Dict[str, Any]] = None) -> None:
        """Toggle ability/inventory menu for player (key 'b' for abilities, 'u' for inventory)."""
        menu_type = 'abilities' if ch.lower() == 'b' else 'inventory'
        player_key = getattr(unit.entity, 'name', None)
        if player_key is not None:
            ds = self.dropdown_state.get(player_key) or {'type': None, 'page':1}
            if ds.get('type') == menu_type:
                ds['type'] = None
                ds['page'] =1
            else:
                ds['type'] = menu_type
                ds['page'] =1
            self.dropdown_state[player_key] = ds
            # re-render so the menu appears/updates
            self.render(sim, active_unit=unit, menu_open=menu_open)
    
    def switch_page_ability_item_menu(self, unit: Unit, ch: str, sim: CombatSimulation) -> None:
        """Handle page left/right while ability/inventory dropdown is open."""
        player_key = unit.entity.name
        if player_key:
            ds = self.dropdown_state.get(player_key)
            if ds and ds.get('type') in ('abilities', 'inventory'):
                if ds.get('type') == 'abilities':
                    items = getattr(unit.entity, 'abilities', []) or []
                else:
                    items = [it for it in (getattr(sim.player_game, 'inventory', []) or []) if isinstance(it, UtilityItem)]
                total = len(items) if items else 0
                page_size = int(ds.get('page_size',5) or 5)
                if page_size <=0:
                    total_pages = 1
                else:
                    total_pages = max(1, math.ceil(total / page_size))
                cur = int(ds.get('page',1) or 1)
                if ch == '<':
                    cur = max(1, cur -1)
                else:
                    cur = min(total_pages, cur +1)
                ds['page'] = cur
                ds['page_size'] = page_size
                self.dropdown_state[player_key] = ds
                self.render(sim, active_unit=unit, menu_open=None)
    
    def select_item_or_ability_from_menu(self, sim: CombatSimulation, unit: Unit, ch: str, menu_open: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """Handle numeric selection when dropdown open -> choose ability or item and perform action."""
        player_key = unit.entity.name
        if not player_key:
            return None
        ds = self.dropdown_state.get(player_key)
        if not ds or ds.get('type') not in ('abilities', 'inventory'):
            return None
        page = int(ds.get('page',1) or 1)
        page_size = int(ds.get('page_size',5) or 5)
        idx_on_page = int(ch) -1
        global_idx = (page -1) * page_size + idx_on_page
        if ds.get('type') == 'abilities':
            abil_list = unit.entity.abilities or []
            #input (f"abil_list: {abil_list}, global_idx: {global_idx}")
            if global_idx <0 or global_idx >= len(abil_list):
                return None
            abil = abil_list[global_idx]
            if unit.entity.current_ap < abil.ap_cost:
                return None

            prefer_f = abil._is_beneficial_ability()#  bool(self._is_beneficial_ability(abil))
            
            targets = self._select_target(sim, unit, header_text=f"select target for {abil.name}", prefer_friendlies=prefer_f, allow_multi= abil.can_aoe)
            if targets is None:
                self.render(sim, active_unit=unit, menu_open=menu_open)
                return None
            # For now, pass first target when single-target behavior expected.

            action_results = sim.perform_unit_action(unit, {'type': 'ability', 'ability': abil, 'targets': targets})
            pk = unit.entity.name
            if pk in self.dropdown_state:
                self.dropdown_state[pk] = {'type': None, 'page':1}

            return action_results
        else:
            # inventory menu shows a filtered list (utility items).
            # Map the selected index from the filtered view back to the full inventory index
            full_inv = sim.player_game.inventory
            filtered = [it for it in full_inv if isinstance(it, UtilityItem)]
            if global_idx <0 or global_idx >= len(filtered):
                return None
            selected_item = filtered[global_idx]
            itm = full_inv.index(selected_item)

            item_obj = selected_item
            item_name = item_obj.name

            prefer_f = item_obj._is_beneficial_item()

            targets = self._select_target(sim, unit, header_text=f"use {item_name}", prefer_friendlies=prefer_f)
            if targets is None:
                self.render(sim, active_unit=unit, menu_open=menu_open)
                return None
            sel = targets
            action_results = sim.perform_unit_action(unit, {'type': 'item', 'item': itm, 'targets': sel})
            pk = unit.entity.name
            if pk in self.dropdown_state:
                self.dropdown_state[pk] = {'type': None, 'page':1}

            return action_results
