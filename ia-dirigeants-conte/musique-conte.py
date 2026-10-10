#!/usr/bin/env python3
"""Two scores for « Le Temps perdu » (ia-dirigeants-conte), composed by script.

numpy synthesis only: no sample, no network, no generative service, so the music is free of rights.
House approach (motion-design/references/music.md, scripts/musique-film.py): the sections are locked on the
edit of STORYBOARD.md and the music changes exactly where the film changes. This tale needs other instruments
than musique-film.py, and no drums: a music box (plucked comb tines) over low strings (cello, double bass).

Acts (global seconds):
  pain      0.00 to 31.15  minor; the box MUFFLED (low-pass 1.4 kHz, heard through a wall), low tense strings;
                           chord changes on the seams 5.25, 10.76, 16.42, 20.38, 25.40; the box runs down
                           around « Interminable Attente » (17.67 to 20.08: longer gaps, flatter, a held note);
                           « Soir après soir » 20.68 to 22.57: a fast repeated figure (time passing); the silent
                           gag 22.57 to 25.51 almost bare, one box note answers like the pendulum at 24.28.
  stop      31.15          the lamp goes out: everything stops, digital silence.
  pivot     32.20          only a very low string drone fades in (the dominant of the major key to come).
  idée      33.30          the box starts again, CLEAR and bright (no low-pass), in the major key.
  solution  34.60 to 53.10 major, warmer and wider strings, clear melody; the opening melody comes back in
                           major at 38.25 (rhyme); gentle swells at 44.97 (gold letters) and 49.83 (the house).
  end       53.10 to 57.10 one final chord, the box rings out, silence at 57.10.

Options (same act times):
  M1  3/4 waltz lullaby around 76 bpm, A minor then A major.
  M2  6/8 lullaby around 60 bpm, D minor then F major (relative major), another melody, rocking strings.
Each section holds a whole number of beats, so the tempo breathes a little from one section to the next
(rubato of a tale) while every chord change and every phrase start falls on its seam.

Under the narrator: no percussion, strings low-passed under 1.1 kHz, box melody one note per beat at most in
the speech, a gentle 2.6 kHz dip on the clear box. Peak -3 dBFS; the project mix lowers and ducks it
(MUSIC=assets/audio/musique-M1.wav bash build-audio.sh, sidechain on the voice).

Usage:
  python3 musique-conte.py              # renders assets/audio/musique-M1.wav and musique-M2.wav, then checks
  python3 musique-conte.py M2           # one option only
  python3 musique-conte.py --check      # checks the existing files only
Output: 44.1 kHz, 16-bit stereo, exactly 57.10 s, deterministic (fixed seed per option).
"""
import json, os, sys, wave
import numpy as np

SR = 44100
TOTAL = 57.10
N = int(round(TOTAL * SR))
HERE = os.path.dirname(os.path.abspath(__file__))
AUDIO = os.path.join(HERE, "assets", "audio")
PEAK_DBFS = -3.0
SEEDS = {"M1": 7301, "M2": 7302}

# the edit (global seconds, STORYBOARD.md)
SEAMS = [0.00, 5.25, 10.76, 16.42, 20.38, 25.40]
SOIR = (20.68, 22.57)     # « Soir après soir »: fast repeated figure, fading as he fades
GAG = (22.57, 25.51)      # silent gag: almost bare
PENDULE = 24.28           # one box note answers like the pendulum
STOP = 31.15              # the lamp goes out: the music stops
DRONE = 32.20             # a very low string drone fades in
IDEE = 33.30              # « idée »: the box again, clear, in major
SOL = 34.60               # solution
REPRISE = 38.25           # the opening melody in major (the swing)
GOLD = 44.97              # swell: the gold letters
HOUSE = 49.83             # swell: the house relights
END = 53.10               # one final chord


# ----------------------------------------------------------------------------------------------------- synthesis
def hz(m, cents=0.0):
    return 440.0 * 2.0 ** ((m - 69) / 12.0 + cents / 1200.0)


def pan_gains(p):
    a = (float(np.clip(p, -1, 1)) + 1) * np.pi / 4
    return np.cos(a), np.sin(a)


def box_tone(f, vel, decay, rng):
    """One plucked comb tine: sine partials with a slight inharmonicity, 1.5 ms attack, long exponential decay,
    a twin tine that beats slowly, the first beam mode of the tine (x6.27, the metal) and a little click."""
    tau = float(np.clip(2.1 * (523.25 / f) ** 0.55, 0.55, 2.8)) * decay
    n = int(min(6.0 * tau, 9.0) * SR)
    t = np.arange(n) / SR
    bright = 0.6 + 0.4 * vel
    B = 0.0004
    parts = ((1.0, 1.0, 1.0),
             (1.0 + rng.uniform(0.5, 1.1) / f, 0.30, 0.8),     # twin tine, about one beat per second
             (2 * np.sqrt(1 + 4 * B), 0.22 * bright, 0.42),
             (3 * np.sqrt(1 + 9 * B), 0.06 * bright, 0.24),
             (6.267, 0.10 * bright, 0.05),                     # beam mode of a clamped tine
             (17.55, 0.025 * bright, 0.015))
    y = np.zeros(n)
    for r, a, k in parts:
        if f * r < 0.45 * SR:
            y += a * np.exp(-t / (tau * k)) * np.sin(2 * np.pi * f * r * t)
    na = int(0.0015 * SR)
    y[:na] *= np.sin(0.5 * np.pi * np.arange(na) / na) ** 2
    nc = int(0.006 * SR)
    c = np.diff(rng.standard_normal(nc + 2), 2) / 2.45
    y[:nc] += 0.10 * bright * c * np.exp(-np.arange(nc) / SR / 0.0008)
    return y * vel


