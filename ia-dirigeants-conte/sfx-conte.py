#!/usr/bin/env python3
"""Sound effects of « Le Temps perdu » (ia-dirigeants-conte), synthesized by script.

numpy only (plus the standard library: wave, zlib): no network, no generative service, no outside sample, so every
sound is free of rights. Each sound has its own fixed seed (derived from its name): two runs give the same files.

Output: assets/audio/sfx/<name>.wav, 44.1 kHz, 16-bit stereo (dry sound in the centre or panned, a small decorrelated
room on both sides), peak normalised to -6 dBFS. The placement on the timeline is assets/audio/sfx-events.json,
mixed by build-audio.sh (which looks in the HeyGen library first, then in assets/audio/sfx).

Families (storyboard, header line **SON**): papier, bois (rods, steps, chair, heel, door), tic and tac (the clock),
roulettes, aiguilles, maillons, punaise, crayon, plume, flamme, vent, ailes, balle, corde, souffle, notes de bois.
The 4 whooshes, the riser and the sparkle come from the shared library (media-use), not from here.

Usage: python3 sfx-conte.py                 # every sound
       python3 sfx-conte.py papier tic      # only the names starting with these prefixes
       python3 sfx-conte.py --list          # names only
"""
import os
import sys
import wave
import zlib

import numpy as np

SR = 44100
PEAK = 10 ** (-6.0 / 20)                       # -6 dBFS
BASE_SEED = 2026
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "assets", "audio", "sfx")


# ---------------------------------------------------------------------------------------------------------------------
# DSP helpers (numpy only)
# ---------------------------------------------------------------------------------------------------------------------
def ns(d):
    """Number of samples of a duration (at least 1)."""
    return max(1, int(round(d * SR)))


def at(t):
    """Sample index of a time."""
    return int(round(t * SR))


def tt(n):
    return np.arange(n) / SR


def nfft(n):
    return 1 << int(np.ceil(np.log2(max(2, n))))


def smoothstep(u):
    u = np.clip(u, 0.0, 1.0)
    return u * u * (3.0 - 2.0 * u)


def shape(f, lo=None, hi=None, order=2, tilt=0.0, peaks=()):
    """Magnitude response: Butterworth-like high-pass (lo) and low-pass (hi), a tilt in dB/octave around 1 kHz and
    resonant peaks (fc, q, gain_db)."""
    fp = np.maximum(f, 1.0)
    g = np.ones_like(fp)
    if hi is not None:
        g = g / np.sqrt(1.0 + (fp / hi) ** (2 * order))
    if lo is not None:
        g = g / np.sqrt(1.0 + (lo / fp) ** (2 * order))
    if tilt:
        g = g * (fp / 1000.0) ** (tilt / 6.0206)
    for fc, q, gain_db in peaks:
        bp = 1.0 / np.sqrt(1.0 + q * q * (fp / fc - fc / fp) ** 2)
        g = g * (1.0 + (10 ** (gain_db / 20.0) - 1.0) * bp)
    g[0] = 0.0
    return g


def noise(rng, n, **kw):
    """Coloured noise of n samples, unit RMS. Built in the frequency domain, so it is circular (loops seamlessly)."""
    m = max(n, 4096)                            # enough frequency resolution even for very short kernels
    f = np.fft.rfftfreq(m, 1.0 / SR)
    spec = (rng.standard_normal(len(f)) + 1j * rng.standard_normal(len(f))) * shape(f, **kw)
    x = np.fft.irfft(spec, m)[:n]
    return x / (np.sqrt(np.mean(x ** 2)) + 1e-12)


def filt(x, **kw):
    """Zero-phase spectral filter (padded, so it does not wrap)."""
    n = len(x)
    m = nfft(n + 4096)
    f = np.fft.rfftfreq(m, 1.0 / SR)
    return np.fft.irfft(np.fft.rfft(x, m) * shape(f, **kw), m)[:n]


def conv(x, h):
    """Causal convolution (FFT), full length."""
    m = len(x) + len(h) - 1
    k = nfft(m)
    return np.fft.irfft(np.fft.rfft(x, k) * np.fft.rfft(h, k), k)[:m]


def lfo(rng, n, rate):
    """Smooth random modulation around 0, unit RMS, bandwidth about `rate` Hz."""
    return noise(rng, n, hi=rate, order=2)


def env_hit(n, attack, decay, start=0.0):
    """Percussive envelope: smooth attack then exponential decay."""
    t = tt(n) - start
    a = smoothstep(t / attack) if attack > 0 else (t >= 0).astype(float)
    d = np.exp(-np.clip(t - attack, 0.0, None) / decay)
    return np.where(t < 0, 0.0, a * d)


def env_bell(n, attack, release, hold=0.0, start=0.0):
    """Trapezoid with smooth edges: attack, hold, release."""
    t = tt(n) - start
    up = smoothstep(t / max(attack, 1e-4))
    down = 1.0 - smoothstep((t - attack - hold) / max(release, 1e-4))
    return np.where(t < 0, 0.0, up * down)


def fade(x, fin=0.0, fout=0.0):
    y = x.copy()
    if fin > 0:
        k = min(len(y), ns(fin))
        y[:k] *= 0.5 - 0.5 * np.cos(np.linspace(0, np.pi, k))
    if fout > 0:
        k = min(len(y), ns(fout))
        y[len(y) - k:] *= 0.5 + 0.5 * np.cos(np.linspace(0, np.pi, k))
    return y


def modes(n, spec):
    """Sum of damped sines (freq, tau, amp), all starting at zero phase: a modal impulse response."""
    t = tt(n)
    y = np.zeros(n)
    for f, tau, a in spec:
        if f < SR / 2:
            y += a * np.exp(-t / tau) * np.sin(2 * np.pi * f * t)
    return y


def soften(x, ms):
    """Contact pulse (raised cosine of `ms` milliseconds): a longer pulse is a softer mallet."""
    w = max(3, int(ms * 1e-3 * SR))
    p = np.hanning(w)
    return np.convolve(x, p / p.sum())[:len(x)]


def place(dst, src, t, gain=1.0):
    i = at(t)
    if i >= len(dst):
        return dst
    m = min(len(src), len(dst) - i)
    dst[i:i + m] += gain * src[:m]
    return dst


def sweep_sine(n, f_start, f_end, tau_f, decay, attack=0.0003):
    """Sine whose pitch falls exponentially from f_start to f_end (a pop, a thump)."""
    t = tt(n)
    f = f_end + (f_start - f_end) * np.exp(-t / tau_f)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env_hit(n, attack, decay)


def crackle(rng, n, rate, lo=1500.0, hi=9000.0, decay=(0.0003, 0.0025), sigma=0.9, kernels=5, tilt=0.0):
    """Poisson stream of tiny crackles (paper fibres, flame). `rate` in events per second, scalar or per sample."""
    rate = np.broadcast_to(np.asarray(rate, dtype=float), (n,))
    hits = rng.random(n) < rate / SR
    amps = rng.lognormal(0.0, sigma, n) * hits
    which = rng.integers(0, kernels, n)
    out = np.zeros(n)
    for k in range(kernels):
        tau = rng.uniform(*decay)
        m = ns(tau * 7)
        ker = noise(rng, m, lo=lo * rng.uniform(0.8, 1.25), hi=hi * rng.uniform(0.8, 1.2), tilt=tilt)
        ker *= env_hit(m, 0.00012, tau)
        ker /= np.max(np.abs(ker)) + 1e-12
        imp = np.where(which == k, amps, 0.0)
        if imp.any():
            out += conv(imp, ker)[:n]
    return out


