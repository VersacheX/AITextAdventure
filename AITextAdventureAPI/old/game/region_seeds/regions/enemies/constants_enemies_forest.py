# Additional hostile seeds for expanded forest locations
# Seeds are organized per-level in `forest` submodules.
from game.region_seeds.regions.enemies.forest.lv1to10 import SEEDS_LV1TO10
from game.region_seeds.regions.enemies.forest.lv11to20 import SEEDS_LV11TO20
from game.region_seeds.regions.enemies.forest.lv21to30 import SEEDS_LV21TO30
from game.region_seeds.regions.enemies.forest.lv31to100 import SEEDS_LV31TO100

RANDOM_HOSTILE_SEEDS = []
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV1TO10)
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV11TO20)
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV21TO30)
RANDOM_HOSTILE_SEEDS.extend(SEEDS_LV31TO100)

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