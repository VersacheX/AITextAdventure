# Random hostile seed data for Tidekin Cove (small-city)
# Each entry is a dict used by encounter/spawn systems.
from .enemies_small.lv1to10 import SEEDS_LV1TO10
from .enemies_small.lv11to20 import SEEDS_LV11TO20

RANDOM_HOSTILE_SEEDS = SEEDS_LV1TO10 + SEEDS_LV11TO20

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