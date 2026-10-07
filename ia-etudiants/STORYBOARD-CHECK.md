---
titre: Passage des grilles de contrôle sur le storyboard « Le carnet » (film 1, formation IA pour les étudiants)
date: 2026-10-07
fichiers: STORYBOARD.md, frame.md, reference/aquarelle.html
---

# Grille de contrôle du storyboard

Verdicts : **tenu**, **tenu après correction** (écart trouvé par la grille et corrigé dans STORYBOARD.md ou frame.md),
**non tenu** (écart restant, avec sa raison). Temps locaux à la séquence sauf mention « global ».

## Vérifications mécaniques

- Durées : 12 séquences, somme 50.80 s (script de method.md § 6), égale à `TOTAL` de build-audio.sh et à la durée du
  montage voix (50.80 s). Chaque frontière de séquence tombe dans un silence de la voix (onsets.json).
- Passages de relais : les 11 coutures ont un `handoff_out` identique caractère pour caractère au `handoff_in`
  suivant, y compris la coupe franche de 23.30 (global), qui porte son raccord de couleur des deux côtés.
- Paquets des sous-agents (`frame-packets.mjs`) : 12 paquets de 16,6 à 43,7 Ko, tous sous la limite de 48 Ko ;
  `_role.md` 19,9 Ko.
- Recettes : les 9 blueprints et les 8 règles cités existent dans `hyperframes-animation/` (camera-journey,
  spatial-pan-stations, zoom-out-workspace-reveal, video-text-pivot, cursor-ui-demo, comparison-split, dataviz-countup,
  logo-assemble-lockup, cta-morph-press ; depth-of-field-blur, coordinate-target-zoom, waterfall-entry, svg-path-draw,
  counting-dynamic-scale, stat-bars-and-fills, cursor-click-ripple, press-release-spring).
- Référence exécutable `reference/aquarelle.html` : rendue dans Chromium sans erreur JavaScript, 10 états de démo
  (pages 1 à 8 au cadrage de référence, double page, écran, pivot). Un écart trouvé au rendu : la boîte du mot clé
  passait derrière la page (z-index -1 hors contexte d'empilement), corrigé par `z-index:0` sur `.aq-sw`.
- `grep -n "{{"` ne renvoie rien dans STORYBOARD.md, frame.md et DIRECTIONS.md.
- Typographie : aucun tiret cadratin ni demi-cadratin dans STORYBOARD.md, frame.md, DIRECTIONS.md et
  reference/aquarelle.html.

## Grille de STORYBOARD-CRAFT.md § 5

1. **En-tête complet** (monde et coordonnées des 8 pages, sol texturé par acte, couleurs de rôle, 2 signatures datées
   avec 12 et 17 occurrences, registres de texte à un mouvement chacun, rimes) : tenu.
2. **Piste caméra dans chaque plan, jamais à l'arrêt plus de 0,5 s hors silence écrit** : tenu. Les 28 plans ont une
   dérive chiffrée (u/s ou %/s) et des mouvements datés avec leur cible `cam(...)` ; le seul arrêt est 3.93 à 4.08 de
   la séquence 5, sous le lavis qui recouvre le cadre (le mouvement est celui de la tache), dans le silence du pivot.
3. **Aucun trou de plus de 1 s entre deux étapes, 0,3 s dans les 3 premières secondes** : tenu après correction. La
   grille a trouvé 0,34 s entre 2.26 et 2.60 dans l'accroche (séquence 1) : ajout du champ qui s'éclaire à 2.40. Les
   plus longs écarts restants : 0,69 s (séquence 11, 1.51 à 2.20, pendant que la signature sèche) et 0,66 s (séquence 4,
   0.47 à 1.13, entre deux effacements), tous sous 1 s. La tenue de fin (séquence 12, 0.80 à 2.60) nomme quatre
   couches vivantes.
4. **Apparitions ≤ 0,2 s, dérives ≥ 1 s, zone 0,3 à 0,9 s réservée à la caméra et au curseur (expo, power3, power4)** :
   tenu après correction. Corrigés : les deux pages tournées du gag (0,3 s power2.inOut → 0,24 s power2.in), le carnet
   qui se referme (0,5 s power3.inOut → 0,28 s power3.in), la goutte ocre qui grossit (0,5 s power2.in → 0,36 s
   power3.in), l'étalement des deux taches du croquis (0,3 s → 0,2 s expo.out), la bavure (0,4 s power1.out → geste de
   0,2 s puis dérive linéaire de 1,0 s), le carnet qui sort du cadre (0,3 s → 0,22 s), l'inclinaison de la page dans
   les mains (0,3 s → 0,2 s), le curseur qui s'écarte après le clic (0,3 s power2.out → 0,4 s power3.out, geste de
   curseur). Les durées de 0,3 à 1,0 s restantes sont des tracés (signature, notes manuscrites, coche, cercle du
   chrono : la vitesse d'une main), des séchages (aqDry 0,4 à 0,8 s, un changement d'état progressif, pas une
   apparition) et des mouvements de caméra.
