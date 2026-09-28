from typing import Any, Dict

from game.objects.npc import NPC
import game.constants as const
import threading

# Event types known (or suspected) to take non-trivial time to execute.
# The TUI uses this to show a "Loading..." overlay (and block input) for the
# duration of these events only.
LONG_RUNNING_EVENT_TYPES = frozenset({
	'create_dungeon',
	'complete_intro_story',
	'remove_ocean',
})

# Guards the nested long-running-event depth counter tracked on each
# PlayerGame (_busy_depth). Task events can nest (an outer long-running event
# executes another event via event.execute), so a plain boolean would let the
# inner finally clear is_busy while the outer mutation is still running. A
# lock-protected counter clears is_busy only when the outermost event exits.
_BUSY_DEPTH_LOCK = threading.Lock()


def _enter_busy(player_game) -> None:
	"""Increment the long-running-event depth; set is_busy on first entry."""
	with _BUSY_DEPTH_LOCK:
		depth = getattr(player_game, '_busy_depth', 0) + 1
		player_game._busy_depth = depth
		player_game.is_busy = True


def _exit_busy(player_game) -> None:
	"""Decrement the depth; clear is_busy only when the outermost event exits."""
	with _BUSY_DEPTH_LOCK:
		depth = getattr(player_game, '_busy_depth', 1) - 1
		if depth <= 0:
			depth = 0
			player_game.is_busy = False
		player_game._busy_depth = depth


def _report_event_error(player_game, message: str) -> None:
	"""Surface a task-event error to the player instead of blocking on stdin.

	These were previously `input(...)` calls that froze the background worker
	thread (and its loading overlay) waiting for a keypress on a UI with no
	console. Route the message to the in-game info dialog queue so it shows on
	screen, and always print for logs.
	"""
	print(f'[task-event error] {message}')
	try:
		if player_game is not None:
			player_game.add_info_dialog_line(None, f'[debug] {message}')
	except Exception:
		pass

# NPCS = [
#     {
#         'npc_id': 'nia',
#         'name': 'Nia',
#         'description': (
#             'A rebellious wind-dancer who senses disturbances in the natural flow of the wind. '
#             'She is determined to stop Serene the Whisper-Thief from stealing future echoes.'
#         )
#     },

def execute_acquire_event(event: Any, player_game, parent_task):
	"""Execute a single task acquire event.

	Currently supports:
	- 	'event_type': 'create_npc',
		'params': {
			'npc_id': 'nia',
			'location': 'region_bar'
		}
	"""
	if event is None:
		return None

	return handle_task_event(event, player_game, parent_task)	

def execute_complete_event(event: Any, player_game, parent_task):
	"""Execute a single task completion event.

	Supported event types (from TaskEventType):
	- award_task: params { 'task_id': 'some_task_id' }
	- award_item: params { 'item_id': 'some_item_id' }
	- award_money: params { 'amount':100 }
	- initiate_dialog: params { 'npc_id': 'ripple', 'dialog_id': 'ripple_intro' }
	- hide_npc: params { 'npc_id': 'grimnaw' }
	- character_join: params { 'character_id': 'name' }
	
	The function mutates player_game (adds tasks, items, money, dialogs, removes NPCs).
	"""
	if event is None:
		return None

	return handle_task_event(event, player_game, parent_task)	

def handle_task_event(event, player_game, parent_task):
	from game.objects.task import TaskEventType
	ev_type = None
	# event may be a TaskAcquireEvent instance or a plain dict
	if hasattr(event, 'event_type'):
		ev_type = event.event_type
		params = getattr(event, 'params', {})

	ev_name = ev_type.value

	# ── conditional guard ─────────────────────────────────────────────────
	# If the event carries a condition, evaluate it first.  A False result
	# silently skips the event; the rest of the task chain continues normally.
	condition = getattr(event, 'condition', None)
	if condition is not None:
		from services.event_condition_service import evaluate_condition  # noqa: PLC0415
		if not evaluate_condition(condition, player_game):
			return None
	# ─────────────────────────────────────────────────────────────────────

	# ── busy flag ─────────────────────────────────────────────────────────
	# Long-running events flip player_game.is_busy so the TUI can show a
	# "Loading..." overlay and block input for their duration only. A depth
	# counter (not a plain bool) handles nested long-running events: is_busy is
	# only cleared when the outermost event exits. Cleared in a finally so an
	# exception mid-event can't leave the UI stuck.
	is_long_running = ev_name in LONG_RUNNING_EVENT_TYPES
	if is_long_running:
		_enter_busy(player_game)
	try:
		return _dispatch_task_event(ev_name, params, player_game, parent_task)
	finally:
		if is_long_running:
			_exit_busy(player_game)


