---
version: 2
name: "IFS · Du mail au parquet : charte du film"
description: >
  Charte image du film de lancement IFS (52 s, 16:9, voix off Paul K), direction A « Le fil rouge » de DIRECTIONS.md.
  Un seul fil rouge, celui de l'aiguille du logo IFS, court du mail au panier et relie toutes les étapes.
  Deux mondes : la DOUCEUR manquée vit sur l'encre (#1A1320), la SOLUTION sur le papier blanc de l'atelier ; le match
  et la carte de fin reviennent sur l'encre. Un seul accent, le magenta IFS, réservé à la boîte du mot clé de chaque
  sous-titre, aux 4 traits des pics et au bouton final. Le rouge du club est la couleur du fil et du maillot, jamais du texte.
  Code commun exécutable : reference/fil.html (copié tel quel par chaque séquence).
unit: 1920×1080
principle: lisible sans le son · une seule chose à regarder · un seul accent, une seule mise en valeur · la voix déclenche chaque révélation

colors:
  canvas: "#1A1320"          # monde sombre (douleur, match, carte de fin)
  canvas-2: "#110C15"        # bord du vignettage sombre
  paper: "#FFFFFF"           # monde clair (l'atelier)
  paper-2: "#F4F0F3"         # surfaces claires secondaires (tapis, fond du studio)
  card-light: "#FFFFFF"
  ink: "#F5EFF3"             # texte sur sombre
  ink-soft: "#C8BCC5"
  ink-mute: "#A89BA5"
  ink-dark: "#1A1320"        # texte sur clair
  ink-dark-soft: "#5E5360"
  hairline-light: "#E7E0E5"
  accent: "#B3125F"          # magenta IFS (catalogue)
  accent-light: "#C2186B"
  accent-deep: "#940E4E"
  accent-glow: "#FF7DBA"     # trait des pics sur le sombre
  thread: "#D62839"          # le fil rouge et le rouge du club (rôle objet, jamais texte)
  thread-faded: "#E8823A"    # le rouge « viré à l'orange » de la douleur
  stickman: "#0d0a10"        # joueurs et entraîneur : silhouette noire détourée de blanc (validé par Antoine le 03/10/2026)

fonts:
  Archivo: { files: ["assets/fonts/archivo-latin.woff2 (700 à 900, stretch 75 à 100 %)", "assets/fonts/archivo-latin-ext.woff2"] }
  Hanken Grotesk: { files: ["assets/fonts/hanken-grotesk-latin.woff2 (400 à 700)", "assets/fonts/hanken-grotesk-latin-ext.woff2"] }

typography:
  subtitle:   { fontFamily: "Hanken Grotesk", px: 62, weight: 600, lineHeight: 74, tracking: "-0.015em", note: "la phrase de la voix EN BAS AU CENTRE (haut à y 896, dans la bande y 890 à 980 qui ne porte rien d'autre), 45 signes au plus par morceau (une phrase plus longue se coupe en morceaux qui se remplacent), mot par mot sur ses temps ; ombre légère ; encre sombre sur le papier, ink sur l'encre. Jamais en haut à gauche" }
  type:       { fontFamily: "Archivo", px: 84, weight: 800, stretch: "85%", lineHeight: 1.08, tracking: "-0.01em", note: "SEUL moment typographique : le pivot « On reprend depuis le début. » (séquence 4), centré, 84 px au plus, sans sous-titre en bas pendant ce temps" }
  ui:         { fontFamily: "Hanken Grotesk", px: 22, weight: 500, lineHeight: 1.35, note: "textes des vraies interfaces (mail, studio, suivi, BAT)" }
  title:      { fontFamily: "Archivo", px: 92, weight: 900, stretch: "80%", note: "titres imprimés du décor seulement : SEPTEMBRE, JUIN, BAT" }
  label:      { fontFamily: "Hanken Grotesk", px: 18, weight: 700, tracking: "0.08em", upper: true, note: "micro-étiquettes des interfaces (SUIVI DE COMMANDE, GRILLE IFS)" }
  wordmark:   { fontFamily: "Archivo", px: 72, weight: 900, stretch: "85%", note: "« IFS » à côté de l'icône du logo, puis « Industrie Française de Sellerie » en Hanken 26 px 600 ink-soft" }
  cta:        { fontFamily: "Hanken Grotesk", px: 30, weight: 700 }

