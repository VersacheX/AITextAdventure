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
from typing import List, Tuple, Dict, Set, Optional, Any
import math
import random

from game.objects.city import City, Tile
from game.objects.player_game import PlayerGame
import game.constants as const
from game.services.city_builder_service import translate_city
from game.services import world_gen_progress as progress
from game.services.region_builder_service import ensure_4_connected


def _emit(line: str) -> None:
    """Surface a continent-building progress line to the dev TUI / overlay.

    Mirrors the world-generation loop so continent assignment, spreading and
    verification are observable in the same report stream.
    """
    progress.emit(line)


def _city_key(region: City) -> Optional[str]:
    """Canonical chapter-city key for a city-bearing region: ``region_name_city_name``.

    This matches the keys used by CHAPTER_CITY_ORDER and PlayerGame.get_continents(),
    so a region can be mapped to the continent it is *supposed* to belong to.
    """
    child = getattr(region, 'child_city', None)
    if region is None or child is None:
        return None
    region_name = getattr(region, 'region_name', None)
    city_name = getattr(child, 'city_name', None)
    if not region_name or not city_name:
        return None
    return f"{region_name}_{city_name}"


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
    """Partition city-bearing regions into continents.

    Cities are assigned to the continent they *canonically* belong to, as defined
    by CONTINENT_COMPOSITION + CHAPTER_CITY_ORDER (exposed via
    ``PlayerGame.get_continents()``), keyed by ``region_name_city_name``. This
    guarantees each continent ends up holding exactly the cities it should,
    instead of relying on arbitrary region-creation order (which previously
    scattered cities onto the wrong continents).

    Any city-bearing region whose key isn't found in the canonical map (e.g. a
    duplicate/unexpected city) falls back to sequential fill so it is never
    dropped. Returns a continents list of lists (city-bearing regions only).
    """
    num_continents = len(continent_city_counts)
    continents: List[List[City]] = [[] for _ in continent_city_counts]

    # Build key -> continent-index map from the canonical composition.
    # get_continents() returns {continent_number(1-based): [chapter_city_key, ...]}.
    key_to_continent: Dict[str, int] = {}
    try:
        canonical = player_game.get_continents()
        for cont_num, keys in canonical.items():
            idx = int(cont_num) - 1
            if 0 <= idx < num_continents:
                for key in keys:
                    key_to_continent[key] = idx
    except Exception as exc:  # noqa: BLE001 - never let mapping errors abort gen
        _emit(f"[continents] WARNING: could not read canonical city map: {exc}")

    city_regions = [r for r in player_game.regions if r and r.child_city is not None]
    _emit(
        f"[continents] Assigning {len(city_regions)} city regions into "
        f"{num_continents} continents by canonical chapter-city map."
    )

    unmatched: List[City] = []
    for region in city_regions:
        key = _city_key(region)
        target = key_to_continent.get(key) if key else None
        if target is None:
            unmatched.append(region)
            _emit(
                f"[continents]   city '{key}' not in canonical map -- deferring "
                f"to sequential fill."
            )
            continue
        continents[target].append(region)
        _emit(f"[continents]   city '{key}' -> continent {target + 1}")

    # Place any unmatched cities into continents that are still under their
    # target count, preserving determinism by continent order.
    for region in unmatched:
        placed = False
        for idx, count in enumerate(continent_city_counts):
            if len(continents[idx]) < count:
                continents[idx].append(region)
                _emit(
                    f"[continents]   fallback city '{_city_key(region)}' -> "
                    f"continent {idx + 1}"
                )
                placed = True
                break
        if not placed:
            # Last resort: smallest continent so nothing is lost.
            idx = min(range(num_continents), key=lambda i: len(continents[i]))
            continents[idx].append(region)
            _emit(
                f"[continents]   overflow city '{_city_key(region)}' -> "
                f"continent {idx + 1}"
            )

    # Log final city counts vs. requested so mismatches are obvious.
    for idx, count in enumerate(continent_city_counts):
        have = len(continents[idx])
        flag = "" if have == count else "  <-- MISMATCH"
        _emit(f"[continents] Continent {idx + 1}: {have}/{count} cities{flag}")

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
    """Assign regions without child_city to their continent (in-place mutate continents).

    Citiless regions are the connective landmass that binds each continent's
    cities together. Each connector now carries a baked ``continent`` attribute
    (stamped at creation in ``create_region_at`` and backfilled on load), so we
    attach it to that continent directly. This keeps every continent's connectors
    with the cities they were grown to link — critical for contiguity.

    Only connectors with a missing/out-of-range continent (legacy data) fall back
    to nearest-centroid assignment so nothing is ever dropped.
    """
    citiless = [r for r in player_game.regions if r and r.child_city is None]
    _emit(
        f"[continents] Attaching {len(citiless)} citiless (connector) regions "
        f"to their baked continents."
    )
    num = len(continents)
    attached_counts = [0] * num
    fallback = 0
    # centroids only needed for the legacy fallback path; computed lazily.
    centers: Optional[List[Tuple[float, float]]] = None
    for region in citiless:
        cont_num = getattr(region, "continent", None)
        idx = (cont_num - 1) if isinstance(cont_num, int) else None
        if idx is None or not (0 <= idx < num):
            # Legacy / unstamped connector: fall back to nearest continent centroid.
            if centers is None:
                centers = [continent_center_from_regions(cont) for cont in continents]
            _, rc = bbox_and_center_from_tiles(set(region.tiles.keys()))
            idx = min(range(num), key=lambda i: (rc[0] - centers[i][0]) ** 2 + (rc[1] - centers[i][1]) ** 2)
            fallback += 1
        continents[idx].append(region)
        attached_counts[idx] += 1

    if fallback:
        _emit(f"[continents]   {fallback} connector(s) had no baked continent -> nearest-centroid fallback")
    for idx, n in enumerate(attached_counts):
        _emit(f"[continents] Continent {idx + 1}: +{n} connector regions")

