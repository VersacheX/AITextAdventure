#!/usr/bin/env python3
"""Run a hostile generator to create test hostiles and display side-by-side.
Usage: python -m old.run_hostile_generator or run this file directly.
"""
import argparse
import random
from typing import List, Dict, Any

from combat_balancing_simulation.hostile_seed_engine import (
    gather_all_seeds,
    region_key_to_region_name,
    estimate_stats_from_seed,
    _instantiate_random_hostile_from_seed,
    generate_hostile_from_legacy_seed
)
from combat_balancing_simulation.hostile_details_screen import format_hostile_summary


def pick_hostiles_from_region(count: int = 4, region: str = None, seed: int = None, level: int = 10) -> List[Any]:
    seeds = gather_all_seeds()
    rng = random.Random(seed)
    # group seeds by region_key -> region name
    regions: Dict[str, List] = {}
    for rk, s in seeds:
        rname = region_key_to_region_name(rk)
        regions.setdefault(rname, []).append((rk, s))

    if region is None:
        # pick random region that has at least count seeds
        viable = [r for r, items in regions.items() if len(items) >= count]
        if not viable:
            # fallback to any region
            viable = list(regions.keys())
        if not viable:
            return []
        region = rng.choice(viable)

    region_items = regions.get(region, [])
    if not region_items:
        return []

    # pick `count` items from the same region
    picked = rng.sample(region_items, min(count, len(region_items)))
    hostiles: List[Any] = []
    for rk, seed_dict in picked:
        lvl = int(seed_dict.get('min_spawn_level', level) or level)
        # derived needs to be transformed into a RandomHostile here manually as there is no mapping yet

        # instantiate a RandomHostile from the raw seed and derived level
        rh = generate_hostile_from_legacy_seed(seed_dict, lvl)  # for side effects / validation`
        #rh = _instantiate_random_hostile_from_seed(seed_dict, lvl)
        hostiles.append(rh)
        
    return hostiles


def main() -> None:
    parser = argparse.ArgumentParser(description="Run hostile generator for combat balancing tests")
    parser.add_argument("--seed", type=int, default=None, help="Random seed (int)")
    parser.add_argument("--count", type=int, default=3, help="Number of hostiles to generate")
    parser.add_argument("--region", default=None, help="Region name (e.g. DESERT, FOREST) to restrict hostiles")
    parser.add_argument("--level", type=int, default=10, help="Target level for hostile stat estimation")

    args = parser.parse_args()

    hostiles = pick_hostiles_from_region(count=args.count, region=args.region, seed=args.seed, level=args.level)
    if not hostiles:
        print("No hostiles available for the selected region")
        return

    # format boxes
    box_width = 60
    all_boxes = [format_hostile_summary(h, box_width) for h in hostiles]
    max_lines = max(len(b) for b in all_boxes)
    for b in all_boxes:
        while len(b) < max_lines:
            b.append(' ' * box_width)

    for i in range(max_lines):
        row = ' '.join(b[i] for b in all_boxes)
        print(row)


if __name__ == '__main__':
    main()
