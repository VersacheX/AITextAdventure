"""Simple city+region generator applet for quick testing.

This will create a City instance (using the existing City class) and carve
non-grid roads by random walks, place buildings adjacent to roads, and
produce an oddly-shaped city area using a paint-brush technique.

The script purposely keeps the generator simple and standalone so you can
iterate quickly on map shapes during development.
"""
import sys
import random
import math
from typing import Tuple, List, Set, Optional
import logging
import time

# create module logger
logger = logging.getLogger(__name__)


# Fix global _sgn implementation
def _sgn(n: int) -> int:
	# return sign of n: -1,0, or1
	if n >0:
		return 1
	if n <0:
		return -1
	return 0

# Import the project's City/Tile and constants. Running this script from the
# repository root should make the package imports resolve as in the project.
from game.objects.city import City, Tile
from game.objects.player import Player
from game.constants import ROAD, ALLEY, BUILDING # type: ignore
import game.constants as const
from game.services.city_builder_service import build_city_map,translate_city

from game.services.region_builder_service import (
	create_region_city,
	prepare_main_context,

	create_region,
)


def _find_translation_away(main_city: City, ignored_set: Set[Tuple[int,int]], origin: Tuple[int,int], max_distance: int, buffer: int = 0) -> Optional[Tuple[int,int]]:
	"""Find a translation (dx,dy) that moves main_city away from ignored_set.

	- `buffer` specifies required tile-gap in tiles (Chebyshev distance). A candidate
	  is considered zero-overlap only if no ignored tile exists within `buffer`
	  tiles of any translated city tile.
	- Search integer translations within radius `max_distance`.
	- Prefer zero-buffer candidates (closest to origin). If none, return the minimal-overlap
	  candidate (overlap = count of city tiles that have at least one ignored tile within buffer).
	"""
	if not ignored_set:
		return (0, 0)

	tiles = list(main_city.tiles.keys())
	if not tiles:
		return (0, 0)

	ignored = set(ignored_set)
	origin_x, origin_y = origin

	# city center (local tile coords) -> use absolute translated center for scoring
	xs = [x for (x, _) in tiles]
	ys = [y for (_, y) in tiles]
	city_center_x = (min(xs) + max(xs)) / 2.0
	city_center_y = (min(ys) + max(ys)) / 2.0

	best_zero: Optional[Tuple[int,int]] = None
	best_zero_d2 = float('inf')  # prefer closer to origin

	best_min: Optional[Tuple[int,int]] = None
	best_min_overlap = float('inf')
	best_min_d2 = float('inf')

	max_d_sq = max_distance * max_distance

	# Precompute neighbor offsets for buffer area (Chebyshev)
	buf_offsets = [(bx, by) for bx in range(-buffer, buffer + 1) for by in range(-buffer, buffer + 1)]

	# scan integer translations in bounding square (filter by circle)
	for dx in range(-max_distance, max_distance + 1):
		for dy in range(-max_distance, max_distance + 1):
			d_sq = dx * dx + dy * dy
			if d_sq > max_d_sq:
				continue

			# count collisions where any ignored tile is within buffer (chebyshev)
			collisions = 0
			# short-circuit if already worse than best minimal overlap
			for (tx, ty) in tiles:
				final_x = tx + origin_x + dx
				final_y = ty + origin_y + dy
				# check neighbor positions within buffer
				hit = False
				for (bx, by) in buf_offsets:
					if (final_x + bx, final_y + by) in ignored:
						hit = True
						break
				if hit:
					collisions += 1
					if collisions > best_min_overlap:
						break

			# d2: squared distance from translated city center to requested origin
			translated_cx = city_center_x + origin_x + dx
			translated_cy = city_center_y + origin_y + dy
			d2_to_origin = (translated_cx - origin_x) ** 2 + (translated_cy - origin_y) ** 2

			if collisions == 0:
				# zero-buffer candidate: prefer closer to origin
				if d2_to_origin < best_zero_d2:
					best_zero = (dx, dy)
					best_zero_d2 = d2_to_origin
			else:
				# minimal-overlap candidate: prefer smaller collisions, tie-break by closer to origin
				if collisions < best_min_overlap or (collisions == best_min_overlap and d2_to_origin < best_min_d2):
					best_min_overlap = collisions
					best_min = (dx, dy)
					best_min_d2 = d2_to_origin

	# prefer zero-buffer candidate
	if best_zero is not None:
		#print(f'Found zero-buffer translation {best_zero} at d2={best_zero_d2} (max_distance={max_distance}, buffer={buffer})')
		return best_zero

	# no perfect placement; return minimal-overlap candidate and diagnostics
	if best_min is not None:
		total_city_tiles = len(tiles)
		overlap = int(best_min_overlap)
		ratio = overlap / max(1, total_city_tiles)
		#print(f'No zero-buffer translation within max_distance={max_distance} (buffer={buffer}). Minimal overlap={overlap} of {total_city_tiles} tiles ({ratio:.2%}) at {best_min} (d2={best_min_d2}).')

		# sample colliding coords (absolute)
		collisions = []
		dx, dy = best_min
		for (tx, ty) in tiles:
			final_pos = (tx + origin_x + dx, ty + origin_y + dy)
			# report the ignored neighbor that caused the collision
			found = None
			for (bx, by) in buf_offsets:
				npos = (final_pos[0] + bx, final_pos[1] + by)
				if npos in ignored:
					found = npos
					break
			if found:
				collisions.append((final_pos, found))
				if len(collisions) >= 12:
					break
		#print('Sample collisions (translated_tile, colliding_ignored):', collisions)
		return best_min

	#print('No translation candidates evaluated (empty ignored set or empty city).')
	return None

