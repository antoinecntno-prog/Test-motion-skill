---
titre: Passage des grilles de contrôle sur le storyboard « Le carnet » (film 3, préparer ses cours avec l'IA)
date: 2026-10-07
fichiers: STORYBOARD.md, frame.md, reference/aquarelle.html
---

# Grille de contrôle du storyboard

Verdicts : **tenu**, **tenu après correction**, **non tenu**. Temps locaux à la séquence sauf mention « global ». Le film
hérite de la direction A et du pilote validés sur le film 1 (DIRECTIONS.md) ; la grille repasse sur ce qui change : le
découpage, les relais, les étapes et les objets du bureau, de la salle et de la porte.

## Vérifications mécaniques (script, 7 octobre)

- Durées : 14 séquences, somme 50.60 s, égale à `TOTAL` de build-audio.sh et d'assemble.sh (50.60) et à la durée du
  montage voix (44.04 + 2.0 + 1.5 + 3.0). Chaque frontière tombe dans un silence de la voix ou au sommet d'un
  mouvement de caméra écrit (onsets.json, DIRECTIONS.md) ; la couture 26.50 tombe au milieu du cran entre les
  vignettes 2 et 3, dans le silence 26.36 à 26.57.
- Passages de relais : les 13 coutures ont un `handoff_out` identique caractère pour caractère au `handoff_in`
  suivant (comparaison par script), y compris la coupe franche de 20.42 (global), qui porte son raccord de couleur des
  deux côtés (#EFD7A6 à 100 %, sans grain ni texte).
- Paquets des sous-agents (`frame-packets.mjs`) : 14 paquets de 19,9 à 44,1 Ko, tous sous la limite de 48 Ko.
- Toutes les séquences entrent en `cut` ; aucune transition « effet ».
- `{{` absent de STORYBOARD.md, frame.md et DIRECTIONS.md ; aucun tiret cadratin ni demi-cadratin dans les quatre
  fichiers (comptage Python sur U+2014 et U+2013).
- Structure des plans : 28 plans ; 27 sur 28 ont une PISTE CAMÉRA chiffrée, 28 sur 28 nomment leur avant-plan,
  28 sur 28 leur objet-pont ou vecteur, 28 sur 28 leur image clé.
- Écarts entre étapes (script) : un seul écart au-dessus de 0,3 s dans les 3 premières secondes de l'accroche, 2.26 →
  2.58 (0,32 s), corrigé par la lueur de la lampe qui vacille à 2.40 ; aucun écart au-dessus de 1 s hors la tenue
  vivante de la fin (0.80 → 2.50, quatre couches nommées).

## Grille de STORYBOARD-CRAFT.md § 5

1. **En-tête complet** (monde et coordonnées des 8 pages, couleurs de rôle, 2 signatures datées avec 6 et 13
   occurrences, registres, rimes, partition caméra, silences, coupes, rythme, son) : tenu.
2. **Piste caméra dans chaque plan, jamais à l'arrêt plus de 0,5 s hors silence écrit** : tenu (27 plans sur 28 avec une
   dérive chiffrée ; le seul arrêt est 3.80 à 4.02 de la séquence 6, pendant la chute de la goutte ocre, dans le
   silence du pivot).
3. **Aucun trou de plus de 1 s entre deux étapes, 0,3 s dans les 3 premières secondes** : tenu après correction (voir
   ci-dessus). Plus longs écarts restants : 0,60 s (séquence 10, 0.54 → 1.14, l'étiquette puis la question),
   0,53 s (séquence 13, 0.66 → 1.19, la signature se trace), 0,50 s (séquence 2, 1.58 → 2.08, les vagues d'écrans).
4. **Apparitions ≤ 0,2 s, dérives ≥ 1 s, zone 0,3 à 0,9 s réservée à la caméra et au curseur** : tenu. Les durées de
   0,3 à 0,9 s à ease lent sont des tracés (bureau 0,5 s, cadres de vignette 0,3 s, cercle barré 0,3 s, trait de craie
   0,4 s), le coup de pinceau du trait ocre (0,4 s) et l'onde du clic (0,45 s) ; aucune apparition d'objet.
5. **Chaque tenue de plus de 0,5 s nomme sa couche vivante ; zéro image figée** : tenu.
6. **Chaque jonction nomme son objet-pont ou son vecteur ; zéro dédoublement** : tenu (28 plans sur 28 ; la
   diapositive de P1 est celle projetée en P2 ; la lueur de la fente est celle des poches ; la marge ocre du plan
   devient les vignettes ; le curseur porte la couture 13 → 14).
7. **Transitions « effet » : 2 au plus** : tenu (zéro).
8. **Coupes franches au quota, chacune justifiée** : tenu (une seule, 20.42 global, « Je » à 20.50).
9. **Chaque entrée d'élément principal a un état de départ écrit** : tenu (gouttes ×4 flou 10 ; cartes glissées
   x +400 flou 6 ; objets posés ×1,1 flou 6 → net ; figures et bulles par tracé ou coup de pinceau ; notes par masque ;
   main et stylo par le bas droit).
10. **Écart image/voix écrit pour chaque mot-image ; changements de composition sur le premier mot ou dans un
    silence ; chaque silence > 0,4 s est un plan** : tenu (10 silences nommés en en-tête, chacun avec son action ;
    les whips et crans partent dans le silence et atterrissent sur le premier mot : « Dans », « Vous », « Le », « Je »,
    « Un », « une », « Vos », « Vos », « Le », « Antoine »).
11. **Au moins 3 verbes joués physiquement** : tenu (défile, s'allument, interdisez, servent, avance, penchent,
    entrer, préparer, corrige, dédouble, tape, vérifie, barre, s'adapte, redevient, se penche, clique).
12. **Au moins la moitié des plans sur 3 niveaux, une parallaxe par acte, mot géant devant ou derrière un objet** :
    tenu (28 plans sur 28 nomment un avant-plan flou coupé par le bord ; parallaxe en en-tête ; aucun mot géant).
13. **Couches animées : régime ≥ 2, pic 3 à 4, un seul élément actif** : tenu.
14. **Rime** : tenu (la salle en couleur 40.38 contre la salle grise 5.80 ; le bureau coloré 20.42 contre le bureau
    gris 0.00 ; la marge ocre reprise trois fois ; la goutte de la signature des trois films).
15. **Fin** : tenu (même carte que les films 1 et 2 ; curseur à (13230, 790) avec 0,20 s de trajet des deux côtés de la
    couture 13 → 14 ; clic direct ; 1,7 s de tenue vivante ; noir à 50.60).

## Grille de contrôle de SKILL.md et règles de la maison

- Première image = le bureau du prof un mardi soir, ce que nomme « Mardi soir » : tenu.
- Chaque phrase a sa composition ; sous-titre mot par mot en bas au centre : tenu (la phrase des quatre vignettes se
  joue en quatre morceaux, une boîte pour l'ensemble, « en direct »).
- Boîtes : Mardi, demain, même, l'IA, l'interdisez, quand même, ailleurs, montre, en direct, s'en servir, réflexes,
  objectifs, pédagogie, redevient, disponible, formateur IA, Réservez ; 4 traits : entrer, préparer, progresser,
  vivant ; aucun mot géant : tenu.
- Aucune interface réelle, aucun outil nommé, aucun chiffre écrit (la date est « l'an dernier », « trente » reste dans
  la voix), aucun nom : tenu.
- Pivot explicite (question sur le noir sur deux lignes, 2,01 s de silence) et le sol change avec lui : tenu.
- Logo : aucun fourni ; la signature arrive à 43.69 : tenu.
- Carte de fin : un bouton, curseur en une courbe, clic direct, tenue vivante, noir : tenu.
- Densité sonore : 7 whooshes, 1 scintillement, aucune lettre sonorisée (sfx-events.json, 122 événements) : tenu.
- Règles de la maison (bande du sous-titre vide, boîte accent, traits fins, curseur sans hésitation, deux vitesses,
  arrivées trop grandes et floues, marque fixée au brief) : tenu par construction, à vérifier au rendu (frame.md §
  framings : la porte 420 × 640 et les rangs d'élèves sont placés pour rester au-dessus de y 880 au cadrage de référence).

## Écarts restants

- Aucun. Points à surveiller au montage : la salle de P2 et de P7 partage ses trente positions ; la diapositive du
  portable, de la pile et du tableau est la même ; la couture 13 → 14 dans le mouvement du curseur.
