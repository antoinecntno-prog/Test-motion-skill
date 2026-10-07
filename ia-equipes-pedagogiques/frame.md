---
version: 2
name: "Antoine Contino, formateur IA · Le carnet, la salle des profs : charte du film 2"
description: >
  Charte image du film « Formation IA pour les équipes pédagogiques » (52,0 s, 16:9, voix off Paul K), direction A
  « Le carnet » héritée du film 1 (DIRECTIONS.md). Le carnet d'un enseignant : huit pages côte à côte que la caméra
  parcourt de gauche à droite, chaque page une scène peinte à l'aquarelle sur papier crème. La douleur est lavée de
  gris : la salle des profs vide un lundi soir, le tableau qui se change en grille ; le pivot est le noir de l'encre ;
  après lui, les pages se colorent (la salle pleine, le bulletin, le mail, la grille, les élèves qui reviennent).
  Une seule mise en valeur du texte, la boîte bordeaux du mot clé ; 4 traits de pinceau ocre sous les pics.
  Code commun exécutable : reference/aquarelle.html (copie conforme du kit du film 1, copié tel quel par chaque séquence).
unit: 1920×1080
principle: lisible sans le son · une seule chose à regarder · un seul accent, une seule mise en valeur · la voix déclenche chaque révélation

colors:
  paper: "#F4EBDD"           # la page du carnet (monde clair, 11 séquences sur 12)
  paper-2: "#EDE1CF"         # page voisine, floue, et reliure
  paper-dark: "#E6D8C2"      # le bureau sous le carnet (hors des pages)
  canvas: "#17110F"          # le noir du pivot (l'intérieur de la goutte d'encre)
  canvas-2: "#0F0A09"        # bord du vignettage du pivot
  ink: "#3A2A24"             # encre brune : traits, texte sur le papier
  ink-2: "#6B5A52"           # encre diluée : textes secondaires, lignes des pages
  ink-light: "#9C8C83"       # encre très diluée : lignes grises, note séchée
  ink-paper: "#F4EBDD"       # texte sur le noir (pivot)
  accent: "#7A1E2E"          # bordeaux : LA boîte du mot clé, la goutte signature, la signature finale
  accent-light: "#9B2F3F"    # bordeaux clair : stylo rouge, traînée de la goutte
  accent-pale: "#C98A93"     # bordeaux pâle : lavis de la douleur, équipe bordeaux en lavis
  ocre: "#C98A2E"            # LA couleur qui revient : traits des pics, tables, équipe ocre, bouton final
  ocre-2: "#E0A84A"          # ocre clair : lueur de la lampe allumée
  ocre-pale: "#EFD7A6"       # ocre pâle : lavis larges de la solution
  gris-lavis: "#A99F95"      # gris de la douleur : la copie, l'eau sale
  gris-lavis-2: "#8E847A"    # gris plus dense : encre de la réponse copiée
  brun: "#B99A74"            # bois : bureau, tables

# Fichiers woff2 locaux seulement (assets/fonts/, fontsource) ; aucun @import réseau.
fonts:
  Fraunces: { files: ["assets/fonts/fraunces-latin-400-normal.woff2 (400)", "assets/fonts/fraunces-latin-600-normal.woff2 (600)", "assets/fonts/fraunces-latin-700-normal.woff2 (700)"] }
  DM Sans: { files: ["assets/fonts/dm-sans-latin-400-normal.woff2 (400)", "assets/fonts/dm-sans-latin-500-normal.woff2 (500)", "assets/fonts/dm-sans-latin-600-normal.woff2 (600)", "assets/fonts/dm-sans-latin-700-normal.woff2 (700)"] }
  Caveat: { files: ["assets/fonts/caveat-latin-400-normal.woff2 (400)", "assets/fonts/caveat-latin-600-normal.woff2 (600)"] }

