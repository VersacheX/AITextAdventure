import game.constants_items as const_items
from typing import List, Dict, Any
from game.objects.player import Player
from game.objects.item import Item
from game.objects.utility_item import UtilityItem
from game.objects.player_ability import PlayerAbility, get_player_ability_instances
from game.constants_other import ABILTITY_EFFECT_DISPLAY_NAME, ABILITY_STATUS_KEY_DISPLAY_NAMES, ELEMENTAL_CHAR_KEYS


def _make_border(width: int) -> str:
	return '*' * width


def header_section(name: str, width: int =60) -> List[str]:
	title = f" {name} "
	if len(title) +4 > width:
		width = len(title) +4
	border = _make_border(width)
	return [border, f"*{title.center(width-2)}*", border]


def stats_section(player: Player, width: int =60) -> List[str]:
	border = _make_border(width)
	# New layout: HP/AP on left column, Level on right column with XP/next_xp beneath
	inner_w = max(0, width -4)
	current_hp = player.current_hp
	current_ap = player.current_ap
	left_hp = f"HP: {current_hp}/{player.max_hp}"
	left_ap = f"AP: {current_ap}/{player.max_ap}"
	# level and xp info on right
	level_s = f"Level: {getattr(player, 'level',0)}"
	next_xp = player.get_required_experience_to_level()
	cur_xp = player.experience
	xp_line = f"XP: {cur_xp}/{next_xp}"

	def _make_spaced_row(left: str, right: str) -> str:
		"""Place left and right into the inner width with appropriate spacing.
		If content is too long, truncate (prefer right first) and add ellipses when possible.
		"""
		left = str(left)
		right = str(right)
		# quick fit
		space = inner_w - len(left) - len(right)
		if space >=1:
			return f"* {left}{' ' * space}{right} *"
		# need to truncate. Prefer truncating right first to preserve left.
		max_right = max(0, inner_w -1) # at least1 space reserved for separation
		if len(right) > max_right:
			if max_right >=3:
				right = right[:max(0, max_right -3)] + '...'
			else:
				right = right[:max_right]
		# now compute how much space remains for left (reserve1 space)
		max_left = max(0, inner_w - len(right) -1)
		if len(left) > max_left:
			if max_left >=3:
				left = left[:max(0, max_left -3)] + '...'
			else:
				left = left[:max_left]
		space = inner_w - len(left) - len(right)
		if space <1:
			space =1
		return f"* {left}{' ' * space}{right} *"

	lines: List[str] = [border]
	# first row: HP (left) and Level (right)
	lines.append(_make_spaced_row(left_hp, level_s))
	# second row: AP (left) and XP (right)
	lines.append(_make_spaced_row(left_ap, xp_line))

	if len(player.statuses) >0:
		# Build list of status names (with element char mappings) and pack them into lines that fit the inner width
		parts: List[str] = []
		for s in player.statuses:
			if not isinstance(s, dict):
				parts.append(str(s))
				continue
			name = s.get('name') or s.get('id') or ''
			# map elements if present
			elems = s.get('elements') or ([s.get('element')] if s.get('element') is not None else [])
			if elems:
				# map each element id to its char key
				chars = ''.join([ELEMENTAL_CHAR_KEYS.get(str(e), str(e)) for e in elems])
				parts.append(f"{name} {chars}")
			else:
				parts.append(name)

		inner_w = max(0, width -4)
		prefix = 'Status: '
		lines_content: List[str] = []
		current = ''
		first_line = True
		for nm in parts:
			# try to append nm to current (with separator if needed)
			candidate = nm if not current else current + ', ' + nm
			if first_line:
				# available space on first line accounts for prefix
				if len(prefix) + len(candidate) <= inner_w:
					current = candidate
				else:
					# if current empty, nm itself is too long to fit after prefix; split nm into chunks
					if not current:
						avail = max(1, inner_w - len(prefix))
						for i in range(0, len(nm), avail):
							chunk = nm[i:i+avail]
							lines_content.append(chunk)
						first_line = False
						current = ''
						continue
					else:
						lines_content.append(current)
						first_line = False
						current = nm
			else:
				# subsequent lines have full inner width
				if len(candidate) <= inner_w:
					current = candidate
				else:
					if not current:
						# nm is too long for a single line; break into chunks
						for i in range(0, len(nm), inner_w):
							lines_content.append(nm[i:i+inner_w])
						current = ''
					else:
						lines_content.append(current)
						current = nm

		# append any remaining buffer
		if current:
			lines_content.append(current)

		# render first line with prefix, subsequent lines without
		if lines_content:
			first = lines_content[0]
			lines.append(f"* {(prefix + first).ljust(inner_w)} *")
			for cont in lines_content[1:]:
				lines.append(f"* {cont.ljust(inner_w)} *")
	lines.append(border)
	return lines


