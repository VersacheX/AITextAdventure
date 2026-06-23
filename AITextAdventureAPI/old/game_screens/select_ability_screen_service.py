from typing import List, Dict, Optional, Any
from game.objects.player_ability import get_potential_player_abilities_as_player_ability_list

class SelectAbilityScreenService:
    def __init__(self, player_game: Any, page_size: int =8):
        self.player_game = player_game
        self.page_size = max(1, int(page_size))
        self.selected_index =0
        self.offset =0

    def get_view_context(self, selected_player=None, ability_type_filter: Optional[str] = None) -> Dict:
        abilities: List = []

        abilities = get_potential_player_abilities_as_player_ability_list(selected_player)

        if ability_type_filter:
            # PlayerAbility.ability_type is an Enum; compare its value to the filter string
            filtered = []
            for a in abilities:
                at = getattr(a, 'ability_type', None)
                if at is not None and getattr(at, 'value', None) == ability_type_filter:
                    filtered.append(a)
                
            abilities = filtered
        total = len(abilities)
        # clamp indices
        self.selected_index = max(0, min(self.selected_index, max(0, total -1)))
        if self.selected_index < self.offset:
            self.offset = self.selected_index
        if self.selected_index >= self.offset + self.page_size:
            self.offset = max(0, self.selected_index - self.page_size +1)
        remaining = max(0, total - self.offset)
        display_n = min(self.page_size, remaining)
        return {
            'abilities': abilities,
            'total': total,
            'selected_index': self.selected_index,
            'offset': self.offset,
            'display_n': display_n,
        }

    def move_up(self):
        if self.selected_index >0:
            self.selected_index -=1
        if self.selected_index < self.offset:
            self.offset = max(0, self.selected_index)

    def move_down(self):
        self.selected_index +=1

    def learn_selected(self, selected_player, ability_type_filter: Optional[str] = None) -> Dict:
        ctx = self.get_view_context(selected_player, ability_type_filter)
        if ctx['total'] ==0:
            return {'ok': False, 'error': 'empty'}
        idx = self.selected_index
        ability = ctx['abilities'][idx]

        if not selected_player:
            return {'ok': False, 'error': 'no_player'}
        selected_player.learn_ability(ability)
        owned = selected_player.abilities

        if ability in owned:
            return {'ok': True, 'ability': ability}

        return {'ok': False, 'error': 'learn_failed'}
