from typing import Any, Dict, List, Tuple, Optional
import random
import importlib

from pydantic.types import T
from game.objects.city import City, Tile
from game.objects.item import Item
from game.objects.task import Task, build_task_from_seed, SpecialTaskToType, TaskType
from game.objects.npc import NPC
from game.objects.dungeon import Dungeon
from game.objects.player import ItemType
from game.services.world_map_generator import generate_world
import game.constants as const
from game.region_builder import build_region_map#, build_region_paint_fill
import time
import datetime


class PlayerGame:
	"""Container for global world tiles and loaded regions.6

	world_tiles maps (x,y) -> Tile instance for any tile we've generated/loaded.
	regions is a list of City/Region objects returned by the region builder so
	callers can inspect or reuse them later.
	"""
	
	from game.objects.player import  Player
	def __init__(self):
		from game.objects.player import  Player
		# self.name = autosave - (mm/dd/yyyy hh:mm:ss)
		self.name = "autosave - " + datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")		
		# world _tiles is the flattened version of all self.regions and those regions' child cities ...
		self.world_tiles: Dict[Tuple[int, int], Tile] = {}
		# we need id's on stored regions since there may be multiples with the same name... we can use position to determine which
		self.regions: List[City] = [] 
		# track last created region name to pick neighbors
		self.previous_region: Optional[City] = None
		self.last_region_name: Optional[str] = None
		self.characters: List[Player] = []
		# self.active_party: List[Player] = [] # 
		self.enemies_slain: Dict[str, int] = {}
		self.inventory: List[Item] = []
		self.money: int = 0
		self.max_inventory_count: int = 300
		self.x: int =0
		self.y: int =0
		self.z: int =0
		self.inside: bool = False
		self.save_id: int = None
		self.current_chapter = 0

		self.active_party: List[str] = [] # list of character _uuid in active party
		self.max_party_count = 5

		self.tasks: List[Task] = [] # List of active tasks for the player
		self.dungeons: List[Dungeon] = [] # List of dungeons created in the world
		self.npcs: List[NPC] = []

		self.info_dialogs: List[str] = [] # List of info dialogs shown to the player
		# Option dialog: a single pending choice prompt. Set by initiate_option_dialog events;
		# cleared by the TUI after the player picks an option (which awards the chosen task).
		self.option_dialog: Optional["OptionDialog"] = None
		self.pending_fight_mob_id: str = None # If set, indicates a pending fight with the given mob id
		self.chapter_task_waiting: bool = False
		self.pending_character: str = None # npc/character id of a pending character to be added to the party
		self.twisted_character: str = None # npc/character id of a twisted character which was changed when joingin from pending_character state
		self.final_character: str = None # npc/character id of the final character in the story
		self.intro_complete: bool = False
		self.completed_regional_quests: List[str] = [] # list of region ids where regional quests have been completed
		self.completed_regional_quests_2: List[str] = [] # list of region ids where Type B regional quests have been completed
		self.random_encounter_timer: int = random.randint(5,15) # timer for random encounters, counts down with player movement
		self.inside_aircraft: bool = False # whether the player is currently inside the aircraft
		self.phased: bool = False # whether the player is currently phased (e.g. introduced later in the game allowing the player overworld movement without encounters)
		self.aircraft_location: Optional[Tuple[int, int]] = None # location of the aircraft on the world map
		self.continents: Dict[int, List[str]] = {} # mapping of continent number to list of city names on that continent
		self.allow_ocean_flight: bool = False # whether the player has unlocked the ability to fly over ocean regions with the aircraft
		self.can_aircraft_fly: bool = True # whether the aircraft can currently fly (unlocked through story progression, separate from allow_ocean_flight which is a prerequisite for this but not sufficient on its own)
		self.npc_log_locked: bool = True # whether the NPC log is locked (unlocked through story progression)
		self.intro_max_cities: int = 4 #max size of the world during intro
		self.hyperway_unlocked: bool = False # whether the hyperway fast travel system is unlocked

	def unlock_hyperway(self):
		self.hyperway_unlocked = True

	def lock_hyperway(self):
		self.hyperway_unlocked = False

	def unlock_npc_log(self):
		self.npc_log_locked = False

	def get_max_cities(self):
		if self.intro_complete:
			return const.AVAILABLE_CITIES
		return self.intro_max_cities

	def set_aircraft_flyable(self, can_fly: bool):
		self.can_aircraft_fly = can_fly

	def allow_ocean_flight(self):
		self.allow_ocean_flight = True

	def set_player_location(self, pos: Tuple[int, int]):
		"""Set the player's location and update inside status."""
		self.x, self.y = pos
		self.z = 0
		tile = self.get_tile(self.x, self.y)
		if tile and tile.building:
			self.inside = True
		else:
			self.inside = False

	def remove_ocean(self):
		"""
		Finds all regions with display_name 'Ocean', removes their tiles from
		world_tiles, and then removes the regions themselves from the regions list.
		"""
		ocean_regions = [region for region in self.regions if region.display_name == 'Ocean']
		if not ocean_regions:
			print("No ocean regions found to remove.")
			return

		tiles_to_remove = set()
		for region in ocean_regions:
			for pos in region.tiles.keys():
				tiles_to_remove.add(pos)

		for pos in tiles_to_remove:
			if pos in self.world_tiles:
				del self.world_tiles[pos]

		# Rebuild the regions list, excluding the ocean regions
		self.regions = [region for region in self.regions if region.display_name != 'Ocean']

		print(f"Ocean removed. {len(tiles_to_remove)} tiles and {len(ocean_regions)} regions removed.")

	def enter_aircraft(self):
		if (self.x, self.y) == self.aircraft_location:
			self.inside_aircraft = True
			self.add_info_dialog_line(None, 'To the skies again.')
		else:
			self.add_info_dialog_line(None, 'The aircraft is not here.')

	def get_city_by_number(self, index: int) -> Optional[City]:
		"""Get city by 1-based index (useful for story/chapter progression)."""
		cities = self.get_cities()
		if 1 <= index <= len(cities):
			return cities[index - 1]
		return None

	def get_city_by_region_city_name(self, region_city_name: str) -> Optional[City]:
		for region in self.regions:
			if region.region_name in region_city_name and region.child_city and region.child_city.city_name in region_city_name:
				return region.child_city
		return None

	def get_cities(self) -> List[City]:
		"""Return a flat list of all child cities (the actual playable cities)."""
		return [region.child_city for region in self.regions 
				if region.child_city is not None]

	def land_aircraft(self):
		# Must be inside the aircraft to land
		if not getattr(self, 'inside_aircraft', False):
			self.add_info_dialog_line(None, "You are not inside the aircraft.")
			return

		# Do not allow landing while inside a dungeon or if a dungeon occupies this position
		if self.get_dungeon_at_position((self.x, self.y)):
			self.add_info_dialog_line(None, "You cannot land here, a dungeon occupies this location.")
			return

		# Check tile validity
		tile = self.get_tile(self.x, self.y)
		if tile is None:
			self.add_info_dialog_line(None, "You cannot land here, the terrain is unknown.")
			return

		# Reject buildings or impassable terrain
		if tile.type == 'building' or tile.type == 'impassable':
			self.add_info_dialog_line(None, "You cannot land here, the terrain is unsuitable (building or impassable).")
			return

		# Successful landing: record aircraft location and mark player not inside aircraft
		self.inside_aircraft = False
		self.aircraft_location = (self.x, self.y)
		self.add_info_dialog_line(None, f"You land the aircraft at {self.x},{self.y}.")

	def set_aircraft_location (self, location: Tuple[int, int]):
		self.aircraft_location = location

	def complete_region_quest(self, region_id: str):
		if region_id not in self.completed_regional_quests:
			self.completed_regional_quests.append(region_id)

		if self.check_regional_quests_complete():
			# check all tasks for task type CompleteRegionalQuests
			for task in self.tasks:
				if task.type == TaskType.CompleteRegionalQuests and not task.completed:
					self.complete_task(task)

	def complete_region_quest_2(self, region_id: str):
		if region_id not in self.completed_regional_quests_2:
			self.completed_regional_quests_2.append(region_id)

		if self.check_regional_quests_2_complete():
			for task in self.tasks:
				if task.type == TaskType.CompleteRegionalQuests2 and not task.completed:
					self.complete_task(task)

	def check_regional_quests_complete(self):
		return len(self.completed_regional_quests) >= len(const.REGIONAL_QUEST_REGIONS)

	def check_regional_quests_2_complete(self):
		return len(self.completed_regional_quests_2) >= len(const.REGIONAL_QUEST_REGIONS)

	def complete_intro_story(self):
		# check all tasks for task type CompleteIntroStory
		self.intro_complete = True

		for task in self.tasks:
			if task.type == TaskType.CompleteIntroStory and not task.completed:
				self.complete_task(task)

		
		print('Generating world regions...')
		seed = abs(hash(self.characters[0].name)) % (10 ** 8) 
		self = generate_world(self, num_regions=10000, seed_base=seed, min_size=500, verbose=True)
		self._create_donut()

	def _create_donut(self):
		"""
		A donut is a flat map world that allows the player to wrap E-W and N-S. effectively not a globe. A donut.
		"""
		seed = abs(hash(self.characters[0].name)) % (10 ** 8) 

		from game.services.continent_service import build_continents_and_ocean
		result = build_continents_and_ocean(self,
										rng_seed=seed,
										spread_radius=30,
										ocean_padding=15)

		# ocean_bbox = result.get("ocean_bbox")
		# ocean_region = result.get("ocean_region")
		# continent_count = len(result.get("continents", []))
		# ocean_tiles = len(ocean_region.tiles) if ocean_region else 0
   
		# print(f"Continents grouped: {continent_count}, ocean_bbox={ocean_bbox}, ocean_tiles={ocean_tiles}")
		# for comp in result.get("continent_compositions", []):
		# 	cont_num = comp.get("continent_number", "?")
		# 	city_names = comp.get("city_names", [])
		# 	print(f" Continent {cont_num} cities: {city_names}")
		# input("Press Enter to continue...")
		#self.continents = {comp.get("continent_number", "?"): comp.get("city_names", []) for comp in result.get("continent_compositions", [])}

	def lock_dungeon_by_id(self, dungeon_id: str):
		dungeon = next((d for d in self.dungeons if d.id == dungeon_id), None)
		if dungeon:
			dungeon.set_locked(True)

	def unlock_dungeon_by_id(self, dungeon_id: str):
		dungeon = next((d for d in self.dungeons if d.id == dungeon_id), None)
		if dungeon:
			dungeon.set_locked(False)

	def set_dungeon_locked_text_by_id(self, dungeon_id: str, locked_text: str):
		dungeon = next((d for d in self.dungeons if d.id == dungeon_id), None)
		if dungeon:
			dungeon.locked_text = locked_text

	def add_dungeon_standing_text(self, dungeon):
		"""" add dungeon standing text to info dialogs"""
		if dungeon.standing_text and len(dungeon.standing_text) > 0:
			for line in dungeon.standing_text:
				self.add_info_dialog_line(dungeon.display_name, line)

	def acquire_task(self, task: Task) -> None:
		"""Add a new task to the player's active tasks."""
		exists = any(t.task_id == task.task_id for t in self.tasks)
		if not exists:
			#print (f'Acquiring task {task.task_id} of type {task.type}')
			self.tasks.append(task)
		else:
			input (f'Task {task.task_id} of type {task.type} already acquired')

		if task.task_acquire_events:
			for event in task.task_acquire_events:
				#print (f'Executing acquire event for task {task.task_id} of type {task.type}')
				event.execute(self, task)

		if task.type == TaskType.CompleteIntroStory:
			if task.check_completion_terms(self):
				self.complete_task(task)
		if task.type == TaskType.CompleteRegionalQuests:
			if task.check_completion_terms(self):
				self.complete_task(task)
		if task.type == TaskType.CompleteRegionalQuests2:
			if task.check_completion_terms(self):
				self.complete_task(task)

	def complete_task(self, task) -> None:
		"""Mark the given task as completed and run its completion events."""
		#print (f'Completing task {task.task_id} of type {task.type}')
		task.completed = True
		if task.task_complete_events:
			for event in task.task_complete_events:
				event.execute(self, task)

	def cancel_task(self, task) -> None:
		"""SET THE TASK TO COMPLETED WITHOUT TRIGGERING IT'S EVENTS"""
		#print (f'Cancelling task {task.task_id} of type {task.type}')
		task.completed = True

	def remove_task(self, task) -> None:
		"""REMOVE THE TASK FROM THE PLAYER GAME WITHOUT TRIGGERING IT'S EVENTS"""
		#print (f'Removing task {task.task_id} of type {task.type}')
		self.tasks = [t for t in self.tasks if t.task_id != task.task_id]

	def check_complete_boss_mob(self, mob_id: str) -> None:
		"""Check for dungeon boss mob completion tasks for the given mob_id.
		If found, complete the task.
		"""
		for task in self.tasks:
			#print (f'Checking task {task.task_id} for mob {mob_id}, task __class__.__name__ ={task.__class__.__name__}')
			if task.type == TaskType.Defeat and not task.completed:
				#print (f'Checking defeat task {task.task_id} for mob {mob_id}')
				if task.to_type == SpecialTaskToType.MOB and task.to_id == mob_id:
					#print (f'Completing defeat task {task.task_id} for mob {mob_id}')
					self.pending_fight_mob_id = None
					self.complete_task(task)
		#input (f'defeat task complete for mob {mob_id}')
			
	def translate_npc_ref_to_id(self, to_id):
		if to_id == 'pending_character':
			return self.pending_character
		if to_id == 'final_character':
			return self.final_character
		if to_id == 'twisted_character':
			return self.twisted_character
		return to_id

	def get_npc_details(self, npc: NPC):
		# if npc in self.npcs:
		exist = next((n for n in self.npcs if n.id == npc.id), None)
		if not exist:
			return None

		# search incomplete tasks for npc_id = npc.id
		# we need to check both Meet tasks and Deliver tasks

		tasks_for_npc  = [n for n in self.tasks 
							if not n.completed and 
								n.type == TaskType.Meet and 
								n.to_type == SpecialTaskToType.NPC and 
								self.translate_npc_ref_to_id(n.to_id) == npc.id]
		tasks_for_npc += [n for n in self.tasks 
							if not n.completed and 
								n.type == TaskType.Deliver and 
								n.to_type == SpecialTaskToType.NPC and 
								self.translate_npc_ref_to_id(n.to_id) == npc.id]
		has_tasks = len(tasks_for_npc) > 0

		result = {
			'npc': exist,
			'location_description': 'Unknown',
			'has_tasks': has_tasks
		}
		if exist.position:
			result['location_description'] = self.get_location_description(exist.position)
		else:
			if exist.location_reference_id:
				dungeon = next((d for d in self.dungeons if d.id == exist.location_reference_id), None)
				if dungeon:
					result['location_description'] = f'Dungeon: {dungeon.display_name}'
		
		return result

	def get_location_description(self, position):
		_, active_area = self.get_region_and_active_area_for_position(position)
		x, y = position
		tile = active_area.get_tile(x, y)
		area_display_name = active_area.display_name
		building_display_name = 'Outside'
		if tile.building:
			building_display_name = tile.building.get('display_name')

		return f'{area_display_name} - {building_display_name}'

	def get_all_characters(self):
		return self.characters

	def add_character_to_active_party(self, char):
		if len(self.active_party) < self.max_party_count:
			if char in self.characters:
				self.active_party.append(char._uuid)

	def remove_character_from_active_party(self, char):		
		if len(self.active_party) >1:
			if char._uuid in self.active_party:
				self.active_party.remove(char._uuid)

	def get_active_party(self):
		active_chars = []
		for char_uuid in self.active_party:
			char = next((c for c in self.characters if c._uuid == char_uuid), None)
			if char:
				active_chars.append(char)
		return active_chars

	def hide_npc(self, npc: NPC):
		""" Set position of NPC to None"""
		for f_npc in self.npcs:
			if f_npc == npc:
				f_npc.position = None

				#print (f'Hiding NPC {npc.name} from player view')
				for dungeon in self.dungeons:
					#print (f'Checking dungeon at position {dungeon.position} for NPC {npc.name}')
					dungeon.hide_npc(npc)

				#input (f'NPC {npc.name} hidden successfully')
				break

	def add_character_dialog_lines(self, npc_id: str, dialog_lines: List[str]):
		""" Add dialog lines of unlocked characters"""
		#print (f'Adding dialog lines to NPC with npc_id {npc_id}.... also len npc = {len(self.npcs)}')
		for character in self.get_all_characters():
			if character.npc_id == npc_id:
				#print (f'Adding dialog lines to NPC {character.name}')
				for line in dialog_lines:
					self.add_info_dialog_line(character.name, line)
				#input (f'Added {len(dialog_lines)} dialog lines to NPC {character.name}')
				break
	
	def add_npc(self, npc: NPC):
		""" Add an NPC to the player game if not already present."""
		exists = next((n for n in self.npcs if n.id == npc.id), None)
		if not exists:
			self.npcs.append(npc)

	def get_available_character_npc_id(self) -> str:
		""" 
		Return an available npc_id from const.PLAYER_NPCS that is not already used by existing characters.
		"""
		exist_npc_ids = [ch.npc_id for ch in self.get_all_characters() if ch.npc_id]
		seed = int(len(exist_npc_ids) * abs(hash(self.name))) % 2147483647
		candidates = [player_npc.get('npc_id') for player_npc in const.PLAYER_NPCS if player_npc.get('npc_id') not in exist_npc_ids]
		if not candidates or len(candidates) == 0:
			return None
		return random.choice(candidates)

	def add_character_npc(self, pos):
		""" 
		NPC added to player game for world events.
		pending_character set to store npc_id for dialog and character creation.
		initiate_dialog events.
		"""
		npc_id = self.get_available_character_npc_id()
		for player_npc in const.NPCS:
			if player_npc.get('npc_id') == npc_id:
				name = player_npc.get('name')
				description = player_npc.get('description', '')
				npc = NPC(id=npc_id, name=name, description=description, position=pos)
				self.add_npc(npc)
				self.pending_character = npc_id
				break

	def add_pending_character(self):
		if self.pending_character:
			seed = int(time.time() * 1000) % 2147483647
			# optionally mix in random to reduce collisions when loop is fast
			seed ^= random.getrandbits(31)

			npc_id = self.pending_character
			p = self.generate_player_character(seed=seed, level=self.get_max_character_level(), character_npc_id=npc_id)
			p.npc_id = npc_id		

			self.add_character(p)
			self.twisted_character = self.pending_character
			self.pending_character = None
			#
			dialog_id = 'add_pending_character'
			from services.task_completion_service import initiate_dialog_to_player_game
			params = {
				'npc_id': npc_id,
				'dialog_id': dialog_id
			}
			initiate_dialog_to_player_game(params, self)

			#### NEED TO ADD THEIR INTRO TEXT IN THE DUNGEON OR SITUATION NOT HERE
			self.add_info_dialog_line(None, f'{p.name} has joined your party!')

	def place_player_in_dungeon_at_location(self, dungeon_id, location_type):
		if not dungeon_id or self is None:
			return None
		dungeon = None
		for d in self.dungeons:
			if d.id == dungeon_id:
				dungeon = d
				break
		if dungeon is None:
			input (f'Dungeon to set player in not found: {dungeon_id}')
			return None
		self.set_position(dungeon.position[0], dungeon.position[1], 0)
		self.inside = False
		dungeon.place_player_at_location(location_type)

	def remove_player_from_dungeon(self, dungeon_id):
		if not dungeon_id or self is None:
			return None
		dungeon = None
		for d in self.dungeons:
			if d.id == dungeon_id:
				dungeon = d
				break
		if dungeon is None:
			input (f'Dungeon to remove player from not found: {dungeon_id}')
			return None
		dungeon.remove_player_from_dungeon()

	def add_final_character(self, dialog_id):
		if self.final_character:
			seed = int(time.time() * 1000) % 2147483647
			# optionally mix in random to reduce collisions when loop is fast
			seed ^= random.getrandbits(31)
			npc_id = self.final_character
			p = self.generate_player_character(seed=seed, level=self.get_max_character_level(), character_npc_id=npc_id)
			p.npc_id = npc_id		
			self.add_character(p)
			from services.task_completion_service import initiate_dialog_to_player_game
			params = {
				'npc_id': npc_id,
				'dialog_id': dialog_id
			}
			initiate_dialog_to_player_game(params, self)
			self.add_info_dialog_line(None, f'{p.name} has joined your party!')

	def add_random_player_character(self, dialog_id: str):
		seed = int(time.time() * 1000) % 2147483647
		# optionally mix in random to reduce collisions when loop is fast
		seed ^= random.getrandbits(31)
		p = self.generate_player_character(seed=seed, level=self.get_max_character_level())
		p_name = p.name
		npc_id = next(player_npc.get('npc_id') for player_npc in const.PLAYER_NPCS if player_npc.get('name') == p_name)

		from services.task_completion_service import initiate_dialog_to_player_game
		params = {
			'npc_id': npc_id,
			'dialog_id': dialog_id
		}
		initiate_dialog_to_player_game(params, self)

		#input (f'Adding random player character {p.name} with npc_id {npc_id}... npc len: {len(self.npcs)}')
		if not any(npc for npc in self.npcs if npc.id == npc_id):
			for npc_seed in const.NPCS:
				seed_id = npc_seed.get('npc_id')
				if seed_id == npc_id:
					seed = npc_seed
					break		

			name = seed.get('name')
			description = seed.get('description', '')
			npc = NPC(id=npc_id, name=name, description=description, position=None)
			self.npcs.append(npc)

		p.npc_id = npc_id		

		self.add_character(p)
		self.add_info_dialog_line(None, f'{p.name} has joined your party!')

	def generate_player_character(self, seed, level, character_npc_id = None):
		rng = random.Random(seed)
		
		if not character_npc_id:
			exist_character_names = [ch.name for ch in self.get_all_characters()]
			candidates = [ch_key for ch_key in const.CHARACTER_CLASS_MAP.keys() if const.CHARACTER_CLASS_MAP[ch_key] not in exist_character_names]

			atype = rng.choice(candidates)
		else:
			atype = character_npc_id
		display_name = f"{const.CHARACTER_CLASS_MAP.get(atype, atype).strip()}"

		from combat_balancing_simulation.player_generator import generate_player
		player = generate_player(name=display_name, focus=atype, target_level=level, seed=seed, player_game=self)

		return player

	def countdown_random_encounter_timer(self):
		if self.phased or self.inside_aircraft:# or True:
			return False

		if self.random_encounter_timer >0:
			#input (f'Random encounter timer: {self.random_encounter_timer}... player position: {(self.x, self.y, self.z)}')
			self.random_encounter_timer -=1
		
		if self.random_encounter_timer <=0:
			# check if in city, region or dungeon... set timer based on location (e.g. shorter in dungeons, longer in cities)
			dungeon = self.get_dungeon_at_position((self.x, self.y))
			if dungeon:
				player_pos = dungeon.get_player_pos()
				#Calculate dungeon random encounter timer
				if player_pos is not None and player_pos != (0,0,0):
					rng = random.Random(abs(hash(player_pos)) * abs(hash(dungeon.id)))
					self.random_encounter_timer = rng.randint(5,13)

			_, current_area = self.get_region_and_active_area_for_position((self.x, self.y))
			if current_area:
				seed_base = (self.x, self.y)
				rng = random.Random(seed_base)
				if current_area.isCity():
					#Calculate city random encounter timer
					self.random_encounter_timer = rng.randint(11,22)
				else:
					#Calculate region random encounter timer
					self.random_encounter_timer = rng.randint(9,16)

			return True


	def add_character(self, character: Player):
		# if len(self.active_party) < self.max_party_count:
		# 	self.active_party.append(character))
		self.characters.append(character)
		if len(self.active_party) < self.max_party_count:
			self.active_party.append(character._uuid)

	def set_pending_fight_mob(self, mob_id: str) -> None:
		"""Set the pending fight mob id."""
		self.pending_fight_mob_id = mob_id

	def pop_dialog(self) -> Optional[str]:
		"""Pop the next info dialog to show to the player, if any."""
		if self.info_dialogs and len(self.info_dialogs) >0:
			return self.info_dialogs.pop(0)
		return None

	def add_info_dialog_line(self, npc_name, l):
		if npc_name is not None:
			self.info_dialogs.append(f'{npc_name}: {l}')
		else:
			self.info_dialogs.append(f'{l}')

	def get_npcs_at_player_location(self) -> List[NPC]:
		"""Return a list of NPCs at the player's current location."""
		npcs_at_location = []
		for npc in self.npcs:
			if npc.position == (self.x, self.y) and self.z == 0:
				npcs_at_location.append(npc)
		return npcs_at_location

	def handle_npc_interaction_at_player_location(self, npc_id: str = None):
		"""Check for NPC interaction at the player's location.
		If an NPC is present, return their name; otherwise return None.

		this signals the completion of a meet task if it exists for this this location

		"""
		if npc_id and npc_id == 'pending_character':
			npc_id = self.pending_character
		if npc_id and npc_id == 'final_character':
			npc_id = self.final_character
		can_interact, npc_name, npc_id = self._can_npc_interact_at_player_location(npc_id)

		if can_interact:
			# check for meet tasks with this npc
			for task in self.tasks:
				if task.type == TaskType.Meet and not task.completed:
					task_to_id = self.translate_npc_ref_to_id( task.to_id)
					if task.to_type == SpecialTaskToType.NPC and task_to_id == npc_id:
						# set NPC met flag to true
						npc = next((n for n in self.npcs if n.id == npc_id), None)
						if npc:
							npc.met = True
						self.complete_task(task)
						return
			# check for deliver tasks with this npc
			for task in self.tasks:
				"""
				    elif ttype == 'deliver':
					special_item_id = seed.get('item_id')
					to_type = seed.get('to_type')
					to_id = seed.get('to_id')
					stt = SpecialTaskToType(to_type)
					task = DeliverTask(tid, special_item_id, stt, to_id)
				"""
				if task.type == TaskType.Deliver and not task.completed:
					task_to_id = self.translate_npc_ref_to_id( task.to_id)
					if task.to_type == SpecialTaskToType.NPC and task_to_id == npc_id:
						self.complete_task(task)
						return
			npc = next((n for n in self.npcs if n.id == npc_id), None)
			if npc:
				npc.met = True
				if npc.standing_text and len(npc.standing_text) > 0:
					for line in npc.standing_text:
						self.add_info_dialog_line(npc.name, line)
	def set_npc_met(self, npc_id: str):
		npc = next((n for n in self.npcs if n.id == npc_id), None)
		if npc:
			npc.met = True

	def _can_npc_interact_at_player_location(self, npc_id: str = None) -> Tuple[bool, str, str]:
		""" if there is an npc at the player location return true and their name"""		
		for npc in self.npcs:
			#input (f'Checking NPC {npc.name} at position {npc.position} against player position {(self.x, self.y, self.z)}')
			if npc.position == (self.x, self.y) and self.z == 0 and (npc.id == npc_id if npc_id else True):
				return True, npc.name, npc.id
		return False, "", ''

	def handle_fast_travel_from_player_location(self, destination: Tuple[int, int]) -> None:
		"""Handle fast travel from the player's current location to the given destination.
		Update the player's position accordingly.
		"""
		self.money -= 100
		self.x, self.y = destination
		self.z = 0  # Assume fast travel always lands on ground level

	def get_player_continent_cities(self):
		"""Return the continent number the player is currently on based on their location."""
		player_chapter_city = self.get_player_chapter_city()
		player_continent_cities = None
		for continent_number, city_names in self.get_continents().items():
			#print (f'Checking continent {continent_number} with cities {city_names} against player chapter city {player_chapter_city}')
			if player_chapter_city in city_names:
				#print (f'Player is on continent {continent_number} with cities {city_names}')
				player_continent_cities = city_names
				break
		#input (f'Player continent cities: {player_continent_cities} for player chapter city {player_chapter_city}')
		return player_continent_cities

	def get_continents(self):
		continents = {}

		index = 0

		for continent_number, comp in enumerate(const.CONTINENT_COMPOSITION, start=1):
			continents[continent_number] = (
				const.CHAPTER_CITY_ORDER[index:index+comp]
			)
			index += comp

		return continents

	def get_player_chapter_city(self):
		player_region, player_area = self.get_region_and_active_area_for_position((self.x, self.y))
		if player_area and player_area.isCity():
			#print (f'Player is in city {player_area.city_name} in region {player_region.region_name}')
			return player_region.region_name + "_" + player_area.city_name
		return None

	def get_all_hyperways(self) -> List[Dict[str, Any]]:
		"""
		Return a list of all hyperway entrances in the world.
		Display list for user selection.

		if hyperway locked only allow subways on the same continent as the player location, if unlocked allow all hyperways with visited active areas.
		use continents to determine if player current location is on the same continent as a hyperway when hyperway is locked. when hyperway is unlocked ignore continents and just check if active area visited.
		self.continents: Dict[int, List[str]] = {} # mapping of continent number to list of city names on that continent
		"""
		player_continent_cities = self.get_player_continent_cities()
		hyperway_positions = []		
		for (x, y), tile in self.world_tiles.items():
			if tile.building and tile.building.get('type') == 'hyperway':
				region_area, area = self.get_region_and_active_area_for_position((x, y))
				if self.hyperway_unlocked:
					if area.visited:
						hyperway_positions.append({ 'description': self.get_location_description((x,y)), 'position': (x, y)})
				else:
					#print (f'Checking hyperway at {(x,y)} for player continent cities {player_continent_cities} with region_area {region_area.region_name if region_area else None} and area {area.city_name if area else None}')
					for city_name in player_continent_cities:
						if area and (region_area.region_name + "_" + area.city_name) == city_name:
							hyperway_positions.append({ 'description': self.get_location_description((x,y)), 'position': (x, y)})
							break
		#input (f'Found {len(hyperway_positions)} hyperway entrances available to player at positions {[p["position"] for p in hyperway_positions]}')
		return hyperway_positions

	def get_dungeon_at_position(self, pos: Tuple[int, int] = None) -> Optional[Dungeon]:
		if not pos:
			pos = self.x, self.y

		for dungeon in self.dungeons:
			if dungeon.position == pos:
				return dungeon
		return None

	def add_dungeon(self, dungeon: Dungeon) -> None:
		exists = any(d.position == dungeon.position for d in self.dungeons)
		if not exists:
			self.dungeons.append(dungeon)

	def set_position(self, x: int, y: int, z: int =0) -> None:
		self.x = x
		self.y = y
		self.z = z

		if self.inside_aircraft:
			self.aircraft_location = (x, y)

	def check_meet_npc_dungeon(self, npc_id):
		"""Check if there is a meet task for the given npc_id in any dungeon the player is in.
		If found, return the NPC object; otherwise return None.
		"""
		for dungeon in self.dungeons:
			for (x, y, z), tile in dungeon.tiles.items(): 
				if tile.entities: 
					for ent in tile.entities: 
						if isinstance(ent, dict) and ent.get("npc_id") == npc_id:
							entity_id = ent.get("npc_id")
							task_completed = False
							for task in self.tasks:
								print(f'Checking task {task.task_id} for npc {npc_id} in dungeon {dungeon.display_name}')
								if task.type == TaskType.Meet and not task.completed:
									print (f'Checking meet task {task.task_id} for npc {npc_id} in dungeon {dungeon.display_name}')
									task_to_id = self.translate_npc_ref_to_id(task.to_id)
									if task.to_type == SpecialTaskToType.NPC and task_to_id == npc_id:
										print (f'Completing meet task {task.task_id} for npc {npc_id} in dungeon {dungeon.display_name}')
										npc = next((n for n in self.npcs if n.id == npc_id), None)
										if npc:
											npc.met = True
										self.complete_task(task)
										task_completed = True
								if task.type == TaskType.Deliver and not task.completed:
									#print (f'Checking deliver task {task.task_id} for npc {npc_id} in dungeon {dungeon.display_name}')
									task_to_id = self.translate_npc_ref_to_id(task.to_id)
									if task.to_type == SpecialTaskToType.NPC and task_to_id == npc_id:
										npc = next((n for n in self.npcs if n.id == npc_id), None)
										if npc:
											npc.met = True
										#print (f'Completing deliver task {task.task_id} for npc {npc_id} in dungeon {dungeon.display_name}')
										self.complete_task(task)
										task_completed = True
							# if no tasks add npc standing text to info dialogs
							if not task_completed:
								npc = next((n for n in self.npcs if n.id == npc_id), None)
								if npc:
									npc.met = True
									if npc.standing_text and len(npc.standing_text) > 0:
										for line in npc.standing_text:
											self.add_info_dialog_line(npc.name, line)

	def enter(self, floor: int =1) -> None:
		"""Mark player as inside on the given display floor (1-based).

		Internally we store vertical position in `z` where z == (floor -1).
		"""
		self.inside = True
		
		self.z = int(floor) -1
	
	def exit(self) -> None:
		"""Exit building and return to main floor (display floor1 -> z =0)."""
		self.inside = False
		self.z =0

	def add_money(self, amount: int) -> None:
		if amount <=0:
			return
		self.money += int(amount)
	
	def pick_up_item(self, item: ItemType) -> bool:
		"""Attempt to pick up an item and add to inventory.
		Returns True if successful, False if inventory full.
		"""
		exist_item = next((i for i in self.inventory if i.id == item.id), None)

		if len(self.inventory) >= self.max_inventory_count and not exist_item:
			return False
		
		if exist_item:
			#print (f'Increasing quantity of existing item {item.id} by {item.quantity}')
			exist_item.quantity += item.quantity
		else:
			if item.quantity <=0:
				item.quantity =1
			self.inventory.append(item)
			#print (f'Adding new item {item.id} with quantity {item.quantity} to inventory')

		#input (f'Picked up item {item.id}, total inventory count now {len(self.inventory)}')
		return True

	def remove_single_item_unit(self, item: ItemType) -> bool:
		"""Remove a single unit of the given item from inventory.
		Returns True if successful, False if item not found.
		"""
		for i, inv_item in enumerate(self.inventory):
			if inv_item.id == item.id:
				if inv_item.quantity >=1:
					inv_item.quantity -=1

				if inv_item.quantity <= 0:
					self.inventory.pop(i)
				return True
		return False

	def remove_single_item_unit_by_id(self, item_id: str) -> bool:
		"""Remove a single unit of the given item from inventory by id.
		Returns True if successful, False if item not found.
		"""
		for i, inv_item in enumerate(self.inventory):
			if inv_item.id == item_id:
				if inv_item.quantity >=1:
					inv_item.quantity -=1
				if inv_item.quantity <= 0:
					self.inventory.pop(i)
				return True
		return False

	def find_region_by_id(self, region_id: int) -> Optional[object]:
		"""Find a region by its id attribute."""
		for region in self.regions:
			
			if region.region_city_id == region_id:
				return region
			
		return None
	
	def merge_region(self, region_city: object) -> None:
		"""Merge all tiles from a generated region city into world_tiles."""
		# merge parent region tiles
		for (x, y), t in list(region_city.tiles.items()):
			self.world_tiles[(x, y)] = t
		# if the region has a child_city (an in-memory city used to seed the
		# region), merge those tiles as well so the world map stores persistent
		# tiles for both. -- no. regions are stored as is with their child_city intact and not flattened data... <thats prodeced data
		# if we need a method for flattening data that is a seperate thing to what is stored in self.regions
		
		if hasattr(region_city, 'child_city') and region_city.child_city:
			for (x, y), t in list(region_city.child_city.tiles.items()):
				self.world_tiles[(x, y)] = t		

	def has_tile(self, x: int, y: int) -> bool:
		return (x, y) in self.world_tiles

	def get_tile(self, x: int, y: int):
		return self.world_tiles.get((x, y))

	def is_new_area_enclosed(self, center: Tuple[int,int], check_rad: int =4) -> bool:
		"""
		Check if the selected area to crea a region in is fully enclosed by existing tiles.
		Radius must be big enough to cover the new region area. Or it can be considered encosed and the second test doesn't matter
		"""
		cx, cy = center
		for dx in range(-check_rad, check_rad +1):
			for dy in range(-check_rad, check_rad +1):
				tx = cx + dx
				ty = cy + dy
				if (tx, ty) not in self.world_tiles:
					return False
		return True

	def can_build_city_in_range(self, center: Tuple[int,int], min_distance: int =10) -> bool:
		""" 
		Checks if a new region which has been selected to be built has a large enough area to build the city... 
		the city must also be a distance from the current region which is detailed in the city creation process
		"""
		cx, cy = center
		for region in self.regions:
			
			# get region center
			min_x = min(tx for (tx, ty) in region.tiles.keys())
			max_x = max(tx for (tx, ty) in region.tiles.keys())
			min_y = min(ty for (tx, ty) in region.tiles.keys())
			max_y = max(ty for (tx, ty) in region.tiles.keys())
			region_cx = (min_x + max_x) //2
			region_cy = (min_y + max_y) //2
			# compute distance
			dist = ((cx - region_cx) **2 + (cy - region_cy) **2) **0.5
			if dist < min_distance:
				return False
			
		return True
	def get_regions_that_can_be_built(self):
		"""Return region types we may still build.

		Previous logic appended a region name whenever no region of that name
		existed (or if there were still unused city names). That allowed
		unbounded creation of region instances of the same type (especially when
		child_city was often None), producing many region instances while only a
		few child cities existed.

		New behavior: limit the total number of region instances per region
		type to the number of available city names (len(const.AVAILABLE_CITIES)).
		If the existing instances for a region_name already reach that limit we
		do not allow more of that region type.
		"""
		res_regions = []
		max_instances_per_region = len(const.AVAILABLE_CITIES)

		for region_name in const.AVAILABLE_REGIONS:
			# count only existing region instances that have an actual child_city
			exist_cities = [c.child_city.city_name for c in self.regions
							if c.region_name == region_name and c.child_city is not None]

			# if we've already used up all distinct city names for this region type, skip it
			if len(exist_cities) >= max_instances_per_region:
				continue

			res_regions.append(region_name)

		return res_regions

	def get_available_city_type_for_region(self, region_name: str) -> Optional[str]:
		"""
		Determines an available city type (e.g., 'small_city') for a given region
		that has not yet been created in the world.
		"""
		existing_cities = {c.child_city.city_name for c in self.regions if c.region_name == region_name and c.child_city}
		available_cities = [city_type for city_type in const.AVAILABLE_CITIES if city_type not in existing_cities]

		if not available_cities:
			return None

		#get chapter city
		if self.current_chapter < len(const.CHAPTER_CITY_ORDER):
			city_order_entry = const.CHAPTER_CITY_ORDER[self.current_chapter]
			# The format is "region_size_city", so we extract the city size.
			parts = city_order_entry.split('_')
			if len(parts) == 3 and parts[0] == region_name:
				city_type = f"{parts[1]}_{parts[2]}"
				if city_type in available_cities:
					return city_type
		
		return None

	def get_region_of_chapter_city(self) -> Optional[str]:
		"""
		Determines the region name for the city corresponding to the current chapter.
		"""
		if self.current_chapter < len(const.CHAPTER_CITY_ORDER):
			city_order_entry = const.CHAPTER_CITY_ORDER[self.current_chapter]
			# The format is "region_size_city", so we split by '_' and take the first part.
			region_name = city_order_entry.split('_')[0]
			if region_name in const.AVAILABLE_REGIONS:
				return region_name
		return None

	def create_region_at(self, origin: Tuple[int,int]) -> object:
		"""Create a new region centered at `origin`.

		If no regions exist yet, pick a random initial region from AVAILABLE_REGIONS.
		Otherwise pick a region type from REGIONAL_NEIGHBORS of the last created region.
		The method imports the appropriate `game.region_seeds.constants_<name>` module
		to obtain `REGION_SETTINGS`, calls `build_region_map`, merges the result and
		returns the created region city.
		"""
		if self.get_city_count() == self.get_max_cities():
			return None

		# decide region name
		possible_regions = self.get_regions_that_can_be_built()
		if not possible_regions or len(possible_regions) == 0:
			return None

		has_city: bool = False
		if self.previous_region and self.previous_region.child_city is not None:
			main_city = False
		elif self.previous_region and random.random() < 0.8:
			has_city = True
		elif self.previous_region is	None:
			has_city = True

		if has_city:
			region_name = self.get_region_of_chapter_city()
		else:
			neigh = const.REGIONAL_NEIGHBORS.get(self.last_region_name, possible_regions)

			neigh = [r for r in neigh if r in possible_regions]

			if not neigh or len(neigh) == 0:
				neigh = possible_regions
			region_name = random.choice(neigh)

		# import region settings module dynamically
		attr = f"{region_name.upper()}_REGION_SETTINGS"
		region_settings = getattr(const, attr)
		
		#input (f'Building region {region_name} at {origin}...')
		rc = build_region_map(self, region_settings, origin, has_city, ignored_locations=set(self.world_tiles.keys()))

		setattr(rc, 'region_name', region_name)

		add_main_story = False
		if not self.regions or len(self.regions) == 0:
			add_main_story = True

		#input (f'Creating region {region_name} at {rc.get_center_position()} with child city {rc.child_city.city_name if rc.child_city else "None"}')
		# determine if there are any other regions with the same name that already have a child_city... if not create and acquire primary_story task
		exists = any(r.region_name == region_name for r in self.regions)
		add_region_task = False
		add_city_task = False
		if rc.child_city is not None:
			add_city_task = True
			if exists:
				exist_cities = [c.child_city.city_name for c in self.regions if c.region_name == region_name and c.child_city is not None]
				#print (f'Existing cities for region {region_name}: {exist_cities}')
				if not exist_cities or len(exist_cities) == 0:
					add_region_task = True
			else:
				add_region_task = True

		self.merge_region(rc)
		self.regions.append(rc)
		self.previous_region = rc
		self.last_region_name = region_name
		
		#print (f'Created region {region_name} at {origin} with child city {rc.child_city.city_name if rc.child_city else "None"}. add_region_task: {add_region_task}, add_city_task: {add_city_task}, add_main_story: {add_main_story}')
		if add_region_task:
			primary_task = self.create_primary_story_task_for_region(rc)
			if primary_task:
				#print (f'Acquired primary story task {primary_task.task_id} for region {region_name}.')
				self.acquire_task(primary_task)

		if add_main_story:
			main_story_task = self.advance_chapter()
			if main_story_task:
				#print (f'Acquired main story task {main_story_task.task_id} for initial chapter.')
				self.acquire_task(main_story_task)

		if add_city_task:
			#print (f'Attempting to acquire city story task for city {rc.child_city.city_name} in region {region_name}...')
			city_task = self.initiate_city_story_task_chain(rc.region_name, rc.child_city)
			if city_task:
				#print (f'Acquired city story task {city_task.task_id} for city {rc.child_city.city_name} in region {region_name}.')
				self.acquire_task(city_task)

		#print (f'city_count: {self.get_city_count()}, current_chapter: {self.current_chapter}, chapter_task_waiting: {self.chapter_task_waiting}')
		if self.get_city_count() >= self.current_chapter and self.chapter_task_waiting:
			#print (f'City count {self.get_city_count()} meets requirement for advancing chapter {self.current_chapter + 1}. Advancing chapter...')
			self.advance_waiting_chapter()
		#input (f'Created region {region_name} at {origin}')
		return rc

	def get_city_count(self):
		return len([region for region in self.regions if region.child_city is not None])

	def advance_waiting_chapter(self):
		self.chapter_task_waiting = False
		self.advance_chapter()

	def advance_chapter(self) -> Optional[Task]:
		# advance to next chapter and return first task of that chapter's main story
		next_chapter = self.current_chapter + 1

		# if not self.chapter_task_waiting:
		#print(f'Advancing to chapter {next_chapter}')
		if self.get_city_count() < next_chapter:
			#print(f'Not enough cities ({self.get_city_count()}) to advance to chapter {next_chapter}, waiting...')
			self.chapter_task_waiting = True
		else:
			story_id = f"main_story_chapter_{next_chapter}"
			game_cities = [region.child_city for region in self.regions if region.child_city is not None]
			#print(f'Looking for main story chapter {next_chapter} with story id {story_id} among {len(game_cities)} available cities.')
			for main_story in const.MAIN_STORY_SETTINGS:
				if main_story['chapter_id'] == story_id:
					first_task_seed = main_story['tasks'][0]
					chapter_city =  game_cities[next_chapter - 1]
					task = build_task_from_seed(first_task_seed, chapter_city)
					#print(f'Acquired main story task {task.task_id} for chapter {next_chapter}.')
					self.current_chapter = next_chapter
					self.acquire_task(task)
		#print(f'No main story found for chapter {next_chapter}.')

	def get_sellable_inventory(self) -> List[Item]:
		"""Return a list of items in inventory that can be sold."""
		sellable_items = []
		from game.objects.special_item import SpecialItem

		# Check if the item has a value and is not a special item
		for item in self.inventory:
			if item.value and item.value > 0 and not isinstance(item, SpecialItem):
				sellable_items.append(item)

		return sellable_items

	def is_location_surrounded_by_impassable_or_buildings(self, pos):
		"""Check if the given tile location is surrounded on all four sides by
		impassable tiles or building tiles.
		"""
		tx, ty = pos
		directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # left, right, up, down
		for dx, dy in directions:
			neighbor_x = tx + dx
			neighbor_y = ty + dy
			neighbor_tile = self.get_tile(neighbor_x, neighbor_y)
			if neighbor_tile:
				if neighbor_tile.type != 'impassable' and not neighbor_tile.type == 'building':
					return False
		return True

	def create_primary_story_task_for_region(self, acquired_region) -> Optional[Task]:
		# get the first task from the primary story for this region
		story_id = f"{acquired_region.region_name}_primary_story"
		for primary_story in const.PRIMARY_STORIES:
			if primary_story['story_id'] == story_id:
				first_task_seed = primary_story['tasks'][0]
				task = build_task_from_seed(first_task_seed, acquired_region)
				return task

	def initiate_city_story_task_chain(self, region_name: str, child_city) -> Optional[Task]:
		# get the first task from the city story for this region
		if child_city.city_name is None:
			input (f'Error: child city for region {region_name} has no city_name. Cannot initiate city story task chain. {child_city.region_name} {child_city.display_name}')
		story_id = f"{region_name}_{child_city.city_name}_story"
		#input (f'Initiating city story task chain for story id {story_id}')
		for city_story in const.CITY_STORIES:
			#print (f'Checking city story {city_story["story_id"]} against {story_id}')	
			if city_story['story_id'] == story_id:
				first_task_seed = city_story['tasks'][0]
				# find the region with this city
				task = build_task_from_seed(first_task_seed, child_city)
				#input (f'Acquired city story task {task.task_id} for city {child_city.city_name}.')
				return task
		input (f'No city story found for story id {story_id}')

	def get_max_character_level(self) -> int:
		"""Return the highest level among all player characters."""
		max_level = 1
		for char in self.characters:
			if char.level > max_level:
				max_level = char.level
		return max_level

	def get_max_city_loot_level_level(self) -> int:
		num_cities = self.get_city_count()
		return max(num_cities, self.get_max_character_level()) +1

	def get_active_party_average_level (self) -> int:
		"""Return the average level of all player characters."""
		active_chars = self.get_active_party()
		if not active_chars:
			return 1
		total_level = sum(char.level for char in active_chars)
		avg_level = total_level // len(active_chars)
		return max(1, avg_level)

	def ensure_tiles_around(self, check_rad: int =4, max_attempts: int =1) -> bool:
		"""Ensure tiles within `check_rad` around `center` exist.

		Attempts at most `max_attempts` region creations. Returns True if the
		checked area is fully filled after attempts, False otherwise.
		"""
		cx = self.x
		cy = self.y
		attempts =0
		while attempts < max_attempts:
			# find first missing tile
			missing = None
			for dx in range(-check_rad, check_rad +1):
				for dy in range(-check_rad, check_rad +1):
					tx = cx + dx
					ty = cy + dy
					if (tx, ty) not in self.world_tiles:
						missing = (tx, ty)
						break
				if missing:
					break
			if not missing:
				return True

			# if missing need to either create a region at the missing location if there is a large enough area
			# large enough area can be determined with flood fill on nonexistent tiles... min size 1000
			if self.is_empty_area_large_enough_for_region(missing, min_size=1000):			
				self.create_region_at(missing)
				attempts +=1
			else:
				self.floodfill_region_with_open_area(missing)
		# final check
		for dx in range(-check_rad, check_rad +1):
			for dy in range(-check_rad, check_rad +1):
				if (cx + dx, cy + dy) not in self.world_tiles:
					return False
		return True

	def floodfill_region_with_open_area(self, center: Tuple[int,int], fill_tile_type: str = 'open_area') -> None:
		"""Fill a contiguous pocket of missing tiles (starting at `center`) with
		open-area tiles belonging to the PARENT REGION that owns the surrounding
		space.

		Important: the region is resolved from an existing neighbour of the gap,
		and we always fill into the parent region (never a child_city). Writing
		into a child_city here silently expands the city footprint, which then
		makes get_region_and_active_area_for_position() mis-classify neighbouring
		region tiles as city tiles and corrupts rendering after the next move.
		"""
		region = self._resolve_region_for_gap(center)
		if region is None:
			return
		cx, cy = center
		visited = set()
		to_visit = [(cx, cy)]
		while to_visit:
			tx, ty = to_visit.pop()
			if (tx, ty) in visited:
				continue
			visited.add((tx, ty))
			if (tx, ty) in self.world_tiles:
				continue
			# create open area tile in the owning PARENT region
			tile = region.create_open_area_tile(tx, ty)
			self.world_tiles[(tx, ty)] = tile
			# add neighbors to visit
			neighbors = [(tx -1, ty), (tx +1, ty), (tx, ty -1), (tx, ty +1)]
			for n in neighbors:
				if n not in visited:
					to_visit.append(n)

	def _resolve_region_for_gap(self, center: Tuple[int,int]):
		"""Find the parent region that owns the space around a missing tile.

		The gap tile itself is in no region (that's why it's a gap), so we look
		at the four cardinal neighbours that DO exist and return the parent
		region for the first one found. Returns the parent REGION, never a
		child_city.
		"""
		cx, cy = center
		for nx, ny in ((cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)):
			if (nx, ny) in self.world_tiles:
				parent_region, _active = self.get_region_and_active_area_for_position((nx, ny))
				if parent_region is not None:
					return parent_region
		# fall back to the region at the player's position, but still the parent
		parent_region, _active = self.get_region_and_active_area_for_position((self.x, self.y))
		return parent_region

	def is_empty_area_large_enough_for_region(self, center: Tuple[int,int], min_size: int =1000) -> bool:
		"""Check if there is a large enough empty area around `center` to build a new region.
		Uses flood fill to count contiguous empty tiles. Returns True if the count
		reaches `min_size`, False otherwise.
		"""
		cx, cy = center
		visited = set()
		to_visit = [(cx, cy)]
		count =0
		while to_visit:
			tx, ty = to_visit.pop()
			if (tx, ty) in visited:
				continue
			visited.add((tx, ty))
			if (tx, ty) in self.world_tiles:
				continue
			count +=1
			if count >= min_size:
				return True
			# add neighbors to visit
			neighbors = [(tx -1, ty), (tx +1, ty), (tx, ty -1), (tx, ty +1)]
			for n in neighbors:
				if n not in visited:
					to_visit.append(n)
		return False

	def is_alive(self) -> bool:
		"""Return True if any player character is alive."""
		for char in self.get_active_party():
			if char.is_alive():
				return True
		return False

	def get_view_city(self, view_w: int, view_h: int) -> City:
		"""Build a temporary City-like object populated from world_tiles covering
		a rectangular viewport centered at `center` with width `view_w` and height `view_h`.
		This is a UI helper; it does not modify world state.
		"""
		cx, cy = (self.x, self.y)
		half_w = view_w //2
		half_h = view_h //2
		c = City(seed=0)
		for vx in range(cx - half_w, cx + half_w +1):
			for vy in range(cy - half_h, cy + half_h +1):
				t = self.get_tile(vx, vy)
				if t:
					c.tiles[(vx, vy)] = t
		return c

	def get_region_and_active_area_for_position(self, coords: Tuple[int, int] = None):
		"""Return (parent_region, active_city) for the given coordinate.

		If the coordinate is inside a child_city, active_city is that child; if
		it's inside the parent's tiles, active_city is the parent region. If no
		matching region is found, returns (None, None).
		"""
		is_player_loc_check = False
		if not coords:
			is_player_loc_check = True
			coords = (self.x, self.y)
		for region in self.regions:
			if region.child_city and coords in region.child_city.tiles:
				if is_player_loc_check:
					# if not region.child_city.visited:
					# 	input (f'Player is in child city {region.child_city.city_name} of region {region.region_name}')
					region.child_city.visited = True					
				return (region, region.child_city)
			if coords in region.tiles:
				if is_player_loc_check:
					# if not region.visited:
					# 	input (f'Player is in region {region.region_name} at location {coords}')
					region.visited = True
				return (region, region)
		return (None, None)

	def __setstate__(self, state: dict) -> None:
		"""Ensure instances unpickled from older saves get new attributes.

		Pickle restores instance __dict__ directly (doesn't call __init__),
		so new attributes added after a save won't exist on the unpickled
		object. Merge saved state then ensure defaults for any missing keys.
		"""
		# restore saved state
		self.__dict__.update(state or {})

		# defaults for fields added over time (ensure attribute exists)
		defaults = {
			'world_tiles': {},
			'regions': [],
			'previous_region': None,
			'last_region_name': None,
			'characters': [],
			'enemies_slain': {},
			'inventory': [],
			'money': 0,
			'max_inventory_count': 300,
			'x': 0, 'y': 0, 'z': 0,
			'inside': False,
			'save_id': None,
			'current_chapter': 0,
			'active_party': [],
			'max_party_count': 5,
			'tasks': [],
			'dungeons': [],
			'npcs': [],
			'info_dialogs': [],
			'pending_fight_mob_id': None,
			'chapter_task_waiting': False,
			'pending_character': None,
			'twisted_character': None,
			'final_character': None,
			'intro_complete': False,
			'random_encounter_timer': random.randint(5, 15),
			'inside_aircraft': False,
			'phased': False,
			'aircraft_location': None,
			'continents': {},
			'allow_ocean_flight': False,
			'can_aircraft_fly': True,
			'npc_log_locked': True,
			'intro_max_cities': 4,
			'hyperway_unlocked': False,
			'option_dialog': None,
			'completed_regional_quests': [],
			'completed_regional_quests_2': [],
		}

		for k, v in defaults.items():
			if not hasattr(self, k):
				setattr(self, k, v)

	def get_active_dungeon(self) -> Optional["Dungeon"]:
		"""Return the dungeon the player is currently inside, or None.
        Uses dungeon.player_pos as the authoritative presence flag.
        Guards against stale (0,0,0) values written by older saves.
		"""
		for dungeon in self.dungeons:
			pos = getattr(dungeon, "player_pos", None)
			if pos is not None and pos != (0, 0, 0):
				return dungeon
		return None

	def has_monster_hunter_active(self) -> bool:
		"""Return True if any active-party member has an accessory equipped whose
		special_effect is 'monster_hunter'.

		Used by the overworld hostile randomizer: when active, encounters are
		drawn only from region hostiles the player has NOT yet logged (see
		enemies_slain), letting the player track down species they missed at
		lower levels.
		"""
		for char in self.get_active_party():
			for acc in (getattr(char, 'accessories', None) or []):
				if getattr(acc, 'special_effect', '') == 'monster_hunter':
					return True
		return False