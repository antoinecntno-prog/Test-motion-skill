---
titre: Passage des grilles de contrôle sur le storyboard « Le Temps perdu » (direction A, arbre doré de C3)
date: 2026-10-09
fichiers: STORYBOARD.md, frame.md, DIRECTIONS.md, onsets.json
---

# Grille de contrôle du storyboard

Verdicts : **tenu**, **tenu après correction**, **non tenu**. Temps locaux à la séquence sauf mention « global ».

## Vérifications mécaniques (script, 9 octobre)

- Durées : 12 séquences, somme 57.10 s, égale à `TOTAL` de build-audio.sh (57.1) et à la durée du montage voix
  (voix-montage.wav, 57,10 s). Chaque frontière tombe dans un silence de la voix (onsets.json) : 5.25, 10.76, 16.42,
  20.38, 25.40, 31.37, 34.60, 38.03, 43.67, 49.47, 53.10.
- Repère corrigé dans onsets.json : « porte » était daté à 5.40 (énergie de « Sa » prise pour le mot) ; la voix le dit
  doucement de 4.64 à 5.02 (enveloppe d'énergie vérifiée), et « Sa » commence à 5.38. La phrase 2 finit donc à 5.02 et
  la couture 5.25 tombe dans le silence 5.02 à 5.38.
- Passages de relais : les 11 coutures ont un `handoff_out` identique caractère pour caractère au `handoff_in`
  suivant (comparaison par script), y compris la coupe franche de 34.60 (global), qui porte son raccord de lumière des
  deux côtés (le cadre entier en dégradé #E0A84A → #FFF4DC, sans grain, sans forme ni texte).
- Paquets des sous-agents (`frame-packets.mjs`) : 12 paquets de 24,8 à 37,9 Ko, tous sous la limite de 48 Ko ; chaque
  paquet contient exactement le plan type et les règles de sa ligne `rules` (aucun identifiant de règle écrit par
  accident).
- Toutes les séquences entrent en `cut` ; aucune transition « effet » de l'assembleur ; pas de flash ni d'iris
  d'assemble.sh (LEAK_AT et IRIS_AT resteront vides) : les transitions sont dans l'image.
- `{{` absent de STORYBOARD.md et frame.md ; aucun tiret cadratin ni demi-cadratin dans les quatre fichiers (comptage
  Python sur U+2014 et U+2013) ; aucune des formules bannies du brief.
- Structure des plans : 28 plans ; 28 sur 28 ont une PISTE CAMÉRA chiffrée, nomment leurs quatre plans de profondeur,
  leur objet-pont ou vecteur et leur image clé.
- Écarts entre étapes (script) : plus long écart 0,48 s (séquence 10, fin de la grue jusqu'à « Désormais ») ; dans les
  3 premières secondes, aucun écart au-dessus de 0,30 s.
- Sous-titres : 22 morceaux, le plus long 45 signes (« Ce dirigeant ramenait le travail à la maison. ») ; la phrase 18
  se joue en deux morceaux (« Celui d'après, ils dessinèrent » puis « un second dinosaure. »).
- Sol au-dessus de la bande des sous-titres : chaque cadrage de référence respecte y_cam ≥ 900 - 340 / s (frame.md),
  ce qui laisse la bande y 890 à 980 au sol sombre.

## Grille de STORYBOARD-CRAFT.md § 5

1. **En-tête complet** (monde et stations par acte, fond texturé, couleurs de rôle, 2 signatures datées avec 6
   occurrences chacune, registres de texte, rimes, partition caméra, silences, coupes, rythme, son) : tenu.
2. **Piste caméra dans chaque plan, jamais à l'arrêt plus de 0,5 s hors silence écrit** : tenu (28 plans sur 28 avec
   une dérive chiffrée, y compris le noir du pivot, qui s'enfonce de 4 %/s, et la carte de fin, qui dérive de 1,5 %/s).
3. **Aucun trou de plus de 1 s, 0,3 s dans les 3 premières secondes** : tenu (0,48 s au plus ; 0,30 s au plus dans
   l'accroche).
4. **Apparitions ≤ 0,2 s, dérives ≥ 1 s, zone 0,3 à 0,9 s réservée à la caméra et au curseur** : tenu. Les durées de
   0,3 à 0,9 s qui ne sont pas de la caméra sont des tracés (second dinosaure 0,4 s, traits d'or 0,4 s, signature
   0,8 s), des boucles de balancier et de balançoire (sine), des chutes d'objets (feuilles 0,5 s, balle 0,6 s), le
   roulement de l'horloge (0,3 s) et la lumière du cadran qui déborde (0,38 s expo.in, mouvement de lumière qui porte la
   coupe) ; aucune apparition d'objet ne dure plus de 0,2 s.
5. **Chaque tenue de plus de 0,5 s nomme sa couche vivante ; zéro image figée** : tenu (la flamme, le grain par plan
   et la dérive vivent partout ; la tenue de fin nomme la flamme, l'oiseau, la poussière, le bouton qui respire).
6. **Chaque jonction nomme son objet-pont ou son vecteur ; zéro dédoublement** : tenu (28 sur 28). Les objets qui
   changent de rôle : la pile de devis (sous le bras, sur la table, tronc d'or), la balle (guide la caméra jusqu'à la
   chaise), les lettres (deviennent les feuilles épinglées), le dessin (mur, mains, devis, poteau), la chaîne (lien,
   puis oiseaux), le cadran (lumière du pivot), les feuilles (oiseaux de la fin). Le père et la fille ne sont jamais deux
   fois à l'écran : au saut « Le soir suivant » (38.03 global), le pied de l'escalier est à l'écran et la balançoire hors
   cadre.
7. **Transitions « effet » : 2 au plus** : tenu (zéro ; la sortie au noir de la fin est la sortie du film).
8. **Coupes franches au quota, chacune justifiée** : tenu (une seule, 34.60 global, « L'horloge » à 34.96, changement
   d'acte sur la même lumière d'or).
9. **Chaque entrée d'élément principal a un état de départ écrit** : tenu (couronne de l'horloge ×1,1 flou 4 ; lettres
   tombées de y -200 ; feuilles épinglées ×1,2 ; chiffre ×1,4 flou 8 ; bouton ×1,1 flou 6 ; « formateur IA » ×1,1
   flou 4 ; les marionnettes entrent en marchant depuis le bord du cadre ; le monde doré arrive par des masques de
   lumière).
10. **Écart image/voix écrit ; changements de composition sur le premier mot ou dans un silence ; chaque silence
    > 0,4 s est un plan** : tenu (17 silences nommés en en-tête, chacun avec son action ; whips, crans et reculs
    partent dans les silences et atterrissent sur « Sa », « Elle », « Pour », « Soir », « Alors », « L'horloge »,
    « Le », « Désormais », « La »).
11. **Au moins 3 verbes joués physiquement, contact à ± 0,1 s** : tenu (ramenait, passa, ouvrit deux fois, prit deux
    fois, s'effaçait, retrouva, glissa, vit, se mit au travail, s'automatisait, poussait, dessinèrent, rendre).
12. **Au moins la moitié des plans sur 3 niveaux, une parallaxe par acte** : tenu (28 plans sur 28 en quatre plans,
    sauf le noir du pivot en trois ; parallaxe ×1,8 / ×1 / ×0,5 / ×0,2 pendant chaque dérive, dans les deux actes).
13. **Couches animées : régime ≥ 2, pic 3 à 4, un seul élément actif par instant** : tenu.
14. **Rime** : tenu (la pile de l'accroche devient le tronc d'or ; l'arc du balancier devient celui de la balançoire ;
    les lettres I et A d'ombre reviennent en or ; le second dinosaure répond au premier ; les cases éteintes se
    rallument).
15. **Fin : un geste qui rassemble le film, curseur en courbe qui clique directement, état pressé en 3 couleurs et
    onde, 2 à 3 s de tenue vivante, sortie au noir** : tenu après correction. Première version : clic à 2.25, tenue de
    1,6 s. Corrigé : la signature s'écrit en 0,8 s, le bouton arrive à 1.00, le clic tombe à 1.80 ; tenue vivante de 1.92
    à 4.00 (2,1 s, noir compris). Le geste qui rassemble est le recul sur la maison relevée, puis les feuilles de l'arbre
    qui s'envolent en oiseaux.

## Grille de contrôle de SKILL.md

- [x] La première image est ce que nomme le premier mot (le dirigeant dans sa porte) ; le premier mot nomme la cible,
      la douleur suit avant 2,1 s (« le travail à la maison »).
- [x] Chaque phrase a sa composition ; sous-titre mot à mot en bas au centre.
- [x] Un mot clé par phrase dans la boîte bordeaux ; une couleur par rôle ; 4 pics soulignés d'or ; aucun mot géant.
- [x] Une seule chose à regarder ; marges égales ; aucun décor sans sens.
- [x] La douleur est montrée dans ce que la cible reconnaît : les devis, les dossiers, la soirée passée dessus (le
      conte remplace les interfaces, choix du brief).
- [x] Un pivot explicite (phrase sur le noir, silence de 1,56 s) avant la marque, et le fond change avec lui.
- [x] Aucun logo ; la signature arrive à la carte de fin.
- [x] Coupes franches au quota de la voix narrative (1) ; aucun fondu ; tout le reste passe par la caméra ou un objet ;
      la caméra ne revient jamais sur un décor quitté.
- [x] Le chiffre roule jusqu'à sa valeur (0 → 10 h sur « dix »).
- [x] Le produit est joué par des gestes : l'horloge tamponne les devis et les envoie seuls (aucune interface réelle,
      choix du brief).
- [x] Un élément de l'accroche revient avant la fin (la pile de devis, devenue le tronc d'or).
- [x] Carte de fin : un bouton, un curseur qui arrive et clique directement, tenue vivante de 2 s, noir.
- [x] Lisible sans le son du début à la fin (la preuve s'écrit à l'écran pendant qu'elle est dite).
- [x] Un événement toutes les 0,5 s au plus ; aucune tenue figée ; aucune mise en page tenue plus de 3 s (tenu après
      correction : crans courts ajoutés à 2.30 de la séquence 1, 1.60 de la 4, 2.20 de la 6 et de la 8, 2.30 et 3.95
      de la 10).
- [ ] Rendu : à vérifier sur la vidéo (pas de letterSpacing, pas de segment noir hors pivot, aucun élément hors de sa
      séquence).

## Règles de la maison et critères du brief

- **Cible et douleur avant 3 s** : tenu (« dirigeant » en boîte à 0.28, « travail » souligné à 1.38, « à la maison »
  à 1.90).
- **Chaque promesse est sur le site** : tenu pour les textes à l'écran (« 10 h gagnées chaque semaine par la dernière
  dirigeante formée », « Réserver un audit IA de 30 minutes », « calendly.com/antoine-cntno/30min ·
  antoinecontino.fr », « Antoine Contino, formateur IA »), repris des citations du site fournies par Antoine (le site
  est bloqué par le proxy de cette session). Aucun prix, aucune durée de formation, aucun nom de client.
- **Seule la technique vient de la référence** : tenu (frame.md § negative : ni capuche, ni squelette, ni faux, ni
  sablier ; aucune tige seule ; aucun départ devant un soleil ; les oiseaux de la fin volent vers la caméra, sur un ciel
  sans astre).
- **Grammaire du brief** : tenu (4 plans de profondeur portant chacun leur grain ; vignettage chaud ; flamme ± 3 % vers
  7 Hz ; poses à 12 i/s et caméra à 30 i/s ; un seul plan continu ; transitions dans l'image : volet de cloison, encre,
  fumée, lumière, feuilles, oiseaux ; monde doré en silhouettes inversées avec poussière d'or ; bordeaux réservé à la
  boîte et à la carte de fin).
- **Sons** : 4 whooshes et 1 scintillement (plafond 7 et 1) ; familles du brief (papier, flamme, vent, ailes, bois des
  tiges et des roulettes). La bibliothèque locale (`media-use/audio/assets/sfx/`) ne contient que des sons d'interface :
  la source des sons de papier, de flamme, de vent, d'ailes et de bois se décide à l'étape 5.
- **Caméra** : deux reculs francs (« Soir après soir », 20.26 global ; la maison relevée, 49.07 global) et une montée
  de grue (43.33 global) ; un cran de suivi de 64 u vers la gauche accompagne la fille qui revient vers son père
  (27.60 global, même pièce, même cadrage). Aucun retour sur un décor quitté.

## Ce qui reste ouvert

- `reference/maison.html` (le monde écrit une fois, copié par chaque séquence) s'écrit au pilote de l'étape 4, avec la
  mesure canvas 2D contre SVG sur 5 s du style complet (--workers 3), à partir de `styleframes/_ombres.js`.
- Source des bruitages à l'étape 5 : synthèse par script (gratuit) ou effets ElevenLabs par le connecteur (crédits, avec
  l'accord d'Antoine).
