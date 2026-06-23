"""
Continent detection / spreading and ocean-rect builder.

Modified to:
 - Preserve the continent that contains the player's start location (do not move it).
 - Assign city-containing regions into continents with explicit per-continent city counts:
     [5, 3, 6, 2, 4, 1] (total 21).
   Assignment is sequential using the creation order in `player_game.regions`, rotated so
   the player's starting region is first. Cities on each continent are kept sequential.
 - Assign remaining (citiless) regions to the nearest continent after city assignment.
 - Spread continents but skip moving the first continent.
"""
from typing import List, Tuple, Dict, Set, Optional
import math
import random

from game.objects.city import City, Tile
from game.objects.player_game import PlayerGame
import game.constants as const
from game.services.city_builder_service import translate_city

# A small helper to compute bbox and center for a set of tiles
def bbox_and_center_from_tiles(tiles: Set[Tuple[int,int]]) -> Tuple[Tuple[int,int,int,int], Tuple[float,float]]:
    xs = [x for (x,y) in tiles]
    ys = [y for (x,y) in tiles]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    cx = (min_x + max_x) / 2.0
    cy = (min_y + max_y) / 2.0
    return (min_x, max_x, min_y, max_y), (cx, cy)

def collect_region_tiles(region: City) -> Set[Tuple[int,int]]:
    return set(region.tiles.keys())

# ------------------------------------------------------------------
# City-centric continent assignment utilities
# ------------------------------------------------------------------
def find_region_for_player(player_game: PlayerGame) -> Optional[City]:
    """Return the region (parent region) that contains the player's current coords (pg.x, pg.y),
    or fallback to the first region in player_game.regions."""
    region, _ = player_game.get_region_and_active_area_for_position((player_game.x, player_game.y))
    if region:
        return region
    return player_game.regions[0] if player_game.regions else None

def ordered_city_regions(player_game: PlayerGame, start_region: Optional[City]) -> List[City]:
    """Return list of regions that have child_city in the order they appear in player_game.regions,
    rotated so first element is `start_region` if present."""
    city_regions = [r for r in player_game.regions if r and r.child_city is not None]
    if not city_regions:
        return []
    if not start_region:
        return city_regions
    # find start_region among city_regions (by identity/region_city_id)
    start_idx = next((i for i, r in enumerate(city_regions) if r.region_city_id == getattr(start_region, 'region_city_id', None)), None)
    if start_idx is None:
        # try matching by containment of player coords into region tiles
        start_idx = next((i for i, r in enumerate(city_regions) if (player_game.x, player_game.y) in r.tiles), None)
    if start_idx is None:
        return city_regions
    # rotate
    return city_regions[start_idx:] + city_regions[:start_idx]

def assign_city_regions_to_continents(player_game: PlayerGame, continent_city_counts: List[int]) -> List[List[City]]:
    """Partition city-bearing regions into continents according to continent_city_counts sequentially.

    Returns continents list of lists (initially containing only the city-bearing regions).
    """
    start_region = find_region_for_player(player_game)
    city_regions = ordered_city_regions(player_game, start_region)
    continents: List[List[City]] = []
    idx = 0
    for count in continent_city_counts:
        group = city_regions[idx: idx + count]
        continents.append(group)
        idx += count
        if idx >= len(city_regions):
            # remaining continents empty
            break
    # ensure we have entry for every requested continent count
    while len(continents) < len(continent_city_counts):
        continents.append([])
    return continents

def continent_center_from_regions(regions: List[City]) -> Tuple[float,float]:
    """Compute combined centroid for given regions (including child cities)."""
    tiles = set()
    for r in regions:
        tiles.update(collect_region_tiles(r))
        if getattr(r, 'child_city', None):
            tiles.update(collect_region_tiles(r.child_city))
    if not tiles:
        return (0.0, 0.0)
    _, center = bbox_and_center_from_tiles(tiles)
    return center

def assign_citiless_regions_to_continents(player_game: PlayerGame, continents: List[List[City]]) -> None:
    """Assign regions without child_city to the nearest continent (in-place mutate continents)."""
    citiless = [r for r in player_game.regions if r and r.child_city is None]
    # precompute continent centers
    centers = [continent_center_from_regions(cont) for cont in continents]
    for region in citiless:
        # region center
        _, rc = bbox_and_center_from_tiles(set(region.tiles.keys()))
        # find nearest non-empty continent center; if all centers are (0,0), pick first
        best = min(range(len(centers)), key=lambda i: (rc[0] - centers[i][0])**2 + (rc[1] - centers[i][1])**2)
        continents[best].append(region)
        # update center for that continent for subsequent assignments
        centers[best] = continent_center_from_regions(continents[best])

