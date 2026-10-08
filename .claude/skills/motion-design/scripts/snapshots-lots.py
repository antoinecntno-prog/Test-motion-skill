#!/usr/bin/env python3
"""Key images of a whole film, in batches, plus one labelled contact sheet (the "planche" shown to the user).

Why: `npx hyperframes snapshot` waits 10 s at most for the page to load (hard-coded). A film of 9 frames or more
exceeds it ("Navigation timeout of 10000 ms exceeded") while each frame alone loads fine. The render itself waits
60 s, so only the snapshots need this. The script assembles a few consecutive frames at a time (assemble.sh skips the
frame files that are absent and packs the others from 0), snapshots them at the requested global times, then puts
every frame back and re-assembles the whole film, even on error.

Usage (from the repository root or anywhere):
  python3 .claude/skills/motion-design/scripts/snapshots-lots.py <project> --at 2.3,4.52,4.60,12.1 [--lot 5]
         [--out snapshots/lots] [--titre "Film · planche"] [--labels labels.json]
  --at     global times in seconds (seams: T-0.04 and T+0.04)
  --labels optional JSON {"4.52": "fin du whip", ...} printed under each image
Writes <project>/<out>/t<time>.png for every time and <project>/planches/<date>-planche.jpg (or --planche PATH).
"""
import argparse, datetime, glob, json, os, re, shutil, subprocess, sys, tempfile

ENV = dict(os.environ, HYPERFRAMES_NO_TELEMETRY="1", DO_NOT_TRACK="1", HYPERFRAMES_SKIP_SKILLS="1",
           HYPERFRAMES_NO_UPDATE_CHECK="1")


def frames_of(project):
    """(id, start, duration, src) of every frame, from the fully assembled index.html."""
    s = open(os.path.join(project, "index.html"), encoding="utf-8").read()
    out = []
    for m in re.finditer(r"<div\b[^>]*?data-composition-id=\"([^\"]+)\"[^>]*>", s):
        tag = m.group(0)
        src = re.search(r'data-composition-src="([^"]+)"', tag)
        st, du = re.search(r'data-start="([0-9.]+)"', tag), re.search(r'data-duration="([0-9.]+)"', tag)
        if src and st and du:
            out.append((m.group(1), float(st.group(1)), float(du.group(1)), src.group(1)))
    return sorted(out, key=lambda f: f[1])


def assemble(project):
    r = subprocess.run(["bash", "assemble.sh"], cwd=project, env=ENV, capture_output=True, text=True)
    if r.returncode:
        sys.exit("snapshots-lots: assemble.sh failed\n" + r.stdout[-2000:] + r.stderr[-2000:])


def planche(pngs, labels, title, path):
    from PIL import Image, ImageDraw, ImageFont
    W, H, pad, lab, cols, top = 560, 315, 14, 30, 3, 60
    rows = (len(pngs) + cols - 1) // cols
    def font(bold, size):
        for p in (f"/usr/share/fonts/truetype/dejavu/DejaVuSans{'-Bold' if bold else ''}.ttf",
                  "/System/Library/Fonts/Supplemental/Arial.ttf"):
            if os.path.exists(p): return ImageFont.truetype(p, size)
        return ImageFont.load_default()
    f, ft = font(False, 16), font(True, 22)
    sheet = Image.new("RGB", (cols * (W + pad) + pad, top + rows * (H + lab + pad) + pad), (24, 22, 28))
    d = ImageDraw.Draw(sheet)
    d.text((pad, 18), title, fill=(245, 239, 243), font=ft)
    for i, (p, l) in enumerate(zip(pngs, labels)):
        x, y = pad + (i % cols) * (W + pad), top + (i // cols) * (H + lab + pad)
        sheet.paste(Image.open(p).convert("RGB").resize((W, H), Image.LANCZOS), (x, y))
        d.text((x, y + H + 6), l, fill=(220, 214, 224), font=f)
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    sheet.save(path, quality=85)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project"); ap.add_argument("--at", required=True)
    ap.add_argument("--lot", type=int, default=5); ap.add_argument("--out", default="snapshots/lots")
    ap.add_argument("--titre", default=None); ap.add_argument("--labels", default=None)
    ap.add_argument("--planche", default=None)
    a = ap.parse_args()
    project = os.path.abspath(a.project)
    times = sorted(float(t) for t in a.at.split(",") if t.strip())
    labels = json.load(open(a.labels, encoding="utf-8")) if a.labels else {}

    assemble(project)
    frames = frames_of(project)
    if not frames:
        sys.exit("snapshots-lots: no frame in index.html")
    def frame_at(t):
        for i, f in enumerate(frames):
            if f[1] <= t < f[1] + f[2]: return i
        return len(frames) - 1
    need = sorted({frame_at(t) for t in times})
    batches, cur = [], []
    for i in need:                                   # consecutive frames, at most --lot per batch
        if cur and (i != cur[-1] + 1 or len(cur) >= a.lot):
            batches.append(cur); cur = []
        cur.append(i)
    if cur: batches.append(cur)

    out = os.path.join(project, a.out); os.makedirs(out, exist_ok=True)
    stash = tempfile.mkdtemp(prefix="lots-")
    srcs = [os.path.join(project, f[3]) for f in frames]
    written = {}
    try:
        for b in batches:
            for i, p in enumerate(srcs):
                if i not in b and os.path.exists(p): shutil.move(p, os.path.join(stash, os.path.basename(p)))
            assemble(project)
            t0 = frames[b[0]][1]
            mine = [t for t in times if frame_at(t) in b]
            tmp = os.path.join(stash, "snap"); shutil.rmtree(tmp, ignore_errors=True)
            local = ",".join(f"{max(0.0, t - t0):.3f}" for t in mine)
            r = subprocess.run(["npx", "hyperframes", "snapshot", "--at", local, "--no-end", "--describe", "false",
                                "--output", tmp], cwd=project, env=ENV, capture_output=True, text=True)
            pngs = sorted(glob.glob(os.path.join(tmp, "frame-*.png")))
            if r.returncode or len(pngs) != len(mine):
                sys.exit(f"snapshots-lots: snapshot failed for frames {[frames[i][0] for i in b]}\n{r.stdout[-1500:]}{r.stderr[-1500:]}")
            for t, p in zip(mine, pngs):
                dst = os.path.join(out, f"t{t:06.2f}.png"); shutil.move(p, dst); written[t] = dst
            for p in glob.glob(os.path.join(stash, "*.html")):
                shutil.move(p, os.path.join(os.path.dirname(srcs[0]), os.path.basename(p)))
            print(f"snapshots-lots: {len(mine)} image(s) for {', '.join(frames[i][0] for i in b)}")
    finally:
        for p in glob.glob(os.path.join(stash, "*.html")):
            shutil.move(p, os.path.join(os.path.dirname(srcs[0]), os.path.basename(p)))
        assemble(project)
        shutil.rmtree(stash, ignore_errors=True)

    pngs = [written[t] for t in times]
    labs = [f"{t:.2f} s · {frames[frame_at(t)][0]}" + (f" · {labels[str(t)]}" if str(t) in labels else "") for t in times]
    path = a.planche or os.path.join(project, "planches", f"{datetime.date.today().isoformat()}-planche.jpg")
    planche(pngs, labs, a.titre or f"{os.path.basename(project)} · images clés", path)
    print(f"snapshots-lots: planche {path}")


if __name__ == "__main__":
    main()
