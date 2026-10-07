---
version: 2
name: "Antoine Contino, formateur IA · Le carnet, le cours : charte du film 3"
description: >
  Charte image du film « Préparer ses cours avec l'IA » (50,6 s, 16:9, voix off Paul K), direction A « Le carnet »
  héritée du film 1 (DIRECTIONS.md). Le carnet d'un enseignant : huit pages côte à côte que la caméra parcourt de
  gauche à droite, chaque page une scène peinte à l'aquarelle sur papier crème. La douleur est lavée de gris : le
  bureau du prof un mardi soir, la salle dans la pénombre où trente téléphones s'allument, la porte au panneau et le
  tableau qui avance seul ; le pivot est le noir de l'encre ; après lui, les pages se colorent (le plan de cours à
  deux encres, les quatre vignettes, l'étudiant et le plan manuscrit, la salle aux mains levées).
  Une seule mise en valeur du texte, la boîte bordeaux du mot clé ; 4 traits de pinceau ocre sous les pics.
  Code commun exécutable : reference/aquarelle.html (copie conforme du kit du film 1, copié tel quel par chaque séquence).
unit: 1920×1080
principle: lisible sans le son · une seule chose à regarder · un seul accent, une seule mise en valeur · la voix déclenche chaque révélation

colors:
  paper: "#F4EBDD"           # la page du carnet (monde clair, 13 séquences sur 14)
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
  type:       { fontFamily: "Fraunces", px: 84, weight: 600, lineHeight: 1.1, tracking: "-0.01em", note: "SEUL moment typographique : le pivot « Et si vous la faisiez entrer dans le cours ? » (séquence 6), centré sur le noir en ink-paper, 84 px au plus, sur deux lignes, sans sous-titre en bas pendant ce temps ; trait ocre sous « entrer »" }
  note:       { fontFamily: "Caveat", px: 34, weight: 600, lineHeight: 1.2, note: "les notes manuscrites des pages du carnet, en ink-2 (« mardi soir », « l'an dernier », « IA interdite », « vos contenus », « vos objectifs »), légèrement penchées (-3 à 3°) ; aucune note chiffrée dans ce film" }
  ui:         { fontFamily: "DM Sans", px: 22, weight: 400, lineHeight: 1.35, note: "aucun texte lisible dans les fenêtres dessinées de ce film : les lignes de texte sont des traits (3 u) d'encre ou d'ocre ; étiquette 16 px 600 espacée de 0,08 em « PLAN DE COURS » sur la fenêtre de la page 4, « NOUVELLE CONVERSATION » sur celle de la page 6" }
  title:      { fontFamily: "Fraunces", px: 72, weight: 600, tracking: "-0.02em", note: "aucun titre imprimé dans ce film ; réservé" }
  craie:      { fontFamily: "Caveat", px: 40, weight: 600, note: "l'écriture à la craie sur le tableau (page 3) : traits paper à 85 % tracés à main levée (aqInk, couleur paper, 6 px), sans mot lisible" }
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
    look: "trait d'encre ink à main levée : stroke 3 à 7 px, bouts ronds, filtre #ink (déplacement 5). Sert au portable, à la lampe, au stylo, à la porte, aux tables vues de côté, aux cadres des fenêtres et des vignettes."
    motion: "il se DESSINE (svg-path-draw : stroke-dashoffset de la longueur vers 0, 0,2 à 0,5 s power2.out), jamais il n'apparaît en fondu."
  drop (signature 1, « la goutte ») :
    look: "une goutte de 12 à 46 u (aqDrop : tache ronde à 7 sommets, opacité 0,85) de la couleur de l'idée : accent (encre), gris-lavis (eau sale de la douleur), ocre (la couleur qui revient)."
    motion: "aqDropFall : elle arrive de la caméra (×4, flou 10 px, 0,25 s power2.in) ou tombe du haut (y -500 → 0, 0,16 s power2.in), touche la page (impact : la tache s'ouvre ×0,2 → ×1 en 0,12 s expo.out, 2 éclaboussures de 6 u à ±60 u), puis sèche en objet (signature 2). Elle revient 8 fois dans le film (STORYBOARD.md, SIGNATURES)."
  dry (signature 2, « le séchage ») :
    motion: "aqDry(g, k) : k 0 → 1 en 0,4 à 0,8 s power1.inOut ; l'anneau de bord fonce (opacité du ring 0 → 1), la granulation paraît, la tache se rétracte de 4 % ; à k = 1 l'objet dessiné dedans (lampe, fenêtre, note, bouton) est net. Inverse (effacement) : la couleur pâlit vers gris-lavis puis la tache s'efface par le centre."
  figure:
    description: "silhouette peinte en taches, sans visage (aqFigure) : buste en dôme + tête ronde, vue de dos ou de trois quarts, poses 'dos', 'penche', 'bras-leve'. Couleur ocre ou accent dans la solution, gris-lavis dans la douleur. Les mêmes gabarits dans les trois films ; en salle, de petits gabarits (90 à 110 u) en rangs ; l'étudiant et le prof en grands gabarits (200 à 230 u)."
  desk-prof:
    description: "le bureau du prof le soir (pages 1 et 4) : bande de bureau en lavis brun à y 860 sur toute la page, la lampe (kit aqLamp, allumée, pied à (260, 800), échelle 0,9) dont la lueur est un lavis ocre-2 doux, le portable (kit aqLaptop) à (850, 575) ; page 1 : son écran montre une diapositive (rectangle paper-2 420 × 240 : un bloc gris de titre et cinq lignes grises) identique à celles de la pile ; la pile de diapositives (4 cartes paper-2 300 × 200, rotations 4°, 9°, 13°, 18°) à (1350, 620) ; la note Caveat « mardi soir » à (300, 96) ; la note Caveat « l'an dernier » sur le coin de la carte du dessus (1240, 540). Page 4 : le même bureau coloré (lueur ocre-2 pleine, bureau brun), le portable à (6052, 575) à l'échelle 1,0 dont l'écran montre la fenêtre « PLAN DE COURS » (aqWindow 560 × 330) : des lignes d'encre (le prof) et des lignes ocre en marge (l'IA), le stylo (kit aqPen) qui barre une ligne et la réécrit."
  classroom:
    description: "la salle vue du fond (pages 2 et 7) : le tableau (chalkboard 1000 × 420 centré à (cx, 300), lavis gris-lavis-2 à 85 %, cadre d'encre 6 px, rebord brun) qui porte la diapositive projetée (rectangle paper-2 600 × 340 à (cx, 310), bloc de titre et cinq lignes grises : la même que sur le portable) ; cinq rangs de six élèves (aqFigure 90 à 110 u, pose 'dos') aux centres x = cx - 650 + j × 260 (j = 0 à 5) et y = 500, 580, 660, 740, 820 (i = 0 à 4) ; trente téléphones = une tache ocre 26 × 40 (aqWash ocre, opacité 0,85) aux mains de chaque élève, à (x, y + 30). Page 2 : la pénombre, un lavis gris-lavis à 35 % sur toute la page, élèves gris-lavis, écrans qui s'allument par vagues (impact ×0,2 → 1). Page 7 : la même salle colorée : élèves ocre et accent en alternance, les trente bras levés (pose 'bras-leve', un trait ocre ou accent de 40 u au-dessus de chaque buste), le tableau sous un lavis ocre-pale, le prof (aqFigure accent 230 u, pose 'penche') dans l'allée centrale à (cx, 640)."
  chat-phone (gag):
    description: "au premier rang (page 2, rang y 820, élève j = 2 à (cx - 130, 820)) : le téléphone agrandi par la caméra, sa fenêtre de chat dessinée (aqWindow 26 × 40 en coordonnées de page, lisible à l'échelle 1,8 : une barre, trois traits de texte ocre, un champ), le pouce = une main peinte (hands) ×0,4 qui tape deux fois ; aucun texte lisible."
  door-sign:
    description: "la porte de la classe (page 3, à gauche) : rectangle d'encre 420 × 640 centré à (3900, 540) (haut 220, bas 860), poignée à l'encre à (4070, 560), entrebâillée : une fente de 40 u le long de son bord droit par où passe une lueur ocre-pale (lavis 40 × 600 à (4130, 540)) ; le panneau : carte paper 260 × 140 à (3900, 380), note Caveat 34 px ink-2 « IA interdite », un cercle barré accent (r 50, trait 6 px) tracé à sa droite ; quatre coins de ruban paper-2."
  board-ailleurs:
    description: "le tableau de la classe (page 3, à droite) : chalkboard 900 × 440 centré à (4700, 320) (haut 100, bas 540), la main à la craie (hand-chalk) qui écrit des traits paper ; six élèves (aqFigure 150 u, pose 'dos') aux centres x = 4330, 4480, 4630, 4780, 4930, 5080 et y = 640, 700, 660, 720, 650, 710, chacun avec la lueur ocre de sa poche (tache ocre 26 × 40 à (x, y + 55)) ; leurs têtes se penchent (rotation 8°) vers la lueur ; la goutte accent (la même encre qu'aux films 1 et 2) au bas de la page à (5050, 820)."
  hand-chalk:
    description: "la main qui écrit (page 3) : une main peinte (lavis ocre-pale + cerne d'encre 4 px, vue de dessus, 220 u) tenant une craie (bâton paper 60 × 12 u) ; elle entre par le bas droit, écrit des traits paper 6 px à main levée, puis sort par le bas droit."
  vignettes:
    description: "quatre vignettes (page 5) : cartes 340 × 230 paper cernées d'encre 4 px aux centres (7186, 480), (7586, 480), (7986, 480), (8386, 480), chacune posée sur une tache de couleur qui sèche (ocre-pale, accent-pale, ocre-pale, accent-pale) ; scène sans texte dans chacune : 1 le quiz = quatre petites figures 'bras-leve' ocre (60 u) devant une ellipse ocre ; 2 le débat = deux bulles d'encre (ellipses 120 × 70) face à face, lavis ocre-pale et accent-pale ; 3 l'étude de cas = quatre tables (ellipses d'encre 90 × 40) avec deux points-figures chacune ; 4 la correction = une feuille 120 × 160 à cinq lignes grises et deux traits ocre en marge. Elles s'ouvrent une à une (coup de pinceau de la tache puis tracé du cadre), jamais en fondu."
  student:
    description: "l'étudiant (page 6, à gauche) : aqFigure ocre 200 u de trois quarts à (9100, 600), sa table en lavis brun 500 × 50 à (9150, 700) ; la fenêtre « NOUVELLE CONVERSATION » (aqWindow 420 × 260 à (9250, 380)) : une ligne de question qui se tape (traits d'encre qui avancent), une ligne de source avec une coche ocre, une ligne barrée d'un trait accent ; le cahier (paper-2 260 × 180 à (9080, 740)) où une tache ocre grandit (goutte puis séchage) puis sèche en deux traits ocre (les réflexes)."
  plan-manuscrit:
    description: "le plan de cours manuscrit (page 6, à droite) : feuille paper-2 420 × 540 à (9950, 540), deux lignes Caveat 34 px ink « vos contenus », « vos objectifs » révélées par masque, quatre lignes ink-light dessous ; l'IA en marge : quatre traits ocre courts (3 u) à droite des lignes, qui se tracent ; sur « s'adapte », deux lignes ink-light échangent leur place (y) et un trait ocre se trace sous la nouvelle première."
  hands:
    description: "mains peintes en taches (lavis accent-pale et ocre-pale cernés d'un trait d'encre 4 px), vues de dessus : la main à la craie (page 3), le pouce du gag (page 2, ×0,4), la main au stylo (page 4)."
  signature:
    description: "« Antoine Contino » en chemin SVG (Caveat 120 px converti en tracé, ou texte Caveat révélé par un masque qui avance de gauche à droite en 1,0 s power1.inOut, à la vitesse d'une main), encre accent, qui naît de la goutte tombée ; « formateur IA » en DM Sans 34 px ink-2 dessous. Aucun logo (non fourni)."
  button:
    description: "UN bouton : une tache ocre (aqBlob 10 sommets, 520 × 110 u, opacité 0,9) séchée en bouton, texte cta « Réserver un appel » ink ; dessous les deux adresses en DM Sans 24 px ink-2. Clic : pression ×0,85 0,06 s, la tache passe en accent 0,07 s puis revient ocre, onde accent qui s'ouvre et s'efface."
  cursor:
    description: "flèche papier (#F8F1E6) cernée d'encre 2,5 px, ombre douce, 34 × 44 u ; arrive en UN mouvement courbe (0,5 s power3.out en x, power2.out en y) et clique directement : pression + onde accent. Jamais d'hésitation."
  end-card:
    description: "page 8 du carnet : la signature, « formateur IA », le bouton ocre, les deux adresses, le curseur qui arrive et clique, puis la tenue vivante (granulation des taches qui dérive, grain du papier qui glisse, la traînée de la goutte qui sèche) avant le noir à 50.60."

