"""AI-controlled demo that uses AI service helpers for navigation, combat and UI.

This replaces the older monolithic demo with a cleaner composition of ai_services helpers:
- ai_city_and_region_helper for tile/subloc queries and pathfinding
- ai_pathing_logic for game-movement-aware pathfinding
- ai_treasure_hunter_logic for loot/shop finding and pickup behavior
- ai_combat_logic for combat simulation
- ai_equipment_logic for shop/equipment decisions
- ai_ui_helper for viewport rendering and boxed output
"""
from typing import Optional
from collections import deque
import os
import time
import random

from game import constants as const
from game.constants import ROAD, BUILDING, ALLEY, DIRECTIONAL_MAPPING
from game.objects.player_game import PlayerGame
from game.objects.player import Player

# services
from services.player_movement_service import (
    get_allowed_moves,
    handle_movement_key,
    get_floor_options,
    handle_floor_action,
    check_for_random_encounter,
)

# ai helpers
from ai_services.ai_city_and_region_helper import (
    get_tile,
    find_sublocations_at,
    find_nearest_sublocation,
    shortest_path,
)
from ai_services.ai_pathing_logic import (
    find_path_to,
    direction_from_path,
    find_nearest_target_by_predicate,
)
from ai_services.ai_treasure_hunter_logic import (
    next_direction_to_loot,
    next_direction_to_nearest_shop,
    shop_is_armor,
    shop_is_items,
    pick_up_sublocations_at_player,
)
from ai_services.ai_combat_logic import run_combat, player_ai_take_turn, hostile_take_turn, is_healing_item
from ai_services.ai_equipment_logic import (
    get_current_armor_defense,
    select_purchases_for_armor,
    equip_item_if_better,
)
from ai_services.ai_ui_helper import (
    clear_screen,
    display_viewport,
    render_compat_combat_box,
    type_victory_message,
    ai_fight_screen,
)
from ai_services.ai_logic_engine import select_task, choose_movement_avoiding_recent
from ai_services.ai_leveling_logic import ai_level_up_player
from ai_services.ai_player_tasks import handle_action

# shop APIs
from services.armor_shop_service import get_stock as GetStockArmor, buy as BuyArmor
from services.utility_shop_service import get_stock as GetStockItems, buy as BuyItems


def setup_player_stats(p: Player) -> None:
    """Auto distribute initial stat and power points for the AI player."""
    pts = getattr(p, 'initial_stat_distribution_amount',10)
    con = max(0, int(pts *0.5))
    rem = pts - con
    strn = max(0, int(rem *0.66))
    rem -= strn
    dex = rem
    intel =0
    power_pts = getattr(p, 'power_points_per_level',10)
    hp_alloc = power_pts
    ap_alloc =0
    p.level_up(strn, dex, con, intel, hp_alloc, ap_alloc, None)


def _format_status_lines(entity) -> list:
    lines = []
    name = getattr(entity, 'name', 'Unknown')
    lines.append(f"{name}")
    # HP/AP lines
    hp = getattr(entity, 'current_hp', None)
    max_hp = getattr(entity, 'max_hp', None)
    if hp is not None and max_hp is not None:
        lines.append(f"HP: {hp}/{max_hp}")
    else:
        lines.append("HP: ?")
    ap = getattr(entity, 'current_ap', None)
    max_ap = getattr(entity, 'max_ap', None)
    if ap is not None and max_ap is not None:
        lines.append(f"AP: {ap}/{max_ap}")
    else:
        lines.append("AP: ?")
    # statuses
    sts = []
    if getattr(entity, 'statuses', None):
        sts = [f"{s.get('name') or s.get('id')}({s.get('turns_remaining', s.get('duration',0))})" for s in entity.statuses]
    lines.append("")
    lines.append('Statuses: ' + (', '.join(sts) if sts else 'None'))
    return lines


def _type_message(msg: str, delay: float =0.02) -> None:
    for ch in msg:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()


