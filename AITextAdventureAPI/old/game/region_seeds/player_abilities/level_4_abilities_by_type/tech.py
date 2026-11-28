LEVEL_4_TECH_ABILITY_SEEDS = [

    # --- SINGLE TARGET DAMAGE (PHOTON / LASER / ANNIHILATION THEMES) ---
    {
        "id": "light_fire_electric_air_tech_lv4_photon_rupture",
        "name": "Photon Rupture",
        "description": "A hyper‑compressed photon lance detonates inside the target, rupturing matter from the inside out in a flash of white‑hot annihilation.",
        "ability_type": "tech",
        "level": 4,
        "elements": ["light", "fire", "electric", "air"],
        "base_power": 128,
        "ap_cost": 115,
        "effect": "damage",
        "can_aoe": False
    },

    {
        "id": "light_fire_earth_dark_tech_lv4_singularity_grenade",
        "name": "Singularity Grenade",
        "description": "A grenade that collapses into a micro‑void of light and shadow, crushing the target with photonic pressure before erupting in molten debris.",
        "ability_type": "tech",
        "level": 4,
        "elements": ["light", "fire", "earth", "dark"],
        "base_power": 130,
        "ap_cost": 118,
        "effect": "damage",
        "can_aoe": False
    },

    {
        "id": "light_ice_air_dark_tech_lv4_voidbeam_array",
        "name": "Voidbeam Array",
        "description": "A tri‑vector laser array fires converging beams of frozen light, carving through armor and leaving a trail of evaporated shadow.",
        "ability_type": "tech",
        "level": 4,
        "elements": ["light", "ice", "air", "dark"],
        "base_power": 122,
        "ap_cost": 110,
        "effect": "damage",
        "can_aoe": False
    },

    # --- AOE DAMAGE (PHOTON STORMS / LASER FIELDS / RADIANT DETONATIONS) ---
    {
        "id": "light_water_fire_air_tech_lv4_radiant_overdrive",
        "name": "Radiant Overdrive",
        "description": "A blinding overdrive burst floods the battlefield with superheated steam and refracted light, shredding everything in a chaotic photon storm.",
        "ability_type": "tech",
        "level": 4,
        "elements": ["light", "water", "fire", "air"],
        "base_power": 105,
        "ap_cost": 120,
        "effect": "damage",
        "can_aoe": True
    },

    {
        "id": "light_earth_electric_ice_tech_lv4_cryo_lumen_barrage",
        "name": "Cryo‑Lumen Barrage",
        "description": "A rotating cannon unleashes a barrage of freezing photon shells that explode into fractal ice‑light shrapnel across the field.",
        "ability_type": "tech",
        "level": 4,
        "elements": ["light", "earth", "electric", "ice"],
        "base_power": 105,
        "ap_cost": 122,
        "effect": "damage",
        "can_aoe": True
    },

    {
        "id": "light_fire_dark_electric_tech_lv4_neon_havoc",
        "name": "Neon Havoc",
        "description": "A cyberpunk riot of neon‑charged plasma arcs outward, burning silhouettes into the air as it tears through anyone caught in its radiant havoc.",
        "ability_type": "tech",
        "level": 4,
        "elements": ["light", "fire", "dark", "electric"],
        "base_power": 105,
        "ap_cost": 120,
        "effect": "damage",
        "can_aoe": True
    },

    # --- DEBUFF / STATUS (PHOTON DISRUPTION / RADIANT CORRUPTION) ---
    {
        "id": "light_dark_air_water_tech_lv4_lumen_disintegrator",
        "name": "Lumen Disintegrator",
        "description": "A sweeping beam of unstable light strips molecular cohesion, leaving enemies weakened, flickering, and half‑phased.",
        "ability_type": "tech",
        "level": 4,
        "elements": ["light", "dark", "air", "water"],
        "base_power": 20,
        "ap_cost": 120,
        "effect": "status",
        "status_keys": ["defense_debuff", "dexterity_debuff", "attack_debuff"],
        "can_aoe": True
    },

    {
        "id": "light_ice_dark_earth_tech_lv4_photon_decay",
        "name": "Photon Decay",
        "description": "A corrosive pulse of decaying light erodes neural signals, slowing reactions and leaving enemies disoriented and unstable.",
        "ability_type": "tech",
        "level": 4,
        "elements": ["light", "ice", "dark", "earth"],
        "base_power": 25,
        "ap_cost": 132,
        "effect": "status",
        "status_keys": ["dexterity_debuff", "stun", "constitution_debuff"],
        "can_aoe": True
    },

    # --- HIGH-END STATUS EFFECTS (PETRIFY / DISABLE / BLIND) ---
    {
        "id": "light_fire_air_dark_tech_lv4_photon_blackout",
        "name": "Photon Blackout",
        "description": "A flash of over‑saturated gamma light burns out matter leaving it petrified.",
        "ability_type": "tech",
        "level": 4,
        "elements": ["light", "fire", "air", "dark"],
        "base_power": 0,
        "ap_cost": 120,
        "effect": "status",
        "status_keys": ["petrify"],
        "can_aoe": True
    },

    {
        "id": "light_earth_water_electric_tech_lv4_radiant_lockdown",
        "name": "Radiant Lockdown",
        "description": "A lattice of electrified light crystallizes around targets, freezing them mid‑motion in a cage of shimmering force.",
        "ability_type": "tech",
        "level": 4,
        "elements": ["light", "earth", "water", "electric"],
        "base_power": 2,
        "ap_cost": 125,
        "effect": "status",
        "status_keys": ["stun", "silence"],
        "can_aoe": True
    },

    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    {"id": "electric_water_ice_air_tech_lv4_storm_cell_projector", "name": "Storm Cell Projector", "description": "Seeds a miniature thunderstorm over the enemy line.", "ability_type": "tech", "level": 4, "elements": ["electric", "water", "ice", "air"], "base_power": 103, "ap_cost": 118, "effect": "damage", "can_aoe": True},
    {"id": "ice_water_earth_fire_tech_lv4_thermal_shock_drill", "name": "Thermal Shock Drill", "description": "A drill bit cycled between red-hot and supercooled until the target cracks.", "ability_type": "tech", "level": 4, "elements": ["ice", "water", "earth", "fire"], "base_power": 125, "ap_cost": 104, "effect": "damage", "can_aoe": False},
    {"id": "earth_electric_water_air_tech_lv4_magnetic_mire_field", "name": "Magnetic Mire Field", "description": "An electromagnetic field that turns the ground beneath the enemy to sucking mud.", "ability_type": "tech", "level": 4, "elements": ["earth", "electric", "water", "air"], "base_power": 5, "ap_cost": 120, "effect": "status", "status_keys": ["dexterity_debuff", "defense_debuff", "elemental_debuff", "attack_debuff"], "can_aoe": True},
    {"id": "fire_earth_ice_dark_tech_lv4_bunker_buster", "name": "Bunker Buster", "description": "A shaped charge that burrows in before it detonates.", "ability_type": "tech", "level": 4, "elements": ["fire", "earth", "ice", "dark"], "base_power": 123, "ap_cost": 101, "effect": "damage", "can_aoe": False},
    {"id": "water_fire_ice_electric_tech_lv4_pressure_cooker_mine", "name": "Pressure Cooker Mine", "description": "A mine that flash-boils its payload into a scalding blast.", "ability_type": "tech", "level": 4, "elements": ["water", "fire", "ice", "electric"], "base_power": 109, "ap_cost": 129, "effect": "damage", "can_aoe": True},
    {"id": "air_earth_water_ice_tech_lv4_climate_shield", "name": "Climate Shield", "description": "Deployable weather shielding that keeps the party safe from the elements.", "ability_type": "tech", "level": 4, "elements": ["air", "earth", "water", "ice"], "base_power": 0, "ap_cost": 115, "effect": "status", "status_keys": ["elemental_defense_buff", "defense_buff", "constitution_buff", "regen"], "can_aoe": True},
    {"id": "dark_electric_fire_dark_tech_lv4_blackout_virus", "name": "Blackout Virus", "description": "A virus that spreads through the enemy line and crashes everything: no casting, no movement, no thought.", "ability_type": "tech", "level": 4, "elements": ["dark", "electric", "fire", "dark"], "base_power": 5, "ap_cost": 148, "effect": "status", "status_keys": ["silence", "stun", "intelligence_debuff"], "can_aoe": True},

    # crux — hazard/damage: scans and debuffs the philosophically corrupt
    {"id": "debuff_the_wicked", "name": "Debuff the Wicked", "description": "Crux runs a cold diagnostic on the target and finds them logically inconsistent — he catalogues every contradiction in their form and systematically dismantles their ability to act, think, and defend.", "ability_type": "tech", "level": 4, "elements": ["dark", "electric", "ice", "air"], "base_power": 28, "ap_cost": 128, "effect": "status", "status_keys": ["intelligence_debuff", "attack_debuff", "defense_debuff", "constitution_debuff"], "can_aoe": False, "non_player_ability": True},
    {"id": "logic_collapse", "name": "Logic Collapse", "description": "Crux broadcasts a terminal contradiction across the entire field — every mind within range short-circuits as it attempts to process something that cannot be true, leaving them slowed, silenced, and unable to reason.", "ability_type": "tech", "level": 4, "elements": ["dark", "dark", "electric", "ice"], "base_power": 15, "ap_cost": 132, "effect": "status", "status_keys": ["intelligence_debuff", "silence", "dexterity_debuff"], "can_aoe": True, "non_player_ability": True},

]
