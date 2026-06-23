# Additional hostile seeds for expanded grassland locations
# Seeds are organized per-level in `grassland` submodules.
from game.region_seeds.regions.enemies.grassland.lv1to10 import SEEDS_LV1TO10
from game.region_seeds.regions.enemies.grassland.lv11to20 import SEEDS_LV11TO20

RANDOM_HOSTILE_SEEDS = []
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV1TO10)
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV11TO20)

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