components:
  ground-dark:
    background: "canvas + rayures diagonales 115° (blanc 2,8 %, 2 px tous les 46 px) qui rendent la dérive lisible + halo radial #241B2B derrière le sujet + vignettage vers canvas-2 + grain 5 %. Calque class=\"clip\" de toute la séquence, jamais sur #root."
  ground-paper:
    background: "paper + rayures diagonales 115° magenta à 5 % (2 px tous les 46 px) + dégradé vertical vers #F7F3F6 + grain 3 %. Calque class=\"clip\"."
  ground-gym:
    background: "salle de nuit : radial #3a2f45 → canvas, 3 projecteurs flous (radial #fff6e6, flou 14 px) en haut, parquet en perspective (rotateX 62°, lattes #b07a46 / #a46f3d / #b8834f) assombri vers le haut, ligne de terrain #f2ede6 à 55 %. Fonction groundGym() de reference/fil.html."
  thread (LE fil rouge, objet-pont du film):
    look: "trait SVG thread #D62839, 5 px (6 à 8 px en gros plan), bouts ronds, un reflet blanc à 35 % en pointillé 2/9 par-dessus en gros plan. Un seul fil par monde, tracé par threadPath(monde) de reference/fil.html : la courbe passe par l'ancre de chaque station."
    motion: "il se DESSINE (stroke-dashoffset de la longueur vers 0, signature 1 « le fil trace »), jamais il n'apparaît en fondu ; sa tête avance au rythme de la caméra ; il peut pâlir vers thread-faded (douleur), se nouer (nœud dessiné par knotPath), devenir le filet, la couture, la ficelle du carton."
  needle:
    look: "l'aiguille du logo IFS : fuseau gris acier (dégradé #3C4452 → #8A93A1 → #4A5260), chas ovale, pointe fine ; 520 px de long au pivot, 150 px sur la carte de fin. Fonction needle() de reference/fil.html."
  word-by-word:
    rule: "chaque mot du sous-titre paraît SUR son temps, gris (encre à 35 %) : fromTo {opacity:0, y:8, filter:blur(6px)} → {opacity:1, y:0, blur(0)} en 0,14 s, immediateRender:false, puis passe à l'encre pleine en 0,2 s. Avant une couture, il sort : opacité 1 → 0 et flou 0 → 6 px en 0,14 s."
  key-word-box (LA mise en valeur, une par phrase):
    look: "petit rectangle accent, angles nets (3 px), qui déborde le mot de 0,14 em de chaque côté ; le mot passe au blanc dedans. Jamais une boîte noire."
    motion: "la boîte se trace depuis la gauche (scaleX 0 → 1, origine à gauche, 0,16 s power3.out), 0 à 2 images avant le mot ; le mot change de couleur au passage (0,1 s)."
    rule: "UNE boîte par phrase, sur le mot nommé [boîte : …]. Aucun autre texte coloré."
  peak-stroke (4 pics du film):
    look: "trait de pinceau effilé accent (accent-glow sur le sombre) sous LE mot clé seulement, attaque ronde, sortie fine, courbe légèrement montante, 7 px."
    motion: "se dessine depuis la gauche (scaleX 0 → 1, 0,4 s power2.out) pendant que le mot est dit."
    rule: "nommé [trait : …] dans le storyboard : « premier match » (3.90), « début » (16.54), « moins d'un mois » (36.60), « resté » (41.14). Jamais une grosse boîte ni un mot géant."
  mail-window:
    description: "fenêtre de nouveau message à la mise en page Outlook web, redessinée en HTML (jamais une capture) : barre bleue #0F6CBD « Nouveau message », bouton Envoyer bleu, lignes À et Objet, une pièce jointe Excel (pastille verte #1D6F42 « X »), corps court. ANONYMISÉE (SOURCES.md) : destinataire « Fournisseur textile » (séquence 1) ou « IFS » (séquence 5), expéditeur « Basket Club Eschau », objet « Commande maillots · saison 2026 », pièce jointe « Commande maillots 2026.xlsx », corps « Bonjour, voici notre commande de maillots pour la saison. ». Aucune adresse, aucun nom de personne, aucun prix, aucune quantité."
  tracking-card:
    description: "carte sombre #2B232E, rayon 18 px : étiquette « SUIVI DE COMMANDE », titre « Maillots · Basket Club Eschau », 4 étapes (2 allumées en spark #FFE45C), état « En cours d'acheminement » en spark. Aucune marque de transporteur. Seule exception au jaune : cet état (repris du jaune du catalogue)."
  calendar:
    description: "page de calendrier murale papier #FBF8F5, spirale de 4 anneaux, titre Archivo « SEPTEMBRE 2026 », grille L à D, le samedi 5 entouré au feutre thread avec « 1er match » écrit au-dessus (détail inventé, assumé : l'accroche est un scénario). Page « JUIN » identique qui s'envole."
  studio:
    description: "le vrai studio de personnalisation IFS (site/personnaliser.html du dépôt ifs-catalogue, capture du 03/10/2026 dans _references/ifs/studio-basket.png), reconstruit en HTML : en-tête logo IFS + « Studio de personnalisation » + « Industrie Française de Sellerie », sélecteur « Maillot basketball double face (réversible) », canevas #F4F0F3 avec bandes diagonales, onglets Produit / Logos / Textes (Logos actif, souligné accent), zone « Déposez votre logo ici », bouton accent « Demander un devis avec ce visuel », bandeau « Aperçu indicatif. … BAT officiel ». Le maillot du canevas est la photo détourée assets/img/maillot-face-rouge-noir-detoure.png."
  bat-sheet:
    description: "feuille A4 blanche « BAT » (Archivo 92 px) avec les deux vues du maillot (face : maillot-face-rouge-noir-detoure.png, dos : maillot-dos-detoure.png) côte à côte, petite légende « Basket Club Eschau · saison 2026 ». Tampon carré accent « VALIDÉ » qui frappe (×1,6 flou 8 → net en 0,08 s, rotation -8°) : c'est la coche tracée par le fil qui devient le tampon."
  size-grid:
    description: "carte blanche « GRILLE IFS » / « Tailles standardisées » avec 6 pastilles XS S M L XL 2XL (M en accent). Tailles seules, AUCUNE mesure (aucune n'a été fournie). Sur le tapis de coupe : patrons de débardeur gradés (M tracé en accent, les autres en pointillé #C8BCC5)."
  cutter:
    description: "cutter rotatif vu de dessus : lame ronde acier 120 px, manche accent (dégradé #B3125F → #940E4E) ; il suit la ligne du fil sur le patron M."
  press:
    description: "plaque de presse à chaud en avant-plan haut, floue (13 px), dégradé acier #3d3940 → #c9c5cc, lueur chaude ; la maille blanche du tissu en macro (points 22 px) ; le motif réel du maillot (maillot-face-rouge-noir-detoure.png) apparaît dans la fibre en halo depuis le point où le fil plonge."
  stitch:
    description: "couture : le fil devient une ligne de points droits (traits de 14 px, pas de 22 px) qui ferme l'emmanchure du maillot plat ; l'aiguille du logo pique à chaque point."
  shipping-box:
    description: "carton kraft vu de dessus (dégradé #d2a874 → #b5844f), papier de soie #fbf6f0, le maillot plié détouré (maillot-plie-detoure.png), étiquette blanche « Livré · moins d'un mois » ; le fil fait la ficelle qui ferme le carton."
  stickman:
    description: "joueurs et entraîneur en bonhomme bâton, sur le modèle validé par Antoine (styleframes/png/A3.png) : silhouette noire #0d0a10, membres en traits de 22 px à bouts ronds avec un liseré blanc flou (trait blanc 30 px à 55 %, flou 2,2 px) dessous, tête disque de 124 px cerclée de blanc à 75 %, poings en disques de 34 px. Aucun visage. Le joueur du match porte un maillot et un short DESSINÉS et ajustés au corps (vecteur, pas la photo) : dos rouge #DC2A2F, épaules noires #15151C, ourlet noir, hachures latérales, « 15 » en Archivo 900 75 % encre au liseré gris #a9aeb6, « Contino » en Pacifico blanc, « SPORT » en Hanken 700 italique blanc ; short rouge à bandes latérales noire et blanche. Les joueurs du gag portent une chasuble grise unie #6d6670. Poses dans stickman(pose) de reference/fil.html : 'echauffement', 'attente', 'telephone', 'saut', 'smash'."
  hoop:
    description: "panier : planche blanche 560 × 340 px bord #f4f0f3, carré intérieur, cercle orange #E8662B (avant) / #a5461a (arrière) avec sa platine, poteau et bras acier de trois quarts à droite ; filet blanc #f4f2f5 en losanges (12 brins, 4 rangs, trait 3,2 px) dont UN brin est le fil rouge (le fil devient le filet)."
  ball:
    description: "ballon 150 px, radial #f39a5a → #d9621f → #9c3d0e, coutures #2a1408."
  swatch:
    description: "nuancier blanc 330 × 470 px, pastille thread en haut, « Rouge club » Archivo 30 px, « BAT validé » Hanken 18 px. Il apparaît dans la douleur à côté du rouge délavé, et revient sur le terrain contre le maillot (rime)."
  logo:
    description: "icône IFS (assets/img/logo-ifs.svg, 150 px, rayon 30 px) + wordmark. Sur la carte de fin, le fil rouge rentre dans le chas de l'aiguille de l'icône."
  cursor:
    description: "flèche macOS blanche, contour encre, ombre ; arrive en UN mouvement courbe (0,4 à 0,5 s power3.out) et clique directement : pression (×0,85, 0,06 s) + onde accent qui s'ouvre et s'efface. Jamais d'hésitation."
  end-card:
    description: "sol d'encre, icône IFS et wordmark, la promesse « Une qualité irréprochable, livrée en moins d'un mois. » en sous-titre, UN bouton accent « Voir le catalogue », URL « catalogue-ifs.netlify.app » en Hanken 24 px ink-soft, un curseur qui arrive et clique, puis 2 à 3 s de tenue vivante (dérive, le fil qui ondule) avant le noir."

