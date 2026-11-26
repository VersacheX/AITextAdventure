
### Player statistic requirements in order to attain abilities of each ability type multiplied by ability_level.
ABILITY_TYPE_REQUIREMENTS = [
    {"ability_type": "technique", "required_stats_per_ability_level": [{"strength": 13, "constitution": 9}]},
    {"ability_type": "spirit", "required_stats_per_ability_level": [{"intelligence": 13}, {"constitution": 9}]},
    {"ability_type": "magic", "required_stats_per_ability_level": [{"intelligence": 18}]},
    {"ability_type": "tech", "required_stats_per_ability_level": [{"intelligence": 13}, {"dexterity": 9}]},
    {"ability_type": "skill", "required_stats_per_ability_level": [{"dexterity": 13}, {"strength": 9}]},
]

### Class stat-growth curve (IMPLEMENTATION_SPEC_class_growth_elements.md Part 1).
# Per-level class-distributed points (6 total per level; magic gets all 6 on INT).
CLASS_STAT_SPLIT = {
    'technique': {'strength': 4, 'constitution': 2},
    'spirit':    {'intelligence': 4, 'constitution': 2},
    'tech':      {'intelligence': 4, 'dexterity': 2},
    'skill':     {'dexterity': 4, 'strength': 2},
    'magic':     {'intelligence': 6},
}

# Level-1 stats per class: 8 base + 10 points distributed (STR, DEX, CON, INT).
CLASS_LEVEL1_STATS = {
    'technique': (14, 8, 12, 8),
    'spirit': (8, 8, 12, 14),
    'tech': (8, 12, 8, 14),
    'skill': (12, 14, 8, 8),
    'magic': (8, 8, 8, 18),
}

# Power-point (HP vs AP) split per class; the rest goes to AP.
CLASS_HP_RATIO = {'technique': 0.80, 'spirit': 0.50, 'magic': 0.35, 'tech': 0.45, 'skill': 0.60}

# Ability stat-requirement scale: players use 2.1, hostiles keep the old 1.5 curve.
PLAYER_REQUIREMENT_SCALE = 2.1
HOSTILE_REQUIREMENT_SCALE = 1.5