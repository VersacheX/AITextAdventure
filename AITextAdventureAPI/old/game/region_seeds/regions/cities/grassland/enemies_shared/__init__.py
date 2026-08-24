# Grassland shared hostile roster package.
#
# Aggregates every rarity-coverage fill band into a single RANDOM_HOSTILE_SEEDS
# list so city aggregators (large / mid / small) and the grassland wilderness
# can pull the full shared roster with ONE import instead of importing each
# band module individually:
#
#     from game.region_seeds.regions.cities.grassland.enemies_shared import (
#         RANDOM_HOSTILE_SEEDS as SHARED_GRASSLAND_HOSTILES,
#     )
#
# This roster is self-sufficient for ANY grassland zone: it places one seed of
# every rarity at each 5-level mark (Lv 5..100), so every validator sliding
# window is covered even in the sparse small city. When the same seed id
# surfaces in more than one zone it resolves to identical data, so there is no
# integrity concern from the overlap.

from game.region_seeds.regions.cities.grassland.enemies_shared.lv1to20_rarity_fill import RANDOM_HOSTILE_SEEDS as _LV1TO20
from game.region_seeds.regions.cities.grassland.enemies_shared.lv21to40_rarity_fill import RANDOM_HOSTILE_SEEDS as _LV21TO40
from game.region_seeds.regions.cities.grassland.enemies_shared.lv41to60_rarity_fill import RANDOM_HOSTILE_SEEDS as _LV41TO60
from game.region_seeds.regions.cities.grassland.enemies_shared.lv61to80_rarity_fill import RANDOM_HOSTILE_SEEDS as _LV61TO80
from game.region_seeds.regions.cities.grassland.enemies_shared.lv81to100_rarity_fill import RANDOM_HOSTILE_SEEDS as _LV81TO100

RANDOM_HOSTILE_SEEDS = (
    (_LV1TO20 or [])
    + (_LV21TO40 or [])
    + (_LV41TO60 or [])
    + (_LV61TO80 or [])
    + (_LV81TO100 or [])
)

__all__ = ["RANDOM_HOSTILE_SEEDS"]
