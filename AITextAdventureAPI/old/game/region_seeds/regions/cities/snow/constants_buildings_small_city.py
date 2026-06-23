CITY_NAME = "Bleakwatch Outpost"
CITY_DESCRIPTION = (
	"Bleakwatch Outpost is a remote settlement perched on the edge of a frozen wasteland. "
	"Once a bustling hub for explorers and traders, it now serves as a solitary refuge against the relentless cold. "
	"The outpost is characterized by its sturdy wooden structures, fortified against the harsh winds and snowstorms that frequently batter the area. "
	"Narrow streets wind between buildings, often obscured by drifting snow, while the distant howls of arctic creatures echo through the icy air. "
	"Despite its isolation, Bleakwatch Outpost is a place of resilience and camaraderie, where inhabitants band together to survive the unforgiving environment. "
	"Visitors to the outpost are greeted with a mix of wary glances and warm hospitality, as locals share stories of survival and adventure in this frozen frontier."
)

# Room Menu
ROOM_MENU = [
	{"id": "public", "name": "Frost Bench", "value":4, "heal_fraction":0.25},
	{"id": "economy", "name": "Bunk Loft", "value":16, "heal_fraction":0.75},
	{"id": "luxury", "name": "Keeper's Niche", "value":60, "heal_fraction":1.0},
]

