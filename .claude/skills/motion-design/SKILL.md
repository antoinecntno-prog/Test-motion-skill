---
name: motion-design
description: Makes an agency-grade launch motion design film (30 to 60 s, 16:9, voice-over) in this repository with HyperFrames and the pinned HeyGen skills, from a one-page brief (subject and global design), in 5 steps the user validates (script, voice, storyboard, animation, music and sound effects), then checks, delivery and, only if asked, distribution. Use when the user asks here for a launch, promo, landing page, product or LinkedIn motion design video, gives a subject and a design for a new video, or asks for "a film like the flagship example". Not for editing filmed footage or talking-head videos.
---

# Motion design: launch film, end to end

You are the orchestrator. You run every step yourself except building the frames (one sub-agent per frame). The detail
of each step is in `references/method.md`; this file is the order, the commands, the gates and the house rules.

**Before anything**: follow `AGENTS.md` (pinned local CLI, forbidden commands, empty `.env` at the root). This skill
replaces Steps 0 to 3.1 of `product-launch-video` (no preset capture, no HeyGen voice or music API) and reuses its
packet builder, assembler and transition injector.

**The reference film**: `examples/ligne-du-temps-v8/` (« La ligne du temps », 49.5 s), the final result of this method.
Its `frame.md`, `STORYBOARD.md`, `reference/frise.html`, frames and `build-audio-v8.py` show everything that works:
imitate them.

**The rule that makes it look like an agency**: the film is written as a storyboard before anything is animated, and
the rhythm is counted in events, not in shots. Something new every 0.5 to 1 s (every 0.1 to 0.3 s in the hook), a
camera that never stops (a slow drift plus dated moves toward what comes next), a bridge object at every seam (an
object of shot N takes another role in shot N+1), elements that arrive too big and blurred from the camera then
settle, three depth levels, one thing to look at at a time. The grammar, with its numbers and GSAP recipes:
`patterns/STORYBOARD-CRAFT.md` (repository root).

**The second reference film**: `ifs-maillot-club/` (Contino Sport, 52 s, 11 sequences, LinkedIn), made in a claude.ai
cloud session with the ElevenLabs connector, the score composed on the edit and a brand changed after the montage. Its
brief, filled after the fact, is `BRIEF.md`; its pilot frame `compositions/frames/01-juin.html` is the
reference implementation for workers, its `assets/audio/` shows `musique.json`, `patch-voix.json` and `sfx-events.json`.

## Quick start: from a brief

The user gives a subject and a global design; everything else follows this skill. In order:

1. Create the project (below), fill `<project>/BRIEF.md` from what the user said, write what is missing as stated
   assumptions, and ask ONE grouped question only for what changes the film (the brand name exactly as said and
   written, its logo, the URL, what must never be shown, the credits allowed).
2. Run the 5 steps. With "reduced gates" in the brief, stop only at the script, the storyboard sheet, the pilot sheet
   and the mix; otherwise at every gate.
3. Show the work as sheets (`snapshots-lots.py` writes one in `<project>/planches/`) and draft renders, never as a
   list of files. Commit after every gate (a cloud container is wiped after an idle period).
4. Keep within the budget of `references/worker-dispatch.md` § Budget: pilot first, workers at medium effort, no
   reviewer agents, one-line fixes yourself.

## Before step 1: preflight and project

`test -f .env || cp .env.example .env` and `test -d node_modules || npm ci`. Pick a kebab-case `<project>` name, then:

```bash
bash .claude/skills/motion-design/scripts/new-project.sh <project> --fonts=<fontsource ids of the brief, comma-separated>
```

