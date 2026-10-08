---
titre: Passage des grilles de contrôle sur le storyboard « Le carnet » (film 2, formation IA pour les équipes pédagogiques)
date: 2026-10-07
fichiers: STORYBOARD.md, frame.md, reference/aquarelle.html
---

# Grille de contrôle du storyboard

Verdicts : **tenu**, **tenu après correction** (écart trouvé par la grille et corrigé dans STORYBOARD.md ou frame.md),
**non tenu** (écart restant, avec sa raison). Temps locaux à la séquence sauf mention « global ». Le film hérite de la
direction A et du pilote validés sur le film 1 (DIRECTIONS.md) ; la grille repasse sur ce qui change : le découpage,
les relais, les étapes et les objets de la salle des profs.

## Vérifications mécaniques (script, 7 octobre)

- Durées : 13 séquences, somme 52.00 s, égale à `TOTAL` de build-audio.sh et d'assemble.sh (52.00) et à la durée
  du montage voix (45.40 + 2.0 + 1.5 + 3.0). Chaque frontière tombe dans un silence de la voix (onsets.json, DIRECTIONS.md).
- Passages de relais : les 12 coutures ont un `handoff_out` identique caractère pour caractère au `handoff_in`
  suivant (comparaison par script après retrait du préfixe « à t : »), y compris la coupe franche de 22.40 (global),
  qui porte son raccord de couleur des deux côtés (#EFD7A6 à 100 %, sans grain ni texte).
- Paquets des sous-agents (`frame-packets.mjs`) : 13 paquets de 16,4 à 43,6 Ko, tous sous la limite de 48 Ko ;
  `_role.md` 19,9 Ko.
- Toutes les séquences entrent en `cut` (13 sur 13) ; aucune transition « effet ».
- `{{` absent de STORYBOARD.md, frame.md et DIRECTIONS.md ; aucun tiret cadratin ni demi-cadratin dans les quatre
  fichiers (comptage Python sur les caractères U+2014 et U+2013).
- Structure des plans : 24 plans ; 23 sur 24 ont une PISTE CAMÉRA chiffrée (u/s ou %/s), 22 sur 24 nomment leur
  avant-plan, 24 sur 24 leur objet-pont ou vecteur, 24 sur 24 leur image clé.
- Aucune apparition « en fondu » hors les rappels négatifs (0 occurrence hors négation).
- frame.md : trois restes du film 1 corrigés (le moment typographique citait la phrase du film 1 et « apprendre »,
  la carte de fin disait « noir à 50.80 », le négatif citait le chronomètre du défi).

## Grille de STORYBOARD-CRAFT.md § 5

1. **En-tête complet** (monde et coordonnées des 8 pages, couleurs de rôle, 2 signatures datées avec 9 et 16
   occurrences, registres de texte, rimes, partition caméra, silences, coupes, rythme, son) : tenu.
2. **Piste caméra dans chaque plan, jamais à l'arrêt plus de 0,5 s hors silence écrit** : tenu (23 plans sur 24 avec une
   dérive chiffrée ; le seul arrêt est la tenue de la question au pivot, sous une dérive d'échelle, dans le silence
   20.72 à 22.67).
3. **Aucun trou de plus de 1 s entre deux étapes, 0,3 s dans les 3 premières secondes** : tenu après correction. Le
   script a trouvé deux écarts dans l'accroche : 0.50 → 0.86 (0,36 s) et 2.18 → 2.66 (0,48 s) ; ajout des
   éclaboussures qui sèchent à 0.68 et des lavis de la nuit qui s'étalent à 2.40. Plus longs écarts restants : 0,74 s
   (séquence 4, 4.26 → 5.00, la main remplit les cases), 0,60 s (séquence 9, 2.80 → 3.40, les verticales se tracent),
   0,55 s (séquence 12, 0.76 → 1.31, la signature se trace). La tenue de fin (séquence 13, 0.80 → 2.40) nomme quatre
   couches vivantes.
4. **Apparitions ≤ 0,2 s, dérives ≥ 1 s, zone 0,3 à 0,9 s réservée à la caméra et au curseur** : tenu. Le script a
   listé les durées de 0,3 à 0,9 s à ease lent : le tracé de la table (0,5 s power2.out), le trait de craie (0,4 s
   power1.inOut), le coup de pinceau du lavis ocre (0,4 s power2.out), l'onde du clic (0,45 s power1.out) : des
   tracés et des gestes de main, un séchage, une onde ; aucune apparition d'objet.
5. **Chaque tenue de plus de 0,5 s nomme sa couche vivante ; zéro image figée** : tenu (dérive de caméra dans chaque
   plan ; ondes de l'encre au pivot ; granulation, grain, séchage et respiration de l'ombre dans la tenue finale).
6. **Chaque jonction nomme son objet-pont ou son vecteur ; zéro dédoublement** : tenu après correction. 24 plans sur 24
   nomment leur objet-pont. La grille a trouvé un dédoublement : le relais 7 → 8 pose le titre « Séquence 3 » sur la
   fiche, et la séquence 8 le révélait une seconde fois à 2.79 ; remplacé par un soulignement à l'encre.
