CITY_NAME = "Boiling Bubble"
CITY_DESCRIPTION = (
	"A mist-shrouded hamlet nestled within an ancient forest, where the air is thick with the scent of herbs and magic. "
	"Winding cobblestone paths weave between quaint cottages and towering trees, their branches adorned with glowing lanterns. "
	"The townsfolk, a mix of witches, herbalists, and mystical creatures, bustle about their daily routines, tending to enchanted gardens "
	"and brewing potent potions. At the heart of the village lies the Boiling Bubble Inn, a cozy tavern known for its bubbling cauldrons of "
	"magical brews and lively gatherings. The atmosphere is one of warmth and mystery, where every corner holds the promise of a new enchantment."
)

# Witchy lodging options
ROOM_MENU = [
	{"id": "hearthbench", "name": "Hearth Bench", "value":6, "heal_fraction":0.30},
	{"id": "cottageroom", "name": "Cottage Room", "value":18, "heal_fraction":0.70},
	{"id": "sanctum", "name": "Sanctum Suite", "value":60, "heal_fraction":1.0},
]

# Witchy drink/menu — potions and brews with immediate effects
DRINK_MENU = [
	{"id": "nightbrew", "name": "Night Brew", "value":3, "hp_fraction":0.12, "ap_fraction":0.08, "min_level":1},
	{"id": "mandrakecordial", "name": "Mandrake Cordial", "value":8, "hp_fraction":0.30, "ap_fraction":0.12, "min_level":1},
	{"id": "moontea", "name": "Moon Tea", "value":15, "hp_fraction":0.55, "ap_fraction":0.30, "min_level":2},
	{"id": "philter", "name": "Philter of Vigor", "value":40, "hp_fraction":0.95, "ap_fraction":0.80, "min_level":4},
]

# Additional seeded variants: use canonical 'name' ids (these are identifiers) but give witchy display names
# Ensure there are exactly two residence and two business variants among the list
BUILDINGS = [
	{ "name": "bar", "display_name": "The Midnight Kettle", "type": "bar", "char": "µ", "seed_range":6, "threshold":0.04, "hostile_prob":0.20, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar_witch.svg", "color": "#6b3a3a"},
	{ "name": "inn", "display_name": "The Sleeping Owl Annex", "type": "inn", "char": "@", "seed_range":6, "threshold":0.07, "hostile_prob":0.00, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn_witch.svg", "color": "#7b5e5e"},
	{ "name": "shopweapons", "display_name": "Brooms & Baubles (Tools)", "type": "shop", "char": "Æ", "seed_range":10, "threshold":0.18, "hostile_prob":0.02, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop_brooms.svg", "color": "#7a5a2a"},
	{ "name": "shopitems", "display_name": "Mist & Mortar (Supplies)", "type": "shop", "char": "₨", "seed_range":10, "threshold":0.36, "hostile_prob":0.03, "can_buy": True, "can_sell": True, "image": "/assets/tiles/apothecary.svg", "color": "#6b4f3b"},
	{ "name": "shoparmor", "display_name": "Ward & Weave (Charms)", "type": "shop", "char": "¥", "seed_range":10, "threshold":0.52, "hostile_prob":0.02, "can_buy": True, "can_sell": True, "image": "/assets/tiles/herbal.svg", "color": "#5f8a6f"},
	{ "name": "residencelarge", "display_name": "Loft of Whispered Rites", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.72, "hostile_prob":0.06, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large_witch.svg", "color": "#e6e0e6"},
	{ "name": "residencesmall", "display_name": "Witch Cottage", "type": "residence", "char": "î", "seed_range":4, "threshold":0.92, "hostile_prob":0.12, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small_witch.svg", "color": "#ffeebb"},
	{ "name": "businesslarge", "display_name": "Coven Hall (Guild)", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.96, "hostile_prob":0.10, "can_buy": False, "can_sell": False, "image": "/assets/tiles/coven.svg", "color": "#6b5f8c"},
	{ "name": "businesssmall", "display_name": "Sorcerer's Spire (Study)", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.12, "can_buy": False, "can_sell": False, "image": "/assets/tiles/tower.svg", "color": "#5f5b7a"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "The Emberlight Conclave", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#7b30a2" }, 
	{ "name": "other2", "display_name": "Moonbrew Experimentarium", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#7b30a2" }
]

# Witchy sublocation map — replace/override mapping
SUBLOC_MAP = {
	"shop": ["arcane shelf","potion rack","counter"],
	"bar": ["cauldron","tasting shelf"],
	"inn": ["hearth","guest ledger","attic trunk"],
	"residence": ["hearth shelf","warded chest","mirror"],
	"business": ["ritual room","curios cabinet"],
	"alley": ["rune-strewn crate","broken altar","owl perch"],
	"street": ["talking post","rune kiosk","lamplighter box"],
}

# Witchy sublocation definitions
SUBLOCATION_DEFS = {
	"arcane shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A shelf of chalked vials and oddities; a tucked scroll hums faintly.", "money_range": (0,10)},
	"potion rack": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "Rows of glass bottles shimmer with moonlight; one has been disturbed recently.", "money_range": (2,18)},
	"counter": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A wooden counter littered with lists and tally beads; a coin rolls into view.", "money_range": (0,6)},

	"cauldron": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A bubbling cauldron scents the air; something glints beneath the surface.", "money_range": (1,12)},
	"tasting shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shelf of tiny cups and notes; one vial rattles when you peer at it.", "money_range": (0,8)},

	"hearth": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "Warm ashes, a tucked charm and a folded note; the smell reminds you of old spells.", "money_range": (0,8)},
	"guest ledger": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A leather ledger full of names; a pressed coin slips from between the pages.", "money_range": (0,6)},
	"attic trunk": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A battered trunk packed with props — perhaps one holds a curious trinket.", "money_range": (1,24)},

	"hearth shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "Packets of dried herbs hang from nails; a hidden sachet feels warm.", "money_range": (0,10)},
	"warded chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A small chest carved with sigils; it resists your touch unless you know the word.", "money_range": (5,40)},
	"mirror": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "An old mirror fogged with time; something moves behind the glass.", "money_range": (0,6)},

	"ritual room": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A circle of chalk and dried petals; an envelope waits beside an altar.", "money_range": (0,18)},
	"curios cabinet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "Glass-front cabinets of oddities; a crooked figurine hides a coin slot.", "money_range": (1,20)},

	"rune-strewn crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A crate carved with runes; the scent of rot and spice suggests something valuable inside.", "money_range": (0,12)},
	"broken altar": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A shattered altar with blackened scorch marks; a small reliquary is half-buried.", "money_range": (3,36)},
	"owl perch": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "An abandoned perch with feathers and a note tied in twine; the note flutters open.", "money_range": (0,8)},

	"talking post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A post carved with faces that whisper; a folded coin pouch falls out.", "money_range": (0,6)},
	"rune kiosk": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A kiosk of charms and pamphlets; a single pamphlet hides a pressed coin.", "money_range": (0,10)},
	"lamplighter box": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A metal box used by lamplighters; an old token rattles within.", "money_range": (0,6)},
}