def _find_translation_away_pre(main_city: City, ignored_set: Set[Tuple[int,int]], origin: Tuple[int,int], max_distance: int, preferred_dir: Optional[str] = None) -> Optional[Tuple[int,int]]:
	"""Find a translation (dx,dy) that moves main_city away from ignored_set.

	Correct coordinate usage: tests collisions against absolute positions that
	will be used by translate_city: final_pos = (tx + origin_x + dx, ty + origin_y + dy).

	- Search integer translations within radius max_distance.
	- Prefer zero-overlap placements; among them prefer ones matching preferred_dir
	  then closest to `origin`.
	- If none zero-overlap, return minimal-overlap candidate (with diagnostics).
	"""
	if not ignored_set:
		return (0, 0)

	tiles = list(main_city.tiles.keys())
	if not tiles:
		return (0, 0)

	ignored = set(ignored_set)
	origin_x, origin_y = origin

	# city center (local tile coords) -> use absolute translated center for scoring
	xs = [x for (x, _) in tiles]
	ys = [y for (_, y) in tiles]
	city_center_x = (min(xs) + max(xs)) / 2.0
	city_center_y = (min(ys) + max(ys)) / 2.0

	best_zero: Optional[Tuple[int,int]] = None
	best_zero_score = (2, float('inf'))  # (dir_penalty, d2_to_origin)

	best_min: Optional[Tuple[int,int]] = None
	best_min_score = (float('inf'), 2, float('inf'))  # (overlap, dir_penalty, d2_to_origin)

	max_d_sq = max_distance * max_distance

	def _direction_penalty(dx: int, dy: int) -> int:
		if not preferred_dir:
			return 0
		if preferred_dir == 'left' and dx < 0:
			return 0
		if preferred_dir == 'right' and dx > 0:
			return 0
		if preferred_dir == 'up' and dy < 0:
			return 0
		if preferred_dir == 'down' and dy > 0:
			return 0
		return 1

	# scan integer translations in bounding square, filter by circle radius
	for dx in range(-max_distance, max_distance + 1):
		for dy in range(-max_distance, max_distance + 1):
			d_sq = dx*dx + dy*dy
			if d_sq > max_d_sq:
				continue

			# count overlap using final absolute positions (include origin)
			overlap = 0
			# short-circuit if already worse than best minimal overlap
			for (tx, ty) in tiles:
				final_pos = (tx + origin_x + dx, ty + origin_y + dy)
				if final_pos in ignored:
					overlap += 1
					if overlap > best_min_score[0]:
						break

			# d2: squared distance from translated city center to requested origin
			translated_cx = city_center_x + origin_x + dx
			translated_cy = city_center_y + origin_y + dy
			d2_to_origin = (translated_cx - origin_x)**2 + (translated_cy - origin_y)**2

			dir_pen = _direction_penalty(dx, dy)

			if overlap == 0:
				score = (dir_pen, d2_to_origin)
				if score < best_zero_score:
					best_zero_score = score
					best_zero = (dx, dy)
			else:
				score = (overlap, dir_pen, d2_to_origin)
				if score < best_min_score:
					best_min_score = score
					best_min = (dx, dy)

	# prefer zero-overlap candidate (best matching preferred_dir then closests to origin)
	if best_zero is not None:
		print(f'Found zero-overlap translation {best_zero} score={best_zero_score} (max_distance={max_distance}, preferred_dir={preferred_dir})')
		return best_zero

	# no perfect placement; return minimal-overlap candidate and diagnostics
	if best_min is not None:
		total_city_tiles = len(tiles)
		overlap = int(best_min_score[0])
		ratio = overlap / max(1, total_city_tiles)
		print(f'No zero-overlap translation within max_distance={max_distance}. Minimal overlap={overlap} of {total_city_tiles} tiles ({ratio:.2%}) at {best_min} (score={best_min_score}).')

		# sample colliding coords (absolute)
		collisions = []
		dx, dy = best_min
		for (tx, ty) in tiles:
			final_pos = (tx + origin_x + dx, ty + origin_y + dy)
			if final_pos in ignored:
				collisions.append(final_pos)
				if len(collisions) >= 12:
					break
		print('Sample collisions (up to 12):', collisions)
		return best_min

	print('No translation candidates evaluated (empty ignored set or empty city).')
	return None

