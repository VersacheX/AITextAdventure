# Technique abilities for level 4
LEVEL_4_TECHNIQUE_ABILITY_SEEDS = [
     {"id": "air_earth_technique_lv4_whirlwind", "name": "Whirlwind", "description": "Spin and strike multiple foes.", "ability_type": "technique", "level":4, "elements": ["air", "earth", "light", "water"], "base_power":165, "ap_cost":144, "effect": "damage", "can_aoe": False},
     {"id": "fire_technique_lv4_berserker_pulse", "name": "Berserker Pulse", "description": "A violent surge of energy that empowers attacks.", "ability_type": "technique", "level":4, "elements": ["fire", "fire", "earth", "electric"], "base_power":0, "ap_cost":105, "effect": "status", "status_keys": ["attack_buff", "elemental_attack_buff", "dexterity_buff"], "can_aoe": True},

    #### NON PLAYER ABILITIES
    #scalpel
    {"id": "cold_execution", "name": "Cold Execution", "description": "A frigid, methodical strike carried out with total detachment. Finds every gap in armour with mechanical precision.", "ability_type": "technique", "level": 4, "elements": ["ice", "ice", "dark", "air"], "base_power": 134, "ap_cost": 122, "effect": "damage", "can_aoe": False, "non_player_ability": True},
    {"id": "blood_spectacle", "name": "Blood Spectacle", "description": "Rapture erupts into a frenzy of devastating strikes, turning the battlefield into a theatre of ruin that thrills as much as it destroys.", "ability_type": "technique", "level": 4, "elements": ["dark", "fire", "dark", "fire"], "base_power": 105, "ap_cost": 118, "effect": "damage", "can_aoe": True, "non_player_ability": True},
    # garbage
    {"id": "absolute_disgust", "name": "Absolute Disgust", "description": "Garbage erupts in a torrent of corrosive self-loathing — the combined weight of every discarded thing crashes down on all nearby, crushing meaning out of existence.", "ability_type": "technique", "level": 4, "elements": ["dark", "dark", "earth", "fire"], "base_power": 116, "ap_cost": 130, "effect": "damage", "can_aoe": True, "non_player_ability": True},
    # edict
    {"id": "ancient_rule", "name": "Ancient Rule", "description": "Edict channels the full crushing weight of an unbreakable law that predates memory — a single devastating strike that cannot be argued with or refused.", "ability_type": "technique", "level": 4, "elements": ["earth", "dark", "fire", "ice"], "base_power": 134, "ap_cost": 120, "effect": "damage", "can_aoe": False, "non_player_ability": True},
    {"id": "ritual_punishment", "name": "Ritual Punishment", "description": "Collective transgression demands collective consequence — Edict brings down punishing force on every target in the field without distinction or mercy.", "ability_type": "technique", "level": 4, "elements": ["dark", "fire", "earth", "dark"], "base_power": 108, "ap_cost": 120, "effect": "damage", "can_aoe": True, "non_player_ability": True},
    # cataclysm — damage: a single target strike delivered on the timetable of ruin
    {"id": "scheduled_obliteration", "name": "Scheduled Obliteration", "description": "Cataclysm does not choose when to strike — it was always going to happen at this exact moment. A devastating, precisely timed blow falls on one target with the weight of a world's final second.", "ability_type": "technique", "level": 4, "elements": ["earth", "fire", "dark", "fire"], "base_power": 132, "ap_cost": 118, "effect": "damage", "can_aoe": False, "non_player_ability": True},

]