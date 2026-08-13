# Additional hostile seeds for expanded snow locations
# Seeds are organized per-level in `snow` submodules.
from game.region_seeds.regions.enemies.snow.lv1to10 import SEEDS_LV1TO10
from game.region_seeds.regions.enemies.snow.lv11to20 import SEEDS_LV11TO20
from game.region_seeds.regions.enemies.snow.lv21to30 import SEEDS_LV21TO30
from game.region_seeds.regions.enemies.snow.lv31to100 import SEEDS_LV31TO100

RANDOM_HOSTILE_SEEDS = []
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV1TO10)
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV11TO20)
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV21TO30)
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV31TO100)

# Ensure ordering by min_spawn_level for predictable dispersal
RANDOM_HOSTILE_SEEDS.sort(key=lambda s: s.get('min_spawn_level', 0))

# Ensure ordering by min_spawn_level for predictable dispersal
RANDOM_HOSTILE_SEEDS.sort(key=lambda s: s.get('min_spawn_level',0))

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