def _find_translation_away_old(main_city: City, ignored_set: Set[Tuple[int,int]], origin: Tuple[int,int], max_distance: int) -> Optional[Tuple[int,int]]:
	"""Find a translation vector (dx,dy) that moves main_city away from ignored_set.

	Strategy: try cardinal/diagonal directions and increasing multiples of
	`min_distance` until we find a translation that yields zero overlap with
	`ignored_set` (no tile collides). 

	prefer the one that places the translated city's center as close
	as possible to `origin` (minimize distance to origin).
	
	# If no perfect candidate exists, return
	# the candidate with minimal overlap. 
	
	# When multiple candidates have the same
	# overlap, 
	
	"""
	if not ignored_set:
		return (0,0)
	# candidate directions (including diagonals)
	dirs = [(1,0), (-1,0), (0,1), (0, -1), (1,1), (1, -1), (-1,1), (-1, -1)]
	best = None
	best_dist = float('inf')
	tiles = list(main_city.tiles.keys())
	if not tiles:
		return (0,0)
	xs = [x for (x, _) in tiles]
	ys = [y for (_, y) in tiles]
	center_x = (min(xs) + max(xs)) /2.0
	center_y = (min(ys) + max(ys)) /2.0

	for dist in range(1, max_distance +1):
		for dx_sign, dy_sign in dirs:
			dx = dx_sign * dist
			dy = dy_sign * dist
			overlap =0
			for (tx, ty) in tiles:
				if (tx + dx, ty + dy) in ignored_set:
					overlap +=1
			translated_cx = center_x + dx
			translated_cy = center_y + dy
			d2 = (translated_cx - origin[0]) **2 + (translated_cy - origin[1]) **2
			if overlap ==0:
				if d2 < best_dist:
					best = (dx, dy)
					best_dist = d2

	return best if best is not None else None

