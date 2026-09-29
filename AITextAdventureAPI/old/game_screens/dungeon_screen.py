from typing import List
import random
import os
from readchar import readkey, key

from game_screens.inventory_screen import InventoryScreen
from combat_balancing_simulation.combat_simulator import CombatSimulation
from combat_balancing_simulation.combat_simulator_screen import CombatScreen

from run_combat_simulator import generate_random_dungeon_mob

from game.objects.dungeon import Dungeon
from game.objects.player import ItemType

import game.constants as const

def _clear_screen() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def _create_dialog_box(text: str, width: int) -> List[str]:
    """
    Create a dialog box with wrapped text.
    contain it in * characters.
    """
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= width - 4:  # 4 for borders
            if current_line:
                current_line += " "
            current_line += word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    # Create the box
    box = []
    border = '*' * width
    box.append(border)
    for line in lines:
        padded_line = line.ljust(width - 4)  # 4 for borders
        box.append(f"* {padded_line} *")
    box.append(border)
    return box

def _render_minimap(d: Dungeon, reveal_all: bool = False, dialog_display: str = None) -> None:
    """Render a centered minimap framed by '#' characters.

    - Display size:74x25 characters total (including border).
    - Interior size:72x23 characters.
    - Center the view on player_pos (x,y) at z level.
    - If reveal_all is False only tiles with tile.discovered==True are shown; others show '?'.
    - Passable tiles: '.'
    - Impassable tiles: 'X'
    - Unrevealed tiles: '?'
    - Empty (no tile): ' ' (but a perimeter '*' will be drawn where empty neighbors a floor)
    - NPCs: 'N' (overrides floor char)
    - Player: '☺' (drawn at center cell)
    """
    _clear_screen()
    print(f"{d.display_name}. use arrows to move, (space)-interact {{ß,#}}, (i)nventory, ctrl+c to quit...sissy")
    player_pos = d.get_player_pos()

    # display geometry
    total_w, total_h =74,25
    inner_w, inner_h = total_w -2, total_h -2

    px, py, pz = player_pos
    z = pz

    # compute world coordinate of top-left interior cell so player is centered
    ox = int(px - inner_w //2)
    oy = int(py - inner_h //2)

    # prepare interior grid
    grid: List[List[str]] = [[" " for _ in range(inner_w)] for _ in range(inner_h)]

    # fill grid from dungeon tiles
    for gy in range(inner_h):
        for gx in range(inner_w):
            wx = ox + gx
            wy = oy + gy

            # unmapped cell
            tile = d.get_tile(wx, wy, z)
            if tile is None:
                grid[gy][gx] = " "
                continue

            # if tile exists
            visible = reveal_all or tile.discovered
            if not visible:
                grid[gy][gx] = '?'
                continue

            # visible tile: mark NPCs first
            #dungeon.impassable_tile
            #dungeon.open_area_tile
            ch = d.open_area_tile if tile.passable else d.impassable_tile

            if tile.entities:
                # prefer showing NPC marker when present
                for ent in tile.entities:
                    if isinstance(ent, dict) and ent.get('type') == 'npc':
                        ch = 'ß'
                        break
                    if isinstance(ent, ItemType):
                        ch = '◘'

            # stairs markers override floor/impassable and entity marks for visibility
            # show both directions if present
            if getattr(tile, 'has_stairs_up', False) and getattr(tile, 'has_stairs_down', False):
                ch = '↕'
            elif getattr(tile, 'has_stairs_up', False): # reverse images so floors appear to go deeper
                ch = '↓'
            elif getattr(tile, 'has_stairs_down', False):
                ch = '↑'

            # if is origin (0,0,0) mark with 'O' (distinct from stairs)
            if wx ==0 and wy ==0 and z ==0:
                ch = '↑'#'O'   # arrows are more fun than o's

            grid[gy][gx] = ch


    # mark perimeter: any empty cell adjacent (4-dir) to a non-empty cell becomes '*'
    for gy in range(inner_h):
        for gx in range(inner_w):
            if grid[gy][gx] != ' ':
                continue
            # check4 neighbors
            adjacent_floor = False
            for dx, dy in ((1,0), (-1,0), (0,1), (0, -1)):
                nx, ny = gx + dx, gy + dy
                if 0 <= nx < inner_w and 0 <= ny < inner_h:
                    tile = d.get_tile(nx + ox, ny + oy, z)
                    if tile and (reveal_all or tile.discovered):
                        adjacent_floor = True
                        break
            if adjacent_floor:
                grid[gy][gx] = '*'

    # replace all ' ' with '?'
    for gy in range(inner_h):
        for gx in range(inner_w):
            if grid[gy][gx] == ' ':
                grid[gy][gx] = '?'

    # put player marker in center (if inside view)
    center_x = inner_w //2
    center_y = inner_h //2
    if 0 <= center_x < inner_w and 0 <= center_y < inner_h:
        grid[center_y][center_x] = '☺'

    # if dialog_display is set, create dialog box 2/3 width and overlay it
    if dialog_display:
        dialog_rows = _create_dialog_box(dialog_display, total_w * 2 // 3)
        dialog_h = len(dialog_rows)
        dialog_w = len(dialog_rows[0]) if dialog_h >0 else 0
        dialog_ox = (inner_w - dialog_w) //2
        dialog_oy = (inner_h - dialog_h) //2
        for dy in range(dialog_h):
            for dx in range(dialog_w):
                ch = dialog_rows[dy][dx]
                gx = dialog_ox + dx
                gy = dialog_oy + dy
                if 0 <= gx < inner_w and 0 <= gy < inner_h:
                    grid[gy][gx] = ch

    # print framed map
    print('#' * total_w)
    for row in grid:
        line = ''.join(row)
        print('#' + line + '#')
    print('#' * total_w)

    print (f'Player Pos: {player_pos} | Entities: {d.get_all_entity_locations()}')
    # Debug: list stair locations on current floor z
    stair_positions = []
    for (tx, ty, tz), t in d.tiles.items():
        if tz == z and (getattr(t, 'has_stairs_up', False) or getattr(t, 'has_stairs_down', False)):
            dirs = ''
            if getattr(t, 'has_stairs_up', False):
                dirs += 'U'
            if getattr(t, 'has_stairs_down', False):
                if dirs:
                    dirs += '/'
                dirs += 'D'
            stair_positions.append(f"({tx},{ty}:{dirs})")
    if stair_positions:
        print(f"Stairs on floor {z}: " + ", ".join(stair_positions))
    else:
        print(f"Stairs on floor {z}: none")

    # end _render_minimap

def _check_for_random_mob_encounter(player_game, hostile_seeds, force_combat = False) -> List[object]: # object is RandomHostile
	rng = random.Random()

	if rng.random() < 0.08 or force_combat:  # 8% chance of encounter
		return generate_random_dungeon_mob(3, player_game.get_max_character_level(), hostile_seeds)
	
	return []

def _simulate_check_random_encounter(dungeon, player_game, force_combat = False):
    dungeon_setting  = None
    for ds in const.DUNGEON_SETTINGS:
        if ds['dungeon_id'] == dungeon.id:
            dungeon_setting = ds
            break
    hostile_seeds = dungeon_setting.get('hostile_seeds', {}) if dungeon_setting else {}

    hostiles = _check_for_random_mob_encounter(player_game, hostile_seeds, force_combat=force_combat)

    players_won = True
    if hostiles and len(hostiles) >0:
        #COMABT SIMULATION IS HANDED A PLAYER GAME  AND HOSTILE OBJECTS as defined in game.objects.player and game.objects.random_hostile
        sim = CombatSimulation(player_game, hostiles)

        # Use CombatScreen to render the UI and handle player input/menus
        screen = CombatScreen (width=220,height=60)
        # set optional per-side widths to control layout precisely
        screen.player_w = 50
        screen.hostile_w = 50
        players_won = screen.run(sim)

    return players_won

def run_dungeon_screen(dungeon: Dungeon, pg, player_pos: tuple) -> None:
    dungeon.set_player_pos(*player_pos)

    
    took_action = False
    while True:        
        if pg.info_dialogs and len(pg.info_dialogs) > 0:
            while len(pg.info_dialogs) > 0:
                display_dialog_text = pg.pop_dialog()
                _render_minimap(dungeon, dialog_display = display_dialog_text)
                readkey()
                _clear_screen() 

        #EVENT DRIVEN ENCOUNTER CHECKS
        if pg.pending_fight_mob_id:
            mob_id = pg.pending_fight_mob_id
            #print (f'Preparing for boss mob encounter: {mob_id}...press Enter to continue...')
            mob = dungeon.get_boss_mob(pg, mob_id)
            #input (f'Preparing for boss mob encounter: {mob}...press Enter to continue...')
            if mob:
                #print (f"A hostile mob '{mob_id}' appears!")
                sim = CombatSimulation(pg, mob)
                screen = CombatScreen (width=220,height=60)
                # set optional per-side widths to control layout precisely
                screen.player_w = 50
                screen.hostile_w = 50
                #print (f"Starting combat with '{mob_id}'...")
                players_won = screen.run(sim)
                #input ('Combat ended...press Enter to continue...')

                if not players_won:
                    break
                else:
                    #input (f"You have defeated the boss mob '{mob_id}'! Press Enter to continue...")
                    pg.check_complete_boss_mob(mob_id)
                    continue

        elif took_action:
            is_combat = pg.countdown_random_encounter_timer()
            if is_combat:
                hostile = _simulate_check_random_encounter(dungeon, pg, force_combat=True)
                #input('check random encoutner...press Enter to continue...')
                if pg.is_alive() == False:
                    break

        _render_minimap(dungeon)
        cmd = readkey()

        # move handling
        dx = dy = dz =0
        if cmd in (key.UP): # map 'up' as north in2D
            dy = -1
        elif cmd in (key.DOWN):
            dy =1
        elif cmd in (key.RIGHT):
            dx =1
        elif cmd in (key.LEFT):
            dx = -1
        elif cmd == 'd': # reverse z for up/down to match stairs arrows so dungeon floors go down
            dz =1
        elif cmd == 'u':
            dz = -1
        elif cmd == 'i':
            screen = InventoryScreen()
            screen.can_save = False
            #RUN THE TEST
            #try:
            screen.run(pg)
            # except Exception as e:
            #     print(f"Error running inventory screen: {e}")
            #     input("Press Enter to continue...")
            # handle_inventory_menu(pg.characters[0], pg)
            took_action = True
            continue
        elif cmd == ' ':
            # Interact with entities on the player's tile and adjacent tiles (4-dir).
            # - Items (ItemType) will be picked up and removed from the tile if inventory has space.
            # - NPC dicts (type == 'npc') will trigger dungeon NPC meeting checks.
            # We'll check the current tile and the four adjacent tiles.
            px, py, pz = dungeon.get_player_pos()
            dirs = [(0,0), (1,0), (-1,0), (0,1), (0, -1)]
            any_interacted = False
            for ddx, ddy in dirs:
                tx, ty, tz = px + ddx, py + ddy, pz
                adj_tile = dungeon.get_tile(tx, ty, tz)
                if not adj_tile or not adj_tile.entities:
                    continue

                # iterate over a copy since we may modify the list
                for ent in list(adj_tile.entities):
                    # NPC interaction: expected as dict with 'type': 'npc' and 'npc_id'
                    if isinstance(ent, dict) and ent.get('type') == 'npc':
                        npc_id = ent.get('npc_id')                        
                        if npc_id:
                            # let PlayerGame handle meet/task completion logic
                            #print(f'Interacting with NPC {npc_id}...')
                            pg.check_meet_npc_dungeon(npc_id)
                            #input('Press Enter to continue...')
                        any_interacted = True

                    # Item pickup: instances of ItemType
                    elif isinstance(ent, ItemType):
                        picked = pg.pick_up_item(ent)
                        if picked:
                            # remove the item entity from tile
                            adj_tile.entities.remove(ent)
                            
                            # inform player
                            name = getattr(ent, 'name', getattr(ent, 'id', 'an item'))
                            pg.add_info_dialog_line(None, f"Picked up {name}.")
                        else:
                            pg.add_info_dialog_line(None, f"Cannot pick up {getattr(ent, 'name', getattr(ent, 'id', 'item'))}: inventory full.")
                        any_interacted = True





        else:
            print('Unknown command. Type help for commands.')
            continue

        if dx != 0 or dy !=0 or dz !=0:
            # compute new position
            x, y, z = dungeon.get_player_pos()
            nx, ny, nz = x + dx, y + dy, z + dz
            if not dungeon.in_bounds(nx, ny, nz):
                print('Out of bounds.')
                continue

            nt = dungeon.get_tile(nx, ny, nz)
            if not nt or not nt.passable or (nt.entities and len(nt.entities) > 0):
                print('Cannot move there (impassable).')
                continue

            # move
            dungeon.move_player(dx, dy, dz)
            took_action = True

            if dungeon.is_player_at_exit():
                # A locked dungeon traps the player: surface the locked_text and
                # keep them inside instead of leaving.
                if dungeon.is_locked():
                    pg.add_dungeon_standing_text(dungeon)
                    while len(pg.info_dialogs) > 0:
                        print(pg.pop_dialog())
                    continue
                # Clear the authoritative presence flag on a real exit so the
                # overworld loop doesn't immediately re-enter this dungeon.
                if getattr(pg, "active_dungeon", None) is dungeon:
                    pg.active_dungeon = None
                break