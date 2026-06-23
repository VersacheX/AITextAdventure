# Random hostile seed data for Gallows Rift (mid-city)
# Each entry is a dict used by encounter/spawn systems.
from .enemies_mid.lv1to10 import SEEDS_LV1TO10
from .enemies_mid.lv11to20 import SEEDS_LV11TO20

RANDOM_HOSTILE_SEEDS = SEEDS_LV1TO10 + SEEDS_LV11TO20

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "pickpocket", "ridge_runt", "bridge_hustler", "dreg_drunk", "barfly",
 "pub_poet", "rumor_monger", "brass_merchant", "tarn_tinker", "tinker_apprentice",
 "rift_runt_pick", "skew_ripper", "gallows_brawler",
 ],

 "alley": [
 "rift_cutpurse", "bandit", "undercity_rat", "alley_cat", "rift_runt_pick",
 "rogue", "rift_wolf", "cliff_viper", "cyber_hound", "umbral_stalker", "shadow_licker",
 ],

 "bar": [
 "barfly", "dreg_drunk", "pub_poet", "anvil_bard", "tinker_apprentice", "madam_fixit",
 ],

 "shop": [
 "pawn_guard", "antique_thief", "ledger_hound", "fixer", "fixer_hacker", "madam_fixit", "brass_merchant",
 ],

 "residence": [
 "ridge_runt", "rift_wolf", "rift_runt_pick", "rift_thief_lady",
 ],

 "business": [
 "pit_custodian", "ledger_hound", "corrupt_cop", "black_market_dealer", "enforcer", "enforcer_heavy",
 "rivet_fiend", "wrecker", "clockwork_colossus", "slag_golem", "forge_colossus", "pit_lieutenant",
 ],

 "inn": [
 "barfly", "dreg_drunk", "pub_poet", "anvil_bard",
 ],

 "arcane": [
 "rift_wraith", "spire_cultist", "slag_acolyte", "banshee", "mindflayer", "wraith_knight", "wandering_lich_apprentice",
 "dream_eater", "dream_smoke", "dream_eater2", "abyssal_serpent", "magma_serpent",
 ],
}