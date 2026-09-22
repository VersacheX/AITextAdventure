"""
Script to reseed/random-hostile seeds by computing a combat score per seed
and assigning rarity buckets to match desired spawn weights.
Outputs a JSON file with reseeded hostiles and prints summary stats.

Usage: run this script from project root with python -m old.combat_balancing_simulation.balance_seed_reseeder
"""
import json
import math
import os
import random
from tkinter import SE
from typing import List, Dict, Any, Tuple

import game.constants as const
from game.objects.random_hostile import RandomHostile
from game.objects.item import instantiate_item_from_id, Item

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "reseeded_hostiles.json")

# Tunable weights for scoring
W_HP = .01
W_DPS = 1.0
W_DEF = 0.8
W_AP = 0.8
W_AB = 1.5

#players get 10 to start + 8 to each stat starting with a total of 42... they then get 6 to distribute/level
RARITY_STAT_POOLS = {
    "common": {"start": 5, "per_level_distribution_amount": 5.5, "power_points_per_level": 8},
    "uncommon": {"start": 6, "per_level_distribution_amount": 6, "power_points_per_level": 10},
    "rare": {"start": 7, "per_level_distribution_amount": 6.5, "power_points_per_level": 15},
    "superrare": {"start": 8, "per_level_distribution_amount": 7, "power_points_per_level": 20},
    "notfound": {"start": 15, "per_level_distribution_amount": 10, "power_points_per_level": 25},
}

# Rarity weights used to compute per-region counts proportionally.
# Interpreted as relative weights: common gets the largest share, superrare the smallest.
RARITY_WEIGHTS = {
 "common":7,
 "uncommon":5,
 "rare":3,
 "superrare":1,
}


# Canonical ordering from rarest to most common when assigning the top combat scores
RARITY_ORDER_DESC = ["superrare", "rare", "uncommon", "common"]
# Small stat boosts for higher rarities (applied AFTER rarity assignment)
RARITY_STAT_BOOSTS = {
 "notfound": 1.5,
 "superrare": 1.25,
 "rare": 1.15,
 "uncommon": 1.06,
 "common": 1.0,
}

# Region -> allowed base elements mapping (strings match ability element values)
REGION_ALLOWED_BASE_ELEMENTS = {
 'DESERT': {'air', 'earth'},
 'FOREST': {'water', 'earth'},
 'GRASSLAND': {'air', 'earth', 'electric'},
 'MOUNTAINS': {'earth', 'fire', 'electric'},
 'SHALLOWS': {'water'},
 'SNOW': {'ice', 'earth', 'air'},
 'SWAMP': {'dark'},
}

# Rarity -> desired assigned ability counts
RARITY_ABILITY_COUNTS = {
 'common':0,
 'uncommon':1,
 'rare':2,
 'superrare':3,
 'notfound':4,
}

# Rarity -> affinity category assignment for weaknesses/resistances/immunities
# common -> weakness, uncommon -> resistance, rare -> immunity, superrare -> immunity
RARITY_AFFINITY_CATEGORY = {
 'common': 'weaknesses',
 'uncommon': 'resistances',
 'rare': 'immunities',
 'superrare': 'immunities',
 'notfound': 'immunities',
}

# All canonical elements
CANONICAL_ELEMENTS = ['light', 'dark', 'water', 'earth', 'fire', 'air', 'electric', 'ice']

REVERSE_ELEMENTS = {
 'light': 'dark',
 'dark': 'light',
 'water': 'fire',
 'fire': 'ice',
 'ice': 'air',
 'air': 'earth',
 'earth': 'electric',
 'electric': 'water'
}

# -----------------------------------------------------------------------------
# New: expected player equipment scaling
# If player characters typically have equipment that boosts their effective
# combat power, we should scale hostile derived stats upward so reseeding and
# combat score comparison account for that. Tweak this multiplier to reflect
# how much stronger players become from equipment (1.0 = no adjustment).
PLAYER_EQUIPMENT_STAT_SCALE = 1.1
# -----------------------------------------------------------------------------


################# GET EXISTING SEEDS #################
def gather_all_seeds() -> List[Tuple[str, Dict[str, Any]]]:
    """Find all variables in game.constants whose name ends with _RANDOM_HOSTILE_SEEDS and collect seeds.
    Returns list of tuples (region_key, seed_dict).
    """
    seeds: List[Tuple[str, Dict[str, Any]]] = []
    for name in dir(const):
        if name.upper().endswith("_RANDOM_HOSTILE_SEEDS"):
            val = getattr(const, name)
            if isinstance(val, list):
                for s in val:
                    if isinstance(s, dict):
                        # attach region name for traceability
                        seeds.append((name, dict(s)))
    return seeds

def region_key_to_region_name(region_key: str) -> str:
    """Derive a simple region name from a region_key like DESERT_SMALL_CITY_RANDOM_HOSTILE_SEEDS -> DESERT"""
    if not region_key:
        return "UNKNOWN"
    parts = region_key.split("_")
    if parts:
        return parts[0].upper()
    return region_key.upper()


########### RESEED EXISTING HOSTILES ##############
def reseed_existing_hostile(e, retain_abilities = False) -> None: 
    generate_derived_stats(e)  
    reseed_hostile(e, retain_abilities = retain_abilities) 
    apply_rarity_boost_and_awards(e)

def generate_derived_stats(e) -> None:
    level = int(e.get('min_spawn_level',1) or 1)
    derived = estimate_stats_from_seed(e["seed"], level)  # Corrected to use 'e["seed"]'
    e['derived'] = derived

