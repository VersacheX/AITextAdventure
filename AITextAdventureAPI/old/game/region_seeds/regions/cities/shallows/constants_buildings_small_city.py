CITY_NAME = "Tidekin Cove"
CITY_DESCRIPTION = (
	"Tidekin Cove is a bustling harbor town nestled along the jagged coastline, known for its vibrant markets and salty air. "
	"The town is a maze of narrow alleys, weathered docks, and lively taverns, where merchants from distant lands trade exotic goods. "
	"Fishermen haul in their daily catch, while sailors share tales of the sea over mugs of brine ale. "
	"Colorful banners flutter in the sea breeze, and the scent of saltwater mingles with the aroma of fresh seafood. "
	"Despite its lively atmosphere, Tidekin Cove has an undercurrent of mystery, with hidden coves and secret passages rumored to be used by smugglers and adventurers alike. "
	"Visitors to the town are captivated by its unique blend of maritime culture and vibrant community spirit."
)

# Room Menu
ROOM_MENU = [
 {"id": "public", "name": "Quay Step", "value":5, "heal_fraction":0.25},
 {"id": "economy", "name": "Berth Loft", "value":18, "heal_fraction":0.75},
 {"id": "luxury", "name": "Keeper's Suite", "value":72, "heal_fraction":1.0},
]

