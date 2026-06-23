from typing import Any, Dict
from game.objects.player import Player
from ai_services.ai_combat_logic import find_healing_item_index
from ai_services.ai_equipment_logic import _is_healing_item
from ai_services.ai_city_and_region_helper import find_nearest_shop
from services.utility_shop_service import get_stock as GetStockItems
from ai_services.ai_treasure_hunter_logic import next_direction_to_loot, next_direction_to_nearest_shop

def select_task(player: Player, player_game: Any, ai_setting: Any) -> Dict[str, Any]:
	status: Dict[str, Any] = {'action': 'explore', 'description': 'Exploring the area.'}


	############### HEAL SELF FIRST
	if player.current_hp < player.max_hp * ai_setting.hp_threshold_percent:
		if find_healing_item_index(player) is not None:
			return{ 'action': 'heal_self', 'description': 'Heal before further actions.'}
	
	################ CHECK TO RESTOCK ITEMS

	healing_count = sum(1 for it in player_game.inventory if _is_healing_item(it))
	need_healing_items = ai_setting.hp_restock_level - healing_count - ai_setting.health_restock_limit

	healing_items_to_buy = []
	if need_healing_items > 0:		
		item_shop_pos, item_shop_region = find_nearest_shop(player.x, player.y, player_game, "shopitems")
		item_stock = GetStockItems(player.level, item_shop_region, 14) if item_shop_region else []

		for item in item_stock:
			if _is_healing_item(item):
				healing_items_to_buy.append(item)

	# if there are any healing items AI cannot afford search an area loot with healing items and set the action to loot that position
	if len(healing_items_to_buy) > 0:
		# if there are any healing items AI can afford go buy them
		for it in healing_items_to_buy:
			if player_game.money >= it.price:
				desc = f"Moving to item shop to buy healing/status items."
				status = {'action': 'buy_items', 'description': desc, 'direction': next_direction_to_nearest_shop(player, player_game, "shopitems"), 'target': item_shop_pos}
				return status

		dir_to_loot = next_direction_to_loot(player, player_game, lambda item: item in healing_items_to_buy)
		if dir_to_loot:
			desc = f"Moving to loot healing/status items."
			status = {'action': 'loot', 'description': desc, 'direction': dir_to_loot}
			return status


	################ CHECK TO BUY BETTER ARMOR
	armor_shop_pos = None
	upgrade_for_armor_list = []
	armor_slot = None
	# check common slots
	armor_shop_pos, armor_shop_region = find_nearest_shop(player.x, player.y, player_game, "shoparmor")
	if armor_shop_pos is not None:
		for slot in ('HEAD','BODY','ARMS','LEGS'):		
			armor_stock  = GetStockArmor(player.level, armor_shop_region, 14) if armor_shop_region else []

			if len(armor_stock) > 0:
				# create list of all armor pieces at nearest armor_shop which are stronger than current armor in slot
				best_upgrade = None
				current_defense = get_current_armor_defense(player, slot)
				for armor in armor_stock:
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
			best_weapon_upgrade = None
			current_weapon_power = player.equipped_weapon.damage if player.equipped_weapon else 0
			current_weapon_crit = player.equipped_weapon.critical_chance if player.equipped_weapon else 0
			for weapon in upgrade_for_weapon_stock:
				if weapon.damage > current_weapon_power or (weapon.damage == current_weapon_power and weapon.critical_chance > current_weapon_crit):
					if best_weapon_upgrade is None or weapon.damage > best_weapon_upgrade.damage or (weapon.damage == best_weapon_upgrade.damage and weapon.critical_chance > best_weapon_upgrade.critical_chance):
						best_weapon_upgrade = weapon

			if best_weapon_upgrade is not None:
				upgrade_for_weapon_list.append(best_weapon_upgrade)

	# create a sublist of armor and weapons for ordering.. ordering armor before weapons
	shopping_list_armor_and_weapons: List[Any] = []
	shopping_list_healing_items: List[Any] = []
	if upgrade_for_armor_list:
		shopping_list_armor_and_weapons.extend(upgrade_for_armor_list)
	if upgrade_for_weapon_list:
		shopping_list_armor_and_weapons.extend(upgrade_for_weapon_list)

	# order that sublist by lowest defense/damage first
	shopping_list_armor_and_weapons.sort(key=lambda it: (it.defense if hasattr(it, 'defense') else (it.damage if hasattr(it, 'damage') else 0)))



	####################### SEE IF THERE IS A LOOT SPORT FOR AN EQUIPMENT ITEM NEARBY FIRST
	for it in shopping_list_armor_and_weapons:
		dir_to_loot = next_direction_to_loot(player, player_game, lambda item: item == it, max_distance=4)
		if dir_to_loot:
			desc = f"Moving to loot {it.name}."
			status = {'action': 'loot', 'description': desc, 'direction': dir_to_loot}
			return status
	
	############################### IF INVENTORY FULL SELL ITEMS FIRST
	if len(player_game.inventory) == player_game.max_inventory_count:
		# set task to go sell at nearest of any type shop
		desc = f"Inventory full; moving to nearest shop to sell items."
		status = {'action': 'sell_items', 'description': desc, 'direction': next_direction_to_nearest_shop(player, player_game, None)}
		return status

	############################### IF THE PLAYER HAS ENOUGH MOENY TO BUY AN ITEM ON THE SHOPPING LIST, GO BUY IT
	for it in shopping_list_armor_and_weapons:
		if player_game.money >= it.value:
			# determine shop type
			shop_type = "shoparmor" if hasattr(it, 'defense') else "shopweapons"
			desc = f"Moving to {shop_type} to buy {it.name}."
			status = {'action': f'buy_{"armor" if shop_type=="shoparmor" else "weapon"}', 'description': desc, 'direction': next_direction_to_nearest_shop(player, player_game, shop_type)}
			return status

	##################### SHOPPING DONE, GO HAVE FUN LOOTING NEARBY SUBLOCATIONS
	dir_to_loot = next_direction_to_loot(player, player_game, lambda item: True)
	if dir_to_loot:
		desc = f"Moving to loot nearest sublocation."
		status = {'action': 'loot', 'description': desc, 'direction': dir_to_loot}
		return status

	
	##################### NO OBVIOUS TASKS, CHECK TO LEAVE ACTIVE REGION AND EXPLORE NEW WORLDS
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