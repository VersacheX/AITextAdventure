CITY_NAME = "Hailward Hold"
CITY_DESCRIPTION = (
	"Nestled within a frozen fjord, Hailward Hold is a bustling city of ice-carved stone and timbered longhouses. "
	"Frost-laden streets wind between towering halls adorned with intricate runic carvings, while the air is filled with the scent of smoked fish and pine. "
	"Citizens clad in furs and leather trade goods in lively markets, their breath misting in the crisp air as they navigate the city's labyrinthine alleys. "
	"At the heart of the hold stands the Jarl's Keep, a formidable structure of ice and stone, overlooking the bustling harbor where longships are moored against the icy waters. "
	"Despite the harsh climate, Hailward Hold thrives as a center of commerce and culture, its people resilient and resourceful in the face of winter's embrace."
)

# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified
# heal_fraction <- fraction of max HP restored <- do not modify
ROOM_MENU = [
	{"id": "public", "name": "Stone Bench", "value":7, "heal_fraction":0.25},
	{"id": "economy", "name": "Bunk Chamber", "value":34, "heal_fraction":0.75},
	{"id": "luxury", "name": "Jarl's Suite", "value":220, "heal_fraction":1.0},
]

# Drinks Menu
DRINK_MENU = [
	{"id": "tiny", "name": "Fjord Ale", "value":11, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
	{"id": "small", "name": "Skald Stout", "value":26, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
	{"id": "mid", "name": "Viking Grog", "value":62, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
	{"id": "big", "name": "Rime Elixir", "value":130, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
	{"id": "huge", "name": "Winter Draught", "value":300, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":6},
	{"id": "max", "name": "Hold Serum", "value":560, "hp_fraction":1.00, "ap_fraction":0.30, "min_level":9},
]

# Buildings
BUILDINGS = [
	{ "name": "bar", "display_name": "The Skald's Lantern", "type": "bar", "char": "µ", "seed_range":6, "threshold":0.05, "hostile_prob":0.32, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#3b4b5b"},
	{ "name": "inn", "display_name": "Hall of Hearths", "type": "inn", "char": "@", "seed_range":9, "threshold":0.08, "hostile_prob":0.02, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#6b7b8b"},
	{ "name": "shopweapons", "display_name": "Rivet & Rune", "type": "shop", "char": "Æ", "seed_range":11, "threshold":0.20, "hostile_prob":0.07, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#6b3b3b"},
	{ "name": "shopitems", "display_name": "Frostwright's Goods", "type": "shop", "char": "₨", "seed_range":11, "threshold":0.36, "hostile_prob":0.04, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#3b5b6b"},
	{ "name": "shoparmor", "display_name": "Pelt & Plate", "type": "shop", "char": "¥", "seed_range":11, "threshold":0.52, "hostile_prob":0.05, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#5b6b6b"},
	{ "name": "residencelarge", "display_name": "Holdquarters", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.72, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#dfeefe"},
	{ "name": "residencesmall", "display_name": "Frostrows", "type": "residence", "char": "î", "seed_range":4, "threshold":0.9, "hostile_prob":0.11, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#eef5f8"},
	{ "name": "businesslarge", "display_name": "Clan Exchange", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.96, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#5b6b7b"},
	{ "name": "businesssmall", "display_name": "Ledger & Tally", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.04, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#7b7f7f"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "Runeflare Assembly Yard", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#4b0082" }, 
	{ "name": "other2", "display_name": "The Icebound Speaker’s Circle", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#4b0082" }
]

# Sublocation mapping
SUBLOC_MAP = {
 "shop": ["longhouse stall", "cold crate", "display case", "ice shelf", "file chest", "vault niche"],
 "bar": ["mead bench", "backroom", "ember shelf", "whisper alcove", "lock brazier", "skald peg"],
 "inn": ["mead hall", "guest chamber", "dresser", "drawer", "coat closet", "hearth shelf"],
 "residence": ["kitchen", "bedroom", "closet", "bath nook", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer"],
 "business": ["reception", "clan office", "bathroom", "file chest", "utility room", "storage chest", "vault niche"],
 "alley": ["snow drift", "broken sled", "hidden alcove", "vendor stall", "service grate", "dumpster hollow", "alley crate", "runestone wall"],
 "street": ["market stall", "fountain pool", "sled post", "vendor stall", "display case", "back shelf", "message post", "mail hollow", "newsstand"],
 "arcane": ["ritual ring", "sigil cache", "enchanted chest", "altar niche", "rime rune"],
}

# SubLocation metadata definitions used when building locations.
SUBLOCATION_DEFS = {
 "longhouse stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A stall within a longhouse piled with furs, tools and salted goods.", "money_range": (3,24)},
 "cold crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A crate rimed in frost; something shifts when you nudge it.", "money_range": (2,20)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A glass case of carved bone trinkets and polished runes.", "money_range": (4,30)},
 "ice shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shelf dusted with rime holding small parcels.", "money_range": (0,12)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A chest of clan manifests and tally slips; a note peeks out.", "money_range": (2,22)},
 "vault niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A narrow niche sealed with iron and rime.", "money_range": (10,80)},

 "mead bench": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A bench where drinking vessels and coins collect.", "money_range": (1,14)},
 "backroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A cramped backroom smelling of tar and smoked fish.", "money_range": (1,12)},
 "ember shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shelf warmed by embers with tins and old tags.", "money_range": (1,12)},
 "whisper alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A narrow alcove where whispered bargains are left in ink.", "money_range": (2,18)},
 "lock brazier": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "An iron brazier concealing a small locked compartment.", "money_range": (4,30)},
 "skald peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A peg where skalds pin notices and scraps of verse.", "money_range": (0,10)},

 "mead hall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A communal hall ringed with benches and carved shields.", "money_range": (5,30)},
 "guest chamber": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A tidy chamber with furs and a loose floorboard hiding a scrap.", "money_range": (2,18)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A battered dresser with a stuck drawer — something rattles inside.", "money_range": (1,14)},
 "drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A shallow drawer with receipts and a folded token.", "money_range": (1,10)},
 "coat closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A closet of fur-lined coats; a pocket hides a scrap.", "money_range": (0,10)},
 "hearth shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A shelf above the hearth where charms and small tools rest.", "money_range": (1,12)},

 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A cold kitchen with jars of preserved meats and spice sachets.", "money_range": (1,12)},
 "bedroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A tight bedroom with piled furs and a coin tucked beneath.", "money_range": (1,12)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A narrow closet with fur-lined coats and a folded note.", "money_range": (0,8)},
 "bath nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A small bath nook warmed by steam; a tin hides below.", "money_range": (0,8)},
 "cupboard": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A cupboard of tins with a secret seam behind a jar.", "money_range": (0,8)},
 "pantry": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A pantry of dried rations with a wrapped sachet.", "money_range": (1,14)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A strapped chest with a faded maker's mark and something clinking inside.", "money_range": (2,20)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A small iron lockbox bolted beneath a shelf — heavy inside.", "money_range": (2,18)},

 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A reception desk with stamped passes and ledger slips.", "money_range": (1,14)},
 "clan office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cramped clan office of ledgers and seals.", "money_range": (2,18)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A chest of manifests and notes; a folded scrap peeks out.", "money_range": (2,22)},
 "utility room": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A small room of tools, rope and a bent key.", "money_range": (0,12)},

 "snow drift": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A drift of powder snow hiding lost trinkets and a crusted coin.", "money_range": (0,10)},
 "broken sled": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A splintered sled with a wrapped parcel tucked beneath.", "money_range": (1,16)},
 "hidden alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A tucked alcove between halls where contraband is stashed.", "money_range": (2,22)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A stall of smoked fish, furs and ironworks; a coin clinks loose.", "money_range": (2,18)},
 "service grate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A grated service slot used for deliveries and secret drops.", "money_range": (0,8)},
 "dumpster hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A hollow beneath boards where refuse and small finds mingle.", "money_range": (0,12)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A crate left in a narrow lane; straps are frost-brittle.", "money_range": (1,14)},
 "runestone wall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A wall carved with runes; a loose stone hides a token.", "money_range": (0,8)},

 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A bustling stall of salted meats, furs, and iron oddments.", "money_range": (4,28)},
 "fountain pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A carved pool half-frozen with coins glinting beneath the ice.", "money_range": (6,36)},
 "sled post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A post where sleds tie; a strap conceals a small pouch.", "money_range": (1,18)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A case of frost-polished curios; a tag slips loose.", "money_range": (2,20)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A back shelf behind a counter where receipts and small coins collect.", "money_range": (0,12)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A post of pinned notices; one envelope flutters free.", "money_range": (0,8)},
 "mail hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A hollowed mail post with frost-streaked letters and a stamped slip.", "money_range": (0,12)},
 "newsstand": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A piled newsstand of broadsheets and frost-notices.", "money_range": (1,16)},

 "ritual ring": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A ring of stones scarred with offerings of bone and shell.", "money_range": (4,40)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cache of engraved sigils humming with frost-power.", "money_range": (8,36)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "An enchanted chest that resists prying fingers unless coaxed.", "money_range": (10,60)},
 "altar niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A carved niche with rime-offerings and a tucked coin.", "money_range": (5,30)},
 "rime rune": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A rune etched into ice-smoothed stone; its grooves hold a tiny token.", "money_range": (0,20)},
}