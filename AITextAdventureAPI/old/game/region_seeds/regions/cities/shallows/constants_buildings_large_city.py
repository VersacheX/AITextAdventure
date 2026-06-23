CITY_NAME = "Brineward Harbor"
CITY_DESCRIPTION = (
	"Brineward Harbor is a bustling port city nestled along the jagged coastline, known for its vibrant markets and diverse populace. The city thrives on maritime trade, with ships from distant lands docking at its busy piers. Narrow cobblestone streets wind through districts filled with colorful stalls, taverns, and inns, where sailors and merchants alike gather to share tales and goods. The air is thick with the scent of saltwater and exotic spices, while the sound of seagulls and lively chatter fills the atmosphere. Brineward Harbor is a melting pot of cultures, where adventurers can find rare artifacts, hearty meals, and opportunities for fortune amidst the lively chaos of the harbor."	
)

# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified
# heal_fraction <- fraction of max HP restored <- do not modify
ROOM_MENU = [
 {"id": "public", "name": "Quay Bench", "value":8, "heal_fraction":0.25},
 {"id": "economy", "name": "Berth Loft", "value":50, "heal_fraction":0.75},
 {"id": "luxury", "name": "Lighthouse Suite", "value":350, "heal_fraction":1.0},
]

# Simple in-bar drinks menu. Effects are immediate and don't create inventory items.
# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency  <- can be modified slightly... bigger drinks are naturally more expensive as buying a drink triggers rng for an enemy, so buying small doesn't pay
# hp_fraction <- fraction of max HP restored immediately <- do not modify
DRINK_MENU = [
 {"id": "tiny", "name": "Saltspray Ale", "value":12, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
 {"id": "small", "name": "Tide Mead", "value":28, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
 {"id": "mid", "name": "Gloom Cocktail", "value":68, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
 {"id": "big", "name": "Lantern Elixir", "value":140, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
 {"id": "huge", "name": "Abyss Draught", "value":320, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":6},
 {"id": "max", "name": "Brine Serum", "value":600, "hp_fraction":1.00, "ap_fraction":0.30, "min_level":9},
]

# Buildings
BUILDINGS = [
	{ "name": "bar", "display_name": "The Lantern & Leech", "type": "bar", "char": "µ", "seed_range":7, "threshold":0.05, "hostile_prob":0.38, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#2f4b4b"},
	{ "name": "inn", "display_name": "Harborfall Inn", "type": "inn", "char": "@", "seed_range":11, "threshold":0.10, "hostile_prob":0.01, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#4b6b6b"},
	{ "name": "shopweapons", "display_name": "Harpoon & Hinge", "type": "shop", "char": "Æ", "seed_range":14, "threshold":0.22, "hostile_prob":0.06, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#5b2f2f"},
	{ "name": "shopitems", "display_name": "Curio Dockworks", "type": "shop", "char": "₨", "seed_range":14, "threshold":0.40, "hostile_prob":0.04, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#2f5b5b"},
	{ "name": "shoparmor", "display_name": "Salvage & Scale", "type": "shop", "char": "¥", "seed_range":14, "threshold":0.58, "hostile_prob":0.05, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#606060"},
	{ "name": "residencelarge", "display_name": "Docksman's Quays", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.80, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#c8e7e7"},
	{ "name": "residencesmall", "display_name": "Kettle Row", "type": "residence", "char": "î", "seed_range":4, "threshold":0.95, "hostile_prob":0.12, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#dfe7df"},
	{ "name": "businesslarge", "display_name": "Maritime Exchange", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.98, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#5b6b6b"},
	{ "name": "businesssmall", "display_name": "Quayside Brokers", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.04, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#6b6b5b"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "The Saltwind Exchange Hall", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#4b0082" }, 
	{ "name": "other2", "display_name": "Harborlight Relic Vault", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#4b0082" }
]

# Internal sublocations per subtype
#  Used when generating buildings to add searchable sublocations.
SUBLOC_MAP = {
 "shop": ["stern alcove", "crate hold", "display case", "shelf unit", "file chest", "vault niche"],
 "bar": ["tap shelf", "bilge nook", "ember shelf", "whisper alcove", "lock brazier", "notice board"],
 "inn": ["common room", "berth loft", "dresser", "drawer", "coat peg", "hearth shelf"],
 "residence": ["kitchen", "bedroom", "closet", "bath nook", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer"],
 "business": ["reception", "office", "bathroom", "file chest", "utility hold", "storage chest", "vault niche"],
 "alley": ["fish heap", "abandoned skiff", "hidden culvert", "vendor stall", "service grate", "dumpster hollow", "alley crate", "barnacle wall"],
 "street": ["market stall", "tide pool", "skiff post", "vendor stall", "display case", "back shelf", "message post", "mail hollow", "newsstand", "parking post", "newsbox"],
 "docks": ["pier side", "rope coil", "cargo hold", "crane gear"],
 "arcane": ["ritual ring", "sigil cache", "enchanted chest", "altar niche", "tide rune"],
}

# SubLocation metadata definitions used when building locations.
# Each entry provides defaults used by the generator and later logic (searchable, loot chance, prompt, etc.).
SUBLOCATION_DEFS = {
 "stern alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A cramped stern alcove full of nets, jars, and trade slips.", "money_range": (3,24)},
 "crate hold": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.24, "prompt": "A hold of salted crates and sealed barrels; one crate creaks.", "money_range": (2,28)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A glass display case with briny curios and tide-polished trinkets.", "money_range": (4,30)},
 "shelf unit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A crowded shelf unit of jars and labelled bottles.", "money_range": (0,10)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A chest of manifests and chits; a folded receipt peeks out.", "money_range": (2,26)},
 "vault niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A water-sealed vault niche behind timber and iron.", "money_range": (12,100)},

 "tap shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shelf behind the taps where coins and notes collect in the salt.", "money_range": (1,14)},
 "bilge nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A low bilge nook smelling of oil and brine; something glints.", "money_range": (1,18)},
 "ember shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A warm shelf holding bottles and smudged notes.", "money_range": (1,12)},
 "whisper alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A narrow alcove where secrets and debt slips are left.", "money_range": (2,20)},
 "lock brazier": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "An iron brazier concealing a small locked compartment.", "money_range": (4,36)},
 "notice board": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A battered notice board plastered with adverts and a hidden note.", "money_range": (0,10)},

 "common room": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A smoky common room where crews swap stories and bounties.", "money_range": (5,32)},
 "berth loft": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A cramped berth loft with tucked pockets and a loose floorboard.", "money_range": (2,20)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A battered dresser with a sticky drawer; something rattles within.", "money_range": (1,14)},
 "drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "A shallow drawer with receipts and a damp photograph tucked away.", "money_range": (1,12)},
 "coat peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A peg with a salt-stiff coat; the pocket holds a scrap.", "money_range": (0,10)},
 "hearth shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A shelf above the hearth with jars of pickled oddments.", "money_range": (1,12)},

 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A fish-scented kitchen with jars and a hidden sachet.", "money_range": (1,12)},
 "bedroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A tight bedroom with a woven berth and a coin tucked below.", "money_range": (1,12)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A narrow closet of oilcloth and sea-stiff garments.", "money_range": (0,8)},
 "bath nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shallow bath nook with brine and a stuck charm.", "money_range": (0,8)},
 "cupboard": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A sea-splattered cupboard with tins and a secret seam.", "money_range": (0,8)},
 "pantry": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A pantry of salted provisions and a hidden packet.", "money_range": (1,16)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "An old chest lashed with rope; something clinks within.", "money_range": (2,24)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A small iron lockbox bolted to a beam — heavy inside.", "money_range": (2,22)},

 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A weathered reception desk with manifest slips and a stub of wax.", "money_range": (1,14)},
 "office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cramped office of papers, ledgers and salted receipts.", "money_range": (2,24)},
 "utility hold": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A damp utility hold with coils and a bent key.", "money_range": (0,12)},

 "fish heap": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A stinking heap of fish guts and discarded tackle; something glints.", "money_range": (0,10)},
 "abandoned skiff": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A beached skiff with a wrapped bundle tucked under a thwart.", "money_range": (1,18)},
 "hidden culvert": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A narrow culvert where someone stashed contraband and notes.", "money_range": (2,24)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A stall of salted goods and tide-processed curios; a coin slips free.", "money_range": (2,20)},
 "service grate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A grated service slot used for deliveries and whispers.", "money_range": (0,8)},
 "dumpster hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A hollow beneath planks where refuse and odd finds mingle.", "money_range": (0,12)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A crate washed up in a lane; straps are salt-brittle.", "money_range": (1,14)},
 "barnacle wall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A wall encrusted with barnacles; one chip reveals something small.", "money_range": (0,10)},

 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A busy market stall of pickled fish, ropes, and trinkets.", "money_range": (4,32)},
 "tide pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shallow tide pool where coins and shells collect.", "money_range": (4,20)},
 "skiff post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A post where skiffs are tied; a strap conceals a pouch.", "money_range": (1,18)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A case of brine-polished curios; a tag is loose.", "money_range": (2,22)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A back shelf where notes and small coins collect in salt.", "money_range": (0,12)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A post of pinned notes and wanted flyers; one envelope flutters free.", "money_range": (0,8)},
 "mail hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A hollowed mail post with folded letters and a salted stamp.", "money_range": (0,12)},
 "newsstand": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A piled newsstand of broadsheets and tide-printed leaflets.", "money_range": (1,16)},
 "parking post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A post where small tokens are left; coins sometimes fall free.", "money_range": (0,6)},
 "newsbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A salt-worn newsbox stuffed with flyers and a folded note.", "money_range": (0,12)},

 "ritual ring": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A ring of stones scarred with shell offerings and faint ash.", "money_range": (4,40)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cache of engraved sigils humming with briny power.", "money_range": (8,36)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "An enchanted chest that resists prying fingers unless coaxed.", "money_range": (10,60)},
 "altar niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A carved niche with offerings of shells and a tucked coin.", "money_range": (5,30)},
 "tide rune": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A rune carved into kelp-stiff rock; its grooves hide a tiny token.", "money_range": (0,24)},
}