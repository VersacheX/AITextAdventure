"""Isolated per-continent world generation.

Each continent (2-6) is grown in its own ``ContinentSandbox`` -- a throwaway
``PlayerGame`` that reuses ALL of the existing region-growth machinery
(``create_region_at`` -> ``build_region_map`` -> weighted ``REGIONAL_NEIGHBORS``
selection) but is sealed off from the live game and from story/task side effects.

Why a sandbox instead of the old monolithic generate-then-partition pipeline:
  - The old flow grew all 21 chapter cities in one shared space, then tried to
    carve them into continents and relocate them. Placement frequently failed
    contiguity verification, triggering a 1000-attempt repair loop that often
    exhausted its retries. A continent that is generated in isolation is already
    self-contained and contiguous, so it can be dropped into the world at a
    single rigid offset with no repair loop.

What the sandbox deliberately does NOT do (see Constraint 3 of the redesign):
  - It never acquires tasks or runs task events. Story initialisation happens in
    the LIVE game AFTER the continent is placed, so event handlers resolve
    location/NPC references against the final world state. The sandbox overrides
    the task-producing hooks to no-ops so ``create_region_at`` builds pure
    geography.
"""
from typing import Dict, List, Optional, Tuple
import random

from game.objects.city import City
from game.objects.player_game import PlayerGame
import game.constants as const
from game.services import world_map_generator


class ContinentSandbox(PlayerGame):
    """Isolated PlayerGame for generating one continent's regions independently."""

    def __init__(self, continent_id: int, target_city_keys: List[str],
                 connector_budget: int = 8, live_pg: Optional[PlayerGame] = None,
                 global_city_offset: int = 0):
        """
        Args:
            continent_id: 1-based continent number (2-6; continent 1 is never
                sandboxed -- it is already built in the live game).
            target_city_keys: Ordered canonical chapter-city keys for this
                continent, e.g. ``["shallows_large_city", "snow_small_city",
                "swamp_small_city"]``. Order is preserved; it drives which city
                is built next.
            connector_budget: Cap on cityless connector regions grown between
                cities. Once spent, the sandbox FORCES the remaining cities so a
                stalled placement can't keep spawning filler.
            live_pg: The live game whose progression (characters/chapter) loot
                scaling must follow. Without it a fresh sandbox has no characters
                and only its own local city count, which would reset loot levels
                for every continent.
            global_city_offset: Number of chapter cities that precede this
                continent in ``CHAPTER_CITY_ORDER``. Added to the sandbox's local
                city count so loot scaling matches the city's true global chapter
                position rather than its 1-based position within the sandbox.
        """
        super().__init__()
        self.continent_id = continent_id
        self.target_city_keys = list(target_city_keys)  # preserve order
        self.connector_budget = connector_budget
        self.connectors_built = 0
        self.cities_built = 0
        self._live_pg = live_pg
        self._global_city_offset = global_city_offset
        # Post-intro cap semantics: the sandbox is "complete" so get_max_cities()
        # returns a city cap (our target count) rather than the intro cap.
        self.intro_complete = True

    # ------------------------------------------------------------------
    # Progression passthrough (keep loot scaling anchored to the live game)
    # ------------------------------------------------------------------
    def get_max_character_level(self) -> int:
        """Defer to the live game's party level so loot doesn't reset to 1.

        City loot scaling (``City.populate_tiles`` ->
        ``get_max_city_loot_level_level``) reads the max character level. A fresh
        sandbox has no characters, so without this it would always see level 1.
        """
        if self._live_pg is not None:
            return self._live_pg.get_max_character_level()
        return super().get_max_character_level()

    def get_max_city_loot_level_level(self) -> int:
        """Scale loot by this city's TRUE global chapter position.

        The base implementation uses the sandbox-local city count, which restarts
        at 0 for every continent and would flatten loot levels. Offset the local
        count by the number of chapter cities that precede this continent so a
        chapter-10 city scales as chapter 10, not as the sandbox's 3rd city.
        """
        num_cities = self._global_city_offset + self.get_city_count()
        return max(num_cities, self.get_max_character_level()) + 1

    # ------------------------------------------------------------------
    # City budgeting overrides (Constraint 2: per-sandbox cursor)
    # ------------------------------------------------------------------
    def get_max_cities(self) -> int:
        """Return THIS sandbox's city target, not the global chapter-city count."""
        return len(self.target_city_keys)

    def get_next_unbuilt_chapter_city(self) -> Optional[str]:
        """Return the next city from this sandbox's ordered list.

        Scans ``self.target_city_keys`` in order and returns the first one not
        yet present in ``self.regions``. This decouples sandbox city selection
        from the global ``CHAPTER_CITY_ORDER`` state, so an empty sandbox never
        restarts at chapter 1 -- it starts at its own first target city.
        """
        built = {
            f"{r.region_name}_{r.child_city.city_name}"
            for r in self.regions
            if r.child_city is not None and r.child_city.city_name
        }
        for city_key in self.target_city_keys:
            if city_key not in built:
                return city_key
        return None  # All target cities built.

    # ------------------------------------------------------------------
    # Connector budget (Constraint: bounded filler, no open-ended growth)
    # ------------------------------------------------------------------
    def _region_should_have_city(self, cities_remaining: int) -> bool:
        """Force cities once the connector budget is spent.

        The base policy biases a region to be a cityless connector whenever the
        previous region had a city. On its own that lets filler accumulate until
        ``generate_world`` hits its stall limit. Here, once we've already grown
        ``connector_budget`` connectors, we FORCE every remaining region to carry
        a city so the sandbox converges on exactly its target set promptly.
        """
        citiless = sum(1 for r in self.regions if r.child_city is None)
        if citiless >= self.connector_budget:
            return True
        return super()._region_should_have_city(cities_remaining)

    # ------------------------------------------------------------------
    # Story suppression (Constraint 3: no task acquisition during generation)
    # ------------------------------------------------------------------
    def acquire_task(self, task) -> None:  # noqa: D401 - intentional no-op
        """Suppress task acquisition inside the sandbox.

        Story tasks (and their acquire/complete events) must only run in the live
        game after the continent is placed. ``create_region_at`` calls this during
        generation; here it does nothing so pure geography is produced.
        """
        return None

    def create_primary_story_task_for_region(self, acquired_region):
        return None

    def initiate_city_story_task_chain(self, region_name, child_city):
        return None

    def advance_chapter(self):
        return None

    # ------------------------------------------------------------------
    # Region creation with continent stamping
    # ------------------------------------------------------------------
    def create_region_at(self, origin: Tuple[int, int]) -> Optional[City]:
        """Grow one region and stamp it with this sandbox's continent id.

        Reuses the full parent ``create_region_at`` (weighted neighbour policy
        from ``REGIONAL_NEIGHBORS`` is untouched -- Constraint 5). The city vs
        connector decision is governed by ``_region_should_have_city`` above.
        """
        # Stop once every target city is built.
        if self.cities_built >= len(self.target_city_keys):
            return None

        region = super().create_region_at(origin)
        if region is None:
            return region

        if region.child_city is not None:
            self.cities_built += 1
        else:
            self.connectors_built += 1

        # Stamp the sandbox's continent id onto the region (and its city).
        region.continent = self.continent_id
        if region.child_city is not None:
            region.child_city.continent = self.continent_id

        return region


