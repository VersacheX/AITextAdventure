from typing import List, Dict, Any
import random

from game.objects.weapon import Weapon, _instantiate_weapon
from game.objects.item import Item
from game import constants as const

SELL_RATIO =0.5




def get_stock(player_level: int, current_region, count: int =8) -> List[Weapon]:
    """Return a list of weapons appropriate for player's level."""
    weapon_seeds = const.WEAPON_SEEDS

    candidates = [s for s in weapon_seeds if s.get('min_spawn_level',1) <= player_level]
    if not candidates:
        return []
    chosen = sorted(candidates, key=lambda x: x.get('value',0) * -1)
    return [_instantiate_weapon(s) for s in chosen]


def buy(player_game, item: Weapon) -> Dict[str, Any]:
    """Attempt to buy the given Item for the player. Returns result dict."""
    price = item.value
    if player_game.money < price:
        return {'success': False, 'error': 'insufficient_funds'}
    
    if not player_game.pick_up_item(item):
        return {'success': False, 'error': 'inventory_full'}
    player_game.money -= price
    return {'success': True, 'item': item}


def sell(player_game, item: Item) -> Dict[str, Any]:
    """Sell an item from player's inventory. Returns dict."""
    if not isinstance(item, Item):
        return {'success': False, 'error': 'not_sellable'}
    value = item.value
    sell_price = int(value * SELL_RATIO)
    player_game.money += sell_price
    player_game.remove_single_item_unit(item)
    return {'success': True, 'price': sell_price, 'item': item}
