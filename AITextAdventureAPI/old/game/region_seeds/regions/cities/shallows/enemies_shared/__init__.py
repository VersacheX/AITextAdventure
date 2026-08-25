# Shallows shared hostile roster package.
#
# Aggregates every rarity-coverage fill band into a single RANDOM_HOSTILE_SEEDS
# list so city aggregators (large / mid / small) can pull the full shared roster
# with ONE import. Efficient design: uniform multiple-of-5 ladder per rarity,
# with only the anchors that NO shallows city reports as a gap dropped.

from game.region_seeds.regions.cities.shallows.enemies_shared.lv1to20b_rarity_fill import RANDOM_HOSTILE_SEEDS as _LV1TO20
from game.region_seeds.regions.cities.shallows.enemies_shared.lv21to40b_rarity_fill import RANDOM_HOSTILE_SEEDS as _LV21TO40
from game.region_seeds.regions.cities.shallows.enemies_shared.lv41to60b_rarity_fill import RANDOM_HOSTILE_SEEDS as _LV41TO60
from game.region_seeds.regions.cities.shallows.enemies_shared.lv61to80_rarity_fill import RANDOM_HOSTILE_SEEDS as _LV61TO80
from game.region_seeds.regions.cities.shallows.enemies_shared.lv81to100_rarity_fill import RANDOM_HOSTILE_SEEDS as _LV81TO100

RANDOM_HOSTILE_SEEDS = (
    (_LV1TO20 or [])
    + (_LV21TO40 or [])
    + (_LV41TO60 or [])
    + (_LV61TO80 or [])
    + (_LV81TO100 or [])
)

__all__ = ["RANDOM_HOSTILE_SEEDS"]
