from typing import Any, Dict, Optional, Tuple
import pickle
import base64
import hashlib
import json
from datetime import datetime

from client_api_requests.client_api_requests import ClientAPI

def save_player_game(player_game: Any, name: Optional[str] = None, client: Any = None, save_adapter: Any = None) -> Tuple[bool, str, Optional[int]]:
    """Serialize and save the current PlayerGame using the ClientAPI.

    Returns (success, message, save_id)
    """
    if ClientAPI is None and client is None and save_adapter is None:
        return False, "API client not available", None

    client = save_adapter or client or ClientAPI()

    try:
        if name:
            player_game.name = name
        # Serialize player_game using pickle and base64-encode it
        blob_bytes = pickle.dumps(player_game)
        #game_hash = hashlib.sha256(blob_bytes).hexdigest()
        blob_b64 = base64.b64encode(blob_bytes).decode("utf-8")

        # Ensure we always have a name to send to the server
        final_name = name or getattr(player_game, 'name', None)
        if not final_name:
            # save name = autosave - (mm/dd/yyyy hh:mm:ss)
            final_name = "autosave - " + datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            
        player_game.name = final_name

        # payload: server expects a JSON-serializable object under 'blob'
        payload: Dict[str, Any] = {"pickle": blob_b64}

        # look for existing saves with same game_id
        #### UPDATE - if name passed in, create new regardless and update player_game.save_id####
        sid = getattr(player_game, 'save_id', None)

        # Prepare sendable forms: convert blob and metadata to JSON string to mimic metadata persistence
        send_blob = json.dumps(payload)

        if sid is not None and not name:
            res = client.update_save(sid, 
                                     final_name, 
                                     player_game.characters[0].name, 
                                     player_game.get_max_character_level(), 
                                     player_game.money, 
                                     send_blob, 
                                     schema_version=1, 
                                     metadata=None)
            result_id = res.get("id")
        else:
            res = client.create_save(final_name, 
                                     player_game.characters[0].name, 
                                     player_game.get_max_character_level(), 
                                     player_game.money, 
                                     send_blob, 
                                     schema_version=1, 
                                     metadata=None)
            new_id = res.get("id")
            player_game.save_id = new_id
            result_id = new_id

        msg = f"Saved: {final_name}"
        if result_id:
            msg += f" (id={result_id})"
        return True, msg, result_id

    except Exception as e:
        return False, f"Save failed: {e}", None
