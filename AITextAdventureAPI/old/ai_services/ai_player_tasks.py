from typing import Any, Dict, List, Tuple

from ai_services.ai_pathing_logic import find_nearest_target_by_predicate, direction_from_path
from ai_services.ai_treasure_hunter_logic import (
 pick_up_sublocations_at_player,
 next_direction_to_loot,
 next_direction_to_nearest_shop,
 shop_is_armor,
 shop_is_items,
)
from ai_services.ai_combat_logic import is_healing_item, find_healing_item_index
from ai_services.ai_equipment_logic import equip_item_if_better
from ai_services.ai_ui_helper import type_victory_message
from ai_services.ai_logic_engine import choose_movement_avoiding_recent

# shop APIs
from services.armor_shop_service import get_stock as GetStockArmor, buy as BuyArmor, sell as SellArmor
from services.utility_shop_service import get_stock as GetStockItems, buy as BuyItems, sell as SellItems
from services.weapon_shop_service import get_stock as GetStockWeapons, buy as BuyWeapons, sell as SellWeapons


def _safe_get_name(obj: Any) -> str:
    try:
        if hasattr(obj, "name"):
            return getattr(obj, "name") or ""
        if isinstance(obj, dict):
            return obj.get("name") or ""
        return str(obj)
    except Exception:
        try:
            return str(obj)
        except Exception:
            return ""


def _safe_int(value: Any, default: int =0) -> int:
    try:
        return int(value)
    except Exception:
        return default


def _move_by_direction(
    direction: Any,
    allowed_moves: Dict[str, Any],
    _try_move,
    player,
    pg,
    recent_positions,
) -> bool:
    """Try suggested direction, otherwise pick an alternative."""
    try:
        if isinstance(direction, str) and direction in allowed_moves and _try_move(direction):
            return True
    except Exception:
        pass

    try:
        alt = choose_movement_avoiding_recent(player, pg, allowed_moves, recent_positions)
        if alt and _try_move(alt):
            return True
    except Exception:
        pass

    return False


