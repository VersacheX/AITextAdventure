# Technique abilities for level 5
LEVEL_5_TECHNIQUE_ABILITY_SEEDS = [ 
    {"id": "earth_technique_lv5_seismic_wave", "name": "Seismic Wave", "description": "A concussive wall of earth.", "ability_type": "technique", "level":5, "elements": ["earth", "earth", "air", "dark", "fire"], "base_power":194, "ap_cost":174, "effect": "damage", "can_aoe": False}, 
    {"id": "technique_lv5_ravaging_strike", "name": "Ravaging Strike", "description": "A devastating single-target brutal strike.", "ability_type": "technique", "level":5, "elements": ["earth", "fire", "dark", "air", "light"], "base_power":192, "ap_cost":180, "effect": "damage", "can_aoe": False},


    #### NON PLAYER ABILITIES
    # cataclysm — damage: apocalyptic physical annihilation, the scheduled end of things
    {"id": "absolute_destruction", "name": "Absolute Destruction", "description": "Cataclysm executes a destruction that was always scheduled — a colossal, perfectly timed strike that annihilates all in range with the inevitability of a closing chapter.", "ability_type": "technique", "level": 5, "elements": ["earth", "fire", "dark", "dark", "fire"], "base_power": 138, "ap_cost": 155, "effect": "damage", "can_aoe": True, "non_player_ability": True},
    # crux_trial — hazard: clinical targeted elimination
    {"id": "objective_elimination", "name": "Objective Elimination", "description": "Crux reduces the target to a variable and erases it — a perfectly efficient strike with no anger, no hesitation, and no margin for survival.", "ability_type": "technique", "level": 5, "elements": ["electric", "dark", "air", "dark", "electric"], "base_power": 175, "ap_cost": 150, "effect": "damage", "can_aoe": False, "non_player_ability": True},
    # edict_trial — tank: rule enforcement strike
    {"id": "rule_enforcement", "name": "Rule Enforcement", "description": "Edict delivers the physical consequence of broken law — a crushing blow whose force is proportional not to strength but to the severity of the transgression.", "ability_type": "technique", "level": 5, "elements": ["dark", "earth", "dark", "light", "earth"], "base_power": 170, "ap_cost": 148, "effect": "damage", "can_aoe": False, "non_player_ability": True},
]