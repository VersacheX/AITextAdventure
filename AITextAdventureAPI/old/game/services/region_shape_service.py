"""Region shaping helpers extracted from region_builder.

Provides helpers used to seed and grow region tiles:
- `perimeter_first_sweep`: seed small dabs hugging a perimeter
- `spawn_clump`: grow a short spine/clump outward from a point
- `dab_at_point`: populate a circular dab and add neighbors to frontier
- `second_pass_fill`: iterative fill to close remaining gaps

These functions operate on a City-like `rc` and require the caller to pass

so this module avoids importing project internals.
"""
from typing import Any, Callable, Deque, Iterable, Set, Tuple
from collections import deque
import random
import logging
import math

logger = logging.getLogger(__name__)

def make_filled_circle(x: int, y: int, radius: int, current_tiles: Set[Tuple[int, int]], ignored_tiles: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    """ fill the area of a circle (not square) around the main_tiles at the center point """
    filled_tiles: Set[Tuple[int, int]] = set()

    if radius <=0:
        return filled_tiles
    
    r2 = radius * radius
    # iterate over x-offsets and compute max y-offset for circle inclusion
    start_count = len(current_tiles)
    added_tile_count = 0
    total_tile_count = 0
    for dx in range(-radius, radius +1):
        # compute the max absolute dy for this dx using circle equation dx^2 + dy^2 <= r^2
        rem = r2 - (dx * dx)
        if rem <0:
            continue
        max_dy = int(math.sqrt(rem))
        for dy in range(-max_dy, max_dy +1):
            px = x + dx
            py = y + dy
            pt = (px, py)
            total_tile_count += 1
            # skip tiles that are part of main city or explicitly ignored
            if pt in current_tiles or pt in ignored_tiles:
                continue
            current_tiles.add(pt)
            filled_tiles.add(pt)
            added_tile_count += 1
    
    # print (f"make_filled_circle added {added_tile_count} tiles of {total_tile_count} possible")
    # print (f"accounting for {start_count} as the difference: control value was: {total_tile_count-added_tile_count}")
    
    return filled_tiles


def make_filled_square(cx: int, cy: int, half_size: int, current_tiles: Set[Tuple[int, int]], ignored_tiles: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    """Return integer grid points inside an axis-aligned filled square centered at (cx,cy).

    half_size is the half-extent (distance from center to side)."""
    filled: Set[Tuple[int, int]] = set()
    if half_size <0:
        return filled
    for dx in range(-half_size, half_size +1):
        for dy in range(-half_size, half_size +1):
            pt = (cx + dx, cy + dy)
            if pt in current_tiles or pt in ignored_tiles:
                continue
            current_tiles.add(pt)
            filled.add(pt)
    logger.debug("make_filled_square: center=(%s,%s) half_size=%d filled=%d", cx, cy, half_size, len(filled))
    return filled


def make_filled_diamond(cx: int, cy: int, radius: int, current_tiles: Set[Tuple[int, int]], ignored_tiles: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    """Return grid points inside a Manhattan-distance diamond: |dx|+|dy| <= radius."""
    filled: Set[Tuple[int, int]] = set()
    if radius <0:
        return filled
    for dx in range(-radius, radius +1):
        max_dy = radius - abs(dx)
        for dy in range(-max_dy, max_dy +1):
            pt = (cx + dx, cy + dy)
            if pt in current_tiles or pt in ignored_tiles:
                continue
            current_tiles.add(pt)
            filled.add(pt)
    logger.debug("make_filled_diamond: center=(%s,%s) radius=%d filled=%d", cx, cy, radius, len(filled))
    return filled


def make_filled_hex(cx: int, cy: int, radius: int, current_tiles: Set[Tuple[int, int]], ignored_tiles: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    """Return grid points inside a hex of axial radius `radius` using axial coords mapped as (x+q, y+r).

    This produces a symmetric hex by iterating axial q,r and testing cube distance.
    """
    filled: Set[Tuple[int, int]] = set()
    if radius <0:
        return filled
    R = radius
    for q in range(-R, R +1):
        for r in range(-R, R +1):
            if max(abs(q), abs(r), abs(-q - r)) <= R:
                pt = (cx + q, cy + r)
                if pt in current_tiles or pt in ignored_tiles:
                    continue
                current_tiles.add(pt)
                filled.add(pt)
    #logger.debug("make_filled_hex: center=(%s,%s) radius=%d filled=%d", cx, cy, radius, len(filled))
    return filled


def _point_in_polygon(px: float, py: float, verts: Tuple[Tuple[float, float], ...]) -> bool:
    """Even-odd ray casting point-in-polygon test. verts is sequence of (x,y)."""
    inside = False
    n = len(verts)
    if n ==0:
        return False
    j = n -1
    for i in range(n):
        xi, yi = verts[i]
        xj, yj = verts[j]
        intersect = ((yi > py) != (yj > py)) and (px < (xj - xi) * (py - yi) / (yj - yi +1e-12) + xi)
        if intersect:
            inside = not inside
        j = i
    return inside


def make_filled_star(cx: int, cy: int, outer_radius: int, points: int =5, inner_ratio: float =0.5, current_tiles: Set[Tuple[int, int]] = None, ignored_tiles: Set[Tuple[int, int]] = None) -> Set[Tuple[int, int]]:
    """Return grid points inside an n-point star polygon centered at (cx,cy).

    inner_ratio controls how deep the star indents (0..1). Uses polygon fill via point-in-polygon.
    """
    if current_tiles is None:
        current_tiles = set()
    if ignored_tiles is None:
        ignored_tiles = set()
    filled: Set[Tuple[int, int]] = set()
    if outer_radius <=0 or points <2:
        return filled
    verts = []
    total_verts = points *2
    for i in range(total_verts):
        angle = (i * math.pi) / points
        r = outer_radius if (i %2 ==0) else (outer_radius * inner_ratio)
        vx = cx + math.cos(angle) * r
        vy = cy + math.sin(angle) * r
        verts.append((vx, vy))

    # bounding box for polygon scan
    xs = [v[0] for v in verts]
    ys = [v[1] for v in verts]
    minx = int(math.floor(min(xs)))
    maxx = int(math.ceil(max(xs)))
    miny = int(math.floor(min(ys)))
    maxy = int(math.ceil(max(ys)))

    verts_t = tuple(verts)
    # test integer grid points using point at cell center for more consistent inclusion
    for gx in range(minx, maxx +1):
        for gy in range(miny, maxy +1):
            if (gx, gy) in current_tiles or (gx, gy) in ignored_tiles:
                continue
            px = gx +0.5
            py = gy +0.5
            if _point_in_polygon(px, py, verts_t):
                current_tiles.add((gx, gy))
                filled.add((gx, gy))

    logger.debug("make_filled_star: center=(%s,%s) outer_radius=%d points=%d filled=%d", cx, cy, outer_radius, points, len(filled))
    return filled
