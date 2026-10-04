import random
from typing import Dict, List, Tuple, Optional, Any

from game import constants as const
from game.constants import DIRECTIONAL_MAPPING
from game.objects.player import Player
from services.random_loot_service import generate_loot_for_sublocation
from game.objects.item import RarityDefaultWeights, Rarity
from run_combat_simulator import generate_random_mob





def get_floor_options(region, player_game) -> Tuple[bool, bool]:
	"""Return (can_up, can_down) for the player's current tile/state. No UI."""
	if not player_game.inside:
		return (False, False)
	current_tile = region.get_tile(player_game.x, player_game.y)
	can_up = False
	can_down = False
	if current_tile.type == 'building':
		pz = player_game.z
	
		floors = current_tile.floors

		if pz < (floors -1):
			can_up = True
		# can go down if above ground (pz >0) or on ground and building has basement
		if pz >0 or (pz ==0 and current_tile.has_basement == True):
			can_down = True
	return (can_up, can_down)


def check_for_random_mob_encounter(player_game, region_key,force_combat:bool = False) -> List[object]: # object is RandomHostile
	rng = random.Random()

	if rng.random() < 0.08 or force_combat:  # 8% chance of encounter
		# Monster Hunter: when a party member has the effect equipped, restrict
		# the overworld pool to hostiles the player has not yet logged so they
		# can find species missed at lower levels.
		exclude_ids = None
		if player_game.has_monster_hunter_active():
			exclude_ids = set((player_game.enemies_slain or {}).keys())
		return generate_random_mob(3, player_game.get_max_character_level(), region_key, exclude_ids=exclude_ids)

	return []

def select_sublocation(cmd: str, sl: List[Dict], player_game: Optional[object] = None) -> Tuple[bool, Optional[str], Optional[str], Optional[Any], Optional[int]]:
	"""Handle numeric sublocation selection. Returns (handled, name, prompt, extra).

	If `player` is provided and is inside a building but not on the main floor,
	this function will prevent sublocation actions that would leave the building
	(i.e. modes 'entered' and 'vertical'). The service returns structured data
	and does not perform UI (printing/input).
	"""
	if not cmd.isdigit():
		return False, None, None, None, None
	sel = int(cmd)
	if not (1 <= sel <= len(sl)):
		return False, None, None, None, None
	chosen = sl[sel - 1]
	name = chosen['name']
	mode = chosen.get('mode')
	prompt = chosen.get('prompt') or f"You look at the {name}."
	# disallow entering/exiting sublocations when inside but not on main (z !=0)
	if player_game and player_game.inside:
		pz = player_game.z
		
		if pz !=0 and mode in ('entered', 'vertical'):
			return False, None, None, None, None
	if mode in ('entered', 'vertical'):
		return True, name, f"You enter the {name}.\n{prompt}", None, None
	if mode == 'searchable':
		item = chosen.get('loot')
		money = chosen.get('money', 0)
		item_name = item.name if item else "nothing"
		money_prompt = f" {money} money" if money and money > 0 else ''
		item_prompt = f" a {item.name}" if item else ''

		final_prompt = f"You search the {name} but find nothing of interest."
		if(not item_prompt == '' or not money_prompt == ''):
			final_prompt = f"You search the {name} and find {item_prompt}{' and ' if item_prompt and not money_prompt == '' else ''}{money_prompt}"

		return True, name, final_prompt, item, money
	# fallback
	return True, name, prompt, None, None

def get_allowed_moves(region, player_game: Any = None) -> Dict[str, str]:
	"""Return mapping of input-key -> direction name for allowed horizontal moves.
	If player is inside a building, only allow exiting via entrances when on the main floor (floor1).
	This function contains only game logic and does not perform any UI.
	
	When `player_game` is provided, neighbour tile lookups will resolve the active
	area for the target coordinate so entrance checks consult the authoritative
	region/city instance for that location instead of relying on the `region`
	argument alone.
	"""
	allowed: Dict[str, str] = {}
	current_tile = region.get_tile(player_game.x, player_game.y)
	inside = bool(player_game.inside)
	for k, (dx, dy, name) in DIRECTIONAL_MAPPING.items():
		nx, ny = player_game.x + dx, player_game.y + dy
		ok = False
		if inside:
			# only allow exiting from the main floor (display floor1 -> z ==0)
			#print(f"Checking move {name} from inside building, possible exits: {current_tile.entrances}")
			
			pz = int(getattr(player_game, 'z',0) or 0)
			
			if current_tile.type == 'building' and name in current_tile.entrances and pz ==0:
				ok = True
		else:
			_, resolved = player_game.get_region_and_active_area_for_position((nx, ny))
			
			if resolved is None:
				continue
			target = resolved.get_tile(nx, ny)
			if target.type == 'building' and resolved._opposite_dir(name) not in target.entrances: 
				ok = False
			else:
				if target.type == 'impassable' and not player_game.inside_aircraft:
					ok = False
				else:
					# allow moving onto alleys/roads/buildings per region rules
					# disallow movement over ocea if not unlocked
					# disallow aircraft moving into buildings ??? might change later as the aircraft zooms out for faster movement
					if player_game.inside_aircraft and resolved.display_name == 'Ocean' and not player_game.allow_ocean_flight:
						ok = False
					elif target.type =='building' and player_game.inside_aircraft:
						ok = False
					else:
						ok = True
		if ok:
			allowed[k] = name
	return allowed

