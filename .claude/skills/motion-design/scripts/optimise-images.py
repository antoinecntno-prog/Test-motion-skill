#!/usr/bin/env python3
"""Shrink the heavy images of a project before the workers use them.

HyperFrames inlines every image of a frame in the bundle (up to 2 MB each, and again in every frame that uses it):
four 2 MB cutouts made the film page too heavy to load. A cutout shown at most ~900 px tall needs no more than
1100 px. PNG cutouts are resized and quantized (256 colors, transparency kept); JPG photos are resized and saved at
quality 85. Files under --min-kb are left alone. Each original is first copied to <project>/assets/img/originaux/.

Usage: python3 optimise-images.py <project> [--max 1100] [--min-kb 600]
"""
import argparse, glob, os, shutil
from PIL import Image


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("project")
    ap.add_argument("--max", type=int, default=1100); ap.add_argument("--min-kb", type=int, default=600)
    a = ap.parse_args()
    src = os.path.join(a.project, "assets", "img"); keep = os.path.join(src, "originaux")
    for p in sorted(glob.glob(os.path.join(src, "*.png")) + glob.glob(os.path.join(src, "*.jp*g"))):
        kb = os.path.getsize(p) // 1024
        if kb < a.min_kb:
            continue
        os.makedirs(keep, exist_ok=True)
        if not os.path.exists(os.path.join(keep, os.path.basename(p))):
            shutil.copy2(p, keep)
        im = Image.open(p); w, h = im.size
        if max(w, h) > a.max:
            k = a.max / max(w, h); im = im.resize((round(w * k), round(h * k)), Image.LANCZOS)
        if p.lower().endswith(".png"):
            im = im.convert("RGBA").quantize(colors=256, method=Image.FASTOCTREE, dither=Image.FLOYDSTEINBERG)
            im.save(p, optimize=True)
        else:
            im.convert("RGB").save(p, quality=85, optimize=True)
        print(f"optimise-images: {os.path.basename(p)} {w}x{h} {kb} KB -> {im.size[0]}x{im.size[1]} {os.path.getsize(p) // 1024} KB")


if __name__ == "__main__":
    main()
