"""
MAGIC ABILITIES  ARE  BASED ON INTELLIGENCE STAT.
they should be offensive magic attacks, or damage over time effects... possible status effects
they have high power but also high ap cost
some lore for magic in a neo noir fantasy setting is created with these abilities

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
"""

LEVEL_2_MAGIC_ABILITY_SEEDS = [
 # --- magic ---
 ## DAMAGE (single-target, high power)
 {"id": "electric_fire_magic_lv2_arclance", "name": "Arc Lance", "description": "A spear of electrified flame.", "ability_type": "magic", "level":2, "elements": ["electric", "fire"], "base_power":34, "ap_cost":28, "effect": "damage", "can_aoe": False},
 {"id": "electric_light_magic_lv2_photon_burst", "name": "Photon Burst", "description": "A concentrated burst of light and charge.", "ability_type": "magic", "level":2, "elements": ["electric", "light"], "base_power":33, "ap_cost":28, "effect": "damage", "can_aoe": False},
 {"id": "electric_dark_magic_lv2_nocturne_shock", "name": "Nocturne Shock", "description": "A jolt steeped in shadow.", "ability_type": "magic", "level":2, "elements": ["electric", "dark"], "base_power":36, "ap_cost":29, "effect": "damage", "can_aoe": False},
 {"id": "electric_ice_magic_lv2_frost_current", "name": "Frost Current", "description": "A cold electric surge.", "ability_type": "magic", "level":2, "elements": ["electric", "ice"], "base_power":32, "ap_cost":25, "effect": "damage", "can_aoe": False},

 {"id": "ice_water_magic_lv2_glacier_spike", "name": "Glacier Spike", "description": "A stabbing wave of frozen water.", "ability_type": "magic", "level":2, "elements": ["ice", "water"], "base_power":34, "ap_cost":28, "effect": "damage", "can_aoe": False},
 {"id": "ice_earth_magic_lv2_permafrost_spear", "name": "Permafrost Spear", "description": "A spear of ice and stone.", "ability_type": "magic", "level":2, "elements": ["ice", "earth"], "base_power":35, "ap_cost":29, "effect": "damage", "can_aoe": False},
 {"id": "ice_light_magic_lv2_crystal_flash", "name": "Crystal Flash", "description": "A bright, freezing shard.", "ability_type": "magic", "level":2, "elements": ["ice", "light"], "base_power":33, "ap_cost":27, "effect": "damage", "can_aoe": False},
 {"id": "ice_dark_magic_lv2_shadowfrost_bolt", "name": "Shadowfrost Bolt", "description": "A biting bolt wrapped in gloom.", "ability_type": "magic", "level":2, "elements": ["ice", "dark"], "base_power":34, "ap_cost":28, "effect": "damage", "can_aoe": False},

 {"id": "fire_earth_magic_lv2_magma_javelin", "name": "Magma Javelin", "description": "A molten javelin of force.", "ability_type": "magic", "level":2, "elements": ["fire", "earth"], "base_power":36, "ap_cost":29, "effect": "damage", "can_aoe": False},
 {"id": "fire_air_magic_lv2_embersurge_gale", "name": "Embersurge Gale", "description": "A flaming gale of cutting heat.", "ability_type": "magic", "level":2, "elements": ["fire", "air"], "base_power":33, "ap_cost":27, "effect": "damage", "can_aoe": False},
 {"id": "fire_light_magic_lv2_solar_spike", "name": "Solar Spike", "description": "A spike of condensed solar fire.", "ability_type": "magic", "level":2, "elements": ["fire", "light"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},

 {"id": "earth_water_magic_lv2_mudslide", "name": "Mudslide", "description": "A bogged bolt that corrodes defenses.", "ability_type": "magic", "level":2, "elements": ["earth", "water"], "base_power":33, "ap_cost":27, "effect": "damage", "can_aoe": False},
 {"id": "earth_light_magic_lv2_prism_shard", "name": "Prism Shard", "description": "A radiant stone projectile.", "ability_type": "magic", "level":2, "elements": ["earth", "light"], "base_power":35, "ap_cost":29, "effect": "damage", "can_aoe": False},
 {"id": "earth_dark_magic_lv2_sinkhole", "name": "Sinkhole", "description": "The ground collapses in a finite area.", "ability_type": "magic", "level":2, "elements": ["earth", "dark"], "base_power":35, "ap_cost":29, "effect": "damage", "can_aoe": False},

 {"id": "air_water_magic_lv2_slicing_drizzle", "name": "Slicing Drizzle", "description": "A rain of razor droplets.", "ability_type": "magic", "level":2, "elements": ["air", "water"], "base_power":34, "ap_cost":28, "effect": "damage", "can_aoe": False},
 {"id": "air_light_magic_lv2_starbreeze", "name": "Starbreeze", "description": "A twinkling gust that slices.", "ability_type": "magic", "level":2, "elements": ["air", "light"], "base_power":35, "ap_cost":29, "effect": "damage", "can_aoe": False},
 {"id": "air_dark_magic_lv2_night_wind", "name": "Night Wind", "description": "A shadowy gust that chills the soul.", "ability_type": "magic", "level":2, "elements": ["air", "dark"], "base_power":32, "ap_cost":25, "effect": "damage", "can_aoe": False},
 {"id": "water_light_magic_lv2_luminous_tide", "name": "Luminous Tide", "description": "A tide infused with radiant force.", "ability_type": "magic", "level":2, "elements": ["water", "light"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},

 ## DAMAGE AOE (wide, high AP)
 {"id": "electric_electric_magic_lv2_chain_bolt", "name": "Chain Bolt", "description": "A crackling bolt that arcs widely.", "ability_type": "magic", "level":2, "elements": ["electric", "electric"], "base_power":30, "ap_cost":32, "effect": "damage", "can_aoe": True},
 {"id": "ice_ice_magic_lv2_glacier_burst", "name": "Glacier Burst", "description": "A wide burst of frigid shards.", "ability_type": "magic", "level":2, "elements": ["ice", "ice"], "base_power":29, "ap_cost":31, "effect": "damage", "can_aoe": True},
 {"id": "dark_dark_magic_lv2_umbra_storm", "name": "Umbra Storm", "description": "A storm of biting shadow.", "ability_type": "magic", "level":2, "elements": ["dark", "dark"], "base_power":31, "ap_cost":33, "effect": "damage", "can_aoe": True},
 {"id": "water_water_magic_lv2_deluge_burst", "name": "Deluge Burst", "description": "A concentrated watery onslaught.", "ability_type": "magic", "level":2, "elements": ["water", "water"], "base_power":29, "ap_cost":31, "effect": "damage", "can_aoe": True},
 {"id": "earth_earth_magic_lv2_quake_field", "name": "Quake Field", "description": "A rumbling field of rubble.", "ability_type": "magic", "level":2, "elements": ["earth", "earth"], "base_power":30, "ap_cost":32, "effect": "damage", "can_aoe": True},
 {"id": "fire_fire_magic_lv2_inferno_spread", "name": "Inferno Spread", "description": "A spreading wall of flame.", "ability_type": "magic", "level":2, "elements": ["fire", "fire"], "base_power":31, "ap_cost":33, "effect": "damage", "can_aoe": True},
 {"id": "air_air_magic_lv2_tempest_note", "name": "Tempest Note", "description": "A compressed gust that rends flesh.", "ability_type": "magic", "level":2, "elements": ["air", "air"], "base_power":30, "ap_cost":32, "effect": "damage", "can_aoe": True},

 ## CONTINUOUS DAMAGE (single-target, DoT)
 {"id": "electric_water_magic_lv2_corrosive_stream", "name": "Corrosive Stream", "description": "A charged drip that corrodes over time.", "ability_type": "magic", "level":2, "elements": ["electric", "water"], "base_power":2, "ap_cost":33, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
 {"id": "electric_earth_magic_lv2_ion_leech", "name": "Ion Leech", "description": "Slow arcing current that burns.", "ability_type": "magic", "level":2, "elements": ["electric", "earth"], "base_power":2, "ap_cost":34, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
 {"id": "light_dark_magic_lv2_twilight_bleed", "name": "Twilight Bleed", "description": "A subtle wound that saps life.", "ability_type": "magic", "level":2, "elements": ["light", "dark"], "base_power":1, "ap_cost":33, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
 {"id": "earth_air_magic_lv2_sandstream", "name": "Sandstream", "description": "A gritty flow that grinds defenses.", "ability_type": "magic", "level":2, "elements": ["earth", "air"], "base_power":2, "ap_cost":34, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
 {"id": "ice_fire_magic_lv2_frostbrand_burn", "name": "Frostbrand Burn", "description": "Cold ember that slowly damages.", "ability_type": "magic", "level":2, "elements": ["ice", "fire"], "base_power":3, "ap_cost":35, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
 {"id": "fire_water_magic_lv2_steaming_wound", "name": "Steaming Wound", "description": "Scalding seep that continues to hurt.", "ability_type": "magic", "level":2, "elements": ["fire", "water"], "base_power":3, "ap_cost":35, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
 {"id": "ice_air_magic_lv2_chill_drift", "name": "Chill Drift", "description": "Icy eddy that chills over time.", "ability_type": "magic", "level":2, "elements": ["ice", "air"], "base_power":1, "ap_cost":30, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},

 ## CONTINUOUS DAMAGE AOE (area DoT / lingering fields)
 {"id": "fire_dark_magic_lv2_ember_mire", "name": "Ember Mire", "description": "A smoky field of searing malice.", "ability_type": "magic", "level":2, "elements": ["fire", "dark"], "base_power":1, "ap_cost":45, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True},
 {"id": "water_dark_magic_lv2_abyssal_tide", "name": "Abyssal Tide", "description": "A dark tide that lingers and erodes.", "ability_type": "magic", "level":2, "elements": ["water", "dark"], "base_power":1, "ap_cost":45, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True},
 {"id": "air_dark_magic_lv2_gloom_vortex", "name": "Gloom Vortex", "description": "A voided gust that saps vigor.", "ability_type": "magic", "level":2, "elements": ["air", "dark"], "base_power":1, "ap_cost":45, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True},
 {"id": "electric_air_magic_lv2_storm_caltrops", "name": "Storm Caltrops", "description": "Electrified caltrops that shock a field.", "ability_type": "magic", "level":2, "elements": ["electric", "air"], "base_power":1, "ap_cost":45, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True},


 ##NON-PLAYER ABILITIES
 {"id": "lv2_hostile_ability_fire_earth_magic_pyroclasm", "name": "Pyroclasm", "description": "A volcanic eruption of molten rock.", "ability_type": "magic", "level":2, "elements": ["fire", "earth"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True, "non_player_ability": True},
 {"id": "lv2_hostile_ability_dark_electric_magic_abyssal_storm", "name": "Abyssal Storm", "description": "A storm of shadow and electricity.", "ability_type": "magic", "level":2, "elements": ["dark", "electric"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True, "non_player_ability": True},
 {"id": "lv2_hostile_ability_water_electric_magic_maelstrom_burst", "name": "Maelstrom Burst", "description": "A swirling burst of water and electricity.", "ability_type": "magic", "level":2, "elements": ["water", "electric"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True, "non_player_ability": True},
 {"id": "lv2_hostile_ability_ice_light_magic_frost_nova", "name": "Frost Nova", "description": "A burst of freezing light.", "ability_type": "magic", "level":2, "elements": ["ice", "light"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True, "non_player_ability": True},
 {"id": "lv2_hostile_ability_ice_light_magic_stellar_fall", "name": "Stellar Fall", "description": "A shower of icy light shards.", "ability_type": "magic", "level":2, "elements": ["ice", "light"], "base_power":30, "ap_cost":30, "effect": "damage", "can_aoe": True, "non_player_ability": True},
 {"id": "lv2_hostile_ability_water_dark_magic_gloom_tide", "name": "Gloom Tide", "description": "A tide of shadowy water.", "ability_type": "magic", "level":2, "elements": ["water", "dark"], "base_power":30, "ap_cost":30, "effect": "damage", "can_aoe": True, "non_player_ability": True},
 {"id": "lv2_hostile_ability_fire_fire_magic_magma_surge", "name": "Magma Surge", "description": "A surge of molten fire.", "ability_type": "magic", "level":2, "elements": ["fire", "fire"], "base_power":30, "ap_cost":30, "effect": "damage", "can_aoe": True, "non_player_ability": True},
]