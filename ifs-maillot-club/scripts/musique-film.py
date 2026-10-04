"""Compose la musique du film (52 s) calée sur le montage : composition procédurale propre au projet,
sans échantillon tiers, donc libre de droits.

Quatre parties, chacune démarre sur sa coupe :
  douleur   0,00 à 15,20 : la minuscule, pulsation qui monte, coupée net au noir du pivot
  pivot    15,20 à 18,70 : un battement grave et une nappe qui gonfle jusqu'à l'éclair
  process  18,70 à 37,45 : groove majeur à 120 BPM, kick, clap, charleston, basse, arpège, pompe de sidechain
  match    37,45 à 52,00 : drop au « Samedi », coup sur le smash (39,58), accords d'hymne, fin qui résonne
"""
import numpy as np, wave, sys

SR = 44100; TOTAL = 52.0; N = int(SR * TOTAL)
L = np.zeros(N); R = np.zeros(N); SC = np.ones(N)          # SC : enveloppe de sidechain (les nappes respirent sur le kick)
rng = np.random.default_rng(11)
BPM = 120; B = 60 / BPM                                    # un temps = 0,5 s

def hz(m): return 440 * 2 ** ((m - 69) / 12)
def put(buf, t, sig, g=1.0):
    i = int(t * SR)
    if i >= N or i + len(sig) <= 0: return
    j = min(N, i + len(sig)); buf[max(i, 0):j] += sig[max(0, -i): j - i] * g
def st(t, sig, g, pan=0.0):
    put(L, t, sig, g * (1 - pan) ); put(R, t, sig, g * (1 + pan))
def lp(x, a):
    y = np.empty_like(x); acc = 0.0
    for k in range(len(x)): acc += (1 - a) * (x[k] - acc); y[k] = acc
    return y
def saw(f, n, phase=0.0):
    t = np.arange(n) / SR; return 2 * ((f * t + phase) % 1) - 1
def adsr(n, a, d, s, r):
    e = np.full(n, s); ia, idd, ir = int(a * SR), int(d * SR), int(r * SR)
    e[:ia] = np.linspace(0, 1, max(ia, 1))[:min(ia, n)]
    e[ia:ia + idd] = np.linspace(1, s, max(idd, 1))[:max(0, min(idd, n - ia))]
    if ir: e[-ir:] *= np.linspace(1, 0, min(ir, n))
    return e

# ---------- instruments ----------
def kick(g=1.0, big=False):
    n = int(SR * (0.6 if big else 0.35)); t = np.arange(n) / SR
    f = 45 + 110 * np.exp(-t / 0.035)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / (0.28 if big else 0.16))
    s[:200] += rng.standard_normal(200) * 0.3 * np.linspace(1, 0, 200)     # clic d'attaque
    return np.tanh(s * 1.6) * g
def clap():
    n = int(SR * 0.22); t = np.arange(n) / SR; x = rng.standard_normal(n)
    x = x - lp(x, 0.85)
    e = np.exp(-t / 0.05); e[:int(.01 * SR)] *= 0.6; return x * e
def hat(open_=False):
    n = int(SR * (0.18 if open_ else 0.05)); x = rng.standard_normal(n); x = x - lp(x, 0.5)
    return x * np.exp(-np.arange(n) / SR / (0.06 if open_ else 0.012))
def bass(m, dur, cut=0.92):
    n = int(SR * dur); s = saw(hz(m), n) + 0.5 * np.sin(2 * np.pi * hz(m - 12) * np.arange(n) / SR)
    return lp(s, cut) * adsr(n, 0.005, 0.08, 0.7, 0.03)
def pluck(m, dur=0.3):
    n = int(SR * dur); s = saw(hz(m), n) + saw(hz(m) * 1.004, n)
    return lp(s, 0.8) * np.exp(-np.arange(n) / SR / 0.09)
def pad(ms, dur, cut=0.95, a=0.3):
    n = int(SR * dur); s = np.zeros(n)
    for m in ms:
        for d in (-0.12, 0, 0.11):                          # supersaw doux
            s += saw(hz(m) * 2 ** (d / 12), n, phase=rng.random())
    return lp(s / (3 * len(ms)), cut) * adsr(n, a, 0.2, 0.85, 0.35)
def sub_drone(m, dur):
    n = int(SR * dur); t = np.arange(n) / SR
    return np.sin(2 * np.pi * hz(m) * t) * np.sin(np.pi * t / dur) ** 0.7

def duck(t, depth=0.65, length=0.32):
    i = int(t * SR); n = int(length * SR); j = min(N, i + n)
    if i >= N: return
    curve = 1 - depth * np.exp(-np.arange(j - i) / SR / (length / 3.5))
    SC[i:j] = np.minimum(SC[i:j], curve)

# ---------- 1. douleur (0 à 15,20) : la mineur, 120 BPM, tension qui monte ----------
PAIN = [(57, [57, 60, 64]), (53, [53, 57, 60]), (55, [55, 59, 62]), (52, [52, 56, 59])]   # Am F G E
t0, end = 0.0, 15.20
for bar in range(8):
    tb = t0 + bar * 4 * B
    if tb >= end: break
    root, ch = PAIN[bar % 4]
    st(tb, pad([m - 12 for m in ch], min(4 * B, end - tb), cut=0.97 - 0.004 * bar), 0.09 + 0.01 * bar)
    for q in range(8):                                       # basse en croches, pulsation
        tq = tb + q * B / 2
        if tq + B / 2 > end: break
        st(tq, bass(root - 24, B / 2 * 0.9, cut=0.94 - 0.01 * bar), 0.16)
    for q in range(4):
        tq = tb + q * B
        if tq >= end - 0.05: break
        if bar >= 1 and (q in (0, 2) or bar >= 4): st(tq, kick(), 0.42); duck(tq)
        if bar >= 2: st(tq + B / 2, hat(), 0.05 + 0.006 * bar, 0.3)
        if bar >= 5 and q in (1, 3): st(tq, clap(), 0.12)
    if bar % 2 == 1 and bar >= 2:                            # motif aigu inquiet
        for k, m in enumerate([ch[2] + 12, ch[1] + 12, ch[0] + 12, ch[1] + 12]):
            st(tb + 2 * B + k * B / 2, pluck(m, 0.25), 0.06, -0.3)
