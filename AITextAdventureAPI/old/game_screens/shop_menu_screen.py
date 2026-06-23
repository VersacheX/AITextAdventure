from typing import List, Any, Optional
from readchar import readkey, key
import os

from game.constants import SELL_RATIO
from services.utility_shop_service import buy as BuyItems, sell as SellItems, get_stock as GetStockItems
from services.weapon_shop_service import buy as BuyWeapon, sell as SellWeapon, get_stock as GetStockWeapon
from services.armor_shop_service import buy as BuyArmor, sell as SellArmor, get_stock as GetStockArmor
from services.inn_service import buy as BuyInn, get_stock as GetStockInn
from services.bar_service import buy as BuyBar, get_stock as GetStockBar
from game.constants_other import ELEMENTAL_CHAR_KEYS
from game.objects.weapon import Weapon
from game.objects.armor import Armor


def clear_screen() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class ListSelectionService:
    def __init__(self, items: List[Any], max_display: int =8):
        self.items = items
        self.max_display = int(max_display)
        self.selected =0
        self.offset =0

    @property
    def total(self) -> int:
        return len(self.items)

    def ensure_selected_visible(self) -> None:
        if self.selected < self.offset:
            self.offset = self.selected
        if self.selected >= self.offset + self.max_display:
            self.offset = max(0, self.selected - self.max_display +1)

    def move_up(self) -> None:
        if self.total ==0:
            return
        self.selected = max(0, self.selected -1)
        self.ensure_selected_visible()

    def move_down(self) -> None:
        if self.total ==0:
            return
        self.selected = min(max(0, self.total -1), self.selected +1)
        self.ensure_selected_visible()

    def page_up(self) -> None:
        if self.total ==0:
            return
        self.selected = max(0, self.selected - self.max_display)
        self.ensure_selected_visible()

    def page_down(self) -> None:
        if self.total ==0:
            return
        self.selected = min(self.total -1, self.selected + self.max_display)
        self.ensure_selected_visible()

    def get_max_qty(self, player_money: int) -> int:
        if self.total ==0:
            return 0
        item = self.items[self.selected]
        value = int(item.get('value') if isinstance(item, dict) else int(item.value))
        if value <=0:
            return 0
        return int(player_money / value)

    def get_min_qty(self, player_money: int) -> int:
        return 1 if self.get_max_qty(player_money) >0 else 0


def _filter_by_min_level(items: List[Any], min_level: int) -> List[Any]:
    if not min_level:
        return items
    out: List[Any] = []
    for it in items:
        if isinstance(it, dict):
            lvl = it.get('min_spawn_level', it.get('min_level',0))
        else:
            lvl = getattr(it, 'min_spawn_level', getattr(it, 'min_level',0))
        if lvl >= min_level:
            out.append(it)
    return out


def _format_elements(elems) -> str:
    if not elems:
        return ''
    out = ''
    # elems may be list of ids or objects with id/value
    if not isinstance(elems, (list, tuple)):
        elems = [elems]
    for e in elems:
        key = None
        if isinstance(e, dict):
            key = e.get('id') or e.get('name')
        elif isinstance(e, str):
            key = e
        elif e.getattr('id'):            
            key = e.id
            
        out += ELEMENTAL_CHAR_KEYS.get(str(key), str(key))
    return out


def _get_unique_equipped(player_game, is_armor: bool = False) -> List[Any]:
    """Return a deduplicated list of equipped items across player characters.
    Attempts common attributes for party storage (players, characters, party).
    """
    chars = getattr(player_game, 'characters', None) or getattr(player_game, 'players', None) or getattr(player_game, 'party', None) or []
    unique = []
    seen = set()
    slots = ('equipped_weapon',) if not is_armor else ('head_armor', 'body_armor', 'arm_armor', 'leg_armor')
    for c in chars:
        # c may be Player object or dict        
        for slot in slots:
            itm = getattr(c, slot, None)
            if not itm:
                continue
            name = getattr(itm, 'name', None) or (itm.get('name') if isinstance(itm, dict) else None)
            if not name:
                continue
            if name in seen:
                continue
            seen.add(name)
            unique.append(itm)
        
    return unique