world:
  camera: "kit de reference/fil.html : #stage > #drift > #cam > #world ; cam(x, y, s) amène le point (x, y) du monde au centre du cadre (960, 540) à l'échelle s. Dérive permanente sur #drift (10 à 30 u/s ou 1 à 3 %/s d'échelle), crans et whips sur #world et #cam (expo.inOut, flou 6 à 12 px au milieu). Toutes les séquences d'un même monde copient le même kit et le même threadPath."
  W1-attente (douleur, sombre, séquences 1 à 3, 0 à 15.20):
    size: "12 000 × 1 080 u, sol ground-dark"
    stations: "S1 fenêtre de message (960, 470) · S2 calendrier (3000, 470) · S3 salle du club, échauffement en chasubles + carte de suivi sur le téléphone de l'entraîneur (5400, 500) · S4 carton ouvert : maillot délavé + nuancier (7800, 470) · S5 hublot de machine à laver (10000, 470)"
    thread: "threadPath('W1') : part du bouton Envoyer de S1 (720, 230 dans la fenêtre → monde (650, 300)), ondule en y 640 ± 70 entre les stations, passe par le 5 entouré de S2 (3150, 420), s'emmêle en nœud au pied de S3 (5400, 760 : knotPath), pâlit en thread-faded à partir de S4, finit accroché au coin du 1 du numéro dans S5 (9920, 380)."
  pivot (séquence 4, 15.20 à 18.70): "noir canvas-2 pur ; l'aiguille entre par la gauche, le fil (redevenu thread) la suit ; la phrase centrée en type. Aucun décor."
  W2-atelier (solution, clair, séquences 5 à 8, 18.70 à 37.45):
    size: "15 000 × 1 080 u, sol ground-paper"
    stations: "S6 enveloppe tracée + fenêtre de message vers « IFS » (960, 470) · S7 studio IFS (3200, 470) · S8 BAT + tampon (5400, 470) · S9 tapis de coupe + grille de tailles (7600, 470) · S10 presse et maille en macro (9800, 470) · S11 couture (12000, 470) · S12 carton d'expédition (14200, 470)"
    thread: "threadPath('W2') : sort du chas de l'aiguille (0, 540), trace l'enveloppe de S6, contourne le maillot dans S7, fait la coche du BAT dans S8 (devient le tampon), suit le contour du patron M dans S9, plonge dans le tissu dans S10, devient la couture dans S11, la ficelle du carton dans S12."
  W3-match (sombre, séquence 9, 37.45 à 42.20): "salle ground-gym, panier à droite (planche en (1480, 210)), le joueur stickman n° 15 qui smashe ; le filet est tracé par le fil ; le nuancier revient contre le maillot."
  W4-fin (sombre, séquences 10 et 11, 42.20 à 52.00): "sol ground-dark ; le fil quitte le filet, traverse le cadre et rentre dans le chas de l'aiguille du logo IFS (rime du pivot) ; promesse, bouton, curseur, URL."
  framings: "cadrages de référence (marges gauche et droite égales) : S1 cam(960, 500, 1.0) · S2 cam(3000, 500, 1.05) · S3 cam(5400, 520, 0.95) · S4 cam(7800, 480, 1.1) · S5 cam(10000, 470, 1.25) · S6 cam(960, 480, 1.0) · S7 cam(3200, 470, 0.95) · S8 cam(5400, 470, 1.05) · S9 cam(7600, 470, 1.0) · S10 cam(9800, 470, 1.4) · S11 cam(12000, 470, 1.2) · S12 cam(14200, 470, 1.0)"

