"""Remplace « IFS » par « Contino Sport » dans le montage voix : les deux phrases de marque sont reprises
(ElevenLabs, voix Paul K, eleven_v4, assets/audio/contino/) et posées dans leurs créneaux, légèrement resserrées."""
import subprocess, sys, os
VOICE = sys.argv[1] if len(sys.argv) > 1 else "assets/audio/voix-montage.wav"
# (prise, début et fin de la parole dans la prise, créneau dans le film, coupe de pause interne (de, à))
PATCHES = [
    ("assets/audio/contino/avec-a.mp3",   0.06, 2.76, (18.86, 21.40), None),
    ("assets/audio/contino/marque-a.mp3", 0.00, 4.93, (42.62, 46.96), (1.22, 1.47)),
]
tmp = VOICE + ".tmp.wav"
args = ["ffmpeg", "-v", "error", "-y", "-i", VOICE]
graph, labels = [], []
mute = []
for k, (src, a, b, (s, e), cut) in enumerate(PATCHES):
    args += ["-i", src]
    speech = (b - a) - ((cut[1] - cut[0]) if cut else 0)
    tempo = max(1.0, speech / (e - s))
    if cut:
        chain = (f"[{k+1}]atrim={a}:{cut[0]},asetpts=PTS-STARTPTS[p{k}a];[{k+1}]atrim={cut[1]}:{b},asetpts=PTS-STARTPTS[p{k}b];"
                 f"[p{k}a][p{k}b]concat=n=2:v=0:a=1,")
    else:
        chain = f"[{k+1}]atrim={a}:{b},asetpts=PTS-STARTPTS,"
    d = int(s * 1000)
    graph.append(chain + f"atempo={tempo:.4f},aformat=sample_rates=44100:channel_layouts=stereo,afade=t=in:d=0.02,adelay={d}|{d}[n{k}]")
    labels.append(f"[n{k}]"); mute.append(f"between(t,{s - 0.45},{e})")   # couvre l'attaque de l'ancien « IFS » (le « i » parasite)
    print(f"{os.path.basename(src)} : {speech:.2f} s de parole dans {e - s:.2f} s, tempo x{tempo:.3f}")
graph.insert(0, f"[0]aformat=sample_rates=44100:channel_layouts=stereo,volume=enable='{'+'.join(mute)}':volume=0[base]")
graph.append("[base]" + "".join(labels) + f"amix=inputs={len(labels)+1}:normalize=0:duration=first[out]")
subprocess.run(args + ["-filter_complex", ";".join(graph), "-map", "[out]", tmp], check=True)
os.replace(tmp, VOICE)