def pulse_train(rng, n, rate, jitter=0.15, sigma=0.25, env=None):
    """Impulses at an instantaneous rate (Hz, per-sample array), jittered in time and amplitude (stick-slip)."""
    phase = np.cumsum(rate) / SR
    idx = np.nonzero(np.diff(np.floor(phase)) > 0)[0] + 1
    out = np.zeros(n)
    if len(idx) == 0:
        return out
    shift = (rng.uniform(-jitter, jitter, len(idx)) * SR / np.maximum(rate[idx], 1.0)).astype(int)
    pos = np.clip(idx + shift, 0, n - 1)
    amp = rng.lognormal(0.0, sigma, len(idx))
    if env is not None:
        amp = amp * env[pos]
    np.add.at(out, pos, amp)
    return out


def resonators(res, dur=0.09):
    """Impulse response of a bank of resonators (fc, q, gain): a wooden or rope body."""
    n = ns(dur)
    return modes(n, [(fc, q / (np.pi * fc), g) for fc, q, g in res])


def knock(rng, f0, q=20.0, ratios=(1.0, 2.32, 3.85, 5.4), amps=(1.0, 0.6, 0.35, 0.2), hard=0.4, dur=0.3,
          thump=None, click=0.3, detune=0.03):
    """Wooden impact: modes at constant Q (higher modes die faster, as in wood), a contact pulse, an optional low
    thump (floor, table) with a slight pitch drop, and a short contact noise."""
    n = ns(dur)
    spec = []
    for r, a in zip(ratios, amps):
        f = f0 * r * (1 + detune * rng.uniform(-1, 1))
        spec.append((f, q / (np.pi * f) * rng.uniform(0.85, 1.15), a * rng.uniform(0.8, 1.2)))
    y = modes(n, spec)
    if thump:
        f1, tau1, a1 = thump
        y += a1 * sweep_sine(n, f1 * 1.35, f1, 0.008, tau1, attack=0.0004)
    y = soften(y, hard)
    if click:
        y += click * noise(rng, n, lo=2500, hi=10000) * env_hit(n, 0.0001, 0.0012)
    return y


def room(rng, x, wet=0.25, t60=0.5, damp=3500.0, pre=0.009, pan=0.0):
    """Mono (panned, equal power) or stereo dry signal -> stereo with a small decorrelated room (a stage, close)."""
    if x.ndim == 1:
        th = (pan + 1.0) * np.pi / 4
        dry = np.stack([x * np.cos(th), x * np.sin(th)], axis=1) * np.sqrt(2.0)
    else:
        dry = x
    mono = dry.mean(axis=1)
    m = ns(t60 * 1.2)
    t = tt(m)
    out = np.zeros((len(mono) + m, 2))
    out[:len(dry)] += dry
    if wet <= 0:
        return out
    for ch in range(2):
        e = noise(rng, m)
        low = filt(e, hi=damp, order=1)
        ir = low * np.exp(-6.91 * t / t60) + 0.5 * (e - low) * np.exp(-6.91 * t / (0.4 * t60))
        ir *= smoothstep((t - pre) / 0.012)
        ir /= np.sqrt(np.sum(ir ** 2)) + 1e-12
        w = conv(mono, ir)[:len(out)]
        out[:len(w), ch] += wet * w
    return out


def stereo_add(dst, mono_src, t, pan=0.0, gain=1.0):
    th = (pan + 1.0) * np.pi / 4
    place(dst[:, 0], mono_src * np.cos(th) * np.sqrt(2.0), t, gain)
    place(dst[:, 1], mono_src * np.sin(th) * np.sqrt(2.0), t, gain)
    return dst


def finish(st, trim=True):
    """Trim the silent tail, short edge fades, peak to -6 dBFS."""
    st = np.asarray(st, dtype=float)
    if st.ndim == 1:
        st = np.stack([st, st], axis=1)
    st = np.stack([filt(st[:, c], lo=30, order=2) for c in range(2)], axis=1)      # no DC, no rumble
    if trim:
        a = np.max(np.abs(st), axis=1)
        live = np.nonzero(a > a.max() * 10 ** (-66 / 20))[0]
        st = st[:min(len(st), live[-1] + ns(0.01))]
    k = min(len(st), 32)
    st[:k] *= np.linspace(0.0, 1.0, k)[:, None]
    k = min(len(st), ns(0.008))
    st[len(st) - k:] *= np.linspace(1.0, 0.0, k)[:, None]
    return st * (PEAK / (np.max(np.abs(st)) + 1e-12))


def write_wav(path, st):
    pcm = np.round(np.clip(st, -1.0, 1.0) * 32767).astype("<i2")
    with wave.open(path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())


# ---------------------------------------------------------------------------------------------------------------------
# PAPIER
# ---------------------------------------------------------------------------------------------------------------------
def papier_froisse(rng, dur=0.4, peak_rate=2200.0, tremble=0.0):
    """Rustle: a dense stream of fibre crackles, a few bigger crinkles, a little friction underneath."""
    n = ns(dur + 0.06)
    t = tt(n)
    env = env_bell(n, dur * 0.22, dur * 0.45, dur * 0.33)
    if tremble:
        env *= 1.0 - tremble + tremble * np.sin(2 * np.pi * rng.uniform(13, 17) * t) ** 2
    gust = np.exp(0.45 * lfo(rng, n, 16))
    act = env * gust / np.max(env * gust)
    y = crackle(rng, n, peak_rate * act, lo=700, hi=5500, decay=(0.0003, 0.003), sigma=1.0, tilt=-1.5)
    y += 1.8 * crackle(rng, n, 22 * act, lo=600, hi=3500, decay=(0.002, 0.006), sigma=0.5, kernels=3)
    y += 0.5 * noise(rng, n, lo=400, hi=4500) * act
    return room(rng, y, wet=0.22, t60=0.45)


def papier_glisse(rng, dur=0.42):
    """A sheet sliding: friction noise that brightens, sparse fibres, a small tap at the end."""
    n = ns(dur + 0.08)
    t = tt(n)
    u = np.clip(t / dur, 0, 1)
    env = env_bell(n, 0.05, 0.16, max(0.0, dur - 0.21))
    low = noise(rng, n, lo=350, hi=2500)
    high = noise(rng, n, lo=1200, hi=6000, tilt=-1.5)
    y = (0.8 * low * (1 - u) + high * (0.4 + 0.6 * u)) * env * (1 + 0.25 * lfo(rng, n, 25))
    y += 0.5 * crackle(rng, n, 90 * env, lo=1000, hi=6000)
    tap = noise(rng, n, lo=500, hi=4000) * env_hit(n, 0.0005, 0.02, start=dur - 0.03)
    y += 0.9 * tap * np.max(np.abs(y)) / (np.max(np.abs(tap)) + 1e-12) * 0.6
    return room(rng, y, wet=0.2, t60=0.45)


def papier_pose(rng, weight=1.0, size=1.0):
    """A sheet landing flat: the air it pushes, then the tap on the surface and a few fibres."""
    n = ns(0.32)
    air = noise(rng, n, lo=120 / size, hi=1100 / size) * env_hit(n, 0.010 * size, 0.045 * size)
    tap = noise(rng, n, lo=600, hi=5000) * env_hit(n, 0.0004, 0.006, start=0.010 * size)
    crk = crackle(rng, n, 500 * env_hit(n, 0.012, 0.03), lo=1000, hi=6000)
    thump = modes(n, [(rng.uniform(150, 190), 0.02, 1.0)])
    thump = np.roll(thump, ns(0.010 * size)) * (tt(n) >= 0.010 * size)
    y = air + 0.6 * tap + 0.5 * crk + 0.45 * weight * thump
    return room(rng, y, wet=0.22, t60=0.45)


