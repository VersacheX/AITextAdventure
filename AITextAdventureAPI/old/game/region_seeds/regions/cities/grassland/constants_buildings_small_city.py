CITY_NAME = "Quantford Hollow"
CITY_DESCRIPTION = (
	"A quiet village nestled within a sprawling grassland, Quantford Hollow is known for its thatched-roof cottages and tranquil ambiance. "
	"The town is surrounded by rolling hills and vibrant meadows, making it a picturesque retreat from the hustle and bustle of larger cities. "
	"Locals here are friendly and welcoming, often gathering at the central inn or the quaint marketplace to share stories and trade goods. "
	"Despite its peaceful appearance, the town has a rich history filled with tales of ancient magic and hidden treasures, attracting adventurers and wanderers alike."	
)

# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified
# heal_fraction <- fraction of max HP restored <- do not modify
ROOM_MENU = [
 {"id": "public", "name": "Stump Seat", "value":4, "heal_fraction":0.25},
 {"id": "economy", "name": "Loft Cot", "value":16, "heal_fraction":0.75},
 {"id": "luxury", "name": "Thatch Suite", "value":56, "heal_fraction":1.0},
]

# Simple in-bar drinks menu. Effects are immediate and don't create inventory items.
# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified slightly... bigger drinks are naturally more expensive as buying a drink triggers rng for an enemy, so buying small doesn't pay
# hp_fraction <- fraction of max HP restored immediately <- do not modify
DRINK_MENU = [
 {"id": "tiny", "name": "Meadow Ale", "value":6, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
 {"id": "small", "name": "Dusk Cider", "value":14, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
 {"id": "mid", "name": "Moonpetal Mix", "value":32, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
 {"id": "big", "name": "Thatch Elixir", "value":68, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
 {"id": "huge", "name": "Quant Draught", "value":140, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":5},
 {"id": "max", "name": "Hollow Serum", "value":220, "hp_fraction":1.00, "ap_fraction":0.20, "min_level":6},
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
	{ "name": "bar", "display_name": "The Hollow Lantern", "type": "bar", "char": "µ", "seed_range":5, "threshold":0.02, "hostile_prob":0.20, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#4b3b2f"},
	{ "name": "inn", "display_name": "The Roofed Loft", "type": "inn", "char": "@", "seed_range":7, "threshold":0.04, "hostile_prob":0.00, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#6b6b5a"},
	{ "name": "shopweapons", "display_name": "Thorn & Peg", "type": "shop", "char": "Æ", "seed_range":6, "threshold":0.12, "hostile_prob":0.03, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#5a2f2f"},
	{ "name": "shopitems", "display_name": "Quant Curios", "type": "shop", "char": "₨", "seed_range":6, "threshold":0.28, "hostile_prob":0.02, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#3b5b4a"},
	{ "name": "shoparmor", "display_name": "Hide & Patch", "type": "shop", "char": "¥", "seed_range":6, "threshold":0.44, "hostile_prob":0.02, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#6b6b5b"},
	{ "name": "residencelarge", "display_name": "Hollowstead", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.60, "hostile_prob":0.01, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#dfe7c8"},
	{ "name": "residencesmall", "display_name": "Thatched Rows", "type": "residence", "char": "î", "seed_range":4, "threshold":0.85, "hostile_prob":0.06, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#efe7c8"},
	{ "name": "businesslarge", "display_name": "Guild Bower", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.88, "hostile_prob":0.01, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#c0c0c0"},
	{ "name": "businesssmall", "display_name": "Ledger Nook", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#c0b88f"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "Hollowfield Heritage", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#4b0082" }, 
	{ "name": "other2", "display_name": "Meadowlight Reading Room", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#4b0082" }
]

# Internal sublocations per subtype
# Used when generating buildings to add searchable sublocations.
SUBLOC_MAP = {
 "shop": ["back alcove", "crate nook", "display case", "shelf unit", "file ledge", "vault nook"],
 "bar": ["stump bench", "back nook", "ember shelf", "cloak peg", "lock brazier", "whisper nook"],
 "inn": ["common nook", "guest loft", "dresser", "drawer", "coat peg", "hearth shelf"],
 "residence": ["kitchen", "bedroom", "closet", "bath nook", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer"],
 "business": ["reception", "office", "wash nook", "file ledge", "utility niche", "storage chest", "vault nook"],
 "alley": ["moss pile", "abandoned wheel", "hidden alcove", "vendor stall", "service root", "alley crate", "sigil post"],
 "street": ["market stall", "fountain pool", "wagon post", "vendor stall", "display case", "back shelf", "message post", "mail hollow", "newsleaf"],
 "arcane": ["ritual ring", "sigil cache", "enchanted chest", "altar niche", "wind sigil"],
}

# SubLocation metadata definitions used when building locations.
# Each entry provides defaults used by the generator and later logic (searchable, loot chance, prompt, etc.).
SUBLOCATION_DEFS = {
 "back alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A cramped back alcove full of jars and wrapped trinkets.", "money_range": (2,16)},
 "crate nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A small nook of stamped crates and loose rope.", "money_range": (1,12)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A glass display case of curious oddments; one tag is loose.", "money_range": (2,14)},
 "shelf unit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A cluttered shelf unit where someone hid a small parcel.", "money_range": (0,8)},
 "file ledge": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A ledge of receipts and notes; something peeks from between pages.", "money_range": (1,18)},
 "vault nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A tiny vault nook sealed behind rough wood.", "money_range": (8,48)},

 "stump bench": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A stump used for seating; coins and notes hide in knots.", "money_range": (0,8)},
 "back nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A tucked back nook where locals whisper and leave slips.", "money_range": (1,12)},
 "ember shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shelf warmed by embers with a few dusty bottles.", "money_range": (1,10)},
 "cloak peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A peg with a weathered cloak; something bulked in a pocket.", "money_range": (0,8)},
 "lock brazier": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "An iron brazier concealing a small locked compartment.", "money_range": (3,20)},
 "whisper nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A narrow nook where hushed deals and notes are left.", "money_range": (1,12)},

 "common nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A common nook with low seats and dim lanterns.", "money_range": (1,12)},
 "guest loft": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A small guest loft with tucked pockets and a loose board.", "money_range": (1,14)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A battered dresser with one drawer that sticks; something rattles inside.", "money_range": (1,12)},
 "drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "A shallow drawer with folded receipts and a faded photograph.", "money_range": (1,10)},
 "coat peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A peg with a coat whose pockets might hide small change.", "money_range": (0,8)},
 "hearth shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A shelf above the hearth where herbs and charms are stored.", "money_range": (1,10)},

 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A modest kitchen with jars and a tucked spice pouch.", "money_range": (1,8)},
 "bedroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A tight bedroom with a woven bed and a coin beneath the mat.", "money_range": (1,10)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A narrow closet of linens; a sealed envelope hides inside.", "money_range": (0,8)},
 "bath nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A small bath nook with scented oils and a stuck charm.", "money_range": (0,8)},
 "cupboard": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A grease-stained cupboard with mismatched plates and a secret stain.", "money_range": (0,8)},
 "pantry": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A pantry of dried jars and a hidden sachet of herbs.", "money_range": (1,12)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "An old chest tied with straps; something metallic rattles inside.", "money_range": (2,18)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A small iron lockbox bolted to a shelf — someone once trusted this.", "money_range": (2,18)},

 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A humble reception with ledger slips and a stub of wax.", "money_range": (1,8)},
 "office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cramped office with petitions and a locked drawer.", "money_range": (1,12)},
 "utility niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A small niche of tools and rope; an invoice peeks from beneath.", "money_range": (0,8)},

 "moss pile": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A damp moss pile with scraps and a rusty coin.", "money_range": (0,6)},
 "abandoned wheel": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "An old wheel half-buried in grass; a wrapped parcel nests within.", "money_range": (1,10)},
 "hidden alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A narrow alcove where someone stashed a folded note.", "money_range": (1,12)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A vendor stall of woven baskets and preserves; a coin falls free.", "money_range": (1,14)},
 "service root": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A root-formed service hatch with an iron catch.", "money_range": (0,8)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A weathered crate in the lane — straps are loose.", "money_range": (1,12)},
 "sigil post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A carved post with faded sigils; one chip comes away.", "money_range": (0,8)},

 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A small market stall piled with preserves and trinkets.", "money_range": (2,18)},
 "fountain pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shallow fountain pool fed by a spring; something glints below.", "money_range": (4,20)},
 "wagon post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A post used to tie wagons; straps hide a small pouch.", "money_range": (1,12)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A small display case with a crooked tag.", "money_range": (1,12)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A back shelf where notes and small coins gather dust.", "money_range": (0,8)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.07, "prompt": "A post of pinned notes; one envelope flutters lose.", "money_range": (0,8)},
 "mail hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A hollowed mail post with folded letters and a faded stamp.", "money_range": (0,10)},
 "newsleaf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A folded newsleaf; tucked inside is a tiny ad.", "money_range": (0,10)},

 "ritual ring": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A small ring of stones with traces of old offerings.", "money_range": (2,30)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cache of small engraved sigils humming faintly.", "money_range": (6,32)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "An enchanted chest resistant to prying fingers; something glows within.", "money_range": (8,48)},
 "altar niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A carved niche with small offerings and a tucked coin.", "money_range": (4,20)},
 "wind sigil": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "A sigil carved on a standing stone; the lines hide a token.", "money_range": (0,12)},
}