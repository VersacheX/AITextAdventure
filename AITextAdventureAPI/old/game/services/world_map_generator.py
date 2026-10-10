"""
Small CLI helper to create a Any and add regions using create_region_at.
Chooses origins on the perimeter outside existing world_tiles and uses a deterministic
per-iteration seed (seed_base * (iteration_index+1)) to pick candidate origins.
"""
from typing import Optional, Tuple, List, Any
import argparse
import random
import time

from game.objects.city import City
from game.services import world_gen_progress as progress


def _bbox_from_world_tiles(pg: Any) -> Optional[Tuple[int, int, int, int]]:
    """Return (min_x, max_x, min_y, max_y) or None if no tiles."""
    if not pg.world_tiles:
        return None
    xs = [x for (x, y) in pg.world_tiles.keys()]
    ys = [y for (x, y) in pg.world_tiles.keys()]
    return min(xs), max(xs), min(ys), max(ys)

def perimeter_candidates(pg: Any, margin: int, step: int = 8) -> List[Tuple[int, int]]:
    """Generate candidate coordinates from the actual perimeter (edge) of pg.world_tiles.

    For each occupied tile, any of its 4-neighbours that are empty become an edge candidate.
    Deduplicate and optionally thin the set by `step`. If no tiles exist, return [(0,0)].
    """
    # if no tiles yet -> recommend origin near 0,0
    if not pg.world_tiles:
        return [(0, 0)]

    edge = set()
    # collect empty 4-neighbour cells adjacent to any occupied tile
    for (x, y) in pg.world_tiles.keys():
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if (nx, ny) not in pg.world_tiles:
                edge.add((nx, ny))

    if not edge:
        # fallback to bounding-box perimeter if something strange happens
        bbox = _bbox_from_world_tiles(pg)
        if bbox is None:
            return [(0, 0)]
        min_x, max_x, min_y, max_y = bbox
        min_x -= margin
        max_x += margin
        min_y -= margin
        max_y += margin
        coords = []
        for x in range(min_x, max_x + 1, step):
            coords.append((x, min_y))
            coords.append((x, max_y))
        for y in range(min_y + step, max_y, step):
            coords.append((min_x, y))
            coords.append((max_x, y))
        seen = set()
        res = []
        for c in coords:
            if c not in seen:
                seen.add(c)
                res.append(c)
        return res

    # convert to list and apply step thinning (keeps order deterministic by sorting)
    candidates = sorted(edge)
    if step > 1:
        candidates = candidates[::step]
    return candidates