# ------------------------------------------------------------------
# Continent compaction (pack a continent's scattered regions into one mass)
# ------------------------------------------------------------------
def _region_all_tiles(region: City) -> Set[Tuple[int, int]]:
    """All world tiles owned by a region, including its child city."""
    tiles: Set[Tuple[int, int]] = set(region.tiles.keys())
    if getattr(region, "child_city", None):
        tiles.update(region.child_city.tiles.keys())
    return tiles

def normalize_region_internal_connectivity(region: City, player_game: PlayerGame) -> int:
    """Bridge a single region's internal gaps so its own tiles form one blob.

    Rigid packing (``compact_region_onto_mass``) applies a single offset to every
    tile of a region, so an internally-disconnected region (e.g. a child city
    whose tiles aren't adjacent to its parent region, or a legacy region saved as
    several blobs) stays disconnected after being unioned into the mass. Repair it
    *before* packing by carving orthogonal bridges between the region's own
    4-connected components, materialising the bridge cells as real region tiles.

    Returns the number of bridge tiles created.
    """
    if not region or not region.tiles:
        return 0
    blob = _region_all_tiles(region)
    if _count_components(blob) <= 1:
        return 0

    # Bridge within this region only. Every world tile owned by another region
    # (i.e. not part of this region/child blob) is off limits, so a bridge can
    # never carve through — and silently steal ownership of — another region's
    # tile when the world is rebuilt.
    blocked = set(player_game.world_tiles) - blob
    bridged = ensure_4_connected(set(blob), ignored_set=blocked)
    added = bridged - blob
    for (x, y) in added:
        if (x, y) not in region.tiles:
            region.create_tile(player_game, x, y)
            # Populate ONLY the newly created bridge tile. Calling populate_tiles()
            # would re-roll every existing tile's subloc_map and could restore
            # already-looted items/money on explored regions.
            region.populate_tile(player_game, region.tiles[(x, y)], x, y)
    return len(added)


def _tiles_touch(a: Set[Tuple[int, int]], b: Set[Tuple[int, int]]) -> bool:
    """True if any tile in `a` is 4-adjacent to (or overlaps) a tile in `b`."""
    for x, y in a:
        if ((x, y) in b
                or (x + 1, y) in b or (x - 1, y) in b
                or (x, y + 1) in b or (x, y - 1) in b):
            return True
    return False

def _select_seed_region_index(cont: List[City], player_game: PlayerGame) -> int:
    """Pick the anchor region a continent is packed around.

    Prefer the region the player currently stands on (so the player is never
    displaced); otherwise prefer the largest city-bearing region; otherwise the
    largest region. Returns an index into `cont`.
    """
    player_pos = (player_game.x, player_game.y)
    for i, r in enumerate(cont):
        if r and player_pos in r.tiles:
            return i
        if r and getattr(r, "child_city", None) and player_pos in r.child_city.tiles:
            return i
    # Fall back to the largest city-bearing region, then largest region overall.
    city_regions = [(i, r) for i, r in enumerate(cont) if r and getattr(r, "child_city", None)]
    pool = city_regions if city_regions else [(i, r) for i, r in enumerate(cont) if r]
    if not pool:
        return 0
    return max(pool, key=lambda ir: len(_region_all_tiles(ir[1])))[0]