def papier_pile(rng, weight=1.0, scatter=0):
    """A pile of quotes put down or dropped: thump with a pitch drop, table body, slap, air, rustle tail."""
    n = ns(0.8)
    t = tt(n)
    f = 95 * rng.uniform(0.9, 1.1) * (1 + 0.6 * np.exp(-t / 0.012))
    thump = np.sin(2 * np.pi * np.cumsum(f) / SR) * env_hit(n, 0.001, 0.075)
    body = modes(n, [(rng.uniform(190, 230), 0.05, 0.7), (rng.uniform(410, 450), 0.03, 0.6),
                     (rng.uniform(740, 800), 0.018, 0.35), (rng.uniform(1050, 1150), 0.012, 0.2)])
    slap = noise(rng, n, lo=300, hi=3000) * env_hit(n, 0.0008, 0.03)
    air = noise(rng, n, lo=60, hi=500) * env_hit(n, 0.004, 0.08)
    rust = crackle(rng, n, 2400 * env_hit(n, 0.01, 0.12), lo=900, hi=5500, tilt=-1.5)
    y = weight * soften(thump + body, 1.5) * 1.1 + 0.55 * slap + 0.35 * air + 0.35 * rust
    for k in range(scatter):                    # sheets that slide off the pile
        s0 = rng.uniform(0.07, 0.28)
        m = ns(0.18)
        sl = noise(rng, m, lo=800, hi=5000) * env_bell(m, 0.02, 0.1, 0.04)
        place(y, sl * 0.12 * rng.uniform(0.6, 1.0), s0)
    return room(rng, y, wet=0.25, t60=0.5)


def papier_dechire(rng, dur=0.22):
    """A tear: a jittered train of fibre fractures (a rip), fibre noise, a flap when the piece comes off."""
    n = ns(dur + 0.1)
    t = tt(n)
    env = env_bell(n, 0.012, 0.025, max(0.0, dur - 0.037)) * (0.7 + 0.3 * np.clip(t / dur, 0, 1))
    rate = rng.uniform(350, 650) * (1 + 0.35 * lfo(rng, n, 25))
    imp = pulse_train(rng, n, np.maximum(rate, 80), jitter=0.3, sigma=0.5, env=env)
    y = np.zeros(n)
    for k in range(4):
        tau = rng.uniform(0.0004, 0.0012)
        m = ns(tau * 7)
        ker = noise(rng, m, lo=800 * rng.uniform(0.8, 1.2), hi=6000, tilt=-1.0) * env_hit(m, 0.0001, tau)
        sel = np.zeros(n)
        sel[k::4] = 1.0
        y += conv(imp * sel, ker / (np.max(np.abs(ker)) + 1e-12))[:n]
    y += 0.12 * noise(rng, n, lo=2000, hi=7000) * env * np.max(np.abs(y))
    flap = noise(rng, n, lo=300, hi=2500) * env_hit(n, 0.004, 0.03, start=dur)
    y += 0.35 * flap * np.max(np.abs(y)) / (np.max(np.abs(flap)) + 1e-12)
    return room(rng, y, wet=0.22, t60=0.45)


def papier_eventail(rng, sheets=7, span=0.32, air=0.3):
    """A fan of sheets: quick flaps that accelerate then settle, on a breath of air."""
    n = ns(span + 0.2)
    u = np.linspace(0, 1, sheets)
    times = span * (0.5 - 0.5 * np.cos(np.pi * u)) + rng.uniform(-0.006, 0.006, sheets)
    times = np.clip(times, 0, None)
    y = np.zeros(n)
    for k, t0 in enumerate(np.sort(times)):
        m = ns(0.08)
        fl = noise(rng, m, lo=500 * rng.uniform(0.8, 1.2), hi=4800) * env_hit(m, 0.003, rng.uniform(0.022, 0.034))
        fl += 0.4 * crackle(rng, m, 1800 * env_hit(m, 0.002, 0.01), lo=1500, hi=6000)
        place(y, fl * rng.uniform(0.6, 1.0), t0)
    y += air * noise(rng, n, lo=200, hi=1600) * env_bell(n, span * 0.4, span * 0.6, 0.0) * np.max(np.abs(y)) * 0.5
    return room(rng, y, wet=0.24, t60=0.5)


def papier_deplie(rng, letters=11, gap=0.03):
    """Paper letters unfolding one after another (0.03 s apart, as in the storyboard): small flicks on a soft rustle."""
    span = letters * gap
    n = ns(span + 0.2)
    y = np.zeros(n)
    for k in range(letters):
        m = ns(0.06)
        fl = noise(rng, m, lo=1000, hi=5500, tilt=-1.0) * env_hit(m, 0.0003, rng.uniform(0.007, 0.012))
        fl += 0.45 * knock(rng, rng.uniform(900, 1300), q=6, ratios=(1.0,), amps=(1.0,), hard=0.4, dur=0.06, click=0)
        a = (1.0 if k == 0 else 0.75 - 0.2 * k / letters) * rng.uniform(0.75, 1.0)
        place(y, fl * a, k * gap + rng.uniform(-0.002, 0.002) + 0.002)
    bed = noise(rng, n, lo=600, hi=4500) * env_bell(n, 0.03, 0.12, span * 0.6)
    y += 0.08 * bed
    return room(rng, y, wet=0.24, t60=0.5)


# ---------------------------------------------------------------------------------------------------------------------
# BOIS
# ---------------------------------------------------------------------------------------------------------------------
def bois_pas(rng, light=False):
    """A puppet step: the foot taps the stage, the rod clacks a few ms later ("pas, clac de bois des tiges")."""
    n = ns(0.35)
    if light:
        foot = knock(rng, rng.uniform(700, 820), q=9, ratios=(1.0, 2.4), amps=(1.0, 0.3), hard=1.0, dur=0.35,
                     thump=(rng.uniform(160, 190), 0.02, 0.2), click=0.1)
        rod = knock(rng, rng.uniform(1500, 1800), q=16, ratios=(1.0, 2.15, 3.6), amps=(1.0, 0.45, 0.2), hard=0.25,
                    dur=0.2, click=0.25)
        y = 0.8 * foot
        place(y, 0.6 * rod, rng.uniform(0.006, 0.012))
    else:
        foot = knock(rng, rng.uniform(480, 560), q=9, ratios=(1.0, 2.4), amps=(1.0, 0.3), hard=1.2, dur=0.35,
                     thump=(rng.uniform(110, 130), 0.03, 0.45), click=0.1)
        rod = knock(rng, rng.uniform(1000, 1200), q=16, ratios=(1.0, 2.15, 3.6), amps=(1.0, 0.5, 0.25), hard=0.25,
                    dur=0.25, click=0.35)
        y = foot
        place(y, 0.9 * rod, rng.uniform(0.010, 0.018))
    return room(rng, y, wet=0.28, t60=0.5)


def creak(rng, n, rate, res, jitter=0.12, grit=0.25, env=None):
    """Stick-slip creak: a jittered pulse train exciting a resonant body."""
    pt = pulse_train(rng, n, rate, jitter=jitter, sigma=0.3, env=env)
    y = conv(pt, resonators(res))[:n]
    if grit:
        g = conv(pt, noise(rng, ns(0.004), lo=1500, hi=7000) * env_hit(ns(0.004), 0.0001, 0.0008))[:n]
        y += grit * g * np.max(np.abs(y)) / (np.max(np.abs(g)) + 1e-12)
    return y


