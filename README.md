# Th’die’s Cast

**A podcast of useful audio tools for tabletop gaming.**

Not primarily a show to *listen to*: a collection of audio instruments you can use at the table. Seek to a random point for a die roll or oracle result; play a timer that runs the table; cue an encounter, a clue, or a soundscape. Created as a lightweight, ordinary podcast alternative to installing large specialized game apps.

**Current host:** **Brother Rubicon**, synthesized from Kokoro British male `bm_lewis`, with the producer-selected **Saved 02 · Natural pitch, light room** settings. The separate offline effects chain approximates the Voice Lab preset; the final master is subject to listening feedback.

**Spoken show title:** “The die's cast.” (audition take 02). **Character name and voice:** Brother Rubicon, until further notice.

**Production voice editor:** [Lewis Voice Lab](https://udeudeude.github.io/voice-lab/) is a standalone browser-based production tool, linked from the [Ude Projects directory](https://udeudeude.github.io/). Its source and the two audition recipes saved on October 11, 2026 are [permanently tracked in GitHub](https://github.com/udeudeude/udeudeude.github.io/tree/main/voice-lab/presets). The voice editor is **not** required for podcast playback.

**Hidden D20 pilot epilogue:** A brief, deliberately unexpected coda follows the 360 genuine rolls; the coda is not a game result. Avoid disclosing its contents in public episode notes.

## Planning documents

- [Show identity, categories, and boundaries](docs/SHOW_BIBLE.md)
- [Ten unselected Brother Rubicon introduction options](docs/BROTHER_RUBICON_INTRO_OPTIONS.md)
- [Comprehensive episode catalog and proposed first releases](docs/EPISODE_CATALOG.md)
- [Production design and open implementation decisions](docs/PRODUCTION_PLAN.md)
- [Reference games, audio sources, and rights research](docs/REFERENCES_AND_RIGHTS.md)
- [Public-domain recorded-voice shortlist](docs/PUBLIC_DOMAIN_VOICE_SOURCES.md)
- [Companion app size research backlog](docs/COMPANION_APP_SIZE_SURVEY_TODO.md)
- [Wilderness Oracle: 80 original encounter scripts](manuscripts/WILDERNESS_ORACLE_80.md)
- [Creatures Behaving Strangely: 80 encounter scripts](manuscripts/CREATURES_BEHAVING_STRANGELY_80.md)
- [Relics and Curiosities: 80 encounter scripts](manuscripts/RELICS_AND_CURIOSITIES_80.md)
- [Audio production runbook: the existing GitHub Actions studio](docs/AUDIO_PRODUCTION_RUNBOOK.md)
- [Seed for a separate audio-native games project](docs/SISTER_PROJECT_SEED.md)

## Listen: 15-episode podcast (dice, three encounter oracles, and a countdown)

**Subscribe in Apple Podcasts by URL:** `https://udeudeude.github.io/thdies-cast/feed.xml`

- [Open the simple podcast listening and feed page](https://udeudeude.github.io/thdies-cast/)
- [RSS feed](https://udeudeude.github.io/thdies-cast/feed.xml)
- [Eight balanced dice editions, with direct audio players](https://udeudeude.github.io/thdies-cast/dice-methods/)
- [Creatures Behaving Strangely, episode 14](https://udeudeude.github.io/thdies-cast/#ep14)
- [Relics and Curiosities, episode 15](https://udeudeude.github.io/thdies-cast/#ep15)
- [Published mathematical methods and outcome manifest](https://github.com/udeudeude/udeudeude.github.io/blob/main/thdies-cast/dice-methods/manifest.json)
- [Pilot master and reproducible build source](https://github.com/udeudeude/udeudeude.github.io/tree/main/thdies-cast)
- [Production manifest (including exact Saved 02 parameters)](https://github.com/udeudeude/udeudeude.github.io/blob/main/thdies-cast/pilot-manifest.json)

The **five original pilot episodes** are D20, 2D6, D100, The Wilderness Oracle (all 80 original encounters), and Ten Minutes to Disaster. **Eight additional full-length balanced dice editions are now also published**, with episode numbers 06–13: three D20 methods (shuffled blocks, giant shuffle, and all 400 ordered pairs), balanced 2D6 and D100, and balanced D4, D8 and D12. The original D20 is a valid shuffled-set method and stays a standard full episode. The initial 2D6 and D100 are retained as clearly labeled archival mathematical experiments; their result sequences and archival classifications remain intact. A 2026-10-24 mastering pass adjusted spoken levels while preserving the recorded outcomes. **Episode 14**, *Creatures Behaving Strangely*, now provides **80** independent encounters, with short natural pauses and **no electronic chimes**. It uses Brother Rubicon's selected Kokoro Lewis voice and the approved Saved 02 sound treatment. Its narrated audio and production manifest are published on the website; its [source manuscript](manuscripts/CREATURES_BEHAVING_STRANGELY_80.md) and [production master](production/CREATURES_BEHAVING_STRANGELY_EPISODE.md) remain here. **Episode 15**, *Relics and Curiosities*, adds 80 original encounters with strange portable artifacts, [available as MP3](https://udeudeude.github.io/thdies-cast/audio/15-relics-and-curiosities.mp3) and through the RSS feed. The Wilderness Oracle and Creatures Behaving Strangely each contain 80 encounters with brief natural pauses, no electronic chimes, and updated seeking guidance.

The [reproducible rendering script](https://github.com/udeudeude/udeudeude.github.io/blob/main/thdies-cast/production/render_creatures.py) and [production workflow](https://github.com/udeudeude/udeudeude.github.io/blob/main/.github/workflows/publish-creatures.yml) live in the website repository.

The feed is a public direct-subscription RSS feed; it has **not** been submitted to the Apple Podcasts public directory. We can change episode mechanics and recording choices after the producer listens to them.

Implementation choices for these first versions: D20 keeps eighteen independently shuffled 1–20 blocks (not independent draws across every adjacent face). 2D6 independently rolls two six-sided dice and speaks both and their sum; 300 rolls at six-second intervals. D100 is independently sampled 1–100 inclusive, 300 rolls at six-second intervals. The Oracle reads only each encounter's prose, marked by a neutral chime, not their numbers or titles. The original timer score has a ten-minute completion cue and a coda afterward.

**Narrator direction adopted October 23:** A different short, old-fashioned, faintly uncanny observation opens every new dice edition, followed verbatim by **“I am Brother Rubicon. The die's cast.”** The closing remark differs by episode; the D12 finishes with the favored **“I believe that was the last. I had been told there would be one more.”** The published episode notes distinguish exact frequency balance from independence of consecutive draws.


The public webpage is for subscription and preview only, **not a gameplay companion app**. All fifteen published episodes work through podcast listening and downloading.

### Listening to the voice tests

[Open the mobile-friendly wizard voice auditions](https://udeudeude.github.io/wizard-auditions/). The audition samples are in the [wizard-voice-auditions branch](https://github.com/udeudeude/Th-die-s-Cast/tree/wizard-voice-auditions); do not confuse them with published podcast episodes.

## D20 pilot: listen and review

- [Play the D20 pilot MP3 (Lewis; includes secret epilogue)](https://raw.githubusercontent.com/udeudeude/Th-die-s-Cast/main/audio/Thdies-Cast-D20-pilot-lewis.mp3)
- [D20 generation manifest and shuffle order](data/d20_pilot_manifest.json)
- Format: 360 rolls, five-second fixed slots, eighteen shuffled permutations of 1–20; spoken instructions at the beginning. **Pilot only, not a published RSS episode.**

## Product principles

- **Low installation and data burden.** One-tap podcast listening, no app dependency for ordinary episodes. Offer selective, compact downloads. Streaming itself still consumes data, and some podcast clients auto-download episodes.
- **Useful at the table.** Timing, audibility, fast recognition, and predictable seeking are more important than filler narration.
- **Podcast only.** All published utilities should operate within an ordinary podcast player, without a companion website or app. For highly configurable games, explore fixed scenario presets and universal recordings rather than software.
- **Original or cleared recordings.** No unlicensed celebrity clips, copyrighted game audio, or ambience repackaging without permission.
- **Keep original games separate.** Designing full original games for podcast audio belongs in a sister project, although ideas can inform each other.

See the linked documents for proposals, constraints, and decisions still to be made.