def reseed_hostile(e, retain_abilities = False) -> None:
    seed = e["seed"]
    rid = e.get("region_key")
    if rid:
        region_name = region_key_to_region_name(rid)
    else:
        region_name = None
    allowed = REGION_ALLOWED_BASE_ELEMENTS.get(region_name, [])

    rarity = e.get("assigned_rarity") or e.get("seed", {}).get("assigned_rarity") or "common"

    desired_abil_count = int(RARITY_ABILITY_COUNTS.get(rarity,0))
    existing = seed.get("player_abilities") or []
    cleaned_existing = []
    # if retain_abilities do not clean
    if not retain_abilities:
        if existing and isinstance(existing, list):
            all_abils = const.PLAYER_ABILITY_SEEDS
            lookup = {a.get('id'): a for a in all_abils if a and isinstance(a, dict) and a.get('id')}
            for aid in existing:
                a = lookup.get(aid)
                if not a:
                    continue
                elems = [str(x).lower() for x in (a.get('elements') or [])]
                if any(x in allowed for x in elems):
                    #ensure derived stats meet requirements
                    if meets_requirements(a, e, a.get('level')):
                        cleaned_existing.append(aid)
        #print (f'cleaned existing abilities for {seed.get("name")}: {cleaned_existing}')
    else:
        cleaned_existing = existing if isinstance(existing, list) else []

    print (f'desired ability count for rarity {rarity}: {desired_abil_count}, existing cleaned: {cleaned_existing}')
    if len(cleaned_existing) < desired_abil_count and len(allowed) > 0:
        to_pick = max(0, desired_abil_count - len(cleaned_existing))
        picks = select_abilities_for_seed(seed, allowed, to_pick, int(e.get('min_spawn_level',1) or 1))
        assigned_abilities = list(cleaned_existing) + picks
        #print (f'picked additional abilities for {seed.get("name")}: {picks}')
    else:
        assigned_abilities = cleaned_existing
    #print (f'assigned abilities for {seed.get("name")}: {assigned_abilities}')

    seed['player_abilities'] = assigned_abilities if assigned_abilities else None
    #input(f'final assigned abilities for {seed.get("name")}: {seed["player_abilities"]}')
    # choose primary element
    all_abils = const.PLAYER_ABILITY_SEEDS
    lookup = {a.get('id'): a for a in all_abils if a and isinstance(a, dict) and a.get('id')}
    assigned_ids = seed.get('player_abilities') or []
    primary_elem = None
    if assigned_ids and isinstance(assigned_ids, list) and len(assigned_ids) >0:
        abil_elems = []
        for aid in assigned_ids:
            a = lookup.get(aid)
            if not a:
                continue
            for el in (a.get('elements') or []):
                abil_elems.append(str(el).lower())
        for el in abil_elems:
            if el in allowed:
                primary_elem = el
                break
        if not primary_elem and abil_elems:
            primary_elem = abil_elems[0]

    if not primary_elem:
        pref_order = ['air', 'earth', 'water', 'fire', 'dark', 'light']
        for p in pref_order:
            if p in allowed:
                primary_elem = p
                break
    if not primary_elem:
        primary_elem = pick_element_for_affinity(seed.get('id') or seed.get('name') or '')

    opposite_elem = REVERSE_ELEMENTS.get(primary_elem, pick_element_for_affinity(seed.get('id') or seed.get('name') or '', excluded=[primary_elem]))

    rid = str(seed.get('id') or seed.get('name') or '')
    rseed = abs(hash(rid)) &0xFFFFFFFF
    rnd = random.Random(rseed)

    p_immunity =0.0
    if rarity == 'rare':
        p_immunity =0.05
    elif rarity == 'superrare':
        p_immunity =0.25

    p_resistance =0.0
    if rarity == 'uncommon':
        p_resistance =0.25
    elif rarity == 'rare':
        p_resistance =0.4
    elif rarity == 'superrare':
        p_resistance =0.4

    p_weakness =0.15

    seed['weaknesses'] = seed.get('weaknesses') or []
    seed['resistances'] = seed.get('resistances') or []
    seed['immunities'] = seed.get('immunities') or []

    if rnd.random() < p_immunity:
        seed['immunities'] = [primary_elem]
    elif rnd.random() < p_resistance:
        seed['resistances'] = [primary_elem]
    elif rnd.random() < p_weakness:
        seed['weaknesses'] = [opposite_elem]

def apply_rarity_boost_and_awards(e) -> None:
    seed = e['seed']
    rarity = e.get('assigned_rarity') or e.get('seed', {}).get('assigned_rarity') or 'common'
    e['assigned_rarity'] = rarity
    seed['assigned_rarity'] = rarity

    boost = float(RARITY_STAT_BOOSTS.get(rarity,1.0))
    derived = e.get('derived', {})
    for k in ['hp', 'dps', 'defense', 'ap_pool', 'ability_pot']:
        if k in derived:
            derived[k] = float(round(float(derived[k]) * boost,2))

    level = int(e.get('min_spawn_level',1) or 1)
    new_score = compute_combat_score(derived, level)
    e['combat_score'] = float(round(new_score,3))
    seed['computed_combat_score'] = e['combat_score']

    xp = int(max(5, round(e['combat_score'] *0.35)))
    if rarity == 'uncommon':
        xp = int(xp *1.2)
    elif rarity == 'rare':
        xp = int(xp *1.6)
    elif rarity == 'superrare':
        xp = int(xp *2.4)
    seed['suggested_xp_reward'] = xp