for k in range(12):                                          # roulement qui accélère avant la coupe
    st(14.0 + k * 0.1, clap(), 0.05 + 0.012 * k)

# ---------- 2. pivot (15,20 à 18,70) : noir, battement, nappe qui gonfle ----------
st(15.20, sub_drone(33, 3.5), 0.08)
for k, tt in enumerate([15.90, 16.30, 16.95, 17.35, 18.00, 18.40]):
    st(tt, kick(big=False), 0.22 + 0.03 * k)
sw = pad([60, 64, 67, 71], 2.0, cut=0.9, a=1.6)             # Cmaj7 qui monte vers l'éclair
st(16.70, sw * np.linspace(0, 1, len(sw)) ** 2, 0.16)

# ---------- 3. process (18,70 à 37,45) : do majeur, groove ----------
PROC = [(48, [60, 64, 67]), (55, [59, 62, 67]), (57, [60, 64, 69]), (53, [57, 60, 65])]   # C G Am F
t0, end = 18.70, 37.45
bars = int(np.ceil((end - t0) / (4 * B)))
for bar in range(bars):
    tb = t0 + bar * 4 * B
    root, ch = PROC[bar % 4]
    dur = min(4 * B, end - tb)
    if dur <= 0: break
    st(tb, pad(ch, dur, cut=0.93, a=0.05), 0.11)
    for q in range(16):                                      # 16 doubles croches
        tq = tb + q * B / 4
        if tq >= end - 0.02: break
        if q % 4 == 0: st(tq, kick(), 0.48); duck(tq)
        if q in (4, 12): st(tq, clap(), 0.16)
        st(tq, hat(open_=(q % 4 == 2)), 0.045 if q % 2 else 0.065, 0.25)
        if q % 2 == 0:                                       # basse syncopée
            bm = root - 12 + (12 if q in (6, 14) else 0)
            st(tq, bass(bm, B / 2 * 0.8), 0.15)
        if bar >= 2:                                         # arpège qui court
            m = ch[q % 3] + 12 * (1 + (q // 8) % 2)
            st(tq, pluck(m, 0.2), 0.045, -0.35 + 0.7 * ((q % 4) / 3))
# montée vers le match
nz = rng.standard_normal(int(SR * 1.5)); nz = (nz - lp(nz, 0.7)) * np.linspace(0, 1, len(nz)) ** 2
st(35.95, nz, 0.09)

# ---------- 4. match et marque (37,45 à 52) ----------
st(37.45, kick(big=True), 0.6); duck(37.45, 0.8, 0.5)
st(37.45, sub_drone(36, 1.6), 0.25)
MATCH = [(53, [65, 69, 72]), (55, [67, 71, 74]), (57, [64, 69, 72]), (48, [64, 67, 72])]   # F G Am C, hymne
t0, end = 37.45, 49.80
bars = int(np.ceil((end - t0) / (4 * B)))
for bar in range(bars):
    tb = t0 + bar * 4 * B
    root, ch = MATCH[bar % 4]
    dur = min(4 * B, end - tb)
    if dur <= 0: break
    st(tb, pad(ch + [ch[0] - 12], dur, cut=0.9, a=0.03), 0.13)
    for q in range(16):
        tq = tb + q * B / 4
        if tq >= end - 0.02: break
        if q % 4 == 0: st(tq, kick(), 0.5); duck(tq)
        if q in (4, 12): st(tq, clap(), 0.18)
        if q in (14,) and bar % 2: st(tq, clap(), 0.10)
        st(tq, hat(open_=(q % 4 == 2)), 0.05 if q % 2 else 0.07, 0.25)
        if q % 2 == 0: st(tq, bass(root - 12, B / 2 * 0.85), 0.16)
        m = ch[(q * 2) % 3] + 12
        st(tq, pluck(m, 0.18), 0.05, 0.3 - 0.6 * ((q % 4) / 3))
st(39.58, kick(big=True), 0.55); duck(39.58, 0.8, 0.45)      # le smash
fin = pad([60, 64, 67, 72, 76], 2.2, cut=0.9, a=0.02)         # accord final qui résonne
st(49.80, fin * np.exp(-np.arange(len(fin)) / SR / 1.1), 0.2); st(49.80, kick(big=True), 0.45)

# ---------- mixage ----------
L *= SC ** 0.6; R *= SC ** 0.6
L = np.tanh(L * 1.4); R = np.tanh(R * 1.4)                   # colle et chaleur
fade = np.ones(N); fi = int(SR * 0.3); fo = int(SR * 1.2)
fade[:fi] = np.linspace(0, 1, fi); fade[-fo:] = np.linspace(1, 0, fo)
L *= fade; R *= fade
peak = max(np.abs(L).max(), np.abs(R).max()); L /= peak / 0.89; R /= peak / 0.89
out = sys.argv[1] if len(sys.argv) > 1 else "assets/audio/musique-film.wav"
w = wave.open(out, "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((np.stack([L, R], 1) * 32767).astype("<i2").tobytes()); w.close()
print(out, f"{TOTAL} s")