def handle_action(
    action: str,
    status: Dict[str, Any],
    player: Any,
    pg: Any,
    active_area: Any,
    allowed_moves: Dict[str, Any],
    _try_move,
    ai_stats: Dict[str, Any],
    ai_state: Dict[str, Any],
    recent_positions: List[Tuple[int, int, bool, int]],
) -> Tuple[bool, Dict[str, Any]]:
    """Handle a single AI action and return (moved_flag, possibly_updated_status)."""
    moved_flag = False

    # Debug (safe in non-interactive environments)
    try:
        print(f"AI Action: {action}, Status: {status}")
        input("Press Enter to continue...")
    except Exception:
        pass

    def _log_pickup() -> None:
        try:
            picked = pick_up_sublocations_at_player(active_area, player)
            if picked:
                for desc in picked:
                    type_victory_message(f"AI: {desc}", delay=0.05)
                ai_stats["loots"] = ai_stats.get("loots",0) + len(picked)
                ai_stats["tasks"] = ai_stats.get("tasks",0) + len(picked)
        except Exception:
            pass

    # BUY ARMOR
    if action == "buy_armor":
        dir_to_shop = status.get("direction")
        if _move_by_direction(dir_to_shop, allowed_moves, _try_move, player, pg, recent_positions):
            moved_flag = True
            _log_pickup()

        # If at an armor shop, attempt purchase
        try:
            cur_tile = active_area.get_tile(player.x, player.y)
        except Exception:
            cur_tile = None

        if cur_tile and getattr(cur_tile, "building", None) and shop_is_armor(cur_tile.building):
            stock = GetStockArmor(player.level, active_area) or []
            for it in stock:
                try:
                    slot = None
                    if hasattr(it, "slot"):
                        slot = getattr(it, "slot")
                    elif isinstance(it, dict):
                        slot = it.get("slot")
                    if isinstance(slot, dict):
                        slot = slot.get("name")
                    if not slot:
                        continue
                    slot = str(slot).upper()

                    val = _safe_int(it.get("defense") if isinstance(it, dict) else getattr(it, "defense", None),0)
                    price = _safe_int(it.get("price") if isinstance(it, dict) else getattr(it, "price", None),0)

                    cur_def =0
                    if slot == "HEAD" and getattr(player, "head_armor", None):
                        cur_def = _safe_int(getattr(player.head_armor, "defense", None),0)
                    elif slot == "BODY" and getattr(player, "body_armor", None):
                        cur_def = _safe_int(getattr(player.body_armor, "defense", None),0)
                    elif slot == "ARMS" and getattr(player, "arm_armor", None):
                        cur_def = _safe_int(getattr(player.arm_armor, "defense", None),0)
                    elif slot == "LEGS" and getattr(player, "leg_armor", None):
                        cur_def = _safe_int(getattr(player.leg_armor, "defense", None),0)

                    if val <= cur_def:
                        continue

                    if price <= getattr(player, "money",0):
                        res = BuyArmor(player, it)
                        if res.get("success"):
                            iname = _safe_get_name(it)
                            type_victory_message(f"AI bought and equipped {iname}", delay=0.05)
                            equip_item_if_better(player, it)
                            ai_stats["purchases"] = ai_stats.get("purchases",0) +1
                            ai_stats["tasks"] = ai_stats.get("tasks",0) +1
                            break
                except Exception:
                    continue

    # BUY ITEMS
    elif action == "buy_items":
        dir_to_shop = status.get("direction")
        if _move_by_direction(dir_to_shop, allowed_moves, _try_move, player, pg, recent_positions):
            moved_flag = True
            _log_pickup()

        try:
            cur_tile = active_area.get_tile(player.x, player.y)
        except Exception:
            cur_tile = None

        if cur_tile and getattr(cur_tile, "building", None) and shop_is_items(cur_tile.building):
            stock = GetStockItems(player.level, active_area) or []
            stock_by_name: Dict[str, Any] = {}
            for it in stock:
                try:
                    if is_healing_item(it):
                        name = _safe_get_name(it)
                        if name:
                            stock_by_name[name] = it
                except Exception:
                    continue

            shopping_list = list(ai_state.get("shopping_list", []))
            restock_threshold = max(1, int(5 * (1 + (getattr(player, "level",1) -1) *0.5)))
            for entry in shopping_list:
                try:
                    name = entry.get("name")
                    target = int(entry.get("target",10))
                    item = stock_by_name.get(name)
                    if not item:
                        continue

                    price = _safe_int(item.get("price") if isinstance(item, dict) else getattr(item, "price", None),0)
                    have = sum(1 for inv in getattr(player, "inventory", []) or [] if (_safe_get_name(inv) == name))
                    if have >= target:
                        continue

                    while (
                        have < target
                        and getattr(player, "money",0) >= price
                        and len(pg.inventory) < pg.max_inventory_count
                    ):
                        res = BuyItems(player, item)
                        if res.get("success"):
                            have +=1
                            ai_stats["purchases"] = ai_stats.get("purchases",0) +1
                            ai_stats["tasks"] = ai_stats.get("tasks",0) +1
                            type_victory_message(f"AI bought {name}", delay=0.1)
                        else:
                            reason = res.get("error") or res.get("message") or "unknown"
                            type_victory_message(f"Purchase failed: {reason}", delay=0.1)
                            if reason == "insufficient_funds":
                                ai_state["seeking_loot"] = True
                                dir_loot = next_direction_to_loot(player, pg)
                                status = {
                                    "action": "move_to_loot",
                                    "description": "Need money: seeking loot nearby",
                                    "direction": dir_loot,
                                }
                            break
                except Exception:
                    continue

    # BUY WEAPONS
    elif action in ("buy_weapon", "buy_weapons"):
        dir_to_shop = status.get("direction")
        if _move_by_direction(dir_to_shop, allowed_moves, _try_move, player, pg, recent_positions):
            moved_flag = True
            _log_pickup()

        try:
            cur_tile = active_area.get_tile(player.x, player.y)
        except Exception:
            cur_tile = None

        building = getattr(cur_tile, "building", None) if cur_tile else None
        is_weapon_shop = False
        if building:
            try:
                name = getattr(building, "name", "") if not isinstance(building, dict) else building.get("name", "")
                if isinstance(name, str) and "weapon" in name.lower():
                    is_weapon_shop = True
            except Exception:
                is_weapon_shop = False

        if cur_tile and building and is_weapon_shop:
            stock = GetStockWeapons(player.level, active_area) or []
            try:
                eq = getattr(player, "equipped_weapon", None)
                cur_dmg = int(getattr(eq, "damage",0) or 0)
            except Exception:
                cur_dmg = 0

            best = None
            best_dmg =0
            for w in stock:
                try:
                    wd = int((w.get("damage") if isinstance(w, dict) else getattr(w, "damage",0)) or 0)
                    price = int((w.get("price") if isinstance(w, dict) else getattr(w, "price",0)) or 0)
                except Exception:
                    continue

                if wd <= cur_dmg:
                    continue
                if price > getattr(player, "money",0):
                    continue
                if best is None or wd > best_dmg:
                    best = w
                    best_dmg = wd

            if best is not None:
                res = BuyWeapons(player, best)
                if res.get("success"):
                    iname = _safe_get_name(best)
                    type_victory_message(f"AI bought and equipped {iname}", delay=0.05)
                    equip_item_if_better(player, best)
                    ai_stats["purchases"] = ai_stats.get("purchases",0) +1
                    ai_stats["tasks"] = ai_stats.get("tasks",0) +1

    # SELL ITEMS
    elif action == "sell_items":
        dir_to_shop = status.get("direction")
        if _move_by_direction(dir_to_shop, allowed_moves, _try_move, player, pg, recent_positions):
            moved_flag = True

        try:
            cur_tile = active_area.get_tile(player.x, player.y)
        except Exception:
            cur_tile = None

        if cur_tile and getattr(cur_tile, "building", None):
            b = cur_tile.building
            sell_fn = SellItems
            try:
                if shop_is_armor(b):
                    sell_fn = SellArmor
                elif shop_is_items(b):
                    sell_fn = SellItems
                else:
                    sell_fn = SellWeapons
            except Exception:
                sell_fn = SellItems

            inv = getattr(player, "inventory", []) or []
            for idx in range(len(inv) -1, -1, -1):
                try:
                    it = inv[idx]
                    # skip equipped armor/weapons
                    if (
                        getattr(player, "head_armor", None) is it
                        or getattr(player, "body_armor", None) is it
                        or getattr(player, "arm_armor", None) is it
                        or getattr(player, "leg_armor", None) is it
                        or getattr(player, "equipped_weapon", None) is it
                    ):
                        continue
                    if sell_fn:
                        res = sell_fn(player, idx)
                        if res.get("success"):
                            ai_stats["tasks"] = ai_stats.get("tasks",0) +1
                            ai_stats["purchases"] = ai_stats.get("purchases",0) +1
                            break
                except Exception:
                    continue

    # MOVE TO LOOT
    elif action == "move_to_loot":
        dir_loot = status.get("direction")
        if isinstance(dir_loot, str) and dir_loot in allowed_moves and _try_move(dir_loot):
            moved_flag = True
            _log_pickup()
        else:
            if _move_by_direction(None, allowed_moves, _try_move, player, pg, recent_positions):
                moved_flag = True

    # HEAL SELF
    elif action == "heal_self":
        idx = None
        try:
            if find_healing_item_index is not None:
                idx = find_healing_item_index(pg)
        except Exception:
            idx = None

        if idx is None:
            inv = getattr(player, "inventory", []) or []
            for i, it in enumerate(inv):
                try:
                    if is_healing_item(it):
                        idx = i
                        break
                except Exception:
                    continue

        if idx is not None:
            try:
                res = player.use_item(idx, pg)
            except Exception:
                res = None

            name = "healing item"
            try:
                item = getattr(player, "inventory", [])[idx]
                name = (
                    getattr(item, "name", None)
                    if hasattr(item, "name")
                    else (item.get("name") if isinstance(item, dict) else str(item))
                )
            except Exception:
                name = "healing item"

            if isinstance(res, dict) and res.get("used"):
                type_victory_message(f"AI used {name} to heal.", delay=0.05)
                ai_stats["tasks"] = ai_stats.get("tasks",0) +1
                return False, status

        # Try to buy healing items
        dir_shop = None
        try:
            dir_shop = next_direction_to_nearest_shop(player, pg, "shopitems")
        except Exception:
            dir_shop = None
        if dir_shop:
            status = {
                "action": "buy_items",
                "description": "Move to shop to restock healing items",
                "direction": dir_shop,
            }
            return False, status

        # Seek loot if nothing else
        ai_state["seeking_loot"] = True
        dir_loot = next_direction_to_loot(player, pg)
        status = {
            "action": "move_to_loot",
            "description": "Seeking loot for healing items",
            "direction": dir_loot,
        }
        return False, status

    # LEAVE REGION
    elif action == "leave_region":
        dir_to_exit = status.get("direction")
        if isinstance(dir_to_exit, str) and dir_to_exit in allowed_moves and _try_move(dir_to_exit):
            moved_flag = True
        else:
            if _move_by_direction(None, allowed_moves, _try_move, player, pg, recent_positions):
                moved_flag = True

    return moved_flag, status
