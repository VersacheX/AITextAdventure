CITY_NAME = "Nightveil Spire"
CITY_DESCRIPTION = (
	"Nightveil Spire is a sprawling metropolis shrouded in perpetual twilight, where towering obsidian skyscrapers pierce the darkened sky. "
	"The city is a labyrinth of narrow alleys and bustling marketplaces, illuminated by the eerie glow of bioluminescent flora and arcane streetlights. "
	"Citizens of Nightveil Spire are a mix of shadowy figures and enigmatic beings, all drawn to the city's promise of power and mystery. "
	"Amidst the urban sprawl, ancient ruins and arcane relics hint at a forgotten past, while modern technology and magic intertwine to create a unique blend of old and new. "
	"Nightveil Spire is a city of contrasts, where danger lurks in the shadows and opportunity shines in the darkest corners."
)

# Room Menu
# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified
# heal_fraction <- fraction of max HP restored <- do not modify
ROOM_MENU = [
 {"id": "public", "name": "Alley Bench", "value":6, "heal_fraction":0.25},
 {"id": "economy", "name": "Rented Cot", "value":28, "heal_fraction":0.75},
 {"id": "luxury", "name": "Shadow Suite", "value":95, "heal_fraction":1.0},
]

# Drinks Menu
# Simple in-bar drinks menu. Effects are immediate and don't create inventory items.
# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified slightly... bigger drinks are naturally more expensive as buying a drink triggers rng for an enemy, so buying small doesn't pay
# hp_fraction <- fraction of max HP restored immediately <- do not modify
DRINK_MENU = [
 {"id": "tiny", "name": "Ash Ale", "value":10, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
 {"id": "small", "name": "Inkbrew", "value":20, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
 {"id": "mid", "name": "Moonlight Cocktail", "value":40, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
 {"id": "big", "name": "Phantom Elixir", "value":85, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
 {"id": "huge", "name": "Shade Draught", "value":170, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":4},
 {"id": "max", "name": "Nocturne Serum", "value":220, "hp_fraction":1.00, "ap_fraction":0.25, "min_level":5},
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
	{ "name": "bar", "display_name": "The Velvet Lantern", "type": "bar", "char": "µ", "seed_range":6, "threshold":0.04, "hostile_prob":0.45, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#2b1b2b"},
	{ "name": "inn", "display_name": "The Gilded Curtain", "type": "inn", "char": "@", "seed_range":6, "threshold":0.07, "hostile_prob":0.00, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#4a3f55"},
	{ "name": "shopweapons", "display_name": "Razor & Rune", "type": "shop", "char": "Æ", "seed_range":10, "threshold":0.18, "hostile_prob":0.03, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#5a2e2e"},
	{ "name": "shopitems", "display_name": "Curios & Curatives", "type": "shop", "char": "₨", "seed_range":10, "threshold":0.36, "hostile_prob":0.02, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#3b3b4f"},
	{ "name": "shoparmor", "display_name": "Wardwright", "type": "shop", "char": "¥", "seed_range":10, "threshold":0.52, "hostile_prob":0.02, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#6b6b5b"},
	{ "name": "residencelarge", "display_name": "Ironspine Flats", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.72, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#2f2f2f"},
	{ "name": "residencesmall", "display_name": "Lantern Rooms", "type": "residence", "char": "î", "seed_range":4, "threshold":0.9, "hostile_prob":0.12, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#3d2f2f"},
	{ "name": "businesslarge", "display_name": "Obsidian Exchange", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.96, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#1f1f2f"},
	{ "name": "businesssmall", "display_name": "Brokerage & Sundries", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#2b2b2b"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range":1000, "threshold":0.02, "hostile_prob":0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070"},
	{ "name": "other1", "display_name": "The Archive Vaults", "type": "other1", "char": "O", "seed_range":1000, "threshold":0.06, "hostile_prob":0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#4b0082"},
	{ "name": "other2", "display_name": "Broker’s Network", "type": "other2", "char": "0", "seed_range":1000, "threshold":0.06, "hostile_prob":0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#4b0082"},
]

# Sublocation mapping
# Internal sublocations per subtype
# Used when generating buildings to add searchable sublocations.
SUBLOC_MAP = {
 "shop": ["backroom", "storage", "arcane display", "shelf unit", "file cabinet", "vault box"],
 "bar": ["backroom", "storage", "back shelf", "coat rack", "lockbox", "whisper cabinet"],
 "inn": ["common room", "guest room", "dresser", "drawer", "coat closet", "back shelf"],
 "residence": ["kitchen", "bedroom", "closet", "bathroom", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer", "ritual circle", "sigil cache", "enchanted chest", "altar niche"],
 "business": ["reception", "office", "bathroom", "file cabinet", "utility cabinet", "storage chest", "vault box"],
 "alley": ["trash can", "vehicle", "hidden alcove", "vendor stall", "service hatch", "dumpster", "alley crate", "graffiti wall"],
 "street": ["market stall", "fountain", "vehicle", "vendor stall", "display case", "back shelf", "phone booth", "mailbox", "newsstand", "parking meter", "newspaper box"]
}

# SubLocation metadata definitions used when building locations.
# Each entry provides defaults used by the generator and later logic (searchable, loot chance, prompt, etc.).
SUBLOCATION_DEFS = {
 "backroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A small backroom.", "money_range": (1,3)},
 "storage": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.25, "prompt": "A storage area with crates.", "money_range": (2,10)},
 "arcane display": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "An ominous glass case filled with glowing curios.", "money_range": (8,24)},
 "fountain": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A tarnished fountain fed by faintly luminescent water.", "money_range": (15,30)},
 "common room": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A comfortable common room with seating.", "money_range": (10,20)},
 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A working kitchen with utensils and food.", "money_range": (1,3)},
 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A reception area with a desk and ledger.", "money_range": (1,3)},
 "office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "An office strewn with paperwork.", "money_range": (2,6)},
 "bedroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.17, "prompt": "A simple bedroom with a bed and a small chest.", "money_range": (2,10)},
 "guest room": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.17, "prompt": "A simple guest room with a bed and a small chest.", "money_range": (2,10)},
 "bathroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.13, "prompt": "A small bathroom with basic amenities.", "money_range": (1,3)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "A small closet with shelves.", "money_range": (1,3)},
 "trash can": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "A trash can that might contain something useful.", "money_range": (1,3)},
 "vehicle": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.17, "prompt": "An abandoned vehicle.", "money_range": (1,3)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A small iron lockbox bolted to a shelf — someone once trusted this.", "money_range": (2,18)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.13, "prompt": "A glass display case housing small trinkets; one looks loose.", "money_range": (2,16)},
 "whisper cabinet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A narrow cabinet where whispers seem to collect.", "money_range": (5,30)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "An old wooden chest tied shut; its lock looks brittle.", "money_range": (3,20)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A battered dresser with one drawer stuck — something rattles inside.", "money_range": (1,14)},
 "shelf unit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A crowded shelf unit of odds and ends; one book is out of place.", "money_range": (0,6)},
 "file cabinet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.24, "prompt": "A metal file cabinet; the bottom drawer is locked with a paperclip nearby.", "money_range": (2,22)},
 "vault box": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A small private vault box — heavy and whispering of secrets.", "money_range": (10,60)},
 "drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.17, "prompt": "A shallow drawer with receipts and a folded photograph tucked away.", "money_range": (1,10)},
 "coat rack": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A lonely coat rack with a suspiciously heavy pocket.", "money_range": (0,6)},
 "service hatch": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A rusted service hatch with smudged fingerprints — reach inside carefully.", "money_range": (0,6)},
 "ritual circle": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A faded circle with arcane residue.", "money_range": (5,40)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cache of small enchanted sigils.", "money_range": (8,36)},
}