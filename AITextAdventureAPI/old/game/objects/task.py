from enum import Enum
from typing import Optional, Union, Tuple, List, Dict, Any
import random
from services.task_completion_service import execute_acquire_event, execute_complete_event


class TaskType(str, Enum):
    Fetch = "fetch"
    Deliver = "deliver"
    Meet = "meet"
    Goto = "goto"
    Defeat = "defeat"
    CompleteIntroStory = "complete_intro_story"
    CompleteRegionalQuests = "complete_regional_quests"


class SpecialTaskToType(str, Enum):
    NPC = "npc"
    SPECIAL_SUBLOCATION = "special_sublocation"
    COORDINATES = "coordinates"
    MOB = "mob"


class TaskEventType(str, Enum):
    CREATE_SUBLOCATION = "create_sublocation_with_loot"
    CREATE_DUNGEON = "create_dungeon"
    CREATE_NPC = "create_npc"
    CREATE_CHARACTER_NPC = "create_character_npc"
    BEGIN_COMBAT = "begin_combat"
    DUNGEON_ADD_TREASURE = 'dungeon_add_treasure'
    DUNGEON_ADD_NPC = 'dungeon_add_npc'
    AWARD_TASK = "award_task"
    AWARD_ITEM = "award_item"
    REMOVE_ITEM = "remove_item"
    AWARD_MONEY = "award_money"
    INITIATE_DIALOG = "initiate_dialog"
    INITIATE_CHARACTER_DIALOG = "initiate_character_dialog"
    SET_NPC_STANDING_TEXT = "set_npc_standing_text"
    HIDE_NPC = "hide_npc"
    SHOW_NPC = "show_npc"
    CHARACTER_JOIN = "character_join"
    PLAYER_CHARACTER_JOIN = "player_character_join"
    ADD_PENDING_CHARACTER = "add_pending_character"
    ADVANCE_CHAPTER = "advance_chapter"
    COMPLETE_INTRO_STORY = "complete_intro_story"
    LOCK_DUNGEON = "lock_dungeon"
    UNLOCK_DUNGEON = "unlock_dungeon"
    SET_DUNGEON_LOCKED_TEXT = "set_dungeon_locked_text"
    SET_PLAYER_IN_DUNGEON = "set_player_in_dungeon"
    REMOVE_PLAYER_FROM_DUNGEON = "remove_player_from_dungeon"
    COMPLETE_REGION_QUEST = "complete_region_quest"
    SET_NPC_MET = "set_npc_met"
    SET_AIRCRAFT = "set_aircraft"
    ALLOW_OCEAN_FLIGHT = 'allow_ocean_flight'
    CAN_AIRCRAFT_FLY = 'can_aircraft_fly'
    UNLOCK_NPC_LOG = 'unlock_npc_log'
    REMOVE_OCEAN = 'remove_ocean'
    SET_PLAYER_LOCATION = 'set_player_location'
    UNLOCK_HYPERWAY = 'unlock_hyperway'
    LOCK_HYPERWAY = 'lock_hyperway'
    CANCEL_TASK = 'cancel_task'
    REMOVE_TASK = 'remove_task'


class TaskAcquireEvent:
    def __init__(self, event_type: TaskEventType, params: Dict[str, Any]):
        self.event_type: TaskEventType = event_type
        self.params: Dict[str, Any] = params

    def execute(self, player_game, parent_task) -> None:
        execute_acquire_event(self, player_game, parent_task)

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "TaskAcquireEvent":
        et = d.get("event_type")
        params = d.get("params") or {}
        evtype = TaskEventType(et)
        return TaskAcquireEvent(evtype, params)


class TaskCompleteEvent:
    def __init__(self, event_type: TaskEventType, params: Dict[str, Any]):
        self.event_type: TaskEventType = event_type
        self.params: Dict[str, Any] = params

    def execute(self, player_game, parent_task) -> None:
        execute_complete_event(self, player_game, parent_task)

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "TaskCompleteEvent":
        et = d.get("event_type")
        params = d.get("params") or {}
        evtype = TaskEventType(et)
        return TaskCompleteEvent(evtype, params)


# ====================== MAIN TASK CLASSES ======================

