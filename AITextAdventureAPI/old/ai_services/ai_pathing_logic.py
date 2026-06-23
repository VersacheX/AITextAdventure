from typing import Optional, List, Tuple
from types import SimpleNamespace
from collections import deque

from game.constants import DIRECTIONAL_MAPPING
from services.player_movement_service import get_allowed_moves


def _make_node(x: int, y: int, inside: bool, z: int):
	return SimpleNamespace(x=x, y=y, inside=inside, z=z)


def _resolve_area_for_pos(player_game, x: int, y: int):
	"""Return an area object for a world position. Prefer active_area (child city) then parent_region.
	This avoids passing None into get_allowed_moves."""
	parent, active = player_game.get_region_and_active_area_for_position((x, y))
	return active or parent

_DIRS = {
	'w': (0, -1),
    's': (0,  1),
    'a': (-1, 0),
    'd': (1,  0),
}

def find_path_to(player, target_xy: Tuple[int, int], player_game, max_search: int = 5000) -> Optional[List[str]]:
	"""
    Simple unweighted 2D BFS ignoring impassable tiles.
	Returns a list of direction keys ('w','a','s','d') or None if no path found.
	"""
	start = (player.x, player.y)
	tx, ty = target_xy
	if start == (tx, ty):
		return []

	q = deque([start])
	visited = {start}
	# parent: child_pos -> (parent_pos, direction_from_parent_to_child)
	parent = {}
	iterations = 0

	while q and iterations < max_search:
		iterations += 1
		x, y = q.popleft()
		_, active_area = player_game.get_region_and_active_area_for_position((x, y))
		inside = player_game.get_tile(x, y).building is not None
		temp = _make_node(x, y, inside, 0)
		allowed_dirs = get_allowed_moves(active_area, temp, player_game)
		allowed_dir_translations = set(allowed_dirs.keys())

		for key in allowed_dir_translations:
			dx, dy = _DIRS[key]
			nx, ny = x + dx, y + dy
			npos = (nx, ny)
			if npos in visited:
				continue

			# get tile and skip impassable
			tile = player_game.get_tile(nx, ny)

			if getattr(tile, "type", None) == 'impassable':
				continue

			# record parent and enqueue
			parent[npos] = ((x, y), key)
			if npos == (tx, ty):
				# reconstruct path
				path = []
				cur = npos
				while cur != start:
					p, dir_from_p = parent[cur]
					path.append(dir_from_p)
					cur = p

				path.reverse()
				# debug: Uncomment to log path discovery
				# print(f"Path found in {iterations} iterations: {path}")
				# input("Press Enter to continue...")
				return path

			visited.add(npos)
			q.append(npos)
	print(f"No path found within {max_search} iterations.")
	return None

def find_nearest_target_by_predicate(player, player_game, predicate, max_targets: int =500) -> Optional[Tuple[Tuple[int,int], List[str]]]:#should return -> Optional[Tuple[Tuple[int,int, int], List[str]]]
	"""Scan the active area for targets satisfying `predicate` and return the
	nearest target coordinate and path to it. Predicate receives (x,y,z,info) and
	should return truthy for desired targets.
	"""
	# build list of candidate targets from active area subloc_map
	_, active_area = player_game.get_region_and_active_area_for_position((player.x, player.y))
	sl_map = getattr(active_area, 'subloc_map', {}) or {}
	candidates = []
	for loc, entries in sl_map.items():
		if not isinstance(loc, tuple) or len(loc) <3:
			continue
		x, y, z = loc[0], loc[1], loc[2]
		if not entries:
			continue
		for s in entries:
			if predicate((x, y, z, s)):
				candidates.append((x, y, z, s))
		if len(candidates) >= max_targets:
			break

	if not candidates:
		return None

	# sort candidates by manhattan distance and try to find path
	candidates.sort(key=lambda t: abs(t[0] - player.x) + abs(t[1] - player.y))
	for tx, ty, tz, info in candidates:
		path = find_path_to(player, (tx, ty), player_game)
		if path is not None:
			# if the path is not none then we have somewhere to go... 
			# we need to ensure AI.z is at 0 so they may move... prepend to the path u for up and j for down the number of times AI needs to move to get to 0
			vertical_difference = player.z - tz
			if vertical_difference > 0:
				path = ['u'] * vertical_difference + path
				print(f"Adding 'u' to ascend out of building {vertical_difference} levels")
			elif vertical_difference < 0: #legacy mapping to 'j' for down and 'u' for up
				print(f"Adding 'j' to descend out of building {vertical_difference} levels")
				path = ['j'] * abs(vertical_difference) + path

			return ( (tx, ty), path)
		#if the path is none then we are at the location now we need to determine if we are on the correct z level.
		# if we are not we append u for up or j for down based on the z difference of the player and the location
		elif (tx, ty) == (player.x, player.y):
			vertical_difference = player.z - tz
			path = []
			if vertical_difference > 0:
				path = ['u'] * vertical_difference
				print(f"Adding 'u' to ascend to loot {vertical_difference} levels")
			elif vertical_difference < 0:
				path = ['j'] * abs(vertical_difference)
				print(f"Adding 'j' to descend to loot {vertical_difference} levels")
			if path:
				return ( (tx, ty), path)
	return None



def direction_from_path(path: List[str]) -> Optional[str]:
	return path[0] if path and len(path) >0 else None