# Drinks Menu
DRINK_MENU = [
 {"id": "tiny", "name": "Brine Ale", "value":7, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
 {"id": "small", "name": "Saltwine", "value":15, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
 {"id": "mid", "name": "Moonkelp Mix", "value":34, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
 {"id": "big", "name": "Dredger's Tonic", "value":70, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
 {"id": "huge", "name": "Abyssal Draught", "value":150, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":6},
 {"id": "max", "name": "Tideheart Serum", "value":280, "hp_fraction":1.00, "ap_fraction":0.30, "min_level":9},
]

# Buildings
BUILDINGS = [
	{ "name": "bar", "display_name": "The Salted Shell", "type": "bar", "char": "µ", "seed_range":5, "threshold":0.03, "hostile_prob":0.25, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#5f8b8b"},
	{ "name": "inn", "display_name": "Harbormoss Inn", "type": "inn", "char": "@", "seed_range":7, "threshold":0.05, "hostile_prob":0.00, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#4b6b6b"},
	{ "name": "shopweapons", "display_name": "Hook & Tine", "type": "shop", "char": "Æ", "seed_range":9, "threshold":0.14, "hostile_prob":0.03, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#8b6b5f"},
	{ "name": "shopitems", "display_name": "Drift Oddments", "type": "shop", "char": "₨", "seed_range":9, "threshold":0.30, "hostile_prob":0.02, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#2f6b5b"},
	{ "name": "shoparmor", "display_name": "Scale & Patch", "type": "shop", "char": "¥", "seed_range":9, "threshold":0.46, "hostile_prob":0.02, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#6b6b5b"},
	{ "name": "residencelarge", "display_name": "Quayside Hall", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.65, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#c8e7e0"},
	{ "name": "residencesmall", "display_name": "Tide Rows", "type": "residence", "char": "î", "seed_range":4, "threshold":0.88, "hostile_prob":0.08, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#dfe7df"},
	{ "name": "businesslarge", "display_name": "Cove Exchange", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.92, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#5b7b7b"},
	{ "name": "businesssmall", "display_name": "Ledger Wharf", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#6b6b5b"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "The Brinewharf Signal Post", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#7b30a2" }, 
	{ "name": "other2", "display_name": "Cove‑Runner’s Hideaway", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#7b30a2" }
]

# Sublocation mapping
SUBLOC_MAP = {
 "shop": ["stern nook", "crate hold", "display case", "shelf unit", "file chest", "vault nook"],
 "bar": ["tap shelf", "bilge nook", "ember shelf", "whisper alcove", "lock brazier", "notice peg"],
 "inn": ["common loft", "guest berth", "dresser", "drawer", "coat peg", "hearth shelf"],
 "residence": ["kitchen", "bedroom", "closet", "bath nook", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer"],
 "business": ["reception", "office", "bathroom", "file chest", "utility hold", "storage chest", "vault nook"],
 "alley": ["fish heap", "beached skiff", "hidden culvert", "vendor stall", "service grate", "dumpster hollow", "alley crate", "barnacle wall"],
 "street": ["market stall", "tide pool", "skiff post", "vendor stall", "display case", "back shelf", "message post", "mail hollow", "newsstand"],
 "docks": ["pier side", "rope coil", "cargo hold", "crane gear"],
 "arcane": ["ritual ring", "sigil cache", "enchanted chest", "altar niche", "tide rune"],
}

# SubLocation metadata definitions
SUBLOCATION_DEFS = {
 "stern nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A tight stern nook lined with nets, jars and salted tags.", "money_range": (2,18)},
 "crate hold": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A small hold of salted crates and sealed barrels; one sloshes when moved.", "money_range": (1,20)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A glass case of tide-polished trinkets and shells.", "money_range": (2,18)},
 "shelf unit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A crowded shelf unit of jars and labelled bottles.", "money_range": (0,8)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A chest of manifests and notes; a folded receipt peeks out.", "money_range": (1,20)},
 "vault nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A tiny vault nook sealed behind tideboard and iron.", "money_range": (8,60)},

 "tap shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shelf behind the taps where tips and notes collect in salt.", "money_range": (1,10)},
 "bilge nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A low bilge nook smelling of oil and brine; something glints.", "money_range": (1,12)},
 "ember shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A warm shelf holding bottles and smudged notes.", "money_range": (1,8)},
 "whisper alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A narrow alcove where whispers and IOUs are left.", "money_range": (1,14)},
 "lock brazier": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "An iron brazier concealing a small locked compartment.", "money_range": (3,24)},
 "notice peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.07, "prompt": "A peg with pinned notices; an envelope flutters loose.", "money_range": (0,8)},

 "common loft": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shared loft with low beds and tucked pockets.", "money_range": (1,12)},
 "guest berth": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A small guest berth with a loose plank hiding a scrap.", "money_range": (1,14)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A battered dresser with a stuck drawer; something rattles inside.", "money_range": (1,12)},
 "drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A shallow drawer with damp receipts and a faded photograph.", "money_range": (1,10)},
 "coat peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A peg with a salt-stiff coat; the pocket holds a scrap.", "money_range": (0,8)},
 "hearth shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A shelf above the hearth where jars and charms are kept.", "money_range": (1,10)},

 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A fish-scented kitchen with jars and a hidden sachet.", "money_range": (1,10)},
 "bedroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A tight bedroom with a woven berth and a coin tucked beneath.", "money_range": (1,10)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A narrow closet of oilskin and sea-stiff garments.", "money_range": (0,8)},
 "bath nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A shallow bath nook with brine and a stuck charm.", "money_range": (0,8)},
 "cupboard": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A sea-stained cupboard with tins and a hidden seam.", "money_range": (0,8)},
 "pantry": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A pantry of salted provisions with a hidden packet.", "money_range": (1,12)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "An old chest lashed with rope; something clinks within.", "money_range": (2,16)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A small iron lockbox bolted to a beam — heavy inside.", "money_range": (2,16)},

 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A weathered reception desk with manifest slips and a stub of wax.", "money_range": (1,10)},
 "office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cramped office of ledgers and salted receipts.", "money_range": (1,14)},
 "utility hold": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A damp hold with coils and a bent key.", "money_range": (0,10)},

 "fish heap": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A stinking heap of fish guts and discarded tackle; something glints.", "money_range": (0,8)},
 "beached skiff": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A small skiff left on the mudflats with a wrapped bundle tucked beneath.", "money_range": (1,12)},
 "hidden culvert": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A narrow culvert where contraband and notes are stashed.", "money_range": (1,18)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A stall of salted goods and tide-polished curios; a coin slips free.", "money_range": (1,16)},
 "service grate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A grated service slot used for deliveries and whispers.", "money_range": (0,8)},
 "dumpster hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A hollow under planks where refuse and odd finds mingle.", "money_range": (0,10)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A crate washed up in a lane; straps are salt-brittle.", "money_range": (1,12)},
 "barnacle wall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A wall encrusted with barnacles; one chip reveals something small.", "money_range": (0,8)},

 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A small market stall of pickled fish, ropes, and trinkets.", "money_range": (2,18)},
 "tide pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shallow tidal pool where shells and coins collect.", "money_range": (2,14)},
 "skiff post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A post where skiffs tie; a strap conceals a pouch.", "money_range": (1,12)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A small case of brine-polished curios; a tag is loose.", "money_range": (1,12)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A back shelf where notes and small coins collect in salt.", "money_range": (0,8)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.07, "prompt": "A post of pinned notes; one envelope flutters loose.", "money_range": (0,8)},
 "mail hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A hollowed mail post with damp letters and a salted stamp.", "money_range": (0,10)},
 "newsstand": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A weathered newsstand with broadsheets and tide-notices.", "money_range": (0,12)},

 "ritual ring": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A ring of stones worn smooth by offerings of shell and bone.", "money_range": (2,30)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cache of engraved sigils humming with briny power.", "money_range": (6,28)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "An enchanted chest resistant to prying fingers.", "money_range": (8,48)},
 "altar niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A carved niche with shells and a tucked coin.", "money_range": (3,18)},
 "tide rune": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "A rune carved into kelp-stiff rock; its grooves hide a token.", "money_range": (0,12)},
}