def compact_region_onto_mass(
    region: City,
    mass: Set[Tuple[int, int]],
    player_game: PlayerGame,
) -> Set[Tuple[int, int]]:
    """Snap `region` flush against one side of `mass`, guaranteed contiguous.

    Rather than sliding toward a centroid (which can miss for irregular shapes),
    this uses an edge-snap that is mathematically guaranteed to produce 4-contact
    with zero overlap for ANY rigid blob shapes:

    - Choose a side (E/W/N/S) based on where the region currently lies relative
      to the mass centroid, so the region moves the natural (short) way.
    - For an EAST snap: take the mass's max-x tile `m` and the region's min-x
      tile `r`, then translate the region so `r` lands at `(m.x + 1, m.y)`.
      Afterwards every region tile has x >= m.x+1 while every mass tile has
      x <= m.x, so the two sets cannot overlap; and `r` sits directly east of
      `m`, so they are 4-adjacent. The other three sides are symmetric.

    A single net offset is computed and applied with one translate call (so
    entities move exactly once). Returns the shifted region tile set for the
    caller to fold into the growing mass. `mass` is not mutated here.
    """
    region_tiles = _region_all_tiles(region)
    if not region or not region.tiles or not mass:
        return region_tiles
    # Only short-circuit when the region is already seated: disjoint from the mass
    # AND 4-adjacent to it. _tiles_touch() is also true for OVERLAP, so an
    # overlapping region must still fall through to the edge snap — otherwise the
    # later world_tiles rebuild would silently overwrite one owner's tiles.
    if region_tiles.isdisjoint(mass) and _tiles_touch(region_tiles, mass):
        return region_tiles

    _, (rcx, rcy) = bbox_and_center_from_tiles(region_tiles)
    _, (mcx, mcy) = bbox_and_center_from_tiles(mass)

    # Pick the snap side from the dominant axis of the region->mass offset.
    if abs(rcx - mcx) >= abs(rcy - mcy):
        side = "E" if rcx >= mcx else "W"
    else:
        side = "N" if rcy >= mcy else "S"

    if side == "E":
        # Region is east of mass: place region's leftmost (min-x) column one tile
        # east of the mass's rightmost (max-x) column, matching y of that anchor.
        m = max(mass, key=lambda p: (p[0], p[1]))
        r = min(region_tiles, key=lambda p: (p[0], p[1]))
        off_x = (m[0] + 1) - r[0]
        off_y = m[1] - r[1]
    elif side == "W":
        m = min(mass, key=lambda p: (p[0], p[1]))
        r = max(region_tiles, key=lambda p: (p[0], p[1]))
        off_x = (m[0] - 1) - r[0]
        off_y = m[1] - r[1]
    elif side == "N":
        m = max(mass, key=lambda p: (p[1], p[0]))
        r = min(region_tiles, key=lambda p: (p[1], p[0]))
        off_y = (m[1] + 1) - r[1]
        off_x = m[0] - r[0]
    else:  # "S"
        m = min(mass, key=lambda p: (p[1], p[0]))
        r = max(region_tiles, key=lambda p: (p[1], p[0]))
        off_y = (m[1] - 1) - r[1]
        off_x = m[0] - r[0]

    cur = {(x + off_x, y + off_y) for (x, y) in region_tiles}
    if off_x or off_y:
        translate_region_tiles(region, off_x, off_y, player_game)
    return cur

