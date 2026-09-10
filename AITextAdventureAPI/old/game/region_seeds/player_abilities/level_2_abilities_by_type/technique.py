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


LEVEL_2_TECHNIQUE_ABILITY_SEEDS = [
 # --- technique ---
   ##DAMAGE
 {"id": "electric_fire_technique_lv2_volt_burn", "name": "Volt Burn", "description": "An electrified blaze that shocks.", "ability_type": "technique", "level":2, "elements": ["electric", "fire"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "electric_air_technique_lv2_storm_rend", "name": "Storm Rend", "description": "A ripping gale of electric wind.", "ability_type": "technique", "level":2, "elements": ["electric", "air"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "electric_light_technique_lv2_luminous_spark", "name": "Luminous Spark", "description": "A bright spark of electric light.", "ability_type": "technique", "level":2, "elements": ["electric", "light"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "electric_dark_technique_lv2_shadow_shock", "name": "Shadow Shock", "description": "A jolt of electric shadow.", "ability_type": "technique", "level":2, "elements": ["electric", "dark"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},

 {"id": "ice_water_technique_lv2_glacial_wave", "name": "Glacial Wave", "description": "A wave of icy water that slows.", "ability_type": "technique", "level":2, "elements": ["ice", "water"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "ice_earth_technique_lv2_permafrost_crush", "name": "Permafrost Crush", "description": "A crushing strike of frozen earth.", "ability_type": "technique", "level":2, "elements": ["ice", "earth"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "ice_light_technique_lv2_crystal_lance", "name": "Crystal Lance", "description": "A lance of pure ice and light.", "ability_type": "technique", "level":2, "elements": ["ice", "light"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "ice_dark_technique_lv2_shadowfrost_bite", "name": "Shadowfrost Bite", "description": "A biting frost laced with shadow.", "ability_type": "technique", "level":2, "elements": ["ice", "dark"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},

 {"id": "fire_earth_technique_lv2_blaze_hammer", "name": "Blaze Hammer", "description": "A molten crush that smashes armor.", "ability_type": "technique", "level":2, "elements": ["fire", "earth"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "fire_air_technique_lv2_burst_gale", "name": "Burst Gale", "description": "A bursting flame ride on the wind.", "ability_type": "technique", "level":2, "elements": ["fire", "air"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "fire_light_technique_lv2_solstice_cleave", "name": "Solstice Cleave", "description": "A radiant cleave heated to brilliance.", "ability_type": "technique", "level":2, "elements": ["fire", "light"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "fire_dark_technique_lv2_shadowflame_rend", "name": "Shadowflame Rend", "description": "A corrosive flame that bites shadows.", "ability_type": "technique", "level":2, "elements": ["fire", "dark"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},
 
 {"id": "earth_air_technique_lv2_crosswind_hammerblow", "name": "Crosswind Hammerblow", "description": "A crushing hit with a slicing wind edge.", "ability_type": "technique", "level":2, "elements": ["earth", "air"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "earth_water_technique_lv2_mire_cleave", "name": "Mire Cleave", "description": "A wet, crushing blow.", "ability_type": "technique", "level":2, "elements": ["earth", "water"], "base_power":34, "ap_cost":28, "effect": "damage", "can_aoe": False},
 {"id": "earth_dark_technique_lv2_dark_impact", "name": "Dark Impact", "description": "A darkened earth strike that gnaws.", "ability_type": "technique", "level":2, "elements": ["earth", "dark"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},
 
 {"id": "air_water_technique_lv2_rainfall_slash", "name": "Rainfall Slash", "description": "A slashing cascade of wind and water.", "ability_type": "technique", "level":2, "elements": ["air", "water"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "air_light_technique_lv2_gleam_pierce", "name": "Gleam Pierce", "description": "A shining strike that rides the wind.", "ability_type": "technique", "level":2, "elements": ["air", "light"], "base_power":34, "ap_cost":30, "effect": "damage", "can_aoe": False}, 
 
 {"id": "water_light_technique_lv2_purewave_clout", "name": "Purewave Clout", "description": "A cleansing light-water strike.", "ability_type": "technique", "level":2, "elements": ["water", "light"], "base_power":34, "ap_cost":30, "effect": "damage", "can_aoe": False},
 {"id": "water_dark_technique_lv2_abyssal_rip", "name": "Abyssal Rip", "description": "A rippling wave tinged with shadow.", "ability_type": "technique", "level":2, "elements": ["water", "dark"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False}, 
 
 {"id": "light_dark_technique_lv2_twilight_cleave", "name": "Twilight Cleave", "description": "A cut between sun and shadow.", "ability_type": "technique", "level":2, "elements": ["light", "dark"], "base_power":36, "ap_cost":30, "effect": "damage", "can_aoe": False},

   ##DAMAGE AOE
 {"id": "fire_fire_technique_lv2_inferno_breach", "name": "Inferno Breach", "description": "A two-handed burning strike.", "ability_type": "technique", "level":2, "elements": ["fire", "fire"], "base_power":22, "ap_cost":25, "effect": "damage", "can_aoe": True},
 {"id": "earth_earth_technique_lv2_terra_slam", "name": "Terra Slam", "description": "A crushing earthbound strike.", "ability_type": "technique", "level":2, "elements": ["earth", "earth"], "base_power":22, "ap_cost":25, "effect": "damage", "can_aoe": True},
 {"id": "air_air_technique_lv2_zephyr_clash", "name": "Zephyr Clash", "description": "A swift clashing of wind-edged strikes.", "ability_type": "technique", "level":2, "elements": ["air", "air"], "base_power":22, "ap_cost":25, "effect": "damage", "can_aoe": True}, 
 {"id": "dark_dark_technique_lv2_void_crush", "name": "Void Crush", "description": "A crushing blow from the void.", "ability_type": "technique", "level":2, "elements": ["dark", "dark"], "base_power":22, "ap_cost":25, "effect": "damage", "can_aoe": True},
 {"id": "light_light_technique_lv2_radiant_bash", "name": "Radiant Bash", "description": "A blindingly bright strike.", "ability_type": "technique", "level":2, "elements": ["light", "light"], "base_power":22, "ap_cost":25, "effect": "damage", "can_aoe": True},
 {"id": "water_water_technique_lv2_torrent_tech", "name": "Torrent Pulse", "description": "A heavy pulse of rushing water.", "ability_type": "technique", "level":2, "elements": ["water", "water"], "base_power":22, "ap_cost":25, "effect": "damage", "can_aoe": True},
 {"id": "ice_ice_technique_lv2_frost_smash", "name": "Frost Smash", "description": "A shattering icy strike.", "ability_type": "technique", "level":2, "elements": ["ice", "ice"], "base_power":22, "ap_cost":25, "effect": "damage", "can_aoe": True},
 {"id": "electric_electric_technique_lv2_thunder_clap", "name": "Thunder Clap", "description": "A booming electric strike.", "ability_type": "technique", "level":2, "elements": ["electric", "electric"], "base_power":22, "ap_cost":25, "effect": "damage", "can_aoe": True},
   ###BUFFS   
 {"id": "electric_water_technique_lv2_conductive_wave", "name": "Conductive Wave", "description": "Electrified tide that sharpens attacks.", "ability_type": "technique", "level":2, "elements": ["electric", "water"], "base_power":0, "ap_cost":25, "effect": "status", "status_keys": ["elemental_attack_buff", "strength_buff"], "can_aoe": False},
 {"id": "ice_fire_technique_lv2_frostbrand_flame", "name": "Frostbrand Flame", "description": "Cold fire that hones offense.", "ability_type": "technique", "level":2, "elements": ["ice", "fire"], "base_power":0, "ap_cost":25, "effect": "status", "status_keys": ["elemental_attack_buff", "strength_buff"], "can_aoe": False},
 {"id": "fire_water_technique_lv2_steam_temper", "name": "Steam Temper", "description": "Scalding steam that sharpens strikes.", "ability_type": "technique", "level":2, "elements": ["fire", "water"], "base_power":0, "ap_cost":25, "effect": "status", "status_keys": ["elemental_attack_buff", "strength_buff"], "can_aoe": False},
 {"id": "ice_air_technique_lv2_hailwind_edge", "name": "Hailwind Edge", "description": "Icy gusts that harden strikes.", "ability_type": "technique", "level":2, "elements": ["ice", "air"], "base_power":0, "ap_cost":25, "effect": "status", "status_keys": ["elemental_attack_buff", "strength_buff"], "can_aoe": False},
 {"id": "earth_air_technique_lv2_stonewind_fortify", "name": "Stonewind Fortify", "description": "Rock and wind that boost offense.", "ability_type": "technique", "level":2, "elements": ["earth", "air"], "base_power":0, "ap_cost":25, "effect": "status", "status_keys": ["elemental_attack_buff", "strength_buff"], "can_aoe": False},
 {"id": "electric_earth_technique_lv2_magnet_quake", "name": "Magnet Quake", "description": "Charged tremors that strengthen hits.", "ability_type": "technique", "level":2, "elements": ["electric", "earth"], "base_power":0, "ap_cost":25, "effect": "status", "status_keys": ["elemental_attack_buff", "strength_buff"], "can_aoe": False},

 {"id": "earth_light_technique_lv2_rally_up", "name": "Rally Up", "description": "A hardens defenses for all those affected.", "ability_type": "technique", "level":2, "elements": ["earth", "light"], "base_power":0, "ap_cost":22, "effect": "status", "status_keys": ["defense_buff", "constitution_buff"], "can_aoe": True},
   ###STATUS EFFECTS
   #THIS ISN'T TECHNIQUE WE CHANGE IT .... big slam into ground whammo sonic slam
 {"id": "air_dark_technique_lv2_hush_now", "name": "Sonic Slam", "description": "An effective technique involving slamming a weapon into the ground to create sonic waves.", "ability_type": "technique", "level":2, "elements": ["air", "dark"], "base_power":1, "ap_cost":40, "effect": "status", "status_keys": ["silence"], "can_aoe": True},




  #### NON PLAYER ABILITIES
  {"id": "earth_dark_technique_lv2_rabid_bite", "name": "Rabid Bite", "description": "A savage bite filled with dark energy.", "ability_type": "technique", "level":2, "elements": ["earth", "dark"], "base_power":30, "ap_cost":25, "effect": "damage", "can_aoe": False, "non_player_ability": True},
  {"id": "dark_dark_technique_lv2_infectious_bite", "name": "Infectious Bite", "description": "A savage bite filled with dark energy.", "ability_type": "technique", "level":2, "elements": ["earth", "dark"], "base_power":5, "ap_cost":30, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False, "non_player_ability": True},
  {"id": "earth_fire_technique_lv2_berserker_tech", "name": "Berserker Technique", "description": "A berserker technique that increases attack power.", "ability_type": "technique", "level":2, "elements": ["earth", "fire"], "base_power":0, "ap_cost":25, "effect": "status", "status_keys": ["elemental_attack_buff", "attack_buff"], "can_aoe": True, "non_player_ability": True},
  {"id": "earth_earth_technique_lv2_earth_sunder", "name": "Earth Sunder", "description": "A devastating earth technique that shatters the ground.", "ability_type": "technique", "level":2, "elements": ["earth", "earth"], "base_power":40, "ap_cost":30, "effect": "damage", "can_aoe": False, "non_player_ability": True},
  {"id": "earth_earth_technique_lv2_brutal_swing", "name": "Brutal Swing", "description": "A powerful swing that crushes enemies.", "ability_type": "technique", "level":2, "elements": ["earth", "earth"], "base_power":35, "ap_cost":25, "effect": "damage", "can_aoe": False, "non_player_ability": True},
  {"id": "earth_light_technique_lv2_stone_guard", "name": "Stone Guard", "description": "A defensive technique that fortifies allies.", "ability_type": "technique", "level":2, "elements": ["earth", "light"], "base_power":0, "ap_cost":25, "effect": "status", "status_keys": ["defense_buff", "elemental_defense_buff"], "can_aoe": True, "non_player_ability": True},
  {"id": "air_air_technique_lv2_whirlwind_barrage", "name": "Whirlwind Barrage", "description": "A flurry of wind attacks that hits multiple enemies.", "ability_type": "technique", "level":2, "elements": ["air", "air"], "base_power":30, "ap_cost":30, "effect": "damage", "can_aoe": True, "non_player_ability": True},
  {"id": "earth_electric_lv2_technique_chain_reactor", "name": "Chain Reactor", "description": "A chain reaction of electric energy that jumps between enemies.", "ability_type": "technique", "level":2, "elements": ["earth", "electric"], "base_power":28, "ap_cost":30, "effect": "damage", "can_aoe": True, "non_player_ability": True},
  {"id": "lv2_hostile_ability_earth_air_technique_petrify_gaze", "name": "Petrify Gaze", "description": "A gaze that turns enemies to stone, immobilizing them.", "ability_type": "technique", "level":2, "elements": ["earth", "air"], "base_power":0, "ap_cost":50, "effect": "status", "status_keys": ["petrify"], "can_aoe": False, "non_player_ability": True},

  #### UNIQUE CHARACTER ABILITIES
  {
      "id": "earth_light_technique_lv2_lawbind_strike",
      "name": "Lawbind Strike",
      "description": "A heavy, measured blow that brands the target with the weight of the law, reducing their attack potency.",
      "ability_type": "technique",
      "level": 2,
      "elements": ["earth", "light"],
      "base_power": 10,
      "ap_cost": 45,
      "effect": "status",
      "status_keys": ["defense_debuff", "elemental_debuff"],
      "can_aoe": False,
      "non_player_ability": True
  }
]