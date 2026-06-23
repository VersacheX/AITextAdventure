# Random hostile seed data for Brineward Harbor (mid-city)
# Each entry is a dict used by encounter/spawn systems.
from .enemies_mid.lv1to10 import SEEDS_LV1TO10
from .enemies_mid.lv11to20 import SEEDS_LV11TO20

RANDOM_HOSTILE_SEEDS = SEEDS_LV1TO10 + SEEDS_LV11TO20

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "mossling_pick", "salty_bum", "sea_gull_swarm", "bilge_brawler", "wallet_weed",
 "jarred_jasper", "lighthouse_busker", "rust_pelican",
 ],

 "alley": [
 "wallet_weed", "tide_knife", "barnacle_crab_mid", "brine_serpentling", "bilge_smuggler",
 "wharf_shade", "night_sneak", "hookhand_ron",
 ],

 "bar": [
 "salty_bum", "bilge_brawler", "tavern_jester", "lighthouse_busker", "hookhand_ron",
 ],

 "shop": [
 "jarred_jasper", "dockbroker_dave", "keel_fix", "rust_pelican",
 ],

 "residence": [
 "salty_bum", "barnacle_crab_mid", "keel_hound", "bilge_brawler",
 ],

 "business": [
 "dockbroker_dave", "harbor_bully", "quay_watch", "keel_fix", "dock_automat",
 ],

 "inn": [
 "bilge_brawler", "tavern_jester", "lighthouse_busker",
 ],

 "arcane": [
 "pier_cultist", "salt_vicar", "tide_wraith", "abyssal_cuttle", "brine_serpentling",
 "harbor_lich", "captain_tide", "kraken_whelp",
 ],
}