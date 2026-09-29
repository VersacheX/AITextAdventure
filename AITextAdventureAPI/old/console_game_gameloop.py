from readchar import readkey, key
import time
import random

import os
from typing import Any

from game.objects.player import Player
from game.objects.player_game import PlayerGame

from game_screens.overworld_screen import display_viewport, handle_shop_menu, simulate_check_random_encounter, handle_pending_boss_encounter

from services.player_movement_service import (
    get_allowed_moves,
    get_floor_options,
    select_sublocation,
    handle_movement_key,
    handle_floor_action
)
from run_combat_simulator import generate_player_character

from game_screens.inventory_screen import InventoryScreen
from game_screens.dungeon_screen import run_dungeon_screen

def clear_screen() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

############################# MAIN CONSOLE DEMO LOOP  #
def run_game_loop(pg: PlayerGame, viewport: tuple, api: Any):
    view_w, view_h, radius = viewport
    took_action = False
    try:
        while True:
            clear_screen()

            # Ensure nearby tiles exist (attempt at most one region generation per loop)
            pg.ensure_tiles_around(check_rad=4, max_attempts=1)

            # Determine parent region and active city for the player's coordinate
            parent_region, active_city = pg.get_region_and_active_area_for_position()

            # Build a view City populated from world_tiles for rendering the viewport
            view_city = pg.get_view_city(view_w, view_h)
            # copy display metadata from the parent region so header shows correct names
            if parent_region:
                
                setattr(view_city, 'region_name', getattr(parent_region, 'region_name', None))
                setattr(view_city, 'display_name', getattr(parent_region, 'display_name', None))
                setattr(view_city, 'seed', getattr(parent_region, 'seed', getattr(view_city, 'seed',0)))
                # ensure child_city reference is preserved for active detection
                setattr(view_city, 'child_city', getattr(parent_region, 'child_city', None))
                

            # Determine which city object to use for game actions (active city if present, otherwise parent region)
            active_area = active_city if active_city else parent_region
            if pg.info_dialogs and len(pg.info_dialogs) > 0:
                ##### I'd like to upgrade dialogs to appear in screen and one at a time the user presses readkey to advance #####
                ### will need to modify display_viewport(pg, parent_region, view_w, view_h) to display an overlay dialog box
                while len(pg.info_dialogs) > 0:
                    display_dialog_text = pg.pop_dialog()
                    display_viewport(pg, parent_region, view_w, view_h, dialog_display_text=display_dialog_text)
                    readkey()
                    clear_screen()

            if pg.pending_fight_mob_id:
                players_won = handle_pending_boss_encounter(pg)
                if not players_won:
                    # player lost in boss encounter -> exit loop (same behavior as dungeon)
                    break
                # if won or resolved, skip random encounter for this loop
                took_action = False
                continue

            # A task can seal the player inside a dungeon (pg.active_dungeon set
            # by set_player_in_dungeon). Enter it here regardless of took_action
            # or its lock state — the lock blocks *exit*, not this already-placed
            # entry. run_dungeon_screen surfaces the locked_text when the player
            # tries to leave and only returns once they actually get out.
            if pg.get_active_dungeon() is not None:
                dungeon = pg.get_active_dungeon()
                prev_ow_x, prev_ow_y = pg.x, pg.y
                player_pos = dungeon.get_player_pos()
                if player_pos is None:
                    pg.active_dungeon = None
                    took_action = False
                    continue
                run_dungeon_screen(dungeon, pg, player_pos)
                if pg.is_alive() == False:
                    break
                took_action = False
                continue

            if took_action:
                dungeon = pg.get_dungeon_at_position()
                if dungeon:
                    if dungeon.is_locked():
                        pg.add_dungeon_standing_text(dungeon)
                    else:
                        # preserve overworld coords so we can restore the overworld view after leaving
                        prev_ow_x, prev_ow_y = pg.x, pg.y
                        # Mark as active before entering so exit handling and the
                        # authoritative presence flag stay consistent with the
                        # task-placement path.
                        pg.active_dungeon = dungeon
                        # use the dungeon's internal player position if set, otherwise default origin
                        player_pos = dungeon.get_player_pos() or (0, 0, 0)
                        run_dungeon_screen(dungeon, pg, player_pos)

                        if pg.is_alive() == False:
                            break
                        # skip overworld encounter for this loop iteration (we just handled dungeon)
                        took_action = False
                        continue
                ############################ THIS METHOD WILL CALL THE NEW COMBAT SIMULATOR

                if not dungeon and not active_city.is_safe_area(pg):
                    is_combat = pg.countdown_random_encounter_timer()
                    if is_combat:
                        hostile = simulate_check_random_encounter(active_area, pg, force_combat=True)
                        if hostile:
                            clear_screen()
                        if pg.is_alive() == False:
                            break

            # render viewport using tiles from world (view_city) while header reflects the parent region
            display_viewport(pg, parent_region, view_w, view_h)

            print(f"Player at {pg.x},{pg.y}")

            # if inside aircraft show specialized description
            if getattr(pg, 'inside_aircraft', False):
                desc = "You are inside the aircraft."
            else:
                desc = active_area.describe_location(pg.x, pg.y, pg.inside, pg.z + 1)  #<<<<<<<<<<  need city level description if in city so we use active
            print(desc)
 
            # sublocations (use active city template when present)
            print(f"Sublocation count for area: {len(active_area.subloc_map)}")
            print(f'dungeon positions: {[d.position for d in pg.dungeons]}')
            #print(f"Player loc key: {(pg.x, pg.y, pg.z)}")
            sl = active_area.get_sublocation_at((pg.x, pg.y, pg.z))
            if sl:
                print("\nSublocations:")
                for idx, s in enumerate(sl, start=1):
                    prompt = s.get('prompt') or ''
                    print(f" {idx}) {s['name']} {prompt}")

            allowed_moves = get_allowed_moves(active_area, pg)
            can_up, can_down = get_floor_options(active_area, pg)
            can_shop, business_def = active_area._is_location_shop_first_floor(pg)
            can_travel = active_area._can_travel_from_player_location(pg)
            can_npc_interact, npc_name, _ = pg._can_npc_interact_at_player_location()
            #move_labels = ' '.join([f"{k.upper()}({v})" for k, v in allowed_moves.items()])
            floor_labels = ' '.join(filter(None, ['U(up)' if can_up else '', 'J(down)' if can_down else '']))
            npc_interact_label = f'(t)alk' if can_npc_interact else ''
            can_travel_label = f'(f)ast travel' if can_travel else ''
            print("Commands:")
            # if move_labels:
            #     print(f" Move: {move_labels}")
            if floor_labels:
                print(f" Floors: {floor_labels}")
            if npc_interact_label:
                print(f" NPC: {npc_interact_label}")
            if can_travel_label:
                print(f" {can_travel_label}")
            if can_shop:
                print(" P(shop)")
            # aircraft actions:
            # - If aircraft is present at player's position and player is not inside it => allow enter (v)
            # - If player is inside aircraft => allow land (l)
            if getattr(pg, 'aircraft_location', None) == (pg.x, pg.y) and not getattr(pg, 'inside_aircraft', False):
                print(" V(enter aircraft)")
            if getattr(pg, 'inside_aircraft', False):
                print(" L(land aircraft)")
            print(" I(inventory)")
            print(" Q(quit)")
            cmd = readkey()
            #cmd = input("Action: ").strip().lower()
            if not cmd:
                continue

            c = cmd#[0]
            if c == 'q':
                print("Are you sure? (y/n)")
                cmd = input().strip().lower()
                if cmd == 'y':
                    break

            # handle aircraft enter/land
            if c == 'v':
                # enter aircraft
                if getattr(pg, 'aircraft_location', None) == (pg.x, pg.y) and not getattr(pg, 'inside_aircraft', False):
                    pg.enter_aircraft()
                    took_action = True
                    continue
                else:
                    print("No aircraft here to enter.")
                    input("Press Enter to continue...")
                    continue

            if c == 'l':
                # land aircraft
                if getattr(pg, 'inside_aircraft', False):
                    pg.land_aircraft()
                    took_action = True
                    continue
                else:
                    print("You are not in the aircraft.")
                    input("Press Enter to continue...")
                    continue

            # sublocation selection
            if cmd.isdigit() and sl:
                handled, name, prompt, item, money = select_sublocation(cmd, sl, pg)
                if handled:
                    print(prompt)
                    final_prompt = ''
                    if item or (money and money >0):
                        if not money or not money >0:
                            pickup = input(f"Do you want to pick up the {item.name}? (y/n): ").strip().lower()
                        elif not item:
                            pickup = input(f"Do you want to pick up {money} money? (y/n): ").strip().lower()
                        else:
                            pickup = input(f"Do you want to pick up the {item.name} and {money} money? (y/n): ").strip().lower()

                        if pickup != 'y':
                            print("You decide not to pick it up.")
                            input("Press Enter to continue...")
                            took_action = True
                            continue

                        s_location = next((s for s in sl if s['name'] == name), None)
                        final_prompt = active_area.loot_sublocation(pg, s_location.get("name"))

                    print(final_prompt)
                    input("Press Enter to continue...")
                    took_action = True
                    continue

            # inventory
            if c == 'i':
                screen = InventoryScreen()
                #RUN THE TEST
                #try:
                screen.run(pg, api=api)
                # except Exception as e:
                #     print(f"Error running inventory screen: {e}")
                #     input("Press Enter to continue...")

                # handle_inventory_menu(pg.characters[0], pg)
                took_action = True
                continue
            if c == 'p':
                if can_shop:
                    handle_shop_menu(pg, business_def, active_area)
                    took_action = True
                else:
                    print("No shop here.")
                    input("Press Enter to continue...")
                continue
            if c == 't':
                if can_npc_interact:
                    selection = handle_select_npc_to_interact_with(pg)
                    if selection:
                        pg.handle_npc_interaction_at_player_location(selection.id)
                        # this will set a number of tasks to run on the next cycle such as display dialogs
                        #print(npc_prompt)
                        #input("Press Enter to continue...")
                        took_action = True
                else:
                    print("No one to talk to here.")
                    input("Press Enter to continue...")
                continue
            if c == 'f':
                if can_travel:
                    to_position = handle_fast_travel_selection(pg)
                    if to_position:
                        pg.handle_fast_travel_from_player_location(to_position)
                    took_action = True
                else:
                    print("There is no hyperway here.")
                    input("Press Enter to continue...")
                continue

            # movement
            if c in (key.UP, key.LEFT, key.DOWN, key.RIGHT):

                if c == key.UP:
                    c = 'w'
                elif c == key.LEFT:
                    c = 'a'
                elif c == key.DOWN:
                    c = 's'
                elif c == key.RIGHT:
                    c = 'd'

                orig_loc = (pg.x, pg.y)
                moved = handle_movement_key(c, active_area, allowed_moves, radius, pg)

                dungeon = pg.get_dungeon_at_position()
                if dungeon and dungeon.is_locked():
                    pg.add_dungeon_standing_text(dungeon)
                    pg.x, pg.y = orig_loc  # revert move if dungeon is locked


                if not moved:
                    # print(f"Command: {c}")
                    # print(f"Allowed moves: {allowed_moves}")
                    # print(f"CurrentTileExits: {active_area.get_tile(pg.x, pg.y).entrances if active_area.get_tile(pg.x, pg.y) else 'N/A'}")
                    # print("You can't move that way.")
                    # input("Press Enter to continue...")
                    continue
                took_action = True
                continue

            # floors
            if c in ('u', 'j'):
                floor_ok = handle_floor_action(cmd, active_area, pg)
                if not floor_ok:
                    if c == 'u':
                        print("You are not inside a building or already at the top floor.")
                    else:
                        print("No lower floors.")
                    input("Press Enter to continue...")
                    continue
                took_action = True
                continue

    except KeyboardInterrupt:
        input(f"\nGame interrupted. Press Enter to exit...")
    finally:

        print("Exiting game. Thank you for playing!")