typography:
  subtitle:   { fontFamily: "DM Sans", px: 62, weight: 600, lineHeight: 74, tracking: "-0.005em", note: "la phrase de la voix EN BAS AU CENTRE (haut à y 896, bande y 890 à 980 qui ne porte rien d'autre), 45 signes au plus par morceau (une phrase plus longue se coupe en morceaux qui se remplacent), mot par mot sur ses temps ; encre ink sur le papier, ombre papier légère (0 2px 14px paper à 80 %). Jamais en haut à gauche" }
  type:       { fontFamily: "Fraunces", px: 84, weight: 600, lineHeight: 1.1, tracking: "-0.01em", note: "SEUL moment typographique : le pivot « Et si vous repreniez ce temps ? » (séquence 6), centré sur le noir en ink-paper, 84 px au plus, sans sous-titre en bas pendant ce temps ; trait ocre sous « temps »" }
  note:       { fontFamily: "Caveat", px: 34, weight: 600, lineHeight: 1.2, note: "les notes manuscrites des pages du carnet, en ink-2 (« lundi, 18 h », « Séquence 3 », « classe A », « classe B », « critère », « acquis », « en cours », « vos documents », « vos outils »), légèrement penchées (-3 à 3°) ; aucune note chiffrée dans ce film" }
  ui:         { fontFamily: "DM Sans", px: 22, weight: 400, lineHeight: 1.35, note: "le texte des fenêtres dessinées (objets des mails, lignes du mail) ; étiquettes 16 px 600 espacées de 0,08 em (BOÎTE DE RÉCEPTION, NOUVEAU MESSAGE)" }
  title:      { fontFamily: "Fraunces", px: 72, weight: 600, tracking: "-0.02em", note: "aucun titre imprimé dans ce film ; réservé" }
  craie:      { fontFamily: "Caveat", px: 40, weight: 600, note: "l'écriture à la craie sur le tableau (page 2) : traits paper à 85 % tracés à main levée (aqInk, couleur paper, 6 px), sans mot lisible" }
  signature:  { fontFamily: "Caveat", px: 120, weight: 600, note: "« Antoine Contino » tracé à l'encre accent sur la page 8 (chemin SVG qui se dessine, aucune apparition en fondu), puis « formateur IA » en DM Sans 34 px 600 ink-2 dessous" }
  cta:        { fontFamily: "DM Sans", px: 32, weight: 700, note: "« Réserver un appel » en ink sur le bouton ocre ; dessous « calendly.com/antoine-cntno/30min · antoinecontino.fr/ecoles » en DM Sans 24 px 500 ink-2" }

