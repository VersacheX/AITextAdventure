"""Region fractal helpers

Provides simple, deterministic fractal-like mask generation and helpers to
carve that shape into a `City` instance. The goal is to let the region
builder optionally drive expansion toward a designed shape (blob, ring,
fractal-like noise) while still respecting `main_tiles` and `ignored_set`.

API:
- `generate_fractal_mask(center, approx_tiles, seed, scale=6.0, octaves=3)`
	-> List[(x,y)] absolute coordinates ordered by score (highest first).
- `carve_fractal_shape(rc, mask, main_tiles, ignored_set, region_tiles, max_size=None)`
	-> Add tiles from mask into `rc.tiles` and `region_tiles`, return number added.

This implementation uses a simple multi-octave value function (sin/cos +
hash perturbation) to produce organic patterns without external deps.
"""
from typing import Tuple, Set, Iterable, List
import math
import logging

logger = logging.getLogger(__name__)

# small primes for hashing
_PRIME_X =73856093
_PRIME_Y =19349663


def _hash_float(x: int, y: int, seed: int) -> float:
	"""Deterministic pseudo-random float in [0,1) based on integer coords."""
	h = (x * _PRIME_X) ^ (y * _PRIME_Y) ^ seed
	h = h &0xFFFFFFFF
	return float(h) / float(0x100000000)


def generate_fractal_mask(
	center: Tuple[int, int],
	approx_tiles: int,
	seed: int,
	scale: float =6.0,
	octaves: int =3,
	padding: int =2,
) -> List[Tuple[int, int]]:
	"""Generate an ordered list of coordinates forming a fractal-like mask.

	- center: (cx,cy) absolute center of the mask
	- approx_tiles: desired number of tiles (used to compute radius)
	- seed: deterministic seed
	- scale: base spatial frequency
	- octaves: number of frequencies to combine
	- padding: extra radius padding to give selection room

	Returns a list of absolute (x,y) coordinates ordered from highest to
	lowest "score" (so callers can iterate and place until they reach a
	desired tile count).
	"""
	cx, cy = center
	if approx_tiles <=0:
		return []

	# estimate radius from desired area (use circle approximation)
	radius = max(1, int(math.ceil(math.sqrt(float(approx_tiles) / math.pi))))
	radius += padding

	candidates: List[Tuple[Tuple[int, int], float]] = []

	# precompute octave scales/weights
	scales = [scale * (2 ** i) for i in range(octaves)]
	weights = [1.0 / (2 ** i) for i in range(octaves)]

	for dy in range(-radius, radius +1):
		yy = cy + dy
		for dx in range(-radius, radius +1):
			xx = cx + dx
			# constrain to circle for compactness
			if dx * dx + dy * dy > radius * radius:
				continue
			# compute multi-octave value
			val =0.0
			for s, w in zip(scales, weights):
				# sin/cos waves at different frequencies create bands
				val += w * (
					math.sin((dx / s) + (seed *0.0001))
					+ math.cos((dy / s) - (seed *0.00007))
				)
			# add small hashed perturbation to introduce splotchiness
			val += (0.5 - _hash_float(xx, yy, seed)) *0.35
			candidates.append(((xx, yy), val))

	# sort candidates by score descending
	candidates.sort(key=lambda t: t[1], reverse=True)

	# return only coordinates ordered by score
	return [coord for coord, _ in candidates]


def carve_fractal_shape(
	rc,
	mask: Iterable[Tuple[int, int]],
	main_tiles: Set[Tuple[int, int]],
	ignored_set: Set[Tuple[int, int]],
	region_tiles: Set[Tuple[int, int]],
	max_size: int = None,
) -> int:
	"""Attempt to carve tiles from `mask` into `rc` and `region_tiles`.

	- rc: City instance
	- mask: ordered iterable of (x,y) candidate positions (highest priority first)
	- main_tiles, ignored_set: sets to respect (do not overwrite)
	- region_tiles: set to add new coordinates
	- max_size: stop when region_tiles reaches this many elements (if provided)

	Returns number of tiles actually added to rc/region_tiles.
	"""
	added =0
	max_sz = max_size if max_size is not None else getattr(rc, "max_size", None)

	for (x, y) in mask:
		if max_sz and len(region_tiles) >= max_sz:
			break
		if (x, y) in main_tiles or (x, y) in ignored_set or (x, y) in region_tiles:
			continue
		# attempt to create/get tile using City's generator
		
		t = rc.get_or_create_tile(x, y)
		# if tile created or exists, record it
		if t is not None:
			region_tiles.add((x, y))
			added +=1

	logger.debug("[region_fractal_service] carved %d tiles from mask (max_size=%s)", added, max_sz)
	return added
