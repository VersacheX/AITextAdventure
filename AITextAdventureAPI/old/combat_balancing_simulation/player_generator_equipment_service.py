import random
from typing import Optional, List, Set

from game.objects.player import Player
import game.constants_items as const_items
import game.constants_other as const_other
from game.objects.weapon import _instantiate_weapon
from game.objects.armor import _instantiate_armor
from game.objects.utility_item import _instantiate_utility
from game.objects.player_ability import PlayerAbility
from game.objects.player_ability import _instantiate_from_seed as _instantiate_abiltiy_from_seed

from game.region_seeds.player_abilities.ability_requirements import (
    ABILITY_TYPE_REQUIREMENTS,
)


def _resolve_stat_weights(ability_type_focus: Optional[str]) -> dict:
    """Return normalized stat weights for the given ability type focus.

    If `required_stats_per_ability_level` contains multiple dicts, aggregate
    them so all relevant stats contribute to the weight (e.g. 'tech' will
    include both intelligence and dexterity). Returns a dict with keys:
    'strength','dexterity','constitution','intelligence' whose values sum to1.0.
    """
    stats = ["strength", "dexterity", "constitution", "intelligence"]
    weights = {s:0.0 for s in stats}

    if ability_type_focus:
        focus_lower = str(ability_type_focus).lower()
        for entry in (ABILITY_TYPE_REQUIREMENTS or []):
            if str(entry.get("ability_type", "")).lower() == focus_lower:
                reqs = entry.get("required_stats_per_ability_level") or []
                if reqs:
                    total =0.0
                    # aggregate all requirement dicts instead of only taking the first
                    for rdict in reqs:
                        for s in stats:
                            
                            v = float(rdict.get(s,0) or 0.0)
                            
                            weights[s] += v
                            total += v
                    if total >0.0:
                        for s in stats:
                            weights[s] = weights[s] / total
                    return weights
                break

    # fallback bias toward strength
    weights = {"strength":4.0, "dexterity":1.0, "constitution":1.0, "intelligence":1.0}
    total = sum(weights.values())
    if total <=0.0:
        even =1.0 / len(stats)
        return {s: even for s in stats}
    for s in stats:
        weights[s] = weights[s] / total
    return weights


###################### Ability selection helpers

def score_key(pb: PlayerAbility, ability_type_focus: Optional[str], player_level: int):
    """Module-level scoring key for ability candidates.

    Separated from `pick_abilities_for_player` to avoid nested function
    definitions. Returns a tuple used for sorting: (preference rank,
    level difference, negative base power) so `sorted(..., key=score_key)`
    produces the desired ordering.
    """
    atype = getattr(pb, 'ability_type', None)
    alv = getattr(pb, 'level',0)
    bp = getattr(pb, 'base_power',0)

    # Preference rank: keep as0 since strict filtering is performed in
    # `pick_abilities_for_player` when ability_type_focus is provided.
    pref_rank =0

    
    alv_int = int(alv)
    
    bp_f = float(bp)

    # Weight base_power more strongly so higher-base-power abilities are
    # preferred when other factors tie. Scale factor can be tuned.
    bp_score = bp_f *100.0

    return (pref_rank, abs(alv_int - int(player_level)), -bp_score)


def pick_abilities_for_player(
    player: Player,
    num: int,
    allowed_elements: Optional[Set[str]],
    ability_type_focus: Optional[str],
    rng: random.Random,
) -> List[PlayerAbility]:
    """Select up to `num` ability ids for `player` based on stats and focus."""
    all_abils = getattr(const_other, "PLAYER_ABILITY_SEEDS", []) or []
    candidates = []

    for a in all_abils:
        if not a or not isinstance(a, dict):
            continue
        # strict filtering: if a focus is provided, skip abilities that do not match
        if ability_type_focus:
            
            if str(a.get('ability_type', '')).lower() != str(ability_type_focus).lower():
                continue
        elems = [str(x).lower() for x in (a.get("elements") or [])]
        if allowed_elements and not any(e in allowed_elements for e in elems):
            continue
        if not meets_ability_requirements(
            a,
            {
                "strength": player.strength,
                "dexterity": player.dexterity,
                "constitution": player.constitution,
                "intelligence": player.intelligence,
            },
        ):
            continue
        player_abil = _instantiate_abiltiy_from_seed(seed=a)
        candidates.append(player_abil)

    # Sort candidates using module-level score_key
    sorted_cands = sorted(candidates, key=lambda tup: score_key(tup, ability_type_focus, player.level))
    selected: List[PlayerAbility] = []  

    #selected: List[str] = []
    known_ids = [x.id for x in player.abilities]

    for c in sorted_cands:
        if len(selected) >= num:
            break
        if c.id not in known_ids:
            selected.append(c)

    return selected ###########RETURN PlayerAbility object

# def select_abilities(
#     player: Player,
#     num: int,
#     allowed_elements: Optional[Set[str]],
#     ability_type_focus: Optional[str],
#     rng: random.Random,
# ) -> List[str]:
#     """Wrapper around pick_abilities_for_player to choose abilities for player."""
#     return pick_abilities_for_player(player, num, allowed_elements, ability_type_focus, rng)

