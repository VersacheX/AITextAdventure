CITY_NAME = "Gallows Rift"
CITY_DESCRIPTION = (
	"A sprawling settlement built into the jagged cliffs and rocky outcrops of a vast mountain range. "
	"Once a mining town, Gallows Rift has transformed into a bustling hub for traders, adventurers, and outcasts seeking refuge from the dangers of the wilds. "
	"The city's architecture is a mix of makeshift shanties and sturdy stone buildings, all interconnected by a labyrinth of rickety bridges and narrow pathways that cling to the mountainside. "
	"Despite its rough exterior, Gallows Rift is a place of opportunity and camaraderie, where diverse cultures converge and tales of daring exploits are shared around flickering campfires. "
	"However, the city's precarious location also means that danger is never far away, with treacherous cliffs, sudden rockslides, and lurking predators posing constant threats to its inhabitants."
)

# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified
# heal_fraction <- fraction of max HP restored <- do not modify
ROOM_MENU = [
 {"id": "public", "name": "Ridge Bench", "value":6, "heal_fraction":0.25},
 {"id": "economy", "name": "Bunk Loft", "value":30, "heal_fraction":0.75},
 {"id": "luxury", "name": "Riveted Suite", "value":140, "heal_fraction":1.0},
]

# Simple in-bar drinks menu. Effects are immediate and don't create inventory items.
# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency  <- can be modified slightly... bigger drinks are naturally more expensive as buying a drink triggers rng for an enemy, so buying small doesn't pay
# hp_fraction <- fraction of max HP restored immediately <- do not modify
DRINK_MENU = [
 {"id": "tiny", "name": "Char Ale", "value":9, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
 {"id": "small", "name": "Coal Cider", "value":20, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
 {"id": "mid", "name": "Gutter Grog", "value":45, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
 {"id": "big", "name": "Orcish Stout", "value":95, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
 {"id": "huge", "name": "Wyrm Draught", "value":190, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":5},
 {"id": "max", "name": "Rift Serum", "value":340, "hp_fraction":1.00, "ap_fraction":0.30, "min_level":7},
]

# name <- building internal id <- do not modify
# display_name <- building display name <- can be modified
# type (bar, inn, shop, residence, business) <- building subtype <- do not modify
# char <- regional console map character  --- must be ascii + extended ascii only <- do not modify
# seed_range <- territorial range of buildings(how close they can be to another of the same name)
# threshold <- determines how high multilevel buildings can grow
# hostile_prob <- probability of enemy encounter on entry
# can_buy <- whether the building type supports buying items
# can_sell <- whether the building type supports selling items
BUILDINGS = [
	{ "name": "bar", "display_name": "The Iron Maw", "type": "bar", "char": "µ", "seed_range":5, "threshold":0.05, "hostile_prob":0.45, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#3b2f2f"},
	{ "name": "inn", "display_name": "Rook's Rest", "type": "inn", "char": "@", "seed_range":6, "threshold":0.07, "hostile_prob":0.03, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#5a4b42"},
	{ "name": "shopweapons", "display_name": "Scrap & Spike", "type": "shop", "char": "Æ", "seed_range":9, "threshold":0.18, "hostile_prob":0.07, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#6b2f2f"},
	{ "name": "shopitems", "display_name": "Oddments of the Rift", "type": "shop", "char": "₨", "seed_range":9, "threshold":0.34, "hostile_prob":0.05, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#4b3b3a"},
	{ "name": "shoparmor", "display_name": "Patch & Plate", "type": "shop", "char": "¥", "seed_range":9, "threshold":0.50, "hostile_prob":0.06, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#575757"},
	{ "name": "residencelarge", "display_name": "Garrison Halls", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.70, "hostile_prob":0.04, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#a8a8a8"},
	{ "name": "residencesmall", "display_name": "Rift Shacks", "type": "residence", "char": "î", "seed_range":4, "threshold":0.88, "hostile_prob":0.12, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#7b6b5b"},
	{ "name": "businesslarge", "display_name": "The Pit Exchange", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.95, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#4a4a4a"},
	{ "name": "businesssmall", "display_name": "Skewed Ledger", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.04, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#50433d"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "The Cliffbound Concord Lodge", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#4b0082" }, 
	{ "name": "other2", "display_name": "Riftwalker’s Ember Camp", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#4b0082" }
]

# Internal sublocations per subtype
#  Used when generating buildings to add searchable sublocations.
SUBLOC_MAP = {
 "shop": ["workbench", "crate pile", "gear shelf", "shelf unit", "file ledge", "vault niche"],
 "bar": ["stump bench", "backroom glade", "ember shelf", "whisper nook", "lock brazier", "notice peg"],
 "inn": ["common bunk", "guest bunk", "dresser", "drawer", "coat peg", "hearth nook"],
 "residence": ["kitchen", "bunkroom", "closet", "wash basin", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer"],
 "business": ["reception", "trade office", "bathroom", "file chest", "utility alcove", "storage chest", "vault niche"],
 "alley": ["ash pile", "broken cart", "hidden alcove", "vendor stall", "service hatch", "dumpster hollow", "alley crate", "scrawl wall"],
 "street": ["market stall", "fountain pool", "wagon post", "vendor stall", "display case", "back shelf", "message post", "mail hollow", "newsleaf"],
 "works": ["forge pit", "engine room", "vent shaft", "grate panel", "oil drum"],
 "arcane": ["ritual ring", "sigil cache", "enchanted chest", "altar niche", "masonry rune"],
}

# SubLocation metadata definitions used when building locations.
# Each entry provides defaults used by the generator and later logic (searchable, loot chance, prompt, etc.).
SUBLOCATION_DEFS = {
 "workbench": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A battered workbench with tools and half-made trinkets.", "money_range": (2,18)},
 "crate pile": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A pile of crates stamped with crude marks — one is unlatched.", "money_range": (1,16)},
 "gear shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A shelf of cogs and odd gears; a small coin nestles between them.", "money_range": (3,20)},
 "shelf unit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A crowded shelf unit; something is taped underneath.", "money_range": (0,8)},
 "file ledge": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A ledge of papers and manifests; a folded receipt peeks out.", "money_range": (1,20)},
 "vault niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A narrow niche sealed with bolts and soot.", "money_range": (10,60)},

 "stump bench": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A stump bench where locals stash small coins.", "money_range": (0,8)},
 "backroom glade": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A damp backroom where off-hours deals happen.", "money_range": (2,18)},
 "ember shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shelf warmed by embers with dusty bottles and notes.", "money_range": (1,12)},
 "whisper nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A cramped nook where whispers leave scraps of paper.", "money_range": (1,16)},
 "lock brazier": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "An iron brazier concealing a small locked compartment.", "money_range": (4,30)},
 "notice peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A peg with pinned notices; one envelope flutters loose.", "money_range": (0,10)},

 "common bunk": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shared bunkroom with pressed tags and tucked notes.", "money_range": (1,14)},
 "guest bunk": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A guest bunk with a loose floorboard hiding something small.", "money_range": (2,18)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A battered dresser with a stuck drawer — it rattles.", "money_range": (1,12)},
 "drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A shallow drawer with folded receipts and a photo.", "money_range": (1,10)},
 "coat peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A peg holding a grimy coat with a coin in the pocket.", "money_range": (0,8)},
 "hearth nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A nook by the hearth where charms and odd tools sit.", "money_range": (1,12)},

 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A cramped kitchen with jars and a hidden spice pouch.", "money_range": (1,10)},
 "bunkroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A crowded bunkroom where tags and trinkets accumulate.", "money_range": (1,12)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A narrow closet with oil-stained rags and a sealed note.", "money_range": (0,8)},
 "wash basin": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A basin where grime gathers; something clings beneath.", "money_range": (0,8)},
 "cupboard": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A cupboard of tins with a secret seam.", "money_range": (0,8)},
 "pantry": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A pantry of dried rations with a tucked sachet.", "money_range": (1,14)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "An old chest bound with straps; something clinks inside.", "money_range": (2,18)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A small iron lockbox bolted to a shelf — someone once trusted this.", "money_range": (2,18)},

 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A worn reception desk with ledger slips and stamped passes.", "money_range": (1,12)},
 "trade office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cramped office of ledgers and tally sticks.", "money_range": (2,18)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A chest of manifests and notes; a folded scrap peeks out.", "money_range": (2,22)},
 "utility alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "An alcove of tools and ropes; a loose key hides here.", "money_range": (0,10)},

 "ash pile": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A cooling ash pile where metal scraps and trinkets appear.", "money_range": (0,10)},
 "broken cart": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A splintered cart with a wrapped parcel inside.", "money_range": (1,16)},
 "hidden alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A tucked alcove between huts where contraband is stashed.", "money_range": (2,22)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A stall of battered wares and pickled goods; a coin falls loose.", "money_range": (2,18)},
 "service hatch": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A small hatch used for deliveries and secret drops.", "money_range": (0,8)},
 "dumpster hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A hollow under boards hiding odd finds.", "money_range": (0,12)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A crate abandoned in a narrow lane; straps are frayed.", "money_range": (1,14)},
 "scrawl wall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A wall scrawled with crude markings and gang sigils.", "money_range": (0,8)},

 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A bustling stall of salted meats, scrap parts, and odds.", "money_range": (4,28)},
 "fountain pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shallow pool fed by a rivulet; something glints beneath oil sheen.", "money_range": (6,40)},
 "wagon post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A post where wagons tie; straps hide a small pouch.", "money_range": (1,18)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A battered case of curios; one tag is loose.", "money_range": (2,20)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A shelf behind a counter where receipts and coins gather.", "money_range": (0,12)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A post of pinned scraps; one envelope flutters free.", "money_range": (0,8)},
 "mail hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A hollowed mail post with folded letters and a faded stamp.", "money_range": (0,10)},
 "newsleaf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A folded newsleaf with a scrawled ad tucked inside.", "money_range": (0,10)},

 "forge pit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A glowing forge pit where hot metal cools; tools litter the rim.", "money_range": (4,40)},
 "engine room": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A humming engine room with labelled cogs and oil-stained ledgers.", "money_range": (8,36)},
 "vent shaft": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A narrow shaft of warm air; something shiny is wedged in the grille.", "money_range": (2,20)},
 "grate panel": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A loose grate panel — reach in carefully.", "money_range": (1,18)},
 "oil drum": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A dented drum of oil; a small tin rattles inside.", "money_range": (0,12)},

 "ritual ring": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A ring of stones scarred with old offerings and faint ash.", "money_range": (4,40)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cache of engraved sigils humming with odd power.", "money_range": (8,36)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "An enchanted chest that resists prying fingers unless coaxed.", "money_range": (10,60)},
 "altar niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A carved niche with offerings and a tucked coin.", "money_range": (5,30)},
 "masonry rune": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A rune cut into bonded stone; the grooves hide a tiny token.", "money_range": (0,20)},
}