"""
FAITH ABILITIES  ARE  BASED ON MYTHICAL PRAYERS TO GODS AND DIETIES... AND THOSE ANSWERS
they channel divine energy to heal, buff, cure statuses... they can also call down holy damage upon foes
some lore for faith in a neo noir fantasy setting is created with these abilities

BENEFICIAL_PLAYER_ABILITY_EFFECTS = [
    "heal",
    "status",
    "*_buff",
    "revive"
    "cure",
]

HARMFUL_STATUS_EFFECTS = {""elemental_debuff",
                          "attack_debuff",
                          "defense_debuff",
                          "intelligence_debuff",
                          "strength_debuff",
                          "dexterity_debuff",
                          "constitution_debuff"," *_debuff
                          "petrify",
                          "stun",
                          "sleep",
                          "confuse",
                          "silence",
                          "continuous_damage"}

35 Ability possibilities

ABILITY DIVISION
 DAMAGE: electric-electric, ice-ice, dark-dark, water-water, earth-earth, fire-fire, air-air <- 30 ap, basepwer 25, light-light <- 50ap basepower 40
 HEALING:  water-light (high power single target heal) 30 basepower 30ap, air-light (medium power aoe heal) 25 basepower 35ap
 STATUS CLEAN: silence (aoe), stun (aoe), debuff, continuous damage (aoe), sleep, confuse <- - all 20ap 0basepower
   - air-water,electric-light,ice-light,fire-light,earth-light, electric-dark
 BUFFS: elemental defense buffs all aoe 20ap 0 base power
   - fire-dark, water-dark, air-dark, electric-air, earth-dark, electric-water, electric-earth,  earth-air, ice-fire, fire-water, ice-air, electric-fire,electric-ice,ice-water,ice-earth,ice-dark,fire-earth,fire-air,earth-water
 STATUS EFFECT:light-dark (aoe confuse) 50ap 0basepower
"""