negative:
  - "Aucune seconde mise en valeur : la boîte accent est la SEULE façon de souligner un mot du sous-titre, le trait marque les 4 pics (aucun texte coloré, aucun texte lumineux)."
  - "Aucune grande phrase : sous-titre 62 px, moment typographique 84 px au plus ; aucun mot géant, aucune grosse boîte. Rien d'autre que le sous-titre dans la bande y 890 à 980 ; jamais de sous-titre en haut à gauche."
  - "Une seule chose à regarder : la caméra isole le sujet de la phrase. Mises en page côte à côte aux marges égales."
  - "Jamais d'aller-retour de caméra sur le décor (le travelling va toujours de gauche à droite dans un monde). Jamais d'hésitation du curseur."
  - "Aucun décor sans sens, aucun symbole abstrait, aucun compteur ; le fil ne traverse JAMAIS une phrase (il reste au-dessus de y 860 et passe derrière le texte des interfaces)."
  - "Aucune teinte hors charte : accent magenta, rouge du fil et du club, jaune spark seulement dans la carte de suivi, couleurs réelles des interfaces (bleu Outlook, vert Excel, orange du ballon et du cercle)."
  - "Aucune donnée réelle des mails : ni adresse, ni nom de personne, ni téléphone, ni prix, ni quantité (SOURCES.md)."
  - "Aucune mesure de taille, aucun délai chiffré autre que « moins d'un mois », aucune mention « fabriqué en France »."
  - "Pas d'Inter, Space Grotesk, Geist, system-ui. Pas d'emoji."
  - "Pas d'ease rebondissant ni élastique ; pas de boucle infinie (repeat:-1) ; pas de poussée lente sur chaque plan."
  - "Aucun texte visible qui ne soit pas cité dans les lignes Scene ou dans les interfaces ci-dessus."
  - "Jamais d'animation de letterSpacing."
