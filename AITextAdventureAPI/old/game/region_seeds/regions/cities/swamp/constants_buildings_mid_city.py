CITY_NAME = "Bayou Nocturne"
CITY_DESCRIPTION = (
	"Bayou Nocturne is a shadowed city of winding canals and moss-draped alleys, where lantern light flickers against the mist. "
	"Built upon ancient swamp grounds, its wooden walkways creak underfoot, and the air is thick with the scent of brine and spice. "
	"The city is a haven for traders, mystics, and those seeking refuge from the outside world, with a rich tapestry of cultures blending together. "
	"At its heart lies the Gator & Gavel, a bustling tavern where deals are struck and secrets exchanged under the watchful eyes of voodoo charms. "
	"Bayou Nocturne is a place where the past and present intertwine, and every shadow holds a story waiting to be uncovered."
)

# Room Menu
ROOM_MENU = [
	{"id": "public", "name": "Stooped Bench", "value":6, "heal_fraction":0.25},
	{"id": "economy", "name": "Boarded Room", "value":30, "heal_fraction":0.75},
	{"id": "luxury", "name": "Bayou Suite", "value":180, "heal_fraction":1.0},
]

# Drinks Menu
DRINK_MENU = [
	{"id": "tiny", "name": "Mire Ale", "value":9, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
	{"id": "small", "name": "Spice Rum", "value":24, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
	{"id": "mid", "name": "Crescent Cocktail", "value":58, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
	{"id": "big", "name": "Lantern Elixir", "value":125, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
	{"id": "huge", "name": "Swampfire Draught", "value":280, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":6},
	{"id": "max", "name": "Nocturne Serum", "value":520, "hp_fraction":1.00, "ap_fraction":0.30, "min_level":9},
]

# Buildings
BUILDINGS = [
	{ "name": "bar", "display_name": "The Gator & Gavel", "type": "bar", "char": "µ", "seed_range":6, "threshold":0.05, "hostile_prob":0.30, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#6b5f5f"},
	{ "name": "inn", "display_name": "Bayou Rest", "type": "inn", "char": "@", "seed_range":9, "threshold":0.08, "hostile_prob":0.03, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#4b5b4b"},
	{ "name": "shopweapons", "display_name": "Hook & Hex", "type": "shop", "char": "Æ", "seed_range":12, "threshold":0.18, "hostile_prob":0.06, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#5b3b2f"},
	{ "name": "shopitems", "display_name": "Crescent Curios", "type": "shop", "char": "₨", "seed_range":12, "threshold":0.36, "hostile_prob":0.05, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#5f8b7b"},
	{ "name": "shoparmor", "display_name": "Hide & Scale", "type": "shop", "char": "¥", "seed_range":12, "threshold":0.52, "hostile_prob":0.05, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#606060"},
	{ "name": "residencelarge", "display_name": "Lantern Quarters", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.75, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#c8d8d0"},
	{ "name": "residencesmall", "display_name": "Shacklines", "type": "residence", "char": "î", "seed_range":4, "threshold":0.92, "hostile_prob":0.10, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#dfe7df"},
	{ "name": "businesslarge", "display_name": "Bay Exchange", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.98, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#5b6b5b"},
	{ "name": "businesssmall", "display_name": "Tally & Taro", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.04, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#6b6b5b"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "Mirelight Bargain Court", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#7b30a2" }, 
	{ "name": "other2", "display_name": "The Lantern‑Sworn Parlour", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#7b30a2" }
]

# Sublocation mapping
SUBLOC_MAP = {
 "shop": ["workbench", "jar shelf", "display case", "shelf unit", "file chest", "vault niche"],
 "bar": ["stoop bench", "brass shelf", "backroom", "whisper alcove", "lock brazier", "notice peg"],
 "inn": ["common hall", "guest room", "dresser", "drawer", "coat peg", "hearth shelf"],
 "residence": ["kitchen", "bedroom", "closet", "wash nook", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer"],
 "business": ["reception", "ledger office", "bathroom", "file chest", "utility hold", "storage chest", "vault niche"],
 "alley": ["muck pool", "half-sunken skiff", "hidden culvert", "vendor stall", "service grate", "dumpster hollow", "alley crate", "moss wall"],
 "street": ["music stall", "canal pool", "sloop post", "vendor stall", "display case", "back shelf", "message post", "mail hollow", "newsleaf"],
 "arcane": ["voodoo shrine", "charms cache", "enchanted chest", "altar niche", "necrotic rune"],
}

# SubLocation metadata definitions
SUBLOCATION_DEFS = {
 "workbench": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A battered workbench littered with hooks, jars and rusted tools.", "money_range": (2,18)},
 "jar shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A shelf of glass jars filled with odd reagents and labeled tags.", "money_range": (1,16)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A glass case of charms, beads and tide-polished trinkets.", "money_range": (3,22)},
 "shelf unit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A crowded shelf unit of tins, maps and wrapped parcels.", "money_range": (0,10)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A chest of manifests and ledger slips; a folded note peeks out.", "money_range": (2,20)},
 "vault niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A small niche sealed behind boards and ironwork.", "money_range": (10,80)},

 "stoop bench": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A stoop full of boots and coins lodged in the creases.", "money_range": (0,10)},
 "brass shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A brass shelf behind the bar where tips and notes gather.", "money_range": (1,14)},
 "backroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A humid backroom thick with tobacco smoke and whispered deals.", "money_range": (1,18)},
 "whisper alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A narrow alcove where notes and IOUs are slipped into cracks.", "money_range": (1,16)},
 "lock brazier": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "An iron brazier hiding a small locked compartment beneath.", "money_range": (3,30)},
 "notice peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A peg with pinned notices and a folded envelope.", "money_range": (0,10)},

 "common hall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A hall where musicians and drinkers gather; coins fall between boards.", "money_range": (4,28)},
 "guest room": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A tidy guest room with a loose board concealing a scrap.", "money_range": (1,16)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A battered dresser with a stuck drawer; something rattles inside.", "money_range": (1,12)},
 "drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "A shallow drawer with damp receipts and a faded photograph.", "money_range": (1,12)},
 "coat peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A peg with a salt-stiff coat; the pocket hides a scrap.", "money_range": (0,10)},
 "hearth shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A shelf above the hearth where jars and charms collect dust.", "money_range": (1,12)},

 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A smoky kitchen with spice jars and a hidden sachet.", "money_range": (1,12)},
 "bedroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A tight bedroom with piled blankets and a coin tucked beneath.", "money_range": (1,12)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A narrow closet of oilcloth and netting; a packet hides inside.", "money_range": (0,8)},
 "wash nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A small wash nook with a cracked basin and a stuck charm.", "money_range": (0,8)},
 "cupboard": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A grease-stained cupboard with tins and a secret seam.", "money_range": (0,8)},
 "pantry": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A pantry of smoked provisions and a hidden packet.", "money_range": (1,14)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "An old chest lashed with rope; something clinks within.", "money_range": (2,18)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A small iron lockbox bolted to a beam — heavy inside.", "money_range": (2,18)},

 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A weathered reception desk with ledger slips and a stub of wax.", "money_range": (1,14)},
 "ledger office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cramped office with tall ledgers and salt-stained receipts.", "money_range": (2,20)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A chest of manifests and notes; a folded scrap peeks out.", "money_range": (2,18)},
 "utility hold": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A damp hold with coils and a bent key.", "money_range": (0,10)},

 "muck pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A slick pool where glints of metal and shells occasionally show.", "money_range": (0,12)},
 "half-sunken skiff": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A skiff half-sunk in the mud; a wrapped bundle hides beneath a thwart.", "money_range": (1,18)},
 "hidden culvert": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A narrow culvert where contraband and notes are stashed.", "money_range": (2,20)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A stall of spice jars, trinkets and tide-polished curios; a coin slips free.", "money_range": (2,18)},
 "service grate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A grated service slot used for deliveries and whispers.", "money_range": (0,8)},
 "dumpster hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A hollow beneath planks where refuse and odd finds gather.", "money_range": (0,12)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A crate left in a lane; straps are waterlogged and frayed.", "money_range": (1,14)},
 "moss wall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A wall covered in hanging moss and tide-scrawl; a loose patch hides a small token.", "money_range": (0,10)},

 "music stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A stall where musicians sell instruments and trinkets; a coin falls when you riff.", "money_range": (3,24)},
 "canal pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A still canal pool where shells and coins gather in the mud.", "money_range": (4,22)},
 "sloop post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A post where sloops moor; a strap conceals a small pouch.", "money_range": (1,18)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A case of tide-polished curios; a tag slips loose.", "money_range": (2,20)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A back shelf behind a counter where receipts and small coins collect.", "money_range": (0,12)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A post of pinned notices and bounties; an envelope flutters free.", "money_range": (0,8)},
 "mail hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A hollowed mail post with damp letters and a salted stamp.", "money_range": (0,12)},
 "newsleaf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A folded newsleaf with a tiny ad tucked inside.", "money_range": (0,10)},

 "voodoo shrine": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A shrine hung with beads, bones and whispered prayers.", "money_range": (4,36)},
 "charms cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cache of small charms humming faintly in a dark cloth.", "money_range": (6,36)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "An enchanted chest that resists prying fingers unless coaxed.", "money_range": (10,60)},
 "altar niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A carved niche with offerings of beads and a tucked coin.", "money_range": (5,30)},
 "necrotic rune": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A rune carved into bogstone; its grooves hide a tiny token.", "money_range": (0,24)},
}