"""Terminal inventory/character screen using readchar for single-key input when available.
Displays up to five player summaries across the top. Uses InventoryScreenService for logic.
"""
from random import Random
from tkinter import LEFT
from typing import List, Dict, Optional, Any
import os
import readchar
# try to use readchar for single-key input

from combat_balancing_simulation.player_details_screen import (
 format_player_summary,
 format_player_sections,
 highlight_box,
)
from game.objects.player import Player
from game_screens.inventory_screen_service import InventoryScreenService
from game_screens.select_items_screen import SelectItemsScreen
from game_screens.select_equipment_screen import SelectEquipmentScreen
from game_screens.select_ability_screen import SelectAbilityScreen
from game_screens.select_upgrade_screen import SelectUpgradeScreen
# Monster log overlay
from game_screens.monster_log_screen import MonsterLogScreen
from game_screens.npc_log_screen import NPCLogScreen
from game_screens.select_party_screen import SelectPartyScreen
from game.objects.random_hostile import RandomHostile
import game.constants as const
from combat_balancing_simulation.hostile_seed_engine import generate_hostile_from_legacy_seed


def _getch() -> str:
    """Return a single keypress. Uses readchar when available, otherwise input()."""
    ch = readchar.readkey()

    # preserve common control constants so callers receive arrow/enter/delete/esc as-is
    
    special = (
        readchar.key.UP,
        readchar.key.DOWN,
        readchar.key.LEFT,
        readchar.key.RIGHT,
        readchar.key.ESC,
        getattr(readchar.key, 'ENTER', None),
        getattr(readchar.key, 'DELETE', None),
    )
    

    if ch in special:
        return ch

    # If this is an escape sequence (starts with ESC) preserve it as-is so
    # overlay handlers that match sequences like '\x1b[A' work correctly.
    
    if isinstance(ch, str) and ch.startswith('\x1b'):
        return ch
    
    return ch.lower()

