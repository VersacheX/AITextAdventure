from typing import List, Dict, Any, Optional, Tuple
import math

# reuse existing formatters
from combat_balancing_simulation.player_details_screen import format_player_summary
from combat_balancing_simulation.hostile_details_screen import format_hostile_summary
from game.objects.random_hostile import RandomHostile
from game.objects.player_game import PlayerGame
from game.objects.player import Player
from game.objects.player_ability import PlayerAbility
import game.status_utils as status_utils
import game.constants_other as const_other
from combat_balancing_simulation.hostile_ai_service import decide_action
import random

class Unit:
    """Minimal simulation wrapper linking to a typed game object.

    Responsibilities:
    - hold reference to the typed entity (Player or RandomHostile)
    - track scheduling state (`next_action_at`)
    - provide small helpers that delegate to the underlying object
    """
    def __init__(self, entity: object):
        self.entity = entity

        # countdown until next action (seconds/ticks). Simulation will decrement this value.
        self.next_action_in: float = 0.0

    def _is_player(self) -> bool:
        return isinstance(self.entity, Player)

    def is_alive(self) -> bool:
        # prefer object's own method
        return bool(self.entity.is_alive())

    def compute_action_delay(self) -> float:
        # derive dex value from entity; be strict about presence but fall back safely
        dex = self.entity.get_modified_dexterity()
        base = 10.0
        delay = base / (1.0 + (dex / 60.0))
        return max(1.0, delay)

    def schedule_first_action(self, current_time: float) -> None:
        # set relative delay until first action
        self.next_action_in = self.compute_action_delay()

    def advance_schedule(self) -> None:
        # reset timer after taking an action
        self.next_action_in = self.compute_action_delay()