def compact_continents_to_contiguous(player_game: PlayerGame, continents: List[List[City]]) -> None:
    """Pack each continent's regions into a single contiguous landmass in-place.

    City->continent membership is canonical and fixed, but the member regions
    were generated at scattered positions, leaving a continent as disconnected
    islands. For each continent we keep a seed region anchored and accrete every
    other region onto the growing mass by sliding it inward until it makes
    edge-contact, guaranteeing 4-connectivity.

    IMPORTANT: this must run AFTER the continents have been spread apart, so each
    continent occupies its own isolated region of space. Packing then only ever
    tests/moves against the continent's own tiles and can never slide a region
    across (and overwrite) another continent's tiles.
    """
    _emit("[continents] Compacting continents into contiguous landmasses...")
    for idx, cont in enumerate(continents):
        regions = [r for r in cont if r and r.tiles]
        if len(regions) <= 1:
            _emit(f"[continents]   continent {idx + 1}: <=1 region, nothing to compact")
            continue

        seed_local = _select_seed_region_index(regions, player_game)
        seed = regions[seed_local]
        # Repair any internally-disconnected region BEFORE rigid packing. A single
        # offset can't reconnect a region's own split blobs, so bridge them first.
        for region in regions:
            bridged = normalize_region_internal_connectivity(region, player_game)
            if bridged:
                _emit(
                    f"[continents]   continent {idx + 1}: bridged "
                    f"{bridged} internal tile(s) in region "
                    f"'{getattr(region, 'region_name', '?')}'"
                )
        mass: Set[Tuple[int, int]] = _region_all_tiles(seed)
        _, seed_center = bbox_and_center_from_tiles(mass)

        # Accrete remaining regions nearest-to-seed first so the mass grows
        # compactly rather than leaving a straggler stranded.
        remaining = [r for i, r in enumerate(regions) if i != seed_local]

        def _dist_to_seed(region: City, center=seed_center) -> float:
            _, (cx, cy) = bbox_and_center_from_tiles(_region_all_tiles(region))
            return (cx - center[0]) ** 2 + (cy - center[1]) ** 2

        remaining.sort(key=_dist_to_seed)

        for region in remaining:
            placed = compact_region_onto_mass(region, mass, player_game)
            mass |= placed

        # Rebuild world tiles so later bbox/centroid reads see the packed layout.
        update_player_game_world_tiles_after_translation(player_game)
        contiguous = _continent_is_contiguous(cont)
        if not contiguous:
            # Diagnose WHY: count connected components of the whole continent, and
            # check whether any individual region blob is itself disconnected
            # (e.g. a child_city whose tiles aren't adjacent to its region).
            # NOTE: avoid '[' / ']' in emitted text — the dev report renders via
            # Rich markup and square brackets would be parsed as markup tags.
            comp = _count_components(continent_tiles(cont))
            bad_regions = []
            for r in regions:
                rt = _region_all_tiles(r)
                blob_parts = _count_components(rt)
                if blob_parts > 1:
                    cname = getattr(getattr(r, "child_city", None), "display_name", None)
                    region_parts = _count_components(set(r.tiles.keys()))
                    city_parts = (
                        _count_components(set(r.child_city.tiles.keys()))
                        if getattr(r, "child_city", None) else 0
                    )
                    bad_regions.append(
                        f"{{{getattr(r, 'region_name', '?')}"
                        f"{'/' + str(cname) if cname else ''}: "
                        f"blob={blob_parts} region={region_parts} city={city_parts}}}"
                    )
            _emit(
                f"[continents]   continent {idx + 1}: components={comp}; "
                f"internally-split regions: {' '.join(bad_regions) or 'none'}"
            )
        _emit(
            f"[continents]   continent {idx + 1}: packed {len(regions)} regions "
            f"(seed kept fixed), contiguous={contiguous}"
        )

    # Clear the per-pass entity-move guard that translate_region_tiles set, so
    # any later translation pass starts with a fresh tracking set.
    if hasattr(player_game, "_continent_translate_moved_entities"):
        delattr(player_game, "_continent_translate_moved_entities")

# ------------------------------------------------------------------
# Translation and spread (modified to allow skipping first continent)
# ------------------------------------------------------------------
def translate_region_tiles(region: City, dx: int, dy: int, player_game: PlayerGame) -> None:
    """Translate region City tiles in-place by (dx,dy).

    Moves both the tile grid AND the sublocation map so the continent moves as a
    rigid unit. ``subloc_map`` is keyed by (x, y, z); only x/y shift (floor z is
    preserved). If sublocs were not re-keyed here they would be stranded at the
    continent's pre-move coordinates and ``get_sublocation_at`` would miss them.
    """
    if not region or not region.tiles:
        return
    if not dx and not dy:
        return
    new_tiles: Dict[Tuple[int,int], Tile] = {}
    for (x,y), t in list(region.tiles.items()):
        t.x = x + dx
        t.y = y + dy
        translate_entities_at_location(x, y, dx, dy, player_game)  # translate any entities at this tile
        new_tiles[(x+dx, y+dy)] = t
    region.tiles = new_tiles
    _translate_subloc_map(region, dx, dy)
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
        _translate_subloc_map(child, dx, dy)


def _translate_subloc_map(city: City, dx: int, dy: int) -> None:
    """Re-key a City's subloc_map by (dx,dy), preserving floor (z)."""
    subloc_map = getattr(city, 'subloc_map', None)
    if not subloc_map:
        return
    new_subloc_map: Dict[Tuple[int,int,int], Any] = {}
    for key, sublocs in subloc_map.items():
        x, y, z = key
        new_subloc_map[(x + dx, y + dy, z)] = sublocs
    city.subloc_map = new_subloc_map

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

