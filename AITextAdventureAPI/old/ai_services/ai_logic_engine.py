"""Central AI decision logic helpers.

This module contains higher-level decision functions that coordinate the
specialised ai_services helpers (pathing, treasure hunting, equipment) and
provides movement selection that avoids recent-state loops.
"""
from typing import Optional, Tuple, List, Dict, Any
import random

from game.constants import DIRECTIONAL_MAPPING

from ai_services.ai_city_and_region_helper import find_nearest_sublocation, get_tile, is_walkable, get_walkable_neighbors, find_sublocations_at, find_nearest_shop
from ai_services.ai_pathing_logic import find_path_to, direction_from_path, _resolve_area_for_pos, _make_node
from ai_services.ai_treasure_hunter_logic import (
	next_direction_to_loot,
	next_direction_to_nearest_shop,
	shop_is_armor,
	shop_is_items,
	find_nearest_loot_path,
)
from ai_services.ai_equipment_logic import _is_healing_item, get_current_armor_defense, get_current_armor_defense, select_purchases_for_armor
from ai_services.ai_combat_logic import find_healing_item_index

from services.armor_shop_service import get_stock as GetStockArmor
from services.weapon_shop_service import get_stock as GetStockWeapons
from services.utility_shop_service import get_stock as GetStockItems


# import helper services (lazy imports inside functions where appropriate to
# avoid circular import issues at module-import time in larger app)

AI_HEALTH_STOCK_LIMIT = 5

def choose_movement_avoiding_recent(player: Any, player_game: Any, allowed_moves: Dict[str, Any], recent_states: List[Tuple[int, int, bool, int]], allow_vertical: bool = False) -> Optional[str]:
	"""Choose a movement key from allowed_moves preferring moves that lead to a
	state not present in recent_states.

	If `allow_vertical` is False, movement keys that change floor/inside will be
	ignored (these are for entering/exiting or moving between floors and should
	only be used when explicitly looting inside a building).
	"""
	if not allowed_moves:
		return None

	# filter keys by vertical allowance
	keys = list(allowed_moves.keys())
	if not allow_vertical:
		# DIRECTIONAL_MAPPING entries are (dx,dy,dz) where dz !=0 indicates vertical move
		keys = [k for k in keys if (DIRECTIONAL_MAPPING.get(k, (0,0,0))[2] ==0)]
		if not keys:
			# if no horizontal moves available, fall back to original allowed moves
			keys = list(allowed_moves.keys())

	# Helper to compute destination state tuple for a movement key
	def dest_state_for_key(k: str):
		dx, dy, _ = DIRECTIONAL_MAPPING.get(k, (0,0,0))
		nx = int(player.x + dx)
		ny = int(player.y + dy)
		# conservative: assume inside/floor unchanged by simple cardinal move.
		return (nx, ny, bool(getattr(player, 'inside', False)), int(getattr(player, 'z',0)))

	# compute candidates not in recent states
	candidates = []
	for k in keys:
		st = dest_state_for_key(k)
		if st not in recent_states:
			candidates.append(k)

	if candidates:
		return random.choice(candidates)

	# all moves would repeat recent state; fallback to any allowed key (respecting vertical filter)
	return random.choice(keys)


