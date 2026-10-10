# Production and implementation plan

_Working design, 2026-10-09. Do not implement unspecified game mechanics without user review._

## Narrator

Use Kokoro `bm_lewis`, chosen over `bm_fable`, `bm_george`, and processed Fable following actual auditions. Keep voice/model identifier, speed, script, pauses, effects, and output normalization in versioned production metadata. Do not assume the Living Patterns `bm_george` speed 0.88 applies to Lewis here. Save reference auditions; they are experiments, not canonical episodes.

### Preferred system layout

- Canonical machine-readable manifests: episode ID, category, mode, dice definitions, source/script chunks, seed (if deterministic), audio asset attribution, revision and production config.
- Deterministic build tools: generate and validate text, audio chunks, complete MP3, embedded chapters where sensible, feed entries, and a static browser listening page.
- Host public assets; produce ordinary podcast RSS enclosures for standard clients.
- Maintain checksum/duration manifest; verify feed enclosures, program duration, bitrate and loudness.
- No server dependency for audio playback. For dynamic modules, consider static hosting plus client-side logic and a tiny subset of cached audio, with no account or analytics required.

## Seek-and-hear interface

**Original user design:** For D20, read numbers 1–20 once each in a random order; repeat with a *different* shuffled order, for about 30 minutes. An interval of roughly three times the spoken duration between announcements. Listener scrubs to an arbitrary point and takes the **next spoken result** as the roll. D4/D6/D8/D10/D12/D100 derivatives and 2D6 proposed.

This is the starting point, **not an immutable production specification**; user explicitly intends to amend the implementation of some formats.

### Accuracy of random-access sampling

**Time weighting:** If result A takes 0.7 seconds and result B takes 2.1 seconds, spacing each by three times its own spoken length creates slot lengths in a 1:3 ratio. Random seeks by playback time will overselect B. Therefore, use fixed total-duration slots, even if internal silence varies. Make sure users understand "next *complete* result spoken" after the seek. Always ensure a result is within a reasonable interval.

**Permutations vs independent rolls:** Reshuffling full sets gives every face exactly once in each block but creates negative dependence across sequential results. Uniform *marginal* selection at random seek positions is attainable with equal-length slots and randomized permutations. If rules require independent sequential rolls, use independent uniform samples instead, with expected short streaks and repeats. Never tell users the two methods are statistically identical.

**Slots and timing:** At 5.0 seconds each, a 30-minute results portion has 360 slots (18 full D20 shuffles); longer intros change the exact count. Set all slot starts on sample-accurate boundaries. Avoid a long intro affecting the outcomes and seek distribution disproportionately; move some instructions into metadata if necessary. Consider distinct short "how to use this" demo episode or chapter.

**Player settings:** Some clients enable speedup/silence skipping; functional timelines may be compromised. Warn when needed, especially for clock episodes.

## Modes

- **Quick**: small fixed slots, short announcements; timings TBD.
- **Leisurely**: more time between face announcements; timings TBD.
- **Ultra-leisurely**: repeated wizard commentary with varied scripts, e.g. lavish praise for 19, disappointment at 1; clear final number within every segment. Choose fixed slots long enough for the longest approved phrase; pad shorter passages with silence. Could include 5–20 script variants per face rather than one repeated catchphrase. Actual target length and rhythm TBD by user.

## Special dice

### 2D6 vs D66

2D6 sum distribution is triangular. Generate face A and face B independently in [1,6] then compute total. There are 36 equally likely ordered outcomes; 7 occurs in six of those and 2 or 12 in one each.

D66 uses face A as "tens" and B as "units": e.g. 1 & 6 yields "16", 6 & 1 yields "61"; neither is the 2D6 sum. Be explicit about notation.

### Exploding D6 / D20

Define a ruleset with `sides`, `explode_on`, `recursive`, `sum_policy`, `maximum_chain_policy`, and `spoken_format` before writing it.

**Candidate algorithm for standard recursive additive explosions:**
1. Roll one uniform integer 1..S.
2. Append it to chain and add it to running total.
3. If face = S, repeat from step 1; otherwise stop.
4. Encode the complete *observed chain* in a spoken segment: “Six, six, three. Total: fifteen.”

