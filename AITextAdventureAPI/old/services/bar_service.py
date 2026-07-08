from tkinter import CURRENT
from typing import List, Dict, Any
from game import constants as const

# Simple in-bar drinks menu. Effects are immediate and don't create inventory items.
# Updated: list ordered from low-tier to high-tier (Ale -> Elixir). All entries are
# alcoholic beverages except Elixir which remains a special restorative.
# Prices have been doubled and an incremental "tax" applied per tier (5% per tier)
# so each subsequent drink costs slightly more than the previous.


# DRINK_MENU = [
#  {"id": "ale", "name": "Ale", "value":10, "hp_fraction":0.10, "ap_fraction":0.0, "min_level":1},
#  {"id": "stout", "name": "Stout", "value":25, "hp_fraction":0.20, "ap_fraction":0.0, "min_level":2},
#  {"id": "cocktail", "name": "Cocktail", "value":50, "hp_fraction":0.30, "ap_fraction":0.0, "min_level":3},
#  {"id": "porter", "name": "Porter", "value":65, "hp_fraction":0.40, "ap_fraction":0.0, "min_level":4},
#  {"id": "rum", "name": "Rum", "value":80, "hp_fraction":0.50, "ap_fraction":0.0, "min_level":5},
#  {"id": "brandy", "name": "Brandy", "value":110, "hp_fraction":0.60, "ap_fraction":0.0, "min_level":6},
#  {"id": "whiskey", "name": "Whiskey", "value":120, "hp_fraction":0.70, "ap_fraction":0.0, "min_level":7},
#  {"id": "cognac", "name": "Cognac", "value":130, "hp_fraction":0.80, "ap_fraction":0.0, "min_level":8},
#  {"id": "absinthe", "name": "Absinthe", "value":140, "hp_fraction":0.90, "ap_fraction":0.0, "min_level":9},
#  {"id": "elixir", "name": "Elixir", "value":200, "hp_fraction":1.00, "ap_fraction":0.3, "min_level":10},
# ]


def get_stock(player_level: int, player_game, current_region) -> List[Dict[str, Any]]:
    """Return available drinks for the given player level."""
    region_name = current_region.city_name if not current_region.isRegion() else current_region.region_name
    parent_region_name = current_region.parent_region_name

    #region_name = current_region.city_name if not current_region.isRegion() else current_region.region_name

    if parent_region_name is None:
        attr = f"{region_name.upper()}_DRINK_MENU"
    else:
        attr = f"{parent_region_name.upper()}_{region_name.upper()}_DRINK_MENU"
    drink_menu = getattr(const, attr)

    return [d for d in drink_menu if d.get("min_level",1) <= player_level]


def buy(player_game, drink: any) -> Dict[str, Any]:
    """Attempt to buy a drink for the player. Applies immediate HP/AP restore.

    Returns a dict: {'success': bool, 'error': str?, 'healed': int, 'ap_restored': int, 'drink': drink}
    """
    if drink is None:
        return {"success": False, "error": "invalid_drink"}
    price = drink.get("value",0)
    if player_game.money < price:
        return {"success": False, "error": "insufficient_funds"}
    # charge
    player_game.money -= price
    healed =0
    ap_restored =0
    hf = drink.get("hp_fraction",0)
    af = drink.get("ap_fraction",0)
    for player in player_game.characters:
        if hf and player.max_hp > 0:
            amt = max(0, int(player.max_hp * float(hf)))
            healed = player.heal(amt)
        if af and player.max_ap > 0:
            amt = max(0, int(player.max_ap * float(af)))
            player.current_ap = min(player.max_ap, player.current_ap + amt)
            ap_restored = amt
    return {"success": True, "drink": drink, "healed": healed, "ap_restored": ap_restored}
