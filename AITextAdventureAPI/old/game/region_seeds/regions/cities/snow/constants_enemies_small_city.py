# Random hostile seed data for Bleakwatch Outpost (small-city)
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

RANDOM_HOSTILE_SEEDS = (SEEDS_LV1TO10 + SEEDS_LV11TO20 + SEEDS_LV21TO30 + SEEDS_LV31TO40 +
                        SEEDS_LV41TO50 + SEEDS_LV51TO60 + SEEDS_LV61TO70 + SEEDS_LV71TO80 +
                        SEEDS_LV81TO90 + SEEDS_LV91TO100)

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "frost_scrapper", "rusty_peddler", "rusty_peddler_sly", "outpost_gull", "outpost_bard",
 "shanty_chorus", "snow_mime", "salt_seller", "slippery_tourist", "ledger_lout", "fishing_bonker",
 ],

 "alley": [
 "locker_cutpurse", "shiver_snip", "cache_smuggler", "alley_skulk", "rime_serpentling",
 "night_shank_small", "drift_wolf_alpha", "ice_gecko",
 ],

 "bar": [
 "hutsman", "sled_pounder", "frozen_clown", "outpost_bard", "rusty_peddler_sly", "shanty_chorus", "beacon_tender",
 ],

 "shop": [
 "ledger_lout", "supply_broker", "kelp_vendor", "watch_repair", "rusty_peddler", "gear_drake",
 ],

 "residence": [
 "frost_scrapper", "ice_crab_small", "pack_hound", "frost_miner", "furrow_old", "drifting_hermit",
 ],

 "business": [
 "supply_broker", "watch_sergeant", "watch_recruit", "watch_repair", "iron_watchman", "gear_drake", "cache_smuggler",
 ],

 "inn": [
 "hutsman", "frozen_clown", "outpost_bard", "shanty_chorus", "sled_pounder", "salted_ranger",
 ],

 "arcane": [
 "altar_believer", "vicar_watch", "watch_wail", "glacier_crawler", "barnacle_shaman", "fog_whisper",
 "ice_weaver", "blubber_widow", "sleet_illusionist", "tundra_gnasher", "keeper_wraith", "crumbled_ogre",
 "captain_bleak", "bleak_keeper", "ice_harpooner", "bone_watchman",
 ],
}