def bois_chaise(rng, kind=1):
    """The chair: legs landing (two knocks), a short creak of the joints, or a scrape when the father gets up."""
    n = ns(0.5)
    t = tt(n)
    y = np.zeros(n)
    leg = lambda: knock(rng, rng.uniform(380, 460), q=12, ratios=(1.0, 2.6, 4.3), amps=(1.0, 0.45, 0.2), hard=0.5,
                        dur=0.3, thump=(rng.uniform(90, 105), 0.04, 0.4), click=0.15)
    res = [(rng.uniform(480, 560), 8, 1.0), (rng.uniform(1100, 1300), 10, 0.6), (rng.uniform(2300, 2600), 12, 0.25)]
    if kind == 1:                               # sits down: two legs, a short creak
        place(y, leg(), 0.0)
        place(y, 0.7 * leg(), rng.uniform(0.018, 0.03))
        m = ns(0.14)
        rate = np.linspace(70, 48, m)
        place(y, 0.25 * creak(rng, m, rate, res, env=env_bell(m, 0.02, 0.06, 0.05)), 0.04)
    elif kind == 2:                             # settles: one knock, a longer creak
        place(y, 0.8 * leg(), 0.0)
        m = ns(0.22)
        rate = 45 + 30 * np.sin(np.pi * np.linspace(0, 1, m))
        place(y, 0.3 * creak(rng, m, rate, res, env=env_bell(m, 0.04, 0.08, 0.08)), 0.03)
    else:                                       # pushed back: a scrape on the floor, then a knock
        m = ns(0.2)
        rate = np.linspace(38, 60, m) * (1 + 0.1 * lfo(rng, m, 20))
        sc = creak(rng, m, rate, [(260, 5, 1.0), (620, 7, 0.7), (1400, 9, 0.35)], jitter=0.2, grit=0.5,
                   env=env_bell(m, 0.03, 0.06, 0.1))
        sc += 0.2 * noise(rng, m, lo=300, hi=2500) * env_bell(m, 0.03, 0.06, 0.1) * np.max(np.abs(sc))
        place(y, 0.45 * sc / (np.max(np.abs(sc)) + 1e-12), 0.0)
        place(y, 0.8 * leg() / 1.0, 0.19)
    return room(rng, y, wet=0.28, t60=0.5)


def bois_talon(rng):
    """A heel on the stage: sharp knock and a firm thump."""
    y = knock(rng, rng.uniform(600, 700), q=14, ratios=(1.0, 2.3, 3.9), amps=(1.0, 0.5, 0.2), hard=0.25, dur=0.3,
              thump=(rng.uniform(130, 150), 0.035, 0.55), click=0.4)
    return room(rng, y, wet=0.28, t60=0.5)


def bois_clic(rng, double=False):
    """Light wooden click (a thread, a pivot, a small button)."""
    y = knock(rng, rng.uniform(2100, 2600), q=28, ratios=(1.0, 2.7), amps=(1.0, 0.3), hard=0.15, dur=0.12, click=0.2)
    if double:
        place(y, 0.4 * knock(rng, rng.uniform(2300, 2800), q=28, ratios=(1.0, 2.7), amps=(1.0, 0.3), hard=0.15,
                             dur=0.1, click=0.15), 0.007)
    return room(rng, y, wet=0.26, t60=0.5)


def bois_leger(rng, knocks=2):
    """Soft wood of the puppet joints (kneeling, hands, lifting): soft knocks and a cloth-like swish."""
    n = ns(0.35)
    y = np.zeros(n)
    t0 = 0.0
    for k in range(knocks):
        kk = knock(rng, rng.uniform(650, 900), q=10, ratios=(1.0, 2.5, 4.0), amps=(1.0, 0.35, 0.12), hard=0.6,
                   dur=0.2, thump=(rng.uniform(170, 210), 0.02, 0.12), click=0.05)
        place(y, kk * (1.0 if k == 0 else 0.6), t0)
        t0 += rng.uniform(0.03, 0.055)
    sw = noise(rng, n, lo=300, hi=2500) * env_bell(n, 0.02, 0.05, 0.02)
    y += 0.08 * sw * np.max(np.abs(y))
    return room(rng, y, wet=0.26, t60=0.5)


def bois_tampon(rng):
    """A dry wooden stamp on paper: knock, paper slap, thump."""
    n = ns(0.25)
    y = knock(rng, rng.uniform(480, 600), q=10, ratios=(1.0, 2.5, 4.1), amps=(1.0, 0.4, 0.15), hard=0.6, dur=0.25,
              thump=(rng.uniform(95, 110), 0.03, 0.3), click=0.2)
    y += 0.6 * noise(rng, n, lo=700, hi=4500) * env_hit(n, 0.0003, 0.010)
    return room(rng, y, wet=0.26, t60=0.5)


def bois_clac(rng):
    """The hands of the clock clack into place, in the dark: two hard pieces of wood, a long empty room."""
    y = knock(rng, rng.uniform(900, 1000), q=22, ratios=(1.0, 1.73, 2.9, 4.4), amps=(1.0, 0.7, 0.4, 0.2), hard=0.15,
              dur=0.35, click=0.5)
    y += 0.4 * modes(len(y), [(rng.uniform(250, 270), 8 / (np.pi * 260), 1.0)])
    return room(rng, y, wet=0.45, t60=0.85)


def bois_porte_ouvre(rng):
    """The door leaf opens: the latch, a short creak of the hinge and wood, the air of the evening coming in."""
    dur = 0.75
    n = ns(dur + 0.1)
    t = tt(n)
    y = np.zeros(n)
    latch = knock(rng, rng.uniform(2500, 2700), q=40, ratios=(1.0, 1.45, 2.3), amps=(1.0, 0.6, 0.3), hard=0.1,
                  dur=0.15, click=0.4)
    place(y, 0.5 * latch, 0.0)
    u = np.clip((t - 0.08) / 0.62, 0, 1)
    rate = 40 + 70 * np.sin(np.pi * u) ** 1.5 * (1 + 0.08 * lfo(rng, n, 12))
    env = env_bell(n, 0.08, 0.15, 0.39, start=0.08)
    cr = creak(rng, n, rate, [(330, 6, 0.7), (720, 8, 1.0), (1500, 10, 0.6), (2800, 12, 0.3)], env=env)
    y += 0.6 * cr / (np.max(np.abs(cr)) + 1e-12)
    y += 0.12 * noise(rng, n, lo=70, hi=380) * env_bell(n, 0.15, 0.3, 0.2, start=0.05)
    return room(rng, y, wet=0.28, t60=0.55)


def bois_porte_ferme(rng):
    """The door leaf closes, dull: a big low thump of the panel, the latch, a puff of air."""
    n = ns(0.7)
    y = modes(n, [(78, 0.09, 0.7), (145, 0.07, 0.6), (230, 0.05, 0.5), (410, 0.03, 0.5), (560, 0.025, 0.45),
                  (760, 0.018, 0.35), (1020, 0.012, 0.2)])
    y = soften(y, 0.8)
    latch = knock(rng, rng.uniform(2200, 2400), q=30, ratios=(1.0, 1.6), amps=(1.0, 0.4), hard=0.12, dur=0.1,
                  click=0.3)
    place(y, 0.18 * latch, 0.025)
    y += 0.3 * noise(rng, n, lo=60, hi=300) * env_hit(n, 0.005, 0.06)
    y = filt(y, hi=3500, order=2)
    return room(rng, y, wet=0.32, t60=0.6)


# ---------------------------------------------------------------------------------------------------------------------
# TIC, TAC (the wooden clock)
# ---------------------------------------------------------------------------------------------------------------------
def tick(rng, kind="tic", dry=False, gold=False):
    f0 = (2400 if kind == "tic" else 1700) * rng.uniform(0.97, 1.03)
    y = knock(rng, f0, q=22 if dry else 34, ratios=(1.0, 1.52, 2.21), amps=(1.0, 0.55, 0.3), hard=0.12, dur=0.25,
              click=0.35)
    body = 310 if kind == "tic" else 270
    y += 0.25 * modes(len(y), [(body * rng.uniform(0.95, 1.05), 0.03 if not dry else 0.018, 1.0)])
    if gold:                                    # a faint golden ring
        y += modes(len(y), [(f0 * 1.5, 0.22, 0.10), (f0 * 2.76, 0.12, 0.05)])
    return y


