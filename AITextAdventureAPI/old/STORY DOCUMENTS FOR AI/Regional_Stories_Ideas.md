############# REGIONAL STORY IDEAS

 

#### Desert — dune_sundial (Ch1) — Barter/Trade resolution
    
# Sable exists in the bar on the outskirts of the first town as all heroes do
# Not sure about sundial need a hook on why she needs it to find zaruun
# quest to find sundial baked into the deliver sun dial task acquire events so the deliver process doesn't change
# sable should join the players before the dungeon, and much dialog must be added, with sable, zaruun, chock, moxie, kade, kaera, and poise


## Step 1: Meet Mara.  a character created in extended story

# mara needs to be used here.... now mira in chapter 2 was a black market dealer. mara arranges favors, introductions, and discreet exchanges
# somehow need to capitalize on that
****
Mara
mara
NPC · Extended
Source: Extended

  A smooth, well-dressed broker who operates out of Broker's Hideout. She arranges favors, introductions, and discreet exchanges for the right price.
***

## Step 2: Meet Oren.  a character from chapter 1 by the time the players can complete this quest he will be in Highsteeple Crossing

# with this task with oren I want to utilize option dialogs
# possibly 3 rounds of puzzles. guess the right answer 3x to get the sun dial.
# will need to put hints for the answers subtly in the game maybe in mara's dialog
# then it makes sense that mara gives the hints to orens puzzle and oren gives the sun dial as a reward.
***
Locations:
  Create - The Desert Metropolis - Ch.1 - Cont.1 - The Cozy Inn (inn) - main_story_ch_1_find_the_inn
  Hide - Boiling Bubble - Ch.2 - Cont.1 - main_story_ch_2_deliver_cursed_couplet_to_mira
  Show - Highsteeple Crossing - Ch.3 - Cont.1 - The Vestry Rest (inn) - main_story_ch_3_setup_npcs

An absent minded and mentally diversive dreamer.  He's not sure if he's wandering reality, or if it's wandering him.
***

## Step 3: deliver the sundial to sable, continue preexisting desert quest line as is
D:\dev\source\repos\AITextAdventure\AITextAdventureAPI\old\game\region_seeds\primary_stories\desert\desert_primary_story.py

 

 

 

#### Forest — grove_lattice (Ch2) — Puzzle/lore-solve resolution

No fight. Reuses the riddle mechanic already established with Leera in ch2 (the cursed couplet arc).

 

Task A (meet Leera): She senses the lattice is sealed behind a ward that responds to a specific phrase tied to forest lore, not force.

Task B: Player must initiate_dialog sequence where the correct dialog choice (already-known lore from her ch2 couplet riddle) unlocks it — a callback/payoff to content the player already engaged with, no new mob needed.

Leera hands over the lattice, mentions "a guardian named Thorn" who'd want this back.

 

 

 

3. Grassland — heirloom_ring (Ch3) — Skirmish resolution (keep one, for variety pacing)

This is the one that keeps a fight — reuses Talla Renn's enforcer role, thematically she's already street-justice muscle.

 

Task A (meet Talla): A petty thief just swiped the ring from a noble in the square; Talla asks you to run him down.

Task B: Quick begin_combat skirmish (no dungeon), recover ring, return it — noble gifts it to you instead ("more trouble than it's worth"), mentions "wind-witches on the steppe."

 

 

 

4. Mountain — coreforge_shard (Ch4) — Technical/investigation resolution

No fight. Marlo Finch is an auditor, not a fighter — fits his ISTJ Si/Te profile perfectly to solve this analytically.

 

Task A (meet Marlo): A foundry golem malfunctioned and locked itself down mid-diagnostic before Marlo could extract the shard.

Task B: Player has to initiate_dialog with Velka (ch4 cartographer) to get the correct shutdown sequence/rune-pattern from her map data, then return to Marlo to safely power down the golem and extract the shard — a fetch-a-clue-from-NPC-B-to-solve-NPC-A's-problem structure, no combat.

Marlo hands it over, mentions "Bragg down in the tunnels."

 

 

 

5. Shallows — moontide_orb (Ch5) — Ambush-defense resolution (the "NPC gets attacked" pattern you originally wanted — use it here)

Task A (meet Dorian Pikefall): He's nervously guarding the orb, convinced someone's been following him.

Task B: Mid-conversation, a begin_combat skirmish fires as tide-scavengers ambush Dorian directly — you defend him in the moment (no separate acquire-stage setup, it's a live interruption of the dialog scene itself). Dorian, grateful and rattled, gives you the orb as thanks.

Dorian mentions "a tide oracle" — Ripple.

 

 

 

6. Snow — boreal_clasp (Ch6) — Moral-choice/persuasion resolution

No fight. Rhett is cold and pragmatic (Ti/Se) — fits a negotiation/leverage beat rather than combat.

 

Task A (meet Rhett): He has the clasp but won't release resistance supplies to "outsiders" without proof of commitment.

Task B: Player must complete a initiate_option_dialog choice proving loyalty (echoing the ch1 pattern) — pick the option that demonstrates understanding of the resistance's cause; wrong choice loops back to the same task node (soft retry, not punished long-term), correct choice unlocks the clasp handoff.

Rhett mentions "an ice trapper" — Kor-in.

 

 

 

7. Swamp — mirethread_pendant (Ch7) — Trade/favor-chain resolution

No fight. Seth is central to this chapter already — fits a "calling in a favor" beat instead of combat.

 

Task A (meet Seth): He knows where the pendant is — with a black-market fence in Gnashwater Hollow — but the fence wants payment, not a fight.

Task B (meet a swamp city_story NPC, e.g. Madra Rotwharf from swamp_small_city_story.py if that's the assigned city, or an equivalent Gnashwater NPC): Player trades money/an existing inventory item (award_money-adjacent, e.g. spend gold or hand over cursed_couplet-tier throwaway item) for the pendant — a pure commerce resolution.

Seth or the fence mentions "a gadgeteer who deals in cursed relics" — Grimnaw.