def handle_fast_travel_selection(pg: PlayerGame):
    """
    get a list of all hyperways in the playergame
    display list for user selection

    	def get_all_hyperways(self) -> List[Dict[str, Any]]:
		hyperway_positions = []
		for region in self.regions:
			for (x, y), tile in region.tiles.items():
				if tile.building and tile.building.get('type') == 'hyperway':
					hyperway_positions.append({ 'description': self.get_location_description((x,y)), 'position': (x, y)})
		return hyperway_positions

        the cost is 100 to travel.. so they must make a selection no auto select. esc to cancel.
    """
    hyperways = pg.get_all_hyperways()
    if not hyperways or len(hyperways) == 0:
        print("No hyperway stations available for fast travel.")
        return None
    while True:
        for idx, hyperway in enumerate(hyperways, start=1):
            desc = hyperway.get('description') or 'Unknown Location'
            pos = hyperway.get('position') or (0,0)
            print(f" {idx}) {desc}")
        
        pick = input("Enter the number of the hyperway station to fast travel to (or empty to cancel): ").strip()
        if not pick:
            return None
        if not isinstance(pick, str) or not pick.isdigit():
            print("Invalid selection. Please try again.")
            return None
        sel = None
        num = int(pick)
        if 1 <= num <= len(hyperways):
            sel = hyperways[num - 1]
            return sel.get('position')
        else:
            print("Invalid selection. Please try again.")
            return None