def _ensure_sandbox_contiguous(sandbox: "ContinentSandbox", cont_id: int) -> None:
    """Repair + verify the sandbox continent's WALKABLE contiguity, failing closed.

    City count alone does not prove a usable continent: edge-grown regions can
    touch only through impassable/building seam tiles, leaving cities unreachable
    on foot. The old monolithic pipeline repaired and verified this
    (``repair_continent_walkable_joins`` / walkable-contiguity check); we must do
    the same before accepting a sandbox, otherwise we'd seat a continent whose
    cities can't be walked between.

    Reuses the shared continent_service helpers, treating the sandbox's entire
    region list as a single continent.
    """
    from game.services.continent_service import (
        normalize_region_internal_connectivity,
        update_player_game_world_tiles_after_translation,
        repair_continent_walkable_joins,
        _continent_is_contiguous,
    )

    continent = list(sandbox.regions)

    # Bridge each region's own internal gaps first (child-city vs parent splits).
    for region in continent:
        normalize_region_internal_connectivity(region, sandbox)
    update_player_game_world_tiles_after_translation(sandbox)

    # Carve non-destructive walkable corridors between region seams.
    repair_continent_walkable_joins(sandbox, [continent])

    if not _continent_is_contiguous(continent):
        raise RuntimeError(
            f"Continent {cont_id}: generated cities are not walkably connected "
            f"after repair; refusing to seat a disconnected continent."
        )


def generate_continent_sandboxes(live_pg: PlayerGame, seed: int) -> Dict[int, ContinentSandbox]:
    """Generate continents 2-6 in isolated sandboxes.

    Args:
        live_pg: The live PlayerGame (continent 1 already built). Its party-level
            progression anchors loot scaling inside each sandbox.
        seed: Base RNG seed for determinism.

    Returns:
        Dict mapping ``continent_id`` -> completed ``ContinentSandbox``.

    Raises:
        RuntimeError: If any sandbox fails to generate its target city set or
            produces a walkably-disconnected continent.
    """
    sandboxes: Dict[int, ContinentSandbox] = {}
    index = 0

    for cont_id, city_count in enumerate(const.CONTINENT_COMPOSITION, start=1):
        if cont_id == 1:
            # Continent 1 is already built in the live game; skip but advance the
            # cursor past its chapter cities.
            index += city_count
            continue

        target_cities = const.CHAPTER_CITY_ORDER[index: index + city_count]
        global_city_offset = index
        index += city_count

        print(f"Generating continent {cont_id} ({city_count} cities): {target_cities}")

        sandbox = ContinentSandbox(
            continent_id=cont_id,
            target_city_keys=target_cities,
            connector_budget=max(2, city_count // 2),
            live_pg=live_pg,
            global_city_offset=global_city_offset,
        )

        seed_base = (seed * (cont_id + 1)) % (10 ** 8) or (cont_id + 1)

        # Seed the module-global RNG deterministically before generation. The
        # region-growth path (create_region_at / _region_should_have_city /
        # REGIONAL_NEIGHBORS selection, and build_region_map's city seed) all draw
        # from the global ``random`` stream, so pinning it here is what actually
        # makes a given world seed reproduce the same continents each run.
        random.seed(seed_base)

        try:
            world_map_generator.generate_world(
                sandbox,
                num_regions=500,
                seed_base=seed_base,
                min_size=500,
                verbose=True,
            )
        except Exception as exc:  # noqa: BLE001
            raise RuntimeError(f"Continent {cont_id} generation failed: {exc}")

        built_cities = sandbox.get_city_count()
        if built_cities != city_count:
            raise RuntimeError(
                f"Continent {cont_id}: generated {built_cities} cities, "
                f"expected {city_count} ({target_cities})."
            )

        # Validate the continent is walkably contiguous before accepting it.
        _ensure_sandbox_contiguous(sandbox, cont_id)

        sandboxes[cont_id] = sandbox
        print(
            f"Continent {cont_id}: OK ({built_cities} cities, "
            f"{len(sandbox.regions) - built_cities} connectors)."
        )

    return sandboxes
