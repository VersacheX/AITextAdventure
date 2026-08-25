# Random hostile seed data for Brineward Harbor (large-city)
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

# Shared shallows-region rarity-coverage fill seeds (single package import).
# Efficient roster: same seeds used by every shallows city size.
from .enemies_shared import RANDOM_HOSTILE_SEEDS as RARITY_FILL_HOSTILES

RANDOM_HOSTILE_SEEDS = (SEEDS_LV1TO10 + SEEDS_LV11TO20 + SEEDS_LV21TO30 + SEEDS_LV31TO40 +
                        SEEDS_LV41TO50 + SEEDS_LV51TO60 + SEEDS_LV61TO70 + SEEDS_LV71TO80 +
                        SEEDS_LV81TO90 + SEEDS_LV91TO100 + RARITY_FILL_HOSTILES)

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