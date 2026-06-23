CITY_NAME = "The Desert Metropolis"
CITY_DESCRIPTION = (
	"A sprawling urban expanse in the heart of a vast desert, where towering skyscrapers of glass and steel rise above sandy streets. "
	"The city is a bustling hub of commerce and culture, with a mix of modern architecture and remnants of old-world charm. "
	"Neon lights flicker against the backdrop of endless dunes, creating a surreal blend of technology and nature. "
	"The air is dry and warm, carrying the scent of spices and machinery. "
	"Amidst the urban chaos, pockets of greenery and oases provide respite for weary travelers."
)

# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified
# heal_fraction <- fraction of max HP restored <- do not modify
ROOM_MENU = [
 {"id": "public", "name": "Bench", "value":5, "heal_fraction":0.25},
 {"id": "economy", "name": "Room", "value":20, "heal_fraction":0.75},
 {"id": "luxury", "name": "Private Suite", "value":75, "heal_fraction":1.0},
]

# Simple in-bar drinks menu. Effects are immediate and don't create inventory items.
# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency  <- can be modified slightly... bigger drinks are naturally more expensive as buying a drink triggers rng for an enemy, so buying small doesn't pay
# hp_fraction <- fraction of max HP restored immediately <- do not modify
DRINK_MENU = [
 {"id": "tiny", "name": "Ale", "value":8, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
 {"id": "small", "name": "Stout", "value":17, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
 {"id": "mid", "name": "Cocktail", "value":35, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
 {"id": "big", "name": "Triple Hitter", "value":75, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
 {"id": "huge", "name": "Absinthe", "value":160, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":4},
 {"id": "max", "name": "Elixir", "value":200, "hp_fraction":1.00, "ap_fraction":0.20, "min_level":4},
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
	{ "name": "bar", "display_name": "The Local", "type": "bar", "char": "µ", "seed_range":1000, "threshold":0.03, "hostile_prob":0.4, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#8b3e3e"},
	{ "name": "inn", "display_name": "The Cozy Inn", "type": "inn", "char": "@", "seed_range":1000, "threshold":0.06, "hostile_prob":0.00, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#9bd0ff"},
	{ "name": "shopweapons", "display_name": "Stuff That Does Damage", "type": "shop", "char": "Æ", "seed_range":1000, "threshold":0.16, "hostile_prob":0.01, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#c28f5b"},
	{ "name": "shopitems", "display_name": "Stuff With Utility", "type": "shop", "char": "₨", "seed_range":1000, "threshold":0.34, "hostile_prob":0.01, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#c28f5b"},
	{ "name": "shoparmor", "display_name": "Stuff You Never Hope You Have To Use", "type": "shop", "char": "¥", "seed_range":1000, "threshold":0.5, "hostile_prob":0.01, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#c28f5b"},
	{ "name": "residencelarge", "display_name": "The Condos", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.7, "hostile_prob":0.01, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#dfe7d8"},
	{ "name": "residencesmall", "display_name": "The Simps", "type": "residence", "char": "î", "seed_range":4, "threshold":0.9, "hostile_prob":0.1, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#ffd"},
	{ "name": "businesslarge", "display_name": "The Offices", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.95, "hostile_prob":0.01, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#c0c0c0"},
	{ "name": "businesssmall", "display_name": "Some Random Service", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.01, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#c0c0c0"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range":1000, "threshold":0.02, "hostile_prob":0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070"},
	{ "name": "other1", "display_name": "The Black Market Guild", "type": "other1", "char": "O", "seed_range":1000, "threshold":0.06, "hostile_prob":0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#4b0082"},
	{ "name": "other2", "display_name": "Broker's Hideout", "type": "other2", "char": "0", "seed_range":1000, "threshold":0.06, "hostile_prob":0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#4b0082"},
	# 
]

# Internal sublocations per subtype
#  Used when generating buildings to add searchable sublocations.
SUBLOC_MAP = {
 "shop": ["backroom", "storage", "display case", "shelf unit", "file cabinet", "vault box"],
 "bar": ["backroom", "storage", "back shelf", "coat rack", "lockbox", "display case"],
 "inn": ["common room", "guest room", "dresser", "drawer", "coat closet", "back shelf"],
 "residence": ["kitchen", "bedroom", "closet", "bathroom", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer"],
 "business": ["reception", "office", "bathroom", "file cabinet", "utility cabinet", "storage chest", "vault box"],
 "alley": ["trash can", "vehicle", "hidden alcove", "vendor stall", "service hatch", "dumpster", "alley crate", "graffiti wall"],
 "street": ["market stall", "fountain", "vehicle", "vendor stall", "display case", "back shelf", "phone booth", "mailbox", "newsstand", "parking meter", "newspaper box"],
 #"sewer": ["tunnel", "junction"],
}

# SubLocation metadata definitions used when building locations.
# Each entry provides defaults used by the generator and later logic (searchable, loot chance, prompt, etc.).
SUBLOCATION_DEFS = {
 "backroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A small backroom.", "money_range": (1,3)},
 "storage": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.25, "prompt": "A storage area with crates.", "money_range": (2,10)},
 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A market stall with goods.", "money_range": (6,12)},
 "fountain": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A fountain.", "money_range": (15,30)},
 "common room": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A comfortable common room with seating.", "money_range": (10,20)},
 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A working kitchen with utensils and food.", "money_range": (1,3)},
 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A reception area with a desk and ledger.", "money_range": (1,3)},
 "office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "An office strewn with paperwork.", "money_range": (2,6)},
 "bedroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.17, "prompt": "A simple bedroom with a bed and a small chest.", "money_range": (2,10)},
 "guest room": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.17, "prompt": "A simple guest room with a bed and a small chest.", "money_range": (2,10)},
 "commercial kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A commercial kitchen with fat friers and grills.", "money_range": (1,3)},
 "bathroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.13, "prompt": "A small bathroom with basic amenities.", "money_range": (1,3)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "A small closet with shelves.", "money_range": (1,3)},
 "trash can": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "A trash can that might contain something useful.", "money_range": (1,3)},
 "vehicle": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.17, "prompt": "An abandoned vehicle.", "money_range": (1,3)} 
}

# Additional sublocation definitions (added variants)
SUBLOCATION_DEFS.update({
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A small iron lockbox bolted to a shelf — someone once trusted this.", "money_range": (2,18)},
 "cupboard": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A grease-stained cupboard with mismatched plates and a secret stain on the back.", "money_range": (0,8)},
 "side room": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A cramped side room where deals used to be made; look under the coat.", "money_range": (1,12)},
 "service hatch": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A rusted service hatch with smudged fingerprints — reach inside carefully.", "money_range": (0,6)},
 "coat closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A narrow coat closet filled with stale coats and hidden receipts.", "money_range": (0,10)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "An old wooden chest tied shut; its lock looks brittle.", "money_range": (3,20)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A battered dresser with one drawer stuck — something rattles inside.", "money_range": (1,14)},
 "shelf unit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A crowded shelf unit of odds and ends; one book is out of place.", "money_range": (0,6)},
 "file cabinet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.24, "prompt": "A metal file cabinet; the bottom drawer is locked with a paperclip nearby.", "money_range": (2,22)},
 "vault box": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A small private vault box — heavy and whispering of secrets.", "money_range": (10,60)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A back shelf behind the register, dust hides loose change and notes.", "money_range": (0,9)},
 "drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.17, "prompt": "A shallow drawer with receipts and a folded photograph tucked away.", "money_range": (1,10)},
 "coat rack": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A lonely coat rack with a suspiciously heavy pocket.", "money_range": (0,6)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.13, "prompt": "A glass display case housing small trinkets; one looks loose.", "money_range": (2,16)},
 "utility cabinet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "A grimy utility cabinet with labeled drawers and a faded receipt stuck inside.", "money_range": (1,12)},
})

# More neo-noir street/urban searchables
SUBLOCATION_DEFS.update({
 "dumpster": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A dented dumpster reeking of yesterday's secrets; something glints at the back.", "money_range": (0,8)},
 "phone booth": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A cracked phone booth with graffiti and folded notes wedged under the receiver.", "money_range": (0,6)},
 "computer desk": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A cluttered computer desk with sticky notes and a drawer full of password hints.", "money_range": (1,20)},
 "gun safe": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "A heavy gun safe bolted to the floor; the combination is long lost, but worth trying.", "money_range": (20,120)},
 "mailbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A battered mailbox stuffed with old letters and the occasional valuable receipt.", "money_range": (0,10)},
 "newsstand": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A tattered newsstand piled with papers; a postcard falls out when you flip through.", "money_range": (1,12)},
 "parking meter": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A coin-stuffed parking meter; slotted coins clink when you prod it.", "money_range": (0,6)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A stack of wooden crates in the alley — one seems freshly moved and slightly ajar.", "money_range": (1,14)},
 "graffiti wall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A graffiti-strewn wall hides a loose brick behind a faded tag.", "money_range": (0,8)},
 "newspaper box": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A metal newspaper box with yesterday's headlines; an envelope is taped inside.", "money_range": (0,12)},
})