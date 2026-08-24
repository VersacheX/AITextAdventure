# Random hostile seed data for Crosswind Bazaar (reimagined)
# Each entry is a dict used by encounter/spawn systems.

from .enemies_large.lv1to10 import RANDOM_HOSTILE_SEEDS as LV1TO10
from .enemies_large.lv11to20 import RANDOM_HOSTILE_SEEDS as LV11TO20
from .enemies_large.lv21to30 import RANDOM_HOSTILE_SEEDS as LV21TO30
from .enemies_large.lv31to40 import RANDOM_HOSTILE_SEEDS as LV31TO40
from .enemies_large.lv41to50 import RANDOM_HOSTILE_SEEDS as LV41TO50
from .enemies_large.lv51to60 import RANDOM_HOSTILE_SEEDS as LV51TO60
from .enemies_large.lv61to70 import RANDOM_HOSTILE_SEEDS as LV61TO70
from .enemies_large.lv71to80 import RANDOM_HOSTILE_SEEDS as LV71TO80
from .enemies_large.lv81to90 import RANDOM_HOSTILE_SEEDS as LV81TO90
from .enemies_large.lv91to100 import RANDOM_HOSTILE_SEEDS as LV91TO100
from .enemies_shared import RANDOM_HOSTILE_SEEDS as RARITY_FILL_HOSTILES

RANDOM_HOSTILE_SEEDS = (
 LV1TO10 + LV11TO20 + LV21TO30 + LV31TO40 + LV41TO50
 + LV51TO60 + LV61TO70 + LV71TO80 + LV81TO90 + LV91TO100 + RARITY_FILL_HOSTILES
)

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "coin_finger", "tent_swashbuckler", "pickpocket_apprentice", "shadow_cat", "vagrant_old", "beggar_swash",
 "streetwise_fox", "alley_tabby", "neon_dancer_implausible", "rumor_monger_glib", "tattooed_rowdy", "flapper_dancer",
 "cyber_hound_pup", "lady_cutpurse", "wind_sniper",
 ],

 "alley": [
 "mole_trader", "pickpocket_apprentice", "undercity_roach", "rat_king", "ganger_rabble", "smuggler_herald",
 "void_weaver", "umbral_racer", "raider_windman",
 ],

 "bar": [
 "barfly_drunkard", "bouncer_bram", "bazaarkeeper", "rogue_poet", "court_jester", "flapper_dancer", "siren_muse",
 "neon_dancer_implausible", "smiling_fixit", "gunslinger_maiden",
 ],

 "shop": [
 "bazaarkeeper", "antique_pick", "pawn_watch", "fixer_hacker_elite", "smuggler_herald", "mole_trader",
 "smiling_fixit", "lady_cutpurse", "gunslinger_maiden",
 ],

 "residence": [
 "mama_keeper", "rat_king", "shadow_cat", "streetwise_fox", "vagrant_old", "beggar_swash", "matron_hired",
 ],

 "business": [
 "enforcer_brute", "caravan_giant", "cybernet_watch", "fixer_hacker_elite", "black_market_lady", "mob_exec", "clockwork_giant", "wrecker_hulker",
 "fixer_shade", "rogue_mistress_redux", "praerie_femme_fatality",
 ],

 "inn": [
 "vagrant_old", "barfly_drunkard", "bouncer_bram", "flapper_dancer", "mama_keeper", "rumor_monger_glib",
 "matron_hired",
 ],

 "arcane": [
 "mind_merchant", "dream_sipper", "elder_tendrils", "abyss_serpent_mini", "lich_apprentice_quiet", "revenant_matron",
 "wraith_watchman", "harbinger_frost", "spectral_hag_grouchy", "banshee_giggle", "plague_baker", "celestial_watch",
 ],
}