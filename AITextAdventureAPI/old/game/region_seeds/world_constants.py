# POTENTIAL ADDITIONAL REGIONS: "volcanic", "jungle", "canyon"
AVAILABLE_REGIONS = ["desert", "forest", "mountains", "swamp", "grassland", "snow", "shallows" ]

AVAILABLE_CITIES = ["small_city", "mid_city", "large_city"]

CHAPTER_CITY_ORDER = [
    "desert_large_city",        # Chapter 1: The Desert Metropolis
    "forest_mid_city",          # Chapter 2: Boiling Bubble
    "grassland_mid_city",       # Chapter 3: Highsteeple Crossing
    "mountains_large_city",       # Chapter 4: Ironveil Foundry
    "shallows_large_city",        # Chapter 5: Brineward Harbor
    "snow_small_city",          # Chapter 6: Bleakwatch Outpost 
    "swamp_small_city",         # Chapter 7: Gnashwater Hollow 
    "desert_mid_city",        # Chapter 8: Nightveil Spire
    "desert_small_city",        # Chapter 9: The Radpost
    "grassland_large_city",     # Chapter 10: Crosswind Bazaar
    "shallows_mid_city",      # Chapter 11: Blackwake Bay
    "grassland_small_city",     # Chapter 12: Quantford Hollow
    "swamp_large_city",           # Chapter 13: The Necropolis
    "snow_mid_city",            # Chapter 14: Hailward Hold
    "shallows_small_city",      # Chapter 15: Tidekin Cove
    "forest_small_city",        # Chapter 16: Thornshade Hamlet
    "mountains_mid_city",     # Chapter 17: Gallows Rift
    "forest_large_city",        # Chapter 18: Aurelion Veil
    "snow_large_city",          # Chapter 19: Frostgate Spire
    "swamp_mid_city",         # Chapter 20: Bayou Nocturne
    "mountains_small_city",     # Chapter 21: Hollerforge Hollow
]

CONTINENT_COMPOSITION = [4, 3, 6, 2, 5, 1]

REGIONAL_NEIGHBORS = {
    "desert": ["grassland", "mountains", "desert","grassland", "mountains", "desert", "desert"],
    "forest": ["grassland", "swamp", "snow", "forest", "forest","grassland", "swamp", "snow", "forest"],
    "mountains": ["desert", "forest", "grassland", "snow", "mountains", "mountains"],
    "swamp": ["forest", "grassland", "shallows", "swamp", "swamp","forest", "grassland", "shallows", "swamp"],
    "grassland": ["desert", "forest", "mountains", "swamp", "snow", "shallows", "grassland", "grassland"],
    "snow": ["mountains", "grassland", "snow","mountains", "grassland", "snow", "snow"],
    "shallows": ["swamp", "grassland", "shallows", "shallows", "shallows"],
}

PATH_TILE_MAPPINGS = {
 # map connectivity mask (N=1, E=2, S=4, W=8) -> box-drawing char for roads
 # Single/double-line variants chosen to match comment examples
 "road": {
0: ' ',
1: '║',
2: '═',
3: '╚',
4: '║',
5: '║',
6: '╔',
7: '╠',
8: '═',
9: '╝',
10: '═',
11: '╩',
12: '╗',
13: '╦',
14: '╣',
15: '╬',
 },
 # single-line box drawing for alleys
 "alley": {
0: ' ',
1: '│',
2: '─',
3: '└',
4: '│',
5: '│',
6: '┌',
7: '├',
8: '─',
9: '┘',
10: '─',
11: '┴',
12: '┐',
13: '┬',
14: '┤',
15: '┼',
 }
}