from typing import Set, Tuple,List
import random
from game.objects.city import City, Tile#, populate_sublocs_for_radius
from game.objects.player import Player
from game.constants import ROAD, BUILDING, ALLEY
from game.region_seeds.city_bitmaps import CITY_BITMAPS
import math
import game.constants as const

def place_open_area_buildings(city: City, city_area: Set[Tuple[int,int]], building_chance: float =0.05):
	"""Place buildings randomly inside open areas of the city footprint. based on regional settings"""
	return

def give_roads_personality(city: City):
	"""Modify existing roads to add alleys or vary road styles.
	Currently a stub for future expansion.

	chooses valid carved road locations for removal in order to construct cul de sacs, turns, and identity away from a grid
	logic constraint must conatin a path from one side to the other vertical/horizontally
	"""

	return

def translate_city(city: City, shifted_location: Tuple[int, int]) -> None:
	"""Translate all tiles in `city` by (dx, dy) in-place.

	This updates the tile dictionary keys and attempts to update Tile.x/Tile.y
	if those attributes are writable. The function modifies the City in-place.
	"""
	dx,dy = shifted_location

	new_tiles = {}
	for (x, y), t in list(city.tiles.items()):
		new_k = (x + dx, y + dy)
		t.x = new_k[0]
		t.y=  new_k[1]
		
		new_tiles[new_k] = t

	city.tiles = new_tiles

def build_city_map(seed: int = random.SystemRandom().randint(0,2**32 -1)):
	""" THIS METHOD ONLY CREATES THE BASE BLUEPRINT FOR THE CITY, Buildings and roads are created later

	Generates an irregular, non-square floor plane up to `city.max_size` tiles.
	Behavior:
	- Grow a core blob from `center` using randomized neighbor expansion.
	- Occasionally spawn small outcroppings detached from the core to create variation.
	- Respect `city.max_size` strictly when creating Tile entries.
	- Use a loose spatial bound (max_dim) derived from sqrt(max_size) *1.25 to allow spread.
	"""
	random.seed(seed)
	# allow caller to override the city's procedural grid spacing so an
	# in-memory city can be generated using the region's grid parameters.
	city = City(seed)
	center = (0,0)
	max_tiles = int(getattr(city, 'max_size',200))
	# spatial bound: linear dimension slightly larger than sqrt(max_tiles)
	max_dim = max(8, int(math.ceil(math.sqrt(max_tiles) *1.25)))
	#print(f"build_city_map: seed={seed} target_max_tiles={max_tiles} max_dim={max_dim}")

	# Simple randomized growth: start at center and expand
	tiles: Set[Tuple[int,int]] = set()
	from collections import deque
	frontier = deque()
	frontier.append(center)

	# neighbor offsets (8-connected to allow organic shapes)
	nbh = [(-1, -1), (-1,0), (-1,1), (0, -1), (0,1), (1, -1), (1,0), (1,1)]

	rng = random.random()

	if rng < 0.5:
		draw_character_bitmap(max_tiles, max_dim, tiles)
	else:
		draw_random_splotches(max_tiles, max_dim, tiles)

	#ensure center
	if center not in tiles:
		if len(tiles) >= max_tiles:
			tiles.pop()
		tiles.add(center)

	# finally, write tiles into city.tiles as Tile objects
	count =0
	for (x, y) in tiles:
		if count >= max_tiles:
			break
		city.tiles[(x, y)] = Tile(x, y, 'open_area')
		count +=1

	#print(f"build_city_map: created {count} floor tiles (requested max {max_tiles})")
	return city, center

