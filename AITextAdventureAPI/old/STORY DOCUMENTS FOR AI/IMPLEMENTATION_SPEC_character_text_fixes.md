# Fracture: Character Sex, Pronoun and Equipment Text Fixes

**STATUS: IMPLEMENTED.** All sections (1-6) applied and verified against the build.

**Scope:** make every reference to the 32 playable characters and 16 Voidwalkers use the correct sex, and rewrite equipment descriptions so they describe the item, not its owner.

Checked against the build uploaded 2026-11-25. Paths are relative to `old/game/region_seeds/`; line numbers are approximate. Text only: no ids, stats or logic change.

**Contents**
1. Rulings (definitive)
2. Lira and Osten: MBTI swap (decided)
3. Playable character fixes
4. Voidwalker pronouns
5. Equipment descriptions (126 items)
6. `sex` field and verification

---

## 1. Rulings (definitive)

### 1.1 The 32 playable characters

Rule: the 16 main-story characters each represent one MBTI type. Each extended character is the **opposite sex** of the main-story character with the same type.

| MBTI | Main-story character | Sex | Extended counterpart | Sex | Status |
|---|---|---|---|---|---|
| ESTJ | Chock | M | Voss Caldera | F | OK |
| ISFJ | Kaera | F | Rynn | M | OK |
| ENTP | Moxie | F | Spark Maddox | M | OK |
| INTJ | Kade | M | Regent Sylvara | F | OK |
| ISTP | Poise | F | Ghost | M | OK |
| ISFP | Lyren Vale | F | Lira Emberforge | F | Fixed in 2 (Osten → ISFP) |
| ENTJ | Marshal Vek Drast | F | Commander Drax | M | OK |
| ISTJ | Warden Hale Brimholt | M | Anita | F | OK |
| ESFJ | Seraphine | F | Talon | M | OK |
| ENFP | Nia | F | Veyr Ashcant | M | OK |
| ENFJ | Sable | F | Alden Brightvein | M | OK |
| ESFP | Thorn | M | Andrea Starveil | F | OK |
| ESTP | Bragg | M | Dare | F | OK |
| INFJ | Ripple | F | Eldon Dawnseer | M | OK |
| INFP | Kor-in | M | Osten Dreamweaver | M | Fixed in 2 (Osten → ISFP) |
| INTP | Grimnaw | M | Lyric | F | OK |

So: **Talon, Veyr, Eldon and Alden are male; Lyric, Dare and Voss are female.**

### 1.2 The 16 Voidwalkers

All Voidwalkers are gendered. Narration and data stop calling them "it".

| Male | Female |
|---|---|
| Crux, Paradox, Cataclysm, Dominion, The Void, Scalpel, Rapture, Edict | Glamour, Revelry, Lament, Garbage, Stigma, Pageant, Oracle, Reliquary |

---

## 2. Lira and Osten: MBTI swap (decided)

Lira (ISFP) shares Lyren's type and sex; Osten (INFP) shares Kor-in's. The ruling: swap their MBTI types and rewrite the auxiliary and tertiary functions to match. Sexes, names, pronouns and art stay as they are.

### The swap

- Lira becomes **INFP** (pairs with Kor-in, M → Lira stays **F**).
- Osten becomes **ISFP** (pairs with Lyren, F → Osten stays **M**).

ISFP and INFP are both **Fi-dominant with Te inferior**, so only the auxiliary and tertiary lines change.

`extended_characters.py`, Lira's `psychology` (~line 167):

| Field | Before | After |
|---|---|---|
| `mbti` | `ISFP` | `INFP` |
| `auxiliary` | Se — Lives through the physical act of forging… | `Ne — Sees every unworked bar of metal as a field of possibilities; she imagines a dozen futures for a blade before choosing the one worth forging.` |
| `tertiary` | Ni — Quietly senses the deeper character or destiny of a piece… | `Si — Anchors her craft in remembered technique: the exact feel of every successful forging and the lesson of every failed one.` |

`extended_characters.py`, Osten's `psychology` (~line 195):

| Field | Before | After |
|---|---|---|
| `mbti` | `INFP` | `ISFP` |
| `auxiliary` | Ne — Explores endless possibilities and metaphors. | `Se — Lives each story in the moment of telling it, reading the firelight and the listener's face and reshaping the tale as it happens.` |
| `tertiary` | Si — Draws on personal memories and vivid sensory details… | `Ni — Senses the hidden shape beneath a dream or a life, and the ending a story is reaching for before anyone else does.` |

Dominant (Fi) and inferior (Te) lines stay as they are: both types share them.

### What the new functions convey

| | Lira (now INFP) | Osten (now ISFP) |
|---|---|---|
| Auxiliary | **Ne:** forges from possibility; sees what a blade *could* be | **Se:** tells stories in the moment; reads the room and the firelight |
| Tertiary | **Si:** remembered technique; every past forging is a lesson | **Ni:** senses where a dream or a life is heading |
| Feel | The idealist smith: each blade is a statement of belief | The live performer: each tale is shaped by who is listening |

