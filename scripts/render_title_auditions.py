#!/usr/bin/env python3
"""Produce a blind-able audition of the show title in the chosen Lewis voice.

These are *phonetic experiments*, not a final title pronunciation.
Each candidate is synthesized as the exact source string below.
"""
from pathlib import Path
import json
import subprocess

import numpy as np
import soundfile as sf
from kokoro import KPipeline

VOICE = "bm_lewis"
SPEED = 0.94
RATE = 24000
OUT = Path("auditions/title")
OUT.mkdir(parents=True, exist_ok=True)

CANDIDATES = [
    ("01", "the-die-is-cast", "The die is cast."),
    ("02", "the-dies-cast", "The die's cast."),
    ("03", "th-dies-cast", "Th' die's cast."),
    ("04", "thud-eyes-cast", "Thud eyes cast."),
    ("05", "tuh-dize-cast", "Tuh dize cast."),
    ("06", "thuh-dies-cast", "Thuh die's cast."),
    ("07", "the-die-is-comma-cast", "The die, is cast."),
    ("08", "the-dies-unspaced", "The'die's cast."),
    ("09", "tha-dies-cast", "Tha die's cast."),
    ("10", "stylized-written-title", "Th'die's Cast."),
]

def render(pipeline, text):
    parts=[]
    for _,_,audio in pipeline(text,voice=VOICE,speed=SPEED):
        parts.append(np.asarray(audio,dtype=np.float32).reshape(-1))
    if not parts:
        raise RuntimeError("No speech for: "+text)
    audio=np.concatenate(parts)
    # Short, consistent padding prevents trimmed consonants on iPhone playback.
    start=np.zeros(round(.4*RATE), dtype=np.float32)
    end=np.zeros(round(.55*RATE), dtype=np.float32)
    return np.concatenate([start,audio,end])

def export(path,wave):
    wav=path.with_suffix(".wav")
    sf.write(wav,wave,RATE)
    subprocess.run([
        "ffmpeg","-hide_banner","-loglevel","error","-y",
        "-i",str(wav),"-af","loudnorm=I=-17:TP=-1.5:LRA=9",
        "-ar","24000","-ac","1","-codec:a","libmp3lame","-b:a","96k",str(path)
    ],check=True)
    wav.unlink()
    return round(len(wave)/RATE,3)

def main():
    pipe=KPipeline(lang_code="b")
    manifest={"voice":VOICE,"speed":SPEED,"description":"Title pronunciation audition; not an approved brand lockup","candidates":[]}
    compilation=[]
    for ident,slug,phrase in CANDIDATES:
        print("Voice take",ident,phrase,flush=True)
        wave=render(pipe,phrase)
        mp3=OUT/f"{ident}-{slug}.mp3"
        length=export(mp3,wave)
        manifest["candidates"].append({"number":int(ident),"tts_text":phrase,"file":mp3.name,"duration_sec_approx":length})
        # A numbered label makes the compilation usable entirely by ear.
        intro=render(pipe,f"Version {int(ident)}.")
        compilation.extend([intro,np.zeros(round(.4*RATE),dtype=np.float32),wave,np.zeros(round(1.0*RATE),dtype=np.float32)])
    compilation_wave=np.concatenate(compilation)
    compile_path=OUT/"00-all-ten-title-pronunciations.mp3"
    duration=export(compile_path,compilation_wave)
    manifest["compilation_file"]=compile_path.name
    manifest["compilation_duration_sec_approx"]=duration
    (OUT/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    for row in manifest["candidates"]:
        assert (OUT/row["file"]).stat().st_size>1000
    print("Ready",compile_path,"duration",duration,"seconds",flush=True)

if __name__=="__main__":
    main()
