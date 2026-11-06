# Additional hostile seeds for expanded grassland locations
# Seeds are organized per-level in `grassland` submodules.
from game.region_seeds.regions.enemies.grassland.lv1to10 import SEEDS_LV1TO10
from game.region_seeds.regions.enemies.grassland.lv11to20 import SEEDS_LV11TO20
from game.region_seeds.regions.enemies.grassland.lv21to30 import SEEDS_LV21TO30
from game.region_seeds.regions.enemies.grassland.lv31to100 import SEEDS_LV31TO100

# Shared rarity-coverage roster (one seed of every rarity at each 5-level mark,
# Lv 5..100). Pulling this in fills the per-level gaps left in the grassland
# band files without duplicating seeds there. Reused across every grassland city
# size and the grassland wilderness.
from game.region_seeds.regions.cities.grassland.enemies_shared import (
    RANDOM_HOSTILE_SEEDS as SHARED_GRASSLAND_HOSTILES,
)

RANDOM_HOSTILE_SEEDS = []
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV1TO10)
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV11TO20)
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV21TO30)
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV31TO100)
RANDOM_HOSTILE_SEEDS.extend(SHARED_GRASSLAND_HOSTILES)

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