world:
  camera: "kit de reference/aquarelle.html : #stage > #drift > #cam > #world ; aqCam(world, cam, x, y, s, blur) amène le point (x, y) du monde au centre du cadre (960, 540) à l'échelle s. Dérive permanente sur #drift (10 à 30 u/s ou 1 à 3 %/s), crans et whips sur #world et #cam (expo.inOut, flou 6 à 12 px au milieu). Toute la caméra du film va de gauche à droite ou s'enfonce ; jamais de retour."
  carnet (monde unique, 8 pages, 14 700 × 1 080 u) :
    pages: "page k (k = 1 à 8) : x de (k - 1) × 1734 à (k - 1) × 1734 + 1700, y de 0 à 1080 ; centre cx_k = 850 + (k - 1) × 1734 : P1 850 · P2 2584 · P3 4318 · P4 6052 · P5 7786 · P6 9520 · P7 11254 · P8 12988 (même géométrie que les films 1 et 2). Reliure (34 u) entre deux pages : x = 1700 + (k - 1) × 1734. Autour des pages, le bureau paper-dark."
    P1 (douleur, 0 à 4.60): "le bureau du prof un mardi soir (desk-prof, page 1) : lampe allumée au pied (260, 800), portable à (850, 575) avec la diapositive à l'écran, pile de diapositives à (1350, 620), notes « mardi soir » à (300, 96) et « l'an dernier » à (1240, 540) ; deux lavis gris-lavis en haut (la nuit), (500, 160) et (1250, 160)."
    P2 (douleur, 4.60 à 10.65): "la salle dans la pénombre (classroom, page 2) : tableau à (2584, 300) avec la diapositive projetée, cinq rangs de six élèves gris (x = 1934 + j × 260, y = 500 à 820), trente téléphones ocre ; le gag au premier rang (chat-phone à (2454, 820))."
    P3 (douleur, 10.65 à 16.40): "la porte et le panneau à gauche (door-sign à (3900, 540)), le tableau et les six élèves à droite (board-ailleurs à (4700, 320)) ; la goutte accent au bas de la page (5050, 820)."
    pivot (16.40 à 20.42): "l'intérieur de la goutte : ground-ink, la question centrée sur deux lignes, puis la goutte ocre qui tombe et ouvre P4."
    P4 (solution, 20.42 à 23.50): "le même bureau coloré (desk-prof, page 4) : lampe au pied (5462, 800), portable à (6052, 575) échelle 1,0 avec la fenêtre « PLAN DE COURS », le stylo ; notes absentes."
    P5 (solution, 23.50 à 30.00): "les quatre vignettes (vignettes) aux centres (7186, 480), (7586, 480), (7986, 480), (8386, 480)."
    P6 (solution, 30.00 à 39.55): "l'étudiant à gauche (student, figure à (9100, 600), fenêtre à (9250, 380), cahier à (9080, 740)) et le plan manuscrit à droite (plan-manuscrit à (9950, 540))."
    P7 (solution, 39.55 à 43.50): "la salle de P2 redessinée en couleur (classroom, page 7) : tableau à (11254, 300) sous un lavis ocre-pale, cinq rangs de six élèves (x = 10604 + j × 260, y = 500 à 820) ocre et accent, trente bras levés, le prof à (11254, 640)."
    P8 (fin, 43.50 à 50.60): "la signature à (12988, 380), « formateur IA » à (12988, 470), le button à (12988, 660), les adresses à (12988, 760) ; la goutte tombe à (12560, 330), à l'attaque du « A »."
  framings: "cadrages de référence (marges gauche et droite égales ; tout objet de la page au-dessus de y 880 à l'écran) : page entière cam(cx, 540, 1.0) · portable P1 cam(850, 560, 1.4) · pile de diapositives P1 cam(1350, 620, 1.5) · premier rang P2 cam(2454, 800, 1.8) · tableau P2 cam(2584, 320, 1.4) · porte P3 cam(3900, 540, 1.0) puis panneau cam(3900, 400, 1.5) · tableau et élèves P3 cam(4700, 520, 1.05) · plan de cours P4 cam(6052, 500, 1.4) · vignettes 1 et 2 cam(7386, 480, 1.25) puis 3 et 4 cam(8186, 480, 1.25) · étudiant P6 cam(9150, 560, 1.2) puis plan manuscrit cam(9950, 540, 1.2) · P7 entière cam(11254, 540, 1.0) puis le prof cam(11254, 640, 1.3) · signature P8 cam(12988, 400, 1.15) · bouton P8 cam(12988, 600, 1.0)"
  depth: "trois niveaux dans chaque plan tenu : avant-plan = le bord flou (7 px) de la page suivante coupé par le bord droit, ou une goutte en vol, ou le stylo ; sujet net = la page ; fond = le bureau paper-dark grainé. Pendant les dérives, l'avant-plan glisse 2,5 fois plus vite que la page, le bureau 0,4 fois (parallaxe)."