def _dispatch_task_event(ev_name, params, player_game, parent_task):
	from game.objects.task import TaskEventType

	# AWARD_TASK: find seed in const.TASKS and build a Task then give to player_game
	if ev_name == TaskEventType.AWARD_TASK.value:
		task_id = params.get('task_id')
		return award_task_to_player_game(task_id, player_game, parent_task)

	# AWARD_ITEM: instantiate item and add to player_game.inventory
	if ev_name == TaskEventType.AWARD_ITEM.value:
		item_id = params.get('item_id')
		return award_item_to_player_game(item_id, player_game)

	# REMOVE_ITEM: remove item from player_game.inventory
	if ev_name == TaskEventType.REMOVE_ITEM.value:
		item_id = params.get('item_id')
		return remove_item_from_player_game(item_id, player_game)

	# AWARD_MONEY: add money
	if ev_name == TaskEventType.AWARD_MONEY.value:
		amount = params.get('amount')
		amount = int(amount) if amount is not None else 0
		return award_money_to_player_game(amount, player_game)

	if ev_name == TaskEventType.REMOVE_MONEY.value:
		amount = int(params.get('amount', 0))
		return remove_money_from_player_game(amount, player_game)

	# INITIATE_DIALOG: locate dialog in const.NPC_DIALOG and push to player_game.info_dialogs
	if ev_name == TaskEventType.INITIATE_DIALOG.value:
		return initiate_dialog_to_player_game(params, player_game)

	if ev_name == TaskEventType.INITIATE_CHARACTER_DIALOG.value:
		return initiate_character_dialog_to_player_game(params, player_game)

	if ev_name == TaskEventType.INITIATE_OPTION_DIALOG.value:
		return initiate_option_dialog_to_player_game(params, player_game)

	if ev_name == TaskEventType.SET_NPC_STANDING_TEXT.value:
		return set_npc_standing_text(params, player_game)

	# HIDE_NPC: remove npc or mark as hidden
	if ev_name == TaskEventType.HIDE_NPC.value:
		return hide_npc_in_player_game(params, player_game)

	# SHOW_NPC: place npc back into the world at a location
	if ev_name == TaskEventType.SHOW_NPC.value:
		return show_npc_in_player_game(params, player_game, parent_task)

	if ev_name == TaskEventType.SET_PLAYER_LOCATION.value:
		return set_player_location(params, player_game, parent_task)

	if ev_name == TaskEventType.SET_AIRCRAFT.value:
		return set_aircraft(params, player_game, parent_task)
	
	if ev_name == TaskEventType.ALLOW_OCEAN_FLIGHT.value:
		return player_game.allow_ocean_flight()
	
	if ev_name == TaskEventType.CAN_AIRCRAFT_FLY.value:
		can_fly = params.get('can_fly') if params.get('can_fly') else False
		return player_game.set_aircraft_flyable(can_fly)

	# CHARACTER_JOIN: try to add a character to player_game.characters from constants if available
	if ev_name == TaskEventType.CHARACTER_JOIN.value:
		return character_join(params, player_game)

	if ev_name == TaskEventType.PLAYER_CHARACTER_JOIN.value:
		return player_character_join(params, player_game)

	if ev_name == TaskEventType.ADD_PENDING_CHARACTER.value:
		return player_game.add_pending_character()

	if ev_name == TaskEventType.CREATE_CHARACTER_NPC.value:
		# call add_character_npc on player_game. selection is random
		pos = _get_npc_seed_location(params, parent_task, player_game)
		return player_game.add_character_npc(pos)

	# CREATE NPC
	if ev_name == TaskEventType.CREATE_NPC.value:
		return create_npc(params, player_game, parent_task)

	# CREATE DUNGEON
	if ev_name == TaskEventType.CREATE_DUNGEON.value:
		return create_dungeon(params, player_game, parent_task)

	#LOCK_DUNGEON
	if ev_name == TaskEventType.LOCK_DUNGEON.value:
		return player_game.lock_dungeon_by_id(params.get('dungeon_id'))

	# UNLOCK_DUNGEON
	if ev_name == TaskEventType.UNLOCK_DUNGEON.value:
		return player_game.unlock_dungeon_by_id(params.get('dungeon_id'))

	# SET DUNGEON LOCKED TEXT set_dungeon_locked_text_by_id
	if ev_name == TaskEventType.SET_DUNGEON_LOCKED_TEXT.value:
		return player_game.set_dungeon_locked_text_by_id(params.get('dungeon_id'), params.get('locked_text'))

	# SET PLAYER IN DUNGEON
	if ev_name == TaskEventType.SET_PLAYER_IN_DUNGEON.value:
		return set_player_in_dungeon_by_id(player_game, params.get('dungeon_id'), params.get('location'))

	if ev_name == TaskEventType.REMOVE_PLAYER_FROM_DUNGEON.value:
		return player_game.remove_player_from_dungeon(params.get('dungeon_id'))

	# BEGIN COMBAT
	if ev_name == TaskEventType.BEGIN_COMBAT.value:
		return create_combat_scenario(params, player_game, parent_task)

	# ADVANCE CHAPTER
	if ev_name == TaskEventType.ADVANCE_CHAPTER.value:
		return advance_chapter_in_player_game(player_game)

	if ev_name == TaskEventType.COMPLETE_INTRO_STORY.value:
		return player_game.complete_intro_story()

	if ev_name == TaskEventType.COMPLETE_REGION_QUEST.value:
		return player_game.complete_region_quest(params.get('region_id'))
	
	if ev_name == TaskEventType.COMPLETE_REGION_QUEST_2.value:
		return player_game.complete_region_quest_2(params.get('region_id'))
	
	# DUNGEON ADD TREASAURE
	if ev_name == TaskEventType.DUNGEON_ADD_TREASURE.value:
		#print('Adding treasure to dungeon...')
		return add_treasure_to_dungeon(params, player_game, parent_task)

	if ev_name == TaskEventType.DUNGEON_ADD_NPC.value:
		return add_npc_to_dungeon(params, player_game, parent_task)

	if ev_name == TaskEventType.SET_NPC_MET.value:
		npc_id = params.get('npc_id')
		if npc_id == 'pending_character':
			npc_id = player_game.pending_character
		if npc_id == 'final_character':
			npc_id = player_game.final_character
		return player_game.set_npc_met(npc_id)

	if ev_name == TaskEventType.UNLOCK_NPC_LOG.value:
		return player_game.unlock_npc_log()

	if ev_name == TaskEventType.REMOVE_OCEAN.value:
		return player_game.remove_ocean()

	if ev_name == TaskEventType.UNLOCK_HYPERWAY.value:
		return player_game.unlock_hyperway()

	if ev_name == TaskEventType.LOCK_HYPERWAY.value:
		return player_game.lock_hyperway()

	if ev_name == TaskEventType.CANCEL_TASK.value:
		return player_game.cancel_task(params.get('task_id'))

	if ev_name == TaskEventType.REMOVE_TASK.value:
		return player_game.remove_task(params.get('task_id'))

	if ev_name == TaskEventType.COMPLETE_TASK.value:
		task_id = params.get('task_id')
		return complete_task_in_player_game(task_id, player_game)

	_report_event_error(player_game, f'Unhandled task event type: {ev_name} with params: {params}')

	return None

