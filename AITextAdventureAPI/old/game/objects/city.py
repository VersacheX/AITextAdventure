from typing import Dict, Tuple, Iterator, List, Any, Optional, TYPE_CHECKING
if TYPE_CHECKING:
	from game.objects.player_game import PlayerGame
import random
from dataclasses import dataclass
from typing import Dict, Tuple, Iterator, List, Any, Optional
from game.constants import ROAD, ALLEY, BUILDING#, SUBLOC_MAP, SUBLOCATION_DEFS, BUILDINGS
from services.random_loot_service import generate_loot_for_sublocation
from game import constants as const
#from services.city_service import get_city_parent_region

@dataclass
class Tile:
	x: int
	y: int
	type: str
	# building will hold a dict from BUILDINGS for building tiles, otherwise None
	building: Any = None
	entrances: Tuple[str, ...] = ()
	floors: int =0
	has_basement: bool = False

	def populate_from_json(self, data: dict) -> None:
		"""Populate tile fields from JSON data."""
		self.x = data.get("x", self.x)
		self.y = data.get("y", self.y)
		self.type = data.get("type", self.type)
		self.building = data.get("building", self.building)
		self.entrances = tuple(data.get("entrances", self.entrances))
		self.floors = data.get("floors", self.floors)
		self.has_basement = data.get("has_basement", self.has_basement)

@dataclass
class Sublocation:
	"""Lightweight design for a sublocation instance.

	This class models a single sublocation (an interactable/searchable spot)
	tied to a tile coordinate and a floor. It's intentionally minimal — fields
	are provided for the common attributes we expect the game to use.

	Implementation details and methods can be added later as needed.
	"""
	name: str
	display_name: str
	x: int
	y: int
	z: int =0  #<  WE USE POSITIONAL COORDINATDS TO DENOTE LOCATION AND FOR DISPLAY AND HEIGHT
	mode: str = "searchable" # e.g. 'searchable', 'interactive', 'static'
	prompt: str = None
	loot: Any = None
	money: int =0
	searchable: bool = True
	level_delta: int =0
	metadata: Dict[str, Any] = None

	def populate_from_json(self, data: dict) -> None:
		"""Populate sublocation fields from JSON data."""
		self.name = data.get("name", self.name)
		self.x = data.get("x", self.x)
		self.y = data.get("y", self.y)
		self.z = data.get("z", self.z)
		self.mode = data.get("mode", self.mode)
		self.prompt = data.get("prompt", self.prompt)
		self.loot = data.get("loot", self.loot)
		self.money = data.get("money", self.money)
		self.searchable = data.get("searchable", self.searchable)
		self.level_delta = data.get("level_delta", self.level_delta)
		self.metadata = data.get("metadata", self.metadata)

