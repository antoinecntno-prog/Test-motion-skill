# One sub-agent per frame

The orchestrator (you) never writes the frames of a film itself: each frame is built by its own sub-agent, in
parallel, from a bounded packet. It keeps your context clean and every frame gets a full, focused worker.

## Before dispatch

1. `STORYBOARD.md` approved, `frame.md` without placeholders, fonts and icons in `<project>/assets/`.
2. Packets built and under 48 KB each:
   `node .claude/skills/product-launch-video/scripts/frame-packets.mjs --project <project> --storyboard <project>/STORYBOARD.md`
3. Read `.claude/skills/hyperframes/references/subagent-dispatch.md` once (harness mapping, waves, waiting rule).

## The prompt

Use the template of SKILL.md (step 8) word for word, with absolute paths. It hands the worker exactly three documents:
`_role.md` (HeyGen's shared worker contract + the product-launch delta), its own packet (storyboard block, blueprint,
motion rules inlined) and `frame.md`, plus the dispatch context and the house rules of this repository. The worker never
sees the conversation, `STORYBOARD.md` or the skills: if something matters, it is in the packet or in the prompt.

Frame-specific lines to add to the dispatch context when they apply:

- **Last dark frame (before the flash)**: "End on a bright point at (LEAK_X, LEAK_Y) from <time>; the orchestrator
  floods the light from that exact point at <LEAK_AT + 0.03 - frame start> s."
- **Frame under the iris**: "The orchestrator keeps this frame mounted until <IRIS_AT + 0.80 - frame start> s: every
  internal clip and the ground must last until then. End on <object> at (IRIS_X, IRIS_Y)."
- **Handoffs**: every frame of the storyboard carries `handoff_in` / `handoff_out` (camera state, blur, world state,
  objects, light, text at the seam); they are binding for both workers: the first image of the frame is exactly its
  `handoff_in`, the last one exactly its `handoff_out`.
- **Shared world**: when `frame.md` points to an executable reference (`reference/<world>.html`), add "Copy the CSS,
  the template, the camera kit and the decor build function of reference/<world>.html verbatim (only `../assets/`
  becomes `assets/`, and the template ids take the prefix of this frame)". Frames that share a decor share the SAME
  function: check it with the diff of `method.md` § 8 once the files exist.
- **Retry**: resume the worker that built the frame (SendMessage) with the lint or check findings that name it,
  verbatim, rather than dispatching a new one; it keeps its context and costs less. A new worker only if the first one
  is gone.

## Pilot, then parallel

1. **Pilot**: dispatch frame 1 alone, in the background. When its file exists, run
   `python3 .claude/skills/motion-design/scripts/lint-frames.py <project> <frame_id>`, then
   `python3 .claude/skills/motion-design/scripts/snapshots-lots.py <project> --at <8 to 11 moments of frame 1>` and
   send the user the sheet it writes in `<project>/planches/`. Fix the look now (in `frame.md` if it is a style issue,
   then resume the pilot worker) before building the rest. The pilot frame becomes the reference implementation the
   other workers read (structure, kit inside the IIFE, proxies and one `render()`, subtitles, depth).
2. **Parallel**: dispatch every remaining frame at once, one worker each, in the background (in waves if the harness caps concurrency:
   never merge two frames into one worker). A worker takes 8 to 30 minutes.
3. **Wait on the files**: a frame is done when `<project>/compositions/frames/<frame_id>.html` exists and is a single
   `<template>...</template>`. A missing file after the worker returned: re-dispatch once with the same prompt.
4. `lint-frames.py <project>` (static faults HyperFrames does not see: network URL, a `var` declared twice, a color
   tween, a kit that differs from the reference), then assemble (`bash <project>/assemble.sh`): it marks the built
   frames `animated`, rebuilds the index and lints.
   For every lint or check error, re-dispatch the frame concerned with the finding (or make the smallest fix yourself
   when it is one line).

## Budget (measured on the Contino Sport film, Pro plan)

A worker that loops on screenshots costs 200 000 to 270 000 tokens; two of them ran for 18 minutes on two frames and
the user saw 40 % of the session quota gone. What keeps a film within one session:

- **Workers at medium effort** (`effort: "medium"` in a Workflow, or say it in the prompt), one self-check only: mount
  the frame headless, no page error, at most 3 screenshots (first image, key image, last image) in ONE sheet, fix the
  clear defects, stop. A report of 8 lines at most.
- **No reviewer agents.** The orchestrator reviews with `lint-frames.py` and one sheet of `snapshots-lots.py` per
  half film, then makes the one-line fixes itself and resumes a worker only for a real rework.
- **The harness runs about 2 workers at a time** (it caps concurrency on the CPUs): 10 frames take 4 to 5 rounds.
  Dispatch the frames that introduce a recurring object first.
- **A session limit kills workers mid-run**: the file written early survives. After the reset, `check-frames.py` and
  re-dispatch only the missing frames (a new script with only those ids; do not resume a run whose agents failed).
- **Images**: shrink them before dispatch (`optimise-images.py`), every worker inlines them.

## What workers must never do

Run `npx hyperframes` (any command), edit `STORYBOARD.md`, `frame.md`, `index.html` or another frame, add `<audio>`,
load a font or a script from the network, invent visible copy that the Scene lines do not quote, put an inner
`<template id>` outside the root element of the frame, or set `style.visibility = "visible"` (always `"inherit"`).
Every worker writes a complete first version of its file early, then refines it: a session cut must leave a usable
file, not half of one.
