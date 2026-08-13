# Random hostile seed data for Thornshade Hamlet (small forest village).
# Each entry is a dict used by encounter/spawn systems.

from .enemies_small.lv1to10 import RANDOM_HOSTILE_SEEDS as LV1TO10
from .enemies_small.lv11to20 import RANDOM_HOSTILE_SEEDS as LV11TO20
from .enemies_small.lv21to100 import RANDOM_HOSTILE_SEEDS as LV21TO100

RANDOM_HOSTILE_SEEDS = LV1TO10 + LV11TO20 + LV21TO100

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "stump_rat", "thatch_runner", "twig_tot", "nocturne_wisp", "moss_barker", "barkbard",
 ],

 "alley": [
 "sapling_swindler", "stump_thug", "fen_spider_small", "hollow_raider", "leaf_hound",
 ],

 "bar": [
 "barkbard", "moss_barker", "barnacle_bruiser", "thatch_runner", "nettlescribe",
 ],

 "shop": [
 "nettlescribe", "ledger_guard", "sapling_swindler", "twig_tot",
 ],

 "residence": [
 "cottage_matron_small", "leaf_hound", "stump_thug", "stump_rat",
 ],

 "business": [
 "ledger_guard", "briar_golem_small", "elder_revenant_small", "hollow_raider",
 ],

 "inn": [
 "moss_barker", "thatch_runner", "barkbard", "nocturne_wisp", "fen_phantom", "herbal_haglet",
 ],
}