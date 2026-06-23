CITY_NAME = "Gnashwater Hollow"
CITY_DESCRIPTION = (
    "A fetid swamp city built on stilts and rotten pilings, Gnashwater Hollow is a haven for outcasts, traders, and those seeking refuge from the law. The air is thick with mist and the scent of decay, while the streets are a labyrinth of wooden walkways and rickety bridges connecting dilapidated buildings. The city's economy thrives on black market dealings, exotic goods salvaged from the swamp, and the services of mercenaries and bounty hunters. Despite its grim appearance, Gnashwater Hollow is a place of opportunity for those willing to navigate its treacherous waters."
)

# Room Menu
ROOM_MENU = [
	{"id": "public", "name": "Mire Step", "value":4, "heal_fraction":0.25},
	{"id": "economy", "name": "Bunk Loft", "value":16, "heal_fraction":0.75},
	{"id": "luxury", "name": "Warden's Niche", "value":64, "heal_fraction":1.0},
]

# Drinks Menu
DRINK_MENU = [
	{"id": "tiny", "name": "Rot Ale", "value":6, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
	{"id": "small", "name": "Bog Rum", "value":14, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
	{"id": "mid", "name": "Fang Cocktail", "value":34, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
	{"id": "big", "name": "Gulper Elixir", "value":72, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
	{"id": "huge", "name": "Carrion Draught", "value":150, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":6},
	{"id": "max", "name": "Hunger Serum", "value":300, "hp_fraction":1.00, "ap_fraction":0.25, "min_level":9},
]

# Buildings
BUILDINGS = [
	{ "name": "bar", "display_name": "The Gulper's Maw", "type": "bar", "char": "µ", "seed_range":4, "threshold":0.03, "hostile_prob":0.45, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#2f2b2b"},
	{ "name": "inn", "display_name": "Boneshade Rest", "type": "inn", "char": "@", "seed_range":6, "threshold":0.05, "hostile_prob":0.08, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#3b4b3b"},
	{ "name": "shopweapons", "display_name": "Jaw & Spike", "type": "shop", "char": "Æ", "seed_range":6, "threshold":0.12, "hostile_prob":0.12, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#5b2f2f"},
	{ "name": "shopitems", "display_name": "Bogcurio", "type": "shop", "char": "₨", "seed_range":6, "threshold":0.28, "hostile_prob":0.08, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#2f4b3b"},
	{ "name": "shoparmor", "display_name": "Hide & Husk", "type": "shop", "char": "¥", "seed_range":6, "threshold":0.44, "hostile_prob":0.09, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#606060"},
	{ "name": "residencelarge", "display_name": "Pit Halls", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.58, "hostile_prob":0.06, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#bcd0c8"},
	{ "name": "residencesmall", "display_name": "Shackline", "type": "residence", "char": "î", "seed_range":4, "threshold":0.86, "hostile_prob":0.18, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#dfe7d0"},
	{ "name": "businesslarge", "display_name": "Toll Mort", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.94, "hostile_prob":0.05, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#4b4b4b"},
	{ "name": "businesssmall", "display_name": "Snap Ledger", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.06, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#6b6b5b"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "The Bogrunner Exchange", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#4b0082" }, 
	{ "name": "other2", "display_name": "Rotwharf Broker’s Den", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#4b0082" }
]

# Sublocation mapping
SUBLOC_MAP = {
 "shop": ["workbench", "jar shelf", "display case", "shelf unit", "file chest", "vault nook"],
 "bar": ["gutter bench", "bilge nook", "ember shelf", "whisper nook", "lock brazier", "notice peg"],
 "inn": ["common bunk", "guest bunk", "dresser", "drawer", "coat peg", "hearth nook"],
 "residence": ["kitchen", "bedroom", "closet", "wash nook", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer"],
 "business": ["reception", "supply post", "bath nook", "file chest", "utility alcove", "storage chest", "vault nook"],
 "alley": ["muck pit", "half-buried bone", "stalking reed", "vendor stall", "latrine grate", "dumpster hollow", "alley crate", "fang-scar wall"],
 "street": ["market stall", "drain pool", "stilt post", "vendor stall", "display case", "back shelf", "message post", "mail hollow", "newsleaf"],
 "arcane": ["ritual ring", "sigil cache", "enchanted chest", "altar niche", "necrotic rune"],
}

# SubLocation metadata definitions
SUBLOCATION_DEFS = {
 "workbench": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A blood-splattered workbench with tools, hooks and a busted jaw-bone.", "money_range": (1,16)},
 "jar shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "Shelves of cloudy jars holding pickled bits and strange powders.", "money_range": (1,14)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A battered case of trinkets, teeth and water-smoothed tokens.", "money_range": (2,18)},
 "shelf unit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A crowded shelf of wrapped parcels and salt-crusted tins.", "money_range": (0,10)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A chest of toll records and name-tags; a folded slip peeks out.", "money_range": (1,18)},
 "vault nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A tiny niche sealed with iron, damp to the touch.", "money_range": (8,48)},

 "gutter bench": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A bench set over a gutter of black water; coins sometimes lodge there.", "money_range": (0,8)},
 "bilge nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A low nook smelling of oil and rot; something glints within.", "money_range": (1,12)},
 "ember shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A warmed shelf holding bottles and smudged notes.", "money_range": (1,10)},
 "whisper nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A narrow nook where IOUs, threats and bargains are slipped.", "money_range": (1,14)},
 "lock brazier": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "An iron brazier with a hidden, rusted compartment beneath.", "money_range": (3,26)},
 "notice peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A peg pinned with warnings, bounties and salted letters.", "money_range": (0,8)},

 "common bunk": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shared bunk where the truly desperate sleep and hide valuables.", "money_range": (1,12)},
 "guest bunk": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A guest bunk with a loose plank concealing a small pouch.", "money_range": (1,14)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A damp dresser with a stuck drawer — something rattles.", "money_range": (1,12)},
 "drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A drawer of brittle receipts and a faded photograph.", "money_range": (1,10)},
 "coat peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A peg with a reeking coat; the pocket holds a scrap.", "money_range": (0,8)},
 "hearth nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A small niche by a smoky fire where charms and tools rest.", "money_range": (1,10)},

 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A cramped kitchen with jars of pickled oddments and a hidden sachet.", "money_range": (1,10)},
 "bedroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A tight bedroom with coil-beds and a coin tucked beneath.", "money_range": (1,10)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A narrow closet of oilcloth and reeking furs; a note hides inside.", "money_range": (0,8)},
 "wash nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A cracked basin and a sooty shelf; something clings underneath.", "money_range": (0,8)},
 "cupboard": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cupboard of tins with a secret seam behind a jar.", "money_range": (0,8)},
 "pantry": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A pantry of dried rations and salted roots with a tucked packet.", "money_range": (1,12)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "An old chest tied with rope; something rattles within.", "money_range": (2,16)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A small iron lockbox bolted to a beam — heavy with secrets.", "money_range": (2,16)},

 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A weathered desk with tally slips and salted stubs.", "money_range": (1,10)},
 "supply post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A small supply post stacked with crates and ledger tags.", "money_range": (1,12)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A chest of manifests and crude receipts; a folded note peeks out.", "money_range": (1,14)},
 "utility alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A damp alcove of coils and a bent key.", "money_range": (0,8)},

 "muck pit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A fetid pit where the desperate dive for shiny things.", "money_range": (0,12)},
 "half-buried bone": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A bone half-swallowed by silt; something is wrapped around it.", "money_range": (1,14)},
 "stalking reed": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A patch of tall reeds where small trinkets tangle in the roots.", "money_range": (0,8)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A stall of smoked meats, odd charms and tide-polished junk.", "money_range": (1,14)},
 "latrine grate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A rusted grate above a latrine; reach carefully for anything small.", "money_range": (0,6)},
 "dumpster hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A hollow beneath planks where refuse and odd finds gather.", "money_range": (0,10)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A crate left in a lane; straps are waterlogged and frayed.", "money_range": (1,12)},
 "fang-scar wall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A wall scored with teeth marks and warnings; a loose chip hides a token.", "money_range": (0,10)},

 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A small market stall of smoked goods, bait and trinkets.", "money_range": (3,20)},
 "drain pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shallow pool where coins and shells collect among the muck.", "money_range": (3,18)},
 "stilt post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A post supporting a shack; straps conceal small pouches.", "money_range": (1,12)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A dusty back shelf where notes and small coins collect.", "money_range": (0,10)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.07, "prompt": "A post of pinned notices; one envelope flutters loose.", "money_range": (0,8)},
 "mail hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A hollowed mail post with damp letters and a salt-streaked stamp.", "money_range": (0,10)},
 "newsleaf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A weathered newsleaf with a tiny ad tucked inside.", "money_range": (0,10)},

 "ritual ring": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A ring of stones scored with offerings and fetid ash.", "money_range": (2,30)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cache of carved sigils humming with swamp-magic.", "money_range": (6,28)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "An enchanted chest that resists prying without the right token.", "money_range": (8,48)},
 "altar niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A carved niche with offerings of bone, beads and a tucked coin.", "money_range": (3,18)},
 "necrotic rune": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "A rune carved into bogstone; its grooves hide a token.", "money_range": (0,12)},
}