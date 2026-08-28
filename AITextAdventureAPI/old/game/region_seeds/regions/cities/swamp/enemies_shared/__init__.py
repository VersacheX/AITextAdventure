#
# Aggregates every swamp rarity-coverage fill band into a single
# RANDOM_HOSTILE_SEEDS list so city aggregators (large / mid / small) can pull
# the full shared roster with ONE import. Efficient design: multiple-of-5 ladder
# per rarity, with only the Lv 1-20 anchors that NO swamp zone reports as a gap
# dropped (common Lv 15/20, uncommon Lv 5/10/15, rare Lv 15, superrare Lv 10/20).

from game.region_seeds.regions.cities.swamp.enemies_shared.lv1to20_rarity_fill import RANDOM_HOSTILE_SEEDS as _LV1TO20
from game.region_seeds.regions.cities.swamp.enemies_shared.lv21to40_rarity_fill import RANDOM_HOSTILE_SEEDS as _LV21TO40
from game.region_seeds.regions.cities.swamp.enemies_shared.lv41to60_rarity_fill import RANDOM_HOSTILE_SEEDS as _LV41TO60
from game.region_seeds.regions.cities.swamp.enemies_shared.lv61to80_rarity_fill import RANDOM_HOSTILE_SEEDS as _LV61TO80
from game.region_seeds.regions.cities.swamp.enemies_shared.lv81to100_rarity_fill import RANDOM_HOSTILE_SEEDS as _LV81TO100

RANDOM_HOSTILE_SEEDS = (
    (_LV1TO20 or [])
    + (_LV21TO40 or [])
    + (_LV41TO60 or [])
    + (_LV61TO80 or [])
    + (_LV81TO100 or [])
)

__all__ = ["RANDOM_HOSTILE_SEEDS"]