#players get 10 to start + 8 to each stat starting with a total of 42... they then get 6 to distribute/level
# RARITY_STAT_POOLS = {
#     "common": {"start": 2, "per_level_distribution_amount": 4},
#     "uncommon": {"start": 4, "per_level_distribution_amount": 5},
#     "rare": {"start": 6, "per_level_distribution_amount": 6},
#     "superrare": {"start": 8, "per_level_distribution_amount": 7},
#     "notfound": {"start": 15, "per_level_distribution_amount": 10},
# }
########### ESTIMATE DERIVED STATS ##############
def estimate_stats_from_seed(seed: Dict[str, Any], level: int) -> Dict[str, float]:
    """Estimate derived numeric stats for a hostile seed at given level.
    Returns dict with hp, dps, defense, ap_pool, ability_power.
    """
    #print (f'seed name: {seed.get("name")}, level: {level}')
    rarity = seed.get("rarity")
    # base stats from seed or defaults
    base_str = RARITY_STAT_POOLS[rarity]["start"]
    base_dex = RARITY_STAT_POOLS[rarity]["start"]
    base_con = RARITY_STAT_POOLS[rarity]["start"]
    base_int = RARITY_STAT_POOLS[rarity]["start"]
    #print (f'start stats: {base_str}, {base_dex}, {base_con}, {base_int}')

    str_per = int(seed.get("str_per_level", 0) or 0)+1
    dex_per = int(seed.get("dex_per_level", 0) or 0)+1
    con_per = int(seed.get("con_per_level", 0) or 0)+1
    int_per = int(seed.get("int_per_level", 0) or 0)+1
    #print (f'per level stats: {str_per}, {dex_per}, {con_per}, {int_per}')
    total_exist_per = str_per + dex_per + con_per + int_per
    per_level_dist_amt = RARITY_STAT_POOLS[rarity]["per_level_distribution_amount"]

    seed["str_per_level"] = (str_per /total_exist_per) * per_level_dist_amt
    seed["dex_per_level"] = (dex_per /total_exist_per) * per_level_dist_amt
    seed["con_per_level"] = (con_per /total_exist_per) * per_level_dist_amt
    seed["int_per_level"] = (int_per /total_exist_per) * per_level_dist_amt
    #print (f'per level stats set in seed: {seed["str_per_level"]}, {seed["dex_per_level"]}, {seed["con_per_level"]}, {seed["int_per_level"]}')
    seed["base_str"] = int(base_str + seed["str_per_level"] * level)
    seed["base_dex"] = int(base_dex + seed["dex_per_level"] * level)
    seed["base_con"] = int(base_con + seed["con_per_level"] * level)
    seed["base_int"] = int(base_int + seed["int_per_level"] * level)    
    
    #print (f'base stats set in seed: {base_str}, {base_dex}, {base_con}, {base_int}')

    strength = int(base_str + (seed["str_per_level"] * level))
    dexterity = int(base_dex + (seed["dex_per_level"] * level)) 
    constitution = int(base_con + (seed["con_per_level"] * level))
    intelligence = int(base_int + (seed["int_per_level"] * level))
    #input (f'final stats at level {level}: {strength}, {dexterity}, {constitution}, {intelligence}')

    min_level = int(seed.get("min_spawn_level", 1) or 1)
    calculate_base_pp = RARITY_STAT_POOLS[rarity]["start"] * 2
    pp_per_level = RARITY_STAT_POOLS[rarity]["power_points_per_level"]
    abil_count = max(len(seed.get("player_abilities") or []), RARITY_ABILITY_COUNTS.get(rarity, 0))
    hp_dist = 1.0 - (abil_count*0.05)# (seed["str_per_level"] +seed["con_per_level"]) / (seed["dex_per_level"] + seed["int_per_level"]) if (seed["dex_per_level"] + seed["int_per_level"]) > 0 else 0.6
    hp_per_level = pp_per_level * (hp_dist)
    ap_per_level = pp_per_level * (1.0 - hp_dist)
    base_hp = calculate_base_pp + int(hp_per_level * min_level)
    base_ap = calculate_base_pp + int(ap_per_level * min_level)
    seed["base_hp"] = base_hp
    seed["base_ap"] = base_ap

    hp = max(3, base_hp + constitution * 2 + int(level * hp_per_level))

    ap_pool = max(0, base_ap + (level * ap_per_level))

    #base_damage += max(1, int(self.get_modified_strength() + (self.level //1)))
    dps = max(1.0, float(strength) * 0.5 + float(dexterity) * 0.3 + float(level) * 0.2)
    # DPS estimate: roughly weaponless damage ~ strength *0.5 + level *0.5

    # Defense: for now approximate as half the constitution value
    # (this is an interim heuristic; can be tuned later)
    defense = max(0.0, float(constitution *0.5))

    # Ability potential: sum of ability base_power from seeds referenced (best-effort)
    ab_pot = 0.0
    abilities = seed.get("player_abilities") or []
    if abilities and isinstance(abilities, list):
        # find ability seeds in constants_other PLAYER_ABILITY_SEEDS
        all_abils = const.PLAYER_ABILITY_SEEDS
        lookup = {a.get("id"): a for a in all_abils if a and isinstance(a, dict) and a.get("id")}
        for aid in abilities:
            s = lookup.get(aid)
            if s:
                lv = int(s.get("level", 1) or 1)
                bp = float(s.get("base_power", 10) or 10)
                # estimated ability potency scales with level
                ab_pot += bp * (1.0 + 0.2 * (lv - 1))

    #compute dps off damage abilities
    dps = max(dps, ab_pot * 0.3)

    # Apply expected player equipment scaling to derived numeric stats so hostiles
    # created for simulation more closely match the effective power of equipped players.
    scale = float(PLAYER_EQUIPMENT_STAT_SCALE or 1.0)

    return {
        "strength": float(strength) * scale,
        "dexterity": float(dexterity) * scale,
        "constitution": float(constitution) * scale,
        "intelligence": float(intelligence) * scale,
        "hp": float(hp) * scale,
        "dps": float(dps) * scale,
        "defense": float(defense) * scale,
        "ap_pool": float(ap_pool) * scale,
        "ability_pot": float(ab_pot) * scale,
}