def _render_shop_two_column(available_items, svc: ListSelectionService, player_game, shop_type, left_hint='Shop', right_hint='Your Gear') -> None:
    # determine terminal width
    
    term_w = os.get_terminal_size().columns
    
    if term_w <60:
        term_w =60
    # separator between columns
    sep = ' ** '
    inner = term_w -2 - len(sep)
    left_w = inner //2
    right_w = inner - left_w

    # print outer top border and title
    print('*' * term_w)
    title = f" {left_hint} " + f"(Money: {getattr(player_game, 'money',0)})"
    title_line = title.center(term_w -2)
    print('*' + title_line + '*')
    print('*' * term_w)

    # column headers: NAME | INFO | COST (cost is6 chars right aligned)
    cost_w =6
    name_info_w = left_w - cost_w
    left_header = (" NAME ").ljust(name_info_w) + ("COST").rjust(cost_w)
    right_header = right_hint.center(right_w)
    print('*' + left_header + sep + right_header + '*')
    print('*' + ('-' * (term_w -2)) + '*')

    # build left and right content lines
    left_lines: List[str] = []
    for idx in range(svc.offset, min(svc.offset + svc.max_display, svc.total)):
        it = available_items[idx]
        # read common fields
        if isinstance(it, dict):
            name = it.get('name') or 'item'
            price = int(it.get('value') or 0)
            desc = str(it.get('description') or '')
            elems = it.get('elements') or it.get('element')
        else:
            name = getattr(it, 'name', 'item')
            price = int(getattr(it, 'value',0) or 0)
            desc = str(getattr(it, 'description', '') or '')
            elems = getattr(it, 'elements', None) or getattr(it, 'element', None)

        # format stat/info depending on shop type or available attrs
        stat_parts: List[str] = []
        # try weapon-ish stats
        dmg = (it.damage if isinstance(it, Weapon) else None)
        crit = (it.critical_chance if isinstance(it, Weapon) else None)
        # class ArmorType(Enum):
	       #  HEAD = "head"
	       #  BODY = "body"
	       #  ARMS = "arms"
	       #  LEGS = "legs"


        # @dataclass
        # class Armor(Item):
	       #  """Armor item that can be equipped to a specific slot.

	       #  Fields:
	       #  - slot: ArmorType where this armor can be equipped
	       #  - defense: flat damage reduction provided by the armor
	       #  - durability: current durability
	       #  - max_durability: maximum durability
	       #  """
	       #  slot: ArmorType = ArmorType.BODY
	       #  defense: int =0
        slot = (it.slot if isinstance(it, Armor) else None)
        defense = (it.defense if isinstance(it, Armor) else None)
        # attribute bonuses
        for k, label in (('strength', 'S'), ('dexterity', 'D'), ('intelligence', 'I'), ('constitution', 'C')):
            v = (it.get(k) if isinstance(it, dict) else getattr(it, k, None))
            if v:
                stat_parts.append(f"{label}:{v}")
        if dmg:
            stat_parts.insert(0, f"dmg:{dmg}")
        if crit:
            stat_parts.insert(1 if dmg else 0, f"c%:{crit}")
        if slot:
            stat_parts.insert(0, f"({slot.name})")
        if defense:
            stat_parts.insert(1 if slot else 0, f"def:{defense}")
        elem_str = _format_elements(elems)
        if elem_str:
            stat_parts.append(elem_str)
        stat_info = ' '.join(stat_parts)

        prefix = '>' if idx == svc.selected else ' '
        # left first line: name + stat_info, reserve cost_w for cost at right
        name_text = f"{prefix} {name}"
        # place stat_info right-aligned inside the name/info area, truncating if needed
        if stat_info:
            # compute how many chars are available for stat_info on the right
            max_stat_width = max(0, name_info_w - len(name_text))
            if max_stat_width <=0:
                # no room for stat, truncate name_text
                if name_info_w >=3:
                    name_disp = name_text[:max(0, name_info_w -3)] + '...'
                else:
                    name_disp = name_text[:name_info_w]
                name_field = name_disp.ljust(name_info_w)
            else:
                # truncate stat_info to fit on the right (keep rightmost chars)
                if len(stat_info) > max_stat_width:
                    if max_stat_width >=4:
                        stat_disp = '...' + stat_info[-(max_stat_width -3):]
                    else:
                        stat_disp = stat_info[-max_stat_width:]
                else:
                    stat_disp = stat_info
                stat_width = len(stat_disp)
                name_field = name_text.ljust(max(0, name_info_w - stat_width)) + stat_disp.rjust(stat_width)
        else:
            # no stat info, just left-justify name in the available space
            if len(name_text) > name_info_w:
                name_field = (name_text[:max(0, name_info_w -3)] + '...')
            else:
                name_field = name_text.ljust(name_info_w)
        cost_part = f"{price:>{cost_w}}"
        left_lines.append(name_field + cost_part)
        # second line: indented description
        desc_line = ('    - ' + desc) if desc else ''
        if len(desc_line) > left_w:
            desc_line = desc_line[:max(0, left_w -3)] + '...'
        left_lines.append(desc_line.ljust(left_w))

    # right column: unique equipped items (one-line entries: name left, stats right)
    right_items = _get_unique_equipped(player_game, is_armor = shop_type == 'shoparmor')
    right_lines: List[str] = []
    if not right_items:
        # keep height consistent with left (two lines per logical item: entry + spacer)
        right_lines.append('(No equipped items)'.center(right_w))
        right_lines.append(' ' * right_w)
    else:
        for it in right_items:
            if isinstance(it, dict):
                rname = it.get('name') or ''
            else:
                rname = getattr(it, 'name', str(it))
            # build same stat summary as left
            stats = []
            # try weapon-ish stats first
            rdmg = (it.get('damage') if isinstance(it, dict) else getattr(it, 'damage', None))
            rcrit = (it.get('critical_chance') or it.get('crit')) if isinstance(it, dict) else getattr(it, 'critical_chance', None)
            if rdmg:
                stats.append(f"dmg:{rdmg}")
            if rcrit:
                stats.append(f"c%:{rcrit}")
            for k in ('strength', 'dexterity', 'intelligence', 'constitution', 'defense'):
                v = (it.get(k) if isinstance(it, dict) else getattr(it, k, None))
                if v:
                    stats.append(f"{k[:3].upper()}:{v}")
            # elements
            elems = (it.get('elements') if isinstance(it, dict) else getattr(it, 'elements', None)) or (it.get('element') if isinstance(it, dict) else getattr(it, 'element', None))
            elem_str = _format_elements(elems)
            if elem_str:
                stats.append(elem_str)
            rinfo = ' '.join(stats)

            # compose single-line: name left, rinfo right within right_w
            rname_text = str(rname)
            if rinfo:
                max_stat_width = max(0, right_w -1 - len(rname_text))
                if max_stat_width <=0:
                    # no room for stats; truncate name to fit
                    rfield = (rname_text[:right_w])[:right_w].ljust(right_w)
                else:
                    if len(rinfo) > max_stat_width:
                        if max_stat_width >=4:
                            stat_disp = '...' + rinfo[-(max_stat_width -3):]
                        else:
                            stat_disp = rinfo[-max_stat_width:]
                    else:
                        stat_disp = rinfo
                    rfield = rname_text.ljust(max(0, right_w - len(stat_disp))) + stat_disp.rjust(len(stat_disp))
            else:
                rfield = rname_text[:right_w].ljust(right_w)

            right_lines.append(rfield)
            # spacer line to match left's description line
            #right_lines.append(' ' * right_w)

    # pad lists to same height
    rows = max(len(left_lines), len(right_lines))
    while len(left_lines) < rows:
        left_lines.append(' ' * left_w)
    while len(right_lines) < rows:
        right_lines.append(' ' * right_w)

    # print rows enclosed in stars
    for l, r in zip(left_lines, right_lines):
        print('*' + l + sep + r + '*')

    # bottom border
    print('*' * term_w)