def draw_character_bitmap(max_tiles, max_dim, tiles):
	""" METHOD draws the tiles as a bitmap based on character bitmaps... ex: (?# is to represent bounds of example, t represents a tile placement)
	Well this is my idea of a mario shroom 
	... the image should scale to use max_size tiles and have no more than max_dim(max(8, int(math.ceil(math.sqrt(max_tiles) *1.25)))) dimension.
	????????????????????????? 
	?                       ?
	?                       ?
	?       tttttttt        ?
	?     ttttttt ttt       ?
	?     ttt ttttt tt      ?
	?     tttttttttttt      ?		
	?        tttttt         ?
	?????????????????????????
	"""
	bitmaps = CITY_BITMAPS

	# pick a bitmap at random
	bm = random.choice(bitmaps)
	# collect tile coords from bitmap (row major), origin top-left
	orig_coords = []
	for ry, row in enumerate(bm):
		for rx, ch in enumerate(row):
			if ch != ' ':
				orig_coords.append((rx, ry))

	if not orig_coords:
		return

	# compute original dims
	w = max(x for x, _ in orig_coords) - min(x for x, _ in orig_coords) +1
	h = max(y for _, y in orig_coords) - min(y for _, y in orig_coords) +1

	# center the bitmap around (0,0)
	minx = min(x for x, _ in orig_coords)
	miny = min(y for _, y in orig_coords)
	# normalize coords to start at (0,0)
	norm = [(x - minx, y - miny) for (x, y) in orig_coords]

	# if bitmap exceeds max_dim, downsample by skipping rows/cols
	current_w, current_h = w, h
	x_skip =1
	y_skip =1
	while (current_w * current_h > max_dim * max_dim) and (x_skip < current_w or y_skip < current_h):
		# increase skip factor to downsample
		# strategy: bump whichever dimension is larger, so area shrinks faster
		if current_w >= current_h and current_w > max_dim:
			x_skip += 1
		elif current_h > max_dim:
			y_skip += 1
		# rebuild normalized coords with skipping
		norm = [(x, y) for (x, y) in norm if (x % x_skip ==0 and y % y_skip ==0)]
		if not norm:
			break
		current_w = (current_w + x_skip -1) // x_skip
		current_h = (current_h + y_skip -1) // y_skip

	# now we may scale up (integer scaling) while staying under max_dim and tile budget
	# compute desired scale factor
	# now we may scale up (integer scaling) while staying under max area and tile budget
	scale = 1

	if current_w * current_h < max_dim * max_dim:
		# compute maximum possible scale factor by area
		max_scale = int(math.sqrt((max_dim * max_dim) / (current_w * current_h)))
		base_tile_count = len(norm)

		for s in range(1, max_scale + 1):
			if base_tile_count * (s * s) <= max_tiles:
				scale = s


	# apply scaling by replicating each normalized tile into an s x s block
	scaled = []
	for (x, y) in norm:
		for sx in range(scale):
			for sy in range(scale):
				scaled.append((x * scale + sx, y * scale + sy))

	if not scaled:
		return

	# center scaled coords around (0,0)
	minx = min(x for x, _ in scaled)
	miny = min(y for _, y in scaled)
	maxx = max(x for x, _ in scaled)
	maxy = max(y for _, y in scaled)
	center_x = (minx + maxx) //2
	center_y = (miny + maxy) //2
	centered = [ (x - center_x, y - center_y) for (x, y) in scaled ]

	# ensure we do not exceed max_tiles
	if len(centered) > max_tiles:
		# sample deterministically (to keep reproducible with RNG seed)
		random.shuffle(centered)
		centered = centered[:max_tiles]

	tiles.clear()
	for c in centered:
		tiles.add(c)