def tic_tac(rng, kind="tic", dry=False, gold=False, far=False, pair=False):
    n = ns(0.85 if pair else 0.3)
    y = np.zeros(n)
    place(y, tick(rng, kind, dry, gold), 0.0)
    if pair:
        place(y, 0.9 * tick(rng, "tac", dry, gold), 0.52)
    if far:
        y = filt(y, hi=2200, order=2)
        return room(rng, y, wet=0.6, t60=0.9, damp=2500)
    return room(rng, y, wet=0.3 if not dry else 0.2, t60=0.55 if not gold else 0.8)


def tictac_accelere(rng):
    """Soir après soir: the clock races (0.9 s)."""
    times = [0.0, 0.20, 0.37, 0.51, 0.62, 0.71, 0.78, 0.84, 0.89]
    y = np.zeros(ns(1.2))
    for k, t0 in enumerate(times):
        place(y, tick(rng, "tic" if k % 2 == 0 else "tac") * (0.8 + 0.2 * k / len(times)), t0)
    return room(rng, y, wet=0.3, t60=0.55)


# ---------------------------------------------------------------------------------------------------------------------
# ROULETTES, AIGUILLES, MAILLONS, PUNAISE
# ---------------------------------------------------------------------------------------------------------------------
def roulettes(rng, dur=0.32, rot=12.0):
    """Small wooden wheels rolling on the stage (the clock follows the father, at 12 poses per second)."""
    n = ns(dur + 0.08)
    t = tt(n)
    env = env_bell(n, 0.03, 0.10, max(0.0, dur - 0.13))
    phi = rng.uniform(0, 2 * np.pi)
    rum = noise(rng, n, lo=90, hi=650, peaks=((260, 3, 6),)) * (0.65 + 0.35 * np.sin(2 * np.pi * rot * t + phi))
    rat = noise(rng, n, lo=600, hi=2600) * (0.5 + 0.5 * np.sin(2 * np.pi * rot * 2 * t + phi)) ** 3
    y = (0.25 * rum + 0.06 * rat) * env
    for w in range(2):                          # two wheels, each bump of the turn is a tiny knock
        r = rot * rng.uniform(0.94, 1.06)
        t0 = rng.uniform(0.0, 1.0 / r)
        while t0 < dur - 0.02:
            kk = knock(rng, rng.uniform(1200, 1600), q=12, ratios=(1.0, 2.4), amps=(1.0, 0.3), hard=0.3, dur=0.06,
                       click=0.15)
            place(y, 0.5 * rng.lognormal(0, 0.3) * kk * env[min(n - 1, at(t0))], t0)
            t0 += 1.0 / r
    return room(rng, y, wet=0.25, t60=0.5)


def click_kernels(rng, f0, count=4, q=26.0):
    return [knock(rng, f0 * rng.uniform(0.92, 1.08), q=q, ratios=(1.0, 1.47, 2.3), amps=(1.0, 0.5, 0.25), hard=0.08,
                  dur=0.05, click=0.5) for _ in range(count)]


def ease_times(count, span, ease):
    """Times at which an eased progress 0 -> 1 over `span` seconds crosses k/count (k = 1..count)."""
    u = np.linspace(0, 1, 4001)
    p = ease(u)
    return [span * float(np.interp(k / count, p, u)) for k in range(1, count + 1)]


def aiguilles(rng, dur=0.5, rate=22.0, f0=3200.0, times=None, whir=0.04):
    """Fast clicking hands: a ratchet (alternate strong and weak teeth) and a faint mechanical whir."""
    if times is None:
        grid = np.arange(0.0, dur - 0.02, 1.0 / rate)
        times = [max(0.0, x) for x in grid + rng.uniform(-0.003, 0.003, len(grid))]
    n = ns(dur + 0.12)
    y = np.zeros(n)
    ks = click_kernels(rng, f0)
    for k, t0 in enumerate(times):
        place(y, ks[k % len(ks)] * (1.0 if k % 2 == 0 else 0.7) * rng.uniform(0.85, 1.0), t0)
    env = env_bell(n, 0.03, 0.06, max(0.0, dur - 0.09))
    y += whir * noise(rng, n, lo=1500, hi=4500) * env * np.max(np.abs(y))
    return room(rng, y, wet=0.25, t60=0.5)


def aiguilles_chiffre(rng):
    """The counter rolls 0 -> 10 in 0.99 s (power2.out): ten light flips, the last one settles."""
    times = ease_times(10, 0.99, lambda u: 1 - (1 - u) ** 2)
    n = ns(1.2)
    y = np.zeros(n)
    for k, t0 in enumerate(times):
        m = ns(0.06)
        fl = 0.6 * knock(rng, rng.uniform(2700, 3000), q=20, ratios=(1.0, 1.6), amps=(1.0, 0.3), hard=0.1, dur=0.06,
                         click=0.3)
        fl += 0.3 * noise(rng, m, lo=2000, hi=7000) * env_hit(m, 0.0002, 0.003)
        if k == len(times) - 1:
            fl = fl * 1.3 + 0.4 * knock(rng, 900, q=10, ratios=(1.0, 2.4), amps=(1.0, 0.3), hard=0.5, dur=0.06,
                                        click=0.0)
        place(y, fl * rng.uniform(0.8, 1.0), t0 - 0.002)
    return room(rng, y, wet=0.28, t60=0.6)


def maillons(rng, links=5, tight=False):
    """Paper chain links tightening: link ticks that accelerate, a stretch rustle, a taut snap."""
    base = rng.uniform(0.045, 0.06)
    times = np.cumsum([0.0] + [base * 0.78 ** k for k in range(links - 1)])
    n = ns(times[-1] + 0.35)
    y = np.zeros(n)
    for t0 in times:
        m = ns(0.05)
        tk = noise(rng, m, lo=1200, hi=5000) * env_hit(m, 0.0001, rng.uniform(0.003, 0.005))
        tk += 0.6 * modes(m, [(rng.uniform(320, 420), 0.012, 1.0)])
        place(y, tk * rng.uniform(0.6, 0.9), t0)
    snap_t = times[-1] + rng.uniform(0.025, 0.04)
    m = ns(0.1)
    sn = noise(rng, m, lo=800, hi=5500) * env_hit(m, 0.0002, 0.005 if tight else 0.008) * 1.5
    sn += 0.5 * modes(m, [(rng.uniform(200, 240), 0.02, 1.0)])
    place(y, sn, snap_t)
    act = env_bell(n, 0.02, 0.05, snap_t - 0.02)
    y += 0.25 * crackle(rng, n, 600 * act, lo=1000, hi=6000)
    return room(rng, y, wet=0.18 if tight else 0.25, t60=0.5)


def punaise(rng):
    """A pin pushed in: a little pop (falling pitch) and a dry wooden tock."""
    n = ns(0.2)
    y = knock(rng, rng.uniform(950, 1250), q=14, ratios=(1.0, 2.05, 3.3), amps=(1.0, 0.45, 0.2), hard=0.3, dur=0.2,
              click=0.3, thump=(240, 0.02, 0.35))
    y += 0.6 * sweep_sine(n, rng.uniform(1600, 2000), rng.uniform(450, 600), 0.004, 0.007)
    return room(rng, y, wet=0.25, t60=0.5)


