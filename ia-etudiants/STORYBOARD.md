---
format: 1920x1080
duration: "50.80s"
message: "Formés à apprendre avec l'IA (questionner, vérifier, contredire, créer), vos étudiants retrouvent la curiosité et le cours redevient le leur."
arc: Hook → Problem → Pivot → Turn → Demo → Payoff → Reassurance → CTA
audience: "directions d'établissement, responsables pédagogiques et enseignants, sur la page LinkedIn d'Antoine Contino, formateur IA"
mode: autonomous
captions: disabled
music: "pre-mixed with voice and SFX in assets/audio/mix.wav (mounted at root by the orchestrator)"
direction: "A « Le carnet » (DIRECTIONS.md), retenue par Antoine le 7 octobre 2026, sans emprunt"
styleframes: "styleframes/png/A1.png (0.9 s), styleframes/png/A2.png (16.5 s), styleframes/png/A3.png (36.8 s)"
patterns: ../patterns/STORYBOARD-CRAFT.md, ../patterns/PATTERNS.md
---

## Video direction

- **Un seul monde** (frame.md) : un carnet de croquis de huit pages posé sur un bureau, que la caméra parcourt de gauche à droite, une page par idée. Séquences 1 à 4 = DOULEUR sur les pages P1 à P3 lavées de gris ; séquence 5 = PIVOT dans le noir de la goutte d'encre ; séquences 6 à 10 = SOLUTION sur les pages P4 à P7 qui se colorent ; séquences 11 et 12 = FIN sur la page P8. Chaque séquence peint son propre fond (bureau paper-dark + pages) sur un calque `class="clip"` de toute sa durée.
- **Coutures invisibles** : toutes les séquences entrent en `cut` ; chaque couture tombe au sommet du flou d'un mouvement de caméra (whip, cran, plongée, recul) ou dans le mouvement du curseur, et le `handoff_out` de la séquence N est recopié mot pour mot dans le `handoff_in` de N+1. Exception voulue : 23.30, coupe franche à l'impact de la goutte ocre (le cadre entier est le lavis ocre des deux côtés) : du noir du pivot au papier de la classe.
- **Texte** (lisible sans le son) : chaque phrase de la voix est un sous-titre `.aq-sub` en bas au centre (bande y 890 à 980, rien d'autre dedans), mot par mot sur les temps de chaque séquence (`mot@secondes`, temps locaux), 45 signes au plus par morceau. Un seul mot ou groupe par phrase dans la boîte bordeaux ([boîte : …]). Aucun autre texte coloré. Un seul moment typographique : « Et si l'IA servait à apprendre ? » au pivot, centré sur le noir, 84 px, sans sous-titre pendant ce temps.
- **Pics** : 4 traits de pinceau ocre [trait : …] : « curiosité » (16.14), « apprendre » (21.20), « revient » (37.52), « le leur » (42.50).
- **Une seule chose à regarder** : chaque plan isole le sujet de la phrase ; la caméra va de gauche à droite dans le carnet ou s'enfonce (écran, goutte, bouton), jamais d'aller-retour ; marges gauche et droite égales ; aucun décor sans sens ; la reliure et les lignes des pages restent au-dessus de y 880 et ne traversent jamais une phrase.
- **Vraies interfaces** : aucune (BRIEF.md) : la fenêtre de chat est générique et dessinée à l'encre (frame.md, chat-window), sans nom d'outil ; aucune donnée réelle, aucun nom d'élève ni d'établissement.
- **Parallaxe** (une par acte au moins) : pendant chaque dérive, l'avant-plan flou (bord de la page suivante, goutte en vol, stylo) glisse 2,5 fois plus vite que la page, le bureau 0,4 fois.
- **Grammaire de mouvement** : deux vitesses, gestes de 1 à 6 images (expo.out) et dérives linéaires qui ne s'arrêtent jamais ; la zone 0,3 à 0,9 s est réservée à la caméra et au curseur (expo, power3, power4) ; les taches naissent d'une goutte ou d'un coup de pinceau et sèchent, jamais en fondu ; aucune tenue figée ; aucune transition « effet ».
- **Texte visible** : exactement le texte cité dans les lignes Scene et les composants de frame.md, rien d'autre.
- **Négatifs** : diaporama (tout à t = 0), écran de veille, tache dédoublée, texte coloré à la place de la boîte, grande phrase, mot géant, titre qui répète la voix, symbole abstrait, curseur qui hésite, plusieurs objets qui bougent pendant une couture, outil d'IA nommé, note ou chiffre réel hors le « 12 » du récit.

**MONDE**
- Carnet (14 700 × 1 080 u, frame.md § world) sur le bureau paper-dark grainé : P1 (850, 540) le bureau de l'étudiant la nuit · P2 (2584, 540) le bureau du prof · P3 (4318, 540) la page de la leçon · P4 (6052, 540) la classe · P5 (7786, 540) l'écran · P6 (9520, 540) le défi · P7 (11254, 540) le carnet des réflexes et les mains · P8 (12988, 540) la signature et le bouton. Reliures à x = 1700 + (k - 1) × 1734.
- Pivot (19.22 à 23.30) : l'intérieur de la goutte d'encre, ground-ink (canvas, ondes sombres qui s'élargissent), la question centrée.
- Couleurs de rôle : accent bordeaux = boîte du mot clé, goutte signature, note « 12 » avant séchage, stylo rouge, signature finale, équipe bordeaux ; ocre = la couleur qui revient (4 traits, lampe allumée, tables, équipe ocre, bulle nette, bouton) ; gris de lavis = la douleur (eau sale, copie, note séchée, lampe éteinte) ; brun = bureau et tables ; encre = traits et texte.

**SIGNATURES**
- Mécanisme 1 « la goutte » (frame.md, drop : elle tombe, s'ouvre en tache, sèche en objet) : 0.02 goutte accent au pied du portable de P1, sa traînée allume l'écran · 4.86 goutte grise sur P2 qui sèche en trois pages · 13.39 goutte accent dans le cadre de la note, « 12 » · 18.77 la caméra plonge dans la goutte du bas de P3 (noir) · 23.23 goutte ocre sur le noir qui ouvre P4 · 26.60, 27.80, 28.90, 30.20 quatre gouttes sur l'écran (question, coche, barre, croquis) · 33.64 goutte accent-pale qui bave (« invente ») · 34.96 deux gouttes qui deviennent deux équipes · 43.50 goutte accent qui trace la signature · 45.90 goutte ocre qui sèche en bouton (12 occurrences).
- Mécanisme 2 « le séchage » (aqDry : l'anneau de bord fonce, la granulation paraît, l'objet dedans devient net ; inverse aqErase : la couleur pâlit puis la tache s'efface par le centre) : 1.60 l'écran · 5.90 la copie · 10.82 lampe éteinte (inverse) · 12.30 la leçon pâlit (inverse) · 13.90 la note sèche en gris · 16.14, 16.80, 17.78, 18.20, 18.88 cinq effacements · 23.60 les tables · 27.00, 28.10, 29.20, 30.60 les quatre gestes · 33.00 la bulle nette · 37.52 la page entière · 44.60 la signature · 46.40 le bouton (17 occurrences).
- Registres de texte : sous-titre mot à mot = gris flou → net (0,14 s) puis encre (0,2 s) ; boîte = tracée depuis la gauche (0,16 s power3.out) ; trait = pinceau depuis la gauche (0,4 s power2.out) ; moment typographique = lettres qui convergent (0,5 s expo.out) ; notes Caveat = révélées par un masque qui avance (vitesse d'une main, 0,3 à 1,0 s).
- Rimes : la goutte de la signature (43.50) rejoue la goutte de l'ouverture (0.02), même encre, même chute, même traînée ; la page du début revient colorée dans les mains (41.11) ; le bouton (45.90) est une goutte ocre séchée comme les tables (23.60) ; le curseur qui colle le sujet (2.90) revient cliquer le bouton (47.85).

**PARTITION CAMÉRA** (temps globaux) : 0.00 dérive sur la lampe de P1 · 0.90 cran vers le portable · 2.00 cran sur l'écran · 4.40 whip P1 → P2 (couture 4.64) · 4.86 atterrissage P2 · 7.34 poussée sur la copie et le stylo · 8.64 poussée courte sur la pointe du stylo · 9.66 whip P2 → P3 (couture 9.80) · 10.00 atterrissage P3 · 11.40 cran sur les lignes de la leçon · 12.80 cran sur le cadre de la note · 15.46 recul vers la double page (couture 15.67) · 15.90 atterrissage double page P2 + P3 · 18.77 plongée dans la goutte (couture 19.22) · 19.22 dérive d'échelle sur le noir · 21.70 recul lent sur le noir · 23.23 impact, coupe 23.30 · 23.30 le papier s'ouvre, dérive sur P4 · 25.80 whip P4 → écran de P5 (sommet 25.95) · 26.00 atterrissage écran · 27.45 cran vers la coche (couture 27.59) · 28.60 cran vers la barre · 29.90 cran vers le croquis · 31.25 cran vers le bas de la page (couture 31.41) · 31.60 atterrissage bulles · 34.30 whip P5 → P6 (couture 34.48) · 34.70 atterrissage P6 · 35.58 cran sur le chrono · 36.50 cran sur les colonnes · 38.00 whip P6 → P7 (couture 38.14) · 38.33 atterrissage carnet · 40.84 cran vers les mains · 43.10 whip P7 → P8 (couture 43.26) · 43.50 atterrissage signature · 45.90 cran vers le bouton · 47.60 couture dans le mouvement du curseur · 47.85 clic · 48.00 à 50.50 dérive lente · 50.50 noir.

**VOIX** : minutage dans onsets.json (DIRECTIONS.md). Silences de plus de 0,4 s, chacun écrit comme un plan : 1.61 à 2.11 (cran vers le portable, l'écran s'allume) · 4.43 à 4.86 (whip vers P2) · 7.29 à 10.01 (gag muet : le stylo rouge tourne deux pages, rien à annoter, se pose ; whip) · 15.46 à 15.88 (recul vers la double page) · 18.97 à 19.47 (plongée dans la goutte, le noir) · 21.59 à 23.67 (le pivot : la question tient, la goutte ocre tombe, le papier s'ouvre) · 25.61 à 26.01 (whip vers l'écran) · 34.25 à 34.72 (whip vers le défi) · 42.94 à 43.58 (whip vers la signature, la goutte tombe) · 45.81 à 46.18 (cran vers le bouton, la tache ocre tombe) · 47.26 à 50.80 (clic, tenue vivante, noir).

**COUPES** (voix narrative, quota 0 à 4) : 23.30 · « Je » (23.67) · changement d'acte, du pivot à la solution, à l'impact de la goutte ocre (le cadre est le lavis ocre des deux côtés). Toutes les autres jonctions sont des coutures de caméra ou d'objet.

**RYTHME** : douleur (0 à 19.22) 12 plans = 6,2 plans / 10 s ; pivot 2 plans ; solution (23.30 à 43.26) 11 plans = 5,5 plans / 10 s ; fin (43.26 à 50.80) 3 plans = 4,0 plans / 10 s.

**SON** (proposition, verrouillée à l'étape 5 ; l'image ne bouge pas pour le son ; 7 whooshes, 1 scintillement) : goutte 0.02 · clavier court 2.60 (le sujet collé) · clic 2.90 · pinceau 3.30 (la réponse grise) · whoosh court 4.40 · papier 5.00, 5.40, 5.80 (les trois pages glissent) · papier 8.30, 8.90 (pages tournées) · stylo posé 9.50 · whoosh court 9.66 · clic d'interrupteur 10.82 (lampe) · pinceau 12.30 · goutte 13.39 (la note) · pinceau 16.14, 16.80, 17.78, 18.20, 18.88 (effacements) · whoosh cinématique 18.77 (plongée) · goutte grave 19.22 · goutte 23.23 et whoosh 23.30 (le papier s'ouvre) · pinceau 24.00 à 25.30 (les figures) · gouttes 26.60, 27.80, 28.90, 30.20 · pinceau 30.40 (le croquis) · pinceau 32.80 (bulle nette) · goutte 33.64 (bavure) · stylo 33.95 (correction) · whoosh court 34.30 · gouttes 34.96 (équipes) · tic-tac 35.84 à 37.90 · pops 36.80 à 37.90 (points) · scintillement 37.52 (« revient ») · whoosh court 38.00 · stylo 38.56 à 40.00 (réflexes cochés) · papier 40.40 (le carnet se referme) · pinceau 41.76 (la page se colore) · whoosh court 43.10 · goutte 43.50 · stylo 43.60 à 44.60 (signature) · goutte 45.90 (bouton) · clic 47.85.

## Frame 1 : Dimanche, le sujet collé · 0.00 → 4.64

- scene: Sur la page P1 du carnet, le bureau de l'étudiant la nuit : la lampe allumée, une goutte d'encre bordeaux tombe au coin de la page et sa traînée allume l'écran du portable ; la caméra s'approche de l'écran où le curseur colle le sujet dans une fenêtre de chat et où la réponse s'écrit en gris ; whip vers la page suivante
- duration: 4.64s
- transition_in: cut
- status: animated
- src: compositions/frames/01-dimanche.html
- voiceover: "Dimanche, vingt-trois heures. Votre étudiant colle le sujet dans une IA."
- type: hook
- blueprint: camera-journey (Adapt)
- focal: la goutte qui tombe au coin de la page, puis l'écran du portable et le sujet collé
- rules: depth-of-field-blur, coordinate-target-zoom
- world: light
- handoff_in: aucun (ouverture du film) ; première image = la page P1 au cadrage cam(430, 600, 1.6) flou 0 : la lampe à l'encre allumée (lavis ocre-2) à gauche, le bord du portable à droite, la nuit en lavis bordeaux pâle en haut, la note Caveat « dim. 23 h 04 », le bord flou de P2 coupé par le bord droit ; aucune goutte encore ; sous-titre vide
- handoff_out: à 4.64 : cam(1900, 560, 1.1) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet, pages P1 et P2 posées sur le bureau paper-dark ; P1 : lampe allumée (lavis ocre-2), portable avec la chat-window (sujet collé, réponse grise), goutte accent au pied du portable (1180, 740) et sa traînée ; P2 encore vide (bureau brun, lampe éteinte) ; aucune page grise à l'écran ; sous-titre sorti ; grain 55 %

Word cues: Dimanche@0.02 vingt-trois@0.74 heures@1.26 Votre@2.11 étudiant@2.42 colle@2.90 le@3.20 sujet@3.50 dans@3.72 une@4.00 IA@4.24

Scene 1 (0.00 à 0.90 s) : P1, la lampe, la goutte tombe
  TEXTE ÉCRAN : sous-titre « [boîte : Dimanche], vingt-trois heures. » (boîte tracée 0.00, Dimanche 0.02, vingt-trois 0.74, heures 1.26) ; écart synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 la lueur de la lampe respire (lavis ocre-2 ×1,03, 0,3 s sine.inOut) et la boîte se trace ; 0.02 la goutte accent arrive de la caméra (×4, flou 10 px, 0,16 s power2.in) vers le pied du portable (1180, 740) ; 0.18 impact : la tache s'ouvre ×0,2 → ×1 (0,12 s expo.out), deux éclaboussures de 6 u ; 0.30 la traînée accent-light se dessine de la goutte vers le bout du clavier (aqDrawPrep, 0,5 s power1.inOut) ; 0.50 la note « dim. 23 h 04 » se révèle (masque, 0,3 s) ; 0.74 « vingt-trois » ; 0.80 la lueur de l'écran commence à monter (lavis ocre-pale opacité 0 → 0,9 en 0,2 s, depuis le point où la traînée touche le clavier).
  PISTE CAMÉRA : dérive x +24 u/s, échelle +2 %/s de 0.00 à 0.90 ; 0.90 départ du cran vers le portable.
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P2 (7 px) coupé par le bord droit et la goutte en vol ; sujet la lampe et le pied du portable nets ; fond le bureau paper-dark grainé ; couches animées 3.
  OBJET-PONT ET VECTEUR : la traînée de la goutte mène la caméra au portable (le cran suit la traînée).
  SON : goutte à 0.02 ; pinceau à 0.30 (la traînée).
  IMAGE CLÉ : 0.20 : la lampe allumée à gauche, au pied du portable la goutte bordeaux qui vient de s'ouvrir, sa traînée qui part vers le clavier, « Dimanche » en boîte dans le sous-titre.

Scene 2 (0.90 à 2.00 s) : P2, cran vers le portable, l'écran s'allume
  TEXTE ÉCRAN : fin de « vingt-trois heures. » (heures 1.26) ; le sous-titre sort de 1.86 à 2.00 ; écart synchro.
  ÉTAPES : 0.90 cran vers cam(760, 575, 1.2) (0,14 s expo.inOut, flou 8 px au milieu) ; 1.04 la traînée atteint le clavier ; 1.10 l'écran s'allume : le lavis ocre-pale de l'écran sèche (aqDry 0 → 1, 0,5 s) et la chat-window se dessine dedans (cadre à l'encre tracé, 0,3 s power2.out) ; 1.26 « heures » ; 1.40 l'étiquette « NOUVELLE CONVERSATION » se révèle (masque 0,2 s) ; 1.60 le champ « Écrire un message » paraît (×1,1 flou 6 → net, 0,12 s) ; 1.70 le curseur entre par le bas droit (début de son mouvement courbe de 0,5 s power3.out vers le champ) ; 1.86 le sous-titre sort.
  PISTE CAMÉRA : 0.90 à 1.04 cran ; puis dérive x +18 u/s, échelle +1,5 %/s jusqu'à 2.00.
  COUCHES ET PROFONDEUR : avant-plan le pied de la lampe flou (10 px) coupé par le bord gauche ; sujet le portable net ; fond la nuit en lavis bordeaux pâle, floue ; couches animées 3 (caméra, écran, curseur).
  OBJET-PONT ET VECTEUR : l'écran qui s'allume devient le sujet du plan 3 ; le curseur en mouvement traverse la couture de plan.
  SON : (aucun : le silence 1.61 à 2.11 porte le cran et la lumière).
  IMAGE CLÉ : 1.50 : le portable au centre, son écran qui vient de sécher en fenêtre de chat vide, la traînée bordeaux qui arrive au clavier.

Scene 3 (2.00 à 4.64 s) : P3, l'écran : le sujet collé, la réponse grise, whip
  TEXTE ÉCRAN : sous-titre « Votre étudiant [boîte : colle] le sujet dans une IA. » (Votre 2.11, étudiant 2.42, boîte tracée 2.86, colle 2.90, le 3.20, sujet 3.50, dans 3.72, une 4.00, IA 4.24) ; il sort de 4.46 à 4.60 ; écart : l'image devance « colle » de 0,3 s (le collage à 2.60).
  IMAGE DE DÉPART : l'écran plein cadre au cadrage cam(760, 575, 1.55), la fenêtre de chat vide, le curseur en fin de course sur le champ.
  ÉTAPES : 2.00 cran sur l'écran vers cam(760, 575, 1.55) (0,12 s expo.inOut, flou 6 px) ; 2.20 le curseur touche le champ et presse (×0,85, 0,06 s) ; 2.26 le caret bordeaux clignote (pas finis 0,5 s) ; 2.40 le champ s'éclaire (ocre-pale à 20 %, 0,1 s) ; 2.60 le sujet se colle d'un bloc dans la bulle « VOUS » (×1,06 flou 4 → net, 0,08 s expo.out) : « Rédige une dissertation de trois pages sur les causes de la Première Guerre mondiale. » ; 2.90 clic sur le bouton rond accent (pression, onde) ; 3.00 la bulle « IA » naît d'une goutte grise (impact ×0,2 → 1, 0,12 s) ; 3.10 à 4.20 la réponse s'écrit en gris-lavis-2, ligne par ligne (4 lignes, 0,25 s chacune, chaque ligne se révèle par un masque) : « Voici une dissertation en trois parties. Introduction : au début du vingtième siècle, les tensions… » ; 3.50 « sujet » : la bulle « VOUS » se tasse (×1 → 0,98) ; 4.00 la fenêtre défile de 40 u vers le haut (la réponse continue) ; 4.24 « IA » : la lueur de l'écran vire du ocre-pale au gris-lavis (aqErase 0 → 0,5 en 0,3 s : la couleur s'en va) ; 4.40 départ du whip vers P2 (power2.in, flou 0 → 12).
  PISTE CAMÉRA : dérive x +12 u/s, échelle +1 %/s de 2.12 à 4.40 ; 4.40 à 4.64 whip vers la droite (power2.in, +7000 u/s à la couture).
  COUCHES ET PROFONDEUR : avant-plan le cadre de l'écran à l'encre flou (6 px) coupé par les bords ; sujet la fenêtre de chat nette ; fond la lueur et le clavier flous ; couches animées 3 (texte, curseur, caméra).
  OBJET-PONT ET VECTEUR : la réponse grise de l'écran devient les trois pages grises de P2 (même gris-lavis, elles glissent dans le sens du whip) ; vecteur : whip vers la droite repris par la séquence 2.
  SON : clavier court 2.60 ; clic 2.90 ; pinceau 3.30.
  IMAGE CLÉ : 3.60 : l'écran plein cadre, le sujet dans sa bulle ocre pâle en haut, la réponse grise qui s'écrit dessous, « colle » en boîte bordeaux dans le sous-titre.

## Frame 2 : Lundi, trois pages grises · 4.64 → 9.80

- scene: Le whip atterrit sur la page P2, le bureau du prof : une goutte grise s'ouvre et sèche en trois pages qui glissent et se posent sur le bureau ; le stylo rouge arrive au-dessus, tourne une page, puis l'autre, n'a rien à annoter et se pose ; whip vers la page suivante
- duration: 5.16s
- transition_in: cut
- status: outline
- src: compositions/frames/02-lundi.html
- voiceover: "Lundi, il rend trois pages qu'il n'a pas lues."
- type: pain_point
- blueprint: spatial-pan-stations (Adapt)
- focal: les trois pages grises qui se posent, puis le stylo rouge au-dessus de la copie
- rules: depth-of-field-blur, waterfall-entry
- world: light
- handoff_in: à 0.00 : cam(1900, 560, 1.1) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet, pages P1 et P2 posées sur le bureau paper-dark ; P1 : lampe allumée (lavis ocre-2), portable avec la chat-window (sujet collé, réponse grise), goutte accent au pied du portable (1180, 740) et sa traînée ; P2 encore vide (bureau brun, lampe éteinte) ; aucune page grise à l'écran ; sous-titre sorti ; grain 55 %
- handoff_out: à 5.16 : cam(3650, 560, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P2 : les trois pages grises posées à (2440, 540), (2520, 560), (2600, 580), le stylo rouge posé à plat sur la première à (2520, 500) rotation -6°, lampe éteinte ; P3 encore nette au cadrage de référence : lampe du coin allumée, 9 lignes de notes en couleur, cadre de note vide, goutte accent au bas de la page (5080, 820) ; sous-titre sorti ; grain 55 %

Word cues: Lundi@0.22 il@0.92 rend@1.16 trois@1.32 pages@1.62 qu'il@1.94 n'a@2.18 pas@2.38 lues@2.58

Scene 1 (0.00 à 2.70 s) : P4, lundi, les trois pages glissent sur le bureau du prof
  TEXTE ÉCRAN : sous-titre « [boîte : Lundi], il rend trois pages qu'il n'a pas lues. » (boîte tracée 0.18, Lundi 0.22, il 0.92, rend 1.16, trois 1.32, pages 1.62, qu'il 1.94, n'a 2.18, pas 2.38, lues 2.58) ; écart : les pages devancent « rend » de 0,2 s.
  IMAGE DE DÉPART : handoff_in (le whip en cours, P2 arrive de la droite, floue).
  ÉTAPES : 0.00 à 0.22 fin du whip, atterrissage sur cam(2584, 540, 1.0) (expo.out, flou 12 → 0) ; 0.22 « Lundi » : la note Caveat « lundi, 8 h » se révèle (masque 0,3 s) ; 0.36 une goutte grise arrive de la caméra (×4, flou 10, 0,16 s) et s'ouvre sur le bureau à (2440, 540) ; 0.50 elle sèche (aqDry 0 → 1, 0,45 s) en première page grise ; 0.96 la deuxième page glisse depuis la gauche (x -600 → 0, 0,16 s power2.in, flou 8 → 0) et se pose à (2520, 560) rotation 14° ; 1.36 la troisième glisse et se pose à (2600, 580) rotation 21° (chaque arrivée décale la précédente de 6 u) ; 1.62 « pages » : les trois se tassent (×1,02 → 1, 0,08 s) ; 1.94 les lignes grises des pages se révèlent (masque, 0,3 s, décalage 0,05 s) : aucune tache de couleur dessus ; 2.18 « n'a » : la note « Dissertation · 1/3 » se révèle sur la première page (0,25 s) ; 2.40 l'ombre du stylo passe sur la copie (une tache ink à 10 % qui glisse, 0,3 s) ; 2.58 « lues » ; 2.70 départ de la poussée.
  PISTE CAMÉRA : atterrissage 0.00 à 0.22 ; dérive x +20 u/s, échelle +1,5 %/s de 0.22 à 2.70.
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P3 (7 px) coupé par le bord droit ; sujet le bureau et les pages nets ; fond la lampe éteinte à l'encre et le mur en lavis gris, flous ; couches animées 3 (pages, note, caméra).
  OBJET-PONT ET VECTEUR : la copie devient le sujet du gag ; l'ombre du stylo annonce le stylo.
  SON : papier 5.00, 5.40, 5.80 global (0.36, 0.76, 1.16 local : les trois pages).
  IMAGE CLÉ : 1.50 : le bureau du prof, trois pages grises en éventail qui viennent de se poser, la lampe éteinte derrière, « Lundi » en boîte.

Scene 2 (2.70 à 4.00 s) : P5, gag muet, le stylo rouge au-dessus de la copie
  TEXTE ÉCRAN : le sous-titre sort de 2.72 à 2.86 ; aucun texte ensuite (le gag se lit sans mot).
  ÉTAPES : 2.70 poussée vers cam(2560, 560, 1.3) (0,4 s expo.out, flou 4 px) ; 2.76 le stylo rouge entre par le haut droit (y -400 → 0, rotation -50 → -34°, 0,18 s power2.out) et s'arrête à (2660, 440), pointe au-dessus de la première page ; 2.95 il hésite : descend de 14 u (0,12 s) et remonte (0,12 s) ; 3.20 il se penche à -28° et glisse vers le bord de la page (x +60, 0,2 s) ; 3.40 la première page se tourne (rotateY 0 → -170° sur son bord gauche, 0,24 s power2.in, ombre qui passe) et montre la deuxième, grise aussi ; 3.72 le stylo remonte de 20 u (0,1 s) ; 3.88 il repart vers le bord.
  PISTE CAMÉRA : poussée 2.70 à 3.10 ; puis dérive x +10 u/s, échelle +1 %/s jusqu'à 4.00.
  COUCHES ET PROFONDEUR : avant-plan le stylo rouge net devant la copie (il est le sujet) et le bord flou de P3 ; sujet la copie ; fond le bureau brun et la lampe flous (6 px) ; couches animées 2 à 3 (stylo, page, caméra).
  OBJET-PONT ET VECTEUR : le stylo reste et continue son geste au plan suivant ; la page tournée appelle la suivante.
  SON : papier 8.30 global (3.66 local : la page tournée).
  IMAGE CLÉ : 3.50 : la copie vue de plus près, la première page en train de se tourner, le stylo rouge bouchon fermé en l'air au-dessus, rien d'écrit en rouge.

Scene 3 (4.00 à 5.16 s) : P6, deuxième page tournée, rien à annoter, le stylo se pose, whip
  TEXTE ÉCRAN : aucun texte.
  ÉTAPES : 4.00 poussée courte vers cam(2600, 540, 1.42) (0,2 s expo.out) sur la pointe du stylo ; 4.04 la deuxième page se tourne (0,24 s power2.in) et montre la troisième, grise ; 4.36 le stylo descend sur la troisième page (y +60, 0,12 s power2.in), pointe à 10 u du papier ; 4.52 il remonte de 8 u : rien à annoter ; 4.70 il bascule à plat (rotation -34 → -6°, y +40, 0,2 s power2.in) et se pose sur la copie à (2520, 500), petit rebond de 6 u (0,08 s yoyo) ; 4.86 les pages se tassent sous le stylo (×1 → 0,99) ; 5.02 départ du whip vers P3 (power2.in, flou 0 → 12).
  PISTE CAMÉRA : poussée 4.00 à 4.20 ; dérive x +10 u/s jusqu'à 5.02 ; 5.02 à 5.16 whip vers la droite (power2.in, +7000 u/s à la couture).
  COUCHES ET PROFONDEUR : avant-plan le stylo (net, devant) ; sujet la copie ; fond flou ; couches animées 2 (stylo, page).
  OBJET-PONT ET VECTEUR : la copie grise et le stylo posé restent sur P2 (la double page de la séquence 4 les retrouve) ; vecteur : whip vers la droite repris par la séquence 3.
  SON : papier 8.90 global (4.26 local) ; stylo posé 9.50 global (4.86 local) ; whoosh court 9.66 global (5.02 local).
  IMAGE CLÉ : 4.90 : gros plan sur la copie grise avec le stylo rouge couché dessus, bouchon fermé, aucune annotation.

## Frame 3 : Une soirée, une leçon, une note · 9.80 → 15.67

- scene: Le whip atterrit sur la page P3, la page de la leçon : la lampe du coin s'éteint sur « soirée », les neuf lignes de notes en couleur pâlissent en gris sur « leçon », une goutte d'encre tombe dans le cadre de la note et écrit « 12 » qui sèche en gris, puis les lignes s'effacent jusqu'au papier nu ; recul vers la double page
- duration: 5.87s
- transition_in: cut
- status: outline
- src: compositions/frames/03-lecon.html
- voiceover: "Il a gagné une soirée. Il a perdu la leçon. La note tombe, et personne n'a rien appris."
- type: pain_point
- blueprint: camera-journey (Adapt)
- focal: la lampe qui s'éteint, puis les lignes de la leçon, puis la note « 12 »
- rules: coordinate-target-zoom, svg-path-draw
- world: light
- handoff_in: à 0.00 : cam(3650, 560, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P2 : les trois pages grises posées à (2440, 540), (2520, 560), (2600, 580), le stylo rouge posé à plat sur la première à (2520, 500) rotation -6°, lampe éteinte ; P3 encore nette au cadrage de référence : lampe du coin allumée, 9 lignes de notes en couleur, cadre de note vide, goutte accent au bas de la page (5080, 820) ; sous-titre sorti ; grain 55 %
- handoff_out: à 5.87 : cam(3700, 560, 0.70) flou 9 px ; caméra en plein recul (échelle -1,2/s, x -1500 u/s), dérive 0 ; monde : carnet, double page P2 + P3 ; P2 : trois pages grises et stylo posé ; P3 : lampe éteinte (lavis gris à 35 %), lignes de notes effacées (papier nu), note « 12 » séchée en ink-light dans son cadre ; quatre taches de couleur restantes aux coins de la double page : ocre-pale (1900, 300) et accent-pale (1850, 760) sur P2, ocre-pale (4950, 240) et accent-pale (5050, 760) sur P3 ; la goutte accent au bas de la page (5080, 820) ; sous-titre sorti ; grain 55 %

Word cues: Il@0.21 a@0.36 gagné@0.54 une@0.76 soirée@1.02 Il@1.67 a@1.82 perdu@2.04 la@2.34 leçon@2.50 La@3.11 note@3.34 tombe@3.59 et@4.25 personne@4.47 n'a@4.94 rien@5.10 appris@5.40

Scene 1 (0.00 à 1.60 s) : P7, la page de la leçon, la lampe s'éteint
  TEXTE ÉCRAN : sous-titre « Il a gagné une [boîte : soirée]. » (Il 0.21, a 0.36, gagné 0.54, une 0.76, boîte tracée 0.98, soirée 1.02) ; il sort de 1.46 à 1.60 ; écart : la lampe s'éteint sur « soirée » (1.02), synchro.
  IMAGE DE DÉPART : handoff_in (le whip en cours, P3 arrive de la droite, floue).
  ÉTAPES : 0.00 à 0.20 fin du whip, atterrissage sur cam(4318, 540, 1.0) (expo.out, flou 12 → 0) ; 0.21 « Il » : la note Caveat « Leçon » se révèle en haut à gauche (masque 0,3 s) ; 0.40 la lueur de la lampe du coin respire une fois (×1,04, 0,3 s) ; 0.54 « gagné » : les neuf lignes de couleur se tassent (×1,01 → 1) ; 0.90 le bras de la lampe s'abaisse de 6 u (0,1 s) ; 1.02 « soirée » : clic, la lueur ocre-2 s'efface par le centre (aqErase 0 → 1, 0,3 s power2.in) et un lavis gris à 35 % se pose sur la page (coup de pinceau depuis la lampe, 0,3 s) ; 1.30 les lignes de couleur perdent 20 % d'opacité ; 1.46 le sous-titre sort.
  PISTE CAMÉRA : atterrissage 0.00 à 0.20 ; dérive x +18 u/s, échelle +1,5 %/s de 0.20 à 1.40 ; 1.40 départ du cran.
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P4 (7 px) coupé par le bord droit ; sujet la page de la leçon nette ; fond le bureau paper-dark ; couches animées 3 (caméra, lampe, lignes).
  OBJET-PONT ET VECTEUR : le lavis gris qui part de la lampe atteint les lignes de la leçon au plan suivant.
  SON : clic d'interrupteur 10.82 global (1.02 local).
  IMAGE CLÉ : 1.10 : la page de la leçon pleine de lignes ocre et bordeaux pâle, la lampe du coin qui vient de s'éteindre, le gris qui gagne depuis le coin, « soirée » en boîte.

Scene 2 (1.60 à 3.00 s) : P8, cran sur les lignes, la leçon pâlit
  TEXTE ÉCRAN : sous-titre « Il a perdu la [boîte : leçon]. » (Il 1.67, a 1.82, perdu 2.04, la 2.34, boîte tracée 2.46, leçon 2.50) ; il sort de 2.86 à 3.00 ; écart : les lignes pâlissent dès « perdu » (2.04), 0,46 s avant « leçon ».
  ÉTAPES : 1.60 cran vers cam(4150, 520, 1.25) (0,14 s expo.inOut, flou 8 px) sur les lignes ; 1.82 « a » : la ligne 1 se tasse ; 2.04 « perdu » : les neuf lignes pâlissent une à une vers gris-lavis (aqErase 0 → 0,5 : la couleur part, la forme reste), 0,08 s d'écart ; 2.50 « leçon » : la dernière ligne a viré au gris ; 2.60 le lavis gris de la lampe atteint le bas de la page (0,3 s) ; 2.80 une goutte accent commence à arriver de la caméra en haut à droite (×4, flou 10), annonce de la note.
  PISTE CAMÉRA : cran 1.60 à 1.74 ; dérive x +14 u/s, y -6 u/s de 1.74 à 2.80 ; 2.80 départ du cran vers le cadre de la note.
  COUCHES ET PROFONDEUR : avant-plan la goutte en vol, floue ; sujet les lignes nettes ; fond le reste de la page ; couches animées 2 à 3.
  OBJET-PONT ET VECTEUR : la goutte en vol tombe dans le cadre de la note au plan suivant (la caméra la suit, vers la droite et le haut).
  SON : pinceau 12.30 global (2.50 local).
  IMAGE CLÉ : 2.30 : les lignes de la leçon de près, les premières déjà grises, les dernières encore ocre et bordeaux, le gris qui monte.

Scene 3 (3.00 à 4.40 s) : P9, le cadre de la note, « 12 » tombe et sèche en gris
  TEXTE ÉCRAN : sous-titre « La [boîte : note] tombe, et personne n'a rien appris. » (La 3.11, boîte tracée 3.30, note 3.34, tombe 3.59, et 4.25 ; le reste au plan 4) ; écart : la goutte touche sur « tombe » (3.59), synchro.
  ÉTAPES : 3.00 cran vers cam(4760, 300, 1.5) (0,14 s expo.inOut, flou 8 px) sur le cadre de la note ; 3.14 le cadre à l'encre se tasse (×1,02 → 1) ; 3.20 la goutte accent plonge (y -500 → 0, 0,16 s power2.in) ; 3.36 impact dans le cadre : la tache s'ouvre ×0,2 → 1 (0,12 s expo.out), deux éclaboussures ; 3.48 le « 12 » s'écrit depuis la tache (Caveat 150 px accent révélé par un masque, 0,5 s power1.inOut, vitesse d'une main) ; 3.59 « tombe » : petit coup de caméra (y +6, 0,06 s) ; 3.90 la note sèche en gris (aqDry 0 → 1 en 0,4 s pendant que la couleur passe de accent à ink-light) ; 4.25 « et » : le « 12 » gris est posé, la tache sous lui granulée.
  PISTE CAMÉRA : cran 3.00 à 3.14 ; 3.59 coup de 6 u ; dérive x +10 u/s, échelle +1 %/s jusqu'à 4.40.
  COUCHES ET PROFONDEUR : avant-plan le coin de la page et la goutte ; sujet le cadre et la note nets ; fond les lignes grises floues (6 px) ; couches animées 3.
  OBJET-PONT ET VECTEUR : la note séchée reste dans son cadre ; les lignes grises floues du fond deviennent le sujet du plan 4 (la caméra recule vers elles).
  SON : goutte 13.39 global (3.59 local).
  IMAGE CLÉ : 3.75 : le cadre de la note plein cadre, « 12 » à l'encre bordeaux encore humide dans sa tache, les éclaboussures, « note » en boîte.

Scene 4 (4.40 à 5.87 s) : P10, personne n'a rien appris : les lignes s'effacent, recul
  TEXTE ÉCRAN : fin du sous-titre (personne 4.47, n'a 4.94, rien 5.10, appris 5.40) ; il sort de 5.66 à 5.80 ; écart : les lignes s'effacent sur « personne » (4.47), 0,1 s avant.
  ÉTAPES : 4.40 recul court vers cam(4400, 500, 1.05) (0,3 s expo.out) : toute la page ; 4.47 « personne » : les neuf lignes grises s'effacent par le centre une à une (aqErase 0,5 → 1, 0,2 s chacune, 0,1 s d'écart) jusqu'au papier nu ; 4.94 « n'a » : la note « Leçon » pâlit en ink-light ; 5.10 « rien » : le lavis gris de la lampe se retire de 30 % ; 5.40 « appris » : la dernière ligne disparaît ; 5.46 départ du recul vers la double page (power2.in, flou 0 → 9) : P2 entre par la gauche avec sa copie et son stylo.
  PISTE CAMÉRA : recul 4.40 à 4.70 ; dérive échelle -1 %/s de 4.70 à 5.46 ; 5.46 à 5.87 recul vers cam(3451, 560, 0.62) en power2.in (échelle -1,2/s, x -1500 u/s à la couture).
  COUCHES ET PROFONDEUR : avant-plan le bord de P4 flou ; sujet la page qui se vide ; fond le bureau ; couches animées 2 à 3 (lignes, caméra, lavis).
  OBJET-PONT ET VECTEUR : les quatre taches de couleur restantes aux coins de la double page deviennent le sujet de la séquence 4 ; vecteur : recul repris par la séquence 4.
  SON : pinceau 15.20 global (5.40 local : la dernière ligne).
  IMAGE CLÉ : 5.30 : la page de la leçon presque nue, deux dernières lignes grises, la note « 12 » grise dans son cadre, la lampe éteinte.

## Frame 4 : La curiosité s'éteint · 15.67 → 19.22

- scene: Le recul s'achève sur la double page P2 + P3 vue de plus loin : la copie grise et le stylo posé à gauche, la page de la leçon nue à droite ; les quatre dernières taches de couleur aux coins s'effacent une à une, un copier-coller à la fois ; il ne reste que la goutte d'encre bordeaux au coin, et la caméra plonge dedans jusqu'au noir
- duration: 3.55s
- transition_in: cut
- status: outline
- src: compositions/frames/04-curiosite.html
- voiceover: "La curiosité s'éteint, un copier-coller à la fois."
- type: pain_point
- blueprint: zoom-out-workspace-reveal (Adapt)
- focal: les quatre taches de couleur qui s'effacent, puis la goutte d'encre du coin
- rules: depth-of-field-blur, coordinate-target-zoom
- world: light
- handoff_in: à 0.00 : cam(3700, 560, 0.70) flou 9 px ; caméra en plein recul (échelle -1,2/s, x -1500 u/s), dérive 0 ; monde : carnet, double page P2 + P3 ; P2 : trois pages grises et stylo posé ; P3 : lampe éteinte (lavis gris à 35 %), lignes de notes effacées (papier nu), note « 12 » séchée en ink-light dans son cadre ; quatre taches de couleur restantes aux coins de la double page : ocre-pale (1900, 300) et accent-pale (1850, 760) sur P2, ocre-pale (4950, 240) et accent-pale (5050, 760) sur P3 ; la goutte accent au bas de la page (5080, 820) ; sous-titre sorti ; grain 55 %
- handoff_out: à 3.55 : cam(5080, 820, 14) flou 10 px ; caméra en pleine plongée (échelle ×2,2/s, power3.in) dans la goutte accent du bas de P3 ; la goutte couvre 95 % du cadre, son accent s'assombrit vers canvas au centre ; aucune autre tache (toutes effacées) ; sous-titre sorti ; grain 55 %

Word cues: La@0.21 curiosité@0.47 s'éteint@1.13 un@1.86 copier@2.11 -coller@2.53 à@2.81 la@2.99 fois@3.21

Scene 1 (0.00 à 3.10 s) : P11, la double page, les taches s'effacent une à une
  TEXTE ÉCRAN : sous-titre « La [trait : curiosité] s'éteint, un [boîte : copier-coller] à la fois. » (La 0.21, curiosité 0.47 avec le trait ocre tracé de 0.47 à 0.87, s'éteint 1.13, un 1.86, boîte tracée 2.07, copier-coller 2.11 puis 2.53, à 2.81, la 2.99, fois 3.21) ; il sort de 3.30 à 3.44 ; écart : chaque effacement tombe sur son mot, synchro.
  IMAGE DE DÉPART : handoff_in (le recul en cours).
  ÉTAPES : 0.00 à 0.23 fin du recul, atterrissage sur cam(3451, 560, 0.62) (expo.out, flou 9 → 0) : la double page entière, la reliure au centre ; 0.30 le stylo posé sur la copie roule de 4 u (0,1 s) ; 0.47 « curiosité » : la tache ocre-pale (1900, 300) pâlit et s'efface par le centre (aqErase 0 → 1, 0,3 s power2.in) ; 1.13 « s'éteint » : la tache accent-pale (1850, 760) s'efface ; 1.60 le lavis gris de P3 gagne 10 % ; 2.11 « copier » : la tache ocre-pale (4950, 240) s'efface ; 2.53 « -coller » : la tache accent-pale (5050, 760) s'efface ; 2.70 la goutte accent du bas de la page (5080, 820) grossit d'un cran (×1 → 1,15, 0,1 s) : seule couleur restante ; 2.99 « la » : elle luit (opacité 0,85 → 1) ; 3.00 départ de la plongée.
  PISTE CAMÉRA : atterrissage 0.00 à 0.23 ; dérive x +16 u/s, échelle -0,8 %/s de 0.23 à 3.00 (la double page recule encore un peu).
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P4 (7 px) coupé par le bord droit ; sujet la double page nette ; fond le bureau paper-dark grainé qui déborde ; parallaxe 2,5 : 1 : 0,4 ; couches animées 2 à 3 (taches, caméra, stylo).
  OBJET-PONT ET VECTEUR : la goutte accent du bas de la page devient le noir du pivot (la caméra plonge dedans).
  SON : pinceau 16.14, 16.80, 17.78, 18.20 global (0.47, 1.13, 2.11, 2.53 local : les effacements).
  IMAGE CLÉ : 1.80 : la double page vue de plus loin, la copie grise et le stylo rouge à gauche, la page nue à droite, deux taches de couleur déjà effacées, deux encore là, la goutte bordeaux en bas (styleframes/png/A2.png).

Scene 2 (3.10 à 3.55 s) : P12, plongée dans la goutte
  TEXTE ÉCRAN : fin du sous-titre (fois 3.21) ; il sort de 3.30 à 3.44 ; écart : la plongée commence dans le silence après « fois ».
  ÉTAPES : 3.10 plongée vers cam(5080, 820, 14) (power3.in, 0,45 s, flou 0 → 10 au sommet 3.55) : la goutte grandit jusqu'à couvrir le cadre ; 3.21 « fois » ; 3.30 le dernier pinceau : la tache accent-pale résiduelle (s'il en reste un éclat) disparaît ; 3.40 le centre de la goutte s'assombrit (dégradé radial accent → canvas, opacité 0 → 1, 0,15 s) ; 3.55 couture au sommet du flou.
  PISTE CAMÉRA : 3.10 à 3.55 plongée power3.in (échelle ×2,2/s à la couture).
  COUCHES ET PROFONDEUR : la goutte seule (avant, net) ; le papier qui sort du cadre ; couches animées 2 (caméra, dégradé).
  OBJET-PONT ET VECTEUR : la goutte devient le fond noir de la séquence 5 (même objet, autre échelle) ; vecteur : plongée reprise par la séquence 5.
  SON : pinceau 18.88 global (3.21 local) ; whoosh cinématique 18.77 global (3.10 local).
  IMAGE CLÉ : 3.40 : la goutte bordeaux énorme et floue qui remplit le cadre, le papier crème qui disparaît aux coins, le centre déjà presque noir.

## Frame 5 : Et si l'IA servait à apprendre ? · 19.22 → 23.30

- scene: Dans le noir de l'encre, la question du film converge lettre à lettre au centre, un trait ocre sous « apprendre » ; elle tient dans le silence, puis une goutte ocre arrive de la caméra, tombe et éclate au centre : à l'impact le cadre entier est le lavis ocre
- duration: 4.08s
- transition_in: cut
- status: outline
- src: compositions/frames/05-pivot.html
- voiceover: "Et si l'IA servait à apprendre ?"
- type: pivot
- blueprint: video-text-pivot (Adapt)
- focal: la question centrée, puis la goutte ocre qui tombe
- rules: depth-of-field-blur
- world: dark
- handoff_in: à 0.00 : cam(5080, 820, 14) flou 10 px ; caméra en pleine plongée (échelle ×2,2/s, power3.in) dans la goutte accent du bas de P3 ; la goutte couvre 95 % du cadre, son accent s'assombrit vers canvas au centre ; aucune autre tache (toutes effacées) ; sous-titre sorti ; grain 55 %
- handoff_out: à 4.08 : aucun raccord de caméra (coupe franche voulue à 23.30, à l'impact de la goutte ocre) ; raccord de couleur des deux côtés : le cadre entier est le lavis ocre-pale #EFD7A6 à 100 %, sans grain ni texte

Word cues: Et@0.25 si@0.56 l'IA@0.72 servait@1.12 à@1.70 apprendre@1.98

Scene 1 (0.00 à 2.40 s) : P13, le noir, la question converge
  TEXTE ÉCRAN : moment typographique centré (Fraunces 84 px, ink-paper) « Et si l'IA servait à [trait : apprendre] ? » : chaque mot converge sur son temps (Et 0.25, si 0.56, l'IA 0.72, servait 1.12, à 1.70, apprendre 1.98, « ? » 2.30), le trait ocre se trace sous « apprendre » de 1.98 à 2.38 ; aucun sous-titre en bas ; écart synchro.
  IMAGE DE DÉPART : handoff_in (la fin de la plongée : le noir de l'encre gagne tout le cadre).
  ÉTAPES : 0.00 à 0.20 la plongée s'achève dans le noir (flou 10 → 0, expo.out) : ground-ink avec ses ondes sombres qui s'élargissent (1 onde toutes les 0,8 s, de ×0,2 à ×1,6, opacité 0,06 → 0) ; 0.25 « Et » converge (lettres depuis ±0,4 em, opacité 0 → 1, flou 12 → 0, 0,5 s expo.out) ; 0.56 « si » ; 0.72 « l'IA » ; 1.12 « servait » ; 1.70 « à » ; 1.98 « apprendre » converge et le trait ocre se trace dessous (0,4 s power2.out) ; 2.30 le « ? » se pose (×1,3 flou 6 → net, 0,12 s).
  PISTE CAMÉRA : dérive d'échelle +1,5 %/s sur le noir et la phrase (de 0.20 à 2.40) ; les ondes dérivent avec.
  COUCHES ET PROFONDEUR : la phrase nette (sujet) ; les ondes de l'encre derrière, floues (4 px) ; le vignettage canvas-2 devant aux bords ; couches animées 2 (ondes, lettres).
  OBJET-PONT ET VECTEUR : la phrase tient et reste le sujet pendant que la goutte arrive au plan suivant.
  SON : goutte grave 19.22 global (0.00 local : l'arrivée dans l'encre).
  IMAGE CLÉ : 2.35 : noir d'encre, ondes concentriques très sombres, la question entière en crème au centre, trait ocre sous « apprendre » (styleframes/png/C2.png pour la typographie, sur le fond A).

Scene 2 (2.40 à 4.08 s) : P14, le silence, la goutte ocre tombe et éclate
  TEXTE ÉCRAN : la question tient jusqu'à 3.90 puis sort (opacité 1 → 0, flou 0 → 6, 0,14 s) juste avant l'impact ; aucun sous-titre.
  ÉTAPES : 2.40 recul lent de la caméra (échelle -2 %/s) ; 2.60 les ondes ralentissent (une toutes les 1,2 s) ; 3.00 une goutte ocre naît d'un point en haut du cadre (×0,05 → ×1, 0,2 s expo.out, flou 8 → 0) à (960, -40) ; 3.20 elle grossit vers la caméra (×1 → ×2,5, flou 0 → 6, 0,36 s power3.in) : elle vient vers nous en tombant ; 3.56 elle tient une image, énorme et floue ; 3.76 elle plonge sur le centre (y → 540, ×2,5 → ×1, 0,17 s power2.in) ; 3.90 la question sort ; 3.93 impact au centre (960, 540) : le lavis ocre-pale s'ouvre ×0,2 → ×14 (0,15 s expo.out) et recouvre tout le cadre ; 4.08 le cadre est entièrement ocre-pale : coupe.
  PISTE CAMÉRA : 2.40 à 3.93 recul lent (échelle -2 %/s) ; 3.93 à 4.08 immobile sous le lavis qui recouvre tout (le mouvement est celui de la tache).
  COUCHES ET PROFONDEUR : avant-plan la goutte en vol (grande, floue) ; sujet la question ; fond les ondes ; couches animées 3.
  OBJET-PONT ET VECTEUR : le lavis ocre qui recouvre le cadre est la première image de la séquence 6 (il sèche en page de la classe).
  SON : goutte 23.23 global (4.01 local) ; whoosh 23.30 global (4.08 local, le papier s'ouvre).
  IMAGE CLÉ : 3.60 : la question en crème sur le noir, une grosse goutte ocre floue qui tombe vers le centre, les ondes derrière.

## Frame 6 : Je forme vos étudiants · 23.30 → 27.59

- scene: Le lavis ocre sèche et laisse apparaître la page P4, la classe : quatre tables, huit silhouettes peintes en taches ocre et bordeaux, un portable par table ; puis la caméra file vers la page P5, l'écran dessiné en grand, où une première goutte tombe et sèche en question tapée ; cran vers la coche
- duration: 4.29s
- transition_in: cut
- status: outline
- src: compositions/frames/06-classe.html
- voiceover: "Je forme vos étudiants à l'IA. Ils apprennent à la questionner,"
- type: demo
- blueprint: spatial-pan-stations (Adapt)
- focal: les tables et les silhouettes qui naissent du lavis, puis la question tapée sur l'écran
- rules: waterfall-entry, svg-path-draw
- world: light
- handoff_in: à 0.00 : aucun raccord de caméra (coupe franche voulue à 23.30, à l'impact de la goutte ocre) ; raccord de couleur des deux côtés : le cadre entier est le lavis ocre-pale #EFD7A6 à 100 %, sans grain ni texte
- handoff_out: à 4.29 : cam(7420, 330, 1.6) flou 6 px ; caméra en plein cran vers la droite (+1400 u/s en x, expo.inOut), dérive 0 ; monde : carnet, page P5 ; la chat-window (1300 × 720) centrée à (7786, 470) : bulle « VOUS » avec la question tapée « Pourquoi la guerre a-t-elle éclaté en 1914 ? » et son « ? » en accent séché, réponse « IA » en 4 lignes ink ; aucune coche, aucune barre, aucun croquis encore ; sous-titre sorti ; grain 55 %

Word cues: Je@0.37 forme@0.70 vos@0.96 étudiants@1.22 à@1.80 l'IA@2.04 Ils@2.71 apprennent@2.98 à@3.32 la@3.50 questionner@3.66

Scene 1 (0.00 à 2.50 s) : P15, le lavis sèche en classe
  TEXTE ÉCRAN : sous-titre « Je [boîte : forme] vos étudiants à l'IA. » (Je 0.37, boîte tracée 0.66, forme 0.70, vos 0.96, étudiants 1.22, à 1.80, l'IA 2.04) ; il sort de 2.36 à 2.50 ; écart : les tables devancent « forme » de 0,2 s.
  IMAGE DE DÉPART : le cadre entier ocre-pale (handoff_in), caméra cam(6052, 540, 1.08).
  ÉTAPES : 0.00 le lavis sèche de l'intérieur (aqDry 0 → 1 en 0,6 s) : son anneau de bord fonce, sa granulation paraît, et le papier de P4 apparaît par le centre (le lavis se rétracte en grand lavis de sol ocre-pale à 55 %, clip-path circle 100 % → 60 %, 0,5 s expo.out) ; 0.30 le grain du papier revient (opacité 0 → 0,55, 0,2 s) ; 0.50 la table 1 naît d'une goutte brune (impact ×0,2 → 1, 0,12 s) à (5592, 560) ; 0.62, 0.74, 0.86 les tables 2, 3, 4 (même geste, 0,12 s d'écart) ; 0.70 « forme » ; 0.96 « vos » : les portables se dessinent sur les tables (tracé 0,3 s, 0,05 s d'écart) ; 1.10 « étudiants » (1.22) : les huit silhouettes se peignent par coups de pinceau (buste scaleY 0 → 1 depuis la table, 0,16 s expo.out, puis la tête ×0,2 → 1, 0,1 s), 0,1 s d'écart, ocre à gauche, bordeaux à droite ; 1.80 « à » : les silhouettes se penchent vers leurs écrans (rotation 2°, 0,2 s) ; 2.04 « l'IA » : les quatre écrans s'allument (lavis ocre-pale ×0,2 → 1) ; 2.36 le sous-titre sort.
  PISTE CAMÉRA : dérive échelle -1,5 %/s (de 1.08 vers 1.0) et x +14 u/s de 0.00 à 2.50 ; 2.50 départ du whip.
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P5 (7 px) coupé par le bord droit et une silhouette du premier rang floue (6 px) ; sujet les tables et les figures ; fond le lavis de sol et le bureau ; couches animées 3 à 4 (tables, figures, écrans, caméra).
  OBJET-PONT ET VECTEUR : l'écran d'un portable allumé devient l'écran en grand de P5 (la caméra file vers la droite, du petit écran au grand).
  SON : goutte 23.23 déjà passée ; pinceau 24.00 à 25.30 global (0.70 à 2.00 local : les figures).
  IMAGE CLÉ : 1.70 : la classe en aquarelle, quatre tables brunes, huit silhouettes ocre et bordeaux de dos, un portable par table, le sol ocre pâle (styleframes/png/A3.png, moitié gauche), « forme » en boîte.

Scene 2 (2.50 à 4.29 s) : P16, whip vers l'écran, la première goutte : questionner
  TEXTE ÉCRAN : sous-titre « Ils apprennent à la [boîte : questionner], » (Ils 2.71, apprennent 2.98, à 3.32, la 3.50, boîte tracée 3.62, questionner 3.66) ; écart : la goutte touche l'écran 0,36 s avant « questionner » (3.30), la question s'écrit sur le mot.
  ÉTAPES : 2.50 whip vers la droite (power2.in, flou 0 → 12, sommet 2.65) puis atterrissage sur cam(7786, 470, 1.25) à 2.70 (expo.out) : la chat-window de P5 (1300 × 720) presque plein cadre, vide ; 2.71 « Ils » : l'étiquette « NOUVELLE CONVERSATION » se révèle ; 2.98 « apprennent » : le champ « Écrire un message » paraît (×1,1 flou 6 → net) ; 3.10 une goutte ocre arrive de la caméra (×4, flou 10, 0,16 s) ; 3.30 impact sur la bulle « VOUS » (impact ×0,2 → 1) ; 3.40 la tache sèche (aqDry 0 → 1, 0,4 s) et la question s'écrit dedans caractère par caractère derrière un caret bordeaux (0,5 s, 2 à 3 caractères par image) : « Pourquoi la guerre a-t-elle éclaté en 1914 ? » ; 3.66 « questionner » ; 3.90 le « ? » final se pose en accent (×1,3 → 1, 0,1 s) ; 4.00 la réponse « IA » se révèle en 4 lignes ink (masque, 0,25 s) ; 4.15 départ du cran vers la droite (vers la coche à venir).
  PISTE CAMÉRA : whip 2.50 à 2.70 ; dérive x +12 u/s, échelle +1 %/s de 2.70 à 4.15 ; 4.15 à 4.29 cran vers cam(7420, 330, 1.6) en expo.inOut (flou 6 px à la couture).
  COUCHES ET PROFONDEUR : avant-plan le cadre à l'encre de la fenêtre flou (6 px) coupé par les bords ; sujet la bulle et la question nettes ; fond le papier de P5 ; couches animées 3 (caméra, goutte, texte).
  OBJET-PONT ET VECTEUR : la question posée reste sur l'écran ; le cran vers la droite est repris par la séquence 7 (il s'achève sur la coche).
  SON : goutte 26.60 global (3.30 local).
  IMAGE CLÉ : 3.80 : la grande fenêtre de chat dessinée, la question en train de s'écrire dans une tache ocre séchée, le caret bordeaux, « questionner » en boîte.

## Frame 7 : Vérifier, contredire, créer · 27.59 → 31.41

- scene: Sur l'écran de P5, trois gouttes sèchent en trois gestes : une coche ocre à côté d'une source, une barre bordeaux à travers une ligne de la réponse, un croquis coloré qui s'étale dans la marge ; la caméra fait un cran vers chaque geste, puis descend vers le bas de la page
- duration: 3.82s
- transition_in: cut
- status: outline
- src: compositions/frames/07-gestes.html
- voiceover: "à la vérifier, à la contredire, à créer avec elle."
- type: demo
- blueprint: cursor-ui-demo (Adapt)
- focal: la coche, puis la barre, puis le croquis
- rules: svg-path-draw, coordinate-target-zoom
- world: light
- handoff_in: à 0.00 : cam(7420, 330, 1.6) flou 6 px ; caméra en plein cran vers la droite (+1400 u/s en x, expo.inOut), dérive 0 ; monde : carnet, page P5 ; la chat-window (1300 × 720) centrée à (7786, 470) : bulle « VOUS » avec la question tapée « Pourquoi la guerre a-t-elle éclaté en 1914 ? » et son « ? » en accent séché, réponse « IA » en 4 lignes ink ; aucune coche, aucune barre, aucun croquis encore ; sous-titre sorti ; grain 55 %
- handoff_out: à 3.82 : cam(7786, 700, 1.4) flou 8 px ; caméra en plein cran vers le bas (+1200 u/s en y, expo.inOut), dérive 0 ; monde : carnet, page P5 ; chat-window avec la question, la coche ocre à (8100, 330), la barre accent sur la ligne 2 de la réponse, le croquis coloré à (8160, 560) ; en bas de la page les deux bulles « IA » encore vides (cadres à l'encre) à (7500, 880) et (8070, 880) ; sous-titre sorti ; grain 55 %

Word cues: à@0.08 la@0.23 vérifier@0.37 à@1.13 la@1.25 contredire@1.49 à@2.40 créer@2.73 avec@3.03 elle@3.39

Scene 1 (0.00 à 1.13 s) : P17, la coche : vérifier
  TEXTE ÉCRAN : sous-titre « à la vérifier, à la contredire, » (à 0.08, la 0.23, vérifier 0.37, à 1.13, la 1.25, contredire 1.49 au plan 2) ; pas de boîte (la boîte de cette phrase est sur « questionner », séquence 6) ; écart : la goutte touche 0,16 s avant « vérifier ».
  IMAGE DE DÉPART : handoff_in (le cran en cours vers la droite de la réponse).
  ÉTAPES : 0.00 à 0.14 fin du cran sur cam(8100, 330, 1.6) (expo.inOut, flou 6 → 0) : la ligne 1 de la réponse et sa marge droite ; 0.06 une goutte ocre arrive de la caméra ; 0.21 impact dans la marge à (8100, 330) ; 0.30 la tache sèche (0,3 s) et une coche s'y dessine à l'encre ocre (tracé 0,25 s power2.out) ; 0.37 « vérifier » ; 0.50 une petite note Caveat « source » se révèle sous la coche (0,2 s) ; 0.70 la ligne 1 de la réponse se souligne d'un trait ink-light (tracé 0,2 s) ; 0.90 la coche se tasse (×1,04 → 1) ; 1.00 départ du cran vers la ligne 2.
  PISTE CAMÉRA : fin du cran 0.00 à 0.14 ; dérive x +10 u/s, y +6 u/s jusqu'à 1.00 ; 1.00 à 1.13 cran vers cam(7900, 420, 1.6) (expo.inOut, flou 6 px).
  COUCHES ET PROFONDEUR : avant-plan le cadre de la fenêtre flou coupé par le bord ; sujet la ligne et la coche nets ; fond les autres lignes floues (4 px) ; couches animées 2 à 3.
  OBJET-PONT ET VECTEUR : le cran descend d'une ligne : la ligne 2 devient le sujet.
  SON : goutte 27.80 global (0.21 local).
  IMAGE CLÉ : 0.60 : la ligne 1 de la réponse nette, une coche ocre dans la marge sur sa tache séchée, « source » en Caveat dessous.

Scene 2 (1.13 à 2.40 s) : P18, la barre : contredire
  TEXTE ÉCRAN : fin de « à la contredire, » (la 1.25, contredire 1.49) ; le sous-titre sort de 2.26 à 2.40 ; écart : la goutte touche 0,18 s avant « contredire ».
  ÉTAPES : 1.13 fin du cran sur la ligne 2 ; 1.16 une goutte accent arrive de la caméra ; 1.31 impact au début de la ligne 2 ; 1.40 la tache s'étire en barre (scaleX 0 → 1 depuis la gauche, 0,2 s power2.out) à travers la ligne : la phrase est barrée ; 1.49 « contredire » ; 1.70 la ligne barrée pâlit (ink → ink-light, 0,2 s) ; 1.85 une correction s'écrit en Caveat accent au-dessus de la ligne barrée (masque 0,4 s) : « non : en 1914 » ; 2.10 la barre sèche (aqDry 0 → 1, 0,3 s) ; 2.26 le sous-titre sort ; 2.28 départ du cran vers la marge basse.
  PISTE CAMÉRA : dérive x +10 u/s, y +6 u/s de 1.13 à 2.28 ; 2.28 à 2.40 cran vers cam(8160, 560, 1.5) (expo.inOut, flou 6 px).
  COUCHES ET PROFONDEUR : avant-plan la goutte en vol puis le cadre ; sujet la ligne 2 et sa barre ; fond les lignes voisines floues ; couches animées 3.
  OBJET-PONT ET VECTEUR : la correction manuscrite ouvre la marge où le croquis va naître ; le cran descend encore.
  SON : goutte 28.90 global (1.31 local) ; stylo 29.30 global (1.71 local : la correction).
  IMAGE CLÉ : 2.00 : la ligne 2 de la réponse barrée d'un trait bordeaux, la correction manuscrite au-dessus, la coche ocre au-dessus hors champ partiel.

Scene 3 (2.40 à 3.82 s) : P19, le croquis : créer avec elle, cran vers le bas
  TEXTE ÉCRAN : sous-titre « à créer avec elle. » (à 2.40, créer 2.73, avec 3.03, elle 3.39) ; pas de boîte (celle de la phrase est sur « questionner », séquence 6) ; il sort de 3.68 à 3.82 ; écart : la goutte touche 0,13 s avant « créer ».
  ÉTAPES : 2.40 fin du cran sur la marge basse de la réponse ; 2.44 une goutte ocre puis une goutte accent arrivent de la caméra (0,06 s d'écart) ; 2.60 impacts côte à côte à (8160, 560) ; 2.73 « créer » : les deux taches s'étalent l'une dans l'autre (×1 → ×1,6, 0,2 s expo.out) et un croquis se dessine à l'encre par-dessus (tracé 0,5 s : une carte d'Europe stylisée en trois traits et une flèche) ; 3.03 « avec » : le croquis se tasse ; 3.20 une étiquette Caveat « croquis : causes » se révèle (0,2 s) ; 3.39 « elle » : les taches sèchent (0,3 s) ; 3.68 le sous-titre sort ; 3.70 départ du cran vers le bas de la page (power2.in, flou 0 → 8).
  PISTE CAMÉRA : dérive x +8 u/s, échelle +1 %/s de 2.40 à 3.70 ; 3.70 à 3.82 cran vers le bas vers cam(7786, 860, 1.5) en expo.inOut (+1200 u/s en y, flou 8 px à la couture).
  COUCHES ET PROFONDEUR : avant-plan les gouttes en vol puis le bord de la fenêtre ; sujet le croquis ; fond la réponse floue ; couches animées 3.
  OBJET-PONT ET VECTEUR : le cran vers le bas quitte la fenêtre pour les deux bulles du bas de la page (séquence 8) ; les deux couleurs du croquis (ocre, bordeaux) sont les couleurs des deux bulles.
  SON : gouttes 30.20 global (2.61 local) ; pinceau 30.40 global (2.81 local).
  IMAGE CLÉ : 3.10 : dans la marge de la réponse, deux taches ocre et bordeaux mêlées, un croquis à l'encre dessus.

## Frame 8 : Ce qu'elle sait, ce qu'elle invente · 31.41 → 34.48

- scene: En bas de la page P5, deux bulles côte à côte : à gauche une tache ocre nette qui sèche en bulle propre (ce qu'elle sait), à droite une tache bordeaux pâle qui bave, coule, et qu'un trait d'encre corrige (ce qu'elle invente) ; whip vers la page du défi
- duration: 3.07s
- transition_in: cut
- status: outline
- src: compositions/frames/08-sait-invente.html
- voiceover: "Ils découvrent ce qu'elle sait, et ce qu'elle invente."
- type: demo
- blueprint: comparison-split (Adapt)
- focal: la bulle nette à gauche, puis la bulle qui bave à droite
- rules: depth-of-field-blur, svg-path-draw
- world: light
- handoff_in: à 0.00 : cam(7786, 700, 1.4) flou 8 px ; caméra en plein cran vers le bas (+1200 u/s en y, expo.inOut), dérive 0 ; monde : carnet, page P5 ; chat-window avec la question, la coche ocre à (8100, 330), la barre accent sur la ligne 2 de la réponse, le croquis coloré à (8160, 560) ; en bas de la page les deux bulles « IA » encore vides (cadres à l'encre) à (7500, 880) et (8070, 880) ; sous-titre sorti ; grain 55 %
- handoff_out: à 3.07 : cam(8900, 560, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P5 : les deux bulles séchées (ocre nette, accent-pale corrigée) ; P6 au cadrage de référence : « Défi 3 · Trouvez l'erreur de l'IA » posé, chrono à (9520, 300) à « 00:42 », colonnes vides, aucune figure encore ; sous-titre sorti ; grain 55 %

Word cues: Ils@0.19 découvrent@0.43 ce@0.97 qu'elle@1.19 sait@1.39 et@1.90 ce@2.03 qu'elle@2.23 invente@2.49

Scene 1 (0.00 à 3.07 s) : P20, les deux bulles côte à côte, whip
  TEXTE ÉCRAN : sous-titre « Ils découvrent ce qu'elle sait, et ce qu'elle [boîte : invente]. » (Ils 0.19, découvrent 0.43, ce 0.97, qu'elle 1.19, sait 1.39, et 1.90, ce 2.03, qu'elle 2.23, boîte tracée 2.45, invente 2.49) ; il sort de 2.86 à 3.00 ; écart : la bulle nette devance « sait » de 0,3 s, la bavure devance « invente » de 0,3 s.
  IMAGE DE DÉPART : handoff_in (le cran en cours vers le bas de la page).
  ÉTAPES : 0.00 à 0.19 fin du cran, atterrissage sur cam(7786, 860, 1.5) (expo.out, flou 8 → 0) : les deux cadres de bulles vides côte à côte, marges égales ; 0.19 « Ils » : les étiquettes « IA » des deux bulles se révèlent (0,2 s) ; 0.43 « découvrent » : une goutte ocre arrive et touche la bulle de gauche (impact 0.60) ; 0.70 elle sèche en tache nette (aqDry 0 → 1, 0,4 s), bord franc, et une ligne de texte ink se révèle dedans : « 1914 : attentat de Sarajevo. » ; 1.10 une coche ocre se trace à côté (0,2 s) ; 1.39 « sait » ; 1.60 une goutte accent-pale arrive et touche la bulle de droite (impact 1.75) ; 1.85 la tache bave : elle s'étire vers le bas (scaleY 1 → 1,3, origine en haut, 0,2 s expo.out) puis coule en deux traînées (dérive linéaire, scaleY 1,3 → 1,5 sur 1,0 s) ; 2.00 une ligne de texte ink-light se révèle dedans : « 1912 : attentat de Vienne. » ; 2.23 « qu'elle » : la traînée atteint le bord de la bulle ; 2.49 « invente » : un trait d'encre bordeaux barre la ligne (scaleX 0 → 1, 0,16 s) et « non » s'écrit en Caveat accent dessous (0,25 s) ; 2.80 les deux bulles sèchent ; 2.93 départ du whip vers P6 (power2.in, flou 0 → 12).
  PISTE CAMÉRA : atterrissage 0.00 à 0.19 ; dérive x +12 u/s, échelle +1 %/s de 0.19 à 2.93 ; 2.93 à 3.07 whip vers la droite (power2.in, +7000 u/s à la couture).
  COUCHES ET PROFONDEUR : avant-plan le bas du cadre de la chat-window flou (6 px) coupé par le bord haut, et le bord flou de P6 à droite ; sujet les deux bulles nettes ; fond le papier de P5 ; couches animées 3 (gouttes, texte, caméra).
  OBJET-PONT ET VECTEUR : les deux couleurs des bulles deviennent les deux équipes de P6 (ocre à gauche, bordeaux à droite) ; vecteur : whip vers la droite repris par la séquence 9.
  SON : pinceau 32.80 global (1.39 local) ; goutte 33.64 global (2.23 local) ; stylo 33.95 global (2.54 local) ; whoosh court 34.30 global (2.89 local).
  IMAGE CLÉ : 2.60 : deux bulles côte à côte en bas de la page : à gauche la tache ocre nette et cochée, à droite la tache bordeaux pâle qui coule, sa ligne barrée, « non » écrit à la main, « invente » en boîte.

## Frame 9 : En équipes, par défis · 34.48 → 38.14

- scene: Le whip atterrit sur la page P6, le défi : deux gouttes deviennent deux équipes de silhouettes, ocre à gauche, bordeaux à droite ; le chronomètre à l'encre se dessine et ses chiffres roulent ; les deux colonnes de points montent goutte à goutte et la couleur revient sur toute la page ; whip vers la page suivante
- duration: 3.66s
- transition_in: cut
- status: outline
- src: compositions/frames/09-defi.html
- voiceover: "En équipes, par défis, la curiosité revient."
- type: payoff
- blueprint: dataviz-countup (Adapt)
- focal: les deux équipes, puis le chronomètre, puis les colonnes de points
- rules: counting-dynamic-scale, stat-bars-and-fills
- world: light
- handoff_in: à 0.00 : cam(8900, 560, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P5 : les deux bulles séchées (ocre nette, accent-pale corrigée) ; P6 au cadrage de référence : « Défi 3 · Trouvez l'erreur de l'IA » posé, chrono à (9520, 300) à « 00:42 », colonnes vides, aucune figure encore ; sous-titre sorti ; grain 55 %
- handoff_out: à 3.66 : cam(10640, 540, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P6 : chrono à « 00:40 », colonnes 7 et 9 pleines, deux équipes en figures, la page entière colorée (lavis ocre-pale et accent-pale) ; P7 : le reflex-notebook ouvert à (11254, 430), lignes encore vides ; sous-titre sorti ; grain 55 %

Word cues: En@0.24 équipes@0.48 par@1.10 défis@1.36 la@2.01 curiosité@2.32 revient@3.04

Scene 1 (0.00 à 1.10 s) : P21, deux gouttes, deux équipes
  TEXTE ÉCRAN : sous-titre « En [boîte : équipes], par défis, la curiosité revient. » (En 0.24, boîte tracée 0.44, équipes 0.48, par 1.10, défis 1.36, la 2.01, curiosité 2.32, revient 3.04 avec le trait ocre tracé de 3.04 à 3.44) ; écart : les gouttes touchent 0,12 s avant « équipes ».
  IMAGE DE DÉPART : handoff_in (le whip en cours, P6 arrive de la droite).
  ÉTAPES : 0.00 à 0.22 fin du whip, atterrissage sur cam(9520, 540, 1.0) (expo.out, flou 12 → 0) : le titre « Défi 3 · Trouvez l'erreur de l'IA » (Fraunces + Caveat) déjà posé en haut à gauche, le chrono à l'encre à droite ; 0.24 « En » : deux gouttes arrivent de la caméra, ocre vers la gauche, accent vers la droite ; 0.36 impacts à (8900, 600) et (10140, 600) ; 0.48 « équipes » : chaque tache se divise en deux silhouettes (deux coups de pinceau depuis la tache, 0,16 s, puis les têtes ×0,2 → 1) ; 0.70 une table en lavis brun se pose devant chaque équipe (×1,1 flou 6 → net, 0,12 s) ; 0.90 les silhouettes se penchent vers la table (2°, 0,2 s) ; 1.00 départ du cran vers le chrono.
  PISTE CAMÉRA : atterrissage 0.00 à 0.22 ; dérive x +16 u/s, échelle +1 %/s jusqu'à 1.00 ; 1.00 à 1.10 cran vers cam(9520, 320, 1.4) (expo.inOut, flou 6 px).
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P7 (7 px) coupé par le bord droit ; sujet les deux équipes nettes ; fond le titre et le chrono légèrement flous (3 px) ; couches animées 3 (gouttes, figures, caméra).
  OBJET-PONT ET VECTEUR : le chrono du fond devient le sujet du plan suivant (cran vers le haut).
  SON : gouttes 34.96 global (0.48 local).
  IMAGE CLÉ : 0.80 : la page du défi, deux équipes de silhouettes qui viennent de naître de deux taches, ocre à gauche, bordeaux à droite, « équipes » en boîte.

Scene 2 (1.10 à 2.00 s) : P22, le chronomètre : par défis
  TEXTE ÉCRAN : « par » 1.10, « défis » 1.36 ; écart : le chrono roule sur « défis », synchro.
  ÉTAPES : 1.10 fin du cran sur le chrono ; 1.14 le cercle d'encre se redessine (tracé 0,3 s power2.out) sur son lavis ocre-pale ; 1.36 « défis » : les chiffres roulent de « 00:42 » à « 00:41 » (chaque chiffre glisse vers le haut, 0,12 s, tabulaire) et l'aiguille accent tourne de 6° ; 1.50 « il reste » en Caveat accent se révèle dessous (0,2 s) ; 1.70 un tic : l'aiguille avance encore (6°, 0,04 s) ; 1.88 « 00:40 » roule ; 1.90 départ du cran vers les colonnes.
  PISTE CAMÉRA : dérive x +10 u/s, y +4 u/s de 1.10 à 1.90 ; 1.90 à 2.00 cran vers cam(9520, 640, 1.2) (expo.inOut, flou 6 px).
  COUCHES ET PROFONDEUR : avant-plan le titre « Défi 3 » flou coupé par le bord gauche ; sujet le chrono net ; fond les équipes floues en bas ; couches animées 2 à 3.
  OBJET-PONT ET VECTEUR : l'aiguille du chrono pointe vers le bas, vers les colonnes (le cran suit).
  SON : tic-tac 35.84 global (1.36 local) puis à chaque seconde.
  IMAGE CLÉ : 1.60 : le chronomètre à l'encre sur sa tache ocre, « 00:41 » au centre, « il reste » à la main dessous.

Scene 3 (2.00 à 3.66 s) : P23, les points montent, la couleur revient, whip
  TEXTE ÉCRAN : « la » 2.01, « curiosité » 2.32, « [trait : revient] » 3.04 (trait ocre 3.04 à 3.44) ; le sous-titre sort de 3.52 à 3.66 ; écart : les points montent dès « la » (2.01), la page se colore sur « revient » (3.04), synchro.
  ÉTAPES : 2.00 fin du cran sur les colonnes vides (le trait d'encre de base à y 870) ; 2.01 « la » : les gouttes tombent en pile, une par 0,12 s, ocre à gauche (7) et bordeaux à droite (9), chacune touche la précédente (impact ×0,2 → 1, petit tassement de la pile) ; 2.32 « curiosité » : les piles continuent ; 2.90 la neuvième goutte bordeaux se pose ; 3.04 « revient » : la couleur revient sur toute la page (deux grands lavis ocre-pale et accent-pale par coups de pinceau depuis les colonnes, scaleX 0 → 1, 0,4 s power2.out, et le lavis de sol ocre-pale monte) ; 3.10 scintillement : trois points ocre-2 naissent et s'éteignent sur les colonnes (0,3 s) ; 3.30 les équipes lèvent un bras (figure 'bras-leve' sur une silhouette par équipe, 0,16 s) ; 3.52 départ du whip vers P7 (power2.in, flou 0 → 12).
  PISTE CAMÉRA : dérive échelle -1 %/s (de 1.2 vers 1.0) et x +16 u/s de 2.00 à 3.52 ; 3.52 à 3.66 whip vers la droite (power2.in, +7000 u/s à la couture).
  COUCHES ET PROFONDEUR : avant-plan les gouttes en vol et le bord flou de P7 ; sujet les colonnes nettes ; fond les équipes et le chrono flous ; couches animées 3 à 4 (gouttes, lavis, figures, caméra).
  OBJET-PONT ET VECTEUR : la couleur revenue sur P6 déborde vers P7 dans le whip ; vecteur : whip vers la droite repris par la séquence 10.
  SON : pops 36.80 à 37.90 global (2.32 à 3.42 local : les points) ; scintillement 37.52 global (3.04 local) ; whoosh court 38.00 global (3.52 local).
  IMAGE CLÉ : 3.20 : les deux colonnes de gouttes, 7 ocre et 9 bordeaux, la page entière colorée, les équipes qui lèvent un bras, « revient » souligné d'un trait ocre.

## Frame 10 : Une méthode, de bons réflexes · 38.14 → 43.26

- scene: Le whip atterrit sur la page P7 : un petit carnet manuscrit ouvert où quatre réflexes s'écrivent et se cochent, puis se referme ; sous lui, la page du début, colorée cette fois, tenue par deux mains peintes ; whip vers la dernière page
- duration: 5.12s
- transition_in: cut
- status: outline
- src: compositions/frames/10-reflexes.html
- blueprint: spatial-pan-stations (Adapt)
- voiceover: "Une méthode et de bons réflexes suffisent. Et le cours redevient le leur."
- type: reassurance
- focal: le carnet des réflexes, puis la page du début dans les mains
- rules: svg-path-draw, depth-of-field-blur
- world: light
- handoff_in: à 0.00 : cam(10640, 540, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P6 : chrono à « 00:40 », colonnes 7 et 9 pleines, deux équipes en figures, la page entière colorée (lavis ocre-pale et accent-pale) ; P7 : le reflex-notebook ouvert à (11254, 430), lignes encore vides ; sous-titre sorti ; grain 55 %
- handoff_out: à 5.12 : cam(12380, 540, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P7 : le carnet refermé sur la page du début colorée dans les mains ; P8 vide (papier nu) ; sous-titre sorti ; grain 55 %

Word cues: Une@0.19 méthode@0.42 et@0.92 de@1.10 bons@1.36 réflexes@1.52 suffisent@2.14 Et@2.97 le@3.16 cours@3.38 redevient@3.62 le@4.36 leur@4.56

Scene 1 (0.00 à 2.70 s) : P24, le carnet des réflexes s'écrit, se coche, se referme
  TEXTE ÉCRAN : sous-titre « Une méthode et de bons [boîte : réflexes] suffisent. » (Une 0.19, méthode 0.42, et 0.92, de 1.10, bons 1.36, boîte tracée 1.48, réflexes 1.52, suffisent 2.14) ; il sort de 2.56 à 2.70 ; écart : les lignes s'écrivent 0,2 s avant leur rythme de voix.
  IMAGE DE DÉPART : handoff_in (le whip en cours, P7 arrive de la droite).
  ÉTAPES : 0.00 à 0.19 fin du whip, atterrissage sur cam(11254, 430, 1.4) (expo.out, flou 12 → 0) : le petit carnet ouvert, spirale à l'encre, quatre lignes vides ; 0.19 « Une » : la spirale se tasse (×1,02 → 1) ; 0.42 « méthode » : « Questionner » s'écrit en Caveat (masque, 0,3 s) ; 0.72 « Vérifier » s'écrit ; 1.02 « Contredire » ; 1.32 « Créer » ; 1.52 « réflexes » : quatre coches ocre se tracent une à une (0,12 s chacune, 0,08 s d'écart) ; 2.14 « suffisent » : le carnet se referme (rotateY 0 → -165° sur la charnière gauche, 0,28 s power3.in, ombre qui balaie) et montre sa couverture paper-2 ; 2.56 le sous-titre sort ; 2.60 départ du cran vers le bas.
  PISTE CAMÉRA : atterrissage 0.00 à 0.19 ; dérive x +14 u/s, échelle +1 %/s de 0.19 à 2.60 ; 2.60 à 2.90 cran vers cam(11254, 640, 1.1) (expo.inOut, flou 6 px).
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P8 (7 px) coupé par le bord droit ; sujet le carnet net ; fond les mains et la page du début encore floues (6 px), en dessous ; couches animées 2 à 3 (écriture, coches, caméra).
  OBJET-PONT ET VECTEUR : le carnet refermé laisse voir la page du début dans les mains, sujet du plan suivant (cran vers le bas).
  SON : stylo 38.56 à 40.00 global (0.42 à 1.86 local : l'écriture et les coches) ; papier 40.40 global (2.26 local : le carnet se referme).
  IMAGE CLÉ : 1.80 : le petit carnet manuscrit ouvert, quatre réflexes écrits à la main et cochés d'ocre, « réflexes » en boîte.

Scene 2 (2.70 à 5.12 s) : P25, la page du début, colorée, dans les mains, whip
  TEXTE ÉCRAN : sous-titre « Et le [boîte : cours] redevient [trait : le leur]. » (Et 2.97, le 3.16, boîte tracée 3.34, cours 3.38, redevient 3.62, le 4.36, leur 4.56 avec le trait ocre tracé de 4.36 à 4.76) ; il sort de 4.98 à 5.12 ; écart : la page se colore sur « redevient » (3.62), 0,7 s avant « le leur ».
  ÉTAPES : 2.70 à 2.90 fin du cran sur les mains ; 2.97 « Et » : les deux mains peintes se posent de chaque côté de la page (coups de pinceau accent-pale et ocre-pale, 0,16 s) et serrent (x ±10 u, 0,1 s) ; 3.16 « le » : le carnet refermé glisse hors du cadre par le haut (y -500, 0,22 s power2.in) ; 3.38 « cours » : la page du début apparaît nette sous les mains : la lampe, le portable, la goutte, en lavis gris ; 3.62 « redevient » : la couleur revient par coups de pinceau (la lampe en ocre-2, l'écran en ocre-pale, la nuit en accent-pale, la goutte en accent, 0,2 s chacun, 0,1 s d'écart) ; 4.20 la page se tasse dans les mains (×1,01 → 1) ; 4.36 « le leur » : le trait ocre se trace ; 4.70 les mains inclinent la page de 2° (0,2 s power2.out) ; 4.98 départ du whip vers P8 (power2.in, flou 0 → 12).
  PISTE CAMÉRA : dérive x +12 u/s, échelle +1 %/s de 2.90 à 4.98 ; 4.98 à 5.12 whip vers la droite (power2.in, +7000 u/s à la couture).
  COUCHES ET PROFONDEUR : avant-plan les pouces des mains nets devant la page, et le bord flou de P8 ; sujet la page du début ; fond le papier de P7 ; couches animées 3 (mains, couleurs, caméra).
  OBJET-PONT ET VECTEUR : la goutte accent de la page du début, redevenue bordeaux, annonce la goutte de la signature (séquence 11) ; vecteur : whip vers la droite repris par la séquence 11.
  SON : pinceau 41.76 global (3.62 local) ; whoosh court 43.10 global (4.96 local).
  IMAGE CLÉ : 4.40 : deux mains peintes qui tiennent la page du début, lampe ocre, écran ocre pâle, goutte bordeaux, tout en couleur, « le leur » souligné d'un trait ocre.

## Frame 11 : Antoine Contino, formateur IA · 43.26 → 47.60

- scene: Le whip atterrit sur la page P8, nue : la même goutte d'encre bordeaux qu'au début tombe et la signature « Antoine Contino » se trace depuis elle, « formateur IA » s'écrit dessous ; la caméra descend vers une tache ocre qui tombe et sèche en bouton « Réserver un appel » avec les deux adresses ; le curseur entre en courbe
- duration: 4.34s
- transition_in: cut
- status: outline
- src: compositions/frames/11-signature.html
- voiceover: "Antoine Contino, formateur IA. Réservez un appel."
- type: cta
- blueprint: logo-assemble-lockup (Adapt)
- focal: la signature qui se trace, puis le bouton ocre
- rules: svg-path-draw, cursor-click-ripple
- world: light
- handoff_in: à 0.00 : cam(12380, 540, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P7 : le carnet refermé sur la page du début colorée dans les mains ; P8 vide (papier nu) ; sous-titre sorti ; grain 55 %
- handoff_out: à 4.34 : cam(12988, 600, 1.0) flou 0 ; dérive x +12 u/s, échelle +1 %/s ; monde : carnet, page P8 ; signature « Antoine Contino » tracée en accent à (12988, 380), « formateur IA » à (12988, 470), bouton ocre « Réserver un appel » à (12988, 660), adresses à (12988, 760) ; le curseur à (13230, 790) en plein mouvement courbe vers la pointe du bouton (13060, 672), reste 0,20 s de trajet power3.out ; sous-titre « Réservez un appel. » en place, boîte sur « Réservez » ; grain 55 %

Word cues: Antoine@0.32 Contino@0.80 formateur@1.51 IA@2.20 Réservez@2.92 un@3.52 appel@3.72

Scene 1 (0.00 à 2.60 s) : P26, la goutte revient, la signature se trace
  TEXTE ÉCRAN : sous-titre « Antoine Contino, [boîte : formateur IA]. » (Antoine 0.32, Contino 0.80, boîte tracée 1.47, formateur 1.51, IA 2.20) ; il sort de 2.46 à 2.60 ; écart : la goutte touche 0,08 s avant « Antoine », la signature s'écrit sur le nom.
  IMAGE DE DÉPART : handoff_in (le whip en cours, P8 nue arrive de la droite).
  ÉTAPES : 0.00 à 0.24 fin du whip, atterrissage sur cam(12988, 400, 1.15) (expo.out, flou 12 → 0) : la page nue ; 0.10 la goutte accent arrive de la caméra (×4, flou 10, 0,16 s), même geste qu'à 0.02 du film ; 0.24 impact à (12560, 330), deux éclaboussures ; 0.32 « Antoine » : la signature « Antoine Contino » se trace depuis la goutte (masque qui avance de gauche à droite, 1,0 s power1.inOut, encre accent) ; 0.80 « Contino » : le tracé passe le « C » ; 1.32 la signature est complète ; 1.40 elle sèche (aqDry 0 → 1, 0,5 s : l'encre fonce) ; 1.51 « formateur » : « formateur IA » se révèle dessous en DM Sans ink-2 (masque, 0,3 s) ; 2.20 « IA » : la traînée de la goutte s'allonge sous la signature (tracé 0,2 s) ; 2.46 le sous-titre sort ; 2.50 départ du cran vers le bas.
  PISTE CAMÉRA : atterrissage 0.00 à 0.24 ; dérive x +12 u/s, échelle +1 %/s de 0.24 à 2.50 ; 2.50 à 2.80 cran vers cam(12988, 600, 1.0) (expo.inOut, flou 6 px).
  COUCHES ET PROFONDEUR : avant-plan la goutte en vol puis le bord du carnet flou coupé par le bord droit ; sujet la signature nette ; fond le papier et le bureau ; couches animées 2 à 3 (tracé, séchage, caméra).
  OBJET-PONT ET VECTEUR : le cran descend de la signature au bouton ; la goutte posée reste au début de la signature.
  SON : goutte 43.50 global (0.24 local) ; stylo 43.60 à 44.60 global (0.34 à 1.34 local : la signature).
  IMAGE CLÉ : 1.00 : la page nue, la goutte bordeaux à gauche et la signature « Antoine Contino » à moitié tracée depuis elle, à l'encre encore humide.

Scene 2 (2.60 à 4.34 s) : P27, la tache ocre sèche en bouton, le curseur entre
  TEXTE ÉCRAN : sous-titre « [boîte : Réservez] un appel. » (boîte tracée 2.88, Réservez 2.92, un 3.52, appel 3.72) ; il reste en place ; écart : la tache tombe 0,3 s avant « Réservez », le bouton est lisible sur « appel ».
  ÉTAPES : 2.60 à 2.80 fin du cran sur le milieu bas de la page ; 2.64 une goutte ocre arrive de la caméra ; 2.78 impact à (12988, 660) : la tache s'ouvre ×0,2 → 1 (0,12 s) en forme allongée (520 × 110) ; 2.92 « Réservez » : la tache sèche (aqDry 0 → 1, 0,4 s) et le texte « Réserver un appel » se révèle dedans (masque, 0,25 s) ; 3.30 un cerne d'encre fin se trace autour (0,2 s) : c'est un bouton ; 3.52 « un » : les deux adresses se révèlent dessous (DM Sans 24 px ink-2, masque 0,3 s) : « calendly.com/antoine-cntno/30min · antoinecontino.fr/ecoles » ; 3.72 « appel » : le bouton se tasse (×1,02 → 1) ; 4.10 le curseur entre par le bas droit du cadre, à (13420, 980) en coordonnées monde, et commence son unique mouvement courbe vers la pointe du bouton (13060, 672) : 0,5 s power3.out en x, power2.out en y ; 4.34 couture : le curseur est à (13230, 790), il lui reste 0,20 s de trajet.
  PISTE CAMÉRA : dérive x +12 u/s, échelle +1 %/s de 2.80 à 4.34 (elle continue telle quelle dans la séquence 12).
  COUCHES ET PROFONDEUR : avant-plan le curseur net (il est le sujet qui arrive) et le bord du carnet flou ; sujet le bouton ; fond la signature floue (4 px) en haut ; couches animées 3 (tache, texte, curseur).
  OBJET-PONT ET VECTEUR : le curseur en plein mouvement traverse la couture : la séquence 12 reprend exactement sa position (13230, 790) et son reste de trajet (0,20 s power3.out vers (13060, 672)).
  SON : goutte 45.90 global (2.64 local).
  IMAGE CLÉ : 3.90 : la page de fin, la signature en haut, le bouton ocre « Réserver un appel » au centre, les deux adresses dessous, le curseur qui arrive du coin bas droit, « Réservez » en boîte.

## Frame 12 : Réserver un appel · 47.60 → 50.80

- scene: Le curseur finit sa courbe et clique le bouton : pression, la tache passe au bordeaux puis revient ocre, une onde s'ouvre ; la page tient, vivante (la granulation des taches dérive, le grain glisse, la traînée de la goutte sèche), puis le noir
- duration: 3.20s
- transition_in: cut
- status: outline
- src: compositions/frames/12-clic.html
- voiceover: ""
- type: cta
- blueprint: cta-morph-press (Adapt)
- focal: le bouton cliqué, puis la page entière qui tient
- rules: cursor-click-ripple, press-release-spring
- world: light
- handoff_in: à 0.00 : cam(12988, 600, 1.0) flou 0 ; dérive x +12 u/s, échelle +1 %/s ; monde : carnet, page P8 ; signature « Antoine Contino » tracée en accent à (12988, 380), « formateur IA » à (12988, 470), bouton ocre « Réserver un appel » à (12988, 660), adresses à (12988, 760) ; le curseur à (13230, 790) en plein mouvement courbe vers la pointe du bouton (13060, 672), reste 0,20 s de trajet power3.out ; sous-titre « Réservez un appel. » en place, boîte sur « Réservez » ; grain 55 %
- handoff_out: aucun (fin du film, noir à 50.80)

Word cues: (aucun mot : tenue de fin)

Scene 1 (0.00 à 3.20 s) : P28, le clic, la tenue vivante, le noir
  TEXTE ÉCRAN : sous-titre « [boîte : Réservez] un appel. » déjà en place ; il sort de 2.60 à 2.80 avec le reste ; écart : aucun mot.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.20 le curseur achève sa courbe (power3.out) jusqu'à la pointe sur le bouton (13060, 672) ; 0.25 clic : pression (curseur et bouton ×0,85, 0,06 s yoyo), la tache passe en accent (0,07 s) puis revient ocre (0,17 s), le texte reste ink ; 0.27 une onde accent s'ouvre depuis le point du clic (×0,2 → ×1,8, opacité 0,55 → 0, 0,45 s power1.out) ; 0.40 un cerne d'encre plus franc entoure le bouton (tracé 0,2 s) ; 0.60 le curseur s'écarte de 30 u vers le bas droit (0,4 s power3.out) et reste ; 0.80 à 2.60 tenue vivante : la granulation des taches dérive (le filtre #aq-soft des lavis glisse de 6 u sur 1,8 s, aller simple), le grain du papier glisse de 8 u/s, la traînée de la goutte sous la signature sèche (aqDry 0,6 → 1 en 1,2 s), l'ombre du carnet respire (opacité 0,14 → 0,18 → 0,14 sur 1,6 s, un cycle) ; 2.60 le sous-titre sort ; 2.70 à 3.20 le noir monte (un lavis canvas s'ouvre depuis le bas du cadre, scaleY 0 → 1,2 en 0,5 s power2.in, par-dessus tout) : noir à 3.20.
  PISTE CAMÉRA : dérive x +12 u/s, échelle +1 %/s de 0.00 à 2.70 ; 2.70 à 3.20 la dérive continue sous le noir.
  COUCHES ET PROFONDEUR : avant-plan le curseur net ; sujet le bouton puis la page entière ; fond le bureau grainé ; couches animées 2 à 3 (onde, granulation, grain) ; aucune image figée.
  OBJET-PONT ET VECTEUR : aucun (fin du film) : le lavis noir qui monte rejoue l'encre du pivot.
  SON : clic 47.85 global (0.25 local).
  IMAGE CLÉ : 0.40 : le bouton ocre pressé avec le curseur dessus, l'onde bordeaux qui s'ouvre, la signature au-dessus, les deux adresses dessous.