def additive(phase, amp):
    """sum_k amp[k-1] sin(k phase), by the Chebyshev recurrence (no aliasing, cheap)."""
    s1 = np.sin(phase)
    c2 = 2 * np.cos(phase)
    y = amp[0] * s1
    sp, sk = np.zeros_like(s1), s1
    for a in amp[1:]:
        sn = c2 * sk - sp
        y += a * sn
        sp, sk = sk, sn
    return y


def string_note(m, dur, vel, cutoff, attack, release, rng, spread, vib, cresc=(1.0, 1.0), trem=None):
    """A section of low strings on one note: band-limited sawtooth voices (low-passed 12 dB/oct at `cutoff`),
    slightly detuned, a gentle delayed vibrato, slow attack, exponential release."""
    f0 = hz(m)
    n = int((dur + release) * SR)
    t = np.arange(n) / SR
    K = max(1, int(min(3.5 * cutoff, 5000.0) / f0))
    k = np.arange(1, K + 1)
    amp = (1.0 / k) / np.sqrt(1.0 + (k * f0 / cutoff) ** 4)
    nv = 3 if m >= 40 else 2
    out = np.zeros((2, n))
    for v in range(nv):
        det = (v - (nv - 1) / 2) * 6.0 + rng.uniform(-1.5, 1.5)
        drift = 2.0 * np.sin(2 * np.pi * rng.uniform(0.07, 0.17) * t + rng.uniform(0, 2 * np.pi))
        vib_env = np.clip((t - 0.3) / 0.9, 0, 1)
        cents = det + drift + vib * vib_env * np.sin(2 * np.pi * rng.uniform(4.7, 5.6) * t + rng.uniform(0, 2 * np.pi))
        phase = 2 * np.pi * np.cumsum(f0 * 2.0 ** (cents / 1200.0)) / SR + rng.uniform(0, 2 * np.pi)
        s = additive(phase, amp)
        p = spread * (2 * v / (nv - 1) - 1) * (0.35 if m < 40 else 1.0)
        gl, gr = pan_gains(p)
        out[0] += s * gl
        out[1] += s * gr
    env = np.ones(n)
    na, nd = int(attack * SR), min(int(dur * SR), n)
    env[:na] = np.sin(0.5 * np.pi * np.arange(na) / na) ** 2
    env[:nd] *= np.interp(t[:nd], [0, dur], cresc)
    if trem is not None:                                  # (start in note seconds, rate Hz, depth)
        ts, rate, depth = trem
        w = (t >= ts) & (t < dur)
        d = depth * np.clip((t[w] - ts) / 0.5, 0, 1)
        env[w] *= 1 - d * (0.5 + 0.5 * np.cos(2 * np.pi * rate * (t[w] - ts)))
    tr = t[nd:] - dur
    env[nd:] *= env[nd - 1] * np.exp(-tr / (release / 3.5)) * np.clip(1 - tr / release, 0, 1)
    return out * env * (vel / nv)


def fft_filter(x, H):
    """Zero-phase filter of a (2, N) bus by the magnitude response H(f)."""
    nfft = 1 << int(np.ceil(np.log2(N + SR)))
    X = np.fft.rfft(x, nfft, axis=1)
    return np.fft.irfft(X * H(np.fft.rfftfreq(nfft, 1 / SR)), nfft, axis=1)[:, :N]


def lowpass(fc, order=4):
    return lambda f: 1.0 / np.sqrt(1.0 + (f / fc) ** (2 * order))


def presence_dip(f0=2600.0, db=-4.0, width=0.9):
    g = 10 ** (db / 20)
    return lambda f: 1.0 - (1.0 - g) * np.exp(-0.5 * (np.log2(np.maximum(f, 1.0) / f0) / width) ** 2)


