# Random hostile seed data (used by encounter/spawn systems)
# Flat list of hostile templates. Each entry is a dict; generator code can
# convert these into RandomHostile instances or influence generation behavior.

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

RANDOM_HOSTILE_SEEDS = (LV1TO10 + LV11TO20 + LV21TO30 + LV31TO40 +
                        LV41TO50 + LV51TO60 + LV61TO70 + LV71TO80 +
                        LV81TO90 + LV91TO100)

# Mapping of zones / building subtypes to hostile ids for Aurelion Veil
RANDOM_HOSTILE_LINKS = {
 "street": [
 "rootling", "mosspiper", "glimmer_sprite", "glowgnat", "silvertongue", "bramble_bandit", "bough_wolf", "fey_trickster",
 ],
 "alley": [
 "bramble_bandit", "court_jester", "arcane_hound", "fey_trickster", "elder_tentacle",
 ],
 "bar": [
 "court_jester", "silvertongue", "glimmer_sprite", "fey_trickster",
 ],
 "shop": [
 "sigil_harvester", "thistle_mage", "silvertongue",
 ],
 "residence": [
 "palais_sentinal", "willow_witch", "mosspiper", "rootling",
 ],
 "business": [
 "palais_sentinal", "starwarden", "vine_colossus", "root_golem", "elder_tentacle",
 ],
 "inn": [
 "mosspiper", "glimmer_sprite", "silvertongue", "court_jester",
 ],
 "arcane": [
 "thistle_mage", "sigil_harvester", "dreamstalker", "arcane_hound",
 ],
}