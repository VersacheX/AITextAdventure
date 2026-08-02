CITY_NAME = "BioHazard"
CITY_DESCRIPTION = (
	"A battered outpost in the wasteland, serving as a hub for scavengers and survivors. "
	"Amidst the ruins, makeshift buildings constructed from salvaged materials provide shelter and trade opportunities. "
	"The air is thick with dust and the distant hum of mutated creatures. "
	"Despite the harsh conditions, the outpost thrives as a beacon of hope and resilience in a desolate world."
)


# Rugged lodging options for survivors
ROOM_MENU = [
	{"id": "bench", "name": "Rust Bench", "value":4, "heal_fraction":0.20},
	{"id": "bunk", "name": "Bunk Bed", "value":15, "heal_fraction":0.60},
	{"id": "safehut", "name": "Safe Hut", "value":50, "heal_fraction":0.95},
]

# Rough survival rations and brews
DRINK_MENU = [
	{"id": "sterilized_water", "name": "Sterilized Water", "value":2, "hp_fraction":0.05, "ap_fraction":0.0, "min_level":1},
	{"id": "jerkyshot", "name": "Jerky Shot", "value":8, "hp_fraction":0.18, "ap_fraction":0.05, "min_level":1},
	{"id": "radtea", "name": "Rad Tea", "value":20, "hp_fraction":0.40, "ap_fraction":0.15, "min_level":2},
	{"id": "adrenaline", "name": "Adrenaline Draught", "value":60, "hp_fraction":0.75, "ap_fraction":0.40, "min_level":4},
]

# Canonical building ids kept; display names set to post-apoc variants
BUILDINGS = [
	{ "name": "bar", "display_name": "Dust & Drums Tap", "type": "bar", "char": "µ", "seed_range":6, "threshold":0.035, "hostile_prob":0.38, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#5b2e2e" },
	{ "name": "inn", "display_name": "Wasteland Rest Stop", "type": "inn", "char": "@", "seed_range":6, "threshold":0.05, "hostile_prob":0.01, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#7fb8ff" },
	{ "name": "shopweapons", "display_name": "Scavenger's Arsenal", "type": "shop", "char": "Æ", "seed_range":10, "threshold":0.20, "hostile_prob":0.03, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#b05f3f" },
	{ "name": "shopitems", "display_name": "Junkyard Jewels", "type": "shop", "char": "₨", "seed_range":10, "threshold":0.30, "hostile_prob":0.02, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#c18f6a" },
	{ "name": "shoparmor", "display_name": "Fortified Finds", "type": "shop", "char": "¥", "seed_range":10, "threshold":0.48, "hostile_prob":0.02, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#8f6b4a" },
	{ "name": "residencelarge", "display_name": "Barricaded Suites", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.74, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#e8efe6"},
	{ "name": "residencesmall", "display_name": "Shelter Row", "type": "residence", "char": "î", "seed_range":4, "threshold":0.88, "hostile_prob":0.11, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#ffecb3" },
	{ "name": "businesslarge", "display_name": "Market Hub", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.94, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#a7a7a7" },
	{ "name": "businesssmall", "display_name": "Trade Post", "type": "business", "char": "ï", "seed_range":4, "threshold":0.98, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#c7c7c7" },

	# region extras
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range":1000, "threshold":0.02, "hostile_prob":0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070"},
	{ "name": "other1", "display_name": "The Neon Spine", "type": "other1", "char": "O", "seed_range":1000, "threshold":0.06, "hostile_prob":0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#4b0082"},
	{ "name": "other2", "display_name": "Black Bazaar", "type": "other2", "char": "0", "seed_range":1000, "threshold":0.06, "hostile_prob":0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#4b0082"},
]

# Post-apocalyptic sublocation map — assign searchables to building types
SUBLOC_MAP = {
	"shop": ["salvage_pile","parts_rack","trade_counter", "gun safe"],
	"bar": ["barrel_fire","jukebox","canteen_stall", "gun safe"],
	"inn": ["bunk_locker","guest_log","attic_cache","gun safe"],
	"residence": ["stash_hole","boarded_chest","hearth_ash", "gun safe"],
	"business": ["workbench","fuel_cache","ledger_box", "gun safe"],
	"alley": ["scrap_heap","oil_drum","makeshift_shrine", "dumpster"],
	"street": ["signal_post","bulletin_board","vendor_box"],
}

# Extended post-apocalyptic sublocation definitions
SUBLOCATION_DEFS = {
	"salvage_pile": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.30, "prompt": "A pile of twisted metal and broken electronics; something useful might be hidden within.", "money_range": (0,12)},
	"parts_rack": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "Shelves of scavenged parts and wire; a labeled crate rattles when you touch it.", "money_range": (1,20)},
	"trade_counter": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A battered counter with trade ledgers and a loose coin; the merchant's safe looks cracked.", "money_range": (0,8)},

	"barrel_fire": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A barrel fire where folks warm themselves; someone left a wrapped bundle beside it.", "money_range": (0,10)},
	"jukebox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A battered music box with a single cassette stuck inside; pockets may have been picked during the revelry.", "money_range": (0,6)},
	"canteen_stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A stall selling boiled water and jerky; a locked crate behind the stall clinks when nudged.", "money_range": (1,14)},

	"bunk_locker": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A rusted locker at the foot of the bunk; someone once hid a small pouch inside.", "money_range": (0,10)},
	"guest_log": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A greasy guest log full of names and scribbles; a pressed coin falls from a torn page.", "money_range": (0,6)},
	"attic_cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.24, "prompt": "A hidden trunk in the attic filled with scavenged trinkets and perhaps a useful spare part.", "money_range": (2,26)},

	"stash_hole": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A hollow dug beneath the floorboards; cloth-wrapped items are tucked inside.", "money_range": (0,14)},
	"boarded_chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A chest reinforced with scrap metal and seals; it groans when opened.", "money_range": (3,30)},
	"hearth_ash": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.07, "prompt": "Swept hearth ashes hide small tokens and sometimes a coin that survived the fires.", "money_range": (0,8)},

	"workbench": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A greasy workbench with half-finished repairs; a labeled box of parts sits within reach.", "money_range": (1,18)},
	"fuel_cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "Barrels marked with faded symbols; a sealed drum might contain usable fuel.", "money_range": (2,22)},
	"ledger_box": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A locked box of trade records and IOUs; a note tucked inside points to a hidden stash.", "money_range": (0,8)},

	"scrap_heap": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.28, "prompt": "A heap of twisted scrap and vehicle parts; a glint near the center catches your eye.", "money_range": (0,12)},
	"oil_drum": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A dented oil drum; a sealed container might hold something useful for trade.", "money_range": (0,10)},
	"Makeshift_shrine": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "A crude shrine of tires and talismans; offerings might include trinkets or odd coins.", "money_range": (0,6)},

	"signal_post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A battered post with flags and notes; a map fragment might be pinned beneath the tacks.", "money_range": (0,6)},
	"bulletin_board": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A board of postings and lost notices; someone stitched a small pouch behind a flyer.", "money_range": (0,8)},
	"vendor_box": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A closed vendor box once used to sell spare parts; a coin rolls out when you shake it.", "money_range": (0,10)},

	# keep a few legacy defs for compatibility
	"dumpster": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A rusted dumpster smelling of decay and metal; you might find something valuable inside.", "money_range": (0,8)},
	"gun safe": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "A heavy gun safe with rusty hinges; possibly contains valuable weapons.", "money_range": (20,120)},
}