def reverb(send, rng, rt60=2.4, length=3.2):
    """A small room behind the canvas: sparse early reflections, a dark tail (highs die 3x faster)."""
    n = int(length * SR)
    t = np.arange(n) / SR
    nfft_ir = 1 << int(np.ceil(np.log2(n)))
    lp = lowpass(3000.0, 2)(np.fft.rfftfreq(nfft_ir, 1 / SR))
    irs = []
    for _ in range(2):
        z = rng.standard_normal(n)
        low = np.fft.irfft(np.fft.rfft(z, nfft_ir) * lp, nfft_ir)[:n]
        ir = low * np.exp(-6.91 * t / rt60) + (z - low) * np.exp(-6.91 * t / (rt60 * 0.33))
        ir *= np.clip((t - 0.022) / 0.03, 0, 1)            # predelay, soft onset
        for tap in rng.uniform(0.009, 0.06, 6):
            ir[int(tap * SR)] += rng.uniform(-0.35, 0.35) * np.sqrt(np.sum(ir ** 2) / 200.0)
        irs.append(ir / np.sqrt(np.sum(ir ** 2)))
    nfft = 1 << int(np.ceil(np.log2(N + n)))
    S = np.fft.rfft(send.mean(axis=0), nfft)
    return np.stack([np.fft.irfft(S * np.fft.rfft(ir, nfft), nfft)[:N] for ir in irs])


def db_curve(points):
    tt, dd = zip(*points)
    return 10 ** (np.interp(np.arange(N) / SR, tt, dd) / 20)


# --------------------------------------------------------------------------------------------------- the score
class Score:
    def __init__(self, seed):
        self.rng = np.random.default_rng(seed)
        self.muf = np.zeros((2, N))      # the box through the wall (pain)
        self.clr = np.zeros((2, N))      # the box in the room (from « idée »)
        self.str = np.zeros((2, N))      # low strings
        self.rock = np.ones(N)           # cradle swell of the strings (M2)

    def put(self, bus, t, sig):
        i = int(round(t * SR))
        n = sig.shape[1]
        if i >= N or i + n <= 0:
            return
        a, j = max(i, 0), min(N, i + n)
        bus[:, a:j] += sig[:, a - i:j - i]

    def box(self, t, m, vel, clear, decay=1.0, cents=None):
        cents = self.rng.uniform(-4.0, 4.0) if cents is None else cents + self.rng.uniform(-1.5, 1.5)
        y = box_tone(hz(m, cents), vel, decay, self.rng)
        gl, gr = pan_gains(np.clip((m - 74) / 30.0, -0.4, 0.4) + self.rng.uniform(-0.08, 0.08))  # comb: low left
        self.put(self.clr if clear else self.muf, t, np.stack([y * gl, y * gr]))

    def line(self, t0, beat, notes, clear, unit=1.0):
        """notes: (position, midi, velocity[, decay]) with position in units of `unit` beats."""
        for nt in notes:
            self.box(t0 + nt[0] * unit * beat, nt[1], nt[2], clear, nt[3] if len(nt) > 3 else 1.0)

    def roll(self, t, notes, clear, gap=0.045, decay=1.0):
        for i, (m, v) in enumerate(notes):
            self.box(t + i * gap, m, v, clear, decay)

    def waltz(self, t0, beat, bars, clear, vb=0.34, vd=0.2):
        """3/4 music-box accompaniment: bass on 1, a soft dyad on 2 and 3."""
        for pos, bass, dyad in bars:
            self.box(t0 + pos * beat, bass, vb, clear, 0.55)
            for q in (1, 2):
                for m in dyad:
                    self.box(t0 + (pos + q) * beat, m, vd, clear, 0.45)

    def chord(self, t0, t1, notes, vel=1.0, cutoff=620.0, attack=0.7, release=0.9, lead=0.12, spread=0.3,
              vib=8.0, cresc=(1.0, 1.0), trem=None):
        """Strings from t0 (the attack starts `lead` earlier so the chord is there on the seam) to t1."""
        start = t0 - lead
        for m, v in notes:
            tr = None if trem is None else (trem[0] - start, trem[1], trem[2])
            self.put(self.str, start, string_note(m, t1 - start, vel * v, cutoff, attack, release, self.rng,
                                                  spread, vib, cresc, tr))

    def rocking(self, anchors, depth_points):
        """Cradle: the strings swell on every dotted-quarter beat. anchors: (time, beat index)."""
        tt, bb = zip(*anchors)
        x = np.arange(N) / SR
        frac = np.interp(x, tt, bb) % 1.0
        depth = np.interp(x, *zip(*depth_points))
        self.rock = 1.0 - depth * (0.5 - 0.5 * np.cos(2 * np.pi * frac))


PAIN = dict(cutoff=620.0, attack=0.75, release=0.9, spread=0.3, vib=8.0)
SOLN = dict(cutoff=950.0, attack=0.55, release=1.0, spread=0.75, vib=11.0)
BLOOM = dict(SOLN, cutoff=1100.0)


def seg(t0, t1, beats):
    return t0, (t1 - t0) / beats