##################################### REGION BUILDING FUNCTIONS #####################################
def build_region_around(main_city: City, region_settings: dict, origin: Tuple[int,int], shifted_location: Tuple[int,int], player_game, ignored_locations: Set[Tuple[int,int]] = None):
	"""High-level orchestration that reads as a sequence of steps.

	This function delegates details to `region_builder_service` and the
	frontier/shape services so it remains compact and easy to follow.


	"""
	# Step1: create and configure region city
	rc = create_region_city(region_settings)

	# Step2: prepare context (bounds, perimeter, neighbor offsets)
	ctx = prepare_main_context(main_city, shifted_location, ignored_locations)
	#print (f"region context: minx={ctx['minx']}, maxx={ctx['maxx']}, miny={ctx['miny']}, maxy={ctx['maxy']}, center=({ctx['center_x']},{ctx['center_y']}), perimeter_tiles={len(ctx['perimeter'])}, neighbor_offsets={ctx['neighbor_offsets']}, main_tiles={len(ctx['main_tiles'])}")
	ignored_set = ctx['ignored_set']
	minx = ctx['minx']; maxx = ctx['maxx']; miny = ctx['miny']; maxy = ctx['maxy']	
	# expose values for downstream helpers
	perimeter = ctx['perimeter']
	neighbor_offsets = ctx['neighbor_offsets']
	center_x = ctx['center_x']; center_y = ctx['center_y']
	main_tiles = ctx['main_tiles']

	#input(f'Region context prepared: minx={minx}, maxx={maxx}, miny={miny}, maxy={maxy}, center=({center_x},{center_y}), perimeter_tiles={len(perimeter)}, neighbor_offsets={neighbor_offsets}, main_tiles={len(main_tiles)}. Press Enter to continue...')
	create_region(rc, origin, shifted_location, main_tiles, neighbor_offsets, center_x, center_y, ignored_set, region_settings, player_game)
		
	return rc

def build_region_map (player_game, region_settings: dict, origin: Tuple[int,int], hasCity: bool = False, ignored_locations: Tuple[int, int] = None):
	#print(f'Building region map for region "{region_settings["region_name"]}" at origin {origin}, hasCity={hasCity}')
	random.seed(random.SystemRandom().randint(0,2**32 -1))
	rng_perc = random.random()
	ignored_set = set(ignored_locations) if ignored_locations else set()

	# Not implemented select City type at random or from region cities... have not decided on how to develop this
	# build_city_map needs a city object in order to determine max_size... which is currently using the default on City
	main_city = None
	center = origin
	if player_game.previous_region and player_game.previous_region.child_city is not None:
		main_city = None
	elif player_game.previous_region and random.random() < 0.8 and hasCity:
		main_city, _ = build_city_map(random.SystemRandom().randint(0,2**32 -1)) # need to pass 
	elif player_game.previous_region is	None:
		main_city, _ = build_city_map(random.SystemRandom().randint(0,2**32 -1))

	#SET hasCity to false if no main_city was built
	if main_city is None:
		hasCity = False

	# if we have a main_city, try to shift it away from ignored locations
	shift_x =0; shift_y =0
	if ignored_set and main_city:
		# compute city half-size
		xs = [x for (x, _) in main_city.tiles.keys()]
		ys = [y for (_, y) in main_city.tiles.keys()]
		width = max(xs) - min(xs) + 1
		height = max(ys) - min(ys) + 1
		half_size = max(width, height) // 2
		# buffer to ensure clearance
		buffer = random.randint(5, 10)
		max_shift = (half_size * 2) + buffer
		shift_loc = _find_translation_away(main_city, ignored_set, origin, max_shift, buffer = buffer)
		#print (f'Computed max_shift={max_shift} for city width={width}, height={height}, half_size={half_size}, buffer={buffer}.')
		#input(f'shift_loc={shift_loc}')
		if shift_loc is None:
			main_city = None
			center = origin
			hasCity = False
		else:
			shift_x, shift_y = shift_loc

	# translate the in-memory city and update origin if needed
	shifted_location = center
	#print (f'shifted_location before shift: {shifted_location}')
	if main_city:
		shifted_location = (origin[0] + shift_x, origin[1] + shift_y)
		
		translate_city(main_city, shifted_location)
		#input(f"Shifted location to {shifted_location} using shift ({shift_x},{shift_y})")	
		#print (f'shifted_location after shift: {shifted_location}')
	
	city_name = None
	if hasCity:
		city_name = player_game.get_available_city_type_for_region(region_settings['region_name'])
		if not city_name:
			# no available cities left; skip creating a new city
			main_city = None
			center = origin
			shifted_location = origin
			hasCity = False
	#print (f'Building region around main_city at shifted_location: {shifted_location}, hasCity={hasCity}')

	region_city = build_region_around(main_city, region_settings, origin, shifted_location, player_game, ignored_locations=ignored_set) 

	if hasCity:		
		attr = f"{city_name.upper()}_REGION_SETTINGS"
		city_settings = getattr(const, attr)

		locations= main_city.tiles.keys()
		main_city = create_region_city(city_settings)

		attr_region_city = f"{region_city.region_name.upper()}_{city_name.upper()}_CITY_NAME"
		attr_region_city_description = f"{region_city.region_name.upper()}_{city_name.upper()}_CITY_DESCRIPTION"
		city_display_name = getattr(const, attr_region_city)
		city_description = getattr(const, attr_region_city_description)
		main_city.display_name = city_display_name
		main_city.description = city_description
		main_city.parent_region_name = region_city.region_name
		
		main_city.ensure_required_buildings(player_game,locations)	
		for x, y in locations:
			if not (x,y) in main_city.tiles.keys():  #self.tiles: Dict[Tuple[int, int], Tile] = {}
				main_city.create_tile(player_game, x, y)
		main_city.populate_tiles(player_game)

	# finalize
	if not region_city.tiles:
		region_city.child_city = None
	else:
		if main_city is not None:
			main_city.parent_region_city_id = region_city.region_city_id
			main_city.parent_region_name = region_city.region_name
		region_city.child_city = main_city

	#DEBUGGGGGGGG
	# print merged map (main city takes precedence over region)
	def print_merged_map(main_city: City, region_city: City, center: Tuple[int,int], radius: int =30):
		# compute bounds from union of both city tile sets
		all_keys = set(main_city.tiles.keys()) | set(region_city.tiles.keys())
		if all_keys:
			xs = [x for (x, _) in all_keys]
			ys = [y for (_, y) in all_keys]
			minx, maxx = min(xs), max(xs)
			miny, maxy = min(ys), max(ys)
		else:
			minx = center[0] - radius
			maxx = center[0] + radius
			miny = center[1] - radius
			maxy = center[1] + radius
		# make square bounds with padding
		width = maxx - minx +1
		height = maxy - miny +1
		size = max(width, height) +2
		start_x = minx -1
		start_y = miny -1
		end_x = start_x + size -1
		end_y = start_y + size - 1
		out_lines: List[str] = []
		for y in range(start_y, end_y +1):
			row = []
			for x in range(start_x, end_x +1):
				# main city takes precedence
				ty = main_city.tiles.get((x, y))
				if ty is None:
					ty = region_city.tiles.get((x, y))
				t = ty
				if t is None:
					row.append('?')
				elif t.type == ROAD:
					row.append('=')
				elif t.type == BUILDING:
					ch = t.building.get('char') if isinstance(t.building, dict) else 'B'
					row.append(ch if ch else 'B')
				elif t.type == 'open_area':
					row.append(' ')
				elif t.type == 'impassable':
					row.append('¤')
				elif t.type == ALLEY:
					row.append('"')
				else:
					row.append(' ')
			out_lines.append(''.join(row))
		print('\n'.join(out_lines))
	#print_merged_map(main_city, region_city, origin, radius=30)

	return region_city

