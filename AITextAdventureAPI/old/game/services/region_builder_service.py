"""Helper wrappers to keep build_region_around concise.

This module exposes small, well-named helpers used by the top-level
`build_region_around` so the orchestration reads like a sequence of steps.
The heavier logic remains in the dedicated frontier/shape services.
"""
from typing import Tuple, Set, Iterable, Callable
import random
import math
import logging
from collections import deque

from game.objects.city import City
from game.objects.player import Player


def ensure_4_connected(tiles: Set[Tuple[int, int]], ignored_set: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
	"""Bridge gaps so `tiles` form a single 4-connected mass.

	Region growth uses 8-directional neighbours, so a footprint can be joined only
	diagonally (e.g. tiles at (0,0) and (1,1) with (1,0)/(0,1) empty). The player,
	however, moves orthogonally (w/s/a/d), and continent contiguity is validated
	with 4-connectivity. A footprint that is merely 8-connected therefore reads as
	several disjoint blobs and can never verify contiguous.

	This repeatedly finds the 4-connected components of the footprint and carves a
	shortest orthogonal bridge from one component to another using a BFS that
	treats cells already claimed by another region (``ignored_set``) as walls, so a
	bridge NEVER crosses occupied cells (which would create overlapping region
	ownership). Only free cells are added. If two components cannot be joined
	without crossing occupied cells, they are left as-is rather than corrupting the
	map. Newly added tiles are returned folded into the input set.
	"""
	if not tiles:
		return tiles
	added: Set[Tuple[int, int]] = set()
	working = set(tiles)

	def _components(cells: Set[Tuple[int, int]]) -> list:
		seen: Set[Tuple[int, int]] = set()
		comps = []
		for start in cells:
			if start in seen:
				continue
			comp: Set[Tuple[int, int]] = set()
			dq = deque([start])
			seen.add(start)
			while dq:
				cx, cy = dq.popleft()
				comp.add((cx, cy))
				for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
					if (nx, ny) in cells and (nx, ny) not in seen:
						seen.add((nx, ny))
						dq.append((nx, ny))
			comps.append(comp)
		return comps

	def _bridge_between(source: Set[Tuple[int, int]],
						targets: Set[Tuple[int, int]],
						blocked: Set[Tuple[int, int]],
						bounds: Tuple[int, int, int, int]) -> list:
		"""Shortest free-cell path from `source` to any `targets` tile.

		BFS outward from every `source` tile across free cells only (never through
		`blocked`/occupied cells). The search is confined to `bounds`
		(min_x, max_x, min_y, max_y) so it can never radiate across the unbounded
		grid — without this an enclosed target would make the BFS expand forever
		and exhaust memory. Returns the list of intermediate free cells to fill, or
		None if no occupied-free route exists inside the bounds.
		"""
		min_x, max_x, min_y, max_y = bounds
		frontier = deque()
		came_from: dict = {}
		for cell in source:
			frontier.append(cell)
			came_from[cell] = None
		while frontier:
			cur = frontier.popleft()
			cx, cy = cur
			for nxt in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
				if nxt in came_from:
					continue
				if nxt in targets:
					# Reconstruct the intermediate cells (exclude both endpoints).
					path = []
					node = cur
					while node is not None and node not in source:
						path.append(node)
						node = came_from[node]
					path.reverse()
					return path
				nx, ny = nxt
				# Confine the search to the padded footprint bounds.
				if nx < min_x or nx > max_x or ny < min_y or ny > max_y:
					continue
				if nxt in blocked:
					continue
				came_from[nxt] = cur
				frontier.append(nxt)
		return None

	# Iteratively merge components by carving a shortest free-cell bridge between
	# the closest reachable pair until a single component remains (or no further
	# bridge can be made without crossing occupied cells).
	comps = _components(working)
	# Occupied cells that bridges must route around: foreign tiles not owned here.
	blocked = set(ignored_set) - working
	xs = [x for (x, _) in working]
	ys = [y for (_, y) in working]
	fminx, fmaxx = min(xs), max(xs)
	fminy, fmaxy = min(ys), max(ys)
	footprint_span = max(fmaxx - fminx, fmaxy - fminy)
	max_iterations = len(comps) + 1
	iterations = 0
	while len(comps) > 1 and iterations < max_iterations:
		iterations += 1
		# Connect the first component to the nearest other component via a route
		# that avoids occupied cells entirely.
		source = comps[0]
		targets = set().union(*comps[1:])
		# A fixed margin can wrongly report "no route" when a valid detour exists
		# just outside it, failing an otherwise repairable world. Instead widen
		# the bridge-search bounds adaptively: start snug and grow the margin
		# (doubling) until a route is found or an explicit cap is hit, so the BFS
		# still can't radiate across the unbounded grid and exhaust memory.
		margin = 4
		# Cap the margin relative to the footprint so the bounded area stays
		# finite but is generous enough to route around sizeable obstacles.
		margin_cap = max(16, footprint_span * 2 + 8)
		path = None
		while path is None:
			# Never exceed the cap, but ALWAYS try the cap itself: doubling could
			# otherwise jump past a non-power-of-two cap and skip valid detours
			# whose required margin lies between the last power of two and the cap.
			margin = min(margin, margin_cap)
			bounds = (fminx - margin, fmaxx + margin, fminy - margin, fmaxy + margin)
			path = _bridge_between(source, targets, blocked, bounds)
			if path is not None or margin == margin_cap:
				break
			margin *= 2
		if path is None:
			# No occupied-free route to any other component even within the
			# expanded (capped) bounds; leave remaining components rather than
			# carving through another region's tiles.
			break
		for cell in path:
			added.add(cell)
			working.add(cell)
		comps = _components(working)

	tiles |= added
	return tiles
from game.services.region_frontier_service import (
	randomized_frontier_perimeter_pathing,
	perimeter_driven_growth
)
from game.services.region_shape_service import make_filled_circle, make_filled_star, make_filled_diamond, make_filled_hex, make_filled_square

logger = logging.getLogger(__name__)


def create_region_city(region_settings: dict) -> City:
	"""Create and configure an empty region City from settings."""
	rseed = (random.SystemRandom().randint(0, 2**32 - 1) ^ 0xA5A5A5) + 1
	rc = City(
		rseed,
		road_spacing=region_settings.get("road_spacing", 0),
		alley_spacing=region_settings.get("alley_spacing", 0),
		alley_offset=region_settings.get("alley_offset", 0),
	)
	# apply other region-level flags
	rc.max_size = region_settings.get("max_size", rc.max_size)
	rc.population_density = region_settings.get("population_density", rc.population_density)
	rc.hasResidence = region_settings.get("hasResidence", rc.hasResidence)
	rc.hasBusiness = region_settings.get("hasBusiness", rc.hasBusiness)
	rc.hasShops = region_settings.get("hasShops", rc.hasShops)
	rc.hasBar = region_settings.get("hasBar", rc.hasBar)
	rc.hasInn = region_settings.get("hasInn", rc.hasInn)
	rc.hasHyperway = region_settings.get("hasHyperway", rc.hasHyperway)
	rc.hasOther1 = region_settings.get("hasOther1", rc.hasOther1)
	rc.hasOther2 = region_settings.get("hasOther2", rc.hasOther2)
	rc.region_name = region_settings.get("region_name", None)
	rc.city_name = region_settings.get("city_name", None)
	rc.display_name = region_settings.get("display_name", rc.city_name)
	rc.child_city = None

	#print(f"all rc info: region_name={rc.region_name}, city_name={rc.city_name}, display_name={rc.display_name}, max_size={rc.max_size}, population_density={rc.population_density}, hasResidence={rc.hasResidence}, hasBusiness={rc.hasBusiness}, hasShops={rc.hasShops}, hasBar={rc.hasBar}, hasInn={rc.hasInn}")
	return rc

def create_region(	
	rc: City,
	origin: Tuple[int, int],
	shifted_location: Tuple[int, int],
	main_tiles: Set[Tuple[int, int]],
	neighbor_offsets: Iterable[Tuple[int, int]],
	center_x: int,
	center_y: int,
	ignored_set: Set[Tuple[int, int]],
	region_settings: dict,
	player_game: object,
) -> Set[Tuple[int, int]]:
	region_tiles = set()
	#print(f"Creating region using: origin={origin}, shifted_location={shifted_location}, main_tiles={len(main_tiles)}, ignored_set={len(ignored_set)}")
	max_size = region_settings.get("max_size", rc.max_size)
	if main_tiles and len(main_tiles) > 0:
		# get the midpoint of the main tiles and the radius to cover them
		midpoint_x = sum(x for x, y in main_tiles) // len(main_tiles)
		midpoint_y = sum(y for x, y in main_tiles) // len(main_tiles)
		radius = max(
			int(math.sqrt((x - midpoint_x) ** 2 + (y - midpoint_y) ** 2))
			for x, y in main_tiles
		) + 1
		#print (f"midpoint_x: {midpoint_x}, midpoint_y: {midpoint_y}, radius: {radius}")
	else:
		#midpoint_x, midpoint_y = origin
		radius = 0
	if not radius:
		radius = 10

	# set radius = half sqrt of max size
	if max_size and max_size > 0:
		radius = int(max(radius, int(math.sqrt(max_size) / 2)) /3)
		
	current_tiles = main_tiles.copy()

	random.seed(random.SystemRandom().randint(0, 2**32 - 1))

	rng = random.random()
	# NOTE TO MAKE OTHER BASE REGIONS SUCH AS TETRIS SHAPES: S, T, L, |, etc.
	#input (f'making something at : ({center_x},{center_y}) with radius {radius}, rng:{rng}')
	if rng < 0.20:
		frontier = make_filled_hex(center_x, center_y, radius, current_tiles, ignored_set)
	elif rng < 0.40:
		frontier = make_filled_diamond(center_x, center_y, radius, current_tiles, ignored_set)
	elif rng < 0.60:
		frontier = make_filled_square(center_x, center_y, radius, current_tiles, ignored_set)
	elif rng < 0.80:
		frontier = make_filled_circle(center_x, center_y, radius, current_tiles, ignored_set)
	else:
		points = random.randint(3,7)

		frontier = make_filled_star(center_x, center_y, radius, points, 1.0, current_tiles, ignored_set)

	# the next step is to use perimeter growth to fill out the region
	#frontier_path = randomized_frontier_perimeter_pathing(center_x, center_y, current_tiles, ignored_set, neighbor_offsets, rc.max_size)
	frontier_path = perimeter_driven_growth( current_tiles, ignored_set, neighbor_offsets, max_size )

	frontier.update(frontier_path)

	# Region growth joins tiles 8-directionally, but the player moves orthogonally
	# and continent contiguity is checked with 4-connectivity. Close any
	# diagonal-only gaps so the footprint is a single 4-connected mass. Capture
	# the newly added bridge cells so we can (a) keep them out of required-building
	# placement and (b) force them to walkable open ground after materialization --
	# create_tile may otherwise roll them impassable or as entrance-less buildings,
	# which would leave the footprint geometrically joined but impassable on foot.
	before_bridge = set(frontier)
	ensure_4_connected(frontier, ignored_set)
	bridge_cells = set(frontier) - before_bridge

	rc.child_city = {}
	# Required buildings must not land on a connective corridor cell (that would
	# re-block the join), so offer only non-bridge locations for placement.
	building_locations = frontier - bridge_cells
	rc.ensure_required_buildings(player_game, building_locations)
	#self.tiles: Dict[Tuple[int, int], Tile] = {}
	for x, y in frontier:
		if not (x,y) in rc.tiles.keys():  #self.tiles: Dict[Tuple[int, int], Tile] = {}
			#print (f'Creating tile at ({x},{y}) for region city "{rc.region_name}".')
			rc.create_tile(player_game, x, y)
		# else:
		# 	input (f'Tile at ({x},{y}) already exists for region city "{rc.region_name}", skipping creation.')

	# Guarantee every bridge cell is a walkable corridor (open ground), overriding
	# any impassable/building tile create_tile may have generated for it.
	for (bx, by) in bridge_cells:
		tile = rc.tiles.get((bx, by))
		if tile is not None:
			tile.type = 'open_area'
			tile.building = None
			tile.entrances = ()
			tile.floors = 0
			tile.has_basement = False

	#input (f'Filled region city "{rc.region_name}" with {len(frontier)} tiles before filling bound uncreated space.')
	rc.populate_tiles(player_game)
	#input (f'Created region city "{rc.region_name}" with {len(frontier)} tiles.')

def fill_bound_uncreated_space (
	rc: City,
	origin: Tuple[int, int],
	shifted_location: Tuple[int, int],
	current_tiles: Set[Tuple[int, int]],
	ignored_set: Set[Tuple[int, int]],
	) -> Set[Tuple[int, int]]:
	"""Scan the bounding box between origin and shifted_location for uncreated tile chunks fully bound by current_tiles."""
	#determine bounding box
	res = set()
	minx = min(origin[0], shifted_location[0])
	maxx = max(origin[0], shifted_location[0])
	miny = min(origin[1], shifted_location[1])
	maxy = max(origin[1], shifted_location[1])
	for x in range(minx, maxx +1):
		for y in range(miny, maxy +1):
			if (x, y) in current_tiles or (x, y) in ignored_set:
				continue
			#check if this tile is fully bound by current_tiles
			bound = True
			for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
				n = (x + dx, y + dy)
				if n not in current_tiles and n not in ignored_set:
					bound = False
					break
			if bound:
				current_tiles.add((x, y))
				res.add((x, y))

def is_origin_created(origin: Tuple[int, int], frontier: deque) -> bool:
	for fx, fy in frontier:
		if (fx, fy) == origin:
			return True
	return False

def get_distance_to_frontier(origin: Tuple[int, int], frontier: deque) -> int:
	"""Calculate the distance from the origin to the nearest point in the frontier."""
	if not frontier:
		return float('inf')
	distance = min(math.sqrt((fx - origin[0]) ** 2 + (fy - origin[1]) ** 2) for fx, fy in frontier)
	#print(f"Distance to frontier from origin {origin}: {distance}")
	return distance


def prepare_main_context(main_city: City, origin: Tuple[int, int], ignored_locations: Iterable[Tuple[int, int]] = None):
	"""Compute bounding box, main tile set, perimeter and neighbor offsets."""
	ignored_set = set(ignored_locations) if ignored_locations else set()

	if main_city is not None:
		xs = [x for (x, _) in main_city.tiles.keys()] if main_city.tiles else []
		ys = [y for (_, y) in main_city.tiles.keys()] if main_city.tiles else []
		if xs and ys:
			minx, maxx = min(xs), max(xs)
			miny, maxy = min(ys), max(ys)
	else:
		minx = origin[0] - 8
		maxx = origin[0] + 8
		miny = origin[1] - 8
		maxy = origin[1] + 8

	main_tiles = set(main_city.tiles.keys()) if main_city is not None else set()

	# perimeter: child tiles that touch empty space
	perimeter = set()
	for (x, y) in main_tiles:
		for dx, dy in ((1,0), (-1,0), (0,1), (0, -1)):
			n = (x + dx, y + dy)
			if n in ignored_set:
				continue
			if n not in main_tiles:
				perimeter.add((x, y))
	neighbor_offsets = [(1,0), (-1,0), (0,1), (0, -1), (1,1), (1, -1), (-1,1), (-1, -1)]
	center_x = (minx + maxx) //2
	center_y = (miny + maxy) //2
	#input (f'origin: {origin},minx {minx},maxx {maxx},miny {miny}, maxy:{maxy}')
	return {
		"ignored_set": ignored_set,
		"minx": minx,
		"maxx": maxx,
		"miny": miny,
		"maxy": maxy,
		"main_tiles": main_tiles,
		"perimeter": perimeter,
		"neighbor_offsets": neighbor_offsets,
		"center_x": center_x,
		"center_y": center_y,
	}
