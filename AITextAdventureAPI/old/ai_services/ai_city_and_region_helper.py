# Utilities for AI to navigate city/region tiles and sublocations
from typing import Any, Tuple, List, Optional, Callable, Dict
from collections import deque

from game.objects.city import City, Tile
from game.objects.player_game import PlayerGame
from game import constants as const
from game.constants import ROAD, ALLEY, BUILDING

def find_nearest_shop(x: int, y: int, player_game: PlayerGame, shop_type: str):
	""" Find nearest shop of given type to (x,y) in player_game's world tiles.
	return position and active region
	"""
	nearest_pos: Optional[Tuple[int, int]] = None
	nearest_region: Optional[City] = None
	min_distance = float('inf')
	current_pos = (x,y)
	x_move = 1
	y_move = 0
	steps_in_current_direction = 1
	direction_changes = 0
	for layer in range(1, 100):  # Limit search to 100 layers
		for _ in range(2):  # Two sides per layer
			for _ in range(steps_in_current_direction):
				# Check current position
				tile = player_game.world_tiles.get(current_pos)    
				if tile and tile.building:
					bname = tile.building.get("name") if isinstance(tile.building, dict) else None
					if bname and ((shop_type is not None and bname == shop_type) or (shop_type is None and bname.startswith("shop"))):
						#print(f"Found shop at {current_pos}")
						distance = abs(current_pos[0] - x) + abs(current_pos[1] - y)
						if distance < min_distance:
							min_distance = distance
							nearest_pos = current_pos
							# Find the region for this position
							_, nearest_region = player_game.get_region_and_active_area_for_position(current_pos)
				# Move to next position
				current_pos = (current_pos[0] + x_move, current_pos[1] + y_move)
			# Change direction
			x_move, y_move = -y_move, x_move
			direction_changes += 1
			if direction_changes % 2 == 0:
				steps_in_current_direction += 1
	return nearest_pos, nearest_region




def get_tile(area: City, x: int, y: int, player_game: Any = None, create: bool = False) -> Optional[Tile]
	"""Return a Tile from `area` at (x,y).

	- If `create` is True, uses area's `get_or_create_tile` which may create/generate the tile.
	- Otherwise returns existing tile or None (no generation side-effects).
	"""
	if area is None:
		return None
	if create:
		return area.get_or_create_tile(x, y, player_game)
	# non-creating accessor
	return area.get_tile(x, y)

def is_walkable(tile: Optional[Tile]) -> bool:
	"""Return True if tile is walkable for pathfinding (not impassable or None)."""
	if tile is None:
		return False
	if getattr(tile, 'type', None) == 'impassable':
		return False
	# treat open_area, road, alley, building as walkable for AI navigation
	return True

def get_walkable_neighbors(area: City, x: int, y: int, player_game: Any = None, create: bool = False) -> List[Tuple[int, int]]:
	"""Return list of (nx, ny) neighbors (N,E,S,W) that are walkable.

	If `create` is True neighbors will be created/generated when missing.
	"""
	res: List[Tuple[int, int]] = []
	for dx, dy in ((0, -1), (1,0), (0,1), (-1,0)):
		nx, ny = x + dx, y + dy
		nt = get_tile(area, nx, ny, player_game=player_game, create=create)
		if is_walkable(nt):
			res.append((nx, ny))
	return res

def find_sublocations_at(area: City, x: int, y: int, floor: int =0, player: Any = None, player_game: Any = None) -> List[Dict]:
	"""Return list of sublocation dicts for (x,y,floor).

	Do NOT create tiles or generate sublocations here. This helper only reads
	the existing `subloc_map` produced during region/tile generation.
	"""
	if area is None:
		return []
	# Return whatever sublocations were produced at generation time; do not call
	# any generation APIs from AI helpers.
	return area.subloc_map.get((x, y, floor), [])

def list_sublocations_in_radius(area: City, x: int, y: int, floor: int =0, radius: int =5, player: Any = None, player_game: Any = None) -> List[Tuple[int, int, int, Dict]]:
	"""Collect sublocations within Manhattan radius around (x,y).

	Returns list of (sx, sy, floor, subloc_dict).
	"""
	out: List[Tuple[int, int, int, Dict]] = []
	for dy in range(-radius, radius +1):
		for dx in range(-radius, radius +1):
			if abs(dx) + abs(dy) > radius:
				continue
			sx, sy = x + dx, y + dy
			for f in range(-1,3):
				items = area.subloc_map.get((sx, sy, f), [])
				for it in items:
					out.append((sx, sy, f, it))
	return out

def find_nearest_sublocation(area: City, x: int, y: int, predicate: Optional[Callable[[Dict], bool]] = None, max_dist: int =50, player: Any = None, player_game: Any = None) -> Optional[Tuple[int, int, int, Dict]]:
	"""BFS to find nearest sublocation matching predicate. Returns (x,y,floor,subloc) or None."""
	if area is None:
		return None
	visited = set()
	q = deque()
	q.append((x, y,0,0)) # sx, sy, floor(0), dist
	visited.add((x, y))
	while q:
		sx, sy, f, dist = q.popleft()
		items = []
		# check a few floors: basement(-1), ground(0),1,2
		for ff in (-1,0,1,2):
			items.extend(area.subloc_map.get((sx, sy, ff), []))
		for it in items:
			if predicate is None or predicate(it):
				return (sx, sy, f, it)
		if dist >= max_dist:
			continue
		for nx, ny in ((sx, sy -1), (sx +1, sy), (sx, sy +1), (sx -1, sy)):
			if (nx, ny) in visited:
				continue
			# Do not create tiles during AI pathing; only consider existing tiles.
			nt = get_tile(area, nx, ny, player_game=player_game, create=False)
			if not is_walkable(nt):
				continue
			visited.add((nx, ny))
			q.append((nx, ny,0, dist +1))
	return None

def shortest_path(area: City, start: Tuple[int, int], goal: Tuple[int, int], player_game: Any = None, max_depth: int =1000) -> Optional[List[Tuple[int, int]]]:
	"""BFS shortest path from start to goal over walkable tiles. Returns list of coords or None."""
	if area is None:
		return None
	if start == goal:
		return [start]
	visited = set()
	q = deque()
	q.append(start)
	came_from: Dict[Tuple[int, int], Optional[Tuple[int, int]]] = {start: None}
	visited.add(start)
	depth =0
	while q and depth <= max_depth:
		for _ in range(len(q)):
			cur = q.popleft()
			if cur == goal:
				# reconstruct
				path = []
				node = cur
				while node is not None:
					path.append(node)
					node = came_from.get(node)
				return list(reversed(path))
			x, y = cur
			for nx, ny in ((x, y -1), (x +1, y), (x, y +1), (x -1, y)):
				if (nx, ny) in visited:
					continue
				# Never create tiles here; pathing should operate on existing world map only.
				nt = get_tile(area, nx, ny, player_game=player_game, create=False)
				if not is_walkable(nt):
					continue
				visited.add((nx, ny))
				came_from[(nx, ny)] = cur
				q.append((nx, ny))
		depth +=1
	return None