5. **Chaque tenue de plus de 0,5 s nomme sa couche vivante ; zéro image figée** : tenu (dérive de caméra dans chaque
   plan ; ondes de l'encre au pivot ; granulation, grain, séchage et respiration de l'ombre dans la tenue finale).
6. **Chaque jonction nomme son objet-pont ou son vecteur ; zéro dédoublement** : tenu. 11 coutures : traînée de la
   goutte (plan 1 → 2), écran qui s'allume (2 → 3), réponse grise → pages grises (séquence 1 → 2), copie et stylo
   (gag), lavis gris de la lampe (séquence 3), goutte en vol → note, lignes du fond → sujet, taches des coins
   (séquence 3 → 4), goutte → noir (4 → 5), lavis ocre → page de la classe (5 → 6), petit écran → grand écran
   (6), question posée (6 → 7), cran d'une ligne à l'autre (7), couleurs du croquis → bulles (7 → 8), couleurs des
   bulles → équipes (8 → 9), aiguille du chrono → colonnes (9), couleur qui déborde (9 → 10), carnet refermé → page
   dans les mains (10), goutte de la page → goutte de la signature (10 → 11), signature → bouton (11), curseur en
   mouvement (11 → 12). La page du début redessinée (séquence 10) et la page P1 ne sont jamais à l'écran ensemble.
7. **Transitions « effet » : 2 au plus** : tenu (zéro : la sortie au noir est un lavis d'encre qui monte, objet du
   pivot rejoué).
8. **Coupes franches au quota, chacune justifiée** : tenu (une seule, 23.30 global, « Je » à 23.67, changement d'acte
   à l'impact de la goutte ocre, masquée par le lavis qui remplit le cadre des deux côtés).
9. **Chaque entrée d'élément principal a un état de départ écrit** : tenu (gouttes ×4 flou 10 depuis la caméra ou
   depuis un point ; pages glissées x -600 flou 8 ; champ et étiquettes ×1,1 flou 6 ; lettres du pivot qui convergent ;
   stylo depuis le haut ; tables par impact ×0,2 → 1 ; figures par coups de pinceau). Aucun fondu à taille finale.
10. **Écart image/voix écrit pour chaque mot-image ; changements de composition sur le premier mot ou dans un silence ;
    chaque silence > 0,4 s est un plan** : tenu. Les 11 silences de l'en-tête ont leur action ; les crans tombent dans
    le silence qui précède le premier mot (1.60 → « Il » 1.67, 3.00 → « La » 3.11, 1.00 → « par » 1.10, 1.90 → « la »
    2.01, 2.60 → « Et » 2.97, 2.50 → « Réservez » 2.92) et les whips atterrissent sur lui (« Lundi », « Il », « Ils »,
    « En », « Une », « Antoine »).
