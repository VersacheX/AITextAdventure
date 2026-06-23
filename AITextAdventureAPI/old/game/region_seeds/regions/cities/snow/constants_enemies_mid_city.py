# Random hostile seed data for Hailward Hold (mid-city)
# Each entry is a dict used by encounter/spawn systems.
from .enemies_mid.lv1to10 import SEEDS_LV1TO10
from .enemies_mid.lv11to20 import SEEDS_LV11TO20

RANDOM_HOSTILE_SEEDS = SEEDS_LV1TO10 + SEEDS_LV11TO20

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
# Use building type names (matching normalized building types), plus 'street' and 'alley'.
# Spawn links using new hold-themed hostile ids
RANDOM_HOSTILE_LINKS = {
 "street": [
 "furrow_scraper", "furrow_scraper_old", "smoked_peddler", "smoked_peddler_sly",
 "hanger_gull", "hanger_gull_old", "sleet_culler", "fjord_gardener",
 "glacial_courier", "skald_singer", "salted_haggle", "barrow_thug",
 "pack_frostfox", "rooftop_ranger", "hold_bard", "frozen_fool",
 ],

 "alley": [
 "fur_lurker", "shard_knife", "rune_apprentice", "rift_scavenger", "rift_wrecker",
 "branch_mole", "alley_wraith", "night_cutter", "runebinder", "glacier_stalker", "vault_scrivener", "rime_eel",
 ],

 "bar": [
 "longhouse_brawler", "rune_smasher", "ice_bowler", "frozen_fool", "hold_bard", "skald_singer",
 ],

 "shop": [
 "tally_clerk", "rune_merchant", "rune_apprentice", "vault_scrivener", "keel_guard", "gear_gull",
 ],

 "residence": [
 "fjord_hound", "ice_claw", "ice_bear_pup", "pack_frostfox", "sleet_culler", "furrow_scraper",
 ],

 "business": [
 "hold_fixer", "fjord_smuggler", "hold_watch", "fell_sargent", "frostwork_sentinel",
 "iron_guardian", "coldwright", "runekeeper_warden", "rift_wrecker",
 ],

 "inn": [
 "longhouse_brawler", "hold_bard", "frozen_fool", "skald_singer", "glacial_courier",
 ],

 "arcane": [
 "rime_shaman", "vicar_rime", "hold_banshee", "glacial_cuttle", "northern_banshee",
 "abyssal_reaver", "cairn_keeper", "captain_rime", "ice_seraph", "frost_herald",
 "wight_captain", "tide_jaw", "glacier_stalker", "runekeeper_warden",
 ],
}