import random
from typing import Optional, List

from game.objects.player import Player
from game.objects.player_game import PlayerGame
import game.constants_items as const_items
import game.constants_other as const_other

from game.objects.weapon import Weapon, _instantiate_weapon
from game.objects.armor import Armor, _instantiate_armor

from game.region_seeds.player_abilities.ability_requirements import ABILITY_TYPE_REQUIREMENTS

# Import equipment & ability selection helpers directly
from combat_balancing_simulation.player_generator_equipment_service import (
    meets_ability_requirements,
    _resolve_stat_weights,
    select_weapon,
    select_armor,
    select_utility_items,
    #select_abilities,
    pick_abilities_for_player,
    equip_player_gear,
)

def equip_player_character(player: Player, player_game = PlayerGame, focus: str = 'technique'):
    # Determine ability type focus and corresponding stat weights
    ability_type_focus = focus
    stat_fallback = None
    
    # derive stat weights (function returns a dict mapping stat -> weight)
    weights = _resolve_stat_weights(ability_type_focus)
    
    equip_player_gear(player, player_game, ability_type_focus)


def generate_player(name: str = 'Test', focus: str = 'technique', target_level: int =15, seed: Optional[int] = None, player_game = PlayerGame) -> Player:
    """Generate a test Player focused on `focus`.

    `focus` IS  an ability_type (e.g. 'technique','magic'). When an
    ability_type id is provided, ABILITY_TYPE_REQUIREMENTS will determine stat
    weights used for allocation and gear/ability preferences.
    """
    rng = random.Random(seed)
    p = Player(name)
    p.level =1

    # determine whether focus refers to an ability type
    ability_type_focus = focus
    stat_fallback = None

    # derive stat weights (function returns a dict mapping stat -> weight)
    weights = _resolve_stat_weights(ability_type_focus)

    # Initial distribution at level1: use initial_stat_distribution_amount and power points
    init_points = int(getattr(p, 'initial_stat_distribution_amount',10))\

    # reserved_points =  int(round(init_points *2.0 /3.0))
    # reserved_points = min(reserved_points, init_points)
    reserved_points = init_points
    random_distribution_points = init_points - reserved_points
    #get the total amount weights in order to calculate proportions
    total_weight = sum(weights.values()) or 1.0
    s_inc = d_inc = c_inc = i_inc =0
    #allocate reserved points according to weights
    for stat in ('strength', 'dexterity', 'constitution', 'intelligence'):
        share = int((weights.get(stat,0.0) / total_weight) * reserved_points)
        if stat == 'strength':
            s_inc += share
        elif stat == 'dexterity':
            d_inc += share
        elif stat == 'constitution':
            c_inc += share
        elif stat == 'intelligence':
            i_inc += share

    #allocate any leftover reserved points to the highest-weight stat
    allocated = s_inc + d_inc + c_inc + i_inc
    leftover = reserved_points - allocated
    if leftover >0:
        top_stat = max(weights.items(), key=lambda x: x[1])[0]
        if top_stat == 'strength':
            s_inc += leftover
        elif top_stat == 'dexterity':
            d_inc += leftover
        elif top_stat == 'constitution':
            c_inc += leftover
        else:
            i_inc += leftover

    #allocate random distribution points randomly across all four stats
    all_stats = ['strength', 'dexterity', 'constitution', 'intelligence']
    for _ in range(random_distribution_points):
        pick = rng.choice(all_stats)
        if pick == 'strength':
            s_inc +=1
        elif pick == 'dexterity':
            d_inc +=1
        elif pick == 'constitution':
            c_inc +=1
        elif pick == 'intelligence':
            i_inc +=1

    # initial power points allocation: split proportional to constitution vs intelligence
    pp = int(getattr(p, 'power_points_per_level',10))
    total = max(1, p.constitution + p.intelligence)
    hp_points = int(round(pp * (p.constitution / float(total))))
    ap_points = pp - hp_points

    p.upgrade_stats(str_inc=s_inc, dex_inc=d_inc, con_inc=c_inc, int_inc=i_inc, hp_points=hp_points, ap_points=ap_points)

    # Simulate leveling from2..target_level
    for new_level in range(2, max(2, target_level +1)):
        # increment level
        p.gain_experience(p.get_required_experience_to_level())

        # Deterministically compute level-up awards
        has_new_ability, stat_points, power_points = p.check_level_up_awards()

        # Distribute stat_points using ABILITY_TYPE_REQUIREMENTS-derived weights
        s_inc = d_inc = c_inc = i_inc =0
        pts = int(stat_points or 0)
        if pts >0:
            biased = int(round(pts *2.0 /3.0))
            biased = min(biased, pts)
            remaining_pts = pts - biased

            # compute weights for this allocation step (re-resolve to be safe)
            alloc_weights = _resolve_stat_weights(ability_type_focus)
            total_alloc_w = sum(alloc_weights.values()) or 1.0

            # distribute biased points proportionally to alloc_weights
            for stat in ('strength', 'dexterity', 'constitution', 'intelligence'):
                share = int((alloc_weights.get(stat,0.0) / total_alloc_w) * biased)
                if stat == 'strength':
                    s_inc += share
                elif stat == 'dexterity':
                    d_inc += share
                elif stat == 'constitution':
                    c_inc += share
                elif stat == 'intelligence':
                    i_inc += share
            # allocate any leftover biased points to the highest-weight stat
            allocated = s_inc + d_inc + c_inc + i_inc
            leftover = biased - allocated
            if leftover >0:
                top_stat = max(alloc_weights.items(), key=lambda x: x[1])[0]
                if top_stat == 'strength':
                    s_inc += leftover
                elif top_stat == 'dexterity':
                    d_inc += leftover
                elif top_stat == 'constitution':
                    c_inc += leftover
                else:
                    i_inc += leftover

            # distribute remaining points randomly across all four stats
            all_stats = ['strength', 'dexterity', 'constitution', 'intelligence']
            for _ in range(remaining_pts):
                pick = rng.choice(all_stats)
                if pick == 'strength':
                    s_inc +=1
                elif pick == 'dexterity':
                    d_inc +=1
                elif pick == 'constitution':
                    c_inc +=1
                elif pick == 'intelligence':
                    i_inc +=1

        # allocate power points proportionally to constitution vs intelligence
        total = max(1, p.constitution + p.intelligence)
        hp_pts = int(round(power_points * (p.constitution / float(total))))
        ap_pts = int(power_points - hp_pts)

        # apply upgrades (stats + power points) before selecting abilities
        p.upgrade_stats(str_inc=s_inc, dex_inc=d_inc, con_inc=c_inc, int_inc=i_inc, hp_points=hp_pts, ap_points=ap_pts)

        # now if an ability is granted this level, pick one and learn it
        if has_new_ability:
            allowed_elements = set(['fire', 'water', 'earth', 'air', 'light', 'dark'])
            picks = pick_abilities_for_player(p,1, allowed_elements, ability_type_focus, rng)
            if picks:
                chosen = picks[0]
                p.learn_ability(chosen)

    equip_player_gear(p, player_game, ability_type_focus)

    return p
