# Reworked hostile seed data for Gnashwater Hollow (small swamp city)
# Each entry is a dict describing a hostile template used by encounter/spawn systems.
from .enemies_small.lv1to10 import SEEDS_LV1TO10
from .enemies_small.lv11to20 import SEEDS_LV11TO20
from .enemies_small.lv21to30 import RANDOM_HOSTILE_SEEDS as SEEDS_LV21TO30
from .enemies_small.lv31to40 import RANDOM_HOSTILE_SEEDS as SEEDS_LV31TO40
from .enemies_small.lv41to50 import RANDOM_HOSTILE_SEEDS as SEEDS_LV41TO50
from .enemies_small.lv51to60 import RANDOM_HOSTILE_SEEDS as SEEDS_LV51TO60
from .enemies_small.lv61to70 import RANDOM_HOSTILE_SEEDS as SEEDS_LV61TO70
from .enemies_small.lv71to80 import RANDOM_HOSTILE_SEEDS as SEEDS_LV71TO80
from .enemies_small.lv81to90 import RANDOM_HOSTILE_SEEDS as SEEDS_LV81TO90
from .enemies_small.lv91to100 import RANDOM_HOSTILE_SEEDS as SEEDS_LV91TO100

# Shared swamp-region rarity-coverage fill seeds (single package import).
# Efficient roster: same seeds used by every swamp city size.
from .enemies_shared import RANDOM_HOSTILE_SEEDS as RARITY_FILL_HOSTILES

RANDOM_HOSTILE_SEEDS = (SEEDS_LV1TO10 + SEEDS_LV11TO20 + SEEDS_LV21TO30 + SEEDS_LV31TO40 +
                        SEEDS_LV41TO50 + SEEDS_LV51TO60 + SEEDS_LV61TO70 + SEEDS_LV71TO80 +
                        SEEDS_LV81TO90 + SEEDS_LV91TO100 + RARITY_FILL_HOSTILES)

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "gutter_pincher", "marsh_rat", "toss_vagrant", "last_call", "neon_drifter",
 "rumor_monger", "courier_gal", "alley_cat", "beggar_spoon", "dock_dame",
 "flinger_flapper", "marsh_marksman", "stilt_sniper",
 ],

 "alley": [
 "drain_mole", "inked_ruffian", "fang_pack", "sewer_rat", "void_spider",
 "pawn_watcher", "skiff_runner", "plank_rogue", "beggar_spoon",
 ],

 "bar": [
 "jaw_brawler", "bilge_bouncer", "rival_barkeep", "madam_wrench", "bog_wrecker",
 "plank_rogue", "flinger_flapper", "marsh_marksman", "shadow_panter",
 ],

 "shop": [
 "curio_snatcher", "pawn_watcher", "ledger_fixer", "net_whisperer", "skiff_runner",
 ],

 "residence": [
 "mire_hound", "mama_hound", "tough_grammy", "sly_madam", "matron_hire",
 ],

 "business": [
 "toll_warden", "rot_constable", "pit_lord", "bog_wrecker", "wreck_johnson",
 "black_market_cat", "servo_watch", "mob_lieutenant", "baroness_guard", "mafia_madam",
 "rogue_mistress", "femme_fatale", "young_lich_apprentice", "revenant_queen", "celestial_watcher",
 ],

 "inn": [
 "last_call", "rival_barkeep", "courier_gal", "tough_grammy", "matron_hire",
 ],

 "arcane": [
 "wailing_thing", "mind_nibbler", "dream_gobbler", "revenant_queen", "celestial_watcher",
 "lich_apprentice", "abyssal_serpent", "elder_tendril", "spectral_hag", "wraith_knight",
 "clockwork_colossus", "harbinger_frost", "siren_shallows", "umbral_stalker",
 ],

 "docks": [
 "skiff_runner", "stilt_sniper", "marsh_marksman",
 ],
}