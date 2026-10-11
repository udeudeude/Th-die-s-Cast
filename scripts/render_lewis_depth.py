#!/usr/bin/env python3
"""Create controlled A/B depth and character auditions for Lewis.

These are experiments only. Do not overwrite or re-publish the podcast pilot.
The same baseline Kokoro output is processed seven different ways. For the
speed comparison, atempo preserves the pitch; for the depth comparisons,
rubberband preserves duration and can preserve or shift formants.
"""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

import numpy as np
import soundfile as sf
from kokoro import KPipeline

OUT = Path("auditions/lewis-depth")
OUT.mkdir(parents=True, exist_ok=True)
BASE = OUT / "_original-temporary.wav"
RATE = 24000
SPEED = 0.94
VOICE = "bm_lewis"
SCRIPT = (
    "I am Brother Berengar. Welcome to the die's cast. "
    "The road is long, and fortune seldom walks beside us. "
    "Still, you may roll."
)
VARIANTS = [
    ("01", "natural", "Natural Lewis", "an unmodified Kokoro recording", None),
    ("02", "slower", "Deliberate and slow", "11 percent slower, with the same pitch", "atempo=0.89"),
    ("03", "deep-gentle", "Six percent deeper", "pitch 0.94, duration preserved, formants preserved", "pitch:0.94:preserved"),
    ("04", "deep-medium", "Twelve percent deeper", "pitch 0.88, duration preserved, formants preserved", "pitch:0.88:preserved"),
    ("05", "deep-dark", "Darkened and resonant", "pitch 0.88, duration preserved, formants shifted", "pitch:0.88:shifted"),
    ("06", "warm-close", "Warm and close", "pitch 0.92, warmth EQ and modest compression", "pitch:0.92:preserved,highpass=f=75,bass=g=2:f=155,acompressor=threshold=-22dB:ratio=1.5:attack=18:release=150"),
    ("07", "stone-hall", "Quiet stone hall", "pitch 0.92, subtle room echo", "pitch:0.92:preserved,highpass=f=75,aecho=0.65:0.16:110:0.10"),
]

def run(cmd):
    subprocess.run(cmd, check=True)

def silence(seconds):
    return np.zeros(round(RATE * seconds), dtype=np.float32)

def synthesis(pipe, words):
    fragments = []
    for _, _, audio in pipe(words, voice=VOICE, speed=SPEED):
        if fragments:
            fragments.append(silence(.08))
        fragments.append(np.asarray(audio, dtype=np.float32).reshape(-1))
    if not fragments:
        raise RuntimeError("Kokoro gave no audio for "+words)
    return np.concatenate(fragments)

def supports_rubberband():
    p = subprocess.run(["ffmpeg","-hide_banner","-filters"],check=True,capture_output=True,text=True)
    return bool(re.search(r"\brubberband\b",p.stdout+p.stderr))

def build_filter(config, rubberband_enabled):
    if not config:
        return "anull"
    parts=[]
    for section in config.split(","):
        if section.startswith("pitch:"):
            _, fraction, formants = section.split(":")
            scale = float(fraction)
            if rubberband_enabled:
                parts.append(f"rubberband=pitch={scale}:tempo=1:formant={formants}")
            else:
                # Fallback: accurate speed, but note that formant preservation
                # is unavailable with this resampling method.
                parts.append(f"asetrate={int(RATE*scale)},aresample={RATE},atempo={1/scale:.7f}")
        else:
            parts.append(section)
    return ",".join(parts)

def export(src, dest, filterchain, bitrate="96k"):
    run([
        "ffmpeg","-hide_banner","-loglevel","error","-y",
        "-i",str(src),"-af",filterchain+",loudnorm=I=-17:TP=-1.5:LRA=7",
        "-ar",str(RATE),"-ac","1","-c:a","libmp3lame",
        "-b:a",bitrate,str(dest),
    ])
    probe=subprocess.check_output([
        "ffprobe","-v","error","-show_entries","format=duration,size",
        "-of","json",str(dest),
    ],text=True)
    return json.loads(probe)["format"]

def main():
    pipe=KPipeline(lang_code="b")
    raw=np.concatenate([silence(.30),synthesis(pipe,SCRIPT),silence(.65)])
    sf.write(BASE,raw,RATE,subtype="PCM_16")
    rubberband=supports_rubberband()
    print("Rubber Band pitch filter:",rubberband,flush=True)
    manifest={
        "series":"Th’die’s Cast",
        "narrator":"Kokoro bm_lewis",
        "base_speed":SPEED,
        "reference_script":SCRIPT,
        "formant_preserving_filter_available":rubberband,
        "status":"technical voice auditions, no changes to released/pilot content",
        "variants":[],
    }
    clips=[]
    for i,slug,title,description,config in VARIANTS:
        name=f"{i}-{slug}.mp3"
        path=OUT/name
        filters=build_filter(config,rubberband)
        print(i,title,filters,flush=True)
        props=export(BASE,path,filters)
        manifest["variants"].append({
            "number":int(i),"label":title,"description":description,
            "filename":name,"filter":filters,
            "duration_seconds":float(props["duration"]),
            "size_bytes":int(props["size"]),
            "formant_caveat":("Fallback resampling shifts formants" if not rubberband and "pitch:" in (config or "") else ""),
        })
        clips.append(path)

    # A single recording for iPhone use. We concatenate the already-mastered MP3
    # files after first decoding to WAV, so the introduction numbering is clear.
    combined=[silence(.3)]
    for k,item in enumerate(manifest["variants"]):
        announcement=synthesis(pipe,f"Version {item['number']}. {item['label']}.")
        combined.extend([announcement,silence(.5)])
        decoded=OUT/f"_clip-{k}.wav"
        run(["ffmpeg","-hide_banner","-loglevel","error","-y",
             "-i",str(clips[k]),"-ar",str(RATE),"-ac","1",str(decoded)])
        wave,sr=sf.read(decoded,dtype="float32")
        assert sr==RATE
        combined.extend([np.asarray(wave,dtype=np.float32).reshape(-1),silence(1.0)])
        decoded.unlink()
    composite_wav=OUT/"_compilation-temp.wav"
    sf.write(composite_wav,np.concatenate(combined),RATE,subtype="PCM_16")
    composite_path=OUT/"00-all-seven-lewis-depth-auditions.mp3"
    composite_details=export(composite_wav,composite_path,"anull")
    manifest["compilation_filename"]=composite_path.name
    manifest["compilation_seconds"]=float(composite_details["duration"])
    (OUT/"manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    BASE.unlink()
    composite_wav.unlink()
    assert len(clips)==7 and all(f.stat().st_size>6000 for f in clips)
    print("All seven auditions generated",manifest["compilation_seconds"],flush=True)

if __name__=="__main__":
    main()
