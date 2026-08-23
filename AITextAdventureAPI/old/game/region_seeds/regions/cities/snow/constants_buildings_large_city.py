CITY_NAME = "Frostgate Spire"
CITY_DESCRIPTION = (
	"Frostgate Spire is a towering city of ice and steel, "
	"rising majestically from the frozen tundra. Its spires and "
	"turrets glisten with frost, reflecting the pale light of the "
	"northern sun. The city is a bustling hub of trade and culture, "
	"where merchants from distant lands converge to barter goods and "
	"stories. The streets are lined with shops and taverns, their "
	"windows aglow with warm light against the cold. Despite the "
	"harsh climate, Frostgate Spire is a place of vibrant life and "
	"endless adventure."
)

# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified
# heal_fraction <- fraction of max HP restored <- do not modify
ROOM_MENU = [
	{"id": "public", "name": "Plaza Bench", "value":10, "heal_fraction":0.25},
	{"id": "economy", "name": "Cold Chamber", "value":48, "heal_fraction":0.75},
	{"id": "luxury", "name": "Spire Suite", "value":360, "heal_fraction":1.0},
]

# Drinks Menu
DRINK_MENU = [
	{"id": "tiny", "name": "Frost Ale", "value":14, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
	{"id": "small", "name": "Glacier Mead", "value":32, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
	{"id": "mid", "name": "Bluefire Cocktail", "value":78, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
	{"id": "big", "name": "Lantern Elixir", "value":170, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
	{"id": "huge", "name": "Aether Draught", "value":380, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":7},
	{"id": "max", "name": "Spire Serum", "value":760, "hp_fraction":1.00, "ap_fraction":0.30, "min_level":10},
]

# Buildings
BUILDINGS = [
	{ "name": "bar", "display_name": "The Blue Lantern", "type": "bar", "char": "µ", "seed_range":7, "threshold":0.06, "hostile_prob":0.36, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#5b7b8b"},
	{ "name": "inn", "display_name": "Hearth of Frost", "type": "inn", "char": "@", "seed_range":12, "threshold":0.10, "hostile_prob":0.02, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#5b7b8b"},
	{ "name": "shopweapons", "display_name": "Rivet & Ice", "type": "shop", "char": "Æ", "seed_range":15, "threshold":0.24, "hostile_prob":0.06, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#6b3b47"},
	{ "name": "shopitems", "display_name": "Frostworks Emporium", "type": "shop", "char": "₨", "seed_range":15, "threshold":0.42, "hostile_prob":0.05, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#3b5b6b"},
	{ "name": "shoparmor", "display_name": "Scale & Pelt", "type": "shop", "char": "¥", "seed_range":15, "threshold":0.60, "hostile_prob":0.05, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#606f7b"},
	{ "name": "residencelarge", "display_name": "Spireholds", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.88, "hostile_prob":0.04, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#dfeef5"},
	{ "name": "residencesmall", "display_name": "Snowrows", "type": "residence", "char": "î", "seed_range":4, "threshold":0.96, "hostile_prob":0.14, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#e8f0f5"},
	{ "name": "businesslarge", "display_name": "Clime Exchange", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.99, "hostile_prob":0.03, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#5b6b7b"},
	{ "name": "businesssmall", "display_name": "Ledger Spindles", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.04, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#7b8b8b"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "The Glacial Concordium", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#7b30a2" }, 
	{ "name": "other2", "display_name": "Frostlight Artificer’s Annex", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#7b30a2" }
]

# Sublocation mapping
SUBLOC_MAP = {
 "shop": ["cold vault", "frozen crate", "display case", "ice shelf", "file chest", "vault niche"],
 "bar": ["tap shelf", "hearth alcove", "ember shelf", "bench row", "lock brazier", "whisper arch"],
 "inn": ["common hall", "guest chamber", "dresser", "trunk drawer", "coat closet", "hearth niche"],
 "residence": ["kitchen", "bedroom", "closet", "bath nook", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer"],
 "business": ["reception", "office", "wash nook", "file chest", "utility room", "storage chest", "vault niche"],
 "alley": ["snow drift", "broken sled", "hidden alcove", "vendor stall", "service grate", "dumpster hollow", "alley crate", "frosted wall"],
 "street": ["market stall", "fountain pool", "sled post", "vendor stall", "display case", "back shelf", "message post", "mail hollow", "newsstand"],
 "arcane": ["ritual ring", "sigil cache", "enchanted chest", "altar niche", "frost rune"],
 "works": ["forge pit", "engine room", "vent shaft", "grate panel", "oil drum"],
}

# SubLocation metadata definitions used when building locations.
SUBLOCATION_DEFS = {
 "cold vault": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A chamber of frost-sealed boxes and chilled receipts.", "money_range": (4,32)},
 "frozen crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.24, "prompt": "A crate rimed with ice; something moves inside when you tap it.", "money_range": (2,30)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A glass case of frost-polished trinkets and engraved charms.", "money_range": (6,36)},
 "ice shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shelf rimed in hoarfrost holding small parcels.", "money_range": (0,12)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A chest of ledgers and blueprints dusted in ice crystals.", "money_range": (2,26)},
 "vault niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A narrow niche sealed with iron and rime.", "money_range": (12,100)},

 "tap shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shelf behind the taps where frosted coins gather.", "money_range": (1,14)},
 "hearth alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "An alcove warmed by a small hearth; notes hide in the mortar.", "money_range": (2,18)},
 "ember shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A shelf warmed by embers with tins and old tags.", "money_range": (1,12)},
 "bench row": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A row of benches carved from driftwood where coins lodge.", "money_range": (0,8)},
 "lock brazier": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "An iron brazier concealing a frost-sealed compartment.", "money_range": (4,40)},
 "whisper arch": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A narrow arch where whispered notes and bribes are passed.", "money_range": (2,18)},
 
 "common hall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A smoky hall hung with banners of white and iron.", "money_range": (6,34)},
 "guest chamber": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A tidy chamber with a loose floorboard hiding a note.", "money_range": (2,20)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A battered dresser with a sticky drawer — something rattles inside.", "money_range": (1,14)},
 "trunk drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A travel trunk with maps and a sealed pouch.", "money_range": (3,24)},
 "coat closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A closet of heavy pelts; a pocket hides a scrap.", "money_range": (0,10)},
 "hearth niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A niche by the hearth where charms and small tools rest.", "money_range": (1,12)},
 
 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A cold kitchen with jars of preserved meats and spice sachets.", "money_range": (1,12)},
 "bedroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A tight bedroom with piled furs and a coin tucked beneath.", "money_range": (1,12)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A narrow closet with fur-lined coats and a sealed note.", "money_range": (0,8)},
 "bath nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A bath nook warmed by steam; a small tin hides below.", "money_range": (0,8)},
 "cupboard": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A cupboard of tins with a hidden seam behind a jar.", "money_range": (0,8)},
 "pantry": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A pantry of dried rations with a wrapped sachet.", "money_range": (1,14)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A strapped chest with a faded maker's mark and something clinking inside.", "money_range": (2,20)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A small iron lockbox bolted beneath a shelf — heavy inside.", "money_range": (2,18)},
 
 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A reception desk with stamped passes and ledger slips.", "money_range": (1,14)},
 "office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cramped office of ledgers, blueprints and frost-scratched notes.", "money_range": (2,26)},
 "utility room": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A small room of tools, rope and a bent key.", "money_range": (0,12)},
 
 "snow drift": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A drift of powder snow hiding lost trinkets and a crusted coin.", "money_range": (0,10)},
 "broken sled": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A splintered sled with a wrapped parcel tucked beneath.", "money_range": (1,16)},
 "hidden alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A tucked alcove between spires where contraband is stashed.", "money_range": (2,22)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A stall of smoked fish, furs and cold-weather wares; a coin clinks loose.", "money_range": (2,18)},
 "service grate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A grated service slot used for deliveries and secret drops.", "money_range": (0,8)},
 "dumpster hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A hollow beneath boards where refuse and small finds mingle.", "money_range": (0,12)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A crate left in a narrow lane; straps are frost-brittle.", "money_range": (1,14)},
 "frosted wall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A wall glazed with rime; one chip reveals something small.", "money_range": (0,8)},
 
 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A bustling stall of salted meats, furs, and mechanical oddments.", "money_range": (4,30)},
 "fountain pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A carved pool half-frozen with coins glinting beneath the ice.", "money_range": (6,40)},
 "sled post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A post where sleds tie; a strap conceals a small pouch.", "money_range": (1,18)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A case of frost-polished curios; a tag slips loose.", "money_range": (2,20)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A back shelf behind a counter where receipts and small coins collect.", "money_range": (0,12)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A post of pinned notices; one envelope flutters free.", "money_range": (0,8)},
 "mail hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A hollowed mail post with frost-streaked letters and a stamped slip.", "money_range": (0,12)},
 "newsstand": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A piled newsstand of broadsheets and frost-notices.", "money_range": (1,16)},

 "ritual ring": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A ring of stones scarred with offerings of bone and shell.", "money_range": (4,40)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cache of engraved sigils humming with cold power.", "money_range": (8,36)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "An enchanted chest that resists prying fingers unless coaxed.", "money_range": (10,60)},
 "altar niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A carved niche with offerings of rime and a tucked coin.", "money_range": (5,30)},
 "frost rune": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A rune etched into ice-smoothed stone; its grooves hold a tiny token.", "money_range": (0,20)},
}