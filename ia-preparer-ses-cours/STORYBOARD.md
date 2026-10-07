---
format: 1920x1080
duration: "50.60s"
message: "Préparés avec l'IA, vos cours redeviennent vivants, et vos étudiants apprennent à s'en servir pour progresser."
arc: Hook → Problem → Pivot → Turn → Demo → Payoff → Reassurance → CTA
audience: "enseignants et formateurs (lycées, écoles, universités) et les directions qui les accompagnent, sur la page LinkedIn d'Antoine Contino, formateur IA"
mode: autonomous
captions: disabled
music: "pre-mixed with voice and SFX in assets/audio/mix.wav (mounted at root by the orchestrator)"
direction: "A « Le carnet » (DIRECTIONS.md), héritée du film 1 validé par Antoine le 7 octobre 2026"
styleframes: "../ia-etudiants/styleframes/png/A1.png, A2.png, A3.png et ../ia-etudiants/planches/2026-10-07-planche-finale.jpg (le rendu final du film 1)"
patterns: ../patterns/STORYBOARD-CRAFT.md, ../patterns/PATTERNS.md
---

## Video direction

- **Un seul monde** (frame.md) : le carnet d'un enseignant, huit pages parcourues de gauche à droite, même géométrie que les films 1 et 2. Séquences 1 à 5 = DOULEUR sur les pages P1 (le bureau du prof), P2 (la salle dans la pénombre) et P3 (la porte et le tableau), lavées de gris ; séquence 6 = PIVOT dans le noir de la goutte d'encre ; séquences 7 à 12 = SOLUTION sur les pages P4 à P7 qui se colorent ; séquences 13 et 14 = FIN sur la page P8. Chaque séquence peint son propre fond (bureau paper-dark + pages) sur un calque `class="clip"` de toute sa durée.
- **Coutures invisibles** : toutes les séquences entrent en `cut` ; chaque couture tombe au sommet du flou d'un mouvement de caméra (whip, cran, plongée) ou dans le mouvement du curseur, et le `handoff_out` de la séquence N est recopié mot pour mot dans le `handoff_in` de N+1. Exception voulue : 20.42, coupe franche à l'impact de la goutte ocre (le cadre entier est le lavis ocre des deux côtés) : du noir du pivot au papier du bureau coloré.
- **Texte** (lisible sans le son) : chaque phrase de la voix est un sous-titre `.aq-sub` en bas au centre (bande y 890 à 980, rien d'autre dedans), mot par mot sur les temps de chaque séquence (`mot@secondes`, temps locaux), 45 signes au plus par morceau (la longue phrase des quatre vignettes se joue en quatre morceaux, un par vignette). Un seul mot ou groupe par phrase dans la boîte bordeaux ([boîte : …]). Aucun autre texte coloré. Un seul moment typographique : « Et si vous la faisiez entrer dans le cours ? » au pivot, centré sur le noir sur deux lignes, 84 px, sans sous-titre pendant ce temps.
- **Pics** : 4 traits de pinceau ocre [trait : …] : « entrer » (17.52), « préparer » (21.62), « progresser » (32.56), « vivant » (41.16).
- **Une seule chose à regarder** : chaque plan isole le sujet de la phrase ; la caméra va de gauche à droite dans le carnet ou s'enfonce (portable, premier rang, panneau, goutte, écran, bouton), jamais d'aller-retour ; marges gauche et droite égales ; aucun décor sans sens ; au cadrage de référence de chaque plan, tout objet de la page reste au-dessus de y 880 à l'écran (frame.md § framings).
- **Vraies interfaces** : aucune (BRIEF.md) : la fenêtre de chat, le plan de cours et la diapositive sont génériques et dessinés à l'encre, sans nom d'outil ; leurs textes sont des traits.
- **Parallaxe** (une par acte au moins) : pendant chaque dérive, l'avant-plan flou (bord de la page suivante, goutte en vol, main, stylo) glisse 2,5 fois plus vite que la page, le bureau 0,4 fois.
- **Grammaire de mouvement** : deux vitesses, gestes de 1 à 6 images (expo.out) et dérives linéaires qui ne s'arrêtent jamais ; la zone 0,3 à 0,9 s est réservée à la caméra et au curseur (expo, power3, power4) ; les taches naissent d'une goutte ou d'un coup de pinceau et sèchent, jamais en fondu ; les traits se tracent ; aucune tenue figée ; aucune transition « effet ».
- **Texte visible** : exactement le texte cité dans les lignes Scene et les composants de frame.md, rien d'autre.
- **Négatifs** : diaporama (tout à t = 0), écran de veille, tache dédoublée, texte coloré à la place de la boîte, grande phrase, mot géant, titre qui répète la voix, symbole abstrait, curseur qui hésite, plusieurs objets qui bougent pendant une couture, outil d'IA nommé, nom d'élève ou de prof, chiffre écrit.

**MONDE**
- Carnet (14 700 × 1 080 u, frame.md § world) sur le bureau paper-dark grainé : P1 (850, 540) le bureau du prof · P2 (2584, 540) la salle dans la pénombre · P3 (4318, 540) la porte et le tableau · P4 (6052, 540) le bureau coloré, le plan de cours · P5 (7786, 540) les quatre vignettes · P6 (9520, 540) l'étudiant et le plan manuscrit · P7 (11254, 540) la salle en couleur · P8 (12988, 540) la signature et le bouton. Reliures à x = 1700 + (k - 1) × 1734.
- Pivot (16.40 à 20.42) : l'intérieur de la goutte d'encre, ground-ink (canvas, ondes sombres qui s'élargissent), la question centrée sur deux lignes.
- Couleurs de rôle : accent bordeaux = boîte du mot clé, goutte signature, cercle barré du panneau, rature du plan, bulle et points de droite, signature finale ; ocre = la couleur qui revient (4 traits, écrans des téléphones, lueur de la porte, marge de l'IA, vignettes, réflexes, élèves, bouton) ; gris de lavis = la douleur (pénombre, diapositives, craie pâlie, élèves gris) ; brun = bureau, rebord du tableau, tables ; encre = traits et texte ; craie = paper sur le tableau.

**SIGNATURES**
- Mécanisme 1 « la goutte » (frame.md, drop : elle tombe, s'ouvre en tache, sèche en objet) : 0.00 goutte grise qui sèche en lampe · 16.14 la caméra plonge dans la goutte du bas de P3 (noir) · 20.35 goutte ocre sur le noir qui ouvre P4 · 32.70 goutte ocre sur le cahier de l'étudiant · 43.54 goutte accent qui trace la signature · 46.08 goutte ocre qui sèche en bouton (6 occurrences, plus les deux éclaboussures de chacune).
- Mécanisme 2 « le séchage » (aqDry : l'anneau fonce, l'objet devient net ; inverse aqErase : la couleur pâlit puis la tache s'efface par le centre) : 0.44 la lampe · 0.68 les éclaboussures · 15.80 la craie (inverse) · 20.42 le bureau coloré · 23.90, 25.18, 26.78, 28.52 les quatre vignettes · 33.43 la tache du cahier · 39.70, 39.96 la diapositive projetée (inverse) · 40.75 les téléphones gris (inverse) · 46.23 le bouton · 46.83 la traînée de la goutte (13 occurrences).
- Registres de texte : sous-titre mot à mot = gris flou → net (0,14 s) puis encre (0,2 s) ; boîte = tracée depuis la gauche (0,16 s power3.out) ; trait = pinceau depuis la gauche (0,4 s power2.out) ; moment typographique = lettres qui convergent (0,5 s expo.out) ; notes Caveat et lignes manuscrites = révélées par un masque qui avance (vitesse d'une main, 0,2 à 1,0 s).
- Rimes : la salle en couleur aux bras levés (40.38) rejoue la salle grise aux téléphones (5.80) ; le bureau coloré du plan de cours (20.42) rejoue le bureau gris des diapositives (0.00) ; les traits ocre de la correction (29.08) et du plan manuscrit (37.40) rejouent la marge de l'IA (22.12) ; la goutte de la signature (43.54) est celle des trois films.

**PARTITION CAMÉRA** (temps globaux) : 0.00 dérive sur P1 · 1.10 cran vers le portable · 2.90 cran vers la pile · 4.52 whip P1 → P2 (couture 4.60) · 4.82 atterrissage P2 · 8.36 cran vers le premier rang (couture 8.50) · 10.50 whip P2 → P3 (couture 10.65) · 10.85 atterrissage sur la porte · 11.75 cran vers le panneau · 13.26 cran vers le tableau (couture 13.40) · 16.14 plongée dans la goutte (couture 16.40) · 16.40 dérive d'échelle sur le noir · 18.60 recul lent · 20.35 impact, coupe 20.42 · 20.42 le papier s'ouvre, dérive sur P4 · 21.72 cran vers l'écran · 23.40 whip P4 → P5 (couture 23.50) · 23.72 atterrissage sur les vignettes 1 et 2 · 26.36 cran vers les vignettes 3 et 4 (couture 26.50) · 29.90 whip P5 → P6 (couture 30.00) · 30.22 atterrissage sur l'étudiant · 34.96 cran vers le plan manuscrit (couture 35.10) · 39.40 whip P6 → P7 (couture 39.55) · 39.77 atterrissage sur la salle · 41.69 cran vers le prof · 43.35 whip P7 → P8 (couture 43.50) · 43.72 atterrissage sur la signature · 45.86 cran vers le bouton · 47.50 couture dans le mouvement du curseur · 50.10 le noir monte.

**VOIX** : minutage dans onsets.json (DIRECTIONS.md). Silences de plus de 0,4 s, chacun écrit comme un plan : 0.84 à 1.29 (le cran vers le portable, la lueur de la lampe) · 4.38 à 4.81 (le whip vers la salle) · 8.38 à 10.79 (gag muet : le pouce répond au chat, la diapositive défile, whip) · 13.16 à 13.56 (le cran vers le tableau) · 16.10 à 16.51 (la plongée dans la goutte, le noir) · 18.49 à 20.50 (le pivot : la question tient, la goutte ocre tombe, le papier s'ouvre) · 23.28 à 23.69 (whip vers les vignettes) · 29.68 à 30.27 (whip vers l'étudiant) · 43.26 à 43.69 (whip vers la signature, la goutte tombe) · 47.26 à 50.60 (clic, tenue vivante, noir).

**COUPES** (voix narrative, quota 0 à 4) : 20.42 · « Je » (20.50) · changement d'acte, du pivot à la solution, à l'impact de la goutte ocre (le cadre est le lavis ocre des deux côtés). Toutes les autres jonctions sont des coutures de caméra ou d'objet.

**RYTHME** : douleur (0 à 16.40) 11 plans = 6,7 plans / 10 s ; pivot 2 plans ; solution (20.42 à 43.50) 12 plans = 5,2 plans / 10 s ; fin (43.50 à 50.60) 3 plans = 4,2 plans / 10 s.

**SON** (proposition, verrouillée à l'étape 5 ; l'image ne bouge pas pour le son ; 7 whooshes, 1 scintillement) : goutte 0.00 · stylo 0.28 à 1.10 (le bureau se dessine) · papier 1.29 (le portable) · clic 1.42 · click-soft 2.18, 2.80 (la diapositive défile) · papier 3.15, 3.28, 3.36, 3.44 (la pile) · stylo 3.90 (la note) · whoosh court 4.52 · pinceau 4.81 (la pénombre) · pops 5.80, 6.18, 6.30, 6.42, 6.54, 6.66 (les écrans) · click-soft 6.68 · papier 7.66 (dans la poche) · click-soft 8.90, 9.40 (le pouce) · clic 9.10, 9.80 (la diapositive) · whoosh court 10.50 · papier 10.96 (le panneau) · stylo 11.15 (le cercle barré) · pinceau 12.05 (la lueur) · pops 12.54, 12.60 · papier 12.72 (le panneau gondole) · stylo 13.78, 13.96, 14.30 (la craie) · papier 14.84 (la main sort) · pops 15.08, 15.32, 15.37, 15.42, 15.47, 15.52 (les poches) · pinceau 15.80 (la craie pâlit) · whoosh cinématique 16.14 · goutte grave 16.40 · goutte 20.20 · impact grave 20.42 · pinceau 20.42 (le lavis sèche) · stylo 20.82 (la lampe) · papier 20.92 (le portable) · stylo 21.24 à 21.82 (les lignes) · pinceau 22.12, 22.18, 22.24, 22.30 (la marge) · stylo 22.56 (la rature), 22.78 (la réécriture) · whoosh court 23.40 · pinceau 23.69 · stylo 23.94 · pops 24.16, 24.22, 24.28, 24.34 · pinceau 24.97 · stylo 25.24, 25.52, 25.72 · pinceau 26.57 · stylo 26.82, 27.10, 27.16, 27.22, 27.28 · pops 27.46 à 27.67 · pinceau 28.31 · stylo 28.56 · papier 28.80 · stylo 29.08, 29.16 · whoosh court 29.90 · papier 30.54 · key-press 31.14, 31.30, 31.46 · pinceau 31.48 · stylo 32.00, 32.20 · goutte 32.70 · pinceau 33.43 · stylo 33.62, 33.95 · papier 35.26 · stylo 35.62 à 35.97, 36.54 à 36.89 · pinceau 37.40, 37.50, 37.60, 37.70 · papier 37.80 · stylo 38.10 · whoosh court 39.40 · pinceau 39.96, 40.38 à 40.85, 41.16 · pinceau 41.87 (le prof) · scintillement 42.05 · pinceau 42.94 · whoosh court 43.35 · goutte 43.54 · stylo 43.69 à 44.69 (la signature) · goutte 46.08 · pinceau 46.23 · stylo 46.60 · clic 47.75.

## Frame 1 : Mardi soir, le même cours · 0.00 → 4.60

- scene: Sur la page P1 du carnet, le bureau du prof se dessine à l'encre autour d'une goutte grise qui sèche en lampe allumée ; le portable montre une diapositive, la pile à côté porte la même, datée « l'an dernier » ; la caméra passe du portable à la pile puis part en whip vers la salle
- duration: 4.60s
- transition_in: cut
- status: outline
- src: compositions/frames/01-mardi.html
- voiceover: "Mardi soir. Vous préparez le cours de demain. Le même que l'an dernier."
- type: hook
- blueprint: camera-journey (Adapt)
- focal: la goutte qui sèche en lampe, puis la diapositive du portable et la pile identique
- rules: depth-of-field-blur, svg-path-draw
- world: light
- handoff_in: aucun (ouverture du film) ; première image = la page P1 au cadrage cam(850, 540, 1.0) flou 0 : le bureau paper-dark grainé, la page nue, aucun objet encore ; sous-titre vide ; grain 55 %
- handoff_out: à 4.60 : cam(1300, 600, 1.1) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P1 (desk-prof) : bande de bureau brune à y 860, lampe allumée au pied (260, 800) ×0,9 et sa lueur ocre-2 pâle, portable à (850, 575) dont l'écran montre la diapositive (bloc de titre gris, cinq lignes grises), pile de quatre diapositives identiques à (1350, 620) (rotations 4°, 9°, 13°, 18°), notes Caveat « mardi soir » à (300, 96) et « l'an dernier » à (1240, 540), deux lavis gris de la nuit en haut ; P2 encore nette au cadrage de référence : la salle dans la pénombre (lavis gris-lavis à 35 % sur la page), tableau à (2584, 300) avec la diapositive projetée, cinq rangs de six élèves gris-lavis (x = 1934 + j × 260, y = 500, 580, 660, 740, 820), trente téléphones éteints (taches gris-lavis-2 26 × 40 aux mains, opacité 0,5) ; sous-titre sorti ; grain 55 %

Word cues: Mardi@0.00 soir@0.50 Vous@1.29 préparez@1.56 le@1.94 cours@2.18 de@2.32 demain@2.58 Le@3.15 même@3.52 que@3.72 l'an@3.90 dernier@4.14

Scene 1 (0.00 à 1.20 s) : P1, la goutte sèche en lampe, le bureau se dessine
  TEXTE ÉCRAN : sous-titre « [boîte : Mardi] soir. » (boîte tracée 0.00, Mardi 0.00, soir 0.50) ; il sort de 1.10 à 1.24 ; écart synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 la boîte se trace et une goutte grise arrive de la caméra (×4, flou 10 px, 0,16 s power2.in) vers le pied de la lampe (260, 800) ; 0.16 impact : la tache s'ouvre ×0,2 → ×1 (0,12 s expo.out), deux éclaboussures ; 0.28 la bande du bureau se dessine à l'encre (tracé 0,5 s power2.out, de gauche à droite) et son lavis brun suit (coup de pinceau) ; 0.44 la tache sèche en lampe (aqDry 0 → 1, 0,5 s) et le pied puis le bras de la lampe se tracent par-dessus (0,3 s) ; 0.50 « soir » : la lueur ocre-2 pâle s'ouvre sous l'abat-jour (×0,2 → 1, 0,12 s) ; 0.68 les deux éclaboussures sèchent (0,2 s) ; 0.80 la note Caveat « mardi soir » se révèle (masque 0,3 s) ; 0.96 les deux lavis gris de la nuit montent en haut (coup de pinceau, 0,2 s chacun) ; 1.10 départ du cran vers le portable (expo.inOut, 0,3 s, flou 0 → 6 → 0).
  PISTE CAMÉRA : dérive x +24 u/s, échelle +2 %/s de 0.00 à 1.10 ; cran de cam(850, 540, 1.0) vers cam(850, 560, 1.4) de 1.10 à 1.40.
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P2 (7 px) coupé par le bord droit et la goutte en vol ; sujet la lampe puis le bureau nets ; fond le bureau paper-dark grainé ; couches animées 3.
  OBJET-PONT ET VECTEUR : la lueur de la lampe éclaire le portable du plan 2 ; le cran suit la bande du bureau vers la droite.
  SON : goutte 0.00 ; stylo de 0.28 à 1.10 (le bureau se dessine).
  IMAGE CLÉ : 1.00 : le bureau à l'encre, la lampe allumée séchée en gris à gauche, la note « mardi soir », deux lavis gris en haut, « Mardi » en boîte.

Scene 2 (1.20 à 3.00 s) : P2, le portable et sa diapositive
  TEXTE ÉCRAN : sous-titre « Vous préparez le cours de [boîte : demain]. » (Vous 1.29, préparez 1.56, le 1.94, cours 2.18, de 2.32, boîte tracée 2.54, demain 2.58) ; il sort de 2.90 à 3.04 ; écart : la diapositive se pose sur « préparez » (1.56), synchro.
  ÉTAPES : 1.20 à 1.40 fin du cran sur cam(850, 560, 1.4) ; 1.29 « Vous » : le portable se pose sur le bureau (kit aqLaptop, ×1,1 flou 6 → net, 0,12 s) ; 1.42 son écran s'allume en gris (lavis gris-lavis ×0,2 → 1 depuis le centre, 0,12 s) ; 1.56 « préparez » : la diapositive se dessine dans l'écran (rectangle paper-2 420 × 240 tracé 0,2 s) ; 1.74 le bloc de titre gris se pose (×1,1 flou 4 → net, 0,1 s) ; 1.94 « le » : cinq lignes grises se révèlent (masque, 0,06 s d'écart) jusqu'à 2.26 ; 2.18 « cours » : la diapositive défile (la carte glisse de x -420 et la même revient de x +420, 0,18 s power2.in) ; 2.40 la lueur de la lampe vacille (opacité 0,75 → 0,6 → 0,75, 0,16 s) ; 2.58 « demain » : la lueur de la lampe se tasse (×1,02 → 1) ; 2.80 la diapositive défile une seconde fois, identique ; 2.90 départ du cran vers la pile (expo.inOut, 0,3 s, flou 0 → 6 → 0).
  PISTE CAMÉRA : dérive x +18 u/s, échelle +1,5 %/s de 1.40 à 2.90 ; cran vers cam(1350, 620, 1.5) de 2.90 à 3.20.
  COUCHES ET PROFONDEUR : avant-plan le bord de la lampe flou (6 px) coupé par le bord gauche ; sujet l'écran du portable net ; fond la page et le bureau grainé ; couches animées 3.
  OBJET-PONT ET VECTEUR : la diapositive qui défile à l'écran est celle de la pile du plan 3 ; le cran suit le bureau vers la droite.
  SON : papier 1.29 (le portable) ; clic 1.42 ; click-soft 2.18, 2.80 (la diapositive défile).
  IMAGE CLÉ : 2.40 : l'écran du portable et sa diapositive grise (bloc de titre, cinq lignes), la lueur de la lampe au bord gauche, « demain » en boîte.

Scene 3 (3.00 à 4.60 s) : P3, la pile identique, « l'an dernier », whip vers la salle
  TEXTE ÉCRAN : sous-titre « Le [boîte : même] que l'an dernier. » (Le 3.15, boîte tracée 3.48, même 3.52, que 3.72, l'an 3.90, dernier 4.14) ; il sort de 4.42 à 4.56 ; écart : la note se révèle sur « l'an » (3.90), synchro.
  ÉTAPES : 3.00 à 3.20 fin du cran sur cam(1350, 620, 1.5) ; 3.15 « Le » : la première diapositive de la pile glisse depuis la droite (x +400 → 0, flou 6 → net, 0,14 s power2.in) ; 3.28 à 3.52 trois autres glissent dessus (0,08 s d'écart, rotations 9°, 13°, 18°) ; 3.52 « même » : la pile se tasse (×1 → 0,99) ; 3.66 les blocs de titre et les lignes grises des cartes visibles se révèlent (masque 0,2 s) ; 3.90 « l'an » : la note Caveat « l'an dernier » se révèle sur le coin de la carte du dessus (1240, 540) (masque 0,3 s, penchée de -3°) ; 4.14 « dernier » : la carte du dessus se soulève de 6 u et retombe (0,1 s) ; 4.30 un lavis gris à 20 % se pose sur la pile (coup de pinceau, 0,2 s) ; 4.52 départ du whip vers P2 (power2.in, flou 0 → 12).
  PISTE CAMÉRA : dérive x +16 u/s, échelle +1,5 %/s de 3.20 à 4.52 ; whip de cam(1350, 620, 1.5) vers cam(2584, 540, 1.0) de 4.52 à 4.82 (power2.in puis expo.out, +7000 u/s au milieu).
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P2 (7 px) coupé par le bord droit ; sujet la pile nette ; fond la page et le bureau grainé ; couches animées 3.
  OBJET-PONT ET VECTEUR : la diapositive de la pile est celle qui sera projetée au tableau de P2 ; le whip va vers la droite.
  SON : papier 3.15, 3.28, 3.36, 3.44 (les cartes) ; stylo 3.90 (la note) ; whoosh court 4.52.
  IMAGE CLÉ : 4.10 : la pile de quatre diapositives identiques, la note « l'an dernier » sur le coin de la première, le portable flou à gauche, « même » en boîte.


## Frame 2 : Trente téléphones dans la pénombre · 4.60 → 8.50

- scene: Le whip atterrit sur la page P2 : la salle vue du fond, dans la pénombre grise, le tableau avec la même diapositive ; sur « trente téléphones », trente écrans s'allument en ocre par vagues, puis descendent dans les poches ; cran vers le premier rang
- duration: 3.90s
- transition_in: cut
- status: outline
- src: compositions/frames/02-telephones.html
- voiceover: "Dans la salle, trente téléphones ont déjà l'IA dans la poche."
- type: problem
- blueprint: camera-journey (Adapt)
- focal: la salle grise, puis les trente écrans ocre qui s'allument
- rules: depth-of-field-blur, waterfall-entry
- world: light
- handoff_in: à 0.00 : cam(1300, 600, 1.1) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P1 (desk-prof) : bande de bureau brune à y 860, lampe allumée au pied (260, 800) ×0,9 et sa lueur ocre-2 pâle, portable à (850, 575) dont l'écran montre la diapositive (bloc de titre gris, cinq lignes grises), pile de quatre diapositives identiques à (1350, 620) (rotations 4°, 9°, 13°, 18°), notes Caveat « mardi soir » à (300, 96) et « l'an dernier » à (1240, 540), deux lavis gris de la nuit en haut ; P2 encore nette au cadrage de référence : la salle dans la pénombre (lavis gris-lavis à 35 % sur la page), tableau à (2584, 300) avec la diapositive projetée, cinq rangs de six élèves gris-lavis (x = 1934 + j × 260, y = 500, 580, 660, 740, 820), trente téléphones éteints (taches gris-lavis-2 26 × 40 aux mains, opacité 0,5) ; sous-titre sorti ; grain 55 %
- handoff_out: à 3.90 : cam(2454, 800, 1.8) flou 7 px ; caméra en plein cran vers le premier rang (-360 u/s en x, +700 u/s en y, échelle +2,2/s, expo.inOut), dérive 0 ; monde : carnet, page P2 (classroom) : la pénombre, trente écrans allumés en ocre (opacité 0,85) descendus de 20 u dans les poches, tableau avec la diapositive projetée (la même), élèves gris-lavis ; sous-titre sorti ; grain 55 %

Word cues: Dans@0.21 la@0.44 salle@0.70 trente@1.20 téléphones@1.58 ont@2.08 déjà@2.26 l'IA@2.70 dans@3.06 la@3.30 poche@3.54

Scene 1 (0.00 à 1.10 s) : P4, la salle dans la pénombre
  TEXTE ÉCRAN : sous-titre « Dans la salle, » (Dans 0.21, la 0.44, salle 0.70) ; il reste et se complète au plan 2 ; écart : la salle est déjà là à l'atterrissage, le lavis de la nuit se pose sur « Dans » (0.21), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.22 fin du whip, atterrissage sur cam(2584, 540, 1.0) (expo.out, flou 12 → 0) : la salle grise au complet ; 0.21 « Dans » : le lavis gris de la pénombre s'épaissit (opacité 0,35 → 0,45, coup de pinceau depuis le haut, 0,3 s) ; 0.44 « la » : la diapositive projetée se tasse (×1,02 → 1) ; 0.70 « salle » : les trente élèves se penchent de 2° vers l'avant (0,02 s d'écart par colonne) ; 0.90 le tableau se tasse ; 1.00 le rebord brun du tableau se dessine (tracé 0,2 s).
  PISTE CAMÉRA : atterrissage expo.out de 0.00 à 0.22 ; dérive x +20 u/s, échelle +1,5 %/s de 0.22 à 3.76.
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P3 (7 px) coupé par le bord droit ; sujet les rangs d'élèves et le tableau nets ; fond la pénombre grise sur la page ; couches animées 2.
  OBJET-PONT ET VECTEUR : la diapositive projetée est celle du portable et de la pile de P1 ; les élèves gris portent les téléphones du plan 2.
  SON : pinceau 0.21 (la pénombre).
  IMAGE CLÉ : 1.00 : la salle vue du fond, cinq rangs de six élèves gris, le tableau avec la même diapositive, la pénombre, « Dans la salle, » en sous-titre.

Scene 2 (1.10 à 3.90 s) : P5, trente écrans s'allument, dans la poche, cran vers le premier rang
  TEXTE ÉCRAN : sous-titre « trente téléphones ont déjà [boîte : l'IA] dans la poche. » (trente 1.20, téléphones 1.58, ont 2.08, déjà 2.26, boîte tracée 2.66, l'IA 2.70, dans 3.06, la 3.30, poche 3.54) ; il sort de 3.80 à 3.94 ; écart : les écrans s'allument sur « téléphones » (1.58), synchro.
  ÉTAPES : 1.20 « trente » : le premier écran du fond s'allume (tache ocre ×0,2 → 1, 0,12 s expo.out) ; 1.58 « téléphones » : les vingt-neuf autres s'allument par vagues de rang en rang (cinq vagues de six, 0,12 s d'écart entre les rangs, 0,02 s dans le rang) jusqu'à 2.10 ; 2.08 « ont » : la diapositive projetée défile, identique (0,18 s power2.in) ; 2.26 « déjà » : la pénombre se referme d'un cran autour des écrans (vignettage +10 %, 0,3 s) ; 2.70 « l'IA » : les trente écrans s'avivent (opacité 0,6 → 0,85, 0,1 s) ; 3.06 « dans » : les écrans descendent de 20 u (y +20, 0,16 s power2.in, 0,02 s d'écart par colonne) ; 3.30 « la » : les élèves se redressent (rotation 2° → 0) ; 3.54 « poche » : les écrans se tassent (×1,02 → 1) ; 3.76 départ du cran vers le premier rang (expo.inOut, flou 0 → 7).
  PISTE CAMÉRA : dérive x +20 u/s, échelle +1,5 %/s de 0.22 à 3.76 ; cran de cam(2584, 540, 1.0) vers cam(2454, 800, 1.8) de 3.76 à 4.04 (expo.inOut, flou 7 au milieu).
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P3 (7 px) coupé par le bord droit ; sujet les trente écrans ocre nets ; fond la pénombre et le tableau ; couches animées 3 à 4.
  OBJET-PONT ET VECTEUR : le téléphone du premier rang (2454, 820) devient le sujet du gag ; le cran descend vers lui.
  SON : pops 1.20, 1.58, 1.70, 1.82, 1.94, 2.06 (les vagues) ; click-soft 2.08 (la diapositive) ; papier 3.06 (dans la poche).
  IMAGE CLÉ : 2.80 : trente taches ocre allumées dans la salle grise, le tableau avec la diapositive, « l'IA » en boîte.


## Frame 3 : Le gag : le pouce répond au chat · 8.50 → 10.65

- scene: Dans le silence, la caméra finit son cran sur le téléphone du premier rang : une fenêtre de chat, un pouce qui tape deux fois, une réponse ocre ; au-dessus, floue, la diapositive défile deux fois, identique ; whip vers la page suivante
- duration: 2.15s
- transition_in: cut
- status: outline
- src: compositions/frames/03-gag.html
- voiceover: ""
- type: problem
- blueprint: cursor-ui-demo (Adapt)
- focal: le pouce sur la fenêtre de chat du premier rang
- rules: depth-of-field-blur, coordinate-target-zoom
- world: light
- handoff_in: à 0.00 : cam(2454, 800, 1.8) flou 7 px ; caméra en plein cran vers le premier rang (-360 u/s en x, +700 u/s en y, échelle +2,2/s, expo.inOut), dérive 0 ; monde : carnet, page P2 (classroom) : la pénombre, trente écrans allumés en ocre (opacité 0,85) descendus de 20 u dans les poches, tableau avec la diapositive projetée (la même), élèves gris-lavis ; sous-titre sorti ; grain 55 %
- handoff_out: à 2.15 : cam(3250, 600, 1.3) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x, échelle 1,8 → 1,0 en cours), dérive 0 ; monde : carnet ; P2 : la salle dans la pénombre, trente écrans ocre, la fenêtre de chat sur le téléphone du premier rang (2454, 820) avec sa ligne de réponse ocre, la diapositive projetée ; P3 au cadrage de référence : la porte fermée (door-sign à (3900, 540)) avec son panneau « IA interdite » et le cercle barré accent, aucune lueur dans la fente ; le tableau vide (board-ailleurs à (4700, 320)), six élèves gris (x = 4330 à 5080, y = 640 à 720) sans lueur, aucune main ; la goutte accent au bas de la page (5050, 820) ; sous-titre sorti ; grain 55 %

Word cues: (aucun mot ; gag muet de 8.38 à 10.79 global)

Scene 1 (0.00 à 1.50 s) : P6, le téléphone du premier rang, le pouce
  TEXTE ÉCRAN : aucun (gag muet).
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.14 fin du cran sur cam(2454, 800, 1.8) (expo.inOut, flou 7 → 0) : l'écran ocre du téléphone à (2454, 850) ; 0.16 la fenêtre de chat se dessine dans l'écran (aqWindow 26 × 40 en unités de page, tracée 0,2 s : une barre, un champ) ; 0.40 le pouce entre par le bas (main peinte ×0,4, y +60 → 0, 0,12 s power2.in) et tape (×0,9 yoyo 0,06 s) : un trait de texte ocre se révèle dans le champ (0,1 s) ; 0.60 la diapositive projetée défile au-dessus, floue (0,18 s) ; 0.90 le pouce tape une seconde fois : un second trait ; 1.10 une réponse ocre se révèle sous la barre (deux traits, 0,1 s d'écart) ; 1.30 la diapositive défile encore, identique ; 1.40 le pouce se retire par le bas (0,12 s power2.in).
  PISTE CAMÉRA : fin du cran expo.inOut de 0.00 à 0.14 ; dérive y -14 u/s, échelle +2 %/s de 0.14 à 2.00.
  COUCHES ET PROFONDEUR : avant-plan le dossier de la chaise du premier rang flou (6 px) coupé par le bord bas ; sujet le téléphone et le pouce nets ; fond le tableau et la diapositive flous (5 px) ; couches animées 3.
  OBJET-PONT ET VECTEUR : la diapositive qui défile au fond rejoue celle du portable ; la réponse ocre est la première action de l'IA du film.
  SON : click-soft 0.40, 0.90 (le pouce) ; clic 0.60, 1.30 (la diapositive).
  IMAGE CLÉ : 1.20 : le téléphone ocre en gros plan, la fenêtre de chat avec deux traits tapés et sa réponse, le pouce, la diapositive floue au-dessus.

Scene 2 (1.50 à 2.15 s) : P7, le tableau reste vide, whip vers la porte
  TEXTE ÉCRAN : aucun.
  ÉTAPES : 1.50 l'écran du téléphone s'avive une dernière fois (opacité 0,85 → 0,95 → 0,85, 0,2 s) ; 1.70 la diapositive projetée se tasse ; 2.00 départ du whip vers P3 (power2.in, flou 0 → 12, échelle 1,8 → 1,0 en cours).
  PISTE CAMÉRA : dérive y -14 u/s jusqu'à 2.00 ; whip de cam(2454, 800, 1.8) vers cam(3900, 540, 1.0) de 2.00 à 2.35 (power2.in puis expo.out, +7000 u/s au milieu).
  COUCHES ET PROFONDEUR : avant-plan le dossier flou ; sujet le téléphone ; fond le tableau flou ; couches animées 2.
  OBJET-PONT ET VECTEUR : le whip part du téléphone allumé vers la porte où l'IA est interdite.
  SON : whoosh court 2.00.
  IMAGE CLÉ : 2.08 : le cadre en plein whip, traînées horizontales, l'ocre des écrans et le gris de la salle filent vers la gauche.


## Frame 4 : Interdite, et pourtant · 10.65 → 13.40

- scene: Le whip atterrit sur la page P3, la porte de la classe : le panneau « IA interdite » se colle, son cercle barré se trace ; puis la porte s'entrebâille et la lueur ocre des écrans passe par la fente ; cran vers le tableau
- duration: 2.75s
- transition_in: cut
- status: outline
- src: compositions/frames/04-interdite.html
- voiceover: "Vous l'interdisez. Ils s'en servent quand même."
- type: problem
- blueprint: camera-journey (Adapt)
- focal: le panneau sur la porte, puis la lueur ocre dans la fente
- rules: depth-of-field-blur, svg-path-draw
- world: light
- handoff_in: à 0.00 : cam(3250, 600, 1.3) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x, échelle 1,8 → 1,0 en cours), dérive 0 ; monde : carnet ; P2 : la salle dans la pénombre, trente écrans ocre, la fenêtre de chat sur le téléphone du premier rang (2454, 820) avec sa ligne de réponse ocre, la diapositive projetée ; P3 au cadrage de référence : la porte fermée (door-sign à (3900, 540)) avec son panneau « IA interdite » et le cercle barré accent, aucune lueur dans la fente ; le tableau vide (board-ailleurs à (4700, 320)), six élèves gris (x = 4330 à 5080, y = 640 à 720) sans lueur, aucune main ; la goutte accent au bas de la page (5050, 820) ; sous-titre sorti ; grain 55 %
- handoff_out: à 2.75 : cam(4300, 540, 1.0) flou 7 px ; caméra en plein cran vers la droite (+900 u/s en x, expo.inOut), dérive 0 ; monde : carnet, page P3 : la porte entrebâillée (fente de 40 u à son bord droit), la lueur ocre-pale dans la fente (lavis 40 × 600 à (4130, 540)), le panneau « IA interdite » gondolé de 4°, le cercle barré accent ; le tableau vide, six élèves gris sans lueur, aucune main ; la goutte accent à (5050, 820) ; sous-titre sorti ; grain 55 %

Word cues: Vous@0.14 l'interdisez@0.31 Ils@1.40 s'en@1.61 servent@1.89 quand@2.07 même@2.33

Scene 1 (0.00 à 1.20 s) : P8, la porte et le panneau
  TEXTE ÉCRAN : sous-titre « Vous [boîte : l'interdisez]. » (Vous 0.14, boîte tracée 0.27, l'interdisez 0.31) ; il sort de 1.10 à 1.24 ; écart : le panneau se colle sur « l'interdisez » (0.31), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.20 fin du whip, atterrissage sur cam(3900, 540, 1.0) (expo.out, flou 12 → 0) : la porte fermée, le panneau déjà posé ; 0.14 « Vous » : la porte se tasse (×1,01 → 1) ; 0.31 « l'interdisez » : le panneau se recolle d'un coup (×1,1 flou 6 → net, 0,12 s) et ses quatre coins de ruban se posent (0,04 s d'écart) ; 0.50 le cercle barré accent se retrace par-dessus (tracé 0,3 s power2.out) ; 0.80 la note Caveat « IA interdite » se tasse (×1,02 → 1) ; 0.96 un lavis gris à 15 % se pose sur la porte (coup de pinceau depuis le haut, 0,2 s) ; 1.10 départ du cran vers le panneau (expo.inOut, 0,3 s, flou 0 → 6 → 0).
  PISTE CAMÉRA : atterrissage expo.out de 0.00 à 0.20 ; dérive x +12 u/s, échelle +1,5 %/s de 0.20 à 1.10 ; cran vers cam(3900, 400, 1.5) de 1.10 à 1.40.
  COUCHES ET PROFONDEUR : avant-plan le bord flou du tableau de droite (7 px) coupé par le bord droit ; sujet la porte et le panneau nets ; fond la page et le bureau grainé ; couches animées 3.
  OBJET-PONT ET VECTEUR : la fente de la porte (plan 2) est le bord droit de l'objet du plan 1 ; le cran monte vers le panneau.
  SON : papier 0.31 (le panneau) ; stylo 0.50 (le cercle barré).
  IMAGE CLÉ : 0.90 : la porte à l'encre, le panneau « IA interdite » et son cercle barré bordeaux, « l'interdisez » en boîte.

Scene 2 (1.20 à 2.75 s) : P9, la lueur dans la fente, cran vers le tableau
  TEXTE ÉCRAN : sous-titre « Ils s'en servent [boîte : quand même]. » (Ils 1.40, s'en 1.61, servent 1.89, boîte tracée 2.03, quand 2.07, même 2.33) ; il sort de 2.60 à 2.74 ; écart : la fente s'ouvre sur « Ils » (1.40), synchro.
  ÉTAPES : 1.20 à 1.40 fin du cran sur cam(3900, 400, 1.5) ; 1.40 « Ils » : la porte s'entrebâille : la fente de 40 u s'ouvre le long de son bord droit (lavis ocre-pale 40 × 600, scaleX 0 → 1 depuis le bord, 0,16 s expo.out) ; 1.61 « s'en » : la lueur s'avive (opacité 0,5 → 0,85, 0,1 s) ; 1.89 « servent » : deux taches ocre 26 × 40 paraissent dans la fente (impact ×0,2 → 1, 0,06 s d'écart) : des écrans derrière la porte ; 2.07 « quand » : le panneau gondole (rotation 0 → 4°, 0,2 s power2.out) ; 2.33 « même » : la lueur déborde de 12 u sur le bord de la porte (scaleX 1 → 1,3, 0,12 s) ; 2.50 la poignée se tasse ; 2.61 départ du cran vers la droite (expo.inOut, flou 0 → 7).
  PISTE CAMÉRA : dérive y -10 u/s, échelle +1 %/s de 1.40 à 2.61 ; cran de cam(3900, 400, 1.5) vers cam(4700, 520, 1.05) de 2.61 à 2.91 (expo.inOut, flou 7 au milieu).
  COUCHES ET PROFONDEUR : avant-plan le bord gauche de la porte flou (6 px) coupé par le bord gauche ; sujet la fente et sa lueur nets ; fond la page grainée ; couches animées 3.
  OBJET-PONT ET VECTEUR : la lueur ocre de la fente est celle des poches du plan suivant ; le cran va vers la droite.
  SON : pinceau 1.40 (la lueur) ; pops 1.89, 1.95 (les écrans) ; papier 2.07 (le panneau gondole).
  IMAGE CLÉ : 2.40 : le panneau gondolé, la fente de la porte avec sa lueur ocre et deux écrans, « quand même » en boîte.


## Frame 5 : Le cours avance, la classe est ailleurs · 13.40 → 16.40

- scene: Le cran atterrit sur le tableau de la page P3 : une main à la craie écrit pendant que six élèves, de dos, penchent la tête vers la lueur ocre de leur poche ; la craie pâlit ; la caméra plonge dans la goutte d'encre du bas de la page
- duration: 3.00s
- transition_in: cut
- status: outline
- src: compositions/frames/05-ailleurs.html
- voiceover: "Le cours avance au tableau, la classe est ailleurs."
- type: problem
- blueprint: comparison-split (Adapt)
- focal: la main à la craie, puis les six têtes penchées vers les poches
- rules: depth-of-field-blur, coordinate-target-zoom
- world: light
- handoff_in: à 0.00 : cam(4300, 540, 1.0) flou 7 px ; caméra en plein cran vers la droite (+900 u/s en x, expo.inOut), dérive 0 ; monde : carnet, page P3 : la porte entrebâillée (fente de 40 u à son bord droit), la lueur ocre-pale dans la fente (lavis 40 × 600 à (4130, 540)), le panneau « IA interdite » gondolé de 4°, le cercle barré accent ; le tableau vide, six élèves gris sans lueur, aucune main ; la goutte accent à (5050, 820) ; sous-titre sorti ; grain 55 %
- handoff_out: à 3.00 : cam(5050, 820, 14) flou 10 px ; caméra en pleine plongée (échelle ×2,2/s, power3.in) dans la goutte accent du bas de P3 ; la goutte couvre 95 % du cadre, son accent s'assombrit vers canvas au centre ; aucune silhouette visible ; sous-titre sorti ; grain 55 %

Word cues: Le@0.16 cours@0.38 avance@0.56 au@0.90 tableau@1.12 la@1.68 classe@1.92 est@2.16 ailleurs@2.40

Scene 1 (0.00 à 1.60 s) : P10, la craie avance au tableau
  TEXTE ÉCRAN : sous-titre « Le cours avance au tableau, » (Le 0.16, cours 0.38, avance 0.56, au 0.90, tableau 1.12) ; il reste et se complète au plan 2 ; écart : la craie trace sur « avance » (0.56), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.14 fin du cran sur cam(4700, 520, 1.05) (expo.inOut, flou 7 → 0) ; 0.20 la main à la craie entre par le bas droit (y +400 → 0, 0,18 s power2.out) jusqu'au tableau ; 0.38 « cours » : un premier trait de craie se trace (couleur paper, 0,4 s power1.inOut) ; 0.56 « avance » : un deuxième trait ; 0.90 « au » : un troisième, plus court ; 1.12 « tableau » : le cadre du tableau se tasse (×1,01 → 1) et le rebord brun fonce (0,2 s) ; 1.30 la main lève la craie (y -10, 0,1 s) ; 1.44 la main sort par le bas droit (y +400, 0,16 s power2.in).
  PISTE CAMÉRA : fin du cran expo.inOut de 0.00 à 0.14 ; dérive x +12 u/s, échelle +1 %/s de 0.14 à 2.74.
  COUCHES ET PROFONDEUR : avant-plan la main et la craie nettes, coupées par le bord bas ; sujet le tableau ; fond les six élèves et la page grainée ; couches animées 3.
  OBJET-PONT ET VECTEUR : les traits de craie pâlissent au plan 2 ; les élèves du fond deviennent le sujet.
  SON : stylo 0.38, 0.56, 0.90 (la craie) ; papier 1.44 (la main sort).
  IMAGE CLÉ : 1.20 : le tableau avec trois traits de craie, la main à la craie en bas à droite, six élèves gris de dos, « Le cours avance au tableau, » en sous-titre.

Scene 2 (1.60 à 3.00 s) : P11, les têtes se penchent vers les poches, plongée dans la goutte
  TEXTE ÉCRAN : sous-titre « Le cours avance au tableau, la classe est [boîte : ailleurs]. » (la 1.68, classe 1.92, est 2.16, boîte tracée 2.36, ailleurs 2.40) ; il sort de 2.72 à 2.86 ; écart : les têtes se penchent sur « classe » (1.92), synchro.
  ÉTAPES : 1.68 « la » : la lueur ocre de la première poche s'ouvre (tache 26 × 40, impact ×0,2 → 1, 0,12 s) ; 1.92 « classe » : les cinq autres poches s'allument (0,05 s d'écart) et les six têtes se penchent vers elles (rotation 0 → 8°, 0,16 s power2.out, 0,04 s d'écart) ; 2.16 « est » : les bustes s'affaissent de 6 u (0,12 s) ; 2.40 « ailleurs » : les trois traits de craie pâlissent (aqErase 0 → 0,6, 0,3 s) ; 2.60 la goutte accent du bas de la page grossit d'un cran (×1 → 1,15, 0,12 s) ; 2.74 plongée : la caméra s'enfonce dans la goutte (5050, 820) (échelle ×2,2/s, power3.in, flou 0 → 10) et la goutte s'ouvre (×1,15 → 4,4) ; 2.90 son centre s'assombrit vers canvas ; 3.00 couture : la goutte couvre tout le cadre.
  PISTE CAMÉRA : dérive x +12 u/s jusqu'à 2.74 ; plongée de cam(4733, 520, 1.08) vers cam(5050, 820, 14) de 2.74 à 3.00 (power3.in, flou 10 au sommet).
  COUCHES ET PROFONDEUR : avant-plan la goutte qui grossit ; sujet les six têtes penchées et leurs lueurs ocre ; fond le tableau pâli ; couches animées 3 à 4.
  OBJET-PONT ET VECTEUR : la goutte d'encre devient le noir du pivot (séquence 6) ; la caméra s'enfonce.
  SON : pops 1.68, 1.92, 1.97, 2.02, 2.07, 2.12 (les poches) ; pinceau 2.40 (la craie pâlit) ; whoosh cinématique 2.74.
  IMAGE CLÉ : 2.30 : six élèves de dos penchés vers la lueur ocre de leur poche, le tableau et sa craie derrière, « ailleurs » en boîte.


## Frame 6 : Et si vous la faisiez entrer dans le cours ? · 16.40 → 20.42

- scene: Dans le noir de l'encre, la question du film converge lettre à lettre au centre sur deux lignes, un trait ocre sous « entrer » ; elle tient dans le silence, puis une goutte ocre arrive de la caméra, tombe et éclate au centre : à l'impact le cadre entier est le lavis ocre
- duration: 4.02s
- transition_in: cut
- status: outline
- src: compositions/frames/06-pivot.html
- voiceover: "Et si vous la faisiez entrer dans le cours ?"
- type: pivot
- blueprint: video-text-pivot (Adapt)
- focal: la question centrée, puis la goutte ocre qui tombe
- rules: waterfall-entry, depth-of-field-blur
- world: dark
- handoff_in: à 0.00 : cam(5050, 820, 14) flou 10 px ; caméra en pleine plongée (échelle ×2,2/s, power3.in) dans la goutte accent du bas de P3 ; la goutte couvre 95 % du cadre, son accent s'assombrit vers canvas au centre ; aucune silhouette visible ; sous-titre sorti ; grain 55 %
- handoff_out: aucun raccord de caméra (coupe franche voulue à 20.42, à l'impact de la goutte ocre) ; raccord de couleur des deux côtés : le cadre entier est le lavis ocre-pale #EFD7A6 à 100 %, sans grain ni texte

Word cues: Et@0.11 si@0.30 vous@0.44 la@0.60 faisiez@0.78 entrer@1.12 dans@1.56 le@1.72 cours@1.96

Scene 1 (0.00 à 2.20 s) : P12, la question converge dans le noir
  TEXTE ÉCRAN : moment typographique « Et si vous la faisiez / entrer dans le cours ? » en Fraunces 84 px ink-paper, centré sur deux lignes (Et 0.11, si 0.30, vous 0.44, la 0.60, faisiez 0.78, entrer 1.12, dans 1.56, le 1.72, cours ? 1.96) ; [trait : entrer] à 1.12 ; aucun sous-titre en bas ; écart synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.10 l'anneau accent du bord se referme vers canvas (opacité 1 → 0, 0,1 s) : le cadre est l'intérieur de la goutte ; 0.11 « Et » : les lettres du premier mot convergent au centre (x ±220 → 0, flou 8 → 0, 0,5 s expo.out) ; 0.30 à 0.78 chaque mot de la première ligne converge sur son temps ; 0.40 une première onde sombre (ink à 6 %) s'élargit depuis le centre (×0,4 → 2,2 en 1,8 s, linéaire) ; 1.12 « entrer » : le mot converge et le trait ocre se peint dessous (coup de pinceau depuis la gauche, 0,4 s power2.out) ; 1.20 une seconde onde ; 1.56 à 1.96 la seconde ligne converge mot à mot ; 1.96 « cours ? » ; 2.00 une troisième onde.
  PISTE CAMÉRA : dérive d'échelle +1 %/s sur le noir de 0.00 à 2.20 ; la caméra ne bouge pas en x.
  COUCHES ET PROFONDEUR : avant-plan les lettres nettes ; sujet la question ; fond les ondes de l'encre et le vignettage ; couches animées 2 à 3.
  OBJET-PONT ET VECTEUR : la question tient jusqu'à la goutte du plan 2 ; l'onde du centre prépare le point d'impact.
  SON : goutte grave 0.00 (l'entrée dans l'encre).
  IMAGE CLÉ : 2.10 : « Et si vous la faisiez / entrer dans le cours ? » en deux lignes claires sur le noir, trait ocre sous « entrer », ondes sombres.

Scene 2 (2.20 à 4.02 s) : P13, la question tient, la goutte ocre tombe
  TEXTE ÉCRAN : la question tient jusqu'à 3.80 puis sort (opacité 1 → 0, flou 0 → 6, 0,14 s) ; aucun sous-titre.
  ÉTAPES : 2.20 recul lent (échelle -1 %/s, linéaire) ; 2.60 une quatrième onde ; 3.00 le trait ocre sous « entrer » s'avive (opacité 0,85 → 1, 0,2 s) ; 3.40 les lettres respirent (×1 → 1,01, 0,4 s) ; 3.80 la question sort (0,14 s) ; 3.80 une goutte ocre arrive de la caméra (×4, flou 10 px → net, 0,15 s power2.in) vers le centre (960, 540) ; 3.95 impact : la tache s'ouvre ×0,2 → ×1 (0,07 s expo.out), deux éclaboussures ; 3.97 à 4.02 la tache s'étale à tout le cadre (×1 → ×12, 0,05 s power2.in) : à 4.02 le cadre entier est le lavis ocre-pale #EFD7A6 à 100 %, sans grain ni texte.
  PISTE CAMÉRA : recul -1 %/s de 2.20 à 3.80 ; arrêt à 3.80 pendant la chute de la goutte (0,22 s, dans le silence du pivot).
  COUCHES ET PROFONDEUR : avant-plan la goutte en vol ; sujet la question ; fond les ondes ; couches animées 2 à 3.
  OBJET-PONT ET VECTEUR : la goutte ocre ouvre la page P4 de la séquence 7 (coupe franche à 20.42, cadre ocre des deux côtés).
  SON : goutte 3.80 ; impact grave 4.02 (couture).
  IMAGE CLÉ : 3.96 : la tache ocre qui éclate au centre du noir, deux éclaboussures, la question partie.


## Frame 7 : Je vous montre comment préparer un cours · 20.42 → 23.50

- scene: Le lavis ocre sèche et laisse apparaître la page P4, le même bureau du prof, coloré ; sur l'écran du portable, le plan de cours s'écrit à deux encres, la main au stylo barre une ligne et la réécrit ; whip vers la page suivante
- duration: 3.08s
- transition_in: cut
- status: outline
- src: compositions/frames/07-plan.html
- voiceover: "Je vous montre comment préparer un cours avec l'IA."
- type: turn
- blueprint: zoom-out-workspace-reveal (Adapt)
- focal: le bureau qui naît du lavis, puis le plan de cours à deux encres
- rules: depth-of-field-blur, svg-path-draw
- world: light
- handoff_in: à 0.00 : aucun raccord de caméra (coupe franche voulue à 20.42, à l'impact de la goutte ocre) ; raccord de couleur des deux côtés : le cadre entier est le lavis ocre-pale #EFD7A6 à 100 %, sans grain ni texte
- handoff_out: à 3.08 : cam(6900, 540, 1.1) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P4 (desk-prof coloré) : lampe au pied (5462, 800) et sa lueur ocre-2 pleine, portable à (6052, 575) ×1,0 dont l'écran porte la fenêtre « PLAN DE COURS » (quatre lignes d'encre, quatre traits ocre en marge, la ligne 3 barrée d'accent et réécrite dessous), le stylo posé au bord droit de l'écran (6360, 520) ; P5 au cadrage de référence : la page nue (aucune vignette encore) ; sous-titre sorti ; grain 55 %

Word cues: Je@0.08 vous@0.30 montre@0.50 comment@0.82 préparer@1.20 un@1.70 cours@1.92 avec@2.14 l'IA@2.52

Scene 1 (0.00 à 1.50 s) : P14, le lavis sèche en bureau coloré, la fenêtre du plan
  TEXTE ÉCRAN : sous-titre « Je vous [boîte : montre] comment préparer un cours avec l'IA. » (Je 0.08, vous 0.30, boîte tracée 0.46, montre 0.50, comment 0.82, [trait : préparer] préparer 1.20, un 1.70, cours 1.92, avec 2.14, l'IA 2.52) ; il sort de 2.86 à 3.00 ; écart : la fenêtre se trace sur « montre » (0.50), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 le lavis sèche de l'intérieur (aqDry 0 → 1 en 0,6 s) : son anneau fonce, le papier de P4 apparaît par le centre (clip-path ellipse 100 % → 60 %, 0,5 s expo.out) et il reste un grand lavis de sol ocre-pale à 55 % ; 0.08 « Je » ; 0.30 « vous » : le grain revient (0,2 s), la bande du bureau se dessine et son lavis brun se pose (0,3 s) ; 0.40 la lampe se dessine (tracé 0,3 s) et sa lueur ocre-2 pleine s'ouvre (×0,2 → 1, 0,12 s) ; 0.50 « montre » : le portable se pose (×1,1 flou 6 → net, 0,12 s) et la fenêtre « PLAN DE COURS » se trace dans l'écran (aqWindow 560 × 330, 0,3 s) ; 0.82 « comment » : l'étiquette se révèle (0,2 s) et quatre lignes d'encre s'écrivent (masque, 0,12 s chacune, 0,02 s d'écart) jusqu'à 1.40 ; 1.20 « préparer » : le trait ocre sous le mot ; 1.30 départ du cran vers l'écran (expo.inOut, 0,3 s, flou 0 → 6 → 0).
  PISTE CAMÉRA : dérive x +14 u/s, échelle +1 %/s de 0.00 à 1.30 ; cran de cam(6052, 540, 1.0) vers cam(6052, 500, 1.4) de 1.30 à 1.60.
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P5 (7 px) coupé par le bord droit ; sujet le portable et la fenêtre nets ; fond le lavis ocre-pale et le bureau grainé ; couches animées 3 à 4.
  OBJET-PONT ET VECTEUR : la fenêtre du plan reçoit l'encre ocre du plan 2 ; le cran s'enfonce vers l'écran.
  SON : pinceau 0.00 (le lavis sèche) ; stylo 0.40 (la lampe) ; papier 0.50 (le portable) ; stylo 0.82 à 1.40 (les lignes).
  IMAGE CLÉ : 1.20 : le bureau coloré, la lampe ocre, le portable avec la fenêtre « PLAN DE COURS » et ses quatre lignes d'encre, « montre » en boîte, trait sous « préparer ».

Scene 2 (1.50 à 3.08 s) : P15, l'IA en marge, la main corrige, whip
  TEXTE ÉCRAN : le même sous-titre se complète (un 1.70, cours 1.92, avec 2.14, l'IA 2.52) ; il sort de 2.86 à 3.00 ; écart : les traits ocre arrivent sur « un » (1.70), synchro.
  ÉTAPES : 1.50 à 1.60 fin du cran sur cam(6052, 500, 1.4) ; 1.70 « un » : quatre traits ocre courts se peignent en marge droite des lignes (coup de pinceau depuis la gauche, 0,12 s, 0,06 s d'écart) ; 1.92 « cours » : le stylo (kit aqPen) entre par le bas droit (y +300 → 0, 0,16 s power2.out) jusqu'à la ligne 3 ; 2.14 « avec » : le stylo barre la ligne 3 (trait accent tracé 0,2 s) ; 2.36 une nouvelle ligne d'encre s'écrit dessous (masque 0,25 s) et le stylo la suit ; 2.52 « l'IA » : le trait ocre de la marge de cette ligne s'avive (0,1 s) ; 2.70 le stylo se pose au bord droit de l'écran (6360, 520) (0,12 s) ; 2.86 le sous-titre sort ; 2.98 départ du whip vers P5 (power2.in, flou 0 → 12).
  PISTE CAMÉRA : dérive x +10 u/s, échelle +1 %/s de 1.60 à 2.98 ; whip de cam(6052, 500, 1.4) vers cam(7386, 480, 1.25) de 2.98 à 3.30 (power2.in puis expo.out, +7000 u/s au milieu).
  COUCHES ET PROFONDEUR : avant-plan le stylo net coupé par le bord bas ; sujet la fenêtre ; fond le bureau flou (4 px) ; couches animées 3.
  OBJET-PONT ET VECTEUR : l'encre ocre de la marge devient la couleur des vignettes de la séquence 8 ; le whip va vers la droite.
  SON : pinceau 1.70, 1.76, 1.82, 1.88 (la marge) ; stylo 2.14 (la rature), 2.36 (la réécriture) ; whoosh court 2.98.
  IMAGE CLÉ : 2.60 : la fenêtre du plan en gros plan, quatre lignes d'encre et leurs traits ocre en marge, la ligne 3 barrée de bordeaux et réécrite dessous, le stylo, « l'IA » dans le sous-titre.


## Frame 8 : Un quiz, un débat · 23.50 → 26.50

- scene: Le whip atterrit sur la page P5, nue : la première vignette s'ouvre d'une tache ocre-pale, quatre petites figures lèvent le bras ; la deuxième d'une tache bordeaux pâle, deux bulles se font face ; cran vers la droite
- duration: 3.00s
- transition_in: cut
- status: outline
- src: compositions/frames/08-quiz-debat.html
- voiceover: "Un quiz en direct, un débat avec la machine,"
- type: demo
- blueprint: spatial-pan-stations (Adapt)
- focal: la vignette du quiz, puis celle du débat
- rules: waterfall-entry, svg-path-draw
- world: light
- handoff_in: à 0.00 : cam(6900, 540, 1.1) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P4 (desk-prof coloré) : lampe au pied (5462, 800) et sa lueur ocre-2 pleine, portable à (6052, 575) ×1,0 dont l'écran porte la fenêtre « PLAN DE COURS » (quatre lignes d'encre, quatre traits ocre en marge, la ligne 3 barrée d'accent et réécrite dessous), le stylo posé au bord droit de l'écran (6360, 520) ; P5 au cadrage de référence : la page nue (aucune vignette encore) ; sous-titre sorti ; grain 55 %
- handoff_out: à 3.00 : cam(7800, 480, 1.25) flou 7 px ; caméra en plein cran vers la droite (+900 u/s en x, expo.inOut), dérive 0 ; monde : carnet, page P5 (vignettes) : vignette 1 complète à (7186, 480) (tache ocre-pale séchée, cadre d'encre, quatre petites figures ocre bras levés devant une ellipse ocre), vignette 2 complète à (7586, 480) (tache accent-pale séchée, cadre, deux bulles face à face, ocre-pale et accent-pale) ; papier nu à droite de x 7816 ; sous-titre sorti ; grain 55 %

Word cues: Un@0.19 quiz@0.44 en@0.66 direct@0.94 un@1.47 débat@1.74 avec@2.02 la@2.22 machine@2.48

Scene 1 (0.00 à 1.30 s) : P16, la vignette du quiz
  TEXTE ÉCRAN : sous-titre « Un quiz [boîte : en direct], » (Un 0.19, quiz 0.44, boîte tracée 0.62, en 0.66, direct 0.94) ; il sort de 1.30 à 1.44 ; écart : la tache s'ouvre sur « Un » (0.19), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.22 fin du whip, atterrissage sur cam(7386, 480, 1.25) (expo.out, flou 12 → 0) : la page nue ; 0.19 « Un » : une tache ocre-pale se peint à (7186, 480) (coup de pinceau depuis la gauche, 0,2 s expo.out) ; 0.40 elle sèche (aqDry 0 → 1, 0,4 s) ; 0.44 « quiz » : le cadre de la vignette se trace (encre 4 px, 0,3 s power2.out) ; 0.66 « en » : quatre petites figures ocre bras levés se posent (×1,1 flou 6 → net, 0,1 s, 0,06 s d'écart) ; 0.94 « direct » : l'ellipse ocre se peint derrière elles (coup de pinceau, 0,2 s) ; 1.10 les bras se lèvent d'un cran (y -6, 0,1 s) ; 1.30 le sous-titre sort.
  PISTE CAMÉRA : atterrissage expo.out de 0.00 à 0.22 ; dérive x +16 u/s, échelle +1 %/s de 0.22 à 2.86.
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P6 (7 px) coupé par le bord droit ; sujet la vignette nette ; fond la page grainée ; couches animées 3.
  OBJET-PONT ET VECTEUR : la tache de la vignette 2 reprend le geste de la vignette 1 ; la dérive va vers la droite.
  SON : pinceau 0.19 (la tache) ; stylo 0.44 (le cadre) ; pops 0.66, 0.72, 0.78, 0.84 (les figures).
  IMAGE CLÉ : 1.10 : la vignette du quiz sur sa tache ocre-pale, quatre figures ocre bras levés, « en direct » en boîte.

Scene 2 (1.30 à 3.00 s) : P17, la vignette du débat, cran vers la droite
  TEXTE ÉCRAN : sous-titre « un débat avec la machine, » (un 1.47, débat 1.74, avec 2.02, la 2.22, machine 2.48) ; il sort de 2.80 à 2.94 ; écart : la tache s'ouvre sur « un » (1.47), synchro.
  ÉTAPES : 1.47 « un » : une tache accent-pale se peint à (7586, 480) (coup de pinceau, 0,2 s) ; 1.68 elle sèche (0,4 s) ; 1.74 « débat » : le cadre se trace (0,3 s) ; 2.02 « avec » : la première bulle (ellipse d'encre 120 × 70, lavis ocre-pale) se trace à gauche (0,2 s) ; 2.22 « la » : la seconde bulle (accent-pale) se trace à droite, face à la première (0,2 s) ; 2.48 « machine » : les deux bulles se rapprochent de 6 u (0,1 s) ; 2.66 la vignette 1 se tasse (×1,01 → 1) ; 2.80 le sous-titre sort ; 2.86 départ du cran vers la droite (expo.inOut, flou 0 → 7).
  PISTE CAMÉRA : dérive x +16 u/s, échelle +1 %/s jusqu'à 2.86 ; cran de cam(7430, 480, 1.28) vers cam(8186, 480, 1.25) de 2.86 à 3.16 (expo.inOut, flou 7 au milieu).
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P6 coupé par le bord droit ; sujet la vignette du débat ; fond la vignette 1 qui passe au flou (3 px) et la page ; couches animées 3.
  OBJET-PONT ET VECTEUR : le papier nu à droite attend les vignettes 3 et 4 ; le cran va vers la droite.
  SON : pinceau 1.47 ; stylo 1.74 (le cadre), 2.02, 2.22 (les bulles).
  IMAGE CLÉ : 2.60 : les deux vignettes côte à côte, le quiz et les deux bulles face à face, « machine » dans le sous-titre.


## Frame 9 : Une étude de cas, une correction · 26.50 → 30.00

- scene: Le cran atterrit sur la droite de la page P5 : la troisième vignette s'ouvre, quatre tables et leurs points-figures ; la quatrième, une feuille à lignes grises que deux traits ocre annotent ; whip vers la page suivante
- duration: 3.50s
- transition_in: cut
- status: outline
- src: compositions/frames/09-etude-correction.html
- voiceover: "une étude de cas par équipe, une correction qui explique."
- type: demo
- blueprint: spatial-pan-stations (Adapt)
- focal: la vignette de l'étude de cas, puis celle de la correction
- rules: waterfall-entry, svg-path-draw
- world: light
- handoff_in: à 0.00 : cam(7800, 480, 1.25) flou 7 px ; caméra en plein cran vers la droite (+900 u/s en x, expo.inOut), dérive 0 ; monde : carnet, page P5 (vignettes) : vignette 1 complète à (7186, 480) (tache ocre-pale séchée, cadre d'encre, quatre petites figures ocre bras levés devant une ellipse ocre), vignette 2 complète à (7586, 480) (tache accent-pale séchée, cadre, deux bulles face à face, ocre-pale et accent-pale) ; papier nu à droite de x 7816 ; sous-titre sorti ; grain 55 %
- handoff_out: à 3.50 : cam(8700, 540, 1.1) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P5 : les quatre vignettes complètes (quiz, débat, étude de cas à (7986, 480) avec ses quatre tables et leurs points-figures, correction à (8386, 480) avec sa feuille à cinq lignes grises et deux traits ocre) ; P6 au cadrage de référence : l'étudiant (aqFigure ocre 200 u de trois quarts à (9100, 600)) à sa table brune (9150, 700), la fenêtre « NOUVELLE CONVERSATION » (aqWindow 420 × 260 à (9250, 380)) tracée, vide, sans étiquette ; le cahier (paper-2 260 × 180 à (9080, 740)) vierge ; le plan manuscrit (feuille paper-2 420 × 540 à (9950, 540)) avec ses quatre lignes ink-light seules ; sous-titre sorti ; grain 55 %

Word cues: une@0.07 étude@0.32 de@0.60 cas@0.84 par@0.96 équipe@1.24 une@1.81 correction@2.06 qui@2.58 explique@2.92

Scene 1 (0.00 à 1.70 s) : P18, la vignette de l'étude de cas
  TEXTE ÉCRAN : sous-titre « une étude de cas par équipe, » (une 0.07, étude 0.32, de 0.60, cas 0.84, par 0.96, équipe 1.24) ; il sort de 1.60 à 1.74 ; écart : la tache s'ouvre sur « une » (0.07), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.16 fin du cran sur cam(8186, 480, 1.25) (expo.inOut, flou 7 → 0) : le papier nu à droite, les vignettes 1 et 2 au bord gauche ; 0.07 « une » : une tache ocre-pale se peint à (7986, 480) (coup de pinceau, 0,2 s) ; 0.28 elle sèche (0,4 s) ; 0.32 « étude » : le cadre se trace (0,3 s) ; 0.60 « de » : quatre tables (ellipses d'encre 90 × 40) se tracent (0,15 s, 0,06 s d'écart) ; 0.96 « par » : deux points-figures (ocre et accent) se posent sur chaque table (×1,1 flou 4 → net, 0,08 s, 0,03 s d'écart) ; 1.24 « équipe » : les tables se tassent (×1,01 → 1) ; 1.44 les points se penchent vers leur table (1 u) ; 1.60 le sous-titre sort.
  PISTE CAMÉRA : fin du cran expo.inOut de 0.00 à 0.16 ; dérive x +16 u/s, échelle +1 %/s de 0.16 à 3.40.
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P6 (7 px) coupé par le bord droit ; sujet la vignette nette ; fond les vignettes 1 et 2 au flou (3 px) ; couches animées 3.
  OBJET-PONT ET VECTEUR : la tache de la vignette 4 reprend le geste ; la dérive va vers la droite.
  SON : pinceau 0.07 ; stylo 0.32 (le cadre), 0.60, 0.66, 0.72, 0.78 (les tables) ; pops 0.96 à 1.17 (les points).
  IMAGE CLÉ : 1.40 : la vignette de l'étude de cas, quatre tables à l'encre et leurs points ocre et bordeaux, « équipe » dans le sous-titre.

Scene 2 (1.70 à 3.50 s) : P19, la vignette de la correction, whip
  TEXTE ÉCRAN : sous-titre « une correction qui explique. » (une 1.81, correction 2.06, qui 2.58, explique 2.92) ; il sort de 3.26 à 3.40 ; écart : la tache s'ouvre sur « une » (1.81), synchro.
  ÉTAPES : 1.81 « une » : une tache accent-pale se peint à (8386, 480) (coup de pinceau, 0,2 s) ; 2.02 elle sèche (0,4 s) ; 2.06 « correction » : le cadre se trace (0,3 s) et la feuille 120 × 160 se dessine dedans (tracé 0,2 s) ; 2.30 cinq lignes grises se révèlent (masque, 0,05 s d'écart) ; 2.58 « qui » : deux traits ocre se peignent en marge de la feuille (coup de pinceau, 0,12 s, 0,08 s d'écart) ; 2.92 « explique » : la feuille se tasse (×1,02 → 1) ; 3.10 les quatre vignettes se tassent ensemble (×1,005 → 1, 0,1 s) ; 3.26 le sous-titre sort ; 3.40 départ du whip vers P6 (power2.in, flou 0 → 12).
  PISTE CAMÉRA : dérive x +16 u/s, échelle +1 %/s jusqu'à 3.40 ; whip de cam(8240, 480, 1.28) vers cam(9150, 560, 1.2) de 3.40 à 3.72 (power2.in puis expo.out, +7000 u/s au milieu).
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P6 coupé par le bord droit ; sujet la vignette de la correction ; fond les trois autres vignettes ; couches animées 3.
  OBJET-PONT ET VECTEUR : les deux traits ocre de la marge annoncent les gestes de l'étudiant (séquence 10) ; le whip va vers la droite.
  SON : pinceau 1.81 ; stylo 2.06 (le cadre) ; papier 2.30 (les lignes) ; stylo 2.58, 2.66 (les traits) ; whoosh court 3.40.
  IMAGE CLÉ : 3.00 : les quatre vignettes alignées, la dernière avec sa feuille annotée d'ocre, « explique » dans le sous-titre.


## Frame 10 : Vos étudiants apprennent à s'en servir · 30.00 → 35.10

- scene: Le whip atterrit sur la page P6, l'étudiant à sa table : dans la fenêtre de chat, une question se tape, une source se coche, une réponse se barre ; une goutte ocre tombe sur son cahier et sèche en deux traits, les réflexes ; cran vers le plan manuscrit
- duration: 5.10s
- transition_in: cut
- status: outline
- src: compositions/frames/10-etudiants.html
- voiceover: "Vos étudiants apprennent à s'en servir pour progresser. Des réflexes qu'ils garderont."
- type: demo
- blueprint: cursor-ui-demo (Adapt)
- focal: l'étudiant et sa fenêtre de chat, puis la tache ocre du cahier
- rules: depth-of-field-blur, svg-path-draw
- world: light
- handoff_in: à 0.00 : cam(8700, 540, 1.1) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P5 : les quatre vignettes complètes (quiz, débat, étude de cas à (7986, 480) avec ses quatre tables et leurs points-figures, correction à (8386, 480) avec sa feuille à cinq lignes grises et deux traits ocre) ; P6 au cadrage de référence : l'étudiant (aqFigure ocre 200 u de trois quarts à (9100, 600)) à sa table brune (9150, 700), la fenêtre « NOUVELLE CONVERSATION » (aqWindow 420 × 260 à (9250, 380)) tracée, vide, sans étiquette ; le cahier (paper-2 260 × 180 à (9080, 740)) vierge ; le plan manuscrit (feuille paper-2 420 × 540 à (9950, 540)) avec ses quatre lignes ink-light seules ; sous-titre sorti ; grain 55 %
- handoff_out: à 5.10 : cam(9550, 550, 1.2) flou 7 px ; caméra en plein cran vers la droite (+800 u/s en x, expo.inOut), dérive 0 ; monde : carnet, page P6 : l'étudiant penché en arrière de 2°, la fenêtre avec son étiquette, la ligne de question en encre, le bloc de réponse (trois traits ocre), la ligne de source cochée d'ocre, la ligne barrée d'accent ; le cahier avec la tache ocre séchée et ses deux traits ocre ; le plan manuscrit à (9950, 540) : quatre lignes ink-light, aucune note, aucun trait ocre ; sous-titre sorti ; grain 55 %

Word cues: Vos@0.27 étudiants@0.54 apprennent@1.14 à@1.48 s'en@1.62 servir@1.88 pour@2.20 progresser@2.56 Des@3.43 réflexes@3.62 qu'ils@4.18 garderont@4.42

Scene 1 (0.00 à 3.20 s) : P20, l'étudiant tape, vérifie, barre
  TEXTE ÉCRAN : sous-titre « Vos étudiants apprennent à [boîte : s'en servir] pour progresser. » (Vos 0.27, étudiants 0.54, apprennent 1.14, à 1.48, boîte tracée 1.58, s'en 1.62, servir 1.88, pour 2.20, [trait : progresser] progresser 2.56) ; il sort de 3.10 à 3.24 ; écart : la question se tape sur « apprennent » (1.14), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.22 fin du whip, atterrissage sur cam(9150, 560, 1.2) (expo.out, flou 12 → 0) : l'étudiant à sa table, la fenêtre vide, le cahier vierge ; 0.27 « Vos » : l'étudiant se penche vers la fenêtre (rotation 2°, 0,2 s) ; 0.54 « étudiants » : l'étiquette « NOUVELLE CONVERSATION » se révèle (0,2 s) ; 1.14 « apprennent » : la ligne de question se tape (traits d'encre qui avancent, masque 0,4 s) ; 1.48 « à » : un bloc de réponse (trois traits ocre) se peint sous la question (coup de pinceau, 0,1 s, 0,06 s d'écart) ; 1.62 « s'en » ; 1.88 « servir » : la ligne de source se révèle (0,15 s) et sa coche ocre se trace (0,15 s) ; 2.20 « pour » : une ligne du bloc se barre d'un trait accent (tracé 0,2 s) ; 2.56 « progresser » : le trait ocre sous le mot ; 2.70 une goutte ocre arrive de la caméra (×4, flou 10 px, 0,16 s power2.in) vers le cahier (9080, 740) ; 2.86 impact : la tache s'ouvre ×0,2 → ×1 (0,12 s), deux éclaboussures ; 3.10 le sous-titre sort.
  PISTE CAMÉRA : atterrissage expo.out de 0.00 à 0.22 ; dérive x +12 u/s, échelle +1 %/s de 0.22 à 4.96.
  COUCHES ET PROFONDEUR : avant-plan le bord flou du plan manuscrit (7 px) coupé par le bord droit et la goutte en vol ; sujet la fenêtre et l'étudiant nets ; fond la page grainée ; couches animées 3 à 4.
  OBJET-PONT ET VECTEUR : la goutte tombée sur le cahier devient les réflexes du plan 2 ; la dérive va vers la droite.
  SON : papier 0.54 ; key-press 1.14, 1.30, 1.46 (la question) ; pinceau 1.48 (la réponse) ; stylo 2.00 (la coche), 2.20 (la rature) ; goutte 2.70.
  IMAGE CLÉ : 2.40 : l'étudiant ocre de trois quarts, la fenêtre avec la question, le bloc ocre, la source cochée et la ligne barrée, « s'en servir » en boîte.

Scene 2 (3.20 à 5.10 s) : P21, la tache sèche en réflexes, cran vers le plan manuscrit
  TEXTE ÉCRAN : sous-titre « Des [boîte : réflexes] qu'ils garderont. » (Des 3.43, boîte tracée 3.58, réflexes 3.62, qu'ils 4.18, garderont 4.42) ; il sort de 4.80 à 4.94 ; écart : la tache sèche sur « Des » (3.43), synchro.
  ÉTAPES : 3.43 « Des » : la tache ocre du cahier sèche (aqDry 0 → 1, 0,5 s) ; 3.62 « réflexes » : un premier trait ocre se trace sur le cahier (0,2 s) ; 3.95 un second ; 4.18 « qu'ils » : l'étudiant se redresse (rotation 2° → 0, 0,2 s) ; 4.42 « garderont » : le cahier se tasse (×1,02 → 1) ; 4.60 la fenêtre passe au flou (0 → 3 px, 0,3 s) ; 4.80 le sous-titre sort ; 4.96 départ du cran vers le plan manuscrit (expo.inOut, flou 0 → 7).
  PISTE CAMÉRA : dérive jusqu'à 4.96 ; cran de cam(9207, 560, 1.26) vers cam(9950, 540, 1.2) de 4.96 à 5.26 (expo.inOut, flou 7 au milieu).
  COUCHES ET PROFONDEUR : avant-plan le bord du plan manuscrit flou coupé par le bord droit ; sujet le cahier et ses deux traits ; fond l'étudiant et la fenêtre ; couches animées 3.
  OBJET-PONT ET VECTEUR : le cran va du cahier de l'étudiant au plan manuscrit du prof, sur la même page.
  SON : pinceau 3.43 (le séchage) ; stylo 3.62, 3.95 (les traits).
  IMAGE CLÉ : 4.30 : le cahier avec sa tache ocre séchée et ses deux traits, l'étudiant redressé, « réflexes » en boîte.


## Frame 11 : Vos contenus, vos objectifs, votre pédagogie · 35.10 → 39.55

- scene: Le cran atterrit sur le plan de cours manuscrit du prof, à droite de la page P6 : « vos contenus », « vos objectifs » s'écrivent à la main ; l'IA s'inscrit en marge en traits ocre et deux lignes échangent leur place ; whip vers la page suivante
- duration: 4.45s
- transition_in: cut
- status: animated
- src: compositions/frames/11-pedagogie.html
- voiceover: "Vos contenus, vos objectifs. L'IA s'adapte à votre pédagogie."
- type: reassurance
- blueprint: camera-journey (Adapt)
- focal: le plan manuscrit qui s'écrit, puis l'IA en marge
- rules: svg-path-draw, depth-of-field-blur
- world: light
- handoff_in: à 0.00 : cam(9550, 550, 1.2) flou 7 px ; caméra en plein cran vers la droite (+800 u/s en x, expo.inOut), dérive 0 ; monde : carnet, page P6 : l'étudiant penché en arrière de 2°, la fenêtre avec son étiquette, la ligne de question en encre, le bloc de réponse (trois traits ocre), la ligne de source cochée d'ocre, la ligne barrée d'accent ; le cahier avec la tache ocre séchée et ses deux traits ocre ; le plan manuscrit à (9950, 540) : quatre lignes ink-light, aucune note, aucun trait ocre ; sous-titre sorti ; grain 55 %
- handoff_out: à 4.45 : cam(10400, 560, 1.1) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P6 : l'étudiant et sa fenêtre, le cahier aux deux traits, le plan manuscrit avec « vos contenus », « vos objectifs » en Caveat ink, les quatre lignes ink-light réordonnées, quatre traits ocre en marge et un trait ocre sous la première ligne ; P7 au cadrage de référence : la salle dans la pénombre redessinée (classroom, page 7) : lavis gris-lavis à 35 %, tableau à (11254, 300) avec la diapositive projetée, cinq rangs de six élèves gris-lavis (x = 10604 + j × 260, y = 500 à 820), trente téléphones gris éteints, aucun bras levé, le prof absent ; sous-titre sorti ; grain 55 %

Word cues: Vos@0.16 contenus@0.52 vos@1.24 objectifs@1.44 L'IA@2.30 s'adapte@2.70 à@3.30 votre@3.46 pédagogie@3.70

Scene 1 (0.00 à 2.10 s) : P22, le plan manuscrit s'écrit
  TEXTE ÉCRAN : sous-titre « Vos contenus, vos [boîte : objectifs]. » (Vos 0.16, contenus 0.52, vos 1.24, boîte tracée 1.40, objectifs 1.44) ; il sort de 1.90 à 2.04 ; écart : la première note s'écrit sur « contenus » (0.52), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.14 fin du cran sur cam(9950, 540, 1.2) (expo.inOut, flou 7 → 0) : la feuille et ses quatre lignes ink-light ; 0.16 « Vos » : la feuille se soulève (y -6, 0,1 s) ; 0.52 « contenus » : « vos contenus » s'écrit en Caveat ink (masque qui avance, 0,35 s, vitesse d'une main) ; 0.90 la première ligne ink-light se tasse ; 1.24 « vos » : la feuille respire (×1,01 → 1) ; 1.44 « objectifs » : « vos objectifs » s'écrit (0,35 s) ; 1.90 le sous-titre sort.
  PISTE CAMÉRA : fin du cran expo.inOut de 0.00 à 0.14 ; dérive x +10 u/s, échelle +1 %/s de 0.14 à 4.30.
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P7 (7 px) coupé par le bord droit ; sujet la feuille nette ; fond l'étudiant et sa fenêtre au flou (3 px) ; couches animées 2 à 3.
  OBJET-PONT ET VECTEUR : la marge droite de la feuille reçoit l'ocre du plan 2 ; la dérive va vers la droite.
  SON : papier 0.16 ; stylo 0.52 à 0.87, 1.44 à 1.79 (les notes).
  IMAGE CLÉ : 1.80 : le plan manuscrit avec « vos contenus » et « vos objectifs » en Caveat, quatre lignes grises dessous, « objectifs » en boîte.

Scene 2 (2.10 à 4.45 s) : P23, l'IA en marge, les lignes se réordonnent, whip
  TEXTE ÉCRAN : sous-titre « L'IA s'adapte à votre [boîte : pédagogie]. » (L'IA 2.30, s'adapte 2.70, à 3.30, votre 3.46, boîte tracée 3.66, pédagogie 3.70) ; il sort de 4.20 à 4.34 ; écart : les traits ocre arrivent sur « L'IA » (2.30), synchro.
  ÉTAPES : 2.30 « L'IA » : quatre traits ocre courts se peignent en marge droite des lignes (coup de pinceau depuis la gauche, 0,12 s, 0,1 s d'écart) ; 2.70 « s'adapte » : deux lignes ink-light échangent leur place (y, 0,24 s power2.inOut) ; 3.00 un trait ocre se trace sous la nouvelle première ligne (0,2 s) ; 3.30 « à » : la feuille se tasse (×1,02 → 1) ; 3.46 « votre » : les deux notes Caveat s'avivent (opacité 0,85 → 1, 0,2 s) ; 3.70 « pédagogie » : les traits de la marge s'épaississent (opacité 0,7 → 1, 0,15 s) ; 3.95 le cahier de l'étudiant, au bord gauche, se tasse ; 4.20 le sous-titre sort ; 4.30 départ du whip vers P7 (power2.in, flou 0 → 12).
  PISTE CAMÉRA : dérive jusqu'à 4.30 ; whip de cam(9993, 540, 1.24) vers cam(11254, 540, 1.0) de 4.30 à 4.62 (power2.in puis expo.out, +7000 u/s au milieu).
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P7 coupé par le bord droit ; sujet la feuille et sa marge ocre ; fond la page grainée ; couches animées 3.
  OBJET-PONT ET VECTEUR : la couleur ocre de la marge devient celle de la salle de la séquence 12 ; le whip va vers la droite.
  SON : pinceau 2.30, 2.40, 2.50, 2.60 (la marge) ; papier 2.70 (les lignes) ; stylo 3.00 (le trait) ; whoosh court 4.30.
  IMAGE CLÉ : 3.60 : le plan manuscrit, deux notes Caveat, quatre lignes réordonnées, quatre traits ocre en marge et un trait sous la première ligne, « pédagogie » en boîte.


## Frame 12 : Le cours redevient vivant · 39.55 → 43.50

- scene: Le whip atterrit sur la page P7, la salle de la pénombre redessinée : le lavis gris s'efface, les élèves reprennent l'ocre et le bordeaux, trente bras se lèvent ; cran sur le prof qui apparaît dans l'allée et se penche vers une table ; whip vers la signature
- duration: 3.95s
- transition_in: cut
- status: animated
- src: compositions/frames/12-vivant.html
- voiceover: "Le cours redevient vivant. Et vous, disponible."
- type: payoff
- blueprint: zoom-out-workspace-reveal (Adapt)
- focal: les trente bras levés, puis le prof entre les tables
- rules: waterfall-entry, depth-of-field-blur
- world: light
- handoff_in: à 0.00 : cam(10400, 560, 1.1) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P6 : l'étudiant et sa fenêtre, le cahier aux deux traits, le plan manuscrit avec « vos contenus », « vos objectifs » en Caveat ink, les quatre lignes ink-light réordonnées, quatre traits ocre en marge et un trait ocre sous la première ligne ; P7 au cadrage de référence : la salle dans la pénombre redessinée (classroom, page 7) : lavis gris-lavis à 35 %, tableau à (11254, 300) avec la diapositive projetée, cinq rangs de six élèves gris-lavis (x = 10604 + j × 260, y = 500 à 820), trente téléphones gris éteints, aucun bras levé, le prof absent ; sous-titre sorti ; grain 55 %
- handoff_out: à 3.95 : cam(12380, 540, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P7 : la salle en couleur (lavis gris effacé, tableau sous un lavis ocre-pale sans diapositive, trente élèves ocre et accent en alternance, trente bras levés, le prof accent 230 u à (11234, 640) penché de 6° vers la table de gauche, deux élèves penchés vers lui) ; P8 vide (papier nu) ; sous-titre sorti ; grain 55 %

Word cues: Le@0.15 cours@0.41 redevient@0.83 vivant@1.61 Et@2.32 vous@2.59 disponible@3.39

Scene 1 (0.00 à 2.10 s) : P24, la salle reprend ses couleurs, trente bras levés
  TEXTE ÉCRAN : sous-titre « Le cours [boîte : redevient] vivant. » (Le 0.15, cours 0.41, boîte tracée 0.79, redevient 0.83, [trait : vivant] vivant 1.61) ; il sort de 2.05 à 2.19 ; écart : la couleur revient sur « redevient » (0.83), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.22 fin du whip, atterrissage sur cam(11254, 540, 1.0) (expo.out, flou 12 → 0) : la salle grise de la séquence 2 ; 0.15 « Le » : la diapositive projetée pâlit (aqErase 0 → 0,5, 0,2 s) ; 0.41 « cours » : elle s'efface par le centre (aqErase 0,5 → 1, 0,2 s) et le lavis gris de la pénombre s'efface du haut vers le bas (0,3 s) ; 0.83 « redevient » : un grand lavis ocre-pale se peint sur le tableau (coup de pinceau depuis la gauche, 0,3 s) et les élèves reprennent leur couleur rang par rang, ocre et accent en alternance (fondu croisé de deux taches superposées, 0,12 s, 0,1 s d'écart par rang) jusqu'à 1.40 ; 1.20 les trente téléphones gris s'effacent par le centre (0,12 s, 0,01 s d'écart) ; 1.61 « vivant » : le trait ocre sous le mot et les trente bras se lèvent (traits de 40 u tracés vers le haut, 0,12 s, 0,02 s d'écart par colonne) jusqu'à 2.00 ; 2.05 le sous-titre sort.
  PISTE CAMÉRA : atterrissage expo.out de 0.00 à 0.22 ; dérive x +14 u/s, échelle +1,5 %/s de 0.22 à 2.14.
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P8 (7 px) coupé par le bord droit ; sujet les rangs d'élèves ; fond le tableau sous son lavis ocre ; couches animées 3 à 4.
  OBJET-PONT ET VECTEUR : l'allée centrale, vide, attend le prof du plan 2 ; rime de la salle grise de la séquence 2.
  SON : pinceau 0.41 (la pénombre s'efface), 0.83 à 1.30 (la couleur revient) ; pinceau 1.61 (les bras).
  IMAGE CLÉ : 1.90 : la salle en couleur, trente élèves ocre et bordeaux bras levés, le tableau sous un lavis ocre, « redevient » en boîte, trait sous « vivant ».

Scene 2 (2.10 à 3.95 s) : P25, le prof entre les tables, whip vers la signature
  TEXTE ÉCRAN : sous-titre « Et vous, [boîte : disponible]. » (Et 2.32, vous 2.59, boîte tracée 3.35, disponible 3.39) ; il sort de 3.70 à 3.84 ; écart : le prof paraît sur « Et » (2.32), synchro.
  ÉTAPES : 2.14 départ du cran vers le prof (expo.inOut, 0,3 s, flou 0 → 6 → 0) vers cam(11254, 640, 1.3) ; 2.32 « Et » : le prof se peint dans l'allée à (11254, 640) (buste scaleY 0 → 1, 0,16 s, tête ×0,2 → 1) ; 2.50 quatre points ocre-2 scintillent au-dessus des bras levés (0,3 s) ; 2.59 « vous » : le prof se tourne (rotation 0 → 4°, 0,2 s) ; 2.90 deux élèves voisins se tournent vers lui (rotation ∓3°, 0,16 s) ; 3.39 « disponible » : le prof se penche vers la table de gauche (rotation 4 → -6°, x -20, 0,2 s power2.out) ; 3.55 les deux élèves se penchent vers lui (2°) ; 3.70 le sous-titre sort ; 3.85 départ du whip vers P8 (power2.in, flou 0 → 12).
  PISTE CAMÉRA : cran de 2.14 à 2.44 ; dérive x +10 u/s, échelle +1 %/s de 2.44 à 3.85 ; whip de cam(11268, 640, 1.31) vers cam(12988, 400, 1.15) de 3.85 à 4.17 (power2.in puis expo.out, +7000 u/s au milieu).
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P8 coupé par le bord droit ; sujet le prof ; fond les rangs et le tableau au flou (3 px) ; couches animées 3.
  OBJET-PONT ET VECTEUR : le prof penché vers la table est la dernière image de la solution ; le whip va vers la signature.
  SON : pinceau 2.32 (le prof) ; scintillement 2.50 ; pinceau 3.39 (il se penche) ; whoosh court 3.85.
  IMAGE CLÉ : 3.50 : le prof bordeaux penché vers une table d'élèves ocre, bras levés autour, « disponible » en boîte.


## Frame 13 : Antoine Contino, formateur IA · 43.50 → 47.50

- scene: Le whip atterrit sur la page P8, nue : la même goutte d'encre bordeaux qu'aux films 1 et 2 tombe et la signature se trace depuis elle, « formateur IA » s'écrit dessous ; la caméra descend vers une tache ocre qui tombe et sèche en bouton ; le curseur entre et commence sa courbe
- duration: 4.00s
- transition_in: cut
- status: animated
- src: compositions/frames/13-signature.html
- voiceover: "Antoine Contino, formateur IA. Réservez un appel."
- type: cta
- blueprint: logo-assemble-lockup (Adapt)
- focal: la signature qui se trace, puis le bouton ocre
- rules: svg-path-draw, press-release-spring
- world: light
- handoff_in: à 0.00 : cam(12380, 540, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P7 : la salle en couleur (lavis gris effacé, tableau sous un lavis ocre-pale sans diapositive, trente élèves ocre et accent en alternance, trente bras levés, le prof accent 230 u à (11234, 640) penché de 6° vers la table de gauche, deux élèves penchés vers lui) ; P8 vide (papier nu) ; sous-titre sorti ; grain 55 %
- handoff_out: à 4.00 : cam(12988, 600, 1.0) flou 0 ; dérive x +12 u/s, échelle +1 %/s ; monde : carnet, page P8 ; signature « Antoine Contino » tracée en accent à (12988, 380), « formateur IA » à (12988, 470), bouton ocre « Réserver un appel » à (12988, 660), adresses à (12988, 760) ; le curseur à (13230, 790) en plein mouvement courbe vers la pointe du bouton (13060, 672), reste 0,20 s de trajet power3.out ; sous-titre « Réservez un appel. » en place, boîte sur « Réservez » ; grain 55 %

Word cues: Antoine@0.19 Contino@0.66 formateur@1.64 IA@2.00 Réservez@2.73 un@3.30 appel@3.54

Scene 1 (0.00 à 2.36 s) : P26, la goutte, la signature se trace
  TEXTE ÉCRAN : sous-titre « Antoine Contino, [boîte : formateur IA]. » (Antoine 0.19, Contino 0.66, boîte tracée 1.60, formateur 1.64, IA 2.00) ; il sort de 2.30 à 2.44 ; écart : la signature part sur « Antoine » (0.19), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.22 fin du whip, atterrissage sur cam(12988, 400, 1.15) (expo.out, flou 12 → 0) : la page nue ; 0.04 la goutte accent arrive de la caméra (×4, flou 10, 0,15 s) ; 0.19 « Antoine » : impact à (12560, 330), deux éclaboussures, et la signature « Antoine Contino » se trace depuis la goutte (masque qui avance de gauche à droite, 1,0 s power1.inOut, encre accent) ; 0.66 « Contino » : le tracé passe le « C » ; 1.19 la signature est complète ; 1.30 elle sèche (opacité 0,85 → 1, 0,5 s) ; 1.64 « formateur » : « formateur IA » se révèle dessous en DM Sans ink-2 (masque, 0,3 s) ; 2.00 « IA » : la traînée de la goutte s'allonge sous la signature (tracé 0,2 s) ; 2.30 le sous-titre sort ; 2.36 départ du cran vers le bas (expo.inOut, 0,3 s, flou 0 → 6 → 0).
  PISTE CAMÉRA : atterrissage expo.out de 0.00 à 0.22 ; dérive x +12 u/s, échelle +1 %/s de 0.22 à 2.36 ; cran de cam(12988, 400, 1.15) vers cam(12988, 600, 1.0) de 2.36 à 2.66.
  COUCHES ET PROFONDEUR : avant-plan la goutte en vol ; sujet la signature nette ; fond la page et le bureau grainé ; couches animées 3.
  OBJET-PONT ET VECTEUR : la goutte de la signature est celle des deux premiers films ; le cran descend vers le bouton.
  SON : goutte 0.04 ; stylo 0.19 à 1.19 (la signature).
  IMAGE CLÉ : 1.40 : « Antoine Contino » tracé en bordeaux depuis la goutte, « formateur IA » en train de se révéler, « formateur IA » en boîte.

Scene 2 (2.36 à 4.00 s) : P27, la tache ocre sèche en bouton, le curseur entre
  TEXTE ÉCRAN : sous-titre « [boîte : Réservez] un appel. » (boîte tracée 2.69, Réservez 2.73, un 3.30, appel 3.54) ; il reste en place à la couture ; écart : le bouton sèche sur « Réservez » (2.73), synchro.
  ÉTAPES : 2.36 à 2.66 fin du cran sur le milieu bas de la page ; 2.58 une goutte ocre arrive de la caméra (×4, flou 10, 0,12 s) ; 2.70 impact à (12988, 660) : la tache s'ouvre ×0,2 → 1 (0,12 s) en forme allongée (520 × 110) ; 2.73 « Réservez » : la tache sèche (aqDry 0 → 1, 0,4 s) et le texte « Réserver un appel » se révèle dedans (masque, 0,25 s) ; 3.10 un cerne d'encre fin se trace autour (0,2 s) ; 3.30 « un » : les deux adresses se révèlent dessous (DM Sans 24 px ink-2, masque 0,3 s) : « calendly.com/antoine-cntno/30min · antoinecontino.fr/ecoles » ; 3.54 « appel » : le bouton se tasse (×1,02 → 1) ; 3.76 le curseur entre par le bas droit du cadre, à (13420, 980) en coordonnées monde, et commence son unique mouvement courbe vers la pointe du bouton (13060, 672) ; 4.00 couture : le curseur est à (13230, 790), il lui reste 0,20 s de trajet power3.out.
  PISTE CAMÉRA : fin du cran jusqu'à 2.66 ; dérive x +12 u/s, échelle +1 %/s de 2.66 à 4.00 (elle continue dans la séquence 14).
  COUCHES ET PROFONDEUR : avant-plan le curseur net ; sujet le bouton ; fond la signature au flou (4 px) ; couches animées 3.
  OBJET-PONT ET VECTEUR : le curseur en mouvement porte la couture 13 → 14 ; rien d'autre ne bouge.
  SON : goutte 2.58 ; pinceau 2.73 (le séchage) ; stylo 3.10 (le cerne).
  IMAGE CLÉ : 3.60 : la carte de fin complète, signature, « formateur IA », bouton ocre « Réserver un appel », les deux adresses, le curseur qui arrive, « Réservez » en boîte.


## Frame 14 : Réserver un appel · 47.50 → 50.60

- scene: Le curseur finit sa courbe et clique le bouton : pression, la tache passe au bordeaux puis revient ocre, une onde s'ouvre ; la page tient, vivante, puis le noir monte comme l'encre du pivot
- duration: 3.10s
- transition_in: cut
- status: outline
- src: compositions/frames/14-clic.html
- voiceover: ""
- type: cta
- blueprint: cta-morph-press (Adapt)
- focal: le bouton cliqué, puis la page entière qui tient
- rules: cursor-click-ripple, press-release-spring
- world: light
- handoff_in: à 0.00 : cam(12988, 600, 1.0) flou 0 ; dérive x +12 u/s, échelle +1 %/s ; monde : carnet, page P8 ; signature « Antoine Contino » tracée en accent à (12988, 380), « formateur IA » à (12988, 470), bouton ocre « Réserver un appel » à (12988, 660), adresses à (12988, 760) ; le curseur à (13230, 790) en plein mouvement courbe vers la pointe du bouton (13060, 672), reste 0,20 s de trajet power3.out ; sous-titre « Réservez un appel. » en place, boîte sur « Réservez » ; grain 55 %
- handoff_out: aucun (fin du film, noir à 50.60)

Word cues: (aucun mot ; sous-titre « Réservez un appel. » en place depuis la séquence 13)

Scene 1 (0.00 à 3.10 s) : P28, le clic, la tenue vivante, le noir
  TEXTE ÉCRAN : sous-titre « [boîte : Réservez] un appel. » déjà en place ; il sort de 2.50 à 2.64.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.20 le curseur achève sa courbe (power3.out) jusqu'à la pointe sur le bouton (13060, 672) ; 0.25 clic : pression (curseur et bouton ×0,85, 0,06 s yoyo), la tache passe en accent (0,07 s) puis revient ocre (0,17 s), le texte reste ink ; 0.27 une onde accent s'ouvre depuis le point du clic (×0,2 → ×1,8, opacité 0,55 → 0, 0,45 s power1.out) ; 0.40 un cerne d'encre plus franc entoure le bouton (tracé 0,2 s) ; 0.60 le curseur s'écarte de 30 u vers le bas droit (0,4 s power3.out) et reste ; 0.80 à 2.50 tenue vivante : la granulation des taches dérive (6 u sur 1,7 s, aller simple), le grain du papier glisse de 8 u/s, la traînée de la goutte sèche (aqDry 0,6 → 1 en 1,2 s), l'ombre du carnet respire (un cycle de 1,7 s) ; 2.50 le sous-titre sort ; 2.60 à 3.10 le noir monte (un lavis canvas s'ouvre depuis le bas du cadre, scaleY 0 → 1,2 en 0,5 s power2.in, par-dessus tout) : noir à 3.10.
  PISTE CAMÉRA : dérive x +12 u/s, échelle +1 %/s de 0.00 à 3.10 (la même qu'à la fin de la séquence 13).
  COUCHES ET PROFONDEUR : avant-plan le curseur net ; sujet le bouton puis la page entière ; fond le bureau grainé ; couches animées 2 à 3 (onde, granulation, grain) ; aucune image figée.
  OBJET-PONT ET VECTEUR : le noir qui monte rejoue l'encre du pivot ; fin du film.
  SON : clic 0.25.
  IMAGE CLÉ : 1.50 : la carte de fin tenue, le bouton cliqué cerné d'encre, le curseur posé à côté, « Réservez » en boîte.