def find_start_point_for_neighboring_region(main_city: City) -> Tuple[int,int]:
	# need to determine an edge of main_city to use as an origin for neighboring region
	# pick a perimeter tile farthest from main_city center to be a starting origin
	start_location = None
	xs = [x for (x, _) in main_city.tiles.keys()]
	ys = [y for (_, y) in main_city.tiles.keys()]
	if xs and ys:
		minx, maxx = min(xs), max(xs)
		miny, maxy = min(ys), max(ys)
		center_x = (minx + maxx)//2
		center_y = (miny + maxy)//2
		# find perimeter candidates and pick one at max distance from center
		perimeter = []
		for (x, y) in main_city.tiles.keys():
			for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
				n = (x+dx, y+dy)
				if n not in main_city.tiles:
					perimeter.append((x,y))
					break
		if perimeter:
			# choose tile that maximizes distance from center, then step one outward
			px, py = max(perimeter, key=lambda p: abs(p[0]-center_x)+abs(p[1]-center_y))
			# step outward from center to be outside main_city
			sx = px + _sgn(px - center_x)
			sy = py + _sgn(py - center_y)
			start_location = (sx, sy)
	if start_location is None:
		start_location = (0,0)
	return start_location
##################################

def get_all_region_tiles(main_city: City):
	ignored_tiles = set()
	if main_city:
		ignored_tiles.update(main_city.tiles.keys())
	if main_city.child_city:
		ignored_tiles.update(main_city.child_city.tiles.keys())
	return ignored_tiles



				
