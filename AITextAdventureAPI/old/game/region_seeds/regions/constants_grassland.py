
REGION_SETTINGS = {
	"road_spacing": 20,
	"alley_spacing": 30,
	"alley_offset": 0,
	"max_size": 2400,
	"population_density": 0.2,
	"hasResidence": False,
	"hasBusiness": False,
	"hasShops": False,
	"hasBar": True,
	"hasInn": False,
	"hasHyperway": False,
	"hasOther1": False,
	"hasOther2": False,
	"display_name": "The hills",
	"region_name": "grassland" ,
}

OPEN_AREA_TILE = "▒"
IMPASSABLE_TILE = "¤"
IMPASSABLE_CHANCE = 0.05

# Import per-level seed lists
from game.region_seeds.regions.enemies.grassland.lv1to10 import SEEDS_LV1TO10
from game.region_seeds.regions.enemies.grassland.lv11to20 import SEEDS_LV11TO20

# Compose randomized hostile seeds for the grassland region
RANDOM_HOSTILE_SEEDS = []
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV1TO10)
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV11TO20)

# Ensure ordering by min_spawn_level for predictable dispersal
RANDOM_HOSTILE_SEEDS.sort(key=lambda s: s.get('min_spawn_level',0))

# If there are fewer than20 hostiles, this is a signal to add more seeds to the per-level files.
# For now, keep the current list but expose it for callers.

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [],
 "alley": [],
 "bar": [],
 "shop": [],
 "residence": [],
 "business": [],
 "inn": [],
}

# Re-export common region assets so callers can import a single module
# Example: from game.region_seeds.constants_grassland import REGION_SETTINGS, BUILDINGS, RANDOM_HOSTILE_SEEDS
__all__ = [
 'REGION_SETTINGS',
 'BUILDINGS',
 'DRINK_MENU',
 'SUBLOC_MAP',
 'SUBLOCATION_DEFS',
 'RANDOM_HOSTILE_SEEDS',
 'RANDOM_HOSTILE_LINKS',
 "OPEN_AREA_TILE"
]
