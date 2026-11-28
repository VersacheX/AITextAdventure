#LEVEL1 Abilities can have1 element. there is1 ability per element and1 ability per ability type.
# ability types are: technique, spirit, magic, tech, skill
# elements are: fire, water, earth, air, light, dark, ice, electric
# ability type mappings to character and hostile stats:
# technique: strength, constitution...physical attack, physical defense
# spirit: intelligence, constitution...spiritual attack, spiritual defense; healing power; debuff power
# magic: intelligence...magical attack, magical defense; debuff power
# tech: intelligence, dexterity...tech attack, tech defense; debuff power
# skill: dexterity, strength...speed, critical hit rate; evasion

# Extracted from constants_other.py — abilities with "level":1
"""8 possibilities *5 ability types *2 abilities per element =80 level1 abilities """
LEVEL_1_PLAYER_ABILITY_SEEDS = [
 # --- Technique ---
  ##DAMAGE lvl 1 techniques cost 9ap, base power 12
 {"id": "fire_technique_lv1_scorch_slash", "name": "Scorch Slash", "description": "A quick fiery slash.", "ability_type": "technique", "level":1, "elements": ["fire"], "base_power":14, "ap_cost":9, "effect": "damage", "can_aoe": False},
 {"id": "ice_technique_lv1_frozen_slash", "name": "Frozen Slash", "description": "A quick cold slash.", "ability_type": "technique", "level":1, "elements": ["ice"], "base_power":14, "ap_cost":9, "effect": "damage", "can_aoe": False},
 {"id": "light_technique_lv1_radiant_slash", "name": "Radiant Slash", "description": "A shining cut that glints brightly.", "ability_type": "technique", "level":1, "elements": ["light"], "base_power":14, "ap_cost":9, "effect": "damage", "can_aoe": False},
 {"id": "dark_technique_lv1_night_claw", "name": "Night Claw", "description": "A vicious swipe from shadow.", "ability_type": "technique", "level":1, "elements": ["dark"], "base_power":14, "ap_cost":9, "effect": "damage", "can_aoe": False},
 {"id": "water_technique_lv1_slick_manuever", "name": "Slick Manuever", "description": "A flowing strike that knocks off balance.", "ability_type": "technique", "level":1, "elements": ["water"], "base_power":12, "ap_cost":8, "effect": "damage", "can_aoe": False},
  ##STATUS EFFECT   lvl status techniques 10ap - 10bp+status
 {"id": "air_technique_lv1_sonic_strike", "name": "Sonic Strike", "description": "An awe inspiring strike from above, that silences the enemy.", "ability_type": "technique", "level":1, "elements": ["air"], "base_power":1, "ap_cost":12, "effect": "status", "status_keys": ["silence"], "can_aoe": False},
 {"id": "electric_technique_lv1_stun_strike", "name": "Stun Strike", "description": "An awe inspiring strike from above, that stuns the enemy.", "ability_type": "technique", "level":1, "elements": ["electric"], "base_power":1, "ap_cost":13, "effect": "status", "status_keys": ["stun"], "can_aoe": False},
  ##BUFF lvl1 buff techniques cost 8ap, 0bp +status
 {"id": "earth_technique_lv1_armor_up", "name": "Arm Up", "description": "The strength of the earth strengthens fortitude and resolve", "ability_type": "technique", "level":1, "elements": ["earth"], "base_power":0, "ap_cost":7, "effect": "status", "status_keys": ["defense_buff", "constitution_buff"], "can_aoe": False},
  ##NEW: IMPLEMENTATION_SPEC_class_growth_elements.md 3.2 — fills the technique L1 earth-pool gap (Thorn)
 {"id": "earth_technique_lv1_stone_fist", "name": "Stone Fist", "description": "A rock-hard punch that hits like a falling boulder.", "ability_type": "technique", "level": 1, "elements": ["earth"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
   ##NEW: fills minimum-2nd-ability-per-element gaps for 2-element recruits (level-1 count floor of 4)
 {"id": "fire_technique_lv1_ember_thrust", "name": "Ember Thrust", "description": "A burning lunge that sears on contact.", "ability_type": "technique", "level": 1, "elements": ["fire"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
 {"id": "ice_technique_lv1_glacial_edge", "name": "Glacial Edge", "description": "A biting blade coated in rime.", "ability_type": "technique", "level": 1, "elements": ["ice"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
 {"id": "light_technique_lv1_sunray_cut", "name": "Sunray Cut", "description": "A blinding arc of radiant steel.", "ability_type": "technique", "level": 1, "elements": ["light"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
 {"id": "dark_technique_lv1_umbral_cleave", "name": "Umbral Cleave", "description": "A cleaving strike wreathed in shadow.", "ability_type": "technique", "level": 1, "elements": ["dark"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
 {"id": "water_technique_lv1_riptide_strike", "name": "Riptide Strike", "description": "A surging blow that drags like a current.", "ability_type": "technique", "level": 1, "elements": ["water"], "base_power": 12, "ap_cost": 8, "effect": "damage", "can_aoe": False},
 {"id": "air_technique_lv1_gale_thrust", "name": "Gale Thrust", "description": "A wind-driven lunge that strikes before it's seen.", "ability_type": "technique", "level": 1, "elements": ["air"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
 {"id": "electric_technique_lv1_volt_slash", "name": "Volt Slash", "description": "A crackling slash charged with static force.", "ability_type": "technique", "level": 1, "elements": ["electric"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},








 # --- Spirit ---
   ##HEALING
   # # single target heal lvl1 spirit heals cost 10ap, 12bp
 {"id": "light_spirit_lv1_minor_heal", "name": "Minor Heal", "description": "Restore a small amount of HP.", "ability_type": "spirit", "level":1, "elements": ["light"], "base_power":9, "ap_cost":10, "effect": "heal", "can_aoe": True},

   ## STATUS CLEAN
 {"id": "water_spirit_lv1_mending_streams", "name": "Mending Streams", "description": "A soothing stream that cures damaging ailments.", "ability_type": "spirit", "level":1, "elements": ["water"], "base_power":0, "ap_cost":8, "effect": "cure", "status_keys": ["continuous_damage"], "can_aoe": False},
 {"id": "light_spirit_lv1_glimmer", "name": "Glimmer", "description": "Holy light returns life to the petrified.", "ability_type": "spirit", "level":1, "elements": ["light"], "base_power":0, "ap_cost":15, "effect": "cure", "status_keys": ["stun"], "can_aoe": False},

   ##BUFFS lvel1 faith buffs cost )10ap aoe)8ap, 0bp +status
 {"id": "electric_spirit_lv1_shock_blessing", "name": "Shock Blessing", "description": "A fervent blessing that imbues weapons with the power of electricity.", "ability_type": "spirit", "level":1, "elements": ["electric"], "base_power":0, "ap_cost":8, "effect": "status", "status_keys": ["elemental_attack_buff"], "can_aoe": True},
 {"id": "fire_spirit_lv1_warmth_blessing", "name": "Warmth Blessing", "description": "A fervent blessing that imbues weapons with the power of fire.", "ability_type": "spirit", "level":1, "elements": ["fire"], "base_power":0, "ap_cost":8, "effect": "status", "status_keys": ["elemental_attack_buff"], "can_aoe": True},
 {"id": "earth_spirit_lv1_earthen_blessing", "name": "Earthen Blessing", "description": "A small grounding aid that bolsters elemental defenses.", "ability_type": "spirit", "level":1, "elements": ["earth"], "base_power":0, "ap_cost":8, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
 
 {"id": "air_spirit_lv1_zephyr_bless", "name": "Zephyr Bless", "description": "A swift blessing that quickens allies and sharpens reflexes.", "ability_type": "spirit", "level":1, "elements": ["air"], "base_power":0, "ap_cost":7, "effect": "status", "status_keys": ["dexterity_buff"], "can_aoe": False}, 
   ##DEBUFFS
 {"id": "dark_spirit_lv1_shade_whisper", "name": "Blessings from Below", "description": "An unsettling benediction that saps vitality and resilience.", "ability_type": "spirit", "level":1, "elements": ["dark"], "base_power":2, "ap_cost":8, "effect": "status", "status_keys": ["constitution_debuff"], "can_aoe": False},
   ##STATUS EFFECT
 {"id": "light_spirit_lv1_convert", "name": "Convert", "description": "Words of the devout to convert their listeners.", "ability_type": "spirit", "level":1, "elements": ["light"], "base_power":0, "ap_cost":13, "effect": "status", "status_keys": ["confuse"], "can_aoe": False},

   ##NEW: IMPLEMENTATION_SPEC_class_growth_elements.md 3.2 — fills spirit L1 water/ice gaps (Ripple, Rynn)
 {"id": "water_spirit_lv1_rain_blessing", "name": "Rain Blessing", "description": "A gentle rain that slowly restores the weary.", "ability_type": "spirit", "level": 1, "elements": ["water"], "base_power": 0, "ap_cost": 9, "effect": "status", "status_keys": ["regen"], "can_aoe": False},
 {"id": "ice_spirit_lv1_frost_salve", "name": "Frost Salve", "description": "A cooling touch that numbs pain and closes wounds.", "ability_type": "spirit", "level": 1, "elements": ["ice"], "base_power": 9, "ap_cost": 10, "effect": "heal", "can_aoe": False},

   ##NEW: fills minimum-2nd-ability-per-element gaps for 2-element recruits (level-1 count floor of 4)
 {"id": "electric_spirit_lv1_static_ward", "name": "Static Ward", "description": "A crackling barrier that sharpens reflexes.", "ability_type": "spirit", "level": 1, "elements": ["electric"], "base_power": 0, "ap_cost": 8, "effect": "status", "status_keys": ["dexterity_buff"], "can_aoe": True},
 {"id": "fire_spirit_lv1_ember_ward", "name": "Ember Ward", "description": "A warming blessing that mends minor wounds.", "ability_type": "spirit", "level": 1, "elements": ["fire"], "base_power": 9, "ap_cost": 10, "effect": "heal", "can_aoe": False},
 {"id": "earth_spirit_lv1_stone_mend", "name": "Stone Mend", "description": "A grounding rite that knits flesh like packed clay.", "ability_type": "spirit", "level": 1, "elements": ["earth"], "base_power": 9, "ap_cost": 10, "effect": "heal", "can_aoe": False},
 {"id": "air_spirit_lv1_windsong", "name": "Windsong", "description": "A lilting hymn carried on the breeze that soothes wounds.", "ability_type": "spirit", "level": 1, "elements": ["air"], "base_power": 9, "ap_cost": 10, "effect": "heal", "can_aoe": False},
 {"id": "dark_spirit_lv1_gloom_ward", "name": "Gloom Ward", "description": "A shadowed rite that wards against creeping rot.", "ability_type": "spirit", "level": 1, "elements": ["dark"], "base_power": 0, "ap_cost": 8, "effect": "cure", "status_keys": ["continuous_damage"], "can_aoe": False},
 {"id": "ice_spirit_lv1_rime_guard", "name": "Rime Guard", "description": "A chilling ward that fortifies the body against harm.", "ability_type": "spirit", "level": 1, "elements": ["ice"], "base_power": 0, "ap_cost": 8, "effect": "status", "status_keys": ["defense_buff"], "can_aoe": True},







 # --- Magic ---
   ##DAMAGE
 {"id": "dark_magic_lv1_shadow_tendril", "name": "Shadow Tendril", "description": "A shadow tendril that whips at the victim rending their flesh..", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":9, "ap_cost":10, "effect": "damage", "can_aoe": True},
 {"id": "electric_magic_lv1_fireball", "name": "Lightning Bolt", "description": "A bolt of lightning.", "ability_type": "magic", "level":1, "elements": ["electric"], "base_power":9, "ap_cost":10, "effect": "damage", "can_aoe": True}, 
 {"id": "ice_magic_lv1_frostbolt", "name": "Frostbolt", "description": "A shard of ice that chills.", "ability_type": "magic", "level":1, "elements": ["ice"], "base_power":9, "ap_cost":10, "effect": "damage", "can_aoe": True},
 {"id": "water_magic_lv1_spray_shard", "name": "Acid Rain", "description": "A searing rain.", "ability_type": "magic", "level":1, "elements": ["water"], "base_power": 9, "ap_cost":10, "effect": "damage", "can_aoe": True}, 
 {"id": "fire_magic_lv1_fireball", "name": "Fireball", "description": "A ball of searing flame.", "ability_type": "magic", "level":1, "elements": ["fire"], "base_power":9, "ap_cost":10, "effect": "damage", "can_aoe": True},
 {"id": "air_magic_lv1_shredding_gust", "name": "Shredding Gust", "description": "A of shredding wind.", "ability_type": "magic", "level":1, "elements": ["air"], "base_power":9, "ap_cost":10, "effect": "damage", "can_aoe": True},
 {"id": "earth_magic_lv1_tremor", "name": "Tremor", "description": "The ground quakes and tears.", "ability_type": "magic", "level":1, "elements": ["earth"], "base_power":9, "ap_cost":10, "effect": "damage", "can_aoe": True},
  ##NEW: IMPLEMENTATION_SPEC_class_growth_elements.md 3.2 — fills the magic L1 fire gap (Veyr)
 {"id": "fire_magic_lv1_cinder_flick", "name": "Cinder Flick", "description": "A flicked ember that bursts on contact.", "ability_type": "magic", "level": 1, "elements": ["fire"], "base_power": 10, "ap_cost": 9, "effect": "damage", "can_aoe": False},

   ##NEW: fills minimum-2nd-ability-per-element gaps for 2-element recruits (level-1 count floor of 4)
 {"id": "dark_magic_lv1_void_lance", "name": "Void Lance", "description": "A lance of condensed darkness.", "ability_type": "magic", "level": 1, "elements": ["dark"], "base_power": 9, "ap_cost": 10, "effect": "damage", "can_aoe": True},
 {"id": "electric_magic_lv1_static_burst", "name": "Static Burst", "description": "A crackling burst of raw current.", "ability_type": "magic", "level": 1, "elements": ["electric"], "base_power": 9, "ap_cost": 10, "effect": "damage", "can_aoe": True},
 {"id": "ice_magic_lv1_hailstorm", "name": "Hailstorm", "description": "A sudden squall of jagged ice.", "ability_type": "magic", "level": 1, "elements": ["ice"], "base_power": 9, "ap_cost": 10, "effect": "damage", "can_aoe": True},
 {"id": "water_magic_lv1_tidal_surge", "name": "Tidal Surge", "description": "A surging wave that crashes over foes.", "ability_type": "magic", "level": 1, "elements": ["water"], "base_power": 9, "ap_cost": 10, "effect": "damage", "can_aoe": True},
 {"id": "air_magic_lv1_cyclone_spark", "name": "Cyclone Spark", "description": "A whirling vortex that tears at everything nearby.", "ability_type": "magic", "level": 1, "elements": ["air"], "base_power": 9, "ap_cost": 10, "effect": "damage", "can_aoe": True},
 {"id": "earth_magic_lv1_stone_spike", "name": "Stone Spike", "description": "Jagged spikes erupt from the ground.", "ability_type": "magic", "level": 1, "elements": ["earth"], "base_power": 9, "ap_cost": 10, "effect": "damage", "can_aoe": True},
 {"id": "light_magic_lv1_radiant_burst", "name": "Radiant Burst", "description": "A searing burst of pure light.", "ability_type": "magic", "level": 1, "elements": ["light"], "base_power": 9, "ap_cost": 10, "effect": "damage", "can_aoe": True},
 {"id": "light_magic_lv1_holy_flare", "name": "Holy Flare", "description": "A flaring sigil of consecrated light.", "ability_type": "magic", "level": 1, "elements": ["light"], "base_power": 10, "ap_cost": 9, "effect": "damage", "can_aoe": False},



 # --- Tech (technology) ---
   ##DAMAGE
 {"id": "ice_tech_lv1_crio_refraction", "name": "Crio-Refraction", "description": "A small device that focuses a beam of absolute-0 energy.", "ability_type": "tech", "level":1, "elements": ["ice"], "base_power":13, "ap_cost":9, "effect": "damage", "can_aoe": False},
 ##DAMAGAE AOE
 {"id": "dark_tech_lv1_void_grenade", "name": "Void Grenade", "description": "A grenade that explodes on impact releasing a dark energy..", "ability_type": "tech", "level":1, "elements": ["dark"], "base_power":12, "ap_cost":12, "effect": "damage", "can_aoe": True},
 ##DEBUFF
 {"id": "fire_tech_lv1_flux_dampener", "name": "Flux Dampener", "description": "Launches a disruptive pulse that corrodes fiery resonance in targets.", "ability_type": "tech", "level":1, "elements": ["fire"], "base_power":0, "ap_cost":8, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
 {"id": "water_tech_lv1_tide_entangler", "name": "Tide Entangler", "description": "Releases a tangling circuit that interferes with aqueous energy matrices.", "ability_type": "tech", "level":1, "elements": ["water"], "base_power":0, "ap_cost":8, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
 {"id": "air_tech_lv1_gale_jammer", "name": "Gale Jammer", "description": "Generates turbulent interference that destabilizes wind-aligned defenses.", "ability_type": "tech", "level":1, "elements": ["air"], "base_power":0, "ap_cost":8, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
 {"id": "earth_tech_lv1_fault_inhibitor", "name": "Fault Inhibitor", "description": "Deploys a grounding field that disrupts earthen bonding.", "ability_type": "tech", "level":1, "elements": ["earth"], "base_power":0, "ap_cost":8, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
 ##STATUS EFFECT
 {"id": "electric_tech_lv1_taze_charge", "name": "Taze Charge", "description": "A tongued projectile that stuns the target.", "ability_type": "tech", "level":1, "elements": ["electric"], "base_power":0, "ap_cost":13, "effect": "status", "status_keys": ["stun"], "can_aoe": False},
 {"id": "light_tech_lv1_aerial_drone", "name": "Aerial Drone", "description": "A small drone that scans enemies.", "ability_type": "tech", "level":1, "elements": ["light"], "base_power":0, "ap_cost":7, "effect": "status", "status_keys": ["scanned"], "can_aoe": True},

   ##NEW: fills minimum-2nd-ability-per-element gaps for 2-element recruits (level-1 count floor of 4)
 {"id": "ice_tech_lv1_frost_turret", "name": "Frost Turret", "description": "A deployable turret that fires absolute-zero rounds.", "ability_type": "tech", "level": 1, "elements": ["ice"], "base_power": 13, "ap_cost": 9, "effect": "damage", "can_aoe": False},
 {"id": "dark_tech_lv1_shadow_drone", "name": "Shadow Drone", "description": "A cloaked drone that strikes from the dark.", "ability_type": "tech", "level": 1, "elements": ["dark"], "base_power": 12, "ap_cost": 12, "effect": "damage", "can_aoe": True},
 {"id": "fire_tech_lv1_thermal_charge", "name": "Thermal Charge", "description": "A payload that detonates in searing heat.", "ability_type": "tech", "level": 1, "elements": ["fire"], "base_power": 13, "ap_cost": 9, "effect": "damage", "can_aoe": False},
 {"id": "water_tech_lv1_hydro_blaster", "name": "Hydro Blaster", "description": "A pressurized jet of water.", "ability_type": "tech", "level": 1, "elements": ["water"], "base_power": 13, "ap_cost": 9, "effect": "damage", "can_aoe": False},
 {"id": "air_tech_lv1_pulse_cannon", "name": "Pulse Cannon", "description": "A concussive blast of compressed air.", "ability_type": "tech", "level": 1, "elements": ["air"], "base_power": 13, "ap_cost": 9, "effect": "damage", "can_aoe": False},
 {"id": "earth_tech_lv1_seismic_charge", "name": "Seismic Charge", "description": "A buried charge that ruptures the ground.", "ability_type": "tech", "level": 1, "elements": ["earth"], "base_power": 12, "ap_cost": 12, "effect": "damage", "can_aoe": True},
 {"id": "electric_tech_lv1_arc_blaster", "name": "Arc Blaster", "description": "A focused arc of lethal current.", "ability_type": "tech", "level": 1, "elements": ["electric"], "base_power": 13, "ap_cost": 9, "effect": "damage", "can_aoe": False},
 {"id": "light_tech_lv1_photon_beam", "name": "Photon Beam", "description": "A focused beam of coherent light.", "ability_type": "tech", "level": 1, "elements": ["light"], "base_power": 13, "ap_cost": 9, "effect": "damage", "can_aoe": False},




 # --- Skill ---
   ##DAMAGE
 {"id": "dark_skill_lv1_creeping_strike", "name": "Creeping Strike", "description": "A sly strike that bites at defenses.", "ability_type": "skill", "level":1, "elements": ["dark"], "base_power":8, "ap_cost":5, "effect": "damage", "can_aoe": False},
 {"id": "ice_skill_lv1_ice_shuriken", "name": "Ice Shuriken", "description": "A cold and calculated shuriken.", "ability_type": "skill", "level":1, "elements": ["ice"], "base_power":8, "ap_cost":5, "effect": "damage", "can_aoe": False},
 {"id": "water_skill_lv1_flowing_fists", "name": "Flowing Fists", "description": "A successive flurry of strikes.", "ability_type": "skill", "level":1, "elements": ["water"], "base_power":8, "ap_cost":5, "effect": "damage", "can_aoe": False},
 {"id": "electric_skill_lv1_lightning_strike", "name": "Lightning Strike", "description": "A technique so fast it cracks the air as it's performed.", "ability_type": "skill", "level":1, "elements": ["electric"], "base_power":8, "ap_cost":5, "effect": "damage", "can_aoe": False},
 {"id": "light_skill_lv1_holy_fists", "name": "Holy Fists", "description": "Successive strikes performed at blinding speed.", "ability_type": "skill", "level":1, "elements": ["light"], "base_power":8, "ap_cost":5, "effect": "damage", "can_aoe": False},
 
   ##DEBUFF
 {"id": "air_skill_lv1_smoke_bomb", "name": "Smoke Bomb", "description": "Create a cloud of choking particulate that slows and disorients.", "ability_type": "skill", "level":1, "elements": ["air"], "base_power":3, "ap_cost":12, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": False}, 
 {"id": "earth_skill_lv1_soporific_veil", "name": "Soporific Veil", "description": "Unleashes a choking, mineral-laden veil inspired by clandestine smoke powders.", "ability_type": "skill", "level":1, "elements": ["earth"], "base_power":5, "ap_cost":8, "effect": "status", "status_keys": ["intelligence_debuff"], "can_aoe": False},
 {"id": "fire_skill_lv1_debilitating_ember_smoke", "name": "Debilitating Ember-Smoke", "description": "Generates an enfeebling cloud.", "ability_type": "skill", "level":1, "elements": ["fire"], "base_power":5, "ap_cost":8, "effect": "status", "status_keys": ["strength_debuff"], "can_aoe": False},
 
   ##STATUS EFFECT
 {"id": "dark_skill_lv1_tranq_dart", "name": "Tranq Dart", "description": "A dart tipped with a sedative.", "ability_type": "skill", "level":1, "elements": ["dark"], "base_power":1, "ap_cost":11, "effect": "status", "status_keys": ["sleep"], "can_aoe": False},

   ##NEW: IMPLEMENTATION_SPEC_class_growth_elements.md 3.2 — fills the skill L1 air gap (Nia)
 {"id": "air_skill_lv1_wind_jab", "name": "Wind Jab", "description": "A jab so fast it carries a gust behind it.", "ability_type": "skill", "level": 1, "elements": ["air"], "base_power": 9, "ap_cost": 8, "effect": "damage", "can_aoe": False},

   ##NEW: fills the skill L1 fire damage gap (Dare) — only a status (debuff) fire skill existed at L1
 {"id": "fire_skill_lv1_ember_fang", "name": "Ember Fang", "description": "A sharp, searing strike that bites like a coal-hot fang.", "ability_type": "skill", "level": 1, "elements": ["fire"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},

   ##NEW: fills minimum-2nd-ability-per-element gaps for 2-element recruits (level-1 count floor of 4)
 {"id": "ice_skill_lv1_frostbite_fang", "name": "Frostbite Fang", "description": "A biting strike that numbs the wound with frost.", "ability_type": "skill", "level": 1, "elements": ["ice"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},
 {"id": "water_skill_lv1_riptide_kick", "name": "Riptide Kick", "description": "A sweeping kick that drags like an undertow.", "ability_type": "skill", "level": 1, "elements": ["water"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},
 {"id": "electric_skill_lv1_static_fist", "name": "Static Fist", "description": "A punch that crackles with built-up charge.", "ability_type": "skill", "level": 1, "elements": ["electric"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},
 {"id": "light_skill_lv1_radiant_step", "name": "Radiant Step", "description": "A flashing, blindingly fast strike.", "ability_type": "skill", "level": 1, "elements": ["light"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},
  {"id": "earth_skill_lv1_boulder_hook", "name": "Boulder Hook", "description": "A heavy hooking blow backed by raw earthen weight.", "ability_type": "skill", "level": 1, "elements": ["earth"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},

    # --- Element fill (IMPLEMENTATION_SPEC_ability_fill.md) ---
    # Technique: fire
    {"id": "fire_technique_lv1_ember_haymaker", "name": "Ember Haymaker", "description": "A wild, swinging punch wreathed in sparks.", "ability_type": "technique", "level": 1, "elements": ["fire"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "fire_technique_lv1_brushfire_sweep", "name": "Brushfire Sweep", "description": "A low, burning arc of the blade that catches every foe in reach.", "ability_type": "technique", "level": 1, "elements": ["fire"], "base_power": 11, "ap_cost": 12, "effect": "damage", "can_aoe": True},
    {"id": "fire_technique_lv1_kindled_grip", "name": "Kindled Grip", "description": "Heat floods the arms so every swing lands heavier.", "ability_type": "technique", "level": 1, "elements": ["fire"], "base_power": 0, "ap_cost": 6, "effect": "status", "status_keys": ["strength_buff"], "can_aoe": False},
    # Technique: water
    {"id": "water_technique_lv1_undertow_throw", "name": "Undertow Throw", "description": "Grab, twist and drag the foe under like a riptide.", "ability_type": "technique", "level": 1, "elements": ["water"], "base_power": 13, "ap_cost": 8, "effect": "damage", "can_aoe": False},
    {"id": "water_technique_lv1_breaker_sweep", "name": "Breaker Sweep", "description": "A wide swing that crashes through the enemy line like surf.", "ability_type": "technique", "level": 1, "elements": ["water"], "base_power": 11, "ap_cost": 12, "effect": "damage", "can_aoe": True},
    {"id": "water_technique_lv1_tidewall_stance", "name": "Tidewall Stance", "description": "Settle low and let elemental blows roll off like water off stone.", "ability_type": "technique", "level": 1, "elements": ["water"], "base_power": 0, "ap_cost": 9, "effect": "status", "status_keys": ["elemental_defense_buff", "defense_buff"], "can_aoe": False},
    # Technique: earth
    {"id": "earth_technique_lv1_quake_stomp", "name": "Quake Stomp", "description": "A heel-drop that cracks the ground under every nearby foe.", "ability_type": "technique", "level": 1, "elements": ["earth"], "base_power": 11, "ap_cost": 12, "effect": "damage", "can_aoe": True},
    {"id": "earth_technique_lv1_guard_breaker", "name": "Guard Breaker", "description": "A shoulder-driven blow that splits the foe's guard and footing.", "ability_type": "technique", "level": 1, "elements": ["earth"], "base_power": 1, "ap_cost": 9, "effect": "status", "status_keys": ["defense_debuff", "strength_debuff"], "can_aoe": False},
    # Technique: air
    {"id": "air_technique_lv1_windshear_cut", "name": "Windshear Cut", "description": "A rising slash that rides the updraft it creates.", "ability_type": "technique", "level": 1, "elements": ["air"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "air_technique_lv1_cyclone_spin", "name": "Cyclone Spin", "description": "A full-body spin, blade out, that buffets everyone close.", "ability_type": "technique", "level": 1, "elements": ["air"], "base_power": 11, "ap_cost": 12, "effect": "damage", "can_aoe": True},
    {"id": "air_technique_lv1_tailwind_footwork", "name": "Tailwind Footwork", "description": "Light, wind-carried steps that speed every follow-up.", "ability_type": "technique", "level": 1, "elements": ["air"], "base_power": 0, "ap_cost": 7, "effect": "status", "status_keys": ["dexterity_buff"], "can_aoe": False},
    # Technique: ice
    {"id": "ice_technique_lv1_rime_hammer", "name": "Rime Hammer", "description": "A frost-crusted hammer blow that rings like cracking ice.", "ability_type": "technique", "level": 1, "elements": ["ice"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "ice_technique_lv1_shatterline", "name": "Shatterline", "description": "A ground strike that sends a line of ice spikes through the enemy ranks.", "ability_type": "technique", "level": 1, "elements": ["ice"], "base_power": 11, "ap_cost": 12, "effect": "damage", "can_aoe": True},
    {"id": "ice_technique_lv1_numbing_chop", "name": "Numbing Chop", "description": "A cold chop to the wrist that leaves the foe slow and clumsy.", "ability_type": "technique", "level": 1, "elements": ["ice"], "base_power": 1, "ap_cost": 8, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": False},
    # Technique: electric
    {"id": "electric_technique_lv1_spark_knuckle", "name": "Spark Knuckle", "description": "A charged punch that crackles on impact.", "ability_type": "technique", "level": 1, "elements": ["electric"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "electric_technique_lv1_arc_cleave", "name": "Arc Cleave", "description": "A wide cleave that throws arcs between every foe it touches.", "ability_type": "technique", "level": 1, "elements": ["electric"], "base_power": 11, "ap_cost": 12, "effect": "damage", "can_aoe": True},
    {"id": "electric_technique_lv1_live_wire", "name": "Live Wire", "description": "Static hums through the muscles and quickens every swing.", "ability_type": "technique", "level": 1, "elements": ["electric"], "base_power": 0, "ap_cost": 10, "effect": "status", "status_keys": ["attack_buff", "strength_buff"], "can_aoe": False},
    # Technique: light
    {"id": "light_technique_lv1_dawn_thrust", "name": "Dawn Thrust", "description": "A straight thrust that flares like first light.", "ability_type": "technique", "level": 1, "elements": ["light"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "light_technique_lv1_halo_sweep", "name": "Halo Sweep", "description": "A circling cut that leaves a ring of light around you.", "ability_type": "technique", "level": 1, "elements": ["light"], "base_power": 11, "ap_cost": 12, "effect": "damage", "can_aoe": True},
    {"id": "light_technique_lv1_blinding_bash", "name": "Blinding Bash", "description": "A shield bash with a flash of light that leaves the foe swinging blind.", "ability_type": "technique", "level": 1, "elements": ["light"], "base_power": 1, "ap_cost": 11, "effect": "status", "status_keys": ["attack_debuff", "dexterity_debuff"], "can_aoe": False},
    # Technique: dark
    {"id": "dark_technique_lv1_shade_rend", "name": "Shade Rend", "description": "A tearing slash that seems to come from the foe's own shadow.", "ability_type": "technique", "level": 1, "elements": ["dark"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "dark_technique_lv1_umbral_reap", "name": "Umbral Reap", "description": "A scything swing that reaps through the dark.", "ability_type": "technique", "level": 1, "elements": ["dark"], "base_power": 11, "ap_cost": 12, "effect": "damage", "can_aoe": True},
    {"id": "dark_technique_lv1_menacing_roar", "name": "Menacing Roar", "description": "A roar from the dark that saps the nerve of every foe.", "ability_type": "technique", "level": 1, "elements": ["dark"], "base_power": 1, "ap_cost": 12, "effect": "status", "status_keys": ["attack_debuff", "strength_debuff"], "can_aoe": True},
    # Spirit: fire
    {"id": "fire_spirit_lv1_hearth_mend", "name": "Hearth Mend", "description": "Warmth from a remembered hearth that closes small wounds.", "ability_type": "spirit", "level": 1, "elements": ["fire"], "base_power": 10, "ap_cost": 10, "effect": "heal", "can_aoe": False},
    {"id": "fire_spirit_lv1_wakefire", "name": "Wakefire", "description": "A spark of warmth that shakes an ally out of unnatural sleep.", "ability_type": "spirit", "level": 1, "elements": ["fire"], "base_power": 0, "ap_cost": 10, "effect": "cure", "status_keys": ["sleep"], "can_aoe": False},
    {"id": "fire_spirit_lv1_censure_flame", "name": "Censure Flame", "description": "A judging flame that singes the wicked.", "ability_type": "spirit", "level": 1, "elements": ["fire"], "base_power": 11, "ap_cost": 7, "effect": "damage", "can_aoe": False},
    # Spirit: water
    {"id": "water_spirit_lv1_wellspring_mist", "name": "Wellspring Mist", "description": "A cool mist that eases the whole party's wounds.", "ability_type": "spirit", "level": 1, "elements": ["water"], "base_power": 8, "ap_cost": 11, "effect": "heal", "can_aoe": True},
    {"id": "water_spirit_lv1_baptismal_rinse", "name": "Baptismal Rinse", "description": "A rinse of holy water that washes curses and weakness from an ally.", "ability_type": "spirit", "level": 1, "elements": ["water"], "base_power": 0, "ap_cost": 7, "effect": "cure", "status_keys": ["debuff"], "can_aoe": False},
    # Spirit: earth
    {"id": "earth_spirit_lv1_rooted_vigil", "name": "Rooted Vigil", "description": "A slow chant that roots the party's feet and steadies their breath.", "ability_type": "spirit", "level": 1, "elements": ["earth"], "base_power": 0, "ap_cost": 7, "effect": "status", "status_keys": ["constitution_buff"], "can_aoe": True},
    {"id": "earth_spirit_lv1_clay_poultice", "name": "Clay Poultice", "description": "A poultice of blessed clay pressed into an ally's wounds.", "ability_type": "spirit", "level": 1, "elements": ["earth"], "base_power": 10, "ap_cost": 10, "effect": "heal", "can_aoe": False},
    {"id": "earth_spirit_lv1_grounding_touch", "name": "Grounding Touch", "description": "A hand on the shoulder that grounds a stunned ally back into the fight.", "ability_type": "spirit", "level": 1, "elements": ["earth"], "base_power": 0, "ap_cost": 13, "effect": "cure", "status_keys": ["stun"], "can_aoe": False},
    # Spirit: air
    {"id": "air_spirit_lv1_second_wind", "name": "Second Wind", "description": "A deep, guided breath that restores a little vigor.", "ability_type": "spirit", "level": 1, "elements": ["air"], "base_power": 10, "ap_cost": 10, "effect": "heal", "can_aoe": False},
    {"id": "air_spirit_lv1_clearing_breeze", "name": "Clearing Breeze", "description": "A fresh breeze that blows the fog out of a confused mind.", "ability_type": "spirit", "level": 1, "elements": ["air"], "base_power": 0, "ap_cost": 15, "effect": "cure", "status_keys": ["confuse"], "can_aoe": False},
    {"id": "air_spirit_lv1_gust_rebuke", "name": "Gust Rebuke", "description": "A sharp rebuke carried on a gust of spirit-wind.", "ability_type": "spirit", "level": 1, "elements": ["air"], "base_power": 11, "ap_cost": 7, "effect": "damage", "can_aoe": False},
    # Spirit: ice
    {"id": "ice_spirit_lv1_snowfall_hush", "name": "Snowfall Hush", "description": "A hush like falling snow that lulls a foe to sleep.", "ability_type": "spirit", "level": 1, "elements": ["ice"], "base_power": 1, "ap_cost": 11, "effect": "status", "status_keys": ["sleep"], "can_aoe": False},
    {"id": "ice_spirit_lv1_frost_ward", "name": "Frost Ward", "description": "A thin rime of blessed frost over each ally that turns aside elemental harm.", "ability_type": "spirit", "level": 1, "elements": ["ice"], "base_power": 0, "ap_cost": 8, "effect": "status", "status_keys": ["elemental_defense_buff"], "can_aoe": True},
    {"id": "ice_spirit_lv1_rime_smite", "name": "Rime Smite", "description": "A cold rebuke that bites at the soul.", "ability_type": "spirit", "level": 1, "elements": ["ice"], "base_power": 11, "ap_cost": 7, "effect": "damage", "can_aoe": False},
    # Spirit: electric
    {"id": "electric_spirit_lv1_quickening_spark", "name": "Quickening Spark", "description": "A spark of spirit that jolts an ally into quicker action.", "ability_type": "spirit", "level": 1, "elements": ["electric"], "base_power": 0, "ap_cost": 7, "effect": "status", "status_keys": ["dexterity_buff"], "can_aoe": False},
    {"id": "electric_spirit_lv1_static_smite", "name": "Static Smite", "description": "A crack of judgment that leaps from palm to foe.", "ability_type": "spirit", "level": 1, "elements": ["electric"], "base_power": 11, "ap_cost": 7, "effect": "damage", "can_aoe": False},
    {"id": "electric_spirit_lv1_voice_spark", "name": "Voice Spark", "description": "A small charge to the throat that restores a silenced ally's voice.", "ability_type": "spirit", "level": 1, "elements": ["electric"], "base_power": 0, "ap_cost": 12, "effect": "cure", "status_keys": ["silence"], "can_aoe": False},
    # Spirit: light
    {"id": "light_spirit_lv1_sanctuary_glow", "name": "Sanctuary Glow", "description": "A soft glow that slowly restores the whole party.", "ability_type": "spirit", "level": 1, "elements": ["light"], "base_power": 0, "ap_cost": 10, "effect": "status", "status_keys": ["regen"], "can_aoe": True},
    # Spirit: dark
    {"id": "dark_spirit_lv1_mourners_hex", "name": "Mourner's Hex", "description": "A mourning curse that makes the foe's blows feel heavy and pointless.", "ability_type": "spirit", "level": 1, "elements": ["dark"], "base_power": 1, "ap_cost": 9, "effect": "status", "status_keys": ["attack_debuff", "strength_debuff"], "can_aoe": False},
    {"id": "dark_spirit_lv1_shadow_mend", "name": "Shadow Mend", "description": "Borrowed shadow quietly knits an ally's wounds closed.", "ability_type": "spirit", "level": 1, "elements": ["dark"], "base_power": 10, "ap_cost": 10, "effect": "heal", "can_aoe": False},
    {"id": "dark_spirit_lv1_grave_smite", "name": "Grave Smite", "description": "A cold touch from beyond that drains the warmth from a foe.", "ability_type": "spirit", "level": 1, "elements": ["dark"], "base_power": 11, "ap_cost": 7, "effect": "damage", "can_aoe": False},
    # Magic: fire
    {"id": "fire_magic_lv1_ember_hex", "name": "Ember Hex", "description": "A smoldering curse that keeps burning long after the spell ends.", "ability_type": "magic", "level": 1, "elements": ["fire"], "base_power": 1, "ap_cost": 10, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
    {"id": "fire_magic_lv1_searing_ray", "name": "Searing Ray", "description": "A thin ray of flame that bores into one target.", "ability_type": "magic", "level": 1, "elements": ["fire"], "base_power": 10, "ap_cost": 6, "effect": "damage", "can_aoe": False},
    # Magic: water
    {"id": "water_magic_lv1_riptide_bolt", "name": "Riptide Bolt", "description": "A spiraling bolt of pressurized water.", "ability_type": "magic", "level": 1, "elements": ["water"], "base_power": 10, "ap_cost": 6, "effect": "damage", "can_aoe": False},
    {"id": "water_magic_lv1_drowsy_mist", "name": "Drowsy Mist", "description": "A damp, heavy mist that drags the target into sleep.", "ability_type": "magic", "level": 1, "elements": ["water"], "base_power": 1, "ap_cost": 10, "effect": "status", "status_keys": ["sleep"], "can_aoe": False},
    {"id": "water_magic_lv1_brine_hex", "name": "Brine Hex", "description": "A salt-sting curse that leaves the target soaked and exposed.", "ability_type": "magic", "level": 1, "elements": ["water"], "base_power": 1, "ap_cost": 7, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": False},
    # Magic: earth
    {"id": "earth_magic_lv1_stone_bullet", "name": "Stone Bullet", "description": "A shard of stone flung at bone-breaking speed.", "ability_type": "magic", "level": 1, "elements": ["earth"], "base_power": 10, "ap_cost": 6, "effect": "damage", "can_aoe": False},
    {"id": "earth_magic_lv1_quicksand_hex", "name": "Quicksand Hex", "description": "The ground softens under the target, slowing every step and loosening its guard.", "ability_type": "magic", "level": 1, "elements": ["earth"], "base_power": 1, "ap_cost": 11, "effect": "status", "status_keys": ["dexterity_debuff", "defense_debuff"], "can_aoe": False},
    {"id": "earth_magic_lv1_dust_veil", "name": "Dust Veil", "description": "A swirl of enchanted dust that dulls every foe's elemental guard.", "ability_type": "magic", "level": 1, "elements": ["earth"], "base_power": 1, "ap_cost": 9, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
    # Magic: air
    {"id": "air_magic_lv1_wind_blade", "name": "Wind Blade", "description": "A crescent of compressed air that slices one target.", "ability_type": "magic", "level": 1, "elements": ["air"], "base_power": 10, "ap_cost": 6, "effect": "damage", "can_aoe": False},
    {"id": "air_magic_lv1_vacuum_hush", "name": "Vacuum Hush", "description": "Pulls the air from the target's lungs and steals its voice.", "ability_type": "magic", "level": 1, "elements": ["air"], "base_power": 1, "ap_cost": 12, "effect": "status", "status_keys": ["silence"], "can_aoe": False},
    {"id": "air_magic_lv1_tailwind", "name": "Tailwind", "description": "A friendly wind at an ally's back that quickens every move.", "ability_type": "magic", "level": 1, "elements": ["air"], "base_power": 0, "ap_cost": 7, "effect": "status", "status_keys": ["dexterity_buff"], "can_aoe": False},
    # Magic: ice
    {"id": "ice_magic_lv1_ice_needle", "name": "Ice Needle", "description": "A needle of ice that strikes faster than the eye can follow.", "ability_type": "magic", "level": 1, "elements": ["ice"], "base_power": 10, "ap_cost": 6, "effect": "damage", "can_aoe": False},
    {"id": "ice_magic_lv1_chilling_hex", "name": "Chilling Hex", "description": "A creeping frost that stiffens the target's joints.", "ability_type": "magic", "level": 1, "elements": ["ice"], "base_power": 1, "ap_cost": 8, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": False},
    {"id": "ice_magic_lv1_sleet_spray", "name": "Sleet Spray", "description": "A spray of stinging sleet that pelts every foe.", "ability_type": "magic", "level": 1, "elements": ["ice"], "base_power": 9, "ap_cost": 10, "effect": "damage", "can_aoe": True},
    # Magic: electric
    {"id": "electric_magic_lv1_spark_bolt", "name": "Spark Bolt", "description": "A quick, needle-thin bolt of lightning.", "ability_type": "magic", "level": 1, "elements": ["electric"], "base_power": 10, "ap_cost": 6, "effect": "damage", "can_aoe": False},
    {"id": "electric_magic_lv1_static_hex", "name": "Static Hex", "description": "A static charge that locks the target's muscles for a moment.", "ability_type": "magic", "level": 1, "elements": ["electric"], "base_power": 1, "ap_cost": 13, "effect": "status", "status_keys": ["stun"], "can_aoe": False},
    {"id": "electric_magic_lv1_ion_field", "name": "Ion Field", "description": "A crackling field that strips elemental guard from every foe.", "ability_type": "magic", "level": 1, "elements": ["electric"], "base_power": 1, "ap_cost": 9, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
    # Magic: light
    {"id": "light_magic_lv1_lumen_dart", "name": "Lumen Dart", "description": "A dart of condensed light.", "ability_type": "magic", "level": 1, "elements": ["light"], "base_power": 10, "ap_cost": 6, "effect": "damage", "can_aoe": False},
    {"id": "light_magic_lv1_solar_flare", "name": "Solar Flare", "description": "A flash of searing sunlight that scorches every foe.", "ability_type": "magic", "level": 1, "elements": ["light"], "base_power": 9, "ap_cost": 10, "effect": "damage", "can_aoe": True},
    {"id": "light_magic_lv1_dazzle", "name": "Dazzle", "description": "A burst of shifting colors that leaves the target confused.", "ability_type": "magic", "level": 1, "elements": ["light"], "base_power": 1, "ap_cost": 15, "effect": "status", "status_keys": ["confuse"], "can_aoe": False},
    {"id": "light_magic_lv1_clarity", "name": "Clarity", "description": "A clear, bright calm that sharpens an ally's focus.", "ability_type": "magic", "level": 1, "elements": ["light"], "base_power": 0, "ap_cost": 6, "effect": "status", "status_keys": ["intelligence_buff"], "can_aoe": False},
    # Magic: dark
    {"id": "dark_magic_lv1_shadow_bolt", "name": "Shadow Bolt", "description": "A bolt of solid shadow.", "ability_type": "magic", "level": 1, "elements": ["dark"], "base_power": 10, "ap_cost": 6, "effect": "damage", "can_aoe": False},
    {"id": "dark_magic_lv1_dread_hex", "name": "Dread Hex", "description": "A whispered dread that clouds the target's mind and weakens its strikes.", "ability_type": "magic", "level": 1, "elements": ["dark"], "base_power": 1, "ap_cost": 9, "effect": "status", "status_keys": ["intelligence_debuff", "attack_debuff"], "can_aoe": False},
    {"id": "dark_magic_lv1_gloom_rot", "name": "Gloom Rot", "description": "A creeping rot that eats at the target over time.", "ability_type": "magic", "level": 1, "elements": ["dark"], "base_power": 1, "ap_cost": 10, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},
    # Tech: fire
    {"id": "fire_tech_lv1_flare_pistol", "name": "Flare Pistol", "description": "A signal pistol loaded with a burning magnesium round.", "ability_type": "tech", "level": 1, "elements": ["fire"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "fire_tech_lv1_incendiary_mine", "name": "Incendiary Mine", "description": "A pressure mine that bursts into a ring of fire.", "ability_type": "tech", "level": 1, "elements": ["fire"], "base_power": 12, "ap_cost": 13, "effect": "damage", "can_aoe": True},
    {"id": "fire_tech_lv1_thermal_plating", "name": "Thermal Plating", "description": "Heat-treated plates clamp onto an ally's armor.", "ability_type": "tech", "level": 1, "elements": ["fire"], "base_power": 0, "ap_cost": 9, "effect": "status", "status_keys": ["defense_buff", "elemental_defense_buff"], "can_aoe": False},
    # Tech: water
    {"id": "water_tech_lv1_hydro_jet", "name": "Hydro Jet", "description": "A pressure washer turned weapon.", "ability_type": "tech", "level": 1, "elements": ["water"], "base_power": 12, "ap_cost": 8, "effect": "damage", "can_aoe": False},
    {"id": "water_tech_lv1_coolant_mist", "name": "Coolant Mist", "description": "A coolant mist laced with med-gel that slowly closes the party's wounds.", "ability_type": "tech", "level": 1, "elements": ["water"], "base_power": 0, "ap_cost": 10, "effect": "status", "status_keys": ["regen"], "can_aoe": True},
    {"id": "water_tech_lv1_slick_spray", "name": "Slick Spray", "description": "A spray of slick polymer that leaves the target slipping.", "ability_type": "tech", "level": 1, "elements": ["water"], "base_power": 1, "ap_cost": 8, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": False},
    # Tech: earth
    {"id": "earth_tech_lv1_rivet_gun", "name": "Rivet Gun", "description": "A heavy-duty rivet gun fired at point-blank range.", "ability_type": "tech", "level": 1, "elements": ["earth"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "earth_tech_lv1_barricade_drop", "name": "Barricade Drop", "description": "Deployable barricades snap up in front of the party.", "ability_type": "tech", "level": 1, "elements": ["earth"], "base_power": 0, "ap_cost": 11, "effect": "status", "status_keys": ["defense_buff", "constitution_buff"], "can_aoe": True},
    {"id": "earth_tech_lv1_tremor_charge", "name": "Tremor Charge", "description": "A shaped charge that rattles the ground under the enemy line.", "ability_type": "tech", "level": 1, "elements": ["earth"], "base_power": 12, "ap_cost": 13, "effect": "damage", "can_aoe": True},
    # Tech: air
    {"id": "air_tech_lv1_pneumatic_bolt", "name": "Pneumatic Bolt", "description": "A compressed-air bolt that punches clean through light armor.", "ability_type": "tech", "level": 1, "elements": ["air"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "air_tech_lv1_gust_turret", "name": "Gust Turret", "description": "A small turbine turret that blasts the area with grit-laden wind.", "ability_type": "tech", "level": 1, "elements": ["air"], "base_power": 12, "ap_cost": 13, "effect": "damage", "can_aoe": True},
    {"id": "air_tech_lv1_jet_boots", "name": "Jet Boots", "description": "Strap-on thrusters that make an ally faster for a while.", "ability_type": "tech", "level": 1, "elements": ["air"], "base_power": 0, "ap_cost": 7, "effect": "status", "status_keys": ["dexterity_buff"], "can_aoe": False},
    # Tech: ice
    {"id": "ice_tech_lv1_cryo_grenade", "name": "Cryo Grenade", "description": "A grenade that bursts into flash-frozen shrapnel.", "ability_type": "tech", "level": 1, "elements": ["ice"], "base_power": 12, "ap_cost": 14, "effect": "damage", "can_aoe": True},
    {"id": "ice_tech_lv1_cryo_clamp", "name": "Cryo Clamp", "description": "A clamp of liquid nitrogen that numbs the target's limbs.", "ability_type": "tech", "level": 1, "elements": ["ice"], "base_power": 1, "ap_cost": 13, "effect": "status", "status_keys": ["dexterity_debuff", "strength_debuff"], "can_aoe": False},
    {"id": "ice_tech_lv1_heat_sink", "name": "Heat Sink", "description": "A clip-on heat sink that soaks up elemental energy before it reaches an ally.", "ability_type": "tech", "level": 1, "elements": ["ice"], "base_power": 0, "ap_cost": 11, "effect": "status", "status_keys": ["elemental_defense_buff", "constitution_buff"], "can_aoe": False},
    # Tech: electric
    {"id": "electric_tech_lv1_shock_baton", "name": "Shock Baton", "description": "A baton that discharges on contact.", "ability_type": "tech", "level": 1, "elements": ["electric"], "base_power": 13, "ap_cost": 8, "effect": "damage", "can_aoe": False},
    {"id": "electric_tech_lv1_tesla_coil", "name": "Tesla Coil", "description": "A portable coil that arcs to everything nearby.", "ability_type": "tech", "level": 1, "elements": ["electric"], "base_power": 12, "ap_cost": 13, "effect": "damage", "can_aoe": True},
    {"id": "electric_tech_lv1_overcharge_cell", "name": "Overcharge Cell", "description": "A battery pack jacked into an ally's gear that boosts every system.", "ability_type": "tech", "level": 1, "elements": ["electric"], "base_power": 0, "ap_cost": 10, "effect": "status", "status_keys": ["attack_buff", "intelligence_buff"], "can_aoe": False},
    # Tech: light
    {"id": "light_tech_lv1_focus_laser", "name": "Focus Laser", "description": "A focused cutting laser.", "ability_type": "tech", "level": 1, "elements": ["light"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "light_tech_lv1_flashbang", "name": "Flashbang", "description": "A blinding, deafening charge that throws off the enemy line's aim and focus.", "ability_type": "tech", "level": 1, "elements": ["light"], "base_power": 1, "ap_cost": 12, "effect": "status", "status_keys": ["attack_debuff", "intelligence_debuff"], "can_aoe": True},
    {"id": "light_tech_lv1_targeting_laser", "name": "Targeting Laser", "description": "Paints the target with a laser so every hit finds a weak spot.", "ability_type": "tech", "level": 1, "elements": ["light"], "base_power": 1, "ap_cost": 9, "effect": "status", "status_keys": ["scanned", "defense_debuff"], "can_aoe": False},
    # Tech: dark
    {"id": "dark_tech_lv1_suppressed_shot", "name": "Suppressed Shot", "description": "A suppressed round fired from the shadows.", "ability_type": "tech", "level": 1, "elements": ["dark"], "base_power": 14, "ap_cost": 9, "effect": "damage", "can_aoe": False},
    {"id": "dark_tech_lv1_blackout_canister", "name": "Blackout Canister", "description": "Thick black smoke that leaves the enemy line stumbling blind.", "ability_type": "tech", "level": 1, "elements": ["dark"], "base_power": 1, "ap_cost": 12, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": True},
    {"id": "dark_tech_lv1_signal_jammer", "name": "Signal Jammer", "description": "Jams the target's comms and casting with white noise.", "ability_type": "tech", "level": 1, "elements": ["dark"], "base_power": 1, "ap_cost": 12, "effect": "status", "status_keys": ["silence"], "can_aoe": False},
    # Skill: fire
    {"id": "fire_skill_lv1_ember_kick", "name": "Ember Kick", "description": "A snapping kick that leaves a trail of sparks.", "ability_type": "skill", "level": 1, "elements": ["fire"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},
    {"id": "fire_skill_lv1_firecracker_toss", "name": "Firecracker Toss", "description": "A handful of firecrackers tossed at the enemy's feet.", "ability_type": "skill", "level": 1, "elements": ["fire"], "base_power": 7, "ap_cost": 8, "effect": "damage", "can_aoe": True},
    {"id": "fire_skill_lv1_kindled_reflexes", "name": "Kindled Reflexes", "description": "A quick breathing trick that heats the blood and speeds the hands.", "ability_type": "skill", "level": 1, "elements": ["fire"], "base_power": 0, "ap_cost": 7, "effect": "status", "status_keys": ["dexterity_buff"], "can_aoe": False},
    # Skill: water
    {"id": "water_skill_lv1_ripple_palm", "name": "Ripple Palm", "description": "A palm strike that sends a ripple through the target's body.", "ability_type": "skill", "level": 1, "elements": ["water"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},
    {"id": "water_skill_lv1_rain_of_needles", "name": "Rain of Needles", "description": "A fan of thin needles thrown like a sudden rain.", "ability_type": "skill", "level": 1, "elements": ["water"], "base_power": 7, "ap_cost": 8, "effect": "damage", "can_aoe": True},
    {"id": "water_skill_lv1_fluid_guard", "name": "Fluid Guard", "description": "Loose, flowing footwork that makes you hard to pin down.", "ability_type": "skill", "level": 1, "elements": ["water"], "base_power": 0, "ap_cost": 10, "effect": "status", "status_keys": ["defense_buff", "dexterity_buff"], "can_aoe": False},
    # Skill: earth
    {"id": "earth_skill_lv1_sling_stone", "name": "Sling Stone", "description": "A sling stone, aimed true.", "ability_type": "skill", "level": 1, "elements": ["earth"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},
    {"id": "earth_skill_lv1_caltrop_scatter", "name": "Caltrop Scatter", "description": "Iron caltrops scattered across the enemy's path.", "ability_type": "skill", "level": 1, "elements": ["earth"], "base_power": 7, "ap_cost": 8, "effect": "damage", "can_aoe": True},
    {"id": "earth_skill_lv1_dirt_in_the_eyes", "name": "Dirt in the Eyes", "description": "A fistful of grit flung at the face.", "ability_type": "skill", "level": 1, "elements": ["earth"], "base_power": 1, "ap_cost": 11, "effect": "status", "status_keys": ["attack_debuff", "dexterity_debuff"], "can_aoe": False},
    # Skill: air
    {"id": "air_skill_lv1_whirling_kick", "name": "Whirling Kick", "description": "A spinning kick that clips everyone in reach.", "ability_type": "skill", "level": 1, "elements": ["air"], "base_power": 7, "ap_cost": 8, "effect": "damage", "can_aoe": True},
    {"id": "air_skill_lv1_gust_feint", "name": "Gust Feint", "description": "A feint inside a sudden gust that leaves the foe turning the wrong way.", "ability_type": "skill", "level": 1, "elements": ["air"], "base_power": 1, "ap_cost": 15, "effect": "status", "status_keys": ["confuse"], "can_aoe": False},
    # Skill: ice
    {"id": "ice_skill_lv1_icicle_dart", "name": "Icicle Dart", "description": "A dart of ice that melts away after it hits.", "ability_type": "skill", "level": 1, "elements": ["ice"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},
    {"id": "ice_skill_lv1_black_ice_trip", "name": "Black Ice Trip", "description": "A sweep across slick ice that sends the foe sprawling.", "ability_type": "skill", "level": 1, "elements": ["ice"], "base_power": 1, "ap_cost": 11, "effect": "status", "status_keys": ["dexterity_debuff", "defense_debuff"], "can_aoe": False},
    {"id": "ice_skill_lv1_cold_focus", "name": "Cold Focus", "description": "A cold, still breath before the next strike.", "ability_type": "skill", "level": 1, "elements": ["ice"], "base_power": 0, "ap_cost": 10, "effect": "status", "status_keys": ["attack_buff", "dexterity_buff"], "can_aoe": False},
    # Skill: electric
    {"id": "electric_skill_lv1_static_palm", "name": "Static Palm", "description": "A palm strike that discharges built-up static.", "ability_type": "skill", "level": 1, "elements": ["electric"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},
    {"id": "electric_skill_lv1_spark_shuriken", "name": "Spark Shuriken", "description": "Charged throwing stars that arc between targets.", "ability_type": "skill", "level": 1, "elements": ["electric"], "base_power": 7, "ap_cost": 8, "effect": "damage", "can_aoe": True},
    {"id": "electric_skill_lv1_nerve_strike", "name": "Nerve Strike", "description": "A precise jab to a nerve cluster that locks the foe in place.", "ability_type": "skill", "level": 1, "elements": ["electric"], "base_power": 1, "ap_cost": 13, "effect": "status", "status_keys": ["stun"], "can_aoe": False},
    # Skill: light
    {"id": "light_skill_lv1_flashstep_strike", "name": "Flashstep Strike", "description": "Step through a flash of light and strike before the foe can turn.", "ability_type": "skill", "level": 1, "elements": ["light"], "base_power": 8, "ap_cost": 5, "effect": "damage", "can_aoe": False},
    {"id": "light_skill_lv1_mirror_flash", "name": "Mirror Flash", "description": "A flash off a polished blade that dazzles the target.", "ability_type": "skill", "level": 1, "elements": ["light"], "base_power": 1, "ap_cost": 9, "effect": "status", "status_keys": ["attack_debuff", "intelligence_debuff"], "can_aoe": False},
    {"id": "light_skill_lv1_sunlit_flurry", "name": "Sunlit Flurry", "description": "A blur of strikes that catches the light, and every nearby foe.", "ability_type": "skill", "level": 1, "elements": ["light"], "base_power": 7, "ap_cost": 8, "effect": "damage", "can_aoe": True},
    # Skill: dark
    {"id": "dark_skill_lv1_shadow_step", "name": "Shadow Step", "description": "Melt into the shadows, then reappear exactly where you need to be.", "ability_type": "skill", "level": 1, "elements": ["dark"], "base_power": 0, "ap_cost": 6, "effect": "status", "status_keys": ["attack_buff", "defense_buff"], "can_aoe": False},
    {"id": "dark_skill_lv1_venom_needle", "name": "Venom Needle", "description": "A needle coated in slow poison.", "ability_type": "skill", "level": 1, "elements": ["dark"], "base_power": 1, "ap_cost": 10, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False},


 # NON PLAYER ABILITIES
 {"id": "acid_slime", "name": "Acid Slime", "description": "Corrosive slime that eats away at flesh.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":1, "ap_cost":9, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False, "non_player_ability": True},
 {"id": "ruin_wight_decay_touch", "name": "Decay Touch", "description": "A rotting strike that inflicts necrotic rot over time.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":1, "ap_cost":9, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False, "non_player_ability": True},
 {"id": "ruin_wight_soulsap", "name": "Soul Sap", "description": "Drains life from the target with a shadowy grasp.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":12, "ap_cost":9, "effect": "damage", "can_aoe": False, "non_player_ability": True},
 {"id": "ruin_sentinel_stone_smash", "name": "Stone Smash", "description": "A crushing strike of stone, raw, blunt physical force.", "ability_type": "technique", "level":1, "elements": ["earth"], "base_power":14, "ap_cost":11, "effect": "damage", "can_aoe": False, "non_player_ability": True},
 {"id": "ruin_sentinel_earthshatter", "name": "Earthshatter", "description": "Violent ground rupture that damages nearby foes.", "ability_type": "technique", "level":1, "elements": ["earth"], "base_power":14, "ap_cost":11, "effect": "damage", "can_aoe": True, "non_player_ability": True},
 {"id": "stone_scarab_chitin_bite", "name": "Chitin Bite", "description": "A quick, precise bite that targets weak points.", "ability_type": "skill", "level":1, "elements": ["earth"], "base_power":10, "ap_cost":6, "effect": "damage", "can_aoe": False, "non_player_ability": True},
 {"id": "stone_scarab_carapace_bash", "name": "Carapace Bash", "description": "A heavy shell bash with a chance to stun the target.", "ability_type": "skill", "level":1, "elements": ["earth"], "base_power":2, "ap_cost":15, "effect": "status", "status_keys": ["stun"], "can_aoe": False, "non_player_ability": True},
 {"id": "level_1_hostile_ability_inspire", "name": "Inspire", "description": "A rallying cry that bolsters allies.", "ability_type": "spirit", "level":1, "elements": ["light"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["attack_buff", "defense_buff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_smoke_screen", "name": "Smoke Screen", "description": "A cloud of choking smoke that disorients foes.", "ability_type": "skill", "level":1, "elements": ["air"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_reinforce_frame", "name": "Reinforce Frame", "description": "A mechanical reinforcement that bolsters defenses.", "ability_type": "tech", "level":1, "elements": ["earth"], "base_power":0, "ap_cost":12, "effect": "status", "status_keys": ["defense_buff", "constitution_buff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_shadow_flicker", "name": "Shadow Flicker", "description": "A shadowy flicker that confuses foes.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":0, "ap_cost":14, "effect": "status", "status_keys": ["confuse"], "can_aoe": False, "non_player_ability": True},
 {"id": "level_1_hostile_ability_bone_spear", "name": "Bone Spear", "description": "A spear of bone that pierces through enemies.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":9, "ap_cost":10, "effect": "damage", "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_arcane_blast", "name": "Arcane Blast", "description": "A blast of arcane energy that damages foes.", "ability_type": "magic", "level":1, "elements": ["light"], "base_power":9, "ap_cost":10, "effect": "damage", "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_shadow_lash", "name": "Shadow Lash", "description": "A lash of shadow that weakens foes.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":1, "ap_cost":8, "effect": "status", "status_keys": ["strength_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_night_whisper", "name": "Night Whisper", "description": "A whisper that saps the will of foes.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":1, "ap_cost":8, "effect": "status", "status_keys": ["intelligence_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_poison_dart", "name": "Poison Dart", "description": "A dart that poisons the target.", "ability_type": "skill", "level":1, "elements": ["dark"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_streamlet", "name": "Streamlet", "description": "A stream of water that washes over foes.", "ability_type": "magic", "level":1, "elements": ["water"], "base_power":9, "ap_cost":10, "effect": "damage", "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_dark_magic_daze_whisper", "name": "Daze Whisper", "description": "A whisper that confuses and disorients foes.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":0, "ap_cost":13, "effect": "status", "status_keys": ["confuse"], "can_aoe": False, "non_player_ability": True},
 {"id": "level_1_hostile_ability_light_spirit_prism_burst", "name": "Prism Burst", "description": "A burst of light that blinds and disorients foes.", "ability_type": "spirit", "level":1, "elements": ["light"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_air_skill_quick_shot", "name": "Quick Shot", "description": "A rapid shot that disorients foes.", "ability_type": "skill", "level":1, "elements": ["air"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_dark_skill_corrosive_spit", "name": "Corrosive Spit", "description": "A spit that corrodes and weakens foes.", "ability_type": "skill", "level":1, "elements": ["dark"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_fire_spirit_ember_shield", "name": "Ember Shield", "description": "A shield of fire that burns and weakens foes.", "ability_type": "spirit", "level":1, "elements": ["fire"], "base_power":1, "ap_cost":9, "effect": "status", "status_keys": ["elemental_attack_buff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_air_magic_gale_surge", "name": "Gale Surge", "description": "A surge of wind that knocks back and disorients foes.", "ability_type": "magic", "level":1, "elements": ["air"], "base_power":1, "ap_cost":9, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_electric_tech_hack_overload", "name": "Hack Overload", "description": "An overload that disrupts and weakens foes.", "ability_type": "tech", "level":1, "elements": ["electric"], "base_power":1, "ap_cost":8, "effect": "status", "status_keys": ["intelligence_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_air_skill_gale_dash", "name": "Gale Dash", "description": "A dash of wind that disorients foes.", "ability_type": "skill", "level":1, "elements": ["air"], "base_power":1, "ap_cost":9, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_electric_magic_chain_lightning", "name": "Chain Lightning", "description": "A bolt of lightning that jumps between foes.", "ability_type": "magic", "level":1, "elements": ["electric"], "base_power":9, "ap_cost":10, "effect": "damage", "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_fire_spirit_hearthsong", "name": "Hearthsong", "description": "A song that warms and strengthens allies.", "ability_type": "spirit", "level":1, "elements": ["fire"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["attack_buff", "defense_buff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_earth_magic_sap_bloom", "name": "Sap Bloom", "description": "A bloom of sap that slows and weakens foes.", "ability_type": "magic", "level":1, "elements": ["earth"], "base_power":1, "ap_cost":9, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "light_magic_lv1_luminous_spike", "name": "Luminous Spike", "description": "A piercing spike of pure light.", "ability_type": "magic", "level":1, "elements": ["light"], "base_power":10, "ap_cost":11, "effect": "damage", "can_aoe": True, "non_player_ability": True},



 # --- Debug / Convenience AOE magic status abilities ---
 # {"id": "earth_magic_lv1_petrify_miasma", "name": "Petrify Miasma", "description": "Crystallizing miasma that petrifies foes.", "ability_type": "magic", "level":1, "elements": ["earth"], "base_power":0, "ap_cost":12, "effect": "status", "status_keys": ["petrify"], "can_aoe": True},
 # {"id": "air_magic_lv1_stunning_burst", "name": "Stunning Burst", "description": "A concussive blast that stuns enemies.", "ability_type": "magic", "level":1, "elements": ["air"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["stun"], "can_aoe": True},
 # {"id": "dark_magic_lv1_sleep_gloom", "name": "Sleep Gloom", "description": "A shadowy lull that puts foes to sleep.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["sleep"], "can_aoe": True},
 # {"id": "dark_magic_lv1_confuse_whisper", "name": "Confuse Whisper", "description": "A disorienting whisper that confuses foes.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["confuse"], "can_aoe": True},
 # {"id": "dark_magic_lv1_silence_veil", "name": "Silence Veil", "description": "A muffling field that silences foes.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["silence"], "can_aoe": True},
]