# Th’die’s Cast — show bible

_Last revised: 2026-10-09. Status: working plan._

## Mission

An audio-first utility podcast for tabletop games. Rather than regular conversation, its episodes *do things*: produce random values when the listener seeks, regulate real-time play, serve up unique procedural prompts, or function as game props. The show should be a modest, shareable tool that is already in a familiar podcast app.

## Voice and attitude

- Narrator **chosen**: Kokoro `bm_lewis` (British male). Base narrator for game instructions, numbers, oracles, and utility episodes. No default processing/speed locked yet.
- **TTS pronunciation audition in progress:** The printed/show/feed title remains **Th’die’s Cast**. The proper spoken rendering has **not yet been selected**. A first D20 re-render uses “The die is cast” provisionally, and ten Lewis variants have been synthesized for listening on the `title-pronunciation-auditions` branch. Once chosen, store the definitive TTS text independently from the printed brand.
- A wizardly host persona is desirable, especially for the ultra-leisurely editions, but keep ordinary tools brief and crisp.
- The wizard is wry and sometimes verbose by design in the ultra-leisurely format; dramatic performance must never obscure the reported outcome.
- Existing test samples: [wizard audition page](https://udeudeude.github.io/wizard-auditions/). Choice of voice does not mean the selected audition performance is the definitive final processing recipe.

## Product rationale: fewer downloads and less storage

Official companion applications can be surprisingly large, and a player may not want to keep an app installed for a game played occasionally. Downloading it at game night may be inconvenient or costly on a limited cellular plan. A standard podcast can be listened to in an already-installed app, subscribed to in advance, selectively downloaded when convenient, and shared as a simple link.

This is an **economy of installation, storage, and network data**, not a promise of zero data: streaming requires connectivity; many podcast clients auto-download; long MP3s still take storage. Prioritize compact mono speech, per-episode files, clear download sizes, and optional lightweight web access. A baseline comparison: a 30-minute mono MP3 at 48 kbps is about 10.8 MB (decimal); 64 kbps is about 14.4 MB. Assess speech quality at those bitrates rather than accepting numbers blindly.

One empirical example, subject to change: Bezier's iOS One Night companion app listing reported 148.5 MB as of 2026-10-09; verify before using in public marketing: https://apps.apple.com/us/app/one-night/id728175611 .

## The ten catalog categories

1. **Dice & Probability Tools** — standard dice, combinations, pools, explosions, advantage, success counting.
2. **Cards & Other Randomizers** — decks, tarot, directions, coin flips, shuffled orders, initiative selection.
3. **Encounter Streams** — thirty-minute sequences of unique wilderness, dungeon, urban and other encounters.
4. **Oracles & Decision Aids** — yes/no, shades of success, dilemmas, small decisions, prompts.
5. **Characters, Locations & Worlds** — NPCs, rumors, weather, settlements, objects, factions, strange places.
6. **Timers, Countdowns & Clocks** — generic clocks, doomsday clocks, round bells, action intervals.
7. **Game-Specific Audio Controllers** — timed soundtracks and fixed moderator tracks designed for named board games.
8. **Atmospheres & Environments** — original ambiences, room tone, continuous location soundscapes.
9. **Audio Clues & In-World Props** — transmissions, overheard voices, invisible movements, environmental evidence.
10. **Archival & Special Editions** — recognizable public-domain/cleared historic voices, alternate narrators and experimental formats.

Keep **original-audio-native games** as a separate sister project, not an episode category.

## Episode families and modes

- **Quick dice:** proposed short result slots and minimal speech, exact interval TBD by user.
- **Leisurely dice:** more room for selection and use at the table, interval TBD.
- **Ultra-leisurely dice:** substantial, varied characterful commentary, e.g., a 19 is splendid but not perfect; a 1 meets with comic disappointment. Crucially, outcome spoken audibly; variable-length remarks fit fixed total time slots to avoid time-weighted outcome bias when seeking.
- **Table format:** short description or result, each occupying an independently seekable slot or chapter; encounter streams prefer *each encounter unique within the episode*, unlike repeatedly reading a finite list.
- **Game timer:** fixed time and function first; original audio designs, optional narrative variants.
- **Podcast-only game moderators:** common fixed role-setup episodes, or a universal recording with phases for all supported roles. If the format cannot work reliably as fixed audio, defer it.

## Core user experience

Listeners can start an episode and follow its instructions, or seek to an arbitrary location and use the **next fully spoken outcome after playback resumes**. It should not require visual cues or the listener counting timestamps. A compact opening disclaimer/instruction is part of the content, but avoid making it impossible to use by immediate seeking.

Podcast clients have varying seek precision, playback speed, silence trimming, and crossfade behavior. Test at least Apple Podcasts and an iPhone web audio element before publishing. No automatically inserted midrolls, transitions, or narration during timed cues.

## Decisions already made

- Use Lewis as narrator.
- Keep all previously discussed dice and randomizer types in planning catalog.
- Add quick, leisurely, **ultra-leisurely** modes.
- User will specify alterations to some dice mechanics before production.
- Explore exploding D6 and D20 and dice pools without falsely uniform distributions.
- Prefer a 30-minute stream of **different** wilderness encounters to recycling a small table.
- No Th’die’s Cast companion app or website. Explore common fixed setup episodes, or a universal recording with correctly timed role phases, for configurable games.
- Investigate a D20 made of **real**, recognizably different famous-voice samples if clips can be cleared; do not pretend short snippets are automatically cleared.
- Provisional first five releases: D20, 2D6, D100, Wilderness Oracle, Ten Minutes to Disaster.
- Original games intended to be played with podcast audio are an adjacent **sister project**.

## Still open (ask when developing each format, not all at once)

- Exact durations, opening instructions, repeat policy, seed protocol, slot intervals, sound cues, and distribution/variant rules for each die or dice combination.
- What a listener should hear for individual dice vs totals; how to handle percentile zero, unusual notation, criticals, and bespoke rule sets.
- The tone library and pacing for ultra-leisurely outcomes.
- Whether any game-specific replacement recordings are worth making once licenses/game mechanics are confirmed.
- Ambience credits, RSS/feed behavior, publishing license, companion feature scope, and naming conventions.

## Anti-goals

- An elaborate, data-heavy app replacing the need for a simple MP3.
- Long theatrical introductions in quick utility episodes.
- Uniformly selecting 2D6 totals instead of rolling two independent D6s.
- Repeated 20-item encounter tables masquerading as an original 30-minute catalog.
- Prematurely hard-coding unapproved dice mechanics.
- Repackaging copyrighted game soundtracks, licensed ambience, or celebrity recordings as though they were public domain.

## Future review protocol: “give me the dice?”

When the user says **“give me the dice?”**, supply a **numbered list** of all suggested dice episodes, with the proposed implementation of each (roll generation, distribution, readout, time spacing, shuffle/independence policy, variants, and specific open questions). Do not assume the list itself authorizes generation; wait for the user's edits and decisions. This phrase is an agreed review trigger, not a demand for current production.
