# Relics and Curiosities | Episode 15 production master

## Source and format

The complete, canonical 80 independent scenes are in [RELICS_AND_CURIOSITIES_80.md](../manuscripts/RELICS_AND_CURIOSITIES_80.md). The original twenty-scene draft is preserved separately as editorial history.

This is a system-neutral audio oracle of portable objects, curious relics, uncertain provenance, and invitations to act. Do not impose game mechanics, explanations, rewards, or combat outcomes. The meaning of each object is determined by the people who encounter it.

Each encounter is spoken without its number or editorial title, followed by **approximately 0.85 seconds of natural silence**. Do not introduce synthetic chimes, musical transitions, or artificial fixed-length slots.

## Brother Rubicon

Voice and mastering follow the approved Lewis `bm_lewis` Saved 02 treatment from the Th’die’s Cast audio studio.

- Opening: “Objects remember more than their owners. They are less inclined to speak of it.”
- Pause approximately 0.32 seconds.
- Recurring identification, as a single utterance: “I am Brother Rubicon. The die's cast.”
- Pause approximately 0.32 seconds.
- Concise instructions: “This is Relics and Curiosities. Seek to a random point during the encounters. Ignore any encounter already in progress. Your encounter is the next complete scene you hear from its beginning.”
- Closing coda, not disclosed in public notes: “There ought to be an inventory. I have never found one that was complete.”

## Production and acceptance

- Studio: [`udeudeude/udeudeude.github.io`](https://github.com/udeudeude/udeudeude.github.io/tree/main/thdies-cast).
- Canonical audio source: `thdies-cast/production/relics_and_curiosities.md`; runner: `render_relics.py`.
- Publication workflow: `.github/workflows/publish-relics.yml`, sequenced behind the corrected Creatures/Wilderness release.
- The intended public identity is **episode 15** with the stable GUID `urn:thdies-cast:encounters:15:v1`.
- Confirm exactly 80 scenes, zero synthetic chimes, close natural spacing, correct voice levels across introduction/scenes/coda, a playable MP3, correct enclosure length, a valid 15-item RSS, and successful GitHub Pages deployment before claiming publication.
- Do not replace or renumber the previous fourteen episodes. Keep their GUIDs and unchanged media. The sole permitted companion change to existing audio is correcting Wilderness's outdated spoken instruction to wait for a chime.

For reproducibility and recovery of failed-but-finished audio jobs, consult [the production runbook](../docs/AUDIO_PRODUCTION_RUNBOOK.md).