11. **Au moins 3 verbes joués physiquement** : tenu (13 : colle 2.60, rend, tourne, s'éteint 1.02, pâlit, tombe 3.59,
    s'effacent, questionner, vérifier, contredire, créer, revient 3.04, se referme 2.14, redevient 3.62, clique 0.25).
12. **Au moins la moitié des plans sur 3 niveaux, une parallaxe par acte, mot géant derrière ou devant un objet** :
    tenu (26 plans sur 28 nomment un avant-plan flou coupé par le bord : bord de la page suivante, goutte en vol,
    stylo, cadre de fenêtre ; parallaxe 2,5 : 1 : 0,4 déclarée en en-tête et dans la séquence 4 ; aucun mot géant,
    le moment typographique du pivot est seul sur le noir, devant les ondes).
13. **Couches animées : régime ≥ 2, pic 3 à 4, un seul élément actif** : tenu (2 à 4 par plan, un sujet par phrase).
14. **Rime** : tenu (la goutte de la signature 43.50 rejoue la goutte d'ouverture 0.02 ; la page du début revient
    colorée à 41.11 ; le bouton est une goutte ocre séchée comme les tables ; le curseur du collage revient cliquer).
15. **Fin** : tenu (la page du début dans les mains rassemble le film ; le curseur arrive en une seule courbe de 0,5 s
    power3.out, à cheval sur la couture 11 → 12, clique directement avec pression, trois couleurs et onde ; 2,4 s de
    tenue vivante ; sortie au noir par le lavis d'encre).

## Grille de contrôle de SKILL.md et règles de la maison

- Première image = la lampe allumée la nuit, ce que nomme « Dimanche, vingt-trois heures » ; jamais le logo (il n'y
  en a pas) : tenu.
- Chaque phrase a sa composition ; sous-titre mot par mot en bas au centre : tenu (16 phrases, 16 compositions).
- Un mot clé par phrase dans la boîte : tenu après correction (la phrase « Ils apprennent à la questionner, à la
  vérifier, à la contredire, à créer avec elle » portait deux boîtes, « questionner » et « créer » ; la seconde est
  retirée). Une couleur par rôle ; 4 pics soulignés ; aucun mot géant : tenu.
- Une seule chose à regarder ; côte à côte aux marges égales (les deux bulles, les deux équipes, les deux colonnes) ;
  aucun décor sans sens (les notes manuscrites datent la scène, le titre « Défi 3 » nomme le défi) : tenu.
- La douleur se joue dans un outil que la cible reconnaît : la fenêtre de chat générique, dessinée : tenu.
- Pivot explicite (phrase sur le noir, 2,08 s de silence) et le sol change avec lui (noir de l'encre, puis page
  colorée) : tenu.
- Logo : aucun fourni ; la signature arrive à 43.58 : tenu.
- Coupes au quota (1), 0 fondu, coutures égales aux relais, caméra sans aller-retour (de gauche à droite ou en
  profondeur) : tenu.
- Chiffres : la note « 12 » s'écrit à l'encre et sèche ; le chrono roule (00:42 → 00:41 → 00:40) ; les points
  s'empilent goutte à goutte : tenu.
- Le produit par des gestes (taper, cocher, barrer, dessiner, cliquer) : tenu.
- Un élément de l'accroche revient (la goutte, la page du début, le curseur) : tenu.
- Carte de fin : un bouton, curseur en une courbe, clic direct, 2,4 s de tenue vivante, noir : tenu.
- Lisible sans le son : tenu (sous-titres complets, gestes littéraux).
- Du nouveau toutes les 0,5 à 1 s, aucune tenue figée : tenu. Jamais la même mise en page plus de 3 s : la séquence 8
  (3,07 s) est un seul plan dont la mise en page change par les deux bulles qui se remplissent ; la séquence 4 (plan de
  3,10 s) change par les quatre effacements : tenu avec cette lecture.
- Règles de la maison : sous-titres (bande y 890 à 980 vide, 62 px), boîte accent, traits fins, curseur sans
  hésitation, deux vitesses, arrivées trop grandes et floues, douleur sans produit du client (fenêtre générique, aucune
  marque), personnages qui font le geste (se penchent, lèvent le bras), marque fixée au brief (« Antoine Contino,
  formateur IA », les deux adresses), anonymisation (aucun nom, aucune note réelle : le « 12 » et la dissertation sont
  des éléments du récit), densité sonore (7 whooshes, 1 scintillement, aucune lettre sonorisée) : tenu. Au rendu : le
  papier sous le monde clair, aucun segment noir hors le pivot et la sortie, aucune animation de letterSpacing, musique
  de tension 2 à 3 dB sous l'élan (étape 5).

## Écarts restants

- Aucun. Deux points à surveiller au pilote : la bande du sous-titre (y 890 à 980) doit rester vide au cadrage de
  référence de chaque plan (frame.md, négatif 4), et la couture 11 → 12 dans le mouvement du curseur demande que les
  deux séquences posent le curseur à (13230, 790) avec le même reste de trajet.