def handle_select_npc_to_interact_with(pg: PlayerGame):
    """
    get list of npcs at location and select one to interact with
    """
    npcs = pg.get_npcs_at_player_location()
    if not npcs or len(npcs) == 0:
        print("No NPCs to interact with here.")
        return
    if len(npcs) == 1:
        npc = npcs[0]        
        return npc

    #while True:
    for idx, npc in enumerate(npcs, start=1):
        print(f" {idx}) {npc.name}")

        
    print("Enter the number of the NPC to interact with (or press esc to cancel): ")
    while True:
        pick = readkey()

        if len(pick.strip()) > 0:
            if pick == key.ESC:
                return None

            if pick.isdigit():
                sel = None
                num = int(pick)
                if 1 <= num <= len(npcs):
                    sel = npcs[num - 1]
                    return sel

def new_game(api):
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty. Returning to main menu.")
        return

    player = Player(name,0,0,0, False)
    #setup_player_stats(player)

    # world state container
    pg = PlayerGame()
    from combat_balancing_simulation.player_generator import equip_player_character
    equip_player_character(player, pg, focus='technique')
    pg.add_character(player)
    clear_screen()

    # build first region around origin using PlayerGame's helper (chooses a random initial region)
    ############# ALTERNATE SINGLE REGION MODE
    print('Please wait - Building initial region...')
    rc = pg.create_region_at((0,0))
    #############################################


    # initial display radius (viewport half-extents)
    viewport = (75, 25, 4)

    # Main loop
    run_game_loop(pg, viewport, api)

# if __name__ == '__main__':
#     new_game()
