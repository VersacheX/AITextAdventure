from typing import Optional, List
from game.objects.player_game import PlayerGame
from game.objects.city import City, Tile
from readchar import readkey, key
import game.constants as const
# from services.utility_shop_service import buy as BuyItems, sell as SellItems, get_stock as GetStockItems
# from services.weapon_shop_service import buy as BuyWeapon, sell as SellWeapon, get_stock as GetStockWeapon
# from services.armor_shop_service import buy as BuyArmor, sell as SellArmor, get_stock as GetStockArmor
# from services.inn_service import buy as BuyInn,  get_stock as GetStockInn
# from services.bar_service import buy as BuyBar, get_stock as GetStockBar

from combat_balancing_simulation.combat_simulator import (
 CombatSimulation
)
from combat_balancing_simulation.combat_simulator_screen import CombatScreen
from combat_balancing_simulation.hostile_seed_engine import generate_hostile_from_legacy_seed
from services.player_movement_service import (
    check_for_random_mob_encounter
)

import os
from game.constants import ROAD, ALLEY, BUILDING, SELL_RATIO
from game_screens.shop_menu_screen import handle_shop_menu as handle_shop_screen

def clear_screen() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def create_dialog_box(text: str, width: int) -> List[str]:
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

def display_viewport(player_game: Optional[PlayerGame], region: City, view_w: int, view_h: int, dialog_display_text: str = None) -> City:
    """Render the rectangular viewport centered on player and return the
    active City/Region to use for actions (child_city if player's coord is in
    it, otherwise the region itself).

    The rendered viewport is surrounded with '*' and shows "{region} - {city}" above.
    """
    # decide active city for actions: if the player's coordinate exists in a child_city, use it
    active = region
    if hasattr(region, 'child_city') and region.child_city and (player_game.x, player_game.y) in region.child_city.tiles:
        active = region.child_city

    cur_region, cur_area = player_game.get_region_and_active_area_for_position()
    # prefer explicit region name/display_name, fall back to generic
    region_name = cur_region.display_name if cur_region else region.display_name
    # city name fallback
    city_name = cur_area.display_name if cur_area else active.display_name

    # header
    width = view_w +4
    print('*' * width)
    header = f" {region_name} - {city_name} "
    # center header within stars
    pad = max(0, width - len(header) -2)
    left = pad //2
    right = pad - left
    print('*' + ' ' * left + header + ' ' * right + '*')
    print('*' * width)

    half_w = view_w //2
    half_h = view_h //2
    start_x = player_game.x - half_w
    end_x = player_game.x + half_w
    start_y = player_game.y - half_h
    end_y = player_game.y + half_h

    # helper to pick the appropriate tile source (active city > world_tiles > region)
    def _pick_tile(tx: int, ty: int):
        if hasattr(active, 'tiles'):
            t2 = active.tiles.get((tx, ty))
            if t2 is not None:
                return t2
        t2 = player_game.world_tiles.get((tx, ty))
        if t2 is not None:
            return t2

        return region.tiles.get((tx, ty))

    display_lines = []
    for y in range(start_y, end_y +1):
        row = []
        for x in range(start_x, end_x +1):
            # prioritize aircraft. its either in flight or a little base
            if getattr(player_game, 'aircraft_location', None) == (x, y):
                # render aircraft marker (bright cyan if terminal supports)
                color_enabled = False
                if os.name != 'nt' or os.getenv('WT_SESSION') or os.getenv('TERM'):
                    color_enabled = True
                if color_enabled:
                    row.append('\x1b[1;36mA\x1b[0m')
                else:
                    row.append('A')
                continue

            # priority: player marker, aircraft marker, then tiles
            if x == player_game.x and y == player_game.y:
                # show player marker; use ANSI color when available
                color_enabled = False
                # simple heuristics: non-windows or modern Windows terminals expose WT_SESSION
                if os.name != 'nt' or os.getenv('WT_SESSION') or os.getenv('TERM'):
                    color_enabled = True
                
                if color_enabled:
                    # bright yellow @
                    row.append('\x1b[1;33m@\x1b[0m')
                else:
                    row.append('☺')
                continue



            # prefer tiles from the active city when available, otherwise try world_tiles then parent region
            t = None
            if hasattr(active, 'tiles'):
                t = active.tiles.get((x, y))
            if t is None and player_game is not None:
                # player_game.world_tiles stores the authoritative persistent world
                t = player_game.world_tiles.get((x, y))
                
            if t is None:
                t = region.tiles.get((x, y))
            if t is None:
                row.append('?')
            else:
                if t.type == ROAD:
                    left_t = _pick_tile(x -1, y)
                    up_t = _pick_tile(x, y -1)
                    right_t = _pick_tile(x +1, y)
                    down_t = _pick_tile(x, y +1)
                    row.append(get_road_or_alley_char(t, left_t, up_t, right_t, down_t))
                elif t.type == BUILDING:
                    ch = t.building.get('char') if isinstance(t.building, dict) else 'B'
                    row.append(ch if ch else 'B')
                elif t.type == 'open_area':
                    dungeon = player_game.get_dungeon_at_position((x, y))
                    if dungeon is not None:
                        row.append(const.DUNGEON_ENTRANCE_CHAR)
                    else:
                        _, active = player_game.get_region_and_active_area_for_position((x, y))
                        type_name = active.city_name if active.city_name is not None else active.region_name
                        attr = f"{type_name.upper()}_OPEN_AREA_CHAR"
                        #input (f'Looking for attribute: {attr}')
                        open_char = getattr(const, attr)
                        row.append(open_char if open_char else ' ')
                elif t.type == 'impassable':
                    _, active = player_game.get_region_and_active_area_for_position((x, y))
                    type_name = active.city_name if active.city_name is not None else active.region_name
                    attr = f"{type_name.upper()}_IMPASSABLE_CHAR"
                    #input (f'Looking for attribute: {attr}')
                    open_char = getattr(const, attr)
                    row.append(open_char if open_char else ' ')
                elif t.type == ALLEY:
                    left_t = _pick_tile(x -1, y)
                    up_t = _pick_tile(x, y -1)
                    right_t = _pick_tile(x +1, y)
                    down_t = _pick_tile(x, y +1)
                    row.append(get_road_or_alley_char(t, left_t, up_t, right_t, down_t))
                else:
                    _, active = player_game.get_region_and_active_area_for_position((x, y))
                    open_char = f"{active.upper()}_OPEN_AREA_CHAR"
                    #input (f'Looking for attribute: {open_char}')
                    row.append(open_char if open_char else ' ')

        display_lines.append(row)
        #print('* ' + ''.join(row) + ' *')
    # if dialog text is provided, create dialog box and merge into display_lines
    if dialog_display_text:
        # display dialog 2/3 width
        dialog_width = (view_w *2) //3
        dialog_box = create_dialog_box(dialog_display_text, dialog_width)
        # calculate starting line to vertically center dialog box
        dialog_start_line = (view_h - len(dialog_box)) //2
        for i, db_line in enumerate(dialog_box):
            target_line = dialog_start_line + i
            if 0 <= target_line < len(display_lines):
                # replace center portion of display_lines[target_line] with db_line content
                line = display_lines[target_line]
                start_col = (view_w - dialog_width) //2
                for j in range(dialog_width):
                    if 0 <= start_col + j < len(line):
                        line[start_col + j] = db_line[j]
                display_lines[target_line] = line

    legend_lines = _create_legend(cur_area)
    max_lines = max(len(display_lines), len(legend_lines))
    
    for i in range(max_lines):
        map_line = ""
        if i < len(display_lines):
            map_line = '* ' + ''.join(display_lines[i]) + ' *'
        else:
            # If there are more legend lines than map lines, pad with empty space
            map_line = ' ' * (view_w + 4)

        legend_line = ""
        if i < len(legend_lines):
            legend_line = "   " + legend_lines[i]
        
        print(map_line + legend_line)

    print('*' * width)