# ------------------------------------------------------------------
# Intelligent linear continent placement (8-directional, bbox-aware fit)
# ------------------------------------------------------------------
def _dilate(tiles: Set[Tuple[int, int]], gap: int) -> Set[Tuple[int, int]]:
    """Return `tiles` grown by (gap-1) in Chebyshev distance.

    A continent offset is valid when its tiles are disjoint from the world's
    dilated set: gap=1 forbids only overlap, gap=2 enforces a one-tile channel,
    and so on. The dilation is computed once per placement.
    """
    if gap <= 1:
        return set(tiles)
    r = gap - 1
    out: Set[Tuple[int, int]] = set()
    for (x, y) in tiles:
        for dx in range(-r, r + 1):
            for dy in range(-r, r + 1):
                out.add((x + dx, y + dy))
    return out

def _lane_key_and_norm(d: Tuple[int, int]) -> Tuple[str, int]:
    """Return (lane_key_kind, squared-norm) for a slide direction.

    A continent slides along ``-d``. Every cell a given point can ever hit while
    sliding shares one invariant ("lane"); grouping occupied cells by that
    invariant lets us binary-search the first collision instead of stepping. The
    invariant per direction:
      - horizontal (±1, 0): constant y
      - vertical   (0, ±1): constant x
      - main diag  (1,1)/(-1,-1): constant x - y
      - anti diag  (1,-1)/(-1,1): constant x + y
    """
    dx, dy = d
    if dy == 0:
        return "y", 1
    if dx == 0:
        return "x", 1
    if dx == dy:
        return "x-y", 2
    return "x+y", 2


def _lane_key(cell: Tuple[int, int], kind: str) -> int:
    x, y = cell
    if kind == "y":
        return y
    if kind == "x":
        return x
    if kind == "x-y":
        return x - y
    return x + y  # "x+y"


def _build_lane_index(world_dilated: Set[Tuple[int, int]],
                      d: Tuple[int, int]) -> Dict[int, List[int]]:
    """Group occupied cells into lanes for direction ``d``.

    Maps lane_key -> sorted list of each cell's scalar progress ``s = x*dx+y*dy``.
    Built once per direction and reused across every jitter candidate.
    """
    import bisect  # local import keeps module import light
    kind, _ = _lane_key_and_norm(d)
    dx, dy = d
    lanes: Dict[int, List[int]] = {}
    for (x, y) in world_dilated:
        key = _lane_key((x, y), kind)
        lanes.setdefault(key, []).append(x * dx + y * dy)
    for vals in lanes.values():
        vals.sort()
    return lanes


def _interior_disjoint(moved_all: Set[Tuple[int, int]],
                       world_dilated: Set[Tuple[int, int]],
                       off: Tuple[int, int]) -> bool:
    """True if no tile of the offset blob overlaps the dilated world.

    Catches the enclosure case (blob wrapping a world tile: boundary disjoint
    while an interior tile overlaps). This is the expensive full-blob scan, so
    callers run it only on the chosen candidate, not every jitter.
    """
    ox, oy = off
    for (x, y) in moved_all:
        if (x + ox, y + oy) in world_dilated:
            return False
    return True


def _push_in_swept(moved_boundary: Set[Tuple[int, int]],
                   world_dilated: Set[Tuple[int, int]],
                   lanes: Dict[int, List[int]],
                   base_off: Tuple[int, int],
                   d: Tuple[int, int],
                   far: int) -> Optional[Tuple[int, int]]:
    """Slide a continent inward along ``-d`` from a far, clear start and return
    the tightest boundary-valid offset — computed by swept projection.

    For each boundary tile at its far start we binary-search its lane for the
    nearest occupied cell ahead of it along the slide, giving that tile's
    first-collision step directly. The global minimum over all boundary tiles is
    the first step ANY boundary tile touches the world, so the last fully-clear
    step is ``min_collision - 1`` — the original "stop at first contact" rule but
    O(boundary·log) per candidate instead of O(boundary·far).

    NOTE: this validates only the boundary (cheap). The caller must run
    `_interior_disjoint` on the WINNING offset to reject the enclosure case; we
    deliberately skip the full-blob scan here so it isn't paid per jitter.
    """
    import bisect
    kind, norm = _lane_key_and_norm(d)
    dx, dy = d

    # Reject immediately if the blob already collides at its far start (t=0).
    ox0, oy0 = base_off
    for (x, y) in moved_boundary:
        if (x + ox0, y + oy0) in world_dilated:
            return None

    min_collision = far + 1
    for (bx, by) in moved_boundary:
        # Start position of this boundary tile at t=0.
        sx, sy = bx + base_off[0], by + base_off[1]
        key = _lane_key((sx, sy), kind)
        vals = lanes.get(key)
        if not vals:
            continue
        s0 = sx * dx + sy * dy
        # Sliding inward decreases s by `norm` per step, so we want the largest
        # occupied s strictly less than s0 (the first obstacle ahead).
        idx = bisect.bisect_left(vals, s0) - 1
        if idx < 0:
            continue
        s_hit = vals[idx]
        t_hit = (s0 - s_hit) // norm  # exact: both on the same lane/line
        if 1 <= t_hit < min_collision:
            min_collision = t_hit
            if min_collision == 1:
                break  # cannot get tighter

    t = min(far, min_collision - 1)
    if t < 0:
        return None
    return (base_off[0] - d[0] * t, base_off[1] - d[1] * t)

