# Random hostile seed data for Brineward Harbor (large-city)
# Each entry is a dict used by encounter/spawn systems.
from .enemies_large.lv1to10 import SEEDS_LV1TO10
from .enemies_large.lv11to20 import SEEDS_LV11TO20

RANDOM_HOSTILE_SEEDS = SEEDS_LV1TO10 + SEEDS_LV11TO20

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "dock_rat", "soggy_seller", "gull_peck", "berth_brawler", "pier_cutpurse",
 "lantern_balladeer", "curio_dealer", "quayside_broker", "rustwork_gull", "tide_hound",
 ],

 "alley": [
 "baitbox_bandit", "brine_smuggler", "barnacle_crab", "void_eel", "dock_shade",
 "night_oiler", "deck_swabby", "pier_cutpurse",
 ],

 "bar": [
 "berth_brawler", "deck_swabby", "shelfboss_sailor", "salty_comedian", "lantern_balladeer", "harpooner",
 ],

 "shop": [
 "curio_dealer", "quayside_broker", "soggy_seller", "brine_smuggler", "rustwork_gull",
 ],

 "residence": [
 "dock_rat", "barnacle_crab", "tide_hound", "berth_brawler",
 ],

 "business": [
 "quayside_broker", "harbor_baron", "pier_enforcer", "dock_fixer", "rustwork_colossus",
 ],

 "inn": [
 "deck_swabby", "berth_brawler", "lantern_balladeer", "salty_comedian",
 ],

 "arcane": [
 "abyssal_serpent_new", "sea_banshee", "siren_songster", "tide_cultist", "slag_priest",
 "brine_krakenling", "captain_abyss", "lighthouse_keeper", "rustwork_colossus", "night_oiler", "dock_shade",
 ],
}