################ ASSIGN ABILITIES AND AFFINITIES ##############
def pick_element_for_affinity(seed_id: str, excluded: List[str] = None) -> str:
    """Deterministically pick an element based on seed id, excluding any in excluded."""
    excluded = excluded or []
    candidates = [e for e in CANONICAL_ELEMENTS if e not in excluded]
    if not candidates:
        return CANONICAL_ELEMENTS[0]
    # deterministic index
    idx = abs(hash(seed_id)) % len(candidates)
    return candidates[idx]

def meets_requirements(ability: Dict[str, Any], seed_stats: Dict[str, float], ability_level: int) -> bool:
    # load ability-type requirements map
    from game.region_seeds.player_abilities.ability_requirements import ABILITY_TYPE_REQUIREMENTS

    req_map = {}
    for entry in (ABILITY_TYPE_REQUIREMENTS or []):
        t = entry.get('ability_type')
        req_map[t] = entry.get('required_stats_per_ability_level', [])

    # If no requirements known, allow by default
    atype = (ability.get('ability_type') or '').lower()
    reqs = req_map.get(atype)
    if not reqs:
        return True
    # For each alternative requirement dict, check if all stats meet scaled requirement
    for rdict in reqs:
        ok = True
        for stat_name, stat_val in rdict.items():
            # scaled requirement: ability_level^2 * stat_val
            required = int(stat_val) + int((int(stat_val) * ((ability_level - 1)* 1.5)) **1.25)
            # map stat_name to seed_stats key if necessary
            s_val = int(seed_stats.get(stat_name,0))
            if s_val < required:
                ok = False
                break
        if ok:
            return True
    return False

def select_abilities_for_seed(seed: Dict[str, Any], allowed_elements: set, desired_count: int, level: int) -> List[str]:
    """Select up to desired_count ability ids from PLAYER_ABILITY_SEEDS that include at least one allowed element.
    Preference: ability level <= seed level +1, higher base_power and level first.

    """
    all_abils = const.PLAYER_ABILITY_SEEDS
    ability_requirements = const.ABILITY_TYPE_REQUIREMENTS

    # compute seed numeric stats once
    seed_stats = estimate_stats_from_seed(seed, level)
    candidates = []
    for a in all_abils:
        if not a or not isinstance(a, dict):
            print (f'skipping invalid ability: {a}')
            continue
        elems = a.get('elements') or []
        # normalize elements to lowercase strings
        elems_norm = [str(x).lower() for x in elems]
        # require that the ability includes at least one allowed element
        if not any(e in allowed_elements for e in elems_norm):
            #print (f'skipping ability {a.get("id")} due to element mismatch: {elems_norm} vs allowed {allowed_elements}')
            continue
        # prefer abilities close to level
        alv = int(a.get('level', 1) or 1)
        bp = float(a.get('base_power', 0) or 0)        
        effect = a.get('effect')
        #status_key = a.get('status_key') if a.get('status_key') else None
        
        # enforce stat requirements scaled by ability level squared
        if not meets_requirements(a, seed_stats, alv):
            #print (f'skipping ability {a.get("id")} due to unmet requirements at level {alv}')
            continue
        candidates.append(a)
    #print (f'found {len(candidates)} candidate abilities for seed {seed.get("name")} at level {level}')
    # sort candidates by level closeness and base_power desc
    # score = -(abs(alv - level)) *1000 + bp -> higher is better
    sorted_cands = sorted(candidates, key=lambda t: (abs(t['level'] - level), -t['base_power']))
    
    selected = get_role_based_abilities(seed, sorted_cands, desired_count)
    #print (f'selected abilities for seed {seed.get("name")}: {len(selected)} of {len(sorted_cands)}')
    # selected = [c[0] for c in sorted_cands[:desired_count]]
    #input (f'sorted candidates: {sorted_cands}')
    return selected

