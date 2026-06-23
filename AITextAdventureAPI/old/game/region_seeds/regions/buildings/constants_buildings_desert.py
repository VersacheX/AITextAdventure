# Simple in-bar drinks menu. Effects are immediate and don't create inventory items.
DRINK_MENU = [
 {"id": "ale", "name": "Ale", "value":10, "hp_fraction":0.10, "ap_fraction":0.0, "min_level":1},
 {"id": "stout", "name": "Stout", "value":25, "hp_fraction":0.20, "ap_fraction":0.0, "min_level":2},
 {"id": "cocktail", "name": "Cocktail", "value":50, "hp_fraction":0.30, "ap_fraction":0.0, "min_level":3},
 {"id": "porter", "name": "Porter", "value":65, "hp_fraction":0.40, "ap_fraction":0.0, "min_level":4},
 {"id": "rum", "name": "Rum", "value":80, "hp_fraction":0.50, "ap_fraction":0.0, "min_level":5},
 {"id": "brandy", "name": "Brandy", "value":110, "hp_fraction":0.60, "ap_fraction":0.0, "min_level":6},
 {"id": "whiskey", "name": "Whiskey", "value":120, "hp_fraction":0.70, "ap_fraction":0.0, "min_level":7},
 {"id": "cognac", "name": "Cognac", "value":130, "hp_fraction":0.80, "ap_fraction":0.0, "min_level":8},
 {"id": "absinthe", "name": "Absinthe", "value":140, "hp_fraction":0.90, "ap_fraction":0.0, "min_level":9},
 {"id": "elixir", "name": "Elixir", "value":200, "hp_fraction":1.00, "ap_fraction":0.3, "min_level":10},
]

BUILDINGS = [
	{ "name": "bar", "display_name": "Down n Dirty", "type": "bar", "char": "µ", "seed_range":60, "threshold":0.03, "hostile_prob":0.4, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#8b3e3e"},
]

# Internal sublocations per subtype
SUBLOC_MAP = {
 "bar": ["phone booth", "gun safe", "pool table", "backroom safe", "bottle rack", "jukebox"],
 "alley": ["vehicle", "phone booth", "trash pile", "looted shack", "abandoned camp"],
 "street": ["vehicle", "phone booth", "truck trailer", "rest stop kiosk", "old signpost", "collapsed overpass"],
 "open_area": ["vehicle", "sand dune cache", "buried crate", "skeleton remains", "rusted well", "cactus grove", "rock formation", "dry riverbed", "water tank", "mining shaft entrance", "service box"],
}

# More neo-noir / desert searchables
SUBLOCATION_DEFS = {
 "phone booth": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A cracked phone booth with graffiti and folded notes wedged under the receiver.", "money_range": (0,6)},
 "gun safe": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "A heavy gun safe bolted to the floor; the combination is long lost, but worth trying.", "money_range": (20,120)},
 "vehicle": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.17, "prompt": "An abandoned vehicle.", "money_range": (1,3)},

 "pool table": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A sticky pool table; loose change and an occasional hidden item can be found beneath the cloth.", "money_range": (0,8)},
 "backroom safe": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "The bar's backroom; a small safe sits in the corner under oil-stained boxes.", "money_range": (10,80)},
 "bottle rack": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A rickety bottle rack. Some bottles are worth more than their contents.", "money_range": (0,12)},
 "jukebox": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.03, "prompt": "An old jukebox with a coin slot; there might be a hidden compartment inside.", "money_range": (0,25)},

 "trash pile": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.22, "prompt": "A wet, reeking pile of trash and broken crates; scavengers sometimes miss useful scraps.", "money_range": (0,4)},
 "looted shack": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.15, "prompt": "A shoddy shack with signs of recent habitation; pockets might contain coin or small items.", "money_range": (2,20)},
 "abandoned camp": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.18, "prompt": "Charred camp remains and overturned crates; someone left in a hurry.", "money_range": (1,15)},

 "truck trailer": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "A rusting truck trailer sits half off the highway; cargo may remain inside.", "money_range": (5,60)},
 "rest stop kiosk": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A battered kiosk with faded maps and a loose register drawer.", "money_range": (0,30)},
 "old signpost": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "An old signpost points to towns long gone; a small tin box may be nailed behind it.", "money_range": (0,10)},
 "collapsed overpass": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.07, "prompt": "Rubble from a collapsed overpass; cavities hide odd items and occasional coin.", "money_range": (1,25)},

 "sand dune cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A patch of disturbed sand conceals a small cache—someone hid supplies here.", "money_range": (0,40)},
 "buried crate": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "Half-buried wooden crate; it might contain tradeable goods if the lock hasn't rotted away.", "money_range": (5,80)},
 "skeleton remains": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "The bleached skeleton of a traveler; pockets may contain a coin or trinket.", "money_range": (0,12)},
 "rusted well": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "An old well with a rusted pump; a bucket may contain hidden items.", "money_range": (0,20)},
 "cactus grove": {"mode": "searchable", "level_delta":0, "searchable": False, "loot_chance":0.03, "prompt": "A stand of barrel cacti; water and odd items can sometimes be found in hollowed trunks.", "money_range": (0,6)},
 "rock formation": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "Wind-polished rocks and crevices; someone may have stashed a small item here.", "money_range": (0,10)},
 "dry riverbed": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.11, "prompt": "A winding dry riverbed where debris collects—good place to find lost goods.", "money_range": (0,15)},
 "water tank": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "An abandoned water tank—rusted access panels sometimes hide small caches.", "money_range": (0,30)},
 "mining shaft entrance": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.07, "prompt": "A collapsed mine mouth; loose timbers and crates suggest someone once worked here.", "money_range": (2,50)},
 "service box": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.04, "prompt": "A utility service box with spare change and loose wiring—dangerous but sometimes rewarding.", "money_range": (0,20)},
}
