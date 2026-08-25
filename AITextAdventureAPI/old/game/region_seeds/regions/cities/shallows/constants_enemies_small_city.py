# Random hostile seed data for Tidekin Cove (small-city)
# Each entry is a dict used by encounter/spawn systems.
from .enemies_small.lv1to10 import SEEDS_LV1TO10
from .enemies_small.lv11to20 import SEEDS_LV11TO20
from .enemies_small.lv21to30 import RANDOM_HOSTILE_SEEDS as SEEDS_LV21TO30
from .enemies_small.lv31to40 import RANDOM_HOSTILE_SEEDS as SEEDS_LV31TO40
from .enemies_small.lv41to50 import RANDOM_HOSTILE_SEEDS as SEEDS_LV41TO50
from .enemies_small.lv51to60 import RANDOM_HOSTILE_SEEDS as SEEDS_LV51TO60
from .enemies_small.lv61to70 import RANDOM_HOSTILE_SEEDS as SEEDS_LV61TO70
from .enemies_small.lv71to80 import RANDOM_HOSTILE_SEEDS as SEEDS_LV71TO80
from .enemies_small.lv81to90 import RANDOM_HOSTILE_SEEDS as SEEDS_LV81TO90
from .enemies_small.lv91to100 import RANDOM_HOSTILE_SEEDS as SEEDS_LV91TO100

# Shared shallows-region rarity-coverage fill seeds (single package import).
# Efficient roster: same seeds used by every shallows city size.
from .enemies_shared import RANDOM_HOSTILE_SEEDS as RARITY_FILL_HOSTILES

RANDOM_HOSTILE_SEEDS = (SEEDS_LV1TO10 + SEEDS_LV11TO20 + SEEDS_LV21TO30 + SEEDS_LV31TO40 +
                        SEEDS_LV41TO50 + SEEDS_LV51TO60 + SEEDS_LV61TO70 + SEEDS_LV71TO80 +
                        SEEDS_LV81TO90 + SEEDS_LV91TO100 + RARITY_FILL_HOSTILES)

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "mudling_scraper", "tide_seller", "cove_gull", "dockrow_heaver", "slick_quart",
 "odd_nick", "dried_castaway", "rust_gull", "berth_hands",
 ],

 "alley": [
 "slick_quart", "shankling", "small_crab", "eellet", "bilge_runner",
 "alley_shade", "grease_snare",
 ],

 "bar": [
 "barnacle_banger", "berth_hands", "tide_clown", "dried_castaway", "harpoon_knot",
 ],

 "shop": [
 "odd_nick", "quayside_arnie", "keel_runner", "rust_gull", "tide_seller",
 ],

 "residence": [
 "mudling_scraper", "small_crab", "rock_pup", "barnacle_banger",
 ],

 "business": [
 "quayside_arnie", "harbor_brawler", "tide_watch", "keel_runner", "tin_watchman",
 ],

 "inn": [
 "berth_hands", "barnacle_banger", "tide_clown", "dried_castaway",
 ],

 "arcane": [
 "tide_wisp", "siren_lure", "brine_warden", "keeper_knell", "tin_watchman",
 ],
}