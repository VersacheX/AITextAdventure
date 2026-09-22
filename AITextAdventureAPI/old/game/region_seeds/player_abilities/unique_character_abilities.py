# UNIQUE CHARACTER ABILITIES
# Naming convention: lv[X]_unique_ability_[type]_[character]_[abil_name]
# All abilities are marked non_player_ability=True.
# Element count == ability level.
# Level caps per character tier:
#   lv30 regional  -> 1 lv2, 2 lv3           (4 total)
#   lv35 ch7       -> 2 lv2, 2 lv3           (4 total)
#   lv50 ch11      -> 2 lv2, 1 lv3, 1 lv4   (4 total)
#   lv65 ch15      -> 1 lv2, 2 lv3, 1 lv4   (4 total)
#   lv75 ch19      -> 1 lv2, 2 lv3, 1 lv4   (4 total)
#   extended lv40  -> 2 lv2, 1 lv3, 1 lv4   (4 total)
#   extended lv55+ -> 1 lv2, 2 lv3, 1 lv4   (4 total)
# NO level-5 abilities anywhere.

UNIQUE_CHARACTER_ABILITY_SEEDS = [

    # =========================================================================
    # REGIONAL CHARACTERS (lv30) -- 1 lv2 + 2 lv3 = 3 abilities, 4 with lv1
    # Wait: comment says 4 total. Using: 1 lv2 + 2 lv3 + 1 lv1 is inconsistent.
    # The comment from the user file says:
    #   "req 1 lv2, 2 lv3" for lv30-ish (ch7 says 2 lv2, 2 lv3 for lv35)
    # Regional primary story chars are lv30; user said:
    #   lv35 -> 2 lv2, 2 lv3
    # lv30 regional chars: using 2 lv2, 2 lv3 (same generosity as lv35)
    # =========================================================================

    # -------------------------------------------------------------------------
    # SABLE (lv30, desert, magic/ENFJ)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_magic_sable_desert_read",
        "name": "Desert Read",
        "description": "Sable reads the heat shimmer around a foe, dissolving their elemental defenses before she strikes.",
        "ability_type": "magic", "level": 2,
        "elements": ["earth", "air"],
        "base_power": 0, "ap_cost": 40, "effect": "status",
        "status_keys": ["elemental_debuff", "defense_debuff", "dexterity_debuff"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv2_unique_ability_magic_sable_sandwitch_brew",
        "name": "Sandwitch Brew",
        "description": "A potent hex that weaves grit and shadow into the target's mind, muddying their thoughts.",
        "ability_type": "magic", "level": 2,
        "elements": ["earth", "dark"],
        "base_power":1, "ap_cost": 40, "effect": "status",
        "status_keys": ["intelligence_buff", "dexterity_buff"], "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_magic_sable_miragebreaker",
        "name": "Miragebreaker",
        "description": "Sable strips away illusion with a focused burst of sand, wind, and void -- a bitter strike from someone who sold hope she no longer believed in.",
        "ability_type": "magic", "level": 3,
        "elements": ["earth", "air", "dark"],
        "base_power": 96, "ap_cost": 80, "effect": "damage",
        "secondary_status": "intelligence_debuff", "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_magic_sable_consuming_dunes",
        "name": "Consuming Dunes",
        "description": "A wide rolling wave of sand and shadow that swallows all enemies in its path.",
        "ability_type": "magic", "level": 3,
        "elements": ["earth", "earth", "dark"],
        "base_power": 78, "ap_cost": 90, "effect": "damage",
        "can_aoe": True,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # THORN (lv30, forest, technique/ESFP)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_technique_thorn_root_snap",
        "name": "Root Snap",
        "description": "Thorn drives his blade through the earth, springing roots that trip and slow the target.",
        "ability_type": "technique", "level": 2,
        "elements": ["earth", "dark"],
        "base_power": 0, "ap_cost": 35, "effect": "status",
        "status_keys": ["dexterity_debuff", "constitution_debuff", "elemental_debuff"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv2_unique_ability_technique_thorn_bark_skin",
        "name": "Bark Skin",
        "description": "Thorn's skin hardens like ancient wood, bracing him against the next strike.",
        "ability_type": "technique", "level": 2,
        "elements": ["earth", "light"],
        "base_power": 0, "ap_cost": 30, "effect": "status",
        "status_keys": ["defense_buff", "constitution_buff", "elemental_defense_buff"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_technique_thorn_feral_surge",
        "name": "Feral Surge",
        "description": "Thorn channels the forest's feral anger -- a primal charge that shatters everything in its path with roots, earth, and void-shadowed fury.",
        "ability_type": "technique", "level": 3,
        "elements": ["earth", "earth", "dark"],
        "base_power": 80, "ap_cost": 85, "effect": "damage",
        "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_technique_thorn_guardian_of_the_grove",
        "name": "Guardian of the Grove",
        "description": "The forest itself answers Thorn's call -- a focused strike that also mends his own wounds through the earth's memory.",
        "ability_type": "technique", "level": 3,
        "elements": ["earth", "light", "water"],
        "base_power": 72, "ap_cost": 80, "effect": "damage",
        "secondary_status": "constitution_buff", "can_aoe": False,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # NIA (lv30, grassland, skill/ENFP)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_skill_nia_wind_read",
        "name": "Wind Read",
        "description": "Nia listens to the wind around her target and slips past their defenses before they know she moved.",
        "ability_type": "skill", "level": 2,
        "elements": ["air", "dark"],
        "base_power": 0, "ap_cost": 35, "effect": "status",
        "status_keys": ["defense_debuff", "elemental_debuff", "attack_debuff"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv2_unique_ability_skill_nia_gale_step",
        "name": "Gale Step",
        "description": "Nia accelerates into the wind until she becomes one with it, sharpening her own speed and evasion.",
        "ability_type": "skill", "level": 2,
        "elements": ["air", "light"],
        "base_power": 0, "ap_cost": 40, "effect": "status",
        "status_keys": ["dexterity_buff", "elemental_defense_buff", "regen"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_skill_nia_echo_step",
        "name": "Echo Step",
        "description": "Nia steps through the wind and reappears somewhere the target did not expect -- the disorientation she leaves behind is entirely the point.",
        "ability_type": "skill", "level": 3,
        "elements": ["air", "air", "dark"],
        "base_power": 10, "ap_cost": 98, "effect": "status",
        "status_keys": ["confuse"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_skill_nia_futures_edge",
        "name": "Future's Edge",
        "description": "Having once heard her own death on the wind, Nia now strikes before her target can act -- a devastating pre-emptive slash from someone who knows what's coming.",
        "ability_type": "skill", "level": 3,
        "elements": ["air", "dark", "air"],
        "base_power": 88, "ap_cost": 70, "effect": "damage",
        "can_aoe": False,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # BRAGG (lv30, mountains, tech/ESTP)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_tech_bragg_golem_pulse",
        "name": "Golem Pulse",
        "description": "Bragg fires a shockwave through the ground, disrupting enemy footing and lowering their defense to the shocks resonating through them.",
        "ability_type": "tech", "level": 2,
        "elements": ["earth", "electric"],
        "base_power": 1, "ap_cost": 40, "effect": "status",
        "status_keys": ["elemental_debuff", "continuous_damage"], "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv2_unique_ability_tech_bragg_forge_armor",
        "name": "Forge Armor",
        "description": "Bragg reinforces his gear on the fly, layering improvised plating that hardens his constitution mid-fight.",
        "ability_type": "tech", "level": 2,
        "elements": ["earth", "fire"],
        "base_power": 0, "ap_cost": 40, "effect": "status",
        "status_keys": ["defense_buff", "constitution_buff", "regen", "elemental_defense_buff"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_tech_bragg_fracture_pulse",
        "name": "Fracture Pulse",
        "description": "Bragg fires a resonant pulse modeled on the micro-fracture that destroyed his forge -- targeted, precise, and deeply personal. Cracks armor and defenses on impact.",
        "ability_type": "tech", "level": 3,
        "elements": ["earth", "electric", "dark"],
        "base_power": 94, "ap_cost": 80, "effect": "damage",
        "secondary_status": "defense_debuff", "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_tech_bragg_core_overload",
        "name": "Core Overload",
        "description": "Bragg channels raw fracture energy through his hammer and detonates it on contact -- a searing blast that burns everything within reach.",
        "ability_type": "tech", "level": 3,
        "elements": ["earth", "electric", "fire"],
        "base_power": 70, "ap_cost": 75, "effect": "damage",
        "can_aoe": True,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # RIPPLE (lv30, shallows, faith/INFJ)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_spirit_ripple_tidal_mend",
        "name": "Tidal Mend",
        "description": "Ripple channels the tide's patient rhythm into a single ally, washing away their wounds.",
        "ability_type": "spirit", "level": 2,
        "elements": ["water", "light"],
        "base_power": 30, "ap_cost": 35, "effect": "heal",
        "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv2_unique_ability_spirit_ripple_drowned_blessing",
        "name": "Drowned Blessing",
        "description": "Born of the depths that once claimed her, Ripple blesses her allies with elemental resilience.",
        "ability_type": "spirit", "level": 2,
        "elements": ["water", "dark"],
        "base_power": 0, "ap_cost": 45, "effect": "status",
        "status_keys": ["elemental_defense_buff", "regen", "constitution_buff"], "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_spirit_ripple_returned_tide",
        "name": "Returned Tide",
        "description": "The tide pulled her under once and brought her back. She can do the same for others -- a revival drawn from that impossible return.",
        "ability_type": "spirit", "level": 3,
        "elements": ["water", "light", "dark"],
        "base_power": 60, "ap_cost": 90, "effect": "revive",
        "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_spirit_ripple_deep_current_surge",
        "name": "Deep Current Surge",
        "description": "Ripple summons a crushing deep-water column that hammers all enemies in a wide arc.",
        "ability_type": "spirit", "level": 3,
        "elements": ["water", "water", "dark"],
        "base_power": 90, "ap_cost": 135, "effect": "damage",
        "can_aoe": True,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # KOR-IN (lv30, snow, technique/INFP)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_technique_korin_frost_step",
        "name": "Frost Step",
        "description": "Kor-in moves through frozen air without a sound, lowering the target's guard before the next strike.",
        "ability_type": "technique", "level": 2,
        "elements": ["ice", "air"],
        "base_power": 0, "ap_cost": 35, "effect": "status",
        "status_keys": ["defense_debuff", "dexterity_debuff", "constitution_debuff"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv2_unique_ability_technique_korin_grief_mantle",
        "name": "Grief Mantle",
        "description": "Kor-in hardens himself with cold grief -- years of loss calcified into an unbreakable shell.",
        "ability_type": "technique", "level": 2,
        "elements": ["ice", "earth"],
        "base_power": 0, "ap_cost": 35, "effect": "status",
        "status_keys": ["defense_buff", "strength_buff", "elemental_defense_buff"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_technique_korin_grief_driven_lance",
        "name": "Grief-Driven Lance",
        "description": "Kor-in pours years of cold, silent grief into a single piercing lance -- a strike so precise and final it feels inevitable.",
        "ability_type": "technique", "level": 3,
        "elements": ["ice", "ice", "dark"],
        "base_power": 105, "ap_cost": 85, "effect": "damage",
        "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_technique_korin_stillwater_strike",
        "name": "Stillwater Strike",
        "description": "A deceptively calm strike that carries the weight of a frozen world -- the silence before grief breaks everything.",
        "ability_type": "technique", "level": 3,
        "elements": ["ice", "dark", "air"],
        "base_power": 90, "ap_cost": 68, "effect": "damage",
        "secondary_status": "dexterity_debuff", "can_aoe": False,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # GRIMNAW (lv30, swamp, tech/INTP)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_tech_grimnaw_hex_charge",
        "name": "Hex Charge",
        "description": "Grimnaw fires a cursed electric bolt through his gadget array, dazing the target.",
        "ability_type": "tech", "level": 2,
        "elements": ["dark", "electric"],
        "base_power": 0, "ap_cost": 30, "effect": "status",
        "status_keys": ["stun"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv2_unique_ability_tech_grimnaw_resonance_shell",
        "name": "Resonance Shell",
        "description": "Grimnaw wraps himself in a tuned resonance field, blunting the next wave of elemental attacks.",
        "ability_type": "tech", "level": 2,
        "elements": ["dark", "air"],
        "base_power": 1, "ap_cost": 40, "effect": "status",
        "status_keys": ["elemental_defense_buff", "regen", "constitution_buff"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_tech_grimnaw_whisper_resonance",
        "name": "Whisper Resonance",
        "description": "Grimnaw weaponizes the fracture's whisper -- a destabilizing resonance blast that damages and unravels the target's cognitive coherence.",
        "ability_type": "tech", "level": 3,
        "elements": ["dark", "dark", "electric"],
        "base_power": 88, "ap_cost": 75, "effect": "damage",
        "secondary_status": "intelligence_debuff", "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_tech_grimnaw_cursed_circuit",
        "name": "Cursed Circuit",
        "description": "Grimnaw loops a cursed electrical circuit through all nearby enemies -- a spreading shock born from relics he catalogued and weaponized.",
        "ability_type": "tech", "level": 3,
        "elements": ["dark", "electric", "electric"],
        "base_power": 76, "ap_cost": 82, "effect": "damage",
        "can_aoe": True,
        "non_player_ability": True,
    },

    # =========================================================================
    # MAIN STORY CH7 CHARACTERS (lv35) -- 2 lv2 + 2 lv3
    # =========================================================================

    # -------------------------------------------------------------------------
    # LYREN VALE (lv35, ch7, faith/ISFP)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_spirit_lyren_riftwater_balm",
        "name": "Riftwater Balm",
        "description": "Lyren draws on the memory of still water to soothe a single ally's wounds.",
        "ability_type": "spirit", "level": 2,
        "elements": ["water", "light"],
        "base_power": 30, "ap_cost": 35, "effect": "heal",
        "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv2_unique_ability_spirit_lyren_gentle_warding",
        "name": "Gentle Warding",
        "description": "Lyren quietly raises a ward of earth and light around her allies, shielding them from elemental harm.",
        "ability_type": "spirit", "level": 2,
        "elements": ["light", "earth"],
        "base_power": 5, "ap_cost": 35, "effect": "status",
        "status_keys": ["elemental_defense_buff", "defense_buff"], "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_spirit_lyren_world_remembers",
        "name": "The World Remembers",
        "description": "Lyren channels the shape of what was before the fractures -- a broad healing tide that reminds wounds they were never meant to stay.",
        "ability_type": "spirit", "level": 3,
        "elements": ["water", "light", "earth"],
        "base_power": 48, "ap_cost": 70, "effect": "heal",
        "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_spirit_lyren_hibiscus_light",
        "name": "Hibiscus Light",
        "description": "Named for the flower that refused to die -- a concentrated beam of resilient light that revives a fallen ally.",
        "ability_type": "spirit", "level": 3,
        "elements": ["light", "light", "water"],
        "base_power": 60, "ap_cost": 90, "effect": "revive",
        "can_aoe": False,
        "non_player_ability": True,
    },

    # =========================================================================
    # MAIN STORY CH11 CHARACTERS (lv50) -- 2 lv2 + 1 lv3 + 1 lv4
    # =========================================================================

    # -------------------------------------------------------------------------
    # VEK (lv50, ch11, technique/ESTJ)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_technique_vek_command_strike",
        "name": "Command Strike",
        "description": "Vek issues a decisive strike backed by field authority -- precise and non-negotiable.",
        "ability_type": "technique", "level": 2,
        "elements": ["earth", "light"],
        "base_power": 30, "ap_cost": 30, "effect": "damage",
        "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv2_unique_ability_technique_vek_rally_line",
        "name": "Rally Line",
        "description": "Vek anchors her allies' resolve with a barked order, shoring up their physical defenses.",
        "ability_type": "technique", "level": 2,
        "elements": ["earth", "electric"],
        "base_power": 0, "ap_cost": 30, "effect": "status",
        "status_keys": ["defense_buff", "constitution_buff"], "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_technique_vek_dominion_breach",
        "name": "Dominion Breach",
        "description": "Vek plants her halberd and channels the city's law through the ground -- a thunderous AOE that stuns and cracks armor.",
        "ability_type": "technique", "level": 3,
        "elements": ["earth", "earth", "electric"],
        "base_power": 85, "ap_cost": 92, "effect": "damage", "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_technique_vek_iron_verdict",
        "name": "Iron Verdict",
        "description": "Vek brings the full weight of command down on a single target -- a crushing blow that simultaneously shatters defense and shocks the target into stillness.",
        "ability_type": "technique", "level": 4,
        "elements": ["earth", "light", "electric", "earth"],
        "base_power": 165, "ap_cost": 142, "effect": "damage", "can_aoe": False,
        "non_player_ability": True,
    },

    # =========================================================================
    # MAIN STORY CH15 CHARACTERS (lv65) -- 1 lv2 + 2 lv3 + 1 lv4
    # =========================================================================

    # -------------------------------------------------------------------------
    # WARDEN HALE (lv65, ch15, technique/ISTJ)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_technique_warden_hale_ledger_guard",
        "name": "Ledger Guard",
        "description": "Hale raises a practiced defense rooted in duty and record -- his shield is the weight of every promise he has kept.",
        "ability_type": "technique", "level": 2,
        "elements": ["earth", "light"],
        "base_power": 0, "ap_cost": 35, "effect": "status",
        "status_keys": ["defense_buff", "constitution_buff", "elemental_defense_buff"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_technique_warden_hale_rite_of_record",
        "name": "Rite of Record",
        "description": "Hale invokes the sacred rite of memory -- a sanctified blow that burns the target with the weight of forgotten names.",
        "ability_type": "technique", "level": 3,
        "elements": ["earth", "light", "dark"],
        "base_power": 95, "ap_cost": 80, "effect": "damage",
        "secondary_status": "defense_debuff", "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_technique_warden_hale_sentinel_ward",
        "name": "Sentinel Ward",
        "description": "Hale stands his ground and extends his warden's oath to all allies -- fortifying their resolve against elemental assault.",
        "ability_type": "technique", "level": 3,
        "elements": ["light", "earth", "light"],
        "base_power": 0, "ap_cost": 60, "effect": "status",
        "status_keys": ["elemental_defense_buff", "defense_buff"], "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_technique_warden_hale_judgment_hammer",
        "name": "Judgment Hammer",
        "description": "A single, crushing overhead strike that carries the full weight of the city's memory. The target is stunned and their defenses crack under the force of order.",
        "ability_type": "technique", "level": 4,
        "elements": ["earth", "earth", "light", "dark"],
        "base_power": 160, "ap_cost": 136, "effect": "damage", "can_aoe": False,
        "non_player_ability": True,
    },

    # =========================================================================
    # MAIN STORY CH19 CHARACTERS (lv85) -- 1 lv2 + 2 lv3 + 1 lv4
    # =========================================================================

    # -------------------------------------------------------------------------
    # SERAPHINE (lv85, ch19, faith/ESFJ)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_spirit_seraphine_hollow_hymn",
        "name": "Hollow Hymn",
        "description": "A fragment of Seraphine's old perfect song -- still beautiful enough to soothe wounds, even if it rings slightly false.",
        "ability_type": "spirit", "level": 2,
        "elements": ["light", "air"],
        "base_power": 25, "ap_cost": 35, "effect": "heal",
        "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_spirit_seraphine_true_harmony",
        "name": "True Harmony",
        "description": "Seraphine sings a song that finally holds shadow and light together -- a broad healing wave born from accepted truth rather than performed perfection.",
        "ability_type": "spirit", "level": 3,
        "elements": ["light", "air", "water"],
        "base_power": 50, "ap_cost": 64, "effect": "heal",
        "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_spirit_seraphine_songs_revive",
        "name": "Song's Revive",
        "description": "Seraphine's voice reaches the fallen -- not with a perfect note, but with a broken, honest one that pulls them back.",
        "ability_type": "spirit", "level": 3,
        "elements": ["light", "light", "dark"],
        "base_power": 60, "ap_cost": 90, "effect": "revive",
        "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_spirit_seraphine_shattered_aria",
        "name": "Shattered Aria",
        "description": "Seraphine unleashes the full force of her voice -- not the hollow harmony of preservation, but the raw, imperfect note of someone who finally stopped performing. It heals all allies deeply.",
        "ability_type": "spirit", "level": 4,
        "elements": ["light", "air", "water", "light"],
        "base_power": 135, "ap_cost": 152, "effect": "heal",
        "can_aoe": True,
        "non_player_ability": True,
    },

    # =========================================================================
    # EXTENDED CHARACTERS lv40 -- 2 lv2 + 1 lv3 + 1 lv4
    # =========================================================================

    # -------------------------------------------------------------------------
    # SERA FLAMEWEAVER (lv40, magic/ENFP)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_magic_veyr_ashcant_passionate_spark",
        "name": "Passionate Spark",
        "description": "Veyr ignites the air with a burst of raw emotional fire -- fast, hot, and completely sincere.",
        "ability_type": "magic", "level": 2,
        "elements": ["fire", "air"],
        "base_power": 30, "ap_cost": 30, "effect": "damage",
        "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv2_unique_ability_magic_veyr_ashcant_embers_veil",
        "name": "Ember's Veil",
        "description": "Veyr wraps himself in smoldering heat that sharpens his elemental strikes.",
        "ability_type": "magic", "level": 2,
        "elements": ["fire", "dark"],
        "base_power": 1, "ap_cost": 45, "effect": "status",
        "status_keys": ["elemental_attack_buff", "elemental_defense_buff"], "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_magic_veyr_ashcant_stage_ignition",
        "name": "Stage Ignition",
        "description": "Veyr turns the battlefield into his theater -- a sweeping arc of theatrical fire that scorches everything in its dramatic path.",
        "ability_type": "magic", "level": 3,
        "elements": ["fire", "fire", "dark"],
        "base_power": 78, "ap_cost": 90, "effect": "damage",
        "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_magic_veyr_ashcant_hearts_conflagration",
        "name": "Heart's Conflagration",
        "description": "Veyr pours raw passion into flame -- a theatrical eruption that scorches everything nearby with the heat of pure emotional truth.",
        "ability_type": "magic", "level": 4,
        "elements": ["fire", "fire", "dark", "fire"],
        "base_power": 115, "ap_cost": 118, "effect": "damage",
        "can_aoe": True,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # REGENT SYLVARA (lv40, magic/INTJ)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_magic_regent_sylvara_cold_analysis",
        "name": "Cold Analysis",
        "description": "Sylvara dissects her target's defenses with clinical precision, weakening their elemental cohesion.",
        "ability_type": "magic", "level": 2,
        "elements": ["dark", "air"],
        "base_power": 2, "ap_cost": 40, "effect": "status",
        "status_keys": ["elemental_debuff", "stun"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv2_unique_ability_magic_regent_sylvara_dominance_field",
        "name": "Dominance Field",
        "description": "Sylvara imposes a field of cold authority that dulls the target's intelligence.",
        "ability_type": "magic", "level": 2,
        "elements": ["dark", "electric"],
        "base_power": 1, "ap_cost": 40, "effect": "status",
        "status_keys": ["intelligence_debuff", "elemental_debuff"], "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_magic_regent_sylvara_inevitable_outcome",
        "name": "Inevitable Outcome",
        "description": "Sylvara has already calculated the end of this fight. A precise, devastating strike that lands before the target can respond.",
        "ability_type": "magic", "level": 3,
        "elements": ["dark", "electric", "air"],
        "base_power": 96, "ap_cost": 82, "effect": "damage",
        "secondary_status": "defense_debuff", "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_magic_regent_sylvara_strategic_unraveling",
        "name": "Strategic Unraveling",
        "description": "Sylvara simultaneously unravels mental acuity and defensive cohesion with cold, calculated precision.",
        "ability_type": "magic", "level": 4,
        "elements": ["dark", "electric", "air", "dark"],
        "base_power": 12, "ap_cost": 135, "effect": "status",
        "status_keys": ["intelligence_debuff", "confuse", 'elemental_debuff'], "can_aoe": True,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # SPARK MADDOX (lv40, tech/ENTP)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_tech_spark_maddox_shock_gadget",
        "name": "Shock Gadget",
        "description": "Maddox throws a hastily-assembled shock device that zaps the target and briefly disorients them.",
        "ability_type": "tech", "level": 2,
        "elements": ["electric", "air"],
        "base_power": 0, "ap_cost": 30, "effect": "status",
        "status_keys": ["stun"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv2_unique_ability_tech_spark_maddox_overclock",
        "name": "Overclock",
        "description": "Maddox overclocks his own systems to think and move faster than should be physically possible.",
        "ability_type": "tech", "level": 2,
        "elements": ["electric", "fire"],
        "base_power": 0, "ap_cost": 30, "effect": "status",
        "status_keys": ["dexterity_buff", "intelligence_buff"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_tech_spark_maddox_chain_explosion",
        "name": "Chain Explosion",
        "description": "Maddox triggers a daisy-chain of improvised explosives -- each one detonating the next in spectacular, wide-area destruction.",
        "ability_type": "tech", "level": 3,
        "elements": ["electric", "fire", "air"],
        "base_power": 82, "ap_cost": 88, "effect": "damage",
        "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_tech_spark_maddox_volatile_prototype",
        "name": "Volatile Prototype",
        "description": "Maddox throws an unstable invention into the fray -- it explodes spectacularly, dealing chaotic wide-area damage. He is already building the next one.",
        "ability_type": "tech", "level": 4,
        "elements": ["electric", "fire", "air", "electric"],
        "base_power": 112, "ap_cost": 120, "effect": "damage",
        "can_aoe": True,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # COMMANDER DRAX (lv40, technique/ENTJ)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_technique_commander_drax_field_order",
        "name": "Field Order",
        "description": "Drax issues a terse command that physically galvanizes his allies' attack output.",
        "ability_type": "technique", "level": 2,
        "elements": ["light", "earth"],
        "base_power": 0, "ap_cost": 30, "effect": "status",
        "status_keys": ["attack_buff", "strength_buff"], "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv2_unique_ability_technique_commander_drax_siege_strike",
        "name": "Siege Strike",
        "description": "Drax brings his claymore down with the force of a battering ram, cracking the target's defenses wide open.",
        "ability_type": "technique", "level": 2,
        "elements": ["earth", "light"],
        "base_power": 40, "ap_cost": 30, "effect": "damage", "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_technique_commander_drax_warfront_crush",
        "name": "Warfront Crush",
        "description": "Drax drives his weight into the enemy line -- a sweeping strike that knocks back and disorients every foe in range.",
        "ability_type": "technique", "level": 3,
        "elements": ["earth", "light", "electric"],
        "base_power": 12, "ap_cost": 90, "effect": "status",
        "status_keys": ["stun"], "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_technique_commander_drax_iron_command",
        "name": "Iron Command",
        "description": "Drax bellows a battle order so absolute it physically fortifies all allies -- sharpening strikes, hardening resolve, demanding excellence.",
        "ability_type": "technique", "level": 4,
        "elements": ["earth", "light", "electric", "earth"],
        "base_power": 0, "ap_cost": 130, "effect": "status",
        "status_keys": ["attack_buff", "defense_buff", "defense_buff", "strength_buff", "constitution_buff", "elemental_defense_buff"], "can_aoe": True,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # GHOST (lv40, skill/ISTP)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_skill_ghost_shadow_mark",
        "name": "Shadow Mark",
        "description": "Ghost marks a target with a thread of shadow -- they cannot hide what Ghost already sees.",
        "ability_type": "skill", "level": 2,
        "elements": ["dark", "air"],
        "base_power": 0, "ap_cost": 40, "effect": "status",
        "status_keys": ["defense_debuff", "dexterity_debuff", "continuous_damage"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv2_unique_ability_skill_ghost_silent_read",
        "name": "Silent Read",
        "description": "Ghost catalogues every gap in the enemy's posture in one cold, silent pass.",
        "ability_type": "skill", "level": 2,
        "elements": ["dark", "ice"],
        "base_power": 0, "ap_cost": 40, "effect": "status",
        "status_keys": ["attack_debuff", "constitution_debuff", "elemental_debuff"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_skill_ghost_disappearing_act",
        "name": "Disappearing Act",
        "description": "Ghost slips between reality and shadow, reappearing behind the target with a precise, devastating strike.",
        "ability_type": "skill", "level": 3,
        "elements": ["dark", "air", "dark"],
        "base_power": 92, "ap_cost": 78, "effect": "damage",
        "secondary_status": "defense_debuff", "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_skill_ghost_void_efface",
        "name": "Void Efface",
        "description": "Ghost disappears entirely and reappears behind the target -- every gap in their defense catalogued and exploited in a single silent pass.",
        "ability_type": "skill", "level": 4,
        "elements": ["dark", "air", "dark", "ice"],
        "base_power": 20, "ap_cost": 125, "effect": "status",
        "status_keys": ["defense_debuff", "elemental_debuff", "scanned"], "can_aoe": False,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # Eldon Dawnseer (lv40, faith/INFJ)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_spirit_eldon_dawnseer_seer_shield",
        "name": "Seer Shield",
        "description": "Eldon glimpses the immediate future and raises a warding light a moment before the blow lands.",
        "ability_type": "spirit", "level": 2,
        "elements": ["light", "air"],
        "base_power": 5, "ap_cost": 35, "effect": "status",
        "status_keys": ["elemental_defense_buff", "intelligence_buff"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv2_unique_ability_spirit_eldon_dawnseer_fragment_vision",
        "name": "Fragment Vision",
        "description": "Eldon shares a fragment of his vision, sharpening an ally's mental acuity.",
        "ability_type": "spirit", "level": 2,
        "elements": ["light", "dark"],
        "base_power": 0, "ap_cost": 35, "effect": "status",
        "status_keys": ["intelligence_buff", "attack_buff", "dexterity_buff"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_spirit_eldon_dawnseer_dawnsight_strike",
        "name": "Dawnsight Strike",
        "description": "Eldon channels the weight of a terrible vision into a single radiant lance that burns the target with prophetic light.",
        "ability_type": "spirit", "level": 3,
        "elements": ["light", "dark", "light"],
        "base_power": 90, "ap_cost": 80, "effect": "damage",
        "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_spirit_eldon_dawnseer_prophetic_vision",
        "name": "Prophetic Vision",
        "description": "Eldon casts a fragment of his visions outward -- allies briefly glimpse the immediate future, gaining heightened awareness and elemental resistance.",
        "ability_type": "spirit", "level": 4,
        "elements": ["light", "dark", "light", "air"],
        "base_power": 0, "ap_cost": 150, "effect": "status",
        "status_keys": ["elemental_defense_buff", "intelligence_buff", "dexterity_buff", "dexterity_buff", "intelligence_buff"], "can_aoe": True,
        "non_player_ability": True,
    },

    # =========================================================================
    # EXTENDED CHARACTERS lv50 -- 1 lv2 + 2 lv3 + 1 lv4
    # =========================================================================

    # -------------------------------------------------------------------------
    # VOSS CALDERA (lv50, technique/ESTJ)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_tech_voss_caldera_leverage",
        "name": "Leverage",
        "description": "Voss finds the point of maximum pressure and applies it -- a focused strike that cracks the target's defenses.",
        "ability_type": "tech", "level": 2,
        "elements": ["earth", "fire"],
        "base_power": 0, "ap_cost": 35, "effect": "status",
        "status_keys": ["defense_debuff", "continuous_damage", "constitution_debuff"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_tech_voss_caldera_boardroom_blitz",
        "name": "Boardroom Blitz",
        "description": "Voss moves with terrifying corporate efficiency, punishing the enemy's weakest point with a crushing AOE sweep.",
        "ability_type": "tech", "level": 3,
        "elements": ["earth", "fire", "light"],
        "base_power": 80, "ap_cost": 85, "effect": "damage",
        "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_tech_voss_caldera_non_negotiable",
        "name": "Non-Negotiable",
        "description": "Voss makes it clear that this conversation is over -- a single decisive strike that brooks no counter.",
        "ability_type": "tech", "level": 3,
        "elements": ["earth", "light", "fire"],
        "base_power": 100, "ap_cost": 80, "effect": "damage",
        "secondary_status": "strength_debuff", "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_tech_voss_caldera_hostile_acquisition",
        "name": "Hostile Acquisition",
        "description": "Voss brings the full weight of corporate authority down on a single target -- a decisive, crushing blow that ends negotiations permanently.",
        "ability_type": "tech", "level": 4,
        "elements": ["earth", "fire", "light", "earth"],
        "base_power": 160, "ap_cost": 146, "effect": "damage",
        "can_aoe": False,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # DARE (lv55, skill/ESTP)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_skill_dare_reckless_opening",
        "name": "Reckless Opening",
        "description": "Dare charges without hesitation, sheer speed turning recklessness into a devastating first hit.",
        "ability_type": "skill", "level": 2,
        "elements": ["fire", "air"],
        "base_power": 30, "ap_cost": 30, "effect": "damage",
        "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_skill_dare_full_tilt",
        "name": "Full Tilt",
        "description": "Dare throws herself into peak speed, body and instinct locked into pure forward momentum.",
        "ability_type": "skill", "level": 3,
        "elements": ["fire", "air", "electric"],
        "base_power": 0, "ap_cost": 95, "effect": "status",
        "status_keys": ["dexterity_buff", "attack_buff", "regen"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_skill_dare_edge_runner",
        "name": "Edge Runner",
        "description": "Dare runs along the most dangerous path available and strikes from an angle no one expected.",
        "ability_type": "skill", "level": 3,
        "elements": ["fire", "electric", "air"],
        "base_power": 94, "ap_cost": 78, "effect": "damage",
        "secondary_status": "defense_debuff", "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_skill_dare_death_defying_rush",
        "name": "Death-Defying Rush",
        "description": "Dare charges straight into the most dangerous point without hesitation -- a blazing, electrified strike that only lands because she never stops moving.",
        "ability_type": "skill", "level": 4,
        "elements": ["fire", "air", "electric", "fire"],
        "base_power": 169, "ap_cost": 144, "effect": "damage",
        "can_aoe": False,
        "non_player_ability": True,
    },

    # =========================================================================
    # EXTENDED CHARACTERS lv60+ -- 1 lv2 + 2 lv3 + 1 lv4
    # =========================================================================

    # -------------------------------------------------------------------------
    # RYNN (lv60, faith/ISFJ)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_spirit_rynn_field_dressing",
        "name": "Field Dressing",
        "description": "Rynn patches wounds with quiet efficiency -- no fanfare, just care that works.",
        "ability_type": "spirit", "level": 2,
        "elements": ["water", "light"],
        "base_power": 30, "ap_cost": 35, "effect": "heal",
        "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_spirit_rynn_medics_blessing",
        "name": "Medic's Blessing",
        "description": "Rynn calls on every promise he made to every patient -- a broad blessing that steadies his entire team.",
        "ability_type": "spirit", "level": 3,
        "elements": ["water", "light", "earth"],
        "base_power": 50, "ap_cost": 70, "effect": "heal",
        "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_spirit_rynn_still_standing",
        "name": "Still Standing",
        "description": "Rynn steadies a fallen ally with the same quiet force he uses for everything -- reviving them with whatever it costs him.",
        "ability_type": "spirit", "level": 3,
        "elements": ["water", "light", "dark"],
        "base_power": 60, "ap_cost": 90, "effect": "revive",
        "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_spirit_rynn_field_mercy",
        "name": "Field Mercy",
        "description": "Rynn channels quiet grief into care -- a broad healing wave that soothes every ally's wounds with the same steady patience he has carried for years.",
        "ability_type": "spirit", "level": 4,
        "elements": ["water", "light", "earth", "water"],
        "base_power": 123, "ap_cost": 134, "effect": "heal",
        "can_aoe": True,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # ANITA (lv65, magic/ISTJ)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_magic_anita_catalogued_flaw",
        "name": "Catalogued Flaw",
        "description": "Anita has already filed the target's weakness. A precision strike that exploits a specific gap in their defenses.",
        "ability_type": "magic", "level": 2,
        "elements": ["dark", "air"],
        "base_power": 5, "ap_cost": 40, "effect": "status",
        "status_keys": ["defense_debuff", "elemental_debuff"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_magic_anita_classified_suppression",
        "name": "Classified Suppression",
        "description": "Anita deploys a targeted information blackout -- a shadow field that simultaneously dims intelligence and attack potency.",
        "ability_type": "magic", "level": 3,
        "elements": ["dark", "earth", "air"],
        "base_power": 0, "ap_cost": 80, "effect": "status",
        "status_keys": ["elemental_debuff", "silence"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_magic_anita_archive_bolt",
        "name": "Archive Bolt",
        "description": "Anita fires a concentrated bolt of dark archival energy -- a strike that feels like everything you forgot hitting you at once.",
        "ability_type": "magic", "level": 3,
        "elements": ["dark", "air", "dark"],
        "base_power": 95, "ap_cost": 80, "effect": "damage",
        "secondary_status": "intelligence_debuff", "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_magic_anita_exposed_weakness",
        "name": "Exposed Weakness",
        "description": "Anita catalogues every structural weakness in her target with archival precision -- simultaneously unraveling defense, intelligence, and attack potency.",
        "ability_type": "magic", "level": 4,
        "elements": ["dark", "earth", "air", "dark"],
        "base_power": 12, "ap_cost": 122, "effect": "status",
        "status_keys": ["elemental_debuff", "continuous_damage"], "can_aoe": False,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # ANDREA STARVEIL (lv70, skill/ESFP)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_skill_andrea_starveil_crowd_read",
        "name": "Crowd Read",
        "description": "Andrea reads the room in an instant, sharpening her own reflexes to match whatever energy is needed.",
        "ability_type": "skill", "level": 2,
        "elements": ["air", "light"],
        "base_power": 0, "ap_cost": 40, "effect": "status",
        "status_keys": ["dexterity_buff", "elemental_defense_buff", "regen"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_skill_andrea_starveil_encore",
        "name": "Encore",
        "description": "Andrea whirls back into the fight with a second devastating strike exactly when the enemy thinks the show is over.",
        "ability_type": "skill", "level": 3,
        "elements": ["air", "light", "fire"],
        "base_power": 88, "ap_cost": 75, "effect": "damage",
        "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_skill_andrea_starveil_raise_the_roof",
        "name": "Raise the Roof",
        "description": "Andrea lifts every ally's spirit with a galvanizing performance -- sharpening attack and dexterity across the whole team.",
        "ability_type": "skill", "level": 3,
        "elements": ["air", "fire", "light"],
        "base_power": 0, "ap_cost": 65, "effect": "status",
        "status_keys": ["attack_buff", "dexterity_buff"], "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_skill_andrea_starveil_meteor_rave",
        "name": "Meteor Rave",
        "description": "Andrea transforms the battlefield into her stage -- a dazzling finale that stirs every ally to peak performance.",
        "ability_type": "skill", "level": 4,
        "elements": ["air", "light", "fire", "air"],
        "base_power": 0, "ap_cost": 100, "effect": "status",
        "status_keys": ["attack_buff", "defense_buff", "strength_buff", "dexterity_buff", "elemental_attack_buff"], "can_aoe": True,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # TALIA SOFTHEART (lv80, faith/ESFJ)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_spirit_talon_tender_mend",
        "name": "Tender Mend",
        "description": "Talon lays his hands on an ally and heals with the warmth of someone who truly means it.",
        "ability_type": "spirit", "level": 2,
        "elements": ["light", "water"],
        "base_power": 30, "ap_cost": 35, "effect": "heal",
        "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_spirit_talon_needed_now",
        "name": "Needed Now",
        "description": "Talon's deepest fear is not being there -- he pours that fear into a revive that refuses to let someone stay fallen.",
        "ability_type": "spirit", "level": 3,
        "elements": ["light", "water", "dark"],
        "base_power": 60, "ap_cost": 90, "effect": "revive",
        "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_spirit_talon_community_light",
        "name": "Community Light",
        "description": "Talon extends his warmth across the whole team -- a gentle healing wave that touches everyone he cares for.",
        "ability_type": "spirit", "level": 3,
        "elements": ["light", "water", "earth"],
        "base_power": 69, "ap_cost":  75, "effect": "heal",
        "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_spirit_talon_heartroot_restoration",
        "name": "Heartroot Restoration",
        "description": "Talon lays both hands on a single ally and pours every ounce of himself into their recovery -- a deep, complete restoration.",
        "ability_type": "spirit", "level": 4,
        "elements": ["light", "water", "earth", "light"],
        "base_power": 200, "ap_cost": 135, "effect": "heal",
        "can_aoe": False,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # KORINA BRIGHTVEIN (lv85, faith/ENFJ)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_spirit_alden_brightvein_rally_call",
        "name": "Rally Call",
        "description": "Alden raises his voice and every ally's resolve tightens around it.",
        "ability_type": "spirit", "level": 2,
        "elements": ["light", "electric"],
        "base_power": 0, "ap_cost": 30, "effect": "status",
        "status_keys": ["attack_buff", "strength_buff"], "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_spirit_alden_brightvein_inspired_defense",
        "name": "Inspired Defense",
        "description": "Alden's inspiration is structural -- a broad blessing that hardens his team's physical and elemental resilience.",
        "ability_type": "spirit", "level": 3,
        "elements": ["light", "electric", "air"],
        "base_power": 0, "ap_cost": 60, "effect": "status",
        "status_keys": ["defense_buff", "elemental_defense_buff"], "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_spirit_alden_brightvein_leaders_mend",
        "name": "Leader's Mend",
        "description": "Alden heals by example -- a focused restorative burst that reminds a single ally they are not alone.",
        "ability_type": "spirit", "level": 3,
        "elements": ["light", "light", "water"],
        "base_power": 85, "ap_cost": 70, "effect": "heal",
        "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_spirit_alden_brightvein_rallying_light",
        "name": "Rallying Light",
        "description": "Alden raises his voice and the light answers -- a rousing divine cry that simultaneously fortifies every aspect of his allies' capability.",
        "ability_type": "spirit", "level": 4,
        "elements": ["light", "electric", "air", "light"],
        "base_power": 0, "ap_cost": 100, "effect": "status",
        "status_keys": ["attack_buff", "defense_buff", "strength_buff", "dexterity_buff", "constitution_buff"], "can_aoe": True,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # LYRIC (lv95, tech/INTP)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_tech_lyric_axiom_probe",
        "name": "Axiom Probe",
        "description": "Lyric scans the target's structure and identifies a critical flaw -- exposing it for immediate exploitation.",
        "ability_type": "tech", "level": 2,
        "elements": ["electric", "dark"],
        "base_power": 0, "ap_cost": 40, "effect": "status",
        "status_keys": ["defense_debuff", "elemental_debuff", "continuous_damage"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_tech_lyric_logical_collapse",
        "name": "Logical Collapse",
        "description": "Lyric finds the internal contradiction in the target's behavior and triggers a cascade shutdown of their cognitive output.",
        "ability_type": "tech", "level": 3,
        "elements": ["electric", "dark", "air"],
        "base_power": 0, "ap_cost": 85, "effect": "status",
        "status_keys": ["intelligence_debuff", "attack_debuff", "continuous_damage"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_tech_lyric_theoretical_discharge",
        "name": "Theoretical Discharge",
        "description": "Lyric turns a theorem into a weapon -- a precise electrical discharge aimed at the exact point of maximum effect.",
        "ability_type": "tech", "level": 3,
        "elements": ["electric", "air", "dark"],
        "base_power": 95, "ap_cost": 82, "effect": "damage",
        "secondary_status": "intelligence_debuff", "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_tech_lyric_system_override",
        "name": "System Override",
        "description": "Lyric identifies the theoretical collapse point of her target's entire capability architecture and triggers all of them simultaneously -- a cold, comprehensive shutdown.",
        "ability_type": "tech", "level": 4,
        "elements": ["electric", "dark", "air", "electric"],
        "base_power": 0, "ap_cost": 125, "effect": "status",
        "status_keys": ["intelligence_debuff", "defense_debuff", "attack_debuff", "dexterity_debuff", "stun"], "can_aoe": False,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # OSTEN DREAMWEAVER (lv100, magic/INFP)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_magic_osten_dreamweaver_waking_shadow",
        "name": "Waking Shadow",
        "description": "Osten blurs the line between dream and reality around the target, confusing their senses.",
        "ability_type": "magic", "level": 2,
        "elements": ["dark", "water"],
        "base_power": 0, "ap_cost": 30, "effect": "status",
        "status_keys": ["confuse"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_magic_osten_dreamweaver_narrators_hex",
        "name": "Narrator's Hex",
        "description": "Osten narrates a different ending for the target's next action -- a dark suppression that dims their intelligence before they can act.",
        "ability_type": "magic", "level": 3,
        "elements": ["dark", "water", "air"],
        "base_power": 0, "ap_cost": 93, "effect": "status",
        "status_keys": ["intelligence_debuff", "attack_debuff", "continuous_damage"], "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_magic_osten_dreamweaver_dreamfall",
        "name": "Dreamfall",
        "description": "Osten opens a chapter of someone else's nightmare and drops the target inside it -- a dark, crushing single strike from which no dream wakes gently.",
        "ability_type": "magic", "level": 3,
        "elements": ["dark", "dark", "water"],
        "base_power": 96, "ap_cost": 82, "effect": "damage",
        "secondary_status": "confuse", "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_magic_osten_dreamweaver_the_story_that_ends",
        "name": "The Story That Ends",
        "description": "Osten narrates an ending for his target -- a dream that closes like a book, folding reality in on itself at one precise, inexorable point.",
        "ability_type": "magic", "level": 4,
        "elements": ["dark", "water", "dark", "air"],
        "base_power": 180, "ap_cost": 110, "effect": "damage",
        "can_aoe": False,
        "non_player_ability": True,
    },

    # -------------------------------------------------------------------------
    # LIRA EMBERFORGE (lv105, technique/ISFP)
    # -------------------------------------------------------------------------
    {
        "id": "lv2_unique_ability_technique_lira_emberforge_smiths_edge",
        "name": "Smith's Edge",
        "description": "Lira strikes with the controlled precision of the forge -- every blow calculated to find the seam.",
        "ability_type": "technique", "level": 2,
        "elements": ["fire", "earth"],
        "base_power": 35, "ap_cost": 30, "effect": "damage",
        "secondary_status": "defense_debuff", "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_technique_lira_emberforge_masterwork_stance",
        "name": "Masterwork Stance",
        "description": "Lira enters the focused state she uses when working on her finest pieces -- her strikes become deliberate, devastating, and artistically complete.",
        "ability_type": "technique", "level": 3,
        "elements": ["fire", "earth", "air"],
        "base_power": 0, "ap_cost": 65, "effect": "status",
        "status_keys": ["attack_buff", "dexterity_buff", "strength_buff"], "can_aoe": False,
        "non_player_ability": True,
    },
    {
        "id": "lv3_unique_ability_technique_lira_emberforge_forge_sweep",
        "name": "Forge Sweep",
        "description": "Lira swings with the full arc of the forge master -- a wide, scorching sweep that burns everything in its path.",
        "ability_type": "technique", "level": 3,
        "elements": ["fire", "earth", "fire"],
        "base_power": 82, "ap_cost": 88, "effect": "damage",
        "can_aoe": True,
        "non_player_ability": True,
    },
    {
        "id": "lv4_unique_ability_technique_lira_emberforge_primas_edge",
        "name": "Prima's Edge",
        "description": "Lira strikes with the full knowledge of every weapon she has ever forged -- a single masterwork blow that carries the weight of her craft and the truth of her soul.",
        "ability_type": "technique", "level": 4,
        "elements": ["fire", "earth", "air", "fire"],
        "base_power": 155, "ap_cost": 110, "effect": "damage",
        "can_aoe": False,
        "non_player_ability": True,
    },
]
