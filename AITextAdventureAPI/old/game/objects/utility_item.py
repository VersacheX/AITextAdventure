from dataclasses import dataclass
from typing import Optional, Dict, Any
from .item import Item


@dataclass
class UtilityItem(Item):
	"""Utility items like potions, keys, crafting components."""
	# effect can be any callable or descriptor in a real game; keep generic here
	effect: Optional[str] = None

	def is_healing_item(self) -> bool:
		"""Return True if this item is a healing item."""
		return self.effect in ('heal_small', 'heal_mid', 'heal_large', 'heal_full')

	def apply(self, user) -> dict:
		"""Apply the item's effect to `user` (Player). Returns a dict describing outcome.

		This consumes one use. The dict may contain keys like 'used', 'healed', 'ap_restored',
		'stat', 'amount', or 'note'."""
		res = {'used': True }

		eff = self.effect
		# HP heals
		if eff in ('heal_small', 'heal_mid', 'heal_large', 'heal_full'):
			# only heal living targets
			if not user.is_alive():
				res['used'] = False
				res['note'] = 'target is dead'
				return res
			hf = getattr(self, 'heal_fraction', None)
			if hf is not None:
				amt = max(self.value, int(user.max_hp * float(hf)))
			else:
				# fallbacks
				if eff == 'heal_small':
					amt = max(self.value, int(user.max_hp *0.25))
				elif eff == 'heal_mid':
					amt = max(self.value, int(user.max_hp *0.5))
				elif eff == 'heal_large':
					amt = max(self.value, int(user.max_hp *0.75))
				else:
					amt = user.max_hp
			res['healed'] = user.heal(amt)
			res['note'] = f'healing {res["healed"]} HP'
			return res

		# AP restores
		if eff in ('restore_ap_small', 'restore_ap_mid', 'restore_ap_large', 'restore_ap_full'):
			# only restore AP for living targets
			if not user.is_alive():
				res['used'] = False
				res['note'] = 'target is dead'
				return res
			af = getattr(self, 'ap_fraction', None)
			if af is not None:
				amt = max(self.value, int(user.max_ap * float(af)))
			else:
				amt = max(self.value, int(user.max_ap *0.25))
			user.current_ap = min(user.max_ap, user.current_ap + amt)
			res['ap_restored'] = amt
			res['note'] = f'restoring {amt} AP'
			return res

		# stat increase (permanent)
		if eff == 'stat_increase':
			if not user.is_alive():
				res['used'] = False
				res['note'] = 'target is dead'
				return res

			stat = getattr(self, 'stat', None)
			amount = int(getattr(self, 'amount',1))
			if stat in ('max_hp', 'max_ap'):
				if stat == 'max_hp':
					user.max_hp += amount
					user.current_hp += amount
				else:
					user.max_ap += amount
					user.current_ap += amount
				res['stat'] = stat
				res['amount'] = amount
				res['note'] = f'increasing {stat} by {amount}'
				return res
			elif stat in ('strength', 'dexterity', 'intelligence', 'constitution'):
				#def allocate_stats(self, str_inc: int =0, dex_inc: int =0, con_inc: int =0, int_inc: int =0) -> None:
				str_inc = amount if stat == 'strength' else 0
				dex_inc = amount if stat == 'dexterity' else 0
				int_inc = amount if stat == 'intelligence' else 0
				con_inc = amount if stat == 'constitution' else 0
				user.allocate_stats(str_inc=str_inc, dex_inc=dex_inc, con_inc=con_inc, int_inc=int_inc, use_stat_points=False)
				res['stat'] = stat
				res['amount'] = amount
				res['note'] = f'increasing {stat} by {amount}'
				return res

		# revive effect
		if eff == 'revive':
			# only revive if target is not alive
			if user.is_alive():
				res['used'] = False
				res['note'] = 'target still alive'
				return res
			
			# revive a fallen ally (user) to a fraction of max_hp or at least `value`
			rf = getattr(self, 'revive_fraction', None)
			if rf is None:
				rf = 0.5
			amt = max(self.value, int(getattr(user, 'max_hp', 0) * float(rf)))

			# bring to life by healing from 0
			res['healed'] = user.heal(amt)
			res['note'] = f'revived with {res["healed"]} HP'
			return res

		# other effects (placeholders)
		if eff == 'open_lock':
			res['note'] = 'open_lock'
			return res

		if eff in ('cure_petrify', 'cure_sleep', 'cure_stun', 'cure_confuse', 'cure_silence', 'cure_continuous_damage'):
			removed_count = user.remove_status_by_id(eff.replace('cure_',''))
			res['note'] = f'curing {removed_count} debuffs'
			return res
		elif eff == 'cure_all_debuffs':
			removed_count = user.cure_all_debuffs()
			res['note'] = f'curing {removed_count} debuffs'
			return res

		# default
		res['note'] = 'used'
		return res


def _instantiate_utility(seed: Dict[str, Any]) -> UtilityItem:
    ui = UtilityItem(
        id=seed.get('id'),
        name=seed.get('name'),
        description=seed.get('description', ''),
        effect=seed.get('effect'),
        #uses=seed.get('uses',1),
        value=seed.get('value',0),
        min_spawn_level=seed.get('min_spawn_level',1),
    )
    # copy optional metadata
    if 'heal_fraction' in seed:
        setattr(ui, 'heal_fraction', seed.get('heal_fraction'))
    if 'ap_fraction' in seed:
        setattr(ui, 'ap_fraction', seed.get('ap_fraction'))
    if 'stat' in seed:
        setattr(ui, 'stat', seed.get('stat'))
    if 'amount' in seed:
        setattr(ui, 'amount', seed.get('amount'))
    if 'revive_fraction' in seed:
        setattr(ui, 'revive_fraction', seed.get('revive_fraction'))
    return ui