def meets_ability_requirements(ability_seed: dict, player_stats: dict) -> bool:
    """Return True if `player_stats` meet `ability_seed` requirements.

    Requirements are defined in ABILITY_TYPE_REQUIREMENTS and scaled by
    ability level (level^2 multiplier).
    """
    if not ability_seed or not isinstance(ability_seed, dict):
        return False

    atype = ability_seed.get("ability_type") or ""
    if not atype:
        return True
    atype = str(atype).lower()

	# build requirement lookup
    req_map = {
        e.get("ability_type"): e.get("required_stats_per_ability_level", [])
        for e in (ABILITY_TYPE_REQUIREMENTS or [])
    }

    reqs = req_map.get(atype)
    if not reqs:
        return True

    alv = int(ability_seed.get("level",1) or 1)
    for rdict in reqs:
        ok = True
        for stat_name, stat_val in (rdict or {}).items():
            required = int(stat_val) + int((int(stat_val) * ((alv - 1)* 1.5)) **1.25)
            if int(player_stats.get(stat_name,0)) < required:
                ok = False
                break
        if ok:
            return True
    return False



################ Equipment selection and equipping helpers
def select_weapon(player: Player, ability_type_focus: Optional[str] = None) -> Optional[dict]:
    """Return best weapon seed for player according to weights."""
    lvl = player.level
    weights = _resolve_stat_weights(ability_type_focus)
    best = None
    best_score = float("-inf")

    # increased stat multiplier; removed durability factor
    STAT_MULTIPLIER =4

    for w in (getattr(const_items, "WEAPON_SEEDS", []) or []):
        
        if int(w.get("min_spawn_level",1) or 1) > lvl:
            continue
        dmg = float(w.get("damage",0) or 0)
        crit = float(w.get("critical_chance",0) or 0)
        base_score = dmg * (1.0 + crit /100.0)
        s_val = float(w.get("strength",0) or 0)
        dx_val = float(w.get("dexterity",0) or 0)
        it_val = float(w.get("intelligence",0) or 0)
        stat_contrib = (
	        weights.get("strength",0.0) * s_val
	        + weights.get("dexterity",0.0) * dx_val
	        + weights.get("intelligence",0.0) * it_val
        )
        score = base_score + (STAT_MULTIPLIER * stat_contrib)
        if score > best_score:
            best_score = score
            best = w
    #input(f"best weapon selected: {best.get('id') if best else 'None'} with score {best_score}. Press Enter to continue...")
    return best


def select_armor(player: Player, ability_type_focus: Optional[str] = None) -> dict:
    """Return mapping slot -> best armor seed for player."""
    lvl = player.level
    weights = _resolve_stat_weights(ability_type_focus)
    chosen = {}

    # increased armor stat multiplier; removed durability factor
    ARMOR_STAT_MULTIPLIER =1.0

    for slot, items in (getattr(const_items, "ARMOR_SEEDS", {}) or {}).items():
        best_a = None
        best_score = float("-inf")
        for a in items:
            if int(a.get("min_spawn_level",1) or 1) > lvl:
                continue
            d = float(a.get("defense",0) or 0)
            s = float(a.get("strength",0) or 0)
            dx = float(a.get("dexterity",0) or 0)
            it = float(a.get("intelligence",0) or 0)
            con = float(a.get("constitution",0) or 0)
            dex_neg_penalty = abs(min(0.0, dx))
            stat_contrib = (
	            weights.get("strength",0.0) * s
	            + weights.get("dexterity",0.0) * dx
	            + weights.get("intelligence",0.0) * it
	            + weights.get("constitution",0.0) * con
            )
            score = d + (ARMOR_STAT_MULTIPLIER * stat_contrib) - (0.6 * dex_neg_penalty)
            if score > best_score:
                best_score = score
                best_a = a
        if best_a:
            chosen[slot] = best_a
    return chosen


def select_utility_items(player: Player, max_heals: int = 5, max_ap: int = 2) -> List[dict]:
    """Return utility item seeds appropriate to player level (not instantiated)."""
    util_seeds = getattr(const_items, "UTILITY_ITEM_SEEDS", []) or []

    def best_candidates(prefix: str, count: int) -> List[dict]:
        cands = []
        for u in util_seeds:
            effect = u.get("effect") or ""
            min_lvl = int(u.get("min_spawn_level",1) or 1)
            if effect.startswith(prefix) and min_lvl <= player.level:
                cands.append(u)
            cands_sorted = sorted(cands, key=lambda x: int(x.get("min_spawn_level",1) or 1), reverse=True)
        # return the top candidate `count` times
        return cands_sorted[:1] * count if cands_sorted else []

    picks: List[dict] = []
    picks.extend(best_candidates("heal", max_heals))
    picks.extend(best_candidates("restore_ap", max_ap))

    pan = next((u for u in util_seeds if u.get("id") == "panacea" and int(u.get("min_spawn_level", 1) or 1) <= player.level), None)
    if pan:
        picks.extend([pan, pan])
    return picks


def equip_player_gear(player: Player, player_game, ability_type_focus: Optional[str] = None) -> None:
    """Instantiate and equip best gear for `player` using selection helpers."""
    if player is None:
        return

    # Weapon    
    wseed = select_weapon(player, ability_type_focus)
    if wseed and _instantiate_weapon:
        wobj = _instantiate_weapon(wseed)
        player_game.pick_up_item(wobj)
        player.equip_weapon(player_game, wobj)
    

    # Armor pieces
    aseeds = select_armor(player, ability_type_focus) or {}
    for slot, seed in aseeds.items():
        if not seed or not _instantiate_armor:
            continue
        aobj = _instantiate_armor(seed, slot)
        player_game.pick_up_item(aobj)
        player.equip_armor(player_game, aobj)
    
    # Utility items
    
    useeds = select_utility_items(player)
    for us in (useeds or []):
        uobj = _instantiate_utility(us)
        player_game.pick_up_item(uobj)
    