Both descriptions already fit, so no description edits are needed. Lira "pours her soul into every creation" and "each blade carries a piece of what she believed", which reads INFP. Osten is "generous with meaning, reckless with truth" and lives "borrowed narratives", which reads as an in-the-moment ISFP performer.

### Enneagram

Both stay **4w5**, which suits INFP and ISFP alike. One pronoun fix in Osten's `enneagram` (~lines 204–206), which uses "their" for a male character:

| Field | Before | After |
|---|---|---|
| `core_desire` | `To understand and express their unique self.` | `To understand and express his unique self.` |
| `defense_mechanism` | `Introjection — Absorbs stories and dreams into their identity.` | `Introjection — Absorbs stories and dreams into his identity.` |


---

## 3. Playable character fixes

Exact replacements. Only the quoted text changes.

| File | Line | Character | Before | After |
|---|---|---|---|---|
| `main_characters.py` | ~190 | Poise | `…giving him a mysterious, focused calm.` | `…giving her a mysterious, focused calm.` |
| `extended_characters.py` | ~398 | Talon | `feels the pain of others as her own.` | `feels the pain of others as his own.` |
| `extended_characters.py` | ~420 | Talon | `Focuses on being central to her community.` | `Focuses on being central to his community.` |
| `city_stories/forest/forest_small_city_story.py` | ~685 | Talon | `# Place Talon so she is ready…` | `# Place Talon so he is ready…` |
| same | ~953 | Talon | `# C-1 — Talon introduces herself…` | `# C-1 — Talon introduces himself…` |
| same | ~999 | Talon | `She'll come with you if you ask.` | `He'll come with you if you ask.` |
| `city_stories/desert/desert_mid_city_story.py` | ~250–251 | Eldon | `— she has been receiving… earns her trust.` (comment) | `— he has been receiving… earns his trust.` |
| same | ~272 | Eldon | `"She reads the pattern the way I read the archive.",` | `"He reads the pattern the way I read the archive.",` |
| same | ~273 | Eldon | `"If she trusts you, tell her I said the index has a new entry."` | `"If he trusts you, tell him I said the index has a new entry."` |
| same | ~582 | Eldon | `# C-3 — Return to Eldon; she joins` | `# C-3 — Return to Eldon; he joins` |
| `city_stories/mountains/mountains_mid_city_story.py` | ~250 | Alden | `Harrock's word opens her trust — she won't` (comment) | `Harrock's word opens his trust — he won't` |
| same | ~273–275 | Alden | `"She didn't use authority — she used belief.", "Tell her I said…", "She'll know what that means."` | `"He didn't use authority — he used belief.", "Tell him I said…", "He'll know what that means."` |
| same | ~572 | Alden | Standing text: same three sentences | Same replacements as ~273–275 |

**Checked and correct (do not change):**
- `snow_primary_story.py` ~11, 57, 59, 66: "she/her" is Kor-in's wife or Lady Aeriola.
- `desert_mid_city_story.py` ~328: "She indexes the archive" is Velra.
- `main_story_chapter_12.py` ~537: "she found it in a bin" is not Kade.
- Voss, Lyric, Dare, Veyr, Rynn, Ghost, Drax, Anita, Andrea, Sylvara, Spark Maddox: their profiles and story text are already correct. Their errors are all in equipment (section 5).

---

## 4. Voidwalker pronouns

**Rule:** a pronoun that refers to a Voidwalker uses he/him/his/himself (male) or she/her/herself (female) per 1.2. Pronouns that refer to anything else (the wound, the mask, the city, a target, an idea) stay as they are.

**Optional exception:** a hero or NPC may still call a Voidwalker "it" in dialogue as a deliberate insult. If you want that, keep it rare and intentional. Narration, descriptions, abilities and psychology data always use the gendered pronoun.

### 4.1 Profile descriptions (exact)

