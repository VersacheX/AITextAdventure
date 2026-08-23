CITY_NAME = "Ironveil Foundry"
CITY_DESCRIPTION  = (
	"Ironveil Foundry is a sprawling industrial city nestled within a rugged mountain range. "
	"Once a thriving hub of manufacturing and innovation, the city is now a shadow of its former self, "
	"with abandoned factories and rusting machinery dominating the landscape. "
	"Despite its decline, Ironveil Foundry retains a gritty charm, with its soot-streaked buildings and "
	"narrow alleyways telling tales of a bygone era. The air is thick with the scent of oil and metal, "
	"and the distant rumble of machinery can still be heard echoing through the streets. "
	"Adventurers who venture into Ironveil Foundry will find a city steeped in history and mystery, "
	"where the remnants of its industrial past intertwine with the arcane, "
	"creating a unique and captivating atmosphere."	
)

# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified
# heal_fraction <- fraction of max HP restored <- do not modify
ROOM_MENU = [
 {"id": "public", "name": "Forge Bench", "value":8, "heal_fraction":0.25},
 {"id": "economy", "name": "Worker Bunk", "value":36, "heal_fraction":0.75},
 {"id": "luxury", "name": "Foundry Suite", "value":210, "heal_fraction":1.0},
]

# Simple in-bar drinks menu. Effects are immediate and don't create inventory items.
# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified slightly... bigger drinks are naturally more expensive as buying a drink triggers rng for an enemy, so buying small doesn't pay
# hp_fraction <- fraction of max HP restored immediately <- do not modify
DRINK_MENU = [
 {"id": "tiny", "name": "Coal Ale", "value":11, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
 {"id": "small", "name": "Smokestout", "value":24, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
 {"id": "mid", "name": "Ironwork Cocktail", "value":56, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
 {"id": "big", "name": "Lantern Elixir", "value":120, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
 {"id": "huge", "name": "Forge Draught", "value":260, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":5},
 {"id": "max", "name": "Veil Serum", "value":480, "hp_fraction":1.00, "ap_fraction":0.30, "min_level":8},
]

# Buildings
BUILDINGS = [
	{ "name": "bar", "display_name": "The Coal Lantern", "type": "bar", "char": "µ", "seed_range":6, "threshold":0.05, "hostile_prob":0.40, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#6b5b5b"},
	{ "name": "inn", "display_name": "Smokestack Rest", "type": "inn", "char": "@", "seed_range":10, "threshold":0.08, "hostile_prob":0.01, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#5a4f4a"},
	{ "name": "shopweapons", "display_name": "Grim Gear", "type": "shop", "char": "Æ", "seed_range":12, "threshold":0.22, "hostile_prob":0.06, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#6b3b2f"},
	{ "name": "shopitems", "display_name": "Engineer's Nook", "type": "shop", "char": "₨", "seed_range":12, "threshold":0.40, "hostile_prob":0.04, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#74807f"},
	{ "name": "shoparmor", "display_name": "Plate & Rivet", "type": "shop", "char": "¥", "seed_range":12, "threshold":0.56, "hostile_prob":0.04, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#606060"},
	{ "name": "residencelarge", "display_name": "Rivermill Quarters", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.78, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#c8c8c8"},
	{ "name": "residencesmall", "display_name": "Worker Shacks", "type": "residence", "char": "î", "seed_range":4, "threshold":0.94, "hostile_prob":0.12, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#bdb4aa"},
	{ "name": "businesslarge", "display_name": "Foundry Exchange", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.99, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#63636a"},
	{ "name": "businesssmall", "display_name": "Brokerage Row", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.04, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#5b544f"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "The Rustweld Archives", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#7b30a2" }, 
	{ "name": "other2", "display_name": "Embercoil Relay Station", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#7b30a2" }
]

# Sublocation mapping
SUBLOC_MAP = {
 "shop": ["tool rack", "parts storage", "display case", "shelf unit", "file cabinet", "vault niche"],
 "bar": ["tap shelf", "coal bin", "ember shelf", "bench row", "lock brazier", "whisper alcove"],
 "inn": ["common hall", "guest berth", "dresser", "trunk drawer", "coat closet", "hearth niche"],
 "residence": ["kitchen", "bunkroom", "closet", "wash basin", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer"],
 "business": ["reception", "engine office", "bathroom", "file chest", "utility room", "storage chest", "vault niche"],
 "alley": ["ash heap", "broken cart", "hidden alcove", "vendor stall", "service hatch", "dumpster hollow", "alley crate", "graffiti wall"],
 "street": ["market stall", "fountain pool", "trolley post", "vendor stall", "display case", "back shelf", "message post", "mailbox", "newsstand", "parking post", "newsbox"],
 "works": ["forge pit", "engine room", "vent shaft", "grate panel", "oil drum"],
 "arcane": ["ritual ring", "sigil cache", "enchanted chest", "altar niche", "masonry rune"],
}

# SubLocation metadata definitions used when building locations.
SUBLOCATION_DEFS = {
 "tool rack": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A rack of tools stained with oil and soot.", "money_range": (2,18)},
 "parts storage": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.24, "prompt": "Shelves of stamped parts and coils; one crate is ajar.", "money_range": (3,24)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A glass case with precision pieces and odd trinkets.", "money_range": (4,28)},
 "shelf unit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A cluttered shelf unit of odds and ends with a hidden box.", "money_range": (0,10)},
 "file cabinet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A metal cabinet of invoices and blueprints; a corner peeks loose.", "money_range": (2,22)},
 "vault niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A narrow vault niche sealed behind ironwork.", "money_range": (10,80)},

 "tap shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shelf behind the taps where tokens and notes collect.", "money_range": (1,12)},
 "coal bin": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A bin of coal; something metallic glints between lumps.", "money_range": (1,14)},
 "ember shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shelf warmed by embers holding bottles and scraps.", "money_range": (1,10)},
 "bench row": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A row of benches where workers leave coins in the cracks.", "money_range": (0,8)},
 "lock brazier": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "An iron brazier concealing a small locked compartment.", "money_range": (4,36)},
 "whisper alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A narrow alcove used for quiet deals and ledger swaps.", "money_range": (2,18)},

 "common hall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A smoky common hall with stain-glass and timber posts.", "money_range": (5,30)},
 "guest berth": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A narrow berth with a loose plank and a tucked note.", "money_range": (2,18)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A battered dresser with a jammed drawer; something rattles inside.", "money_range": (1,14)},
 "trunk drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A travel trunk with oilcloth maps and a hidden pouch.", "money_range": (3,24)},
 "coat closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A closet of soot-dark cloaks; a pocket hides a scrap.", "money_range": (0,10)},
 "hearth niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A niche by the hearth where charms and small tools rest.", "money_range": (1,12)},

 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A cramped kitchen with jars, pans, and a hidden spice pouch.", "money_range": (1,10)},
 "bunkroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A crowded bunkroom full of stamped tags and a loose coin.", "money_range": (1,12)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A narrow closet of linens and grease-stained rags.", "money_range": (0,8)},
 "wash basin": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A basin where grease collects; a coin clings beneath.", "money_range": (0,8)},
 "cupboard": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A cupboard with tins and a sealed jar tucked behind.", "money_range": (0,8)},
 "pantry": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A pantry of dried rations; a wrapped sachet rattles.", "money_range": (1,14)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A strapped chest with a faded maker's mark.", "money_range": (2,20)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A small iron lockbox bolted beneath a shelf — heavy inside.", "money_range": (2,18)},

 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A worn reception with ledger sheets and stamped passes.", "money_range": (1,12)},
 "engine office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "An office of blueprints and soot-streaked schedules.", "money_range": (2,20)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A chest of files and manifests; a folded note is wedged inside.", "money_range": (2,24)},
 "utility room": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A room of tools, rope, and a bent key.", "money_range": (0,12)},

 "ash heap": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A cooling ash heap where odd metal scraps glint.", "money_range": (0,10)},
 "broken cart": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cart with splintered boards; a wrapped parcel hides inside.", "money_range": (1,16)},
 "hidden alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A tucked alcove between buildings where contraband waits.", "money_range": (2,22)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A stall selling heat-treated wares; a loose coin falls.", "money_range": (2,18)},
 "service hatch": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A small hatch used for deliveries and secret drops.", "money_range": (0,8)},
 "dumpster hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A hollow under boards where refuse and small finds mingle.", "money_range": (0,12)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A crate left in a narrow alley; straps are frayed.", "money_range": (1,14)},
 "graffiti wall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A soot-streaked wall scrawled with technical diagrams and tags.", "money_range": (0,8)},

 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A bustling market stall of parts, tins, and oddities.", "money_range": (4,28)},
 "fountain pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A carved pool fed by a mountain spring; something glints beneath a sheen of oil.", "money_range": (6,40)},
 "trolley post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A post where trolleys tie; a strap conceals a pouch.", "money_range": (1,18)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A case of forged curios; a tag is loose.", "money_range": (2,20)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A back shelf behind a counter where receipts and small coins gather.", "money_range": (0,12)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A post of pinned notices; one envelope flutters free.", "money_range": (0,8)},
 "mailbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A battered mailbox stuffed with manifests and a faded receipt.", "money_range": (0,10)},
 "newsstand": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A piled newsstand of broadsheets and schematics; a pamphlet falls loose.", "money_range": (1,16)},
 "parking post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A post where tokens are left; coins sometimes fall free.", "money_range": (0,6)},
 "newsbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A metal newsbox stuffed with flyers and a folded note.", "money_range": (0,12)},

 "forge pit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A deep pit where metal glows; tools and scraps litter the edge.", "money_range": (4,40)},
 "engine room": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A humming engine room with levers and labelled cogs.", "money_range": (8,36)},
 "vent shaft": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A narrow shaft of warm air; something shiny is wedged in the grille.", "money_range": (2,20)},
 "grate panel": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A metal grate with a loose panel — reach in carefully.", "money_range": (1,18)},
 "oil drum": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A dented drum of oil; a small tin rattles inside.", "money_range": (0,12)},

 "ritual ring": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A ring of stones scarred with old offerings and faint ash.", "money_range": (4,40)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cache of engraved sigils humming with odd power.", "money_range": (8,36)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "An enchanted chest that resists prying fingers unless coaxed.", "money_range": (10,60)},
 "altar niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A carved niche with offerings and a tucked coin.", "money_range": (5,30)},
 "masonry rune": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A rune cut into a bonded stone; the grooves hide a tiny token.", "money_range": (0,20)},
}