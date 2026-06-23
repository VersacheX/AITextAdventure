"""
SKILL ABILITIES ARE FOCUSED ON DEXTERITY AND SPEED, CRITICAL HIT RATE, AND EVASION.
they should be low cost and low damage,
examples of skillsets include:
ninjutsu (smokebombs, pwders, darts)
assassins (precise strikes, debilitating strikes)
stealth operatives (quick strikes, evasive maneuvers)
thiefs (quick strikes, debuffs)

35 Ability possibilities

ABILITY DIVISION
 DAMAGE: electric-fire,electric-light,electric-dark,electric-ice,ice-water,ice-earth,ice-light,ice-dark,fire-earth,fire-air,fire-light,earth-water,earth-light,air-water,air-light,water-light
   -- base_power: 16-20 ap_cost: 15-20
 DAMAGE AOE: electric-electric, ice-ice, light-light, dark-dark, water-water, earth-earth, fire-fire, air-air
    -- base_power: 14-18 ap_cost: 18-22 
 CONTINUOUS DAMAGE: electric-water, electric-earth, light-dark, earth-air, ice-fire, fire-water, ice-air
    -- base_power: 1-3 ap_cost: 26-35
 DEBUFFS: fire-dark (aoe strength debuff), water-dark (aoe intelligence debuff), air-dark (aoe dexterity debuff)
    -- base_power: 0 ap_cost: 30
 STATUS EFFECTS: electric-air (aoe stun) "Static Caltrops" ap-30, earth-dark (petrify) "Petrify Dart" ap-50
    -- base_power: 0 ap_cost: 30 and 50

    

----------------------- level 3 seeding layout -----------------------
120 Ability possibilities -- we will only use so many
8x-pure_color: fire_fire_fire, water_water_water, earth_earth_earth, air_air_air, light_light_light, dark_dark_dark, ice_ice_ice, electric_electric_electric
6x-enemies: fire_ice_air, ice_air_earth, air_earth_electric, earth_electric_water, electric_water_fire, water_fire_ice
2x-allies: ice_earth_water, air_electric_fire
6x-light+enemies: light_fire_ice, light_ice_air, light_air_earth, light_earth_electric, light_electric_water, light_water_fire
6x-dark+enemies: dark_fire_ice, dark_ice_air, dark_air_earth, dark_earth_electric, dark_electric_water, dark_water_fire
DAMAGE:use 8x pure color -- base_power: 30-40 ap_cost: 30-40
DAMAGE AOE: use 6x dark+enemies -- base_power: 25-35 ap_cost: 35-45
CONTINUOUS DAMAGE: 6x enemies + 3xlight+enemies -- base_power: 3-7 ap_cost: 60-70
DEBUFFS: 3xlight+enemies (aoe strength debuff), (aoe intelligence debuff), (aoe dexterity debuff) -- base_power: 0 ap_cost: 70
STATUS EFFECTS: 2x allies -- base_power: 0 ap_cost: 75 aoe silence (air_electric_fire) and aoe confuse (ice_earth_water) 125 and 150 ap
"""

