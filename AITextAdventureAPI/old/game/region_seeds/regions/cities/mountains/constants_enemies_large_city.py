# Random hostile seed data for Ironveil Foundry (restored and normalized)
# Imports split into level files for maintainability
from .enemies_large.lv1to10 import RANDOM_HOSTILE_SEEDS as SEEDS_LV1TO10
from .enemies_large.lv11to20 import RANDOM_HOSTILE_SEEDS as SEEDS_LV11TO20
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
 "pickpocket", "pickpocket_gangling", "rumor_hawker", "brass_merchant",
 "forge_swash", "vagrant", "barfly", "brawler", "sniper", "anvil_comedian",
 ],

 "alley": [
 "thug", "bandit", "pickpocket_gangling", "jackal", "coal_rat", "moss_rat",
 "rogue", "raider", "wrecker_small",
 ],

 "bar": [
 "barfly", "tindermaid", "anvil_comedian", "brawler", "tinker_apprentice",
 ],

 "shop": [
 "clocksmith_archie", "tinker_apprentice", "brass_merchant", "broker_braggart",
 "fixer_tinker", "fixer_hacker", "fixer", "black_market_dealer", "weldling",
 ],

 "residence": [
 "vagrant", "wolf", "jackal", "coal_rat", "moss_rat", "old_vagrant",
 ],

 "business": [
 "foundry_watch", "rivet_fiend", "rivet_roper", "steam_collosus", "clockwork_colossus",
 "slag_golem", "iron_warden", "sunder_priest", "enforcer_heavy", "ganger_elder", "wrecker",
 "black_market_dealer", "broker_braggart",
 ],

 "inn": [
 "vagrant", "barfly", "brawler", "tindermaid", "anvil_comedian",
 ],

 "arcane": [
 "cultist", "slag_cultist", "wailing_bell_foundry", "umbral_stalker", "umbral_forgehound",
 "dream_eater", "dream_smoke", "elder_tentacle", "cinder_widow", "magma_serpent",
 ],
}