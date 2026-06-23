CITY_NAME = "Crosswind Bazaar"
CITY_DESCRIPTION = (
	"A bustling trade hub nestled within the vast grasslands, where colorful tents and sturdy stone buildings form a lively marketplace. "
	"The air is filled with the sounds of haggling merchants, clinking coins, and the distant calls of exotic animals. "
	"Caravans from far-off lands converge here, bringing with them a rich tapestry of goods, spices, and artifacts. "
	"The streets are lined with vendors selling everything from finely crafted weapons to rare textiles, while the aroma of sizzling street food wafts through the air. "
	"At the heart of the bazaar lies the Wayfarer's Rest Inn, a welcoming haven for travelers seeking respite from their journeys. "
	"The atmosphere is one of vibrant energy and endless possibility, where every corner holds the promise of a new discovery."
)

# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified
# heal_fraction <- fraction of max HP restored <- do not modify
ROOM_MENU = [
 {"id": "public", "name": "Stone Bench", "value":7, "heal_fraction":0.25},
 {"id": "economy", "name": "Renting Loft", "value":45, "heal_fraction":0.75},
 {"id": "luxury", "name": "Skybox Suite", "value":300, "heal_fraction":1.0},
]

# Simple in-bar drinks menu. Effects are immediate and don't create inventory items.
# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified slightly... bigger drinks are naturally more expensive as buying a drink triggers rng for an enemy, so buying small doesn't pay
# hp_fraction <- fraction of max HP restored immediately <- do not modify
DRINK_MENU = [
 {"id": "tiny", "name": "Steppe Ale", "value":10, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
 {"id": "small", "name": "Trader's Mead", "value":22, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
 {"id": "mid", "name": "Crosswind Cocktail", "value":55, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
 {"id": "big", "name": "Gale Elixir", "value":115, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
 {"id": "huge", "name": "Caravan Draught", "value":230, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":5},
 {"id": "max", "name": "Bazaar Serum", "value":420, "hp_fraction":1.00, "ap_fraction":0.30, "min_level":8},
]

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
	{ "name": "bar", "display_name": "The Sundered Keg", "type": "bar", "char": "µ", "seed_range":6, "threshold":0.04, "hostile_prob":0.36, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#6b3e2f"},
	{ "name": "inn", "display_name": "Wayfarer's Rest", "type": "inn", "char": "@", "seed_range":10, "threshold":0.08, "hostile_prob":0.00, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#7a6b5c"},
	{ "name": "shopweapons", "display_name": "Windsong Armory", "type": "shop", "char": "Æ", "seed_range":12, "threshold":0.20, "hostile_prob":0.05, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#5a2f2f"},
	{ "name": "shopitems", "display_name": "Nomad Curios", "type": "shop", "char": "₨", "seed_range":12, "threshold":0.38, "hostile_prob":0.03, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#4b5b4b"},
	{ "name": "shoparmor", "display_name": "Hearth & Hide", "type": "shop", "char": "¥", "seed_range":12, "threshold":0.54, "hostile_prob":0.03, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#6b6b5b"},
	{ "name": "residencelarge", "display_name": "Steppe Spires", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.75, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#dfe7c8"},
	{ "name": "residencesmall", "display_name": "Caravan Rows", "type": "residence", "char": "î", "seed_range":4, "threshold":0.92, "hostile_prob":0.10, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#efd"},
	{ "name": "businesslarge", "display_name": "Consulate Quarter", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.98, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#c0c0c0"},
	{ "name": "businesssmall", "display_name": "Market Annex", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#c0b88f"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "Spicewind Menagerie", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#4b0082" }, 
	{ "name": "other2", "display_name": "The Caravaner’s Exchange", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#4b0082" }
]

# Internal sublocations per subtype
# Used when generating buildings to add searchable sublocations.
SUBLOC_MAP = {
 "shop": ["back stall", "crate storage", "canopy display", "shelf unit", "ledger box", "vault niche"],
 "bar": ["tap trough", "keg nook", "ember shelf", "cloak peg", "lock brazier", "notice board"],
 "inn": ["common hall", "guest berth", "dresser alcove", "trunk drawer", "stables", "hearth shelf"],
 "residence": ["kitchen nook", "sleeping loft", "closet nook", "wash basin", "pantry box", "dresser trunk", "storage chest", "lockbox", "drawer slot"],
 "business": ["reception desk", "council office", "wash alcove", "file chest", "utility nook", "storage chest", "vault niche", "ledger alcove"],
 "alley": ["trash heap", "abandoned wagon", "hidden alcove", "vendor stall", "service hatch", "dumpster hollow", "alley crate", "banner wall"],
 "street": ["market stall", "fountain pool", "caravan post", "vendor stall", "display case", "back shelf", "message post", "mail box", "newsstand", "parking post", "newsbox"],
 "arcane": ["ritual ring", "sigil cache", "enchanted chest", "altar niche", "wind rune"],
}

# SubLocation metadata definitions used when building locations.
# Each entry provides defaults used by the generator and later logic (searchable, loot chance, prompt, etc.).
SUBLOCATION_DEFS = {
 "back stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A cramped back stall where merchants hide extra stock.", "money_range": (3,20)},
 "crate storage": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.24, "prompt": "A row of crates stamped with foreign sigils.", "money_range": (2,18)},
 "canopy display": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A sun-faded canopy hung with trinkets and tags.", "money_range": (4,28)},
 "shelf unit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cluttered shelf unit with odds and ends.", "money_range": (0,10)},
 "ledger box": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A locked ledger box filled with receipts and IOUs.", "money_range": (2,30)},
 "vault niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A small vault niche hidden behind a false panel.", "money_range": (10,80)},

 "tap trough": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A wooden trough used for serving ale; coins and notes collect in the cracks.", "money_range": (1,12)},
 "keg nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A tucked-away nook with a row of dusty kegs.", "money_range": (2,14)},
 "ember shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shelf warmed by embers where bottles and slips gather.", "money_range": (1,10)},
 "cloak peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A peg with a weathered cloak; pockets might hide something.", "money_range": (0,8)},
 "lock brazier": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A brazier with a hidden compartment beneath the coals.", "money_range": (4,36)},
 "notice board": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A battered notice board with pinned ads and a folded note.", "money_range": (0,10)},

 "common hall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A communal hall where tales and debts are told.", "money_range": (5,30)},
 "guest berth": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A narrow berth with a loose floorboard and tucked notes.", "money_range": (2,18)},
 "dresser alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A small alcove with a dresser; one drawer is stuck.", "money_range": (1,14)},
 "trunk drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A travel trunk with maps and a hidden pouch.", "money_range": (3,24)},
 "stables": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A stable stall with lost saddlebags and bridle bits.", "money_range": (1,20)},
 "hearth shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A shelf above the hearth with dried herbs and small pouches.", "money_range": (1,12)},

 "kitchen nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A tiny kitchen nook with jars and a wrapped spice sack.", "money_range": (1,10)},
 "sleeping loft": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "A loft with woven mats and a concealed pouch.", "money_range": (1,14)},
 "closet nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A narrow closet with hanging coats and hidden seams.", "money_range": (0,8)},
 "wash basin": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A basin with suds and a copper coin lodged beneath.", "money_range": (0,8)},
 "pantry box": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A small pantry box of dried goods; something rattles inside.", "money_range": (1,16)},
 "dresser trunk": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A trunk folded with linens; a seam hides a coin.", "money_range": (1,14)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "An old chest bound with straps; something clinks within.", "money_range": (2,20)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A small iron lockbox bolted to a shelf — someone once trusted this.", "money_range": (2,18)},
 "drawer slot": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A shallow drawer with receipts and a folded photograph tucked away.", "money_range": (1,12)},

 "reception desk": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A worn desk with ledger sheets and a stub of wax.", "money_range": (1,12)},
 "council office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "An office stacked with decrees and a sealed parcel.", "money_range": (2,20)},
 "wash alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A small wash alcove with cracked tiles and a loose coin.", "money_range": (0,8)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A chest of files with brittle receipts and a tucked note.", "money_range": (2,24)},
 "utility nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A nook of tools and rope; an invoice peeks from the corner.", "money_range": (0,12)},
 "ledger alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "An alcove where ledgers rest; margins hide scribbled sums.", "money_range": (1,20)},

 "trash heap": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A heap of refuse where lost trinkets sometimes surface.", "money_range": (0,8)},
 "abandoned wagon": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "An old wagon left to rot; a wrapped bundle sits inside.", "money_range": (1,16)},
 "hidden alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A secret alcove between stalls where billets are swapped.", "money_range": (2,22)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A vendor stall of braided baskets and wares; a coin falls loose.", "money_range": (2,18)},
 "service hatch": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A small service hatch used for deliveries and whispers.", "money_range": (0,8)},
 "dumpster hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A hollow under crates where refuse and rare finds mingle.", "money_range": (0,12)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A weathered crate in the alley — straps are loose.", "money_range": (1,14)},
 "banner wall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A wall of woven banners; one corner hides a pin.", "money_range": (0,10)},

 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A busy market stall piled with goods from across the plains.", "money_range": (4,28)},
 "fountain pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A carved fountain fed by a distant spring; coins glint below.", "money_range": (6,40)},
 "caravan post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A post where caravans tie; straps hide small pouches.", "money_range": (1,18)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A glass case of curios; one tag is loose.", "money_range": (2,20)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A back shelf where small notes and change collect.", "money_range": (0,12)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A post of pinned notices; one envelope flutters free.", "money_range": (0,8)},
 "mail box": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A battered mailbox with folded letters and the scent of ink.", "money_range": (0,10)},
 "newsstand": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A piled newsstand; a pamphlet slips out when you flip through.", "money_range": (1,16)},
 "parking post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A post bearing small tokens and forgotten coins.", "money_range": (0,6)},
 "newsbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A carved newsbox stuffed with flyers and a folded note.", "money_range": (0,12)},

 "ritual ring": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A ring of stones etched with old offerings and ash.", "money_range": (4,40)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cache of small sigils humming with distant power.", "money_range": (8,36)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "An enchanted chest that resists prying fingers unless coaxed.", "money_range": (10,60)},
 "altar niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A carved niche with offerings and a tucked coin.", "money_range": (5,30)},
 "wind rune": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A rune carved into a standing stone; its grooves hide a tiny token.", "money_range": (0,20)},
}