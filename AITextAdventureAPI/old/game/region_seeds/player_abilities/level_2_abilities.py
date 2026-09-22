import game.region_seeds.player_abilities.level_2_abilities_by_type as level_2_abilities

#LEVEL2 Abilities can have2 elements. 
# there is1 ability per element combination and1 ability per ability type.
# an ability may have2 of the same element so effectively fire+fire, fire+wind, fire+water, fire+earth, fire+light, fire+dark
# there must be a technique, a spirit, a magic, a tech, and a skill ability for each element combination.
# ability types are: technique, spirit, magic, tech, skill
# elements are: fire, water, earth, air, light, dark, ice, electric
# ability type mappings to character and hostile stats:
# technique: strength, constitution...physical attack, physical defense
# spirit: intelligence, constitution...spiritual attack, spiritual defense; healing power; debuff power
# magic: intelligence...magical attack, magical defense; debuff power
# tech: intelligence, dexterity...tech attack, tech defense; debuff power
# skill: dexterity, strength...speed, critical hit rate; evasion
"""35 possibilities *5 ability types =175 level2 abilities
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

LEVEL_2_PLAYER_ABILITY_SEEDS = level_2_abilities.LEVEL_2_TECH_ABILITY_SEEDS + level_2_abilities.LEVEL_2_SPIRIT_ABILITY_SEEDS + level_2_abilities.LEVEL_2_MAGIC_ABILITY_SEEDS + level_2_abilities.LEVEL_2_SKILL_ABILITY_SEEDS + level_2_abilities.LEVEL_2_TECHNIQUE_ABILITY_SEEDS