# Skill seeds extracted from level_3_player_ability_seeds
LEVEL_3_SKILL_SEEDS = [
    ##DAMAGE
    {"id": "fire_fire_fire_skill_lv3_blazing_strike", "name": "Blazing Strike", "description": "A swift strike engulfed in flames.", "ability_type": "skill", "level":3, "elements": ["fire","fire","fire"], "base_power":38, "ap_cost":40, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
    {"id": "water_water_water_skill_lv3_raging_wave", "name": "Raging Wave", "description": "A powerful wave crashing down on foes.", "ability_type": "skill", "level":3, "elements": ["water","water","water"], "base_power":36, "ap_cost":40, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
    {"id": "earth_earth_earth_skill_lv3_quake_pummel", "name": "Quake Pummel", "description": "A heavy pummel that shakes the ground.", "ability_type": "skill", "level":3, "elements": ["earth","earth","earth"], "base_power":40, "ap_cost":40, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
    {"id": "air_air_air_skill_lv3_gale_slash", "name": "Gale Slash", "description": "A slicing wind attack that cuts through foes.", "ability_type": "skill", "level":3, "elements": ["air","air","air"], "base_power":35, "ap_cost":40, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
    {"id": "light_light_light_skill_lv3_radiant_strike", "name": "Radiant Strike", "description": "A blinding strike of pure light.", "ability_type": "skill", "level":3, "elements": ["light","light","light"], "base_power":37, "ap_cost":40, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
    {"id": "dark_dark_dark_skill_lv3_shadow_cleave", "name": "Shadow Cleave", "description": "A dark strike that drains vitality.", "ability_type": "skill", "level":3, "elements": ["dark","dark","dark"], "base_power":39, "ap_cost":40, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
    {"id": "ice_ice_ice_skill_lv3_frost_bite", "name": "Frost Bite", "description": "A chilling strike that slows foes.", "ability_type": "skill", "level":3, "elements": ["ice","ice","ice"], "base_power":34, "ap_cost":40, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
    {"id": "electric_electric_electric_skill_lv3_thunder_strike", "name": "Thunder Strike", "description": "A jolting strike that stuns enemies.", "ability_type": "skill", "level":3, "elements": ["electric","electric","electric"], "base_power":38, "ap_cost":40, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
    ##DAMAGE AOE
    {"id": "dark_fire_ice_skill_lv3_nightmare_burst", "name": "Nightmare Burst", "description": "A burst of dark flames and ice that engulfs multiple foes.", "ability_type": "skill", "level":3, "elements": ["dark","fire","ice"], "base_power":33, "ap_cost":45, "effect": "damage", "can_aoe": True},
    {"id": "dark_ice_air_skill_lv3_frozen_shadow_wave", "name": "Frozen Shadow Wave", "description": "A wave of icy darkness that chills and disorients.", "ability_type": "skill", "level":3, "elements": ["dark","ice","air"], "base_power":31, "ap_cost":45, "effect": "damage", "can_aoe": True},
    {"id": "dark_air_earth_skill_lv3_voidquake", "name": "Voidquake", "description": "A tremor of shadowy wind and earth that unsettles foes.", "ability_type": "skill", "level":3, "elements": ["dark","air","earth"], "base_power":35, "ap_cost":45, "effect": "damage", "can_aoe": True},
    {"id": "dark_earth_electric_skill_lv3_shadow_shockwave", "name": "Shadow Shockwave", "description": "A shockwave of dark earth and electricity that stuns multiple enemies.", "ability_type": "skill", "level":3, "elements": ["dark","earth","electric"], "base_power":34, "ap_cost":45, "effect": "damage", "can_aoe": True},
    {"id": "dark_electric_water_skill_lv3_abyssal_current", "name": "Abyssal Current", "description": "A current of dark electricity and water that confuses foes.", "ability_type": "skill", "level":3, "elements": ["dark","electric","water"], "base_power":30, "ap_cost":45, "effect": "damage", "can_aoe": True},
    {"id": "dark_water_fire_skill_lv3_dread_flame_wave", "name": "Dread Flame Wave", "description": "A wave of dark fire and water that burns and drenches enemies.", "ability_type": "skill", "level":3, "elements": ["dark","water","fire"], "base_power":32, "ap_cost":45, "effect": "damage", "can_aoe": True},
    ##CONTINUOUS DAMAGE
    {"id": "fire_ice_air_skill_lv3_burning_frost_wind", "name": "Burning Frost Wind", "description": "A chilling wind laced with burning embers that damages over time.", "ability_type": "skill", "level":3, "elements": ["fire","ice","air"], "base_power":5, "ap_cost":70, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
    {"id": "ice_air_earth_skill_lv3_frostquake_strike", "name": "Frostquake Strike", "description": "A freezing strike that causes tremors, damaging over time.", "ability_type": "skill", "level":3, "elements": ["ice","air","earth"], "base_power":4, "ap_cost":65, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
    {"id": "air_earth_electric_skill_lv3_gale_shockwave", "name": "Gale Shockwave", "description": "A shocking gust that stuns and deals damage over time.", "ability_type": "skill", "level":3, "elements": ["air","earth","electric"], "base_power":6, "ap_cost":70, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
    {"id": "earth_electric_water_skill_lv3_tectonic_current_strike", "name": "Tectonic Current Strike", "description": "A strike combining earth and electricity that destabilizes and deals damage over time.", "ability_type": "skill", "level":3, "elements": ["earth","electric","water"], "base_power":5, "ap_cost":70, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
    {"id": "electric_water_fire_skill_lv3_shockwave_burn_strike", "name": "Shockwave Burn Strike", "description": "A wave of electric and fire energy that burns and stuns, causing damage over time.", "ability_type": "skill", "level":3, "elements": ["electric","water","fire"], "base_power":4, "ap_cost":65, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
    {"id": "water_fire_ice_skill_lv3_boiling_frost_strike", "name": "Boiling Frost Strike", "description": "A freezing and scalding strike that deals damage over time.", "ability_type": "skill", "level":3, "elements": ["water","fire","ice"], "base_power":3, "ap_cost":65, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
    ##STATUS EFFECTS
    {"id": "ice_earth_water_skill_lv3_confusing_mist", "name": "Confusing Mist", "description": "A mist that clouds the mind, causing confusion among allies.", "ability_type": "skill", "level":3, "elements": ["ice","earth","water"], "base_power":0, "ap_cost":150, "effect": "status", "status_keys": ["confuse"], "can_aoe": True},
    {"id": "air_electric_fire_skill_lv3_silencing_gale", "name": "Silencing Gale", "description": "A swift gale that silences allies, preventing spellcasting.", "ability_type": "skill", "level":3, "elements": ["air","electric","fire"], "base_power":0, "ap_cost":125, "effect": "status", "status_keys": ["silence"], "can_aoe": True},
]