# ------------------------------------------------------------------
# Translation and spread (modified to allow skipping first continent)
# ------------------------------------------------------------------
def translate_region_tiles(region: City, dx: int, dy: int, player_game: PlayerGame) -> None:
    """Translate region City tiles in-place by (dx,dy)."""
    if not region or not region.tiles:
        return
    new_tiles: Dict[Tuple[int,int], Tile] = {}
    for (x,y), t in list(region.tiles.items()):
        t.x = x + dx
        t.y = y + dy
        translate_entities_at_location(x, y, dx, dy, player_game)  # translate any entities at this tile
        new_tiles[(x+dx, y+dy)] = t
    region.tiles = new_tiles
    # child_city if present
    if getattr(region, 'child_city', None):
        child = region.child_city
        new_child_tiles: Dict[Tuple[int,int], Tile] = {}
        for (x,y), t in list(child.tiles.items()):
            t.x = x + dx
            t.y = y + dy
            translate_entities_at_location(x, y, dx, dy, player_game)  # translate any entities at this tile
            new_child_tiles[(x+dx, y+dy)] = t
        child.tiles = new_child_tiles

def translate_entities_at_location(x: int, y: int, dx: int, dy: int, player_game: PlayerGame) -> None:
    """Translate any entities (NPCs, dungeons) at the given world (x,y) by (dx,dy).

    Notes:
    - `Dungeon.position` is (x,y)
    - `NPC.position` is typically (x,y,z) but we handle a legacy 2-tuple too.
    - This function may be called many times during a region translation pass, so
      we guard against moving the same entity more than once per pass.
    """
    if player_game is None:
        return

    # Guard: prevent moving the same entity multiple times during one translation pass.
    # Stored on PlayerGame dynamically to avoid changing its class.
    moved = getattr(player_game, "_continent_translate_moved_entities", None)
    if moved is None:
        moved = set()
        setattr(player_game, "_continent_translate_moved_entities", moved)

    # ---- Dungeons ----
    dungeons = player_game.dungeons
    if dungeons:
        for d in dungeons:
            pos = d.position
            if not pos:
                continue
            # Dungeon position is (x,y)
            if len(pos) == 2 and pos[0] == x and pos[1] == y:
                key = ("dungeon", d.id)
                if key in moved:
                    continue
                d.position = (pos[0] + dx, pos[1] + dy)
                moved.add(key)

    # ---- NPCs ----
    npcs = player_game.npcs
    if npcs:
        for npc in npcs:
            pos = npc.position
            if not pos:
                continue

            # NPC position should be (x,y,z). Handle legacy (x,y).
            if len(pos) == 2 and pos[0] == x and pos[1] == y:
                key = ("npc", npc.id)
                if key in moved:
                    continue

                npc.position = (pos[0] + dx, pos[1] + dy)
                #print (f"Translated NPC {npc.name} (id={npc.id}) from ({pos[0]},{pos[1]}) to ({npc.position[0]},{npc.position[1]})")
                moved.add(key)

    # ---- Aircraft (optional but consistent with "entity at location") ----
    aircraft_loc = player_game.aircraft_location
    if aircraft_loc and len(aircraft_loc) == 2 and aircraft_loc[0] == x and aircraft_loc[1] == y:
        key = ("aircraft", "aircraft_location")
        if key not in moved:
            player_game.aircraft_location = (aircraft_loc[0] + dx, aircraft_loc[1] + dy)
            moved.add(key)

def update_player_game_world_tiles_after_translation(player_game: PlayerGame) -> None:
    """Rebuild player_game.world_tiles from player_game.regions.

    This is robust: after translations, remerge all region tiles into world_tiles.
    """
    player_game.world_tiles.clear()
    for region in player_game.regions:
        for (x,y), t in region.tiles.items():
            player_game.world_tiles[(x,y)] = t
        if getattr(region, 'child_city', None):
            for (x,y), t in region.child_city.tiles.items():
                player_game.world_tiles[(x,y)] = t