def _find_seed_by_name_or_id(value: str) -> Dict[str, Any]:
	if not value:
		return None
	vstr = str(value).lower()
	# search weapons
	for w in (getattr(const_items, 'WEAPON_SEEDS', []) or []):
		if str(w.get('id', '')).lower() == vstr or str(w.get('name', '')).lower() == vstr:
			return w
	# search armor across slots
	for slot, items in (getattr(const_items, 'ARMOR_SEEDS', {}) or {}).items():
		for a in items:
			if str(a.get('id', '')).lower() == vstr or str(a.get('name', '')).lower() == vstr:
				return a
	return None


def attributes_equipment_section(attrs: Dict[str, Any], equipped: Dict[str, str], width: int =60) -> List[str]:
	"""Create a section showing attributes on left and equipment on right in rows.

	Also shows per-stat total bonuses granted by equipped gear (summed).
	"""
	border = _make_border(width)
	lines = [f"*{' Stats & Gear '.center(width-2)}*"]


	# rows: STR/HEAD, DEX/BODY, INT/ARMS, CON/LEGS
	pairs = [
		(f"STR: {attrs.get('strength')}", f"HEAD: {equipped.get('head') or 'None'}"),
		(f"DEX: {attrs.get('dexterity')}", f"BODY: {equipped.get('body') or 'None'}"),
		(f"INT: {attrs.get('intelligence')}", f"ARMS: {equipped.get('arms') or 'None'}"),
		(f"CON: {attrs.get('constitution')}", f"LEGS: {equipped.get('legs') or 'None'}"),
	]
	for left, right in pairs:
		# left area20 chars, right area is the remainder of the inner width
		left_area =20
		right_area = max(0, width -4 - left_area)
		# ensure left side fits fixed area
		ltext = (left[:left_area]).ljust(left_area)
		# truncate right side with ellipsis if it doesn't fit
		if len(right) > right_area:
			if right_area >=3:
				rtrunc = right[: max(0, right_area -3)] + '...'
			else:
				rtrunc = right[: right_area]
		else:
			rtrunc = right
		rtext = rtrunc.rjust(right_area)
		lines.append(f"* {ltext}{rtext} *")
	# add weapon line separately (truncate if necessary)
	weapon = equipped.get('weapon') or 'None'
	wlabel = f"Weapon: {str(weapon)}"
	inner_w = max(0, width -4)
	if len(wlabel) > inner_w:
		if inner_w >=3:
			wlabel = wlabel[: max(0, inner_w -3)] + '...'
		else:
			wlabel = wlabel[:inner_w]
	# center/left justify within inner area
	lines.append(f"* {wlabel.ljust(inner_w)} *")
	return lines + [border]