class InventoryScreen:
    def __init__(self, width: int =140, height: int =40):
        self.width = width
        self.height = height
        self.max_display =5
        self.last_message: Optional[str] = None
        self.can_save: bool = True

    def clear(self) -> None:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def _make_box_for_player(self, player: Player, player_game: Any, box_w: int, show_abilities: bool = False) -> List[str]:

        sections = format_player_sections(player, player_game, width=box_w, is_selection_window=False)

        lines: List[str] = []
        lines.extend(sections.get('header', []))
        lines.extend(sections.get('stats', []))
        lines.extend(sections.get('unused_awards', []))        
        lines.extend(sections.get('attributes_equipment', []))

        if show_abilities:
            lines.extend(sections.get('abilities', []))
        else:
            lines.append('*' * box_w)

        return lines

    def render(
        self,
        player_game: Any,
        selected_index: int =0,
        offset: int =0,
        abilities_map: Optional[Dict[int, bool]] = None,
        overlay: Optional[object] = None,
        ) -> None:
        abilities_map = abilities_map or {}
 
        
        term_w = os.get_terminal_size().columns
        term_h = os.get_terminal_size().lines
        

        players: List[Player] = list(player_game.characters)
        total = len(players)

        selected_index = max(0, min(selected_index, max(0, total -1)))
        offset = max(0, min(offset, max(0, total -1)))

        if selected_index < offset:
            offset = selected_index
        if selected_index >= offset + self.max_display:
            offset = max(0, selected_index - self.max_display +1)

        remaining = max(0, total - offset)
        display_n = min(self.max_display, remaining)
        to_show = players[offset: offset + display_n]

        per_box_w = max(20, min(40, (max(20, term_w -4) - (display_n -1)) // max(1, display_n)))

        boxes: List[List[str]] = []
        for idx, p in enumerate(to_show, start=offset):
            show_abil = bool(abilities_map.get(idx, False))
            lines = self._make_box_for_player(p, player_game, per_box_w, show_abilities=show_abil)
            if idx == selected_index:
                lines = highlight_box(lines)
            boxes.append(lines)

        heights = [len(b) for b in boxes] if boxes else [0]
        max_h = max(heights + [3])
        for i in range(len(boxes)):
            if len(boxes[i]) < max_h:
                boxes[i].extend([' ' * per_box_w for _ in range(max_h - len(boxes[i]))])

        # build a full-screen buffer (term_h lines) so the overlay can overwrite the bottom
        screen: List[str] = [" " * term_w for _ in range(max(0, term_h))]

        # top border and title
        top_border = '*' * term_w
        # determine whether to show learn/upgrade actions based on selected player's unused awards
        show_learn = False
        show_upgrade = False
        
        players_all = list(player_game.characters)
        sel_player = players_all[selected_index] if players_all else None
        if sel_player:
            up_pow = sel_player.unused_power_points
            up_stat = sel_player.unused_stat_points
            up_abil = sel_player.unused_ability_slots
            show_upgrade = (up_pow >0) or (up_stat >0)
            show_learn = (up_abil >0)
        
        
        actions = ['\u2190/\u2192 move', 'a(b)ility', '(i)tems', '(e)quip', '(p)arty']
        if self.can_save:
            actions.append('(s)ave')
        if show_learn:
            actions.append('(l)earn')
        if show_upgrade:
            actions.append('(u)pgrade stats')
        actions.append('(m)onster log')
        if not getattr(player_game, 'npc_log_locked', True):
            actions.append("(n)pc's")
        actions.append('a(r)eas')
        actions.append('esc:exit')
        title = f'Chapter: {player_game.current_chapter}| Money: {player_game.money} | Inventory - ' + ' | '.join(actions)
        header_line = '*' + title.center(term_w -2)[: term_w -2] + '*'
        screen[0] = top_border
        screen[1] = header_line.ljust(term_w)[:term_w]
        screen[2] = top_border

        # render player boxes area starting at row3
        base_row =3
        for row_idx in range(max_h):
            parts: List[str] = []
            for bi in range(len(boxes)):
                parts.append(boxes[bi][row_idx])
            line = (' ' + ' ').join(parts) if parts else ''
            inner = ('*' + line.ljust(term_w -2)[: term_w -2] + '*') if line or term_w >=2 else '*' * term_w
            # ensure we don't exceed buffer
            if base_row + row_idx < len(screen):
                screen[base_row + row_idx] = inner.ljust(term_w)[:term_w]

        footer_row = base_row + max_h
        # blank spacer / pager area
        if footer_row < len(screen):
            screen[footer_row] = ('*' + ' ' * (term_w -2) + '*')[:term_w]
        pager = f"Showing {offset +1}-{offset + display_n} of {total} characters | Selected: " + (str(selected_index +1) if total >0 else '0')
        if footer_row +1 < len(screen):
            screen[footer_row +1] = ('*' + pager.center(term_w -2)[: term_w -2] + '*')[:term_w]
        if footer_row +2 < len(screen):
            screen[footer_row +2] = ('*' + ' ' * (term_w -2) + '*')[:term_w]
        if footer_row +3 < len(screen):
            screen[footer_row +3] = top_border[:term_w]

        # If there's a last_message, render it centered in a box of '*' below the pager/footer area
        if self.last_message:
            # start message one row below the top_border (footer_row +4)
            msg_start = footer_row +4
            box_w = min(60, max(20, term_w -20))
            box_left = (term_w - box_w) //2
            inner = box_w -2
            msg = str(self.last_message)
            parts = [msg[i:i+inner] for i in range(0, len(msg), inner)] if msg else ['']
            mlines: List[str] = []
            mlines.append('*' * box_w)
            for p in parts:
                mlines.append('*' + p.center(inner)[:inner] + '*')
            mlines.append('*' * box_w)
            for i, mline in enumerate(mlines):
                if msg_start + i < len(screen):
                    screen[msg_start + i] = (' ' * box_left) + mline.ljust(box_w)

        # if there's an overlay, render its lines and write them into the bottom area of screen
        if overlay:
            # determine currently selected player to pass to overlay (for comparative stats)
            sel_player = players[selected_index] if players else None
            overlay_lines = overlay.render_overlay(term_w, term_h, selected_player=sel_player)
            ol_h = len(overlay_lines)
            start = max(0, term_h - ol_h)
            for i, ol in enumerate(overlay_lines):
                if start + i < len(screen):
                    screen[start + i] = ol[:term_w]

        # finally print the composed screen buffer
        self.clear()
        for ln in screen:
            print(ln)

    def run(self, player_game: Any, api: Any = None) -> None:
        svc = InventoryScreenService(player_game, max_display=self.max_display)
        overlay: Optional[object] = None
        overlay_active = False

        while True:
            ctx = svc.get_view_context()
            self.render(
                player_game,
                selected_index=ctx['selected_index'],
                offset=ctx['offset'],
                abilities_map=ctx['abilities_map'],
                overlay=overlay if overlay_active else None,
            )

            ch = _getch()

            # If overlay active, forward keys to it first
            if overlay_active and overlay is not None:
                # pass selected player so items apply to that player
                sel_player = None
                
                players = list(player_game.characters)
                if players and 0 <= ctx['selected_index'] < len(players):
                    sel_player = players[ctx['selected_index']]
                

                
                res = overlay.handle_key(ch, selected_player=sel_player)
                

                if res.get('handled'):
                    msg = res.get('message')
                    if msg:
                        # record as last message to display in inventory screen
                        self.last_message = str(msg)
                    # if overlay requested close, clear and redraw next loop
                    if res.get('close'):
                        overlay_active = False
                        overlay = None
                        continue
                    # handled but not closed -> force immediate redraw so UI updates (cursor movement)
                    ctx2 = svc.get_view_context()
                    self.render(
                    player_game,
                    selected_index=ctx2['selected_index'],
                    offset=ctx2['offset'],
                    abilities_map=ctx2['abilities_map'],
                    overlay=overlay if overlay_active else None,
                    )
                    continue
                else:
                    # If overlay didn't handle the key, but it is a shift+arrow sequence,
                    # consume it so the outer screen doesn't treat it as plain left/right.
                    shift_left_seqs = ('\x1b[1;2D', '\x1b[1;2;D', '\x1b[1;2;4D', '<')
                    shift_right_seqs = ('\x1b[1;2C', '\x1b[1;2;C', '\x1b[1;2;4C', '>')
                    if ch in shift_left_seqs or ch in shift_right_seqs:
                        # suppress outer handling
                        continue

            # Exit on ESC
            if ch == readchar.key.ESC:
                # print ("Are you sure you wish to exit? Any unsaved progress will be lost. (y/n)> ")
                # resp = _getch()
                # if resp == 'y' or resp == 'Y':
                return

             # If ability overlay is active, prevent horizontal movement from changing selected player
            if overlay_active and isinstance(overlay, SelectAbilityScreen):
                
                if ch == readchar.key.LEFT or ch == readchar.key.RIGHT or ch in ('\x1b[D', '\x1b[C'):
                    # consume key
                    continue
                
            if ch == readchar.key.LEFT:
                svc.move_left()
                continue

            if ch == readchar.key.RIGHT:
                svc.move_right()
                continue

            if ch == 'b':
                svc.toggle_abilities()
                continue

            if ch == 'i':
                # toggle item overlay
                if not overlay_active:
                    overlay = SelectItemsScreen(player_game, width=80)
                    overlay_active = True
                else:
                    overlay_active = False
                    overlay = None
                continue

            if ch == 'e':
                # toggle equipment overlay
                if not overlay_active:
                    overlay = SelectEquipmentScreen(player_game, width=80)
                    overlay_active = True
                else:
                    overlay_active = False
                    overlay = None
                continue

            if ch == 'p':
                # toggle party overlay
                if not overlay_active:
                    overlay = SelectPartyScreen(player_game, width=80, party_mode=True)
                    overlay_active = True
                else:
                    overlay_active = False
                    overlay = None
                continue

            if ch == 'l':
                # open ability overlay only if selected player has ability slots
                
                players_all = list(player_game.characters)
                sel_player = players_all[ctx['selected_index']] if players_all and 0 <= ctx['selected_index'] < len(players_all) else None
                
                if sel_player and int(getattr(sel_player, 'unused_ability_slots',0) or 0) >0:
                    if not overlay_active:
                        overlay = SelectAbilityScreen(player_game)
                        overlay_active = True
                    else:
                        overlay_active = False
                        overlay = None
                else:
                    self.last_message = 'No ability slots available for selected player'
                continue

            if ch == 'u':
                # toggle upgrade overlay
                if not overlay_active:
                    overlay = SelectUpgradeScreen(player_game)
                    overlay_active = True
                else:
                    overlay_active = False
                    overlay = None
                continue

            if ch == 's' and self.can_save:
                # save game via service -> ClientAPI
                res = input ('Press (enter) to save the game or type a name for your save to create that slot> ')
                if res.strip() == '':
                    ok, msg = svc.save_game(client=api)
                else:
                    ok, msg = svc.save_game(name=res.strip(), client=api)
                self.last_message = str(msg)
                
                continue

            if ch == 'm':
                # toggle monster log overlay; instantiate RandomHostile objects from player_game.enemies_slain
                if not overlay_active:
                    hostiles: List[RandomHostile] = []
                    slain_map = player_game.enemies_slain
                    for hid in list(slain_map.keys()):
                        # try to locate seed source using HOSTILE_SEED_PATHS
                        src_name = const.HOSTILE_SEED_PATHS.get(hid)
                        choice = None
                        if src_name:
                            src_list = getattr(const, src_name, None)
                            if src_list:
                                #print (f'Found hostile seed source "{src_name}" for id "{hid}"')
                                choice = next((s for s in src_list if s.get('id') == hid), None)

                        if choice:
                            rh = generate_hostile_from_legacy_seed(choice, choice.get('min_spawn_level'))

                            # lvl = choice.get('min_spawn_level',1) if choice else1
                            # rh = generate_random_hostile(None, None, player_game, choice or {'id': hid, 'name': hid}, level=lvl)
                            hostiles.append(rh)
                    overlay = MonsterLogScreen(hostiles, slain_map, width=80)
                    overlay_active = True
                else:
                    overlay_active = False
                    overlay = None
                continue
            
            if ch == 'n':
                 # toggle NPC log overlay; show NPCs from player_game.npcs
                 if not getattr(player_game, 'npc_log_locked', True):
                     if not overlay_active:
                         overlay = NPCLogScreen(player_game, width=80)
                         overlay_active = True
                     else:
                         overlay_active = False
                         overlay = None
                 continue

            # ignore other keys
            continue
