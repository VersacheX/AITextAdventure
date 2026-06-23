from typing import List, Dict, Any
from game.objects.random_hostile import RandomHostile
from game.constants_other import ELEMENTAL_CHAR_KEYS


def _make_border(width: int) -> str:
    return '*' * width


def header_section(name: str, level: int, width: int =60, align_right: bool = False) -> List[str]:
    title = f" {name} - Level {level} "
    if len(title) +4 > width:
        width = len(title) +4
    border = _make_border(width)
    if not align_right:
        return [border, f"*{title.center(width-2)}*", border]
    # align_right: produce a right-justified title line with left filler dashes
    # build a line of form '*'+ left_filler + title.rjust(width-2 - len(left_filler)) + '*'
    # choose left_filler width to leave room; use half of available space or a fixed filler
    filler = '-' * max(1, (width -2 - len(title)))
    # ensure total length width-2
    content = (filler + title).rjust(width-2)
    return [border, f"*{content}*", border]


def stats_section(hostile: RandomHostile, width: int =60, align_right: bool = False) -> List[str]:
    """Render stats with lists for left/right so callers can append them.

    Left contains HP/AP lines, right contains Level/Status lines. Compose each
    pair into a single framed line when space allows; otherwise split into
    separate lines to avoid overflow.
    """
    border = _make_border(width)

    left = [
        f"HP {hostile.current_hp}/{int(hostile.max_hp)}",
        f"AP {hostile.current_ap}/{int(hostile.max_ap)}",
    ]
    right = [
        f"Rarity: {hostile.rarity}",
        f"Level {hostile.level}"        
    ]
    if len(hostile.statuses) >0:
        # format statuses to include mapped elemental chars when present
        parts: List[str] = []
        for s in hostile.statuses:
            name = s.get('name')
            elems = s.get('elements')
            if elems:
                chars = ''.join([ELEMENTAL_CHAR_KEYS.get(str(e)) for e in elems])
                parts.append(f"{name} {chars}")
            else:
                parts.append(name)
        status_string = ', '.join(parts)
        left.append('Status: ' + status_string )

    content_w = max(0, width -4)
    lines: List[str] = []

    rows = max(len(left), len(right))
    for i in range(rows):
        l = left[i] if i < len(left) else ''
        r = right[i] if i < len(right) else ''
        space = content_w - len(l) - len(r)
        if align_right:
            content = f"{l} {r}".rjust(content_w)
            lines.append(f"* {content} *")
        elif space >=1:
            lines.append(f"* {l}{' ' * space}{r} *")
        else:
            # not enough room: emit left on its own line, then right on its own line
            if l:
                lines.append(f"* {l.ljust(content_w)} *")
            if r:
                lines.append(f"* {r.ljust(content_w)} *")

    return lines + [border]


def attributes_section(hostile: RandomHostile, width: int =60) -> List[str]:
    """Show main stats and a short ability list on the right."""
    border = _make_border(width)
    header = f"*{' Hostile Stats '.center(width-2)}*"
    # left side: STR, DEX, INT, CON (raw text lines)
    raw = [
        f"STR: {hostile.strength} DEX: {hostile.dexterity} INT: {hostile.intelligence} CON: {hostile.constitution}"
    ]
    lines: List[str] = [header]
    # create framed lines right-aligned into the content width
    content_w = width -2
    for item in raw:
        content = f"{item}".rjust(content_w)
        lines.append(f"*{content}*")

    return lines + [border]


def abilities_section(hostile: RandomHostile, width: int =60, top_border: bool = True, align_right: bool = False) -> List[str]:
    """Render abilities section; if top_border is False the leading border is omitted so
    the caller can embed this block as a dropdown under an existing border.
    """
    border = _make_border(width)
    lines = [f"*{' Abilities '.center(width-2)}*"]
    if not hostile.abilities:
        lines.append(f"* {'None'.ljust(width-4)} *")
    else:
        for a in hostile.abilities:
            name = a.name
            ln = f"- {name} lvl {a.level}"
            for i in range(0, len(ln), width-4):
                chunk = ln[i:i+width-4]
                if align_right:
                    # right align ability entries
                    content = chunk.rjust(width-4)
                    lines.append(f"* {content} *")
                else:
                    lines.append(f"* {chunk.ljust(width-4)} *")
    out = lines + [border]
    return out