# Drinks Menu
DRINK_MENU = [
	{"id": "tiny", "name": "Snow Ale", "value":6, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
	{"id": "small", "name": "Cinder Mead", "value":14, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
	{"id": "mid", "name": "Hearth Grog", "value":32, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
	{"id": "big", "name": "Watcher Elixir", "value":68, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
	{"id": "huge", "name": "Polar Draught", "value":140, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":6},
	{"id": "max", "name": "Bleak Serum", "value":260, "hp_fraction":1.00, "ap_fraction":0.25, "min_level":8},
]

# Buildings
BUILDINGS = [
	{ "name": "bar", "display_name": "The Lantern Trap", "type": "bar", "char": "µ", "seed_range":4, "threshold":0.02, "hostile_prob":0.28, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#2b3b3b"},
	{ "name": "inn", "display_name": "Wayfarer's Rest", "type": "inn", "char": "@", "seed_range":6, "threshold":0.04, "hostile_prob":0.01, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#5b6b6b"},
	{ "name": "shopweapons", "display_name": "Spike & Husk", "type": "shop", "char": "Æ", "seed_range":7, "threshold":0.10, "hostile_prob":0.04, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#5b2f2f"},
	{ "name": "shopitems", "display_name": "Trader's Cache", "type": "shop", "char": "₨", "seed_range":7, "threshold":0.26, "hostile_prob":0.03, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#3b5b5b"},
	{ "name": "shoparmor", "display_name": "Pelt & Plate", "type": "shop", "char": "¥", "seed_range":7, "threshold":0.42, "hostile_prob":0.03, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#666666"},
	{ "name": "residencelarge", "display_name": "Watcher's Hall", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.60, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#dfe7ee"},
	{ "name": "residencesmall", "display_name": "Hutline", "type": "residence", "char": "î", "seed_range":4, "threshold":0.86, "hostile_prob":0.07, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#eef3f5"},
	{ "name": "businesslarge", "display_name": "Supply Exchange", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.90, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#5b6b6b"},
	{ "name": "businesssmall", "display_name": "Ledger Post", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.02, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#7b7b7b"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "The Windbreak Vigil Station", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#4b0082" }, 
	{ "name": "other2", "display_name": "Frostline Survivor’s Exchange", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#4b0082" }
]

# Sublocation mapping
SUBLOC_MAP = {
 "shop": ["supply nook", "crate pile", "display case", "ice shelf", "file chest", "vault nook"],
 "bar": ["stump bench", "backroom", "ember shelf", "whisper nook", "lock brazier", "notice peg"],
 "inn": ["common loft", "guest bunk", "dresser", "drawer", "coat peg", "hearth nook"],
 "residence": ["kitchen", "bedroom", "closet", "bath nook", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer"],
 "business": ["reception", "supply office", "wash nook", "file chest", "utility hold", "storage chest", "vault nook"],
 "alley": ["snow drift", "broken sled", "hidden alcove", "vendor stall", "service grate", "dumpster hollow", "alley crate", "frost scrawl"],
 "street": ["market stall", "fountain pool", "sled post", "vendor stall", "display case", "back shelf", "message post", "mail hollow", "newsleaf"],
 "arcane": ["ritual ring", "sigil cache", "enchanted chest", "altar niche", "frost rune"],
}

# SubLocation metadata definitions
SUBLOCATION_DEFS = {
 "supply nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A cramped nook of salted supplies and trade slips.", "money_range": (2,18)},
 "crate pile": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A pile of frost-rimmed crates; one lid is loose.", "money_range": (1,16)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A glass case of small curios and carved tokens.", "money_range": (2,16)},
 "ice shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shelf dusted with rime holding jars and tins.", "money_range": (0,10)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A chest of manifests and supply ledgers; a scrap peeks out.", "money_range": (1,18)},
 "vault nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A tiny vault nook behind packed snowboards and iron.", "money_range": (8,48)},

 "stump bench": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A frost-carved stump bench where coins lodge in the grain.", "money_range": (0,8)},
 "backroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cramped backroom smelling of tar and smoke.", "money_range": (1,12)},
 "ember shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A warm shelf holding tins and smudged notes.", "money_range": (1,10)},
 "whisper nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A narrow nook where secret messages are slipped.", "money_range": (1,14)},
 "lock brazier": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "An iron brazier hiding a small locked compartment.", "money_range": (3,26)},
 "notice peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A peg with pinned notices; one envelope flutters loose.", "money_range": (0,8)},

 "common loft": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shared loft with low beds and tucked pockets.", "money_range": (1,12)},
 "guest bunk": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A small bunk with a loose plank hiding a scrap.", "money_range": (1,14)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A battered dresser with a stuck drawer; something rattles inside.", "money_range": (1,12)},
 "drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A shallow drawer with damp receipts and a faded photograph.", "money_range": (1,10)},
 "coat peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A peg with a heavy coat; the pocket hides a scrap.", "money_range": (0,8)},
 "hearth nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A nook by the hearth where charms and small tools are kept.", "money_range": (1,10)},

 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A simple kitchen with jars of preserved meat and spice pouches.", "money_range": (1,8)},
 "bedroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A tight bedroom with piled furs and a coin tucked beneath.", "money_range": (1,10)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A narrow closet of furs and oilcloth; a folded note hides inside.", "money_range": (0,8)},
 "bath nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A small bath nook warmed by steam; a tin hides below.", "money_range": (0,8)},
 "cupboard": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cupboard of tins with a hidden seam behind a jar.", "money_range": (0,8)},
 "pantry": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A pantry of dried rations with a wrapped sachet.", "money_range": (1,12)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "An old chest lashed with rope; something clinks within.", "money_range": (2,16)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A small iron lockbox bolted to a beam — heavy inside.", "money_range": (2,16)},

 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A weathered reception desk with manifest slips and a stub of wax.", "money_range": (1,10)},
 "supply office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cramped supply office with ledgers and crates.", "money_range": (1,12)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A chest of manifests and supply notes; a folded scrap peeks out.", "money_range": (1,14)},
 "utility hold": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A damp hold with coils and a bent key.", "money_range": (0,10)},

 "snow drift": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A drift of powder snow hiding lost trinkets and a crusted coin.", "money_range": (0,8)},
 "broken sled": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A splintered sled with a wrapped parcel tucked beneath.", "money_range": (1,12)},
 "hidden alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A narrow alcove between stout huts where contraband is stashed.", "money_range": (1,16)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A stall of smoked fish and small wares; a coin slides loose.", "money_range": (1,14)},
 "service grate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A grated service slot used for deliveries and whispers.", "money_range": (0,8)},
 "dumpster hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A hollow beneath planks where odd finds gather.", "money_range": (0,10)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A crate left in a lane; straps are frost-brittle.", "money_range": (1,12)},
 "frost scrawl": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A wall scrawled with marks; a loose chip reveals a token.", "money_range": (0,8)},

 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A small market stall of salted meat, furs and handcrafts.", "money_range": (3,20)},
 "fountain pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shallow pool half-frozen where coins glint beneath.", "money_range": (4,24)},
 "sled post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A post where sleds tie; a strap conceals a small pouch.", "money_range": (1,12)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A small case of frost-polished curios; a tag is loose.", "money_range": (1,12)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A back shelf where notes and coins collect in frost.", "money_range": (0,8)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.07, "prompt": "A post of pinned notices; one envelope flutters loose.", "money_range": (0,8)},
 "mail hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A hollowed mail post with damp letters and a salt-stained stamp.", "money_range": (0,10)},
 "newsleaf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A weathered newsleaf with a tiny advert tucked inside.", "money_range": (0,10)},

 "ritual ring": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A ring of stones worn smooth by offerings of bone and shell.", "money_range": (2,30)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cache of engraved sigils humming with frost-power.", "money_range": (6,28)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "An enchanted chest resistant to prying fingers.", "money_range": (8,48)},
 "altar niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A carved niche with rime-offerings and a tucked coin.", "money_range": (3,18)},
 "frost rune": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "A rune etched into ice-smoothed stone; its grooves hide a token.", "money_range": (0,12)},
}