def _find_continent_placement(moved_all: Set[Tuple[int, int]],
                              moved_boundary: Set[Tuple[int, int]],
                              world_set: Set[Tuple[int, int]],
                              gap: int) -> Tuple[int, int]:
    """Choose the offset that seats a continent blob against the current world
    mass with the smallest resulting world bbox (compact objective).

    Tries all 8 directions (cardinals + diagonals). For each, the blob starts
    far out along that bearing and is pushed inward to first contact, with
    perpendicular jitter so it can slide along the coast into pockets. Candidates
    are scored by the area of the combined bbox; the tightest fit wins. Because
    every side is probed, a continent that can't nestle beside its predecessor
    still finds a valid perimeter edge somewhere (ordering is a preference, not a
    hard constraint). If nothing fits (degenerate), a guaranteed east placement
    outside the bbox is returned so generation always terminates.
    """
    if not world_set:
        return (0, 0)

    (wminx, wmaxx, wminy, wmaxy), (wcx, wcy) = bbox_and_center_from_tiles(world_set)
    (cminx, cmaxx, cminy, cmaxy), (ccx, ccy) = bbox_and_center_from_tiles(moved_all)
    world_dilated = _dilate(world_set, gap)

    w_span = max(wmaxx - wminx, wmaxy - wminy)
    c_span = max(cmaxx - cminx, cmaxy - cminy)
    far = w_span + c_span + gap + 6

    directions = [
        (1, 0), (0, 1), (-1, 0), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1),
    ]

    jitter_half = (w_span + c_span) // 2
    jitter_step = max(1, (w_span + c_span) // 12)

    best_off: Optional[Tuple[int, int]] = None
    best_score: Optional[Tuple[int, float]] = None
    # Collect every boundary-valid candidate with its score, then run the
    # expensive interior (enclosure) scan only in best-score order until one
    # passes. This caps full-blob scans at ~1 (not ~100) in the common case.
    candidates: List[Tuple[Tuple[int, float], Tuple[int, int]]] = []

    for d in directions:
        px, py = -d[1], d[0]  # perpendicular axis for jitter
        # Build the lane index for this direction ONCE and reuse it across every
        # jitter candidate — this is what makes placement near-linear in tiles.
        lanes = _build_lane_index(world_dilated, d)
        for j in range(-jitter_half, jitter_half + 1, jitter_step):
            fcx = wcx + d[0] * far + px * j
            fcy = wcy + d[1] * far + py * j
            base_off = (int(round(fcx - ccx)), int(round(fcy - ccy)))
            off = _push_in_swept(moved_boundary, world_dilated, lanes, base_off, d, far)
            if off is None:
                continue
            nminx = min(wminx, cminx + off[0])
            nmaxx = max(wmaxx, cmaxx + off[0])
            nminy = min(wminy, cminy + off[1])
            nmaxy = max(wmaxy, cmaxy + off[1])
            area = (nmaxx - nminx) * (nmaxy - nminy)
            # tie-break: keep the new continent's centre near the world centre
            dcx = (ccx + off[0]) - wcx
            dcy = (ccy + off[1]) - wcy
            closeness = dcx * dcx + dcy * dcy
            score = (area, closeness)
            candidates.append((score, off))

    # Validate interiors in ascending score order; first that is enclosure-free
    # wins. Only here do we pay the full-blob scan, and usually just once.
    candidates.sort(key=lambda c: c[0])
    for score, off in candidates:
        if _interior_disjoint(moved_all, world_dilated, off):
            best_score = score
            best_off = off
            break

    if best_off is None:
        # Degenerate fallback: drop it just east of the bbox, centre-aligned.
        return (wmaxx + gap + 1 - cminx, int(round(wcy - ccy)))
    return best_off

def place_continents_linearly(player_game: PlayerGame,
                              continents: List[List[City]],
                              *,
                              anchor_index: int = 0,
                              gap: int = 3) -> None:
    """Position continents one at a time around a fixed anchor using intelligent,
    bbox-aware fitting (replaces blind radial spread).

    The anchor continent (the player's) never moves. Each remaining continent is
    treated as a rigid blob and seated against the accumulated world mass via
    `_find_continent_placement`: it is offset to the best-fitting coastline and
    folded in, so the next continent fits against the growing landmass. This
    keeps the world compact and contiguous-friendly while preserving continent
    ordering as a placement preference.

    Requires each continent to already be a single contiguous mass (run
    `compact_continents_to_contiguous` first) and to be isolated in space so the
    initial per-continent tile sets don't interleave.
    """
    if not continents:
        return

    order = [anchor_index] + [i for i in range(len(continents)) if i != anchor_index]

    anchor = continents[anchor_index] if 0 <= anchor_index < len(continents) else None
    world_set: Set[Tuple[int, int]] = continent_tiles(anchor) if anchor else set()

    _emit(
        f"[continents] Placing {len(continents)} continents linearly "
        f"(anchor={anchor_index + 1}, gap={gap})."
    )

    for i in order:
        if i == anchor_index:
            continue
        cont = continents[i]
        if not cont:
            _emit(f"[continents]   continent {i + 1}: empty, skipped")
            continue
        moved_all = continent_tiles(cont)
        if not moved_all:
            continue

        if not world_set:
            # No anchor mass yet (e.g. empty anchor): this becomes the seed.
            world_set = set(moved_all)
            _emit(f"[continents]   continent {i + 1}: seeded as initial mass")
            continue

        moved_boundary = boundary_tiles(moved_all)
        off = _find_continent_placement(moved_all, moved_boundary, world_set, gap)
        dx, dy = off
        if dx or dy:
            for r in cont:
                translate_region_tiles(r, dx, dy, player_game)
        world_set |= {(x + dx, y + dy) for (x, y) in moved_all}
        _emit(
            f"[continents]   continent {i + 1}: placed by ({dx},{dy}) "
            f"({len(cont)} regions)"
        )

    if hasattr(player_game, "_continent_translate_moved_entities"):
        delattr(player_game, "_continent_translate_moved_entities")

    update_player_game_world_tiles_after_translation(player_game)

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

    _emit(
        f"[continents] Spreading {len(continents)} continents radially "
        f"(radius={radius}, skip_first={skip_first})."
    )

    for i, cont in enumerate(continents):
        if not cont:
            _emit(f"[continents]   continent {i + 1}: empty, skipped")
            continue
        if skip_first and i == 0:
            _emit(f"[continents]   continent {i + 1}: anchored (player start), not moved")
            continue

        cur_center = cont_centers[i]
        angle = base_angle + i * angle_step
        target_cx = world_center[0] + math.cos(angle) * radius
        target_cy = world_center[1] + math.sin(angle) * radius
        dx = int(round(target_cx - cur_center[0]))
        dy = int(round(target_cy - cur_center[1]))

        for r in cont:
            translate_region_tiles(r, dx, dy, player_game)

        _emit(
            f"[continents]   continent {i + 1}: moved by ({dx},{dy}) to "
            f"angle {math.degrees(angle):.0f}deg ({len(cont)} regions)"
        )

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

    _emit(
        f"[continents] Building continents: composition={list(requested_counts)} "
        f"(total {sum(requested_counts)} cities)."
    )


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

    # 4) spread continents radially but skip first (player) continent. This moves
    # each continent (as a rigid body) onto its own distinct angle around the
    # world center, so the continents no longer spatially interleave — each now
    # occupies an isolated region of space.
    spread_continents_radial(player_game, continents, rng, radius=spread_radius, skip_first=True)

    # 4.a) compact each continent's regions into a single contiguous landmass.
    # City->continent membership is canonical/fixed, but the member regions were
    # created at scattered world positions, so a continent's own regions form
    # islands. Now that the continents are isolated in space (post-spread), pack
    # each one's regions edge-to-edge around a seed region (the player's region
    # for the player's continent, so the player is never displaced). Because each
    # continent is isolated, sliding a region toward its own seed can never cross
    # into — and overwrite — another continent's tiles.
    compact_continents_to_contiguous(player_game, continents)

    # 4.b) position continents around the anchor using intelligent, bbox-aware
    # fitting. Each continent is now a rigid contiguous blob isolated in space,
    # so the packer can seat it against the growing world mass at the tightest
    # fitting coastline (8-directional, interior-pocket aware), keeping the world
    # compact. This replaces the old radial pull, which only shrank distances
    # without regard to how blobs actually nest together.
    place_continents_linearly(player_game, continents, anchor_index=0, gap=3)

    # 4.c) verify each continent holds exactly the cities it should per the
    # canonical chapter-city map, and that its landmass is contiguous enough to
    # connect those cities. If verification fails we must NOT silently accept the
    # layout — retry compaction + placement, re-verifying each time, before
    # giving up. The final status is propagated to the caller so an invalid world
    # can be rejected/rolled back rather than reported as complete.
    verified = verify_continent_city_containment(player_game, continents, requested_counts)
    max_repair_attempts = 2
    attempt = 0
    while not verified and attempt < max_repair_attempts:
        attempt += 1
        _emit(
            f"[continents] Verification failed -- repair attempt "
            f"{attempt}/{max_repair_attempts}: recompacting and replacing."
        )
        compact_continents_to_contiguous(player_game, continents)
        place_continents_linearly(player_game, continents, anchor_index=0, gap=3)
        verified = verify_continent_city_containment(player_game, continents, requested_counts)

    if not verified:
        _emit(
            "[continents] ERROR: continents still invalid after repair attempts; "
            "world layout is NOT contiguous. Aborting ocean build; caller must "
            "reject this layout."
        )
        # Do not build the ocean around (and thereby commit) a broken layout.
        # Return early with verification_passed=False so the caller can reject.
        return {
            "continents": continent_bboxes,
            "ocean_bbox": None,
            "ocean_region": None,
            "verification_passed": False,
        }

    # 5) recompute world bounds and create ocean bbox
    all_tiles = set(player_game.world_tiles.keys())
    if not all_tiles:
        return {
            "continents": continent_bboxes,
            "ocean_bbox": None,
            "ocean_region": None,
            "verification_passed": verified,
        }

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
        "verification_passed": verified,
        #"continent_groups": continents
    }