def get_role_based_abilities(seed, sorted_cands, desired_count):
    """
    choose from the strongest matches that meet stat requirements.
    ABILITY_TYPE_REQUIREMENTS = [
        {"ability_type": "technique", "required_stats_per_ability_level": [{"strength": 13, "constitution": 9}]},
        {"ability_type": "spirit", "required_stats_per_ability_level": [{"intelligence": 13}, {"constitution": 9}]},
        {"ability_type": "magic", "required_stats_per_ability_level": [{"intelligence": 18}]},
        {"ability_type": "tech", "required_stats_per_ability_level": [{"intelligence": 13}, {"dexterity": 9}]},
        {"ability_type": "skill", "required_stats_per_ability_level": [{"dexterity": 18}]},
    ]
    """
    from game.region_seeds.player_abilities.ability_requirements import ABILITY_TYPE_REQUIREMENTS
    remaining = list(sorted_cands)
    selected = []

    # deterministic RNG per-seed for stable shuffling
    const_rand = abs(hash(seed.get('id') or seed.get('name') or ''))
    rnd = random.Random(const_rand)

    # compute seed derived stats at seed min level for scoring purposes
    level_for_seed = int(seed.get('min_spawn_level', 1) or 1)
    seed_stats = estimate_stats_from_seed(seed, level_for_seed)

    # build quick lookup of ability type -> list of requirement dicts
    req_lookup = {}
    for entry in (ABILITY_TYPE_REQUIREMENTS or []):
        t = (entry.get('ability_type') or '').lower()
        req_lookup[t] = entry.get('required_stats_per_ability_level', []) or []

    # helper: scaled requirement formula (same as elsewhere in project)
    def scaled_required(per_level_val: int, ability_level: int) -> int:
        try:
            base = int(per_level_val)
        except Exception:
            base = 0
        if ability_level <= 1:
            return base
        # formula used in get_potential_player_abilities / meets_requirements
        return int(base + int((base * ((ability_level - 1) * 1.5)) ** 1.25))

    # Precompute a match score for each candidate ability.
    # Score is the best (max) sum of (seed_stat - required) across alternative requirement dicts.
    # Higher score means the seed exceeds requirements by a larger margin.
    score_map = {}
    for abil in sorted_cands:
        aid = abil.get('id')
        if not aid:
            continue
        atype = (abil.get('ability_type') or '').lower()
        alv = int(abil.get('level', 1) or 1)
        reqs = req_lookup.get(atype) or []
        # If no reqs defined for this ability type, treat as neutral (score 0)
        if not reqs:
            score_map[aid] = 0
            continue

        best_score = None
        # Evaluate each alternative requirement dict and keep best (highest) total margin
        for rdict in reqs:
            total_margin = 0
            for stat_name, per_level_val in (rdict.items()):
                req_val = scaled_required(per_level_val, alv)
                seed_val = int(seed_stats.get(stat_name, 0) or 0)
                margin = seed_val - req_val
                total_margin += margin
            if best_score is None or total_margin > best_score:
                best_score = total_margin
        # store best_score (can be negative if requirements not met)
        score_map[aid] = int(best_score or 0)
    ###################DULY NOTED NEED TO ADD ABILITY SELECTION BASED ON STAT DISTRIBUTION ###############
    def pick_group(group):
        nonlocal remaining, selected
        # iterate by level (highest first)
        for grp_level in sorted(set([int(s.get('level', 1) or 1) for s in group]), reverse=True):
            level_group = [s for s in group if int(s.get('level', 1) or 1) == grp_level]

            # bucket by (score, base_power) so we can deterministically shuffle ties
            buckets = {}
            for s in level_group:
                aid = s.get('id')
                sc = score_map.get(aid, 0)
                bp = float(s.get('base_power', 0) or 0)
                key = (sc, bp)
                buckets.setdefault(key, []).append(s)

            # process buckets in descending score, then descending base_power
            for (sc, bp) in sorted(buckets.keys(), key=lambda k: (k[0], k[1]), reverse=True):
                bucket = buckets[(sc, bp)]
                # deterministic shuffle within tied bucket
                rnd.shuffle(bucket)
                for abil in bucket:
                    if len(selected) >= desired_count:
                        return
                    if abil.get('id') not in selected:
                        selected.append(abil.get('id'))
                        if abil in remaining:
                            remaining.remove(abil)

    # Support first (if seed role is support)
    role = seed.get('role')
    if role == 'support':
        supp_abil_set = [
            abil for abil in sorted_cands
            if abil.get('effect') in ('revive', 'cure', 'heal')
            or (abil.get('effect') == 'status' and any(str(sk).endswith('_buff') for sk in (abil.get('status_keys') or [])))
        ]
        if supp_abil_set:
            pick_group(supp_abil_set)

    # Hazard abilities next if role isn't 'damage'
    if role != 'damage':
        hazard_abil_set = [
            abil for abil in sorted_cands
            if abil.get('effect') == 'status' and any(str(sk) in const.HARMFUL_STATUS_EFFECTS for sk in (abil.get('status_keys') or []))
        ]
        if hazard_abil_set:
            pick_group(hazard_abil_set)

    # Damage abilities next
    damage_abil_set = [c for c in sorted_cands if c.get('effect') == 'damage']
    if damage_abil_set:
        pick_group(damage_abil_set)

    # Filler: pick from remaining highest-level first
    if len(selected) < desired_count and remaining:
        pick_group(remaining)

    # Trim to desired_count and return
    return selected[:desired_count]


############ COMPUTE RARITY AND COMBAT SCORE ##############

def assign_rarities(all_entries: List[Dict[str, Any]]) -> None:
    """Assign rarity strings to entries in place for each region using proportional weights."""
    if not all_entries:
        return

    # Group entries by region
    regions: Dict[str, List[Dict[str, Any]]] = {}
    for e in all_entries:
        rk = e.get("region_key") or "UNKNOWN"
        regions.setdefault(rk, []).append(e)

    for rk, group in regions.items():
        # sort group by initial combat score descending
        sorted_group = sorted(group, key=lambda x: x["combat_score"], reverse=True)
        N = len(sorted_group)

        # compute per-rarity counts from weights so the final distribution approximates the
        # desired ratio (common:uncommon:rare:superrare -> weights)
        weights = dict(RARITY_WEIGHTS)
        total_weight = float(sum(weights.values())) if weights else 1.0

        # initial allocation (floor of proportional share)
        counts: Dict[str, int] = {}
        assigned = 0
        for r, w in weights.items():
            cnt = int(math.floor((float(w) / total_weight) * N))
            counts[r] = max(0, cnt)
            assigned += counts[r]

        # distribute any remaining slots (due to flooring) favoring the largest weight (common)
        remaining = N - assigned
        if remaining > 0:
            # order rarities by descending weight so commons get extra slots first
            order = sorted(weights.keys(), key=lambda k: weights[k], reverse=True)
            oi = 0
            while remaining > 0:
                r = order[oi % len(order)]
                counts[r] = counts.get(r, 0) + 1
                remaining -= 1
                oi += 1
        

        #use the original seed raririty only
        for entry in sorted_group:
            original_rarity = entry.get("seed", {}).get("rarity", "common")

