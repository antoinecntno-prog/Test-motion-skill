---
format: 1920x1080
duration: "52.00s"
message: "IFS : vous envoyez votre design et votre logo, nous faisons le reste, livré en moins d'un mois."
arc: Hook → Problem → Pivot → Turn → Demo → Payoff → CTA
audience: "dirigeants bénévoles et responsables équipement des clubs sportifs amateurs, sur la page LinkedIn d'IFS"
mode: autonomous
captions: disabled
music: "pre-mixed with voice and SFX in assets/audio/mix.wav (mounted at root by the orchestrator)"
direction: "A « Le fil rouge » (DIRECTIONS.md), joueur stickman au modèle validé par Antoine le 03/10/2026"
styleframes: "styleframes/png/A1.png (3.9 s), styleframes/png/A2.png (31.6 s), styleframes/png/A3.png (39.3 s)"
patterns: ../patterns/STORYBOARD-CRAFT.md, ../patterns/PATTERNS.md
---

## Video direction

- **Un seul objet** (frame.md) : le fil rouge de l'aiguille du logo IFS court dans quatre lieux que la caméra parcourt de gauche à droite. Séquences 1 à 3 = DOULEUR dans le monde W1 sur l'encre ; séquence 4 = PIVOT sur le noir ; séquences 5 à 8 = SOLUTION dans l'atelier W2 sur le papier ; séquence 9 = MATCH dans la salle W3 ; séquences 10 et 11 = FIN sur l'encre W4. Chaque séquence peint son propre fond sur un calque `class="clip"` de toute sa durée.
- **Coutures invisibles** : toutes les séquences entrent en `cut` ; chaque couture tombe au sommet du flou d'un mouvement de caméra et le `handoff_out` de la séquence N est recopié mot pour mot dans le `handoff_in` de N+1. Exceptions voulues : 15.20 coupe franche au noir (pivot, sur l'impact grave) ; 37.45 coupe franche au sommet d'un whip (changement d'acte : le jour du match) ; 18.70 le point de lumière s'ouvre sur le papier (éclair de lumière ajouté par assemble.sh) ; 42.20 au sommet du flou du tilt, la salle laisse place au sol d'encre de la fin.
- **Texte** (lisible sans le son) : chaque phrase de la voix est un `subtitle` en bas au centre (bande y 890 à 980, rien d'autre dedans), mot par mot sur les temps de chaque séquence (`mot@secondes`, temps locaux). Un seul mot ou groupe par phrase dans la `key-word-box` ([boîte : …]). Aucun autre texte coloré. Un seul moment typographique : « On reprend depuis le début. » au pivot, centré, 84 px.
- **Pics** : 4 traits [trait : …] : « premier match » (3.90), « début » (16.54), « moins d'un mois » (36.60), « resté » (41.14).
- **Une seule chose à regarder** : chaque plan isole le sujet de la phrase ; travelling toujours de gauche à droite dans un monde, jamais d'aller-retour ; marges gauche et droite égales ; aucun décor sans sens ; le fil ne traverse jamais une phrase (il reste au-dessus de y 860).
- **Vraies interfaces** (frame.md) : fenêtre de message à la mise en page Outlook web, redessinée et anonymisée (SOURCES.md) ; le vrai studio de personnalisation IFS (capture du 03/10/2026) ; le vrai maillot Basket Club Eschau (photos détourées) ; le logo IFS.
- **Parallaxe** (une par acte au moins) : pendant chaque dérive, l'avant-plan flou glisse 2,5 fois plus vite que le sujet et le fond 0,4 fois (W1 : boucles de fil et page JUIN ; W2 : règle, papier de soie, boucles de fil ; W3 : joueur adverse flou et projecteurs ; W4 : boucle de fil floue).
- **Grammaire de mouvement** : deux vitesses, gestes de 1 à 6 images (expo.out) et dérives linéaires qui ne s'arrêtent jamais ; la zone 0,3 à 0,9 s est réservée à la caméra et au curseur (expo, power3, power4) ; les éléments arrivent trop grands et flous puis se posent, jamais en fondu à leur taille finale ; aucune tenue figée ; aucune transition « effet ».
- **Texte visible** : exactement le texte cité dans les lignes Scene et les interfaces de frame.md, rien d'autre.
- **Négatifs** : diaporama (tout à t=0), écran de veille, objet dédoublé, texte coloré à la place de la boîte, grande phrase, mot géant, symbole abstrait, curseur qui hésite, plusieurs objets qui bougent pendant une couture, donnée réelle d'un mail (adresse, nom, prix, quantité), mesure de taille inventée.

**MONDE**
- Acte 1 (0.00 à 15.20), W1 « l'attente », 12 000 × 1 080 u sur sol d'encre rayé : S1 fenêtre de message (960, 470) · S2 calendrier (3000, 470) · S3 salle du club : 4 joueurs stickman en chasuble grise, l'entraîneur au téléphone, carte de suivi (5400, 500) · S4 carton ouvert, maillot délavé et nuancier « Rouge club » (7800, 470) · S5 hublot de machine à laver (10000, 470). Fil : threadPath('W1').
- Pivot (15.20 à 18.70) : noir #110C15 pur, l'aiguille du logo (520 px), le fil, la phrase centrée.
- Acte 2 (18.70 à 37.45), W2 « l'atelier », 15 000 × 1 080 u sur sol papier rayé magenta : S6 enveloppe et fenêtre de message « À : IFS » (960, 470) · S7 studio IFS (3200, 470) · S8 BAT et tampon (5400, 470) · S9 tapis de coupe et grille de tailles (7600, 470) · S10 presse et maille en macro (9800, 470) · S11 couture (12000, 470) · S12 carton d'expédition (14200, 470). Fil : threadPath('W2').
- Acte 3 (37.45 à 42.20), W3 « le match » : salle de nuit (ground-gym), panier de trois quarts à droite (planche (1590 à 1750, -20 à 390) à l'écran au cadrage de départ), joueur stickman n° 15 qui smashe (styleframes/png/A3.png).
- Fin (42.20 à 52.00), W4 : sol d'encre, icône IFS et wordmark, l'aiguille et son fil, promesse, bouton, URL.
- Couleurs de rôle : accent magenta = boîte du mot clé, 4 traits, bouton final, tampon VALIDÉ, onglet actif du studio ; rouge du fil = le fil, le maillot, le nuancier ; orange délavé = le rouge qui a viré (douleur) ; jaune spark = l'état « En cours d'acheminement » seulement ; bleu Outlook et vert Excel dans la fenêtre de message.

**SIGNATURES**
- Mécanisme 1 « le fil trace » (svg-path-draw, fxDrawThread) : 0.70 le fil sort du bouton Envoyer · 2.40 il file vers le calendrier · 5.60 il se noue · 18.98 il sort du chas de l'aiguille · 20.10 il trace l'enveloppe · 22.10 il contourne le maillot dans le studio · 24.85 il trace la coche du BAT · 27.10 il suit le patron M · 33.10 il devient la couture · 35.70 il fait la ficelle du carton · 38.40 il devient le brin rouge du filet · 42.30 il rentre dans le chas du logo (12 fois).
- Mécanisme 2 « l'aiguille pique » : 15.40 l'aiguille traverse le noir · 18.40 sa pointe devient le point de lumière · 33.30, 33.80, 34.30 trois points de couture · 42.90 elle se pose dans l'icône du logo (6 fois).
- Registres de texte : sous-titre mot à mot = gris flou → net (0,14 s) puis encre (0,2 s) ; boîte = tracé depuis la gauche (0,16 s power3.out) ; trait = pinceau depuis la gauche (0,4 s power2.out) ; moment typographique = lettres qui convergent (0,5 s expo.out).
- Rimes : l'aiguille du pivot (15.40) est celle du logo final (42.90) ; le nuancier « Rouge club » à côté du rouge délavé (10.90) revient contre le maillot du match (41.14) ; la fenêtre de message de juin (0.00) revient adressée à IFS (19.54) ; les joueurs en chasuble du gag (6.40) reviennent en maillot sur le terrain (37.45).

**PARTITION CAMÉRA** (temps globaux) : 0.00 dérive sur S1 · 1.96 poussée courte sur le bouton Envoyer · 2.30 whip S1 → S2 (sommet 2.45) · 2.62 atterrissage sur le calendrier · 4.40 whip S2 → S3 (couture 4.56) · 4.70 atterrissage sur la salle · 6.40 poussée lente vers le téléphone de l'entraîneur · 8.90 whip S3 → S4 (couture 9.05) · 9.20 atterrissage sur le carton · 12.35 whip S4 → S5 (sommet 12.50) · 12.70 poussée dans le hublot · 15.20 coupe franche au noir · 15.40 dérive sur le noir · 18.40 cran vers le point de lumière · 18.70 le point s'ouvre sur le papier · 21.20 whip S6 → S7 (sommet 21.35) · 23.85 whip S7 → S8 (couture 24.00) · 26.55 whip S8 → S9 (sommet 26.70) · 29.55 plongée dans la ligne de coupe (couture 29.80) · 29.95 atterrissage sur la maille S10 · 32.65 whip S10 → S11 (couture 32.80) · 35.20 whip S11 → S12 (sommet 35.32) · 37.30 whip vers la droite, coupe franche 37.45 · 37.45 dérive sur le joueur · 38.60 poussée vers le cercle · 40.05 poussée sur le dos du joueur suspendu et le nuancier · 41.95 tilt vers le haut (couture 42.20) · 42.40 atterrissage sur le logo · 46.60 cran vers le bouton (couture 46.75) · 47.85 clic · 48.10 à 52.00 dérive lente, noir à 52.00.

**VOIX** : minutage dans onsets.json. Silences de plus de 0,4 s, chacun écrit comme un plan : 2.26 à 2.80 (whip vers le calendrier, la page JUIN s'arrache) · 4.30 à 4.82 (whip vers la salle, les joueurs s'échauffent) · 6.40 à 9.19 (le gag muet : chasubles, téléphone, suivi qui ne bouge pas, le nœud qui se serre) · 16.87 à 18.84 (le pivot : l'aiguille et le fil sur le noir) · 21.08 à 21.48 (whip vers le studio) · 41.71 à 42.49 (le brin rouge quitte le filet) · 48.24 à 52.00 (carte de fin : clic, tenue vivante, noir).

**COUPES** (voix narrative, quota 0 à 4) : 15.20 · « On » (15.43) · changement d'acte, de la douleur au pivot, sur l'impact grave ; 37.45 · « Samedi » (37.53) · changement d'acte, de l'atelier au match, au sommet du flou d'un whip. Toutes les autres jonctions sont des coutures de caméra ou d'objet.

**RYTHME** : douleur (0 à 15.20) 12 plans = 7,9 plans / 10 s ; pivot 2 plans ; solution (18.70 à 37.45) 12 plans = 6,4 plans / 10 s ; match et fin (37.45 à 52.00) 6 plans = 4,1 plans / 10 s.

**SON** (proposition, verrouillée à l'étape 5 ; l'image ne bouge pas pour le son) : clic 0.94 (Envoyer) · whoosh court 2.30 · pop 2.62 (page SEPTEMBRE) · whoosh court 4.40 · pop 5.94 (le nœud se serre) · erreur 8.40 (le suivi ne bouge pas) · whoosh court 8.90 · whoosh court 12.35 · montée 12.20 à 15.20 · impact grave 15.20 (coupe au noir) · scintillement 18.40 · whoosh cinématique 18.70 · clic 20.86 (« mail ») · whoosh court 21.20 · pop 23.40 (l'écusson se pose) · whoosh court 23.85 · impact sec (tampon VALIDÉ) 24.92 · whoosh court 26.55 · clic doux 29.06 (la lame) · whoosh 29.55 · pops doux 33.30, 33.80, 34.30 (points de couture) · whoosh court 35.20 · NOTIFICATION À DEUX TONS 35.84 (« livrés » : la signature) · whoosh court 37.30 · impact grave 39.06 (le smash) · carillon 41.42 · whoosh 41.95 · scintillement 42.90 (l'aiguille se pose) · clic 47.85.

## Frame 1 : Juin, septembre · 0.00 → 4.56

- scene: Sur l'encre, la fenêtre de message « Commande maillots · saison 2026 » part vers le fournisseur ; le fil rouge sort du bouton Envoyer ; la caméra file le long du fil jusqu'au calendrier de septembre où le samedi 5 est entouré « 1er match »
- duration: 4.56s
- transition_in: cut
- status: animated
- src: compositions/frames/01-juin.html
- voiceover: "Juin, vous commandez les maillots du club. Septembre, premier match..."
- type: hook
- blueprint: spatial-pan-stations (Adapt)
- focal: le bouton Envoyer de la fenêtre de message, puis le 5 entouré du calendrier
- rules: svg-path-draw, depth-of-field-blur
- world: dark
- handoff_in: aucun (ouverture du film) ; première image = sol d'encre W1, cam(960, 500, 1.1) flou 0, la fenêtre de message S1 au centre déjà composée (À : Fournisseur textile, objet, pièce jointe, corps), le curseur à 300 px en bas à droite du bouton Envoyer, la page JUIN floue tout près de la caméra en haut à droite, aucun fil
- handoff_out: à 4.56 : cam(4200, 560, 1.0) flou 12 px ; caméra en plein whip vers la droite (+6000 u/s en x), dérive 0 ; monde W1, sol d'encre ; fil tracé jusqu'à (4500, 660), couleur thread ; stations posées : fenêtre de message S1 envoyée, calendrier S2 page SEPTEMBRE avec le 5 entouré ; aucun joueur à l'écran ; sous-titre sorti ; grain 5 %

Word cues: Juin@0.03 vous@0.70 commandez@0.94 les@1.36 maillots@1.56 du@1.74 club@1.96 Septembre@2.62 premier@3.52 match@3.90

Scene 1 (0.00 à 2.30 s) : P1 et P2, juin, le mail part
  TEXTE ÉCRAN : sous-titre « [boîte : Juin], vous commandez les maillots du club. » (Juin 0.03, boîte tracée 0.00, vous 0.70, commandez 0.94, les 1.36, maillots 1.56, du 1.74, club. 1.96) ; il sort de 2.16 à 2.30.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 la page JUIN glisse de 40 px vers la caméra (flou 10 → 12) ; 0.10 le titre « Nouveau message » se tasse (×1,04 → 1, 0,1 s) ; 0.25 la pièce jointe « Commande maillots 2026.xlsx » se pose (×1,3 flou 6 → net, 0,12 s expo.out) ; 0.45 le curseur part en courbe vers Envoyer (0,45 s power3.out) ; 0.90 il presse (×0,85, 0,06 s), onde bleue, le bouton passe en bleu foncé ; 0.94 « commandez » ; 0.70 à 1.40 le fil rouge naît du bouton et se dessine vers la droite (fxDrawThread 0 → 0,08, expo.out) ; 1.10 la fenêtre se replie en carte (×1 → 0,62, 0,2 s power2.in) et glisse sur le fil comme sur un rail ; 1.36 « les » : la carte accélère sur le fil (x +60, 0,12 s) ; 1.60 la page JUIN s'arrache vers le haut à droite (rotation +18°, y -400, 0,25 s power2.in) ; 1.96 « club » : petite poussée vers la tête du fil ; 2.10 la carte sort par le bord droit (x +400, 0,14 s power2.in).
  PISTE CAMÉRA : dérive x +20 u/s, échelle -1 %/s de 0.00 à 1.90 ; 1.96 à 2.20 poussée ×1,1 → ×1,18 vers la tête du fil (expo.out) ; 2.30 départ du whip (power2.in, flou 0 → 12).
  COUCHES ET PROFONDEUR : avant-plan la page JUIN floue coupée par le bord droit ; sujet la fenêtre nette ; fond le sol rayé ; couches animées 2 à 3.
  OBJET-PONT ET VECTEUR : le fil sort du mail et devient le rail que la caméra suit ; vecteur vers la droite.
  SON : clic 0.94.
  IMAGE CLÉ : 0.92 : la fenêtre de message nette, le curseur qui presse Envoyer, le fil rouge qui naît du bouton, JUIN floue en avant-plan.

Scene 2 (2.30 à 4.56 s) : P3 et P4, septembre, premier match
  TEXTE ÉCRAN : sous-titre « [boîte : Septembre], [trait : premier match]... » (boîte tracée 2.58, Septembre 2.62, premier 3.52, match... 3.90 ; trait 3.52 à 3.92) ; il sort de 4.36 à 4.50.
  IMAGE DE DÉPART : la tête du fil filant vers la droite, flou de whip.
  ÉTAPES : 2.30 à 2.45 whip, le fil défile ; 2.45 sommet du flou ; 2.50 le calendrier S2 arrive trop grand et flou (×1,15 flou 8 → net, 0,14 s expo.out) et se pose à -3,5° ; 2.62 « Septembre » : le titre SEPTEMBRE 2026 s'imprime (lettres en 0,02 s d'écart) ; 2.90 la grille des jours s'allume ligne par ligne (0,03 s d'écart) ; 3.30 le fil remonte jusqu'au samedi 5 (fxDrawThread 0,08 → 0,22) ; 3.52 « premier » : le feutre rouge entoure le 5 (tracé circulaire 0,3 s power2.out) ; 3.90 « match » : « 1er match » s'écrit au-dessus (×1,2 flou 4 → net, 0,12 s) ; 4.10 le fil repart du 5 vers la droite et descend (fxDrawThread 0,22 → 0,30) ; 4.40 départ du whip.
  PISTE CAMÉRA : 2.30 à 2.45 whip power2.in vers S2 ; 2.45 à 2.75 expo.out jusqu'à cam(3000, 500, 1.05) ; dérive x +25 u/s, échelle +1 %/s de 2.75 à 4.40 ; 4.40 à 4.56 whip power2.in vers l'état de couture cam(4200, 560, 1.0), flou 0 → 12.
  COUCHES ET PROFONDEUR : avant-plan une boucle de fil floue (flou 11 px) en haut à gauche, coupée par le bord ; sujet le calendrier net ; fond la page JUIN qui s'envole, floue, en haut à droite ; couches animées 3.
  OBJET-PONT ET VECTEUR : le fil qui passe par le 5 entouré file vers la salle du club ; vecteur vers la droite repris par la séquence 2.
  SON : whoosh court 2.30 ; pop 2.62 ; whoosh court 4.40.
  IMAGE CLÉ : 3.95 : styleframes/png/A1.png sans la carte de suivi (elle arrive en séquence 2) : SEPTEMBRE 2026, le 5 entouré « 1er match », le fil noué dessus, sous-titre « [Septembre], premier match... ».

## Frame 2 : Toujours pas de maillots · 4.56 → 9.05

- scene: La caméra arrive dans la salle du club : quatre joueurs stickman s'échauffent en chasubles grises ; « et toujours pas de maillots » ; gag muet : l'entraîneur rafraîchit le suivi de commande sur son téléphone, rien ne bouge, le fil se noue au pied du groupe
- duration: 4.49s
- transition_in: cut
- status: outline
- src: compositions/frames/02-chasubles.html
- voiceover: "...et toujours pas de maillots."
- type: pain_point
- blueprint: spatial-pan-stations (Adapt)
- focal: les joueurs en chasuble, puis la carte de suivi sur le téléphone de l'entraîneur
- rules: svg-path-draw, depth-of-field-blur
- world: dark
- handoff_in: à 0.00 : cam(4200, 560, 1.0) flou 12 px ; caméra en plein whip vers la droite (+6000 u/s en x), dérive 0 ; monde W1, sol d'encre ; fil tracé jusqu'à (4500, 660), couleur thread ; stations posées : fenêtre de message S1 envoyée, calendrier S2 page SEPTEMBRE avec le 5 entouré ; aucun joueur à l'écran ; sous-titre sorti ; grain 5 %
- handoff_out: à 4.49 : cam(7000, 560, 1.0) flou 12 px ; whip vers la droite (+6000 u/s), dérive 0 ; monde W1, sol d'encre ; fil tracé jusqu'à (7000, 620), noué en S3 (nœud serré, tension 1), couleur thread ; stations : S1, S2, S3 (4 joueurs en chasuble grise, entraîneur au téléphone, carte de suivi sur « En cours d'acheminement ») ; carton S4 fermé, hors champ à droite ; sous-titre sorti ; grain 5 %

Word cues: Et@0.18 toujours@0.57 pas@1.02 de@1.24 maillots@1.38

Scene 1 (0.00 à 1.84 s) : P5, la salle, toujours pas de maillots
  TEXTE ÉCRAN : sous-titre « et toujours pas de maillots. » (et 0.18, toujours 0.57, pas 1.02, de 1.24, maillots. 1.38) ; pas de boîte (la phrase a la sienne sur « Septembre ») ; il sort de 1.70 à 1.84.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.14 fin du whip ; 0.14 la salle S3 se pose (×1,1 flou 8 → net, 0,12 s) : parquet sombre, 4 joueurs stickman en chasuble grise (pose 'echauffement', frame.md) répartis en arc ; 0.30 le premier joueur saute sur place (y -30 → 0, 0,2 s, finie) ; 0.50 le deuxième fait un moulinet de bras ; 0.57 « toujours » : l'entraîneur (pose 'telephone') entre par la gauche, trop grand et flou (×1,15 flou 6 → net, 0,14 s expo.out), téléphone à l'oreille puis devant lui ; 1.02 « pas » : les quatre chasubles grises s'éclairent une à une (luminosité +15 %, 0,04 s d'écart) : rien de rouge ; 1.38 « maillots » : le fil traverse le parquet devant eux (fxDrawThread 0,30 → 0,40), seul objet rouge du plan.
  PISTE CAMÉRA : 0.00 à 0.30 expo.out jusqu'à cam(5400, 520, 0.95) ; dérive x +18 u/s, échelle +1 %/s de 0.30 à 1.84.
  COUCHES ET PROFONDEUR : avant-plan l'épaule floue d'un joueur coupée par le bord gauche (flou 14 px) ; sujet les joueurs ; fond le mur sombre avec 2 projecteurs flous ; couches animées 3.
  OBJET-PONT ET VECTEUR : le fil continue au pied du groupe, il va se nouer.
  SON : rien (la voix porte).
  IMAGE CLÉ : 1.45 : quatre stickmen en chasuble grise qui s'échauffent, l'entraîneur à gauche, le fil rouge qui passe à leurs pieds, « et toujours pas de maillots. ».

Scene 2 (1.84 à 4.49 s) : P6 et P7, le gag muet (silence 6.40 à 9.19)
  TEXTE ÉCRAN : aucun texte (silence écrit).
  IMAGE DE DÉPART : la salle, les joueurs, l'entraîneur au centre gauche.
  ÉTAPES : 1.84 poussée vers l'entraîneur ; 2.10 la carte de suivi sort de son téléphone et grandit à côté de lui (×0,2 → 1, 0,18 s expo.out) : « SUIVI DE COMMANDE », « Maillots · Basket Club Eschau », 2 étapes allumées sur 4, « En cours d'acheminement » ; 2.60 il rafraîchit : son pouce tape (×0,9, 0,06 s), la carte tremble (x ±6 px, 0,12 s) ; 2.80 les étapes restent à 2 sur 4 ; 3.10 il rafraîchit encore, même tremblement, rien ne change ; 3.40 un joueur à l'arrière-plan s'arrête et met les mains sur les hanches (pose 'attente') ; 3.60 le fil fait une boucle au pied de l'entraîneur ; 3.84 erreur : la carte flashe d'un liseré gris (0,1 s) ; 3.90 à 4.30 le fil se noue (fxKnotD, tension 0 → 1, 0,4 s power2.in) ; 4.34 départ du whip.
  PISTE CAMÉRA : 1.84 à 2.30 poussée ×0,95 → ×1,25 vers cam(5150, 470) (expo.out) ; dérive échelle +2 %/s de 2.30 à 4.30 ; 4.34 à 4.49 whip power2.in vers cam(7000, 560, 1.0), flou 0 → 12.
  COUCHES ET PROFONDEUR : avant-plan la carte de suivi (nette) ; sujet l'entraîneur ; fond les joueurs flous (flou 4 px) ; couches animées 2 à 3.
  OBJET-PONT ET VECTEUR : le nœud reste posé dans S3 ; le fil repart vers la droite, vers le carton.
  SON : pop 1.38 (le fil) ; tic 2.60 et 3.10 (les rafraîchissements) ; erreur 3.84 ; whoosh court 4.34.
  IMAGE CLÉ : 3.20 : l'entraîneur stickman, téléphone en main, la carte « En cours d'acheminement » bloquée à 2 sur 4, les joueurs en chasuble flous derrière, le fil qui boucle à ses pieds.

## Frame 3 : Le rouge a viré, le numéro se décolle · 9.05 → 15.20

- scene: Le carton arrive enfin : le maillot sort délavé, son rouge a viré à l'orange à côté du nuancier « Rouge club » ; le fil pâlit ; la caméra file jusqu'au hublot de la machine à laver où le numéro 15 se fissure et se décolle, tiré par le fil
- duration: 6.15s
- transition_in: cut
- status: outline
- src: compositions/frames/03-delave.html
- voiceover: "Le jour où ils arrivent, le rouge a viré à l'orange. Et le numéro se décolle au premier lavage."
- type: pain_point
- blueprint: spatial-pan-stations (Adapt)
- focal: le maillot délavé contre le nuancier, puis le coin du 1 qui se soulève derrière la vitre
- rules: svg-path-draw, depth-of-field-blur, motion-blur-streak
- world: dark
- handoff_in: à 0.00 : cam(7000, 560, 1.0) flou 12 px ; whip vers la droite (+6000 u/s), dérive 0 ; monde W1, sol d'encre ; fil tracé jusqu'à (7000, 620), noué en S3 (nœud serré, tension 1), couleur thread ; stations : S1, S2, S3 (4 joueurs en chasuble grise, entraîneur au téléphone, carte de suivi sur « En cours d'acheminement ») ; carton S4 fermé, hors champ à droite ; sous-titre sorti ; grain 5 %
- handoff_out: aucun raccord de caméra (coupe franche voulue à 15.20, changement d'acte, impact grave) ; raccord de position seulement : le bout du fil, thread, au centre du cadre (960, 540), filant vers la droite

Word cues: Le@0.14 jour@0.35 où@0.53 ils@0.67 arrivent@0.91 le@1.51 rouge@1.85 a@2.11 viré@2.47 à@2.75 l'orange@2.89 Et@3.63 le@3.81 numéro@4.05 se@4.33 décolle@4.69 au@4.99 premier@5.27 lavage@5.55

Scene 1 (0.00 à 3.30 s) : P8 et P9, le carton, le rouge a viré
  TEXTE ÉCRAN : sous-titre « Le jour où ils arrivent, le rouge a viré à [boîte : l'orange]. » en deux morceaux : « Le jour où ils arrivent, » (0.14 à 0.91) puis « le rouge a viré à l'orange. » (le 1.51, rouge 1.85, a 2.11, viré 2.47, à 2.75, boîte tracée 2.85, l'orange. 2.89) ; il sort de 3.16 à 3.30.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.14 fin du whip ; 0.14 le carton S4 TOMBE du haut du cadre (y -600 → 0, 0,26 s power2.in) ; 0.40 contact, tassement 0,97 → 1 en 0,08 s ; 0.67 les rabats s'ouvrent (rotation 0 → 110°, 0,16 s, l'un après l'autre à 0,05 s) ; 0.91 « arrivent » : le maillot plié sort du carton (y +80 → 0, ×1,1 flou 6 → net, 0,14 s), en couleurs délavées (saturate .55, hue-rotate +14°, l'orange de thread-faded) ; 1.51 le nuancier « Rouge club » arrive depuis la caméra (×4 flou 12 → net, 0,22 s expo.out) et se pose à droite du maillot, pastille thread ; 1.85 « rouge » : la pastille du nuancier s'allume (luminosité +20 %, 0,1 s) ; 2.20 la caméra pousse entre les deux rouges ; 2.47 « viré » : le fil qui passe derrière le carton pâlit de thread vers thread-faded sur toute sa longueur visible (couleur, 0,4 s) ; 2.89 « l'orange » : un liseré orange se trace autour du maillot (0,2 s) ; 3.16 départ du whip.
  PISTE CAMÉRA : 0.00 à 0.30 expo.out jusqu'à cam(7800, 480, 1.1) ; dérive x +15 u/s ; 2.20 à 2.60 poussée ×1,1 → ×1,3 vers cam(7860, 470) (expo.out) ; 3.16 à 3.30 whip power2.in vers S5, flou 0 → 12.
  COUCHES ET PROFONDEUR : avant-plan un rabat du carton flou coupé par le bord bas gauche (au-dessus de y 860) ; sujet le maillot délavé et le nuancier côte à côte, marges égales ; fond le sol d'encre ; couches animées 3.
  OBJET-PONT ET VECTEUR : le fil pâli passe du carton au hublot ; vecteur vers la droite.
  SON : impact sourd 9.45 (le carton touche) ; pop 10.56 (le nuancier) ; whoosh court 12.21.
  IMAGE CLÉ : 2.95 : le maillot plié délavé (orange) à gauche, le nuancier « Rouge club » rouge vif à droite, le fil pâle entre les deux, « le rouge a viré à [l'orange]. ».

Scene 2 (3.30 à 6.15 s) : P10 et P11, le hublot, le numéro se décolle
  TEXTE ÉCRAN : sous-titre « Et le numéro se [boîte : décolle] au premier lavage. » (Et 3.63, le 3.81, numéro 4.05, se 4.33, boîte tracée 4.65, décolle 4.69, au 4.99, premier 5.27, lavage. 5.55) ; il sort de 5.98 à 6.12.
  IMAGE DE DÉPART : sommet du whip, le hublot S5 qui arrive flou par la droite.
  ÉTAPES : 3.30 à 3.45 sommet du whip ; 3.45 le hublot se pose (×1,1 flou 8 → net, 0,14 s) : anneau chromé, vitre, le dos du maillot (maillot-dos-detoure.png, numéro 15 en très gros plan) qui tourne avec le tambour (rotation +14°, puis +3°/s) ; 3.80 des gouttes perlent sur la vitre (3 disques, 0,05 s d'écart) ; 4.05 « numéro » : la mousse monte en bas de la vitre (y +60 → 0, 0,3 s) ; 4.33 le fil pâle entre dans le cadre et s'accroche au coin du 1 ; 4.69 « décolle » : le fil tire, le coin du 1 se soulève en rabat avec son ombre (rotation 0 → -24°, 0,18 s power2.out) ; 4.99 trois fissures se tracent dans le 5 (0,05 s d'écart) ; 5.27 le rabat claque (petite secousse de 4 px) ; 5.55 « lavage » : le tambour accélère (rotation +40°/s, flou de rotation 2 px) ; 5.80 le fil se tend vers la droite, sa tête au centre du cadre (960, 540) ; 6.15 coupe.
  PISTE CAMÉRA : 3.30 à 3.60 expo.out jusqu'à cam(10000, 470, 1.25) ; 3.60 à 6.15 poussée linéaire dans le hublot ×1,25 → ×1,45 (riser visuel) ; secousse 4 px à 5.27 (0,1 s).
  COUCHES ET PROFONDEUR : avant-plan l'anneau chromé flou (flou 16 px) en haut à gauche ; sujet le 15 derrière la vitre ; fond le tambour sombre ; reflet de la vitre ; couches animées 3 à 4.
  OBJET-PONT ET VECTEUR : la tête du fil, au centre du cadre, survit à la coupe franche (raccord de position).
  SON : montée de 12.20 à 15.20 ; clac 14.32 (le rabat).
  IMAGE CLÉ : 4.80 : la matière de styleframes/png/C1.png (hublot, 15 en très gros plan, coin du 1 soulevé, fissures) avec le fil pâle accroché au coin du 1, « Et le numéro se [décolle] au premier lavage. ».

## Frame 4 : On reprend depuis le début · 15.20 → 18.70

- scene: Coupe au noir sur l'impact ; le bout du fil est seul au centre ; l'aiguille du logo IFS traverse le noir et se renfile sur le fil, qui redevient rouge vif ; « On reprend depuis le début. » s'écrit au centre ; l'aiguille sort, sa pointe devient un point de lumière
- duration: 3.50s
- transition_in: cut
- status: outline
- src: compositions/frames/04-pivot.html
- voiceover: "On reprend depuis le début."
- type: pivot
- blueprint: kinetic-type-beats (Adapt)
- focal: l'aiguille et le fil, puis la phrase
- rules: svg-path-draw, kinetic-beat-slam
- world: dark
- handoff_in: aucun raccord de caméra (coupe franche voulue à 15.20, changement d'acte, impact grave) ; raccord de position seulement : le bout du fil, thread, au centre du cadre (960, 540), filant vers la droite
- handoff_out: à 3.50 : cam(960, 540, 1.0) flou 0 ; pas de monde : un point de lumière blanc chaud (radial #fff → #FF7DBA → transparent, 60 px) au centre du cadre, au bout du fil qui sort du chas de l'aiguille ; l'aiguille (520 px) sortie par le bord droit du cadre ; le fil thread traverse le cadre du bord gauche jusqu'au point ; noir #110C15 ; aucune phrase ; grain 5 %

Word cues: On@0.23 reprend@0.46 depuis@0.84 le@1.14 début@1.34

Scene 1 (0.00 à 1.80 s) : P12, la phrase sur le noir
  TEXTE ÉCRAN : moment typographique centré, 84 px Archivo, encre ink : « On reprend depuis le [trait : début]. » (On 0.23, reprend 0.46, depuis 0.84, le 1.14, début. 1.34 ; trait 1.34 à 1.74) ; pas de sous-titre en bas.
  IMAGE DE DÉPART : noir #110C15, le bout du fil (pâle, thread-faded) au centre, immobile une image.
  ÉTAPES : 0.00 impact : le noir tombe ; 0.05 le bout du fil glisse de 40 px vers la gauche (power2.out) ; 0.23 « On » : les mots s'écrivent au-dessus du fil, lettres qui convergent (0,5 s expo.out, flou 12 → 0) ; 0.46 « reprend » : le fil redevient rouge vif (thread-faded → thread, de la tête vers la queue, 0,5 s) ; 0.84 « depuis » ; 1.14 l'aiguille du logo (fxNeedle(520)) entre par la gauche, trop grande et floue (×1,6 flou 10 → net, 0,2 s expo.out), pointe vers la droite ; 1.34 « début » : le fil passe dans son chas (le bout du fil glisse dans l'ellipse noire du chas, 0,1 s) ; 1.34 à 1.74 trait accent-glow sous « début ».
  PISTE CAMÉRA : dérive échelle +1,5 %/s de 0.00 à 1.80 (aucun cran : le noir respire).
  COUCHES ET PROFONDEUR : la phrase (devant), l'aiguille et le fil (milieu), le noir et son grain ; couches animées 2.
  OBJET-PONT ET VECTEUR : l'aiguille renfilée va traverser le cadre.
  SON : impact grave 15.20 (porté par la musique).
  IMAGE CLÉ : 1.50 : noir, « On reprend depuis le début. » centrée avec son trait sous « début », l'aiguille IFS nette qui vient d'enfiler le fil rouge.

Scene 2 (1.80 à 3.50 s) : P13, l'aiguille traverse (silence 16.87 à 18.84)
  TEXTE ÉCRAN : la phrase sort de 1.80 à 1.94 (opacité 1 → 0, flou 0 → 6) ; aucun autre texte.
  IMAGE DE DÉPART : la phrase, l'aiguille enfilée à gauche.
  ÉTAPES : 1.80 la phrase sort ; 1.94 l'aiguille traverse le cadre de gauche à droite (x 420 → 2300, 1,2 s power3.inOut), le fil rouge se dessine derrière elle (fxDrawThread sur un trait droit qui ondule de ±20 px) ; 2.50 le fil ondule (vague qui court de gauche à droite, 0,4 s) ; 3.14 l'aiguille sort par le bord droit ; 3.20 la tête du fil s'arrête au centre et s'allume : point de lumière (×0 → 1, 0,14 s expo.out, glow accent-glow) ; 3.36 le point gonfle (×1 → 1,4, 0,14 s).
  PISTE CAMÉRA : dérive x +12 u/s de 1.80 à 3.20 ; 3.20 à 3.50 cran ×1 → ×1,06 vers le point (expo.out) puis retour à cam(960, 540, 1.0) à 3.50.
  COUCHES ET PROFONDEUR : le fil et l'aiguille (sujet), le noir ; couches animées 2.
  OBJET-PONT ET VECTEUR : le point de lumière s'ouvre sur l'atelier (éclair de lumière d'assemble.sh à 18.70).
  SON : scintillement 18.40.
  IMAGE CLÉ : 2.60 : le noir traversé par l'aiguille IFS qui file à droite, le fil rouge ondulant derrière elle.

## Frame 5 : Avec IFS, tout part d'un mail · 18.70 → 24.00

- scene: Le point de lumière s'ouvre sur le papier de l'atelier ; le fil trace une enveloppe et la même fenêtre de message qu'en juin, adressée cette fois à IFS, part ; la caméra file au vrai studio IFS où le maillot Eschau se construit et où l'écusson du club arrive depuis la caméra et se pose sur la poitrine
- duration: 5.30s
- transition_in: cut
- status: outline
- src: compositions/frames/05-mail-ifs.html
- voiceover: "Avec IFS, tout part d'un mail. Vous envoyez votre design et votre logo."
- type: demo
- blueprint: spatial-pan-stations (Adapt)
- focal: l'enveloppe et la fenêtre de message vers IFS, puis le maillot dans le studio et l'écusson
- rules: svg-path-draw, cursor-click-ripple
- world: light
- handoff_in: à 0.00 : cam(960, 540, 1.0) flou 0 ; pas de monde : un point de lumière blanc chaud (radial #fff → #FF7DBA → transparent, 60 px) au centre du cadre, au bout du fil qui sort du chas de l'aiguille ; l'aiguille (520 px) sortie par le bord droit du cadre ; le fil thread traverse le cadre du bord gauche jusqu'au point ; noir #110C15 ; aucune phrase ; grain 5 %
- handoff_out: à 5.30 : cam(4300, 480, 1.0) flou 12 px ; whip vers la droite (+6000 u/s), dérive 0 ; monde W2, sol papier ; fil tracé jusqu'à (4600, 640) ; stations : S6 (enveloppe tracée, fenêtre de message « À : IFS » envoyée), S7 (studio IFS, écusson posé sur la poitrine du maillot) ; BAT S8 pas encore entré ; sous-titre sorti ; grain 3 %

Word cues: Avec@0.14 IFS@0.84 tout@1.41 part@1.60 d'un@1.84 mail@2.16 Vous@2.76 envoyez@3.04 votre@3.38 design@3.66 et@4.14 votre@4.42 logo@4.70

Scene 1 (0.00 à 2.50 s) : P14 et P15, l'atelier s'allume, le mail part vers IFS
  TEXTE ÉCRAN : sous-titre « Avec IFS, tout part d'un [boîte : mail]. » (Avec 0.14, IFS, 0.84, tout 1.41, part 1.60, d'un 1.84, boîte tracée 2.12, mail. 2.16) ; il sort de 2.36 à 2.50.
  IMAGE DE DÉPART : handoff_in ; l'éclair de lumière (assemble.sh) blanchit le cadre de 0.00 à 0.20.
  ÉTAPES : 0.00 le point s'ouvre en disque blanc qui remplit le cadre (0,2 s expo.out) : sol papier W2 ; 0.20 le fil, rouge vif sur le blanc, part du bord gauche ; 0.30 à 1.00 il trace une enveloppe (rectangle 520 × 340 et son rabat en V, fxDrawThread sur le contour, expo.out) centrée en S6 ; 0.84 « IFS » ; 1.00 la fenêtre de message (même gabarit qu'en séquence 1) sort de l'enveloppe (×0,6 → 1, flou 6 → net, 0,16 s) : « À : IFS », « Objet : Commande maillots · saison 2026 », pièce jointe « Commande maillots 2026.xlsx », corps « Bonjour, voici notre commande de maillots pour la saison. » ; 1.41 « tout » : le curseur arrive en courbe sur Envoyer (0,45 s power3.out) ; 2.10 il clique (onde bleue) ; 2.16 « mail » : la fenêtre se replie dans l'enveloppe, le rabat se ferme (0,12 s), l'enveloppe file vers la droite sur le fil ; 2.36 départ du whip.
  PISTE CAMÉRA : dérive x +20 u/s, échelle -1 %/s de 0.20 à 2.36 ; 2.36 à 2.50 whip power2.in vers S7, flou 0 → 12.
  COUCHES ET PROFONDEUR : avant-plan une boucle de fil floue en haut à droite ; sujet l'enveloppe et la fenêtre ; fond le papier rayé ; couches animées 2 à 3.
  OBJET-PONT ET VECTEUR : l'enveloppe file sur le fil et arrive dans le studio comme pièce jointe ; vecteur vers la droite.
  SON : scintillement et whoosh cinématique 18.70 ; clic 20.80 ; whoosh court 21.06.
  IMAGE CLÉ : 2.05 : sur le papier, l'enveloppe tracée par le fil rouge, la fenêtre « À : IFS » au-dessus, le curseur sur Envoyer.

Scene 2 (2.50 à 5.30 s) : P16 et P17, le studio IFS, le design et le logo
  TEXTE ÉCRAN : sous-titre « Vous envoyez votre [boîte : design] et votre logo. » (Vous 2.76, envoyez 3.04, votre 3.38, boîte tracée 3.62, design 3.66, et 4.14, votre 4.42, logo. 4.70) ; il sort de 5.02 à 5.16.
  IMAGE DE DÉPART : sommet du whip, le studio S7 qui arrive flou par la droite.
  ÉTAPES : 2.50 à 2.65 sommet du whip ; 2.65 le studio se pose (×1,1 flou 8 → net, 0,14 s) : en-tête IFS, sélecteur « Maillot basketball double face (réversible) », canevas, onglets ; 2.76 l'enveloppe se pose dans la zone « Déposez votre logo ici » et devient la ligne « logo-club.png » ; 3.04 « envoyez » : le maillot Eschau (maillot-face-rouge-noir-detoure.png) se construit dans le canevas : fond rouge puis empiècement noir puis motif (3 étapes, 0,12 s d'écart, chacune ×1,04 → 1) ; 3.66 « design » : le fil contourne le maillot (fxDrawThread sur la silhouette, 0,5 s expo.out) ; 4.14 l'onglet « Logos » s'active (soulignement accent, 0,1 s) ; 4.40 l'écusson du club arrive depuis la caméra, trop grand et flou (×4 flou 12 → net, 0,22 s expo.out) ; 4.70 « logo » : il se pose sur la poitrine (contact, tassement 0,96 → 1, 0,08 s), cadre pointillé accent autour ; 5.16 départ du whip.
  PISTE CAMÉRA : 2.50 à 2.80 expo.out jusqu'à cam(3200, 470, 0.95) ; 3.70 à 4.60 poussée ×0,95 → ×1,15 vers la poitrine du maillot (power3.out) ; 5.16 à 5.30 whip power2.in vers l'état de couture cam(4300, 480, 1.0), flou 0 → 12.
  COUCHES ET PROFONDEUR : avant-plan l'écusson en vol (grand, flou) puis un second écusson flou coupé par le bord bas gauche (au-dessus de y 860) ; sujet le maillot dans le canevas ; fond la fenêtre du studio et le papier ; couches animées 3.
  OBJET-PONT ET VECTEUR : le fil quitte le contour du maillot et file vers le BAT ; vecteur vers la droite.
  SON : pop 23.40 (l'écusson se pose) ; whoosh court 23.85.
  IMAGE CLÉ : 4.55 : le vrai studio IFS, le maillot Eschau dans le canevas contourné par le fil rouge, l'écusson du club qui arrive flou vers la poitrine, « Vous envoyez votre [design] et votre logo. ».

## Frame 6 : BAT, le reste, les tailles, la coupe · 24.00 → 29.80

- scene: Le design s'imprime en BAT ; le fil trace une coche qui devient le tampon VALIDÉ ; « Nous faisons le reste » ; la caméra file au tapis de coupe : la grille de tailles IFS, les patrons gradés, le cutter rotatif suit la ligne du fil sur le patron M
- duration: 5.80s
- transition_in: cut
- status: outline
- src: compositions/frames/06-bat-coupe.html
- voiceover: "Vous validez le BAT. Nous faisons le reste. Nos tailles sont standardisées. La coupe va plus vite."
- type: demo
- blueprint: spatial-pan-stations (Adapt)
- focal: le BAT et son tampon, puis la grille de tailles et le cutter
- rules: svg-path-draw, kinetic-beat-slam, depth-of-field-blur
- world: light
- handoff_in: à 0.00 : cam(4300, 480, 1.0) flou 12 px ; whip vers la droite (+6000 u/s), dérive 0 ; monde W2, sol papier ; fil tracé jusqu'à (4600, 640) ; stations : S6 (enveloppe tracée, fenêtre de message « À : IFS » envoyée), S7 (studio IFS, écusson posé sur la poitrine du maillot) ; BAT S8 pas encore entré ; sous-titre sorti ; grain 3 %
- handoff_out: à 5.80 : cam(8400, 640, 3.2) flou 10 px ; plongée en cours dans la ligne de coupe du patron M (échelle ×1,0 → ×3,2, expo.in), dérive 0 ; monde W2 ; fil tracé jusqu'à (8800, 640) ; tapis de coupe S9 avec le patron M découpé, cutter sorti du cadre ; sous-titre sorti ; grain 3 %

Word cues: Vous@0.01 validez@0.28 le@0.64 BAT@0.92 Nous@1.59 faisons@1.82 le@2.10 reste@2.30 Nos@2.87 tailles@3.14 sont@3.40 standardisées@3.68 La@4.64 coupe@4.90 va@5.06 plus@5.26 vite@5.50

Scene 1 (0.00 à 2.70 s) : P18 et P19, le BAT validé, nous faisons le reste
  TEXTE ÉCRAN : sous-titre « Vous validez le [boîte : BAT]. » (Vous 0.01, validez 0.28, le 0.64, boîte tracée 0.88, BAT. 0.92) puis « Nous faisons [boîte : le reste]. » (Nous 1.59, faisons 1.82, boîte tracée 2.06, le 2.10, reste. 2.30) ; il sort de 2.56 à 2.70.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.14 fin du whip ; 0.14 la feuille BAT (frame.md bat-sheet) se pose (×1,1 flou 8 → net, 0,12 s) : « BAT », les vues face et dos du maillot, « Basket Club Eschau · saison 2026 » ; 0.28 « validez » : le curseur arrive en courbe sous la feuille (0,4 s power3.out) ; 0.70 à 0.92 le fil trace une coche en bas à droite de la feuille (fxDrawThread, 0,2 s expo.out) ; 0.92 « BAT » : la coche devient le tampon carré accent « VALIDÉ » qui frappe (×1,6 flou 8 → net en 0,08 s, rotation -8°), secousse de la feuille 4 px ; 1.30 le curseur sort par le bas ; 1.59 « Nous » : la feuille BAT recule et glisse vers la gauche (×1 → 0,8, x -300, 0,4 s power3.out), elle reste dans le champ ; 1.82 le fil repart du tampon vers la droite (fxDrawThread) ; 2.30 « reste » : la tête du fil tire vers le bord droit ; 2.56 départ du whip.
  PISTE CAMÉRA : 0.00 à 0.30 expo.out jusqu'à cam(5400, 470, 1.05) ; secousse 4 px à 0.92 ; dérive x +25 u/s de 0.30 à 2.56 ; 2.56 à 2.70 whip power2.in vers S9, flou 0 → 12.
  COUCHES ET PROFONDEUR : avant-plan l'ombre floue du tampon en vol ; sujet la feuille BAT ; fond le papier rayé ; couches animées 2 à 3.
  OBJET-PONT ET VECTEUR : la coche devient le tampon ; le fil sort du tampon et file vers le tapis de coupe.
  SON : impact sec 24.92 (le tampon) ; whoosh court 26.56.
  IMAGE CLÉ : 0.98 : la feuille BAT nette avec les deux vues du maillot Eschau, le tampon VALIDÉ qui vient de frapper sur la coche du fil, « Vous validez le [BAT]. ».

Scene 2 (2.70 à 5.80 s) : P20 et P21, la grille de tailles, la coupe
  TEXTE ÉCRAN : sous-titre « Nos tailles sont [boîte : standardisées]. » (Nos 2.87, tailles 3.14, sont 3.40, boîte tracée 3.64, standardisées. 3.68) puis « La coupe va [boîte : plus vite]. » (La 4.64, coupe 4.90, va 5.06, boîte tracée 5.22, plus 5.26, vite. 5.50) ; il sort de 5.62 à 5.76.
  IMAGE DE DÉPART : sommet du whip, le tapis de coupe S9 qui arrive flou par la droite.
  ÉTAPES : 2.70 à 2.85 sommet du whip ; 2.85 le tapis de coupe et le tissu blanc se posent (×1,1 flou 8 → net, 0,12 s) ; 2.87 « Nos » : la carte « GRILLE IFS / Tailles standardisées » arrive depuis la caméra à droite (×3 flou 10 → net, 0,2 s expo.out) ; 3.14 « tailles » : ses 6 pastilles XS S M L XL 2XL s'impriment (0,04 s d'écart) ; 3.40 la pastille M passe en accent ; 3.68 « standardisées » : les patrons gradés se tracent sur le tissu, du plus grand au plus petit (pointillé #C8BCC5, 0,06 s d'écart), le M en trait accent ; 4.20 le fil rejoint le départ du patron M ; 4.64 « La » : le cutter rotatif arrive en courbe (comme un curseur, 0,4 s power3.out) et se pose sur le départ ; 4.90 « coupe » : la lame suit la ligne du fil sur le contour du M (0,6 s, power2.inOut), traînée magenta floue ; 5.26 « plus » : la pièce découpée se soulève de 6 px (ombre) ; 5.50 « vite » : le cutter file hors du cadre en haut à droite (0,12 s power2.in) ; 5.55 départ de la plongée dans la ligne de coupe.
  PISTE CAMÉRA : 2.70 à 3.00 expo.out jusqu'à cam(7600, 470, 1.0) ; dérive x +20 u/s de 3.00 à 4.60 ; 4.90 à 5.40 la caméra suit la lame (x +200 u en 0,5 s, power2.inOut) ; 5.55 à 5.80 plongée vers cam(8400, 640, 3.2) (expo.in), flou 0 → 10.
  COUCHES ET PROFONDEUR : avant-plan la règle jaune floue coupée par le bord haut gauche ; sujet le patron M et le cutter ; fond le tapis quadrillé et la carte de tailles ; couches animées 3.
  OBJET-PONT ET VECTEUR : la ligne de coupe devient, au fond de la plongée, la maille du tissu sous la presse.
  SON : clic doux 29.06 (la lame) ; whoosh 29.55.
  IMAGE CLÉ : 4.95 : styleframes/png/B2.png adaptée au fil : le tapis de coupe, les patrons gradés, le M tracé en accent suivi par la ligne du fil rouge, le cutter magenta en mouvement, la carte « GRILLE IFS » à droite.

## Frame 7 : La sublimation fixe les couleurs · 29.80 → 32.80

- scene: Au fond de la plongée, la maille blanche du tissu en macro ; la presse descend ; le fil plonge dans la fibre et la couleur du vrai maillot Eschau s'y répand en halo
- duration: 3.00s
- transition_in: cut
- status: outline
- src: compositions/frames/07-sublimation.html
- voiceover: "La sublimation fixe les couleurs dans la fibre."
- type: demo
- blueprint: zoom-out-workspace-reveal (Adapt)
- focal: le point où le fil plonge dans la maille, puis le motif qui apparaît
- rules: svg-path-draw, depth-of-field-blur
- world: light
- handoff_in: à 0.00 : cam(8400, 640, 3.2) flou 10 px ; plongée en cours dans la ligne de coupe du patron M (échelle ×1,0 → ×3,2, expo.in), dérive 0 ; monde W2 ; fil tracé jusqu'à (8800, 640) ; tapis de coupe S9 avec le patron M découpé, cutter sorti du cadre ; sous-titre sorti ; grain 3 %
- handoff_out: à 3.00 : cam(10900, 520, 1.3) flou 12 px ; whip vers la droite (+6000 u/s), dérive 0 ; monde W2 ; fil tracé jusqu'à (10600, 600), ressorti du tissu ; S10 : la maille avec le motif rouge et noir du maillot apparu, presse relevée hors champ ; sous-titre sorti ; grain 3 %

Word cues: La@0.24 sublimation@0.52 fixe@1.14 les@1.58 couleurs@1.82 dans@2.10 la@2.30 fibre@2.54

Scene 1 (0.00 à 3.00 s) : P22 et P23, la presse, la couleur dans la fibre
  TEXTE ÉCRAN : sous-titre en deux morceaux : « La sublimation fixe » (La 0.24, sublimation 0.52, fixe 1.14) puis « les [boîte : couleurs] dans la fibre. » (les 1.58, boîte tracée 1.78, couleurs 1.82, dans 2.10, la 2.30, fibre. 2.54) ; il sort de 2.84 à 2.98.
  IMAGE DE DÉPART : handoff_in ; sous le flou de 0.00 à 0.15, la ligne de coupe devient la maille blanche en macro (S10).
  ÉTAPES : 0.00 à 0.15 fin de la plongée, la maille se pose (points de 22 px) ; 0.24 « La » : la plaque de presse descend du haut du cadre, floue (y -260 → -150, 0,2 s power2.in), lueur chaude sous elle ; 0.44 contact : légère secousse 3 px ; 0.52 « sublimation » : le fil arrive de la gauche et plonge dans le tissu au point (860, 470) du cadre ; 0.70 à 2.40 depuis ce point, le motif réel du maillot (maillot-face-rouge-noir-detoure.png) apparaît dans la fibre en halo qui s'étend (masque radial 0 → 46 %, power2.out), la maille reste visible à travers l'encre ; 1.14 « fixe » : le halo marque un temps (tassement), la presse se relève de 20 px ; 1.82 « couleurs » : le halo atteint « ESCHAU » ; 2.54 « fibre » : le fil ressort du tissu à droite (fxDrawThread) ; 2.84 départ du whip.
  PISTE CAMÉRA : 0.00 à 0.20 expo.out jusqu'à cam(9800, 470, 1.4) ; 0.20 à 2.80 recul lent ×1,4 → ×1,3 (zoom arrière qui révèle le motif) ; 2.84 à 3.00 whip power2.in vers l'état de couture cam(10900, 520, 1.3), flou 0 → 12.
  COUCHES ET PROFONDEUR : avant-plan la plaque de presse floue (13 px) coupée par le bord haut ; sujet le point d'entrée du fil et le halo de couleur ; fond la maille blanche ; voile blanc sous y 760 pour garder la bande du sous-titre claire ; couches animées 3.
  OBJET-PONT ET VECTEUR : le fil qui ressort du tissu file vers la couture.
  SON : souffle chaud 30.04 (la presse) ; whoosh court 32.64.
  IMAGE CLÉ : 1.85 : styleframes/png/A2.png : la maille blanche, le fil qui plonge, le motif ESCHAU rouge et noir qui apparaît dans la fibre, la presse floue en haut, « les [couleurs] dans la fibre. ».

## Frame 8 : Confection, livraison · 32.80 → 37.45

- scene: L'aiguille du logo pique et le fil devient la couture qui ferme l'emmanchure du maillot ; le maillot fini se plie dans un carton IFS, le fil en fait la ficelle ; étiquette « Livré · moins d'un mois »
- duration: 4.65s
- transition_in: cut
- status: outline
- src: compositions/frames/08-couture-livraison.html
- voiceover: "La confection assemble chaque maillot. Et vous êtes livrés en moins d'un mois."
- type: payoff
- blueprint: spatial-pan-stations (Adapt)
- focal: l'aiguille et la couture, puis le carton fermé et son étiquette
- rules: svg-path-draw, depth-of-field-blur
- world: light
- handoff_in: à 0.00 : cam(10900, 520, 1.3) flou 12 px ; whip vers la droite (+6000 u/s), dérive 0 ; monde W2 ; fil tracé jusqu'à (10600, 600), ressorti du tissu ; S10 : la maille avec le motif rouge et noir du maillot apparu, presse relevée hors champ ; sous-titre sorti ; grain 3 %
- handoff_out: aucun raccord de caméra (coupe franche voulue à 37.45, changement d'acte : le jour du match, au sommet du flou d'un whip vers la droite) ; raccord de position seulement : le fil thread entre par le bord gauche du cadre à mi-hauteur

Word cues: La@0.08 confection@0.38 assemble@0.90 chaque@1.50 maillot@1.88 Et@2.53 vous@2.68 êtes@2.82 livrés@3.04 en@3.44 moins@3.80 d'un@3.96 mois@4.26

Scene 1 (0.00 à 2.40 s) : P24, la couture
  TEXTE ÉCRAN : sous-titre « La confection assemble [boîte : chaque maillot]. » (La 0.08, confection 0.38, assemble 0.90, boîte tracée 1.46, chaque 1.50, maillot. 1.88) ; il sort de 2.26 à 2.40.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.15 fin du whip ; 0.15 le maillot à plat (vue face, maillot-face-rouge-noir-detoure.png, emmanchure droite ouverte) se pose (×1,1 flou 8 → net, 0,12 s) ; 0.20 l'aiguille du logo (fxNeedle(150)) entre en haut, trop grande et floue (×3 flou 10 → net, 0,2 s), en avance sur « confection » (0.38) ; 0.50, 1.00, 1.50 elle pique trois fois le long de l'emmanchure (descente de 30 px en 0,06 s, remontée 0,1 s) et à chaque piqûre le fil dessine un point de couture (trait de 14 px) ; 0.90 « assemble » : les deux bords de l'emmanchure se rapprochent (x ±12 → 0, 0,3 s) ; 1.88 « maillot » : le maillot se plie en deux puis en quatre (scaleY 1 → 0,5 → 0,25, 0,12 s chaque, power2.in) et devient le maillot plié (maillot-plie-detoure.png) ; 2.26 départ du whip.
  PISTE CAMÉRA : 0.00 à 0.30 expo.out jusqu'à cam(12000, 470, 1.2) ; dérive suit l'aiguille (x +30 u/s) ; 2.26 à 2.40 whip power2.in vers S12, flou 0 → 12.
  COUCHES ET PROFONDEUR : avant-plan la pointe de l'aiguille floue à chaque montée ; sujet l'emmanchure et ses points ; fond le papier ; couches animées 3.
  OBJET-PONT ET VECTEUR : le maillot plié glisse sur le fil jusqu'au carton.
  SON : pops doux 33.30, 33.80, 34.30 (les points) ; whoosh court 35.06.
  IMAGE CLÉ : 1.05 : l'emmanchure du maillot Eschau en gros plan, l'aiguille IFS qui pique, trois points de couture rouges, « La confection assemble [chaque maillot]. ».

Scene 2 (2.40 à 4.65 s) : P25, le carton, livré en moins d'un mois
  TEXTE ÉCRAN : sous-titre « Et vous êtes [boîte : livrés] en [trait : moins d'un mois]. » (Et 2.53, vous 2.68, êtes 2.82, boîte tracée 3.00, livrés 3.04, en 3.44, moins 3.80, d'un 3.96, mois. 4.26 ; trait 3.80 à 4.20) ; il sort de 4.42 à 4.56.
  IMAGE DE DÉPART : sommet du whip, le carton kraft S12 qui arrive par la droite.
  ÉTAPES : 2.40 à 2.55 sommet du whip ; 2.55 le carton ouvert se pose (×1,1 flou 8 → net), papier de soie ; 2.68 le maillot plié tombe dedans (y -300 → 0, 0,2 s power2.in, tassement) ; 3.04 « livrés » : les rabats se ferment (0,1 s chacun, 0,04 s d'écart) ; 3.20 le fil fait la ficelle : il entoure le carton en croix (fxDrawThread, 0,3 s) et noue une boucle ; 3.44 l'étiquette « Livré · moins d'un mois » arrive depuis la caméra et se colle (×3 flou 10 → net, 0,2 s, rotation 6°) ; 3.80 « moins » : notification à deux tons, le carton fait un petit saut de 8 px ; 4.26 « mois » : le carton glisse vers la droite sur le fil (x +400, 0,3 s power2.in) ; 4.50 départ du whip ; coupe franche à 4.65 au sommet du flou.
  PISTE CAMÉRA : 2.40 à 2.70 expo.out jusqu'à cam(14200, 470, 1.0) ; dérive x +20 u/s ; 4.50 à 4.65 whip power2.in vers la droite, flou 0 → 14.
  COUCHES ET PROFONDEUR : avant-plan un pan de papier de soie flou coupé par le bord haut gauche ; sujet le carton et l'étiquette ; fond le papier rayé ; couches animées 3.
  OBJET-PONT ET VECTEUR : le fil-ficelle file hors du cadre vers la droite et entre dans la salle par le bord gauche (raccord de position).
  SON : NOTIFICATION À DEUX TONS 35.84 (la signature) ; whoosh court 37.30.
  IMAGE CLÉ : 3.95 : styleframes/png/B3.png sans le bloc de marque : le carton kraft fermé par la ficelle rouge, le maillot plié visible par le rabat, l'étiquette « Livré · moins d'un mois », « Et vous êtes [livrés] en moins d'un mois. » avec son trait.

## Frame 9 : Samedi, le numéro 15 · 37.45 → 42.20

- scene: Samedi, dans la salle de nuit : le joueur stickman n° 15, maillot Eschau dessiné, s'élance et smashe ; le fil devient le brin rouge du filet ; il reste suspendu au cercle et la caméra pousse sur son dos : le nuancier « Rouge club » se pose contre le tissu, même rouge ; le brin rouge quitte le filet et file vers le haut
- duration: 4.75s
- transition_in: cut
- status: outline
- src: compositions/frames/09-match.html
- voiceover: "Samedi, le numéro quinze monte au panier. Le rouge est resté rouge."
- type: payoff
- blueprint: camera-journey (Adapt)
- focal: le joueur qui smashe, puis le nuancier contre le maillot
- rules: svg-path-draw, motion-blur-streak, depth-of-field-blur
- world: dark
- handoff_in: aucun raccord de caméra (coupe franche voulue à 37.45, changement d'acte : le jour du match, au sommet du flou d'un whip vers la droite) ; raccord de position seulement : le fil thread entre par le bord gauche du cadre à mi-hauteur
- handoff_out: à 4.75 : cam(1480, 120, 1.15) flou 10 px ; tilt vers le haut en cours (-2400 u/s en y), dérive 0 ; salle W3 : panier en haut du cadre, le brin rouge du filet détaché qui file vers le haut à gauche ; joueur n° 15 suspendu au cercle, son dos hors champ bas ; nuancier posé contre le dos du maillot ; sous-titre sorti ; grain 5 %

Word cues: Samedi@0.08 le@0.85 numéro@1.01 15@1.31 monte@1.61 au@1.95 panier@2.13 Le@2.70 rouge@3.03 est@3.31 resté@3.69 rouge@3.97

Scene 1 (0.00 à 2.60 s) : P26 et P27, le smash
  TEXTE ÉCRAN : sous-titre « Samedi, le numéro [boîte : 15] monte au panier. » (Samedi, 0.08, le 0.85, numéro 1.01, boîte tracée 1.27, 15 1.31, monte 1.61, au 1.95, panier. 2.13) ; il sort de 2.46 à 2.60.
  IMAGE DE DÉPART : la salle de nuit (ground-gym) au sommet d'un flou de whip qui retombe, le fil rouge qui entre par le bord gauche à mi-hauteur.
  ÉTAPES : 0.00 à 0.12 le flou retombe (14 → 0 px) ; 0.08 « Samedi » : les projecteurs s'allument un à un (0,05 s d'écart) ; 0.20 le joueur stickman n° 15 (frame.md stickman, maillot et short dessinés, vue de dos) court de la gauche vers le panier (x 400 → 900, 0,6 s, pose de course) ; le fil court au sol derrière lui ; 0.85 il s'élance (impulsion, traînées verticales sous les pieds) ; 1.01 « numéro » : la caméra passe sur son dos, le 15 net ; 1.31 « 15 » : il est en l'air, bras droit tendu, ballon en main (pose 'smash' de styleframes/png/A3.png) ; 1.61 « monte » : il monte jusqu'au cercle (y -120, 0,3 s power2.out) ; 1.80 à 2.20 le fil remonte le long du poteau et se tisse dans le filet blanc : il devient le brin rouge (fxDrawThread, expo.out) ; 2.13 « panier » : SMASH : la main enfonce le ballon dans le cercle, le cercle plie de 6 px et revient (0,1 s), le filet s'étire (scaleY 1 → 1,15 → 1, 0,2 s), secousse caméra 6 px.
  PISTE CAMÉRA : dérive x +25 u/s ; 0.85 à 1.40 la caméra monte avec le joueur (y -180 u, power3.out) vers cam(1300, 360, 1.0) ; 1.60 à 2.13 poussée ×1 → ×1,12 vers le cercle (expo.out) ; secousse 6 px à 2.13 (0,12 s).
  COUCHES ET PROFONDEUR : avant-plan un joueur adverse flou coupé par le bord gauche (stickman blanc à 50 %, flou 16 px) ; sujet le joueur n° 15 et le cercle ; fond les projecteurs flous et le mur ; couches animées 3 à 4.
  OBJET-PONT ET VECTEUR : le fil devient le brin rouge du filet.
  SON : impact grave 39.58 (le smash, sur « panier »).
  IMAGE CLÉ : 2.15 : styleframes/png/A3.png : le stickman noir détouré de blanc, maillot rouge n° 15 « Contino Sport », short rouge, qui smashe ; filet blanc avec un brin rouge ; « Samedi, le numéro [15] monte au panier. ».

Scene 2 (2.60 à 4.75 s) : P28, le rouge est resté rouge, le joueur suspendu au cercle (silence 41.71 à 42.49)
  TEXTE ÉCRAN : sous-titre « Le rouge est [trait : resté] [boîte : rouge]. » (Le 2.70, rouge 3.03, est 3.31, resté 3.69, trait 3.69 à 4.09, boîte tracée 3.93, rouge. 3.97) ; il sort de 4.40 à 4.54.
  IMAGE DE DÉPART : le cercle et le filet après le smash, le joueur suspendu au cercle par la main droite.
  ÉTAPES : 2.60 le joueur reste suspendu au cercle, ses jambes se balancent (rotation ±6°, boucle finie de 0,8 s) ; 2.70 « Le » : la caméra continue de pousser, sur son dos, le 15 et « Contino Sport » plein cadre au centre gauche ; 2.80 le nuancier « Rouge club / BAT validé » arrive depuis la caméra (×4 flou 12 → net, 0,22 s expo.out), en avance sur « rouge » (3.03), et se pose contre le dos du maillot, à droite du 15 ; 3.31 sa pastille et le rouge du maillot s'alignent (même teinte, petit éclat blanc qui passe sur les deux, 0,2 s) ; 3.69 « resté » : trait sous le mot ; 3.97 « rouge » : le nuancier se tasse contre le tissu (×0,98 → 1) ; 4.20 le brin rouge se détache du filet (en haut du cadre) et file vers le haut à gauche (fxDrawThread inverse sur le filet, dessin vers le haut) ; 4.55 départ du tilt.
  PISTE CAMÉRA : 2.60 à 3.00 poussée ×1,12 → ×1,6 vers le dos du joueur, cam(1240, 420) (expo.out), dans le même sens que la poussée vers le cercle ; dérive échelle +1 %/s ; 4.55 à 4.75 tilt vers le haut power2.in vers l'état de couture cam(1480, 120, 1.15), flou 0 → 10.
  COUCHES ET PROFONDEUR : avant-plan le ballon qui retombe sous le cercle, flou, coupé par le bord droit ; sujet le dos du maillot et le nuancier côte à côte, marges égales ; fond la salle floue ; couches animées 3.
  OBJET-PONT ET VECTEUR : le brin rouge du filet file vers le haut et devient le fil qui rentre dans le chas du logo.
  SON : carillon 41.42 ; whoosh 41.95.
  IMAGE CLÉ : 3.98 : le dos du maillot n° 15 du joueur suspendu au cercle, le nuancier « Rouge club » posé contre le tissu, le même rouge, « Le rouge est [resté] [rouge]. ».

## Frame 10 : IFS, une qualité irréprochable · 42.20 → 46.75

- scene: Au bout du tilt, le sol d'encre de la fin ; le fil traverse le cadre et rentre dans le chas de l'aiguille de l'icône IFS, qui se pose ; le wordmark s'assemble ; la promesse s'écrit en sous-titre
- duration: 4.55s
- transition_in: cut
- status: outline
- src: compositions/frames/10-ifs.html
- voiceover: "IFS. Une qualité irréprochable, livrée en moins d'un mois."
- type: cta
- blueprint: logo-assemble-lockup (Adapt)
- focal: l'aiguille et le fil qui rentre dans son chas, puis le logo IFS
- rules: svg-path-draw, depth-of-field-blur
- world: dark
- handoff_in: à 0.00 : cam(1480, 120, 1.15) flou 10 px ; tilt vers le haut en cours (-2400 u/s en y), dérive 0 ; salle W3 : panier en haut du cadre, le brin rouge du filet détaché qui file vers le haut à gauche ; joueur n° 15 suspendu au cercle, son dos hors champ bas ; nuancier posé contre le dos du maillot ; sous-titre sorti ; grain 5 %
- handoff_out: à 4.55 : cam(960, 540, 1.0) flou 0 ; dérive x +12 u/s ; monde W4 sol d'encre ; à l'écran : icône IFS (150 px) et wordmark « IFS / Industrie Française de Sellerie » en haut au centre, l'aiguille de l'icône avec le fil rouge passé dans son chas qui ondule jusqu'au bord gauche ; bouton « Voir le catalogue » pas encore né ; sous-titre sorti ; grain 5 %

Word cues: IFS@0.29 Une@1.25 qualité@1.50 irréprochable@1.96 livrée@2.96 en@3.48 moins@3.82 d'un@3.98 mois@4.26

Scene 1 (0.00 à 4.55 s) : P29 et P30, le fil rentre dans le chas, le logo, la promesse
  TEXTE ÉCRAN : sous-titre « IFS. » (0.29) puis « Une qualité [boîte : irréprochable], » (Une 1.25, qualité 1.50, boîte tracée 1.92, irréprochable, 1.96) puis « livrée en moins d'un mois. » (livrée 2.96, en 3.48, moins 3.82, d'un 3.98, mois. 4.26) ; il sort de 4.40 à 4.54.
  IMAGE DE DÉPART : handoff_in ; au sommet du flou (0.00 à 0.12), la salle laisse place au sol d'encre W4 (exception écrite dans l'en-tête).
  ÉTAPES : 0.00 à 0.20 fin du tilt, le sol d'encre se pose ; 0.05 le fil traverse le cadre de la gauche vers le centre haut (fxDrawThread, 0,4 s expo.out) ; 0.12 l'icône IFS arrive depuis la caméra (×3 flou 12 → net, 0,22 s expo.out) au centre haut (960, 300), en avance sur « IFS » (0.29) ; 0.60 l'aiguille de l'icône s'allume (reflet qui la parcourt, 0,2 s) ; 0.80 le fil passe dans son chas (0,15 s) : rime du pivot ; scintillement ; 1.00 « IFS » du wordmark s'assemble lettre par lettre à droite de l'icône (0,05 s d'écart, ×1,3 flou 6 → net), puis « Industrie Française de Sellerie » (0,15 s) ; 1.25 à 4.26 le fil ondule lentement (vague de ±10 px qui court, boucle finie de 1,6 s) ; 1.96 « irréprochable » : le logo se tasse (×1,02 → 1) ; 2.40 cran de caméra ×1 → ×1,06 vers l'aiguille (0,3 s expo.out) ; 2.96 « livrée » : une vague plus forte court le long du fil jusqu'au chas (0,4 s) ; 3.40 le reflet repasse sur l'aiguille ; 3.82 « moins » : le fil se tend un instant ; 4.26 le bloc logo remonte de 40 px pour laisser la place au bouton (0,25 s power3.out).
  PISTE CAMÉRA : 0.00 à 0.30 fin du tilt, expo.out jusqu'à cam(960, 540, 1.0) ; dérive x +12 u/s de 0.30 à 4.55 ; 2.40 à 2.70 cran ×1 → ×1,06 vers l'aiguille, puis retour progressif à ×1 par une dérive d'échelle de -1,3 %/s jusqu'à 4.55.
  COUCHES ET PROFONDEUR : avant-plan une boucle du fil floue en bas à gauche (au-dessus de y 860) ; sujet le logo et l'aiguille ; fond le sol d'encre rayé ; couches animées 2.
  OBJET-PONT ET VECTEUR : l'aiguille et son fil restent en place pour la carte de fin.
  SON : scintillement 42.90 (l'aiguille se pose).
  IMAGE CLÉ : 1.40 : sur l'encre, l'icône IFS nette, le fil rouge passé dans le chas de son aiguille, « IFS » et « Industrie Française de Sellerie », « Une qualité irréprochable, » qui s'écrit.

## Frame 11 : Découvrez notre catalogue · 46.75 → 52.00

- scene: Le bouton « Voir le catalogue » naît sous le logo, l'URL s'écrit ; le curseur arrive d'un seul mouvement et clique ; le bouton se remplit ; tenue vivante, le fil ondule ; noir à 52.00
- duration: 5.25s
- transition_in: cut
- status: outline
- src: compositions/frames/11-catalogue.html
- voiceover: "Découvrez notre catalogue."
- type: cta
- blueprint: cta-morph-press (Adapt)
- focal: le bouton « Voir le catalogue », puis le curseur
- rules: cursor-click-ripple, press-release-spring
- world: dark
- handoff_in: à 0.00 : cam(960, 540, 1.0) flou 0 ; dérive x +12 u/s ; monde W4 sol d'encre ; à l'écran : icône IFS (150 px) et wordmark « IFS / Industrie Française de Sellerie » en haut au centre, l'aiguille de l'icône avec le fil rouge passé dans son chas qui ondule jusqu'au bord gauche ; bouton « Voir le catalogue » pas encore né ; sous-titre sorti ; grain 5 %
- handoff_out: aucun (fin du film, noir à 5.25)

Word cues: Découvrez@0.11 notre@0.67 catalogue@0.97

Scene 1 (0.00 à 5.25 s) : P31 et P32, le bouton, le clic, la tenue
  TEXTE ÉCRAN : sous-titre « Découvrez notre [boîte : catalogue]. » (Découvrez 0.11, notre 0.67, boîte tracée 0.93, catalogue. 0.97) ; il reste jusqu'à 4.60 puis sort avec le noir. Bouton « Voir le catalogue » ; URL « catalogue-ifs.netlify.app ».
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 le fil descend sous le logo et trace une ligne horizontale de 420 px (fxDrawThread, 0,3 s) ; 0.30 la ligne s'ouvre en bouton accent « Voir le catalogue » (clip inset 49,5 % → 0, 0,22 s power3.out) ; 0.67 « notre » : l'URL « catalogue-ifs.netlify.app » s'écrit sous le bouton (lettres à 0,015 s d'écart) ; 0.97 « catalogue » ; 0.70 à 1.15 le curseur arrive en UNE courbe depuis le bas à droite (x et y sur deux courbes, 0,45 s power3.out) ; 1.10 clic direct : pression ×0,85 (0,06 s), bouton accent-light → blanc → accent en 0,27 s, onde accent qui s'ouvre et s'efface ; 1.40 à 4.60 tenue vivante : le fil ondule (vague de ±10 px, boucle finie), l'aiguille brille une fois (2.80), le curseur dérive de 8 px ; 4.60 à 5.25 fondu au noir (le seul fondu du film).
  PISTE CAMÉRA : 0.00 à 0.20 cran ×1,0 → ×1,04 vers le bouton (expo.out) ; dérive x +12 u/s, échelle +0,6 %/s de 0.20 à 5.25.
  COUCHES ET PROFONDEUR : sujet le bouton et le curseur ; fond le logo et le fil ; sol d'encre ; couches animées 2.
  OBJET-PONT ET VECTEUR : aucun (fin).
  SON : clic 47.85.
  IMAGE CLÉ : 1.30 : sur l'encre, le logo IFS et son aiguille enfilée, le bouton magenta « Voir le catalogue » qui vient d'être cliqué, l'onde, l'URL, « Découvrez notre [catalogue]. ».
