"""
MAGIC ABILITIES  ARE  BASED ON INTELLIGENCE STAT.
they should be offensive magic attacks, or damage over time effects... possible status effects
they have high power but also high ap cost
some lore for magic in a neo noir fantasy setting is created with these abilities


----------------------- level 2 seeding layout -----------------------
35 Ability possibilities

ABILITY DIVISION
 DAMAGE: electric-fire,electric-light,electric-dark,electric-ice,ice-water,ice-earth,ice-light,ice-dark,fire-earth,fire-air,fire-light,earth-water,earth-light,air-water,air-light,water-light
   -- base_power: 32-38 ap_cost: 25-30
 DAMAGE AOE: electric-electric, ice-ice, light-light, dark-dark, water-water, earth-earth, fire-fire, air-air
    -- base_power: 28-32 ap_cost: 30-35
 CONTINUOUS DAMAGE: electric-water, electric-earth, light-dark, earth-air, ice-fire, fire-water, ice-air
    -- base_power: 1-3 ap_cost: 30-35
 CONTINUOUS DAMAGE AOE: fire-dark, water-dark, air-dark, electric-air, earth-dark
    -- base_power: 0 ap_cost: 30

----------------------- level 3 seeding layout -----------------------
120 Ability possibilities -- we will only use so many
8x-pure_color: fire_fire_fire, water_water_water, earth_earth_earth, air_air_air, light_light_light, dark_dark_dark, ice_ice_ice, electric_electric_electric
6x-enemies: fire_ice_air, ice_air_earth, air_earth_electric, earth_electric_water, electric_water_fire, water_fire_ice
2x-allies: ice_earth_water, air_electric_fire
6x-dark+enemies: dark_fire_ice, dark_ice_air, dark_air_earth, dark_earth_electric, dark_electric_water, dark_water_fire
DAMAGE:use 6x dark+enemies -- base_power: 90-100 ap_cost: 60-70
DAMAGE AOE: use 8x pure color -- base_power: 80-90 ap_cost: 90-100
CONTINUOUS DAMAGE: 6x enemies -- base_power: 8-15 ap_cost: 60-65
CONTINUOUS DAMAGE AOE: 2x allies -- base_power: 0 ap_cost: 75
"""

