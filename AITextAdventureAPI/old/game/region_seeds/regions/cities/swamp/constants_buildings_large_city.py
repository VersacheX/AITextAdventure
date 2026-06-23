CITY_NAME = "The Necropolis"
CITY_DESCRIPTION = (
	"A sprawling city of the dead, where ancient crypts and mausoleums rise from the misty swamplands. "
	"Shrouded in perpetual twilight, the Necropolis is a labyrinth of narrow canals, moss-covered stone pathways, "
	"and towering obelisks that pierce the foggy sky. The air is thick with the scent of damp earth and decaying foliage, "
	"and the distant echoes of mournful chants and rustling leaves create an eerie symphony. "
	"Residents clad in tattered robes and bone jewelry navigate the shadowy streets, trading in relics of the past "
	"and practicing ancient rites to commune with the spirits that linger in this haunted city."
)

# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency <- can be modified
# heal_fraction <- fraction of max HP restored <- do not modify
ROOM_MENU = [
	{"id": "public", "name": "Mire Bench", "value":6, "heal_fraction":0.25},
	{"id": "economy", "name": "Grave Loft", "value":28, "heal_fraction":0.75},
	{"id": "luxury", "name": "Seer's Suite", "value":180, "heal_fraction":1.0},
]

# Simple in-bar drinks menu. Effects are immediate and don't create inventory items.
# id <- defined type <- do not modify
# name <- display name <- can be modified
# value <- cost in game currency  <- can be modified slightly... bigger drinks are naturally more expensive as buying a drink triggers rng for an enemy, so buying small doesn't pay
# hp_fraction <- fraction of max HP restored immediately <- do not modify
DRINK_MENU = [
	{"id": "tiny", "name": "Mire Ale", "value":9, "hp_fraction":0.10, "ap_fraction":0.00, "min_level":1},
	{"id": "small", "name": "Bog Mead", "value":22, "hp_fraction":0.20, "ap_fraction":0.00, "min_level":1},
	{"id": "mid", "name": "Swamp Grog", "value":52, "hp_fraction":0.35, "ap_fraction":0.00, "min_level":2},
	{"id": "big", "name": "Lantern Elixir", "value":120, "hp_fraction":0.55, "ap_fraction":0.00, "min_level":4},
	{"id": "huge", "name": "Necrotic Draught", "value":280, "hp_fraction":0.80, "ap_fraction":0.00, "min_level":6},
	{"id": "max", "name": "Mort Serum", "value":520, "hp_fraction":1.00, "ap_fraction":0.30, "min_level":9},
]

