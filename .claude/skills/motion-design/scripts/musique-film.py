#!/usr/bin/env python3
"""Compose a score locked on the edit, by script: no sample, no generative service, so it is free of rights.

Use it when the user provides no CC0 track (references/music.md). The sections follow the acts and the cuts of the
storyboard, so the music changes exactly where the film changes. Written for the Contino Sport film, whose user found
a calm loop "boring": the score must follow the picture (tension that builds, a cut to the pivot, a groove for the
process, a drop on the payoff, a final chord).

Config <project>/assets/audio/musique.json:
  {"total": 52.0, "bpm": 120, "seed": 11,
   "sections": [
     {"type": "tension", "start": 0.0,   "end": 15.2,  "key": "A"},   # minor, pulses and builds, roll into the cut
     {"type": "pivot",   "start": 15.2,  "end": 18.7,  "key": "C"},   # low drone, heartbeat, swell into the light
     {"type": "groove",  "start": 18.7,  "end": 37.45, "key": "C"},   # major groove: kick, clap, hats, bass, arpeggio
     {"type": "hymne",   "start": 37.45, "end": 49.8,  "key": "F"},   # drop on the first beat, wider chords
     {"type": "fin",     "start": 49.8,  "end": 52.0,  "key": "C"}],  # one ringing chord
   "hits": [39.58]}                                                   # extra big kicks (a smash, a stamp)

Usage: python3 musique-film.py <project>/assets/audio/musique.json [out.wav]   (default out: musique.wav beside it)
Then: MUSIC=assets/audio/musique.wav MUSIC_VOLUME=0.22 bash <project>/build-audio.sh (the mix ducks it under the voice).
"""
import json, os, sys, wave
import numpy as np

