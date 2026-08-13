"""
Script to append missing hostile seed level bands to lv21to100.py files.
Run from: AITextAdventureAPI/old
"""
import os
import sys
sys.path.insert(0, '.')

# Needed bands per file (only 21-100 relevant here)
MISSING = {
    "game/region_seeds/regions/cities/forest/enemies_mid/lv21to100.py": [51, 61, 81],
    "game/region_seeds/regions/cities/forest/enemies_small/lv21to100.py": [51, 71, 81],
    "game/region_seeds/regions/cities/grassland/enemies_large/lv21to100.py": [41, 61, 81],
    "game/region_seeds/regions/cities/grassland/enemies_mid/lv21to100.py": [71, 81],
    "game/region_seeds/regions/cities/grassland/enemies_small/lv21to100.py": [51, 71, 81],
    "game/region_seeds/regions/cities/mountains/enemies_large/lv21to100.py": [61, 81],
    "game/region_seeds/regions/cities/mountains/enemies_mid/lv21to100.py": [61, 81],
    "game/region_seeds/regions/cities/mountains/enemies_small/lv21to100.py": [51, 61, 71, 81],
    "game/region_seeds/regions/cities/shallows/enemies_large/lv21to100.py": [51, 71],
    "game/region_seeds/regions/cities/shallows/enemies_mid/lv21to100.py": [61, 81],
    "game/region_seeds/regions/cities/shallows/enemies_small/lv21to100.py": [51, 61, 81],
    "game/region_seeds/regions/cities/snow/enemies_large/lv21to100.py": [51, 71],
    "game/region_seeds/regions/cities/snow/enemies_mid/lv21to100.py": [51, 71],
    "game/region_seeds/regions/cities/snow/enemies_small/lv21to100.py": [51, 61, 81],
    "game/region_seeds/regions/cities/swamp/enemies_large/lv21to100.py": [41, 61, 81],
    "game/region_seeds/regions/cities/swamp/enemies_mid/lv21to100.py": [51, 71],
    "game/region_seeds/regions/cities/swamp/enemies_small/lv21to100.py": [51, 61, 81],
}

# Generic seed template maker
def make_seeds(path, bands):
    """Generate seed entries for missing bands given a file path."""
    # Infer region and zone from path
    parts = path.split("/")
    region = parts[4]  # e.g. forest
    zone_dir = parts[5]  # enemies_large / enemies_mid / enemies_small
    zone = zone_dir.replace("enemies_", "")  # large / mid / small

    seeds = []
    for band_start in bands:
        lv1 = band_start + 2
        lv2 = band_start + 7
        xp1 = band_start * 80
        xp2 = band_start * 120
        hp1 = band_start * 180
        hp2 = band_start * 240
        str1 = band_start // 5
        str2 = band_start // 4
        con1 = (band_start // 5) - 1 if band_start >= 10 else 1
        int1 = band_start // 6
        ap1 = 8 + band_start // 10
        ap2 = 12 + band_start // 8
        mon1 = band_start * 30
        mon2 = band_start * 100
        xp_big = band_start * 200
        hp_big = band_start * 400

        id1 = f"{region}_{zone}_fill_{band_start}a"
        id2 = f"{region}_{zone}_fill_{band_start}b"
        name1 = f"{region.title()} {zone.title()} Warrior {band_start}"
        name2 = f"{region.title()} {zone.title()} Shade {band_start}"

        seeds.append(f"""
 # Lv{band_start}-{band_start+9} band (gap fill)
 {{"id": "{id1}", "name": "{name1}", "hostile_type": "humanoid", "role": "damage", "min_spawn_level": {lv1}, "rarity": "superrare", "base_xp": {xp1},
  "common_drop": "herb_major", "rare_drop": "herb_major", "money_range": ({mon1}, {mon2}),
  "basic_attack": "warrior strike", "strong_attack": "crushing blow",
  "player_abilities": None,
  "base_str": {str1*4}, "base_dex": {str1*2}, "base_con": {str1*4-2}, "base_int": {int1*2}, "base_hp": {hp1}, "base_ap": {ap1},
  "str_per_level": {max(1,str1//4)}, "dex_per_level": {max(0,str1//8)}, "con_per_level": {max(1,str1//4)}, "int_per_level": {max(0,int1//6)}}}?

 {{"id": "{id2}", "name": "{name2}", "hostile_type": "spirit", "role": "hazard", "min_spawn_level": {lv2}, "rarity": "superrare", "base_xp": {xp2},
  "common_drop": "tome_int", "rare_drop": "herb_major", "money_range": ({mon1//2}, {mon2//2}),
  "basic_attack": "shade touch", "strong_attack": "spectral burst",
  "player_abilities": ["dark_dark_magic_lv2_umbra_storm"],
  "base_str": {int1*2}, "base_dex": {str1*2+2}, "base_con": {int1*2+2}, "base_int": {str1*4}, "base_hp": {hp2}, "base_ap": {ap2},
  "str_per_level": {max(0,int1//6)}, "dex_per_level": {max(1,str1//8)}, "con_per_level": {max(0,int1//6)}, "int_per_level": {max(1,str1//4)}}}?""")

    return "\n".join(seeds)


for filepath, bands in MISSING.items():
    if not os.path.exists(filepath):
        print(f"SKIP (not found): {filepath}")
        continue

    content = open(filepath, 'r', encoding='utf-8-sig', errors='replace').read()
    # Remove trailing ]
    if content.rstrip().endswith(']'):
        content = content.rstrip()
        content = content[:-1].rstrip()  # remove ]

        additions = make_seeds(filepath, bands)
        # Replace the fullwidth comma (?) with regular comma
        additions = additions.replace("?", ",")

        new_content = content + "\n" + additions + "\n]\n"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"PATCHED: {filepath} bands={bands}")
    else:
        print(f"WARN: {filepath} does not end with ]")

print("Done.")
