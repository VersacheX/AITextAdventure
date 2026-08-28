# Random hostile seed data for The Necropolis (large-city)
# Each entry is a dict used by encounter/spawn systems.
from .enemies_large.lv1to10 import SEEDS_LV1TO10
from .enemies_large.lv11to20 import SEEDS_LV11TO20
from .enemies_large.lv21to30 import RANDOM_HOSTILE_SEEDS as SEEDS_LV21TO30
from .enemies_large.lv31to40 import RANDOM_HOSTILE_SEEDS as SEEDS_LV31TO40
from .enemies_large.lv41to50 import RANDOM_HOSTILE_SEEDS as SEEDS_LV41TO50
from .enemies_large.lv51to60 import RANDOM_HOSTILE_SEEDS as SEEDS_LV51TO60
from .enemies_large.lv61to70 import RANDOM_HOSTILE_SEEDS as SEEDS_LV61TO70
from .enemies_large.lv71to80 import RANDOM_HOSTILE_SEEDS as SEEDS_LV71TO80
from .enemies_large.lv81to90 import RANDOM_HOSTILE_SEEDS as SEEDS_LV81TO90
from .enemies_large.lv91to100 import RANDOM_HOSTILE_SEEDS as SEEDS_LV91TO100

# Shared swamp-region rarity-coverage fill seeds (single package import).
# Efficient roster: same seeds used by every swamp city size.
from .enemies_shared import RANDOM_HOSTILE_SEEDS as RARITY_FILL_HOSTILES

RANDOM_HOSTILE_SEEDS = (SEEDS_LV1TO10 + SEEDS_LV11TO20 + SEEDS_LV21TO30 + SEEDS_LV31TO40 +
                        SEEDS_LV41TO50 + SEEDS_LV51TO60 + SEEDS_LV61TO70 + SEEDS_LV71TO80 +
                        SEEDS_LV81TO90 + SEEDS_LV91TO100 + RARITY_FILL_HOSTILES)

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
# Use building type names (matching normalized building types), plus 'street' and 'alley'.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "mire_tosser", "grave_hawker", "sock_rat", "swamp_bard", "moss_jester",
 "skeleton_minion_01", "skeleton_minion_02", "skeleton_minion_03", "cryptling_01", "cryptling_02",
 "undertaker_apprentice", "grave_digger_01",
 ],

 "alley": [
 "coffin_cutpurse", "mire_mocker", "moss_spider", "rot_brigand", "ghoul_runner_01",
 "ghoul_runner_02", "tomb_stalker_01", "tomb_stalker_02", "tomb_wight_01", "tomb_wight_02",
 "skeleton_archer_01",
 ],

 "bar": [
 "sluice_brawler", "bone_hauler", "funeral_pallbearer", "casket_crusher", "moss_jester", "swamp_bard",
 ],

 "shop": [
 "talon_merchant", "vial_trader", "bone_tinker", "sexton_mad", "grave_hawker",
 ],

 "residence": [
 "mire_gator", "sepulcher_hound_01", "sepulcher_hound_02", "putrid_zombie_01", "putrid_zombie_02",
 "grave_digger_02", "undertaker_apprentice",
 ],

 "business": [
 "crypt_warden", "vault_keeper", "marrow_collector", "marrow_sentinel", "rot_surgeon",
 "grave_digger_02", "bone_spinner",
 ],

 "inn": [
 "sluice_brawler", "swamp_bard", "moss_jester", "funeral_pallbearer", "undertaker_apprentice",
 ],

 "arcane": [
 "mort_priest", "tide_specter", "mud_lich", "necromancer_lord", "mort_queen", "death_herald",
 "tomb_stigilist", "ossuary_priest_01", "grave_banshee",
 ],

 "works": [
 "bone_colossus", "grate_sentry", "bone_tinker", "bone_spinner",
 ],

 "sewers": [
 "bog_wyrm", "mire_mocker", "moss_spider", "putrid_zombie_02", "carrion_bat_01", "carrion_bat_02",
 "corpse_moth", "crypt_revenant", "skeleton_archer_02",
 ],
}