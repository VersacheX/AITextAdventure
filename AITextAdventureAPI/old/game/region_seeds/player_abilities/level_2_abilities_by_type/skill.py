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
"""
LEVEL_2_SKILL_ABILITY_SEEDS = [
 # --- skill ---
 ##DAMAGE (single-target, low cost)
 {"id": "electric_fire_skill_lv2_thunder_katana", "name": "Thunder Katana", "description": "A swift electrified blade strike.", "ability_type": "skill", "level":2, "elements": ["electric", "fire"], "base_power":6, "ap_cost":26, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
 {"id": "electric_light_skill_lv2_solar_shiv", "name": "Solar Shiv", "description": "A bright, piercing electric jab.", "ability_type": "skill", "level":2, "elements": ["electric", "light"], "base_power":5, "ap_cost":25, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
 {"id": "electric_dark_skill_lv2_nightward_dart", "name": "Nightward Dart", "description": "A shadowy spark that pierces armor.", "ability_type": "skill", "level":2, "elements": ["electric", "dark"], "base_power":5, "ap_cost":25, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
 {"id": "electric_ice_skill_lv2_frostbolt_trap", "name": "Frostbolt Trap", "description": "A chilling electric projectile.", "ability_type": "skill", "level":2, "elements": ["electric", "ice"], "base_power":4, "ap_cost":23, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},

 {"id": "ice_water_skill_lv2_mist_kurosawa", "name": "Mist Kurosawa", "description": "A flowing cold stab shrouded in mist.", "ability_type": "skill", "level":2, "elements": ["ice", "water"], "base_power":5, "ap_cost":25, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
 {"id": "ice_earth_skill_lv2_glacial_talon", "name": "Glacial Talon", "description": "A stony, freezing slash.", "ability_type": "skill", "level":2, "elements": ["ice", "earth"], "base_power":6, "ap_cost":26, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
 {"id": "ice_light_skill_lv2_crystal_shiv", "name": "Crystal Shiv", "description": "A refracting cold strike.", "ability_type": "skill", "level":2, "elements": ["ice", "light"], "base_power":5, "ap_cost":25, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
 {"id": "ice_dark_skill_lv2_shadow_spike", "name": "Shadow Spike", "description": "A chilling strike laced with shadow.", "ability_type": "skill", "level":2, "elements": ["ice", "dark"], "base_power":4, "ap_cost":23, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},

 {"id": "fire_earth_skill_lv2_volcanic_pike", "name": "Volcanic Pike", "description": "A molten thrust that cracks defenses.", "ability_type": "skill", "level":2, "elements": ["fire", "earth"], "base_power":5, "ap_cost":25, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
 {"id": "fire_air_skill_lv2_flame_quill", "name": "Flame Quill", "description": "A quick fiery needle.", "ability_type": "skill", "level":2, "elements": ["fire", "air"], "base_power":5, "ap_cost":25, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
 {"id": "fire_light_skill_lv2_sunstrike_shade", "name": "Sunstrike", "description": "A focused flare-infused strike.", "ability_type": "skill", "level":2, "elements": ["fire", "light"], "base_power":5, "ap_cost":25, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},

 {"id": "earth_water_skill_lv2_river_hook", "name": "River Hook", "description": "A pulling strike with muddy force.", "ability_type": "skill", "level":2, "elements": ["earth", "water"], "base_power":4, "ap_cost":23, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
 {"id": "earth_light_skill_lv2_hoplite_prick", "name": "Hoplite Prick", "description": "A disciplined, radiant stab.", "ability_type": "skill", "level":2, "elements": ["earth", "light"], "base_power":6, "ap_cost":26, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},

 {"id": "air_water_skill_lv2_gale_sting", "name": "Gale Sting", "description": "A swift sting carried on spray.", "ability_type": "skill", "level":2, "elements": ["air", "water"], "base_power":5, "ap_cost":25, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
 {"id": "air_light_skill_lv2_dawn_cut", "name": "Dawn Cut", "description": "A blindingly quick slice.", "ability_type": "skill", "level":2, "elements": ["air", "light"], "base_power":5, "ap_cost":25, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
 {"id": "water_light_skill_lv2_lustral_pin", "name": "Lustral Pin", "description": "A cleansing jab that strikes true.", "ability_type": "skill", "level":2, "elements": ["water", "light"], "base_power":5, "ap_cost":25, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},

 ##DAMAGE AOE (wider, low cost)
 {"id": "electric_electric_skill_lv2_static_spread", "name": "Static Spread", "description": "A rapid shock that arcs widely.", "ability_type": "skill", "level":2, "elements": ["electric", "electric"], "base_power":17, "ap_cost":20, "effect": "damage", "can_aoe": True},
 {"id": "ice_ice_skill_lv2_shiver_burst", "name": "Shiver Burst", "description": "A frost burst that chills many.", "ability_type": "skill", "level":2, "elements": ["ice", "ice"], "base_power":17, "ap_cost":20, "effect": "damage", "can_aoe": True},
 {"id": "light_light_skill_lv2_dazzle_wave", "name": "Dazzle Wave", "description": "A blinding slash that hits multiple.", "ability_type": "skill", "level":2, "elements": ["light", "light"], "base_power":16, "ap_cost":19, "effect": "damage", "can_aoe": True},
 {"id": "dark_dark_skill_lv2_void_whorl", "name": "Void Whorl", "description": "A shadowy ripple that strikes many.", "ability_type": "skill", "level":2, "elements": ["dark", "dark"], "base_power":17, "ap_cost":20, "effect": "damage", "can_aoe": True},
 {"id": "water_water_skill_lv2_ripple_cascade", "name": "Ripple Cascade", "description": "A quick splash that slashes a group.", "ability_type": "skill", "level":2, "elements": ["water", "water"], "base_power":16, "ap_cost":19, "effect": "damage", "can_aoe": True},
 {"id": "earth_earth_skill_lv2_grit_swath", "name": "Grit Swath", "description": "A sweeping stony strike.", "ability_type": "skill", "level":2, "elements": ["earth", "earth"], "base_power":17, "ap_cost":20, "effect": "damage", "can_aoe": True},
 {"id": "fire_fire_skill_lv2_singe_wheel", "name": "Singe Wheel", "description": "A fiery wheel of quick strikes.", "ability_type": "skill", "level":2, "elements": ["fire", "fire"], "base_power":16, "ap_cost":19, "effect": "damage", "can_aoe": True},
 {"id": "air_air_skill_lv2_gust_blitz", "name": "Gust Blitz", "description": "A flurry of swift air strikes.", "ability_type": "skill", "level":2, "elements": ["air", "air"], "base_power":17, "ap_cost":20, "effect": "damage", "can_aoe": True},

 ##CONTINUOUS DAMAGE (low per-turn, sustained)
 {"id": "electric_water_skill_lv2_corrosive_splash_bomb", "name": "Corrosive Splash Bomb", "description": "A splash bomb that corrodes and disrupts elemental defenses over time.", "ability_type": "skill", "level":2, "elements": ["electric", "water"], "base_power":1, "ap_cost":40, "effect": "status", "status_keys": ["continuous_damage", "elemental_debuff"], "can_aoe": True},
 {"id": "electric_earth_skill_lv2_ion_trickle", "name": "Ion Trickle", "description": "Slow arcing current that lingers.", "ability_type": "skill", "level":2, "elements": ["electric", "earth"], "base_power":3, "ap_cost":35, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True},
 {"id": "light_dark_skill_lv2_twilight_bleed", "name": "Twilight Bleed", "description": "A subtle wound that saps vitality.", "ability_type": "skill", "level":2, "elements": ["light", "dark"], "base_power":3, "ap_cost":35, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True},
 {"id": "earth_air_skill_lv2_sandstream", "name": "Sandstream", "description": "A gritty flow that grinds defenses.", "ability_type": "skill", "level":2, "elements": ["earth", "air"], "base_power":3, "ap_cost":35, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True},
 {"id": "ice_fire_skill_lv2_acid_slime_spray", "name": "Acid Slime Spray", "description": "A corrosive spray that damages and weakens defenses over time.", "ability_type": "skill", "level":2, "elements": ["ice", "fire"], "base_power":1, "ap_cost":35, "effect": "status", "status_keys": ["continuous_damage", "defense_debuff"], "can_aoe": True},
 {"id": "fire_water_skill_lv2_steaming_wound", "name": "Steaming Wound", "description": "Scalding seep that continues to hurt.", "ability_type": "skill", "level":2, "elements": ["fire", "water"], "base_power":3, "ap_cost":35, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True},
 {"id": "ice_air_skill_lv2_razor_chill_drift", "name": "Razor Chill Drift", "description": "A sharp, chilling wind that slows and damages over time.", "ability_type": "skill", "level":2, "elements": ["ice", "air"], "base_power":3, "ap_cost":35, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True},

 ##DEBUFFS (aoe, no base damage)
 {"id": "fire_dark_skill_lv2_embersmoke", "name": "Ember Smoke", "description": "A smoky blast that weakens strength.", "ability_type": "skill", "level":2, "elements": ["fire", "dark"], "base_power":1, "ap_cost":30, "effect": "status", "status_keys": ["strength_debuff", "elemental_debuff"], "can_aoe": True},
 {"id": "water_dark_skill_lv2_deep_water_blitz", "name": "Deep Water Blitz", "description": "A deep water attack that disrupts intelligence and elemental defenses.", "ability_type": "skill", "level":2, "elements": ["water", "dark"], "base_power":1, "ap_cost":35, "effect": "status", "status_keys": ["intelligence_debuff", "elemental_debuff"], "can_aoe": True},
 {"id": "air_dark_skill_lv2_gale_of_doubt", "name": "Gale of Doubt", "description": "A dark gust that dulls reflexes.", "ability_type": "skill", "level":2, "elements": ["air", "dark"], "base_power":0, "ap_cost":25, "effect": "status", "status_keys": ["confuse"], "can_aoe": False},

 ##STATUS EFFECTS (special)
 {"id": "electric_air_skill_lv2_static_caltrops", "name": "Static Caltrops", "description": "Deploy electrified spikes that stun.", "ability_type": "skill", "level":2, "elements": ["electric", "air"], "base_power":0, "ap_cost":30, "effect": "status", "status_keys": ["stun"], "can_aoe": True},
 {"id": "earth_dark_skill_lv2_petrify_dart", "name": "Petrify Dart", "description": "A dark mineral dart that petrifies.", "ability_type": "skill", "level":2, "elements": ["earth", "dark"], "base_power":0, "ap_cost":50, "effect": "status", "status_keys": ["petrify"], "can_aoe": False},

 
   ##NON-PLAYER ABILITIES
 {"id": "lv2_hostile_ability_dark_air_skill_nightmare_wave", "name": "Nightmare Wave", "description": "A dark gust that terrifies.", "ability_type": "skill", "level":2, "elements": ["dark", "air"], "base_power":0, "ap_cost":30, "effect": "status", "status_keys": ["confuse"], "can_aoe": False, "non_player_ability": True},
 {"id": "lv2_hostile_ability_dark_ice_skill_void_spike", "name": "Void Spike", "description": "A chilling spike that saps will.", "ability_type": "skill", "level":2, "elements": ["dark", "ice"], "base_power":20, "ap_cost":15, "effect": "damage", "can_aoe": False, "non_player_ability": True},
]