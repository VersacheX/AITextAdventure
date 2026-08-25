# Random hostile seed data for Brineward Harbor (mid-city)
# Each entry is a dict used by encounter/spawn systems.
from .enemies_mid.lv1to10 import SEEDS_LV1TO10
from .enemies_mid.lv11to20 import SEEDS_LV11TO20
from .enemies_mid.lv21to30 import RANDOM_HOSTILE_SEEDS as SEEDS_LV21TO30
from .enemies_mid.lv31to40 import RANDOM_HOSTILE_SEEDS as SEEDS_LV31TO40
from .enemies_mid.lv41to50 import RANDOM_HOSTILE_SEEDS as SEEDS_LV41TO50
from .enemies_mid.lv51to60 import RANDOM_HOSTILE_SEEDS as SEEDS_LV51TO60
from .enemies_mid.lv61to70 import RANDOM_HOSTILE_SEEDS as SEEDS_LV61TO70
from .enemies_mid.lv71to80 import RANDOM_HOSTILE_SEEDS as SEEDS_LV71TO80
from .enemies_mid.lv81to90 import RANDOM_HOSTILE_SEEDS as SEEDS_LV81TO90
from .enemies_mid.lv91to100 import RANDOM_HOSTILE_SEEDS as SEEDS_LV91TO100

# Shared shallows-region rarity-coverage fill seeds (single package import).
# Efficient roster: same seeds used by every shallows city size.
from .enemies_shared import RANDOM_HOSTILE_SEEDS as RARITY_FILL_HOSTILES

RANDOM_HOSTILE_SEEDS = (SEEDS_LV1TO10 + SEEDS_LV11TO20 + SEEDS_LV21TO30 + SEEDS_LV31TO40 +
                        SEEDS_LV41TO50 + SEEDS_LV51TO60 + SEEDS_LV61TO70 + SEEDS_LV71TO80 +
                        SEEDS_LV81TO90 + SEEDS_LV91TO100 + RARITY_FILL_HOSTILES)

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "mossling_pick", "salty_bum", "sea_gull_swarm", "bilge_brawler", "wallet_weed",
 "jarred_jasper", "lighthouse_busker", "rust_pelican",
 ],

 "alley": [
 "wallet_weed", "tide_knife", "barnacle_crab_mid", "brine_serpentling", "bilge_smuggler",
 "wharf_shade", "night_sneak", "hookhand_ron",
 ],

 "bar": [
 "salty_bum", "bilge_brawler", "tavern_jester", "lighthouse_busker", "hookhand_ron",
 ],

 "shop": [
 "jarred_jasper", "dockbroker_dave", "keel_fix", "rust_pelican",
 ],

 "residence": [
 "salty_bum", "barnacle_crab_mid", "keel_hound", "bilge_brawler",
 ],

 "business": [
 "dockbroker_dave", "harbor_bully", "quay_watch", "keel_fix", "dock_automat",
 ],

 "inn": [
 "bilge_brawler", "tavern_jester", "lighthouse_busker",
 ],

 "arcane": [
 "pier_cultist", "salt_vicar", "tide_wraith", "abyssal_cuttle", "brine_serpentling",
 "harbor_lich", "captain_tide", "kraken_whelp",
 ],
}