def score_m1(s):
    """3/4 waltz lullaby, about 76 bpm, A minor then A major. Opening motif E A B C | B A."""
    # ---- pain: A minor, the box through the wall -------------------------------------------------------------
    t0, b = seg(0.00, 5.25, 7)                                  # Am: the opening melody (returns at 38.25)
    s.line(t0, b, [(0, 76, .62), (1, 81, .66), (2, 83, .62), (3, 84, .72, 1.3), (5, 83, .58), (6, 81, .64, 1.5)], False)
    s.waltz(t0, b, [(0, 57, (60, 64)), (3, 57, (60, 64))], False)
    s.chord(0.00, 5.25, [(33, .5), (45, .55), (52, .45), (60, .32)], lead=0.0, **PAIN)

    t0, b = seg(5.25, 10.76, 7)                                 # F: he walks past her
    s.line(t0, b, [(0, 84, .64), (1, 83, .58), (2, 81, .6), (3, 77, .68, 1.3), (5, 76, .55), (6, 77, .6, 1.5)], False)
    s.waltz(t0, b, [(0, 53, (57, 60)), (3, 53, (57, 60))], False)
    s.chord(5.25, 10.76, [(29, .45), (41, .5), (48, .45), (57, .36)], **PAIN)

    t0, b = seg(10.76, 16.42, 7)                                # Dm: the motif sinks a fifth, the evening
    s.line(t0, b, [(0, 69, .6), (1, 74, .62), (2, 76, .6), (3, 77, .7, 1.3), (5, 76, .56), (6, 74, .62, 1.5)], False)
    s.waltz(t0, b, [(0, 50, (53, 57)), (3, 50, (53, 57))], False)
    s.chord(10.76, 16.42, [(38, .5), (45, .5), (50, .42), (53, .4), (57, .22)], **PAIN)

    # E7: « Interminable Attente », the mechanism runs out: gaps grow, pitch sags, the last note is held
    for t, m, v, c, d in ((16.42, 83, .62, 0, 1.0), (17.00, 81, .58, -5, 1.0), (17.67, 80, .56, -11, 1.1),
                          (18.45, 77, .55, -18, 1.2), (19.38, 76, .6, -27, 2.6)):
        s.box(t, m, v, False, d, cents=c)
    s.chord(16.42, 20.38, [(28, .45), (40, .5), (47, .42), (50, .38), (56, .34)], cresc=(0.85, 1.2), **PAIN)

    # Am: « Soir après soir », a fast repeated figure that fades with him, then the bare gag
    s.chord(20.38, 22.75, [(52, .4), (60, .28)], **dict(PAIN, release=1.2))
    s.chord(20.38, 25.40, [(33, .45), (45, .45)], cresc=(1.0, 0.6), **PAIN)
    t, i = SOIR[0], 0
    while t <= SOIR[1] - 0.12:
        fr = (t - SOIR[0]) / (SOIR[1] - SOIR[0])
        s.box(t, (76, 81, 84)[i % 3], 0.6 - 0.28 * fr, False, 0.7)
        t += 0.21 - 0.045 * fr
        i += 1
    s.box(PENDULE, 76, .5, False, 1.6)                          # the lone note answers like the pendulum

    t0, b = seg(25.40, STOP, 7)                                 # Dm, then E7b9 rising to the stop
    s.line(t0, b, [(0, 77, .6), (1, 81, .62), (2, 86, .66), (3, 84, .7, 1.2), (5, 83, .6), (6, 80, .64, 1.6)], False)
    s.waltz(t0, b, [(0, 50, (53, 57)), (3, 52, (56, 62))], False)
    s.chord(25.40, t0 + 3 * b, [(38, .5), (45, .5), (50, .42), (53, .4)], **PAIN)
    s.chord(t0 + 3 * b, STOP + 0.3, [(28, .45), (40, .52), (47, .42), (50, .38), (53, .3), (56, .34)],
            cresc=(0.9, 1.35), trem=(30.10, 7.5, 0.35), **PAIN)

    # ---- pivot: silence, then the dominant pedal very low; « idée »: the box, clear, A major -----------------
    s.chord(DRONE, 34.75, [(28, .6), (40, .5), (35, .18)], lead=0.0, cutoff=320.0, attack=1.8, release=1.2,
            spread=0.15, vib=3.0)
    s.box(IDEE, 88, .6, True, 1.2)
    s.box(IDEE + 0.012, 81, .32, True)
    for t, m, v in ((33.92, 81, .42), (34.17, 85, .48), (34.40, 88, .52), (SOL, 93, .55)):
        s.box(t, m, v, True, 1.3 if t == SOL else 1.0)

    # ---- solution: A major, warm and wide ------------------------------------------------------------------
    t0, b = seg(SOL, REPRISE, 5)                                # A (held), then D/A: the clock gets to work
    s.chord(SOL, t0 + 2 * b, [(33, .42), (45, .5), (52, .45), (57, .4), (61, .34)], **SOLN)
    s.chord(t0 + 2 * b, REPRISE, [(33, .38), (45, .45), (50, .42), (54, .4), (57, .36), (62, .28)], **SOLN)
    s.line(t0, b, [(2, 78, .45), (3, 81, .48), (4, 78, .44)], True)
    s.box(t0 + 2 * b, 62, .3, True, 0.55)
    for q in (3, 4):
        for m in (66, 69):
            s.box(t0 + q * b, m, .18, True, 0.45)

    t0, b = seg(REPRISE, GOLD, 9)                               # the opening melody, in major (rhyme)
    s.line(t0, b, [(0, 76, .6), (1, 81, .64), (2, 83, .6), (3, 85, .7, 1.2), (5, 83, .58), (6, 81, .62),
                   (7, 80, .55), (8, 83, .56)], True)
    s.waltz(t0, b, [(0, 57, (61, 64)), (3, 62, (66, 69)), (6, 64, (68, 71))], True, vb=.3, vd=.17)
    s.chord(REPRISE, t0 + 3 * b, [(33, .42), (45, .5), (52, .45), (57, .4), (61, .34)], **SOLN)
    s.chord(t0 + 3 * b, t0 + 6 * b, [(38, .45), (45, .48), (50, .42), (54, .4), (57, .36), (62, .26)], **SOLN)
    s.chord(t0 + 6 * b, GOLD, [(28, .4), (40, .48), (47, .44), (52, .38), (56, .36), (59, .28)], **SOLN)

    t0, b = seg(GOLD, HOUSE, 6)                                 # swell: the gold letters (D bloom, then E)
    s.roll(GOLD, [(62, .3), (74, .42), (78, .4), (81, .5)], True)
    s.line(t0, b, [(2, 86, .52), (3, 85, .6, 1.2), (5, 83, .55)], True)
    for q in (1, 2):
        for m in (66, 69):
            s.box(t0 + q * b, m, .16, True, 0.45)
    s.waltz(t0, b, [(3, 64, (68, 71))], True, vb=.28, vd=.16)
    s.chord(GOLD, t0 + 3 * b, [(38, .45), (45, .5), (50, .45), (54, .42), (57, .4), (62, .32), (66, .24)], **BLOOM)
    s.chord(t0 + 3 * b, HOUSE, [(28, .4), (40, .5), (47, .44), (52, .4), (56, .38), (59, .3), (64, .22)], **BLOOM)

    t0, b = seg(HOUSE, END, 4)                                  # swell: the house relights (A bloom), E7
    s.roll(HOUSE, [(57, .3), (69, .38), (73, .4), (76, .45), (81, .52)], True)
    s.line(t0, b, [(1, 85, .5), (2, 83, .48), (3, 80, .5)], True)
    for q in (1, 2):
        for m in (61, 64):
            s.box(t0 + q * b, m, .16, True, 0.45)
    s.box(t0 + 3 * b, 64, .26, True, 0.55)
    s.chord(HOUSE, t0 + 3 * b, [(33, .45), (45, .52), (52, .46), (57, .42), (61, .38), (64, .3), (69, .22)], **BLOOM)
    s.chord(t0 + 3 * b, END, [(28, .4), (40, .5), (47, .44), (50, .38), (56, .36), (59, .28)], **SOLN)

    # ---- end: one A major chord, the box rings out -----------------------------------------------------------
    s.chord(END, 56.4, [(33, .48), (45, .52), (52, .46), (57, .42), (61, .38), (64, .3)], **dict(SOLN, release=1.4))
    s.roll(END, [(57, .3), (69, .36), (73, .4), (76, .44), (81, .5), (85, .46), (88, .42)], True, gap=0.06, decay=1.8)


