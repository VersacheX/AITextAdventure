#LEVEL3 Abilities can have3 elements. 
# there is1 ability per element combination and1 ability per ability type.
# an ability may have3 of the same element so effectively fire+fire+fire, fire+fire+water, ...
# there must be a technique, a faith, a magic, a tech, and a skill ability for each element combination.
# ability types are: technique, faith, magic, tech, skill
# elements are: fire, water, earth, air, light, dark, ice, electric
# ability type mappings to character and hostile stats:
# technique: strength, constitution...physical attack, physical defense
# faith: intelligence, constitution...spiritual attack, spiritual defense; healing power; debuff power
# magic: intelligence...magical attack, magical defense; debuff power
# tech: intelligence, dexterity...tech attack, tech defense; debuff power
# skill: dexterity, strength...speed, critical hit rate; evasion
"""56 element triples *5 ability types =280 level3 abilities
This file previously contained an explicit static list of all level-3 player ability seeds.
Ability-type-specific seeds have been moved into per-type modules under
level_3_abilities_by_type/*. Each module exposes a list named
LEVEL_3_<TYPE>_SEEDS which are imported and concatenated below.
"""

from .level_3_abilities_by_type.technique import LEVEL_3_TECHNIQUE_SEEDS
from .level_3_abilities_by_type.faith import LEVEL_3_FAITH_SEEDS
from .level_3_abilities_by_type.magic import LEVEL_3_MAGIC_SEEDS
from .level_3_abilities_by_type.tech import LEVEL_3_TECH_SEEDS
from .level_3_abilities_by_type.skill import LEVEL_3_SKILL_SEEDS

# Master list assembled from per-type seed modules
LEVEL_3_PLAYER_ABILITY_SEEDS = []
LEVEL_3_PLAYER_ABILITY_SEEDS.extend(LEVEL_3_TECHNIQUE_SEEDS)
LEVEL_3_PLAYER_ABILITY_SEEDS.extend(LEVEL_3_FAITH_SEEDS)
LEVEL_3_PLAYER_ABILITY_SEEDS.extend(LEVEL_3_MAGIC_SEEDS)
LEVEL_3_PLAYER_ABILITY_SEEDS.extend(LEVEL_3_TECH_SEEDS)
LEVEL_3_PLAYER_ABILITY_SEEDS.extend(LEVEL_3_SKILL_SEEDS)

# Additional handcrafted seeds that are not part of the generated per-type lists
# (kept here if any special-case entries are required)
# Example preserved seeds may be added below as dicts.

# End of file