def _get_npc_seed_location(params: Dict[str, Any], parent_task, player_game) -> Any:
	pos = None
	if params.get('location') is not None:
		used_region = _get_location_region_area_from_params(params, parent_task, player_game)
		if used_region:
			building_name = params['location'].split('_')[-1]
			if building_name == 'center':
				pos = used_region.get_center_position()
			elif 'open_area' in params['location']:
				pos = used_region.find_coords_of_random_tile_of_type(player_game, 'open_area')
			else:
				pos = used_region.find_coords_of_random_building_of_type(player_game, building_name)
	return pos


def create_npc(params: Dict[str, Any], player_game, parent_task) -> NPC:
	"""Create an NPC from params and attach to player_game if provided.

	Expected params keys: 'npc_id' or 'id', optional 'name', 'description',
	optional 'position' as [x,y,z], and 'location' or 'location_reference_id'.

	'event_type': 'create_npc',
	 'params': {
	 'npc_id': 'nia',
	 'location': 'region_bar'
	 }

	location format (region_|region_city_)(tile.building_def['name'])
	region_ use current_region
	region_city_ use active_city

	def find_nearest_building_of_type(self, player_game, building_type: str, pos: Tuple[int,int,int] = None) -> Optional[Tuple[int, int]]:
	"""
	# print ('Creating NPC...')
	# print (f' NPC params: {params}')
	if not params:
		return None

	
	npc_id = params.get('npc_id') or params.get('id')
	if not npc_id:
		return None

	if npc_id == 'final_character':
		npc_id = player_game.get_available_character_npc_id()
		player_game.final_character = npc_id

	# find npc seed in const.NPCS
	for npc_seed in const.NPCS:
		seed_id = npc_seed.get('npc_id') or npc_seed.get('id')
		if seed_id == npc_id:
			seed = npc_seed
			break
		

	name = seed.get('name')
	description = seed.get('description', '')

	pos = _get_npc_seed_location(params, parent_task, player_game)
	#input (f'creating npc {npc_id}, {name}, {description}, {pos}')
	npc = NPC(id=npc_id, name=name, description=description, position=pos)

	#input (f'Created NPC: {npc.name} at position {npc.position}')
	if player_game is not None:
		player_game.add_npc(npc)

	return npc

