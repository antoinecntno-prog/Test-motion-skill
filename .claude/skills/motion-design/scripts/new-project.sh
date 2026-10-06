#!/bin/bash
# New motion design project, ready for the method (brief, script, voice, storyboard, animation, music).
# Creates the folder tree and the HyperFrames project files (meta.json, hyperframes.json), copies what the method
# fills for each film from this skill's templates/ (BRIEF.md, frame.md, STORYBOARD.md, assemble.sh, build-audio.sh,
# build-music-options.py, musique.json) plus DIRECTIONS.md from templates/DIRECTIONS-TEMPLATE.md at the repository
# root, and vendors GSAP in assets/vendor/ (the frames and the assembled film load it locally: the CDN is blocked in
# cloud sessions). GSAP and the fonts come from the npm registry (npm pack), with jsDelivr as a fallback.
#
# Usage (from anywhere):
#   bash .claude/skills/motion-design/scripts/new-project.sh <name> [--fonts[=family,family,...]]
#        -> <repository root>/<name>/ ; --fonts alone fetches the default trio (instrument-sans, space-mono,
#           big-shoulders); --fonts=archivo,hanken-grotesk,pacifico fetches those Fontsource families (latin, every
#           weight, SIL Open Font License)
#   bash .claude/skills/motion-design/scripts/new-project.sh <path/to/name>   -> that folder (tests only: the project
#        scripts reach the skills through ../.claude/skills/, so a real film lives at the repository root)
# Films to imitate: examples/ligne-du-temps-v8/ and ifs-maillot-club/ (Contino Sport, cloud session, 11 sequences).
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
SKILL="$(dirname "$HERE")"
TPL="$SKILL/templates"
ROOT="$(cd "$SKILL/../../.." && pwd)"
GSAP_V="3.14.2"

ARG="${1:-}"
FONTS="${2:-}"
[ -n "$ARG" ] || { echo "usage: new-project.sh <name> [--fonts[=family,...]]" >&2; exit 1; }
case "$ARG" in
  */*) DST="$ARG" ;;
  *) DST="$ROOT/$ARG" ;;
esac
NAME="$(basename "$DST")"
[[ "$NAME" =~ ^[a-z0-9][a-z0-9-]*$ ]] || { echo "new-project: use a kebab-case name (a-z, 0-9, -), not '$NAME'" >&2; exit 1; }
[ ! -e "$DST" ] || { echo "new-project: $DST already exists" >&2; exit 1; }
[ -f "$ROOT/templates/DIRECTIONS-TEMPLATE.md" ] || { echo "new-project: templates/ not found at $ROOT" >&2; exit 1; }

mkdir -p "$DST"/assets/{audio/sfx,audio/reprises,fonts,icons,img,music,vendor} "$DST"/compositions/frames \
         "$DST"/reference "$DST"/styleframes "$DST"/planches
cp "$TPL"/BRIEF.md "$TPL"/frame.md "$TPL"/STORYBOARD.md "$TPL"/assemble.sh "$TPL"/build-audio.sh \
   "$TPL"/build-music-options.py "$DST"/
cp "$TPL"/musique.json "$DST"/assets/audio/musique.json
cp "$ROOT"/templates/DIRECTIONS-TEMPLATE.md "$DST"/DIRECTIONS.md
chmod +x "$DST"/assemble.sh "$DST"/build-audio.sh "$DST"/build-music-options.py
echo '[]' > "$DST"/assets/audio/sfx-events.json   # format: templates/sfx-events.json

cat > "$DST"/meta.json <<EOF
{
  "id": "$NAME",
  "name": "$NAME",
  "width": 1920,
  "height": 1080,
  "fps": 30
}
EOF
cat > "$DST"/hyperframes.json <<'EOF'
{
  "$schema": "https://hyperframes.heygen.com/schema/hyperframes.json",
  "paths": { "blocks": "compositions", "components": "compositions/components", "assets": "assets" }
}
EOF

TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
# GSAP, vendored: the frames load assets/vendor/gsap-<v>.min.js and assemble.sh rewrites the index to it
( cd "$TMP" && npm pack "gsap@$GSAP_V" --silent >/dev/null 2>&1 && tar xzf "gsap-$GSAP_V.tgz" package/dist/gsap.min.js ) \
  && cp "$TMP/package/dist/gsap.min.js" "$DST/assets/vendor/gsap-$GSAP_V.min.js" \
  || curl -sfL "https://cdn.jsdelivr.net/npm/gsap@$GSAP_V/dist/gsap.min.js" -o "$DST/assets/vendor/gsap-$GSAP_V.min.js" \
  || echo "warning: GSAP not vendored (no npm registry nor CDN): copy gsap.min.js to assets/vendor/gsap-$GSAP_V.min.js" >&2

fetch_family() {   # $1 = Fontsource id (archivo, hanken-grotesk, pacifico...): every latin weight, normal and italic
  local fam="$1" got=0
  if ( cd "$TMP" && npm pack "@fontsource/$fam" --silent >/dev/null 2>&1 ); then
    mkdir -p "$TMP/$fam" && tar xzf "$TMP"/fontsource-"$fam"-*.tgz -C "$TMP/$fam"
    for f in "$TMP/$fam"/package/files/"$fam"-latin-*.woff2; do
      [ -e "$f" ] || continue; cp "$f" "$DST/assets/fonts/"; got=$((got + 1))
    done
    [ -f "$TMP/$fam/package/LICENSE" ] && cp "$TMP/$fam/package/LICENSE" "$DST/assets/fonts/$fam-LICENSE.txt"
  fi
  if [ "$got" = 0 ]; then
    for w in 400 500 600 700 800 900; do
      curl -sfL "https://cdn.jsdelivr.net/fontsource/fonts/$fam@latest/latin-$w-normal.woff2" \
        -o "$DST/assets/fonts/$fam-latin-$w-normal.woff2" && got=$((got + 1)) || rm -f "$DST/assets/fonts/$fam-latin-$w-normal.woff2"
    done
  fi
  echo "fonts: $fam, $got file(s)"
}
case "$FONTS" in
  --fonts) for fam in instrument-sans space-mono big-shoulders; do fetch_family "$fam"; done ;;
  --fonts=*) IFS=',' read -ra FAMS <<< "${FONTS#--fonts=}"; for fam in "${FAMS[@]}"; do fetch_family "$fam"; done ;;
  "") ;;
  *) echo "new-project: unknown option $FONTS" >&2; exit 1 ;;
esac

echo "project created: $DST"
[ "$(cd "$DST/.." && pwd)" = "$ROOT" ] || echo "warning: not at the repository root, assemble.sh and build-audio.sh will not find ../.claude/skills/"
echo "to fill for this film: BRIEF.md first, then SCRIPT.md, DIRECTIONS.md, frame.md, STORYBOARD.md (grep -n '{{' must"
echo "print nothing), then the settings of build-audio.sh, assemble.sh and assets/audio/musique.json"
[ -n "$FONTS" ] || echo "fonts: not fetched (pass --fonts=family,... at creation, Fontsource ids)"
