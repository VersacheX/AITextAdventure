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
                 connector_budget: int = 8):
        """
        Args:
            continent_id: 1-based continent number (2-6; continent 1 is never
                sandboxed -- it is already built in the live game).
            target_city_keys: Ordered canonical chapter-city keys for this
                continent, e.g. ``["shallows_large_city", "snow_small_city",
                "swamp_small_city"]``. Order is preserved; it drives which city
                is built next.
            connector_budget: Soft cap on cityless connector regions grown
                between cities.
        """
        super().__init__()
        self.continent_id = continent_id
        self.target_city_keys = list(target_city_keys)  # preserve order
        self.connector_budget = connector_budget
        self.connectors_built = 0
        self.cities_built = 0
        # Post-intro cap semantics: the sandbox is "complete" so get_max_cities()
        # returns a city cap (our target count) rather than the intro cap.
        self.intro_complete = True

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
    # Region creation with budget + continent stamping
    # ------------------------------------------------------------------
    def create_region_at(self, origin: Tuple[int, int]) -> Optional[City]:
        """Grow one region, enforcing this sandbox's city/connector budgets.

        Reuses the full parent ``create_region_at`` (weighted neighbour policy
        from ``REGIONAL_NEIGHBORS`` is untouched -- Constraint 5), then stamps the
        resulting region with this sandbox's continent id.
        """
        # Stop once every target city is built.
        if self.cities_built >= len(self.target_city_keys):
            return None

        # If the connector budget is spent and no more cities remain to anchor a
        # new region, stop rather than growing endless filler.
        citiless = [r for r in self.regions if r.child_city is None]
        if len(citiless) >= self.connector_budget:
            if self.get_next_unbuilt_chapter_city() is None:
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


def generate_continent_sandboxes(live_pg: PlayerGame, seed: int) -> Dict[int, ContinentSandbox]:
    """Generate continents 2-6 in isolated sandboxes.

    Args:
        live_pg: The live PlayerGame (continent 1 already built). Only used for
            logging context; the sandboxes are fully independent.
        seed: Base RNG seed for determinism.

    Returns:
        Dict mapping ``continent_id`` -> completed ``ContinentSandbox``.

    Raises:
        RuntimeError: If any sandbox fails to generate its target city set.
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
        index += city_count

        print(f"Generating continent {cont_id} ({city_count} cities): {target_cities}")

        sandbox = ContinentSandbox(
            continent_id=cont_id,
            target_city_keys=target_cities,
            connector_budget=max(2, city_count // 2),
        )

        seed_base = (seed * (cont_id + 1)) % (10 ** 8) or (cont_id + 1)

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

        sandboxes[cont_id] = sandbox
        print(
            f"Continent {cont_id}: OK ({built_cities} cities, "
            f"{len(sandbox.regions) - built_cities} connectors)."
        )

    return sandboxes
