#!/usr/bin/env python3
"""Sentence-level timing table of the voice, for the "Minutage" section of DIRECTIONS.md and the storyboard.

Reads <project>/onsets.json (written by onsets.py on the EDITED voice) and groups its phrases into sentences at the
final punctuation (. ? !). Prints a Markdown table: sentence, start, end, silence after it, with the cue of its
first word. Usage: python3 minutage.py <project>/onsets.json
"""
import json, sys

END = (".", "?", "!", "…")


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    o = json.load(open(sys.argv[1], encoding="utf-8"))
    rows, cur = [], None
    for p in o["phrases"]:                                   # p["words"] holds indices into o["words"]
        for n, idx in enumerate(p["words"]):
            w, last = o["words"][idx], n == len(p["words"]) - 1
            if not any(c.isalnum() for c in w["w"]):          # a lone "?" or "." closes the sentence
                if cur:
                    cur["words"][-1]["w"] += w["w"]; rows.append(cur); cur = None
                continue
            if cur is None:
                cur = {"start": w["s"], "words": []}
            cur["words"].append(dict(w)); cur["end"] = p["end"]; cur["silence"] = p.get("silence_after")
            if w["w"].rstrip("»\"')").endswith(END) or (last and (p.get("silence_after") or 0) > 1.5):
                rows.append(cur); cur = None
    if cur:
        rows.append(cur)
    print(f"Voix montée : {o['duration']:.2f} s, {len(rows)} phrases. Repères complets mot à mot dans `onsets.json`.\n")
    print("| # | Phrase | Début | Fin | Silence après |\n|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        text = " ".join(w["w"] for w in r["words"]).replace(" -", "-")
        sil = f"{r['silence']:.2f} s" if r.get("silence") is not None else "fin"
        print(f"| {i} | {text} | {r['start']:.2f} | {r['end']:.2f} | {sil} |")


if __name__ == "__main__":
    main()