# ---------------------------------------------------------------------------------------------------------------------
# CRAYON, PLUME
# ---------------------------------------------------------------------------------------------------------------------
def scribble(rng, dur, lo, hi, stroke, gap, grit_rate, grit, inner=0.0, flourish=False, res=2600.0):
    """Graphite or nib on paper: strokes (speed rises and falls), friction band, grains of the paper."""
    n = ns(dur + 0.05)
    t = tt(n)
    speed = np.zeros(n)
    t0 = 0.0
    strokes = []
    while t0 < dur - 0.03:
        length = min(rng.uniform(*stroke), dur - t0)
        strokes.append((t0, length))
        t0 += length + rng.uniform(*gap)
    for k, (s0, length) in enumerate(strokes):
        i0, i1 = at(s0), min(n, at(s0 + length))
        u = np.linspace(0, 1, max(2, i1 - i0))
        a = rng.uniform(0.7, 1.0)
        prof = np.sin(np.pi * u) ** 0.6
        if flourish and k == len(strokes) - 1:
            prof = np.sin(np.pi * np.minimum(u * 2.5, 0.5)) * np.exp(-2.5 * u)
            a = 1.0
        speed[i0:i0 + len(u)] = a * prof[:max(0, min(len(u), n - i0))]
    if inner:
        speed *= 1.0 - inner + inner * (0.5 + 0.5 * np.sin(2 * np.pi * rng.uniform(6, 9) * t + rng.uniform(0, 6)))
    bed = noise(rng, n, lo=lo, hi=hi, peaks=((res, 2.0, 4.0),)) * speed * (1 + 0.35 * lfo(rng, n, 60))
    grain = crackle(rng, n, grit_rate * speed, lo=lo * 1.3, hi=hi, decay=(0.00015, 0.0006), sigma=0.7)
    y = 0.5 * bed + grit * grain
    return room(rng, y, wet=0.18, t60=0.4)


def crayon(rng, dur=0.4):
    return scribble(rng, dur, 900, 6000, stroke=(0.07, 0.12), gap=(0.01, 0.03), grit_rate=1800, grit=0.6, res=2400)


def plume(rng, dur=0.8):
    return scribble(rng, dur, 1600, 7000, stroke=(0.08, 0.22), gap=(0.0, 0.06), grit_rate=500, grit=0.45,
                    inner=0.45, flourish=True, res=3000)


# ---------------------------------------------------------------------------------------------------------------------
# FLAMME
# ---------------------------------------------------------------------------------------------------------------------
def flamme_souffle(rng, dur=0.75):
    """The flame breathes and flares: a soft low whoomph, a little brighter at the start, flicker, few crackles."""
    n = ns(dur)
    t = tt(n)
    env = env_hit(n, 0.07, 0.22)
    bright = smoothstep(t / 0.06) * np.exp(-t / 0.18)
    flick = 1 + 0.35 * lfo(rng, n, 14)
    y = (0.9 * noise(rng, n, lo=50, hi=380) + 0.5 * noise(rng, n, lo=250, hi=1600) * bright) * env * flick
    y += 0.5 * crackle(rng, n, 35 * env / env.max(), lo=1500, hi=7000, decay=(0.0005, 0.002))
    return room(rng, fade(y, 0, 0.1), wet=0.22, t60=0.5)


def flamme_baisse(rng, dur=0.7):
    """The flame goes down: a breath whose colour falls from bright to low, two or three crackles."""
    n = ns(dur)
    t = tt(n)
    centres = [1800, 1000, 560, 300, 160]
    y = np.zeros(n)
    for i, fc in enumerate(centres):
        c = 0.45 * dur * i / (len(centres) - 1)
        w = np.exp(-0.5 * ((t - c) / 0.11) ** 2)
        y += noise(rng, n, lo=fc / 1.8, hi=fc * 1.8) * w * (0.7 if fc > 1500 else 1.0)
    y *= env_hit(n, 0.04, 0.3) * (1 + 0.3 * lfo(rng, n, 12))
    y += 0.6 * crackle(rng, n, 10 * env_hit(n, 0.05, 0.2), lo=1500, hi=7000, decay=(0.0005, 0.002))
    return room(rng, fade(y, 0, 0.12), wet=0.22, t60=0.5)


def flamme_crepite(rng, dur=0.36):
    """The lamp crackles before it dies: sparse pops, a low roar."""
    n = ns(dur)
    env = env_bell(n, 0.02, 0.1, dur - 0.12)
    y = crackle(rng, n, 60 * env, lo=1000, hi=7000, decay=(0.0005, 0.002), sigma=0.6)
    y += 0.5 * crackle(rng, n, 12 * env, lo=200, hi=900, decay=(0.002, 0.006), sigma=0.4, kernels=3)
    y += 0.15 * noise(rng, n, lo=50, hi=400) * env * np.max(np.abs(y))
    return room(rng, y, wet=0.25, t60=0.55)


def flamme_eteinte(rng):
    """The lamp is blown out: a puff, the flame folds down (fwup), a thin hiss of smoke."""
    n = ns(0.9)
    t = tt(n)
    puff = noise(rng, n, lo=350, hi=3200, peaks=((1200, 1.5, 3.0),)) * env_bell(n, 0.015, 0.16, 0.04)
    fw = np.zeros(n)
    for i, fc in enumerate([500, 320, 200, 120]):
        c = 0.06 + 0.05 * i
        fw += noise(rng, n, lo=fc / 1.7, hi=fc * 1.7) * np.exp(-0.5 * ((t - c) / 0.04) ** 2)
    smoke = noise(rng, n, lo=3000, hi=9000) * env_bell(n, 0.08, 0.4, 0.0, start=0.12)
    y = puff + 0.7 * fw + 0.05 * smoke
    return room(rng, fade(y, 0, 0.1), wet=0.3, t60=0.7)


# ---------------------------------------------------------------------------------------------------------------------
# VENT (beds with gentle fades at both ends: they can be overlapped or chained)
# ---------------------------------------------------------------------------------------------------------------------
def vent(rng, dur, bands, gust_rate=0.35, whistle=(), leaves=0.0, fin=0.8, fout=0.9):
    n = ns(dur)
    gust = 0.55 + 0.45 * np.tanh(lfo(rng, n, gust_rate))
    y = np.zeros(n)
    for lo, hi, lvl, mod_rate in bands:
        y += noise(rng, n, lo=lo, hi=hi) * lvl * (1 + 0.35 * lfo(rng, n, mod_rate))
    y *= gust
    for fw, lvl in whistle:                     # three narrow bands whose levels swap slowly: a drifting whistle
        for r in (0.96, 1.0, 1.045):
            a = np.clip(lfo(rng, n, 0.3), 0, None) ** 2
            y += lvl * noise(rng, n, lo=fw * r / 1.025, hi=fw * r * 1.025, order=4) * a * gust
    if leaves:
        y += leaves * crackle(rng, n, 500 * gust ** 3, lo=2500, hi=9000, decay=(0.0004, 0.002))
    y = fade(y, fin, fout)
    return room(rng, y, wet=0.15, t60=0.6)


# ---------------------------------------------------------------------------------------------------------------------
# AILES
# ---------------------------------------------------------------------------------------------------------------------
def flap(rng, size=1.0):
    """One paper wing flap: the air it pushes, a membrane snap, paper fibres at the turn of the stroke."""
    m = ns(0.14)
    air = noise(rng, m, lo=160 / size, hi=1300 / size) * env_hit(m, 0.011 * size, 0.04 * size)
    snap = noise(rng, m, lo=1200, hi=6000) * env_hit(m, 0.0015, 0.010, start=0.004)
    crk = crackle(rng, m, 2500 * env_hit(m, 0.004, 0.012), lo=2000, hi=8000)
    return air + 0.45 * snap + 0.35 * crk


def ailes(rng, dur=0.45, rate=11.0, birds=1, crescendo=False, spread=0.5, single=0):
    n = ns(dur + 0.2)
    st = np.zeros((n, 2))
    if single:
        t0 = 0.0
        for k in range(single):
            stereo_add(st, flap(rng, size=1.3) * (1.0 if k == 0 else 0.6), t0, pan=rng.uniform(-0.2, 0.2))
            t0 += rng.uniform(0.10, 0.13)
    else:
        for b in range(birds):
            pan = rng.uniform(-spread, spread) if birds > 1 else rng.uniform(-0.15, 0.15)
            r = rate * rng.uniform(0.85, 1.15)
            t0 = rng.uniform(0.0, 0.6 / r) if birds > 1 else 0.0
            while t0 < dur - 0.03:
                a = rng.uniform(0.7, 1.0)
                if crescendo:
                    a *= 0.35 + 0.65 * (t0 / dur)
                stereo_add(st, flap(rng, size=rng.uniform(0.85, 1.15)) * a, t0, pan=pan)
                t0 += (1.0 / r) * rng.uniform(0.88, 1.12)
    return room(rng, st, wet=0.22, t60=0.55)


