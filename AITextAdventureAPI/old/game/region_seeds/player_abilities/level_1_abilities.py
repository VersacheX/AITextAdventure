#LEVEL1 Abilities can have1 element. there is1 ability per element and1 ability per ability type.
# ability types are: technique, faith, magic, tech, skill
# elements are: fire, water, earth, air, light, dark, ice, electric
# ability type mappings to character and hostile stats:
# technique: strength, constitution...physical attack, physical defense
# faith: intelligence, constitution...spiritual attack, spiritual defense; healing power; debuff power
# magic: intelligence...magical attack, magical defense; debuff power
# tech: intelligence, dexterity...tech attack, tech defense; debuff power
# skill: dexterity, strength...speed, critical hit rate; evasion

# Extracted from constants_other.py — abilities with "level":1
"""8 possibilities *5 ability types =40 level1 abilities """
LEVEL_1_PLAYER_ABILITY_SEEDS = [
 # --- Technique ---
  ##DAMAGE lvl 1 techniques cost 9ap, base power 12
 {"id": "fire_technique_lv1_scorch_slash", "name": "Scorch Slash", "description": "A quick fiery slash.", "ability_type": "technique", "level":1, "elements": ["fire"], "base_power":18, "ap_cost":9, "effect": "damage", "can_aoe": False},
 {"id": "ice_technique_lv1_frozen_slash", "name": "Frozen Slash", "description": "A quick cold slash.", "ability_type": "technique", "level":1, "elements": ["ice"], "base_power":18, "ap_cost":9, "effect": "damage", "can_aoe": False},
 {"id": "light_technique_lv1_radiant_slash", "name": "Radiant Slash", "description": "A shining cut that glints brightly.", "ability_type": "technique", "level":1, "elements": ["light"], "base_power":18, "ap_cost":9, "effect": "damage", "can_aoe": False},
 {"id": "dark_technique_lv1_night_claw", "name": "Night Claw", "description": "A vicious swipe from shadow.", "ability_type": "technique", "level":1, "elements": ["dark"], "base_power":18, "ap_cost":9, "effect": "damage", "can_aoe": False},
 {"id": "water_technique_lv1_slick_manuever", "name": "Slick Manuever", "description": "A flowing strike that knocks off balance.", "ability_type": "technique", "level":1, "elements": ["water"], "base_power":16, "ap_cost":8, "effect": "damage", "can_aoe": False},
  ##STATUS EFFECT   lvl status techniques 10ap - 10bp+status
 {"id": "air_technique_lv1_sonic_strike", "name": "Sonic Strike", "description": "An awe inspiring strike from above, that silences the enemy.", "ability_type": "technique", "level":1, "elements": ["air"], "base_power":10, "ap_cost":10, "effect": "status", "status_keys": ["silence"], "can_aoe": False},
 {"id": "electric_technique_lv1_stun_strike", "name": "Stun Strike", "description": "An awe inspiring strike from above, that stuns the enemy.", "ability_type": "technique", "level":1, "elements": ["electric"], "base_power":10, "ap_cost":10, "effect": "status", "status_keys": ["stun"], "can_aoe": False},
  ##BUFF lvl1 buff techniques cost 8ap, 0bp +status
 {"id": "earth_technique_lv1_armor_up", "name": "Arm Up", "description": "The strength of the earth strengthens fortitude and resolve", "ability_type": "technique", "level":1, "elements": ["earth"], "base_power":0, "ap_cost":6, "effect": "status", "status_keys": ["defense_buff", "constitution_buff"], "can_aoe": False},








 # --- Faith ---
   ##HEALING
   # # single target heal lvl1 faith heals cost 10ap, 12bp
 {"id": "light_faith_lv1_minor_heal", "name": "Minor Heal", "description": "Restore a small amount of HP.", "ability_type": "faith", "level":1, "elements": ["light"], "base_power":12, "ap_cost":10, "effect": "heal", "can_aoe": True},

   ## STATUS CLEAN
 {"id": "water_faith_lv1_mending_streams", "name": "Mending Streams", "description": "A soothing stream that cures damaging ailments.", "ability_type": "faith", "level":1, "elements": ["water"], "base_power":0, "ap_cost":6, "effect": "cure", "status_keys": ["continuous_damage"], "can_aoe": False},
 {"id": "light_faith_lv1_glimmer", "name": "Glimmer", "description": "Holy light returns life to the petrified.", "ability_type": "faith", "level":1, "elements": ["light"], "base_power":0, "ap_cost":10, "effect": "cure", "status_keys": ["petrify"], "can_aoe": False},

   ##BUFFS lvel1 faith buffs cost )10ap aoe)8ap, 0bp +status
 {"id": "electric_faith_lv1_shock_blessing", "name": "Shock Blessing", "description": "A fervent blessing that imbues weapons with the power of electricity.", "ability_type": "faith", "level":1, "elements": ["electric"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["elemental_attack_buff"], "can_aoe": True},
 {"id": "fire_faith_lv1_warmth_blessing", "name": "Warmth Blessing", "description": "A fervent blessing that imbues weapons with the power of fire.", "ability_type": "faith", "level":1, "elements": ["fire"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["elemental_attack_buff"], "can_aoe": True},
 {"id": "earth_faith_lv1_earthen_blessing", "name": "Earthen Blessing", "description": "A small grounding aid that bolsters elemental defenses.", "ability_type": "faith", "level":1, "elements": ["earth"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["defense_buff", "elemental_defense_buff"], "can_aoe": True},
 
 {"id": "air_faith_lv1_zephyr_bless", "name": "Zephyr Bless", "description": "A swift blessing that quickens allies and sharpens reflexes.", "ability_type": "faith", "level":1, "elements": ["air"], "base_power":0, "ap_cost":8, "effect": "status", "status_keys": ["dexterity_buff"], "can_aoe": False}, 
   ##DEBUFFS
 {"id": "dark_faith_lv1_shade_whisper", "name": "Blessings from Below", "description": "An unsettling benediction that saps vitality and resilience.", "ability_type": "faith", "level":1, "elements": ["dark"], "base_power":8, "ap_cost":8, "effect": "status", "status_keys": ["constitution_debuff"], "can_aoe": False},
   ##STATUS EFFECT
 {"id": "light_faith_lv1_convert", "name": "Convert", "description": "Words of the devout to convert their listeners.", "ability_type": "faith", "level":1, "elements": ["light"], "base_power":0, "ap_cost":12, "effect": "status", "status_keys": ["confuse"], "can_aoe": False},







 # --- Magic ---
   ##DAMAGE
 {"id": "dark_magic_lv1_shadow_tendril", "name": "Shadow Tendril", "description": "A shadow tendril that whips at the victim rending their flesh..", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":12, "ap_cost":8, "effect": "damage", "can_aoe": True},
 {"id": "electric_magic_lv1_fireball", "name": "Lightning Bolt", "description": "A bolt of lightning.", "ability_type": "magic", "level":1, "elements": ["electric"], "base_power":12, "ap_cost":8, "effect": "damage", "can_aoe": True}, 
 {"id": "ice_magic_lv1_frostbolt", "name": "Frostbolt", "description": "A shard of ice that chills.", "ability_type": "magic", "level":1, "elements": ["ice"], "base_power":12, "ap_cost":8, "effect": "damage", "can_aoe": True},
 {"id": "water_magic_lv1_spray_shard", "name": "Acid Rain", "description": "A searing rain.", "ability_type": "magic", "level":1, "elements": ["water"], "base_power":12, "ap_cost":8, "effect": "damage", "can_aoe": True}, 
 {"id": "fire_magic_lv1_fireball", "name": "Fireball", "description": "A ball of searing flame.", "ability_type": "magic", "level":1, "elements": ["fire"], "base_power":12, "ap_cost":8, "effect": "damage", "can_aoe": True},
 {"id": "air_magic_lv1_shredding_gust", "name": "Shredding Gust", "description": "A of shredding wind.", "ability_type": "magic", "level":1, "elements": ["air"], "base_power":12, "ap_cost":8, "effect": "damage", "can_aoe": True},
 {"id": "earth_magic_lv1_tremor", "name": "Tremor", "description": "The ground quakes and tears.", "ability_type": "magic", "level":1, "elements": ["earth"], "base_power":12, "ap_cost":8, "effect": "damage", "can_aoe": True},
 



 # --- Tech (technology) ---
   ##DAMAGE
 {"id": "ice_tech_lv1_crio_refraction", "name": "Crio-Refraction", "description": "A small device that focuses a beam of absolute-0 energy.", "ability_type": "tech", "level":1, "elements": ["ice"], "base_power":13, "ap_cost":9, "effect": "damage", "can_aoe": False},
 ##DAMAGAE AOE
 {"id": "dark_tech_lv1_void_grenade", "name": "Void Grenade", "description": "A grenade that explodes on impact releasing a dark energy..", "ability_type": "tech", "level":1, "elements": ["dark"], "base_power":12, "ap_cost":12, "effect": "damage", "can_aoe": True},
 ##DEBUFF
 {"id": "fire_tech_lv1_flux_dampener", "name": "Flux Dampener", "description": "Launches a disruptive pulse that corrodes fiery resonance in targets.", "ability_type": "tech", "level":1, "elements": ["fire"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
 {"id": "water_tech_lv1_tide_entangler", "name": "Tide Entangler", "description": "Releases a tangling circuit that interferes with aqueous energy matrices.", "ability_type": "tech", "level":1, "elements": ["water"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
 {"id": "air_tech_lv1_gale_jammer", "name": "Gale Jammer", "description": "Generates turbulent interference that destabilizes wind-aligned defenses.", "ability_type": "tech", "level":1, "elements": ["air"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
 {"id": "earth_tech_lv1_fault_inhibitor", "name": "Fault Inhibitor", "description": "Deploys a grounding field that disrupts earthen bonding.", "ability_type": "tech", "level":1, "elements": ["earth"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["elemental_debuff"], "can_aoe": True},
 ##STATUS EFFECT
 {"id": "electric_tech_lv1_taze_charge", "name": "Taze Charge", "description": "A tongued projectile that stuns the target.", "ability_type": "tech", "level":1, "elements": ["electric"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["stun"], "can_aoe": False},
 {"id": "light_tech_lv1_aerial_drone", "name": "Aerial Drone", "description": "A small drone that scans enemies.", "ability_type": "tech", "level":1, "elements": ["light"], "base_power":0, "ap_cost":5, "effect": "status", "status_keys": ["scanned"], "can_aoe": True},




 # --- Skill ---
   ##DAMAGE
 {"id": "dark_skill_lv1_creeping_strike", "name": "Creeping Strike", "description": "A sly strike that bites at defenses.", "ability_type": "skill", "level":1, "elements": ["dark"], "base_power":3, "ap_cost":6, "effect": "damage", "can_aoe": False},
 {"id": "ice_skill_lv1_ice_shuriken", "name": "Ice Shuriken", "description": "A cold and calculated shuriken.", "ability_type": "skill", "level":1, "elements": ["ice"], "base_power":3, "ap_cost":6, "effect": "damage", "can_aoe": False},
 {"id": "water_skill_lv1_flowing_fists", "name": "Flowing Fists", "description": "A successive flurry of strikes.", "ability_type": "skill", "level":1, "elements": ["water"], "base_power":3, "ap_cost":6, "effect": "damage", "can_aoe": False},
 {"id": "electric_skill_lv1_lightning_strike", "name": "Lightning Strike", "description": "A technique so fast it cracks the air as it's performed.", "ability_type": "skill", "level":1, "elements": ["electric"], "base_power":3, "ap_cost":6, "effect": "damage", "can_aoe": False},
 {"id": "light_skill_lv1_holy_fists", "name": "Holy Fists", "description": "Successive strikes performed at blinding speed.", "ability_type": "skill", "level":1, "elements": ["light"], "base_power":3, "ap_cost":6, "effect": "damage", "can_aoe": False},
 
   ##DEBUFF
 {"id": "air_skill_lv1_smoke_bomb", "name": "Smoke Bomb", "description": "Create a cloud of choking particulate that slows and disorients.", "ability_type": "skill", "level":1, "elements": ["air"], "base_power":3, "ap_cost":12, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": False}, 
 {"id": "earth_skill_lv1_soporific_veil", "name": "Soporific Veil", "description": "Unleashes a choking, mineral-laden veil inspired by clandestine smoke powders.", "ability_type": "skill", "level":1, "elements": ["earth"], "base_power":3, "ap_cost":12, "effect": "status", "status_keys": ["intelligence_debuff"], "can_aoe": False},
 {"id": "fire_skill_lv1_debilitating_ember_smoke", "name": "Debilitating Ember-Smoke", "description": "Generates an enfeebling cloud.", "ability_type": "skill", "level":1, "elements": ["fire"], "base_power":3, "ap_cost":12, "effect": "status", "status_keys": ["strength_debuff"], "can_aoe": False},
 
   ##STATUS EFFECT
 {"id": "dark_skill_lv1_tranq_dart", "name": "Tranq Dart", "description": "A dart tipped with a sedative.", "ability_type": "skill", "level":1, "elements": ["dark"], "base_power":3, "ap_cost":8, "effect": "status", "status_keys": ["sleep"], "can_aoe": False},


 # NON PLAYER ABILITIES
 {"id": "acid_slime", "name": "Acid Slime", "description": "Corrosive slime that eats away at flesh.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":1, "ap_cost":6, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False, "non_player_ability": True},
 {"id": "ruin_wight_decay_touch", "name": "Decay Touch", "description": "A rotting strike that inflicts necrotic rot over time.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":2, "ap_cost":8, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False, "non_player_ability": True},
 {"id": "ruin_wight_soulsap", "name": "Soul Sap", "description": "Drains life from the target with a shadowy grasp.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":12, "ap_cost":10, "effect": "damage", "can_aoe": False, "non_player_ability": True},
 {"id": "ruin_sentinel_stone_smash", "name": "Stone Smash", "description": "A crushing strike of stone, raw, blunt physical force.", "ability_type": "technique", "level":1, "elements": ["earth"], "base_power":14, "ap_cost":8, "effect": "damage", "can_aoe": False, "non_player_ability": True},
 {"id": "ruin_sentinel_earthshatter", "name": "Earthshatter", "description": "Violent ground rupture that damages nearby foes.", "ability_type": "technique", "level":1, "elements": ["earth"], "base_power":16, "ap_cost":12, "effect": "damage", "can_aoe": True, "non_player_ability": True},
 {"id": "stone_scarab_chitin_bite", "name": "Chitin Bite", "description": "A quick, precise bite that targets weak points.", "ability_type": "skill", "level":1, "elements": ["earth"], "base_power":6, "ap_cost":6, "effect": "damage", "can_aoe": False, "non_player_ability": True},
 {"id": "stone_scarab_carapace_bash", "name": "Carapace Bash", "description": "A heavy shell bash with a chance to stun the target.", "ability_type": "skill", "level":1, "elements": ["earth"], "base_power":8, "ap_cost":10, "effect": "status", "status_keys": ["stun"], "can_aoe": False, "non_player_ability": True},
 {"id": "level_1_hostile_ability_inspire", "name": "Inspire", "description": "A rallying cry that bolsters allies.", "ability_type": "faith", "level":1, "elements": ["light"], "base_power":0, "ap_cost":8, "effect": "status", "status_keys": ["attack_buff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_smoke_bomb", "name": "Smoke Bomb", "description": "A cloud of choking smoke that disorients foes.", "ability_type": "skill", "level":1, "elements": ["air"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_reinforce_frame", "name": "Reinforce Frame", "description": "A mechanical reinforcement that bolsters defenses.", "ability_type": "tech", "level":1, "elements": ["earth"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["defense_buff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_shadow_flicker", "name": "Shadow Flicker", "description": "A shadowy flicker that confuses foes.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["confuse"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_bone_spear", "name": "Bone Spear", "description": "A spear of bone that pierces through enemies.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":12, "ap_cost":10, "effect": "damage", "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_arcane_blast", "name": "Arcane Blast", "description": "A blast of arcane energy that damages foes.", "ability_type": "magic", "level":1, "elements": ["light"], "base_power":12, "ap_cost":10, "effect": "damage", "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_shadow_lash", "name": "Shadow Lash", "description": "A lash of shadow that weakens foes.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["strength_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_night_whisper", "name": "Night Whisper", "description": "A whisper that saps the will of foes.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["intelligence_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_poison_dart", "name": "Poison Dart", "description": "A dart that poisons the target.", "ability_type": "skill", "level":1, "elements": ["dark"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_streamlet", "name": "Streamlet", "description": "A stream of water that washes over foes.", "ability_type": "magic", "level":1, "elements": ["water"], "base_power":12, "ap_cost":10, "effect": "damage", "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_dark_magic_daze_whisper", "name": "Daze Whisper", "description": "A whisper that confuses and disorients foes.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["confuse"], "can_aoe": False, "non_player_ability": True},
 {"id": "level_1_hostile_ability_light_faith_prism_burst", "name": "Prism Burst", "description": "A burst of light that blinds and disorients foes.", "ability_type": "faith", "level":1, "elements": ["light"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_air_skill_quick_shot", "name": "Quick Shot", "description": "A rapid shot that disorients foes.", "ability_type": "skill", "level":1, "elements": ["air"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_dark_skill_corrosive_spit", "name": "Corrosive Spit", "description": "A spit that corrodes and weakens foes.", "ability_type": "skill", "level":1, "elements": ["dark"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["strength_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_fire_faith_ember_shield", "name": "Ember Shield", "description": "A shield of fire that burns and weakens foes.", "ability_type": "faith", "level":1, "elements": ["fire"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["strength_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_air_magic_gale_surge", "name": "Gale Surge", "description": "A surge of wind that knocks back and disorients foes.", "ability_type": "magic", "level":1, "elements": ["air"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_electric_tech_hack_overload", "name": "Hack Overload", "description": "An overload that disrupts and weakens foes.", "ability_type": "tech", "level":1, "elements": ["electric"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["intelligence_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_air_skill_gale_dash", "name": "Gale Dash", "description": "A dash of wind that disorients foes.", "ability_type": "skill", "level":1, "elements": ["air"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_electric_magic_chain_lightning", "name": "Chain Lightning", "description": "A bolt of lightning that jumps between foes.", "ability_type": "magic", "level":1, "elements": ["electric"], "base_power":12, "ap_cost":10, "effect": "damage", "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_fire_faith_hearthsong", "name": "Hearthsong", "description": "A song that warms and strengthens allies.", "ability_type": "faith", "level":1, "elements": ["fire"], "base_power":0, "ap_cost":7, "effect": "status", "status_keys": ["attack_buff", "defense_buff"], "can_aoe": True, "non_player_ability": True},
 {"id": "level_1_hostile_ability_earth_magic_sap_bloom", "name": "Sap Bloom", "description": "A bloom of sap that slows and weakens foes.", "ability_type": "magic", "level":1, "elements": ["earth"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["dexterity_debuff"], "can_aoe": True, "non_player_ability": True},
 {"id": "light_magic_lv1_luminous_spike", "name": "Luminous Spike", "description": "A piercing spike of pure light.", "ability_type": "magic", "level":1, "elements": ["light"], "base_power":14, "ap_cost":10, "effect": "damage", "can_aoe": True, "non_player_ability": True},



 # --- Debug / Convenience AOE magic status abilities ---
 # {"id": "earth_magic_lv1_petrify_miasma", "name": "Petrify Miasma", "description": "Crystallizing miasma that petrifies foes.", "ability_type": "magic", "level":1, "elements": ["earth"], "base_power":0, "ap_cost":12, "effect": "status", "status_keys": ["petrify"], "can_aoe": True},
 # {"id": "air_magic_lv1_stunning_burst", "name": "Stunning Burst", "description": "A concussive blast that stuns enemies.", "ability_type": "magic", "level":1, "elements": ["air"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["stun"], "can_aoe": True},
 # {"id": "dark_magic_lv1_sleep_gloom", "name": "Sleep Gloom", "description": "A shadowy lull that puts foes to sleep.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["sleep"], "can_aoe": True},
 # {"id": "dark_magic_lv1_confuse_whisper", "name": "Confuse Whisper", "description": "A disorienting whisper that confuses foes.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["confuse"], "can_aoe": True},
 # {"id": "dark_magic_lv1_silence_veil", "name": "Silence Veil", "description": "A muffling field that silences foes.", "ability_type": "magic", "level":1, "elements": ["dark"], "base_power":0, "ap_cost":10, "effect": "status", "status_keys": ["silence"], "can_aoe": True},
]