SR = 44100
NOTE = {"C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5, "F#": 6, "Gb": 6, "G": 7, "G#": 8,
        "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11}
# chord progressions as (root offset, chord intervals), one chord per bar
PROG = {
    "tension": [(0, [0, 3, 7]), (-4, [0, 4, 7]), (-2, [0, 4, 7]), (-5, [0, 4, 7])],   # i VI VII V (Am F G E)
    "groove": [(0, [0, 4, 7]), (7, [0, 4, 7]), (9, [0, 3, 7]), (5, [0, 4, 7])],       # I V vi IV
    "hymne": [(0, [0, 4, 7]), (2, [0, 4, 7]), (4, [0, 3, 7]), (-5, [0, 4, 7])],       # IV V vi I seen from IV
}


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    cfg = json.load(open(sys.argv[1], encoding="utf-8"))
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(sys.argv[1]), "musique.wav")
    total = float(cfg["total"]); N = int(SR * total); B = 60.0 / float(cfg.get("bpm", 120))
    rng = np.random.default_rng(int(cfg.get("seed", 11)))
    L = np.zeros(N); R = np.zeros(N); SC = np.ones(N)

    def hz(m): return 440 * 2 ** ((m - 69) / 12)

    def put(buf, t, sig, g):
        i = int(t * SR)
        if i >= N or i + len(sig) <= 0: return
        j = min(N, i + len(sig)); buf[max(i, 0):j] += sig[max(0, -i): j - i] * g

    def st(t, sig, g, pan=0.0):
        put(L, t, sig, g * (1 - pan)); put(R, t, sig, g * (1 + pan))

    def lp(x, a):
        y = np.empty_like(x); acc = 0.0
        for k in range(len(x)):
            acc += (1 - a) * (x[k] - acc); y[k] = acc
        return y

    def saw(f, n, phase=0.0):
        return 2 * ((f * np.arange(n) / SR + phase) % 1) - 1

    def adsr(n, a, d, s, r):
        e = np.full(n, s); ia, idd, ir = int(a * SR), int(d * SR), int(r * SR)
        e[:ia] = np.linspace(0, 1, max(ia, 1))[:min(ia, n)]
        e[ia:ia + idd] = np.linspace(1, s, max(idd, 1))[:max(0, min(idd, n - ia))]
        if ir: e[-ir:] *= np.linspace(1, 0, min(ir, n))
        return e

    def kick(big=False):
        n = int(SR * (0.6 if big else 0.35)); t = np.arange(n) / SR
        f = 45 + 110 * np.exp(-t / 0.035)
        s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / (0.28 if big else 0.16))
        s[:200] += rng.standard_normal(200) * 0.3 * np.linspace(1, 0, 200)
        return np.tanh(s * 1.6)

    def clap():
        n = int(SR * 0.22); x = rng.standard_normal(n); x = x - lp(x, 0.85)
        return x * np.exp(-np.arange(n) / SR / 0.05)

    def hat(open_=False):
        n = int(SR * (0.18 if open_ else 0.05)); x = rng.standard_normal(n); x = x - lp(x, 0.5)
        return x * np.exp(-np.arange(n) / SR / (0.06 if open_ else 0.012))

    def bass(m, dur, cut=0.92):
        n = int(SR * dur); s = saw(hz(m), n) + 0.5 * np.sin(2 * np.pi * hz(m - 12) * np.arange(n) / SR)
        return lp(s, cut) * adsr(n, 0.005, 0.08, 0.7, 0.03)

    def pluck(m, dur=0.25):
        n = int(SR * dur); s = saw(hz(m), n) + saw(hz(m) * 1.004, n)
        return lp(s, 0.8) * np.exp(-np.arange(n) / SR / 0.09)

    def pad(ms, dur, cut=0.95, a=0.3):
        n = int(SR * dur); s = np.zeros(n)
        for m in ms:
            for d in (-0.12, 0, 0.11):
                s += saw(hz(m) * 2 ** (d / 12), n, phase=rng.random())
        return lp(s / (3 * len(ms)), cut) * adsr(n, a, 0.2, 0.85, 0.35)

    def drone(m, dur):
        n = int(SR * dur); t = np.arange(n) / SR
        return np.sin(2 * np.pi * hz(m) * t) * np.sin(np.pi * t / dur) ** 0.7

    def duck(t, depth=0.65, length=0.32):
        i = int(t * SR); j = min(N, i + int(length * SR))
        if i >= N: return
        SC[i:j] = np.minimum(SC[i:j], 1 - depth * np.exp(-np.arange(j - i) / SR / (length / 3.5)))

    def bars_of(sec):
        t0, t1 = float(sec["start"]), float(sec["end"])
        k = 0
        while t0 + k * 4 * B < t1 - 0.05:
            tb = t0 + k * 4 * B; yield k, tb, min(4 * B, t1 - tb); k += 1

    sections = cfg["sections"]
    for si, sec in enumerate(sections):
        typ = sec["type"]; t0, t1 = float(sec["start"]), float(sec["end"])
        key = NOTE[sec.get("key", "C")]
        nxt = sections[si + 1]["type"] if si + 1 < len(sections) else None
        if typ == "tension":
            base = 57 + ((key - 9 + 6) % 12) - 6                     # around A3
            nb = max(1, int(np.ceil((t1 - t0) / (4 * B))))
            for k, tb, dur in bars_of(sec):
                ro, iv = PROG["tension"][k % 4]; root = base + ro; ch = [root + x for x in iv]
                g = k / max(1, nb - 1)
                st(tb, pad([m - 12 for m in ch], dur, cut=0.97 - 0.03 * g), 0.09 + 0.07 * g)
                for q in range(8):
                    tq = tb + q * B / 2
                    if tq + B / 2 > t1: break
                    st(tq, bass(root - 24, B / 2 * 0.9, cut=0.94 - 0.07 * g), 0.16)
                for q in range(4):
                    tq = tb + q * B
                    if tq >= t1 - 0.05: break
                    if k >= 1 and (q in (0, 2) or g > 0.45): st(tq, kick(), 0.42); duck(tq)
                    if k >= 2: st(tq + B / 2, hat(), 0.05 + 0.04 * g, 0.3)
                    if g > 0.6 and q in (1, 3): st(tq, clap(), 0.12)
                if k % 2 == 1 and k >= 2:
                    for j, m in enumerate([ch[2] + 12, ch[1] + 12, ch[0] + 12, ch[1] + 12]):
                        st(tb + 2 * B + j * B / 2, pluck(m), 0.06, -0.3)
            if nxt in ("pivot", None):                                 # roll that accelerates into the cut
                for j in range(12):
                    st(t1 - 1.2 + j * 0.1, clap(), 0.05 + 0.012 * j)
        elif typ == "pivot":
            dur = t1 - t0
            st(t0, drone(33 + key % 12, dur), 0.08)
            for j in range(6):                                         # heartbeat that speeds up
                tt = t0 + dur * (0.2 + 0.75 * (1 - (1 - j / 6) ** 1.6))
                st(tt, kick(), 0.22 + 0.03 * j)
            sw = pad([60 + key, 64 + key, 67 + key, 71 + key], min(2.0, dur * 0.6), cut=0.9, a=1.4)
            st(t1 - len(sw) / SR, sw * np.linspace(0, 1, len(sw)) ** 2, 0.16)
        elif typ in ("groove", "hymne"):
            base = 48 + key if typ == "groove" else 53 + ((key - 5) % 12)
            if typ == "hymne":
                st(t0, kick(big=True), 0.6); duck(t0, 0.8, 0.5); st(t0, drone(36 + key % 12, 1.6), 0.25)
            for k, tb, dur in bars_of(sec):
                ro, iv = PROG[typ][k % 4]; root = base + ro
                ch = [root + 12 + x for x in iv] if typ == "groove" else [root + 12 + x for x in iv] + [root]
                st(tb, pad(ch, dur, cut=0.93 if typ == "groove" else 0.9, a=0.05 if typ == "groove" else 0.03),
                   0.11 if typ == "groove" else 0.13)
                for q in range(16):
                    tq = tb + q * B / 4
                    if tq >= t1 - 0.02: break
                    if q % 4 == 0: st(tq, kick(), 0.48 if typ == "groove" else 0.5); duck(tq)
                    if q in (4, 12): st(tq, clap(), 0.16 if typ == "groove" else 0.18)
                    st(tq, hat(open_=(q % 4 == 2)), 0.045 if q % 2 else 0.065, 0.25)
                    if q % 2 == 0:
                        bm = root - 12 + (12 if (typ == "groove" and q in (6, 14)) else 0)
                        st(tq, bass(bm, B / 2 * 0.8), 0.15 if typ == "groove" else 0.16)
                    if typ == "hymne" or k >= 2:
                        m = ch[(q * (2 if typ == "hymne" else 1)) % 3] + (12 * (1 + (q // 8) % 2) if typ == "groove" else 0)
                        st(tq, pluck(m, 0.2 if typ == "groove" else 0.18), 0.045 if typ == "groove" else 0.05,
                           -0.35 + 0.7 * ((q % 4) / 3))
            if nxt == "hymne":                                         # noise riser into the drop
                nz = rng.standard_normal(int(SR * 1.5)); nz = (nz - lp(nz, 0.7)) * np.linspace(0, 1, len(nz)) ** 2
                st(t1 - 1.5, nz, 0.09)
        elif typ == "fin":
            fin = pad([60 + key, 64 + key, 67 + key, 72 + key, 76 + key], max(1.0, t1 - t0), cut=0.9, a=0.02)
            st(t0, fin * np.exp(-np.arange(len(fin)) / SR / 1.1), 0.2); st(t0, kick(big=True), 0.45)
        else:
            sys.exit(f"musique-film: unknown section type {typ!r} (tension, pivot, groove, hymne, fin)")
    for t in cfg.get("hits", []):
        st(float(t), kick(big=True), 0.55); duck(float(t), 0.8, 0.45)

    L *= SC ** 0.6; R *= SC ** 0.6
    L = np.tanh(L * 1.4); R = np.tanh(R * 1.4)
    fade = np.ones(N); fi, fo = int(SR * 0.3), int(SR * 1.2)
    fade[:fi] = np.linspace(0, 1, fi); fade[-fo:] = np.linspace(1, 0, fo)
    L *= fade; R *= fade
    peak = max(np.abs(L).max(), np.abs(R).max()); L /= peak / 0.89; R /= peak / 0.89
    w = wave.open(out, "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.stack([L, R], 1) * 32767).astype("<i2").tobytes()); w.close()
    print(f"musique-film: {out} ({total:.2f} s, {len(sections)} sections, {len(cfg.get('hits', []))} hit(s))")


if __name__ == "__main__":
    main()