def format_hostile_summary_compact(hostile: RandomHostile, width: int =60, align_right: bool = False) -> List[str]:
    """Compact hostile summary: header, stats, and a condensed attributes/abilities block.

    Layout (example):
     border
     * STR: X DEX: Y *
     * INT: A CON: B *
     * Abilities: <list wrapped> *
     border
    """
    name = hostile.name
    level = hostile.level
    max_hp = hostile.max_hp
    max_ap = hostile.max_ap
    stats = {
        'strength': hostile.strength,
        'dexterity': hostile.dexterity,
        'constitution': hostile.constitution,
        'intelligence': hostile.intelligence
    }

    out: List[str] = []
    # header + stats reuse existing formatters for consistency
    out += header_section(name, level, width, align_right=align_right)
    out += stats_section(hostile, width, align_right=align_right)

    # compact attributes block
    border = _make_border(width)
    content_w = max(0, width -4)
    half = content_w //2

    # build single-line: STR / DEX / INT / CON across the content width
    s_str = f"STR: {hostile.strength}"
    s_dex = f"DEX: {hostile.dexterity}"
    s_int = f"INT: {hostile.intelligence}"
    s_con = f"CON: {hostile.constitution}"
    parts = [s_str, s_dex, s_int, s_con]

    # Ensure total fits: iterative truncate longest part until it fits with minimum1-space separators
    def total_len(pieces):
        return sum(len(p) for p in pieces) + (len(pieces) -1)

    # If necessary, truncate the longest piece until it fits
    while total_len(parts) > content_w and any(len(p) >1 for p in parts):
        # find index of longest piece
        idx = max(range(len(parts)), key=lambda i: len(parts[i]))
        if len(parts[idx]) >1:
            parts[idx] = parts[idx][:-1]
        else:
            break

    # distribute spacing (at least one space between parts), spread remaining evenly
    remaining_after_min = content_w - sum(len(p) for p in parts) - (len(parts) -1)
    extra_per_gap =0
    extra_leftover =0
    gaps = max(1, len(parts) -1)
    if remaining_after_min >0:
        extra_per_gap = remaining_after_min // gaps
        extra_leftover = remaining_after_min % gaps

    sep_counts = []
    for i in range(len(parts) -1):
        cnt =1 + extra_per_gap + (1 if i < extra_leftover else 0)
        sep_counts.append(cnt)

    # build content string
    content_chunks: List[str] = []
    for i, p in enumerate(parts):
        content_chunks.append(p)
        if i < len(sep_counts):
            content_chunks.append(' ' * sep_counts[i])
    content = ''.join(content_chunks)
    # pad to full width
    content = content.ljust(content_w)[:content_w]
    line1 = f"* {content} *"

    # abilities header and list (wrapped)
    ab_header = "Abilities:"
    ab_lines: List[str] = []
    if not hostile.abilities:
        ab_lines.append(f"* { 'None'.ljust(content_w) } *")
    else:
        # join ability entries into wrapped lines
        for a in hostile.abilities:
            name = a.name
            lvl = a.level
            entry = f"- {name}{(' (lvl ' + str(lvl) + ')') if lvl else ''}"
            # wrap entry into chunks of content_w
            for i in range(0, len(entry), content_w):
                chunk = entry[i:i+content_w]
                ab_lines.append(f"* {chunk.ljust(content_w)} *")

    #out.append(border)
    out.append(line1)
    out.append(f"* {ab_header.ljust(content_w)} *")
    out.extend(ab_lines)
    out.append(border)

    return out

