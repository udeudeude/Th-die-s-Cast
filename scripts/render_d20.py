#!/usr/bin/env python3
"""Render the first D20 podcast audition with Kokoro bm_lewis.

Pilot only; not published to RSS.
Thirty minutes of five-second sample-aligned slots:
18 independently shuffled blocks of all 20 face values. An introductory
voiceover precedes the results. The introduction is *not* included in the
thirty-minute dice portion. This is a pilot, not an approved production lock.
"""
from __future__ import annotations

import json
import random
import subprocess
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro import KPipeline

SAMPLE_RATE = 24_000
SLOT_SECONDS = 5
SLOT_SAMPLES = SAMPLE_RATE * SLOT_SECONDS
START_PAD_SECONDS = 0.52
START_PAD_SAMPLES = round(START_PAD_SECONDS * SAMPLE_RATE)
BLOCKS = 18
SEED = 20261009
VOICE = "bm_lewis"
SPEED = 0.94
SPOKEN_TITLE = "The die's cast."
SECRET_FALSE_ROLL = "Twenty-one."
SECRET_REVEAL = "No. Not really. That would be ridiculous. This is the end of the recording. You shouldn't be here anyway."
SECRET_LEAD_IN_SECONDS = 6.0
SECRET_BEAT_SECONDS = 2.5
WAV_PATH = Path("audio/.d20-pilot-temporary.wav")
MP3_PATH = Path("audio/Thdies-Cast-D20-pilot-lewis.mp3")
MANIFEST_PATH = Path("data/d20_pilot_manifest.json")

NUMBER_WORDS = [
    "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
]

INTRO = (
    # The displayed title is Th’die’s Cast. Audition 02 is the approved sound.
    SPOKEN_TITLE + " D twenty. "
    "To roll, seek to a random point in this episode. "
    "If you land partway through a number, ignore that fragment. "
    "Your roll is the next number you hear from its beginning. "
    "Every twenty numbers is a new shuffle of the die's faces. "
    "Good fortune."
)