---

# IFS · Du mail au parquet : charte du film

Le film a trois lieux et un seul objet. **La douleur** se joue sur l'encre : le mail de juin part, le fil traîne le
long du calendrier jusqu'au premier match, s'emmêle pendant que l'équipe s'échauffe en chasubles, pâlit quand les
maillots arrivent délavés et finit accroché au numéro qui se décolle. Au **pivot**, dans le noir, l'aiguille du logo
IFS traverse le cadre et renfile le fil : « On reprend depuis le début. » La lumière ouvre **l'atelier**, sur le papier
blanc : le fil trace le mail à IFS, le design dans le vrai studio, la coche du BAT, le patron sur la grille de tailles,
plonge dans le tissu sous la presse, devient la couture puis la ficelle du carton. **Le match**, dans la salle de
nuit : le joueur n° 15 smashe, le filet est le fil. **La fin** : le fil rentre dans le chas de l'aiguille du logo, la
promesse, le bouton, le clic.

Tout ce qu'on lit est en Hanken Grotesk : la phrase de la voix en sous-titre en bas au centre, mot par mot, avec un
seul mot clé par phrase dans une petite boîte magenta qui se trace d'abord. Un trait de pinceau magenta marque les 4
pics. Archivo sert aux titres imprimés du décor (SEPTEMBRE, BAT), au moment typographique du pivot et au wordmark.