########################### UI FUNCTIONS FOR TESTING ###########################	
def print_all_regions(cities: List[City], center: Tuple[int, int] = (0,0), radius: int =30):
	"""Render all provided regions and their child_cities together.

	- Merges tiles from each City and its child_city (if present).
	- Computes bounding box from all tiles and prints a square map with a one-tile
	'?' border framing the output (outermost row/col are forced to '?'). 
	- Precedence: later cities in the list overwrite earlier ones; parent city
	tiles overwrite its child_city tiles.
	"""
	# collect all tiles into merged map with source index. We'll add child_city first
	# then parent so parent overwrites child. Cities later in list overwrite earlier.
	# merged maps position -> (tile, region_index)
	merged = {}
	for idx, city in enumerate(cities):
		if city is None:
			continue
		# child_city first (associate with parent's index)
		if city.child_city:
			for k, t in city.child_city.tiles.items():
				merged[k] = (t, idx)
		# then parent city (overwrites child)
		for k, t in city.tiles.items():
			merged[k] = (t, idx)

	if merged:
		xs = [x for (x, _) in merged.keys()]
		ys = [y for (_, y) in merged.keys()]
		minx, maxx = min(xs), max(xs)
		miny, maxy = min(ys), max(ys)
	else:
		minx = center[0] - radius
		maxx = center[0] + radius
		miny = center[1] - radius
		maxy = center[1] + radius

	# make square bounds with padding of1 (so we can draw a framing border)
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
			# force framing border on the outermost cells
			if x == start_x or x == end_x or y == start_y or y == end_y:
				row.append('?')
				continue
			cell = merged.get((x, y))
			if cell is None:
				row.append('?')
				continue
			t, src_idx = cell
			if t.type == ROAD:
				row.append('=')
			elif t.type == BUILDING:
				ch = t.building.get('char') if isinstance(t.building, dict) else 'B'
				row.append(ch if ch else 'B')
			elif t.type == 'open_area':
				# render region index as character:0-9 then A-Z for indices >=10
				if src_idx <10:
					row.append(str(src_idx))
				else:
					row.append(chr(ord('A') + ((src_idx -10) %26)))
			elif t.type == 'impassable':
				row.append('¤')
			elif t.type == ALLEY:
				row.append('"')
			else:
				row.append(' ')
		out_lines.append(''.join(row))
	print('\n'.join(out_lines))

