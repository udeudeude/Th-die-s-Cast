#!/usr/bin/env python3
"""Voice-test ten possible 'Brother ...' narrator names using Kokoro Lewis.

No character identity is approved until the user listens. Synthesis text uses
the already-approved spoken podcast title "the die's cast", not the stylized
written title. All clips are fully rendered MP3, not device TTS.
"""
from pathlib import Path
import json
import subprocess

import numpy as np
import soundfile as sf
from kokoro import KPipeline

SAMPLE_RATE = 24000
VOICE = "bm_lewis"
SPEED = 0.94
OUT = Path("auditions/brother")
OUT.mkdir(parents=True, exist_ok=True)

NAMES = [
    "Godric", "Blaise", "Oswin", "Aelfric", "Cuthbert",
    "Dunstan", "Peregrine", "Anselm", "Wulfstan", "Berengar"
]

def silence(seconds):
    return np.zeros(round(SAMPLE_RATE*seconds), dtype=np.float32)

def say(pipeline, phrase):
    chunks = []
    for _,_,audio in pipeline(phrase, voice=VOICE, speed=SPEED):
        chunks.append(np.asarray(audio, dtype=np.float32).reshape(-1))
    if not chunks:
        raise RuntimeError(f"Speech synthesis returned nothing: {phrase}")
    audio = np.concatenate(chunks)
    fade = min(int(0.015*SAMPLE_RATE), len(audio)//4)
    if fade:
        ramp = np.linspace(0,1,fade,endpoint=False,dtype=np.float32)
        audio[:fade] *= ramp
        audio[-fade:] *= ramp[::-1]
    return audio

def save_mp3(destination,wave):
    wav = destination.with_suffix(".wav")
    sf.write(wav, wave, SAMPLE_RATE, subtype="PCM_16")
    subprocess.run([
        "ffmpeg","-hide_banner","-loglevel","error","-y",
        "-i",str(wav),"-af","loudnorm=I=-17:TP=-1.5:LRA=9",
        "-ar","24000","-ac","1","-codec:a","libmp3lame",
        "-b:a","80k",str(destination)
    ], check=True)
    wav.unlink()
    assert destination.stat().st_size > 1000
    return round(len(wave)/SAMPLE_RATE,3)

def main():
    pipeline = KPipeline(lang_code="b")
    manifest = {
        "written_series_title":"Th’die’s Cast",
        "approved_tts_series_name":"The die's cast.",
        "voice":VOICE,"speed":SPEED,
        "purpose":"Draft auditions only. Character name not selected.",
        "candidates":[]
    }
    collection = []
    for index,name in enumerate(NAMES,1):
        print(f"Rendering {index}: Brother {name}",flush=True)
        lines = [
            f"Greetings. I'm Brother {name}. Welcome to the die's cast.",
            f"I'm Brother {name}. Thank you for joining the die's cast."
        ]
        takes = [say(pipeline,line) for line in lines]
        clip = np.concatenate([silence(.3),takes[0],silence(1.2),takes[1],silence(.65)])
        target=OUT/f"{index:02d}-brother-{name.lower()}.mp3"
        duration=save_mp3(target,clip)
        manifest["candidates"].append({
            "number":index,"name":f"Brother {name}","tts_lines":lines,
            "mp3":target.name,"duration_seconds_approx":duration
        })
        spoken_number=say(pipeline,f"Number {index}. Brother {name}.")
        collection.extend([silence(.9),spoken_number,silence(.7),clip,silence(1.3)])
    compilation=OUT/"00-all-ten-brother-names.mp3"
    compilation_duration=save_mp3(compilation,np.concatenate(collection))
    manifest["compilation_file"]=compilation.name
    manifest["compilation_duration_seconds_approx"]=compilation_duration
    (OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    assert len(manifest["candidates"])==10
    print("Ready:",compilation,compilation.stat().st_size,"bytes",flush=True)

if __name__=="__main__":
    main()
