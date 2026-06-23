from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.objects.player_game import PlayerGame # pragma: no cover
    from game.objects.city import City # pragma: no cover

def get_city_parent_region(city, player_game):
    """Given a city, find its parent region in the player_game's regions list.

    This function avoids importing PlayerGame at module import time to prevent
    circular import problems. Type hints are only used during static analysis.
    """
    for region in player_game.regions:
        if hasattr(region, 'child_city') and region.child_city == city:
            return region
    return None