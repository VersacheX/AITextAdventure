# Random hostile seed data for Highsteeple Crossing (reimagined)
# Each entry is a dict used by encounter/spawn systems.

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
from .enemies_shared import RANDOM_HOSTILE_SEEDS as RARITY_FILL_HOSTILES

RANDOM_HOSTILE_SEEDS = (
 LV1TO10 + LV11TO20 + LV21TO30 + LV31TO40 + LV41TO50
 + LV51TO60 + LV61TO70 + LV71TO80 + LV81TO90 + LV91TO100 + RARITY_FILL_HOSTILES
)

# Mapping of zone/subtype -> list of hostile ids that can spawn there.
RANDOM_HOSTILE_LINKS = {
 "street": [
 "coin_mumbler", "shifty_apprentice", "homeless_lyric", "taproom_fly", "rumor_monger_mid",
 "civic_dame", "inked_row", "vesper_dancer", "alderman_ruffians", "steeple_sniper", "lady_cutpurse_mid",
 ],

 "alley": [
 "mole_apothecary", "beggar_cutpurse", "alley_feral", "void_moth", "sewer_scrap", "rat_warren_king",
 "raider_crossbow", "wrecking_vice",
 ],

 "bar": [
 "taproom_fly", "doorwatch", "pewter_brawler", "rogue_minstrel", "jester_sermon", "vesper_dancer",
 "altar_fixit", "siren_of_halls",
 ],

 "shop": [
 "curio_snatcher", "vault_warden", "fixer_scriptorium", "smuggler_chorister", "mole_apothecary", "gunslinger_vicar",
 ],

 "residence": [
 "rat_warren_king", "shadow_mouser", "matron_grasp", "plague_baker_mid", "sacred_hound",
 ],

 "business": [
 "canon_enforcer", "corrupt_deacon", "vestment_brute", "fixer_abbot", "cybernet_sentinel", "black_reliquary_dealer",
 "underboss_decree", "fixer_scriptorium", "rogue_mistress_mid", "femme_preacher", "clockwork_warden",
 ],

 "inn": [
 "homeless_lyric", "taproom_fly", "doorwatch", "rumor_monger_mid", "vesper_dancer",
 ],

 "arcane": [
 "mind_scribe", "dream_harvester", "elder_root", "lich_apprentice_lost", "wraith_chalice", "spectral_midwife",
 "harbinger_frost_mid", "abyssal_serpent_mid", "revenant_pastor", "celestial_chalice", "wailing_bell", "umbral_courser",
 ],
}