def create_dungeon(params: Dict[str, Any], player_game, parent_task):
	dungeon_seed = None
	if not params:
		return None
	dungeon_id = params.get('dungeon_id') or params.get('id')
	if not dungeon_id:
		return None
	for ds in const.DUNGEON_SETTINGS:
		seed_id = ds.get('dungeon_id') or ds.get('id')
		if seed_id == dungeon_id:
			dungeon_seed = ds
			break
	if dungeon_seed is None:
		return None
	from game.services.dungeon_builder_service import build_dungeon
	dungeon = build_dungeon(dungeon_seed)

	task_region = _get_location_region_area_from_params(params, parent_task, player_game)

	if player_game is not None and dungeon is not None:
		position = task_region.find_random_dungeon_position(dungeon, player_game)
		dungeon.position = position
		#input (f'Created dungeon: {dungeon.display_name} at position {dungeon.position}')
		player_game.add_dungeon(dungeon)
		return
	_report_event_error(player_game, f'create_dungeon failed (dungeon is None? {dungeon is None}) for id={dungeon_id}')

def _get_location_region_area_from_params(params: Dict[str, Any], parent_task, player_game):
	if params.get('location') is not None:
		# if params['location'] contains city_number_ then parse city_index_## for ## is the city index on playergame. if has suffix _region as city_index_##_region use that cities region 
		if 'city_number_' in params['location']:
			parts = params['location'].split('_')
			city_number = int(parts[2])
			if city_number <= len(player_game.get_cities()):
				used_region = player_game.get_city_by_number(city_number)
				if '_region' in params['location']:
					used_region = used_region.get_parent(player_game)

				return used_region

		# if params['location'] contains {desert|grassland|shallows|mountains|swamp|snow|forest}_{large_city|mid_city|small_city} find appropriate city in current region or parent region based on suffix and find coords of random building of type {large_city|mid_city|small_city} in that city by reference... if appended _region use that cities region.
		for region_type in const.REGION_TYPES:
			if region_type in params['location']:
				for city_type in const.CITY_TYPES:
					if city_type in params['location']:
						used_region = player_game.get_city_by_region_city_name(f"{region_type}_{city_type}")						
						if '_region' in params['location']:
							used_region = used_region.get_parent(player_game)

						return used_region

		used_region = parent_task.acquired_region
		use_city = 'region_city_' in params['location']
		if not use_city:
			if not used_region.isRegion():
				used_region = used_region.get_parent(player_game)
		else:
			if used_region.child_city is not None:
				used_region = used_region.child_city
	
		return used_region
	return None


def set_player_in_dungeon_by_id(player_game, dungeon_id: str, location: str):
	"""
		player_game.set_player_in_dungeon(dungeon, location)
	"""
	from game.objects. dungeon import DungeonTileType
	player_game.place_player_in_dungeon_at_location(dungeon_id, DungeonTileType(location))

