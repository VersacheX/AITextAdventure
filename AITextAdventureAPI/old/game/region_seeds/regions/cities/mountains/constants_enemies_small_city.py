# Random hostile seed data for Hollerforge Hollow (small-city)
# Each entry is a dict used by encounter/spawn systems.
from .enemies_small.lv1to10 import SEEDS_LV1TO10
from .enemies_small.lv11to20 import SEEDS_LV11TO20

RANDOM_HOSTILE_SEEDS = SEEDS_LV1TO10 + SEEDS_LV11TO20

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "hobnail_scrapper", "roundhouse_rummy", "log_beggar", "stump_shyster", "hollow_peddler",
 "secondhand_sally", "moss_nicker", "anvil_humorist", "taproom_tapster", "holler_fox",
 ],

 "alley": [
 "sly_cooperette", "moss_nicker", "rift_raider", "ledger_band", "cliff_viper", "mire_spider",
 "trail_hound", "snare_reaver",
 ],

 "bar": [
 "roundhouse_rummy", "taproom_tapster", "anvil_humorist", "granny_bruiser", "secondhand_sally",
 ],

 "shop": [
 "hollow_peddler", "ledger_louse", "hollow_tinker", "rivet_madame", "axle_mason",
 ],

 "residence": [
 "log_beggar", "stone_marmot", "holler_fox", "pit_beetle", "trail_hound",
 ],

 "business": [
 "picktoe_lin", "forge_hewer", "axle_mason", "timber_watch", "guild_rigger", "rivet_madame",
 "marauder_matriarch", "ledger_band", "hollow_colossus", "forge_warden",
 ],

 "inn": [
 "taproom_tapster", "roundhouse_rummy", "secondhand_sally", "anvil_humorist", "granny_bruiser",
 ],

 "arcane": [
 "hollow_cultist", "slag_watcher", "furnace_wail", "ironshade", "hollow_savant",
 "dream_stag", "timber_wyrm", "ember_drake", "dream_stag",
 ],
}