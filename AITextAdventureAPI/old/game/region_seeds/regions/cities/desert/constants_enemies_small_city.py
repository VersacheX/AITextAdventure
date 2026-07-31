# Random hostile seed data for "BioHazard" (small post-apocalyptic city).
# Each entry is a simple dict used by encounter/spawn systems.

from .enemies_small.lv1to10 import RANDOM_HOSTILE_SEEDS as LV1TO10
from .enemies_small.lv11to20 import RANDOM_HOSTILE_SEEDS as LV11TO20

RANDOM_HOSTILE_SEEDS = LV1TO10 + LV11TO20

# Map spawn zones to new hostile ids
RANDOM_HOSTILE_LINKS = {
 "street": [
 "scav_runner", "scrap_rodent", "jerky_barker", "junk_jester", "barrel_marauder", "gearhound", "night_raven",
 "canteen_keeper",
 ],

 "alley": [
 "rust_clubber", "radio_fix", "vault_microthief", "scrap_shaman", "barrel_marauder", "junk_jester",
 ],

 "bar": [
 "canteen_keeper", "jerky_barker", "junk_jester", "muttering_matron", "scrap_siren",
 ],

 "shop": [
 "trader_ricochet", "radio_fix", "vault_microthief", "gearhound",
 ],

 "residence": [
 "scrap_rodent", "canteen_keeper", "muttering_matron", "barrel_marauder", "scav_runner",
 ],

 "business": [
 "scrap_colossus", "mad_mechanic", "wasteland_wrecker", "peddler_phantom", "scrap_shaman",
 ],

 "inn": [
 "canteen_keeper", "jerky_barker", "scav_runner", "scrap_siren", "peddler_phantom",
 ],
}