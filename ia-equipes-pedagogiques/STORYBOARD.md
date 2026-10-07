---
format: 1920x1080
duration: "52.00s"
message: "Formées à l'IA sur leurs vrais documents, vos équipes pédagogiques récupèrent du temps pour les élèves, et le sens du métier avec."
arc: Hook → Problem → Pivot → Turn → Demo → Payoff → Reassurance → CTA
audience: "directions d'établissement, coordinateurs et équipes enseignantes, sur la page LinkedIn d'Antoine Contino, formateur IA"
mode: autonomous
captions: disabled
music: "pre-mixed with voice and SFX in assets/audio/mix.wav (mounted at root by the orchestrator)"
direction: "A « Le carnet » (DIRECTIONS.md), héritée du film 1 validé par Antoine le 7 octobre 2026"
styleframes: "../ia-etudiants/styleframes/png/A1.png, A2.png, A3.png et ../ia-etudiants/planches/2026-10-07-planche-douleur.jpg, 2026-10-07-planche-solution.jpg (le rendu validé du film 1)"
patterns: ../patterns/STORYBOARD-CRAFT.md, ../patterns/PATTERNS.md
---

## Video direction

- **Un seul monde** (frame.md) : le carnet d'un enseignant, huit pages parcourues de gauche à droite, même géométrie que le film 1. Séquences 1 à 5 = DOULEUR sur les pages P1 (la salle des profs vide) et P2 (le tableau qui se quadrille), lavées de gris ; séquence 6 = PIVOT dans le noir de la goutte d'encre ; séquences 7 à 11 = SOLUTION sur les pages P3 à P7 qui se colorent ; séquences 12 et 13 = FIN sur la page P8. Chaque séquence peint son propre fond (bureau paper-dark + pages) sur un calque `class="clip"` de toute sa durée.
- **Coutures invisibles** : toutes les séquences entrent en `cut` ; chaque couture tombe au sommet du flou d'un mouvement de caméra (whip, cran, plongée, recul) ou dans le mouvement du curseur, et le `handoff_out` de la séquence N est recopié mot pour mot dans le `handoff_in` de N+1. Exception voulue : 22.40, coupe franche à l'impact de la goutte ocre (le cadre entier est le lavis ocre des deux côtés) : du noir du pivot au papier de la salle pleine.
- **Texte** (lisible sans le son) : chaque phrase de la voix est un sous-titre `.aq-sub` en bas au centre (bande y 890 à 980, rien d'autre dedans), mot par mot sur les temps de chaque séquence (`mot@secondes`, temps locaux), 45 signes au plus par morceau. Un seul mot ou groupe par phrase dans la boîte bordeaux ([boîte : …]). Aucun autre texte coloré. Un seul moment typographique : « Et si vous repreniez ce temps ? » au pivot, centré sur le noir, 84 px, sans sous-titre pendant ce temps.
- **Pics** : 4 traits de pinceau ocre [trait : …] : « transmettre » (12.20), « temps » (20.62), « élèves » (42.76), « avec » (44.39).
- **Une seule chose à regarder** : chaque plan isole le sujet de la phrase ; la caméra va de gauche à droite dans le carnet ou s'enfonce (pile, écran, goutte, bouton), jamais d'aller-retour ; marges gauche et droite égales ; aucun décor sans sens ; au cadrage de référence de chaque plan, tout objet de la page reste au-dessus de y 880 à l'écran (frame.md § framings).
- **Vraies interfaces** : aucune (BRIEF.md) : la boîte de réception et la fenêtre de mail sont génériques et dessinées à l'encre, sans nom d'outil, d'expéditeur ni de famille.
- **Parallaxe** (une par acte au moins) : pendant chaque dérive, l'avant-plan flou (bord de la page suivante, goutte en vol, tasse, rebord du tableau) glisse 2,5 fois plus vite que la page, le bureau 0,4 fois.
- **Grammaire de mouvement** : deux vitesses, gestes de 1 à 6 images (expo.out) et dérives linéaires qui ne s'arrêtent jamais ; la zone 0,3 à 0,9 s est réservée à la caméra et au curseur (expo, power3, power4) ; les taches naissent d'une goutte ou d'un coup de pinceau et sèchent, jamais en fondu ; les traits se tracent ; aucune tenue figée ; aucune transition « effet ».
- **Texte visible** : exactement le texte cité dans les lignes Scene et les composants de frame.md, rien d'autre.
- **Négatifs** : diaporama (tout à t = 0), écran de veille, tache dédoublée, texte coloré à la place de la boîte, grande phrase, mot géant, titre qui répète la voix, symbole abstrait, curseur qui hésite, plusieurs objets qui bougent pendant une couture, outil d'IA nommé, nom de famille ou d'élève, chiffre.

**MONDE**
- Carnet (14 700 × 1 080 u, frame.md § world) sur le bureau paper-dark grainé : P1 (850, 540) la salle des profs vide · P2 (2584, 540) le tableau de la classe · P3 (4318, 540) la salle pleine · P4 (6052, 540) le bulletin et la séquence · P5 (7786, 540) le mail et la grille · P6 (9520, 540) le carnet des outils et la tasse · P7 (11254, 540) le tableau qui s'efface, les élèves · P8 (12988, 540) la signature et le bouton. Reliures à x = 1700 + (k - 1) × 1734.
- Pivot (18.89 à 22.40) : l'intérieur de la goutte d'encre, ground-ink (canvas, ondes sombres qui s'élargissent), la question centrée.
- Couleurs de rôle : accent bordeaux = boîte du mot clé, goutte signature, lignes du bulletin, aiguilles de l'horloge, signature finale, silhouettes de droite ; ocre = la couleur qui revient (4 traits, café, coches, élèves, bouton, lavis de la fin) ; gris de lavis = la douleur (horloge, copies, écran, cases, élèves pâlis) ; brun = table et rebord du tableau ; encre = traits et texte ; craie = paper sur le tableau.

**SIGNATURES**
- Mécanisme 1 « la goutte » (frame.md, drop : elle tombe, s'ouvre en tache, sèche en objet) : 0.02 goutte grise qui sèche en horloge · 3.88 goutte grise sur la pile · 18.64 la caméra plonge dans la goutte du bas de P2 (noir) · 22.33 goutte ocre sur le noir qui ouvre P3 · 27.53 goutte accent qui écrit le bulletin · 33.24 goutte ocre qui replie le mail · 39.68 goutte ocre dans la tasse · 45.23 goutte accent qui trace la signature · 47.48 goutte ocre qui sèche en bouton (9 occurrences).
- Mécanisme 2 « le séchage » (aqDry : l'anneau fonce, l'objet devient net ; inverse aqErase : la couleur pâlit puis la tache s'efface par le centre) : 0.50 l'horloge · 3.98 la pile · 7.36 les cases des bulletins · 9.33, 9.58 la vapeur (inverse) · 13.19 la craie (inverse) · 14.66 à 15.60 les cases du tableau · 16.40 à 18.52 les élèves (inverse) · 22.40 la salle pleine · 27.72 le bulletin · 30.77 les fiches · 33.64 le mail (inverse puis plein) · 41.40 à 42.00 les cases (inverse) · 42.18 les élèves · 44.49 le lavis de la fin · 46.31 la signature · 47.62 le bouton (16 occurrences).
- Registres de texte : sous-titre mot à mot = gris flou → net (0,14 s) puis encre (0,2 s) ; boîte = tracée depuis la gauche (0,16 s power3.out) ; trait = pinceau depuis la gauche (0,4 s power2.out) ; moment typographique = lettres qui convergent (0,5 s expo.out) ; notes Caveat et lignes manuscrites = révélées par un masque qui avance (vitesse d'une main, 0,2 à 1,0 s).
- Rimes : la tasse qui fume à nouveau (40.28) rejoue la tasse qui refroidit (9.33) ; les élèves qui reviennent en ocre (42.18) rejouent les élèves effacés (17.58) ; la salle pleine (22.40) rejoue la salle vide (0.02) ; la goutte de la signature (45.23) est celle des deux films.

**PARTITION CAMÉRA** (temps globaux) : 0.00 dérive sur P1 · 3.40 cran vers la pile (couture 3.55) · 5.05 cran vers l'écran · 6.89 cran vers la feuille des bulletins (couture 7.03) · 8.03 recul sur la salle entière · 10.26 whip P1 → P2 (couture 10.40) · 10.62 atterrissage P2 · 12.90 cran sur le tableau · 15.64 cran vers les élèves (couture 15.78) · 18.64 plongée dans la goutte (couture 18.89) · 18.89 dérive d'échelle sur le noir · 20.84 recul lent · 22.33 impact, coupe 22.40 · 22.40 le papier s'ouvre, dérive sur P3 · 24.90 cran sur les documents · 27.13 whip P3 → P4 (couture 27.27) · 27.49 atterrissage P4 · 29.57 cran vers la fiche · 32.00 whip P4 → P5 (couture 32.14) · 32.36 atterrissage P5 · 34.14 cran vers la grille · 37.11 whip P5 → P6 (couture 37.25) · 37.47 atterrissage P6 · 40.81 whip P6 → P7 (couture 40.95) · 41.15 atterrissage P7 · 43.25 recul court · 44.86 whip P7 → P8 (couture 45.00) · 45.22 atterrissage signature · 47.40 cran vers le bouton · 49.00 couture dans le mouvement du curseur · 49.25 clic · 49.40 à 51.50 dérive lente · 51.50 noir.

**VOIX** : minutage dans onsets.json (DIRECTIONS.md). Silences de plus de 0,4 s, chacun écrit comme un plan : 1.49 à 1.98 (la lumière baisse, la vapeur se trace) · 8.06 à 10.59 (gag muet : l'horloge tourne, la pile monte, la tasse refroidit ; whip) · 18.61 à 19.18 (plongée dans la goutte, le noir) · 20.72 à 22.67 (le pivot : la question tient, la goutte ocre tombe, le papier s'ouvre) · 36.97 à 37.54 (whip vers le carnet) · 40.75 à 41.15 (whip vers le tableau) · 44.68 à 45.31 (whip vers la signature, la goutte tombe) · 48.67 à 52.00 (clic, tenue vivante, noir).

**COUPES** (voix narrative, quota 0 à 4) : 22.40 · « Je » (22.67) · changement d'acte, du pivot à la solution, à l'impact de la goutte ocre (le cadre est le lavis ocre des deux côtés). Toutes les autres jonctions sont des coutures de caméra ou d'objet.

**RYTHME** : douleur (0 à 18.89) 10 plans = 5,3 plans / 10 s ; pivot 2 plans ; solution (22.40 à 45.00) 9 plans = 4,0 plans / 10 s ; fin (45.00 à 52.00) 3 plans = 4,3 plans / 10 s.

**SON** (proposition, verrouillée à l'étape 5 ; l'image ne bouge pas pour le son ; 7 whooshes, 1 scintillement) : goutte 0.02 · stylo 0.30 à 1.30 (la salle se dessine) · papier 2.66 à 3.00 (les chaises) · goutte 3.88 · papier 3.98, 4.10 · clic 5.58 (l'écran) · pops 5.70 à 6.50 (les objets des mails) · pinceau 7.36 à 7.80 (les cases) · click-soft 8.53, 9.03 (l'horloge) · papier 8.83 (la pile) · whoosh court 10.26 · stylo 10.74 à 12.00 (la craie) · pinceau 13.19 · stylo 13.42 à 14.00 (la grille) · pinceau 14.66 à 15.60 (les cases) · pinceau 16.40, 16.76, 17.58, 17.90, 18.12, 18.38, 18.52 (les élèves) · whoosh cinématique 18.64 · goutte grave 18.89 · goutte 22.33 · impact grave 22.40 · pinceau 23.40 à 24.10 (les silhouettes) · clic 24.68 · papier 26.42 à 26.60 · whoosh court 27.13 · goutte 27.53 · stylo 27.72 à 28.90, 29.12 · papier 30.50 · pinceau 30.77 · whoosh court 32.00 · goutte 33.24 · pinceau 33.64 · stylo 34.48 à 35.40, 36.02 à 36.50 · whoosh court 37.11 · stylo 38.00, 38.46, 39.20, 39.44 · goutte 39.68 · pinceau 40.28 · whoosh court 40.81 · pinceau 41.40 à 42.00, 42.18 à 42.80 · scintillement 43.05 · pinceau 43.84 · whoosh court 44.86 · goutte 45.23 · stylo 45.31 à 46.31 · goutte 47.48 · clic 49.25.

## Frame 1 : Lundi, la salle vide · 0.00 → 3.55

- scene: Sur la page P1 du carnet, la salle des profs se dessine à l'encre autour d'une goutte grise qui sèche en horloge à dix-huit heures ; les chaises se rentrent, la lumière grise de la nuit tombe aux fenêtres ; la caméra part vers la pile de copies
- duration: 3.55s
- transition_in: cut
- status: animated
- src: compositions/frames/01-lundi.html
- voiceover: "Lundi, dix-huit heures. La salle des profs est vide."
- type: hook
- blueprint: camera-journey (Adapt)
- focal: la goutte qui sèche en horloge, puis la table et les chaises rentrées
- rules: depth-of-field-blur, svg-path-draw
- world: light
- handoff_in: aucun (ouverture du film) ; première image = la page P1 au cadrage cam(850, 540, 1.0) flou 0 : le bureau paper-dark grainé, la page nue, aucun objet encore ; sous-titre vide ; grain 55 %
- handoff_out: à 3.55 : cam(620, 600, 1.3) flou 7 px ; caméra en plein cran vers la pile de copies (-900 u/s en x, expo.inOut), dérive 0 ; monde : carnet, page P1 (staff-room) : table brune et six chaises rentrées à l'encre, horloge à (1350, 200) séchée en gris à 18 h, pile de 4 copies grises à (560, 560), tasse à (980, 575) avec ses deux boucles de vapeur, portable ×0,6 à (1150, 560) écran gris éteint, feuille des bulletins (grille à l'encre 8 × 5) vide à (1400, 740), note « lundi, 18 h », deux lavis gris de la nuit en haut ; sous-titre sorti ; grain 55 %

Word cues: Lundi@0.02 dix-huit@0.86 heures@1.16 La@1.98 salle@2.18 des@2.42 profs@2.66 est@2.86 vide@3.10

Scene 1 (0.00 à 1.80 s) : P1, la goutte sèche en horloge, la salle se dessine
  TEXTE ÉCRAN : sous-titre « [boîte : Lundi], dix-huit heures. » (boîte tracée 0.00, Lundi 0.02, dix-huit 0.86, heures 1.16) ; il sort de 1.70 à 1.84 ; écart synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 la boîte se trace ; 0.02 une goutte grise arrive de la caméra (×4, flou 10 px, 0,16 s power2.in) vers (1350, 200) ; 0.18 impact : la tache s'ouvre ×0,2 → ×1 (0,12 s expo.out), deux éclaboussures ; 0.30 la table se dessine à l'encre (tracé 0,5 s power2.out, de gauche à droite) ; 0.50 la tache sèche en horloge (aqDry 0 → 1, 0,5 s) et le cercle d'encre se trace par-dessus (0,3 s) ; 0.68 les deux éclaboussures sèchent (aqDry 0 → 1, 0,2 s) et le petit trait des pieds de table se termine ; 0.86 « dix-huit » : les aiguilles accent se posent à 18 h (×1,3 flou 6 → net, 0,1 s) ; 1.00 les six chaises se dessinent (tracé 0,3 s, 0,05 s d'écart) ; 1.16 « heures » : la note Caveat « lundi, 18 h » se révèle (masque 0,3 s) ; 1.40 la pile de copies, la tasse et le portable se posent (×1,1 flou 6 → net, 0,12 s, 0,06 s d'écart) ; 1.60 les deux lavis gris de la nuit montent en haut (coup de pinceau, 0,2 s chacun).
  PISTE CAMÉRA : dérive x +24 u/s, échelle +2 %/s de 0.00 à 1.80.
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P2 (7 px) coupé par le bord droit et la goutte en vol ; sujet l'horloge puis la table nets ; fond le bureau paper-dark grainé ; couches animées 3.
  OBJET-PONT ET VECTEUR : l'horloge posée sert au gag (séquence 3) ; la table amène les chaises du plan 2.
  SON : goutte à 0.02 ; stylo de 0.30 à 1.30 (la salle se dessine).
  IMAGE CLÉ : 1.20 : la salle des profs à l'encre, l'horloge à 18 h séchée en gris en haut à droite, la pile, la tasse et le portable sur la table, « Lundi » en boîte.

Scene 2 (1.80 à 3.55 s) : P2, la salle est vide, les chaises se rentrent, cran vers la pile
  TEXTE ÉCRAN : sous-titre « La salle des profs est [boîte : vide]. » (La 1.98, salle 2.18, des 2.42, profs 2.66, est 2.86, boîte tracée 3.06, vide 3.10) ; il sort de 3.40 à 3.54 ; écart : les chaises se rentrent sur « vide » (3.10), synchro.
  ÉTAPES : 1.80 la lumière baisse : un lavis gris à 20 % se pose sur la page (coup de pinceau depuis le haut, 0,3 s) ; 1.98 « La » : la vapeur de la tasse se trace (deux boucles, 0,4 s) ; 2.18 « salle » : l'horloge se tasse (×1,02 → 1) ; 2.40 les deux lavis gris de la nuit s'étalent de 10 % (coup de pinceau, 0,2 s expo.out) ; 2.66 « profs » : la première chaise se rentre (x +20 u, 0,12 s power2.in) ; 2.86 « est » : les cinq autres se rentrent (0,06 s d'écart) ; 3.10 « vide » : la pile penche de 2° (0,1 s) ; 3.40 départ du cran vers la pile (expo.inOut, flou 0 → 7).
  PISTE CAMÉRA : dérive x +18 u/s, échelle +1,5 %/s de 1.80 à 3.40 ; 3.40 à 3.55 cran vers cam(620, 600, 1.3) (expo.inOut, flou 7 px à la couture).
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P2 ; sujet la table et les chaises nets ; fond l'horloge et les lavis de nuit, flous (4 px) ; couches animées 3 (chaises, vapeur, caméra).
  OBJET-PONT ET VECTEUR : la pile de copies devient le sujet de la séquence 2 (le cran va vers elle).
  SON : papier 2.66 à 3.00 (les chaises) ; (le cran est muet).
  IMAGE CLÉ : 3.00 : la salle vide, chaises rentrées, la lumière grise, « vide » en boîte, la vapeur fine sur la tasse.

## Frame 2 : Copies, mails, bulletins · 3.55 → 7.03

- scene: Gros plan sur la pile de copies : une goutte grise y tombe et la pile monte de deux feuilles ; cran vers l'écran du portable qui s'allume en gris et aligne les objets des mails aux familles ; cran vers la feuille des bulletins
- duration: 3.48s
- transition_in: cut
- status: animated
- src: compositions/frames/02-copies.html
- voiceover: "Les copies sont encore là. Les mails aux familles attendent."
- type: pain_point
- blueprint: spatial-pan-stations (Adapt)
- focal: la pile de copies, puis la boîte de réception sur l'écran
- rules: depth-of-field-blur, waterfall-entry
- world: light
- handoff_in: à 0.00 : cam(620, 600, 1.3) flou 7 px ; caméra en plein cran vers la pile de copies (-900 u/s en x, expo.inOut), dérive 0 ; monde : carnet, page P1 (staff-room) : table brune et six chaises rentrées à l'encre, horloge à (1350, 200) séchée en gris à 18 h, pile de 4 copies grises à (560, 560), tasse à (980, 575) avec ses deux boucles de vapeur, portable ×0,6 à (1150, 560) écran gris éteint, feuille des bulletins (grille à l'encre 8 × 5) vide à (1400, 740), note « lundi, 18 h », deux lavis gris de la nuit en haut ; sous-titre sorti ; grain 55 %
- handoff_out: à 3.48 : cam(1400, 740, 1.5) flou 6 px ; caméra en plein cran vers la feuille des bulletins (+700 u/s en x, +500 u/s en y, expo.inOut), dérive 0 ; monde : carnet, page P1 : écran du portable allumé avec la boîte de réception (7 lignes d'objets), pile de 6 copies, horloge à 18 h, tasse et sa vapeur ; feuille des bulletins (grille 8 × 5, 300 × 400) à (1400, 740) encore vide ; sous-titre sorti ; grain 55 %

Word cues: Les@0.19 copies@0.43 sont@0.69 encore@0.93 là@1.37 Les@1.82 mails@2.03 aux@2.25 familles@2.49 attendent@2.77

Scene 1 (0.00 à 1.60 s) : P3, la pile de copies
  TEXTE ÉCRAN : sous-titre « Les [boîte : copies] sont encore là. » (Les 0.19, boîte tracée 0.39, copies 0.43, sont 0.69, encore 0.93, là 1.37) ; il sort de 1.50 à 1.64 ; écart : la goutte touche 0,1 s avant « copies ».
  IMAGE DE DÉPART : handoff_in (le cran en cours vers la pile).
  ÉTAPES : 0.00 à 0.14 fin du cran sur cam(620, 600, 1.3) (expo.inOut, flou 7 → 0) ; 0.19 « Les » : une goutte grise arrive de la caméra ; 0.33 impact sur la pile (×0,2 → 1, 0,12 s) ; 0.43 « copies » : la tache sèche (0,4 s) et deux feuilles de plus glissent sur la pile depuis la droite (x +400 → 0, 0,14 s power2.in, 0,1 s d'écart) ; 0.69 « sont » : la pile se tasse (×1 → 0,99) ; 0.93 « encore » : les lignes grises des copies se révèlent (masque 0,25 s) ; 1.37 « là » : la pile penche de 3° (0,1 s) ; 1.50 départ du cran vers l'écran.
  PISTE CAMÉRA : fin du cran 0.00 à 0.14 ; dérive x +14 u/s, échelle +1 %/s de 0.14 à 1.50 ; 1.50 à 1.64 cran vers cam(1150, 560, 1.4) (expo.inOut, flou 8 px).
  COUCHES ET PROFONDEUR : avant-plan la tasse floue (8 px) coupée par le bord droit ; sujet la pile nette ; fond la table et les chaises flous ; couches animées 3 (goutte, feuilles, caméra).
  OBJET-PONT ET VECTEUR : la tasse de l'avant-plan reste entre la pile et l'écran ; le cran va vers la droite, vers l'écran.
  SON : goutte 3.88 global (0.33 local) ; papier 3.98, 4.10 global (0.43, 0.55 local).
  IMAGE CLÉ : 1.00 : la pile de six copies grises de près, la tache grise séchée dessus, « copies » en boîte.

Scene 2 (1.60 à 3.48 s) : P4, l'écran s'allume, les mails aux familles s'alignent, cran vers les bulletins
  TEXTE ÉCRAN : sous-titre « Les [boîte : mails] aux familles attendent. » (Les 1.82, boîte tracée 1.99, mails 2.03, aux 2.25, familles 2.49, attendent 2.77) ; il sort de 3.30 à 3.44 ; écart : l'écran s'allume 0,2 s avant « mails ».
  ÉTAPES : 1.60 à 1.74 fin du cran sur cam(1150, 560, 1.4) : l'écran éteint du portable ; 1.82 « Les » : l'écran s'allume en gris (lavis gris-lavis ×0,2 → 1 depuis le centre, 0,12 s) et la boîte de réception se dessine (aqWindow 560 × 330 tracée, 0,3 s) ; 2.03 « mails » : l'étiquette « BOÎTE DE RÉCEPTION » se révèle (0,2 s) ; 2.10 à 2.80 sept lignes d'objets se révèlent une à une (0,1 s d'écart, masque) : « Objet : absence de lundi », « Objet : réunion de rentrée », « Objet : sortie du 12 », « Objet : rendez-vous », « Objet : relance », « Objet : certificat », « Objet : question » ; 2.49 « familles » : la fenêtre se tasse ; 2.77 « attendent » : la liste défile de 20 u vers le haut (0,2 s) ; 3.34 départ du cran vers la feuille des bulletins (expo.inOut, flou 0 → 6).
  PISTE CAMÉRA : fin du cran 1.60 à 1.74 ; dérive x +12 u/s, échelle +1 %/s de 1.74 à 3.34 ; 3.34 à 3.48 cran vers cam(1400, 740, 1.5) (expo.inOut, flou 6 px à la couture).
  COUCHES ET PROFONDEUR : avant-plan le bord du cadre de l'écran flou (6 px) ; sujet la boîte de réception nette ; fond la pile et la tasse flous ; couches animées 3 (lignes, caméra, lavis).
  OBJET-PONT ET VECTEUR : la feuille des bulletins, visible en bas à droite de l'écran, devient le sujet de la séquence 3 ; le cran descend vers elle.
  SON : clic 5.58 global (2.03 local) ; pops 5.70 à 6.50 global (2.15 à 2.95 local : les objets).
  IMAGE CLÉ : 2.90 : l'écran du portable gris, sept objets de mails alignés, « mails » en boîte.

## Frame 3 : Les bulletins, le gag · 7.03 → 10.40

- scene: La feuille des bulletins se remplit de gris sur la table ; puis, dans le silence, la caméra recule sur la salle vide : l'horloge saute de dix minutes en dix minutes, la pile monte d'une copie, la vapeur de la tasse s'éteint ; whip vers la page suivante
- duration: 3.37s
- transition_in: cut
- status: animated
- src: compositions/frames/03-gag.html
- voiceover: "Les bulletins aussi."
- type: pain_point
- blueprint: zoom-out-workspace-reveal (Adapt)
- focal: la feuille des bulletins, puis l'horloge et la tasse de la salle vide
- rules: depth-of-field-blur, coordinate-target-zoom
- world: light
- handoff_in: à 0.00 : cam(1400, 740, 1.5) flou 6 px ; caméra en plein cran vers la feuille des bulletins (+700 u/s en x, +500 u/s en y, expo.inOut), dérive 0 ; monde : carnet, page P1 : écran du portable allumé avec la boîte de réception (7 lignes d'objets), pile de 6 copies, horloge à 18 h, tasse et sa vapeur ; feuille des bulletins (grille 8 × 5, 300 × 400) à (1400, 740) encore vide ; sous-titre sorti ; grain 55 %
- handoff_out: à 3.37 : cam(1900, 560, 1.1) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P1 : la salle vide, horloge à 18 h 20, pile de 7 copies, tasse sans vapeur, écran allumé (boîte de réception), feuille des bulletins remplie de gris ; P2 encore nette au cadrage de référence : tableau vide (chalkboard 1100 × 560 à (2584, 400)), six élèves en taches ocre devant (x 2130 à 3040, y 620 à 800), aucune main, aucune case ; la goutte accent au bas de la page (3300, 820) ; sous-titre sorti ; grain 55 %

Word cues: Les@0.12 bulletins@0.33 aussi@0.69

Scene 1 (0.00 à 1.10 s) : P5, la feuille des bulletins se remplit de gris
  TEXTE ÉCRAN : sous-titre « Les [boîte : bulletins] aussi. » (Les 0.12, boîte tracée 0.29, bulletins 0.33, aussi 0.69) ; il sort de 0.96 à 1.10 ; écart : les cases se remplissent sur « bulletins », synchro.
  IMAGE DE DÉPART : handoff_in (le cran en cours vers la feuille).
  ÉTAPES : 0.00 à 0.14 fin du cran sur cam(1400, 740, 1.5) ; 0.12 « Les » : la feuille se tasse (×1,02 → 1) ; 0.33 « bulletins » : six cases de la grille se remplissent de lavis gris (impact ×0,2 → 1, 0,1 s d'écart) ; 0.69 « aussi » : la feuille penche de 2° ; 0.90 la dernière case sèche (aqDry 0,3 s) ; 1.00 départ du recul.
  PISTE CAMÉRA : fin du cran 0.00 à 0.14 ; dérive x +10 u/s, y +4 u/s de 0.14 à 1.00 ; 1.00 à 1.40 recul vers cam(850, 540, 1.0) (expo.out, flou 4 px au départ).
  COUCHES ET PROFONDEUR : avant-plan le bord du portable flou (6 px) coupé par le bord gauche ; sujet la feuille nette ; fond la table ; couches animées 2 à 3.
  OBJET-PONT ET VECTEUR : le recul ramène toute la salle : l'horloge, la pile et la tasse deviennent les acteurs du gag.
  SON : pinceau 7.36 à 7.80 global (0.33 à 0.77 local).
  IMAGE CLÉ : 0.80 : la feuille des bulletins de près, six cases grises sur la grille, « bulletins » en boîte.

Scene 2 (1.10 à 3.37 s) : P6, gag muet : l'horloge tourne, la pile monte, la tasse refroidit, whip
  TEXTE ÉCRAN : aucun texte (le gag se lit sans mot).
  ÉTAPES : 1.10 à 1.40 fin du recul : la salle entière ; 1.50 l'aiguille des minutes saute (18 h 00 → 18 h 10, rotation 60° en 0,06 s) ; 1.80 une copie de plus glisse sur la pile depuis la droite (x +400 → 0, 0,14 s power2.in) ; 2.00 l'aiguille saute (18 h 20) ; 2.30 la première boucle de vapeur s'efface par le centre (aqErase 0 → 1, 0,25 s) ; 2.55 la seconde boucle s'efface ; 2.80 la lumière baisse encore (lavis gris +10 %, 0,2 s) ; 3.00 la pile se tasse ; 3.23 départ du whip vers P2 (power2.in, flou 0 → 12).
  PISTE CAMÉRA : dérive x +12 u/s, échelle +1 %/s de 1.40 à 3.23 ; 3.23 à 3.37 whip vers la droite (power2.in, +7000 u/s à la couture).
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P2 (7 px) coupé par le bord droit ; sujet la salle nette ; fond le bureau grainé ; couches animées 2 à 3 (aiguille, copie, vapeur).
  OBJET-PONT ET VECTEUR : la tasse sans vapeur et l'horloge reviennent dans la solution (séquence 10, la tasse fume à nouveau) ; vecteur : whip vers la droite repris par la séquence 4.
  SON : click-soft 8.53, 9.03 global (1.50, 2.00 local : l'horloge) ; papier 8.83 global (1.80 local) ; whoosh court 10.26 global (3.23 local).
  IMAGE CLÉ : 2.40 : la salle des profs vide et grise, l'horloge à 18 h 20, la pile de sept copies, la tasse dont la vapeur s'éteint.

## Frame 4 : Transmettre, puis remplir des tableaux · 10.40 → 15.78

- scene: Le whip atterrit sur la page P2, le tableau de la classe : une main peinte écrit à la craie devant six élèves en taches ocre ; puis la craie s'efface, le tableau se quadrille en cases et la même main les remplit de gris ; cran vers les élèves
- duration: 5.38s
- transition_in: cut
- status: animated
- src: compositions/frames/04-tableau.html
- voiceover: "Vous avez choisi ce métier pour transmettre. Vous passez vos soirées à remplir des tableaux."
- type: pain_point
- blueprint: camera-journey (Adapt)
- focal: la main à la craie devant le tableau, puis la grille qui se remplit
- rules: svg-path-draw, depth-of-field-blur
- world: light
- handoff_in: à 0.00 : cam(1900, 560, 1.1) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P1 : la salle vide, horloge à 18 h 20, pile de 7 copies, tasse sans vapeur, écran allumé (boîte de réception), feuille des bulletins remplie de gris ; P2 encore nette au cadrage de référence : tableau vide (chalkboard 1100 × 560 à (2584, 400)), six élèves en taches ocre devant (x 2130 à 3040, y 620 à 800), aucune main, aucune case ; la goutte accent au bas de la page (3300, 820) ; sous-titre sorti ; grain 55 %
- handoff_out: à 5.38 : cam(2584, 640, 1.15) flou 6 px ; caméra en plein cran vers le bas (+900 u/s en y, expo.inOut), dérive 0 ; monde : carnet, page P2 ; tableau quadrillé (10 × 5) avec 8 cases grises, la main à la craie posée au bord droit du tableau (3100, 560), six élèves en taches ocre nets devant (y 620 à 800) ; la goutte accent au bas de la page (3300, 820) ; sous-titre sorti ; grain 55 %

Word cues: Vous@0.19 avez@0.34 choisi@0.64 ce@0.96 métier@1.14 pour@1.48 transmettre@1.80 Vous@2.79 passez@3.02 vos@3.38 soirées@3.62 à@4.04 remplir@4.26 des@4.70 tableaux@5.00

Scene 1 (0.00 à 2.60 s) : P7, le tableau, la main écrit à la craie
  TEXTE ÉCRAN : sous-titre « Vous avez choisi ce [boîte : métier] pour [trait : transmettre]. » (Vous 0.19, avez 0.34, choisi 0.64, ce 0.96, boîte tracée 1.10, métier 1.14, pour 1.48, transmettre 1.80 avec le trait ocre tracé de 1.80 à 2.20) ; il sort de 2.46 à 2.60 ; écart : la main écrit dès « Vous » (0,2 s avant « avez »).
  IMAGE DE DÉPART : handoff_in (le whip en cours, P2 arrive de la droite).
  ÉTAPES : 0.00 à 0.22 fin du whip, atterrissage sur cam(2584, 540, 1.0) (expo.out, flou 12 → 0) ; 0.19 « Vous » : la main à la craie entre par le bas droit (y +400 → 0, 0,18 s power2.out) jusqu'au tableau ; 0.34 « avez » : un premier trait de craie se trace (couleur paper, 0,4 s power1.inOut) ; 0.64 « choisi » : un second trait ; 0.96 « ce » : les six élèves se penchent vers le tableau (2°, 0,2 s) ; 1.14 « métier » : la boîte ; 1.48 « pour » : un troisième trait, plus long ; 1.80 « transmettre » : la main souligne le dernier trait (tracé 0,3 s) ; 2.20 la main se relève de 20 u (0,1 s) ; 2.46 le sous-titre sort ; 2.50 départ du cran.
  PISTE CAMÉRA : atterrissage 0.00 à 0.22 ; dérive x +16 u/s, échelle +1 %/s de 0.22 à 2.50 ; 2.50 à 2.64 cran vers cam(2584, 420, 1.3) (expo.inOut, flou 8 px).
  COUCHES ET PROFONDEUR : avant-plan un élève du premier rang flou (6 px) coupé par le bord bas et le bord flou de P3 ; sujet le tableau et la main nets ; fond le papier ; couches animées 3 (main, traits, élèves).
  OBJET-PONT ET VECTEUR : la main reste et change de geste au plan suivant (elle remplit) ; le cran monte sur le tableau.
  SON : stylo 10.74 à 12.00 global (0.34 à 1.60 local : la craie).
  IMAGE CLÉ : 1.90 : le tableau gris-vert à l'encre, trois traits de craie et un soulignement, la main peinte qui écrit, six élèves ocre de dos, « transmettre » souligné d'ocre.

Scene 2 (2.60 à 5.38 s) : P8, la craie s'efface, la grille, la main remplit les cases
  TEXTE ÉCRAN : sous-titre « Vous passez vos soirées à remplir des [boîte : tableaux]. » (Vous 2.79, passez 3.02, vos 3.38, soirées 3.62, à 4.04, remplir 4.26, des 4.70, boîte tracée 4.96, tableaux 5.00) ; il sort de 5.24 à 5.38 ; écart : la grille se trace 0,4 s avant « tableaux » et les cases se remplissent sur « remplir ».
  ÉTAPES : 2.60 à 2.74 fin du cran sur le tableau ; 2.79 « Vous » : les traits de craie s'effacent par le centre (aqErase, 0,3 s, 0,05 s d'écart) ; 3.02 « passez » : les lignes de la grille se tracent (5 horizontales puis 10 verticales, 0,6 s au total) ; 3.62 « soirées » : le tableau s'assombrit (lavis gris +10 %) ; 4.04 « à » : la main descend sur la première case ; 4.26 « remplir » : les cases se remplissent de gris une à une (impact ×0,2 → 1, 0,12 s d'écart, 8 cases) jusqu'à 5.20 ; 5.00 « tableaux » ; 5.24 la main se pose au bord droit du tableau (3100, 560) (0,12 s) ; 5.24 départ du cran vers les élèves (expo.inOut, flou 0 → 6).
  PISTE CAMÉRA : dérive x +12 u/s, y -4 u/s de 2.74 à 5.24 ; 5.24 à 5.38 cran vers cam(2584, 640, 1.15) (expo.inOut, flou 6 px à la couture).
  COUCHES ET PROFONDEUR : avant-plan la main nette (elle est le sujet) et la craie ; sujet la grille ; fond les élèves flous (4 px) en bas ; couches animées 3 (grille, cases, main).
  OBJET-PONT ET VECTEUR : les cases grises de la grille deviennent le voile derrière lequel les élèves pâlissent (séquence 5) ; le cran descend vers eux.
  SON : pinceau 13.19 global (2.79 local) ; stylo 13.42 à 14.00 global (3.02 à 3.60 local : la grille) ; pinceau 14.66 à 15.60 global (4.26 à 5.20 local : les cases).
  IMAGE CLÉ : 4.80 : la grille à l'encre sur le tableau, huit cases grises, la main qui remplit la neuvième, « tableaux » en boîte.

## Frame 5 : Le sens s'use, une case à la fois · 15.78 → 18.89

- scene: Le cran descend sur les six élèves devant la grille : les dernières cases se remplissent, les taches ocre pâlissent puis s'effacent une à une, une case à la fois ; il ne reste que la goutte d'encre au bas de la page et la caméra plonge dedans jusqu'au noir
- duration: 3.11s
- transition_in: cut
- status: animated
- src: compositions/frames/05-sens.html
- voiceover: "Et le sens s'use. Une case à la fois."
- type: pain_point
- blueprint: camera-journey (Adapt)
- focal: les six élèves qui pâlissent derrière la grille, puis la goutte d'encre
- rules: depth-of-field-blur, coordinate-target-zoom
- world: light
- handoff_in: à 0.00 : cam(2584, 640, 1.15) flou 6 px ; caméra en plein cran vers le bas (+900 u/s en y, expo.inOut), dérive 0 ; monde : carnet, page P2 ; tableau quadrillé (10 × 5) avec 8 cases grises, la main à la craie posée au bord droit du tableau (3100, 560), six élèves en taches ocre nets devant (y 620 à 800) ; la goutte accent au bas de la page (3300, 820) ; sous-titre sorti ; grain 55 %
- handoff_out: à 3.11 : cam(3300, 820, 14) flou 10 px ; caméra en pleine plongée (échelle ×2,2/s, power3.in) dans la goutte accent du bas de P2 ; la goutte couvre 95 % du cadre, son accent s'assombrit vers canvas au centre ; aucune silhouette (toutes effacées) ; sous-titre sorti ; grain 55 %

Word cues: Et@0.19 le@0.36 sens@0.62 s'use@0.98 Une@1.80 case@2.12 à@2.34 la@2.60 fois@2.74

Scene 1 (0.00 à 2.86 s) : P9, les élèves pâlissent derrière la grille
  TEXTE ÉCRAN : sous-titre « Et le [boîte : sens] s'use. Une [boîte : case] à la fois. » en deux morceaux : « Et le [boîte : sens] s'use. » (Et 0.19, le 0.36, boîte tracée 0.58, sens 0.62, s'use 0.98 ; sort 1.60 à 1.74) puis « Une [boîte : case] à la fois. » (Une 1.80, boîte tracée 2.08, case 2.12, à 2.34, la 2.60, fois 2.74 ; sort 2.86 à 3.00) ; écart : chaque élève s'efface sur son mot, synchro.
  IMAGE DE DÉPART : handoff_in (le cran en cours vers le bas).
  ÉTAPES : 0.00 à 0.14 fin du cran sur cam(2584, 640, 1.15) : les six élèves et le bas du tableau ; 0.19 « Et » : deux cases de plus se remplissent de gris ; 0.62 « sens » : les six élèves pâlissent vers gris-lavis (aqErase 0 → 0,5, 0,3 s, 0,06 s d'écart) ; 0.98 « s'use » : encore deux cases ; 1.40 la main posée glisse de 10 u ; 1.80 « Une » : le premier élève s'efface par le centre (aqErase 0,5 → 1, 0,2 s) ; 2.12 « case » : le deuxième ; 2.34 « à » : le troisième ; 2.60 « la » : le quatrième et le cinquième ; 2.74 « fois » : le dernier ; 2.78 la goutte accent du bas de la page (3300, 820) grossit d'un cran (×1 → 1,15, 0,1 s) : seule couleur restante ; 2.86 départ de la plongée.
  PISTE CAMÉRA : fin du cran 0.00 à 0.14 ; dérive x +14 u/s, échelle +1 %/s de 0.14 à 2.86.
  COUCHES ET PROFONDEUR : avant-plan le rebord brun du tableau flou (6 px) coupé par le bord haut ; sujet les élèves ; fond la grille grise ; couches animées 3 (cases, élèves, caméra).
  OBJET-PONT ET VECTEUR : la goutte accent devient le noir du pivot (la caméra plonge dedans).
  SON : pinceau 16.40, 16.76 global (0.62, 0.98 local) ; pinceau 17.58, 17.90, 18.12, 18.38, 18.52 global (1.80, 2.12, 2.34, 2.60, 2.74 local : les effacements).
  IMAGE CLÉ : 2.20 : la grille grise pleine, trois élèves déjà effacés, trois encore gris pâle, la goutte bordeaux en bas (planche A2 du film 1 pour le ton).

Scene 2 (2.86 à 3.11 s) : P10, plongée dans la goutte
  TEXTE ÉCRAN : fin du sous-titre (il sort de 2.86 à 3.00) ; écart : la plongée commence dans le silence après « fois ».
  ÉTAPES : 2.86 plongée vers cam(3300, 820, 14) (power3.in, 0,25 s, flou 0 → 10 au sommet 3.11) : la goutte grandit jusqu'à couvrir le cadre ; 2.95 le centre de la goutte s'assombrit (dégradé radial accent → canvas, opacité 0 → 1, 0,15 s) ; 3.11 couture au sommet du flou.
  PISTE CAMÉRA : 2.86 à 3.11 plongée power3.in (échelle ×2,2/s à la couture).
  COUCHES ET PROFONDEUR : la goutte seule (avant, net) ; le papier qui sort du cadre ; couches animées 2 (caméra, dégradé).
  OBJET-PONT ET VECTEUR : la goutte devient le fond noir de la séquence 6 (même objet, autre échelle) ; vecteur : plongée reprise par la séquence 6.
  SON : whoosh cinématique 18.64 global (2.86 local).
  IMAGE CLÉ : 3.00 : la goutte bordeaux énorme et floue qui remplit le cadre, le papier qui disparaît aux coins, le centre déjà presque noir.

## Frame 6 : Et si vous repreniez ce temps ? · 18.89 → 22.40

- scene: Dans le noir de l'encre, la question du film converge lettre à lettre au centre, un trait ocre sous « temps » ; elle tient dans le silence, puis une goutte ocre arrive de la caméra, tombe et éclate au centre : à l'impact le cadre entier est le lavis ocre
- duration: 3.51s
- transition_in: cut
- status: animated
- src: compositions/frames/06-pivot.html
- voiceover: "Et si vous repreniez ce temps ?"
- type: pivot
- blueprint: video-text-pivot (Adapt)
- focal: la question centrée, puis la goutte ocre qui tombe
- rules: depth-of-field-blur
- world: dark
- handoff_in: à 0.00 : cam(3300, 820, 14) flou 10 px ; caméra en pleine plongée (échelle ×2,2/s, power3.in) dans la goutte accent du bas de P2 ; la goutte couvre 95 % du cadre, son accent s'assombrit vers canvas au centre ; aucune silhouette (toutes effacées) ; sous-titre sorti ; grain 55 %
- handoff_out: aucun raccord de caméra (coupe franche voulue à 22.40, à l'impact de la goutte ocre) ; raccord de couleur des deux côtés : le cadre entier est le lavis ocre-pale #EFD7A6 à 100 %, sans grain ni texte

Word cues: Et@0.29 si@0.49 vous@0.67 repreniez@0.97 ce@1.47 temps@1.73

Scene 1 (0.00 à 1.95 s) : P11, le noir, la question converge
  TEXTE ÉCRAN : moment typographique centré (Fraunces 84 px, ink-paper) « Et si vous repreniez ce [trait : temps] ? » : chaque mot converge sur son temps (Et 0.29, si 0.49, vous 0.67, repreniez 0.97, ce 1.47, temps 1.73, « ? » 1.90), le trait ocre se trace sous « temps » de 1.73 à 2.13 ; aucun sous-titre en bas ; écart synchro.
  IMAGE DE DÉPART : handoff_in (la fin de la plongée : le noir de l'encre gagne tout le cadre).
  ÉTAPES : 0.00 à 0.20 la plongée s'achève dans le noir (flou 10 → 0, expo.out) : ground-ink avec ses ondes sombres (1 toutes les 0,8 s, ×0,2 → ×1,6, opacité 0,06 → 0) ; 0.29 « Et » converge (lettres depuis ±0,4 em, opacité 0 → 1, flou 12 → 0, 0,5 s expo.out) ; 0.49 « si » ; 0.67 « vous » ; 0.97 « repreniez » ; 1.47 « ce » ; 1.73 « temps » converge et le trait ocre se trace dessous (0,4 s power2.out) ; 1.90 le « ? » se pose (×1,3 flou 6 → net, 0,12 s).
  PISTE CAMÉRA : dérive d'échelle +1,5 %/s sur le noir et la phrase (de 0.20 à 1.95).
  COUCHES ET PROFONDEUR : la phrase nette (sujet) ; les ondes de l'encre derrière, floues (4 px) ; le vignettage canvas-2 devant aux bords ; couches animées 2.
  OBJET-PONT ET VECTEUR : la phrase tient et reste le sujet pendant que la goutte arrive au plan suivant.
  SON : goutte grave 18.89 global (0.00 local).
  IMAGE CLÉ : 1.95 : noir d'encre, ondes concentriques très sombres, la question entière en crème au centre, trait ocre sous « temps ».

Scene 2 (1.95 à 3.51 s) : P12, le silence, la goutte ocre tombe et éclate
  TEXTE ÉCRAN : la question tient jusqu'à 3.30 puis sort (opacité 1 → 0, flou 0 → 6, 0,14 s) juste avant l'impact ; aucun sous-titre.
  ÉTAPES : 1.95 recul lent de la caméra (échelle -2 %/s) ; 2.20 les ondes ralentissent (une toutes les 1,2 s) ; 2.60 une goutte ocre naît d'un point en haut du cadre (×0,05 → ×1, 0,2 s expo.out) à (960, -40) ; 2.80 elle grossit vers la caméra (×1 → ×2,5, flou 0 → 6, 0,36 s power3.in) en descendant vers y 60 ; 3.16 elle tient une image, énorme et floue ; 3.27 elle plonge sur le centre (y → 540, ×2,5 → ×1, 0,17 s power2.in) ; 3.30 la question sort ; 3.44 impact au centre (960, 540) : le lavis ocre-pale s'ouvre ×0,2 → ×14 (0,07 s expo.out) et recouvre tout le cadre ; 3.51 le cadre est entièrement ocre-pale : coupe.
  PISTE CAMÉRA : 1.95 à 3.44 recul lent (échelle -2 %/s) ; 3.44 à 3.51 immobile sous le lavis qui recouvre tout.
  COUCHES ET PROFONDEUR : avant-plan la goutte en vol (grande, floue) ; sujet la question ; fond les ondes ; couches animées 3.
  OBJET-PONT ET VECTEUR : le lavis ocre qui recouvre le cadre est la première image de la séquence 7 (il sèche en salle pleine).
  SON : goutte 22.33 global (3.44 local) ; impact grave 22.40 global (3.51 local, le papier s'ouvre).
  IMAGE CLÉ : 3.20 : la question en crème sur le noir, une grosse goutte ocre floue qui tombe vers le centre.

## Frame 7 : Je forme vos équipes · 22.40 → 27.27

- scene: Le lavis ocre sèche et laisse apparaître la page P3, la même salle des profs, pleine : six silhouettes autour de la table, portables allumés ; la caméra s'approche des vrais documents sur la table ; whip vers la page suivante
- duration: 4.87s
- transition_in: cut
- status: animated
- src: compositions/frames/07-salle-pleine.html
- voiceover: "Je forme vos équipes pédagogiques à l'IA, sur leurs outils et leurs vrais documents."
- type: demo
- blueprint: spatial-pan-stations (Adapt)
- focal: les silhouettes qui naissent du lavis autour de la table, puis les documents
- rules: waterfall-entry, depth-of-field-blur
- world: light
- handoff_in: à 0.00 : aucun raccord de caméra (coupe franche voulue à 22.40, à l'impact de la goutte ocre) ; raccord de couleur des deux côtés : le cadre entier est le lavis ocre-pale #EFD7A6 à 100 %, sans grain ni texte
- handoff_out: à 4.87 : cam(5300, 560, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P3 : la salle pleine (table, six silhouettes ocre et accent, trois portables allumés, trois feuilles à lignes de couleur, tasse ocre-pale) ; P4 au cadrage de référence : feuille du bulletin (300 × 400 à (5700, 520), en-tête à l'encre, lignes vides) à gauche, fiche de séquence (320 × 220 à (6400, 520), cadre à l'encre, titre Caveat « Séquence 3 », trois lignes ink-light) à droite ; sous-titre sorti ; grain 55 %

Word cues: Je@0.27 forme@0.58 vos@0.86 équipes@1.14 pédagogiques@1.42 à@2.10 l'IA@2.28 sur@2.66 leurs@2.94 outils@3.20 et@3.58 leurs@3.80 vrais@4.02 documents@4.36

Scene 1 (0.00 à 2.60 s) : P13, le lavis sèche en salle pleine
  TEXTE ÉCRAN : sous-titre « Je [boîte : forme] vos équipes pédagogiques à l'IA, » (Je 0.27, boîte tracée 0.54, forme 0.58, vos 0.86, équipes 1.14, pédagogiques 1.42, à 2.10, l'IA 2.28) ; il sort de 2.46 à 2.60 ; écart : la table devance « forme » de 0,2 s.
  IMAGE DE DÉPART : le cadre entier ocre-pale (handoff_in), caméra cam(4318, 540, 1.08).
  ÉTAPES : 0.00 le lavis sèche de l'intérieur (aqDry 0 → 1 en 0,6 s) : son anneau fonce, le papier de P3 apparaît par le centre (clip-path ellipse 100 % → 60 %, 0,5 s expo.out) et il reste un grand lavis de sol ocre-pale à 55 % ; 0.30 le grain revient (0,2 s) ; 0.40 la table se dessine à l'encre et son lavis brun se pose (0,4 s) ; 0.58 « forme » ; 0.86 « vos » : les six chaises se dessinent (0,05 s d'écart) ; 1.00 à 1.70 les six silhouettes se peignent par coups de pinceau (buste scaleY 0 → 1, 0,16 s, tête ×0,2 → 1), 0,1 s d'écart, ocre à gauche, bordeaux à droite ; 1.42 « pédagogiques » ; 2.10 « à » : les silhouettes se penchent vers la table (2°) ; 2.28 « l'IA » : trois portables s'allument (lavis ocre-pale ×0,2 → 1) ; 2.46 le sous-titre sort ; 2.50 départ du cran.
  PISTE CAMÉRA : dérive échelle -1,5 %/s (de 1.08 vers 1.0) et x +14 u/s de 0.00 à 2.50 ; 2.50 à 2.64 cran vers cam(4318, 600, 1.3) (expo.inOut, flou 6 px).
  COUCHES ET PROFONDEUR : avant-plan une silhouette de dos au premier plan floue (6 px) coupée par le bord bas et le bord flou de P4 ; sujet la table et les silhouettes ; fond le lavis de sol ; couches animées 3 à 4.
  OBJET-PONT ET VECTEUR : la table amène les documents du plan suivant (le cran descend sur elle).
  SON : pinceau 23.40 à 24.10 global (1.00 à 1.70 local : les silhouettes) ; clic 24.68 global (2.28 local : les écrans).
  IMAGE CLÉ : 1.80 : la salle des profs pleine et colorée, six silhouettes ocre et bordeaux autour de la table, trois portables allumés, « forme » en boîte.

Scene 2 (2.60 à 4.87 s) : P14, les outils et les vrais documents sur la table, whip
  TEXTE ÉCRAN : sous-titre « sur leurs outils et leurs vrais [boîte : documents]. » (sur 2.66, leurs 2.94, outils 3.20, et 3.58, leurs 3.80, vrais 4.02, boîte tracée 4.32, documents 4.36) ; il sort de 4.73 à 4.87 ; écart : les feuilles glissent 0,3 s avant « documents ».
  ÉTAPES : 2.60 à 2.74 fin du cran sur la table ; 2.66 « sur » : l'écran du portable central montre une fenêtre dessinée (aqWindow 300 × 180 tracée, 0,3 s) ; 3.20 « outils » : deux autres écrans montrent la même fenêtre (0,1 s d'écart) ; 3.58 « et » : la tasse ocre-pale se pose sur la table (×1,1 flou 6 → net) ; 4.02 « vrais » : trois feuilles à lignes de couleur glissent sur la table depuis la droite (x +500 → 0, 0,16 s power2.in, 0,08 s d'écart) ; 4.36 « documents » : elles se tassent ; 4.70 fin ; 4.73 départ du whip vers P4 (power2.in, flou 0 → 12).
  PISTE CAMÉRA : dérive x +12 u/s, échelle +1 %/s de 2.74 à 4.73 ; 4.73 à 4.87 whip vers la droite (power2.in, +7000 u/s à la couture).
  COUCHES ET PROFONDEUR : avant-plan les épaules d'une silhouette floues coupées par le bord bas ; sujet les documents et les écrans nets ; fond le lavis de sol ; couches animées 3.
  OBJET-PONT ET VECTEUR : les feuilles à lignes de couleur annoncent le bulletin de P4 (même papier, mêmes lignes) ; vecteur : whip vers la droite repris par la séquence 8.
  SON : papier 26.42 à 26.60 global (4.02 à 4.20 local) ; whoosh court 27.13 global (4.73 local).
  IMAGE CLÉ : 4.40 : la table de près, trois portables avec leur fenêtre dessinée, trois feuilles à lignes ocre et bordeaux, la tasse, « documents » en boîte.

## Frame 8 : Un bulletin, une séquence · 27.27 → 32.14

- scene: Le whip atterrit sur la page P4 : une goutte bordeaux tombe sur la feuille du bulletin et cinq lignes s'écrivent à l'encre, une coche relit ; cran vers la fiche de séquence qui se dédouble en deux versions, ocre et bordeaux ; whip
- duration: 4.87s
- transition_in: cut
- status: animated
- src: compositions/frames/08-bulletin.html
- voiceover: "Un bulletin se rédige en quelques minutes. Une séquence s'adapte à chaque classe."
- type: demo
- blueprint: spatial-pan-stations (Adapt)
- focal: le bulletin qui s'écrit, puis la fiche qui se dédouble
- rules: svg-path-draw, scale-swap-transition
- world: light
- handoff_in: à 0.00 : cam(5300, 560, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P3 : la salle pleine (table, six silhouettes ocre et accent, trois portables allumés, trois feuilles à lignes de couleur, tasse ocre-pale) ; P4 au cadrage de référence : feuille du bulletin (300 × 400 à (5700, 520), en-tête à l'encre, lignes vides) à gauche, fiche de séquence (320 × 220 à (6400, 520), cadre à l'encre, titre Caveat « Séquence 3 », trois lignes ink-light) à droite ; sous-titre sorti ; grain 55 %
- handoff_out: à 4.87 : cam(7030, 560, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P4 : bulletin écrit (5 lignes accent, coche ocre en marge de la ligne 3), deux fiches de séquence côte à côte (ocre « classe A » à (6310, 520), accent-pale « classe B » à (6490, 520)) ; P5 au cadrage de référence : fenêtre « NOUVEAU MESSAGE » (620 × 420 à (7450, 520), 9 lignes ink-light) à gauche, papier nu à droite (7786 à 8500) ; sous-titre sorti ; grain 55 %

Word cues: Un@0.18 bulletin@0.35 se@0.73 rédige@0.97 en@1.25 quelques@1.55 minutes@1.85 Une@2.56 séquence@2.79 s'adapte@3.23 à@3.77 chaque@4.07 classe@4.26

Scene 1 (0.00 à 2.40 s) : P15, le bulletin s'écrit
  TEXTE ÉCRAN : sous-titre « Un [boîte : bulletin] se rédige en quelques minutes. » (Un 0.18, boîte tracée 0.31, bulletin 0.35, se 0.73, rédige 0.97, en 1.25, quelques 1.55, minutes 1.85) ; il sort de 2.26 à 2.40 ; écart : la goutte touche 0,1 s avant « bulletin », les lignes s'écrivent sur « rédige ».
  IMAGE DE DÉPART : handoff_in (le whip en cours, P4 arrive de la droite).
  ÉTAPES : 0.00 à 0.22 fin du whip, atterrissage sur cam(6052, 540, 1.0) (expo.out, flou 12 → 0) ; 0.18 « Un » : une goutte accent arrive de la caméra ; 0.26 impact sur la feuille du bulletin (×0,2 → 1, 0,12 s) ; 0.35 « bulletin » ; 0.45 la tache sèche (0,4 s) et la première ligne s'écrit depuis elle (masque, 0,2 s) ; 0.73 à 1.55 les lignes 2 à 5 s'écrivent (0,2 s chacune) ; 1.25 « en » : la feuille se tasse ; 1.85 « minutes » : une coche ocre se trace en marge de la ligne 3 (0,2 s) ; 2.26 le sous-titre sort ; 2.30 départ du cran vers la fiche.
  PISTE CAMÉRA : atterrissage 0.00 à 0.22 ; dérive x +14 u/s, échelle +1 %/s de 0.22 à 2.30 ; 2.30 à 2.44 cran vers cam(6400, 520, 1.3) (expo.inOut, flou 6 px).
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P5 (7 px) coupé par le bord droit et la goutte en vol ; sujet la feuille nette ; fond le papier ; couches animées 3.
  OBJET-PONT ET VECTEUR : la fiche de séquence, à droite, devient le sujet (le cran va vers elle).
  SON : goutte 27.53 global (0.26 local) ; stylo 27.72 à 28.90 global (0.45 à 1.63 local) ; stylo 29.12 global (1.85 local : la coche).
  IMAGE CLÉ : 1.60 : la feuille du bulletin, quatre lignes bordeaux écrites et la cinquième en cours, la fiche de séquence floue à droite, « bulletin » en boîte.

Scene 2 (2.40 à 4.87 s) : P16, la fiche se dédouble pour deux classes, whip
  TEXTE ÉCRAN : sous-titre « Une [boîte : séquence] s'adapte à chaque classe. » (Une 2.56, boîte tracée 2.75, séquence 2.79, s'adapte 3.23, à 3.77, chaque 4.07, classe 4.26) ; il sort de 4.73 à 4.87 ; écart : la fiche se dédouble sur « s'adapte », synchro.
  ÉTAPES : 2.40 à 2.54 fin du cran sur la fiche ; 2.56 « Une » : la fiche se soulève (y -8, 0,1 s) ; 2.79 « séquence » : son titre « Séquence 3 » se souligne d'un trait d'encre (tracé 0,2 s) ; 3.23 « s'adapte » : une copie de la fiche glisse de 180 u vers la droite (0,2 s expo.out), la fiche d'origine recule de 90 u vers la gauche (même geste) : deux fiches côte à côte à (6310, 520) et (6490, 520) ; 3.50 la gauche prend un lavis ocre-pale (coup de pinceau, 0,2 s), la droite un lavis accent-pale ; 3.77 « à » : les deux se tassent ; 4.07 « chaque » : la note Caveat « classe A » se révèle sous la gauche ; 4.26 « classe » : « classe B » sous la droite ; 4.70 fin ; 4.73 départ du whip vers P5 (power2.in, flou 0 → 12).
  PISTE CAMÉRA : dérive x +10 u/s, échelle +1 %/s de 2.54 à 4.73 ; 4.73 à 4.87 whip vers la droite (power2.in, +7000 u/s à la couture).
  COUCHES ET PROFONDEUR : avant-plan le bord du bulletin flou (6 px) coupé par le bord gauche ; sujet les fiches nettes ; fond le papier ; couches animées 3 (fiches, lavis, notes).
  OBJET-PONT ET VECTEUR : les deux fiches (ocre, bordeaux) annoncent les deux couleurs de la grille de P5 ; vecteur : whip repris par la séquence 9.
  SON : papier 30.50 global (3.23 local : la fiche se dédouble) ; pinceau 30.77 global (3.50 local) ; whoosh court 32.00 global (4.73 local).
  IMAGE CLÉ : 4.30 : deux fiches de séquence côte à côte, l'une ocre « classe A », l'autre bordeaux « classe B », « séquence » en boîte.

## Frame 9 : Un mail, une grille · 32.14 → 37.25

- scene: Le whip atterrit sur la page P5 : la fenêtre d'un long mail se replie en trois lignes qui trouvent leur ton ; cran vers la droite où une grille d'évaluation se trace ligne à ligne avec ses étiquettes et ses coches ; whip
- duration: 5.11s
- transition_in: cut
- status: animated
- src: compositions/frames/09-mail-grille.html
- voiceover: "Un mail difficile trouve son ton. Une grille d'évaluation se construit en direct."
- type: demo
- blueprint: spatial-pan-stations (Adapt)
- focal: le mail qui se replie, puis la grille qui se trace
- rules: svg-path-draw, depth-of-field-blur
- world: light
- handoff_in: à 0.00 : cam(7030, 560, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P4 : bulletin écrit (5 lignes accent, coche ocre en marge de la ligne 3), deux fiches de séquence côte à côte (ocre « classe A » à (6310, 520), accent-pale « classe B » à (6490, 520)) ; P5 au cadrage de référence : fenêtre « NOUVEAU MESSAGE » (620 × 420 à (7450, 520), 9 lignes ink-light) à gauche, papier nu à droite (7786 à 8500) ; sous-titre sorti ; grain 55 %
- handoff_out: à 5.11 : cam(8760, 560, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P5 : mail replié en 3 lignes d'encre pleine, grille d'évaluation tracée (5 × 4 à (8150, 540)) avec ses trois étiquettes et trois coches ocre ; P6 au cadrage de référence : petit carnet (520 × 360 à (9520, 430), spirale, deux lignes vides) et la tasse à l'encre à (9900, 720), café gris, sans vapeur ; sous-titre sorti ; grain 55 %

Word cues: Un@0.18 mail@0.38 difficile@0.58 trouve@1.16 son@1.56 ton@1.90 Une@2.34 grille@2.60 d'évaluation@2.80 se@3.52 construit@3.88 en@4.34 direct@4.74

Scene 1 (0.00 à 2.10 s) : P17, le mail difficile trouve son ton
  TEXTE ÉCRAN : sous-titre « Un [boîte : mail] difficile trouve son ton. » (Un 0.18, boîte tracée 0.34, mail 0.38, difficile 0.58, trouve 1.16, son 1.56, ton 1.90) ; il sort de 1.96 à 2.10 ; écart : le mail se replie 0,4 s avant « ton ».
  IMAGE DE DÉPART : handoff_in (le whip en cours, P5 arrive de la droite).
  ÉTAPES : 0.00 à 0.22 fin du whip, atterrissage sur cam(7786, 540, 1.0) (expo.out, flou 12 → 0) : la fenêtre du mail à gauche, neuf lignes grises ; 0.18 « Un » : l'étiquette « NOUVEAU MESSAGE » se révèle ; 0.38 « mail » ; 0.58 « difficile » : les neuf lignes frémissent (rotation ±1°, 0,2 s, 0,02 s d'écart) ; 0.90 une goutte ocre arrive de la caméra ; 1.10 impact au milieu de la fenêtre (×0,2 → 1) ; 1.16 « trouve » : la tache sèche ; 1.50 les six lignes du bas s'effacent par le centre (aqErase, 0,2 s, 0,04 s d'écart) et les trois du haut passent à l'encre pleine (opacité 0,5 → 1, 0,2 s) ; 1.90 « ton » : la fenêtre se tasse ; 1.96 le sous-titre sort ; 2.00 départ du cran vers la droite.
  PISTE CAMÉRA : atterrissage 0.00 à 0.22 ; dérive x +14 u/s, échelle +1 %/s de 0.22 à 2.00 ; 2.00 à 2.14 cran vers cam(8150, 540, 1.2) (expo.inOut, flou 6 px).
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P6 (7 px) coupé par le bord droit et la goutte en vol ; sujet la fenêtre nette ; fond le papier nu à droite ; couches animées 3.
  OBJET-PONT ET VECTEUR : le papier nu à droite de la fenêtre reçoit la grille (le cran va vers lui).
  SON : goutte 33.24 global (1.10 local) ; pinceau 33.64 global (1.50 local).
  IMAGE CLÉ : 1.70 : la fenêtre « NOUVEAU MESSAGE » avec trois lignes d'encre pleine là où il y en avait neuf, la tache ocre séchée, « mail » en boîte.

Scene 2 (2.10 à 5.11 s) : P18, la grille d'évaluation se construit en direct, whip
  TEXTE ÉCRAN : sous-titre « Une [boîte : grille] d'évaluation se construit en direct. » (Une 2.34, boîte tracée 2.56, grille 2.60, d'évaluation 2.80, se 3.52, construit 3.88, en 4.34, direct 4.74) ; il sort de 4.97 à 5.11 ; écart : les lignes se tracent sur « grille », synchro.
  ÉTAPES : 2.10 à 2.24 fin du cran sur le papier nu ; 2.34 « Une » : la première ligne horizontale se trace (0,2 s) ; 2.60 « grille » : les trois autres horizontales (0,1 s d'écart) ; 2.80 « d'évaluation » : les cinq verticales se tracent (0,08 s d'écart) jusqu'à 3.40 ; 3.52 « se » : les étiquettes Caveat « critère », « acquis », « en cours » se révèlent (0,2 s, 0,1 s d'écart) ; 3.88 « construit » : trois coches ocre se tracent dans des cases (0,15 s, 0,15 s d'écart) ; 4.34 « en » : la grille se tasse ; 4.74 « direct » : une dernière coche ; 4.83 fin ; 4.97 départ du whip vers P6 (power2.in, flou 0 → 12).
  PISTE CAMÉRA : dérive x +12 u/s, échelle +1 %/s de 2.24 à 4.97 ; 4.97 à 5.11 whip vers la droite (power2.in, +7000 u/s à la couture).
  COUCHES ET PROFONDEUR : avant-plan le bord de la fenêtre du mail flou (6 px) coupé par le bord gauche ; sujet la grille nette ; fond le papier ; couches animées 3 (lignes, étiquettes, coches).
  OBJET-PONT ET VECTEUR : les coches ocre reviennent sur le carnet de P6 ; vecteur : whip repris par la séquence 10.
  SON : stylo 34.48 à 35.40 global (2.34 à 3.26 local : les lignes) ; stylo 36.02 à 36.50 global (3.88 à 4.36 local : les coches) ; whoosh court 37.11 global (4.97 local).
  IMAGE CLÉ : 4.40 : la grille d'évaluation à l'encre, trois étiquettes manuscrites, trois coches ocre, « grille » en boîte.

## Frame 10 : Aucun prérequis, votre quotidien · 37.25 → 40.95

- scene: Le whip atterrit sur la page P6 : un petit carnet manuscrit où « vos documents » et « vos outils » s'écrivent et se cochent ; à côté, la tasse se remplit d'un café ocre et sa vapeur se retrace ; whip vers la page suivante
- duration: 3.70s
- transition_in: cut
- status: animated
- src: compositions/frames/10-quotidien.html
- voiceover: "Aucun prérequis technique. On part de votre quotidien."
- type: reassurance
- blueprint: spatial-pan-stations (Adapt)
- focal: le carnet des outils, puis la tasse qui fume à nouveau
- rules: svg-path-draw, depth-of-field-blur
- world: light
- handoff_in: à 0.00 : cam(8760, 560, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P5 : mail replié en 3 lignes d'encre pleine, grille d'évaluation tracée (5 × 4 à (8150, 540)) avec ses trois étiquettes et trois coches ocre ; P6 au cadrage de référence : petit carnet (520 × 360 à (9520, 430), spirale, deux lignes vides) et la tasse à l'encre à (9900, 720), café gris, sans vapeur ; sous-titre sorti ; grain 55 %
- handoff_out: à 3.70 : cam(10500, 560, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P6 : carnet « vos documents », « vos outils » cochés d'ocre, tasse au café ocre-pale avec ses deux boucles de vapeur ; P7 au cadrage de référence : le tableau de P2 redessiné (chalkboard 1100 × 560 à (11254, 400)) avec ses 10 × 5 cases grises pleines, six silhouettes gris pâle devant (x 10800 à 11710, y 620 à 800) ; sous-titre sorti ; grain 55 %

Word cues: Aucun@0.29 prérequis@0.75 technique@1.21 On@1.95 part@2.19 de@2.43 votre@2.73 quotidien@3.03

Scene 1 (0.00 à 3.70 s) : P19, le carnet des outils et la tasse qui fume, whip
  TEXTE ÉCRAN : sous-titre « Aucun [boîte : prérequis] technique. » (Aucun 0.29, boîte tracée 0.71, prérequis 0.75, technique 1.21 ; sort 1.70 à 1.84) puis « On part de votre [boîte : quotidien]. » (On 1.95, part 2.19, de 2.43, votre 2.73, boîte tracée 2.99, quotidien 3.03 ; sort 3.56 à 3.70) ; écart : « vos documents » s'écrit sur « technique », la vapeur revient sur « quotidien », synchro.
  IMAGE DE DÉPART : handoff_in (le whip en cours, P6 arrive de la droite).
  ÉTAPES : 0.00 à 0.22 fin du whip, atterrissage sur cam(9520, 540, 1.0) (expo.out, flou 12 → 0) : le carnet ouvert, deux lignes vides, la tasse à droite ; 0.29 « Aucun » : la spirale du carnet se tasse (×1,02 → 1) ; 0.75 « prérequis » : « vos documents » s'écrit en Caveat (masque, 0,35 s) ; 1.21 « technique » : une coche ocre se trace devant (0,15 s) ; 1.70 le premier morceau sort ; 1.95 « On » : « vos outils » s'écrit (0,35 s) ; 2.19 « part » : sa coche ocre ; 2.43 « de » : le café de la tasse passe du gris à l'ocre-pale (un lavis ocre-pale s'ouvre ×0,2 → 1 dans la tasse, 0,2 s) ; 2.73 « votre » : la tasse se tasse (×1,02 → 1) ; 3.03 « quotidien » : les deux boucles de vapeur se retracent (aqDraw, 0,4 s, 0,1 s d'écart) : rime du gag ; 3.50 fin ; 3.56 départ du whip vers P7 (power2.in, flou 0 → 12).
  PISTE CAMÉRA : atterrissage 0.00 à 0.22 ; dérive x +14 u/s, échelle +1 %/s de 0.22 à 3.56 ; 3.56 à 3.70 whip vers la droite (power2.in, +7000 u/s à la couture).
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P7 (7 px) coupé par le bord droit ; sujet le carnet puis la tasse nets ; fond le papier ; couches animées 3 (écriture, coches, vapeur).
  OBJET-PONT ET VECTEUR : la tasse qui fume rejoue la tasse du gag ; vecteur : whip repris par la séquence 11.
  SON : stylo 38.00, 38.46 global (0.75, 1.21 local) ; stylo 39.20, 39.44 global (1.95, 2.19 local) ; goutte 39.68 global (2.43 local : le café) ; pinceau 40.28 global (3.03 local : la vapeur) ; whoosh court 40.81 global (3.56 local).
  IMAGE CLÉ : 3.20 : le petit carnet avec « vos documents » et « vos outils » cochés d'ocre, à droite la tasse au café ocre dont la vapeur se retrace, « quotidien » en boîte.

## Frame 11 : Le temps revient aux élèves · 40.95 → 45.00

- scene: Le whip atterrit sur la page P7, le tableau de la classe redessiné avec sa grille pleine de gris : les cases s'effacent ligne par ligne, les six élèves reviennent en ocre, nets ; le cadre du tableau s'efface et un grand lavis ocre les entoure ; whip vers la dernière page
- duration: 4.05s
- transition_in: cut
- status: animated
- src: compositions/frames/11-eleves.html
- voiceover: "Le temps gagné revient aux élèves. Et le sens avec."
- type: payoff
- blueprint: zoom-out-workspace-reveal (Adapt)
- focal: les cases qui s'effacent, puis les six élèves en ocre
- rules: depth-of-field-blur, waterfall-entry
- world: light
- handoff_in: à 0.00 : cam(10500, 560, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P6 : carnet « vos documents », « vos outils » cochés d'ocre, tasse au café ocre-pale avec ses deux boucles de vapeur ; P7 au cadrage de référence : le tableau de P2 redessiné (chalkboard 1100 × 560 à (11254, 400)) avec ses 10 × 5 cases grises pleines, six silhouettes gris pâle devant (x 10800 à 11710, y 620 à 800) ; sous-titre sorti ; grain 55 %
- handoff_out: à 4.05 : cam(12380, 540, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P7 : le tableau effacé (cadre d'encre seul), six silhouettes ocre nettes sur un grand lavis ocre-pale ; P8 vide (papier nu) ; sous-titre sorti ; grain 55 %

Word cues: Le@0.20 temps@0.45 gagné@0.63 revient@1.23 aux@1.61 élèves@1.81 Et@2.50 le@2.67 sens@2.89 avec@3.44

Scene 1 (0.00 à 2.30 s) : P20, les cases s'effacent, les élèves reviennent
  TEXTE ÉCRAN : sous-titre « Le [boîte : temps] gagné revient aux [trait : élèves]. » (Le 0.20, boîte tracée 0.41, temps 0.45, gagné 0.63, revient 1.23, aux 1.61, élèves 1.81 avec le trait ocre tracé de 1.81 à 2.21) ; il sort de 2.30 à 2.44 ; écart : les cases s'effacent dès « temps », les élèves se colorent sur « revient » (0,6 s avant « élèves »).
  IMAGE DE DÉPART : handoff_in (le whip en cours, P7 arrive de la droite).
  ÉTAPES : 0.00 à 0.20 fin du whip, atterrissage sur cam(11254, 540, 1.0) (expo.out, flou 12 → 0) : la grille pleine, six élèves gris pâle ; 0.20 « Le » ; 0.45 « temps » : la première ligne de cases s'efface par le centre (aqErase, 0,25 s) ; 0.63 « gagné » : les lignes 2 et 3 ; 0.95 les lignes 4 et 5 ; 1.23 « revient » : les six élèves reprennent leur ocre par coups de pinceau (scaleX 0 → 1 depuis la gauche sur chaque tache, 0,16 s, 0,1 s d'écart) ; 1.61 « aux » : les élèves se redressent (rotation -2° → 0, 0,2 s) ; 1.81 « élèves » : le trait ocre ; 2.10 scintillement : trois points ocre-2 naissent et s'éteignent au-dessus des élèves (0,3 s) ; 2.30 le sous-titre sort.
  PISTE CAMÉRA : atterrissage 0.00 à 0.20 ; dérive x +12 u/s, échelle +1 %/s de 0.20 à 2.30.
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P8 (7 px) coupé par le bord droit ; sujet les élèves nets ; fond le tableau ; couches animées 3 (cases, élèves, points).
  OBJET-PONT ET VECTEUR : les élèves redevenus ocre sont la rime de la page du tableau (séquence 5) ; le tableau vidé devient le fond qui s'efface au plan suivant.
  SON : pinceau 41.40 à 42.00 global (0.45 à 1.05 local : les cases) ; pinceau 42.18 à 42.80 global (1.23 à 1.85 local : les élèves) ; scintillement 43.05 global (2.10 local).
  IMAGE CLÉ : 1.90 : le tableau vidé de ses cases, six élèves en taches ocre nettes devant, « élèves » souligné d'un trait ocre.

Scene 2 (2.30 à 4.05 s) : P21, et le sens avec : le tableau s'efface, le lavis ocre, whip
  TEXTE ÉCRAN : sous-titre « Et le [boîte : sens] [trait : avec]. » (Et 2.50, le 2.67, boîte tracée 2.85, sens 2.89, avec 3.44 avec le trait ocre tracé de 3.44 à 3.84) ; il sort de 3.86 à 4.00 ; écart : le lavis ocre se répand sur « sens », synchro.
  ÉTAPES : 2.30 recul court vers cam(11254, 560, 0.95) (0,3 s expo.out) ; 2.50 « Et » : le cadre du tableau et son lavis gris pâlissent (aqErase 0 → 0,7, 0,3 s) ; 2.89 « sens » : un grand lavis ocre-pale se répand derrière les élèves (coup de pinceau depuis la gauche, 0,4 s power2.out) ; 3.20 les élèves se penchent les uns vers les autres (2°, 0,2 s) ; 3.44 « avec » : le trait ocre ; 3.60 le lavis ocre sèche (aqDry, 0,3 s) ; 3.86 le sous-titre sort ; 3.91 départ du whip vers P8 (power2.in, flou 0 → 12).
  PISTE CAMÉRA : recul 2.30 à 2.60 ; dérive x +12 u/s de 2.60 à 3.91 ; 3.91 à 4.05 whip vers la droite (power2.in, +7000 u/s à la couture).
  COUCHES ET PROFONDEUR : avant-plan le bord flou de P8 ; sujet les élèves ; fond le lavis ocre ; couches animées 2 à 3.
  OBJET-PONT ET VECTEUR : la couleur revenue déborde vers P8 dans le whip ; vecteur : whip repris par la séquence 12.
  SON : pinceau 43.84 global (2.89 local) ; whoosh court 44.86 global (3.91 local).
  IMAGE CLÉ : 3.60 : six élèves ocre sur un grand lavis ocre pâle, le tableau presque effacé derrière, « avec » souligné d'un trait ocre.

## Frame 12 : Antoine Contino, formateur IA · 45.00 → 49.00

- scene: Le whip atterrit sur la page P8, nue : la même goutte d'encre bordeaux qu'au début du film 1 tombe et la signature se trace depuis elle, « formateur IA » s'écrit dessous ; la caméra descend vers une tache ocre qui tombe et sèche en bouton « Réserver un appel » avec les deux adresses ; le curseur entre en courbe
- duration: 4.00s
- transition_in: cut
- status: animated
- src: compositions/frames/12-signature.html
- voiceover: "Antoine Contino, formateur IA. Réservez un appel."
- type: cta
- blueprint: logo-assemble-lockup (Adapt)
- focal: la signature qui se trace, puis le bouton ocre
- rules: svg-path-draw, cursor-click-ripple
- world: light
- handoff_in: à 0.00 : cam(12380, 540, 1.05) flou 12 px ; caméra en plein whip vers la droite (+7000 u/s en x), dérive 0 ; monde : carnet ; P7 : le tableau effacé (cadre d'encre seul), six silhouettes ocre nettes sur un grand lavis ocre-pale ; P8 vide (papier nu) ; sous-titre sorti ; grain 55 %
- handoff_out: à 4.00 : cam(12988, 600, 1.0) flou 0 ; dérive x +12 u/s, échelle +1 %/s ; monde : carnet, page P8 ; signature « Antoine Contino » tracée en accent à (12988, 380), « formateur IA » à (12988, 470), bouton ocre « Réserver un appel » à (12988, 660), adresses à (12988, 760) ; le curseur à (13230, 790) en plein mouvement courbe vers la pointe du bouton (13060, 672), reste 0,20 s de trajet power3.out ; sous-titre « Réservez un appel. » en place, boîte sur « Réservez » ; grain 55 %

Word cues: Antoine@0.31 Contino@0.76 formateur@1.74 IA@2.08 Réservez@2.62 un@3.20 appel@3.44

Scene 1 (0.00 à 2.50 s) : P22, la goutte, la signature se trace
  TEXTE ÉCRAN : sous-titre « Antoine Contino, [boîte : formateur IA]. » (Antoine 0.31, Contino 0.76, boîte tracée 1.70, formateur 1.74, IA 2.08) ; il sort de 2.36 à 2.50 ; écart : la goutte touche 0,08 s avant « Antoine », la signature s'écrit sur le nom.
  IMAGE DE DÉPART : handoff_in (le whip en cours, P8 nue arrive de la droite).
  ÉTAPES : 0.00 à 0.22 fin du whip, atterrissage sur cam(12988, 400, 1.15) (expo.out, flou 12 → 0) : la page nue ; 0.08 la goutte accent arrive de la caméra (×4, flou 10, 0,16 s) ; 0.23 impact à (12560, 330), deux éclaboussures ; 0.31 « Antoine » : la signature « Antoine Contino » se trace depuis la goutte (masque qui avance de gauche à droite, 1,0 s power1.inOut, encre accent) ; 0.76 « Contino » : le tracé passe le « C » ; 1.31 la signature est complète ; 1.40 elle sèche (opacité 0,85 → 1, 0,5 s) ; 1.74 « formateur » : « formateur IA » se révèle dessous en DM Sans ink-2 (masque, 0,3 s) ; 2.08 « IA » : la traînée de la goutte s'allonge sous la signature (tracé 0,2 s) ; 2.36 le sous-titre sort ; 2.40 départ du cran vers le bas.
  PISTE CAMÉRA : atterrissage 0.00 à 0.22 ; dérive x +12 u/s, échelle +1 %/s de 0.22 à 2.40 ; 2.40 à 2.70 cran vers cam(12988, 600, 1.0) (expo.inOut, flou 6 px).
  COUCHES ET PROFONDEUR : avant-plan la goutte en vol puis le bord du carnet flou coupé par le bord droit ; sujet la signature nette ; fond le papier et le bureau ; couches animées 2 à 3.
  OBJET-PONT ET VECTEUR : le cran descend de la signature au bouton ; la goutte posée reste au début de la signature.
  SON : goutte 45.23 global (0.23 local) ; stylo 45.31 à 46.31 global (0.31 à 1.31 local : la signature).
  IMAGE CLÉ : 1.00 : la page nue, la goutte bordeaux à gauche et la signature « Antoine Contino » à moitié tracée depuis elle.

Scene 2 (2.50 à 4.00 s) : P23, la tache ocre sèche en bouton, le curseur entre
  TEXTE ÉCRAN : sous-titre « [boîte : Réservez] un appel. » (boîte tracée 2.58, Réservez 2.62, un 3.20, appel 3.44) ; il reste en place ; écart : la tache tombe 0,3 s avant « Réservez », le bouton est lisible sur « appel ».
  ÉTAPES : 2.50 à 2.70 fin du cran sur le milieu bas de la page ; 2.34 une goutte ocre arrive de la caméra ; 2.48 impact à (12988, 660) : la tache s'ouvre ×0,2 → 1 (0,12 s) en forme allongée (520 × 110) ; 2.62 « Réservez » : la tache sèche (aqDry 0 → 1, 0,4 s) et le texte « Réserver un appel » se révèle dedans (masque, 0,25 s) ; 3.00 un cerne d'encre fin se trace autour (0,2 s) ; 3.20 « un » : les deux adresses se révèlent dessous (DM Sans 24 px ink-2, masque 0,3 s) : « calendly.com/antoine-cntno/30min · antoinecontino.fr/ecoles » ; 3.44 « appel » : le bouton se tasse (×1,02 → 1) ; 3.76 le curseur entre par le bas droit du cadre, à (13420, 980) en coordonnées monde, et commence son unique mouvement courbe vers la pointe du bouton (13060, 672) ; 4.00 couture : le curseur est à (13230, 790), il lui reste 0,20 s de trajet power3.out.
  PISTE CAMÉRA : dérive x +12 u/s, échelle +1 %/s de 2.70 à 4.00 (elle continue telle quelle dans la séquence 13).
  COUCHES ET PROFONDEUR : avant-plan le curseur net (il est le sujet qui arrive) et le bord du carnet flou ; sujet le bouton ; fond la signature floue (4 px) en haut ; couches animées 3 (tache, texte, curseur).
  OBJET-PONT ET VECTEUR : le curseur en plein mouvement traverse la couture : la séquence 13 reprend exactement sa position (13230, 790) et son reste de trajet (0,20 s power3.out vers (13060, 672)).
  SON : goutte 47.48 global (2.48 local).
  IMAGE CLÉ : 3.60 : la page de fin, la signature en haut, le bouton ocre « Réserver un appel » au centre, les deux adresses dessous, le curseur qui arrive du coin bas droit, « Réservez » en boîte.

## Frame 13 : Réserver un appel · 49.00 → 52.00

- scene: Le curseur finit sa courbe et clique le bouton : pression, la tache passe au bordeaux puis revient ocre, une onde s'ouvre ; la page tient, vivante, puis le noir monte comme l'encre du pivot
- duration: 3.00s
- transition_in: cut
- status: animated
- src: compositions/frames/13-clic.html
- voiceover: ""
- type: cta
- blueprint: cta-morph-press (Adapt)
- focal: le bouton cliqué, puis la page entière qui tient
- rules: cursor-click-ripple, press-release-spring
- world: light
- handoff_in: à 0.00 : cam(12988, 600, 1.0) flou 0 ; dérive x +12 u/s, échelle +1 %/s ; monde : carnet, page P8 ; signature « Antoine Contino » tracée en accent à (12988, 380), « formateur IA » à (12988, 470), bouton ocre « Réserver un appel » à (12988, 660), adresses à (12988, 760) ; le curseur à (13230, 790) en plein mouvement courbe vers la pointe du bouton (13060, 672), reste 0,20 s de trajet power3.out ; sous-titre « Réservez un appel. » en place, boîte sur « Réservez » ; grain 55 %
- handoff_out: aucun (fin du film, noir à 52.00)

Word cues: (aucun mot : tenue de fin)

Scene 1 (0.00 à 3.00 s) : P24, le clic, la tenue vivante, le noir
  TEXTE ÉCRAN : sous-titre « [boîte : Réservez] un appel. » déjà en place ; il sort de 2.40 à 2.60 avec le reste ; écart : aucun mot.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.20 le curseur achève sa courbe (power3.out) jusqu'à la pointe sur le bouton (13060, 672) ; 0.25 clic : pression (curseur et bouton ×0,85, 0,06 s yoyo), la tache passe en accent (0,07 s) puis revient ocre (0,17 s), le texte reste ink ; 0.27 une onde accent s'ouvre depuis le point du clic (×0,2 → ×1,8, opacité 0,55 → 0, 0,45 s power1.out) ; 0.40 un cerne d'encre plus franc entoure le bouton (tracé 0,2 s) ; 0.60 le curseur s'écarte de 30 u vers le bas droit (0,4 s power3.out) et reste ; 0.80 à 2.40 tenue vivante : la granulation des taches dérive (6 u sur 1,6 s, aller simple), le grain du papier glisse de 8 u/s, la traînée de la goutte sèche (aqDry 0,6 → 1 en 1,2 s), l'ombre du carnet respire (un cycle de 1,6 s) ; 2.40 le sous-titre sort ; 2.50 à 3.00 le noir monte (un lavis canvas s'ouvre depuis le bas du cadre, scaleY 0 → 1,2 en 0,5 s power2.in, par-dessus tout) : noir à 3.00.
  PISTE CAMÉRA : dérive x +12 u/s, échelle +1 %/s de 0.00 à 2.50 ; 2.50 à 3.00 la dérive continue sous le noir.
  COUCHES ET PROFONDEUR : avant-plan le curseur net ; sujet le bouton puis la page entière ; fond le bureau grainé ; couches animées 2 à 3 (onde, granulation, grain) ; aucune image figée.
  OBJET-PONT ET VECTEUR : aucun (fin du film) : le lavis noir qui monte rejoue l'encre du pivot.
  SON : clic 49.25 global (0.25 local).
  IMAGE CLÉ : 0.40 : le bouton ocre pressé avec le curseur dessus, l'onde bordeaux qui s'ouvre, la signature au-dessus, les deux adresses dessous.
