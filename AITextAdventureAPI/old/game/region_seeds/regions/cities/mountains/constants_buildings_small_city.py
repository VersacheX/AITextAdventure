CITY_NAME = "Hollerforge Hollow"
CITY_DESCRIPTION = (
	"A rugged mining town nestled within a vast mountain hollow, Hollerforge Hollow is a hub of industry and resilience."
	"The town is characterized by its sturdy timber buildings, winding cobblestone streets, and the ever-present hum of mining activity."
	"Towering cliffs encircle the settlement, their faces scarred by centuries of excavation."
	"The air is thick with the scent of pine and earth, mingling with the smoke from forge fires and the distant clang of pickaxes."
	"Despite the harsh environment, the townsfolk are known for their hearty spirit and tight-knit community, often gathering at the local tavern to share stories and celebrate their hard-won successes."
)

# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified
# heal_fraction <- fraction of max HP restored <- do not modify
ROOM_MENU = [
 {"id": "public", "name": "Log Bench", "value":4, "heal_fraction":0.25},
 {"id": "economy", "name": "Loft Cot", "value":15, "heal_fraction":0.75},
 {"id": "luxury", "name": "Miner's Suite", "value":55, "heal_fraction":1.0},
]

# Simple in-bar drinks menu. Effects are immediate and don't create inventory items.
# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency  <- can be modified slightly... bigger drinks are naturally more expensive as buying a drink triggers rng for an enemy, so buying small doesn't pay
# hp_fraction <- fraction of max HP restored immediately <- do not modify
DRINK_MENU = [
 {"id": "tiny", "name": "Straw Ale", "value":6, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
 {"id": "small", "name": "Holler Cider", "value":13, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
 {"id": "mid", "name": "Moonshine Mix", "value":28, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
 {"id": "big", "name": "Rivet Rum", "value":62, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
 {"id": "huge", "name": "Forge Draught", "value":130, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":5},
 {"id": "max", "name": "Hollow Serum", "value":210, "hp_fraction":1.00, "ap_fraction":0.20, "min_level":6},
]

# Buildings
BUILDINGS = [
	{ "name": "bar", "display_name": "The Still & Spindle", "type": "bar", "char": "µ", "seed_range":5, "threshold":0.02, "hostile_prob":0.22, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#7b645b"},
	{ "name": "inn", "display_name": "Holler's Rest", "type": "inn", "char": "@", "seed_range":7, "threshold":0.04, "hostile_prob":0.01, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#6b5a4a"},
	{ "name": "shopweapons", "display_name": "Spike & Splint", "type": "shop", "char": "Æ", "seed_range":6, "threshold":0.12, "hostile_prob":0.03, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#5a2b2b"},
	{ "name": "shopitems", "display_name": "Hollow Oddments", "type": "shop", "char": "₨", "seed_range":6, "threshold":0.28, "hostile_prob":0.02, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#6b7b6b"},
	{ "name": "shoparmor", "display_name": "Patch & Plate", "type": "shop", "char": "¥", "seed_range":6, "threshold":0.44, "hostile_prob":0.02, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#6b6b5b"},
	{ "name": "residencelarge", "display_name": "Hearthstead", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.60, "hostile_prob":0.01, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#dfe1d8"},
	{ "name": "residencesmall", "display_name": "Thatched Hollows", "type": "residence", "char": "î", "seed_range":4, "threshold":0.85, "hostile_prob":0.06, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#efe7d8"},
	{ "name": "businesslarge", "display_name": "Timberwright Guild", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.88, "hostile_prob":0.01, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#b4b0a8"},
	{ "name": "businesssmall", "display_name": "Ledger Nook", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#c0b88f"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "Forgehand Fellowship", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#7b30a2" }, 
	{ "name": "other2", "display_name": "The Deepdelve Muster Hall", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#7b30a2" }
]

# Internal sublocations per subtype
#  Used when generating buildings to add searchable sublocations.
SUBLOC_MAP = {
 "shop": ["back shack", "crate nook", "display case", "shelf unit", "file box", "vault nook"],
 "bar": ["stump bench", "tap shelf", "moonshine jar", "whisper nook", "lockbox", "notice peg"],
 "inn": ["common loft", "guest room", "dresser", "drawer", "coat peg", "hearth shelf"],
 "residence": ["kitchen", "bedroom", "closet", "bath nook", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer"],
 "business": ["reception", "office", "wash nook", "file box", "utility nook", "storage chest", "vault nook"],
 "alley": ["brush pile", "broken cart", "hidden alcove", "vendor stall", "service root", "dumpster hollow", "alley crate", "scrawl post"],
 "street": ["market stall", "fountain pool", "wagon post", "vendor stall", "display case", "back shelf", "message post", "mail hollow", "newsleaf"],
 "arcane": ["ritual ring", "sigil cache", "enchanted chest", "altar niche", "wind sigil"],
}

# SubLocation metadata definitions used when building locations.
# Each entry provides defaults used by the generator and later logic (searchable, loot chance, prompt, etc.).
SUBLOCATION_DEFS = {
 "back shack": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A cramped back shack full of jars, rope, and wrapped odds.", "money_range": (1,14)},
 "crate nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A nook of stamped crates; one lid is loose.", "money_range": (1,12)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A glass case holding local oddments; one tag is missing.", "money_range": (2,14)},
 "shelf unit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shelf unit crowded with tins and wrapped parcels.", "money_range": (0,8)},
 "file box": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A battered file box with receipts and a folded note.", "money_range": (1,16)},
 "vault nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A small vault nook hidden behind rough timber.", "money_range": (8,48)},

 "stump bench": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A carved stump used for seating; coins hide in the knots.", "money_range": (0,8)},
 "tap shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shelf behind the taps where tips and notes gather.", "money_range": (1,10)},
 "moonshine jar": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A jar of homemade shine; a small pouch is taped to the underside.", "money_range": (2,18)},
 "whisper nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A cramped nook where locals swap scraps and slivers of gossip.", "money_range": (1,12)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A small iron lockbox bolted to a shelf — heavy inside.", "money_range": (2,18)},
 "notice peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A peg with pinned notices; an envelope flutters loose.", "money_range": (0,10)},

 "common loft": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shared loft with low beds and tucked pockets.", "money_range": (1,12)},
 "guest room": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A humble guest room with a loose board hiding something small.", "money_range": (1,14)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A battered dresser with a drawer that squeaks and resists.", "money_range": (1,12)},
 "drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "A shallow drawer with folded receipts and a faded photo.", "money_range": (1,10)},
 "coat peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A peg with a rough coat; the pocket bulges slightly.", "money_range": (0,8)},
 "hearth shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A shelf above the hearth where tins and charms are kept.", "money_range": (1,10)},

 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A humble kitchen with jars and a hidden spice pouch.", "money_range": (1,8)},
 "bedroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A tight bedroom with a woven bed and a coin tucked beneath.", "money_range": (1,10)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A narrow closet of linens; a sealed envelope is tucked inside.", "money_range": (0,8)},
 "bath nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A small bath nook with oils and a stuck charm.", "money_range": (0,8)},
 "cupboard": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A grease-stained cupboard with mismatched plates and a secret stain.", "money_range": (0,8)},
 "pantry": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A pantry of dried jars and a hidden sachet of herbs.", "money_range": (1,12)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "An old chest tied with straps; a metal clink echoes within.", "money_range": (2,18)},

 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A humble reception with ledger slips and a stub of wax.", "money_range": (1,8)},
 "office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cramped office with tally sticks and a locked drawer.", "money_range": (1,12)},
 "wash nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A small wash nook with cracked basin and a copper token.", "money_range": (0,8)},
 "utility nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A nook of tools and rope; an invoice peeks from the corner.", "money_range": (0,8)},

 "brush pile": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A pile of brambles and brush; something metallic glints within.", "money_range": (0,8)},
 "broken cart": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A splintered cart with a wrapped parcel tucked inside.", "money_range": (1,12)},
 "hidden alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A narrow alcove where someone stashed a folded note.", "money_range": (1,12)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A stall with preserves and woven baskets; a coin slides loose.", "money_range": (1,14)},
 "service root": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A root-formed service hatch with an iron catch.", "money_range": (0,8)},
 "dumpster hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A hollow under boards where odd finds appear.", "money_range": (0,10)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A weathered crate in the lane — straps fray at the seam.", "money_range": (1,12)},
 "scrawl post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A post scrawled with names and crude marks; a chip peels free.", "money_range": (0,8)},

 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A small market stall of preserves, rope, and trinkets.", "money_range": (2,18)},
 "fountain pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shallow fountain fed by a spring; something glints below.", "money_range": (4,20)},
 "wagon post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A post where wagons tie; straps hide a small pouch.", "money_range": (1,12)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A small case of curios; one tag hangs loose.", "money_range": (1,12)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A back shelf where notes and small coins gather dust.", "money_range": (0,8)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.07, "prompt": "A post of pinned notes; one envelope flutters lose.", "money_range": (0,8)},
 "mail hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A hollowed mail post with folded letters and a faded stamp.", "money_range": (0,10)},
 "newsleaf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A folded newsleaf with a tiny ad tucked inside.", "money_range": (0,10)},

 "ritual ring": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A ring of stones with traces of old offerings.", "money_range": (2,30)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cache of small sigils humming faintly.", "money_range": (6,32)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "An enchanted chest resistant to prying fingers.", "money_range": (8,48)},
 "altar niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A carved niche with small offerings and a tucked coin.", "money_range": (4,20)},
 "wind sigil": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "A sigil carved on a standing stone; the lines hide a token.", "money_range": (0,12)},
}