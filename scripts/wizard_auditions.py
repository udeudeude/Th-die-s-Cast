#!/usr/bin/env python3
"""Generate four reproducible Th'die's Cast wizard-voice auditions with Kokoro.

Run in GitHub Actions using .github/workflows/wizard-auditions.yml.
"""
from pathlib import Path
import subprocess
import numpy as np
import soundfile as sf
from kokoro import KPipeline

OUT = Path("auditions")
OUT.mkdir(exist_ok=True)

SCRIPT = (
    "Welcome, traveler. The dice have spoken. "
    "Three doors stand before you. "
    "Behind the first, a treasure. Behind the second, a rather unpleasant death. "
    "And behind the third... hmm. Curious. I seem to have misplaced the third door. "
    "Roll a twenty-sided die, if you please."
)

VOICES = [
    ("01-fable", "bm_fable", 0.90),
    ("02-george", "bm_george", 0.86),
    ("03-lewis", "bm_lewis", 0.91),
]

pipeline = KPipeline(lang_code="b")

def encode(wav, mp3, effects=None):
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(wav)]
    filters = []
    if effects:
        filters.append(effects)
    filters.append("loudnorm=I=-17:TP=-1.5:LRA=9")
    cmd += ["-af", ",".join(filters), "-ar", "44100", "-ac", "1",
            "-codec:a", "libmp3lame", "-b:a", "128k", str(mp3)]
    subprocess.run(cmd, check=True)

for stem, voice, speed in VOICES:
    print("Synthesizing", stem, voice, speed, flush=True)
    sections = []
    for _, _, audio in pipeline(SCRIPT, voice=voice, speed=speed):
        audio = np.asarray(audio, dtype=np.float32).reshape(-1)
        sections.append(audio)
        sections.append(np.zeros(4800, dtype=np.float32))
    if not sections:
        raise RuntimeError(f"No audio for {voice}")
    wave = np.concatenate(sections)
    wav = OUT / f"{stem}.wav"
    sf.write(wav, wave, 24000)
    encode(wav, OUT / f"{stem}.mp3")
    if stem == "01-fable":
        # Shift perceived pitch downward ~6% without lengthening speech.
        # This is deliberately restrained: character, not caricature.
        encode(wav, OUT / "04-fable-deeper.mp3",
               "asetrate=22560,aresample=24000,atempo=1.0638298,"
               "highpass=f=75,lowpass=f=7500,aecho=0.65:0.28:60:0.09")
    wav.unlink()

print("Generated", [str(f) for f in OUT.glob("*.mp3")])