def select_task(player: Any, player_game: Any) -> Dict[str, Any]:
	"""High-level task selector for the AI.

	Returns a dict describing the intended action and optional target: e.g.
	{'action': 'heal_self', 'description': 'Heal before further actions.'}
	{'action':'buy_armor', 'direction': 'd', 'target': (x,y)}

	The function uses equipment and treasure helpers where available.
	"""
	# lazy imports to avoid circular deps

	# default task: explore
	status: Dict[str, Any] = {'action': 'explore', 'description': 'Exploring the area.'}
	

	################ HEAL SELF FIRST
	# Heal if hurt below threshold and have healing items
	max_hp = player.max_hp
	cur_hp = player.current_hp
	if max_hp >0 and cur_hp / max_hp <0.5 and find_healing_item_index is not None:
		if find_healing_item_index(player) is not None:
			return {'action': 'heal_self', 'description': 'Heal before further actions.'}

	############ REVIEW SHOPPPING LIST ############
	

	################# CHECK TO RESTOCK ITEMS
	healing_count = sum(1 for it in player.inventory if _is_healing_item(it))
	need_healing_items = healing_count < AI_HEALTH_STOCK_LIMIT

	#### OPTIONALLY LATER CHECK IF STATUS AILMENT ITEMS SHOULD BE BOUGHT FROM "FEAR" BY AI GETTING HIT WITH IT. UNTIL THEN JUST BUY HEALING ITEMS ####
	needed_status_items = []

	healing_items_to_buy = None
	if need_healing_items or len(needed_status_items):
		healing_items_to_buy = []
		item_shop_pos, item_shop_region = find_nearest_shop(player.x, player.y, player_game, "shopitems")
		# get prices of healing items... if can afford set aaction to go to the item shop and continue
		item_stock = GetStockItems(player.level, item_shop_region, 14) if item_shop_region else []
		
		if need_healing_items:
			# find healing items in stock
			for item in item_stock:
				if _is_healing_item(item):
					healing_items_to_buy.append(item)
		# find status ailment items in stock
		for item in item_stock:
			if item.id in needed_status_items:
				healing_items_to_buy.append(item)

	# if there are any healing items AI cannot afford search an area [-2.-2]-[2,2] around the AI for loot with healing items and set the action to loot that position
	if healing_items_to_buy:
		# if there are any healing items AI can afford go buy them
		for it in healing_items_to_buy:
			if player.money >= it.price:
				desc = f"Moving to item shop to buy healing/status items."
				status = {'action': 'buy_items', 'description': desc, 'direction': next_direction_to_nearest_shop(player, player_game, "shopitems"), 'target': item_shop_pos}
				return status

		dir_to_loot = next_direction_to_loot(player, player_game, lambda item: item in healing_items_to_buy)
		if dir_to_loot:
			desc = f"Moving to loot healing/status items."
			status = {'action': 'loot', 'description': desc, 'direction': dir_to_loot}
			return status


	################# CHECK TO BUY BETTER ARMOR
	armor_shop_pos = None
	upgrade_for_armor_list = []
	armor_slot = None
	# check common slots
	armor_shop_pos, armor_shop_region = find_nearest_shop(player.x, player.y, player_game, "shoparmor")
	if not armor_shop_pos or not armor_shop_region:
		for slot in ('HEAD','BODY','ARMS','LEGS'):
			armor_stock  = GetStockArmor(player.level, armor_shop_region, 14) if armor_shop_region else []

			if len(armor_stock) > 0:
				# create list of all armor pieces at nearest armor_shop which are stronger than current armor in slot
				best_upgrade = None
				current_defense = get_current_armor_defense(player, slot)
				for armor in armor_stock:
					# normalize armor.slot to an uppercase slot name (e.g. 'HEAD','BODY')
					armor_slot_name = armor.slot.name.upper()
					
					if armor_slot_name == slot and getattr(armor, 'defense',0) > current_defense:
						if best_upgrade is None or getattr(armor, 'defense',0) > getattr(best_upgrade, 'defense',0):
							best_upgrade = armor

				# this will go into the list of purchaseable armor upgrades
				if best_upgrade is not None:
					upgrade_for_armor_list.append(best_upgrade)
			continue


	############## CHECK TO BUY BETTER WEAPONS
	weapon_shop_pos = None
	upgrade_for_weapon_list = []

	# make note of best weapon at nearest weapon_shop which is stronger than current weapon in slot
	# this will go into the list of purchaseable weapon upgrades		
	upgrade_for_weapon_shop_pos, upgrade_for_weapon_shop_region = find_nearest_shop(player.x, player.y, player_game, "shopweapons")
	if upgrade_for_weapon_shop_pos is not None:
		upgrade_for_weapon_stock = GetStockWeapons(player.level, upgrade_for_weapon_shop_region, 14) if upgrade_for_weapon_shop_region else []

		if upgrade_for_weapon_stock:
			#print(f"AI Logic Engine: weapon shop stock={upgrade_for_weapon_stock}")
			best_weapon_upgrade = None
			current_weapon_power = player.equipped_weapon.damage if player.equipped_weapon else 0
			current_weapon_crit = player.equipped_weapon.critical_chance if player.equipped_weapon else 0
			for weapon in upgrade_for_weapon_stock:
				if weapon.damage > current_weapon_power or (weapon.damage == current_weapon_power and weapon.critical_chance > current_weapon_crit):
					if best_weapon_upgrade is None or weapon.damage > best_weapon_upgrade.damage or (weapon.damage == best_weapon_upgrade.damage and weapon.critical_chance > best_weapon_upgrade.critical_chance):
						best_weapon_upgrade = weapon

			#print(f"AI Logic Engine: best_weapon_upgrade={best_weapon_upgrade}, current_weapon_power={current_weapon_power}, current_weapon_crit={current_weapon_crit}")

			if best_weapon_upgrade is not None:
				upgrade_for_weapon_list.append(best_weapon_upgrade)

		#print(f"AI Logic Engine: upgrade_for_purchase_nearby={upgrade_for_weapon_list}, armor_slot={armor_slot}")

	# create a sublist of armor and weapons for ordering.. ordering armor before weapons
	shopping_list_armor_and_weapons: List[Any] = []
	shopping_list_healing_items: List[Any] = []
	if upgrade_for_armor_list:
		shopping_list_armor_and_weapons.extend(upgrade_for_armor_list)
	if upgrade_for_weapon_list:
		shopping_list_armor_and_weapons.extend(upgrade_for_weapon_list)

	# order that sublist by lowest defense/damage first
	shopping_list_armor_and_weapons.sort(key=lambda it: (it.defense if hasattr(it, 'defense') else (it.damage if hasattr(it, 'damage') else 0)))

	# instead of running straight to the shop with gear we can look for items in our shopping list that we can loot in an area around us
	# we will use a 6 square radius around AI searching only tiles within the active_region
	for it in shopping_list_armor_and_weapons:
		dir_to_loot = next_direction_to_loot(player, player_game, lambda item: item == it, max_distance=4)
		if dir_to_loot:
			desc = f"Moving to loot {it.name}."
			status = {'action': 'loot', 'description': desc, 'direction': dir_to_loot}
			return status

	# If there are any armor/weapon upgrades AI can afford go buy them
	for it in shopping_list_armor_and_weapons:
		if pg.money >= it.value:
			# determine shop type
			shop_type = "shoparmor" if hasattr(it, 'defense') else "shopweapons"
			desc = f"Moving to {shop_type} to buy {it.name}."
			status = {'action': f'buy_{"armor" if shop_type=="shoparmor" else "weapon"}', 'description': desc, 'direction': next_direction_to_nearest_shop(player, player_game, shop_type)}
			return status

	# check if the inventory is full and handle selling items
	if len(pg.inventory) == pg.max_inventory_count:
		# set task to go sell at nearest of any type shop
		desc = f"Inventory full; moving to nearest shop to sell items."
		status = {'action': 'sell_items', 'description': desc, 'direction': next_direction_to_nearest_shop(player, player_game, None)}
		return status

	# if we are through with our shopping list we can loot the nearest sublocation in the region
	dir_to_loot = next_direction_to_loot(player, player_game, lambda item: True)
	if dir_to_loot:
		desc = f"Moving to loot nearest sublocation."
		status = {'action': 'loot', 'description': desc, 'direction': dir_to_loot}
		return status

	# if ai still has nothing to do leave the active region. (the process will continue in the next region)(set direction to the closes tile position not in active region tiles)

	_, active_area = player_game.get_region_and_active_area_for_position((player.x, player.y))
	if active_area:
		#def find_path_to(player, target_xy: Tuple[int, int], player_game, max_search: int =2000) -> Optional[List[str]]:
		# for all tiles in active_area find the nearest tile not in active_area
		closest_exit_tile = None
		closest_exit_dist = None
		for (tx, ty) in active_area.tiles.keys():
			# check neighbors for walkable tile not in active area
			neighbors = get_walkable_neighbors(active_area, tx, ty, player_game)
			for (nx, ny) in neighbors:
				if (nx, ny) not in active_area.tiles:
					# compute distance
					dist = abs(player.x - nx) + abs(player.y - ny)
					if closest_exit_tile is None or dist < closest_exit_dist:
						closest_exit_tile = (nx, ny)
						closest_exit_dist = dist
		if closest_exit_tile:
			dir_to_exit = direction_from_path(find_path_to(player, closest_exit_tile, player_game))
			if dir_to_exit:
				desc = f"Leaving active region area."
				status = {'action': 'leave_region', 'description': desc, 'direction': dir_to_exit}
				return status

		

		

