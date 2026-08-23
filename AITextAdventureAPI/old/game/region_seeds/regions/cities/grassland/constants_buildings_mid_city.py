CITY_NAME = "Highsteeple Crossing" # mid-sized grasslands city with pious, sanctimonious rulers
CITY_DESCRIPTION = (
	"Highsteeple Crossing is a bustling mid-sized city nestled in the heart of the expansive grasslands."
	"Known for its towering spires and grand cathedrals, the city serves as a religious and cultural hub for the surrounding region."
	"he streets are lined with cobblestone pathways, and the air is filled with the scent of incense and blooming wildflowers."
)

# Room Menu
# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified
# heal_fraction <- fraction of max HP restored <- do not modify
ROOM_MENU = [
 {"id": "public", "name": "Stone Ledge", "value":7, "heal_fraction":0.25},
 {"id": "economy", "name": "Chamber Loft", "value":38, "heal_fraction":0.75},
 {"id": "luxury", "name": "Canon Suite", "value":160, "heal_fraction":1.0},
]

# Drinks Menu
# Simple in-bar drinks menu. Effects are immediate and don't create inventory items.
# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified slightly
# hp_fraction <- fraction of max HP restored immediately <- do not modify
DRINK_MENU = [
 {"id": "tiny", "name": "Pewter Ale", "value":10, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
 {"id": "small", "name": "Cleric's Mead", "value":22, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
 {"id": "mid", "name": "Vesper Cocktail", "value":50, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
 {"id": "big", "name": "Prelate Elixir", "value":110, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
 {"id": "huge", "name": "Throne Draught", "value":230, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":5},
 {"id": "max", "name": "Highsteeple Serum", "value":420, "hp_fraction":1.00, "ap_fraction":0.30, "min_level":8},
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
	{ "name": "bar", "display_name": "The Cloister Tap", "type": "bar", "char": "µ", "seed_range":6, "threshold":0.04, "hostile_prob":0.35, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#5b3b3b"},
	{ "name": "inn", "display_name": "The Vestry Rest", "type": "inn", "char": "@", "seed_range":6, "threshold":0.07, "hostile_prob":0.00, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#6b5b4f"},
	{ "name": "shopweapons", "display_name": "Pious Blades", "type": "shop", "char": "Æ", "seed_range":10, "threshold":0.18, "hostile_prob":0.04, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#7a2f2f"},
	{ "name": "shopitems", "display_name": "Reliquary & Oddments", "type": "shop", "char": "₨", "seed_range":10, "threshold":0.36, "hostile_prob":0.03, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#4b5b4b"},
	{ "name": "shoparmor", "display_name": "Vestments & Vambraces", "type": "shop", "char": "¥", "seed_range":10, "threshold":0.52, "hostile_prob":0.03, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#6b6b5b"},
	{ "name": "residencelarge", "display_name": "Aldermanic Row", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.70, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#dfe7c8"},
	{ "name": "residencesmall", "display_name": "Cantor Cottages", "type": "residence", "char": "î", "seed_range":4, "threshold":0.9, "hostile_prob":0.10, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#efe7d0"},
	{ "name": "businesslarge", "display_name": "The Diocese Exchange", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.95, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#c0c0c0"},
	{ "name": "businesssmall", "display_name": "Ledger & Sermon", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#c0b88f"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "Highspire Doctrine Hall", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#7b30a2" }, 
	{ "name": "other2", "display_name": "The Sanctum of Quiet Oaths", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#7b30a2" }
]

# Sublocation mapping
# Internal sublocations per subtype used when generating buildings to add searchable sublocations.
SUBLOC_MAP = {
 "shop": ["rear reliquary", "crate storage", "gallery case", "shelf unit", "file alcove", "vault niche"],
 "bar": ["tap shelf", "keg store", "back alcove", "pew bench", "lock brazier", "whisper alcove"],
 "inn": ["common hall", "guest chamber", "dresser", "drawer", "coat niche", "hearth shelf"],
 "residence": ["kitchen", "bedroom", "closet", "wash basin", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer"],
 "business": ["reception", "office", "bathroom", "file cabinet", "utility cabinet", "storage chest", "vault niche"],
 "alley": ["trash heap", "abandoned cart", "hidden alcove", "vendor stall", "service hatch", "dumpster hollow", "alley crate", "sigil wall"],
 "street": ["market stall", "fountain pool", "wagon post", "vendor stall", "display case", "back shelf", "message post", "mailbox", "newsstand", "parking post", "newsbox"],
 "arcane": ["ritual ring", "sigil cache", "enchanted chest", "altar niche", "sanctum rune"],
}

# SubLocation metadata definitions used when building locations.
# Each entry provides defaults used by the generator and later logic (searchable, loot chance, prompt, etc.).
SUBLOCATION_DEFS = {
 "rear reliquary": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A cramped rear reliquary filled with wrapped icons and jars.", "money_range": (4,28)},
 "crate storage": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.24, "prompt": "A stacked row of crates stamped with merchant marks.", "money_range": (2,18)},
 "gallery case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A glass gallery case displaying foreign reliquaries and trinkets.", "money_range": (6,32)},
 "shelf unit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A crowded shelf unit of odds and ends; one tag flutters loose.", "money_range": (0,8)},
 "file alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "An alcove of ledgers and petition slips; something is tucked between pages.", "money_range": (2,24)},
 "vault niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A small vault niche sealed behind carved stone.", "money_range": (10,80)},

 "tap shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shelf behind the taps where coins and vows accumulate.", "money_range": (1,12)},
 "keg store": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A cool nook of kegs and ledger scraps.", "money_range": (2,14)},
 "back alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A tucked-away alcove where hushed deals are struck.", "money_range": (1,18)},
 "pew bench": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A worn bench where locals fold notes into prayers.", "money_range": (0,8)},
 "lock brazier": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "An iron brazier concealing a small locked compartment.", "money_range": (4,36)},
 "whisper alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A narrow alcove where rumors and IOUs are traded.", "money_range": (2,18)},

 "common hall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A timbered hall hung with banners where petitions are read.", "money_range": (5,30)},
 "guest chamber": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A modest chamber with a loose board hiding a note.", "money_range": (2,18)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A battered dresser with a stuck drawer; something rattles within.", "money_range": (1,14)},
 "drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "A shallow drawer with receipts and a folded photograph.", "money_range": (1,10)},
 "coat niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A small niche of cloaks; a pocket hides a coin.", "money_range": (0,10)},
 "hearth shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A shelf above the hearth with dried herbs and lost trinkets.", "money_range": (1,12)},

 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A busy kitchen with jars, knives, and a hidden spice pouch.", "money_range": (1,10)},
 "bedroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A small bedroom with a woven bed and a coin tucked under the mat.", "money_range": (1,12)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A narrow closet full of garments and a sealed envelope.", "money_range": (0,8)},
 "wash basin": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A basin with suds and a copper token lodged beneath.", "money_range": (0,8)},
 "cupboard": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A grease-stained cupboard with mismatched plates and a secret stain.", "money_range": (0,8)},
 "pantry": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A pantry of dried goods and a hidden sachet of herbs.", "money_range": (1,14)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "An old chest sealed with straps; something clinks within.", "money_range": (2,20)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A small iron lockbox bolted to a shelf — someone once trusted this.", "money_range": (2,18)},

 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A worn reception desk with ledger sheets and a stub of wax.", "money_range": (1,12)},
 "office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cramped office piled high with petitions and sealed envelopes.", "money_range": (2,20)},
 "utility cabinet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cabinet of tools and invoices; something peeks from the corner.", "money_range": (0,10)},

 "trash heap": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A heap of refuse where lost trinkets are sometimes unearthed.", "money_range": (0,8)},
 "abandoned cart": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A rotting cart; a wrapped bundle hides inside.", "money_range": (1,16)},
 "hidden alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A secret alcove between stalls where billets are swapped.", "money_range": (2,22)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A vendor stall stacked with foreign wares; a coin rolls loose.", "money_range": (2,18)},
 "service hatch": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A small hatch used for deliveries and whispered exchanges.", "money_range": (0,8)},
 "dumpster hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A hollow under crates where refuse and rare finds mingle.", "money_range": (0,12)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A weathered crate in the alley — straps are loose.", "money_range": (1,14)},
 "sigil wall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A wall carved with sigils; one stone is loose and hides something small.", "money_range": (0,8)},

 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A busy market stall piled with goods from across the grasslands.", "money_range": (4,28)},
 "fountain pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A carved fountain fed by a distant spring; coins glint beneath algae.", "money_range": (6,40)},
 "wagon post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A post where caravans tie; straps hide small pouches.", "money_range": (1,18)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A glass case of curios; one tag is loose.", "money_range": (2,20)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A back shelf where small notes and change collect.", "money_range": (0,12)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A post of pinned notices; one envelope flutters free.", "money_range": (0,8)},
 "mailbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A battered mailbox stuffed with letters and a faded receipt.", "money_range": (0,10)},
 "newsstand": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A piled newsstand; a pamphlet slips out when you flip through.", "money_range": (1,16)},
 "parking post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A post where small tokens are left; coins sometimes fall free.", "money_range": (0,6)},
 "newsbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A carved newsbox stuffed with flyers and a folded note.", "money_range": (0,12)},

 "ritual ring": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A ring of stones scarred with old offerings and faint ash.", "money_range": (4,40)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cache of engraved sigils humming with odd power.", "money_range": (8,36)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "An enchanted chest that resists prying fingers unless coaxed.", "money_range": (10,60)},
 "altar niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A carved niche with offerings and a tucked coin.", "money_range": (5,30)},
 "sanctum rune": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A rune etched into stone; its grooves hide a tiny token.", "money_range": (0,20)},
}