def spread_continents_radial(player_game: PlayerGame, continents: List[List[City]], rng: random.Random, radius: int = 80, skip_first: bool = True) -> None:
    """Place continent clusters on distinct radial angles around world center.

    If skip_first is True the first continent (index 0) will not be moved.
    """
    all_tiles = set(player_game.world_tiles.keys()) if player_game.world_tiles else set()
    if not all_tiles:
        world_center = (0.0, 0.0)
    else:
        _, world_center = bbox_and_center_from_tiles(all_tiles)

    cont_centers = [continent_center_from_regions(cont) for cont in continents]

    # NEW: pick a safe radius based on continent extents + padding
    extents = [continent_extent_radius(cont) for cont in continents]
    max_extent = max(extents) if extents else 0.0
    padding = 25.0
    min_safe_radius = int(math.ceil((2.0 * max_extent) + padding))
    radius = max(int(radius), min_safe_radius)

    angle_step = 2 * math.pi / max(1, len(continents))
    base_angle = rng.random() * 2 * math.pi

    for i, cont in enumerate(continents):
        if not cont:
            continue
        if skip_first and i == 0:
            continue

        cur_center = cont_centers[i]
        angle = base_angle + i * angle_step
        target_cx = world_center[0] + math.cos(angle) * radius
        target_cy = world_center[1] + math.sin(angle) * radius
        dx = int(round(target_cx - cur_center[0]))
        dy = int(round(target_cy - cur_center[1]))

        for r in cont:
            translate_region_tiles(r, dx, dy, player_game)

    if hasattr(player_game, "_continent_translate_moved_entities"):
        #print (f'total npc + dungeon + aircraft = {len(player_game.dungeons) + len(player_game.npcs) + (1 if player_game.aircraft_location else 0)} entities moved during continent translation')
        #input (f"total unique entities moved during continent translation: {len(getattr(player_game, '_continent_translate_moved_entities', set()))} (enter to continue and clear tracking)")
        delattr(player_game, "_continent_translate_moved_entities")

    update_player_game_world_tiles_after_translation(player_game)

# ------------------------------------------------------------------
# Ocean builder (unchanged other than minor clarity)
# ------------------------------------------------------------------
def build_ocean_region_from_bbox(player_game: PlayerGame, bbox: Tuple[int,int,int,int], seed: Optional[int] = None) -> City:
    """Create a rectangular 'ocean' region using SHALLOWS_REGION_SETTINGS (shallow water).

    The created City is merged into player_game via merge_region and appended to regions.
    Returns the created region City.
    """
    min_x, max_x, min_y, max_y = bbox
    seed = seed if seed is not None else random.SystemRandom().randint(0, 2**31 -1)
    region_city = City(seed)
    # reuse shallows settings so rendering/tiles use same open-area char for now
    region_city.region_name = 'shallows'  # TODO: replace with 'ocean' and dedicated constants later
    region_city.display_name = 'Ocean'
    # create water/impassable tiles for every cell in bbox, but DO NOT overwrite existing world tiles
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) in player_game.world_tiles:
                continue
            region_city.tiles[(x, y)] = Tile(x, y, 'impassable')
    # merge and append
    player_game.merge_region(region_city)
    player_game.regions.append(region_city)
    return region_city