def run_ai_demo():
    player = Player('AI_Bot',0,0,0, False)
    setup_player_stats(player)

    # track recent positions to avoid repeating movement loops
    recent_positions = deque(maxlen=12)
    recent_positions.append((player.x, player.y))

    ai_stats = {
        'fights':0,
        'tasks':0,
        'loots':0,
        'purchases':0,
        'tasks_abandoned':0,
        'hostiles_defeated':0,
        'last_move': None,
    }

    # persistent AI state (shopping list, pathing state)
    def _level_scaled(base: int, lvl: int) -> int:
        return max(base, int(base * (1.5 ** max(0, lvl -1))))
        
    # shopping_list: ordered list of dicts {name: str, target: int}
    ai_state = {
        'shopping_list': [],
        'seeking_loot': False,
        'armor_slots': set(),
    }

    pg = PlayerGame()
    pg.add_character(player)
    print('Building initial region...')
    pg.create_region_at((0,0), player)

    # initial restock: ensure AI starts with a healthy supply of healing/utility items
    parent_region, active_city = pg.get_region_and_active_area_for_position()
    active_area = active_city if active_city else parent_region
    stock = GetStockItems(player.level, active_area) or []
    def _target_count_for_level(base: int, lvl: int) -> int:
        return max(base, int(base * (1.5 ** max(0, lvl -1))))
    target_base =10
    target = _target_count_for_level(target_base, player.level)
    seen = set()
    for it in stock:
        if is_healing_item(it):
            name = it.name
            if not name or name in seen:
                continue
            seen.add(name)
            # count existing
            have = sum(1 for inv in pg.inventory)
            while have < target and len(pg.inventory) < pg.max_inventory_count:
                pg.pick_up_item(it)

            # add to shopping list
            ai_state['shopping_list'].append({'name': name, 'target': target})

    view_w =41
    view_h =11
    move_delay =0.5

    try:
        while True:
            clear_screen()
            pg.ensure_tiles_around(check_rad=4, max_attempts=1)
            parent_region, active_city = pg.get_region_and_active_area_for_position()
            active_area = active_city if active_city else parent_region

            # decide high-level task using logic engine (render after selecting task so UI reflects intent)
            status = select_task(player, pg)
            print(f"AI Task: {status.get('description','Unknown task')}")
            # Expose structured status to UI
            ai_status = status
            display_viewport(pg, parent_region, pg, view_w, view_h, ai_status=ai_status, ai_stats=ai_stats)
            print(f"Player at {pg.x},{pg.y} inside={pg.inside} floor={player.z + 1}")
            print(active_area.describe_location(pg.x, pg.y, pg.inside, pg.z + 1))

            # check for encounter
            hostile = check_for_random_encounter(active_area, player, pg)
            if hostile is not None:
                ai_stats['fights'] = ai_stats.get('fights',0) +1
                # use combat simulator
                res = run_combat(player, hostile)
                for line in res.get('log', []):
                    print(line)
                if res.get('winner') == 'hostile':
                    print('AI died in combat.')
                    return
                else:
                    ai_stats['hostiles_defeated'] = ai_stats.get('hostiles_defeated',0) +1
                # award loot using game's API
                loot, gained_level = hostile.award_player(player, pg)
                if loot:
                    for it in loot:
                        print(f"Hostile dropped: {getattr(it, 'name', str(it))}")
                        ai_stats['loots'] = ai_stats.get('loots',0) +1
                if gained_level:
                    # perform automated AI level-up allocation
                    res = ai_level_up_player(player, build='brawler')
                    # res includes allocations and selected ability; the helper types messages
                    # echo concise summary
                    type_victory_message(f"AI reached level {player.level}.", delay=0.1)
                time.sleep(1.0)
                continue

            # update shopping list targets on level up
            new_target = _level_scaled(10, player.level)
            for entry in ai_state.get('shopping_list', []):
                entry['target'] = new_target

            # decide needs (armor, items)
            need_armor = (
                get_current_armor_defense(player, 'HEAD') <=0
                or get_current_armor_defense(player, 'BODY') <=0
                or get_current_armor_defense(player, 'ARMS') <=0
                or get_current_armor_defense(player, 'LEGS') <=0
            )

            moved_flag = False

            allowed_moves = get_allowed_moves(active_area, player, pg) or {}

            # Helper to attempt a movement key
            def _try_move(move_key):
                if not move_key:
                    return False
                if move_key in (allowed_moves or {}):
                    moved = handle_movement_key(move_key, active_area, allowed_moves,4, pg)
                    ai_stats['last_move'] = move_key
                    return moved
                return False

            # Action handling via task handler
            action = status.get('action')
            moved_flag, status = handle_action(action, status, player, pg, active_area, allowed_moves, _try_move, ai_stats, ai_state, list(recent_positions))

            # After action handling, always check current tile for sublocations/loot
            got_here_items = pick_up_sublocations_at_player(active_area, player)
            if got_here_items:
                for desc in got_here_items:
                    # helper already typed messages; echo and update counters
                    type_victory_message(f"AI: {desc}", delay=0.02)
                    ai_stats['loots'] = ai_stats.get('loots',0) +1
                    ai_stats['tasks'] = ai_stats.get('tasks',0) +1

            # record full state after actions to avoid loops
            recent_positions.append((player.x, player.y, player.inside, player.z))

            time.sleep(move_delay)
    except KeyboardInterrupt:
        print('Demo interrupted.')


if __name__ == '__main__':
    run_ai_demo()