components:
  ground-paper:
    background: "le bureau paper-dark sous le carnet (grain .aq-grain à 55 % en multiply + fibres à 35 %), les pages paper posées dessus avec une ombre douce (0 18px 40px ink à 14 %), la reliure .aq-spine entre deux pages (dégradé ink à 0 → 28 % → 0 sur 34 u). Calque class=\"clip\" de toute la séquence, jamais sur #root. Le grain rend la dérive lisible."
  ground-ink (pivot):
    background: "canvas, vignettage radial vers canvas-2, ondes concentriques très sombres (ink à 6 %) qui s'élargissent lentement : l'intérieur de la goutte d'encre. Calque class=\"clip\"."
  wash (la tache d'aquarelle):
    look: "chemin SVG organique (aqBlob : 7 à 12 sommets, ondulation 0,1 à 0,3) rempli d'une couleur de rôle, filtre #aq (turbulence + déplacement 46, anneau de bord foncé, granulation), mix-blend-mode multiply, opacité 0,3 à 0,9 ; #aq-soft pour un lavis large. Déterministe : un seed par tache, jamais Math.random."
    motion: "une tache n'apparaît jamais en fondu : elle naît d'une goutte (signature 1) ou d'un coup de pinceau (scaleX 0 → 1 depuis la gauche, 0,2 s expo.out) ; elle sèche (signature 2) ; elle s'efface par le centre (clip-path circle 100 % → 0 en 0,3 s power2.in, « séchage inversé »)."
  ink-stroke:
    look: "trait d'encre ink à main levée : stroke 3 à 7 px, bouts ronds, filtre #ink (déplacement 5). Sert au portable, à la lampe, au stylo, au chronomètre, aux tables vues de côté, aux cadres des fenêtres."
    motion: "il se DESSINE (svg-path-draw : stroke-dashoffset de la longueur vers 0, 0,2 à 0,5 s power2.out), jamais il n'apparaît en fondu."
  drop (signature 1, « la goutte ») :
    look: "une goutte de 12 à 46 u (aqDrop : tache ronde à 7 sommets, opacité 0,85) de la couleur de l'idée : accent (encre), gris-lavis (eau sale de la douleur), ocre (la couleur qui revient)."
    motion: "aqDropFall : elle arrive de la caméra (×4, flou 10 px, 0,25 s power2.in) ou tombe du haut (y -500 → 0, 0,16 s power2.in), touche la page (impact : la tache s'ouvre ×0,2 → ×1 en 0,12 s expo.out, 2 éclaboussures de 6 u à ±60 u), puis sèche en objet (signature 2). Elle revient 9 fois dans le film (STORYBOARD.md, SIGNATURES)."
  dry (signature 2, « le séchage ») :
    motion: "aqDry(g, k) : k 0 → 1 en 0,4 à 0,8 s power1.inOut ; l'anneau de bord fonce (opacité du ring 0 → 1), la granulation paraît, la tache se rétracte de 4 % ; à k = 1 l'objet dessiné dedans (fenêtre, table, note, bouton) est net. Inverse (effacement) : la couleur pâlit vers gris-lavis puis la tache s'efface par le centre."
  figure:
    description: "silhouette peinte en taches, sans visage (aqFigure) : buste en dôme + tête ronde, 170 à 210 u de haut, vue de dos ou de trois quarts, poses 'dos', 'penche', 'bras-leve'. Couleur ocre (équipe ocre) ou accent (équipe bordeaux). Un étudiant = une figure ; les mêmes gabarits dans les trois films."
  mail-inbox:
    description: "boîte de réception GÉNÉRIQUE dessinée à l'encre dans l'écran du portable (aqWindow 560 × 330, barre, étiquette « BOÎTE DE RÉCEPTION ») : 5 à 7 lignes d'objets en DM Sans 20 px ink-light, sans expéditeur ni nom : « Objet : absence de lundi », « Objet : réunion de rentrée », « Objet : sortie du 12 », « Objet : rendez-vous », « Objet : relance », « Objet : certificat », « Objet : question ». Aucun logo, aucune adresse."
  mail-window:
    description: "fenêtre « NOUVEAU MESSAGE » dessinée à l'encre (aqWindow 620 × 420, fond paper à 92 %) : 9 lignes de texte ink-light (traits de 3 u) qui se replient en 3 lignes d'encre pleine quand le mail trouve son ton. Aucun destinataire, aucun nom."
  staff-room:
    description: "la salle des profs (pages 1 et 3) : une longue table en lavis brun (x 250 à 1450 de la page, y 600 à 660, pieds à l'encre), six chaises à l'encre rentrées sous la table (dossiers 60 × 90 u), l'horloge murale (cercle d'encre r 90 à (1350, 200), aiguilles accent, 18 h), la pile de copies (feuilles paper-2 300 × 400 ×0,45 empilées à (560, 560), de 4 à 7 feuilles), la tasse (cup) à (980, 575), le portable (kit aqLaptop ×0,6 à (1150, 560), écran gris éteint puis boîte de réception), la feuille des bulletins (300 × 400 à (1400, 740), grille à l'encre 8 × 5). Page 3 : la même salle, colorée : six silhouettes autour de la table (ocre à gauche, accent à droite), trois portables allumés (ocre-pale), trois feuilles à lignes de couleur."
  chalkboard:
    description: "le tableau de la classe (pages 2 et 7) : rectangle 1100 × 560 u centré à (cx, 400) rempli d'un lavis gris-lavis-2 à 85 % cerné d'un trait d'encre 6 px, un rebord brun en bas. Craie : traits paper à main levée (aqInk 6 px). Grille : 10 colonnes × 5 lignes à l'encre ink-light 3 px tracées (aqDrawPrep) ; les cases se remplissent de lavis gris (impact ×0,2 → 1) ; sur la page 7 elles s'effacent par le centre (aqErase) ligne par ligne."
  hand-chalk:
    description: "la main qui écrit (page 2) : une main peinte comme celles du film 1 (lavis ocre-pale + cerne d'encre 4 px, vue de dessus, 220 u) tenant une craie (bâton paper 60 × 12 u) ; elle entre par le bas droit, écrit, puis remplit les cases ; elle se pose au bord droit du tableau à (3100, 560)."
  figures-eleves:
    description: "six élèves en taches (aqFigure 150 à 180 u, pose 'dos' ou 'penche') devant le tableau, à y 620 à 800, ocre ; dans la douleur ils pâlissent vers gris-lavis puis s'effacent par le centre (aqErase) ; sur la page 7 ils reviennent nets en ocre par coups de pinceau."
  bulletin:
    description: "feuille de bulletin (page 4) : 300 × 400 u paper-2 à (5700, 520), en-tête à l'encre (deux traits), 5 lignes qui s'écrivent en encre accent (traits 4 u tracés par masque, 0,2 s chacune), une coche ocre tracée en marge de la ligne 3 (la relecture)."
  sequence-card:
    description: "fiche de séquence (page 4) : carte 320 × 220 u paper cernée d'encre 4 px à (6400, 520), titre Caveat 34 px « Séquence 3 », trois lignes ink-light ; elle se dédouble (une copie glisse de 180 u vers la droite, 0,2 s expo.out) : la gauche prend un lavis ocre-pale et la note Caveat « classe A », la droite un lavis accent-pale et « classe B »."
  grille-evaluation:
    description: "grille d'évaluation (page 5) : 5 colonnes × 4 lignes à l'encre 4 px tracées ligne à ligne (aqDrawPrep), 640 × 320 u centrée à (8150, 540) ; étiquettes Caveat 28 px ink-2 « critère », « acquis », « en cours » ; trois coches ocre tracées dans des cases."
  reflex-notebook:
    description: "petit carnet manuscrit 520 × 360 u (page 6, à (9520, 430)) : paper, ombre, spirale de 6 anneaux à l'encre, deux lignes Caveat 34 px ink-2 « vos documents », « vos outils », chacune cochée d'un trait ocre."
  cup:
    description: "la tasse (pages 1 et 6) : cylindre à l'encre 70 × 60 u avec son anse, café en lavis (gris-lavis dans la douleur, ocre-pale dans la solution), vapeur : deux boucles d'encre ink-light 3 px (chemins tracés par aqDraw) qui s'effacent par le centre quand le café refroidit (gag) et se retracent sur « quotidien » (rime)."
  hands:
    description: "mains peintes en taches (lavis accent-pale et ocre-pale cernés d'un trait d'encre 4 px), vues de dessus : la main à la craie (page 2)."
  signature:
    description: "« Antoine Contino » en chemin SVG (Caveat 120 px converti en tracé, ou texte Caveat révélé par un masque qui avance de gauche à droite en 1,0 s power1.inOut, à la vitesse d'une main), encre accent, qui naît de la goutte tombée ; « formateur IA » en DM Sans 34 px ink-2 dessous. Aucun logo (non fourni)."
  button:
    description: "UN bouton : une tache ocre (aqBlob 10 sommets, 520 × 110 u, opacité 0,9) séchée en bouton, texte cta « Réserver un appel » ink ; dessous les deux adresses en DM Sans 24 px ink-2. Clic : pression ×0,85 0,06 s, la tache passe en accent 0,07 s puis revient ocre, onde accent qui s'ouvre et s'efface."
  cursor:
    description: "flèche papier (#F8F1E6) cernée d'encre 2,5 px, ombre douce, 34 × 44 u ; arrive en UN mouvement courbe (0,5 s power3.out en x, power2.out en y) et clique directement : pression + onde accent. Jamais d'hésitation. Dans la douleur elle colle le sujet dans la fenêtre (clic sur le champ)."
  end-card:
    description: "page 8 du carnet : la signature, « formateur IA », le bouton ocre, les deux adresses, le curseur qui arrive et clique, puis 2,5 s de tenue vivante (granulation des taches qui dérive, grain du papier qui glisse, la traînée de la goutte qui sèche) avant le noir à 52.00."

world:
  camera: "kit de reference/aquarelle.html : #stage > #drift > #cam > #world ; aqCam(world, cam, x, y, s, blur) amène le point (x, y) du monde au centre du cadre (960, 540) à l'échelle s. Dérive permanente sur #drift (10 à 30 u/s ou 1 à 3 %/s), crans et whips sur #world et #cam (expo.inOut, flou 6 à 12 px au milieu). Toute la caméra du film va de gauche à droite ou s'enfonce ; jamais de retour."
  carnet (monde unique, 8 pages, 14 700 × 1 080 u) :
    pages: "page k (k = 1 à 8) : x de (k - 1) × 1734 à (k - 1) × 1734 + 1700, y de 0 à 1080 ; centre cx_k = 850 + (k - 1) × 1734 : P1 850 · P2 2584 · P3 4318 · P4 6052 · P5 7786 · P6 9520 · P7 11254 · P8 12988 (même géométrie que le film 1). Reliure (34 u) entre deux pages : x = 1700 + (k - 1) × 1734. Autour des pages, le bureau paper-dark."
    P1 (douleur, 0 à 10.40): "la salle des profs vide un lundi soir (staff-room) : table (250 à 1450, 600 à 660), six chaises rentrées, horloge à (1350, 200) à 18 h, pile de copies à (560, 560), tasse à (980, 575) avec sa vapeur, portable ×0,6 à (1150, 560) écran éteint, feuille des bulletins à (1400, 740) ; note Caveat « lundi, 18 h » à (300, 96) ; deux lavis gris-lavis en haut (la nuit aux fenêtres), (500, 160) et (900, 160)."
    P2 (douleur, 10.40 à 18.89): "le tableau de la classe (chalkboard 1100 × 560 à (2584, 400)), la main à la craie, six élèves en taches ocre devant (x 2130 à 3040, y 620 à 800) ; la goutte accent (la même encre qu'au film 1) au bas de la page (3300, 820)."
    pivot (18.89 à 22.40): "l'intérieur de la goutte : ground-ink, la question centrée, puis la goutte ocre qui tombe et ouvre P3."
    P3 (solution, 22.40 à 27.27): "la même salle des profs, pleine et colorée (staff-room, page 3) : table (3718 à 4918, 600 à 660), six silhouettes autour (ocre à (3950, 470), (4150, 480), (4350, 470) ; accent à (4550, 480), (4750, 470) et (4250, 700) de dos), trois portables allumés sur la table, trois feuilles à lignes de couleur, la tasse ocre-pale à (4700, 590)."
    P4 (solution, 27.27 à 32.14): "le bulletin (5700, 520) et la fiche de séquence (6400, 520) qui se dédouble."
    P5 (solution, 32.14 à 37.25): "la fenêtre de mail (7450, 520) et la grille d'évaluation (8150, 540)."
    P6 (solution, 37.25 à 40.95): "le petit carnet des outils à (9520, 430) et la tasse qui fume à nouveau à (9900, 720)."
    P7 (solution, 40.95 à 45.00): "le tableau de P2 redessiné (chalkboard 1100 × 560 à (11254, 400)) avec sa grille pleine de gris, six élèves gris pâles devant (x 10800 à 11710, y 620 à 800) ; les cases s'effacent, les élèves reviennent en ocre sur un lavis ocre-pale."
    P8 (fin, 45.00 à 52.00): "la signature à (12988, 380), « formateur IA » à (12988, 470), le button à (12988, 660), les adresses à (12988, 760) ; la goutte tombe à (12560, 330), à l'attaque du « A »."
  framings: "cadrages de référence (marges gauche et droite égales ; tout objet de la page au-dessus de y 880 à l'écran) : page entière cam(cx, 540, 1.0) · pile de copies P1 cam(620, 600, 1.3) · écran du portable P1 cam(1150, 560, 1.4) · feuille des bulletins P1 cam(1400, 740, 1.5) · tableau P2 cam(2584, 420, 1.3) · élèves P2 cam(2584, 640, 1.15) · P3 entière cam(4318, 540, 1.0) puis documents cam(4318, 600, 1.3) · P4 entière cam(6052, 540, 1.0) puis fiche cam(6400, 520, 1.3) · P5 entière cam(7786, 540, 1.0) puis grille cam(8150, 540, 1.2) · P6 entière cam(9520, 540, 1.0) · P7 entière cam(11254, 540, 1.0) · signature P8 cam(12988, 400, 1.15) · bouton P8 cam(12988, 600, 1.0)"
  depth: "trois niveaux dans chaque plan tenu : avant-plan = le bord flou (7 px) de la page suivante coupé par le bord droit, ou une goutte en vol, ou le stylo ; sujet net = la page ; fond = le bureau paper-dark grainé. Pendant les dérives, l'avant-plan glisse 2,5 fois plus vite que la page, le bureau 0,4 fois (parallaxe)."

negative:
  - "Aucune seconde mise en valeur : la boîte accent est la SEULE façon de souligner un mot du sous-titre, le trait ocre marque les 4 pics (aucun autre texte coloré, aucun texte lumineux)."
  - "Aucune grande phrase : sous-titre 62 px, moment typographique 84 px au plus (le pivot seulement) ; aucun mot géant, aucune grosse boîte. Rien d'autre que le sous-titre dans la bande y 890 à 980 ; jamais de sous-titre en haut à gauche ; aucun titre Fraunces qui répète la voix sur la page."
  - "Une seule chose à regarder : la caméra isole le sujet de la phrase ; marges gauche et droite égales ; la caméra va de gauche à droite ou s'enfonce, jamais d'aller-retour ; jamais d'hésitation du curseur."
  - "Aucun décor sans sens, aucun symbole abstrait, aucun compteur, aucun chronomètre ; aucune ligne du décor ne traverse une phrase (la reliure et les lignes des pages restent au-dessus de y 880)."
  - "Aucune teinte hors charte : accent et ses pâles, ocre et ses pâles, gris de lavis, brun des tables, encre."
  - "Aucun outil d'IA nommé, aucun logo, aucun nom d'élève, de famille, d'établissement ou de prof (les objets des mails restent génériques), aucune note, aucun chiffre de gain, aucune durée ni prix de formation."
  - "Aucune tache ni aucun trait qui apparaît en fondu : goutte, pinceau ou tracé ; aucune tache dédoublée pendant une couture."
  - "Pas d'Inter, Space Grotesk, Geist, system-ui. Pas d'emoji. Pas de Math.random (seeds)."
  - "Pas d'ease rebondissant ni élastique ; pas de boucle infinie (repeat:-1) ; pas de poussée lente sur chaque plan."
  - "Aucun texte visible qui ne soit pas cité dans les lignes Scene ou dans les composants ci-dessus."
  - "Jamais d'animation de letterSpacing ; jamais de tween de width, height, top, left (échelle, translation, masques)."
---

# Le carnet, la salle des profs : charte du film 2

Le film reprend le carnet du film 1. **La douleur** tient sur deux pages lavées de gris : lundi, dix-huit heures, la
salle des profs est vide, une goutte grise sèche en horloge, la pile de copies monte, l'écran du portable aligne les
mails aux familles et la feuille des bulletins se remplit de gris pendant que l'horloge tourne et que la tasse
refroidit ; puis le tableau de la classe, où une main à la craie transmet à six élèves en ocre, se quadrille en cases
que la même main remplit, et les élèves pâlissent derrière la grille, une case à la fois. Au **pivot**, la caméra
plonge dans la goutte d'encre : « Et si vous repreniez ce temps ? ». Une goutte ocre ouvre **la solution** : la même
salle, pleine et colorée ; le bulletin qui s'écrit et se relit ; la séquence qui se dédouble pour deux classes ; le
mail qui trouve son ton en trois lignes ; la grille d'évaluation tracée en direct ; le petit carnet des outils et la
tasse qui fume à nouveau ; le tableau qui s'efface pour laisser revenir les élèves. **La fin** : la même carte que le
film 1, la goutte, la signature, le bouton, le clic.

Tout ce qu'on lit est en DM Sans : la phrase de la voix en sous-titre en bas au centre, mot par mot, avec un seul mot
clé par phrase dans une petite boîte bordeaux qui se trace d'abord. Un trait de pinceau ocre marque les 4 pics
(« transmettre », « temps », « élèves », « avec »). Caveat écrit les notes manuscrites et la signature ; Fraunces ne
sert qu'au moment typographique du pivot.