# ------------------------------------------------------------------
# Top-level: build continents and ocean with new rules
# ------------------------------------------------------------------
def build_continents_and_ocean(player_game: PlayerGame,
                               num_continents: int = 6,
                               rng_seed: int = 123456,
                               spread_radius: int = 140,
                               ocean_padding: int = 10) -> Dict[str, any]:
    """High-level procedure adapted to user rules:
      - Explicit city counts per continent: [5,3,6,2,4,1] (sum=21)
      - First continent is where the player starts and is not moved.
      - City-bearing regions assigned sequentially and partitioned accordingly (city order preserved).
      - Citiless regions assigned to nearest continent.
      - Spread continents but skip the first.
    Returns a dictionary with info (continent groups, ocean bbox, ocean_region)
    """
    rng = random.Random(rng_seed)

    # explicit city counts requested by user
    requested_counts = const.CONTINENT_COMPOSITION


    if num_continents != len(requested_counts):
        # if caller passed different num_continents, adjust counts proportionally or truncate/extend.
        # For now, prefer requested_counts and ignore num_continents parameter.
        num_continents = len(requested_counts)

    # 1) assign city-bearing regions into continents sequentially, rotated so player's region is first
    continents: List[List[City]] = assign_city_regions_to_continents(player_game, requested_counts)

    # 2) assign citiless regions to nearest continent
    assign_citiless_regions_to_continents(player_game, continents)

    # 3) compute continent bboxes for return metadata (before spread)
    continent_bboxes = []
    for cont in continents:
        tiles = set()
        for r in cont:
            tiles.update(collect_region_tiles(r))
            if r.child_city:
                tiles.update(collect_region_tiles(r.child_city))
        if tiles:
            continent_bboxes.append(bbox_and_center_from_tiles(tiles)[0])
        else:
            continent_bboxes.append((0,0,0,0))

    # 4) spread continents radially but skip first (player) continent
    spread_continents_radial(player_game, continents, rng, radius=spread_radius, skip_first=True)

    # 4.b) pull continents tighter if any are still too far after radial spread (but skip first continent as anchor)
    pull_continents_closer_by_tiles(
		player_game,
		continents,
		anchor_index=0,
		min_gap=30,
		max_gap=70,
		max_iters=30,
		step_cap=12,
	)

    # 5) recompute world bounds and create ocean bbox
    all_tiles = set(player_game.world_tiles.keys())
    if not all_tiles:
        return {"continents": continent_bboxes, "ocean_bbox": None, "ocean_region": None}

    xs = [x for (x,y) in all_tiles]
    ys = [y for (x,y) in all_tiles]
    min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)

    ocean_bbox = (min_x - ocean_padding, max_x + ocean_padding, min_y - ocean_padding, max_y + ocean_padding)
    ocean_region = build_ocean_region_from_bbox(player_game, ocean_bbox, seed=rng.randint(0,2**31 -1))


    #continent compositions is a list of each continent by number and the cite display names
    continent_cities = []
    for i, cont in enumerate(continents):
        city_names = [r.child_city.display_name for r in cont if r.child_city]
        continent_cities.append({"continent_number": i+1, "city_names": city_names})

    # Return continents bboxes (metadata), ocean info, composition summaries, AND the actual continent groups
    return {
        "continents": continent_bboxes,
        "ocean_bbox": ocean_bbox,
        "ocean_region": ocean_region,
        "continent_compositions": continent_cities,
        #"continent_groups": continents
    }

def continent_extent_radius(cont: List[City]) -> float:
    """Return an approximate radius for a continent based on its bbox diagonal/2."""
    tiles = set()
    for r in cont:
        tiles.update(collect_region_tiles(r))
        if getattr(r, 'child_city', None):
            tiles.update(collect_region_tiles(r.child_city))
    if not tiles:
        return 0.0
    (min_x, max_x, min_y, max_y), _ = bbox_and_center_from_tiles(tiles)
    w = (max_x - min_x) + 1
    h = (max_y - min_y) + 1
    # half-diagonal ~= radius that bounds the bbox
    return math.sqrt(w * w + h * h) / 2.0

def continent_tiles(cont: List[City]) -> Set[Tuple[int, int]]:
	tiles: Set[Tuple[int, int]] = set()
	for r in cont:
		if not r:
			continue
		tiles.update(r.tiles.keys())
		if getattr(r, "child_city", None):
			tiles.update(r.child_city.tiles.keys())
	return tiles


