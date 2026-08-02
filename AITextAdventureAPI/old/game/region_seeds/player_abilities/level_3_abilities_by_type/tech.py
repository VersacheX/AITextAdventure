"""

 # --- tech ---
 ----------------------- level 3 seeding layout -----------------------
120 Ability possibilities -- we will only use so many
8x-pure_color: fire_fire_fire, water_water_water, earth_earth_earth, air_air_air, light_light_light, dark_dark_dark, ice_ice_ice, electric_electric_electric
6x-enemies: fire_ice_air, ice_air_earth, air_earth_electric, earth_electric_water, electric_water_fire, water_fire_ice
2x-allies: ice_earth_water, air_electric_fire
6x-light+enemies: light_fire_ice, light_ice_air, light_air_earth, light_earth_electric, light_electric_water, light_water_fire
6x-dark+enemies: dark_fire_ice, dark_ice_air, dark_air_earth, dark_earth_electric, dark_electric_water, dark_water_fire

   ##DAMAGE "base_power":60, "ap_cost":50, "effect": "damage", "can_aoe": False},
    6xlight+enemies & 2xallies

   ##DAMAGE AOE "base_power":40, "ap_cost":60, "effect": "damage", "can_aoe": True},
    6x enemies

   ##DEBUFF "base_power":14, "ap_cost":55, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
    -6xdark+enemies

   ##ELEMENTAL_ATTACK_BUFFS base_power: 0 ap_cost: 50 "effect": "status", "status_keys": ["elemental_attack_buff"], "can_aoe": True},
    -8xpure_color
]
"""

