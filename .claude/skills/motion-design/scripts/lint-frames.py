#!/usr/bin/env python3
"""Static checks on the frames of a project, for the faults HyperFrames' lint does not see and that cost a render
(each one happened on a real film). Run it after every wave of workers, before assembling.

BLOCKING (exit 1):
  network      a script, font or image loaded from the network (the CDN is blocked in cloud sessions)
  doublon-var  the same `var NAME` declared twice in a frame's script: the second silently overwrites the first
               (a camera proxy `WB` overwrote the word list `WB`, the frame showed only its thread)
  random       Math.random / Date.now / repeat: -1 / CSS animation (the render seeks, it must be deterministic)
  visible      style.visibility = "visible" (the element shows over the whole film)
  ancres       FX.ANCHORS overridden inside a frame (frames of one world must draw the same thread)
  kit          the shared kit pasted in the frame differs from reference/<world>.html
WARNING:
  couleur      a color tweened (use opacity: grey = ink at 35 %)
  dash         strokeDashoffset tweened directly (tween a proxy, draw with the kit's fxDrawThread)
  z-index      a negative z-index (paints behind the stacking context; carry shadows in a drop-shadow filter)
  image-lourde an image over 1 MB (it is inlined in the bundle; run optimise-images.py)

Usage: python3 lint-frames.py <project> [frame_id ...]
"""
import glob, os, re, sys

KIT_RE = re.compile(r"/\* =+ (?:FIL [^:]+|KIT[^:]*) : début du kit JS à copier =+ \*/(.*?)/\* =+ (?:FIL [^:]+|KIT[^:]*) : fin du kit JS à copier =+ \*/", re.S)


def kit_block(text):
    m = KIT_RE.search(text)
    return m.group(1).replace("../assets/", "assets/").strip() if m else None


CSS_RE = re.compile(r"/\* =+ [^:]+ : début du bloc CSS à copier =+ \*/.*?/\* =+ [^:]+ : fin du bloc CSS à copier =+ \*/", re.S)


def duplicate_vars(code):
    """Names declared twice with `var` in the same function scope (comments and strings stripped first)."""
    code = re.sub(r"/\*.*?\*/|//[^\n]*", "", code, flags=re.S)
    code = re.sub(r"`(?:\\.|[^`\\])*`|\"(?:\\.|[^\"\\\n])*\"|'(?:\\.|[^'\\\n])*'", '""', code)
    stack, scopes, seen, dups = [], [0], {}, set()
    fid = 0
    for m in re.finditer(r"[{}]|\bvar\s+([A-Za-z_$][\w$]*)", code):
        tok = m.group(0)
        if tok == "{":
            is_fn = re.search(r"(?:function\b[^{(]*\([^()]*\)|=>)\s*$", code[max(0, m.start() - 300):m.start()])
            if is_fn:
                fid += 1; scopes.append(fid)
            stack.append(bool(is_fn))
        elif tok == "}":
            if stack and stack.pop(): scopes.pop()
        else:
            key = (scopes[-1], m.group(1))
            if key in seen: dups.add(m.group(1))
            seen[key] = True
    return sorted(dups)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    project = sys.argv[1]
    only = set(sys.argv[2:])
    refs = {}
    for r in glob.glob(os.path.join(project, "reference", "*.html")):
        k = kit_block(open(r, encoding="utf-8").read())
        if k: refs[os.path.basename(r)] = k
    blocking = 0
    for path in sorted(glob.glob(os.path.join(project, "compositions", "frames", "*.html"))):
        fid = os.path.basename(path)[:-5]
        if only and fid not in only:
            continue
        s = open(path, encoding="utf-8").read()
        kit = kit_block(s)
        body = s.replace(KIT_RE.search(s).group(0), "") if kit else s      # the frame's own code, kit excluded
        body = CSS_RE.sub("", body)                                            # and the shared CSS block
        found = []
        for m in re.finditer(r"(?:src|href)\s*=\s*[\"'](https?://[^\"']+)|url\(\s*[\"']?(https?://[^)\"']+)", s):
            u = m.group(1) or m.group(2)
            if "w3.org" not in u: found.append(("B", "network", u[:90]))
        dups = duplicate_vars(body)
        if dups: found.append(("B", "doublon-var", ", ".join(dups)))
        for pat, what in ((r"Math\.random", "Math.random"), (r"Date\.now|new Date\(\)", "Date"),
                          (r"repeat\s*:\s*-1", "repeat: -1"), (r"@keyframes|animation\s*:", "CSS animation")):
            if re.search(pat, body): found.append(("B", "random", what))
        if re.search(r"visibility\s*=\s*[\"']visible", s): found.append(("B", "visible", "style.visibility = \"visible\""))
        if re.search(r"FX\.ANCHORS\.\w+\s*=", body): found.append(("B", "ancres", "FX.ANCHORS overridden in the frame"))
        if kit and refs:
            if not any(kit == k for k in refs.values()):
                found.append(("B", "kit", "kit differs from " + ", ".join(refs)))
        for m in re.finditer(r"(?:ft|tw|\.to|\.fromTo|\.from)\s*\([^;]*?\bcolor\s*:", body):
            found.append(("W", "couleur", body[m.start():m.start() + 70].replace("\n", " ")))
            break
        if re.search(r"(?:ft|tw|\.to|\.fromTo)\s*\([^;]*strokeDashoffset", body):
            found.append(("W", "dash", "strokeDashoffset tweened directly"))
        if re.search(r"z-index\s*:\s*-\d", body): found.append(("W", "z-index", "negative z-index"))
        for img in set(re.findall(r"assets/img/[\w.-]+", s)):
            p = os.path.join(project, img)
            if os.path.exists(p) and os.path.getsize(p) > 1_000_000:
                found.append(("W", "image-lourde", f"{img} ({os.path.getsize(p) // 1024} KB)"))
        if not found:
            print(f"ok      {fid}")
        for lvl, code, msg in found:
            print(f"{'BLOQUANT' if lvl == 'B' else 'alerte '} {fid}: {code}: {msg}")
            blocking += lvl == "B"
    sys.exit(1 if blocking else 0)


if __name__ == "__main__":
    main()