def format_hostile_summary_full(hostile: RandomHostile, width: int =60) -> List[str]:
	"""
	Produce a full, multi-section framed summary of a RandomHostile.

	Sections (in order):
	- header (name/level)
	- stats (hp/ap, rarity, level info)
	- attributes (STR/DEX/INT/CON)
	- abilities (detailed list)
	- extended info (drops, money, type, defense, elements, attacks, base xp)

	Returns a list of strings where each string is a framed line (including
	leading/trailing '*' border characters). Width controls the total frame
	width.
	"""

	name = hostile.name
	level = hostile.level

	out: List[str] = []
	# header and core stats
	out += header_section(name, level, width)
	out += stats_section(hostile, width)

	out += attributes_section(hostile, width)
	
	# render abilities block (manual to avoid relying on abilities_section signature)
	border = _make_border(width)
	out.append(border)
	out.append(f"*{' Abilities '.center(width-2)}*")
	content_w = max(0, width -4)
	if not hostile.abilities:
		out.append(f"* {'None'.ljust(content_w)} *")
	else:
		for a in hostile.abilities:
			entry = f"- {a.name} lvl {a.level}"
			for i in range(0, len(entry), content_w):
				chunk = entry[i:i+content_w]
				out.append(f"* {chunk.ljust(content_w)} *")
	out.append(border)

	# Extended information
	border = _make_border(width)
	content_w = max(0, width -4)
	# build paired rows for a two-column layout
	pairs = []

	# Drops (use safe name extraction)
	common_drop = hostile.common_drop
	rare_drop = hostile.rare_drop
	cd_name = common_drop.name if common_drop is not None else 'None'
	rd_name = rare_drop.name if rare_drop is not None else 'None'

	pairs.append((f"Common Drop", cd_name))
	pairs.append((f"Rare Drop", rd_name))

	# Money / Type
	money_range = hostile.money_range
	pairs.append(("Money", str(money_range if money_range is not None else 'None')))
	pairs.append(("Type", str(hostile.hostile_type)))

	# Defense / Base XP
	pairs.append(("Defense", str(hostile.defense)))
	pairs.append(("Base XP", str(hostile.base_xp)))

	# format pairs into two-column framed lines
	out.append(border)
	out.append(f"*{' Extended Info '.center(width-2)}*")
	if content_w <=0:
		# nothing fits; just print border and return
		out.append(border)
	else:
		half = content_w //2
		for i in range(0, len(pairs),2):
			left = pairs[i]
			right = pairs[i+1] if i+1 < len(pairs) else ("", "")
			left_txt = f"{left[0]}: {left[1]}"
			right_txt = f"{right[0]}: {right[1]}" if right[0] else ""
			# truncate each side to its column width
			lpart = left_txt[:half].ljust(half)
			rpart = right_txt[:content_w - half].ljust(content_w - half)
			out.append(f"* {lpart}{rpart} *")
	out.append(border)

	return out


def format_hostile_summary(hostile: RandomHostile, width: int =50, align_right: bool = False) -> List[str]:
    """Return lines for a single RandomHostile object.

    This function requires a proper RandomHostile instance and will raise
    TypeError if given anything else.
    """
    if not isinstance(hostile, RandomHostile):
        raise TypeError('format_hostile_summary expects a RandomHostile instance')

    name = hostile.name
    level = hostile.level

    out: List[str] = []
    out += header_section(name, level, width, align_right=align_right)
    out += stats_section(hostile, align_right=align_right)
    out += attributes_section(hostile)
    out += abilities_section(hostile, width, align_right=align_right)
    return out


def format_hostile_sections(hostile: RandomHostile, width: int =50) -> Dict[str, List[str]]:
    """Return individual sections for a RandomHostile object."""

    name = hostile.name
    level = hostile.level
    max_hp = hostile.max_hp
    max_ap = hostile.max_ap

    return {
        'header': header_section(name, level, width),
        'stats': stats_section(hostile),
        'attributes': attributes_section(hostile),
        'abilities': abilities_section(hostile.abilities, width),
    }


def highlight_box(lines: List[str]) -> List[str]:
    """Replace leading/trailing '*' with '#' to indicate an active/highlighted box."""
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