def score_m2(s):
    """6/8 lullaby, about 60 bpm (dotted quarter), D minor then F major. Positions in eighths (unit 1/3)."""
    E = 1 / 3
    # ---- pain: D minor, the box through the wall -------------------------------------------------------------
    t0, b = seg(0.00, 5.25, 5)                                  # Dm: the opening melody (returns at 38.25)
    s.line(t0, b, [(0, 74, .6), (2, 76, .5), (3, 77, .64), (5, 81, .6), (6, 79, .62), (8, 77, .52),
                   (9, 76, .64, 1.3), (12, 74, .64, 1.6)], False, E)
    s.line(t0, b, [(0, 50, .32, .6), (3, 57, .24, .5), (6, 50, .3, .6), (9, 57, .22, .5), (12, 50, .26, .6)], False, E)
    s.chord(0.00, 5.25, [(38, .5), (45, .48), (50, .42), (53, .38)], lead=0.0, **PAIN)

    t0, b = seg(5.25, 10.76, 6)                                 # Bb
    s.line(t0, b, [(0, 77, .62), (2, 74, .5), (3, 70, .58), (5, 74, .5), (6, 77, .62), (8, 79, .52),
                   (9, 77, .64, 1.3), (12, 74, .6, 1.2), (15, 72, .55, 1.3)], False, E)
    s.line(t0, b, [(0, 58, .3, .6), (3, 53, .22, .5), (6, 58, .3, .6), (9, 53, .22, .5), (12, 58, .28, .6),
                   (15, 53, .2, .5)], False, E)
    s.chord(5.25, 10.76, [(34, .45), (46, .48), (53, .4), (58, .36), (62, .28)], **PAIN)

    t0, b = seg(10.76, 16.42, 6)                                # Gm, the leading tone at the end
    s.line(t0, b, [(0, 67, .58), (2, 70, .5), (3, 74, .62), (5, 72, .5), (6, 70, .6), (8, 69, .5),
                   (9, 67, .6, 1.3), (12, 69, .56, 1.2), (15, 73, .58, 1.3)], False, E)
    s.line(t0, b, [(0, 55, .3, .6), (3, 50, .22, .5), (6, 55, .3, .6), (9, 50, .22, .5), (12, 57, .28, .6),
                   (15, 52, .2, .5)], False, E)
    s.chord(10.76, 16.42, [(31, .4), (43, .48), (50, .42), (55, .38), (58, .34)], **PAIN)

    # A7: « Interminable Attente », the opening motif tries again and runs out, stuck on the seventh (held)
    for t, m, v, c, d in ((16.42, 74, .6, 0, 1.0), (17.02, 76, .56, -5, 1.0), (17.67, 77, .56, -11, 1.1),
                          (18.47, 81, .55, -18, 1.2), (19.42, 79, .6, -28, 2.6)):
        s.box(t, m, v, False, d, cents=c)
    s.chord(16.42, 20.38, [(33, .45), (45, .5), (52, .42), (55, .38), (61, .32)], cresc=(0.85, 1.2), **PAIN)

    # Dm: « Soir après soir », a pendulum figure in fast motion that fades with him, then the bare gag
    s.chord(20.38, 22.75, [(50, .42), (53, .36)], **dict(PAIN, release=1.2))
    s.chord(20.38, 25.40, [(38, .45), (45, .4)], cresc=(1.0, 0.6), **PAIN)
    t, i = SOIR[0], 0
    while t <= SOIR[1] - 0.12:
        fr = (t - SOIR[0]) / (SOIR[1] - SOIR[0])
        s.box(t, (74, 77, 81, 77)[i % 4], 0.58 - 0.28 * fr, False, 0.7)
        t += 0.19 - 0.04 * fr
        i += 1
    s.box(PENDULE, 69, .52, False, 1.6)                         # the lone note answers like the pendulum

    t0, b = seg(25.40, STOP, 6)                                 # Gm, then A7b9 rising to the stop
    s.line(t0, b, [(0, 70, .58), (2, 74, .5), (3, 79, .64), (5, 77, .52), (6, 76, .62), (8, 79, .52),
                   (9, 82, .66, 1.2), (12, 81, .64, 1.2), (15, 73, .6, 1.6)], False, E)
    s.line(t0, b, [(0, 55, .3, .6), (3, 50, .22, .5), (6, 57, .3, .6), (9, 52, .22, .5), (12, 57, .28, .6)], False, E)
    s.chord(25.40, t0 + 2 * b, [(31, .4), (43, .48), (50, .42), (55, .38), (58, .34)], **PAIN)
    s.chord(t0 + 2 * b, STOP + 0.3, [(33, .45), (45, .52), (52, .42), (55, .38), (58, .3), (61, .34)],
            cresc=(0.9, 1.35), trem=(30.10, 7.0, 0.35), **PAIN)
    s.rocking([(0.0, 0), (5.25, 5), (10.76, 11), (16.42, 17), (20.38, 21), (25.40, 26), (STOP, 32), (SOL, 35),
               (REPRISE, 39), (GOLD, 46), (HOUSE, 51), (END, 54), (TOTAL, 58)],
              [(0, .16), (20.2, .16), (20.5, 0), (25.3, 0), (25.6, .16), (31.0, .16), (31.1, 0), (34.5, 0),
               (35.0, .12), (52.9, .12), (53.2, 0)])

    # ---- pivot: silence, then C (the dominant of F) very low; « idée »: the box, clear, F major -------------
    s.chord(DRONE, 34.75, [(24, .55), (36, .55), (43, .16)], lead=0.0, cutoff=320.0, attack=1.8, release=1.2,
            spread=0.15, vib=3.0)
    s.box(IDEE, 84, .6, True, 1.2)
    s.box(IDEE + 0.012, 77, .32, True)
    for t, m, v in ((33.92, 77, .42), (34.17, 81, .48), (34.40, 84, .52), (SOL, 89, .55)):
        s.box(t, m, v, True, 1.3 if t == SOL else 1.0)

    # ---- solution: F major, warm and wide ------------------------------------------------------------------
    t0, b = seg(SOL, REPRISE, 4)                                # F, then Bb/F: the clock gets to work
    s.chord(SOL, t0 + 2 * b, [(29, .42), (41, .5), (48, .45), (53, .42), (57, .38), (60, .3)], **SOLN)
    s.chord(t0 + 2 * b, REPRISE, [(29, .4), (41, .48), (46, .42), (53, .4), (58, .36), (62, .28)], **SOLN)
    s.line(t0, b, [(3, 69, .2), (3, 72, .2), (6, 74, .42), (8, 72, .36), (9, 70, .38), (11, 72, .36)], True, E)
    s.line(t0, b, [(0, 53, .26, .6), (6, 58, .26, .6), (9, 53, .2, .5)], True, E)

    t0, b = seg(REPRISE, GOLD, 7)                               # the opening melody, in major (rhyme)
    s.line(t0, b, [(0, 77, .6), (2, 79, .5), (3, 81, .64), (5, 84, .6), (6, 82, .62), (8, 81, .52),
                   (9, 79, .62, 1.2), (12, 77, .62, 1.3), (15, 81, .5), (17, 82, .45), (18, 84, .56)], True, E)
    s.line(t0, b, [(0, 53, .26, .6), (3, 60, .2, .5), (6, 58, .26, .6), (9, 53, .2, .5), (12, 53, .24, .6),
                   (15, 60, .26, .6), (18, 55, .2, .5)], True, E)
    s.chord(REPRISE, t0 + 2 * b, [(29, .42), (41, .5), (48, .45), (53, .42), (57, .38), (60, .3)], **SOLN)
    s.chord(t0 + 2 * b, t0 + 4 * b, [(34, .42), (46, .5), (53, .44), (58, .4), (62, .32)], **SOLN)
    s.chord(t0 + 4 * b, t0 + 5 * b, [(29, .4), (41, .48), (48, .44), (53, .4), (57, .36)], **SOLN)
    s.chord(t0 + 5 * b, GOLD, [(36, .42), (48, .48), (52, .4), (55, .38), (58, .3)], **SOLN)

    t0, b = seg(GOLD, HOUSE, 5)                                 # swell: the gold letters (Bb bloom, then C7)
    s.roll(GOLD, [(58, .3), (70, .42), (74, .4), (77, .5)], True)
    s.line(t0, b, [(3, 86, .52, 1.2), (6, 84, .56), (8, 82, .45), (9, 79, .5, 1.2), (12, 76, .5, 1.3)], True, E)
    s.line(t0, b, [(3, 53, .2, .5), (6, 60, .26, .6), (9, 55, .2, .5), (12, 60, .22, .6)], True, E)
    s.chord(GOLD, t0 + 2 * b, [(34, .45), (46, .5), (53, .45), (58, .42), (62, .34), (65, .24)], **BLOOM)
    s.chord(t0 + 2 * b, HOUSE, [(36, .42), (48, .5), (52, .42), (55, .4), (58, .32), (64, .22)], **BLOOM)

    t0, b = seg(HOUSE, END, 3)                                  # swell: the house relights (F bloom), C7
    s.roll(HOUSE, [(53, .3), (65, .38), (69, .4), (72, .45), (77, .52)], True)
    s.line(t0, b, [(3, 81, .5), (5, 79, .42), (6, 79, .5), (8, 76, .45)], True, E)
    s.line(t0, b, [(3, 60, .2, .5), (6, 55, .24, .6)], True, E)
    s.chord(HOUSE, t0 + 2 * b, [(29, .45), (41, .52), (48, .46), (53, .42), (57, .38), (60, .3), (65, .22)], **BLOOM)
    s.chord(t0 + 2 * b, END, [(36, .42), (48, .5), (52, .42), (55, .4), (58, .3)], **SOLN)

    # ---- end: one F major chord, the box rings out -----------------------------------------------------------
    s.chord(END, 56.4, [(29, .48), (41, .52), (48, .46), (53, .42), (57, .38), (60, .3)], **dict(SOLN, release=1.4))
    s.roll(END, [(53, .3), (65, .36), (69, .4), (72, .44), (77, .5), (81, .46), (84, .42)], True, gap=0.06, decay=1.8)


