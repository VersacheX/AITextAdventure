# LEVEL4 Abilities can have4 elements.
# There is1 ability per element combination and1 ability per ability type.
# An ability may have up to3 of the same element but diverse combinations are preferred.
# There must be a technique, a faith, a magic, a tech, and a skill ability for each element combination.
# Ability types are: technique, faith, magic, tech, skill
# elements are: fire, water, earth, air, light, dark, ice, electric
# Ability type mappings to character and hostile stats:
# technique: strength, constitution...physical attack, physical defense
# faith: intelligence, constitution...spiritual attack, spiritual defense; healing power; debuff power
# magic: intelligence...magical attack, magical defense; debuff power
# tech: intelligence, dexterity...tech attack, tech defense; debuff power
# skill: dexterity, strength...speed, critical hit rate; evasion
LEVEL_4_PLAYER_ABILITY_SEEDS = [
 {"id": "air_earth_technique_lv4_whirlwind", "name": "Whirlwind", "description": "Spin and strike multiple foes.", "ability_type": "technique", "level":4, "elements": ["air", "earth", "light", "water"], "base_power":55, "ap_cost":44, "effect": "damage", "can_aoe": False},
 {"id": "fire_technique_lv4_berserker_pulse", "name": "Berserker Pulse", "description": "A violent surge of energy that empowers attacks.", "ability_type": "technique", "level":4, "elements": ["fire", "fire", "earth", "electric"], "base_power":0, "ap_cost":75, "effect": "status", "status_keys": ["attack_buff", "elemental_attack_buff"], "can_aoe": True},
 
 {"id": "light_light_light_light_faith_lv4_pure_ascendance", "name": "Pure Ascendance", "description": "A concentrated beam of pure light that mends grievous wounds of a single ally.", "ability_type": "faith", "level":4, "elements": ["light", "light", "light", "light"], "base_power":120, "ap_cost":72, "effect": "heal", "can_aoe": False},
 {"id": "light_light_light_water_faith_lv4_prismatic_shower", "name": "Prismatic Shower", "description": "A broad shower of light and water that soothes and restores multiple allies.", "ability_type": "faith", "level":4, "elements": ["light", "light", "light", "water"], "base_power":50, "ap_cost":44, "effect": "heal", "can_aoe": True},
 {"id": "light_light_light_dark_faith_lv4_twilight_renaissance", "name": "Twilight Renaissance", "description": "A twilight rite that can restore life to a fallen ally (percentage-based revive).", "ability_type": "faith", "level":4, "elements": ["light", "light", "light", "dark"], "base_power":60, "ap_cost":175, "effect": "revive", "can_aoe": True},
 {"id": "light_light_light_dark_faith_lv4_renewed_life", "name": "Renewed Life", "description": "A rejuvenating light that brings a fallen ally back to life.", "ability_type": "faith", "level":4, "elements": ["light", "light", "fire", "water"], "base_power":120, "ap_cost":150, "effect": "revive", "can_aoe": False},
 {"id": "light_earth_faith_lv4_dawn_bulwark", "name": "Dawn Bulwark", "description": "Holy radiance to bolster defenses.", "ability_type": "faith", "level":4, "elements": ["light", "earth", "light", "water"], "base_power":0, "ap_cost":75, "effect": "status", "status_keys": ["elemental_defense_buff", "defense_buff"], "can_aoe": True},
 {"id": "light_air_earth_water_faith_lv4_starfall", "name": "Starfall", "description": "Celestial fragments rain down.", "ability_type": "faith", "level":4, "elements": ["light", "air", "earth", "water"], "base_power":135, "ap_cost":110, "effect": "damage", "can_aoe": False},
 {"id": "light_faith_lv4_solar_edge", "name": "Solar Edge", "description": "Light imbuement sharpens weapon precision.", "ability_type": "faith", "level":4, "elements": ["light", "light", "fire", "fire"], "base_power":0, "ap_cost":50, "effect": "status", "status_keys": ["elemental_attack_buff"], "can_aoe": True},

 {"id": "dark_magic_lv4_nightmare_echo", "name": "Nightmare Echo", "description": "A psychic backlash that erodes comprehension.", "ability_type": "magic", "level":4, "elements": ["dark", "air", "earth", "fire"], "base_power":1, "ap_cost":87, "effect": "status", "status_keys": ["intelligence_debuff", "elemental_debuff"], "can_aoe": True},
 {"id": "dark_magic_lv4_mind_shiver", "name": "Mind Shiver", "description": "A psychic twinge that makes strikes hesitant.", "ability_type": "magic", "level":4, "elements": ["dark", "dark", "air", "earth"], "base_power":0, "ap_cost":65, "effect": "status", "status_keys": ["attack_debuff", "dexterity_debuff"], "can_aoe": True},
 {"id": "dark_earth_air_magic_lv4_void_rupture", "name": "Void Rupture", "description": "A spear of pure nothingness.", "ability_type": "magic", "level":4, "elements": ["dark", "earth", "air", "dark"], "base_power":150, "ap_cost":110, "effect": "damage", "can_aoe": False},
 {"id": "water_air_dark_fire_magic_lv4_cataclysmic_maelstrom", "name": "Cataclysmic Maelstrom", "description": "A focused maelstrom burst into a point.", "ability_type": "magic", "level":4, "elements": ["water", "air", "dark", "fire"], "base_power":150, "ap_cost":110, "effect": "damage", "can_aoe": False},
 {"id": "earth_air_light_light_magic_lv4_sodom_and_gamora", "name": "Sodom and Gamora", "description": "Judgement is passed.  The wicked are turned to salt.", "ability_type": "magic", "level":4, "elements": ["earth","air","light","light"], "base_power":0, "ap_cost":200, "effect": "status", "status_keys": ["petrify"], "can_aoe": True},
]

from .level_4_abilities_by_type.tech import LEVEL_4_TECH_ABILITY_SEEDS
from .level_4_abilities_by_type.skill import LEVEL_4_SKILL_ABILITY_SEEDS
from .level_4_abilities_by_type.magic import LEVEL_4_MAGIC_ABILITY_SEEDS
from .level_4_abilities_by_type.technique import LEVEL_4_TECHNIQUE_ABILITY_SEEDS
from .level_4_abilities_by_type.faith import LEVEL_4_FAITH_ABILITY_SEEDS

LEVEL_4_PLAYER_ABILITY_SEEDS += LEVEL_4_TECH_ABILITY_SEEDS
LEVEL_4_PLAYER_ABILITY_SEEDS += LEVEL_4_SKILL_ABILITY_SEEDS
LEVEL_4_PLAYER_ABILITY_SEEDS += LEVEL_4_MAGIC_ABILITY_SEEDS
LEVEL_4_PLAYER_ABILITY_SEEDS += LEVEL_4_TECHNIQUE_ABILITY_SEEDS
LEVEL_4_PLAYER_ABILITY_SEEDS += LEVEL_4_FAITH_ABILITY_SEEDS