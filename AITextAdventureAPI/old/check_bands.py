import sys
sys.path.insert(0,'.')
from collections import defaultdict

def missing_bands(seeds):
    bc = defaultdict(int)
    for s in seeds:
        lv = s.get('min_spawn_level',0)
        if 1 <= lv <= 100:
            band = ((lv-1)//10)*10+1
            bc[band]+=1
    return [f'{b}-{b+9}' for b in range(1,100,10) if b not in bc]

from game.region_seeds.regions.cities.forest.enemies_mid.lv21to100 import RANDOM_HOSTILE_SEEDS as a
from game.region_seeds.regions.cities.forest.enemies_small.lv21to100 import RANDOM_HOSTILE_SEEDS as b
from game.region_seeds.regions.cities.grassland.enemies_large.lv21to100 import RANDOM_HOSTILE_SEEDS as c
from game.region_seeds.regions.cities.grassland.enemies_mid.lv21to100 import RANDOM_HOSTILE_SEEDS as d
from game.region_seeds.regions.cities.grassland.enemies_small.lv21to100 import RANDOM_HOSTILE_SEEDS as e
from game.region_seeds.regions.cities.mountains.enemies_large.lv21to100 import RANDOM_HOSTILE_SEEDS as f
from game.region_seeds.regions.cities.mountains.enemies_mid.lv21to100 import RANDOM_HOSTILE_SEEDS as g
from game.region_seeds.regions.cities.mountains.enemies_small.lv21to100 import RANDOM_HOSTILE_SEEDS as h
from game.region_seeds.regions.cities.shallows.enemies_large.lv21to100 import RANDOM_HOSTILE_SEEDS as i_
from game.region_seeds.regions.cities.shallows.enemies_mid.lv21to100 import RANDOM_HOSTILE_SEEDS as j_
from game.region_seeds.regions.cities.shallows.enemies_small.lv21to100 import RANDOM_HOSTILE_SEEDS as k_
from game.region_seeds.regions.cities.snow.enemies_large.lv21to100 import RANDOM_HOSTILE_SEEDS as l_
from game.region_seeds.regions.cities.snow.enemies_mid.lv21to100 import RANDOM_HOSTILE_SEEDS as m_
from game.region_seeds.regions.cities.snow.enemies_small.lv21to100 import RANDOM_HOSTILE_SEEDS as n_
from game.region_seeds.regions.cities.swamp.enemies_large.lv21to100 import RANDOM_HOSTILE_SEEDS as o_
from game.region_seeds.regions.cities.swamp.enemies_mid.lv21to100 import RANDOM_HOSTILE_SEEDS as p_
from game.region_seeds.regions.cities.swamp.enemies_small.lv21to100 import RANDOM_HOSTILE_SEEDS as q_

for name, seeds in [
    ('Forest Mid', a), ('Forest Small', b),
    ('Grassland Large', c), ('Grassland Mid', d), ('Grassland Small', e),
    ('Mountains Large', f), ('Mountains Mid', g), ('Mountains Small', h),
    ('Shallows Large', i_), ('Shallows Mid', j_), ('Shallows Small', k_),
    ('Snow Large', l_), ('Snow Mid', m_), ('Snow Small', n_),
    ('Swamp Large', o_), ('Swamp Mid', p_), ('Swamp Small', q_),
]:
    miss = missing_bands(seeds)
    if miss:
        print(f'{name}: missing {miss}')

# Also check the full combined datasets
from game.constants import REGION_DATA
from tui.services.dev.dataservices.city_region_validator import validate_region_data
sys.path.insert(0, '..')
nodes = validate_region_data(REGION_DATA)
errors = sum(1 for n in nodes for e in n.errors if e.severity == 'error')
warnings = sum(1 for n in nodes for e in n.errors if e.severity == 'warning')
print(f'\nVALIDATOR: {errors} error(s), {warnings} warning(s)')
for n in nodes:
    errs = [e for e in n.errors if e.severity == 'error']
    if errs:
        print(f'  {n.label}: {len(errs)} errors')
        for e in errs:
            print(f'    {e.message}')