def draw_random_splotches(max_tiles, max_dim, tiles):
	""" METHOD draws the tiles as random blocks with independently random sides of length between3 and7, but x * y <=25... ex: (? is to represent bounds of example, t represents a tile placement)
	The idea is to stamp variable sized blocks in random clocations to create diversity in the city layout
	the image should scale to fill max size and no more.
	... the area should use max_size tiles and have no more than max_dim(max(8, int(math.ceil(math.sqrt(max_tiles) *1.25)))) dimension.
	"""
	# Clear incoming list and build up a set to avoid duplicates
	tiles_set = set()
	# bounding box within which stamps can be placed (centered on0)
	half = max(1, max_dim //2)
	attempts =0
	max_attempts = max(200, max_tiles *4)
	# stamp rectangles until we fill or run out of attempts
	while len(tiles_set) < max_tiles and attempts < max_attempts:
		attempts +=1
		# choose a random rectangle size. width*height <=25, side lengths between1 and7
		w = random.randint(1,7)
		h = random.randint(1,7)
		if w * h >25:
			# reduce the larger side to fit
			if w > h:
				w = max(1,25 // h)
			else:
				h = max(1,25 // w)
		# pick an origin within bounds such that the rectangle will likely fit
		ox = random.randint(-half, half)
		oy = random.randint(-half, half)
		# compute candidate coords
		cand = []
		fits = True
		for dx in range(w):
			for dy in range(h):
				x = ox + dx
				y = oy + dy
				# if this would push bounding box beyond max_dim, mark as not fit
				# compute potential bbox if this were added
				# quick check: if coordinate outside allowed half-range, skip
				if abs(x) > half or abs(y) > half:
					fits = False
					break
				cand.append((x, y))
			if not fits:
				break
		if not fits:
			continue
		# add candidates, but respect max_tiles
		space_left = max_tiles - len(tiles_set)
		for c in cand:
			if space_left <=0:
				break
			if c not in tiles_set:
				tiles_set.add(c)
				space_left -=1

	# ensure we have at least one tile (fallback)
	if not tiles_set:
		tiles_set.add((0,0))

	# convert to list and center if needed
	coords = list(tiles_set)
	minx = min(x for x, _ in coords)
	miny = min(y for _, y in coords)
	maxx = max(x for x, _ in coords)
	maxy = max(y for _, y in coords)
	# if any dimension exceeds max_dim, shift/clip to center
	width = maxx - minx +1
	height = maxy - miny +1
	if width > max_dim or height > max_dim:
		# translate to center and crop
		center_x = (minx + maxx) //2
		center_y = (miny + maxy) //2
		half_w = max_dim //2
		coords = [ (x - center_x, y - center_y) for (x, y) in coords if abs(x - center_x) <= half_w and abs(y - center_y) <= half_w ]

	# truncate if over max_tiles
	if len(coords) > max_tiles:
		random.shuffle(coords)
		coords = coords[:max_tiles]

	# write back to provided tiles list or set

	tiles.clear()
	for c in coords:
		tiles.add(c)



############################################# UI METHOD

def print_city_map(city: City, center: Tuple[int, int], radius: int =30):
	# compute bounding square from current city tiles
	if city.tiles:
		xs = [x for (x, _) in city.tiles.keys()]
		ys = [y for (_, y) in city.tiles.keys()]
		minx, maxx = min(xs), max(xs)
		miny, maxy = min(ys), max(ys)
	else:
		minx = center[0] - radius
		maxx = center[0] + radius
		miny = center[1] - radius
		maxy = center[1] + radius
	# make square bounds with padding of1
	width = maxx - minx +1
	height = maxy - miny +1
	size = max(width, height) +2
	start_x = minx -1
	start_y = miny -1
	end_x = start_x + size -1
	end_y = start_y + size -1

	out_lines: List[str] = []
	for y in range(start_y, end_y +1):
		row = []
		for x in range(start_x, end_x +1):
			t = city.tiles.get((x, y))
			if t is None:
				row.append('?')
			elif t.type == ROAD:
				row.append('=')
			elif t.type == BUILDING:
				ch = t.building.get('char') if isinstance(t.building, dict) else 'B'
				row.append(ch if ch else 'B')
			elif t.type == 'open_area':
				row.append(' ')
			elif t.type == 'open_area':
				row.append('*')
			elif t.type == ALLEY:
				row.append('"')
			else:
				row.append(' ')
		out_lines.append(''.join(row))
	#print('\n'.join(out_lines))