This distribution is unbounded, though extraordinarily long runs are rare; a fixed-length program requires explicit handling of rare overlong announcements. Do **not** impose an unstated cap and present the results as faithful to an uncapped ruleset.

**Possible solutions for overlong chains:** size slots to a high percentile, allow exceptionally long slots only if we compensate time weighting in selection (hard), or use a specific declared finite-chain game variant; optionally a "continue rolling" instruction if appropriate to a game. Choose after discussing user intent.

A common alternative only rolls an extra die once, without recursive explosions; this is a *different mechanic*, not interchangeable with the recursive one. "Compounding" is used inconsistently across games and should not be used as a synonym for "one explosion only" without naming a particular game's rule.

**D20 explosions are not a general D20 rule**, so label them as a special mechanic and investigate actual supported systems, not a default D20 feature.

### Other modifiers

Advantage/disadvantage 2D20 draw two independent rolls and select max/min; 4D6 drop lowest means four independent D6 samples, remove the minimum and total the other three; D66 uses ordered digits; 4dF rolls four equally likely {-1,0,+1} faces. Pools and exploding/threshold dice must specify the relevant system and version.

## Unique encounter stream

The user prefers **~30 minutes of all different wilderness encounters** rather than repeating a 20-encounter table in new permutations. Generate original encounter premises, edit out duplicates/near duplicates, and use a mix of social, nonviolent, surprising, logistical, weather, hazards, and threatening situations. Equal-length slots are attractive for unbiased seeks, but each spoken encounter may vary in length; edit scripts to shared maximum time or offer a link to a text index in the show notes.

Decide with user whether each snippet contains an outcome alone, a short GM prompt, or acted voices/sound. Consider no narrator in more diegetic episodes.

## Audio timers

- **Correct duration and cues** outrank mood. Validate against a legal rule source before advertising compatibility with a named game.
- Use original sound design, not redistributed game audio. Support a no-ambience / cues-only version and themed versions.
- Track sample-exact deadlines. If content mentions time remaining, bake it into the timing tests.
- No adverts, crossfades, time-stretching or silence skipping. Playback at 1× only.
- For timers requiring interactivity or random mission events, use the companion instead of implying a pre-recorded file can handle it.

## One Night modular narration: reduce combinatorial explosion

An independent role clip library and scheduler can construct a night with configured roles without rendering a separate MP3 for each role combination:

1. User selects game/expansion, player count, and available roles.
2. Rules engine validates setup and ordered wake phases.
3. Web client plays a pre-recorded intro, only the selected role modules in sequence, required pauses, and closing; then a configurable day timer.
4. Precache the required small assets for optional offline play and make any asset download sizes explicit.
5. Publish several common configuration presets as podcast episodes for users who want completely app-less playback.

For base One Night, this is plausible; some expansions (especially Alien) involve randomized instructions and actual on-screen choices, so a basic modular clip list is insufficient. Implement conditional logic only after confirming official behavior; consider *not* supporting variants where input is necessary.

This is a **hybrid utility**, not a commitment to reimplement the official app. Bezier's official page already links a browser version, which should be assessed before duplicating a working solution.

## Delivery and size

- Encode spoken mono MP3s at evaluated bitrates such as 48 or 64 kbps; test on iPhone speaker and headphones for intelligibility. At 30 min: ~10.8 MB at 48 kbps, ~14.4 MB at 64 kbps (decimal estimate, excluding metadata).
- Mixed soundscapes and layered music may need stereo and more bitrate; don't sacrifice function for a nominal small size.
- Website link should launch quickly and allow play in Safari; podcast RSS remains canonical for noninteractive episodes.
- Explain selective downloading, podcast app's auto-download settings, and network/cache considerations to users.

## Quality assurance before publishing

- Uniform dice face histogram and per-block permutation; 2D6 expected total frequency; unbiased time-based seeking tests using simulated seek positions.
- Exact recurring program length within tolerance; check beginning and ending slots, gaps, transitions, absence of clipped first words.
- Cross-client iPhone test: Apple Podcasts, Safari audio control; phone speaker and earphones.
- Compare Lewis's spoken numbers, including teens vs tens, in quiet and noisy environments.
- Verify cues for real-time games within second-level precision and sync after seeking/pausing.
- Check show notes and rights attribution, correct URL, unique GUID and enclosure sizes, and that no episode is labeled published before a file exists.
