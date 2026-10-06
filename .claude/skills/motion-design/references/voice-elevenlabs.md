# Voice with ElevenLabs (Eleven v4)

The voice is the clock of the whole film: every reveal is cued on it. It is made by the user in the ElevenLabs web app
(https://elevenlabs.io), no API key, nothing to install. The agent prepares the text and explains the settings.

## Prepare the text (agent)

The validated script lives in `<project>/SCRIPT.md` in two forms: the **staged version** (the text with its staging:
the silent gag, the pivot on black, what the screen shows) and the **version to paste** in ElevenLabs, which carries no
staging at all (the voice reads everything it is given). Rules for the version to paste, with Eleven v4:

- **No pause tags**: v4 has none. Pauses come from punctuation (full stops, commas, `...`) and line breaks, one
  sentence per line. Long silences (the silent gag, the pivot) are made at the montage, never in the text.
- **Few acting tags**, in square brackets (`[sighs]`, `[dry amusement]`, `[lower, slower]`): one or two per film.
  More makes the voice unstable.
- **Numbers in letters** for the voice ("mille euros", "deux point zéro"); the screen keeps "1 000 €", "2.0".
- **Words written as they are**: v4 does not understand phonetic spelling. Write "l'IA", not `/li.a/`.
- A sentence that ends on a past participle ("lancées") can be read as an imperative: turn it another way.

Example (the flagship film, `examples/ligne-du-temps-v8/`):

```
Lundi, tu demandes une modif sur ton site.
Mercredi, le devis tombe : mille euros.
Vendredi... toujours rien.
```

## Generate (user)

1. ElevenLabs, Text to Speech, model **Eleven v4**.
2. Pick a voice from the library that fits the brand (the flagship film uses « Paul K, French Ad & Trailer Voice »).
3. Settings: Stability **40 to 50 %**, Similarity **80 to 90 %**, and the **language set explicitly** (for French: if it
   is left on automatic, the accent can drift, often to Canadian French).
4. Paste the whole text in one go (the intonation carries from one sentence to the next).
5. Generate **2 or 3 takes**, listen, keep the best one. Download it as MP3 (or WAV) and drop it as
   `<project>/assets/audio/voix.mp3`.

A paid plan is required for commercial use of the audio. Recording your own voice works the same way (quiet room,
phone close to the mouth, export MP3): the rest of the method does not change.

## Generate with the ElevenLabs connector (when it is attached)

When the session has the ElevenLabs connector, you can generate the takes yourself, with the user's go for the
credits (about 40 credits per short sentence, 70 for a long one, per variation). Never an API key.

1. `creative_generate_speech`: `model_id: "eleven_v4"`, the `voice_id` of the brief (default Paul K,
   `ecxPjiGTvAfpGEams6ec`), the whole text in `prompt`, `generations_count: 2`, and the `flow_id` of the film once one
   exists (all the film's generations on one canvas).
2. Poll `creative_get_flow_run_status` with the `session_ids` until `all_completed`; each generation has a signed
   `content_url` (valid 2 h): download it with `curl -sS -o <project>/assets/audio/<name>.mp3 "<url>"`.
3. A `429 rate_limited` means too many generations at once: nothing started, nothing is charged. Wait for the running
   ones to finish, then send it again. Never resend a call that did start (it charges a second generation).
4. Sound effects go the same way: `creative_generate_in_flow`, `node_type: "sfx"`, `model_id:
   "eleven_text_to_sound_v2"`, a precise English prompt ("single basketball bounce on an indoor hardwood floor, close
   mic, one bounce only"), 2 variations, then `curl` into `<project>/assets/audio/sfx/<name>.mp3`.

## After the voice

- **Montage, never regeneration, for the silences**: the silent gag (2 to 3 s), the pivot (about 1.5 s of silence),
  a breath before the end card and a tail of about 4 s. Cut only in the middle of a silence (`onsets.py --no-whisper`
  prints the cut points), 5 ms fades on every join (`build-audio.sh`, `CUTS`).
- **One wrong word in the best take** (v4 once read "l'IA" as "Lydia"), **or a brand name that changes after the
  montage** (IFS became Contino Sport on a finished film): regenerate that sentence alone with the same voice and model,
  then lay it over its slot without touching the rest of the montage: write `<project>/assets/audio/patch-voix.json`
  (`scripts/patch-voix.py` documents the format: the take, its slot, an optional pause to shorten) and rerun
  `build-audio.sh`, which applies it after every montage. The old sentence is muted from 0.45 s before its slot (with
  0.12 s, the attack of the old "IFS" stayed audible as a stray "i"). Then redo the word timings (`mots.py`) and
  update the word cues of the frames concerned, and every visible mention of the old word (logo, interface, URL).