def synthesize(pipeline: KPipeline, text: str) -> np.ndarray:
    parts = []
    for _, _, audio in pipeline(text, voice=VOICE, speed=SPEED):
        parts.append(np.asarray(audio, dtype=np.float32).reshape(-1))
    if not parts:
        raise RuntimeError(f"Kokoro produced no audio for {text!r}")
    if len(parts) == 1:
        out = parts[0]
    else:
        divider = np.zeros(round(SAMPLE_RATE * 0.08), dtype=np.float32)
        joined = []
        for i, p in enumerate(parts):
            if i:
                joined.append(divider)
            joined.append(p)
        out = np.concatenate(joined)
    # Avoid sharp clicks at the start and end of each number.
    fade_samples = min(int(SAMPLE_RATE * 0.015), len(out)//4)
    if fade_samples:
        ramp = np.linspace(0, 1, fade_samples, endpoint=False, dtype=np.float32)
        out[:fade_samples] *= ramp
        out[-fade_samples:] *= ramp[::-1]
    return out

def main() -> None:
    WAV_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SEED)
    sequences = []
    for _ in range(BLOCKS):
        permutation = list(range(1, 21))
        rng.shuffle(permutation)
        # Reject only an identical block; other incidental adjacency is fine.
        while sequences and permutation == sequences[-1]:
            rng.shuffle(permutation)
        sequences.append(permutation)
    assert len(sequences)==BLOCKS
    assert all(sorted(block)==list(range(1,21)) for block in sequences)

    print(f"Initializing {VOICE} at speed {SPEED}", flush=True)
    pipeline = KPipeline(lang_code="b")
    print("Rendering intro", flush=True)
    intro = synthesize(pipeline, INTRO)
    speech = {}
    for n, label in enumerate(NUMBER_WORDS, start=1):
        print(f"Synthesizing {n}: {label}", flush=True)
        speech[n] = synthesize(pipeline, label.capitalize() + ".")
        dur = len(speech[n]) / SAMPLE_RATE
        print(f"  duration: {dur:.3f} seconds", flush=True)
        if len(speech[n]) > SLOT_SAMPLES - START_PAD_SAMPLES - round(.3*SAMPLE_RATE):
            raise RuntimeError(f"Number {n} too long for the {SLOT_SECONDS}-second slot.")

    print("Writing sample-accurate sequence to WAV", flush=True)
    with sf.SoundFile(
        WAV_PATH, mode="w", samplerate=SAMPLE_RATE, channels=1,
        subtype="PCM_16", format="WAV"
    ) as wave:
        wave.write(np.zeros(round(.45*SAMPLE_RATE), dtype=np.float32))
        wave.write(intro)
        wave.write(np.zeros(round(1.6*SAMPLE_RATE), dtype=np.float32))
        introduction_duration = wave.frames / SAMPLE_RATE
        for block in sequences:
            for die in block:
                frame = np.zeros(SLOT_SAMPLES, dtype=np.float32)
                audio = speech[die]
                frame[START_PAD_SAMPLES:START_PAD_SAMPLES+len(audio)] = audio
                wave.write(frame)
        # This coda follows the 360 valid rolls, and is NOT an additional roll.
        rolls_end_seconds = wave.frames / SAMPLE_RATE
        wave.write(np.zeros(round(SECRET_LEAD_IN_SECONDS * SAMPLE_RATE), dtype=np.float32))
        epilogue_start_seconds = wave.frames / SAMPLE_RATE
        print("Rendering hidden false-21 epilogue", flush=True)
        wave.write(synthesize(pipeline, SECRET_FALSE_ROLL))
        wave.write(np.zeros(round(SECRET_BEAT_SECONDS * SAMPLE_RATE), dtype=np.float32))
        wave.write(synthesize(pipeline, SECRET_REVEAL))
        wave.write(np.zeros(round(1.1 * SAMPLE_RATE), dtype=np.float32))
        total_duration = wave.frames / SAMPLE_RATE

    print(f"Total WAV seconds: {total_duration:.3f}", flush=True)
    print(f"Die slots: {BLOCKS*20} x {SLOT_SECONDS}s", flush=True)
    args = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(WAV_PATH),
        "-af", "loudnorm=I=-17:TP=-1.5:LRA=7",
        "-ar", "24000", "-ac", "1", "-codec:a", "libmp3lame",
        "-b:a", "64k", str(MP3_PATH)
    ]
    subprocess.run(args, check=True)
    WAV_PATH.unlink()

    # Useful for reproducibility and spot-checking the actual audio,
    # but NOT to be shown to the listener who is seeking a random result.
    MANIFEST_PATH.write_text(json.dumps({
        "series": "Th’die’s Cast", "spoken_series_name": SPOKEN_TITLE, "episode": "D20 — Pilot",
        "status": "audition, not released", "voice": VOICE, "speed": SPEED,
        "source": "Kokoro (generated speech)",
        "seed": SEED, "block_count": BLOCKS, "die_sides": 20,
        "slot_seconds": SLOT_SECONDS, "slot_onset_seconds": START_PAD_SECONDS,
        "intro_seconds": round(introduction_duration, 3),
        "rolls_end_seconds": round(rolls_end_seconds, 3),
        "epilogue_start_seconds": round(epilogue_start_seconds, 3),
        "epilogue_text": SECRET_FALSE_ROLL + " [pause] " + SECRET_REVEAL,
        "epilogue_is_a_roll": False,
        "total_rolls": BLOCKS * 20,
        "total_seconds_approx": round(total_duration, 3),
        "randomization": "independent new shuffled permutations, each face exactly once per block",
        "permutations": sequences,
        "notes": "Approximately 30 minutes of dice plus opening instructions. Each slot is 5.0 seconds, including variable silence. Seek randomly, discard clipped numbers, use next complete number. This is not an independent-roll stream. The fake twenty-one after all 360 valid rolls is a hidden joke, not a roll."
    }, indent=2) + "\n")

    print("Ready:", MP3_PATH, MP3_PATH.stat().st_size, "bytes", flush=True)
    print("Ready:", MANIFEST_PATH, flush=True)

if __name__ == "__main__":
    main()