class City:
	def __init__(self, seed: int, road_spacing: int =6, alley_spacing: int =3, alley_offset: int =2):
		self.seed = seed
		self.region_city_id: int = id(self)
		############################# REGIONAL SETTINSGS #############################		
		self.road_spacing = road_spacing
		self.alley_spacing = alley_spacing
		self.alley_offset = alley_offset
		self.max_size = 200  # defines how large a region can be (created when a player enters within a radius)
		self.population_density = 0.7  # applies controls to development
		self.hasResidence = True # whether residences are generated
		self.hasBusiness = True # whether business buildings are generated
		self.hasShops = True # whether shops are generated
		self.hasBar = True # whether bars are generated
		self.hasInn = True # whether inns are generated
		self.hasHyperway = True # whether hyperway stations are generated
		self.hasOther1 = True # whether other building types are generated
		self.hasOther2 = True # whether other building types are generated
		############################# TILE/SUBLOCATION STORAGE #############################
		self.region_name: str = None
		self.city_name: str = None
		self.display_name: str = "Uknow"
		self.parent_region_city_id: int
		self.parent_region_name: str = None	
		# which continent this region/city belongs to (1-based). Defaults to 1;
		# backfilled for older saves that predate continent association.
		self.continent: int = 1
		self.child_city: City = None # for cities in regions (not used in old game mode)
		self.tiles: Dict[Tuple[int, int], Tile] = {}
		# storage for generated sublocations per tile coordinate+floor
		# keys are (x, y, floor) -> List[Dict]
		self.subloc_map: Dict[Tuple[int, int, int], List[Dict]] = {}
		self.visited: bool = False # whether player has visited this city/region before (used to control generation and descriptions)
		self.description: str = "No description provided."

	def get_center_position(self) -> Tuple[int, int]:
		"""Return the center position (x,y) of the city based on current tiles."""
		if not self.tiles:
			return (0, 0)
		min_x = min(t.x for t in self.tiles.values())
		max_x = max(t.x for t in self.tiles.values())
		min_y = min(t.y for t in self.tiles.values())
		max_y = max(t.y for t in self.tiles.values())
		center_x = (min_x + max_x) //2
		center_y = (min_y + max_y) //2
		return (center_x, center_y)

	def is_safe_area(self, pg: 'PlayerGame') -> bool:
		"""Return True if the player's current tile is considered a safe area.

		This inspects the city's `tiles` mapping at `(pg.x, pg.y)` and returns True
		when the tile is a building whose type/name is one of: 'residence', 'business', 'inn', 'shop'.

		Per your request this method expects a `PlayerGame` instance and does not
		provide fallbacks; if the tile is not present it will raise a KeyError.
		"""
		# access player's coordinates (assume pg is valid PlayerGame as requested)
		x = pg.x
		y = pg.y
		# directly index into tiles (no fallbacks)
		tile = self.tiles[(x, y)]
		# must be a building to be a safe area
		if tile.type != BUILDING:
			return False
		b = tile.building
		# building may be a dict or a string; prefer dict fields
		btype = None
		if isinstance(b, dict):
			btype = b.get('type')
		if not btype:
			return False
		btype = str(btype).lower()
		return btype in {'residence', 'business', 'inn', 'shop', 'other1', 'other2'}

	def _opposite_dir(self, name: str) -> str:
		return {
			'north': 'south',
			'south': 'north',
			'west': 'east',
			'east': 'west'
		}.get(name, name)

	##### PLAYER INTERACTION METHODS #####
	def get_sublocation_at_location_with_loot_by_name(
		self, x: int, y: int, z: int, name: str
	) -> Optional[Dict]:
		"""Return the sublocation dict with the given name at (x,y,z) that has loot or money, or None."""
		sublocs = self.subloc_map.get((x, y, z))
		if not sublocs:
			return None

		return next(
			(s for s in sublocs
				 if s.get("name") == name and (s.get("loot") is not None or s.get("money") is not None)),
			None
		)

	# from game.objects.player import Player
	def loot_sublocation(self, player_game, location_name) -> List[Dict]:
		"""find sublocation in self.subloc_map and add to player inventory then remove from subloc_map.
		Use `x`, `y`, and `floor` along with name, use those instead of player's current position/floor.

		self.subloc_map: Dict[Tuple[int, int, int], List[Dict]] = {}
		find the sublocation dict in the list matching s_location['name']
		if inventory not full, add item to inventory and set s_location['loot'] = None
		if money >0, add to player money and set s_location['money'] =0
		return final prompt string summarizing results
		"""
		# Precise implementation: expect s_location to contain 'x','y','z' and 'name'
		# self.subloc_map = out where : out.append({"name": name, "mode": defn.get("mode"), "prompt": defn.get("prompt"), "loot": generated_loot, "money": money})
		#we need to find the subloc at key with name
		dictionary_item = self.get_sublocation_at_location_with_loot_by_name(player_game.x, player_game.y, player_game.z, location_name)
		
		x= player_game.x
		y= player_game.y
		z= player_game.z
		final_prompt = ''

		# if the dictionary_items returns any results we loot out the first one in the list
		if not dictionary_item:
			final_prompt += 'There is nothing to loot here.'
			return final_prompt

		name = dictionary_item.get('name')

		# require explicit coordinates and name to operate
		if x is None or y is None or z is None or location_name is None:
			# be strict: caller must supply exact x,y,floor and name
			#print(f'loot_sublocation: invalid s_location: {location_name}')
			return final_prompt

		key = (x, y, z)
		sl_list = self.subloc_map.get(key, [])
		# find the matching sublocation dict by name
		target = None
		if name:
			for s in sl_list:				
				if isinstance(s, dict) and s.get('name') == name:
					target = s
					break
				
		# nothing to loot
		if target is None:
			return final_prompt

		item = target.get('loot')
		money = int(target.get('money',0) or 0)

		if item:
			# strict behavior: use player's inventory and capacity
			if not player_game.pick_up_item(item):
				final_prompt += 'Your inventory is full. '
			else:
				target['loot'] = None
				final_prompt += f"You pick up the {item.name}. "

		if money and money >0:
			player_game.add_money(money)
			target['money'] =0
			final_prompt += f"You pick up {money} money."

		return final_prompt.strip()

	def find_coords_of_random_tile_of_type(self, player_game, tile_type: str) -> Optional[Tuple[int, int]]:
		# gather all tiles of the given type
		coords = None
		candidates = []
		if tile_type in {ROAD, ALLEY, 'open_area'}:
			for (tx, ty), tile in self.tiles.items():
				if tile.type == tile_type:
					candidates.append((tx, ty))
			rng = random.Random(self.seed)
			if candidates:
				coords = rng.choice(candidates)  # use rng instead of random.choice
		else:
			return self.find_coords_of_random_building_of_type(player_game, tile_type) 

		return coords

	def find_coords_of_random_building_of_type(self, player_game, building_type: str) -> Optional[Tuple[int, int]]:
		# gather all building tiles of the given type
		coords = None
		candidates = []
		for (tx, ty), tile in self.tiles.items():
			if tile.type != BUILDING:
				continue
			b = tile.building
			bname = None
			if isinstance(b, dict):
				bname = b.get('name')
			elif isinstance(b, str):
				bname = b
			if bname == building_type:
				candidates.append((tx, ty))

		rng = random.Random(self.seed)
		if candidates:
			coords = rng.choice(candidates)  # use rng instead of random.choice

		return coords

	def find_random_dungeon_position(self, dungeon, player_game) -> Optional[Tuple[int, int]]:
		# gather all passable tiles in the dungeon
		coords = None
		candidates = []
		for (tx, ty), tile in self.tiles.items():
			#input (f'tile: {tile.type}')
			if tile.type == 'open_area' and not player_game.get_dungeon_at_position((tx, ty)):
				candidates.append((tx, ty))

		#print (f'cand count: {len(candidates)}')
		#for each candidate ensure there an unobstructed path to any road or alley tile in the city.. this will create our acceptable positions
		semi_final_candidates = []
		for (tx, ty) in candidates:
			if self.find_path_to_road_or_alley((tx, ty)):
				semi_final_candidates.append((tx, ty))

		#print (f'semi final cand count: {len(semi_final_candidates)}')
		final_candidates = []
		for (tx, ty) in semi_final_candidates:
			# check player game to ensure tile is not surrounded by buildings or impassable tiles
			if not player_game.is_location_surrounded_by_impassable_or_buildings((tx, ty)):
				final_candidates.append((tx, ty))
		
		#print (f'final cand count: {len(final_candidates)}')
		if final_candidates:
			rng = random.Random(self.seed)
			coords = rng.choice(final_candidates)
		
		#input (f'coords: {coords}')
		return coords

	def find_path_to_road_or_alley(self, start_pos: Tuple[int,int]) -> bool: # ensure cannot walk through imppassable tile
		# simple breadth-first search to find a path to any road or alley tile
		# MUST NOT  WALK THROUGH ... t.type == 'impassable':
		visited = set()
		queue = [start_pos]
		while queue:
			current = queue.pop(0)
			if current in visited:
				continue
			visited.add(current)
			tile = self.get_tile(current[0], current[1])
			if tile is None:
				continue
			if tile.type == ROAD or tile.type == ALLEY:
				return True  # found a path to road or alley
			# add neighbors to queue
			for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
				neighbor = (current[0] + dx, current[1] + dy)
				ntile = self.get_tile(neighbor[0], neighbor[1])
				if ntile and ntile.type != 'impassable' and neighbor not in visited:
					queue.append(neighbor)

	def find_nearest_building_of_type(self, player_game, building_type: str, pos: Tuple[int,int,int] = None) -> Optional[Tuple[int, int]]:
		if not pos:
			pos = (player_game.x, player_game.y, player_game.z)

		# look at city_tiles with building def where building_def['name'] == building_type
		# use pythagorean theorem to find nearest building by calculating distance
		min_dist = None
		nearest_coords = None
		for (tx, ty), tile in self.tiles.items():
			if tile.type != BUILDING:
				continue
			b = tile.building
			bname = None
			if isinstance(b, dict):
				bname = b.get('name')
			elif isinstance(b, str):
				bname = b
			if bname != building_type:
				continue
			# calculate distance
			dx = tx - pos[0]
			dy = ty - pos[1]
			dist = (dx * dx) + (dy * dy)  # squared distance is sufficient for comparison
			if min_dist is None or dist < min_dist:
				min_dist = dist
				nearest_coords = (tx, ty)

		return nearest_coords

	##### CITY/REGION ACCESSORS #####

	def get_parent_region_name (self, player_game) -> str:
		"""Return the region name for this city (region_name if city is a region, else parent region_name)."""
		# if not self.isRegion():
		# 	parent = self.get_parent(player_game)
		# 	if parent:
		# 		return parent.region_name
		return self.parent_region_name
	
	def isCity(self) -> bool:
		"""Return True if this city is a city (has a parent_region)."""
		return self.city_name is not None

	def isRegion(self) -> bool:
		"""Return True if this city is a region (has a child_city)."""
		return self.parent_region_name is None

	def get_parent(self, player_game):
		from services.city_service import get_city_parent_region
		"""
		Return the parent region city for this city in the given player_game.
		Return none if this is not a City
		"""
		return get_city_parent_region(self, player_game)

	##### TILE ACCESSORS, LOCATIONAL INFORMATION #####

	def get_sublocation_at(self, coords: Tuple[int, int, int]) -> List[Dict]:
		return self.subloc_map.get(coords, [])

	def get_tile(self, x: int, y: int):
		"""Return existing Tile at (x,y) or None. Does NOT create a new tile.
		Use this when you want to inspect a tile without causing generation side-effects.
		"""
		return self.tiles.get((x, y))

	def _can_travel_from_player_location(self, player_game) -> bool:
		"""
		very simple check to see if the players_game postiion is standing on a tile with a building that has a type of hyperway
		"""
		tile = self.get_tile(player_game.x, player_game.y)
		if tile is None:
			return False
		if tile.type != BUILDING:
			return False
		b = tile.building
		if b.get('type') == 'hyperway':
			return True


	def _is_location_shop_first_floor(self, player_game):
		"""Return (can_shop, building_def) for the player's current location.

		Rules used:
		- Location must be a building tile with a building definition.
		- The building must have `can_buy` truthy in its definition.
		- If the player is inside, they must be on the main floor (1) to access the shop.
		- If the player is outside (not inside), they may access the shop only if the building
		 has visible entrances (so the player is standing at the facade).
	
		This function is intentionally conservative and returns (False, None) when the
		building definition cannot be resolved.
		"""	
		region_name = self.city_name if not self.isRegion() else self.region_name
		parent_region_name = self.get_parent_region_name(player_game)
		if len(player_game.regions) == 0:  parent_region_name = self.parent_region_name
		if not parent_region_name:
			attr = f"{region_name.upper()}_BUILDINGS"
		else:
			attr = f"{parent_region_name.upper()}_{self.city_name.upper()}_BUILDINGS"
		buildings = getattr(const, attr)

		# Get the tile without creating side-effects
		tile = self.get_tile(player_game.x, player_game.y)
		if tile is None:
			return False, None
		if tile.type != BUILDING:
			return False, None
		# resolve building definition dict
		bdef = None
		b = tile.building
		if isinstance(b, dict):
			bdef = b
		elif isinstance(b, str):
			# find matching entry in BUILDINGS by name
			for bd in buildings:
				if bd.get('name') == b:
					bdef = bd
					break
		else:
			# unknown building representation
			return False, None
		if bdef is None:
			return False, None
		if not bdef.get('can_buy', False):
			return False, None
		# check accessibility: inside -> must be main floor; outside -> must have entrances visible
		if player_game.inside:
			if player_game.z == 0:
				return True, bdef
			return False, None
		# outside player
		if tile.entrances and len(tile.entrances) >0:
			return True, bdef
		return False, None

	def get_entrances_for_building(self, x: int, y: int) -> List[str]:
		t = self.get_tile(x, y)
		if t.type != BUILDING:
			return []
		return list(t.entrances)
	
	##### UI METHODS #####

	def _tile_char(self, tile: Tile) -> str:
		if tile.type == ROAD:
			return ' '
		if tile.type == ALLEY:
			return '"'
		if tile.type == BUILDING:
			return tile.building["char"]# self._building_char(tile.building)
		return ' '

	def describe_location(self, x: int, y: int, inside: bool = False, floor: int =0) -> str: # floor is z + 1
		t = self.get_tile(x, y)
		if inside and t.type == BUILDING:
			fb = f" (floor {floor}" + (", basement" if floor <=0 and t.has_basement else "") + ")"
			return f"You are inside the {t.building['display_name']}{fb}."
		if t.type == BUILDING:
			entrances = self.get_entrances_for_building(x, y)
			if entrances:
				return f"You are at a {t.building['display_name']}. Entrances: {', '.join(entrances)}."
			else:
				return f"You are at a {t.building['display_name']}. No visible entrances from the street."
		if t.type == ROAD:
			is_road, rv, rh = self._is_road_pos(x, y)
			if rv and rh:
				return "You are at a road intersection."
			return "You are on a road."
		if t.type == ALLEY:
			return "You are in an alley."
		return "You are in an open area."
















	########### CITY/REGION BUILDER METHODS ###########	

	def _is_road_pos(self, x: int, y: int) -> Tuple[bool, bool, bool]:
		# returns (is_road, is_vertical, is_horizontal)
		is_v = (x % self.road_spacing ==0)
		is_h = (y % self.road_spacing ==0)
		return (is_v or is_h, is_v, is_h)

	def _is_alley_pos(self, x: int, y: int) -> Tuple[bool, bool, bool]:
		# normalized alley detection with consistent tabs
		is_alley_v = ((x + self.alley_offset) % self.alley_spacing ==0)
		is_alley_h = ((y + self.alley_offset) % self.alley_spacing ==0)
		is_v = is_alley_v
		is_h = is_alley_h
		if not (is_v or is_h):
			return (False, False, False)
		# avoid alleys that are directly adjacent-parallel to roads
		if is_v:
			if ((x +1) % self.road_spacing ==0) or ((x -1) % self.road_spacing ==0):
				is_v = False
		if is_h:
			if ((y +1) % self.road_spacing ==0) or ((y -1) % self.road_spacing ==0):
				is_h = False
		if not (is_v or is_h):
			return (False, False, False)
		# adjacency to a road on any side qualifies
		for dx, dy in ((1,0), (-1,0), (0,1), (0, -1)):
			nx, ny = x + dx, y + dy
			r_is_road, _, _ = self._is_road_pos(nx, ny)
			if r_is_road:
				return (True, is_v, is_h)
		# continuity checks along the alley orientation
		if is_v:
			for dy in (-1,1):
				nx, ny = x, y + dy
				n_is_alley_v = ((nx + self.alley_offset) % self.alley_spacing ==0)
				n_is_alley_h = ((ny + self.alley_offset) % self.alley_spacing ==0)
				n_is_v = n_is_alley_v and not n_is_alley_h
				if n_is_v and not (((nx +1) % self.road_spacing ==0) or ((nx -1) % self.road_spacing ==0)):
					return (True, is_v, is_h)
			for dy in (-2,2):
				nx, ny = x, y + dy
				n_is_alley_v = ((nx + self.alley_offset) % self.alley_spacing ==0)
				n_is_alley_h = ((ny + self.alley_offset) % self.alley_spacing ==0)
				n_is_v = n_is_alley_v and not n_is_alley_h
				if n_is_v:
					midx, midy = x, y + (dy //2)
					if not (((midx +1) % self.road_spacing ==0) or ((midx -1) % self.road_spacing ==0)):
						return (True, is_v, is_h)
		if is_h:
			for dx in (-1,1):
				nx, ny = x + dx, y
				n_is_alley_v = ((nx + self.alley_offset) % self.alley_spacing ==0)
				n_is_alley_h = ((ny + self.alley_offset) % self.alley_spacing ==0)
				n_is_h = n_is_alley_h and not n_is_alley_v
				if n_is_h and not (((ny +1) % self.road_spacing ==0) or ((ny -1) % self.road_spacing ==0)):
					return (True, is_v, is_h)
			for dx in (-2,2):
				nx, ny = x + dx, y
				n_is_alley_v = ((nx + self.alley_offset) % self.alley_spacing ==0)
				n_is_alley_h = ((ny + self.alley_offset) % self.alley_spacing ==0)
				n_is_h = n_is_alley_h and not n_is_alley_v
				if n_is_h:
					midx, midy = x + (dx //2), y
					if not (((midy +1) % self.road_spacing ==0) or ((midy -1) % self.road_spacing ==0)):
						return (True, is_v, is_h)
		return (False, False, False)

	def _adjacent_roads(self, x: int, y: int) -> List[Tuple[int, int, str]]:
		res = []
		checks = [((0, -1), 'north'), ((0,1), 'south'), ((-1,0), 'west'), ((1,0), 'east')]
		for (dx, dy), name in checks:
			nx, ny = x + dx, y + dy
			is_road, road_v, road_h = self._is_road_pos(nx, ny)
			if is_road:
				res.append((nx, ny, name))
		return res

	def _adjacent_alleys(self, x: int, y: int) -> List[Tuple[int, int, str]]:
		res = []
		checks = [((0, -1), 'north'), ((0,1), 'south'), ((-1,0), 'west'), ((1,0), 'east')]
		for (dx, dy), name in checks:
			nx, ny = x + dx, y + dy
			is_alley, av, ah = self._is_alley_pos(nx, ny)
			if is_alley:
				res.append((nx, ny, name))
		return res

	def find_similar_tile_in_range(self, x: int, y: int, building_def: any):
		# search nearby tiles for similar building to enforce spacing rules
		# use building_def['name'], building_def['seed_range']
		name = building_def['name']
		seed_range = building_def['seed_range']
		# use region map to find existing buildings with the same name within seed_range in this method using self.tiles
		for dy in range(-seed_range, seed_range +1):
			for dx in range(-seed_range, seed_range +1):
				nx, ny = x + dx, y + dy
				tile = self.tiles.get((nx, ny))
				if tile and tile.type == BUILDING:
					bld = tile.building
					if isinstance(bld, dict) and bld.get('name') == name:
						return tile
					
		return None


	#################################  CREATE A TILE (street/building/openarea/impassable)#######################
	# from game.objects.player import Player
	def create_tile(self, player_game, x = None, y = None):
		"""
		Create a tile and add buildings, roads, and alleys.
		Decoupled from ensure_sublocations_for_tile to allow subs to be populated after region is fully built.
		"""
		x = x if x is not None else player_game.x
		y = y if y is not None else player_game.y

		key = (x, y, 0)

		# use non-creating accessor so we don't generate tiles as a side-effect
		t = self.get_or_create_tile(x, y, player_game)
		
	def get_or_create_tile(self, x: int, y: int, player_game) -> Tile:
		key = (x, y)
		if key in self.tiles:
			return self.tiles[key]
		t = self._generate_tile(x, y, player_game)
		self.tiles[key] = t
		return t

	def _generate_tile(self, x: int, y: int, player_game) -> Tile:
		# roads
		is_road, road_v, road_h = self._is_road_pos(x, y)
		if is_road:
			return Tile(x, y, ROAD)
		# alleys
		is_alley, alley_v, alley_h = self._is_alley_pos(x, y)
		if is_alley:
			return Tile(x, y, ALLEY)

		# create buildings on any non-road/non-alley tile... 
		# only if they are alley or road adjacent
		adj_roads = self._adjacent_roads(x, y)
		adj_alleys = self._adjacent_alleys(x, y)
				
		building_type, entrances, floors, has_basement = self._create_building(x, y, adj_roads, adj_alleys, player_game) if (adj_roads or adj_alleys) else (None, [],0, False)
		# if _create_building returned None for building_type treat this as open space
		if building_type is None:
			region_name = self.city_name if not self.isRegion() else self.region_name
			attr = f"{region_name.upper()}_IMPASSABLE_CHANCE"
			impassable_chance = getattr(const, attr, 0.0)
			h = self.seed
			h = (h *397) ^ x
			h = (h *397) ^ y
			rnd = random.Random(h)
			if impassable_chance > 0.0 and rnd.random() < impassable_chance:
				return Tile(x, y, 'impassable')

			return Tile(x, y, 'open_area')

		valid_entrances = []
		for name in entrances:
			if any(r[2] == name for r in adj_roads) or any(a[2] == name for a in adj_alleys):
				valid_entrances.append(name)
		
		return Tile(x, y, BUILDING, building_type, tuple(valid_entrances), floors, has_basement)

	def _create_building(self, x: int, y: int, adj_roads: List[Tuple[int, int, str]], adj_alleys: List[Tuple[int, int, str]], player_game):
		# deterministic selection based on position+seed
		# include an attempt counter in the hash so repeated iterations produce a different
		# deterministic random sequence; this prevents the loop from repeatedly
		# selecting the same building definition when a nearby similar building forces a retry.
		attempt =0
		
		region_name = self.city_name if not self.isRegion() else self.region_name

		# print(f"info about player game: {player_game}")
		# input("PAUSE")
		parent_region_name = self.get_parent_region_name(player_game)
		if len(player_game.regions) == 0:  parent_region_name = self.parent_region_name
		if not parent_region_name:
			attr = f"{region_name.upper()}_BUILDINGS"
		else:
			attr = f"{parent_region_name.upper()}_{self.city_name.upper()}_BUILDINGS"
		buildings = getattr(const, attr)

		# filter buildings to only allow type= residence or business... then select building from those 4 at random
		allowed_buildings  = []
		for b in buildings:
			btype = b.get('type')
			if (btype == 'residence' and self.hasResidence) or (btype == 'business' and self.hasBusiness):
				allowed_buildings.append(b)

		if len(allowed_buildings) ==0:
			return None, [],0, False

		#for allowed building types  determine which ones are within the threshold of the seed_range
		final_buildings = []
		for b in allowed_buildings:
			seed_range = b.get('seed_range', 0)
			# calculate distance from (x,y) to nearest existing building of this type
			nearby_building = self.find_similar_tile_in_range(x, y, b)
			if nearby_building is None:
				final_buildings.append(b)

		if len(final_buildings) ==0:
			return None, [],0, False

		h = self.seed
		h = (h *397) ^ x
		h = (h *397) ^ y
		h = (h *397) ^ attempt
		rnd = random.Random(h)

		building_def = rnd.choice(final_buildings)
		building_key = building_def.get('name')
		# max_attempts = 10
		# while True:
		# 	h = self.seed
		# 	h = (h *397) ^ x
		# 	h = (h *397) ^ y
		# 	h = (h *397) ^ attempt
		# 	rnd = random.Random(h)
		# 	v = rnd.random()

		# 	# previous distribution thresholds
		# 	# safe selection: if no threshold matches, fall back to last building
		# 	idx = next((i for i, t in enumerate(buildings) if v < t.get('threshold',1.0)), None)
		# 	if idx is None:
		# 		idx = len(buildings) -1
		# 	building_def = buildings[idx] if idx < len(buildings) else buildings[-1]
		# 	# determine normalized category (residence/business/shop/bar/inn/etc)
		# 	bname = building_def.get('name', '')
		# 	category = _normalize_building_name(bname)
		# 	# if this category is disabled in the city settings, treat as no building
		# 	if (category == 'residence' and not getattr(self, 'hasResidence', True)) or \
		# 		(category == 'business' and not getattr(self, 'hasBusiness', True)) or \
		# 		(category == 'shop' and not getattr(self, 'hasShops', True)) or \
		# 		(category == 'bar' and not getattr(self, 'hasBar', True)) or \
		# 		(category == 'inn' and not getattr(self, 'hasInn', True)):
		# 		# return None to indicate open tile
		# 		return None, [],0, False
		# 	building_key = building_def.get('name')
		# 	building = self.find_similar_tile_in_range(x, y, building_def)
		# 	# if no similar building is nearby we're done; otherwise retry with a new attempt
		# 	if building is None:
		# 		break
		# 	attempt +=1

		# 	if attempt >max_attempts:
		# 		# give up after 10 attempts to avoid infinite loops
		# 		return None, [],0, False

		# floors: small building types are single-floor
		if building_key in ('residencesmall', 'businesssmall'):
			floors =1
		else:
			floors = max(1,  int(sum(rnd.randint(1,4) for r in range(3)) * self.population_density))

		entrances: List[str] = []
		if adj_roads:
			if len(adj_roads) ==1:
				street_dir = adj_roads[0][2]
			else:
				street_idx = rnd.randrange(len(adj_roads))
				street_dir = adj_roads[street_idx][2]
			entrances.append(street_dir)
		for _, _, name in adj_alleys:
			if name not in entrances:
				entrances.append(name)

		has_basement = rnd.random() <0.25
		# return building definition dict so callers can access ['name'] and ['char']
		return building_def, entrances, floors, has_basement	

	def create_open_area_tile(self, x: int, y: int):
		# force creation of an open area tile at (x,y)
		key = (x, y)
		t = Tile(x, y, 'open_area')
		self.tiles[key] = t
		return t

	#################################   POPULATE TILES IN CITY/REGION WITH SUBLOCATIONS AND LOOT #######################
	# from game.objects.player import Player
	def populate_tiles(self, player_game):
		# populates sublocations for all tiles in the city after creation
		for (x, y), t in self.tiles.items():
			self.populate_tile(player_game, t, x, y)

		pass	

	# from game.objects.player import Player
	def populate_tile(self, player_game, t: Tile, x: int, y: int):
		# when querying sublocations for an interior floor we still inspect the tile type to
		# decide which subtype to use (buildings get building subtypes, streets/alley otherwise)
		if t.type == 'building':
			# t.building may be a dict (new) or a legacy string; extract name accordingly
			b = t.building
			if isinstance(b, dict):
				bname = b.get('name', '')
			else:
				bname = b
			subtype = _normalize_building_name(bname)
		elif t.type == 'road':
			subtype = 'street'
		elif t.type == 'alley':
			subtype = 'alley'
		else:
			subtype = t.type
				
		# print(f"info about player game: {player_game}")
		# input("PAUSE")
		parent_region_name = self.get_parent_region_name(player_game)
		if len(player_game.regions) == 0:  parent_region_name = self.parent_region_name
		region_name = self.city_name if not self.isRegion() else self.region_name

		subloc_maps, subloc_defs = self.get_tile_subloc_defs(region_name, parent_region_name)

		self.add_available_sublocations_to_tile(player_game, x, y, t, subtype, subloc_maps, subloc_defs)

	def get_tile_subloc_defs(self, region_name, parent_region_name):
		
		if not parent_region_name:
			attr = f"{region_name.upper()}_SUBLOC_MAP"
		else:
			attr = f"{parent_region_name.upper()}_{self.city_name.upper()}_SUBLOC_MAP"  # Updated to use get_parent_region_name()
		subloc_maps = getattr(const, attr)
		
		if not parent_region_name:
			attr = f"{region_name.upper()}_SUBLOCATION_DEFS"
		else:
			attr = f"{parent_region_name.upper()}_{self.city_name.upper()}_SUBLOCATION_DEFS"  # Updated to use get_parent_region_name()
		subloc_defs = getattr(const, attr)

		return subloc_maps, subloc_defs

	def add_available_sublocations_to_tile(self, player_game,x, y, t, subtype, subloc_maps, subloc_defs):
		key = (x, y, 0)
		available = subloc_maps.get(subtype, []) if subtype else []
		# include provided floor in deterministic seed so different floors yield different sublocations
		rnd = random.Random((self.seed &0xFFFFFFFF) ^ (x <<16) ^ (y &0xFFFF))
		out: List[Dict] = []
		if available:
			bottom_floor = -1 if t.has_basement else 0
			for z in range(bottom_floor, max(1, t.floors)):
				key = (x, y, z)
				out: List[Dict] = []
				k = rnd.randint(0, min(2, len(available)))
				picked = rnd.sample(available, k=k)
				for name in picked:
					defn = subloc_defs.get(name)
					if defn is None:
						defn = {"mode": "searchable", "level_delta":0, "searchable": False, "loot_chance":0.0, "prompt": None}
					# setup loot for searchable sublocations using random_loot_service
					generated_loot = None
					money =0
					if defn.get("mode") == "searchable":
						loot_chance = defn.get('loot_chance',0.0)
						# Seed using floor to ensure different floors yield different sublocations/loot
						rnd.seed((self.seed &0xFFFFFFFF) ^ (x <<16) ^ (y &0xFFFF) ^ (z &0xFFFF) ^ hash(name))
						rng = rnd.random()
						found = rng < loot_chance
						if found:
							# GET AVG PLAYER LEVEL FROM player_game.characters.level
							max_level = player_game.get_max_city_loot_level_level()
							generated_loot = generate_loot_for_sublocation(defn, max_level)
						rnd.seed((self.seed &0xFFFFFFFF) ^ (x <<16) ^ (y &0xFFFF) ^ (z &0xFFFF) ^ hash(rng))
						rng_money = rnd.random()
						found_money = rng_money < loot_chance
						if found_money:
							min_money, max_money = defn.get('money_range', (0,0))
							rnd.seed((self.seed &0xFFFFFFFF) ^ (x <<16) ^ (y &0xFFFF) ^ (z &0xFFFF) ^ hash(rng_money))
							money = rnd.randint(min_money, max_money)

					out.append({"name": name, "mode": defn.get("mode"), "prompt": defn.get("prompt"), "loot": generated_loot, "money": money})

					#out.append({"name": name, "mode": defn.get("mode"), "prompt": defn.get("prompt"), "loot_chance": defn.get('loot_chance',0.0)})
				self.subloc_map[key] = out
		else:
			self.subloc_map[key] = out

	############### JSON METHODS ###############
	def populate_from_json(self, data: dict) -> None:
		self.city_name = data.get('city_name', 'UnknownCity')
		self.region_name = data.get('region_name', None)
		self.parent_region_name = data.get('parent_region_name', None)
		self.continent = data.get('continent', 1)
		self.seed = data.get('seed', 0)
		self.population_density = data.get('population_density', 1.0)
		self.road_spacing = data.get('road_spacing', 5)
		self.alley_spacing = data.get('alley_spacing', 3)
		self.alley_offset = data.get('alley_offset', 1)
		self.hasResidence = data.get('hasResidence', True)
		self.hasBusiness = data.get('hasBusiness', True)
		self.hasShops = data.get('hasShops', True)
		self.hasBar = data.get('hasBar', True)
		self.hasInn = data.get('hasInn', True)
		self.visited = bool(data.get('visited', False))
		# Load tiles
		tiles_data = data.get('tiles', {})
		for key_str, tile_data in tiles_data.items():
			x_str, y_str = key_str.split(',')
			x, y = int(x_str), int(y_str)
			tile = Tile(x, y, tile_data['type'])
			tile.building = tile_data.get('building')
			tile.entrances = tuple(tile_data.get('entrances', ()))
			tile.floors = tile_data.get('floors', 0)
			tile.has_basement = tile_data.get('has_basement', False)
			self.tiles[(x, y)] = tile
		# Load sublocation map
		subloc_map_data = data.get('subloc_map', {})
		for key_str, sublocs in subloc_map_data.items():
			x_str, y_str, z_str = key_str.split(',')
			x, y, z = int(x_str), int(y_str), int(z_str)
			self.subloc_map[(x, y, z)] = sublocs

	def ensure_required_buildings(self, player_game, locations: List[Tuple[int,int]]) -> None:
		"""Ensure the city contains at least one instance of each building defined for this city/region.

		this is simply a pre placement mechanism placing one of each required building on the map next to a road or alley...

		when this method is called nothing has been placed yet.
		no entrances are built here... no subdefs are created... just the building tiles...

	

		THIS IS HOW IT'S DONE NORMALLY... WE NEED TO CREATE EACH TILE AND THEN CREATE THE SPECIFIC BUILDINGS TO 
		ENSURE ONE OF EACH REQUIRED BUILDING BEFORE MASS TILE GENERATION

		"""
		# determine attribute name for buildings list (same logic as _create_building)
		parent_region_name = self.get_parent_region_name(player_game)
		if len(player_game.regions) ==0:
			parent_region_name = self.parent_region_name
		if not parent_region_name:
			attr = f"{self.region_name.upper()}_BUILDINGS"
		else:
			attr = f"{parent_region_name.upper()}_{self.city_name.upper()}_BUILDINGS"
		buildings = getattr(const, attr, [])

		# helper: allowed categories per city flags
		def _category_allowed(bdef: dict) -> bool:
			category = _normalize_building_name(bdef.get('name', ''))
			if (category == 'residence' and not getattr(self, 'hasResidence', True)):
				return False
			if (category == 'business' and not getattr(self, 'hasBusiness', True)):
				return False
			if (category == 'shop' and not getattr(self, 'hasShops', True)):
				return False
			if (category == 'bar' and not getattr(self, 'hasBar', True)):
				return False
			if (category == 'inn' and not getattr(self, 'hasInn', True)):
				return False
			if (category == 'hyperway' and not getattr(self, 'hasHyperway', True)):
				return False
			if (category == 'other1' and not getattr(self, 'hasOther1', True)):
				return False
			if (category == 'other2' and not getattr(self, 'hasOther2', True)):
				return False
			return True

		# collect existing building names
		existing = set()

		# For each building def ensure at least one exists
		for bdef in buildings:
			#print (f'bdef: {bdef}')
			bname = bdef.get('name')
			if not bname or bname in existing:
				continue
			# skip if category disabled
			if not _category_allowed(bdef):
				continue

			# find candidate tile: prefer tiles adjacent to road/alley and not already a building
			candidates = []
			for (tx, ty) in locations:
				if self._is_road_pos(tx, ty)[0] or self._is_alley_pos(tx,ty)[0]:
					continue
				# prefer tiles that are adjacent to road or alley so building looks natural
				adj_roads = self._adjacent_roads(tx, ty)
				adj_alleys = self._adjacent_alleys(tx, ty)
				if not adj_roads and not adj_alleys:
					continue
				# ensure spacing: find_similar_tile_in_range returns existing similar building
				if (tx,ty) not in self.tiles.keys():
					if self.find_similar_tile_in_range(tx, ty, bdef) is None:
						candidates.append((tx, ty, adj_roads, adj_alleys))
						break

			rng = random.Random((self.seed &0xFFFFFFFF))
			candidate = None
			if candidates:
				candidate = rng.choice(candidates)
			if candidate is None:
				continue

			tx, ty, adj_roads, adj_alleys = candidate

			# determine floors: mimic small building single-floor rule
			if bname in ('residencesmall', 'businesssmall'):
				floors =1
			else:
				floors =1
			
			entrances: List[str] = []
			if adj_roads:
				if len(adj_roads) ==1:
					street_dir = adj_roads[0][2]
				else:
					street_idx = random.randrange(len(adj_roads))
					street_dir = adj_roads[street_idx][2]
				entrances.append(street_dir)
			for _, _, name in adj_alleys:
				if name not in entrances:
					entrances.append(name)

			# place building by replacing/creating the tile
			self.tiles[(tx, ty)] = Tile(tx, ty, BUILDING, bdef, tuple(entrances), floors, False)
			existing.add(bname)
			# continue to next building
		# end for

def _normalize_building_name(name: str) -> str:
	n = name.lower()
	if n.startswith('shop'):
		return 'shop'
	if 'inn' in n:
		return 'inn'
	if 'bar' in n:
		return 'bar'
	if 'residence' in n:
		return 'residence'
	if 'business' in n:
		return 'business'
	if 'hyperway' in n:
		return 'hyperway'
	if 'other1' in n:
		return 'other1'
	if 'other2' in n:
		return 'other2'
	return n
