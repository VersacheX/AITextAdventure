# --- Seed data for items (used by generators/shops) ---
# These are plain dicts; game code should convert them to Item/Weapon/Armor objects as needed.
from game.region_seeds.weapons.lv1_10 import WEAPONS_LV1_10
from game.region_seeds.weapons.lv11_20 import WEAPONS_LV11_20
from game.region_seeds.weapons.lv21_35 import WEAPONS_LV21_35
from game.region_seeds.weapons.lv36_50 import WEAPONS_LV36_50
from game.region_seeds.weapons.lv51_65 import WEAPONS_LV51_65
from game.region_seeds.armor.lv1_10 import ARMOR_LV1_10
from game.region_seeds.armor.lv11_20 import ARMOR_LV11_20
from game.region_seeds.armor.lv21_35 import ARMOR_LV21_35
from game.region_seeds.armor.lv36_50 import ARMOR_LV36_50
from game.region_seeds.armor.lv51_65 import ARMOR_LV51_65

# Combine weapons from seed files and sort by:
#1) min_spawn_level (ascending)
#2) strength (descending)
#3) intelligence (descending)
#4) dexterity (descending)
WEAPON_SEEDS = sorted(
     (WEAPONS_LV1_10 or []) + (WEAPONS_LV11_20 or []) + (WEAPONS_LV21_35 or []) + (WEAPONS_LV36_50 or []) + (WEAPONS_LV51_65 or []),
     key=lambda w: (
         int(w.get('min_spawn_level',0)),
         -int(w.get('strength',0)),
         -int(w.get('intelligence',0)),
         -int(w.get('dexterity',0)),
     ),
)

ARMOR_TYPES = {
    'head': 'head',
    'body': 'body',
    'arms': 'arm',
    'legs': 'leg'
}
# Merge armor seeds from per-level modules into ARMOR_SEEDS per slot and sort similarly.
# Ensure ARMOR_SEEDS exactly has the expected slots: head, body, arms, legs
ARMOR_SEEDS = {}
SLOTS = ARMOR_TYPES.keys()
for slot in SLOTS:
    list1 = ARMOR_LV1_10.get(slot, []) if isinstance(ARMOR_LV1_10, dict) else []
    list2 = ARMOR_LV11_20.get(slot, []) if isinstance(ARMOR_LV11_20, dict) else []
    list3 = ARMOR_LV21_35.get(slot, []) if isinstance(ARMOR_LV21_35, dict) else []
    list4 = ARMOR_LV36_50.get(slot, []) if isinstance(ARMOR_LV36_50, dict) else []
    list5 = ARMOR_LV51_65.get(slot, []) if isinstance(ARMOR_LV51_65, dict) else []
    combined = (list1 or []) + (list2 or []) + (list3 or []) + (list4 or []) + (list5 or [])
    # sort by min_spawn_level ascending, then strength/intelligence/dexterity descending
    combined_sorted = sorted(
        combined,
        key=lambda a: (
            int(a.get('min_spawn_level',0)),
            -int(a.get('strength',0)),
            -int(a.get('intelligence',0)),
            -int(a.get('dexterity',0)),
            ),
    )
    ARMOR_SEEDS[slot] = combined_sorted