def add_npc_to_dungeon(params: Dict[str, Any], player_game, parent_task):
	"""
	 use dungeon_id to find dungeon in player_game.dungeons
	 				
				'event_type': 'dungeon_add_npc',
				'params': {
					'dungeon_id': 'seth_hideout',
					'npc_id': 'seth',
					'location': 'final_chamber'
				}

	    then add npc to it based on params['npc_id']
        #npcs can block items... but may not be placed on the same tile
        for npc in self.npcs_spec:
            loc = npc.get("location")
            npc_id = npc.get("id")
            entity = {'type': 'npc', 'npc_id': npc_id}
            dungeon.place_entity_at_location(entity, DungeonTileType(loc))
	"""
	dungeon_id = params.get('dungeon_id')
	if not dungeon_id:
		_report_event_error(player_game, f'Dungeon ID not provided in params: {params}')
		return None
	dungeon = None
	for d in player_game.dungeons:
		if d.id == dungeon_id:
			dungeon = d
			break
	if dungeon is None:
		_report_event_error(player_game, f'Dungeon to add npc not found: {dungeon_id}')
		return None
	npc_id = params.get('npc_id')
	if not npc_id:
		#input ('NPC ID not provided in params')
		return None
	if npc_id == 'final_character':
		npc_id = player_game.final_character
	location = params.get('location')
	depth = params.get('depth')           # optional 0-100 depth percentage
	entity = {'type': 'npc', 'npc_id': npc_id}
	from game.objects.dungeon import DungeonTileType
	dungeon.place_entity_at_location(entity, DungeonTileType(location), depth=depth)



def add_treasure_to_dungeon(params: Dict[str, Any], player_game, parent_task):
	"""
	 use dungeon_id to find dungeon in player_game.dungeons
	    then add treasure to it based on params['treasure_id']
				
				'event_type': 'dungeon_add_treasure',
				'params': {
					'dungeon_id': 'seth_hideout',
					'item_id': 'ornate_bracers',
					'location': 'final_chamber'
				}

		def add_treasure_at_location(self, item: ItemType, location_type):
        candidates = [tile for tile in self.tiles.values() if tile.tile_type == DungeonTileType(location_type)]
        if not candidates:
            return False
        import random
        rng = random.seed(abs(hash(self.id)) % (10 ** 8))
        chosen_tile = random.choice(candidates)
        chosen_tile.entities.append(item)
	"""
	dungeon_id = params.get('dungeon_id')
	if not dungeon_id:
		#input(f'Dungeon ID not provided in params: {params}')
		return None
	dungeon = None
	for d in player_game.dungeons:
		if d.id == dungeon_id:
			dungeon = d
			break
	if dungeon is None:
		_report_event_error(player_game, f'Dungeon to add treasure not found: {dungeon_id}')
		return None
	item_id = params.get('item_id')
	if not item_id:
		_report_event_error(player_game, 'Item ID not provided in params')
		return None
	# instantiate item
	from game.objects.item import instantiate_item_from_id

	item = instantiate_item_from_id(item_id)
	if item is None:
		_report_event_error(player_game, f'Item to add to dungeon not found: {item_id}')
		return None

	location_type = params.get('location')  # e.g. 'final_chamber'
	depth = params.get('depth')
	if not location_type:
		_report_event_error(player_game, 'Location type not provided in params')
		return None
	from game.objects.dungeon import DungeonTileType
	dungeon.place_entity_at_location(item, DungeonTileType(location_type), depth=depth)
	return item

def create_combat_scenario(params: Dict[str, Any], player_game, parent_task):
	"""
	            {
                'event_type': 'begin_combat',
                'params': {
                    'boss_mob_id': 'serene_1',
                    'combat_type': 'boss_battle'
                }
            }
			player_game.set_pending_fight_mob()
	"""
	boss_mob_id = params.get('boss_mob_id') or params.get('id')
	if not boss_mob_id:
		return None
	#input(f'Beginning combat scenario with boss mob id: {boss_mob_id}')
	player_game.set_pending_fight_mob(boss_mob_id)

def player_character_join(params, player_game):
	if 'is_final_character' in params and params['is_final_character']:
		player_game.add_final_character(params.get('dialog_id'))
	else:
		player_game.add_random_player_character(params.get('dialog_id'))

def character_join(params, player_game):
	char_id = params.get('character_id') 
	if not char_id or player_game is None:
		return None
	# search attainable characters
	for seed in const.ATTAINABLE_PLAYER_CHARACTERS:
		if seed.get('id') == char_id:
			# local import to avoid cycle
			from game.objects.player import Player, generate_player_from_attainable_character_seed
			p = generate_player_from_attainable_character_seed(seed)
			player_game.add_character(p)
				
			return p

	return None