def print_player_game(player_game):
	"""
	Render the entire PlayerGame world map from player_game.world_tiles.
	This prints a character grid similar to print_all_regions but uses
	player_game.get_region_and_active_area_for_position to determine
	open-area/impassable chars.
	"""
	# helper to pick a tile from the world map
	def _pick_tile(x: int, y: int):
		
		return player_game.world_tiles.get((x, y))
		

	# simple connector for road/alley rendering
	def get_road_or_alley_char(t, left_t, up_t, right_t, down_t):
		# consider neighbor a connector if it's a road or alley
		def is_connector(n):
			return n is not None and (getattr(n, 'type', None) in (ROAD, ALLEY))
		h = is_connector(left_t) or is_connector(right_t)
		v = is_connector(up_t) or is_connector(down_t)
		# roads get a clearer connective glyph
		if getattr(t, 'type', None) == ROAD:
			if h and not v:
				return '-'
			if v and not h:
				return '|'
			if h and v:
				return '+'
			return '='
		# alley: use a light quote glyph for atmosphere, but show connectors if obvious
		if getattr(t, 'type', None) == ALLEY:
			if h and not v:
				return ','
			if v and not h:
				return ':'
			if h and v:
				return ';'
			return '"'
		# fallback
		return '?'

	# determine bounds from world_tiles
	wt = getattr(player_game, 'world_tiles', None) or {}
	if wt:
		xs = [x for (x, _) in wt.keys()]
		ys = [y for (_, y) in wt.keys()]
		minx, maxx = min(xs), max(xs)
		miny, maxy = min(ys), max(ys)
	else:
		# nothing to render
		print('(no world tiles)')
		return

	# make square-ish bounds with small padding
	width = maxx - minx +1
	height = maxy - miny +1
	size = max(width, height)
	start_x = minx
	start_y = miny
	end_x = start_x + size -1
	end_y = start_y + size -1

	out_lines: List[str] = []
	for y in range(start_y, end_y +1):
		row = []
		for x in range(start_x, end_x +1):
			t = _pick_tile(x, y)
			if t is None:
				row.append('?')
			else:
				ttype = getattr(t, 'type', None)
				if ttype == ROAD:
					left_t = _pick_tile(x-1, y)
					up_t = _pick_tile(x, y-1)
					right_t = _pick_tile(x+1, y)
					down_t = _pick_tile(x, y+1)
					row.append(get_road_or_alley_char(t, left_t, up_t, right_t, down_t))
				elif ttype == BUILDING:
					ch = None
					
					ch = t.building.get('char') if isinstance(t.building, dict) else (getattr(t.building, 'char', None) if t.building is not None else None)
					
					row.append(ch if ch else 'B')
				elif ttype == 'open_area':
					# determine which region/city this open tile belongs to
					_, active = player_game.get_region_and_active_area_for_position((x, y))
					type_name = active.city_name if (active and getattr(active, 'city_name', None) is not None) else (active.region_name if active else None)
					if type_name:
						attr = f"{type_name.upper()}_OPEN_AREA_CHAR"
						#input (f'Getting open area char for type_name={type_name}, attr={attr}')
						open_char = getattr(const, attr, None)
						row.append(open_char if open_char else ' ')
					else:
						row.append(' ')
				elif ttype == 'impassable':
					_, active = player_game.get_region_and_active_area_for_position((x, y))
					type_name = active.city_name if (active and getattr(active, 'city_name', None) is not None) else (active.region_name if active else None)
					if type_name:
						attr = f"{type_name.upper()}_IMPASSABLE_CHAR"
						#input (f'Getting impassable char for type_name={type_name}, attr={attr}')
						open_char = getattr(const, attr, None)
						row.append(open_char if open_char else '¤')
					else:
						row.append('¤')
				elif ttype == ALLEY:
					left_t = _pick_tile(x-1, y)
					up_t = _pick_tile(x, y-1)
					right_t = _pick_tile(x+1, y)
					down_t = _pick_tile(x, y+1)
					row.append(get_road_or_alley_char(t, left_t, up_t, right_t, down_t))
				else:
					# fallback to region open-area char if available
					_, active = player_game.get_region_and_active_area_for_position((x, y))
					if active:
						name = active.city_name if getattr(active, 'city_name', None) is not None else active.region_name
						attr = f"{name.upper()}_OPEN_AREA_CHAR"
						#input (f'Getting fallback open area char for name={name}, attr={attr}')
						open_char = getattr(const, attr, None)
						row.append(open_char if open_char else ' ')
					else:
						row.append(' ')
		out_lines.append(''.join(row))
	print('\n'.join(out_lines))

def main():
	from game.objects.player_game import PlayerGame
	arg_seed = int(sys.argv[1]) if len(sys.argv) >1 else 42
	player = Player('Player', x=0, y=0)
	
	pg = PlayerGame()
	print('Please wait - Building initial region...')
	rc = pg.create_region_at((0,0))
	
	desert_start_location = find_start_point_for_neighboring_region(rc) if rc else None	
	if desert_start_location is None:
		desert_start_location = (0,0)
		
