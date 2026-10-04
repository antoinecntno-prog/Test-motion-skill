"""Compose la musique du film (52 s, chill, 84 BPM) : piano électrique, basse douce, batterie feutrée.
Composition procédurale propre au projet, sans échantillon tiers : libre de droits (CC0).
Le pivot (15,20 à 18,70 s) retire la batterie et les accords, pour laisser le noir respirer."""
import numpy as np, wave, sys
SR = 44100; TOTAL = 52.0; BPM = 84; BEAT = 60 / BPM; BAR = 4 * BEAT
N = int(SR * TOTAL); L = np.zeros(N); R = np.zeros(N)
rng = np.random.default_rng(7)
def note(f): return 440 * 2 ** ((f - 69) / 12)
def add(buf, start, sig, gain=1.0):
    i = int(start * SR)
    if i >= N: return
    j = min(N, i + len(sig)); buf[i:j] += sig[: j - i] * gain
def env(n, a, d):
    t = np.arange(n) / SR
    return np.minimum(1, t / a) * np.exp(-t / d)
def epiano(f, dur):
    n = int(SR * (dur + 1.5)); t = np.arange(n) / SR
    mod = np.sin(2 * np.pi * f * t) * 1.6 * np.exp(-t / 0.35)       # FM : attaque de type Rhodes
    s = np.sin(2 * np.pi * f * t + mod) + 0.25 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / 0.6)
    trem = 1 + 0.12 * np.sin(2 * np.pi * 4.2 * t)
    return s * env(n, 0.006, 1.6) * trem
def lowpass(x, a):                                                     # filtre à un pôle, a proche de 1 = plus doux
    y = np.empty_like(x); acc = 0.0
    for k in range(len(x)): acc = a * acc + (1 - a) * x[k]; y[k] = acc
    return y
# progression : Fmaj7 Em7 Dm7 Cmaj7 (un accord par mesure)
CH = [[53, 57, 60, 64], [52, 55, 59, 62], [50, 53, 57, 60], [48, 52, 55, 59]]
ROOT = [41, 40, 38, 36]
pivot = (15.20, 18.70)
def in_pivot(t): return pivot[0] - 0.2 <= t < pivot[1]
bar = 0; t = 0.0
while t < TOTAL - 0.5:
    c = CH[bar % 4]
    if not in_pivot(t):
        for k, m in enumerate(c):                                      # accord arpégé doucement (strum)
            s = epiano(note(m), BAR)
            pan = 0.35 + 0.1 * k
            add(L, t + k * 0.018, s, 0.11 * (1 - pan)); add(R, t + k * 0.018, s, 0.11 * pan)
        if bar % 2 == 1:                                               # petite réponse mélodique
            for k, m in enumerate([c[3] + 12, c[2] + 12]):
                s = epiano(note(m), BEAT); add(L, t + 2.5 * BEAT + k * BEAT * 0.75, s, 0.05); add(R, t + 2.5 * BEAT + k * BEAT * 0.75, s, 0.06)
        n = int(SR * BAR); tt = np.arange(n) / SR                      # basse ronde
        b = np.sin(2 * np.pi * note(ROOT[bar % 4]) * tt) * np.minimum(1, tt / 0.02) * np.exp(-tt / 1.8)
        add(L, t, b, 0.20); add(R, t, b, 0.20)
        for q in range(8):                                             # batterie feutrée
            bt = t + q * BEAT / 2
            if in_pivot(bt) or bt < 2.0: continue                     # pas de batterie avant 2 s : l'accroche reste à la voix
            if q in (0, 4):
                m = int(SR * 0.4); tk = np.arange(m) / SR
                k = np.sin(2 * np.pi * (48 + 70 * np.exp(-tk / 0.03)) * tk) * np.exp(-tk / 0.12)
                add(L, bt, k, 0.32); add(R, bt, k, 0.32)
            if q in (2, 6):
                m = int(SR * 0.25); r = rng.standard_normal(m) * np.exp(-np.arange(m) / SR / 0.06)
                add(L, bt, r, 0.035); add(R, bt, r, 0.04)
            m = int(SR * 0.05); h = rng.standard_normal(m) * np.exp(-np.arange(m) / SR / 0.012)
            h = h - lowpass(h, 0.6)
            add(L, bt, h, 0.03 if q % 2 else 0.05); add(R, bt + 0.004, h, 0.03 if q % 2 else 0.05)
    else:                                                              # pivot : une seule nappe grave, très basse
        n = int(SR * BAR); tt = np.arange(n) / SR
        p = np.sin(2 * np.pi * note(36) * tt) * np.sin(np.pi * np.minimum(1, tt / BAR))
        add(L, t, p, 0.08); add(R, t, p, 0.08)
    bar += 1; t += BAR
# grain de vinyle très discret, adoucissement global, fondus
noise = lowpass(rng.standard_normal(N) * 0.004, 0.7)
L += noise; R += noise
L = lowpass(L, 0.35); R = lowpass(R, 0.35)
fade = np.ones(N); fi = int(SR * 1.2); fo = int(SR * 3.0)
fade[:fi] = np.linspace(0, 1, fi); fade[-fo:] = np.linspace(1, 0, fo)
L *= fade; R *= fade
peak = max(np.abs(L).max(), np.abs(R).max()); L /= peak / 0.89; R /= peak / 0.89
out = sys.argv[1] if len(sys.argv) > 1 else "assets/audio/musique-chill.wav"
w = wave.open(out, "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((np.stack([L, R], 1) * 32767).astype("<i2").tobytes()); w.close()
print(out, f"{TOTAL} s")