def hide_npc_in_player_game(params, player_game):
	#print (f'Hiding NPC with params: {params}')
	npc_id = params.get('npc_id')	
	if npc_id == 'pending_character':
		npc_id = player_game.pending_character
	if npc_id == 'final_character':
		npc_id = player_game.final_character
	if not npc_id or player_game is None:
		return None
	removed = []
	for i, n in enumerate(list(player_game.npcs)):
		#print( f' Checking NPC: {n.id} vs {npc_id}')
		if n.id == npc_id:
			#print (f' NPC found to hide: {n.name} at position {n.position}')
			player_game.hide_npc(n)
	return removed

def set_aircraft(params, player_game, parent_task):
	""" Show aircraft at location as show_npc_in_player_game to find pos, then call set_aircraft_location(pos) on player_game.
	"""
	used_region = _get_location_region_area_from_params(params, parent_task, player_game)
	if used_region:
		location_name = params['location'].replace('region_city_', '').replace('region_', '')
		pos = used_region.find_coords_of_random_tile_of_type(player_game, location_name)
		player_game.set_aircraft_location(pos)

def set_player_location(params, player_game, parent_task):
	""" Show player at location as show_npc_in_player_game to find pos, then call set_player_location(pos) on player_game.
	"""
	used_region = _get_location_region_area_from_params(params, parent_task, player_game)
	if used_region:
		location_name = params['location'].replace('region_city_', '').replace('region_', '')
		pos = used_region.find_coords_of_random_tile_of_type(player_game, location_name)
		player_game.set_player_location(pos)

def show_npc_in_player_game(params, player_game, parent_task):
	""" unlike hide_npoc which simply sets the npc position to None, so it's effectively nowhere.
	show_npc must behave like create_npc and place the npc back into the world at a location.
	using the npc in player_game.npcs ... if does not exist do nothing (throw error).
	"""
	npc_id = params.get('npc_id')	
	if npc_id == 'pending_character':
		npc_id = player_game.pending_character
	if npc_id == 'final_character':
		npc_id = player_game.final_character

	for n in player_game.npcs:
		if n.id == npc_id:
			# npc found
			# now set position based on params['location']
			used_region = _get_location_region_area_from_params(params, parent_task, player_game)
			if used_region:
				location_name = params['location'].replace('region_city_', '').replace('region_', '')
				pos = used_region.find_coords_of_random_tile_of_type(player_game, location_name)
				n.position = pos
				return n
	# not found
	_report_event_error(player_game, f'NPC to show not found: {npc_id}')
	return None

def set_npc_standing_text(params, player_game):
	npc_id = params.get('npc_id')	
	if npc_id == 'pending_character':
		npc_id = player_game.pending_character
	if npc_id == 'final_character':
		npc_id = player_game.final_character
	standing_text = params.get('standing_text')
	if not npc_id or not standing_text or player_game is None:
		return None
	for n in player_game.npcs:
		if n.id == npc_id:
			n.standing_text = standing_text
			return n
	return None

def initiate_character_dialog_to_player_game(params, player_game):
	#print (f'Initiating dialog with params: {params}')
	npc_id = params.get('npc_id')
	if npc_id == 'pending_character':
		npc_id = player_game.pending_character
	if npc_id == 'final_character':
		npc_id = player_game.final_character
	if npc_id == 'twisted_character':
		npc_id = player_game.twisted_character
	if not npc_id:
		#input ('NPC ID not provided in params')
		return None

	dialog_id = params.get('dialog_id')
	# search const.NPC_DIALOG
	for dlg in const.NPC_DIALOG:
		if (dlg.get('npc_id') == npc_id) and (dlg.get('dialog_id') == dialog_id):
			# get the npc name from const.NPC using npc_id
			npc_name = None
			for n in const.NPCS:
				seed_id = n.get('npc_id')
				if seed_id == npc_id:
					npc_name = n.get('name')
					break
			
			player_game.set_npc_met(npc_id)
			lines = dlg.get('dialog') or []			
			# extend with each line so UI can pop them
			player_game.add_character_dialog_lines(npc_id, lines)
			return lines
	# not found -> return None
	_report_event_error(player_game, f'Dialog not found for npc_id={npc_id}, dialog_id={dialog_id}')
	return None