# ---------------------------------------------------------------------------------------------------------------------
# BALLE, CORDE, SOUFFLE, NOTES
# ---------------------------------------------------------------------------------------------------------------------
def balle(rng, drop=0.14, e=0.62, roll=0.22):
    """A soft wooden ball falls and rolls (dull wood): bounces closer and softer, then a short roll."""
    n = ns(0.75)
    t = tt(n)
    y = np.zeros(n)
    t0, a, dt = 0.0, 1.0, drop * rng.uniform(0.95, 1.05)
    while dt > 0.018 and t0 < 0.42:
        kk = knock(rng, rng.uniform(420, 500), q=10, ratios=(1.0, 2.6, 4.1), amps=(1.0, 0.35, 0.15), hard=0.7,
                   dur=0.12, thump=(rng.uniform(140, 160), 0.025, 0.35), click=0.08)
        place(y, a * kk, t0)
        t0 += dt
        a *= e ** 0.9
        dt *= e
    r0 = t0
    env = env_bell(n, 0.02, roll * 0.7, roll * 0.3, start=r0)
    rot = 14 * np.exp(-np.clip(t - r0, 0, None) / 0.4)
    am = 0.6 + 0.4 * np.sin(2 * np.pi * np.cumsum(rot) / SR)
    rum = noise(rng, n, lo=80, hi=600, peaks=((300, 2, 6),)) * am * env
    y += 0.18 * rum * np.max(np.abs(y)) / (np.max(np.abs(rum)) + 1e-12)
    return room(rng, y, wet=0.26, t60=0.5)


def corde(rng, rising=True, dur=0.62):
    """The swing rope creaks on the branch: a slow stick-slip through a rope and wood body, a small knock."""
    n = ns(dur + 0.12)
    t = tt(n)
    u = np.clip(t / dur, 0, 1)
    u = u ** 0.8 if rising else u ** 1.25
    rate = (24 + 38 * np.sin(np.pi * u) ** 1.2) * (1 + 0.06 * lfo(rng, n, 8))
    env = env_bell(n, 0.12, 0.2, dur - 0.32)
    base = 1.0 if rising else 0.88
    y = creak(rng, n, rate, [(260 * base, 5, 0.6), (560 * base, 7, 1.0), (1150 * base, 9, 0.6), (2300 * base, 11, 0.3)],
              jitter=0.12, grit=0.3, env=env)
    y /= np.max(np.abs(y)) + 1e-12
    y += 0.04 * noise(rng, n, lo=900, hi=4000) * env
    place(y, 0.35 * knock(rng, rng.uniform(480, 560), q=9, ratios=(1.0, 2.4), amps=(1.0, 0.3), hard=1.0, dur=0.15,
                          click=0.05), 0.0)
    return room(rng, y, wet=0.3, t60=0.7)


def souffle(rng, dur=0.22, kind="main"):
    """Soft air. main: a hand that swishes (the colour rises); lumiere: a long glowing breath; doux: dark and soft."""
    n = ns(dur + 0.15)
    t = tt(n)
    if kind == "main":
        u = np.clip(t / dur, 0, 1)
        env = env_bell(n, dur * 0.35, dur * 0.55, dur * 0.1)
        y = (noise(rng, n, lo=200, hi=900) * (1 - u) + noise(rng, n, lo=800, hi=3500) * u) * env
        return room(rng, y * (1 + 0.15 * lfo(rng, n, 20)), wet=0.22, t60=0.45)
    if kind == "lumiere":
        env = env_bell(n, 0.35, dur - 0.4, 0.05)
        y = noise(rng, n, lo=700, hi=9000, tilt=-3.0) * env
        y += 0.3 * noise(rng, n, lo=150, hi=600) * env
        y += 0.15 * crackle(rng, n, 300 * env, lo=5000, hi=12000, decay=(0.0002, 0.0008))
        return room(rng, y * (1 + 0.15 * lfo(rng, n, 6)), wet=0.35, t60=0.9)
    env = env_bell(n, 0.18, dur - 0.25, 0.07)
    y = noise(rng, n, lo=250, hi=2200, peaks=((1100, 1.2, 3.0),)) * env * (1 + 0.15 * lfo(rng, n, 8))
    return room(rng, y, wet=0.3, t60=0.7)


def note_bois(rng, freq):
    """A soft marimba-like note of light wood (a case of the house lights up again)."""
    n = ns(1.4)
    spec = [(freq, 0.42 * (600 / freq) ** 0.35, 1.0), (freq * 1.0035, 0.55 * (600 / freq) ** 0.35, 0.12),
            (freq * 3.93, 0.1, 0.3), (freq * 9.2, 0.025, 0.05)]
    y = soften(modes(n, spec), 0.35)
    y += 0.04 * noise(rng, n, lo=200, hi=2500) * env_hit(n, 0.0005, 0.004)
    return room(rng, y, wet=0.35, t60=0.9)


# ---------------------------------------------------------------------------------------------------------------------
# Catalogue: name -> generator (each name has its own seed)
# ---------------------------------------------------------------------------------------------------------------------
NOTES = {1: 523.25, 2: 587.33, 3: 783.99, 4: 880.00, 5: 1046.50, 6: 1174.66}     # C5 D5 G5 A5 C6 D6