def handle_movement_key(cmd: str, region,allowed_moves: Dict[str, str], radius: int, player_game) -> bool:
	"""Process movement keys (wasd). Returns True if the command was handled."""
	if not cmd:
		return False
	c = cmd[0]
	if c not in ('w', 'a', 's', 'd'):
		return False
	if c not in allowed_moves:
		return False

	dx, dy, name = DIRECTIONAL_MAPPING[c]
	nx, ny = player_game.x + dx, player_game.y + dy
	#after changing the players position we need to check the player_game.regions and each region.child_city 
	# to determine if the player moved into a known region... 
	# if so we change to that region without affecting the current region in the player_game ... not sure if that means we need to update the version of the current region or not

	# fetch target
	current_tile = region.get_tile(player_game.x, player_game.y)
	
	pz = player_game.z
		
	_, active_area = player_game.get_region_and_active_area_for_position((nx, ny))
	if active_area is None:
		return False

	#inside movement exit
	if player_game.inside:
		# exiting building via entrance — only allowed from main floor (z ==0)
		if current_tile.type == 'building' and pz !=0:
			return False
		player_game.set_position(nx, ny)
		player_game.exit()

		return True

	# outside movement into target
	target = active_area.get_tile(nx, ny)

	if target.type == 'building' and active_area._opposite_dir(name) in target.entrances:
		if current_tile is None:
			print(f"Current Location: {player_game.x}, {player_game.y} Active Areas Tiles: {active_area.tiles}")

		# auto-enter
		player_game.set_position(nx, ny)
		# Enter display floor1 if building defines floors >=1, otherwise use display floor1
		# (display floor1 corresponds to z ==0). Some maps may use different conventions
		# for sublocation indexing; server/client should normalise on z for internal logic.
		tf = int(getattr(target, 'floors',1) or 1)
		
		# always enter display floor1 (z ==0) on auto-enter
		player_game.enter(1)

		return True
	# normal move
	player_game.set_position(nx, ny)
	player_game.exit()
	# outside view -> ground floor
	# populate_sublocs_for_radius(region, region.subloc_map, player, radius,0,0)
	return True


def handle_floor_action(cmd: str, region, pg) -> bool:
	"""Process floor up/down commands 'u' and 'j'. Returns True if handled."""
	if not cmd:
		return False
	c = cmd[0]
	if c == 'u':
		if not (pg.inside and region.get_tile(pg.x, pg.y).type == 'building'):
			pg.add_info_dialog_line(None, f"Cannot go up here: inside={pg.inside}, tile type={region.get_tile(pg.x, pg.y).type}")
			return False
		current_tile = region.get_tile(pg.x, pg.y)
		floors = current_tile.floors

		# cannot go above top floor
		if ( pg.z + 1) >= floors:
			pg.add_info_dialog_line(None, f"Current floor: {pg.z + 1}: floors {floors}")
			return False
		# go up one display floor -> increment z
		pg.z += 1
		# regeneration of sublocations is handled by the main loop; it will call
		# populate_sublocs_for_radius at the top of the next iteration.
		return True
	if c == 'j':
		if not (pg.inside and region.get_tile(pg.x, pg.y).type == 'building'):
			return False
		tile = region.get_tile(pg.x, pg.y)
		pz = pg.z
		# if on ground floor and building has no basement and only one floor, cannot go down
		if pz ==0 and not tile.has_basement and tile.floors <=1:
			return False
		
		if pz >0:
			pg.z = pz -1
		else:
			if tile.has_basement:
				# go to basement level (represent as z = -1)
				pg.z = -1
			else:
				return False
		# regeneration of sublocations is handled by the main loop
		return True
	return False