negative:
  - "Aucune seconde mise en valeur : la boîte accent est la SEULE façon de souligner un mot du sous-titre, le trait ocre marque les 4 pics (aucun autre texte coloré, aucun texte lumineux)."
  - "Aucune grande phrase : sous-titre 62 px, moment typographique 84 px au plus (le pivot seulement) ; aucun mot géant, aucune grosse boîte. Rien d'autre que le sous-titre dans la bande y 890 à 980 ; jamais de sous-titre en haut à gauche ; aucun titre Fraunces qui répète la voix sur la page."
  - "Une seule chose à regarder : la caméra isole le sujet de la phrase ; marges gauche et droite égales ; la caméra va de gauche à droite ou s'enfonce, jamais d'aller-retour ; jamais d'hésitation du curseur."
  - "Aucun décor sans sens, aucun symbole abstrait, aucun compteur ; aucune ligne du décor ne traverse une phrase (la reliure et les lignes des pages restent au-dessus de y 880)."
  - "Aucune teinte hors charte : accent et ses pâles, ocre et ses pâles, gris de lavis, brun des tables, encre."
  - "Aucun outil d'IA nommé, aucun logo, aucun nom d'élève, d'établissement ou de prof (les fenêtres dessinées ne portent que des traits), aucune note, aucun chiffre de gain, aucune durée ni prix de formation ; aucun chiffre écrit à l'écran (la date est « l'an dernier », le nombre est dit par la voix)."
  - "Aucune tache ni aucun trait qui apparaît en fondu : goutte, pinceau ou tracé ; aucune tache dédoublée pendant une couture."
  - "Pas d'Inter, Space Grotesk, Geist, system-ui. Pas d'emoji. Pas de Math.random (seeds)."
  - "Pas d'ease rebondissant ni élastique ; pas de boucle infinie (repeat:-1) ; pas de poussée lente sur chaque plan."
  - "Aucun texte visible qui ne soit pas cité dans les lignes Scene ou dans les composants ci-dessus."
  - "Jamais d'animation de letterSpacing ; jamais de tween de width, height, top, left (échelle, translation, masques)."