# Magic seeds extracted from level_3_player_ability_seeds
LEVEL_3_MAGIC_SEEDS = [
      ##DAMAGE
    {"id": "dark_fire_ice_magic_lv3_flame_wraith", "name": "Flame Wraith", "description": "A burning specter that scorches and chills.", "ability_type": "magic", "level":3, "elements": ["dark", "fire", "ice"], "base_power":95, "ap_cost":85, "effect": "damage", "can_aoe": False},
    {"id": "dark_ice_air_magic_lv3_frost_bite", "name": "Frost Bite", "description": "A chilling gust that freezes and numbs.", "ability_type": "magic", "level":3, "elements": ["dark", "ice", "air"], "base_power":95, "ap_cost":85, "effect": "damage", "can_aoe": False},
    {"id": "dark_air_earth_magic_lv3_shadow_quake", "name": "Shadow Quake", "description": "A tremor of darkness that unsettles and shatters.", "ability_type": "magic", "level":3, "elements": ["dark", "air", "earth"], "base_power":100, "ap_cost":90, "effect": "damage", "can_aoe": False},
    {"id": "dark_earth_electric_magic_lv3_void_shock", "name": "Void Shock", "description": "A jolt of shadowy energy that disrupts and drains.", "ability_type": "magic", "level":3, "elements": ["dark", "earth", "electric"], "base_power":95, "ap_cost":85, "effect": "damage", "can_aoe": False},
    {"id": "dark_electric_water_magic_lv3_night_tide", "name": "Night Tide", "description": "A wave of dark energy that drowns and confuses.", "ability_type": "magic", "level":3, "elements": ["dark", "electric", "water"], "base_power":90, "ap_cost":85, "effect": "damage", "can_aoe": False},
    {"id": "dark_water_fire_magic_lv3_abyssal_flame", "name": "Abyssal Flame", "description": "A consuming fire that burns with dark intensity.", "ability_type": "magic", "level":3, "elements": ["dark", "water", "fire"], "base_power":95, "ap_cost":85, "effect": "damage", "can_aoe": False},

      ##DAMAGE AOE
    {"id": "dark_dark_dark_magic_lv3_shadow_blast", "name": "Shadow Blast", "description": "A burst of concentrated darkness.", "ability_type": "magic", "level":3, "elements": ["dark", "dark", "dark"], "base_power":88, "ap_cost":100, "effect": "damage", "can_aoe": True},
    {"id": "fire_fire_fire_magic_lv3_inferno_wave", "name": "Inferno Wave", "description": "A wave of intense flames.", "ability_type": "magic", "level":3, "elements": ["fire", "fire", "fire"], "base_power":90, "ap_cost":95, "effect": "damage", "can_aoe": True},
    {"id": "water_water_water_magic_lv3_tsunami_burst", "name": "Tsunami Burst", "description": "A massive burst of water energy.", "ability_type": "magic", "level":3, "elements": ["water", "water", "water"], "base_power":85, "ap_cost":95, "effect": "damage", "can_aoe": True},
    {"id": "earth_earth_earth_magic_lv3_earthshaker", "name": "Earthshaker", "description": "A powerful quake that shakes the ground.", "ability_type": "magic", "level":3, "elements": ["earth", "earth", "earth"], "base_power":90, "ap_cost":95, "effect": "damage", "can_aoe": True},
    {"id": "air_air_air_magic_lv3_storm_surge", "name": "Storm Surge", "description": "A surge of violent winds.", "ability_type": "magic", "level":3, "elements": ["air", "air", "air"], "base_power":88, "ap_cost":95, "effect": "damage", "can_aoe": True},
    {"id": "light_light_light_magic_lv3_radiant_burst", "name": "Radiant Burst", "description": "A burst of pure light energy.", "ability_type": "magic", "level":3, "elements": ["light", "light", "light"], "base_power":92, "ap_cost":100, "effect": "damage", "can_aoe": True},
    {"id": "ice_ice_ice_magic_lv3_hailstorm", "name": "Hailstorm", "description": "A nova of freezing energy.", "ability_type": "magic", "level":3, "elements": ["ice", "ice", "ice"], "base_power":86, "ap_cost":95, "effect": "damage", "can_aoe": True},
    {"id": "electric_electric_electric_magic_lv3_thunderstorm", "name": "Thunderstorm", "description": "A storm of electric fury.", "ability_type": "magic", "level":3, "elements": ["electric", "electric", "electric"], "base_power":90, "ap_cost":100, "effect": "damage", "can_aoe": True},

      ##CONTINUOUS DAMAGE
    {"id": "fire_ice_air_magic_lv3_scorch_and_bite", "name": "Scorch and Bite", "description": "A burning and freezing assault that sears flesh raw and slows the blood.", "ability_type": "magic", "level":3, "elements": ["fire", "ice", "air"], "base_power":3, "ap_cost":85, "effect": "status", "status_keys": ["continuous_damage", "dexterity_debuff"], "can_aoe": False},
    {"id": "ice_air_earth_magic_lv3_frostquake", "name": "Frostquake", "description": "A chilling tremor that freezes and shatters, leaving foes brittle and off-balance.", "ability_type": "magic", "level":3, "elements": ["ice", "air", "earth"], "base_power":10, "ap_cost":90, "effect": "status", "status_keys": ["continuous_damage", "defense_debuff"], "can_aoe": False},
    {"id": "air_earth_electric_magic_lv3_gale_shock", "name": "Gale Shock", "description": "A shocking gust that stuns and disrupts, jangling nerves and dulling reactions.", "ability_type": "magic", "level":3, "elements": ["air", "earth", "electric"], "base_power":3, "ap_cost":85, "effect": "status", "status_keys": ["continuous_damage", "dexterity_debuff"], "can_aoe": False},
    {"id": "earth_electric_water_magic_lv3_tectonic_current", "name": "Tectonic Current", "description": "A current of earth and electricity that destabilizes and shocks, cracking guard and grinding footing.", "ability_type": "magic", "level":3, "elements": ["earth", "electric", "water"], "base_power":13, "ap_cost":85, "effect": "status", "status_keys": ["continuous_damage", "defense_debuff"], "can_aoe": False},
    {"id": "electric_water_fire_magic_lv3_shockwave_burn", "name": "Shockwave Burn", "description": "A wave of electric and fire energy that burns and stuns, scrambling aim and searing skin.", "ability_type": "magic", "level":3, "elements": ["electric", "water", "fire"], "base_power":3, "ap_cost":85, "effect": "status", "status_keys": ["continuous_damage", "dexterity_debuff"], "can_aoe": False},
    {"id": "water_fire_ice_magic_lv3_boiling_frost", "name": "Boiling Frost", "description": "A freezing and scalding assault that wracks the body and slows every motion.", "ability_type": "magic", "level":3, "elements": ["water", "fire", "ice"], "base_power":10, "ap_cost":85, "effect": "status", "status_keys": ["continuous_damage", "dexterity_debuff"], "can_aoe": False},

    ##CONTINUOUS DAMAGE AOE
    {"id": "ice_earth_water_magic_lv3_glacial_mudslide", "name": "Glacial Mudslide", "description": "A sliding wave of ice and earth that chills and roots, miring all it touches in freezing sludge.", "ability_type": "magic", "level":3, "elements": ["ice", "earth", "water"], "base_power":0, "ap_cost":85, "effect": "status", "status_keys": ["continuous_damage", "dexterity_debuff"], "can_aoe": True},
    {"id": "air_electric_fire_magic_lv3_storm_of_flames", "name": "Storm of Flames", "description": "A fiery storm charged with electric energy that burns and shocks, leaving foes scorched and rattled.", "ability_type": "magic", "level":3, "elements": ["air", "electric", "fire"], "base_power":0, "ap_cost":85, "effect": "status", "status_keys": ["continuous_damage", "dexterity_debuff"], "can_aoe": True},

    ## NON PLAYER ABILITIES
    {"id": "wild_possibility", "name": "Wild Possibility", "description": "Revelry channels unfiltered chaos into a single volatile blast — every particle of air and electricity crackling with the unbounded energy of a world refusing to be tamed.", "ability_type": "magic", "level": 3, "elements": ["air", "electric", "fire"], "base_power": 95, "ap_cost": 90, "effect": "damage", "can_aoe": False, "non_player_ability": True},
    {"id": "singularity_of_grief", "name": "Singularity of Grief", "description": "Grief so pure and dense it collapses into a point of terrible gravity — all nearby are pulled into the void of Lament's accumulated sorrow.", "ability_type": "magic", "level": 3, "elements": ["dark", "ice", "water"], "base_power": 96, "ap_cost": 88, "effect": "damage", "can_aoe": True, "non_player_ability": True},
    # lament - hazard role: continuous_damage presses on targets persistently
    {"id": "weight_of_memory", "name": "Weight of Memory", "description": "Lament saturates the air with the crushing mass of irrecoverable memory — a field of dark, icy grief that settles on all caught within, eroding them continuously while dragging their bodies and spirits down.", "ability_type": "magic", "level": 3, "elements": ["dark", "ice", "dark"], "base_power": 0, "ap_cost": 90, "effect": "status", "status_keys": ["continuous_damage", "dexterity_debuff", "attack_debuff"], "can_aoe": True, "non_player_ability": True},
    # stigma - support/overworld first encounter 4th ability
    {"id": "seductive_void", "name": "Seductive Void", "description": "Stigma opens a tender, irresistible rift in the target's sense of self — they step toward the void willingly, and it tears them apart from the inside.", "ability_type": "magic", "level": 3, "elements": ["dark", "air", "light"], "base_power": 100, "ap_cost": 90, "effect": "damage", "can_aoe": False, "non_player_ability": True},
    # pageant - velvet veil first encounter 4th ability
    {"id": "performance_is_mandatory", "name": "Performance is Mandatory", "description": "Pageant broadcasts the demand for perfection across the entire floor — those who fail to meet the standard are blasted by the contempt of the crowd.", "ability_type": "magic", "level": 3, "elements": ["light", "air", "dark"], "base_power": 88, "ap_cost": 86, "effect": "damage", "can_aoe": True, "non_player_ability": True},
    # crux origin — lv3 filler: a glitch-burst of corrupted logic
    {"id": "glitch_cascade", "name": "Glitch Cascade", "description": "Crux emits a cascade of corrupted logical packets that detonate across the field as visible errors — fragments of impossible data that burn what they touch.", "ability_type": "magic", "level": 3, "elements": ["dark", "electric", "ice"], "base_power": 98, "ap_cost": 90, "effect": "damage", "can_aoe": True, "non_player_ability": True},
    # paradox — lv3 filler: a quick contradiction strike
    {"id": "paradox_touch", "name": "Paradox Touch", "description": "Paradox brushes a single target with the lightest contradiction — a moment of contact that makes the target simultaneously certain they are winning and losing, freezing action entirely.", "ability_type": "magic", "level": 3, "elements": ["dark", "air", "electric"], "base_power": 0, "ap_cost": 92, "effect": "status", "status_keys": ["stun", "continuous_damage", "intelligence_debuff"], "can_aoe": False, "non_player_ability": True},
]