class CombatSimulation:
    def __init__(self, player_game: PlayerGame, hostiles: List[RandomHostile]):
        """Create simulation from a PlayerGame (contains Player objects) and
        a list of RandomHostile objects.

        This initializer strictly expects typed objects and will raise if the
        expected collections are not present on player_game or hostiles.
        """
        self.time =0.0
        self.units: List[Unit] = []
        # keep player_game reference for reward distribution
        self.player_game = player_game

        for p in player_game.get_active_party():
            # p is expected to be a Player instance
            self.units.append(Unit(p))

        # Hostiles is expected to be a list of RandomHostile instances
        for h in hostiles:
            self.units.append(Unit(h))

        # initialize schedules
        for u in self.units:
            u.schedule_first_action(self.time)
    
    def is_player_annhilation(self) -> bool:
        """Return True if all player units are dead."""
        # Consider a player effectively alive if they are alive and not petrified.
        for u in self.units:
            if not u._is_player():
                continue
            if not u.is_alive():
                continue
            ent = u.entity
            statuses = ent.statuses
            # if any player is alive and not petrified, return True (players remain)
            petrified = any((s.get('id') == 'petrify') for s in statuses if isinstance(s, dict))
            if not petrified:
                return True
        return False

    def is_hostile_annhilation(self) -> bool:
        """Return True if at least one hostile unit is alive and not petrified.

        Mirrors the player-side check: a hostile that is alive but petrified does not
        count as active. Returns True if any hostile is alive and not petrified.
        """
        for u in self.units:
            if u._is_player():
                continue

            if not u.is_alive():
                continue
            ent = getattr(u, 'entity', None)
            statuses = getattr(ent, 'statuses', []) or []
            
            petrified = any((s.get('id') == 'petrify') for s in statuses if isinstance(s, dict))
            if not petrified:
                return True
        return False

    def next_active_unit(self) -> Optional[Unit]:
        # remove dead units
        alive_units = [u for u in self.units if u.is_alive()]
        if not alive_units:
            return None
        # find smallest countdown
        min_tick = min(u.next_action_in for u in alive_units)
        # advance global time and decrement all timers by min_tick
        self.time += float(min_tick)
        for u in alive_units:
            u.next_action_in = max(0.0, u.next_action_in - min_tick)
        # return first unit whose timer reached zero
        ready = [u for u in alive_units if u.next_action_in <= 0.0]
        return ready[0] if ready else None

    def perform_unit_action(self, unit: Unit, action: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        """Dispatch a unit action and return a result dict containing
        ordered textual messages (no printing) and structured fields.

        The returned dict will include at least 'actor_name', 'action_type' and
        'messages' (List[str]). Other keys such as 'target_name'/'damage'/'
        'action_result' may be present depending on the action.
        """
        if not unit.is_alive():
            actor_name = getattr(unit.entity, 'name', 'unit')
            return {'actor_name': actor_name, 'action_type': 'none', 'messages': [f"{actor_name} is dead."], 'note': 'dead'}

        actor = unit.entity
        # enemies/allies determined by whether the unit is a player or not
        enemies = [u for u in self.units if u._is_player() != unit._is_player() and u.is_alive()]
        allies = [u for u in self.units if u._is_player() == unit._is_player() and u.is_alive()]
        atype = (action or {}).get('type') if action else 'auto'

        result: Dict[str, Any] = {'actor_name': actor.name, 'action_type': atype, 'messages': []}

        # note to later add multitarget/area effects handling
        # resolve explicit target if supplied in action (index into enemies or name)
        target_units: List[Optional[Unit]] = action.get('targets')

        # Special-case: allow auto-skip (used when unit is blocked by a status)
        if atype == 'auto_skip':
            bs = status_utils.get_blocking_status(actor)
            disp = None
            if bs:
                disp = const_other.ABILITY_STATUS_KEY_DISPLAY_NAMES.get(bs.get('id'), bs.get('id'))
            msg = f"{actor.name} is {disp or 'unable to act'} and skips their turn."
            result['messages'].append(msg)
            # tick statuses and apply continuous damage at end of skipped turn
                        
            actor.tick_statuses()

            cd = status_utils.apply_continuous_damage(actor)
            if cd and cd.get('applied'):
                result['messages'].append(f"{actor.name} suffers {cd.get('applied')} continuous damage.")

            rg = status_utils.apply_regen(actor)
            if rg and rg.get('restored'):
                result['messages'].append(f"{actor.name} regenerates {rg.get('restored')} HP.")

            unit.advance_schedule()
            return result

        # Special-case: confused units delegate decision to AI engine and execute
        if atype == 'confused':
            msgs: List[str] = result['messages']
            # prepare entity lists for AI
            enemy_entities = [u.entity for u in enemies]
            ally_entities = [u.entity for u in allies]
            # ask AI for a chaotic decision
            decision = decide_action(actor, enemies=enemy_entities, allies=ally_entities)
            if not decision:
                msgs.append(f"{actor.name} is confused and does nothing.")
                unit.advance_schedule()
                return result

            # Map decision targets (entities) back to Unit wrappers when needed
            dec_targets = decision.get('targets') or []
            target_units: List[Optional[Unit]] = []
            for dt in dec_targets:
                found = next((u for u in self.units if u.entity._uuid == dt._uuid))
                target_units.append(found)

            # If AI chose an ability, attempt to use it
            if decision.get('type') == 'ability' and decision.get('ability'):
                abil = decision.get('ability')
                # targets for use_ability should be entity objects
                res = actor.use_ability(abil, targets=dec_targets)
                result['action_result'] = res
                # human-readable messages from ability result
                if isinstance(res, dict) and isinstance(res.get('results'), list):
                    msgs.append(f"{actor.name} (confused) uses {getattr(abil, 'name', getattr(abil, 'id', 'ability'))}.")
                    for rr in res.get('results'):
                        if rr and rr.get('action'):
                            msgs.append(rr.get('action'))
                        else:
                            msgs.append(str(rr))
                else:
                    msgs.append(f"{actor.name} (confused) tried to use an ability but it failed.")
                # advance schedule and return
                unit.advance_schedule()
                return result

            # perform a single-target attack against chosen target
            if decision.get('type') == 'attack':
                tgt_unit = target_units[0] if target_units else None
                tgt_ent = getattr(tgt_unit, 'entity', None) if tgt_unit is not None else (dec_targets[0] if dec_targets else None)
                # If actor is a Player (player.attack expects single target)
                if unit._is_player():
                    attack_res = actor.attack(tgt_ent)
                else:
                    # Hostile: delegate to RandomHostile.perform_basic_attack if available
                    attack_res = actor.perform_basic_attack(tgt_ent)                    

                result['action_result'] = attack_res
                if not attack_res:
                    msgs.append(f"{actor.name} (confused) fails to act.")
                else:
                    if not attack_res.get('hit'):
                        msgs.append(f"{actor.name} (confused) attacks {getattr(tgt_ent, 'name', 'target')} but misses.")
                    else:
                        dmg = attack_res.get('applied', attack_res.get('damage',0))
                        msgs.append(f"{actor.name} (confused) hits {getattr(tgt_ent, 'name', 'target')} for {dmg} damage.")
                unit.advance_schedule()
                return result

        # Player-controlled actions
        if unit._is_player():
            if atype in ('attack', 'auto'):
                target = target_units[0]
                res = self._player_attack(unit, target)
                result.update(res)
            elif atype == 'ability':
                abil = (action or {}).get('ability')
                res = self._player_use_ability(unit, abil, enemies, allies, target_units)
                result.update(res)
            elif atype == 'item':
                itm = (action or {}).get('item')
                res = self._player_use_item(unit, itm, enemies, allies, target_units[0])
                result.update(res)
            #need to add escape action later
            elif atype == 'pass':
                result['messages'].append('You pass your turn.')
            else:
                result['messages'].append('Unknown action.')

            # advance player schedule after performing action
            # tick statuses and apply continuous damage at end of turn
            actor.tick_statuses()

            cd = status_utils.apply_continuous_damage(actor)
            if cd and cd.get('applied'):
                result['messages'].append(f"{actor.name} suffers {cd.get('applied')} continuous damage.")

            rg = status_utils.apply_regen(actor)
            if rg and rg.get('restored'):
                result['messages'].append(f"{actor.name} regenerates {rg.get('restored')} HP.")
            unit.advance_schedule()
            return result

        # Hostile AI actions
        else:
            # perform hostile action against first enemy (usually player)
            res = self._perform_hostile_action(unit, enemies, allies) # Note: add hostile targeting services later
            result.update(res)
            # tick statuses and apply continuous damage at end of hostile turn
            actor.tick_statuses()

            cd = status_utils.apply_continuous_damage(actor)
            if cd and cd.get('applied'):
                result['messages'].append(f"{actor.name} suffers {cd.get('applied')} continuous damage.")

            rg = status_utils.apply_regen(actor)
            if rg and rg.get('restored'):
                result['messages'].append(f"{actor.name} regenerates {rg.get('restored')} HP.")
            # advance schedule here for hostiles as well
            unit.advance_schedule()
            return result

    # --- Player action implementations (collect messages instead of printing) ---
    def _player_attack(self, unit: Unit, target_unit: Optional[Unit]) -> Dict[str, Any]:
        actor = unit.entity
        msgs: List[str] = []
        out: Dict[str, Any] = {'messages': msgs, 'action_type': 'attack'}

        if target_unit is None:
            msgs.append('No targets available.')
            out['note'] = 'no_target'
            return out

        hostile = target_unit.entity
        # Use actor.attack if available
        attack_res = actor.attack(hostile)
        
        out['action_result'] = attack_res

        if not attack_res.get('hit'):
            msgs.append(f"{actor.name} attacks with {attack_res.get('weapon')} but miss.")
        else:
            dmg = attack_res.get('applied', attack_res.get('damage', 0))
            msg = f"{actor.name} hit the {hostile.name} for {dmg} damage."
            if attack_res.get('crit'):
                msg += ' (critical)'
            msgs.append(msg)

        # armor broken handling
        if attack_res.get('armor_broken'):
            for aname in attack_res.get('armor_broken', []):
                msgs.append(f"{hostile.name}'s {aname} breaks and falls off!")
            hostile.armor = [aa for aa in hostile.armor if aa.name not in attack_res.get('armor_broken', [])]

        return out

    def _player_use_ability(self, unit: Unit, ability: PlayerAbility, enemies: List[Unit], allies: List[Unit], target_units: List[Optional[Unit]] = None) -> Dict[str, Any]:
        actor = unit.entity
        msgs: List[str] = []
        out: Dict[str, Any] = {'messages': msgs, 'action_type': 'ability', 'ability': ability.id}

        # get target entities is target_units.entity
        target_entities = []
        if target_units:
            for tu in target_units:
                if tu is not None:
                    target_entities.append(tu.entity)
        
        res = actor.use_ability(ability, target=None, targets=target_entities)

        out['action_result'] = res

        # WEIRD ERROR HANDLING SHIT I DONT UNDERSTAND YET, BUT WILL CLEAN UP
        # Strict message handling: use the actor/ability-provided human readable text.
        # Expect either a single 'action' string on the result or a 'results' list
        # where each entry contains an 'action' string. If the expected fields are
        # not present, surface an error instead of synthesizing messages.
        if isinstance(res, dict) and isinstance(res.get('results'), list):
            for idx, r in enumerate(res.get('results') or []):
                if r is None:
                    msgs.append(f"Invalid ability result at index {idx}: missing entry.")
                    out['note'] = 'invalid_result'
                    return out
                action_text = r.get('action') if isinstance(r, dict) else None
                if not action_text:
                    msgs.append(f"Invalid ability result at index {idx}: missing 'action' text.")
                    out['note'] = 'invalid_result'
                    return out
                msgs.append(str(action_text))
        else:
            input ("res output: "+str(res))
            # single-target expected to provide an 'action' human-readable string
            action_text = res.get('action') if isinstance(res, dict) else None
            if not action_text:
                msgs.append('Invalid ability result: missing "action" text.')
                out['note'] = 'invalid_result'
                return out
            msgs.append(str(action_text))

        return out

    def _player_use_item(self, unit: Unit, item: Any, enemies: List[Unit], allies: List[Unit], target_unit: Optional[Unit] = None) -> Dict[str, Any]:
        actor = unit.entity
        msgs: List[str] = []
        out: Dict[str, Any] = {'messages': msgs, 'action_type': 'item'}

        # Expect `item` to be an index into actor.inventory (legacy UI behavior).
        idx = None
        if isinstance(item, int):
            idx = item
            item = self.player_game.inventory[idx] if 0 <= idx < len(self.player_game.inventory) else None
        elif item in self.player_game.inventory:
            idx = self.player_game.inventory.index(item)

        # try calling with target entity when available and API accepts it
        if target_unit is not None:
            res = actor.use_item(idx,  self.player_game,target_unit.entity)
        else:
            res = actor.use_item(idx,self.player_game)

        out['action_result'] = res
        # Mirror console behavior: check 'used' and report effects
        if not res.get('used'):
            msgs.append(str(res.get('error', 'No effect.')))
            out['note'] = 'use_item_failed'
            return out

        # report effects
        if 'healed' in res:
            msgs.append(f"{actor.name} uses the {item.name} on {target_unit.entity.name}.  They recover {res.get('healed')} HP.")
            out.update({'healed': res.get('healed')})
        if 'ap_restored' in res:
            msgs.append(f"{actor.name} uses the {item.name} on {target_unit.entity.name}.  They recover {res.get('ap_restored')} AP.")
            out.update({'ap_restored': res.get('ap_restored')})
        if 'stat' in res:
            msgs.append(f"{actor.name} uses the {item.name} on {target_unit.entity.name}.  They permanently increase {res.get('stat')} by {res.get('amount')}.")
            out.update({'stat': res.get('stat'), 'amount': res.get('amount')})
        if 'note' in res:
            msgs.append(str(res.get('note')))

        return out

    # needs to be updated to pass in all possibble targets, this includes other enemies as enemies have heals
    # hostile. attack will control the logic on which target to pick
    def _perform_hostile_action(self, unit: Unit, enemies: List[Optional[Unit]], allies: List[Optional[Unit]]) -> Dict[str, Any]: 
        msgs: List[str] = []
        out: Dict[str, Any] = {'messages': msgs, 'action_type': 'hostile_action'}
        hostile = unit.entity

        # no target
        if enemies is None:
            msgs.append('Hostile has no target.')
            out['note'] = 'no_target'
            return out

        player_ents = [t.entity for t in enemies if t is not None]
        hostile_ents = [t.entity for t in allies if t is not None]

        # If hostile is silenced, prevent ability usage by temporarily zeroing AP
        silenced = any((s.get('id') == 'silence') for s in (hostile.statuses or []))

        old_ap = None
        if silenced:
            old_ap = hostile.current_ap
            hostile.current_ap =0

        res = hostile.attack(player_ents, hostile_ents)

        # restore AP
        if silenced and old_ap is not None:
            hostile.current_ap = old_ap

        if isinstance(res, dict):
            if res.get('used_ability'):
                abil_res = res.get('ability_result') or {}
                # Multi-target support: if ability returned per-target results, map to alive players
                if isinstance(abil_res, dict) and isinstance(abil_res.get('results'), list):
                    # collect alive player units in order
                    player_units = [u for u in self.units if u._is_player() and u.is_alive()]
                    #input(f"abil_res: {abil_res}")
                    msgs.append(f"{hostile.name} uses {abil_res.get('ability_name')}!")

                    for idx, r in enumerate(abil_res.get('results') or []):                        
                        msgs.append(r.get('action',''))
                    out.update({'action_result': res, 'ability_result': abil_res})
            else:
                if not res.get('hit'):
                    target_name = res.get('target_name')
                    weapon_name = res.get('weapon') or res.get('weapon_name')
                    msgs.append(f"{hostile.name} attacks {target_name} with {weapon_name} but misses!")
                    out.update({'action_result': res, 'target_name': target_name})
                else:
                    dmg = res.get('applied', res.get('damage',0))
                    target_name = res.get('target_name')
                    weapon_name = res.get('weapon') or res.get('weapon_name')
                    msgs.append(f"{hostile.name} hits {target_name} with {weapon_name} for {dmg} damage!")
                    out.update({'action_result': res, 'damage': dmg, 'target_name': target_name})
        else:
            msgs.append(f"{hostile.name} spazzed out!")
            out['note'] = 'bad_result'

        return out

    def distribute_rewards(self) -> List[str]:
        """Award loot/xp for defeated hostiles to players in player_game.
        Returns a flattened list of human-readable messages (List[str]) suitable for
        appending directly to a UI message queue. This aggregates results across
        all defeated hostiles in the simulation.
        Each hostile will be awarded only once (marked with attribute `_awarded`).
        """
        messages: List[str] = []
        # collect player objects
        players: List[Player] = list(self.player_game.get_active_party())
        # Dead/petrified players do not share in combat rewards: they neither
        # count toward the XP division nor receive a portion of it.
        players = [p for p in players if not p.is_incapacitated()]
        if not players:
            return messages

        # helper map from player id -> player object (for nice messages)
        id_to_player: Dict[str, Player] = {}
        for p in players:
            pid = getattr(p, '_uuid', None) or getattr(p, 'id', None) or getattr(p, 'name', None)
            if pid:
                id_to_player[str(pid)] = p

        total_xp =0
        total_money =0
        per_player_levels: Dict[str, int] = {}
        awarded_items: List[Any] = []
        awarded_loot: List[Any] = []

        # iterate hostiles and collect structured results while marking awarded
        for u in self.units:
            if u._is_player():
                continue
            hostile = u.entity
            
            is_petrified = any((s.get('id') == 'petrify') for s in (hostile.statuses or []))
            if hostile.is_alive() and not is_petrified:
                continue

            res = hostile.award_players(self.player_game, players) or {}
            if hostile.id in self.player_game.enemies_slain:
                self.player_game.enemies_slain[hostile.id] +=1
            else:
                self.player_game.enemies_slain[hostile.id] =1

            # accumulate totals safely
            xp_aw = int(res.get('xp_awarded') or 0)
            
            total_xp += xp_aw

            money_aw = int(res.get('money_awarded') or 0)
            
            total_money += money_aw

            # levels_gained entries: list of {'player_id': pid, 'levels_gained': n}
            for lg in (res.get('levels_gained') or []):
                pid = lg.get('player_id')
                cnt = int(lg.get('levels_gained') or 0)

                if not pid or cnt <=0:
                    continue
                per_player_levels[str(pid)] = per_player_levels.get(str(pid),0) + cnt

            # collect awarded items and raw loot for messages
            for it in (res.get('awarded_items') or []):
                awarded_items.append(it)
            for it in (res.get('loot') or []):
                awarded_loot.append(it)


        # Build flattened message list in the requested order
        messages.append(f'{total_xp} XP gained')

        # Per-player level messages
        if per_player_levels:
            messages.append('Level gains')
            for pid, cnt in per_player_levels.items():
                p = id_to_player.get(pid)
                name = p.name if p is not None else str(pid)
                messages.append(f"{name} gained {cnt} level(s)")

        # Coins summary
        if total_money > 0:
            messages.append(f"total Coins gained {total_money}")

        # Awarded items
        if awarded_items:
            for it in awarded_items:
                iname = it.name
                messages.append(f"found item {iname}")


        return messages