---

# Le carnet, le cours : charte du film 3

Le film reprend le carnet des films 1 et 2. **La douleur** tient sur trois pages lavées de gris : mardi soir, le
bureau du prof, une goutte grise sèche en lampe, le portable montre la même diapositive que la pile, « l'an dernier » ;
la salle dans la pénombre où trente téléphones s'allument en ocre, un pouce qui répond à un chat pendant que la
diapositive défile ; la porte au panneau « IA interdite » dont l'entrebâillement laisse passer la lueur ocre, puis le
tableau où la craie avance pendant que les têtes se penchent vers les poches. Au **pivot**, la caméra plonge dans la
goutte d'encre : « Et si vous la faisiez entrer dans le cours ? ». Une goutte ocre ouvre **la solution** : le même
bureau, coloré, où le plan de cours s'écrit à deux encres et où la main corrige ; quatre vignettes qui s'ouvrent une à
une ; l'étudiant qui tape, vérifie et barre, et sa tache ocre qui sèche en réflexes ; le plan manuscrit avec l'IA en
marge ; la salle redessinée en couleur, trente mains levées, le prof entre les tables. **La fin** : la même carte que
les films 1 et 2, la goutte, la signature, le bouton, le clic.

Tout ce qu'on lit est en DM Sans : la phrase de la voix en sous-titre en bas au centre, mot par mot, avec un seul mot
clé par phrase dans une petite boîte bordeaux qui se trace d'abord. Un trait de pinceau ocre marque les 4 pics
(« entrer », « préparer », « progresser », « vivant »). Caveat écrit les notes manuscrites et la signature ; Fraunces
ne sert qu'au moment typographique du pivot.