def abilities_section(abilities: List[PlayerAbility], width: int =60, top_border: bool = True, is_selection_window: bool = False, page_size: int =5, current_page: int =1) -> List[str]:
	"""Render abilities section. If top_border is False, omit the leading border line so
	the caller can insert this block as a dropdown without duplicating the top border.
	"""
	border = _make_border(width)
	lines = [f"*{' Abilities '.center(width-2)}*"]
	if not abilities:
		lines.append(f"* {'None'.ljust(width-4)} *")
	else:
		# pagination when in selection mode
		total = len(abilities)
		if is_selection_window and page_size >0:
			total_pages = (total + page_size -1) // page_size
			if current_page <1:
				current_page =1
			if current_page > total_pages:
				current_page = total_pages
			start = (current_page -1) * page_size
			page_items = abilities[start: start + page_size]
		else:
			page_items = abilities

		for idx, a in enumerate(page_items, start=1):
			# enforce type: callers must provide PlayerAbility instances
			if not isinstance(a, PlayerAbility):
				raise TypeError(f"abilities_section expects PlayerAbility instances; found {type(a)} in page_items")
			lvl = a.level
			name = a.name
			prefix = f"{idx}) " if is_selection_window else "- "
			ln = f"{prefix}{name}{(' (lvl ' + str(lvl) + ')') if lvl else ''}"
			# wrap if needed; allow full width of content area = width-4
			for i in range(0, len(ln), width-4):
				chunk = ln[i:i+width-4]
				lines.append(f"* {chunk.ljust(width-4)} *")
			# Additional info row: effect, status (if any), elements (chars), AP cost
			
			effect_display = ABILTITY_EFFECT_DISPLAY_NAME.get(a.effect.value, str(a.effect.value).capitalize()) if ABILTITY_EFFECT_DISPLAY_NAME else str(a.effect.value)
			extra = ''
			if getattr(a, 'status_keys', None):
				for sk in a.status_keys:
					if extra != '':
						extra += ', '
					extra += ABILITY_STATUS_KEY_DISPLAY_NAMES.get(sk, sk) if ABILITY_STATUS_KEY_DISPLAY_NAMES else sk

			# elements as char sequence
			elems = a.elements or []
			chars = ''.join([ELEMENTAL_CHAR_KEYS.get(e.value, '?') for e in elems]) if elems else 'None'
			info = f"{effect_display}{(' - ' + extra) if extra else ''} {'(aoe)' if a.can_aoe else ''} {chars} AP: {getattr(a, 'ap_cost', '')}"
			for i in range(0, len(info), width-4):
				chunk = info[i:i+width-4]
				lines.append(f"* {chunk.rjust(width-4)} *")

		# page indicator
		if is_selection_window and page_size >0 and total > page_size:
			total_pages = (total + page_size -1) // page_size
			lines.append(f"* {('Page %d/%d' % (current_page, total_pages)).center(width-4)} *")
	out = lines + [border]
	if top_border:
		out = out
	return out


def inventory_section(inventory: List[Item], width: int =60, top_border: bool = True, is_selection_window: bool = False, page_size: int =5, current_page: int =1) -> List[str]:
	"""Render inventory section. If top_border is False, omit the leading border line so the
	caller can insert this block as a dropdown without duplicating the top border.
	"""
	border = _make_border(width)
	lines = [f"*{' Inventory '.center(width-2)}*"]
	if not inventory:
		lines.append(f"* {'Empty'.ljust(width-4)} *")
	else:
		total = len(inventory)
		if is_selection_window and page_size >0:
			total_pages = (total + page_size -1) // page_size
			if current_page <1:
				current_page =1
			if current_page > total_pages:
				current_page = total_pages
			start = (current_page -1) * page_size
			page_items = inventory[start: start + page_size]
		else:
			page_items = inventory

		for idx, it in enumerate(page_items, start=1):
			name = it.name
			eff = it.quantity
			prefix = f"{idx}) " if is_selection_window else "- "
			ln = f"{prefix}{name}{(' (' + str(eff) + ')') if eff else ''}"
			for i in range(0, len(ln), width-4):
				chunk = ln[i:i+width-4]
				lines.append(f"* {chunk.ljust(width-4)} *")

		if is_selection_window and page_size >0 and total > page_size:
			total_pages = (total + page_size -1) // page_size
			lines.append(f"* {('Page %d/%d' % (current_page, total_pages)).center(width-4)} *")
	out = lines + [border]
	if top_border:
		out = out
	return out


