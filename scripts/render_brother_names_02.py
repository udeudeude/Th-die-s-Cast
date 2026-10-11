#!/usr/bin/env python3
"""Audition seven speculative Brother names in Lewis's Kokoro voice.

The first introduction stays consistent across candidates, so the name
is the only variable. The second is an individually written line, to hear
each name in a natural, characterful context. The exact user's spelling
is passed to Kokoro, intentionally without phonetic corrections.
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro import KPipeline

OUT = Path("auditions/brother-names-02")
VOICE = "bm_lewis"
SPEED = 0.94
SAMPLE_RATE = 24_000
COMPILATION = "00-eight-brother-names-compilation.mp3"

CANDIDATES = [
    {
        "name": "Brother Rubicon",
        "slug": "rubicon",
        "second": (
            "Beyond this threshold, there is no going back. "
            "Brother Rubicon will see you across."
        ),
    },
    {
        "name": "Brother TheDie",
        "slug": "thedie",
        "second": (
            "A name may be a sign, or merely a sound. "
            "Mine is Brother TheDie. Now, shall we begin?"
        ),
    },
    {
        "name": "Brother The Die",
        "slug": "the-die",
        "second": (
            "Some folk swear that fortune has a face. "
            "They call me Brother The Die. I have never seen it."
        ),
    },
    {
        "name": "Brother Thudiey",
        "slug": "thudiey",
        "second": (
            "The last bell has rung, and no one knows why. "
            "Brother Thudiey knows even less."
        ),
    },
    {
        "name": "Brother Thudie",
        "slug": "thudie",
        "second": (
            "The fire is warm, and the hour is late. "
            "Brother Thudie, they call me. Sit, and hear what chance has to say."
        ),
    },
    {
        "name": "Brother The Dhai",
        "slug": "the-dhai",
        "second": (
            "A traveler once asked my name. "
            "I told him: Brother The Dhai. He wrote it wrong, of course."
        ),
    },
    {
        "name": "Brother Thadhai",
        "slug": "thadhai",
        "second": (
            "What is a name but an old word spoken twice? "
            "Brother Thadhai is quite enough for me."
        ),
    },
    {
        "name": "Brother Berengar",
        "slug": "berengar",
        "second": (
            "I am Brother Berengar. The road is long, "
            "and chance has not yet spoken."
        ),
    },
]

def silence(seconds: float) -> np.ndarray:
    return np.zeros(round(SAMPLE_RATE * seconds), dtype=np.float32)

def synth(pipeline: KPipeline, text: str) -> np.ndarray:
    parts = []
    for _, _, audio in pipeline(text, voice=VOICE, speed=SPEED):
        parts.append(np.asarray(audio, dtype=np.float32).reshape(-1))
    if not parts:
        raise RuntimeError(f"No speech generated: {text}")
    wave = np.concatenate(parts)
    fade = min(round(SAMPLE_RATE * .012), len(wave) // 4)
    if fade:
        ramp = np.linspace(0, 1, fade, endpoint=False, dtype=np.float32)
        wave[:fade] *= ramp
        wave[-fade:] *= ramp[::-1]
    return wave

def export_mp3(path: Path, wave: np.ndarray) -> float:
    wav = path.with_suffix(".wav")
    sf.write(wav, wave, SAMPLE_RATE, subtype="PCM_16")
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(wav), "-af", "loudnorm=I=-17:TP=-1.5:LRA=9",
        "-ar", "24000", "-ac", "1", "-c:a", "libmp3lame", "-b:a", "80k",
        str(path),
    ], check=True)
    wav.unlink()
    assert path.stat().st_size > 2000, path
    return round(len(wave) / SAMPLE_RATE, 3)

def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    pipeline = KPipeline(lang_code="b")
    combined = [silence(.4)]
    metadata = {
        "project": "Th’die’s Cast",
        "voice": VOICE,
        "speed": SPEED,
        "spoken_podcast_title": "The die's cast",
        "status": "experimental name auditions; no name chosen",
        "note": "TTS was given the seven exact candidate spellings, including TheDie vs The Die.",
        "candidates": [],
    }
    for i, candidate in enumerate(CANDIDATES, 1):
        name = candidate["name"]
        a = (
            f"The old roads have brought you to {name}. "
            "This is the die's cast. Listen well."
        )
        b = candidate["second"]
        print(f"Rendering {i:02d}: {name}", flush=True)
        intro = synth(pipeline, a)
        outro = synth(pipeline, b)
        track = np.concatenate([
            silence(.35), intro, silence(1.15),
            outro, silence(.6)
        ])
        filename = f"{i:02d}-{candidate['slug']}.mp3"
        duration = export_mp3(OUT / filename, track)
        announcement = synth(pipeline, f"Candidate {i}.")
        combined += [
            silence(.2), announcement, silence(.45),
            track, silence(1.35)
        ]
        metadata["candidates"].append({
            "number": i,
            "printed_name": name,
            "tts_text_one": a,
            "tts_text_two": b,
            "filename": filename,
            "duration_seconds_approx": duration,
        })

    audio = np.concatenate(combined + [silence(.4)])
    compilation_duration = export_mp3(OUT / COMPILATION, audio)
    metadata["compilation_filename"] = COMPILATION
    metadata["compilation_duration_seconds_approx"] = compilation_duration
    (OUT / "manifest.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Ready: {len(CANDIDATES)} candidates; compilation {compilation_duration}s", flush=True)

if __name__ == "__main__":
    main()