# --------------------------------------------------------------------------------------------------------- mix
def render(opt):
    s = Score(SEEDS[opt])
    (score_m1 if opt == "M1" else score_m2)(s)
    muf = fft_filter(s.muf, lowpass(1400.0, 4)) * 0.6           # through the wall: 24 dB/oct from 1.4 kHz
    clr = fft_filter(s.clr, presence_dip()) * 1.0               # clear and bright, a gentle dip under the voice
    strings = s.str * s.rock * db_curve([
        (0, -1.0), (16.42, -1.0), (20.2, 0.8), (20.5, -1.0), (22.4, -1.0), (23.1, -3.5), (25.2, -3.5),
        (25.5, -1.0), (STOP, 1.5), (STOP + 0.01, 0.0),                       # pain, rising to the stop
        (34.4, 0.0), (SOL, 0.5), (44.3, 0.5), (45.4, 3.0), (47.0, 1.5),       # swell at 44.97
        (49.2, 1.0), (50.3, 4.0), (51.8, 2.5), (TOTAL, 2.5)]) * 0.55           # swell at 49.83
    wet = reverb(muf * 0.55 + clr * 0.32 + strings * 0.2, s.rng)
    mix = muf + clr + strings + wet * 0.45
    x = np.arange(N) / SR                                       # master: the stop, the silence, the end
    g = np.ones(N)
    g[x < 0.01] = x[x < 0.01] / 0.01
    w = (x >= STOP - 0.05) & (x < STOP)
    g[w] = 0.5 + 0.5 * np.cos(np.pi * (x[w] - (STOP - 0.05)) / 0.05)
    g[(x >= STOP) & (x < DRONE)] = 0.0
    w = x >= 54.9
    g[w] = np.cos(0.5 * np.pi * np.clip((x[w] - 54.9) / (TOTAL - 1 / SR - 54.9), 0, 1)) ** 2
    mix *= g
    mix *= 10 ** (PEAK_DBFS / 20) / np.abs(mix).max()
    out = os.path.join(AUDIO, f"musique-{opt}.wav")
    pcm = np.round(mix.T * 32767).astype("<i2")
    with wave.open(out, "wb") as f:
        f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR); f.writeframes(pcm.tobytes())
    print(f"musique-conte: {out} ({N / SR:.2f} s)")
    return out