def boundary_tiles(tiles: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
	"""Return tiles on the perimeter (has at least one 4-neighbor missing)."""
	if not tiles:
		return set()
	out: Set[Tuple[int, int]] = set()
	for x, y in tiles:
		if ((x - 1, y) not in tiles) or ((x + 1, y) not in tiles) or ((x, y - 1) not in tiles) or ((x, y + 1) not in tiles):
			out.add((x, y))
	return out


def _spatial_hash(points: Set[Tuple[int, int]], cell_size: int) -> Dict[Tuple[int, int], List[Tuple[int, int]]]:
	grid: Dict[Tuple[int, int], List[Tuple[int, int]]] = {}
	if cell_size <= 0:
		cell_size = 1
	for x, y in points:
		key = (x // cell_size, y // cell_size)
		grid.setdefault(key, []).append((x, y))
	return grid


def _bbox_from_tiles(tiles: Set[Tuple[int, int]]) -> Optional[Tuple[int, int, int, int]]:
	if not tiles:
		return None
	xs = [x for x, _ in tiles]
	ys = [y for _, y in tiles]
	return (min(xs), max(xs), min(ys), max(ys))


def _bbox_gap(a: Tuple[int, int, int, int], b: Tuple[int, int, int, int]) -> float:
	"""Minimum Euclidean distance between two axis-aligned bboxes (0 if overlap/touch)."""
	a_min_x, a_max_x, a_min_y, a_max_y = a
	b_min_x, b_max_x, b_min_y, b_max_y = b

	if a_max_x < b_min_x:
		dx = b_min_x - a_max_x
	elif b_max_x < a_min_x:
		dx = a_min_x - b_max_x
	else:
		dx = 0

	if a_max_y < b_min_y:
		dy = b_min_y - a_max_y
	elif b_max_y < a_min_y:
		dy = a_min_y - b_max_y
	else:
		dy = 0

	return math.sqrt(dx * dx + dy * dy)


def min_distance_between_tile_sets(a: Set[Tuple[int, int]], b: Set[Tuple[int, int]], *, search_radius_cells: int = 2) -> float:
	"""
	Min Euclidean distance between two point sets using a spatial hash.
	If neighbor search finds nothing (too far apart), fall back to bbox distance
	so we always return a finite value.
	"""
	if not a or not b:
		return float("inf")

	cell_size = 16
	b_grid = _spatial_hash(b, cell_size)

	best_sq = None

	for ax, ay in a:
		cx, cy = (ax // cell_size, ay // cell_size)

		for gx in range(cx - search_radius_cells, cx + search_radius_cells + 1):
			for gy in range(cy - search_radius_cells, cy + search_radius_cells + 1):
				pts = b_grid.get((gx, gy))
				if not pts:
					continue
				for bx, by in pts:
					dx = ax - bx
					dy = ay - by
					ds = (dx * dx) + (dy * dy)
					if best_sq is None or ds < best_sq:
						best_sq = ds
						if best_sq == 0:
							return 0.0

	# If nothing was close enough to be found via local cell search, fall back to bbox gap.
	if best_sq is None:
		a_bb = _bbox_from_tiles(a)
		b_bb = _bbox_from_tiles(b)
		if a_bb is None or b_bb is None:
			return float("inf")
		return _bbox_gap(a_bb, b_bb)

	return math.sqrt(best_sq)


def pull_continents_closer_by_tiles(
	player_game: PlayerGame,
	continents: List[List[City]],
	*,
	anchor_index: int = 0,
	min_gap: int = 30,
	max_gap: int = 70,
	max_iters: int = 30,
	step_cap: int = 12,
) -> None:
	"""
	Pull each continent toward the anchor so the closest boundary-tile distance
	ends up <= max_gap (and not forced below min_gap).

	This only tightens; it won't push continents apart.
	"""
	if not continents or anchor_index < 0 or anchor_index >= len(continents):
		return

	anchor_cont = continents[anchor_index]
	if not anchor_cont:
		return

	# Precompute anchor boundary once per outer iteration (it changes only if anchor moves; it doesn't)
	anchor_all = continent_tiles(anchor_cont)
	anchor_boundary = boundary_tiles(anchor_all)

	for _ in range(max_iters):
		moved_any = False

		# anchor boundary stays constant since anchor isn't moved
		for i, cont in enumerate(continents):
			if i == anchor_index or not cont:
				continue

			cont_all = continent_tiles(cont)
			cont_boundary = boundary_tiles(cont_all)
			if not cont_boundary:
				continue

			gap = min_distance_between_tile_sets(anchor_boundary, cont_boundary, search_radius_cells=3)

			if not math.isfinite(gap):
				continue

			if gap <= max_gap:
				continue

			# Pull toward anchor center
			ax, ay = continent_center_from_regions(anchor_cont)
			cx, cy = continent_center_from_regions(cont)

			vx = ax - cx
			vy = ay - cy
			vlen = math.sqrt(vx * vx + vy * vy)
			if vlen <= 0.0001:
				continue

			# distance to reduce: bring gap down near middle of [min_gap, max_gap]
			target = (min_gap + max_gap) / 2.0
			need = max(0.0, gap - target)

			# cap per-iteration movement to avoid overshoot / jitter
			move = int(min(step_cap, max(1, round(need))))
			dx = int(round((vx / vlen) * move))
			dy = int(round((vy / vlen) * move))
			if dx == 0 and dy == 0:
				# ensure progress if rounding killed movement
				dx = 1 if vx > 0 else -1

			for r in cont:
				translate_region_tiles(r, dx, dy, player_game)

			moved_any = True

		if not moved_any:
			break

	update_player_game_world_tiles_after_translation(player_game)