def choose_origin(pg: Any, rng: random.Random, min_size: int, attempts: int = 400) -> Optional[Tuple[int, int]]:
    """Try to find a perimeter origin outside existing world_tiles where a region can be created.

    Uses is_empty_area_large_enough_for_region to validate space and can_build_city_in_range
    to enforce distance rules between regions.

    This now picks candidates from the true edge of pg.world_tiles (per-tile neighbours)
    rather than a large rectangular ring.
    """
    margin = 32
    attempt = 0
    while attempt < attempts:
        # use perimeter derived from actual world tiles
        cand_list = perimeter_candidates(pg, margin, step=max(1, margin // 4))
        rng.shuffle(cand_list)
        for (cx, cy) in cand_list:
            # ensure not already a tile
            if pg.has_tile(cx, cy):
                continue
            # ensure sufficient empty area
            if not pg.is_empty_area_large_enough_for_region((cx, cy), min_size=min_size):
                continue
            # ensure distance from existing regions (uses service method)
            if not pg.can_build_city_in_range((cx, cy), min_distance=10):
                continue
            return (cx, cy)
        # widen search area and retry (this will increase thinning step inside perimeter_candidates)
        margin += 24
        attempt += len(cand_list) or 1
    return None


def build_regions(num_regions: int, seed_base: int = 12345, min_size: int = 1000, verbose: bool = True) -> Any:
    pg = Any()
    created = 0
    start = time.time()
    for i in range(num_regions):
        seed = seed_base * (i + 1)
        rng = random.Random(seed)
        origin = choose_origin(pg, rng, min_size=min_size, attempts=600)
        if origin is None:
            if verbose:
                print(f"[{i+1}/{num_regions}] Failed to find valid origin after retries. Skipping.")
            continue
        rc = pg.create_region_at(origin)
        if not rc:
            if verbose:
                print(f"[{i+1}/{num_regions}] create_region_at failed at origin {origin}. Skipping.")
            break
        created += 1
        if verbose:
            region_name = getattr(rc, "region_name", "<unknown>")
            child = getattr(rc, "child_city", None)
            child_name = getattr(child, "city_name", None) if child else None
            center = getattr(rc, "get_center_position", lambda: origin)()
            print(f"[{i+1}/{num_regions}] Seed={seed} Origin={origin} Created region='{region_name}' center={center} child_city={child_name}")
    elapsed = time.time() - start
    if verbose:
        print(f"Requested {num_regions}, created {created} regions in {elapsed:.2f}s. World tiles count={len(pg.world_tiles)}")
    return pg

def generate_world(pg: Any, num_regions: int, seed_base: int, min_size: int, verbose: bool) -> Any:
    """Generate regions in the given Any instance.

    Terminates as soon as the world reaches its city cap (``pg.get_max_cities()``)
    or when progress stalls -- i.e. too many consecutive iterations produce no
    new city. Without the stall guard a bad chapter/region selection could spin
    the full ``num_regions`` loop (historically 10000), flooding the console and
    never finishing.
    """
    created = 0
    start = time.time()

    try:
        max_cities = int(pg.get_max_cities())
    except Exception:
        max_cities = 21

    # Anchor the progress elapsed-time clock to the start of this run so emitted
    # timestamps read as +0.00s at the first line and reveal bottleneck phases.
    progress.reset_clock()

    # If we go this many iterations without the city count increasing, assume
    # the world can't place any more cities and stop. Scaled to the cap so we
    # still give generous room to find valid origins for the final cities.
    stall_limit = max(60, max_cities * 12)
    stalls_without_city = 0
    last_city_count = pg.get_city_count()

    if verbose:
        progress.emit(
            f"Generating world: target {max_cities} cities "
            f"(have {last_city_count}), up to {num_regions} region attempts."
        )
    # Player-facing headline for the loading overlay.
    try:
        progress.status("Generating your world...")
    except Exception:  # noqa: BLE001
        pass

    for i in range(num_regions):
        # Bail the instant we've placed every city.
        if pg.get_city_count() >= max_cities:
            if verbose:
                progress.emit(f"Reached city cap ({max_cities}) at iteration {i}. Stopping region creation.")
            break

        seed = seed_base * (i + 1)
        rng = random.Random(seed)
        origin = choose_origin(pg, rng, min_size=min_size, attempts=600)
        if origin is None:
            if verbose:
                progress.emit(f"[{i+1}/{num_regions}] Failed to find valid origin after retries. Skipping.")
            stalls_without_city += 1
            if stalls_without_city >= stall_limit:
                if verbose:
                    progress.emit(f"No progress toward new cities in {stalls_without_city} iterations. Stopping.")
                break
            continue

        rc = pg.create_region_at(origin)
        if not rc:
            if verbose:
                progress.emit(f"[{i+1}/{num_regions}] create_region_at failed at origin {origin}. Skipping.")
            if pg.get_city_count() >= max_cities:
                if verbose:
                    progress.emit(f"Reached city cap ({max_cities}) at iteration {i+1}. Stopping region creation.")
                break
        else:
            created += 1
            if verbose:
                region_name = getattr(rc, "region_name", "<unknown>")
                child = getattr(rc, "child_city", None)
                child_name = getattr(child, "city_name", None) if child else None
                center = getattr(rc, "get_center_position", lambda: origin)()
                progress.emit(
                    f"[{i+1}/{num_regions}] cities {pg.get_city_count()}/{max_cities} "
                    f"Seed={seed} Origin={origin} Created region='{region_name}' "
                    f"center={center} child_city={child_name}"
                )

        # Track city-count progress for the stall guard.
        current_city_count = pg.get_city_count()
        if current_city_count > last_city_count:
            last_city_count = current_city_count
            stalls_without_city = 0
            # Friendly, coarse progress for the loading overlay.
            try:
                progress.status(
                    f"Building the world's cities ({current_city_count}/{max_cities})..."
                )
            except Exception:  # noqa: BLE001
                pass
        else:
            stalls_without_city += 1
            if stalls_without_city >= stall_limit:
                if verbose:
                    progress.emit(
                        f"No new city in {stalls_without_city} iterations "
                        f"(have {current_city_count}/{max_cities}). Stopping region creation."
                    )
                break

    elapsed = time.time() - start
    if verbose:
        progress.emit(
            f"World generation done: requested {num_regions}, created {created} regions, "
            f"{pg.get_city_count()}/{max_cities} cities in {elapsed:.2f}s. "
            f"World tiles count={len(pg.world_tiles)}"
        )
    return pg
