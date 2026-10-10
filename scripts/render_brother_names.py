#!/usr/bin/env python3
"""Compare ten medieval/folkloric Brother names with the selected Lewis voice.

Two consistent spoken lines per candidate, preserving the chosen pronunciation
'The die's cast.' Written podcast title remains Th’die’s Cast.
"""
from pathlib import Path
import json
import subprocess

import numpy as np
import soundfile as sf
from kokoro import KPipeline

VOICE = "bm_lewis"
SPEED = 0.94
SAMPLE_RATE = 24_000
OUT = Path("auditions/brother-names")
OUT.mkdir(parents=True, exist_ok=True)

NAMES = [
    "Godric",
    "Blaise",
    "Oswin",
    "Aelfric",
    "Cuthbert",
    "Dunstan",
    "Peregrine",
    "Anselm",
    "Wulfstan",
    "Berengar",
]

# These are matched scripts: pronunciation of the personal name is the variable.
TEMPLATE_A = "Greetings. I'm Brother {name}. Welcome to the die's cast."
TEMPLATE_B = "I'm Brother {name}. Thank you for joining the die's cast."

def silence(seconds):
    return np.zeros(round(seconds * SAMPLE_RATE), dtype=np.float32)

def synth(pipe, words):
    parts = []
    for _, _, audio in pipe(words, voice=VOICE, speed=SPEED):
        parts.append(np.asarray(audio, dtype=np.float32).reshape(-1))
    if not parts:
        raise RuntimeError("No Kokoro output for " + words)
    wave = np.concatenate(parts)
    fade = min(round(.012 * SAMPLE_RATE), len(wave)//4)
    if fade:
        ramp = np.linspace(0, 1, fade, endpoint=False, dtype=np.float32)
        wave[:fade] *= ramp
        wave[-fade:] *= ramp[::-1]
    return wave

def export_mp3(path, audio):
    wav = path.with_suffix(".wav")
    sf.write(wav, audio, SAMPLE_RATE, subtype="PCM_16")
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(wav), "-af", "loudnorm=I=-17:TP=-1.5:LRA=9",
        "-ac", "1", "-ar", "24000", "-c:a", "libmp3lame", "-b:a", "80k",
        str(path),
    ], check=True)
    wav.unlink()
    assert path.stat().st_size > 2000, path
    return round(len(audio) / SAMPLE_RATE, 3)

def main():
    pipe = KPipeline(lang_code="b")
    manifest = {
        "project": "Th’die’s Cast",
        "voice": VOICE,
        "speed": SPEED,
        "spoken_podcast_title": "The die's cast.",
        "status": "name auditions, no winner selected",
        "candidates": [],
    }
    combined = [silence(.3)]
    for i, name in enumerate(NAMES, start=1):
        phrase_a = TEMPLATE_A.format(name=name)
        phrase_b = TEMPLATE_B.format(name=name)
        print("Creating candidate", i, name, flush=True)
        a = synth(pipe, phrase_a)
        b = synth(pipe, phrase_b)
        track = np.concatenate([
            silence(.4), a, silence(1.1), b, silence(.7)
        ])
        filename = f"{i:02d}-Brother-{name}.mp3"
        duration = export_mp3(OUT / filename, track)
        manifest["candidates"].append({
            "number": i,
            "name": f"Brother {name}",
            "script_one": phrase_a,
            "script_two": phrase_b,
            "filename": filename,
            "duration_seconds": duration,
        })
        announcement = synth(pipe, f"Candidate {i}.")
        combined.extend([
            announcement, silence(.55), track, silence(1.2)
        ])

    combined_wave = np.concatenate(combined)
    compilation_name = "00-All-Ten-Brothers-Lewis.mp3"
    length = export_mp3(OUT / compilation_name, combined_wave)
    manifest["compilation_filename"] = compilation_name
    manifest["compilation_duration_seconds"] = length
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    assert len(manifest["candidates"]) == 10
    print(f"Generated {len(NAMES)} names, compilation {length}s", flush=True)

if __name__ == "__main__":
    main()
