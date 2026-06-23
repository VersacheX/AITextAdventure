CITY_NAME = "Aurelion Veil"
CITY_DESCRIPTION = (
    "A sprawling city nestled within the ancient boughs of colossal trees, Aurelion Veil is a sanctuary where nature and civilization intertwine. "
    "The city's architecture is a harmonious blend of living wood and crafted stone, with homes and shops carved directly into the trunks "
    "and branches of the great trees. Bioluminescent flora illuminate the streets, casting a gentle glow that guides residents and visitors "
    "alike through the winding pathways. The air is filled with the scent of moss and blooming flowers, creating an atmosphere of tranquility "
    "amidst the bustling market squares and lively taverns. Aurelion Veil is renowned for its skilled artisans, herbalists, and mystics who "
    "draw upon the forest's magic to create wondrous goods and potions. The city thrives on a deep respect for nature, with communal gardens "
    "and sacred groves serving as places of reflection and celebration. Visitors to Aurelion Veil are often captivated by its serene beauty "
    "and the harmonious coexistence of its inhabitants with the surrounding wilderness."        
)

# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified
# heal_fraction <- fraction of max HP restored <- do not modify
ROOM_MENU = [
 {"id": "public", "name": "Root Bench", "value":8, "heal_fraction":0.25},
 {"id": "economy", "name": "Canopy Cot", "value":40, "heal_fraction":0.75},
 {"id": "luxury", "name": "Silken Arbor Suite", "value":220, "heal_fraction":1.0},
]

