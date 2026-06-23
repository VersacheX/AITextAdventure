"""Helpers for frontier management and selection used by region_builder.

This module extracts frontier construction and scoring logic so the
main region generator can remain readable and testable.
"""
from collections import deque
import math
import logging
from typing import Deque, Iterable, Set, Tuple, Callable, Any, Optional
import random
#from game.services.region_shape_service import make_filled_circle, make_filled_square, make_filled_hex, make_filled_diamond, make_filled_star

logger = logging.getLogger(__name__)





def randomized_frontier_perimeter_pathing(midpoint_x: int, midpoint_y: int, current_tiles: Set[Tuple[int,int]], ignored_set: Set[Tuple[int,int]], neighbor_offsets: Iterable[Tuple[int,int]], max_size: int) -> Iterable[Tuple[int,int]]:
	# expand perimeter points randomly updating perimiter points until max_size is reached
	"""EXPAND current_tiles outward from its perimeter until max_size is reached.

	This uses a randomized breadth-first expansion seeded from the current
	perimeter. It only adds tiles that are adjacent to the existing
	`current_tiles` set, which prevents creating isolated holes inside the
	expanded area.

	Returns the iterable of positions that were added (in addition order).
	"""
	# collect perimeter tiles (tiles in current_tiles that touch empty space)
	perim = list(find_perimiter_points(midpoint_x, midpoint_y, current_tiles, ignored_set, neighbor_offsets, max_size))
	if not perim:
		return []

	# seed candidate neighbors from perimeter
	seen = set()
	from collections import deque as _dq
	queue = _dq()
	for (px, py) in perim:
		for dx, dy in neighbor_offsets:
			n = (px + dx, py + dy)
			if n in ignored_set or n in current_tiles or n in seen:
				continue
			seen.add(n)
			queue.append(n)

	# randomize initial order
	tmp = list(queue)
	random.shuffle(tmp)
	queue = _dq(tmp)

	added = []
	# diagnostics
	enqueued_total = len(queue)
	skipped_adj_ignored =0
	added_total =0
	# defer counts to avoid infinite cycling for unattainable points
	defer_counts = {}
	max_defer =6

	# helper: check adjacency to current_tiles (4- or8-connected as provided)
	def _has_adjacent_in_current(pt):
		for ndx, ndy in neighbor_offsets:
			if (pt[0] + ndx, pt[1] + ndy) in current_tiles:
				return True
		return False

	while queue and len(current_tiles) < max_size:
		"""
		This method uses a randomized BFS approach:
		- dequeue a candidate point (occasionally random pick from queue to increase variance)
		- if point is invalid (in ignored or already in current), skip
		- try to add point and all its neighbors when a point is picked, to prevent single tile holes
		- if point is not adjacent to current_tiles, defer it by re-enqueuing at end (up to max_defer times)
		- when adding a point, enqueue its neighbors (shuffled order to reduce directional bias)
		"""
		# occasional random pick to increase variance
		if random.random() <0.18 and len(queue) >1:
			idx = random.randrange(len(queue))
			# rotate so desired index is at left, pop, then rotate back
			queue.rotate(-idx)
			pt = queue.popleft()
			queue.rotate(idx)
		else:
			pt = queue.popleft()
		# re-check conditions (may have changed)
		if pt in ignored_set or pt in current_tiles:
			continue
		# ensure we attach to existing area to avoid holes
		if not _has_adjacent_in_current(pt):
			# defer: push to end to possibly attach later
			# increment defer count and drop if exceeded
			c = defer_counts.get(pt,0) +1
			defer_counts[pt] = c
			if c > max_defer:
				continue
			queue.append(pt)
			# avoid infinite deferral: if queue cycles only of non-adjacent, break
			if len(queue) > (max_size *8):
				break
			continue
		current_tiles.add(pt)
		added.append(pt)
		added_total +=1
		# need to check if the position just added is adjacent to a free location and 2 spaces next to an ignored tile
		adj_check = get_is_adjacent_to_free_and_ignored(pt, current_tiles, ignored_set, neighbor_offsets)

		if adj_check is not None:
			for required_pt in adj_check:
				if required_pt in queue:
					queue.remove(required_pt)
				current_tiles.add(required_pt)
				added.append(required_pt)
				added_total +=1
					

		# enqueue neighbors of the new tile
		# shuffle neighbor ordering to reduce directional bias
		neighs = list(neighbor_offsets)
		random.shuffle(neighs)
		for dx, dy in neighs:
			nn = (pt[0] + dx, pt[1] + dy)
			if nn in ignored_set or nn in current_tiles or nn in seen:
				continue
			# skip candidates that are adjacent to ignored tiles to avoid creeping
			adj_ignored = False
			for adx, ady in neighbor_offsets:
				if (nn[0] + adx, nn[1] + ady) in ignored_set:
					adj_ignored = True
					break
			if adj_ignored:
				skipped_adj_ignored +=1
				continue
			seen.add(nn)
			queue.append(nn)

	return added

