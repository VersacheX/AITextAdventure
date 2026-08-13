# Random hostile seed data for Nightveil Spire (reworked). Each entry is a dict that describes
# a hostile template used by encounter/spawn systems. Fields follow the project's expected schema.

# NOTE: Level1-10 seeds moved to enemies_mid.lv1to10 for maintainability
from game.region_seeds.regions.cities.desert.enemies_mid.lv1to10 import RANDOM_HOSTILE_SEEDS as LV1TO10_HOSTILES
from game.region_seeds.regions.cities.desert.enemies_mid.lv11to20 import RANDOM_HOSTILE_SEEDS as LV11TO20_HOSTILES
from game.region_seeds.regions.cities.desert.enemies_mid.lv21to30 import RANDOM_HOSTILE_SEEDS as LV21TO30_HOSTILES
from game.region_seeds.regions.cities.desert.enemies_mid.lv31to50 import RANDOM_HOSTILE_SEEDS as LV31TO50_HOSTILES
from game.region_seeds.regions.cities.desert.enemies_mid.lv51to100 import RANDOM_HOSTILE_SEEDS as LV51TO100_HOSTILES

# Higher-tier seeds (min_spawn_level >30)
HIGHER_LEVEL_SEEDS = []

# Compose final seed list
RANDOM_HOSTILE_SEEDS = []
RANDOM_HOSTILE_SEEDS.extend(LV1TO10_HOSTILES or [])
RANDOM_HOSTILE_SEEDS.extend(LV11TO20_HOSTILES or [])
RANDOM_HOSTILE_SEEDS.extend(LV21TO30_HOSTILES or [])
RANDOM_HOSTILE_SEEDS.extend(LV31TO50_HOSTILES or [])
RANDOM_HOSTILE_SEEDS.extend(LV51TO100_HOSTILES or [])
RANDOM_HOSTILE_SEEDS.extend(HIGHER_LEVEL_SEEDS or [])

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "gloam_urchin", "inkling_pickpocket", "lantern_vendor", "candle_jester", "cloak_roustabout",
 "bookish_bumbler", "cowl_thief", "arcane_hound", "ombre_brawler", "neon_siren",
 ],

 "alley": [
 "cowl_thief", "inkling_pickpocket", "fixer_runt", "candle_jester", "cloak_roustabout", "void_spider",
 "ombre_brawler", "whisper_cultist", "shadow_assassin",
 ],

 "bar": [
 "lantern_vendor", "candle_jester", "neon_siren", "bookish_bumbler", "cloak_roustabout",
 "ombre_brawler", "wrecker", "femme_fatale",
 ],

 "shop": [
 "sigil_monger", "fixer_runt", "lantern_vendor", "cloak_roustabout",
 ],

 "residence": [
 "gloam_urchin", "inkling_pickpocket", "bookish_bumbler", "cloak_roustabout", "neon_siren",
 ],

 "business": [
 "shade_guard", "clockwork_colossus", "shadow_assassin", "wrecker", "dream_eater", "femme_fatale",
 ],

 "inn": [
 "gloam_urchin", "lantern_vendor", "bookish_bumbler", "banshee", "dream_eater", "neon_siren",
 ],
}