# Desert shared hostiles - rarity-coverage fill, Lv 1-20.
#
# Reusable across all desert city sizes (large / mid / small) and the desert
# wilderness. Each seed is placed at exactly the level the validator suggested
# so a single seed clears each stacked REGION_HOSTILE_RARITY_GAP window.
# Ability ids are reused from existing loaded band files, so they are
# known-valid against PLAYER_ABILITY_SEEDS.

RANDOM_HOSTILE_SEEDS = [

    # min_spawn_level == 5 (superrare window Lv 1-5)
    {"id": "mirage_prowler", "name": "Mirage Prowler", "hostile_type": "eldritch", "role": "hazard", "min_spawn_level": 5, "rarity": "superrare", "base_xp": 90,
     "common_drop": "herb_minor", "rare_drop": "stimulant_med", "money_range": (20, 90),
     "basic_attack": "shimmering feint", "strong_attack": "heat-warped lunge",
     "player_abilities": ["dark_magic_lv1_shadow_tendril", "fire_magic_lv1_fireball", "level_1_hostile_ability_poison_dart"],
     "base_str": 5, "base_dex": 7, "base_con": 5, "base_int": 8, "base_hp": 48, "base_ap": 6,
     "str_per_level": 1, "dex_per_level": 1, "con_per_level": 1, "int_per_level": 1},

    # min_spawn_level == 17 (superrare window Lv 13-17)
    {"id": "gilded_tomb_sentry", "name": "Gilded Tomb Sentry", "hostile_type": "construct", "role": "damage", "min_spawn_level": 17, "rarity": "superrare", "base_xp": 260,
     "common_drop": "herb_minor", "rare_drop": "stimulant_large", "money_range": (40, 160),
     "basic_attack": "gilded halberd sweep", "strong_attack": "sentinel overdrive",
     "player_abilities": ["level_1_hostile_ability_reinforce_frame", "earth_magic_lv1_tremor", "fire_technique_lv1_scorch_slash"],
     "base_str": 14, "base_dex": 5, "base_con": 12, "base_int": 4, "base_hp": 120, "base_ap": 7,
     "str_per_level": 2, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 0},

    # min_spawn_level == 20 (uncommon window Lv 16-20)
    {"id": "neon_racket_enforcer", "name": "Neon Racket Enforcer", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": 20, "rarity": "uncommon", "base_xp": 150,
     "common_drop": "herb_minor", "rare_drop": "stimulant_med", "money_range": (30, 130),
     "basic_attack": "brass-knuckle jab", "strong_attack": "shakedown combo",
     "player_abilities": ["fire_technique_lv1_scorch_slash"],
     "base_str": 9, "base_dex": 6, "base_con": 8, "base_int": 3, "base_hp": 90, "base_ap": 6,
     "str_per_level": 2, "dex_per_level": 1, "con_per_level": 2, "int_per_level": 0},
]
