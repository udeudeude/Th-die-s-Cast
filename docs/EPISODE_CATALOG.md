# Episode catalog and release roadmap

_Last revised 2026-10-09. Brainstorming catalog, not an approval of exact mechanics._

## Initial release slate (proposed order)

| # | Episode | Purpose | Status |
| --- | --- | --- | --- |
| 01 | **D20** | Establish seek-and-hear-a-roll behavior, approx. 30 minutes | Proposed, user to give detailed behavior |
| 02 | **2D6** | Show two-die results with authentic probability | Proposed, mechanics presentation TBD |
| 03 | **D100** | Percentile results as a general-purpose utility | Proposed, whether 1–100 vs percentile notation TBD |
| 04 | **The Wilderness Oracle** | Approx. 30 minutes of **distinct** wilderness encounters rather than a repeated 20-entry table | Proposed; develop original material |
| 05 | **Ten Minutes to Disaster** | Original ten-minute functional timer; generic enough for many games | Proposed; original cues and script TBD |

These are **not yet published**. No production dates committed. Dice variants below need explicit user review before implementation.

## Category 1: Dice & Randomizers

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
- **Compounding / nonrecursive variants**: bonus roll on first maximum only, or alternate bonus and cap mechanics, should be separately named and parameterized.
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

### Other audio randomizers

- **The Deck**: shuffled 52-card deck, multiple full permutations; potential tarot/other deck editions.
- **Hexcrawl Compass**: six hex directions, and perhaps 4/8-way compass variants.
- **Initiative Caller**: numeric or player-named orders; named players require a companion or fixed generic slots.
- **The Oracle of Small Decisions**: yes/no, coin toss, cardinal directions, colors, short choices, degrees of success.
- **Found-voice D20**: one or more real famous people saying the numbers (James Earl Jones, J.R.R. Tolkien, Tom Rosenthal's *157*, Kermit, Sesame Street performers). Research and rights clearance required before publishing, including sound recording, underlying music, character/likeness/publicity considerations. No assumed clearance from a short duration.

## Category 2: Clocks & Game Soundtracks

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

### Generic reusable timers

- **Ten Minutes to Disaster**: a themed, clear ten-minute countdown (first slate).
- **The Doomsday Clock**: escalating announcements at selected intervals.
- **Countdown Series**: clean 2, 3, 5, 10, 15, 20, 30-minute tracks, with and without periodic spoken checkpoints.
- **Turn / Phase Bell**: recurring turn-end and round-end signals.
- **Initiative / Action Clock**: predefined intervals, clear remaining-time calls.

## Category 3: Oracles & Generators

- **The Wilderness Oracle / Wilderness Encounters**: thirty-ish minutes of **nonrepeating original encounters**, not a repeated 20-entry list. Set the encounter count based on measured spoken length and usability; develop a varied master list. Include mundane, mysterious, ecological, social, and dangerous encounters.
- **Dungeon Discoveries**: new rooms, traps, objects, events, structural anomalies.
- **The Tavern**: patrons, rumors, events, overheard fragments.
- **NPC Generator**: occupation, motivation, mannerism, relationships, eccentricities.
- **Yes / No Oracle**: yes/no with optionally skewed probabilities and compound outcomes such as yes-and/no-but.
- **Weather Oracle**: setting, climate, biome, season, and escalating conditions.
- **Rumors & Secrets**: independent story hooks, revelations, misleading leads.
- **Treasure Beyond Gold**: curious possessions and objects, strange materials, inscriptions.
- **The Wizard's Laboratory**: spell mishaps, consequences, sounds, unstable experiments.
- **The Dungeon Speaks**: encounter audio heard *in-world*, rather than dry narration.
- **Random locations / monuments / factions / motives**: future additions.

### Distinctness requirement for long generator episodes

A short dice episode repeats values by design. A thirty-minute encounter stream should *not* repeat the same printed table. Every segment should offer a different original encounter within a given episode. Define seeds and repeat policy if more than one installment exists, and track duplication/near-duplication across releases.

## Category 4: Soundscapes & Audio Props

- **Ambient environments**: original forests, taverns, caverns, machinery, weather, battlefield distance, city nights.
- **Audio-only encounters**: footsteps, voices, creature calls, and noises communicate the encounter directly, perhaps with separate GM descriptions.
- **Audio clues / invisible movement**: inspired by games using sound as information, but with original game-agnostic clues.
- **In-world letters, warnings, transmissions, recordings, and magical communications**, including a recurring wizard persona when appropriate.
- **At-the-table atmosphere**: optional quiet room tone, no mandatory bed under dice oracles.
- **Guest/licensed sound libraries**: investigate Tabletop Audio, D20sounds, official game soundtracks and CC0 Freesound recordings; catalog licensing before reusing anything. Free streaming does not equal redistribution rights.

## Adjacent work, NOT an episode category

**Original games whose mechanics fundamentally involve listening to podcasts** belong in a sister project. Ideas such as a sound-deduction game, the wizard intervening unpredictably, or narrated world exploration should be transferred to the sister project's own repository and thread when pursued.

## Next editorial decisions

- Get user-specific edits to dice mechanics; defer locking full die behaviors.
- Pilot D20 at 30 minutes, audit seeking in common podcast clients.
- Write and voice-test 10–20 distinctive ultraleisurely lines, measure speech lengths and slot fairness.
- Build a prototype library of many genuinely distinct wilderness encounters before deciding full runtime.
- Identify timer cues from rulebooks, then independently author new compatible sounds.
- Investigate permissions for found celebrity samples; keep copyrighted content out of commits until cleared.
