---
titre: Passage des grilles de contrôle sur le storyboard IFS « Du mail au parquet »
date: 2026-10-03
fichiers: STORYBOARD.md, frame.md, reference/fil.html
---

# Grille de contrôle du storyboard

Verdicts : **tenu**, **tenu après correction** (écart trouvé par la grille et corrigé dans STORYBOARD.md), **non
tenu** (écart restant, avec sa raison). Temps locaux à la séquence sauf mention « global ».

## Vérifications mécaniques

- Durées : 11 séquences, somme 52.00 s, égale à `TOTAL` de build-audio.sh et à la durée du montage voix (52.00 s).
- Passages de relais : les 10 coutures ont un `handoff_out` identique caractère pour caractère au `handoff_in` suivant,
  y compris les deux coupes franches (15.20 et 37.45 global), qui portent leur raccord de position des deux côtés.
- Paquets des sous-agents (`frame-packets.mjs`) : 11 paquets de 23,0 à 45,7 Ko, tous sous la limite de 48 Ko. La
  séquence 5 dépassait (51,2 Ko avec cursor-ui-demo et cursor-drag) : passée en spatial-pan-stations avec
  svg-path-draw et cursor-click-ripple.
- Recettes : tous les blueprints et règles cités existent dans `hyperframes-animation/`.
- Référence exécutable `reference/fil.html` : rendue dans Chromium sans erreur JavaScript (monde W1, monde W2,
  stickman en pose 'smash', aiguille du pivot).
- Typographie : aucun tiret cadratin ni demi-cadratin dans STORYBOARD.md et frame.md.

## Grille de STORYBOARD-CRAFT.md § 5

1. **En-tête complet** (monde et coordonnées, sols texturés, couleurs de rôle, 2 signatures datées, registres de
   texte) : tenu.
2. **Piste caméra dans chaque plan, jamais à l'arrêt plus de 0,5 s hors silence écrit** : tenu (dérive chiffrée dans
   les 19 blocs de plans, qui couvrent les plans P1 à P32, y compris le noir du pivot qui dérive en échelle).
3. **Aucun trou de plus de 1 s, 0,3 s dans les 3 premières secondes** : tenu après correction. Séquence 1 : trous de
   0,50 s (1.10 → 1.60) et 0,34 s (1.96 → 2.30) comblés par 1.36 (la carte accélère sur le fil) et 2.10 (elle sort du
   cadre). Séquence 10 : trou de 1,86 s (1.96 → 3.82) comblé par 2.40 (cran), 2.96 (vague du fil), 3.40 (reflet).
   La carte de fin (séquence 11, 1.40 à 4.60) est le silence écrit 48.24 à 52.00 global, tenu par sa couche vivante.
4. **Apparitions ≤ 0,2 s, dérives ≥ 1 s, zone 0,3 à 0,9 s réservée à la caméra et au curseur** : tenu avec une
   exception écrite : le tracé du fil (signature 1) dure 0,3 à 0,7 s ; il se comporte comme un curseur (sa tête mène,
   courbe expo.out) et la caméra le suit. La course du joueur (séquence 9, 0,6 s) est rangée dans le même cas.
5. **Chaque tenue nomme sa couche vivante** : tenu (dérives, fil qui ondule, tambour qui tourne, jambes du joueur
   suspendu qui se balancent).
6. **Chaque jonction nomme son objet-pont ou son vecteur, aucun dédoublement** : tenu. Objets-ponts : la carte du mail
   sur le fil, le fil qui file vers la salle, le nœud, le fil pâli, le bout du fil (coupe 15.20 global), le point de
   lumière, l'enveloppe, le tampon, la ligne de coupe, le fil qui ressort du tissu, la ficelle (coupe 37.45 global),
   le brin rouge du filet, l'aiguille et son fil.
7. **Transitions « effet » : 2 au plus** : tenu (2 : l'éclair de lumière de 18.70 global, le fondu au noir final).
8. **Coupes franches au quota de la voix narrative, chacune justifiée** : tenu (2 : 15.20 global sur « On », pivot ;
   37.45 global sur « Samedi », le jour du match).
9. **Chaque entrée d'élément principal a un état de départ écrit** : tenu après correction (l'entraîneur de la
   séquence 2 entrait sans état : ajouté ×1,15 flou 6 → net en 0,14 s).
10. **Mots-images en avance de 0,1 à 0,6 s, changements de plan sur le premier mot ou dans un silence, silences
    > 0,4 s écrits comme des plans** : tenu après correction. Trois images arrivaient en même temps que leur mot :
    l'aiguille de la couture (avancée à 0.20 pour « confection » 0.38), le nuancier du match (2.80 pour « rouge »
    3.03), l'icône IFS (0.12 pour « IFS » 0.29). Le BAT se pose 0,78 s avant « BAT » : gardé, c'est le sujet du plan
    depuis son premier mot (« Vous »). Les 8 silences de plus de 0,4 s sont des plans avec leur action muette.
