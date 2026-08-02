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
                          --- Level 2 distribution example ---
ABILITY DIVISION
 DAMAGE: electric-electric, ice-ice, dark-dark, water-water, earth-earth, fire-fire, air-air <- 30 ap, basepwer 25, light-light <- 50ap basepower 40
 HEALING:  water-light (high power single target heal) 30 basepower 30ap, air-light (medium power aoe heal) 25 basepower 35ap
 STATUS CLEAN: silence (aoe), stun (aoe), debuff, continuous damage (aoe), sleep, confuse <- - all 20ap 0basepower
   - air-water,electric-light,ice-light,fire-light,earth-light, electric-dark
 BUFFS: elemental defense buffs all aoe 20ap 0 base power
   - fire-dark, water-dark, air-dark, electric-air, earth-dark, electric-water, electric-earth,  earth-air, ice-fire, fire-water, ice-air, electric-fire,electric-ice,ice-water,ice-earth,ice-dark,fire-earth,fire-air,earth-water
 STATUS EFFECT:light-dark (aoe confuse) 50ap 0basepower

 120 total combinations... we'll use around 20
                          --- Level 3 distribution ---
"""

# Faith seeds extracted from level_3_player_ability_seeds
LEVEL_3_FAITH_SEEDS = [
   ##DAMAGE  faith damaging abilities are high cost low power   100 ap for 80 bp   or 90ap for 50bp
 {"id": "fire_ice_air_faith_lv3_invocation_of_zephyrus", "name": "Invocation of Zephyrus", "description": "A sacred invocation calling Zephyrus' burning breath to sear enemies.", "ability_type": "faith", "level":3, "elements": ["fire", "ice", "air"], "base_power":50, "ap_cost":90, "effect": "damage", "can_aoe": False},
 {"id": "ice_air_earth_faith_lv3_skadi_tremor", "name": "Skadi's Tremor", "description": "A prayer to Skadi that conjures a freezing quake to bind foes.", "ability_type": "faith", "level":3, "elements": ["ice", "air", "earth"], "base_power":50, "ap_cost":90, "effect": "damage", "can_aoe": False},
 {"id": "air_earth_electric_faith_lv3_raijin_verdict", "name": "Raijin's Verdict", "description": "A thunderous verdict from Raijin that rends the air with electric force.", "ability_type": "faith", "level":3, "elements": ["air", "earth", "electric"], "base_power":50, "ap_cost":90, "effect": "damage", "can_aoe": False},
 {"id": "earth_electric_water_faith_lv3_tlaloc_torrent", "name": "Tlaloc's Torrent", "description": "An invocation of Tlaloc that sends electrified deluge crashing over enemies.", "ability_type": "faith", "level":3, "elements": ["earth", "electric", "water"], "base_power":70, "ap_cost":100, "effect": "damage", "can_aoe": False},
 {"id": "electric_water_fire_faith_lv3_pele_tempest", "name": "Pele's Tempest", "description": "A volcanic invocation calling Pele's furious conflagration across the field.", "ability_type": "faith", "level":3, "elements": ["electric", "water", "fire"], "base_power":70, "ap_cost":100, "effect": "damage", "can_aoe": False},
 {"id": "water_fire_ice_faith_lv3_chione_embrace", "name": "Chione's Embrace", "description": "A sacred lullaby of Chione that freezes foes in burning ice.", "ability_type": "faith", "level":3, "elements": ["water", "fire", "ice"], "base_power":70, "ap_cost":100, "effect": "damage", "can_aoe": False},
 {"id": "light_light_light_faith_lv3_sols_radiance", "name": "Sol's Radiance", "description": "An exalted beam from the sun-god Sol that scorches all who stand opposed.", "ability_type": "faith", "level":3, "elements": ["light", "light", "light"], "base_power":90, "ap_cost":135, "effect": "damage", "can_aoe": True},
 {"id": "dark_dark_dark_faith_lv3_nyx_shadow_nova", "name": "Nyx's Shadow Nova", "description": "A divine implosion of night invoked by Nyx to rend the souls of enemies.", "ability_type": "faith", "level":3, "elements": ["dark", "dark", "dark"], "base_power":90, "ap_cost":135, "effect": "damage", "can_aoe": True},
 {"id": "electric_electric_electric_faith_lv3_thor_storm", "name": "Thor's Storm", "description": "A godly tempest called down by Thor that batters all foes with lightning.", "ability_type": "faith", "level":3, "elements": ["electric", "electric", "electric"], "base_power":90, "ap_cost":135, "effect": "damage", "can_aoe": True},
 {"id": "ice_ice_ice_faith_lv3_skadi_frostwave", "name": "Skadi's Frostwave", "description": "A sweeping frozen tide offered in Skadi's name that chills every enemy.", "ability_type": "faith", "level":3, "elements": ["ice", "ice", "ice"], "base_power":90, "ap_cost":135, "effect": "damage", "can_aoe": True},
 {"id": "water_water_water_faith_lv3_poseidon_wrath", "name": "Poseidon's Wrath", "description": "A titanic wave summoned by Poseidon to crush all foes.", "ability_type": "faith", "level":3, "elements": ["water", "water", "water"], "base_power":90, "ap_cost":135, "effect": "damage", "can_aoe": True},
 {"id": "earth_earth_earth_faith_lv3_gaia_earthshaker", "name": "Gaia's Earthshaker", "description": "A primal quake called by Gaia that shatters the ground and foes alike.", "ability_type": "faith", "level":3, "elements": ["earth", "earth", "earth"], "base_power":90, "ap_cost":135, "effect": "damage", "can_aoe": True},
 {"id": "fire_fire_fire_faith_lv3_vulcan_inferno", "name": "Vulcan's Inferno", "description": "A searing inferno blessed by Vulcan that consumes the battlefield.", "ability_type": "faith", "level":3, "elements": ["fire", "fire", "fire"], "base_power":90, "ap_cost":135, "effect": "damage", "can_aoe": True},
 {"id": "air_air_air_faith_lv3_aether_hurricane", "name": "Aether's Hurricane", "description": "A divine hurricane from Aether that rends the skies and smites all enemies.", "ability_type": "faith", "level":3, "elements": ["air", "air", "air"], "base_power":90, "ap_cost":135, "effect": "damage", "can_aoe": True},


   ##HEALING FAITH ABILITIES
 {"id": "light_light_air_faith_lv3_major_heal", "name": "Major Heal", "description": "Restore a large amount of HP.", "ability_type": "faith", "level":3, "elements": ["light", "light", "air"], "base_power":48, "ap_cost":100, "effect": "heal", "can_aoe": True},
 {"id": "light_light_light_faith_lv3_pure_resurgence", "name": "Pure Resurgence", "description": "A focused, powerful restorative beam that mends a single ally's grievous wounds.", "ability_type": "faith", "level":3, "elements": ["light", "light", "light"], "base_power":120, "ap_cost":120, "effect": "heal", "can_aoe": False},
   ##REVIVE FAITH ABILITIES
 {"id": "light_light_dark_faith_lv3_dusk_balm", "name": "Dusk Balm", "description": "A twilight balm that can restore life to a fallen ally.", "ability_type": "faith", "level":3, "elements": ["light", "light", "dark"], "base_power":25, "ap_cost":120, "effect": "revive", "can_aoe": False},
   ##STATUS CLEAN
 {"id": "light_dark_air_faith_lv3_silent_night", "name": "Silent Night", "description": "A hushed prayer that cleanses silence from all allies.", "ability_type": "faith", "level":3, "elements": ["light","dark","air"], "base_power":0, "ap_cost":80, "effect": "cure", "status_keys": ["silence"], "can_aoe": True},
 {"id": "light_dark_earth_faith_lv3_stone_release", "name": "Stone Release", "description": "A grounding chant that frees all allies from petrification.", "ability_type": "faith", "level":3, "elements": ["light","dark","earth"], "base_power":0, "ap_cost":80, "effect": "cure", "status_keys": ["petrify"], "can_aoe": True},
 {"id": "light_dark_light_faith_lv3_clarity_prayer", "name": "Clarity Prayer", "description": "A luminous prayer that clears confusion from all allies.", "ability_type": "faith", "level":3, "elements": ["light","dark","light"], "base_power":0, "ap_cost":80, "effect": "cure", "status_keys": ["confuse"], "can_aoe": True},


   #buff notes electric->water->fire->ice->air->earth->..electric      light<->dark
   #light + allies ie: light+fire+air, light+ice+earth. light+air+electric, light+earth+water, light+electric+fire, light+water+ice
   #dark + enemies ie: dark+fire+ice, dark+ice+air, dark+air+earth, dark+earth+electric, dark+electric+water, dark+water+fire
   #allies: water->ice+earth, electric->air+fire
   ##BUFFS    elemental defense buffs all  are 60ap
 {"id": "light_fire_air_faith_lv3_radiant_shield", "name": "Radiant Shield", "description": "A bright shield that bolsters allies' elemental defenses.", "ability_type": "faith", "level":3, "elements": ["light","fire","air"], "base_power":0, "ap_cost":60, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "light_ice_earth_faith_lv3_luminous_barrier", "name": "Luminous Barrier", "description": "A glowing barrier that enhances allies' elemental defenses.", "ability_type": "faith", "level":3, "elements": ["light","ice","earth"], "base_power":0, "ap_cost":60, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "light_air_electric_faith_lv3_solar_aegis", "name": "Solar Aegis", "description": "A solar aegis that fortifies allies' elemental defenses.", "ability_type": "faith", "level":3, "elements": ["light","air","electric"], "base_power":0, "ap_cost":60, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "light_earth_water_faith_lv3_divine_protection", "name": "Divine Protection", "description": "A divine protection that strengthens allies' elemental defenses.", "ability_type": "faith", "level":3, "elements": ["light","earth","water"], "base_power":0, "ap_cost":60, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "light_electric_fire_faith_lv3_luminous_guardian", "name": "Luminous Guardian", "description": "A radiant guardian that boosts allies' elemental defenses.", "ability_type": "faith", "level":3, "elements": ["light","electric","fire"], "base_power":0, "ap_cost":60, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "light_water_ice_faith_lv3_holy_shielding", "name": "Holy Shielding", "description": "A holy shielding that enhances allies' elemental defenses.", "ability_type": "faith", "level":3, "elements": ["light","water","ice"], "base_power":0, "ap_cost":60, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "dark_fire_ice_faith_lv3_shadow_barrier", "name": "Shadow Barrier", "description": "A dark barrier that strengthens allies' elemental defenses.", "ability_type": "faith", "level":3, "elements": ["dark","fire","ice"], "base_power":0, "ap_cost":60, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "dark_ice_air_faith_lv3_nightfall_shroud", "name": "Nightfall Shroud", "description": "A shroud of darkness that increases allies' elemental defenses.", "ability_type": "faith", "level":3, "elements": ["dark","ice","air"], "base_power":0, "ap_cost":60, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "dark_air_earth_faith_lv3_void_aegis", "name": "Void Aegis", "description": "A void aegis that strengthens allies' elemental defenses.", "ability_type": "faith", "level":3, "elements": ["dark","air","earth"], "base_power":0, "ap_cost":60, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "dark_earth_electric_faith_lv3_oblivion_shield", "name": "Oblivion Shield", "description": "An oblivion shield that strengthens allies' elemental defenses.", "ability_type": "faith", "level":3, "elements": ["dark","earth","electric"], "base_power":0, "ap_cost":60, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "dark_electric_water_faith_lv3_shadow_guardian", "name": "Shadow Guardian", "description": "A shadow guardian that strengthens allies' elemental defenses.", "ability_type": "faith", "level":3, "elements": ["dark","electric","water"], "base_power":0, "ap_cost":60, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "dark_water_fire_faith_lv3_dread_shielding", "name": "Dread Shielding", "description": "A dread shielding that strengthens allies' elemental defenses.", "ability_type": "faith", "level":3, "elements": ["dark","water","fire"], "base_power":0, "ap_cost":60, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "water_ice_earth_faith_lv3_aqua_fortitude", "name": "Aqua Fortitude", "description": "A watery chant that strengthens allies' elemental defenses.", "ability_type": "faith", "level":3, "elements": ["water","ice","earth"], "base_power":0, "ap_cost":90, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 {"id": "electric_air_fire_faith_lv3_thunderous_vigor", "name": "Thunderous Vigor", "description": "A stormy invocation that strengthens allies' elemental defenses.", "ability_type": "faith", "level":3, "elements": ["electric","air","fire"], "base_power":0, "ap_cost":90, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},


   ##STAT BUFFS
 {"id": "fire_fire_dark_faith_lv3_ember_benediction", "name": "Ember Benediction", "description": "A fervent chant that empowers allies.", "ability_type": "faith", "level":3, "elements": ["fire","fire","fire"], "base_power":0, "ap_cost":90, "effect": "status", "status_keys": ["attack_buff"], "can_aoe": True},
 {"id": "earth_earth_light_faith_lv3_strengthened_resolve", "name": "Strengthened Resolve", "description": "A call to the gods for fortified defenses.", "ability_type": "faith", "level":3, "elements": ["earth","earth","earth"], "base_power":0, "ap_cost":90, "effect": "status", "status_keys": ["defense_buff"], "can_aoe": True},
 {"id": "fire_air_water_faith_lv3_athena_wisdom", "name": "Athena's Wisdom", "description": "Invoke Athena to temper flame, gale and tide - granting allies heightened intellect and clarity.", "ability_type": "faith", "level":3, "elements": ["fire","air","water"], "base_power":0, "ap_cost":90, "effect": "status", "status_keys": ["intelligence_buff"], "can_aoe": True},
 {"id": "fire_electric_earth_faith_lv3_hephaestus_forge_might", "name": "Hephaestus' Forge-Might", "description": "A forge-benediction calling Hephaestus to temper sinew and steel, granting raw strength to allies.", "ability_type": "faith", "level":3, "elements": ["fire","electric","earth"], "base_power":0, "ap_cost":90, "effect": "status", "status_keys": ["strength_buff"], "can_aoe": True},
 {"id": "air_water_earth_faith_lv3_gaia_fortitude", "name": "Gaia's Fortitude", "description": "A primal supplication to Gaia that grounds allies with earth, water and wind, bolstering their constitution against harm.", "ability_type": "faith", "level":3, "elements": ["air","water","earth"], "base_power":0, "ap_cost":90, "effect": "status", "status_keys": ["constitution_buff"], "can_aoe": True},


   ##DEBUFF 1*aoe constitution debuff
 {"id": "light_dark_dark_faith_lv3_twilight_woe", "name": "Twilight Woe", "description": "A shadowy lament that weakens foes' constitution.", "ability_type": "faith", "level":3, "elements": ["light","dark","dark"], "base_power":0, "ap_cost":60, "effect": "status", "status_keys": ["constitution_debuff"], "can_aoe": True},

    ## NON PLAYER ABILITIES
  #glamour
  {"id": "suffocating_allure", "name": "Suffocating Allure", "description": "An aura of oppressive beauty radiates outward, closing the throats of all who behold it and stealing their voice.", "ability_type": "faith", "level": 3, "elements": ["light", "dark", "air"], "base_power": 0, "ap_cost": 85, "effect": "status", "status_keys": ["silence"], "can_aoe": True, "non_player_ability": True},
  {"id": "the_epic_you_never_were", "name": "The Epic You Never Were", "description": "Garbage drowns all in the suffocating truth of their own inadequacy — the grand story they told themselves collapses, sapping their will to strike.", "ability_type": "faith", "level": 3, "elements": ["dark", "dark", "earth"], "base_power": 22, "ap_cost": 96, "effect": "status", "status_keys": ["attack_debuff"], "can_aoe": True, "non_player_ability": True},
  # stigma - support role: identity replacement as hazard status
  {"id": "you_can_be_me", "name": "You Can Be Me", "description": "Stigma offers the most dangerous gift — her identity to replace your own. The target's mind fractures as it tries to hold two selves simultaneously.", "ability_type": "faith", "level": 3, "elements": ["dark", "light", "air"], "base_power": 0, "ap_cost": 90, "effect": "status", "status_keys": ["confuse"], "can_aoe": False, "non_player_ability": True},
  # pageant - hazard role: social obligation as silence
  {"id": "obligation_chain", "name": "Obligation Chain", "description": "Pageant wraps a single target in the invisible chains of every social debt they've ever owed — the weight of obligation silences them completely.", "ability_type": "faith", "level": 3, "elements": ["light", "dark", "air"], "base_power": 0, "ap_cost": 88, "effect": "status", "status_keys": ["silence"], "can_aoe": False, "non_player_ability": True},
  # edict - damage role: law as silence
  {"id": "the_letter_of_the_law", "name": "The Letter of the Law", "description": "Edict invokes the precise, unanswerable text of the oldest rule — all speech, all protest, all defiance is legally prohibited and physically impossible.", "ability_type": "faith", "level": 3, "elements": ["dark", "earth", "light"], "base_power": 0, "ap_cost": 92, "effect": "status", "status_keys": ["silence"], "can_aoe": True, "non_player_ability": True},
 ]
