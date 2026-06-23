CITY_NAME = "Thornshade Hamlet"
CITY_DESCRIPTION = (
	"A small hamlet nestled within a dense forest, Thornshade Hamlet is known for its towering trees and "
	"the soft glow of bioluminescent flora that lights its winding paths. The village is a haven for travelers "
	"seeking respite from the wilds, offering cozy inns and a lively tavern where stories are shared over hearty meals. "
	"Locals are friendly and knowledgeable about the surrounding woods, often guiding adventurers to hidden groves "
	"and ancient ruins. The air is filled with the scent of pine and earth, and the gentle rustling of leaves creates "
	"a soothing backdrop to life in this tranquil settlement."
)

# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified
# heal_fraction <- fraction of max HP restored <- do not modify
ROOM_MENU = [
 {"id": "public", "name": "Stump Bench", "value":4, "heal_fraction":0.25},
 {"id": "economy", "name": "Loft Cot", "value":18, "heal_fraction":0.75},
 {"id": "luxury", "name": "Moonlit Suite", "value":60, "heal_fraction":1.0},
]

# Simple in-bar drinks menu. Effects are immediate and don't create inventory items.
# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified slightly... bigger drinks are naturally more expensive as buying a drink triggers rng for an enemy, so buying small doesn't pay
# hp_fraction <- fraction of max HP restored immediately <- do not modify
DRINK_MENU = [
 {"id": "tiny", "name": "Bark Ale", "value":6, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
 {"id": "small", "name": "Dusk Mead", "value":14, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
 {"id": "mid", "name": "Moonpetal Mix", "value":30, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
 {"id": "big", "name": "Shade Elixir", "value":65, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
 {"id": "huge", "name": "Willow Draught", "value":130, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":5},
 {"id": "max", "name": "Thorn Serum", "value":200, "hp_fraction":1.00, "ap_fraction":0.20, "min_level":6},
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
	{ "name": "bar", "display_name": "The Moss & Lantern", "type": "bar", "char": "µ", "seed_range":5, "threshold":0.02, "hostile_prob":0.25, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#27412f"},
	{ "name": "inn", "display_name": "Hearthfall Inn", "type": "inn", "char": "@", "seed_range":7, "threshold":0.04, "hostile_prob":0.00, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#3b5a4a"},
	{ "name": "shopweapons", "display_name": "Thorn & Thread", "type": "shop", "char": "Æ", "seed_range":9, "threshold":0.12, "hostile_prob":0.03, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#5a2f2f"},
	{ "name": "shopitems", "display_name": "Curio Hollow", "type": "shop", "char": "₨", "seed_range":9, "threshold":0.28, "hostile_prob":0.02, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#35524a"},
	{ "name": "shoparmor", "display_name": "Barkshield Crafts", "type": "shop", "char": "¥", "seed_range":9, "threshold":0.44, "hostile_prob":0.02, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#6b6b5b"},
	{ "name": "residencelarge", "display_name": "Elmhold", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.60, "hostile_prob":0.01, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#2e4b3a"},
	{ "name": "residencesmall", "display_name": "Thatch Cottages", "type": "residence", "char": "î", "seed_range":4, "threshold":0.85, "hostile_prob":0.08, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#3b5a3a"},
	{ "name": "businesslarge", "display_name": "Guild Bower", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.90, "hostile_prob":0.01, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#2a3a2a"},
	{ "name": "businesssmall", "display_name": "Ledger & Lantern", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#274b3a"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "Grovekeeper’s Archive", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#4b0082" }, 
	{ "name": "other2", "display_name": "Hollowshade Listening Post", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#4b0082" }
]

# Internal sublocations per subtype
# Used when generating buildings to add searchable sublocations.
SUBLOC_MAP = {
 "shop": ["back alcove", "storage", "arcane rack", "shelf unit", "lockbox", "display case"],
 "bar": ["moss bench", "back nook", "ember shelf", "whisper nook", "bottle rack", "lock brazier"],
 "inn": ["common nook", "guest loft", "dresser", "drawer", "coat peg", "hearth shelf"],
 "residence": ["kitchen", "bedroom", "closet", "bath nook", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer"],
 "business": ["reception", "office", "bath nook", "file ledge", "utility hollow", "storage chest", "vault niche"],
 "alley": ["moss pile", "fallen limb", "hidden alcove", "vendor stall", "service root", "alley crate", "graffiti lichen"],
 "street": ["market stall", "fountain pool", "display case", "back shelf", "message post", "mail hollow", "newsleaf"],
 "arcane": ["ritual ring", "sigil cache", "enchanted chest", "sylvan rune"],
}

# SubLocation metadata definitions used when building locations.
# Each entry provides defaults used by the generator and later logic (searchable, loot chance, prompt, etc.).
SUBLOCATION_DEFS = {
 "back alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A cramped back alcove cluttered with odd jars and ledger slips.", "money_range": (2,18)},
 "storage": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A low storage room with stacked crates and wrapped parcels.", "money_range": (1,12)},
 "arcane rack": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A rack of arcane trinkets, some humming faintly.", "money_range": (6,28)},
 "shelf unit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A shelf unit of mismatched goods; one box is unlabelled.", "money_range": (0,8)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A small iron lockbox bolted beneath a counter; it muffles something heavy.", "money_range": (3,30)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A glass display case housing small trinkets; one looks loose.", "money_range": (2,16)},

 "moss bench": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A mossy bench often used by locals; coins and notes hide in crevices.", "money_range": (0,8)},
 "back nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A tucked away nook behind the bar where secrets are traded.", "money_range": (1,14)},
 "ember shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shelf warmed by a small embers; bottles and notes rest here.", "money_range": (1,12)},
 "whisper nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A narrow whisper nook where hushed voices leave behind receipts.", "money_range": (1,10)},
 "bottle rack": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A rack of bottles, some labeled in a script you half-remember.", "money_range": (2,12)},
 "lock brazier": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A small brazier with a hidden compartment beneath the coals.", "money_range": (4,20)},

 "common nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A common nook with low stools and dim lanterns.", "money_range": (2,12)},
 "guest loft": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A tight guest loft with tucked pockets and a loose floorboard.", "money_range": (1,14)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A battered dresser with one drawer sticking; something rattles inside.", "money_range": (1,12)},
 "drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "A shallow drawer with pressed receipts and a folded photograph.", "money_range": (1,10)},
 "coat peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A peg with a coat whose pockets hide jingling coins.", "money_range": (0,8)},
 "hearth shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shelf above the hearth where herbs and small charms are kept.", "money_range": (1,10)},

 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A tidy kitchen with jars, knives, and a hidden spice pouch.", "money_range": (1,8)},
 "bedroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A small bedroom with a woven bed and a coin tucked under the mat.", "money_range": (1,12)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A narrow closet full of cloaks and a sealed envelope.", "money_range": (0,8)},
 "bath nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shallow bath nook with scented oils and a rusted trinket.", "money_range": (0,8)},
 "cupboard": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A grease-stained cupboard with mismatched plates and a secret stain.", "money_range": (0,8)},
 "pantry": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A small pantry with jars and a hidden sachet of dried herbs.", "money_range": (1,14)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "An old storage chest sealed with straps; something clinks within.", "money_range": (2,20)},

 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A humble reception with a ledger and a stub of wax.", "money_range": (1,8)},
 "office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A small office cluttered with notes and a locked drawer.", "money_range": (1,12)},
 "file ledge": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A ledge of files and scraps; one envelope bulges.", "money_range": (1,18)},
 "utility hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A hollow filled with brooms, ropes, and an old invoice.", "money_range": (0,8)},
 "vault niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A small vault niche carved into living wood; it hums when touched.", "money_range": (10,40)},

 "moss pile": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A damp pile of moss hiding scraps and a bottle cap.", "money_range": (0,6)},
 "fallen limb": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A fallen limb with a hollow pocket concealing a small bundle.", "money_range": (1,10)},
 "hidden alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A tight hidden alcove where someone stashed a folded note.", "money_range": (1,12)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A small vendor stall with woven trays and a rattling coin.", "money_range": (1,14)},
 "service root": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A service root with an iron catch and a stuck compartment.", "money_range": (0,8)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A weathered crate in a narrow alley — straps are loose.", "money_range": (1,12)},
 "graffiti lichen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A patch of lichen carved with odd marks; one chip comes away.", "money_range": (0,8)},

 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A market stall piled with jars and trinkets; a coin slides loose.", "money_range": (2,16)},
 "fountain pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A still pool at the village center; something glints beneath the surface.", "money_range": (4,20)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A small display case of curios; one tag is missing.", "money_range": (1,12)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A back shelf behind a stall where receipts and small coins accumulate.", "money_range": (0,8)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A post with pinned notes; one envelope flutters loose.", "money_range": (0,8)},
 "mail hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A hollowed mail post with folded letters and a faded stamp.", "money_range": (0,10)},
 "newsleaf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A stack of newsleafs; tucked inside is a small ad.", "money_range": (0,10)},

 "ritual ring": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A ring of stones scarred with old offerings and faint ash.", "money_range": (2,30)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cache of small engraved sigils humming softly.", "money_range": (6,32)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "An enchanted chest resistant to prying fingers; it whispers when approached.", "money_range": (8,48)},
 "sylvan rune": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "A rune carved into bark; the groove hides a tiny token.", "money_range": (0,12)},
}