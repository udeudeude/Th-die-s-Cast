# Th’die’s Cast: how to make a real episode

**Start here before saying the voice generator, model, or audio tools are unavailable.** This project already has a working remote audio studio: **GitHub Actions in `udeudeude/udeudeude.github.io`**. A ChatGPT execution container without Kokoro, Rubber Band, or network access is *not* a reason to stop.

## Repositories and known working precedent

- Editorial manuscripts, show bible, and voice decisions: [`udeudeude/Th-die-s-Cast`](https://github.com/udeudeude/Th-die-s-Cast).
- **Actual audio production, published MP3s, podcast RSS, and GitHub Pages:** [`udeudeude/udeudeude.github.io`](https://github.com/udeudeude/udeudeude.github.io/tree/main/thdies-cast).
- Production source: `thdies-cast/production/`; feed: `thdies-cast/feed.xml`; media: `thdies-cast/audio/`.
- Proven workflows: `.github/workflows/produce-thdies-cast-pilot.yml`, `publish-expanded-dice.yml`, and `publish-creatures.yml`.
- Creatures' original successful production: [run 40073108602](https://github.com/udeudeude/udeudeude.github.io/actions/runs/40073108602). Audio synthesis and validation succeeded; publishing initially failed because untracked temporary files prevented a rebase. The [recovery workflow run 40073467958](https://github.com/udeudeude/udeudeude.github.io/actions/runs/40073467958) downloaded the generated artifact, released it, and verified the 14-episode feed. **This is the working precedent for recovering expensive completed work.**
- Existing `render_pilot_season.py` exposes `synthesize`, `blank`, `emit_mp3`, `sound_file`, the neutral cue (now prohibited in encounter episodes), and saved Lewis processing.
- GitHub Actions Ubuntu runner installs Python 3.11, `ffmpeg` with Rubber Band filter, `espeak-ng`, `torch`, and `thdies-cast/production/requirements.txt` (Kokoro 0.9.4).

## Approved voice and delivery

- Narrator: Brother Rubicon, Kokoro `bm_lewis`, spoken show title **“The die's cast.”**
- Preserve **Saved 02 · Natural pitch, light room** treatment and recorded sample rate; exact values are in `pilot-manifest.json`. Offline Rubber Band + equalizer + room treatment approximates, but does not exactly duplicate, the Voice Lab preview.
- Distinct quiet observation, subtle 0.32-second beat, **“I am Brother Rubicon. The die's cast.”** as one utterance, another beat, then concise functional instruction.
- **Every encounter episode must identify itself aloud** at the start of the practical instructions: “This is the Wilderness Oracle.”, “This is Creatures Behaving Strangely.”, or “This is Relics and Curiosities.” Do not add the unnecessary wraparound instruction “If you reach the end, return to the first encounter after the introduction.”
- Original encounter prose is read without entry numbers or headings. **No synthesized chimes or musical separator** in encounter recordings; use short natural silence. Never spoil the closing coda in public descriptions.
- Don't put internal implementation prose, model names, audio technicalities, fairness caveats or claims about the coda in public show descriptions. Those belong in source documentation, not the podcast player.
- Avoid lengthy dead air. For prose scenes, prefer short inter-scene gaps to rigid 35-second blocks. This may make arbitrary seeking time-weighted; document it internally and prioritize the listener experience.
- **Level matching is part of mastering.** Compare spoken introductions and endings *against* spoken rolls/scenes, not merely against peak or whole-file loudness. Measure, adjust and remeasure all affected episodes; preserve timer timestamps and avoid clipping or sudden gain jumps.

## Procedure for new or revised episodes

1. Review the approved manuscript and production master; inspect main branches, active workflows/jobs, artifacts, commits, the public feed and existing audio. **Do not assume an interrupted job failed.**
2. Add/update a deterministic renderer under `thdies-cast/production`, preserving the approved voice, ordered source text, boundaries, and production manifest. Back up and verify old MP3 hashes before modifying.
3. Add/run a narrowly scoped GitHub Actions workflow with `contents: write`. Install the above dependencies on the runner, compile/check source, synthesize, measure levels, validate durations and RSS, then commit audio + metadata + listening page.
4. Preserve the full MP3 and manifest using `actions/upload-artifact` **even if publication later fails**. If publishing fails, recover the existing completed artifact instead of running Kokoro again.
5. Before pushing, `git add` only publication files, commit, then stash unrelated modified/untracked runtime files (or otherwise clean the tree), fetch/rebase, and push. Check the return code. A clean push is not identical to deployed GitHub Pages.
6. Verify the actual new commit, all RSS enclosures and unique GUIDs, previous episodes' retention, and the separate GitHub Pages deployment; report honestly whether each succeeded.
7. Keep heavy production workflows **manual dispatch** after a release so unrelated edits do not rerender/publish episodes.

## Avoid repeating these failures

- Missing Kokoro on a local container does not mean it cannot be run through GitHub Actions.
- Don't claim the job succeeded or failed until reading the job steps/logs and checking produced MP3/artifacts.
- The original 20-creature build used **35-second slots** with at most 15 seconds of narration, which produced excessive silence. Don't recreate it.
- The original Wilderness Oracle and 20-creature episode used a procedurally synthesized chime. The producer explicitly rejected this; do not bring it back. If an actual separator is ever necessary, obtain producer approval for a properly licensed *real-world recording* with attribution.
- **Keep public notes editorial, not engineering reports.** In particular, do not discuss hand-seeking uniformity, voice model or the closing-coda trick in episode descriptions.