# ------------------------------------------------------------------------------------------------------- check
def read_wav(path):
    with wave.open(path, "rb") as f:
        a = np.frombuffer(f.readframes(f.getnframes()), "<i2").astype(float) / 32768
        return a.reshape(-1, f.getnchannels()).T, f.getframerate()


def band(x, lo, hi):
    nfft = 1 << int(np.ceil(np.log2(x.shape[1])))
    f = np.fft.rfftfreq(nfft, 1 / SR)
    return np.fft.irfft(np.fft.rfft(x, nfft, axis=1) * ((f >= lo) & (f < hi)), nfft, axis=1)[:, :x.shape[1]]


def db(v):
    return 20 * np.log10(max(v, 1e-12))


def check(opts):
    speech = []
    try:
        speech = [(p["start"], p["end"]) for p in json.load(open(os.path.join(HERE, "onsets.json")))["phrases"]]
    except (OSError, KeyError, ValueError):
        pass
    rows, sp = {}, {}
    for opt in opts:
        x, sr = read_wav(os.path.join(AUDIO, f"musique-{opt}.wav"))
        n = x.shape[1]
        hb = band(x, 1000, 4000)
        rms = lambda y, a, b: np.sqrt(np.mean(y[:, int(a * sr):int(b * sr)] ** 2)) if b > a else 0.0
        up = np.fft.irfft(np.fft.rfft(x, axis=1), 4 * n, axis=1) * 4
        sil = np.abs(x[:, int(STOP * sr):int(DRONE * sr)]).max()
        print(f"{opt}: {n / sr:.3f} s, {n} frames, {x.shape[0]} ch, {sr} Hz, peak {db(np.abs(x).max()):.2f} dBFS, "
              f"true peak (4x) {db(np.abs(up).max()):.2f} dBTP, max |x| in {STOP}-{DRONE} s = {sil:.1e}")
        acts = (("pain", 0.0, STOP), ("pivot", STOP, SOL), ("solution", SOL, END), ("end", END, TOTAL))
        print("   acts RMS: " + ", ".join(f"{k} {db(rms(x, a, b)):.1f}" for k, a, b in acts) + " dBFS")
        rows[opt] = [(db(rms(x, k, k + 1)), db(rms(hb, k, k + 1))) for k in range(int(np.ceil(TOTAL)))]
        if speech:
            m = np.zeros(n, bool)
            for a, b in speech:
                m[int(a * sr):int(b * sr)] = True
            sol = np.zeros(n, bool); sol[int(SOL * sr):int(END * sr)] = True
            share = lambda mask: db(np.sqrt(np.mean(hb[:, mask] ** 2)) / np.sqrt(np.mean(x[:, mask] ** 2)))
            sp[opt] = (share(m & sol), share(~m & sol), share(m & ~sol & (np.arange(n) < STOP * sr)))
    print("RMS per second, dBFS (full band / 1-4 kHz):")
    print("   s   " + "".join(f"{o + ' full':>9}{o + ' 1-4k':>9}" for o in opts))
    for k in range(int(np.ceil(TOTAL))):
        print(f"  {k:2d}   " + "".join(f"{rows[o][k][0]:9.1f}{rows[o][k][1]:9.1f}" for o in opts))
    for o, (a, b, c) in sp.items():
        print(f"{o}: 1-4 kHz share of the music, solution in speech {a:.1f} dB, solution between phrases {b:.1f} dB,"
              f" pain in speech {c:.1f} dB")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    opts = [a.upper() for a in args] or ["M1", "M2"]
    for o in opts:
        if o not in SEEDS:
            sys.exit(__doc__)
    if "--check" not in sys.argv:
        os.makedirs(AUDIO, exist_ok=True)
        for o in opts:
            render(o)
    check(opts)


if __name__ == "__main__":
    main()