def verify_continent_city_containment(
    player_game: PlayerGame,
    continents: List[List[City]],
    requested_counts: List[int],
) -> bool:
    """Verify each continent holds exactly the cities it should and that those
    cities sit on a single contiguous landmass. Logs results to the dev TUI.

    Returns True if every continent matches its canonical city set and is
    contiguous; False otherwise. This is a diagnostic -- it does not mutate the
    world, it only surfaces problems so bad splits are visible.
    """
    _emit("[continents] Verifying city containment + contiguity...")

    # Canonical expected key set per continent index.
    expected: Dict[int, Set[str]] = {}
    try:
        canonical = player_game.get_continents()
        for cont_num, keys in canonical.items():
            idx = int(cont_num) - 1
            expected[idx] = set(keys)
    except Exception as exc:  # noqa: BLE001
        _emit(f"[continents] WARNING: cannot read canonical map for verify: {exc}")
        expected = {}

    all_ok = True
    for idx, cont in enumerate(continents):
        actual_keys = {_city_key(r) for r in cont if r.child_city is not None}
        actual_keys.discard(None)
        want = expected.get(idx, set())

        missing = want - actual_keys
        extra = actual_keys - want

        count_ok = (idx >= len(requested_counts)) or (len(actual_keys) == requested_counts[idx])
        set_ok = (not want) or (not missing and not extra)
        contiguous = _continent_is_contiguous(cont)

        if not (count_ok and set_ok and contiguous):
            all_ok = False

        status = "OK" if (count_ok and set_ok and contiguous) else "PROBLEM"
        _emit(
            f"[continents] Continent {idx + 1} [{status}]: "
            f"cities={sorted(k for k in actual_keys if k)} "
            f"contiguous={contiguous}"
        )
        if missing:
            _emit(f"[continents]   MISSING expected cities: {sorted(missing)}")
        if extra:
            _emit(f"[continents]   UNEXPECTED cities present: {sorted(extra)}")
        if not contiguous:
            _emit(
                f"[continents]   NOT CONTIGUOUS: cities are not all connected by "
                f"this continent's regions (need more connector regions)."
            )

    _emit(f"[continents] Verification {'passed' if all_ok else 'found problems'}.")
    return all_ok


def _continent_is_contiguous(cont: List[City]) -> bool:
    """Return True if all tiles of a continent's regions form one 4-connected mass.

    Used to confirm that the citiless connector regions actually bridge the
    continent's cities into a single landmass rather than leaving islands.
    """
    tiles = continent_tiles(cont)
    if not tiles:
        return True  # vacuously contiguous

    start = next(iter(tiles))
    seen: Set[Tuple[int, int]] = {start}
    stack = [start]
    while stack:
        x, y = stack.pop()
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if (nx, ny) in tiles and (nx, ny) not in seen:
                seen.add((nx, ny))
                stack.append((nx, ny))

    return len(seen) == len(tiles)


def _count_components(tiles: Set[Tuple[int, int]]) -> int:
    """Number of 4-connected components in a tile set (0 for empty)."""
    if not tiles:
        return 0
    remaining = set(tiles)
    components = 0
    while remaining:
        start = next(iter(remaining))
        stack = [start]
        remaining.discard(start)
        while stack:
            x, y = stack.pop()
            for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if (nx, ny) in remaining:
                    remaining.discard((nx, ny))
                    stack.append((nx, ny))
        components += 1
    return components


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