# Buildings
BUILDINGS = [
	{ "name": "bar", "display_name": "The Sluice & Skull", "type": "bar", "char": "µ", "seed_range":6, "threshold":0.06, "hostile_prob":0.35, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#3b2f2f"},
	{ "name": "inn", "display_name": "Mirehold Rest", "type": "inn", "char": "@", "seed_range":12, "threshold":0.10, "hostile_prob":0.05, "can_buy": True, "can_sell": False, "image": "/assets/tiles/inn.svg", "color": "#4b3b3b"},
	{ "name": "shopweapons", "display_name": "Boneworks & Blades", "type": "shop", "char": "Æ", "seed_range":16, "threshold":0.22, "hostile_prob":0.08, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#6b3b2f"},
	{ "name": "shopitems", "display_name": "Vial & Talisman", "type": "shop", "char": "₨", "seed_range":16, "threshold":0.40, "hostile_prob":0.06, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#2f4b3b"},
	{ "name": "shoparmor", "display_name": "Hide & Husk", "type": "shop", "char": "¥", "seed_range":16, "threshold":0.58, "hostile_prob":0.06, "can_buy": True, "can_sell": True, "image": "/assets/tiles/shop.svg", "color": "#575757"},
	{ "name": "residencelarge", "display_name": "Crypt Quarters", "type": "residence", "char": "Î", "seed_range":6, "threshold":0.82, "hostile_prob":0.04, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#c8c8c8"},
	{ "name": "residencesmall", "display_name": "Bog Shacks", "type": "residence", "char": "î", "seed_range":4, "threshold":0.96, "hostile_prob":0.14, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#dfe7d0"},
	{ "name": "businesslarge", "display_name": "Mortuary Exchange", "type": "business", "char": "Ï", "seed_range":6, "threshold":0.98, "hostile_prob":0.04, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_large.svg", "color": "#5b5b5b"},
	{ "name": "businesssmall", "display_name": "Ledger of Wights", "type": "business", "char": "ï", "seed_range":4, "threshold":1.0, "hostile_prob":0.05, "can_buy": False, "can_sell": False, "image": "/assets/tiles/residence_small.svg", "color": "#6b6b5b"},
	{ "name": "hyperway", "display_name": "The Hyperway", "type": "hyperway", "char": "Ṣ", "seed_range": 1000, "threshold": 0.02, "hostile_prob": 0.3, "can_buy": False, "can_sell": False, "image": "/assets/tiles/hyperway.svg", "color": "#707070" }, 
	{ "name": "other1", "display_name": "The Ossuary Concord", "type": "other1", "char": "O", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other1.svg", "color": "#4b0082" }, 
	{ "name": "other2", "display_name": "Veil‑Whisper Reliquary", "type": "other2", "char": "0", "seed_range": 1000, "threshold": 0.06, "hostile_prob": 0.25, "can_buy": False, "can_sell": False, "image": "/assets/tiles/other2.svg", "color": "#4b0082" }
]

# Internal sublocations per subtype
#  Used when generating buildings to add searchable sublocations.
SUBLOC_MAP = {
 "shop": ["workbench", "jar shelf", "display case", "shelf unit", "file chest", "vault niche"],
 "bar": ["stump bench", "backroom glade", "ember shelf", "whisper nook", "lock brazier", "notice peg"],
 "inn": ["common bunk", "guest bunk", "dresser", "drawer", "coat peg", "hearth nook"],
 "residence": ["kitchen", "bunkroom", "closet", "wash basin", "cupboard", "pantry", "dresser", "storage chest", "lockbox", "drawer"],
 "business": ["reception", "mort office", "bathroom", "file chest", "utility alcove", "storage chest", "vault niche"],
 "alley": ["muck pool", "half-buried coffin", "hidden culvert", "vendor stall", "service hatch", "dumpster hollow", "alley crate", "ghoul-scar wall"],
 "street": ["market stall", "drain pool", "cart post", "vendor stall", "display case", "back shelf", "message post", "mail hollow", "newsleaf"],
 "arcane": ["ritual ring", "sigil cache", "enchanted chest", "altar niche", "necrotic rune"],
 "works": ["bone forge", "engine room", "vent shaft", "grate panel", "oil drum"],
}

# SubLocation metadata definitions used when building locations.
# Each entry provides defaults used by the generator and later logic (searchable, loot chance, prompt, etc.).
SUBLOCATION_DEFS = {
 "workbench": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A blood-splashed workbench with tools and brittle bone fragments.", "money_range": (2,20)},
 "jar shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A shelf of glass jars filled with murky reagents and tags.", "money_range": (1,18)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A glass case of odd trinkets, teeth and polished talons.", "money_range": (3,24)},
 "shelf unit": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A crowded shelf unit of tins, bones and stitched scraps.", "money_range": (0,12)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A chest of ledgers and death-roll slips; a folded note peeks out.", "money_range": (2,26)},
 "vault niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A water-sealed niche behind rotting planks and iron.", "money_range": (12,120)},

 "stump bench": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A moss-covered stump bench where locals hide small coins.", "money_range": (0,10)},
 "backroom glade": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A damp backroom overgrown with fungus and whispered deals.", "money_range": (2,18)},
 "ember shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shelf warmed by a dim brazier with vials and notes.", "money_range": (1,14)},
 "whisper nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A cramped nook where secrets are left in folded skins.", "money_range": (1,16)},
 "lock brazier": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "An iron brazier concealing a rusted locked compartment.", "money_range": (4,36)},
 "notice peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A peg with pinned warnings and a salted envelope.", "money_range": (0,12)},

 "common bunk": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shared bunk with scratched names and tucked notes.", "money_range": (1,14)},
 "guest bunk": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A guest bunk with a loose board hiding a small pouch.", "money_range": (2,18)},
 "dresser": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A damp dresser with a stuck drawer — something rattles inside.", "money_range": (1,12)},
 "drawer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A shallow drawer with brittle receipts and a faded scrap.", "money_range": (1,10)},
 "coat peg": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A peg with a moldy coat; the pocket hides a scrap.", "money_range": (0,8)},
 "hearth nook": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A nook by a smoldering hearth where charms and tools rest.", "money_range": (1,12)},

 "kitchen": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A greasy kitchen with jars of pickled weirdness and a hidden sachet.", "money_range": (1,14)},
 "bunkroom": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A crowded bunkroom where scraps and trinkets accumulate.", "money_range": (1,12)},
 "closet": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A narrow closet with oil-stained rags and a sealed note.", "money_range": (0,8)},
 "wash basin": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A basin where grime gathers; something clings beneath.", "money_range": (0,8)},
 "cupboard": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A cupboard of jars with a secret seam behind a tin.", "money_range": (0,8)},
 "pantry": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A pantry of dried rations and strange roots with a tucked sachet.", "money_range": (1,14)},
 "storage chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "An old chest tied with sea-rope; a metallic clink echoes within.", "money_range": (2,20)},
 "lockbox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A small iron lockbox bolted to a shelf — heavy with secrets.", "money_range": (2,20)},

 "reception": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A weathered reception desk with death-roll slips and ledger tags.", "money_range": (1,14)},
 "mort office": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A cramped mortuary office with ledgers and bone tags.", "money_range": (2,22)},
 "file chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A chest of manifests and death notices; a folded scrap peeks out.", "money_range": (2,22)},
 "utility alcove": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "An alcove of tools, coils and a bent key.", "money_range": (0,10)},

 "muck pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A stagnant pool of muck where glints of metal sometimes show.", "money_range": (0,12)},
 "half-buried coffin": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A coffin half-swallowed by silt; something taps from within.", "money_range": (1,20)},
 "hidden culvert": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A narrow culvert where contraband and old tokens are hidden.", "money_range": (2,24)},
 "vendor stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A stall of pickled oddments and reconstituted wares; a coin rolls free.", "money_range": (2,20)},
 "service hatch": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A rusted service hatch used for deliveries and secret drops.", "money_range": (0,8)},
 "dumpster hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "A hollow beneath planks where refuse and odd finds gather.", "money_range": (0,12)},
 "alley crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "A crate left in a lane; straps are waterlogged and frayed.", "money_range": (1,14)},
 "ghoul-scar wall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A wall etched with warning sigils and claw marks; a loose chip hides a token.", "money_range": (0,10)},

 "market stall": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A busy stall of pickled fish, reconstituted trinkets and odd bait.", "money_range": (4,32)},
 "drain pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A shallow drain pool where coins and shells collect among the muck.", "money_range": (4,24)},
 "cart post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A post where carts tie; a strap hides a small pouch.", "money_range": (1,18)},
 "display case": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A case of rewashed curios; one tag slips loose.", "money_range": (2,22)},
 "back shelf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A back shelf where notes and small coins settle in dust.", "money_range": (0,12)},
 "message post": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A post of pinned notices; one salted envelope flutters free.", "money_range": (0,8)},
 "mail hollow": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A hollowed mail post with damp letters and a salted stamp.", "money_range": (0,12)},
 "newsleaf": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A folded broadsheet with a scrawled ad tucked inside.", "money_range": (0,10)},

 "ritual ring": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A ring of stones scored with offerings and dark ash.", "money_range": (4,40)},
 "sigil cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cache of carved sigils humming with stale power.", "money_range": (8,36)},
 "enchanted chest": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "An enchanted chest that resists prying unless placated.", "money_range": (10,60)},
 "altar niche": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A carved niche with offerings and a tucked coin.", "money_range": (5,30)},
 "necrotic rune": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A rune carved into bogstone; its grooves hide a tiny token.", "money_range": (0,24)},

 # works
 "bone forge": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A forge for rebinding bone and metal — sparks stick to the air.", "money_range": (4,40)},
 "engine room": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cluttered engine room of pumps and rusted valves.", "money_range": (6,36)},
 "vent shaft": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A narrow shaft of warm, stale air; something shiny is wedged in the grille.", "money_range": (1,18)},
 "grate panel": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A loose grate panel — reach in carefully.", "money_range": (1,18)},
 "oil drum": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A dented drum of oil; a small tin rattles inside.", "money_range": (0,12)},
}