#def build_region_map (player_game, region_settings: dict, origin: Tuple[int,int], hasCity: bool = False, ignored_locations: Tuple[int, int] = None):
	desert = build_region_map (pg, const.DESERT_REGION_SETTINGS, desert_start_location, True, pg.world_tiles.keys())
	pg.merge_region(desert)
	pg.regions.append(desert)
	pg.previous_region = desert
	pg.last_region_name = desert.region_name

	# if desert.child_city:
	# 	print(f"Desert Complete: {desert.child_city.get_parent_region_name(pg)}")
	# else:
	# 	print("Desert Complete: No Child City")
	# input("Press Enter to continue...")

	#get all tiles from desert and desert city gathered as a tuple list to pass in the ignored tiles field in forest region build
	forest_start_location = find_start_point_for_neighboring_region(desert) if desert else None	
	if forest_start_location is None:
		forest_start_location = (0,0)	
	forest = build_region_map (pg, const.FOREST_REGION_SETTINGS, forest_start_location, True, pg.world_tiles.keys())
	pg.merge_region(forest)
	pg.regions.append(forest)
	pg.previous_region = forest
	pg.last_region_name = forest.region_name

	# if forest.child_city:
	# 	print(f"Forest Complete: {forest.child_city.get_parent_region_name(pg)}")
	# else:
	# 	print("Forest Complete: No Child City")
	# input("Press Enter to continue...")

	grass_start_location = find_start_point_for_neighboring_region(forest) if desert else None	
	if grass_start_location is None:
		grass_start_location = (0,0)
	grass = build_region_map (pg, const.GRASSLAND_REGION_SETTINGS, grass_start_location, True, pg.world_tiles.keys())
	pg.merge_region(grass)
	pg.regions.append(grass)
	pg.previous_region = grass
	pg.last_region_name = grass.region_name

	# if grass.child_city:
	# 	print(f"Grassland Complete: {grass.child_city.get_parent_region_name(pg)}")
	# else:
	# 	print("Grassland Complete: No Child City")
	# input("Press Enter to continue...")

	mountains_start_location = find_start_point_for_neighboring_region(grass) if grass else None	
	if mountains_start_location is None:
		mountains_start_location = (0,0)
	mountains = build_region_map (pg, const.MOUNTAINS_REGION_SETTINGS, mountains_start_location, True, pg.world_tiles.keys())
	pg.merge_region(mountains)
	pg.regions.append(mountains)
	pg.previous_region = mountains
	pg.last_region_name = mountains.region_name

	# if mountains.child_city:
	# 	print(f"Mountains Complete: {mountains.child_city.get_parent_region_name(pg)}")
	# else:
	# 	print("Mountains Complete: No Child City")
	# input("Press Enter to continue...")


	shallows_start_location = find_start_point_for_neighboring_region(mountains) if mountains else None	
	if shallows_start_location is None:
		shallows_start_location = (0,0)
	shallows = build_region_map (pg, const.SHALLOWS_REGION_SETTINGS, shallows_start_location, True, pg.world_tiles.keys())
	pg.merge_region(shallows)
	pg.regions.append(shallows)
	pg.previous_region = shallows
	pg.last_region_name = shallows.region_name

	# if shallows.child_city:
	# 	print(f"Shallows Complete: {shallows.child_city.get_parent_region_name(pg)}")
	# else:
	# 	print("Shallows Complete: No Child City")
	# input("Press Enter to continue...")


	swamp_start_location = find_start_point_for_neighboring_region(shallows) if shallows else None	
	if swamp_start_location is None:
		swamp_start_location = (0,0)
	swamp = build_region_map (pg, const.SWAMP_REGION_SETTINGS, swamp_start_location, True, pg.world_tiles.keys())
	pg.merge_region(swamp)
	pg.regions.append(swamp)
	pg.previous_region = swamp
	pg.last_region_name = swamp.region_name

	# if swamp.child_city:
	# 	print(f"Swamp Complete: {swamp.child_city.get_parent_region_name(pg)}")
	# else:
	# 	print("Swamp Complete: No Child City")
	# input("Press Enter to continue...")


	snow_start_location = find_start_point_for_neighboring_region(swamp) if swamp else None	
	if snow_start_location is None:
		snow_start_location = (0,0)
	snow = build_region_map (pg, const.SNOW_REGION_SETTINGS, snow_start_location, True, pg.world_tiles.keys())
	pg.merge_region(snow)
	pg.regions.append(snow)
	pg.previous_region = snow
	pg.last_region_name = snow.region_name

	# if snow.child_city:
	# 	print(f"Snow Complete: {snow.child_city.get_parent_region_name(pg)}")
	# else:
	# 	print("Snow Complete: No Child City")
	# input("Press Enter to continue...")

	#ignored_tiles.update(get_all_region_tiles(snow))
	#print_all_regions([rc, snow,swamp,shallows,mountains, grass, forest, desert])
	print_player_game(pg)


if __name__ == '__main__':
	main()