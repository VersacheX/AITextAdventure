from typing import List, Dict, Any
import random

from game.objects.armor import Armor, ArmorType, _instantiate_armor
from game.objects.item import Item
from game import constants as const

SELL_RATIO =0.5

def get_stock(player_level: int, current_region, count: int =8) -> List[Armor]:
    candidates = []
    armor_seeds = const.ARMOR_SEEDS

    for slot, group in armor_seeds.items():
        for s in group:
            if s.get('min_spawn_level',1) <= player_level:
                candidates.append((slot, s))
    if not candidates:
        return []
    # sort/sample by the seed's value (second element of the tuple)
    # switch to max to ensure all
    chosen = sorted(candidates, key=lambda x: x[1].get('value',0) * -1)
    return [_instantiate_armor(seed, slot) for slot, seed in chosen]


def buy(player_game, item: Armor) -> Dict[str, Any]:
    price = getattr(item, 'value',0)
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