def format_player_summary(player: Player, player_game, width: int =60) -> List[str]:
	"""Render a Player object into framed text lines. Expects a proper Player instance."""
	if not isinstance(player, Player):
		raise TypeError('format_player_summary expects a Player instance')
	title = f" {player.name} "
	eff_width = max(width, len(title) +4)
	out: List[str] = []
	out += header_section(player.name, eff_width)
	cur_hp = player.current_hp
	cur_ap = player.current_ap
	out += stats_section(player, eff_width)
	attrs = {
		'strength': f"{player.strength} + {player.get_modified_strength() - player.strength}",
		'dexterity': f"{player.dexterity} + {player.get_modified_dexterity() - player.dexterity}",
		'constitution': f"{player.constitution} + {player.get_modified_constitution() - player.constitution}",
		'intelligence': f"{player.intelligence} + {player.get_modified_intelligence() - player.intelligence}",
	}
	equipped = {
		'weapon': player.equipped_weapon.name if player.equipped_weapon else None,
		'head': player.head_armor.name if player.head_armor else None,
		'body': player.body_armor.name if player.body_armor else None,
		'arms': player.arm_armor.name if player.arm_armor else None,
		'legs': player.leg_armor.name if player.leg_armor else None,
	}
	# build abilities and inventory lists for the formatter
	# enforce PlayerAbility instances: convert from player's stored ids to instances
	abilities = player.abilities
	# show only utility items in the player inventory in this view
	inventory = [it for it in player_game.inventory if isinstance(it, UtilityItem)]
	out += attributes_equipment_section(attrs, equipped, eff_width)
	out += abilities_section(abilities, eff_width)
	out += inventory_section(inventory, eff_width)
	return out

def unused_awards_section(player: Player, width: int =60) -> List[str]:
	unused_power_points = player.unused_power_points
	unused_ability_slots = player.unused_ability_slots
	unused_stat_points = player.unused_stat_points
	border = _make_border(width)
	lines = [f"*{' Unused Awards '.center(width-2)}*"]
	if unused_power_points <=0 and unused_ability_slots <=0 and unused_stat_points <=0:
		lines.append(f"* {'None'.ljust(width-4)} *")
	else:
		# display in single line : Pow: X | Stat: Y | Abil: Z
		parts = []
		if unused_power_points >0:
			parts.append(f"Pow: {unused_power_points}")
		if unused_stat_points >0:
			parts.append(f"Stat: {unused_stat_points}")
		if unused_ability_slots >0:
			parts.append(f"Abil: {unused_ability_slots}")
		line = ' | '.join(parts)
		lines.append(f"* {line.ljust(width-4)} *")
	return lines + [border]

def format_player_sections(player: Player, player_game, width: int =60, is_selection_window: bool = False, page_size: int =5, current_page: int =1) -> Dict[str, List[str]]:
	if not isinstance(player, Player):
		raise TypeError('format_player_sections expects a Player instance')
	title = f" {player.name} - Level {player.level} "
	eff_width = max(width, len(title) +4)
	cur_hp = player.current_hp
	cur_ap = player.current_ap
	attrs = {
		'strength': f"{player.strength} + {player.get_modified_strength() - player.strength}",
		'dexterity': f"{player.dexterity} + {player.get_modified_dexterity() - player.dexterity}",
		'constitution': f"{player.constitution} + {player.get_modified_constitution() - player.constitution}",
		'intelligence': f"{player.intelligence} + {player.get_modified_intelligence() - player.intelligence}",
	}
	equipped = {
		'weapon': player.equipped_weapon.name if player.equipped_weapon else None,
		'head': player.head_armor.name if player.head_armor else None,
		'body': player.body_armor.name if player.body_armor else None,
		'arms': player.arm_armor.name if player.arm_armor else None,
		'legs': player.leg_armor.name if player.leg_armor else None,
	}
	abilities = player.abilities
	# show only utility items in the player inventory in this view
	inventory = [it for it in player_game.inventory if isinstance(it, UtilityItem)]
	#input(f"DEBUG: player abilities raw: {abilities}")
	return {
		'header': header_section(player.name, eff_width),
		'stats': stats_section(player, eff_width),
		'attributes_equipment': attributes_equipment_section(attrs, equipped, eff_width),
		'abilities': abilities_section(abilities, eff_width, True, is_selection_window, page_size, current_page),
		'inventory': inventory_section(inventory, eff_width, True, is_selection_window, page_size, current_page),
		'unused_awards': unused_awards_section(player, eff_width)
	}


def highlight_box(lines: List[str]) -> List[str]:
	"""Replace leading/trailing '*' with '#' to indicate active/highlighted box."""
	out: List[str] = []
	for ln in lines:
		if not ln:
			out.append(ln)
			continue
		first = ln[0]
		last = ln[-1]
		if first == '*':
			ln = '#' + ln[1:]
		if last == '*':
			ln = ln[:-1] + '#'
		out.append(ln)
	return out
