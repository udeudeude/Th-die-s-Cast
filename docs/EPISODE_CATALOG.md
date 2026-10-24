# Episode catalog and release roadmap

_Updated 2026-10-24. Published and provisional mechanics are distinguished below; unproduced entries remain exploratory._

## Five-episode pilot feed (first released 2026-10-11)

Subscribe by URL: **https://udeudeude.github.io/thdies-cast/feed.xml**

These five numbered **pilot episodes are published for listening and feedback** with **Brother Rubicon** and the Saved 02 Lewis voice treatment. They do not settle every future mechanic.

| # | Episode | Pilot implementation |
| --- | --- | --- |
| 01 | **D20** | 360 values in 18 reshuffled permutations of 1–20, 5-second fixed slots; **not independent adjacent rolls** |
| 02 | **2D6** | 300 rolls of two independent D6s, speaking both faces and the sum, 6-second slots |
| 03 | **D100** | 300 independent uniformly selected integers 1–100 (inclusive), 6-second slots |
| 04 | **The Wilderness Oracle** | 80 original, individually narrated encounters from `manuscripts/WILDERNESS_ORACLE_80.md`; short natural pauses without chimes, no spoken titles/numbers |
| 05 | **Ten Minutes to Disaster** | Ten-minute original synthesized functional score with timed voice landmarks, a completion bell at 10:00, then an optional coda |