def handle_shop_menu(player_game, business_def: any, region) -> Optional[bool]:
    # Determine available actions from business_def
    while True:
        options: List[str] = []
        can_buy = business_def.get('can_buy', False)
        can_sell = business_def.get('can_sell', False)
        if can_buy:
            options.append('1) Buy')
        if can_sell:
            options.append('2) Sell')
        options.append('Esc) Back')
        clear_screen()
        print(f"Welcome to {business_def.get('name','the shop')}!\n")
        print("What would you like to do?\n")
        print('\n'.join(options))
        choice = readkey()

        if not choice:
            continue
        if choice == key.ESC:
            return None
        if choice == '1' and can_buy:
            res = handle_shop_buy_menu(player_game, business_def, region)
            if res:
                return True
            else:
                continue
        if choice == '2' and can_sell:
            handle_shop_sell_menu(player_game, business_def)
            continue

        return None


def handle_shop_buy_menu(player_game, business_def: any, region) -> bool:
    shop_type = business_def.get('name', 'general')
    available_items: List[Any] = []
    if shop_type == 'shopweapons':
        available_items = GetStockWeapon(player_game.get_max_character_level(), region)
    elif shop_type == 'shoparmor':
        available_items = GetStockArmor(player_game.get_max_character_level(), region)
    elif shop_type == 'shopitems':
        available_items = GetStockItems(player_game.get_max_character_level(), region)
    elif shop_type == 'inn':
        available_items = GetStockInn(player_game.get_max_character_level(), player_game, region)
    elif shop_type == 'bar':
        available_items = GetStockBar(player_game.get_max_character_level(), player_game, region)

    min_level = business_def.get('min_spawn_level',0)
    available_items = _filter_by_min_level(available_items, min_level)

    svc = ListSelectionService(available_items, max_display=8)
    quantity =1
    isAction = False

    while True:
        clear_screen()
        print("What would you like to buy? (Use Up/Down to move, +/- to change qty, Enter to buy, Esc to back)\n")
        print(f"Your Money: {player_game.money}\n")
        if svc.total ==0:
            print("(No items available)")
        else:
            # render a richer two-column shop view (shop items left, unique equipped items right)
            _render_shop_two_column(available_items, svc, player_game, shop_type)
        print(f"\nQuantity: {quantity}")
        choice = readkey()
        if not choice:
            continue
        if choice == key.ESC:
            return isAction
        if choice == key.UP:
            svc.move_up()
            max_qty = svc.get_max_qty(player_game.money)
            quantity = quantity if max_qty >= quantity else max_qty
            continue
        if choice == key.DOWN:
            svc.move_down()
            max_qty = svc.get_max_qty(player_game.money)
            quantity = quantity if max_qty >= quantity else max_qty
            continue
        if choice == key.PAGE_UP:
            svc.page_up()
            max_qty = svc.get_max_qty(player_game.money)
            quantity = quantity if max_qty >= quantity else max_qty
            continue
        if choice == key.PAGE_DOWN:
            svc.page_down()
            max_qty = svc.get_max_qty(player_game.money)
            quantity = quantity if max_qty >= quantity else max_qty

            continue
        if choice in ('+', '='):            
            max_qty = svc.get_max_qty(player_game.money)
            quantity = min(quantity + 1, max_qty)
            continue
        if choice == '-':            
            min_val = svc.get_min_qty(player_game.money)
            quantity = max(min_val, quantity - 1)
            continue
        if choice in ('\r', '\n'):
            if svc.total ==0:
                continue
            item_to_buy = available_items[svc.selected]
            success = False
            # perform purchases quantity times (best-effort)
            for _ in range(quantity):
                import copy
                # make a copy of the item to buy if needed
                copy_item = copy.deepcopy(item_to_buy)
                if shop_type == 'shopweapons':
                    res = BuyWeapon(player_game, copy_item)
                elif shop_type == 'shoparmor':
                    res = BuyArmor(player_game, copy_item)
                elif shop_type == 'shopitems':
                    res = BuyItems(player_game, copy_item)
                elif shop_type == 'inn':
                    res = BuyInn(player_game, copy_item)
                elif shop_type == 'bar':
                    res = BuyBar(player_game, copy_item)
                else:
                    res = {'success': False, 'error': 'unknown_shop_type'}
                if not res.get('success'):
                    print(f"Purchase failed: {res.get('error', 'unknown_error')}")
                    input("Press Enter to continue...")
                    break
                else:
                    success = True
            if success:
                bought_name = item_to_buy.name if not isinstance(item_to_buy, dict) else item_to_buy.get('name', 'item')
                print(f"You purchased {bought_name} x{quantity}.")
                input("Press Enter to continue...")
                if shop_type == 'bar':
                    isAction = True
                # refresh stock if desired by re-fetching available_items
                return isAction
        # support numeric selection as before
        if choice.isdigit():
            sel = int(choice)
            if 1 <= sel <= svc.total:
                svc.selected = sel -1
                svc.ensure_selected_visible()
                continue


