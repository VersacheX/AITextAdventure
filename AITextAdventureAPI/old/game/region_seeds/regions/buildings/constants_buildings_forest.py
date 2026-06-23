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
	{ "name": "bar", "display_name": "The Woodlands Lush", "type": "bar", "char": "µ", "seed_range":60, "threshold":0.03, "hostile_prob":0.4, "can_buy": True, "can_sell": False, "image": "/assets/tiles/bar.svg", "color": "#8b3e3e"},
]

# Internal sublocations per subtype
SUBLOC_MAP = {
 "bar": ["phone booth", "gun safe", "barrel stash", "pool table", "backroom safe"],
 "alley": ["vehicle", "hiker cache", "trash pile", "hunter blind", "fallen tent"],
 "street": ["vehicle", "old signpost", "bridge", "forest kiosk"],
 "open_area": ["mossy rock", "hollow tree", "berry bush", "creek pool", "abandoned campsite", "stump", "root cellar", "mushroom patch"],
}

# Forest-themed searchables
SUBLOCATION_DEFS = {
 "phone booth": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A battered phone booth with moss at the base and old flyers tucked into cracks.", "money_range": (0,6)},
 "gun safe": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.03, "prompt": "A heavy safe tucked behind a bar shelf; it's rusted but might still open.", "money_range": (20,120)},
 "barrel stash": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A set of wooden barrels behind the bar; someone may have hidden goods inside.", "money_range": (0,20)},
 "pool table": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.07, "prompt": "A neglected pool table; coins and small trinkets collect under the felt.", "money_range": (0,8)},
 "backroom safe": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A locked safe and a few ledgers piled on top - someone kept valuables here.", "money_range": (10,80)},

 "vehicle": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.16, "prompt": "An overturned or abandoned vehicle half-swallowed by undergrowth.", "money_range": (1,5)},
 "hiker cache": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A small cache hidden beneath leaves with canned goods and a few coins.", "money_range": (0,20)},
 "trash pile": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.20, "prompt": "A pile of discarded bottles and wrappers; people sometimes toss away useful things.", "money_range": (0,4)},
 "hunter blind": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A camouflaged blind with tarps and a small cache of hunting supplies.", "money_range": (0,12)},
 "fallen tent": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "An old tent ripped by wind; a rucksack might still contain something.", "money_range": (0,15)},

 "old signpost": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "A weathered signpost with nails and a small tin box behind it.", "money_range": (0,10)},
 "bridge": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A wooden bridge spanning a creek; the underside hides lost items.", "money_range": (0,12)},
 "forest kiosk": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.07, "prompt": "An informational kiosk with a loose cashbox or a map sleeve containing notes.", "money_range": (0,20)},

 "mossy rock": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.08, "prompt": "A cluster of moss-covered stones with small crevices; someone might have hidden a trinket.", "money_range": (0,8)},
 "hollow tree": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.09, "prompt": "A large hollow tree trunk; perfect for hiding a small cache or note.", "money_range": (0,12)},
 "berry bush": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.12, "prompt": "A cluster of edible berries; some locals stash small items beneath leaves.", "money_range": (0,6)},
 "creek pool": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.10, "prompt": "A clear pool in a creek where travelers washed gear; coins sometimes glint below.", "money_range": (0,15)},
 "abandoned campsite": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.14, "prompt": "Cold campfire rings and overturned crates - someone left in haste.", "money_range": (1,25)},
 "stump": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.06, "prompt": "A wide tree stump with beetle holes and cracked bark; small items can be wedged in.", "money_range": (0,8)},
 "root cellar": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.05, "prompt": "An old root cellar door half-buried in earth; it may hold preserved goods or supplies.", "money_range": (5,40)},
 "mushroom patch": {"mode": "searchable", "level_delta":0, "searchable": True, "loot_chance":0.07, "prompt": "A patch of mushrooms; some are edible and others hide sprouting truffles or roots.", "money_range": (0,10)},
}