"""35 possibilities
electric-electric
electric-water
electric-earth
electric-air
electric-fire
electric-light
electric-dark
electric-ice
ice-ice
ice-water
ice-earth
ice-air
ice-fire
ice-light
ice-dark
fire-fire
fire-earth
fire-air
fire-water
fire-light
fire-dark
earth-earth
earth-air
earth-water
earth-light
earth-dark
air-air
air-water
air-light
air-dark
water-water
water-light
water-dark
light-light
light-dark
dark-dark
"""

LEVEL_2_TECH_ABILITY_SEEDS = [
 # --- tech ---
   ##DAMAGE

 {"id": "electric_air_tech_lv2_thunder_vent", "name": "Thunder Vent", "description": "Electrified gust emitter.", "ability_type": "tech", "level":2, "elements": ["electric", "air"], "base_power":28, "ap_cost":24, "effect": "damage", "can_aoe": False},
 {"id": "electric_fire_tech_lv2_plasma_emitter", "name": "Plasma Emitter", "description": "Superheated plasma discharge.", "ability_type": "tech", "level":2, "elements": ["electric", "fire"], "base_power":30, "ap_cost":25, "effect": "damage", "can_aoe": False},
 {"id": "electric_light_tech_lv2_photon_lance", "name": "Photon Lance", "description": "Focused photon-electric strike.", "ability_type": "tech", "level":2, "elements": ["electric", "light"], "base_power":30, "ap_cost":25, "effect": "damage", "can_aoe": False},
 {"id": "electric_dark_tech_lv2_void_shocker", "name": "Void Shocker", "description": "Disruptive void-electric shock.", "ability_type": "tech", "level":2, "elements": ["electric", "dark"], "base_power":32, "ap_cost":26, "effect": "damage", "can_aoe": False},
 
 {"id": "ice_water_tech_lv2_glacial_projector", "name": "Glacial Projector", "description": "Freezing water wave projector.", "ability_type": "tech", "level":2, "elements": ["ice", "water"], "base_power":30, "ap_cost":25, "effect": "damage", "can_aoe": False},
 {"id": "ice_air_tech_lv2_chill_vent", "name": "Chill Vent", "description": "Cold gust emitter.", "ability_type": "tech", "level":2, "elements": ["ice", "air"], "base_power":28, "ap_cost":24, "effect": "damage", "can_aoe": False},
 {"id": "ice_light_tech_lv2_ice_prism", "name": "Ice Prism", "description": "Refracting cold-energy beam.", "ability_type": "tech", "level":2, "elements": ["ice", "light"], "base_power":30, "ap_cost":25, "effect": "damage", "can_aoe": False},
 {"id": "ice_dark_tech_lv2_shadowfrost_emitter", "name": "Shadowfrost Emitter", "description": "Dark frost generator.", "ability_type": "tech", "level":2, "elements": ["ice", "dark"], "base_power":32, "ap_cost":26, "effect": "damage", "can_aoe": False},
  
 {"id": "fire_earth_tech_lv2_forge_pulse", "name": "Forge Pulse", "description": "Magma-forged pulse launcher.", "ability_type": "tech", "level":2, "elements": ["fire", "earth"], "base_power":30, "ap_cost":25, "effect": "damage", "can_aoe": False},
 {"id": "fire_air_tech_lv2_aero_flare", "name": "Aero Flare", "description": "Flare projector on air currents.", "ability_type": "tech", "level":2, "elements": ["fire", "air"], "base_power":28, "ap_cost":24, "effect": "damage", "can_aoe": False},
 {"id": "fire_light_tech_lv2_beacon_drive", "name": "Beacon Drive", "description": "Solar-heat beam module.", "ability_type": "tech", "level":2, "elements": ["fire", "light"], "base_power":30, "ap_cost":25, "effect": "damage", "can_aoe": False},
 {"id": "fire_dark_tech_lv2_hell_blast", "name": "Hell Blast", "description": "A highly-focused dark charged fire projectile.", "ability_type": "tech", "level":2, "elements": ["fire", "dark"], "base_power":32, "ap_cost":26, "effect": "damage", "can_aoe": False},
 
 {"id": "earth_water_tech_lv2_trench_drive", "name": "Trench Drive", "description": "Burrowing impact driver.", "ability_type": "tech", "level":2, "elements": ["earth", "water"], "base_power":30, "ap_cost":25, "effect": "damage", "can_aoe": False},
 {"id": "earth_light_tech_lv2_impact_percussion", "name": "Impact Percussion", "description": "A high-powered focused percussion blast.", "ability_type": "tech", "level":2, "elements": ["earth", "light"], "base_power":30, "ap_cost":25, "effect": "damage", "can_aoe": False},
 {"id": "earth_dark_tech_lv2_shadow_missile", "name": "Shadow Missile", "description": "Dark-earth missile.", "ability_type": "tech", "level":2, "elements": ["earth", "dark"], "base_power":32, "ap_cost":26, "effect": "damage", "can_aoe": False},
 
 {"id": "air_water_tech_lv2_hydro_propulsor", "name": "Hydro Propulsor", "description": "Pressurized water-air impact grenade.", "ability_type": "tech", "level":2, "elements": ["air", "water"], "base_power":30, "ap_cost":25, "effect": "damage", "can_aoe": False},
 {"id": "air_light_tech_lv2_photon_blast", "name": "Photon Blast", "description": "Air infused light laser.", "ability_type": "tech", "level":2, "elements": ["air", "light"], "base_power":30, "ap_cost":25, "effect": "damage", "can_aoe": False},
 {"id": "air_dark_tech_lv2_rift_blast", "name": "Rift Blast", "description": "Air infused dark laser.", "ability_type": "tech", "level":2, "elements": ["air", "dark"], "base_power":32, "ap_cost":26, "effect": "damage", "can_aoe": False},
 
 {"id": "water_light_tech_lv2_solar_flume", "name": "Solar Flume", "description": "Gleaming water beam.", "ability_type": "tech", "level":2, "elements": ["water", "light"], "base_power":30, "ap_cost":25, "effect": "damage", "can_aoe": False},
 {"id": "water_dark_tech_lv2_shadow_cannon", "name": "Shadow Cannon", "description": "Eldritch water cannon.", "ability_type": "tech", "level":2, "elements": ["water", "dark"], "base_power":32, "ap_cost":26, "effect": "damage", "can_aoe": False},


 
   ##DAMAGE AOE
 {"id": "electric_electric_tech_lv2_arc_barrage", "name": "Arc Barrage", "description": "A wide barrage of electrical arcs.", "ability_type": "tech", "level":2, "elements": ["electric", "electric"], "base_power":18, "ap_cost":20, "effect": "damage", "can_aoe": True},
 {"id": "ice_ice_tech_lv2_glacier_cannon", "name": "Glacier Cannon", "description": "A broad blast of concentrated ice.", "ability_type": "tech", "level":2, "elements": ["ice", "ice"], "base_power":20, "ap_cost":22, "effect": "damage", "can_aoe": True},
 {"id": "fire_fire_tech_lv2_infernal_coil", "name": "Infernal Coil", "description": "A searing coil that scorches multiple foes.", "ability_type": "tech", "level":2, "elements": ["fire", "fire"], "base_power":18, "ap_cost":20, "effect": "damage", "can_aoe": True},
 {"id": "earth_earth_tech_lv2_seismic_rupture", "name": "Seismic Rupture", "description": "A ground rupture that damages nearby.", "ability_type": "tech", "level":2, "elements": ["earth", "earth"], "base_power":20, "ap_cost":22, "effect": "damage", "can_aoe": True},
 {"id": "air_air_tech_lv2_tempest_array", "name": "Tempest Array", "description": "A sweeping storm of compressed air.", "ability_type": "tech", "level":2, "elements": ["air", "air"], "base_power":20, "ap_cost":22, "effect": "damage", "can_aoe": True},
 {"id": "water_water_tech_lv2_tidal_burst", "name": "Tidal Burst", "description": "A pressurized water burst hitting many.", "ability_type": "tech", "level":2, "elements": ["water", "water"], "base_power":18, "ap_cost":20, "effect": "damage", "can_aoe": True},
 {"id": "dark_dark_tech_lv2_abyssal_core", "name": "Abyssal Core", "description": "A dark pulse from a void core.", "ability_type": "tech", "level":2, "elements": ["dark", "dark"], "base_power":17, "ap_cost":18, "effect": "damage", "can_aoe": True},
 {"id": "light_light_tech_lv2_luminous_core", "name": "Luminous Core", "description": "A blinding core of pure light.", "ability_type": "tech", "level":2, "elements": ["light", "light"], "base_power":22, "ap_cost":24, "effect": "damage", "can_aoe": True},

   ##DEBUFF
 {"id": "light_dark_tech_lv2_contrast_burst", "name": "Contrast Burst", "description": "Light and shadow clash, weakening foes.", "ability_type": "tech", "level":2, "elements": ["light", "dark"], "base_power":1, "ap_cost":30, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
 {"id": "electric_earth_tech_lv2_grounded_spike", "name": "Grounded Spike", "description": "Charge forced into ground, sapping strength.", "ability_type": "tech", "level":2, "elements": ["electric", "earth"], "base_power":1, "ap_cost":30, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
 {"id": "electric_water_tech_lv2_ion_tide", "name": "Ion Tide", "description": "Charged tide that corrodes defenses.", "ability_type": "tech", "level":2, "elements": ["electric", "water"], "base_power":1, "ap_cost":30, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
 {"id": "ice_earth_tech_lv2_glacial_rivet", "name": "Glacial Rivet", "description": "Frozen earth shards chill and hinder.", "ability_type": "tech", "level":2, "elements": ["ice", "earth"], "base_power":1, "ap_cost":30, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
 {"id": "ice_fire_tech_lv2_frostflare", "name": "Frostflare", "description": "Freezing flames that sap strength.", "ability_type": "tech", "level":2, "elements": ["ice", "fire"], "base_power":1, "ap_cost":30, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
 {"id": "earth_air_tech_lv2_rivet_gale", "name": "Rivet Gale", "description": "Stone and gale unsettle foes' footing.", "ability_type": "tech", "level":2, "elements": ["earth", "air"], "base_power":1, "ap_cost":30, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
 {"id": "fire_water_tech_lv2_steam_burst", "name": "Steam Burst", "description": "Scalding steam that weakens armor.", "ability_type": "tech", "level":2, "elements": ["fire", "water"], "base_power":1, "ap_cost":30, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
   ##STATUS EFFECT
 {"id": "dark_air_lv2_echo_displacer", "name": "Echo Displacer", "description": "A device that disrupts sound resonance nearby.", "ability_type": "tech", "level":2, "elements": ["dark", "air"], "base_power":0, "ap_cost":30, "effect": "status", "status_keys": ["silence"], "can_aoe": True},



   ##NON-PLAYER ABILITIES
 {"id": "lv2_hostile_ability_fire_water_tech_steam_grenade", "name": "Steam Grenade", "description": "A grenade that releases scalding steam.", "ability_type": "tech", "level":2, "elements": ["fire", "water"], "base_power":3, "ap_cost":35, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True, "non_player_ability": True},
 {"id": "lv2_hostile_ability_earth_light_tech_primal_disunion", "name": "Primal Disunion", "description": "A device that emits an invasive harmonic pulse.", "ability_type": "tech", "level":2, "elements": ["earth", "light"], "base_power":0, "ap_cost":35, "effect": "status", "status_keys": ["continuous_damage", "attack_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "lv2_hostile_ability_dark_electric_tech_nether_catalyst_bomb", "name": "Nether Catalyst Bomb", "description": "A device that releases a disruptive energy pulse.", "ability_type": "tech", "level":2, "elements": ["dark", "electric"], "base_power":0, "ap_cost":35, "effect": "status", "status_keys": ["continuous_damage", "defense_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "lv2_hostile_ability_dark_water_tech_void_spatter", "name": "Void Spatter", "description": "A device that releases a corrosive void liquid.", "ability_type": "tech", "level":2, "elements": ["dark", "water"], "base_power":3, "ap_cost":35, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True, "non_player_ability": True},
 {"id": "lv2_hostile_ability_electric_earth_tech_ion_leech", "name": "Ion Leech", "description": "A device that drains energy from nearby electronics.", "ability_type": "tech", "level":2, "elements": ["electric", "earth"], "base_power":3, "ap_cost":35, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True, "non_player_ability": True},
]