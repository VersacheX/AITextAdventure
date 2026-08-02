# Skill abilities for level5
LEVEL_5_SKILL_ABILITY_SEEDS = [

  #### NON PLAYER ABILITIES
    # rapture_trial — damage: pure adrenaline burst
    {"id": "adrenaline_surge", "name": "Adrenaline Surge", "description": "Rapture floods the body with manufactured adrenaline until every nerve is screaming forward — a burst of violence so fast and total that it doesn't feel like a choice so much as a detonation.", "ability_type": "skill", "level": 5, "elements": ["fire", "electric", "air", "fire", "electric"], "base_power": 160, "ap_cost": 126, "effect": "damage", "can_aoe": False, "non_player_ability": True},
    # rapture_trial — damage AoE: all-in, no recovery
    {"id": "reckless_abandon", "name": "Reckless Abandon", "description": "Rapture throws every resource into a single eruption of force with no thought for what comes after — the joy is in the going, not the surviving.", "ability_type": "skill", "level": 5, "elements": ["fire", "air", "electric", "air", "fire"], "base_power": 128, "ap_cost": 145, "effect": "damage", "can_aoe": True, "non_player_ability": True},
    # rapture_trial — damage: the high that demands more
    {"id": "thrill_addiction", "name": "Thrill Addiction", "description": "Rapture locks the target into an escalating feedback loop of stimulation — each hit wires the nervous system for more, and the damage compounds as the body struggles to process the overload.", "ability_type": "skill", "level": 5, "elements": ["fire", "electric", "air", "electric", "fire"], "base_power": 65, "ap_cost": 118, "effect": "status", "status_keys": ["continuous_damage"], "can_aoe": False, "non_player_ability": True},
    # revelry_trial — damage: pure speed burst
    {"id": "the_rush", "name": "The Rush", "description": "Revelry moves at the frequency of pure exhilaration — a strike so fast it lands before the target's perception catches up, hitting the body and the will simultaneously.", "ability_type": "skill", "level": 5, "elements": ["fire", "air", "electric", "fire", "air"], "base_power": 168, "ap_cost": 130, "effect": "damage", "can_aoe": False, "non_player_ability": True},
]