class Task:
    def __init__(self, task_id: str):
        self.task_id: str = task_id
        self.type: TaskType = TaskType.Fetch
        self.task_acquire_events: List = []
        self.task_complete_events: List = []
        self.acquired_region = None
        self.completed: bool = False

    def check_completion_terms(self, player_game=None) -> bool:
        """Centralized completion check - this is the one that should be used."""
        if player_game is None:
            return False

        if self.type == TaskType.Fetch:
            return self._check_fetch(player_game)
        elif self.type == TaskType.Deliver:
            return self._check_deliver(player_game)
        elif self.type == TaskType.Meet:
            return self._check_meet(player_game)
        elif self.type == TaskType.Goto:
            return self._check_goto(player_game)
        elif self.type == TaskType.Defeat:
            return self._check_defeat(player_game)
        elif self.type == TaskType.CompleteIntroStory:
            return player_game.intro_complete
        elif self.type == TaskType.CompleteRegionalQuests:
            return player_game.check_regional_quests_complete()

        return False

    def _check_fetch(self, pg) -> bool:
        if not hasattr(self, 'item_id'):
            return False
        for item in pg.inventory:
            if getattr(item, 'id', None) == self.item_id and getattr(item, 'quantity', 0) > 0:
                return True
        return False

    def _check_deliver(self, pg) -> bool:
        return False  # Handled manually in NPC interaction

    def _check_meet(self, pg) -> bool:
        if not hasattr(self, 'to_type') or self.to_type != SpecialTaskToType.NPC:
            return False
        npc_id = pg.translate_npc_ref_to_id(self.to_id)
        npc = next((n for n in pg.npcs if n.id == npc_id), None)
        return bool(npc and getattr(npc, 'met', False))

    def _check_goto(self, pg) -> bool:
        if not hasattr(self, 'coordinates'):
            return False
        return (pg.x, pg.y, pg.z) == tuple(self.coordinates)

    def _check_defeat(self, pg) -> bool:
        if not hasattr(self, 'to_type') or self.to_type != SpecialTaskToType.MOB:
            return False
        return pg.enemies_slain.get(self.to_id, 0) > 0


# Subclasses now inherit the good check_completion_terms instead of overriding with False
class MeetTask(Task):
    def __init__(self, task_id: str, to_type: SpecialTaskToType, to_id: Union[str, Tuple[int, int, int]]):
        super().__init__(task_id)
        self.to_type = to_type
        self.to_id = to_id
        self.type = TaskType.Meet


class DefeatTask(Task):
    def __init__(self, task_id: str, to_type: SpecialTaskToType, to_id: Union[str, Tuple[int, int, int]]):
        super().__init__(task_id)
        self.to_type = to_type
        self.to_id = to_id
        self.type = TaskType.Defeat


class FetchTask(Task):
    def __init__(self, task_id: str, item_id: str):
        super().__init__(task_id)
        self.item_id = item_id
        self.type = TaskType.Fetch


class DeliverTask(Task):
    def __init__(self, task_id: str, special_item_id: str, to_type: SpecialTaskToType, to_id: Union[str, Tuple[int, int, int]]):
        super().__init__(task_id)
        self.special_item_id = special_item_id
        self.to_type = to_type
        self.to_id = to_id
        self.type = TaskType.Deliver


class GotoTask(Task):
    def __init__(self, task_id: str, coordinates: Tuple[int, int, int]):
        super().__init__(task_id)
        self.coordinates = coordinates
        self.type = TaskType.Goto


class CompleteIntroStoryTask(Task):
    def __init__(self, task_id: str):
        super().__init__(task_id)
        self.type = TaskType.CompleteIntroStory

class CompleteRegionalQuestsTask(Task):
    def __init__(self, task_id: str):
        super().__init__(task_id)
        self.type = TaskType.CompleteRegionalQuests


# ------------------ Seed Builder ------------------
def build_task_from_seed(seed: Dict[str, Any], acquired_region: Any) -> Task:
    tid = seed.get('task_id') or seed.get('id')
    ttype = seed.get('type', 'meet').lower()

    if ttype == 'meet':
        task = MeetTask(tid, SpecialTaskToType(seed.get('to_type')), seed.get('to_id'))
    elif ttype == 'defeat':
        task = DefeatTask(tid, SpecialTaskToType(seed.get('to_type')), seed.get('to_id'))
    elif ttype == 'fetch':
        task = FetchTask(tid, seed.get('item_id') or seed.get('to_id'))
    elif ttype == 'deliver':
        task = DeliverTask(tid, seed.get('item_id'), SpecialTaskToType(seed.get('to_type')), seed.get('to_id'))
    elif ttype == 'goto':
        task = GotoTask(tid, seed.get('to_id') or seed.get('coordinates'))
    elif ttype == 'complete_intro_story':
        task = CompleteIntroStoryTask(tid)
    elif ttype == 'complete_regional_quests':
        task = CompleteRegionalQuestsTask(tid)
    else:
        task = Task(tid)

    # Attach events
    acquire = seed.get('task_acquire_events') or seed.get('acquire_events') or []
    complete = seed.get('task_complete_events') or seed.get('complete_events') or []

    task.task_acquire_events = [TaskAcquireEvent.from_dict(d) for d in acquire]
    task.task_complete_events = [TaskCompleteEvent.from_dict(d) for d in complete]
    task.acquired_region = acquired_region

    return task


def build_tasks_from_seed(seed_list: List[Dict[str, Any]], acquired_region: Any) -> List[Task]:
    return [build_task_from_seed(s, acquired_region) for s in (seed_list or [])]