LEVEL_2_FAITH_ABILITY_SEEDS = [
 # --- faith ---
 ## DAMAGE (single-target, divine strikes)
 {"id": "electric_electric_faith_lv2_heavenly_rupture", "name": "Heavenly Rupture", "description": "A bolt of consecrated electricity.", "ability_type": "faith", "level":2, "elements": ["electric", "electric"], "base_power":25, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "ice_ice_faith_lv2_glacial_fury", "name": "Glacial Fury", "description": "A bitter, holy frost strike.", "ability_type": "faith", "level":2, "elements": ["ice", "ice"], "base_power":25, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "dark_dark_faith_lv2_oblivion_blast", "name": "Oblivion Blast", "description": "A sanctified shadow eruption.", "ability_type": "faith", "level":2, "elements": ["dark", "dark"], "base_power":25, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "water_water_faith_lv2_deluge_benedict", "name": "Deluge Benedict", "description": "A consecrated torrent strike.", "ability_type": "faith", "level":2, "elements": ["water", "water"], "base_power":25, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "earth_earth_faith_lv2_earthward_smite", "name": "Earthward Smite", "description": "A crushing holy stone strike.", "ability_type": "faith", "level":2, "elements": ["earth", "earth"], "base_power":25, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "fire_fire_faith_lv2_infernal_benediction", "name": "Infernal Benediction", "description": "A searing sacred conflagration.", "ability_type": "faith", "level":2, "elements": ["fire", "fire"], "base_power":25, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "air_air_faith_lv2_tempest_hymn", "name": "Tempest Hymn", "description": "A roaring hymn that rends air.", "ability_type": "faith", "level":2, "elements": ["air", "air"], "base_power":25, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "light_light_faith_lv2_seraphic_nova", "name": "Seraphic Nova", "description": "A blinding, overwhelming light.", "ability_type": "faith", "level":2, "elements": ["light", "light"], "base_power":40, "ap_cost":50, "effect": "damage", "can_aoe": True},

 ## HEALING
 {"id": "water_light_faith_lv2_holy_fountain", "name": "Holy Fountain", "description": "A potent single-target heal.", "ability_type": "faith", "level":2, "elements": ["water", "light"], "base_power":30, "ap_cost":30, "effect": "heal", "can_aoe": False},
 {"id": "air_light_faith_lv2_serene_breath", "name": "Serene Breath", "description": "A gentle AoE restorative breeze.", "ability_type": "faith", "level":2, "elements": ["air", "light"], "base_power":25, "ap_cost":35, "effect": "heal", "can_aoe": True},

 ## STATUS CLEAN (remove specific harmful statuses)
 {"id": "air_water_faith_lv2_mute_cleansing", "name": "Mute Cleansing", "description": "Cleansing gust that removes silence.", "ability_type": "faith", "level":2, "elements": ["air", "water"], "base_power":0, "ap_cost":20, "effect": "cure", "status_keys": ["silence"], "can_aoe": False},
 {"id": "electric_light_faith_lv2_shock_catharsis", "name": "Shock Catharsis", "description": "A purging spark that clears stuns.", "ability_type": "faith", "level":2, "elements": ["electric", "light"], "base_power":0, "ap_cost":20, "effect": "cure", "status_keys": ["stun"], "can_aoe": True},
 {"id": "ice_light_faith_lv2_purging_veil", "name": "Purging Veil", "description": "A frost veil that ends lingering wounds.", "ability_type": "faith", "level":2, "elements": ["ice", "light"], "base_power":0, "ap_cost":20, "effect": "cure", "status_keys": ["continuous_damage"], "can_aoe": True},
 {"id": "fire_light_faith_lv2_dream_awakening", "name": "Dream Awakening", "description": "A warming light that wakes the sleeping.", "ability_type": "faith", "level":2, "elements": ["fire", "light"], "base_power":0, "ap_cost":20, "effect": "cure", "status_keys": ["sleep"], "can_aoe": True},
 {"id": "earth_light_faith_lv2_clarify", "name": "Clarify", "description": "", "ability_type": "faith", "level":2, "elements": ["earth", "light"], "base_power":0, "ap_cost":20, "effect": "cure", "status_keys": ["confuse", "stun", "silence"], "can_aoe": False},
 {"id": "electric_dark_faith_lv2_purge_tide", "name": "Purge Tide", "description": "A black-light surge that strips debuffs.", "ability_type": "faith", "level":2, "elements": ["electric", "dark"], "base_power":0, "ap_cost":20, "effect": "cure", "status_keys": ["elemental_debuff"], "can_aoe": True},

 ## BUFFS (elemental defense buffs, AoE)
 {"id": "fire_dark_faith_lv2_sanctified_shield", "name": "Sanctified Shield", "description": "A dark-fire aura that bolsters defense.", "ability_type": "faith", "level":2, "elements": ["fire", "dark"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "water_dark_faith_lv2_ebbing_barrier", "name": "Ebbing Barrier", "description": "A shadowy water ward that defends.", "ability_type": "faith", "level":2, "elements": ["water", "dark"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "air_dark_faith_lv2_gloom_aegis", "name": "Gloom Aegis", "description": "A dark gale that steadies defenses.", "ability_type": "faith", "level":2, "elements": ["air", "dark"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "electric_air_faith_lv2_storm_ward", "name": "Storm Ward", "description": "An electric breeze that deflects harm.", "ability_type": "faith", "level":2, "elements": ["electric", "air"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "earth_dark_faith_lv2_tomb_shield", "name": "Tomb Shield", "description": "A dark-earth bulwark that hardens skin.", "ability_type": "faith", "level":2, "elements": ["earth", "dark"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "electric_water_faith_lv2_conductive_guard", "name": "Conductive Guard", "description": "A charged water ward that protects.", "ability_type": "faith", "level":2, "elements": ["electric", "water"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "electric_earth_faith_lv2_magnet_bastion", "name": "Magnet Bastion", "description": "Magnetic stones that reinforce armor.", "ability_type": "faith", "level":2, "elements": ["electric", "earth"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "earth_air_faith_lv2_skyward_bulwark", "name": "Skyward Bulwark", "description": "Stone-and-wind ward that resists hits.", "ability_type": "faith", "level":2, "elements": ["earth", "air"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "ice_fire_faith_lv2_glowfrost_barrier", "name": "Glowfrost Barrier", "description": "A chilly flame barrier that guards.", "ability_type": "faith", "level":2, "elements": ["ice", "fire"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "fire_water_faith_lv2_boiling_shield", "name": "Boiling Shield", "description": "A steamy ward that soothes and guards.", "ability_type": "faith", "level":2, "elements": ["fire", "water"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "ice_air_faith_lv2_frostwing_bastion", "name": "Frostwing Bastion", "description": "A wind-frost ward that steadies allies.", "ability_type": "faith", "level":2, "elements": ["ice", "air"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "electric_fire_faith_lv2_scorch_shroud", "name": "Scorch Shroud", "description": "A charged flame veil that defends.", "ability_type": "faith", "level":2, "elements": ["electric", "fire"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "electric_ice_faith_lv2_glace_wrap", "name": "Glace Wrap", "description": "A freezing charge that cushions blows.", "ability_type": "faith", "level":2, "elements": ["electric", "ice"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "ice_water_faith_lv2_marine_shield", "name": "Marine Shield", "description": "A watery frost barrier for allies.", "ability_type": "faith", "level":2, "elements": ["ice", "water"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "ice_earth_faith_lv2_permafrost_guard", "name": "Permafrost Guard", "description": "A stony cold ward that holds firm.", "ability_type": "faith", "level":2, "elements": ["ice", "earth"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "fire_earth_faith_lv2_molten_bulwark", "name": "Molten Bulwark", "description": "A magma-stone ward against harm.", "ability_type": "faith", "level":2, "elements": ["fire", "earth"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "fire_air_faith_lv2_ember_gale_shield", "name": "Ember Gale Shield", "description": "A burning wind shield that protects.", "ability_type": "faith", "level":2, "elements": ["fire", "air"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "earth_water_faith_lv2_silted_barrier", "name": "Silted Barrier", "description": "A mud-and-stone ward to guard allies.", "ability_type": "faith", "level":2, "elements": ["earth", "water"], "base_power":0, "ap_cost":20, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},

 ## STATUS EFFECT (special)
 {"id": "light_dark_faith_lv2_dusk_confessional", "name": "Dusk Confessional", "description": "A twilight rite that confuses foes.", "ability_type": "faith", "level":2, "elements": ["light", "dark"], "base_power":0, "ap_cost":50, "effect": "status", "status_keys": ["confuse"], "can_aoe": True},


 ##NON-PLAYER ABILITIES
 {"id": "lv2_hostile_ability_dark_dark_faith_void_veil", "name": "Void Veil", "description": "A dark shroud that confuses enemies.", "ability_type": "faith", "level":2, "elements": ["dark", "dark"], "base_power":1, "ap_cost":10, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "lv2_hostile_ability_air_water_faith_gale_of_silence", "name": "Gale of Silence", "description": "A wind that silences all foes.", "ability_type": "faith", "level":2, "elements": ["air", "water"], "base_power":1, "ap_cost":10, "effect": "status", "status_keys": ["silence"], "can_aoe": True, "non_player_ability": True},
 {"id": "lv2_hostile_ability_water_light_fae_glimmer", "name": "Glimmer", "description": "A shimmering light that confuses enemies.", "ability_type": "faith", "level":2, "elements": ["water", "light"], "base_power":1, "ap_cost":10, "effect": "status", "status_keys": ["confuse"], "can_aoe": False, "non_player_ability": True},
 {"id": "lv2_hostile_ability_dark_light_faith_calm_bleat", "name": "Calm Bleat", "description": "A soothing sound that confuses enemies.", "ability_type": "faith", "level":2, "elements": ["dark", "light"], "base_power":30, "ap_cost":30, "effect": "heal", "can_aoe": False, "non_player_ability": True},
 {"id": "lv2_hostile_ability_earth_air_faith_thornbind", "name": "Thornbind", "description": "A binding thorn that immobilizes foes.", "ability_type": "faith", "level":2, "elements": ["earth", "air"], "base_power":1, "ap_cost":10, "effect": "status", "status_keys": ["stun"], "can_aoe": False, "non_player_ability": True},
]