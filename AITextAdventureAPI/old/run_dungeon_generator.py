"""
Standalone runner to test dungeon generation for Rokhuld's Deep Core.
"""

from game.services.dungeon_builder_service import build_dungeon
from game.region_seeds.primary_stories.mountains.rokhuld_lair import DUNGEON_SETTINGS as ROKHULD_DUNGEON_SETTINGS
from game.region_seeds.primary_stories.desert.zaruun_lair import DUNGEON_SETTINGS as ZARUUN_DUNGEON_SETTINGS
from game.region_seeds.primary_stories.snow.aeriola_lair import DUNGEON_SETTINGS as AERIOLA_DUNGEON_SETTINGS
from game.region_seeds.primary_stories.forest.marrowroot_lair import DUNGEON_SETTINGS as MARROWROOT_DUNGEON_SETTINGS
from game.region_seeds.primary_stories.grassland.serene_lair import DUNGEON_SETTINGS as SERENE_DUNGEON_SETTINGS
from game.region_seeds.primary_stories.shallows.uulthar_lair import DUNGEON_SETTINGS as UULTHAR_DUNGEON_SETTINGS
from game.region_seeds.primary_stories.swamp.miregloom_lair import DUNGEON_SETTINGS as MIREGLOOM_DUNGEON_SETTINGS


def render_dungeon_to_console(dungeon):
    """
    Prints the dungeon floor0 to the console.
    - passable tiles: '.'
    - impassable tiles: '?'
    - NPCs: 'N'
    - Boss: 'B'
    """
    z = 0  # only one floor for now

    # Compute bounding box using dungeon helpers
    min_x = dungeon.get_level_min_x(z)
    min_y = dungeon.get_level_min_y(z)
    width, height = dungeon.get_level_width_height(z)

    # Guard against empty dungeon
    if width <= 0 or height <= 0:
        print("No tiles on this level to render")
        return

    # Build a 2D char grid initialized to impassable
    
    grid = [["?" for _ in range(width)] for _ in range(height)]

    # Iterate grid positions and map to world coordinates
    for gy in range(height):
        for gx in range(width):
            wx = gx + min_x
            wy = gy + min_y
            # Directly lookup tile in dungeon.tiles to avoid in_bounds/get_tile behavior
            tile = dungeon.tiles.get((wx, wy, z))
            if not tile:
                continue

            if tile.passable:
                grid[gy][gx] = dungeon.open_area_tile
                
            if not tile.passable:
                grid[gy][gx] = dungeon.impassable_tile

            # NPCs
            if tile.entities:
                #input (f'tile entities: {tile.entities}')
                for ent in tile.entities:
                    if ent.get('type') == 'npc':
                        grid[gy][gx] = 'N'

            # Mark start if world coords equal origin
            if wx == 0 and wy == 0:
                grid[gy][gx] = '☺'  # Start position

    # for each item in the grid if it is a ? and has at least one non-? neighbor convert it to a *
    for gy in range(height):
        for gx in range(width):
            if grid[gy][gx] == '?':
                # check neighbors
                neighbors = [
                    (gy-1, gx),  # up
                    (gy+1, gx),  # down
                    (gy, gx-1),  # left
                    (gy, gx+1)   # right
                ]
                for ny, nx in neighbors:
                    if 0 <= ny < height and 0 <= nx < width:
                        if grid[ny][nx] != '?' and grid[ny][nx] != '*':
                            grid[gy][gx] = '*'
                            break

    # # Boss placement (optional) -- map world coords to grid indices
    # for boss in dungeon.boss_mob:
    #     bx, by, bz = boss['x'], boss['y'], boss['z']
    #     if bz == z:
    #         gx = bx - min_x
    #         gy = by - min_y
    #         if 0 <= gy < height and 0 <= gx < width:
    #             grid[gy][gx] = 'B'

    # Print to console
    for row in grid:
        print(''.join(row))


def main():

    dungeons = [ ROKHULD_DUNGEON_SETTINGS, ZARUUN_DUNGEON_SETTINGS, MARROWROOT_DUNGEON_SETTINGS, AERIOLA_DUNGEON_SETTINGS, SERENE_DUNGEON_SETTINGS, UULTHAR_DUNGEON_SETTINGS, MIREGLOOM_DUNGEON_SETTINGS,]
    for dungeon_settings in dungeons:
        print("Building dungeon:", dungeon_settings["dungeon_id"])
        dungeon = build_dungeon(dungeon_settings)

        print("\nDungeon generated. Rendering...\n")
        render_dungeon_to_console(dungeon)

    print("\nDone.")


if __name__ == "__main__":
    main()