**Crux** (`main_story/main_story_chapter_16.py` ~234–236)
```
"The Voidwalker of meaninglessness and paradox. Crux is a living contradiction - a presence that"
" unravels the logic that gives purpose its structure. He speaks in a voice of static and shattered"
" glass, targeting each person's core drive and methodically dismantling it."
```
(Only `It speaks` → `He speaks`. "its structure" is purpose's structure, so leave it.)

**Paradox** (`main_story_chapter_17.py` ~56–57)
```
" Where Crux deconstructs, Paradox entangles. He speaks in perfect logical contradictions that"
" somehow feel undeniable, and he takes a specific, predatory joy in watching coherent minds unravel."
```

**Cataclysm** (`main_story_chapter_18.py` ~28–30)
```
" Cataclysm does not hate life — he simply classifies life as an inefficiency in the equation and"
" schedules its correction with the cold, procedural certainty of a bureaucratic system that has"
" achieved total self-belief. He speaks in declarative, all-caps proclamations, each one a verdict."
```
(“its correction” is life's correction, so leave it.)

**Garbage** (`main_story_chapter_13.py` ~29)
```
"A Voidwalker that embodies self-loathing, fraudulence, and the feeling of worthlessness. She manifests as a rotting, many-mouthed shadow, whispering insecurities and lies to break her victims' spirits."
```

**Oracle** (`main_story_chapter_20.py` ~31–33)
```
" them all into a single, immutable arc. Oracle does not destroy freedom; she makes freedom feel"
" pointless by demonstrating that every choice has already been seen, catalogued, and accounted for."
" She speaks in calm, absolute declarations, each one a verdict delivered without malice. Her horror"
```

**Reliquary** (`main_story_chapter_20.py` ~61–64)
```
" and loss and holds them as sacred, unchangeable record. Reliquary does not destroy; she preserves."
" Her horror is the horror of a museum that never closes, where every wound is kept pristine under"
" glass and no one is permitted to heal. She speaks of preservation as an act of love and cannot"
" understand why her collection would not want to remain."
```

### 4.2 Story text and standing text (exact)

| File | Line | Before | After |
|---|---|---|---|
| `main_story_chapter_8.py` | ~802 | `"Scalpel. That's what they call it. And it doesn't play games."` | `"Scalpel. That's what they call him. And he doesn't play games."` |
| `main_story_chapter_9.py` | ~454 | `…You are stronger than its lies.` | `…You are stronger than his lies.` |
| `main_story_chapter_16.py` | ~387 | `Its very presence is a living paradox…` | `His very presence is a living paradox…` |
| `main_story_chapter_16.py` | ~565 and ~758 | `Crux didn't die. It just burrowed deeper.` | `Crux didn't die. He just burrowed deeper.` |
| `main_story_chapter_18.py` | ~96 and ~333 | `Cataclysm doesn't hate life. It simply sees it as a flaw in the equation. And it is very, very good at balancing equations.` | `Cataclysm doesn't hate life. He simply sees it as a flaw in the equation. And he is very, very good at balancing equations.` |
| `main_story_chapter_18.py` | ~139 | `…a colossal titan of living collapse, its form made of…` | `…a colossal titan of living collapse, his form made of…` |

### 4.3 Ability descriptions (exact)

All are `non_player_ability` entries under `player_abilities/`.

| File | Ability id | Before | After |
|---|---|---|---|
| `level_3_abilities_by_type/technique.py` | `rot_of_potential` | `Garbage drives itself into the target` | `Garbage drives herself into the target` |
| `level_4_abilities_by_type/magic.py` | `demonic_fury` | `the very contradiction of its existence` | `the very contradiction of his existence` |
| `level_4_abilities_by_type/spirit.py` | `eternal_nerve` | `Cataclysm does not rage — it endures.` | `Cataclysm does not rage — he endures.` |
| `level_4_abilities_by_type/tech.py` | `debuff_the_wicked` | `— it catalogues every contradiction` | `— he catalogues every contradiction` |
| `level_5_abilities_by_type/magic.py` | `memory_of_suffering` | `from its archive` | `from her archive` |
| `level_5_abilities_by_type/magic.py` | `hollow_silence` | `Lament does not suppress sound. It removes` | `Lament does not suppress sound. She removes` |
| `level_5_abilities_by_type/magic.py` | `self_sabotage` | `Garbage doesn't attack the target. It hands them` | `Garbage doesn't attack the target. She hands them` |
| `level_5_abilities_by_type/magic.py` | `void_lattice` | `It does not hurry. It does not need to.` | `He does not hurry. He does not need to.` |
| `level_5_abilities_by_type/magic.py` | `eternal_void` | `The Void does not strike. It arrives` | `The Void does not strike. He arrives` |
| `level_5_abilities_by_type/spirit.py` | `inescapable_fate` | `Dominion does not threaten. It informs.` | `Dominion does not threaten. He informs.` |
| `level_5_abilities_by_type/spirit.py` | `absolution` | `The Void does not offer forgiveness. It offers` | `The Void does not offer forgiveness. He offers` |
| `level_5_abilities_by_type/spirit.py` | `burden_of_the_lost` | `Reliquary opens its archive` | `Reliquary opens her archive` |
| `level_5_abilities_by_type/spirit.py` | `unwanted_knowing` | `Garbage doesn't explain or argue. It simply makes` | `Garbage doesn't explain or argue. She simply makes` |
| `level_5_abilities_by_type/tech.py` | `contradiction_loop` | `in its target` | `in his target` |
| `level_5_abilities_by_type/tech.py` | `systematic_destruction` | `Cataclysm does not strike randomly. It identifies` | `Cataclysm does not strike randomly. He identifies` |
| `level_5_abilities_by_type/tech.py` | `inevitability_matrix` | `— it calculates.` | `— he calculates.` |

### 4.4 Psychology and enneagram blocks (apply the rule)

These lines each contain at least one pronoun that refers to the Voidwalker. Change **only** those pronouns; leave others (e.g. "unmaking it" = reality).

| Voidwalker | Sex | File | Lines (~) |
|---|---|---|---|
| Crux | M | `main_story/main_story_chapter_16.py` | 241, 248, 249, 250, 251, 252, 253 |
| Paradox | M | `main_story/main_story_chapter_17.py` | 63, 65, 70, 72, 73 |
| Cataclysm | M | `main_story/main_story_chapter_18.py` | 37, 44, 45, 47 |
| Dominion | M | `world_enemies.py` | 107, 108 |
| The Void | M | `world_enemies.py` | 82, 83, 84, 85, 86 |
| Scalpel | M | `main_story/main_story_chapter_8.py` | 122, 128, 129, 130, 131 |
| Rapture | M | `main_story/main_story_chapter_11.py` | 132, 133, 134, 135, 136 |
| Revelry | F | `main_story/main_story_chapter_11.py` | 157, 158 |
| Lament | F | `main_story/main_story_chapter_12.py` | 61, 63, 65 |
| Garbage | F | `main_story/main_story_chapter_13.py` | 33, 34, 35, 36, 41, 42, 43, 45 |
| Oracle | F | `main_story/main_story_chapter_20.py` | 39, 40, 41, 42, 46, 47, 49, 50, 51 |
| Reliquary | F | `main_story/main_story_chapter_20.py` | 69, 78, 79, 81 |

Examples:
- Crux ~248: `That something genuinely has meaning and it cannot destroy it.` → `…and he cannot destroy it.`
- The Void ~83: `Denies the validity of existence itself, asserting its own power by erasing it.` → `…asserting his own power by erasing it.`
- Oracle ~51: `its entire identity is constructed around… it preserves itself by preserving the narrative.` → `her entire identity… she preserves herself by preserving the narrative.`

### 4.5 Checked and correct (do not change)

These lines matched a search but the pronoun refers to something else:
- Crux: ch16 ~16 ("meaning itself"), ~696 ("Crux is at its heart" = the Spire's heart), theme song "Everything In Its Right Place".
- Paradox: ch17 ~55 ("choice and its opposite").
- Cataclysm: ch18 ~254 ("It wasn't" = the failure); `scheduled_obliteration` ("it was always going to happen" = the strike); `calamity` ("releases it" = the entropy).
- Crux abilities `impossibility_storm`, `structural_paradox`, `logic_collapse`, `simulated_truth`, `objective_elimination`: "it" is the target, the matter or a mind.
- Paradox abilities `they_arent_who_you_are`, `paradox_embrace`, `impossible_truth`: "it" is identity, the attack or the statement.
- Rapture/Revelry ch11 ~180, ~216, ~259, ~802; abilities `blood_spectacle`, `manic_freedom`, `collapse_of_joy`, `euphoric_cascade`, `adrenaline_surge`, `thrill_addiction`, `the_rush`: "it" is the city, the festival, the storm or the strike.
- Lament/Garbage ch12 ~73, ~274; ch13 ~53, ~279; abilities `distortion_of_reality`, Lament's level 4 magic implosion.
- Stigma ch14 ~47, ~361, ~526, ~895; abilities `seductive_void`, `you_can_be_me`, `the_darkness_consuming`.
- Pageant ch15 ~440, ~955 ("it" = the stage, the mask). Edict ch15 ~125, ~472; abilities `inescapable_edict`, `system_lockdown`.
- Oracle/Reliquary ch16 ~638–639, ch20 ~614; `eternal_wound`.
- Void: ch20 ~227, ~527 ("Bracelet of Void"); `desert_primary_story.py` ~124; `eternal_void` "It is the end of the category" (= the silence).
- Glamour `instinctual_variant` ("uses it" = adoration). `world_enemies.py` ~168 ("her workshop" = Sindra).

---

## 5. Equipment descriptions

**Rule:** an equipment description describes the item: its material, construction, behaviour and history as an object. It never names a character, and never uses he/she/his/her about an owner. Generic wording ("the wearer", "whoever wears it") is fine.

126 items break the rule: 100 name a character, 26 more refer to their owner by pronoun only. Replace each item's `description` with the text below, matched by `id`. Do not change ids, names, stats or elements. These are drop-in strings (no double quotes inside).


### `armor/lv21_35.py`

| id | Name | New description |
|---|---|---|
| `barkhide_helm` | Barkhide Helm | A helm grown from hardened bark, its grain still following the shape of the branch it was cut from. |
| `rootwalker_greaves` | Rootwalker Greaves | Greaves that grip the ground like roots, anchoring a low, feral stance against any push. |
| `bogwalker_greaves` | Bogwalker Greaves | Greaves coated in slick mire-resin that lets the wearer stride through rot and sludge without sinking. |

### `armor/lv36_50.py`

| id | Name | New description |
|---|---|---|
| `flamecrest_circlet` | Flamecrest Circlet | A circlet crowned with a single raised flame-crest that pulses brighter with every surge of emotion it senses. |
| `sovereignty_circlet` | Sovereignty Circlet | An unadorned band of cold alloy, weighted to sit perfectly level without adjustment. It requires no maintenance and offers no ornament. |
| `juryrig_goggles` | Juryrig Goggles | Goggles assembled from four different models. The magnification is wrong, the tint is inconsistent and the strap is electrical tape, yet they somehow work better this way. |
| `ironfront_helm` | Ironfront Helm | A full-face war helm scored with campaign tallies. The visor slot is narrow, built for a forward view and nothing else. |
| `ironwill_helm` | Ironwill Helm | A command helmet reinforced at the brow ridge, a field modification added after a blow that came from nowhere. |
| `shroud_wrap` | Shroud Wrap | A head wrap treated with a light-absorbing compound that must be applied in exactly the right order to hold. |
| `seer_veil` | Seer's Veil | A translucent veil that softens physical vision and sharpens prophetic sight. It is meant to be worn loose. |
| `omen_hood` | Omen Hood | A deep hood stitched with sigils whose meaning reveals itself only to those who wear it long enough. |
| `executive_helm` | Executive Helm | A reinforced helmet with a brushed-alloy finish and the clean lines of a boardroom. It is not decorative. |
| `acquisition_visor` | Acquisition Visor | A tactical visor fitted with threat-assessment overlays, originally commissioned for a corporate security team. |
| `vigil_robe` | Vigil Robe | A robe worn through night vigils for those who could not wake themselves. It carries the weight of every one it kept. |
| `warden_surcoat` | Warden's Surcoat | A surcoat layered with protective weave beneath a ceremonial outer face. The ceremony has faded; the weave never has. |
| `emberstitch_coat` | Emberstitch Coat | A long coat embroidered with heat-reactive thread that glows brighter as its wearer's emotions run hotter. |
| `dominion_mantle` | Dominion Mantle | A mantle with a collar high enough to hide the jaw, leaving the wearer's expression unreadable. |
| `vanguard_breastplate` | Vanguard Breastplate | A breastplate scored by thirty-one known engagements, each dent left in place as a record. |
| `shadow_weave_coat` | Shadow-Weave Coat | A long coat woven with light-absorbing composite. It doesn't make anyone invisible; it makes the eye slide past. |
| `null_jacket` | Null Jacket | A reinforced jacket treated to suppress heat signature and sound resonance, built to a specification no one has explained. |
| `oracle_mantle` | Oracle's Mantle | A mantle whose weave dampens the physical shock of seeing too far ahead, made for visions that are going to be difficult. |
| `acquisition_plate` | Acquisition Plate | A reinforced plate commissioned for hostile-environment negotiations, the kind expected to go badly. |
| `leverage_harness` | Leverage Harness | A heavy tactical harness designed to carry field equipment and stop bullets. Both functions are intended. |
| `currentflow_bracers` | Currentflow Bracers | Bracers that guide healing energy along the forearms with a current like standing in a slow river. |
| `shelter_bracers` | Shelter Bracers | Bracers etched with names: not enemies, but the people the wearer stands in front of. |
| `covenant_bracers` | Covenant Bracers | Bracers woven with a single faith-binding, a promise made once and never revisited. |
| `current_gloves` | Current Gloves | Thin gloves woven with conductive thread, built to test charge paths without burning the hands. They work about sixty percent of the time. |
| `ironveil_vambraces` | Ironveil Vambraces | Slim black-alloy vambraces etched with dimming micro-runes. They channel dark current along the forearm without a flicker of warmth. |
| `traceless_gloves` | Traceless Gloves | Thin leather gloves with grip-coated palms. They wear out fast, so they are rarely found as a single pair. |
| `dawnseer_gloves` | Dawnseer Gloves | Soft gloves with bare fingertips, made for keeping contact with vision-surfaces during a reading. |
| `boardroom_gauntlets` | Boardroom Gauntlets | Armored gloves with a polished finish that signal the meeting is already over. |
| `meadowstep_greaves` | Meadowstep Greaves | Greaves grown from living fibre that flex without resistance, moving with the wearer rather than behind them. |
| `guardian_greaves` | Guardian Greaves | Greaves built wide at the shin to shield the stance, made for holding ground rather than advancing. |
| `keeper_greaves` | Keeper Greaves | Greaves etched with a repeating keep-glyph down the shin, one repetition for each vigil that should not have been survived. |
| `cinder_greaves` | Cinder Greaves | Greaves baked in forge-heat until the alloy fused with the fire-coating. They always run warm. |
| `coldmarch_greaves` | Coldmarch Greaves | Greaves of matte obsidian plate, balanced to make no sound on any surface. |
| `circuit_greaves` | Circuit Greaves | Greaves with exposed charge-routing along the outer shin, added to stop the legs from overloading. |
| `siege_sabatons` | Siege Sabatons | Heavy sabatons with reinforced toe-caps for sustained pushing engagements. The toe-caps take most of the wear. |
| `silent_step_boots` | Silent-Step Boots | Boots with a sound-dampening sole compound applied in three careful layers. |
| `seer_boots` | Seer's Boots | Soft boots made for moving through a vision, proof that standing still during prophecy is a choice, not a necessity. |
| `takeover_sabatons` | Takeover Sabatons | Heavy sabatons fitted with pressure-monitoring soles that measure exactly how hard each step lands. |

### `armor/lv51_65.py`

| id | Name | New description |
|---|---|---|
| `reckless_bandana` | Reckless Bandana | A salt-bleached bandana worn so long it has absorbed a faint, permanent static charge. |
| `caretaker_hood` | Caretaker's Hood | A soft hood worn low over the brow, not for concealment but so patients can't see the worry underneath. |
| `field_medic_cap` | Field Medic's Cap | A plain soft cap with a medic cross stitched on the brow, faded from years of use and still pressed flat. |
| `cipher_hood` | Cipher Hood | A deep hood stitched with ledgers in invisible ink, a private shorthand only its author can read. |
| `archivists_hood` | Archivist's Hood | A deep hood with a reinforced brim for reading in low light, its scholar's lining replaced with classified-grade weave. |
| `fieldmedic_wrap` | Field Medic's Wrap | A wrap of layered healing cloth with trauma-response panels and pockets organized for reaching without looking. |
| `archive_coat` | Archive Coat | A long coat with ledger-pockets sewn into the lining, each one holding something exact. |
| `crypt_recorded_coat` | Crypt-Recorded Coat | A coat whose lining is printed with the full text of a library of classified documents. The print is very small. |
| `rigging_bracers` | Rigging Bracers | Bracers threaded with ship-rigging cord wound tight enough to deflect blows, tied with a knot that can be done one-handed. |
| `corsair_bracers` | Corsair Bracers | Bracers built from corsair-standard boarding kit, reinforced at the outer face, weighted at the wrist, with knuckle plating added later. |
| `steadyhands_bracers` | Steadyhands Bracers | Bracers fitted with micro-stabilizers designed to counter tremor under stress. |
| `steadfast_wraps` | Steadfast Wraps | Compression wraps reinforced with stabilizer thread, tight enough to steady a needle hand and loose enough to flex for a carry. |
| `ledger_bracers` | Ledger Bracers | Bracers etched on the inside with a compressed index, readable in the dark by touch. |
| `ledger_vambraces` | Ledger Vambraces | Heavy vambraces with an indexed inner etching, made to protect the information as much as the arm. |
| `breakneck_boots` | Breakneck Boots | Boots built for sustained high-speed movement across unstable terrain. The ankle reinforcement has been extended twice. |
| `wavechaser_boots` | Wavechaser Boots | Boots designed for shoreline pursuit: grip-plated sole, sealed ankle, no heel to catch on wet rock. |
| `surefoot_sandals` | Surefoot Sandals | Simple woven sandals with pressure-spreading soles, easy to remove in the field and made to last for years. |
| `hearthstep_boots` | Hearthstep Boots | Soft-soled boots that carry a faint warmth at the insole regardless of temperature. No one knows why. |
| `vault_boots` | Vault Boots | Heavy-soled boots with concealed document compartments in the heels. The most valuable thing is never carried in the hands. |
| `vaultwalker_boots` | Vaultwalker Boots | A reinforced variant of the Vault Boots with extended heel compartments and a secondary compartment in the tongue. |

### `armor/lv66_80.py`

| id | Name | New description |
|---|---|---|
| `spotlight_wreath` | Spotlight Wreath | A wreath of compressed light-wire made to look celebratory. It draws every eye in a room toward its wearer and away from everything else. |
| `compassion_circlet` | Compassion Circlet | A circlet of pale silver set with a soft-glow healing stone at the brow. Patients often reach for it before they reach for a hand. |
| `warmth_cowl` | Warmth Cowl | A deep cowl woven from sun-linen that holds ambient heat and releases it slowly, warm enough to bring a cold patient back before treatment. |
| `ovation_leathers` | Ovation Leathers | Performance leathers built to take applause and impact in equal measure, with a raised collar that keeps the face visible to the crowd. |
| `gentlehand_bracers` | Gentlehand Bracers | Slim bracers padded on the inner face for patient handling, built to steady a trauma wound without adding pressure. |
| `starchasers_boots` | Starchasers' Boots | Boots with soles inlaid with compressed starfall crystal. Every exit in them feels like an arrival. |
| `softstep_sandals` | Softstep Sandals | Sandals soled with healing-foam derived from compress material, the quietest footwear in any room. That is on purpose. |
| `softpath_sandals` | Softpath Sandals | Sandals woven to carry no sound and leave no impression, so a patient is never startled by an approach. |

### `armor/lv81_105.py`

| id | Name | New description |
|---|---|---|
| `rallying_crown` | Rallying Crown | A crown of interlocked light-bands, each band added for a group pulled back from the edge. No one has counted them in years. |
| `theorem_circlet` | Theorem Circlet | A circlet engraved with seven unfinished theorems. Proofs tend to appear in the margins of every surface nearby when it is worn. |
| `abstract_lens_headset` | Abstract Lens Headset | A custom headset with multi-focal lenses for reading seven things at once. Most people see one thing through it; the right mind sees the structure underneath. |
| `dreamveil_crown` | Dreamveil Crown | A crown woven from sleep-silk harvested from a dreamweaver spider that died mid-dream. |
| `reverie_hood` | Reverie Hood | A hood woven from reverie-thread, a material spun in the state between sleep and waking, made for the stories that matter most. |
| `smithsong_helm` | Smithsong Helm | A full-face forge helm made on the night of a first masterwork. The inside is engraved with the exact temperature at which steel sings. |
| `artisan_helm` | Artisan's Helm | A lighter forge helm built for precision work, with an adjustable face-guard and a low-cut brow ridge for leaning into the work. |
| `inspirator_robe` | Inspirator Robe | A robe with resonance chambers sewn into the chest panel. Voices carry further and spells radiate greater warmth when it is worn. |
| `brightweave_mantle` | Brightweave Mantle | A mantle woven from brightweave, a material that radiates a faint warmth without heat. People lean toward whoever wears it. |
| `paradox_robe` | Paradox Robe | A robe that appears to be two overlapping garments that should cancel each other out. They don't. The theory as to why runs to eleven pages of footnotes. |
| `logic_lattice_robe` | Logic Lattice Robe | A robe whose structure follows a formal logical proof, each layer of weave a conditional statement. The proof is valid. |
| `storywoven_robe` | Storywoven Robe | A robe made from cloth that carries the impressions of stories told while wearing it. The patterns shift slowly, over days, as the stories change. |
| `folklore_robe` | Folklore Robe | A robe embroidered with scenes from old fireside stories. The embroidery moves when no one is watching. |
| `embercraft_coat` | Embercraft Coat | A thick leather work coat fused with forge-tempered metal panels along every strike zone. It was made to outlast its maker. |
| `masterwork_apron` | Masterwork Apron | A forge apron built from the same materials as a masterwork blade. It has taken every heat, splash and spark and still looks new. |
| `rallying_bracers` | Rallying Bracers | Bracers engraved with a full-circle motif, one mark for every person pulled back from the edge. The circle isn't closed yet. |
| `goldvein_bracers` | Goldvein Bracers | Bracers threaded with compressed goldvein ore, a material that conducts inspiration the way copper conducts current. |
| `axiom_bracers` | Axiom Bracers | Bracers inscribed with fundamental logical axioms, not for reference but as a reminder of what is actually true. |
| `theorem_bracers` | Theorem Bracers | Bracers etched with partial theorems: the working assumptions to a matching circlet's conclusions. |
| `reverie_bracers` | Reverie Bracers | Bracers that hum faintly with a lullaby composed from a dream that came twice. It has never been written down. |
| `dreamthread_bracers` | Dreamthread Bracers | Bracers woven from dreamthread spun during an extended trance. The pattern carries the structure of a story that hasn't been told yet. |
| `forgegrip_gauntlets` | Forgegrip Gauntlets | Heavy forge gauntlets rebuilt four times over, each iteration slightly heavier than the last. The weight keeps the work honest. |
| `soulforge_gauntlets` | Soulforge Gauntlets | Gauntlets forged in a single sitting of pure intent. The metal remembers why it was made, and they are kept for work that matters. |
| `brightpath_sandals` | Brightpath Sandals | Sandals whose straps glow faintly when walking toward someone in need. Officially this is not a magical effect. The sandals disagree. |
| `inspirer_greaves` | Inspirer Greaves | Greaves fitted with a resonance channel at the knee. Every forward step carries a faint harmonic that others nearby can feel but not quite name. |
| `postulate_boots` | Postulate Boots | Boots reinforced with a compound synthesized from first principles. It has no name yet; the paper is still being written. |
| `analysis_greaves` | Analysis Greaves | Greaves with sensor-thread woven into the shin panel that map terrain pressure and feed it to a linked headset, so the wearer never needs to look down. |
| `wanderer_sandals` | Wanderer's Sandals | Sandals that have walked a great many roads, repaired in a dozen places, each repair from a different stop. |
| `wanderer_wraps` | Wanderer's Wraps | Leg wraps pieced together from travel-cloth collected at every significant stop along the way. |
| `hammerfall_boots` | Hammerfall Boots | Steel-toed forge boots with anti-vibration soles, designed for twelve straight hours at the anvil. |
| `forgestride_boots` | Forgestride Boots | A field-modified Hammerfall with a lighter sole and higher ankle, built for moving between forge stations fast enough to catch a falling casting. |

### `weapons/lv36_50.py`

| id | Name | New description |
|---|---|---|
| `blazeheart_staff` | Blazeheart Staff | A twin-core variant of the Flameheart: two preserved embers wound together, their competing heat creating an unstable surge that takes skill to channel. |
| `scepter_of_dominion` | Scepter of Dominion | A ceremonial scepter whose grip is wrapped in compressed void-thread. It was never meant to be carried openly. |
| `voltage_wrench` | Voltage Wrench | An oversized wrench rebuilt with conductive plating and a charge accumulator in the handle. It was a repair tool once. It has been improved. |
| `shockdart_launcher` | Shockdart Launcher | A wrist-mounted launcher built from salvage that fires compressed-charge darts at range. The safety toggle went missing several versions ago. |
| `command_greataxe` | Command Greataxe | A two-handed greataxe forged in a forward operating base under active siege. The haft is wrapped in field-stripped uniform cord taken from the soldiers who held the line. |
| `wardens_claymore` | Warden's Claymore | A claymore bearing the warden crest, commissioned as a promotion gift. Its owners tend to outgrow the rank and keep the sword. |
| `phantom_edge` | Phantom Edge | A single-edge variant of the Phantom Blade with a thinner profile, a silent draw and a shaved-down spine that only the right grip can hold at the proper angle. |
| `omen_staff` | Omen Staff | A gnarled staff grown from a tree struck by lightning at the exact moment of a fracture event. Visions pass through it first. |
| `seer_focus_wand` | Seer's Focus Wand | A short wand carved from vision-bone, a material that softens at the moment of prophecy and hardens again when the vision resolves. It works best kept against the palm. |
| `leverage_maul` | Leverage Maul | A heavy maul cast in the same foundry as a corporate seal. Its head is shaped like a gavel. This was intentional. |

### `weapons/lv51_65.py`

| id | Name | New description |
|---|---|---|
| `tiderunner_blades` | Tiderunner Blades | A matched pair of short blades balanced for dual-wield at speed. The off-hand blade is weighted heavier to even out the spin. |
| `mending_staff` | Mending Staff | A staff grown from a single branch of a living tree that has never stopped healing itself. It is often kept wrapped in bandages between uses. |
| `mending_scepter` | Mending Scepter | A shorter scepter variant of the Mending Staff, easier to manage in tight field conditions. The head doubles as a splinting post. |
| `cryptseal_blade` | Cryptseal Blade | A short broad-blade etched with classified registry marks. Each mark is a file that was never returned. |
| `codex_blade` | Codex Blade | A blade etched with the index of a private codex that no longer exists anywhere else. The blade is the only copy. |

### `weapons/lv66_80.py`

| id | Name | New description |
|---|---|---|
| `morale_blade` | Morale Blade | A single-edged performance saber engraved on both sides with names: two different lists of people kept moving forward. |
| `encore_blades` | Encore Blades | A matched pair of performance sabers, one for the show and one for what comes after. Over time the difference stopped mattering. |
| `mercy_staff` | Mercy Staff | A staff carved from a fallen healer's tree of an uncatalogued species. It blooms with pale flowers when near the dying. |
| `kindness_staff` | Kindness Staff | A staff whose grip is re-wrapped by hand every season. The wood has absorbed so much healing energy it glows faintly on overcast days. |

### `weapons/lv81_105.py`

| id | Name | New description |
|---|---|---|
| `voice_of_valor_staff` | Voice of Valor Staff | A staff that resonates at the frequency of collective will. Words spoken through it remind people why they started. It has ended more fights than it has begun. |
| `collapse_staff` | Collapse Staff | A staff built from the structural core of an institution that collapsed under its own contradictions, recovered from the rubble. |
| `axiom_focus_rod` | Axiom Focus Rod | A rod machined to exacting dimensional specifications, with tolerances tighter than anything commercially available. The resonance chamber was measured three times. |
| `dreamer_staff` | Dreamer's Staff | A staff carved from driftwood that floated into a camp one morning with no shore in reach. Its story is still being told. |
| `storyteller_staff` | Storyteller's Staff | A staff for when a story needs witnesses. It hums at a frequency that makes people lean in, and spells cast through it sound like narration. |
| `masterwork_blade` | Masterwork Blade | A blade made at the moment a smith finally understood the craft. Everyone who has held it agrees something changed. |
| `prima_blade` | Prima Blade | The first blade a master smith chose to keep. Hundreds have been made since. None of them are this one. |

---

## 6. `sex` field and verification

### 6.1 Add a `sex` field (data only)

Purpose: a plain, unambiguous record of each character's sex so future AI agents and writers stop guessing from names or art. **No game mechanics read it. No validator or dev TUI check is added.**

Add `"sex": "M"` or `"sex": "F"` as a top-level key, next to `name`, in every profile dict:

| File | Profiles |
|---|---|
| `main_characters.py` | The 16 main-story characters |
| `extended_characters.py` | The 16 extended characters |
| `main_story/` chapter files | The Voidwalker profiles defined there |
| `world_enemies.py` | Dominion, The Void |

Values are exactly those in section 1 (1.1 and 1.2).

**Why saves are safe:** these profile dicts are static seed data. Recruiting a character doesn't copy the dict into the `Player` object, and the dev TUI reads profile keys with `.get()`, so an extra key is ignored everywhere. No `__setstate__` backfill, no save migration, no version bump. Do not add a `sex` attribute to `Player`, `Hostile` or any other pickled class.

### 6.2 Verification after the edits

1. Search `armor/` and `weapons/` descriptions for every character name and for he/she pronouns: zero hits.
2. Search for `Talon` and `Alden` with she/her in the same sentence: zero hits.
3. The Voidwalker profile descriptions for Crux, Paradox, Cataclysm, Garbage, Oracle and Reliquary contain no standalone "It"/"Its" referring to the Voidwalker.
4. Lira shows `INFP` and Osten shows `ISFP`; every MBTI type now has one male and one female across the main-story and extended casts.
5. All 48 profiles have a `sex` key set to `M` or `F`.
6. An existing save loads without errors; the equipment and character screens show the new text.