def handle_shop_sell_menu(player_game, business_def: any) -> None:
    svc = ListSelectionService(list(player_game.get_sellable_inventory()), max_display=8)
    while True:
        clear_screen()
        print("What would you like to sell? (Use Up/Down to move, Enter to sell, Esc to back)\n")
        for idx in range(svc.offset, min(svc.offset + svc.max_display, svc.total)):
            item = svc.items[idx]
            print(f"{'>' if idx == svc.selected else ' '} {idx +1}) {item.name} - Value: {item.value * SELL_RATIO}")
        choice = readkey()
        if not choice:
            continue
        if choice == key.ESC:
            return
        if choice == key.UP:
            svc.move_up()
            continue
        if choice == key.DOWN:
            svc.move_down()
            continue
        if choice in ('\r', '\n'):
            if svc.total ==0:
                continue
            selected = svc.items[svc.selected]
            shop_name = business_def.get('name')
            if shop_name == 'shopweapons':
                res = SellWeapon(player_game, selected)
            elif shop_name == 'shoparmor':
                res = SellArmor(player_game, selected)
            elif shop_name == 'shopitems':
                res = SellItems(player_game, selected)
            else:
                res = {'success': False, 'error': 'unknown_shop_type'}
            if res.get('success'):
                print(f"You sold {res['item'].name} for {res['price']} money.")
            else:
                print(f"Sale failed: {res.get('error', 'unknown_error')}")
            input("Press Enter to continue...")
            return
        if choice.isdigit():
            sel = int(choice)
            if 1 <= sel <= svc.total:
                svc.selected = sel -1
                svc.ensure_selected_visible()
                continue