def _create_legend(cur_area: City) -> List[str]:
    """Creates a legend of building characters and their display names."""
    if not cur_area or not hasattr(cur_area, 'tiles'):
        return []

    unique_buildings = {}
    for tile in cur_area.tiles.values():
        if tile.type == BUILDING and isinstance(tile.building, dict):
            # Use 'name' as a unique key for the building type
            building_name = tile.building.get('name')
            if building_name and building_name not in unique_buildings:
                unique_buildings[building_name] = tile.building

    if not unique_buildings:
        return []

    legend_lines = ["--- Legend ---"]
    # Sort buildings by their character for a consistent order
    sorted_buildings = sorted(unique_buildings.values(), key=lambda b: b.get('char', ''))
    for building in sorted_buildings:
        char = building.get('char', '?')
        display_name = building.get('display_name', 'Unknown')
        legend_lines.append(f"{char} - {display_name}")
    
    return legend_lines


# Use PATH_TILE_MAPPINGS for road/alley rendering and provide helper
def get_road_or_alley_char(tile: Tile, left_tile: Tile = None, up_tile: Tile = None, right_tile: Tile = None, down_tile: Tile = None) -> str:
    """Return an appropriate character for road or alley tiles using the
    centralized PATH_TILE_MAPPINGS from constants.

    Uses a4-bit connectivity mask: N=1, E=2, S=4, W=8 to pick a box-drawing
    character from the mapping when the mapping provides a dict. Falls back
    to single-character mappings for backwards compatibility.
    """
    mapping = getattr(const, 'PATH_TILE_MAPPINGS', {}) or {}
    
    # helper to select from either dict or single-char mapping
    def _select(kind_map, mask, default):
        if isinstance(kind_map, dict):
            return kind_map.get(mask, default)
        return kind_map or default

    if tile is None:
        # default to road char
        return _select(mapping.get('road'),0, '=')

    kind = 'road' if tile.type == ROAD else 'alley' if tile.type == ALLEY else None
    if kind is None:
        return ' '

    kind_map = mapping.get(kind)
    # if mapping is a simple string, return it
    if not isinstance(kind_map, dict):
        return _select(kind_map,0, '=' if kind == 'road' else '"')

    # Build4-bit mask: N=1, E=2, S=4, W=8
    mask =0
    
    if up_tile is not None and getattr(up_tile, 'type', None) == tile.type:
        mask |=1
    if right_tile is not None and getattr(right_tile, 'type', None) == tile.type:
        mask |=2
    if down_tile is not None and getattr(down_tile, 'type', None) == tile.type:
        mask |=4
    if left_tile is not None and getattr(left_tile, 'type', None) == tile.type:
        mask |=8
    
    return kind_map.get(mask, '=' if kind == 'road' else '"')

