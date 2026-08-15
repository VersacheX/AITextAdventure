# Random hostile seed data for Frostgate Spire (large-city)
# Each entry is a dict used by encounter/spawn systems.
from .enemies_large.lv1to10 import SEEDS_LV1TO10
from .enemies_large.lv11to20 import SEEDS_LV11TO20
from .enemies_large.lv21to30 import RANDOM_HOSTILE_SEEDS as SEEDS_LV21TO30
from .enemies_large.lv31to40 import RANDOM_HOSTILE_SEEDS as SEEDS_LV31TO40
from .enemies_large.lv41to50 import RANDOM_HOSTILE_SEEDS as SEEDS_LV41TO50
from .enemies_large.lv51to60 import RANDOM_HOSTILE_SEEDS as SEEDS_LV51TO60
from .enemies_large.lv61to70 import RANDOM_HOSTILE_SEEDS as SEEDS_LV61TO70
from .enemies_large.lv71to80 import RANDOM_HOSTILE_SEEDS as SEEDS_LV71TO80
from .enemies_large.lv81to90 import RANDOM_HOSTILE_SEEDS as SEEDS_LV81TO90
from .enemies_large.lv91to100 import RANDOM_HOSTILE_SEEDS as SEEDS_LV91TO100

RANDOM_HOSTILE_SEEDS = (SEEDS_LV1TO10 + SEEDS_LV11TO20 + SEEDS_LV21TO30 + SEEDS_LV31TO40 +
                        SEEDS_LV41TO50 + SEEDS_LV51TO60 + SEEDS_LV61TO70 + SEEDS_LV71TO80 +
                        SEEDS_LV81TO90 + SEEDS_LV91TO100)

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "frostling_scrub", "frostling_scrub_2", "ice_mumbler", "ice_mumbler_older",
 "frozen_gull", "frozen_gull_fledgling", "tome_trader", "tome_trader_scribe",
 "snow_merchant_bard", "snow_merchant_bard_senior",
 ],

 "alley": [
 "snow_slip", "snow_slip_trickster", "shiver_blade", "shiver_blade_cold",
 "spire_shade", "spire_shade_lurker", "night_shank", "night_shank_assassin",
 ],

 "bar": [
 "glacier_brawler", "glacier_brawler_young", "frozen_jester", "frozen_jester_prince",
 "snow_merchant_bard", "snow_merchant_bard_senior",
 ],

 "shop": [
 "tome_trader", "tome_trader_scribe", "spire_broker", "spire_broker_merchant",
 "odd_nick",
 ],

 "residence": [
 "ice_hewer", "ice_hewer_apprentice", "frostling_scrub", "frostling_scrub_2",
 "snow_hound", "snow_hound_alpha", "ice_crab", "ice_crab_larval",
 ],

 "business": [
 "spire_broker", "spire_broker_merchant", "frost_fix", "frost_fix_rogue",
 "cold_smuggler", "cold_smuggler_band", "spire_watch", "spire_watch_sergeant",
 "frost_enforcer", "frost_enforcer_veteran",
 ],

 "inn": [
 "glacier_brawler", "glacier_brawler_young", "frozen_jester", "frozen_jester_prince",
 "snow_merchant_bard",
 ],

 "arcane": [
 "rime_cultist", "rime_cultist_zealot", "ice_vicar", "ice_vicar_high",
 "tide_banshee", "tide_banshee_weeper", "glacier_cuttle", "glacier_cuttle_guard",
 "lorekeeper_frost", "lorekeeper_frost_archivist", "captain_glacier", "captain_glacier_warden",
 "kraken_ice_whelp", "kraken_ice_whelp_giant", "iron_spire_colossus", "iron_spire_colossus_guard",
 "frostwork_gull", "frostwork_gull_scout",
 ],
}