def compute_combat_score(derived: Dict[str, float], level: int) -> float:
    raw = (
        W_HP * derived["hp"]
        + W_DPS * derived["dps"]
        + W_DEF * derived["defense"]
        + W_AP * derived["ap_pool"]
        + W_AB * derived["ability_pot"]
    )
    level_scale = 1.0 + float(level) * 0.05
    return raw * level_scale

#################### SAVE TO JSON ####################

def reseed_and_save(output_path: str = OUTPUT_PATH) -> None:
    entries = []
    # Perform full reseed pipeline and return entries for caller to use
    seeds = gather_all_seeds()
    # initial population
    for region_key, seed in seeds:
        lvl = int(seed.get("min_spawn_level",1) or 1)
        derived = estimate_stats_from_seed(seed, lvl)
        score = compute_combat_score(derived, lvl)
        entries.append({
        "region_key": region_key,
        "id": seed.get("id"),
        "name": seed.get("name"),
        "min_spawn_level": lvl,
        "seed": seed,
        "derived": derived,
        "combat_score": float(round(score,3)),
        })

    # assign rarities and attach abilities/affinities
    assign_rarities(entries)
    for e in entries:
        reseed_existing_hostile(e)

    # Save JSON output
    out = {
        "summary_count": len(entries),
        "generated_from": "game.constants *_RANDOM_HOSTILE_SEEDS",
        "entries": entries,
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    # Print short summary by region and overall
    counts_by_r = {}
    counts_by_region: Dict[str, Dict[str, int]] = {}
    for e in entries:
        r = e.get("assigned_rarity", "common")
        counts_by_r[r] = counts_by_r.get(r, 0) + 1
        rk = e.get("region_key") or "UNKNOWN"
        rr = counts_by_region.setdefault(rk, {})
        rr[r] = rr.get(r, 0) + 1

    print("Assigned rarity counts (global):", counts_by_r)
    print("Assigned rarity counts by region:")
    # print all region summaries
    for rk, summary in counts_by_region.items():
        print(f"  {rk}: {summary}")
    print(f"Wrote reseeded hostiles to {output_path}")
    return entries


####  INSTANTIATE FROM PROCESSED ENTRY  ####  
def _instantiate_random_hostile_from_seed(entry_or_seed: Dict[str, Any], level: int) -> RandomHostile:
    """Instantiate a RandomHostile from a processed entry or raw seed.

    If an `entry` produced by the reseed pipeline is provided, this will
    use `entry['seed']` and `entry['derived']`. Otherwise `entry_or_seed`
    may be a raw seed dict and derived stats will be computed.
    """
    # accept either an entry (with keys 'seed' and 'derived') or a raw seed dict
    entry = entry_or_seed if entry_or_seed.get('seed') is not None else None
    seed = entry.get('seed') if entry is not None else entry_or_seed
    # ensure seed is a dict
    seed = seed or {}

    # derived stats prefer entry['derived'] when present
    if entry is not None and entry.get('derived') is not None:
        derived = entry.get('derived')
        seed = derived.get('seed', seed)
    else:
        derived = estimate_stats_from_seed(seed, level)

    # local import to avoid cycles
    from game.objects.player_ability import _instantiate_from_seed as _inst_ability

    rh = RandomHostile()
    rh.id = str(seed.get('id') or '')
    rh.name = str(seed.get('name') or rh.name)
    rh.level = int(level)

    # core stats from derived (rounded)
    rh.strength = int(round(derived.get('strength', getattr(rh, 'strength',1))))
    rh.dexterity = int(round(derived.get('dexterity', getattr(rh, 'dexterity',1))))
    rh.constitution = int(round(derived.get('constitution', getattr(rh, 'constitution',1))))
    rh.intelligence = int(round(derived.get('intelligence', getattr(rh, 'intelligence',1))))

    # pools
    rh.max_hp = int(round(derived.get('hp', getattr(rh, 'max_hp',0))))
    rh.current_hp = int(round(derived.get('hp', getattr(rh, 'current_hp', rh.max_hp))))
    rh.max_ap = int(round(derived.get('ap_pool', getattr(rh, 'max_ap',0))))
    rh.current_ap = int(round(derived.get('ap_pool', getattr(rh, 'current_ap', rh.max_ap))))

    rh.base_hp = int(round(derived.get('hp', getattr(rh, 'base_hp',0))))
    rh.base_ap = int(round(derived.get('ap_pool', getattr(rh, 'base_ap',0))))

    rh.min_spawn_level = int(seed.get('min_spawn_level', getattr(rh, 'min_spawn_level',1)))
    rh.rarity = str(seed.get('rarity', getattr(rh, 'rarity', 'common')))
    rh.base_str = seed.get('base_str')
    rh.base_con = seed.get('base_con')
    rh.base_int = seed.get('base_int')
    rh.base_dex = seed.get('base_dex')
    rh.str_per_level = seed.get('str_per_level')
    rh.dex_per_level = seed.get('dex_per_level')
    rh.con_per_level = seed.get('con_per_level')
    rh.int_per_level = seed.get('int_per_level')
    rh.level = seed.get('min_spawn_level')

    # copy basic metadata
    rh.hostile_type = seed.get('hostile_type', getattr(rh, 'hostile_type', None))
    rh.basic_attack = seed.get('basic_attack', getattr(rh, 'basic_attack', ''))
    rh.strong_attack = seed.get('strong_attack', getattr(rh, 'strong_attack', ''))

    # loot / rewards
    
    rh.common_drop = instantiate_item_from_id(seed.get('common_drop', None))
    rh.rare_drop = instantiate_item_from_id(seed.get('rare_drop', None))
    rh.money_range = tuple(seed.get('money_range')) if seed.get('money_range') else getattr(rh, 'money_range', None)
    if rh.money_range:
        lo, hi = rh.money_range
        qty = random.randint(max(0, lo), max(lo, hi))
    else:
        qty = random.randint(1,20 + level *5)

    # affinities
    rh.weaknesses = list(seed.get('weaknesses') or [])
    rh.resistances = list(seed.get('resistances') or [])
    rh.immunities = list(seed.get('immunities') or [])

    # abilities: instantiate PlayerAbility objects when possible
    rh.abilities = []
    abil_ids = seed.get('player_abilities') or []
    if abil_ids and isinstance(abil_ids, list):
        all_abils = const.PLAYER_ABILITY_SEEDS
        lookup = {a.get('id'): a for a in all_abils if a and isinstance(a, dict) and a.get('id')}
        for aid in abil_ids:
            aseed = lookup.get(aid)
            if aseed:
                rh.abilities.append(_inst_ability(aseed))

    # attach XP/base xp if available
    if seed.get('base_xp') is not None:
        rh.base_xp = int(seed.get('base_xp'))
        
    if seed.get('suggested_xp_reward') is not None:
        rh.base_xp = int(seed.get('suggested_xp_reward'))
        
    rh.defense = int(round(derived.get('defense', getattr(rh, 'defense',0))))
    
    return rh



#################### Additional functions for selective seed picking
def pick_seeds_for_rarity(rarity: str, num: int, region_seeds, level) -> List[Dict[str, Any]]:
    candidates = [s for s in region_seeds if (s.get("rarity") == rarity)]
    preferred = []
    for s in candidates:
        min_lvl = int(s.get("min_spawn_level",1) or 1)
        if min_lvl > level - 5 and min_lvl <= level:
            preferred.append(s)
    rng = random.Random()
    picks = []
    if len(preferred) > 0:
        picks = [rng.choice(preferred) for _ in range(num)]
    return picks

def pick_highest_seeds_for_rarity(rarity: str, num: int, region_seeds, level) -> List[Dict[str, Any]]:
    """Monster Hunter rarity picker.

    Unlike `pick_seeds_for_rarity`, this ignores the ±5 level band because
    Monster Hunter draws from species the player has NOT yet logged, which are
    typically LOW level (missed while out-levelling earlier areas).

    It takes the highest-`min_spawn_level` seeds of the requested rarity that
    are AT OR BELOW the party level. It never returns over-level seeds: if no
    unlogged seed of this rarity qualifies, it returns an empty list so the
    caller's rarity-cascade reallocates the slot to a lower rarity rather than
    spawning an absurdly over-level enemy.
    """
    candidates = [
        s for s in region_seeds
        if s.get("rarity") == rarity
        and int(s.get("min_spawn_level", 1) or 1) <= level
    ]
    if not candidates:
        return []

    pool_sorted = sorted(
        candidates, key=lambda s: int(s.get("min_spawn_level", 1) or 1), reverse=True
    )

    # Fill `num` slots from the highest available downward, cycling if the pool
    # is smaller than the requested count so a rarity slot is never left empty
    # by *this* rarity when it does have qualifying seeds.
    return [pool_sorted[i % len(pool_sorted)] for i in range(num)]

def pick_seeds_at_random(region_seeds: List[Dict[str, Any]], level_min: int = None, level_max: int = None) -> List[Dict[str, Any]]:
    """Pick a seed at random from region_seeds, optionally within level range."""
    filtered = []
    for s in region_seeds:
        min_lvl = int(s.get("min_spawn_level",1) or 1)
        if (level_min is not None and min_lvl < level_min) or (level_max is not None and min_lvl > level_max):
            continue
        filtered.append(s)
    if not filtered:
        return []
    rng = random.Random()
    return rng.sample(filtered, k=len(filtered))

def _select_seeds_by_rarity(region_seeds, level, pick_for_rarity,
                            superrare_count, rare_count, uncommon_count, common_count):
    """Run the rarity-cascade selection over `region_seeds` using `pick_for_rarity`.

    Leftover slots for a rarity (when that rarity is exhausted) cascade down to
    the next-lower rarity, mirroring the original inline logic. Returned as a
    flat list of picked seed dicts (may be shorter than the requested total if
    the pool can't satisfy every slot).
    """
    picked_seeds = []
    total_mob_count = superrare_count + rare_count + uncommon_count + common_count

    if superrare_count > 0:
        found = pick_for_rarity("superrare", superrare_count, region_seeds, level)
        picked_seeds.extend(found)
        superrare_count -= len(found)
        rare_count += superrare_count
    if rare_count > 0:
        found = pick_for_rarity("rare", rare_count, region_seeds, level)
        picked_seeds.extend(found)
        rare_count -= len(found)
        uncommon_count += rare_count
    if uncommon_count > 0:
        found = pick_for_rarity("uncommon", uncommon_count, region_seeds, level)
        picked_seeds.extend(found)
        uncommon_count -= len(found)
        common_count += uncommon_count
    if common_count > 0:
        found = pick_for_rarity("common", common_count, region_seeds, level)
        picked_seeds.extend(found)
        common_count -= len(found)
        uncommon_count += common_count
    if uncommon_count > 0 and len(picked_seeds) < total_mob_count:
        found = pick_for_rarity("uncommon", uncommon_count, region_seeds, level)
        picked_seeds.extend(found)
        uncommon_count -= len(found)
        rare_count += uncommon_count
    if rare_count > 0 and len(picked_seeds) < total_mob_count:
        found = pick_for_rarity("rare", rare_count, region_seeds, level)
        picked_seeds.extend(found)

    return picked_seeds

#########################PUBLIC METHODS #########################
def instantiate_random_hostiles(count: int, level: int, selected_region: str = None, superrare_count: int = 0, rare_count: int = 0, uncommon_count: int = 0, common_count: int = 0, exclude_ids: set = None) -> List[RandomHostile]:
    """Create a RandomHostile instance populated from a seed dict and a target level.

    This function uses estimate_stats_from_seed to derive numeric stats and then
    maps seed fields into the RandomHostile dataclass. It will instantiate
    PlayerAbility objects for any `player_abilities` referenced in the seed.

    When `exclude_ids` is provided (Monster Hunter special_effect), seeds whose
    id is already logged in the player's monster log are removed from the pool
    so encounters draw only from species the player has not yet recorded.
    """
    # local imports to avoid import cycles at module import time
    from game.objects.player_ability import _instantiate_from_seed as _inst_ability
    
    seeds = gather_all_seeds()
    # initial population
    
    entries = []
    # select  a region key from seeds at random if selected_region is None

    if selected_region is None:
        region_keys = list(set([rk for rk, s in seeds]))
        rng = random.Random()
        selected_region = rng.choice(region_keys) if region_keys else None
     
    # select count seeds at random from the selected region
    region_seeds = [s for rk, s in seeds if rk == selected_region] if selected_region else [s for rk, s in seeds]

    # Full (non-MH) region pool, kept so we can fall back to it when Monster
    # Hunter has nothing left to offer in this region.
    full_region_seeds = list(region_seeds)

    # Monster Hunter: drop already-logged hostiles so the player can hunt down
    # species they missed. Only enter MH mode while unlogged species remain in
    # THIS region.
    mh_mode = False
    if exclude_ids:
        remaining = [s for s in region_seeds if s.get("id") not in exclude_ids]
        if remaining:
            region_seeds = remaining
            mh_mode = True

    # sort region_seeds by combat score descending
    region_seeds.sort(key=lambda x: compute_combat_score(estimate_stats_from_seed(x, int(x.get("min_spawn_level", 1))), int(x.get("min_spawn_level", 1))), reverse=True)

    picked_seeds = []
    if mh_mode:
        # MH pass: highest unlogged seed per rarity, capped at party level.
        picked_seeds = _select_seeds_by_rarity(
            region_seeds, level, pick_highest_seeds_for_rarity,
            superrare_count, rare_count, uncommon_count, common_count,
        )

    # Fallback: if not in MH mode, or MH found nothing (every huntable species
    # in this region is already logged), run the normal band-based selection
    # over the FULL region pool so the player still gets level-appropriate
    # encounters instead of walking around with nothing to fight.
    if not picked_seeds:
        full_region_seeds.sort(key=lambda x: compute_combat_score(estimate_stats_from_seed(x, int(x.get("min_spawn_level", 1))), int(x.get("min_spawn_level", 1))), reverse=True)
        picked_seeds = _select_seeds_by_rarity(
            full_region_seeds, level, pick_seeds_for_rarity,
            superrare_count, rare_count, uncommon_count, common_count,
        )

    for seed in picked_seeds:
        lvl = int(seed.get("min_spawn_level",1) or 1)
        derived = estimate_stats_from_seed(seed, lvl)
        score = compute_combat_score(derived, lvl)
        entries.append({
        "region_key": selected_region,
        "id": seed.get("id"),
        "name": seed.get("name"),
        "min_spawn_level": lvl,
        "seed": seed,
        "derived": derived,
        "combat_score": float(round(score,3)),
        "assigned_rarity": seed.get("rarity", "common"),
        })

        
    hostiles: List[RandomHostile] = []
    for e in entries:
        reseed_existing_hostile(e)
        rh = _instantiate_random_hostile_from_seed(e, e['min_spawn_level'])
        hostiles.append(rh)

    return hostiles

#possibly used for monster log.... not used for combat
def generate_hostile_from_legacy_seed(seed, level, retain_abilities = False):
    lvl = int(seed.get("min_spawn_level",1) or 1)
    derived = estimate_stats_from_seed(seed, lvl)
    score = compute_combat_score(derived, lvl)
    entry = {
        #"region_key": selected_region,
        "id": seed.get("id"),
        "name": seed.get("name"),
        "min_spawn_level": lvl,
        "seed": seed,
        "derived": derived,
        "combat_score": float(round(score,3)),
        "assigned_rarity": seed.get("rarity", "common"),
        }

        
    reseed_existing_hostile(entry, retain_abilities = retain_abilities)
    rh = _instantiate_random_hostile_from_seed(entry, entry['min_spawn_level'])
    return rh



if __name__ == "__main__":
    reseed_and_save()
    print("Done")

