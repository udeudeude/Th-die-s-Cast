# Creatures Behaving Strangely | Episode 14 production master

## Editorial source

The approved episode consists of **80 independent encounters**, not the earlier 20-scene audition. The definitive spoken prose is in [CREATURES_BEHAVING_STRANGELY_80.md](../manuscripts/CREATURES_BEHAVING_STRANGELY_80.md). Numbers and headings are for editors only and must never be spoken.

The 20-scene first draft remains in version control as a historical prototype, **not** the current episode source.

## Voice and performance

- Brother Rubicon; Kokoro `bm_lewis`, Saved 02 · Natural pitch, light room.
- Opening observation: “Animals are said to know things before we do. This does not mean they intend to tell us.”
- After ~0.32 seconds: “I am Brother Rubicon. The die's cast.” Speak this entire phrase as one utterance.
- After another ~0.32 seconds: “Seek to a random point during the encounters. Ignore any encounter already in progress. Your encounter is the next complete scene you hear from its beginning.”
- Read all 80 scenes, no numbers or titles, with **no electronic chimes, musical separators, or synthesized sound effects**. Natural silence between scenes: approximately 0.85 seconds. Do not pad individual scenes to fixed-length slots.
- Closing coda (not included in public descriptions): “The animals have gone quiet. I do not believe that means they have finished.”

Short pauses deliberately take precedence over perfect time-uniform random seeking, which made the earlier 35-second slots unpleasantly empty.

## Publication and quality assurance

The **active source and renderer** are in the [public podcast website repository](https://github.com/udeudeude/udeudeude.github.io/tree/main/thdies-cast/production), specifically `creatures_behaving_strangely.md` and `render_creatures.py`.

The feed maintains episode number 14 and its existing GUID. Publishing a revised MP3 requires updated enclosure length and duration, a cache-busting URL, and verification of the public GitHub Pages release.

Before rendering or claiming the model is unavailable, consult [AUDIO_PRODUCTION_RUNBOOK.md](../docs/AUDIO_PRODUCTION_RUNBOOK.md). The existing GitHub Actions runner installs the required voice and mastering software.

Compare the level of the opening identification and coda against the actual encounter narration before release; preserve the entire prior catalog and its episode IDs.