It creates `<project>/` at the repository root (folders, `meta.json`, `hyperframes.json`, `BRIEF.md` and the templates
to fill, GSAP vendored in `assets/vendor/`, the fonts from the npm registry). Fill `BRIEF.md` (template:
`templates/BRIEF.md`): the subject (the pain, the promise, the steps to show), the global design, the brand exactly as
it is said and written with its logo and URL, where the film will be seen, the real interfaces and photos (recent
screenshots; raw ones stay out of the repository), what to anonymize and what never to show in the pain (a generic
product, never the client's own), the voice, the music, the gates and the credits allowed. Shrink the heavy images:
`python3 .claude/skills/motion-design/scripts/optimise-images.py <project>`. All paths below are relative to the
repository root. `references/method.md` § 2.

## The 5 steps (each one ends on the user's approval)

### 1. Script (gate)

Propose 5 to 7 concepts in one line each, then write 2 versions in full in `<project>/SCRIPT.md`, each in two forms:
the staged version and the version to paste in ElevenLabs (no staging at all). Structure in 6 parts: a concrete, dated
hook; a silent gag of 2 to 3 s; the diagnosis with 3 concrete pains; the pivot on black; the solution and its
benefits; the brand and the call to action. Short sentences, one idea each, 170 to 180 words per minute of speech.
The user chooses and corrects word by word. Rules and examples: `references/method.md` § 1.

### 2. Voice (the user generates it, gate)

1. Give the user the text to paste and the settings: Eleven v4, no pause tag (punctuation, `...`, line breaks), few
   acting tags, numbers in letters, the language set explicitly, Stability 40 to 50 %, Similarity 80 to 90 %, 2 or 3
   takes. Wait for `<project>/assets/audio/voix.mp3`. With the ElevenLabs connector attached and the user's go for the
   credits, generate the 2 takes yourself (`creative_generate_speech`, the voice of the brief) and download them.
   `references/voice-elevenlabs.md`.
2. Montage: `python3 .claude/skills/motion-design/scripts/onsets.py <project>/assets/audio/voix.mp3 --no-whisper`
   prints the cut points; make room for the silent gag and the pivot, cutting only in silences (5 ms fades): set
   `CUTS`, `TAIL`, `TOTAL` in `<project>/build-audio.sh`, then `MUSIC= bash <project>/build-audio.sh`.
3. Word timings: `python3 .claude/skills/motion-design/scripts/mots.py <project>/assets/audio/voix-montage.wav`
   writes `voix-montage-mots.json` and lists the silences over 0.4 s (each one becomes a shot with its own action).
   Then snap the phrase starts onto the real sound:
   `python3 .claude/skills/motion-design/scripts/onsets.py <project>/assets/audio/voix-montage.wav --transcript <project>/assets/audio/voix-montage-mots.json --out <project>/onsets.json`.
   From now on every cue comes from `onsets.json` (`--transcript <project>/onsets.json --window START END` for
   frame-local cues). `references/method.md` § 4.

Gate: the user validates the take and the montage (listen to the gag and the pivot).

### 3. Storyboard (gate)

1. **Three directions.** Read `patterns/STORYBOARD-CRAFT.md` (the 10 laws and the retained settings) and
   `patterns/PATTERNS.md`. Fill `<project>/DIRECTIONS.md`: 3 truly different directions for the same voice, each with a
   concept (the place the camera travels through), the thread of bridge objects and 3 styleframes (a frozen image of
   the future film at final quality, real interfaces). One standalone 1920x1080 HTML page per styleframe in
   `<project>/styleframes/`, then `python3 .claude/skills/motion-design/scripts/render-styleframes.py <project>`.
   Show the 9 PNGs direction by direction and **wait for the choice**.
2. **The frame spec** `<project>/frame.md` for that direction: palette as roles (one accent), fonts, the subtitle and
   its two highlights (key-word box, peak stroke), the geometry of the world with the coordinates of its stations, the
   reference framings (the camera state that isolates each subject), the camera kit, the real interfaces (from recent
   screenshots, never from memory). A complex world is written once in `<project>/reference/<world>.html`, the single
   source every frame copies verbatim (like `examples/ligne-du-temps-v8/reference/frise.html`).
   `grep -n "{{" <project>/frame.md` must print nothing.
3. **The storyboard** `<project>/STORYBOARD.md`, shot by shot on the word timings: the film header (world, signatures,
   camera score, voice silences, cuts, rhythm, sound), then per sequence: scene, duration, `handoff_in`,
   `handoff_out` (written twice, word for word, between N and N+1: every seam falls at the top of a camera move's
   blur), word cues; per shot: screen text with its `[boîte : …]` and `[trait : …]`, timed steps about every 0.5 s,
   camera track, layers and depth, bridge object, sound, key image. Format: `templates/STORYBOARD-TEMPLATE.md`.
4. **Checks**: the 15-point grid of `patterns/STORYBOARD-CRAFT.md` § 5, the control grid and the house rules below,
   verdicts in `<project>/STORYBOARD-CHECK.md`; the sum of durations and the handoffs with the script of
   `references/method.md` § 6.

Show the sequence list (title, duration, what we see, the key image of each shot) and wait for the go. Nothing is
animated before it. `references/method.md` § 5 and § 6.

### 4. Animation (pilot gate)

1. **Packets**: `node .claude/skills/product-launch-video/scripts/frame-packets.mjs --project <project> --storyboard <project>/STORYBOARD.md`
   (each under 48 KB: 1 or 2 rules per frame).
2. **Pilot**: frame 1 alone, then `python3 .claude/skills/motion-design/scripts/lint-frames.py <project>` and
   `python3 .claude/skills/motion-design/scripts/snapshots-lots.py <project> --at <8 to 11 times in frame 1>`, send the
   sheet, lock the look. The pilot frame becomes the reference implementation the other workers read.
3. **One sub-agent per sequence**, in the background, with the dispatch template below and the budget of
   `references/worker-dispatch.md` (medium effort, one self-check, short report, no reviewers): the frames that
   introduce a recurring object first, then the others. Done = the file exists on disk; then `lint-frames.py`.
4. **Shared decor**: sequences that show the same place share the SAME build function, copied verbatim from
   `reference/<world>.html`; check it with a diff before assembling (`references/method.md` § 8).
5. **Fixes**: resume the worker that built the frame (SendMessage with the finding) rather than dispatching a new one;
   make one-line fixes yourself.
6. **Assembly**: fill the settings of `<project>/assemble.sh` and run it (HeyGen assembler, transitions, audio at the
   root, paper bed, light flash, iris, lint), then `cd <project> && npx hyperframes validate`.
   `references/orchestrator-layer.md`, `references/worker-dispatch.md`.

After a session cut: `python3 .claude/skills/motion-design/scripts/check-frames.py <project>` and re-dispatch only the
frames that are MISSING or BROKEN (`references/variants.md` § Resume).

### 5. Music and sound effects (gate: the user chooses by ear)

- **Sound effects locked on the picture** in `<project>/assets/audio/sfx-events.json` (format:
  `templates/sfx-events.json`, names from `.claude/skills/media-use/audio/assets/sfx/` or from
  `<project>/assets/audio/sfx/`): clicks, pops, impacts, and ONE signature sound (a two-tone notification) on the key
  moment; about one sound per second, at most 7 whooshes and 1 sparkle. Real sounds on the hero gestures (a bounce, a
  dunk, a stamp) generated with the ElevenLabs connector on the user's go. The picture never moves for the sound.
- **Music**, in this order of preference: the CC0 tracks the user provides in `<project>/assets/music/` (sources:
  `references/music.md`); otherwise the score composed on the edit by
  `python3 .claude/skills/motion-design/scripts/musique-film.py <project>/assets/audio/musique.json` (sections on the
  acts and cuts of the storyboard); ElevenLabs Music only on the user's explicit go (credits). Whatever the source: a
  tension part up to the pivot, a cut on it, the élan back with its drop on the light or the payoff, an end on the end
  card, ducked under the voice (sidechain in `build-audio.sh`) and loud enough in the silences to carry the film;
  `loudnorm` to -16 LUFS and -1.5 dBTP.
- **Level**: the tension 2 to 3 dB under the élan at most, taken from a full section of its track (the script
  measures it in LUFS). Lower, the start of the film feels soft.
- **3 or 4 options** on the same edit:
  `python3 .claude/skills/motion-design/scripts/analyze-music.py <project>/assets/music/*.mp3 --drop-at <light time>`,
  then `python3 <project>/build-music-options.py` and `MIX=mix-M1.wav bash <project>/assemble.sh`. Reference mix:
  `examples/ligne-du-temps-v8/build-audio-v8.py`. `references/music.md`.

## Then: checks, delivery, distribution

6. **Checks before the render.** `lint-frames.py` and the lint of `assemble.sh` clean,
   `cd <project> && npx hyperframes check`, then
   `python3 .claude/skills/motion-design/scripts/snapshots-lots.py <project> --at <every key image, and each seam -0.04 and +0.04>`
   (the whole film at once times out past 8 or 9 frames) and read the sheet in `<project>/planches/`: every key image, the image before and after every seam (same
   camera, same objects, same blur, nothing doubled, nothing missing), the subtitle band free, no element cut at the
   edge, balanced margins. Re-dispatch the frame concerned with the finding. `references/method.md` § 11.
7. **Render and real control.** A draft render first
   (`cd <project> && npx hyperframes render --quality draft --output renders/draft.mp4`), then
   `cd <project> && npx hyperframes render --quality high --output renders/video.mp4`, then
   `bash .claude/skills/motion-design/scripts/contact-sheets.sh <project>/renders/video.mp4` (black segments, sheets
   every 0.25 s), one strip per seam, `freezedetect` (no unwanted hold), `ffmpeg -v error` (no decoding error), the mix
   at -16 LUFS and under -1.5 dBTP, and the duration of the render equal to the voice montage with both a video and an
   audio stream (`references/method.md` § 12). Never say it is done before this control.
8. **Delivery (gate).** The MP4 path per music option (other options without a new render:
   `python3 <project>/build-music-options.py --mux <project>/renders/video.mp4`), its duration, the contact sheets, the
   frame ids for targeted revisions. Close any player window on a file before rewriting it. At every piece of
   feedback: fix the film, write the rule in `<project>/frame.md`, and when it is general, in the house rules of this
   skill (rewrite the rule in place, never two versions side by side).
9. **Distribution, only when the user asks.** For a website: web encode, poster, muted autoplay, framed player,
   optional silent loop (`references/landing-integration.md`, `templates/LaunchFilm.tsx`). Nothing leaves the machine
   without the user's explicit request (`AGENTS.md`).
10. **Options, when asked for "better" or "other versions".** Same voice, same timings: a polished version, a restyle
    that keeps the choreography, a new direction; recurring objects built first. `references/variants.md`.

## House rules (from the feedback on the reference film)

- **Subtitles** at the bottom center (band y 890 to 980, 60 to 64 px, 45 characters at most per chunk), word by word
  on the voice. Never at the top left. Nothing else in that band.
- **Key words** of the subtitles in a small box in the accent color of the brand (never a black box).
- **Peaks**: a thin stroke or a tapered brush stroke under THE key word, never a big box nor a giant word.
- **One thing to look at at a time**: the camera isolates the subject of the sentence and shows the whole only when
  it makes sense.
- **Camera**: never a back-and-forth on the decor; a clear zoom in one direction is welcome. Every shot continues the
  move of the previous one (handoff), and one transition is one gesture readable in a second.
- **Side-by-side layouts** with equal left and right margins (the tasks on the left, the AI on the right).
- **Zero decor without meaning**: no grey bars "to fill", no abstract symbol, no counter that says nothing. Every image
  illustrates its sentence literally.
- **No line crossing a sentence**: a line of the decor folds away before a typographic moment.
- **Real, recent interfaces** (ask for recent screenshots: from memory you draw last year's app), uncluttered, placed
  where they make sense: a change request is an annotation linked to the element, not a bubble dropped on it.
- **Cursor**: it arrives in one move and clicks directly, no hesitation.
- **Rhythm**: something new every 0.5 to 1 s; two speeds (slow drift, fast notches); elements arrive too big and
  blurred, then settle.
- **Music level**: the tension 2 to 3 dB under the élan, taken from a full section of its track.
- **Script**: the offer is not detailed in the film (the page does it); the pains are concrete; the solution says
  who does the work ("l'IA le fait").
- **Costs**: resume existing agents, make small fixes yourself; any paid generation in series starts with 1 or 2
  tries; report the credits spent.
- **The pain never shows the client's own product**: a generic, unbranded one (a plain red jersey, not the club's
  jersey with its crest), so that the defect is never attached to the brand.
- **Characters do the real gesture**: a player dribbles the ball while running before he dunks; a jersey never rises
  to the hoop alone. A character drawn once and approved by the user is copied exactly in every frame.
- **The brand is fixed at the brief**: its exact name in the voice and on screen, its logo file, its URL. A change
  after the montage costs a voice patch, new cues and every visible mention (`references/voice-elevenlabs.md`).
- **Anonymize real documents**: a redrawn interface carries only the names the user allows (no address, person,
  price or quantity); raw screenshots stay out of the repository.
- **Sound density**: dense, but at most 7 whooshes and 1 sparkle in the film, nothing on the letters of a logo; the
  music follows the cuts (a calm loop reads as boring).

## Control grid (storyboard, then render)

From `patterns/PATTERNS.md` and the house rules above. The storyboard also passes the 15 points of
`patterns/STORYBOARD-CRAFT.md` § 5 (events, camera, bridge objects, depth, voice sync, ending).

- [ ] The first image is the first word or what it names, never the logo; the first word names the target or their pain.
- [ ] Every sentence of the voice has its composition; the subtitle arrives word by word at the bottom center.
- [ ] One key word per sentence in the accent box; one accent color per role; 3 or 4 peaks underlined, no giant word.
- [ ] One thing to look at at a time; side-by-side layouts with equal margins; no decor without meaning.
- [ ] The pain is shown in a tool the target recognizes.
- [ ] An explicit pivot (a sentence on black, a silence) before the brand, and the ground changes with it.
- [ ] The full logo does not arrive before 5 s (unless it is an object of the story that transforms at once).
- [ ] Hard cuts at the quota of the voice (narrative: 0 to 4, at act changes); 0 to 2 fades; everything else chains
      through objects or the camera, every seam matches its handoff, and the camera never goes back and forth.
- [ ] Every number rolls to its value or rushes in from the camera; none is faded in.
- [ ] The product is shown by gestures (type, tick, click) in its real, recent interface, not by a static screenshot.
- [ ] An element of the hook comes back before the end.
- [ ] End card: one button, a cursor that arrives and clicks directly, 2 to 3 s of living hold, then iris or black.
- [ ] Readable without sound from start to end.
- [ ] Something new every 0.5 to 1 s, no frozen hold, never the same layout for more than 3 s.
- [ ] Render: no `letterSpacing` tween; a paper bed under the light world; no black segment; no element shown outside
      its frame; the tension music 2 to 3 dB under the élan.

## Dispatch template (one per frame, absolute paths)

```
You build ONE frame of a HyperFrames motion design. You do not see my conversation: these files are your whole world.

Read first, in this order, and follow them as your role:
1. <PROJECT_DIR>/.hyperframes/frame-packets/_role.md (worker contract)
2. <PROJECT_DIR>/.hyperframes/frame-packets/<frame_id>.md (your storyboard block, blueprint and motion rules)
3. <PROJECT_DIR>/frame.md (colors, fonts, components, world: the only style source)

## Dispatch context
- PROJECT_DIR: <PROJECT_DIR>
- frame_id: <frame_id>
- output: <PROJECT_DIR>/compositions/frames/<frame_id>.html (the only file you write)
- canvas: 1920x1080, 30 fps; frame duration: <D> s; world: <dark|light>
- confirmed sketch: none
- captions: disabled
- <frame-specific lines: shared world to copy, flash point, iris hold, retry findings (see worker-dispatch.md)>

## House rules of this repository (they override the contract where they differ)
- Captions are disabled: the narration IS the on-screen text. Show each sentence as the subtitle of frame.md, at the
  bottom center (band y 890 to 980, nothing else in it), word by word, exactly as the Scene lines quote it, with the
  named [boîte : ...] (key-word box) and [trait : ...] (peak stroke). A typographic moment named in the Scene lines
  centers the sentence instead (84 px at most). No giant word, no big box.
- Word cues are frame-local seconds: each word appears on its cue (0 to 2 frames early), never late.
- One thing to look at at a time: follow the camera track, which isolates the subject of each sentence; never a
  camera back-and-forth; equal side margins; no decor that the Scene lines do not name; no line crossing a sentence.
- The cursor arrives in one curved move and clicks directly, never a hesitation.
- BLOCKING. A frame is not masked before its start: every element not on screen at t=0 starts with `opacity: 0` in
  CSS, and every `fromTo` that starts after t=0 has `immediateRender: false`.
- BLOCKING. handoff_in and handoff_out are binding: your first image is exactly handoff_in, your last image is exactly
  handoff_out; no element is born or dies in the 2 images around a seam.
- BLOCKING. An inner `<template id="...">` goes INSIDE the root element of the frame (`<div id="root">`), never beside
  it: the engine only embeds the root, and the frame renders black.
- BLOCKING. Never set `style.visibility = "visible"`: use `"inherit"`, otherwise the element shows over the whole film.
- BLOCKING. Tween transforms only (x, y, scale, rotation, opacity, filter): never top, left, width, height or
  letterSpacing (split a word into letters and tween their x). No backdrop-filter. No interpolated clip-path polygon
  (circle, ellipse and inset are fine). Every id starts with a letter and carries the prefix of this frame. No giant
  blurred 3D layer (a floor is a canvas, no blurred object over 1800 px).
- When frame.md points to reference/<world>.html, copy its CSS, templates, camera kit and decor function verbatim
  (only `../assets/` becomes `assets/`): the decor must be byte for byte the same as in the other frames.
- Follow the steps of the Scene lines at their times (an event every 0.5 s, the camera track apart from the object
  tweens, no frozen hold). power3.out / expo.out, no bounce, exits faster than entries.
- Write a complete first version of your file early (every scene roughed in, timeline registered), then refine it: a
  session cut must not leave a half-written file. Check your key images before you answer.
- No `repeat: -1` and no CSS animation: a loop (the living layer of a hold) repeats a finite number of times computed
  from the frame duration. No `Math.random`.
- Fonts, images and icons from `assets/...` (project-root relative), never from the network. No `<audio>`.
- Only the copy quoted in the Scene lines appears on screen, in the language and typography of the voice.
- Tween proxies, not colors: subtitle words fade by opacity (0, 0.35, 1), SVG strokes are drawn through the kit's
  draw function, no negative z-index (a shadow goes in a drop-shadow filter). Every `var` name is declared once in the
  frame (two declarations silently overwrite each other).
- GSAP and every asset load from the project (`assets/vendor/gsap-3.14.2.min.js`, `assets/...`): the network is
  blocked. Thread progress values are measured on the real path, never taken from the storyboard's numbers.
- Budget: write the file in one or two passes; one self-check only (headless mount, no page error, at most 3
  screenshots in one sheet), then stop. Report in 8 lines at most: what you built, each deviation and its reason, the
  state of your first and last images.
- Do not run any `npx hyperframes` command, do not edit any other file. Writing your file is your last action.
```

## References

| File | When |
|---|---|
| `references/method.md` | the detail and the exact commands of every step |
| `examples/ligne-du-temps-v8/` (repository root) | the reference film: frame spec, storyboard, world code, the 9 frames, assembly and mix |
| `patterns/STORYBOARD-CRAFT.md` (repository root) | step 3: the 10 laws of an agency storyboard, the retained settings, the format, the 15-point grid |
| `templates/DIRECTIONS-TEMPLATE.md`, `templates/STORYBOARD-TEMPLATE.md` (repository root) | step 3: the three directions, the film header and the sequence block with a filled example |
| `examples/C-le-devis-v7a/` (repository root) | a storyboard step in full: directions, frame spec, storyboard, checked grid, executable world reference |
| `references/voice-elevenlabs.md` | step 2 |
| `references/worker-dispatch.md` | step 4 |
| `references/orchestrator-layer.md` | step 4 (assembly) |
| `references/music.md` | step 5: pick, sync, level and mix the music options, commercial-safe CC0 sources |
| `references/landing-integration.md` | distribution: put the film on a website |
| `references/variants.md` | options, and to resume after a session cut |
| `references/pitfalls.md` | before steps 3 and 4, and whenever something looks wrong |
| `patterns/PATTERNS.md` (repository root) | steps 1 and 3 (choose patterns), checks (control) |
| `templates/` | `BRIEF.md`, `frame.md`, `STORYBOARD.md`, `assemble.sh`, `build-audio.sh`, `sfx-events.json`, `musique.json`, `build-music-options.py`, `LaunchFilm.tsx` |
| `scripts/` | `new-project.sh` (project folder, GSAP vendored, fonts from npm), `mots.py` (word timings), `onsets.py` (cut points, onsets), `render-styleframes.py` (styleframes to PNG), `optimise-images.py` (heavy images), `lint-frames.py` (static faults of the frames), `snapshots-lots.py` (key images of the whole film in batches, labelled sheet), `patch-voix.py` (lay a re-recorded sentence over its slot), `musique-film.py` (score composed on the edit), `analyze-music.py` (tempo, drops, sync), `contact-sheets.sh` (render control), `check-frames.py` (resume), `waveform.py` (real voice envelope) |
| `ifs-maillot-club/` (repository root) | the second reference film: cloud session, ElevenLabs connector, composed score, voice patch, pilot frame to imitate |
| `.claude/skills/hyperframes-animation/blueprints-index.md`, `rules-index.md` | step 3: shot shapes and motion recipes |
