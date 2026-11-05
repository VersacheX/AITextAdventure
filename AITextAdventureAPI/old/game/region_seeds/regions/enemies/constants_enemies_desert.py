# Additional hostile seeds for expanded locations
# Seeds are organized per-level in `desert` submodules.
from game.region_seeds.regions.enemies.desert.lv1to10 import SEEDS_LV1TO10
from game.region_seeds.regions.enemies.desert.lv11to20 import SEEDS_LV11TO20
from game.region_seeds.regions.enemies.desert.lv21to30 import SEEDS_LV21TO30
from game.region_seeds.regions.enemies.desert.lv31to100 import SEEDS_LV31TO100

# Shared rarity-coverage roster (one seed of every rarity at each 5-level mark,
# Lv 5..100). Pulling this in fills the per-level gaps left in the desert band
# files without duplicating seeds there. Reused across every desert city size
# and the desert wilderness.
from game.region_seeds.regions.cities.desert.enemies_shared import (
	RANDOM_HOSTILE_SEEDS as SHARED_DESERT_HOSTILES,
)

RANDOM_HOSTILE_SEEDS = []
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV1TO10)
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV11TO20)
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV21TO30)
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV31TO100)
RANDOM_HOSTILE_SEEDS.extend(SHARED_DESERT_HOSTILES)

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 # Streets: high variety and RNG; common riffraff plus occasional dangerous loners
 "street": [
 ],

 # Alleys: ambushes, creatures, smugglers, and the nastier low-mid tier threats
 "alley": [
 ],

 # Bars: fights and social encounters; can include rogues, performers and one-off dramatic foes
 "bar": [ "dune_rat", "sand_scrapper", "wind_skiff", "dune_hustler", "dust_whistler", "dune_bandit",
		 "sand_sniper", "sand_berserker", "oasis_nymph","tomb_keeper","sand_howler","mirage_witch",
		 "dune_pioneer","sand_hydra","dune_warden","rock_gargant","sand_raven","desert_archmage",
		 "bone_revenant","sand_colossus","auric_stela","dune_emperor","sand_herald"
 ],

 # Shops: theft, guards, fixers and shady merchants (black market dealers are rare but possible)
 "shop": [
 ],

 # Residences: domestic encounters, defensive NPCs and occasional cultist activity
 "residence": [
 ],

 # Businesses: corporate security, hired wreckers, and organized crime presence
 "business": [
 ],

 # Inns: travelers, barflies and the occasional haunted guestroom or spirit
 "inn": [
 ],
}