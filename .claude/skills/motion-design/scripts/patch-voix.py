#!/usr/bin/env python3
"""Lay re-recorded sentences over their slots in the voice montage (a brand name that changed, a wrong word).

build-audio.sh calls it after the montage when <project>/assets/audio/patch-voix.json exists, so the patch survives
every rebuild. Each entry replaces one sentence:

  [{"take": "assets/audio/reprises/marque.mp3",   # the new take (ElevenLabs, same voice and model as the film)
    "slot": [42.62, 46.96],                       # where it goes in the montage (s): from the old sentence's start
                                                  # to just before the next sentence
    "speech": [0.00, 4.93],                       # optional: speech bounds inside the take (default: detected)
    "drop": [1.22, 1.47]}]                        # optional: a pause inside the take to shorten

The old sentence is muted from slot start - 0.45 s (the attack of its first word starts before the transcript says:
a stray "i" of the old "IFS" stayed audible with a 0.12 s margin) to slot end. The take is sped up just enough to fit
(atempo, never slowed down); keep it under x1.10 or regenerate a tighter take. Afterwards redo the word timings
(mots.py) and update the cues of the frames concerned.

Usage: python3 patch-voix.py <voix-montage.wav> <patch-voix.json>
"""
import json, os, re, subprocess, sys

LEAD = 0.45


def speech_bounds(path):
    out = subprocess.run(["ffmpeg", "-nostats", "-i", path, "-af", "silencedetect=n=-40dB:d=0.08", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                               capture_output=True, text=True).stdout)
    starts = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", out)]
    ends = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", out)]
    a = ends[0] if starts and starts[0] < 0.02 and ends else 0.0          # leading silence
    b = starts[-1] if starts and (not ends or starts[-1] > ends[-1]) else dur  # trailing silence
    return max(0.0, a - 0.02), min(dur, b + 0.03)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    voice, cfg = sys.argv[1], sys.argv[2]
    patches = json.load(open(cfg, encoding="utf-8"))
    args = ["ffmpeg", "-v", "error", "-y", "-i", voice]
    graph, labels, mute = [], [], []
    for k, p in enumerate(patches):
        take = p["take"]
        if not os.path.exists(take):
            sys.exit(f"patch-voix: {take} not found")
        a, b = p.get("speech") or speech_bounds(take)
        s, e = p["slot"]
        drop = p.get("drop")
        args += ["-i", take]
        speech = (b - a) - ((drop[1] - drop[0]) if drop else 0)
        tempo = max(1.0, speech / (e - s))
        if drop:
            chain = (f"[{k + 1}]atrim={a}:{drop[0]},asetpts=PTS-STARTPTS[p{k}a];[{k + 1}]atrim={drop[1]}:{b},"
                     f"asetpts=PTS-STARTPTS[p{k}b];[p{k}a][p{k}b]concat=n=2:v=0:a=1,")
        else:
            chain = f"[{k + 1}]atrim={a}:{b},asetpts=PTS-STARTPTS,"
        d = int(s * 1000)
        graph.append(chain + f"atempo={tempo:.4f},aformat=sample_rates=44100:channel_layouts=stereo,"
                             f"afade=t=in:d=0.02,adelay={d}|{d}[n{k}]")
        labels.append(f"[n{k}]")
        mute.append(f"between(t,{max(0.0, s - LEAD):.3f},{e:.3f})")
        warn = "  (over x1.10: regenerate a tighter take)" if tempo > 1.10 else ""
        print(f"patch-voix: {os.path.basename(take)}: {speech:.2f} s of speech in {e - s:.2f} s, tempo x{tempo:.3f}{warn}")
    graph.insert(0, f"[0]aformat=sample_rates=44100:channel_layouts=stereo,volume=enable='{'+'.join(mute)}':volume=0[base]")
    graph.append("[base]" + "".join(labels) + f"amix=inputs={len(labels) + 1}:normalize=0:duration=first[out]")
    tmp = voice + ".tmp.wav"
    subprocess.run(args + ["-filter_complex", ";".join(graph), "-map", "[out]", tmp], check=True)
    os.replace(tmp, voice)


if __name__ == "__main__":
    main()
