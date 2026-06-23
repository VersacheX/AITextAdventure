from typing import List, Dict, Any
from game import constants as const

# ROOM_MENU = [
#  {"id": "bench", "name": "Bench", "value":5, "heal_fraction":0.25},
#  {"id": "room", "name": "Room", "value":20, "heal_fraction":0.75},
#  {"id": "private", "name": "Private Suite", "value":75, "heal_fraction":1.0},
# ]

def get_stock(player_level: int, player_game, current_region) -> List[Dict[str, Any]]:
    region_name = current_region.city_name if not current_region.isRegion() else current_region.region_name
    parent_region_name = current_region.parent_region_name
    if parent_region_name is None:
        attr = f"{region_name.upper()}_ROOM_MENU"
    else:
        attr = f"{parent_region_name.upper()}_{region_name.upper()}_ROOM_MENU"
    room_menu = getattr(const, attr)

    return [r for r in room_menu if r.get('min_level',1) <= player_level]


def buy(player_game, room) -> Dict[str, Any]:
    if room is None:
        return {'success': False, 'error': 'invalid_room'}
    price = room.get('value', 0)
    if player_game.money < price:
        return {'success': False, 'error': 'insufficient_funds'}
    player_game.money -= price
    # full heal behavior: fraction applied to both HP and AP, with private being full
    frac = room.get('heal_fraction',1.0)
    healed =0
    for player in player_game.characters:
        if frac and player.max_hp >0:
            amt = max(1, int(player.max_hp * float(frac)))
            healed = player.heal(amt)
            # also restore AP partially
            ap_amt = max(1, int(player.max_ap * float(frac))) if player.max_ap > 0 else 0
            player.current_ap = min(player.max_ap, player.current_ap + ap_amt)
    return {'success': True, 'room': room, 'healed': healed, 'ap_restored': ap_amt}
