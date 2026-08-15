# Reworked hostile seed data for Boiling Bubble (mid-city witch district).
# Each entry is a dict used by the encounter/spawn systems. Fields follow the project's schema.

from .enemies_mid.lv1to10 import RANDOM_HOSTILE_SEEDS as LV1TO10
from .enemies_mid.lv11to20 import RANDOM_HOSTILE_SEEDS as LV11TO20
from .enemies_mid.lv21to30 import RANDOM_HOSTILE_SEEDS as LV21TO30
from .enemies_mid.lv31to40 import RANDOM_HOSTILE_SEEDS as LV31TO40
from .enemies_mid.lv41to50 import RANDOM_HOSTILE_SEEDS as LV41TO50
from .enemies_mid.lv51to60 import RANDOM_HOSTILE_SEEDS as LV51TO60
from .enemies_mid.lv61to70 import RANDOM_HOSTILE_SEEDS as LV61TO70
from .enemies_mid.lv71to80 import RANDOM_HOSTILE_SEEDS as LV71TO80
from .enemies_mid.lv81to90 import RANDOM_HOSTILE_SEEDS as LV81TO90
from .enemies_mid.lv91to100 import RANDOM_HOSTILE_SEEDS as LV91TO100

RANDOM_HOSTILE_SEEDS = (
 LV1TO10 + LV11TO20 + LV21TO30 + LV31TO40 + LV41TO50
 + LV51TO60 + LV61TO70 + LV71TO80 + LV81TO90 + LV91TO100
)

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "pocket_imp", "tea_barker", "cauldron_clown", "neon_siren", "bookish_bumbler", "arcane_hound",
 ],

 "alley": [
 "pocket_imp", "fixer_runt", "moss_smuggler", "rune_scribe", "whisper_acolyte",
 ],

 "bar": [
 "cauldron_clown", "tea_barker", "kettle_brawler", "neon_siren", "bookish_bumbler",
 ],

 "shop": [
 "rune_scribe", "coven_fixer", "fixer_runt", "cloak_roustabout",
 ],

 "residence": [
 "pocket_imp", "cloak_roustabout", "bookish_bumbler", "hexed_constable", "moss_smuggler",
 ],

 "business": [
 "hexed_constable", "owl_sharpshooter", "shadow_assassin", "wrecker", "reclaimed_clockwork_colossus",
 ],

 "inn": [
 "cauldron_clown", "tea_barker", "pocket_imp", "neon_siren", "dryad_femme_fatale", "banshee", "dream_eater",
 ],
}