#################################### SHOP MENUS ###########################
# Shop menu UI moved to `shop_menu_screen.py` — use that implementation
def handle_shop_menu(player_game, business_def: any, region):
 # Delegate to the centralized shop menu implementation
 return handle_shop_screen(player_game, business_def, region)

# Note: specific buy/sell UIs are provided by game_screens.shop_menu_screen

def simulate_check_random_encounter(active_city, player_game, force_combat:bool = False):

    ### DEFINE NEW CHECK FOR RANDOM ENCOUNTER TO FIND MOBS IN THE REGION IGNORING HOSTILE SUBLOCATION PLACEMENT
    ### CALL NEW COMBAT SIMULATOR USING THE FOUND MOB
    _, region = player_game.get_region_and_active_area_for_position((player_game.x, player_game.y))
    parent_region_name = region.get_parent_region_name(player_game)
    region_name = region.city_name if not region.isRegion() else region.region_name

    if not parent_region_name:
        region_key = f"{region_name.upper()}_RANDOM_HOSTILE_SEEDS"
    else:
        region_key = f"{parent_region_name.upper()}_{region.city_name.upper()}_RANDOM_HOSTILE_SEEDS"
    
    hostiles = check_for_random_mob_encounter(player_game, region_key, force_combat=force_combat)

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



########TODO
def handle_pending_boss_encounter(player_game: PlayerGame) -> bool:
    """
    If player_game.pending_fight_mob_id is set, resolve boss mob hostiles
    from const.DUNGEON_SETTINGS, run the CombatSimulation/CombatScreen and
    call player_game.check_complete_boss_mob on success.

    Returns True if players won or there was no blocking failure; False if the
    players lost (caller should end the game loop).
    """
    #input ("Checking for pending boss encounter... (press Enter to continue)")
    mob_id = player_game.pending_fight_mob_id
    if not mob_id:
        return True

    # find boss definition in WORLD_BOSS_MOBS (reuse same source as Dungeon.get_boss_mob)
    boss_setting = None
    for boss_mob in const.WORLD_BOSS_MOBS:
        if boss_mob.get('id') == mob_id:
            boss_setting = boss_mob
            break
        
    """
        { 
        'id': 'mini_void_1', 
		'name': '????',
		'hostiles': [
			'mini_void'
        ]
	},
    """
    #input (f"Found pending boss mob ID: {mob_id} - {boss_setting.get('name') if boss_setting else 'NOT FOUND'} (press Enter to continue)")
    if not boss_setting:
        # fallback: unknown boss id, clear pending and continue
        try:
            input(f"Boss mob ID not found: {mob_id} (press Enter to continue)")
        except Exception:
            pass
        player_game.pending_fight_mob_id = None
        return True

    hostiles = []
    for hostile_id in boss_setting.get('hostiles', []):
        
        #const.WORLD_HOSTILES
        src_name = const.HOSTILE_SEED_PATHS.get(hostile_id)
        seed = None
        if src_name:
            src_list = getattr(const, src_name, None)
            if src_list:
                #print (f'Found hostile seed source "{src_name}" for id "{hid}"')
                seed = next((s for s in src_list if s.get('id') == hostile_id), None)

        if seed is None:
            # skip missing seed entry
            continue
        hostile = generate_hostile_from_legacy_seed(seed, player_game.get_max_character_level(), retain_abilities=True)
        hostiles.append(hostile)
    #input (f"Generated hostiles for boss mob: {[h.name for h in hostiles]} (press Enter to continue)")
    if not hostiles:
        # nothing to fight; clear pending id and continue
        player_game.pending_fight_mob_id = None
        return True

    sim = CombatSimulation(player_game, hostiles)
    screen = CombatScreen(width=220, height=60)
    screen.player_w = 50
    screen.hostile_w = 50
    players_won = screen.run(sim)

    if players_won:
        # delegate task completion handling to PlayerGame
        player_game.check_complete_boss_mob(mob_id)
        return True

    # players lost; don't clear pending id here (caller will break)
    return False