# Utility items like healing herbs, lockpicks, stimulants
# User requested rarities in order: common, rare, uncommon, uncommon
UTILITY_ITEM_SEEDS = [
    # HP healing tiers (fractions of max HP: small=25%, mid=50%, large=75%, full=100%)
    {"id": "herb_minor", "name": "Pocket Salve", "description": "Restores a small fraction of your max HP.", "effect": "heal_small", "uses":1, "value":8, "min_spawn_level":1, "rarity": "common", "heal_fraction":0.25},
    {"id": "herb_med", "name": "Patch Kit", "description": "Restores a moderate fraction of your max HP.", "effect": "heal_mid", "uses":1, "value":18, "min_spawn_level":4, "rarity": "uncommon", "heal_fraction":0.5},
    {"id": "herb_major", "name": "Curative Salve", "description": "Restores a large fraction of your max HP.", "effect": "heal_large", "uses":1, "value":40, "min_spawn_level":10, "rarity": "rare", "heal_fraction":0.75},
    {"id": "elixir_full_heal", "name": "Stimpak", "description": "Fully restores your HP.", "effect": "heal_full", "uses":1, "value":200, "min_spawn_level":15, "rarity": "superrare", "heal_fraction":1.0},

    # AP (action points) restoration tiers (fractions of max AP)
    {"id": "stimulant_small", "name": "Caffeine Shot", "description": "Restores a small fraction of your max AP.", "effect": "restore_ap_small", "uses":1, "value":10, "min_spawn_level":1, "rarity": "common", "ap_fraction":0.25},
    {"id": "stimulant_med", "name": "Energy Drink", "description": "Restores a moderate fraction of your max AP.", "effect": "restore_ap_mid", "uses":1, "value":28, "min_spawn_level":4, "rarity": "uncommon", "ap_fraction":0.5},
    {"id": "stimulant_large", "name": "Adrenaline Shot", "description": "Restores a large fraction of your max AP.", "effect": "restore_ap_large", "uses":1, "value":60, "min_spawn_level":10, "rarity": "rare", "ap_fraction":0.75},
    {"id": "stimulant_full", "name": "Neuro Stim", "description": "Fully restores your AP.", "effect": "restore_ap_full", "uses":1, "value":180, "min_spawn_level":15, "rarity": "superrare", "ap_fraction":1.0},



    # Utility / tools   <- remove lockpicks... this tech will never be built
    #{"id": "lockpick", "name": "Slim Jim", "description": "Useful for opening simple locks.", "effect": "open_lock", "uses":5, "value":20, "min_spawn_level":1, "rarity": "uncommon"},

    # Revive Items
    {"id": "revive_kit", "name": "Revival Kit", "description": "A compact kit that can revive a fallen ally with partial HP.", "effect": "revive", "uses":1, "value":150, "min_spawn_level":5, "rarity": "rare", "revive_fraction":0.5},
    {"id": "defibrillator", "name": "Defibrillator", "description": "A portable defibrillator that can revive a fallen ally with full HP.", "effect": "revive", "uses":1, "value":400, "min_spawn_level":12, "rarity": "superrare", "revive_fraction":1.0},


    # Status-curing commons
    {"id": "ointment", "name": "Balm", "description": "A curative ointment that removes ongoing damage effects", "effect": "cure_continuous_damage", "uses":1, "value":10, "min_spawn_level":1, "rarity": "common"},
    {"id": "petrify_salve", "name": "Limestone Salve", "description": "A gritty salve that helps reverse the process of petrification.", "effect": "cure_petrify", "uses":1, "value":50, "min_spawn_level":1, "rarity": "common"},
    {"id": "wake_potion", "name": "Wake Draught", "description": "A bitter potion that snaps sleepers awake.", "effect": "cure_sleep", "uses":1, "value":15, "min_spawn_level":1, "rarity": "common"},
    {"id": "shock_patch", "name": "Shock Patch", "description": "A small patch that jolts the mind and frees one from stun.", "effect": "cure_stun", "uses":1, "value":20, "min_spawn_level":1, "rarity": "common"},
    {"id": "clarity_tonic", "name": "Clarity Tonic", "description": "A bright tonic that clears the head and cures confusion.", "effect": "cure_confuse", "uses":1, "value":20, "min_spawn_level":1, "rarity": "common"},
    {"id": "vocalsalve", "name": "Vocal Salve", "description": "An herbal salve that soothes and restores the ability to speak.", "effect": "cure_silence", "uses":1, "value":20, "min_spawn_level":1, "rarity": "common"},
    # Universal cure (all status) - very rare / special
    {"id": "panacea", "name": "Doc's Panacea", "description": "A fabled one-shot remedy from a legend — cleanses every negative effect from the body.", "effect": "cure_all_debuffs", "uses":1, "value":800, "min_spawn_level":10, "rarity": "superrare"},



    # Permanent stat-increase tomes (superrare)
    {"id": "tome_hp", "name": "Dummy's Guide to Health", "description": "Permanently increases your max HP by1.", "effect": "stat_increase", "uses":1, "value":500, "min_spawn_level":10, "rarity": "notfound", "stat": "max_hp", "amount":1},
    {"id": "tome_ap", "name": "Dummy's Guide to Focus", "description": "Permanently increases your max AP by1.", "effect": "stat_increase", "uses":1, "value":500, "min_spawn_level":10, "rarity": "notfound", "stat": "max_ap", "amount":1},
    {"id": "tome_str", "name": "Dummy's Guide to Lifting", "description": "Permanently increases your Strength by1.", "effect": "stat_increase", "uses":1, "value":500, "min_spawn_level":10, "rarity": "notfound", "stat": "strength", "amount":1},
    {"id": "tome_dex", "name": "Dummy's Guide to Crossfit", "description": "Permanently increases your Dexterity by1.", "effect": "stat_increase", "uses":1, "value":500, "min_spawn_level":10, "rarity": "notfound", "stat": "dexterity", "amount":1},
    {"id": "tome_int", "name": "Dummy's Encyclopedia of Everything", "description": "Permanently increases your Intelligence by1.", "effect": "stat_increase", "uses":1, "value":500, "min_spawn_level":10, "rarity": "notfound", "stat": "intelligence", "amount":1},
    {"id": "tome_con", "name": "Dummy's Way to Resistance", "description": "Permanently increases your Constitution by1.", "effect": "stat_increase", "uses":1, "value":500, "min_spawn_level":10, "rarity": "notfound", "stat": "constitution", "amount":1},
    # Stronger/superrare versions of the tomes (grant +2 to stat)
    {"id": "tome_hp_superrare", "name": "Masterwork Guide to Health", "description": "Permanently increases your max HP by2.", "effect": "stat_increase", "uses":1, "value":1500, "min_spawn_level":15, "rarity": "notfound", "stat": "max_hp", "amount":2},
    {"id": "tome_ap_superrare", "name": "Masterwork Guide to Focus", "description": "Permanently increases your max AP by2.", "effect": "stat_increase", "uses":1, "value":1500, "min_spawn_level":15, "rarity": "notfound", "stat": "max_ap", "amount":2},
    {"id": "tome_str_superrare", "name": "Masterwork Guide to Strength", "description": "Permanently increases your Strength by2.", "effect": "stat_increase", "uses":1, "value":1500, "min_spawn_level":15, "rarity": "notfound", "stat": "strength", "amount":2},
    {"id": "tome_dex_superrare", "name": "Masterwork Guide to Agility", "description": "Permanently increases your Dexterity by2.", "effect": "stat_increase", "uses":1, "value":1500, "min_spawn_level":15, "rarity": "notfound", "stat": "dexterity", "amount":2},
    {"id": "tome_int_superrare", "name": "Masterwork Encyclopedia of Lore", "description": "Permanently increases your Intelligence by2.", "effect": "stat_increase", "uses":1, "value":1500, "min_spawn_level":15, "rarity": "notfound", "stat": "intelligence", "amount":2},
    {"id": "tome_con_superrare", "name": "Masterwork Way to Resistance", "description": "Permanently increases your Constitution by2.", "effect": "stat_increase", "uses":1, "value":1500, "min_spawn_level":15, "rarity": "notfound", "stat": "constitution", "amount":2},
]