Source and distribution files: [five-episode production folder](https://github.com/udeudeude/udeudeude.github.io/tree/main/thdies-cast). Podcast-only playback: no companion app is needed. New standard dice and format decisions below remain under review.

## Additional balanced dice editions (first released October 23, 2026)

Eight more full-length audio recordings are published in the [same subscription feed](https://udeudeude.github.io/thdies-cast/feed.xml). Each opens with an original short observation, followed by the fixed wording **“I am Brother Rubicon. The die's cast.”**, and uses a different closing remark. The endings are deliberately not disclosed in public episode descriptions.

| # | New edition | Fairness construction | Results-only length |
|---|---|---|---|
| 06 | D20 · Shuffled Sets | 18 independent shuffles of 1–20 (360 outcomes) | 30:00 |
| 07 | D20 · One Giant Shuffle | 18 copies of each face in a single randomized pool (360 outcomes) | 30:00 |
| 08 | D20 · Every Possible Pair | Order-two de Bruijn cycle: every ordered pair once (400 outcomes, including doubles) | 33:20 |
| 09 | 2D6 · Thirty-Six Possibilities | 10 permutations of all 36 ordered pairs (360 outcomes) | 30:00 |
| 10 | D100 · Three Complete Shuffles | Three permutations of values 1–100 (300 outcomes) | 30:00 |
| 11 | D4 · Four Paths | 90 permutations of 1–4 (360 outcomes) | 30:00 |
| 12 | D8 · Eight Paths | 45 permutations of 1–8 (360 outcomes) | 30:00 |
| 13 | D12 · Twelve Paths | 30 permutations of 1–12 (360 outcomes) | 30:00 |

Each provides *exact frequencies across the functional recording*, conditional on selecting uniformly distributed time slots. Sequential results are generally not independent, and hand-operated seeking may not be uniform. The original D20 remains a valid full episode using balanced shuffled sets. Only the original 2D6 and D100 are archival experiments: they used fair generators, but their fixed recordings are not globally balanced (the original D100 omits six possible numbers).

- [All eight playable editions and method notes](https://udeudeude.github.io/thdies-cast/dice-methods/)
- [Versioned production manifest with precise sequences](https://github.com/udeudeude/udeudeude.github.io/blob/main/thdies-cast/dice-methods/manifest.json)


## Encounter oracle expansion (October 24, 2026)

- **Episode 14, Creatures Behaving Strangely:** 80 independent, original scenes about strange animal conduct, available in the same subscription feed. [Canonical manuscript](../manuscripts/CREATURES_BEHAVING_STRANGELY_80.md).
- **Episode 15, Relics and Curiosities:** 80 independent, original scenes about peculiar portable artifacts. [Canonical manuscript](../manuscripts/RELICS_AND_CURIOSITIES_80.md). Its narrated release is in production.
- **Wilderness Oracle:** still 80 independent scenes. The synthetic chimes were removed, long gaps shortened, and the spoken instruction to wait for chimes is being replaced.
- All three encounter oracles use **no synthetic transition sounds**, no spoken entry numbers/titles, and approximately 0.85-second natural separation. Only complete encountered scenes are usable after seeking.

## Category 1: Dice & Probability Tools

### Standard dice

- **D4**, **D6**, **D8**, **D10**, **D12**, **D20**, **D100**: initially discussed as ≈30-minute series in which each complete set of faces appears in randomized order, repeated with new shuffles. User intends to specify modifications to some items.
- **2D6**: two actual dice, not uniformly selected totals. Independently uniform values 1–6; totals 2–12 have a triangular distribution. Whether read faces, sum, or both remains open.
- **3D6**: ability scores and many roll-under systems. Read faces and/or sum TBD.
- **4D6 drop lowest**: typical character creation mechanism; presentation and arithmetic TBD.
- **D20 advantage** and **D20 disadvantage**: roll two D20s, use higher or lower. Explicitly state both and selected value? TBD.
- **D66**: two distinguishable D6s used as digits, results 11–16, 21–26, …, 61–66, not a 2D6 sum.
- **D2/coin flip**, **D3**: binary and three-way oracles.
- **4dF (Fate/Fudge)**: four −1/0/+1 dice, sum range −4 to +4.
- **2D10**, **2D20**, **D24**, **D30**, plus unusual polyhedra, specialist notation or dice sets.

### Exploding dice

- **Exploding D6**: if the D6 maximum (6) appears, add it and roll again. A repeated maximum explodes again where the chosen ruleset permits. Example chain: 6+6+3=15; this is a **15**, not a D6 face. More than one definition of exploding dice exists.
- **Exploding D20**: analogous behavior on 20 **for a ruleset that explicitly calls for it**; it is not a general D20 rule. Example 20+20+14=54.
- **Alternative explosion variants**: bonus roll on first maximum only (nonrecursive), recursive additional rolls, and other game-specific compounding or cap mechanics should each be named, described and parameterized. 'Compounding' is not by itself a reliable synonym for 'nonrecursive'.
- **Presentation candidate 1 (preferred for seekability):** one fully resolved outcome per seekable slot, announcing chain and/or sum. Internally generate independently random dice until a non-maximum is rolled.
- **Presentation candidate 2:** speak the maximum and cue users to continue listening to subsequent rolls; visually simple but seeks and randomization can break sequence semantics.
- **Presentation candidate 3:** precompute full explosion chains as standalone sequences; concatenate onto the timed track. If a cap on chaining exists for practical runtime, clearly announce rule before ending rather than silently altering probabilities.
- A true exploding distribution is **unbounded**. Truncating chains or treating each finite possible total as equiprobable is incorrect. The exact policy remains to be defined and approved.

### Pools and conversions

- **Exploding D6 pool** (pool size TBD), **success-counting D6 pools** (e.g. Shadowrun mechanics, edition-specific), **highest-die pool** (e.g. Blades in the Dark style), **roll-under** and threshold decisions.
- **Keep/drop high/low**, **critical/fumble** commentary, percentile two-die notation, and conditional reroll mechanics.
- Any named system demands edition-specific verification before claiming rules compatibility.

### Listening modes

1. **Quick:** minimal introduction, succinct spoken value, short interval; actual timings TBD.
2. **Leisurely:** relaxed pauses, still direct and unambiguous.
3. **Ultra-leisurely:** a wizard performs varied characterful monologues around each outcome, in the spirit of:
   - 20: “Magnificent. Twenty. The universe has briefly abandoned its customary indifference toward you.”
   - 19: “Nineteen! An admirable result. Perfection, naturally, would have been vulgar.”
   - 10: “Ten. Precisely the sort of result from which uncertainty derives its livelihood.”
   - 2: “Two. The dice are displaying a troubling lack of confidence in your enterprise.”
   - 1: “One. Oh, unfortunate. Even the laws of probability appear embarrassed.”
   These are **working examples**, not locked final script.
   Make multiple original lines for every outcome to avoid the same wording repeatedly. Use equally long time slots even when comments vary substantially in length, so time-based seeking does not favor long results.

## Category 2: Cards & Other Randomizers

- **The Deck**: shuffled 52-card deck, multiple full permutations; potential tarot/other deck editions.
- **Hexcrawl Compass**: six hex directions, and perhaps 4/8-way compass variants.
- **Initiative Caller**: numeric or player-named orders; named players require a companion or fixed generic slots.
- **The Oracle of Small Decisions**: yes/no, coin toss, cardinal directions, colors, short choices, degrees of success.
- **Found-voice D20**: one or more real famous people saying the numbers (James Earl Jones, J.R.R. Tolkien, Tom Rosenthal's *157*, Kermit, Sesame Street performers). Research and rights clearance required before publishing, including sound recording, underlying music, character/likeness/publicity considerations. No assumed clearance from a short duration.

## Category 3: Encounter Streams

- **The Wilderness Oracle / Wilderness Encounters:** eighty original independent scenarios drafted as a first ~30-minute manuscript, no repetition of a smaller list. Printed numbers and titles are **not read** aloud. Entries contain enough setting and decision texture to use by themselves.
- **Dungeon Encounters, Road Encounters, Urban Encounters, Social Encounters:** related all-unique collections.

## Category 4: Oracles & Decision Aids

- **Yes / No Oracle**: yes/no with optionally skewed probabilities and compound outcomes such as yes-and/no-but.

### Distinctness requirement for long generator episodes

A short dice episode repeats values by design. A thirty-minute encounter stream should *not* repeat the same printed table. Every segment should offer a different original encounter within a given episode. Define seeds and repeat policy if more than one installment exists, and track duplication/near-duplication across releases.

## Category 5: Characters, Locations & Worlds

- **Dungeon Discoveries**: new rooms, architectural anomalies, broken rituals and curious objects.
- **The Tavern**: patrons, rumors, disturbances and overheard fragments.
- **NPC Generator**: occupation, motive, mannerism, distinguishing detail and relationship.
- **Weather Oracle**: conditions weighted by climate, season and terrain.
- **Rumors & Secrets**: hooks, scandals, revelations and misleading leads.
- **Treasure Beyond Gold**: odd possessions, inscriptions and discoveries.
- **The Wizard's Laboratory**: experiments, spell mishaps and unstable apparatus.
- **Random locations, monuments, factions and settlements**: generated situation and place.

## Category 6: Timers, Countdowns & Clocks

### Generic reusable timers

- **Ten Minutes to Disaster**: a themed, clear ten-minute countdown (first slate).
- **The Doomsday Clock**: escalating announcements at selected intervals.
- **Countdown Series**: clean 2, 3, 5, 10, 15, 20, 30-minute tracks, with and without periodic spoken checkpoints.
- **Turn / Phase Bell**: recurring turn-end and round-end signals.
- **Initiative / Action Clock**: predefined intervals, clear remaining-time calls.

## Category 7: Game-Specific Audio Controllers

### Game-specific candidates

- **Escape: The Curse of the Temple**: original compatible timer with correct warning/recall cues and overall playtime; confirm exact cue schedule against official rules.
- **FUSE**: original ten-minute bomb/clock-themed timer, possibly with a computer voice and escalating urgency. Don't copy official sound assets.
- **5-Minute Dungeon**, **5-Minute Marvel**, **5-Minute Mystery**: five-minute phase clocks and reminders.
- **Flatline**: time-critical emergency soundtrack.
- **Project: ELITE**: short recurring action-phase clocks.
- **Space Alert**: synchronized mission/event announcements; straightforward fixed podcasts unlikely to cover all randomized mission configurations.
- **One Night Ultimate Werewolf** (and expansions): role-dependent nighttime moderator; see `PRODUCTION_PLAN.md` for hybrid model.
- **XCOM: The Board Game**: investigate timed-app orchestration, probably too interactive for static podcast replication.
- **Nightmare / Atmosfear**: references for a voice that interrupts gameplay, not a promise of replacement.
- **Stop Thief!**: sound clues are rules-bearing; reference for potential original clues, not an unlicensed recreation.

## Category 8: Atmospheres & Environments

- Original forests, taverns, caverns, machinery, distant battle, weather, urban nights and room tone; optional pure ambience, no intrusive bed under spoken dice.

## Category 9: Audio Clues & In-World Props

- **Audio-only encounters**: footsteps, voices, creature calls, and noises communicate the encounter directly, perhaps with separate GM descriptions.
- **Audio clues / invisible movement**: inspired by games using sound as information, but with original game-agnostic clues.
- **In-world letters, warnings, transmissions, recordings, and magical communications**, including a recurring wizard persona when appropriate.
- **At-the-table atmosphere**: optional quiet room tone, no mandatory bed under dice oracles.
- **Guest/licensed sound libraries**: investigate Tabletop Audio, D20sounds, official game soundtracks and CC0 Freesound recordings; catalog licensing before reusing anything. Free streaming does not equal redistribution rights.

## Category 10: Archival & Special Editions

- **Found-voice D20**, other verified public-domain/cleared celebrity recordings, eccentric Lewis narrator modes, collage editions. A specific clip's legal reuse and intelligibility must be confirmed before inclusion.

## Adjacent work, NOT an episode category

**Original games whose mechanics fundamentally involve listening to podcasts** belong in a sister project. Ideas such as a sound-deduction game, the wizard intervening unpredictably, or narrated world exploration should be transferred to the sister project's own repository and thread when pursued.

## Next editorial decisions

- Get user-specific edits to dice mechanics; defer locking full die behaviors.
- Pilot D20 at 30 minutes, audit seeking in common podcast clients.
- Write and voice-test 10–20 distinctive ultraleisurely lines, measure speech lengths and slot fairness.
- Build a prototype library of many genuinely distinct wilderness encounters before deciding full runtime.
- Identify timer cues from rulebooks, then independently author new compatible sounds.
- Investigate permissions for found celebrity samples; keep copyrighted content out of commits until cleared.