11. **Au moins 3 verbes joués par un objet** : tenu (commandez : clic sur Envoyer ; décolle : le fil tire le coin du
    1 ; reprend : le fil renfilé ; validez : le tampon frappe ; coupe : la lame suit le fil ; fixe : la presse ;
    assemble : les bords de l'emmanchure se rejoignent ; livrés : le carton se ferme ; monte : le smash).
12. **La moitié des plans sur 3 niveaux, une parallaxe par acte** : tenu après correction. 3 niveaux écrits dans
    16 blocs de plans sur 19 (les 3 autres sont le pivot sur le noir et le bouton final, voulus dépouillés) ; la parallaxe n'était pas chiffrée : ajoutée dans l'en-tête (avant-plan ×2,5, fond ×0,4, avec
    les objets de chaque acte). Aucun mot géant dans le film.
13. **Couches animées : courant ≥ 2, pic 3 à 4, un seul élément actif** : tenu.
14. **Rime** : tenu (l'aiguille du pivot est celle du logo final ; le nuancier de la douleur revient contre le
    maillot ; la fenêtre de message de juin revient adressée à IFS ; les chasubles reviennent en maillot).
15. **Fin : un geste qui rassemble, curseur en courbe et clic direct, 2 à 3 s de tenue vivante, sortie au noir** :
    tenu avec une réserve. Le geste qui rassemble est le fil, qui a relié toutes les stations, rentrant dans le chas
    du logo ; la tenue vivante dure 3,2 s (1.40 à 4.60 de la séquence 11), soit 0,2 s au-dessus de la cible, gardée
    pour laisser le temps de lire l'URL.

## Grille de contrôle de SKILL.md

- Première image = le premier mot (« Juin » : la page JUIN et le mail de commande), jamais le logo : tenu.
- Chaque phrase a sa composition, sous-titre mot à mot en bas au centre : tenu.
- Un mot clé par phrase dans la boîte accent ; 4 pics soulignés ; aucun mot géant : tenu. La phrase du pivot n'a pas
  de boîte (moment typographique centré, trait sous « début »).
- Une seule chose à regarder, côte à côte aux marges égales (maillot délavé et nuancier ; dos du maillot et
  nuancier), aucun décor sans sens : tenu.
- La douleur dans des outils que la cible connaît (message à la mise en page Outlook, suivi de commande, calendrier) :
  tenu.
- Pivot explicite sur noir avec silence, le sol change (encre → noir → papier) : tenu.
- Logo complet pas avant 5 s (42.49 global) : tenu. Le petit logo dans l'en-tête du vrai studio (21.3 global) fait
  partie de l'interface réelle.
- Coupes franches au quota (2), 0 à 2 fondus (2), tout le reste par objet ou caméra, aucun aller-retour de caméra :
  tenu après correction. Séquence 9 : la caméra montait vers le cercle puis redescendait sur le maillot ; le joueur
  reste désormais suspendu au cercle et la caméra continue de pousser, sur son dos, dans le même sens.
- Chaque nombre roule ou fonce depuis la caméra : tenu (l'étiquette « moins d'un mois » fonce depuis la caméra ; le 15
  est un objet imprimé du maillot, pas un compteur).
- Le produit montré par des gestes dans sa vraie interface (studio IFS : le maillot se construit, l'écusson se dépose,
  l'onglet Logos s'active) : tenu.
- Un élément de l'accroche revient avant la fin (la fenêtre de message, le rouge, les joueurs) : tenu.
- Carte de fin : un bouton, curseur en courbe, clic direct, tenue vivante, noir : tenu.
- Lisible sans le son : tenu.
- Quelque chose de neuf toutes les 0,5 à 1 s, jamais la même mise en page plus de 3 s : tenu après correction
  (séquence 10, voir point 3 ; le bloc logo bouge à 4.26 pour accueillir le bouton).
- Points de rendu (letterSpacing, sol sous le monde clair, segments noirs, niveau de la musique) : à contrôler à
  l'étape 6.

## Règles maison

- Sous-titres en bas au centre, 62 px, 45 signes au plus par morceau : tenu (phrases longues coupées en morceaux :
  séquences 3, 7, 10).
- Anonymisation des mails (SOURCES.md) : tenu, seuls « Basket Club Eschau », « Fournisseur textile » et « IFS »
  apparaissent ; aucune adresse, aucun nom, aucun prix, aucune quantité.
- Aucune mesure de taille, aucun délai autre que « moins d'un mois », aucune mention « fabriqué en France » : tenu.
- Joueur au modèle validé par Antoine (silhouette noire détourée de blanc, maillot et short dessinés) : tenu.