# Simple in-bar drinks menu. Effects are immediate and don't create inventory items.
# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified slightly... bigger drinks are naturally more expensive as buying a drink triggers rng for an enemy, so buying small doesn't pay
# hp_fraction <- fraction of max HP restored immediately <- do not modify
DRINK_MENU = [
 {"id": "tiny", "name": "Saplight Draught", "value":12, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
 {"id": "small", "name": "Murkflower Mead", "value":24, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
 {"id": "mid", "name": "Moonvine Cocktail", "value":50, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
 {"id": "big", "name": "Nocturn Elixir", "value":110, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
 {"id": "huge", "name": "Shadebloom Draught", "value":220, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":5},
 {"id": "max", "name": "Aurelian Serum", "value":360, "hp_fraction":1.00, "ap_fraction":0.35, "min_level":8},
]

# Buildings
# name <- building internal id <- do not modify
# display_name <- building display name <- can be modified
# type (bar, inn, shop, residence, business) <- building subtype <- do not modify
# char <- regional console map character --- must be ascii + extended ascii only <- do not modify
# seed_range <- territorial range of buildings(how close they can be to another of the same name)
# threshold <- determines how high multilevel buildings can grow
# hostile_prob <- probability of enemy encounter on entry
# can_buy <- whether the building type supports buying items
# can_sell <- whether the building type supports selling items
BUILDINGS = [
 {"name": "bar", "display_name": "The Gilded Bramble", "type": "bar", "char": "µ", "seed_range":6, "threshold":0.04, "hostile_prob":0.30, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#2a4a3a"},
 {"name": "inn", "display_name": "Evensong Rest", "type": "inn", "char": "@", "seed_range":10, "threshold":0.09, "hostile_prob":0.00, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#4b6b5a"},
 {"name": "shopweapons", "display_name": "Thistle & Fang", "type": "shop", "char": "Æ", "seed_range":12, "threshold":0.22, "hostile_prob":0.05, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#5a2f2f"},
 {"name": "shopitems", "display_name": "Silvershard Curios", "type": "shop", "char": "₨", "seed_range":12, "threshold":0.40, "hostile_prob":0.04, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#344b4b"},
 {"name": "shoparmor", "display_name": "Grovewarden Armory", "type": "shop", "char": "¥", "seed_range":12, "threshold":0.56, "hostile_prob":0.04, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#6b6b5b"},
 {"name": "residencelarge", "display_name": "Palais of Boughs", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.78, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#2e5b3a"},
 {"name": "residencesmall", "display_name": "Sylvan Chambers", "type": "residence", "char": "î", "seed_range":4, "threshold":0.94, "hostile_prob":0.12, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#3b6b4a"},
 {"name": "businesslarge", "display_name": "Council of Veil", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.99, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#243a2f"},
 {"name": "businesssmall", "display_name": "Ledger & Lantern", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#274b3a"},
 {"name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range":1000, "threshold":0.02, "hostile_prob":0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070"},
 {"name": "other1", "display_name": "Hollow Exchange", "type": "other1", "char": "O", "seed_range":1000, "threshold":0.06, "hostile_prob":0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#4b0082"},
 {"name": "other2", "display_name": "Branchbound Broker's Den", "type": "other2", "char": "0", "seed_range":1000, "threshold":0.06, "hostile_prob":0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#4b0082"},
]

# Internal sublocations per subtype
# Used when generating buildings to add searchable sublocations.
SUBLOC_MAP = {
 "shop": ["apothecary alcove", "arcane display", "silken shelf", "file ledge", "vault niche", "curio pedestal"],
 "bar": ["moss bench", "ember shelf", "backroom glade", "whisper nook", "lock brazier", "bottle grove"],
 "inn": ["common arboreal", "guest loft", "dresser alcove", "drawer trunk", "balcony perch", "hearth niche"],
 "residence": ["kitchen alcove", "sleeping loft", "cloister closet", "bathe basin", "root pantry", "dresser trunk", "storage chest", "lockbox nook", "drawer slot"],
 "business": ["reception bower", "council office", "bath alcove", "file ledger", "utility hollow", "storage chest", "vault niche", "ledger alcove"],
 "alley": ["moss pile", "fallen limb", "hidden alcove", "vendor stall", "service root", "dumpster hollow", "alley crate", "sigil wall"],
 "street": ["market stall", "fountain pool", "carriage stump", "vendor stall", "display case", "back shelf", "message post", "mail hollow", "newsleaf", "parking post", "newsbox"],
 "arcane": ["ritual ring", "sigil cache", "enchanted chest", "altar niche", "sylvan rune"],
}

# SubLocation metadata definitions used when building locations.
# Each entry provides defaults used by the generator and later logic (searchable, loot chance, prompt, etc.).
SUBLOCATION_DEFS = {
 "apothecary alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A cramped apothecary alcove filled with jars and pressed petals.", "money_range": (6,30)},
 "arcane display": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "An arcane display of sigils and glasswork humming faintly.", "money_range": (8,36)},
 "silken shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "Shelves draped in dark silk, small trinkets tucked between folds.", "money_range": (4,22)},
 "file ledge": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A ledge of scrolls and ledger leaves; one seems dog-eared.", "money_range": (2,24)},
 "vault niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A small sealed niche with cold metal and carved vines.", "money_range": (12,80)},
 "curio pedestal": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A pedestal holding a single curio under a bell jar.", "money_range": (6,28)},

 "moss bench": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A moss-lined bench where whispered deals are traded.", "money_range": (1,8)},
 "ember shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shelf warmed by a perpetual ember; bottles and notes lie discarded.", "money_range": (2,14)},
 "backroom glade": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A hidden glade behind the bar stacked with barrels and secrets.", "money_range": (4,20)},
 "whisper nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A narrow nook where whispers collect like dust.", "money_range": (2,18)},
 "lock brazier": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "An iron brazier with an embedded lockbox beneath the coals.", "money_range": (6,36)},
 "bottle grove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A clustered shelf of bottles, some labeled in an unfamiliar script.", "money_range": (3,20)},

 "common arboreal": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A common room carved into living wood with low seats and dim lamps.", "money_range": (8,30)},
 "guest loft": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A suspended guest loft with silk curtains and hidden pockets.", "money_range": (4,26)},
 "dresser alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A narrow alcove with a carved dresser; one drawer resists.", "money_range": (2,18)},
 "drawer trunk": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A trunk drawer swollen with old maps and letters.", "money_range": (3,22)},
 "balcony perch": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A narrow balcony overlooking the Veil, coins and charms tucked in crevices.", "money_range": (1,12)},
 "hearth niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A hearth niche where herbs are dried and small pouches hide.", "money_range": (2,16)},

 "kitchen alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A tiny kitchen alcove with jars and a sharpened knife.", "money_range": (1,8)},
 "sleeping loft": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "A sleeping loft with woven mats and a hidden pouch beneath.", "money_range": (1,12)},
 "cloister closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A small closet hung with ritual cloths and long-stitched receipts.", "money_range": (0,10)},
 "bathe basin": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A stone basin with scented oils and a curled coin under the lip.", "money_range": (0,10)},
 "root pantry": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A cool root pantry stacked with jars and the rustle of hidden things.", "money_range": (2,22)},

 "reception bower": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A reception bower with a ledger bound in bark.", "money_range": (1,12)},
 "council office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A council office strewn with decrees and a sealed envelope.", "money_range": (2,18)},
 "file ledger": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A file ledge with brittle pages and a tucked coin.", "money_range": (2,24)},
 "utility hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A utility hollow with ropes and an old invoice rolled away.", "money_range": (0,12)},
 "ledger alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A narrow alcove where ledgers sleep; the margins hold notes.", "money_range": (1,20)},

 "moss pile": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A pile of damp moss; something metallic glints within.", "money_range": (0,10)},
 "fallen limb": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A fallen limb hollowed by time; a wrapped bundle is tucked inside.", "money_range": (1,14)},
 "hidden alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A hidden alcove where smugglers once left parcels.", "money_range": (2,22)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A vendor stall of bark and woven trays; a coin rolls free.", "money_range": (2,18)},
 "service root": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A service root with iron fittings and a stuck compartment.", "money_range": (0,8)},
 "dumpster hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A hollow under old boards where refuse and rare finds mingle.", "money_range": (0,12)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A stack of wooden crates in the branchway — one is unlatched.", "money_range": (1,16)},
 "sigil wall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A wall of carved sigils; one stone is loose and hides a coin.", "money_range": (0,18)},

 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A bustling market stall of woven baskets and oddities.", "money_range": (4,24)},
 "fountain pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A still pool fed by a carved fountain; coins glint beneath algae.", "money_range": (6,30)},
 "carriage stump": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A stump used as a carriage post; a rusted clasp hides within.", "money_range": (0,12)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A glass display case housing small trinkets; one looks loose.", "money_range": (2,20)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A back shelf behind a stall where coins and notes gather dust.", "money_range": (0,12)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A post where messages are pinned; a folded note flutters loose.", "money_range": (0,8)},
 "mail hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A hollowed mail post with old envelopes and the scent of ink.", "money_range": (0,10)},
 "newsleaf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A stack of newsleaves; one conceals a pressed leaflet with a price.", "money_range": (1,12)},
 "parking post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A post where small tokens are left; coins sometimes fall free.", "money_range": (0,6)},
 "newsbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A carved newsbox stuffed with yesterday's leaves and a folded note.", "money_range": (0,12)},

 "ritual ring": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A ritual ring scarred with old offerings and faint ash.", "money_range": (4,40)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cache of small engraved sigils humming softly.", "money_range": (8,36)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "An enchanted chest that resists curious fingers unless coaxed.", "money_range": (10,60)},
 "altar niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A carved altar niche with offerings and a coin tucked beneath.", "money_range": (5,30)},
 "sylvan rune": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A rune etched into living bark; the grooves hide a tiny token.", "money_range": (0,20)},
}