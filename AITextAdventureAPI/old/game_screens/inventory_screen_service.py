from typing import List, Dict, Any, Tuple

import pickle
import base64
from datetime import datetime
import hashlib
import json

# Lazy import client API to avoid hard dependency at module import time
from client_api_requests.client_api_requests import ClientAPI
from client_api_requests.save_game_service import save_player_game


class InventoryScreenService:
    """Encapsulate selection and view logic for the inventory screen.

    Responsibilities:
    - Track selected character index and viewport offset
    - Provide methods to move selection left/right and toggle abilities view
    - Provide a lightweight view context for UI rendering
    """

    def __init__(self, player_game: Any, max_display: int = 5) -> None:
        self.player_game = player_game
        self.max_display = int(max_display)
        self.selected: int = 0
        self.offset: int = 0
        # mapping absolute index -> bool whether abilities panel is shown for that character
        self.abilities_map: Dict[int, bool] = {}

    @property
    def players(self) -> List:
        return list(self.player_game.characters)

    @property
    def total(self) -> int:
        return len(self.players)

    def ensure_selected_visible(self) -> None:
        if self.selected < self.offset:
            self.offset = self.selected
        if self.selected >= self.offset + self.max_display:
            self.offset = max(0, self.selected - self.max_display + 1)

    def move_left(self) -> None:
        if self.total == 0:
            return
        self.selected = max(0, self.selected - 1)
        if self.selected < self.offset:
            self.offset = self.selected

    def move_right(self) -> None:
        if self.total == 0:
            return
        self.selected = min(max(0, self.total - 1), self.selected + 1)
        if self.selected >= self.offset + self.max_display:
            self.offset = self.selected - self.max_display + 1

    def toggle_abilities(self) -> None:
        if self.total == 0:
            return
        self.abilities_map[self.selected] = not self.abilities_map.get(
            self.selected, False
        )

    def get_view_context(self) -> Dict[str, Any]:
        """Return current view state used by UI renderer.

        Contains: players, total, selected_index, offset, abilities_map, display_n
        """
        players = self.players
        total = len(players)
        # clamp selected and offset to sensible ranges
        if total == 0:
            sel = 0
            off = 0
        else:
            sel = max(0, min(self.selected, total - 1))
            off = max(0, min(self.offset, total - 1))
        # ensure visibility
        if sel < off:
            off = sel
        if sel >= off + self.max_display:
            off = max(0, sel - self.max_display + 1)
        remaining = max(0, total - off)
        display_n = min(self.max_display, remaining)
        return {
            "players": players,
            "total": total,
            "selected_index": sel,
            "offset": off,
            "abilities_map": dict(self.abilities_map),
            "display_n": display_n,
        }

    def save_game(self, name: str = None, client: Any = None) -> Tuple[bool, str]:
        """Serialize and save the current PlayerGame using the ClientAPI.

        Delegates to `save_load_game_service.save_player_game` to keep payload/metadata handling consistent.
        Returns (success, message)."""
        
        # prefer delegating to central helper if available
        if save_player_game is not None:
            client = client or (ClientAPI() if ClientAPI else None)
            success, msg, _ = save_player_game(self.player_game, name=name, client=client)
            return success, msg