7. **Transitions « effet » : 2 au plus** : tenu (zéro).
8. **Coupes franches au quota, chacune justifiée** : tenu (une seule, 22.40 global, « Je » à 22.67, changement
   d'acte à l'impact de la goutte ocre, cadre entièrement lavis des deux côtés).
9. **Chaque entrée d'élément principal a un état de départ écrit** : tenu (gouttes ×4 flou 10 depuis la caméra ;
   feuilles glissées x +400 ou +500 flou ; objets posés ×1,1 flou 6 → net ; silhouettes par coups de pinceau ; traits
   tracés ; notes révélées par masque ; fiche dédoublée par glissement de 180 u).
10. **Écart image/voix écrit pour chaque mot-image ; changements de composition sur le premier mot ou dans un
    silence ; chaque silence > 0,4 s est un plan** : tenu. Les 8 silences de l'en-tête ont leur action ; les crans
    et les whips partent dans le silence qui précède le premier mot et atterrissent sur lui (« Les », « Vous »,
    « Je », « Un », « Un », « Aucun », « Le », « Antoine »).
11. **Au moins 3 verbes joués physiquement** : tenu (se rentrent, monte, s'allume, se remplit, tourne, refroidit,
    transmet, se quadrille, pâlissent, plonge, s'écrit, se relit, se dédouble, se replie, se trace, fume, s'efface,
    reviennent, clique).
12. **Au moins la moitié des plans sur 3 niveaux, une parallaxe par acte, mot géant derrière ou devant un objet** :
    tenu (22 plans sur 24 nomment un avant-plan flou coupé par le bord ; parallaxe 2,5 : 1 : 0,4 en en-tête ; aucun mot
    géant, le moment typographique du pivot est seul sur le noir).
13. **Couches animées : régime ≥ 2, pic 3 à 4, un seul élément actif** : tenu (2 à 4 par plan, un sujet par phrase).
14. **Rime** : tenu (tasse qui fume 40.28 contre tasse qui refroidit 9.33 ; élèves qui reviennent 42.18 contre élèves
    effacés 17.58 ; salle pleine 22.40 contre salle vide 0.02 ; la goutte de la signature des deux films).
15. **Fin** : tenu (même carte que le film 1 ; curseur en une seule courbe à cheval sur la couture 12 → 13, position
    (13230, 790) et reste de trajet 0,20 s écrits des deux côtés ; clic direct ; 1,6 s de tenue vivante ; noir à 52.00
    par le lavis d'encre).

## Grille de contrôle de SKILL.md et règles de la maison

- Première image = la page nue qui se dessine en salle des profs, ce que nomme « Lundi, dix-huit heures » : tenu.
- Chaque phrase a sa composition ; sous-titre mot par mot en bas au centre : tenu (21 phrases ou morceaux, une boîte
  chacun : Lundi, vide, copies, mails, bulletins, métier, tableaux, sens, case, forme, documents, bulletin,
  séquence, mail, grille, prérequis, quotidien, temps, sens, formateur IA, Réservez).
- Un mot clé par phrase dans la boîte, une couleur par rôle, 4 pics soulignés, aucun mot géant : tenu.
- Une seule chose à regarder ; aucun décor sans sens ; aucune interface réelle (boîte de réception et fenêtre de mail
  génériques, dessinées à l'encre, objets sans nom) : tenu.
- Pivot explicite (question sur le noir, 1,95 s de silence) et le sol change avec lui : tenu.
- Logo : aucun fourni ; la signature arrive à 45.31 : tenu.
- Anonymisation : aucun nom de famille, d'élève, d'établissement, aucun chiffre de gain, aucun prix (BRIEF.md) : tenu ;
  le seul chiffre à l'écran est « 12 » dans « Objet : sortie du 12 », une date générique d'un objet de mail.
- Carte de fin : un bouton, curseur en une courbe, clic direct, tenue vivante, noir : tenu.
- Lisible sans le son : tenu (sous-titres complets, gestes littéraux).
- Densité sonore : 7 whooshes, 1 scintillement, aucune lettre sonorisée (sfx-events.json, 73 événements) : tenu.
- Règles de la maison (bande du sous-titre vide, boîte accent, traits fins, curseur sans hésitation, deux vitesses,
  arrivées trop grandes et floues, marque fixée au brief) : tenu par construction, à vérifier au rendu comme au
  film 1 (bande y 890 à 980 : au cadrage de référence, tout objet au-dessus de y 880).

## Écarts restants

- Aucun. Points à surveiller au montage : les états partagés de la salle des profs entre les séquences 1, 2 et 3
  (horloge, pile, vapeur, écran) et du tableau entre 3, 4 et 5 (cases, main, élèves), passés à chaque constructeur
  avec les mêmes coordonnées ; la couture 12 → 13 dans le mouvement du curseur.