def initiate_option_dialog_to_player_game(params, player_game):
	"""Set player_game.option_dialog from an initiate_option_dialog event.

	Expected params:
	    {
	        'message': 'What do you want to do?',
	        'options': [
	            ('Fight the guard', 'ch1_fight_seth'),
	            ('Sneak past',      'ch1_sneak'),
	        ]
	    }

	Any pending info_dialogs are displayed in full before the option prompt
	surfaces in the TUI (handled by _check_dialogs_and_refresh ordering).
	The TUI mounts an OptionDialogWidget, awards the chosen task_id via
	award_task_to_player_game, then clears option_dialog back to None.
	"""
	message = params.get('message', '')
	raw_options = params.get('options') or []

	# Accept both list-of-tuples and list-of-dicts for author convenience
	options = []
	for opt in raw_options:
		if isinstance(opt, (list, tuple)) and len(opt) == 2:
			options.append((str(opt[0]), str(opt[1])))
		elif isinstance(opt, dict):
			options.append((str(opt.get('text', '')), str(opt.get('task_id', ''))))

	if not message or not options:
		_report_event_error(player_game, f'initiate_option_dialog: missing message or options in params: {params}')
		return None

	player_game.option_dialog = {'message': message, 'options': options}
	return player_game.option_dialog

def initiate_dialog_to_player_game(params, player_game):
	#print (f'Initiating dialog with params: {params}')

	npc_id = params.get('npc_id') # if none then is narrative

	if npc_id == 'pending_character':
		npc_id = player_game.pending_character
	if npc_id == 'final_character':
		npc_id = player_game.final_character
		#input (f'Using pending character npc_id: {npc_id}')
	dialog_id = params.get('dialog_id')
	# search const.NPC_DIALOG
	for dlg in const.NPC_DIALOG:
		if (dlg.get('npc_id') == npc_id) and (dlg.get('dialog_id') == dialog_id):
			# get the npc name from const.NPC using npc_id
			npc_name = None
			for n in const.NPCS:
				seed_id = n.get('npc_id')
				if seed_id == npc_id:
					npc_name = n.get('name')
					break
			player_game.set_npc_met(npc_id)
			lines = dlg.get('dialog') or []
			
			# extend with each line so UI can pop them
			for l in lines:
				player_game.add_info_dialog_line(npc_name, l)

			return lines
	# not found -> return None
	_report_event_error(player_game, f'Dialog not found for npc_id={npc_id}, dialog_id={dialog_id}')
	return None

def remove_money_from_player_game(amount: int, player_game):
    """Deduct money from player_game by amount. Floors at 0."""
    if player_game is not None and amount and amount > 0:
        current = getattr(player_game, 'money', 0)
        player_game.money = max(0, current - amount)
        player_game.add_info_dialog_line(None, f'Lost money: {amount}')
    return amount

def award_money_to_player_game(amount: int, player_game):
	"""Award money to player_game by amount."""
	if player_game is not None and amount and amount >0:
		player_game.add_money(amount)

		player_game.add_info_dialog_line(None, f'Acquired money: {amount}')
	return amount

def award_item_to_player_game(item_id: str, player_game):
	"""Award an item to player_game by item_id.
	Finds the item seed in const.ITEM_SEEDS, builds the Item, and gives to player_game.
	"""
	# local import to avoid circular dependency
	from game.objects.item import instantiate_item_from_id
	new_item = instantiate_item_from_id(item_id)
	# give to player_game
	if player_game is not None and new_item is not None:
		player_game.pick_up_item(new_item)

		player_game.add_info_dialog_line(None, f'Acquired item: {new_item.name}')


	return new_item

def remove_item_from_player_game(item_id: str, player_game):
	"""Remove an item from player_game by item_id."""
	if player_game is not None:
		removed = player_game.remove_single_item_unit_by_id(item_id)
		return removed
	return None

def award_task_to_player_game(task_id: str, player_game, parent_task):
	"""Award a task to player_game by task_id.
	Finds the task seed in const.TASKS, builds the Task, and gives to player_game.
	"""
	# find seed in constants
	seed = None
	for t in const.TASKS:
		if t.get('task_id') == task_id:
			seed = t
			break
	if seed is None:
		# nothing found
		return None
	# local import to avoid circular dependency
	from game.objects.task import build_task_from_seed
	new_task = build_task_from_seed(seed, parent_task.acquired_region if parent_task is not None else None)
	# give to player_game
	if player_game is not None:
		player_game.acquire_task(new_task)
	return new_task

def advance_chapter_in_player_game(player_game):
	player_game.advance_chapter()
	#input (f'Advanced to chapter {player_game.current_chapter}')
