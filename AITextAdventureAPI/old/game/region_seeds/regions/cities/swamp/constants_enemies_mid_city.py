# Reworked hostile seed data for Bayou Nocturne (Bayou Nocturne has its own flavor)
# Each entry is a dict describing a hostile template used by encounter/spawn systems.
from game.region_seeds.regions.cities.swamp.enemies_mid.lv1to10 import SEEDS_LV1TO10
from game.region_seeds.regions.cities.swamp.enemies_mid.lv11to20 import SEEDS_LV11TO20

# Compose RANDOM_HOSTILE_SEEDS from level-specific lists
RANDOM_HOSTILE_SEEDS = []
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV1TO10)
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV11TO20)

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "bayou_pick", "marsh_rat", "tattered_vagrant", "last_call", "board_bandit", "smash_thug",
 "rumor_monger_bay", "neon_street_dancer", "courier_gal", "flitting_flapper", "beggar_blade",
 "jackal_pack", "undercity_rat", "egret_sniper", "grit_hound", "bog_wolf", "alley_cat_bay", "muck_brawler",
 ],

 "alley": [
 "board_bandit", "bayou_pick", "tunnel_mole", "undercity_rat", "skiff_smuggler", "skulk_dog",
 "tattooed_rascal", "void_spider_bay", "plague_stoker_bay", "beggar_blade", "lady_board",
 "wrecker_johnson", "slick_rogue", "umbral_stalker_bay",
 ],

 "bar": [
 "last_call", "rival_bartender_bay", "bouncer_gator", "dame_of_streets", "flitting_flapper",
 "gunslinger_miss", "madam_mechanic", "sly_madam_bay", "femme_folly", "bog_wrecker",
 "shadow_panter", "antique_snatcher", "neon_siren_bay", "siren_of_mist",
 ],

 "shop": [
 "antique_snatcher", "pawn_watcher", "fixer_quill", "fixer_hacker_bay", "skiff_smuggler",
 "rumor_monger_bay",
 ],

 "residence": [
 "irate_resident", "watch_dog", "mama_gator", "tough_grammy", "tattered_vagrant", "sly_madam_bay",
 "swamp_cultist", "courier_gal", "bog_wolf",
 ],

 "business": [
 "salted_cop", "pawn_watcher", "fixer_hacker_bay", "cybernet_watch", "black_market_crook",
 "wrecker_johnson", "elder_ganger", "baroness_guard", "mob_lieutenant_bay", "rogue_mistress_bay",
 "gavel_enforcer", "mafia_madam_bay",
 ],

 "inn": [
 "tattered_vagrant", "last_call", "courier_gal", "tough_grammy", "matron_hire", "rival_bartender_bay",
 ],

 "arcane": [
 "wailing_banshee", "mind_nibbler", "dream_gobbler", "revenant_queen_bay", "celestial_watcher_bay",
 "lich_apprentice_bay", "abyssal_serpent_bay", "elder_tendril", "spectral_hag_bay", "wraith_knight_bay",
 "clockwork_colossus_bay", "harbinger_frost", "siren_of_mist", "umbral_stalker_bay",
 ],

 "docks": [
 "sloop_raider", "skiff_smuggler", "smash_thug",
 ],
}