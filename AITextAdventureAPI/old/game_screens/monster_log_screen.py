from typing import List, Optional
import readchar
from game.objects.random_hostile import RandomHostile
from combat_balancing_simulation.hostile_details_screen import format_hostile_summary_full


class MonsterLogScreen:
	"""Overlay that displays monsters the player has slain.

	Expects a pre-built list of RandomHostile instances and an accompanying
	map of counts (id -> slain count). Shows a detailed summary for the
	currently selected hostile above the list.
	"""

	def __init__(self, hostiles: List[RandomHostile], slain_counts: dict, width: int =80, height: int =16):
		self.hostiles = hostiles or []
		self.slain_counts = slain_counts or {}
		self.width = width
		self.height = max(6, int(height))
		self.selected_index =0

	def render_overlay(self, term_w: int, term_h: int, selected_player=None) -> List[str]:
		box_w = min(self.width, max(40, term_w -10))
		box_h = min(self.height, max(6, term_h -4))
		left = (term_w - box_w) //2
		inner_w = box_w -2

		lines: List[str] = []
		# top border and title
		lines.append(' ' * left + '*' * box_w)
		title = f" Monster Log ({len(self.hostiles)} entries) - esc:close"
		lines.append(' ' * left + '*' + title.center(inner_w)[:inner_w] + '*')
		lines.append(' ' * left + '*' + ' ' * inner_w + '*')

		# Selected hostile summary (if available)
		sel = max(0, min(self.selected_index, max(0, len(self.hostiles) -1)))
		sel_hostile = self.hostiles[sel] if self.hostiles else None
		summary_lines: List[str] = []
		if sel_hostile is not None:
			# reuse existing formatter to build a framed summary block
			summary_lines = format_hostile_summary_full(sel_hostile, width=box_w)

		# append summary lines into our boxed overlay (no truncation; summary sits above list)
		for s in summary_lines:
			lines.append(' ' * left + s.ljust(box_w)[:box_w])

		# spacer between summary and list
		lines.append(' ' * left + '*' + ' ' * inner_w + '*')

		# Now render the list region — its height is controlled by box_h.
		# We'll create a boxed list with its own top/bottom borders and a fixed
		# number of inner rows = max(1, box_h -2).
		list_inner_rows = max(1, box_h -2)
		# top border for the list area
		lines.append(' ' * left + '*' * box_w)

		# determine which entries fit into the fixed list_inner_rows
		start = max(0, min(self.selected_index, max(0, len(self.hostiles) - list_inner_rows)))
		shown = self.hostiles[start:start + list_inner_rows]

		for i, h in enumerate(shown, start=start):
			count = self.slain_counts.get(getattr(h, 'id', None),0)
			name = h.name
			lvl = h.level
			prefix = '>' if i == self.selected_index else ' '
			line = f" {prefix} {name} (lvl {lvl})  x{count}"
			lines.append(' ' * left + '*' + line.ljust(inner_w)[:inner_w] + '*')

		# fill remaining inner rows if any
		remaining = list_inner_rows - len(shown)
		for _ in range(remaining):
			lines.append(' ' * left + '*' + ' ' * inner_w + '*')

		# bottom border for the list area
		lines.append(' ' * left + '*' * box_w)

		# pad/truncate to term_w
		padded: List[str] = []
		for ln in lines:
			if len(ln) < term_w:
				padded.append(ln + ' ' * (term_w - len(ln)))
			else:
				padded.append(ln[:term_w])
		return padded

	def handle_key(self, ch: str, selected_player: Optional[object] = None):
		def _is_up(k: str) -> bool:
			return k == getattr(readchar.key, 'UP', None) or k in ('\x1b[A', '\x1bOA', '\x00H', '\xe0H')

		def _is_down(k: str) -> bool:
			return k == getattr(readchar.key, 'DOWN', None) or k in ('\x1b[B', '\x1bOB', '\x00P', '\xe0P')

		def _is_esc(k: str) -> bool:
			return k == getattr(readchar.key, 'ESC', None) or k == '\x1b'

		if _is_esc(ch):
			return {'handled': True, 'close': True}

		if _is_up(ch):
			if self.selected_index >0:
				self.selected_index -=1
			return {'handled': True, 'close': False}

		if _is_down(ch):
			if self.selected_index < max(0, len(self.hostiles) -1):
				self.selected_index +=1
			return {'handled': True, 'close': False}

		return {'handled': False}
