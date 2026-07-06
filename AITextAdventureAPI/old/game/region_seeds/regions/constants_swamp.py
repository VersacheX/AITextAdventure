
REGION_SETTINGS = {
	"road_spacing": 20,
	"alley_spacing": 30,
	"alley_offset": 0,
	"max_size": 2100,
	"population_density": 0.2,
	"hasResidence": False,
	"hasBusiness": False,
	"hasShops": False,
	"hasBar": True,
	"hasInn": False,
	"hasHyperway": False,
	"hasOther1": False,
	"hasOther2": False,
	"display_name": "Down and Dirty Swamp",
	"region_name": "swamp",
}

OPEN_AREA_TILE = "░"
IMPASSABLE_TILE = "†"
IMPASSABLE_CHANCE = 0.10
OPEN_AREA_COLOR = "#5f6b3f"
IMPASSABLE_COLOR = "#3a3a28"

# Re-export common region assets so callers can import a single module
# Example: from game.region_seeds.constants_swamp import REGION_SETTINGS, BUILDINGS, RANDOM_HOSTILE_SEEDS
__all__ = [
 'REGION_SETTINGS',
 'BUILDINGS',
 'DRINK_MENU',
 'SUBLOC_MAP',
 'SUBLOCATION_DEFS',
 'RANDOM_HOSTILE_SEEDS',
 'RANDOM_HOSTILE_LINKS',
 "OPEN_AREA_TILE",
 "OPEN_AREA_COLOR",
 "IMPASSABLE_COLOR"
]