# Special items (unique/quest) - these are rare and may be referenced by NPCs/quests
SPECIAL_ITEM_SEEDS = [
    ### When Special Items eventuall have use effect specials they will relate to task events: create_dungeon, award_task, etc.
    {"id": "ancient_amulet", "name": "Ancient Amulet", "description": "An amulet with unknown runes. It hums faintly.", "effect_description": "May unlock hidden lore or power.", "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "vault_key", "name": "Vault Key", "description": "A heavy iron key stamped with a crest.", "effect_description": "Opens a specific locked vault.", "value":0, "min_spawn_level":1, "rarity": "notfound"},

    ## CH 1 special items 
    {"id": "mnemonic_logger", "name": "Mnemonic Logger", "description": "A compact device that records and plays back memories. It has a worn leather strap and a small screen.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "cursed_couplet", "name": "Cursed Couplet", "description": "A matched set of ritual bracelets, their bands intertwined by corrosion and time. Runes along the inner edges glow faintly when the pair is disturbed.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "ornate_bracers", "name": "Ornate Bracers", "description": "An ornate pair of bracers unsuitable for combat with an intricate design pattern", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    ## CH 2 special items
    {"id": "rare_ingredient_ch2", "name": "Rare Ingredient", "description": "A rare alchemical ingredient sought by many.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "volatile_concoction_ch2", "name": "Volatile Concoction", "description": "A bubbling concoction that seems unstable.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "resonance_shard_ch2", "name": "Resonance Shard", "description": "A shard that vibrates with latent energy.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "grift_stone", "name": "Grift Stone", "description": "A stone imbued with mysterious properties.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "demigorgon_tooth", "name": "Demigorgon Tooth", "description": "A sharp tooth from a demigorgon.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    ## CH 3 special items
    {"id": "scarred_thyme", "name": "Scarred Thyme", "description": "A peculiar herb with leaves that appear to have tiny scars.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "scribe_mint", "name": "Scribe Mint", "description": "A rare mint used in potions with a sharp refreshing taste.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "memory_tonic_ch3", "name": "Lost but not forgotten Tonic", "description": "A tonic that is said to restore lost memories.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    ## CH 5 special items
    {"id": "tracking_map", "name": "Tracking Map", "description": "A magical map used set to track the Bracelet of Existence.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "stormglass_ember", "name": "Stormglass Ember", "description": "A fragment of stormglass that glows with inner light.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "dorians_sketch_of_distortion", "name": "Dorian's Sketch of Distortion", "description": "A sketchbook page with Dorian's scratchings of a distorted figure... It's quite curvaceous", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    ## CH 6 special items
    {"id": "riftland_stabilizer_core", "name": "Riftland Stabilizer Core", "description": "A core component of the Riftland Stabilizer, humming with unstable energy.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    ## CH 13 special items
    {"id": "voice_of_lost_loved_ones", "name": "Voice of Lost Loved Ones", "description": "A small, enchanted music box that plays a haunting melody. It is said to carry the voices of lost loved ones.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "key_to_grand_mausoleum", "name": "Key to the Grand Mausoleum", "description": "An ornate key that is said to unlock the Grand Mausoleum, a place of great significance.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    ## CH 15 special items
    {"id": "pageant_mask", "name": "Pageant Mask", "description": "A beautifully crafted mask used in ancient pageants. It is said to grant the wearer a glimpse of past performances.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    ## CH 17 special items
    {"id": "puzzle_box_legend", "name": "Legend to a Puzzle Box", "description": "A worn parchment containing a legend about a mysterious puzzle box. The legend hints at the box's location and the rewards it holds.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "echofoil_nullglass", "name": "Echofoil Nullglass", "description": "A shard of echofoil nullglass that absorbs sound and light, creating an eerie silence around it.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "puzzle_box", "name": "Puzzle Box", "description": "A mysterious box with intricate carvings and a complex locking mechanism. Solving the puzzle is said to reveal great secrets.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},
    ## CH 20 special items
    {"id": "memory_tonic_ch20", "name": "Memory Tonic", "description": "A rare tonic that is said to restore lost memories. It has a sweet, nostalgic scent.", "effect_description": None, "value":0, "min_spawn_level":1, "rarity": "notfound"},

    #7 region deliver items (region-specific heirlooms used by primary stories)
    {"id": "heirloom_ring", "name": "Heirloom Ring", "description": "A wind-etched ring of braided silver, its filigree whispers of open plains.", "effect_description": "", "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "dune_sundial", "name": "Dune Sundial", "description": "A small brass dial rimed with grit; when held to the sun it casts three shadowed spokes.", "effect_description": "", "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "grove_lattice", "name": "Grove Lattice", "description": "A woven lattice of root and resin, faintly warm and humming with old growth.", "effect_description": "", "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "coreforge_shard", "name": "Coreforge Shard", "description": "A sliver of volcanic glass ringed in metalwork — it thrums with slow, tectonic heat.", "effect_description": "", "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "moontide_orb", "name": "Moontide Orb", "description": "A translucent bead that glows faintly at night; droplets bead on its surface as if remembering surf.", "effect_description": "", "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "boreal_clasp", "name": "Boreal Clasp", "description": "A frosted metal clasp engraved with wind sigils; it leaves a cold print on skin for a moment.", "effect_description": "", "value":0, "min_spawn_level":1, "rarity": "notfound"},
    {"id": "mirethread_pendant", "name": "Mirethread Pendant", "description": "A pendant braided from preserved reeds and small vertebrae, smelling faintly of peat and iron.", "effect_description": "", "value":0, "min_spawn_level":1, "rarity": "notfound"},

    # SPECIAL RIFT ITEMS FOUND IN THE FIRST FRACTURE
    {"id":"rift_dust", "name":"Rift Dust", "description":"A small vial of shimmering dust that seems to warp light around it.  This looks like it could be mixed into an illicit potion.", "effect_description":"", "value":0, "min_spawn_level":1, "rarity":"notfound"},
    {"id":"unstable_relic", "name":"Unstable Relic", "description":"An ancient relic that crackles with unpredictable energy.  It looks like it would fetch a high price on the black market.", "effect_description":"", "value":0, "min_spawn_level":1, "rarity":"notfound"},

    {"id":"phase_crystal", "name":"Phase Crystal", "description":"A crystal that phases in and out of visibility, pulsing with an inner light.", "effect_description":"", "value":0, "min_spawn_level":1, "rarity":"notfound"},
    {"id":"rift_core", "name":"Rift Core", "description":"A dense core of condensed rift energy, humming with unstable power.", "effect_description":"", "value":0, "min_spawn_level":1, "rarity":"notfound"},
    {"id":"bracelet_of_void", "name":"Bracelet of the Void", "description":"A dark bracelet that seems to absorb light, with an unsettling aura.", "effect_description":"", "value":0, "min_spawn_level":1, "rarity":"notfound"},
    {"id":"bracelet_of_existence", "name":"Bracelet of Existence", "description":"A radiant bracelet that emits a soft glow, it eminates the power of life and creation.", "effect_description":"", "value":0, "min_spawn_level":1, "rarity":"notfound"},
]

# Export convenience lists for simple random selection
SEED_WEAPON_IDS = [w["id"] for w in WEAPON_SEEDS]
SEED_ARMOR_IDS = {slot: [a["id"] for a in group] for slot, group in ARMOR_SEEDS.items()}
SEED_UTILITY_IDS = [u["id"] for u in UTILITY_ITEM_SEEDS]
SEED_SPECIAL_IDS = [s["id"] for s in SPECIAL_ITEM_SEEDS]