# need to check if the positionjust added is adjacent to a free location and 2 spaces next to an ignored tile
# will need position, all current tiles, ignored set, neighbor offsets
def get_is_adjacent_to_free_and_ignored(pt: Tuple[int,int], current_tiles: Set[Tuple[int,int]], ignored_set: Set[Tuple[int,int]], neighbor_offsets: Iterable[Tuple[int,int]]) -> bool:
	"""Check if `pt` is adjacent to at least one free tile and two ignored tiles.
	Used to ensure no gaps between current tiles and ignored areas.
	"""
	res = set()
	adj_free = False
	adj_ignored_count =0
	for dx, dy in neighbor_offsets:
		n = (pt[0] + dx, pt[1] + dy)
		n2 = (pt[0] + (dx*2), pt[1] + (dy*2))
		if n not in current_tiles and n not in ignored_set:
			adj_free = True
		if n2 in ignored_set:
			res.add(n)
			adj_ignored_count +=1
	return res if len(res) > 0 else None

def find_perimiter_points(midpoint_x: int, midpoint_y: int, current_tiles: Set[Tuple[int,int]], ignored_set: Set[Tuple[int,int]], neighbor_offsets: Iterable[Tuple[int,int]], max_size: int) -> Iterable[Tuple[int,int]]:
	"""Find perimeter tiles from `current_tiles`.

	Returns a list of perimeter tile coordinates sorted by distance to the midpoint
	(closest first) and limited to `max_size` entries.
	"""
	perimeter_points: Set[Tuple[int,int]] = set()
	for (x, y) in current_tiles:
		for dx, dy in neighbor_offsets:
			n = (x + dx, y + dy)
			if n in ignored_set:
				continue
			if n not in current_tiles:
				perimeter_points.add((x, y))
				break

	# sort perimeter points by distance to midpoint (closest first) and return up to max_size
	if not perimeter_points:
		return []
	sorted_perimeter = sorted(perimeter_points, key=lambda pt: math.sqrt((pt[0] - midpoint_x) ** 2 + (pt[1] - midpoint_y) ** 2))
	return sorted_perimeter[:max_size]



#################EXPIRIMENTAL #$#######################

def perimeter_driven_growth(
    current_tiles: Set[Tuple[int,int]],
    ignored_set: Set[Tuple[int,int]],
    neighbor_offsets: Iterable[Tuple[int,int]],
    max_size: int,
    shuffle_interval: int = 10
):
    """Grow region outward by repeatedly processing perimeter tiles.
    Preserves initial shape far better than BFS blob expansion.
    """

    # 1. Initial perimeter
    perimeter = list(find_perimiter_points(
        0, 0,  # midpoint irrelevant for this version
        current_tiles,
        ignored_set,
        neighbor_offsets,
        max_size
    ))

    if not perimeter:
        return []

    added = []
    iteration = 0

    while len(current_tiles) < max_size and perimeter:
        iteration += 1

        # 2. Shuffle every N iterations
        if iteration % shuffle_interval == 0:
            random.shuffle(perimeter)

        # 3. Pop first perimeter tile
        px, py = perimeter.pop(0)

        # 4. Check its 8 neighbors
        for dx, dy in neighbor_offsets:
            nx, ny = px + dx, py + dy
            n = (nx, ny)

            if n in current_tiles or n in ignored_set:
                continue

            # 5. Must be adjacent to existing tiles
            if not any((nx + ox, ny + oy) in current_tiles for ox, oy in neighbor_offsets):
                continue

            # 6. Add tile
            current_tiles.add(n)
            added.append(n)

            # 7. Apply your adjacency rule
            adj_fix = get_is_adjacent_to_free_and_ignored(
                n, current_tiles, ignored_set, neighbor_offsets
            )
            if adj_fix:
                for fx, fy in adj_fix:
                    if (fx, fy) not in current_tiles and (fx, fy) not in ignored_set:
                        current_tiles.add((fx, fy))
                        added.append((fx, fy))

            # 8. Newly added tile becomes new perimeter candidate
            perimeter.append(n)

            if len(current_tiles) >= max_size:
                break

    return added

