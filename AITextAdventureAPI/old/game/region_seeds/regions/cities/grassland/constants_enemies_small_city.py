# Random hostile seed data for Quantford Hollow (restored + expanded)
# Each entry is a dict used by encounter/spawn systems.
from .enemies_small.lv1to10 import RANDOM_HOSTILE_SEEDS as _LV1
from .enemies_small.lv11to20 import RANDOM_HOSTILE_SEEDS as _LV11
from .enemies_small.lv21to100 import RANDOM_HOSTILE_SEEDS as _LV21

RANDOM_HOSTILE_SEEDS = _LV1 + _LV11 + _LV21

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "pickpocket", "stump_thief", "market_bandit", "old_vagrant", "barfly", "rumor_monger",
 "streetwise_dame", "courier_girl", "moss_rat", "rat", "alley_cat", "loft_watch", "hedge_thug", "tattooed_thug",
 "sniper", "cyber_hound", "peasant_fixit",
 ],

 "alley": [
 "mole_troublemaker", "beggar_blade", "stump_thief", "thatch_rogue", "pickpocket", "void_spider",
 "wrecker_small", "fixer", "shadow_assassin", "rogue", "raider", "undercity_rat",
 ],

 "bar": [
 "barn_brawler", "brawler", "ledger_guard", "thatch_rogue", "cottage_matron", "rival_bartender",
 "nightclub_bouncer", "tough_granny", "siren", "neon_dancer", "neon_siren",
 ],

 "shop": [
 "curio_fox", "ladys_cutpurse_small", "antique_thief", "pawn_guard", "fixer_tinker", "fixer_hacker",
 "fixer", "smuggler", "black_curio_peddler", "madam_fixit", "sly_madam", "lady_rogue", "gun_slinger_gal", "peasant_fixit",
 ],

 "residence": [
 "cottage_matron", "pond_wolf", "moss_rat", "old_vagrant", "hired_matron", "mama_bear",
 ],

 "business": [
 "clockwork_colossus", "clockwork_mill", "black_curio_peddler", "cybernet_guard", "wrecker", "wrecker_small",
 "enforcer_heavy", "ganger_elder", "mob_lieutenant", "baroness_guard", "enforcer", "corrupt_cop", "black_market_dealer",
 ],

 "inn": [
 "old_vagrant", "barfly", "courier_girl", "flapper", "neon_dancer", "rival_bartender", "hired_matron", "neon_siren",
 ],

 "arcane": [
 "banshee", "mindflayer", "wraith_knight", "elder_tentacle", "spectral_hag", "dream_moth_small",
 "abyssal_serpent", "abyssal_eel_small", "soft_lich_apprentice", "void_spider",
 ],
}