SOUNDS = {
    # papier
    "papier-froisse-1": lambda r: papier_froisse(r, 0.40, 2200),
    "papier-froisse-2": lambda r: papier_froisse(r, 0.32, 1800),
    "papier-froisse-3": lambda r: papier_froisse(r, 0.45, 2600),
    "papier-froisse-4": lambda r: papier_froisse(r, 0.50, 1500, tremble=0.7),     # the sheet trembles
    "papier-glisse-1": lambda r: papier_glisse(r, 0.42),
    "papier-glisse-2": lambda r: papier_glisse(r, 0.34),
    "papier-glisse-3": lambda r: papier_glisse(r, 0.50),
    "papier-pose-1": lambda r: papier_pose(r, 1.0, 1.0),
    "papier-pose-2": lambda r: papier_pose(r, 0.7, 1.2),
    "papier-pose-3": lambda r: papier_pose(r, 1.2, 0.9),
    "papier-pose-4": lambda r: papier_pose(r, 0.9, 1.1),
    "papier-pile-1": lambda r: papier_pile(r, 1.0, 0),                             # put down
    "papier-pile-2": lambda r: papier_pile(r, 1.3, 3),                             # falls, sheets slide off
    "papier-pile-3": lambda r: papier_pile(r, 0.75, 1),                            # light stack
    "papier-dechire-1": lambda r: papier_dechire(r, 0.22),
    "papier-dechire-2": lambda r: papier_dechire(r, 0.16),
    "papier-dechire-3": lambda r: papier_dechire(r, 0.26),
    "papier-eventail-1": lambda r: papier_eventail(r, 7, 0.30),
    "papier-eventail-2": lambda r: papier_eventail(r, 6, 0.26),
    "papier-eventail-3": lambda r: papier_eventail(r, 9, 0.38),
    "papier-eventail-4": lambda r: papier_eventail(r, 12, 0.32, air=0.4),          # 12 sheets rise from the pile
    "papier-deplie-1": lambda r: papier_deplie(r, 11),                             # nterminable
    "papier-deplie-2": lambda r: papier_deplie(r, 6),                              # ttente
    "papier-deplie-3": lambda r: papier_deplie(r, 11),                             # ntelligence
    "papier-deplie-4": lambda r: papier_deplie(r, 11),                             # rtificielle
    # bois
    "bois-pas-1": lambda r: bois_pas(r), "bois-pas-2": lambda r: bois_pas(r),
    "bois-pas-3": lambda r: bois_pas(r), "bois-pas-4": lambda r: bois_pas(r),
    "bois-pas-leger-1": lambda r: bois_pas(r, light=True), "bois-pas-leger-2": lambda r: bois_pas(r, light=True),
    "bois-pas-leger-3": lambda r: bois_pas(r, light=True),
    "bois-chaise-1": lambda r: bois_chaise(r, 1), "bois-chaise-2": lambda r: bois_chaise(r, 2),
    "bois-chaise-3": lambda r: bois_chaise(r, 3),
    "bois-talon-1": bois_talon, "bois-talon-2": bois_talon,
    "bois-clic-1": lambda r: bois_clic(r), "bois-clic-2": lambda r: bois_clic(r, double=True),
    "bois-clic-3": lambda r: bois_clic(r),
    "bois-leger-1": lambda r: bois_leger(r, 2), "bois-leger-2": lambda r: bois_leger(r, 1),
    "bois-leger-3": lambda r: bois_leger(r, 3),
    "bois-tampon-1": bois_tampon, "bois-tampon-2": bois_tampon, "bois-tampon-3": bois_tampon,
    "bois-clac-1": bois_clac,
    "bois-porte-ouvre": bois_porte_ouvre,
    "bois-porte-ferme": bois_porte_ferme,
    # tic, tac
    "tic-1": lambda r: tic_tac(r, "tic"), "tic-2": lambda r: tic_tac(r, "tic"), "tic-3": lambda r: tic_tac(r, "tic"),
    "tac-1": lambda r: tic_tac(r, "tac"), "tac-2": lambda r: tic_tac(r, "tac"),
    "tic-sec": lambda r: tic_tac(r, "tic", dry=True),
    "tic-lointain": lambda r: tic_tac(r, "tic", far=True), "tac-lointain": lambda r: tic_tac(r, "tac", far=True),
    "tictac-1": lambda r: tic_tac(r, pair=True), "tictac-2": lambda r: tic_tac(r, pair=True),
    "tictac-3": lambda r: tic_tac(r, pair=True),
    "tictac-lointain": lambda r: tic_tac(r, pair=True, far=True),
    "tictac-dore": lambda r: tic_tac(r, pair=True, gold=True),
    "tictac-accelere": tictac_accelere,
    # roulettes, aiguilles, maillons, punaise
    "roulettes-1": lambda r: roulettes(r, 0.30, 12.0), "roulettes-2": lambda r: roulettes(r, 0.34, 11.0),
    "roulettes-3": lambda r: roulettes(r, 0.28, 13.0), "roulettes-4": lambda r: roulettes(r, 0.36, 12.0),
    "aiguilles-1": lambda r: aiguilles(r, 0.50, 22.0, 3200.0),
    "aiguilles-2": lambda r: aiguilles(r, 0.60, 30.0, 3600.0),                     # fast
    "aiguilles-rebours": lambda r: aiguilles(r, 0.67, f0=2700.0, times=ease_times(
        24, 0.64, lambda u: np.where(u < 0.5, 2 * u * u, 1 - (-2 * u + 2) ** 2 / 2))),   # a turn backwards, inOut
    "aiguilles-chiffre": aiguilles_chiffre,
    "maillons-1": lambda r: maillons(r, 5), "maillons-2": lambda r: maillons(r, 4), "maillons-3": lambda r: maillons(r, 6),
    "maillons-tendu": lambda r: maillons(r, 5, tight=True),
    "punaise-1": punaise, "punaise-2": punaise, "punaise-3": punaise,
    # crayon, plume
    "crayon-1": lambda r: crayon(r, 0.40), "crayon-2": lambda r: crayon(r, 0.47), "crayon-3": lambda r: crayon(r, 0.35),
    "plume-1": lambda r: plume(r, 0.80), "plume-2": lambda r: plume(r, 0.80),
    # flamme
    "flamme-souffle-1": lambda r: flamme_souffle(r, 0.75), "flamme-souffle-2": lambda r: flamme_souffle(r, 0.65),
    "flamme-baisse-1": lambda r: flamme_baisse(r, 0.70), "flamme-baisse-2": lambda r: flamme_baisse(r, 0.62),
    "flamme-crepite": flamme_crepite,
    "flamme-eteinte": flamme_eteinte,
    # vent
    "vent-soir": lambda r: vent(r, 4.75, [(150, 1500, 1.0, 0.8), (500, 3000, 0.35, 1.2)], 0.45,
                                whistle=((720, 0.10),), fin=0.6, fout=0.45),
    "vent-nuit": lambda r: vent(r, 2.6, [(90, 900, 1.0, 0.6), (300, 1400, 0.3, 0.9)], 0.5,
                                whistle=((420, 0.06),), fin=0.5, fout=0.8),
    "vent-nuit-lointain": lambda r: vent(r, 3.6, [(70, 600, 1.0, 0.4)], 0.3, fin=0.8, fout=1.2),
    "vent-doux": lambda r: vent(r, 4.6, [(140, 2200, 1.0, 0.5), (900, 5000, 0.2, 0.9)], 0.3, leaves=0.25,
                                fin=0.9, fout=1.4),
    # ailes
    "ailes-rafale-1": lambda r: ailes(r, 0.36, 12.0), "ailes-rafale-2": lambda r: ailes(r, 0.58, 11.0),
    "ailes-rafale-3": lambda r: ailes(r, 0.45, 12.5, birds=3, spread=0.5),
    "ailes-nuee": lambda r: ailes(r, 0.55, 12.0, birds=5, crescendo=True, spread=0.8),
    "ailes-simple-1": lambda r: ailes(r, single=2), "ailes-simple-2": lambda r: ailes(r, single=1),
    # balle, corde, souffle
    "balle-1": lambda r: balle(r), "balle-2": lambda r: balle(r, drop=0.12, e=0.58),
    "corde-1": lambda r: corde(r, True), "corde-2": lambda r: corde(r, False),
    "souffle-1": lambda r: souffle(r, 0.20), "souffle-2": lambda r: souffle(r, 0.18), "souffle-3": lambda r: souffle(r, 0.24),
    "souffle-lumiere-1": lambda r: souffle(r, 1.0, "lumiere"), "souffle-lumiere-2": lambda r: souffle(r, 0.85, "lumiere"),
    "souffle-doux": lambda r: souffle(r, 0.7, "doux"),
}
SOUNDS.update({f"note-bois-{k}": (lambda f: (lambda r: note_bois(r, f)))(f) for k, f in NOTES.items()})


def rng_for(name):
    return np.random.default_rng([BASE_SEED, zlib.crc32(name.encode("utf-8"))])


def main(argv):
    if "--list" in argv:
        print("\n".join(sorted(SOUNDS)))
        return
    prefixes = [a for a in argv if not a.startswith("-")]
    os.makedirs(OUT_DIR, exist_ok=True)
    count = 0
    for name in sorted(SOUNDS):
        if prefixes and not any(name.startswith(p) for p in prefixes):
            continue
        st = finish(SOUNDS[name](rng_for(name)), trim=not name.startswith("vent"))
        write_wav(os.path.join(OUT_DIR, name + ".wav"), st)
        count += 1
        print(f"{name:22s} {len(st) / SR:5.2f} s")
    print(f"{count} sound(s) in {os.path.relpath(OUT_DIR, HERE)}/")


if __name__ == "__main__":
    main(sys.argv[1:])