# Tech seeds extracted from level_3_player_ability_seeds
LEVEL_3_TECH_SEEDS = [
    ##DAMAGE light_fire_ice, light_ice_air, light_air_earth, light_earth_electric, light_electric_water, light_water_fire <- photon concepts   ice_earth_water, air_electric_fire <- something cool and techy
    {"id": "light_fire_ice_tech_lv3_photon_blade", "name": "Photon Blade", "description": "A blade of concentrated photon energy.", "ability_type": "tech", "level":3, "elements": ["light", "fire", "ice"], "base_power":62, "ap_cost":50, "effect": "damage", "can_aoe": False},
    {"id": "light_ice_air_tech_lv3_photon_gust", "name": "Photon Gust", "description": "A gust of photon-charged wind.", "ability_type": "tech", "level":3, "elements": ["light", "ice", "air"], "base_power":60, "ap_cost":50, "effect": "damage", "can_aoe": False},
    {"id": "light_air_earth_tech_lv3_photon_quake", "name": "Photon Quake", "description": "A quake of photon-infused earth.", "ability_type": "tech", "level":3, "elements": ["light", "air", "earth"], "base_power":64, "ap_cost":50, "effect": "damage", "can_aoe": False},
    {"id": "light_earth_electric_tech_lv3_photon_shock", "name": "Photon Shock", "description": "A shock of photon-charged electricity.", "ability_type": "tech", "level":3, "elements": ["light", "earth", "electric"], "base_power":62, "ap_cost":50, "effect": "damage", "can_aoe": False},
    {"id": "light_electric_water_tech_lv3_photon_wave", "name": "Photon Wave", "description": "A wave of photon-infused water.", "ability_type": "tech", "level":3, "elements": ["light", "electric", "water"], "base_power":60, "ap_cost":50, "effect": "damage", "can_aoe": False},
    {"id": "light_water_fire_tech_lv3_photon_flare", "name": "Photon Flare", "description": "A flare of photon-charged fire.", "ability_type": "tech", "level":3, "elements": ["light", "water", "fire"], "base_power":64, "ap_cost":50, "effect": "damage", "can_aoe": False},
    {"id": "ice_earth_water_tech_lv3_subzero_sludge", "name": "Subzero Sludge", "description": "A chilling sludge that freezes and slows.", "ability_type": "tech", "level":3, "elements": ["ice", "earth", "water"], "base_power":60, "ap_cost":50, "effect": "damage", "can_aoe": False},
    {"id": "air_electric_fire_tech_lv3_emp_burst", "name": "EMP Burst", "description": "A burst of electromagnetic energy that disrupts electronics.", "ability_type": "tech", "level":3, "elements": ["air", "electric", "fire"], "base_power":62, "ap_cost":50, "effect": "damage", "can_aoe": False},
    ##DAMAGE AOE fire_ice_air, ice_air_earth, air_earth_electric, earth_electric_water, electric_water_fire, water_fire_ice
    {"id": "fire_ice_air_tech_lv3_thermal_storm", "name": "Thermal Storm", "description": "A storm of heated air and ice shards.", "ability_type": "tech", "level":3, "elements": ["fire", "ice", "air"], "base_power": 42, "ap_cost":60, "effect": "damage", "can_aoe": True},
    {"id": "ice_air_earth_tech_lv3_frostquake_wave", "name": "Frostquake Wave", "description": "A wave of freezing wind and earth tremors.", "ability_type": "tech", "level":3, "elements": ["ice", "air", "earth"], "base_power": 40, "ap_cost":60, "effect": "damage", "can_aoe": True},
    {"id": "air_earth_electric_tech_lv3_gale_shockwave", "name": "Gale Shockwave", "description": "A shockwave of electrified wind and earth.", "ability_type": "tech", "level":3, "elements": ["air", "earth", "electric"], "base_power": 44, "ap_cost":60, "effect": "damage", "can_aoe": True},
    {"id": "earth_electric_water_tech_lv3_tectonic_current", "name": "Tectonic Current", "description": "A current of electrified water and earth tremors.", "ability_type": "tech", "level":3, "elements": ["earth", "electric", "water"], "base_power": 42, "ap_cost":60, "effect": "damage", "can_aoe": True},
    {"id": "electric_water_fire_tech_lv3_shockwave_burn", "name": "Shockwave Burn", "description": "A wave of electrified fire and water.", "ability_type": "tech", "level":3, "elements": ["electric", "water", "fire"], "base_power": 40, "ap_cost":60, "effect": "damage", "can_aoe": True},
    {"id": "water_fire_ice_tech_lv3_scalding_frostwave", "name": "Scalding Frostwave", "description": "A wave of hot water and ice shards.", "ability_type": "tech", "level":3, "elements": ["water", "fire", "ice"], "base_power": 42, "ap_cost":60, "effect": "damage", "can_aoe": True},
    ##DEBUFF dark_fire_ice, dark_ice_air, dark_air_earth, dark_earth_electric, dark_electric_water, dark_water_fire
    {"id": "dark_fire_ice_tech_lv3_corrosive_flame", "name": "Corrosive Flame", "description": "A corrosive flame that weakens enemy strength.", "ability_type": "tech", "level":3, "elements": ["dark", "fire", "ice"], "base_power": 0, "ap_cost":55, "effect": "status", "status_keys": ["strength_debuff"], "can_aoe": True},
    {"id": "dark_ice_air_tech_lv3_shadow_frost", "name": "Shadow Frost", "description": "A chilling shadow that dulls enemy intelligence.", "ability_type": "tech", "level":3, "elements": ["dark", "ice", "air"], "base_power": 0, "ap_cost":55, "effect": "status", "status_keys": ["intelligence_debuff"], "can_aoe": True},
    {"id": "dark_air_earth_tech_lv3_void_gale", "name": "Void Gale", "description": "A dark gale that disrupts enemy dexterity.", "ability_type": "tech", "level":3, "elements": ["dark", "air", "earth"], "base_power": 0, "ap_cost":55, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": True},
    {"id": "dark_water_fire_tech_lv3_dread_flame", "name": "Dread Flame", "description": "A dread flame that weakens enemy defenses.", "ability_type": "tech", "level":3, "elements": ["dark", "water", "fire"], "base_power": 0, "ap_cost":55, "effect": "status", "status_keys": ["defense_debuff"], "can_aoe": True},
    ##ELEMENTAL_ATTACK_BUFFS fire_fire_fire, water_water_water, earth_earth_earth, air_air_air, light_light_light, dark_dark_dark, ice_ice_ice, electric_electric_electric
    {"id": "fire_fire_fire_tech_lv3_incendiary_burst", "name": "Incendiary Burst", "description": "Enhances fire attacks; deals burn damage.", "ability_type": "tech", "level":3, "elements": ["fire", "fire", "fire"], "base_power":36, "ap_cost":100, "effect": "damage", "can_aoe": False},
    {"id": "water_water_water_tech_lv3_hydro_pulse", "name": "Hydro Pulse", "description": "Enhances water attacks; deals soak damage.", "ability_type": "tech", "level":3, "elements": ["water", "water", "water"], "base_power":34, "ap_cost":100, "effect": "damage", "can_aoe": False},
    {"id": "earth_earth_earth_tech_lv3_tectonic_surge", "name": "Tectonic Surge", "description": "Enhances earth attacks; deals crush damage.", "ability_type": "tech", "level":3, "elements": ["earth", "earth", "earth"], "base_power":38, "ap_cost":100, "effect": "damage", "can_aoe": False},
    {"id": "air_air_air_tech_lv3_gale_force", "name": "Gale Force", "description": "Enhances air attacks; deals slash damage.", "ability_type": "tech", "level":3, "elements": ["air", "air", "air"], "base_power":32, "ap_cost":100, "effect": "damage", "can_aoe": False},
    {"id": "light_light_light_tech_lv3_photon_amplifier", "name": "Photon Amplifier", "description": "Enhances light attacks; deals radiant damage.", "ability_type": "tech", "level":3, "elements": ["light", "light", "light"], "base_power":36, "ap_cost":100, "effect": "damage", "can_aoe": False},
    {"id": "dark_dark_dark_tech_lv3_shadow_enhancer", "name": "Shadow Enhancer", "description": "Enhances dark attacks; deals necrotic damage.", "ability_type": "tech", "level":3, "elements": ["dark", "dark", "dark"], "base_power":40, "ap_cost":100, "effect": "damage", "can_aoe": True},
    {"id": "ice_ice_ice_tech_lv3_frost_amplifier", "name": "Frost Amplifier", "description": "Enhances ice attacks; deals freeze damage.", "ability_type": "tech", "level":3, "elements": ["ice", "ice", "ice"], "base_power":30, "ap_cost":100, "effect": "damage", "can_aoe": False},
    {"id": "electric_electric_electric_tech_lv3_static_overload", "name": "Static Overload", "description": "Enhances electric attacks; deals shock damage.", "ability_type": "tech", "level":3, "elements": ["electric", "electric", "electric"], "base_power":38, "ap_cost":100, "effect": "damage", "can_aoe": False},

    ## STATUS EFFECT
    {"id": "dark_earth_electric_tech_lv3_petrifying_shock", "name": "Petrifying Shock", "description": "A petrifying shock that turns enemies to stone.", "ability_type": "tech", "level":3, "elements": ["dark", "earth", "electric"], "base_power": 0, "ap_cost":50, "effect": "status", "status_keys": ["petrify"], "can_aoe": False},
    {"id": "dark_electric_water_tech_lv3_abyssal_current", "name": "Abyssal Current", "description": "An abyssal current that confuses enemies.", "ability_type": "tech", "level":3, "elements": ["dark", "electric", "water"], "base_power": 0, "ap_cost":50, "effect": "status", "status_keys": ["confuse"], "can_aoe": False},

    ## NON PLAYER ABILITIES
    # crux origin — lv3 filler: a cold diagnostic that silences
    {"id": "static_erasure", "name": "Static Erasure", "description": "Crux runs an immediate purge of the target's communication channels — all signals are replaced with white noise and the target is cut off from every ability to call out or respond.", "ability_type": "tech", "level": 3, "elements": ["dark", "electric", "ice"], "base_power": 0, "ap_cost": 82, "effect": "status", "status_keys": ["silence"], "can_aoe": False, "non_player_ability": True},
]
