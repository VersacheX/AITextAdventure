# Reworked hostile seed data for the Great Dune City (large desert metropolis).
# Level1-10 seeds were split into a separate module for maintainability.
# This module imports those and appends higher-level seeds.

from game.region_seeds.regions.cities.desert.enemies_large.lv1to10 import RANDOM_HOSTILE_SEEDS as LV1TO10_HOSTILES
from game.region_seeds.regions.cities.desert.enemies_large.lv11to20 import RANDOM_HOSTILE_SEEDS as LV11TO20_HOSTILES
from game.region_seeds.regions.cities.desert.enemies_large.lv21to30 import RANDOM_HOSTILE_SEEDS as LV21TO30_HOSTILES

# Higher-tier seeds (min_spawn_level >10)
HIGHER_LEVEL_SEEDS = [
]

# Compose final seed list: include level1-10 seeds first, then higher-level seeds
RANDOM_HOSTILE_SEEDS = []
RANDOM_HOSTILE_SEEDS.extend(LV1TO10_HOSTILES or [])
RANDOM_HOSTILE_SEEDS.extend(LV11TO20_HOSTILES or [])
RANDOM_HOSTILE_SEEDS.extend(LV21TO30_HOSTILES or [])
RANDOM_HOSTILE_SEEDS.extend(HIGHER_LEVEL_SEEDS or [])

                            

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 # common -> mid threats seen on main thoroughfares
 "dune_brawler", "sand_rat", "sand_jackal", "sand_pick", "drift_vagrant", "dune_hound",
 "dune_dame", "rumor_monger", "neon_merchant", "tunnel_viper", "sand_sniper",
 "umbral_stalker", "dune_overlord", "plank_marauder", "tattooed_brigand", "courier_girl",
 "marksman_drifter", "oasis_smuggler", "scorpion_enforcer", "abyssal_serpent",
 ],

 "alley": [
 # ambush-prone & occult contacts
 "plank_marauder", "dune_brawler", "sand_rat", "undercity_flea", "alley_cat", "sand_pick",
 "void_spider", "oasis_smuggler", "tattooed_brigand", "plague_stoker", "caravan_fixer",
 "spoon_beggar", "wreck_khan", "net_hag", "mindflayer", "elder_tentacle", "mirage_stalker",
 ],

 "bar": [
 # social hotbeds and brawls
 "barfly", "rival_barkeep", "dune_brawler", "market_bouncer", "plank_marauder",
 "dune_dame", "sand_flapper", "marksman_drifter", "femme_fatale", "wrench_madam", "sly_madam",
 "salt_marshall", "oasis_smuggler", "dune_overlord", "glass_wrecker", "mirage_stalker",
 "treasure_snatcher", "black_dune_dealer",
 ],

 "shop": [
 # thieves, guards and shady fixers near commerce
 "sand_pick", "treasure_snatcher", "vault_watcher", "caravan_fixer", "net_hag", "oasis_smuggler",
 "neon_merchant", "black_dune_dealer", "scorpion_enforcer",
 ],

 "residence": [
 # homes, small hauntings and domestic defenders
 "sand_rat", "vault_watcher", "drift_vagrant", "spoon_beggar", "tough_grammy", "maternal_guardian",
 "sly_madam", "matron_hire", "baron_guard", "dune_dame",
 ],

 "business": [
 # corporate and organized crime presence, higher-tier threats
 "salt_marshall", "vault_watcher", "net_hag", "servo_sentinel", "black_dune_dealer",
 "wreck_khan", "dune_overlord", "baron_guard", "dune_lieutenant", "clockwork_colossus",
 "revenant_queen", "celestial_watcher", "mindflayer", "dream_eater",
 ],

 "inn": [
 # travelers, hauntings, and oddities
 "drift_vagrant", "barfly", "courier_girl", "tough_grammy", "matron_hire", "spectral_hag",
 "wailing_banshee", "neon_siren", "mirage_stalker", "lich_apprentice",
 ]
}