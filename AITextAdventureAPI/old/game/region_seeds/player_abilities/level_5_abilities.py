# LEVEL5+ ability seeds
# Extracted from constants_other.py — abilities with level >=5
LEVEL_5_PLAYER_ABILITY_SEEDS = [
 # -- Level5 dedicated light healing/rescue seeds --


 
 # --- Additional level-5+ abilities (added18 entries across ability types) ---



]

from .level_5_abilities_by_type.tech import LEVEL_5_TECH_ABILITY_SEEDS
from .level_5_abilities_by_type.skill import LEVEL_5_SKILL_ABILITY_SEEDS
from .level_5_abilities_by_type.magic import LEVEL_5_MAGIC_ABILITY_SEEDS
from .level_5_abilities_by_type.technique import LEVEL_5_TECHNIQUE_ABILITY_SEEDS
from .level_5_abilities_by_type.spirit import LEVEL_5_SPIRIT_ABILITY_SEEDS

LEVEL_5_PLAYER_ABILITY_SEEDS += LEVEL_5_TECH_ABILITY_SEEDS
LEVEL_5_PLAYER_ABILITY_SEEDS += LEVEL_5_SKILL_ABILITY_SEEDS
LEVEL_5_PLAYER_ABILITY_SEEDS += LEVEL_5_MAGIC_ABILITY_SEEDS
LEVEL_5_PLAYER_ABILITY_SEEDS += LEVEL_5_TECHNIQUE_ABILITY_SEEDS
LEVEL_5_PLAYER_ABILITY_SEEDS += LEVEL_5_SPIRIT_ABILITY_SEEDS