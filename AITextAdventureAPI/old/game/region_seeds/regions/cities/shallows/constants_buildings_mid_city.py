CITY_NAME = "Blackwake Bay"
CITY_DESCRIPTION  = (
	"A bustling port town nestled within a sheltered bay, Blackwake Bay is a hub of maritime activity and intrigue. "
	"Its docks are alive with the sounds of creaking ships, shouting dockworkers, and the salty tang of the sea air. "
	"The town is a labyrinth of narrow alleys, crowded marketplaces, and weathered taverns, where sailors and merchants from distant lands converge to trade goods and share tales of the high seas. "
	"Blackwake Bay is known for its vibrant culture, rich history, and the ever-present undercurrent of danger that lurks in its shadows. "
	"Pirates, smugglers, and adventurers alike are drawn to this coastal haven, seeking fortune and excitement amidst its bustling streets and treacherous waters."
)

# Room Menu
ROOM_MENU = [
 {"id": "public", "name": "Quay Step", "value":6, "heal_fraction":0.25},
 {"id": "economy", "name": "Berth Room", "value":30, "heal_fraction":0.75},
 {"id": "luxury", "name": "Captain's Loft", "value":160, "heal_fraction":1.0},
]

# Drinks Menu
DRINK_MENU = [
 {"id": "tiny", "name": "Dock Ale", "value":10, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
 {"id": "small", "name": "Rum & Brine", "value":22, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
 {"id": "mid", "name": "Cutthroat Cocktail", "value":50, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
 {"id": "big", "name": "Buccaneer Elixir", "value":110, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
 {"id": "huge", "name": "Leviathan Draught", "value":240, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":6},
 {"id": "max", "name": "Blackwake Serum", "value":420, "hp_fraction":1.00, "ap_fraction":0.30, "min_level":9},
]

# Buildings
BUILDINGS = [
	{ "name": "bar", "display_name": "The Rusted Lantern", "type": "bar", "char": "µ", "seed_range":5, "threshold":0.05, "hostile_prob":0.40, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#5f6b6b"},
	{ "name": "inn", "display_name": "The Crow's Berth", "type": "inn", "char": "@", "seed_range":6, "threshold":0.08, "hostile_prob":0.02, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#4b5a5a"},
	{ "name": "shopweapons", "display_name": "Harpoon & Hook", "type": "shop", "char": "Æ", "seed_range":10, "threshold":0.20, "hostile_prob":0.07, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#8b5f5f"},
	{ "name": "shopitems", "display_name": "Booty & Bric-a-brac", "type": "shop", "char": "₨", "seed_range":10, "threshold":0.36, "hostile_prob":0.05, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#5f8b7f"},
	{ "name": "shoparmor", "display_name": "Scale & Salvage", "type": "shop", "char": "¥", "seed_range":10, "threshold":0.52, "hostile_prob":0.05, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#606060"},
	{ "name": "residencelarge", "display_name": "Harbor Blocks", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.74, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#c8dfe0"},
	{ "name": "residencesmall", "display_name": "Skiff Row", "type": "residence", "char": "î", "seed_range":4, "threshold":0.92, "hostile_prob":0.10, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#dfe7df"},
	{ "name": "businesslarge", "display_name": "The Wharf Exchange", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.98, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#4b6b6b"},
	{ "name": "businesssmall", "display_name": "Tally & Tar", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.04, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#6b6b5b"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "Blackwake Tidecourt", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#7b30a2" }, 
	{ "name": "other2", "display_name": "The Smuggler’s Lanternhouse", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#7b30a2" }
]

# Sublocation mapping
SUBLOC_MAP = {
 "shop": ["stern stall", "crate hold", "display case", "shelf unit", "file chest", "vault nook"],
 "bar": ["backroom", "bilge shelf", "embershelf", "whisper peg", "lock brazier", "notice board"],
 "inn": ["common berth", "guest loft", "dresser", "drawer", "coat peg", "hearth shelf"],
 "residence": ["kitchen", "berth", "closet", "bath nook", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer"],
 "business": ["reception", "tally office", "bathroom", "file chest", "utility hold", "storage chest", "vault nook"],
 "alley": ["fish heap", "abandoned skiff", "hidden culvert", "vendor stall", "service grate", "dumpster hollow", "alley crate", "scrawl wall"],
 "street": ["market stall", "tide pool", "skiff post", "vendor stall", "display case", "back shelf", "message post", "mail hollow", "newsstand"],
 "docks": ["pier side", "rope coil", "cargo hold", "crane gear"],
 "arcane": ["ritual ring", "sigil cache", "enchanted chest", "altar niche", "tide rune"],
}

# SubLocation metadata definitions
SUBLOCATION_DEFS = {
 "stern stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A cramped stern stall stacked with salted goods and oddities.", "money_range": (3,20)},
 "crate hold": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A damp crate hold with sealed barrels; one lid creaks open.", "money_range": (2,22)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A glass case of briny trinkets and tide-polished coins.", "money_range": (4,24)},
 "shelf unit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A crowded shelf of jars and ropes; a neat tag flutters.", "money_range": (0,10)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A chest of manifests and ledgers; a folded receipt peeks out.", "money_range": (2,20)},
 "vault nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A small vault nook hidden behind tideboard and iron.", "money_range": (10,80)},

 "backroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cramped backroom smelling of tar and brine.", "money_range": (1,12)},
 "bilge shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A low bilge shelf where oily scraps and coins gather.", "money_range": (1,16)},
 "embershelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A warm shelf holding bottles and tide-stained notes.", "money_range": (1,10)},
 "whisper peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A peg where secret messages and IOUs are hung.", "money_range": (1,14)},
 "lock brazier": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "An iron brazier with a small locked compartment beneath.", "money_range": (3,30)},
 "notice board": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A battered notice board plastered with bounties and scraps.", "money_range": (0,10)},

 "common berth": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shared berth where crews swap stories and lost coins.", "money_range": (2,18)},
 "guest loft": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A cramped guest loft with a loose board hiding a scrap.", "money_range": (1,16)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A battered dresser with a stuck drawer; something rattles.", "money_range": (1,12)},
 "drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "A shallow drawer with damp receipts and a faded photograph.", "money_range": (1,12)},
 "coat peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A peg with a tarred coat; the pocket holds a scrap.", "money_range": (0,10)},
 "hearth shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A shelf above the hearth with jars of pickled oddments.", "money_range": (1,12)},

 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A fish-scented kitchen with jars and a hidden sachet.", "money_range": (1,10)},
 "berth": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A narrow berth with a coin tucked beneath the plank.", "money_range": (1,12)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A closet of oilskin garments and a sealed note.", "money_range": (0,8)},
 "bath nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A salt-stained bath nook with a stuck charm.", "money_range": (0,8)},
 "cupboard": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A sea-splattered cupboard with tins and a secret seam.", "money_range": (0,8)},
 "pantry": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A pantry of salted provisions with a hidden packet.", "money_range": (1,14)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "An old chest lashed with rope; something clinks within.", "money_range": (2,18)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A small iron lockbox bolted to a beam — heavy inside.", "money_range": (2,18)},

 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A weathered reception desk with manifest slips and a stub of wax.", "money_range": (1,12)},
 "tally office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cramped tally office with ledgers and a folded note.", "money_range": (2,18)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A chest of manifests; a folded scrap peeks out.", "money_range": (2,20)},
 "utility hold": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A damp hold with coils and a bent key.", "money_range": (0,10)},

 "fish heap": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A stinking heap of fish guts and discarded tackle; something glints.", "money_range": (0,10)},
 "abandoned skiff": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A beached skiff with a wrapped bundle tucked under a thwart.", "money_range": (1,18)},
 "hidden culvert": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A narrow culvert where contraband and notes are stashed.", "money_range": (2,20)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A stall of salted goods and tide-polished curios; a coin slips free.", "money_range": (2,18)},
 "service grate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A grated service slot used for deliveries and whispers.", "money_range": (0,8)},
 "dumpster hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A hollow beneath planks where refuse and odd finds mingle.", "money_range": (0,12)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A crate washed up in a lane; straps are salt-brittle.", "money_range": (1,14)},
 "scrawl wall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A wall scrawled with gang marks and tide-scribed names.", "money_range": (0,8)},

 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A bustling stall of pickled fish, ropes, and odd trinkets.", "money_range": (4,24)},
 "tide pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shallow tide pool where coins and shells collect.", "money_range": (4,20)},
 "skiff post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A post where skiffs are tied; a strap conceals a pouch.", "money_range": (1,18)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A case of brine-polished curios; a tag is loose.", "money_range": (2,20)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A back shelf where notes and small coins collect in salt.", "money_range": (0,12)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A post of pinned notices and bounties; an envelope flutters loose.", "money_range": (0,8)},
 "mail hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A hollowed mail post with folded letters and a salted stamp.", "money_range": (0,12)},
 "newsstand": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A stacked newsstand of broadsheets and tide-printed notices.", "money_range": (1,16)},

 "ritual ring": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A ring of stones scarred with shell offerings and faint ash.", "money_range": (4,40)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cache of engraved sigils humming with briny power.", "money_range": (8,36)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "An enchanted chest that resists prying fingers unless coaxed.", "money_range": (10,60)},
 "altar niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A carved niche with shell offerings and a tucked coin.", "money_range": (5,30)},
 "tide rune": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A rune carved into kelp-stiff rock; its grooves hide a token.", "money_range": (0,20)},
}