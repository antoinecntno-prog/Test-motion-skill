---
version: 2
name: "Antoine Contino, formateur IA · Le carnet : charte du film"
description: >
  Charte image du film « Formation IA pour les étudiants » (50,8 s, 16:9, voix off Paul K), direction A « Le carnet »
  de DIRECTIONS.md. Le film est un carnet de croquis ouvert : huit pages côte à côte que la caméra parcourt de gauche
  à droite, chaque page une scène peinte à l'aquarelle sur papier crème. La douleur est lavée de gris et de bordeaux
  pâle, ses taches s'effacent ; le pivot est le noir de l'encre ; après lui, les pages se colorent (ocre, bordeaux).
  Une seule mise en valeur du texte, la boîte bordeaux du mot clé ; 4 traits de pinceau ocre sous les pics.
  Code commun exécutable : reference/aquarelle.html (copié tel quel par chaque séquence).
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
  type:       { fontFamily: "Fraunces", px: 84, weight: 600, lineHeight: 1.1, tracking: "-0.01em", note: "SEUL moment typographique : le pivot « Et si l'IA servait à apprendre ? » (séquence 5), centré sur le noir en ink-paper, 84 px au plus, sans sous-titre en bas pendant ce temps ; trait ocre sous « apprendre »" }
  note:       { fontFamily: "Caveat", px: 34, weight: 600, lineHeight: 1.2, note: "les notes manuscrites des pages du carnet, en ink-2 (« dim. 23 h 04 », « Dissertation · 1/3 », « Leçon », « Défi 3 », les réflexes), légèrement penchées (-3 à 3°) ; la note « 12 » en Caveat 150 px accent qui sèche en ink-light" }
  ui:         { fontFamily: "DM Sans", px: 22, weight: 400, lineHeight: 1.35, note: "le texte des fenêtres de chat dessinées (sujet collé, réponse, question tapée) ; étiquettes 16 px 600 espacées de 0,08 em (VOUS, IA, NOUVELLE CONVERSATION)" }
  title:      { fontFamily: "Fraunces", px: 92, weight: 600, tracking: "-0.02em", note: "titre imprimé du carnet seulement : « Défi 3 » (page 6)" }
  chrono:     { fontFamily: "DM Sans", px: 74, weight: 700, tracking: "-0.02em", tabularNums: true, note: "le chronomètre de la page 6 : « 00:42 » puis « 00:41 », « 00:40 » ; chaque chiffre roule" }
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
  chat-window:
    description: "fenêtre de chat GÉNÉRIQUE dessinée à l'encre (aqWindow : cadre arrondi 14 u, barre d'en-tête, étiquette « NOUVELLE CONVERSATION »), fond paper à 92 %. Bulles : « VOUS » à gauche (fond ocre à 14 % dans la solution, gris-lavis à 10 % dans la douleur), « IA » à droite (fond gris-lavis à 16 %, texte gris-lavis-2 dans la douleur ; paper-2 et ink dans la solution). Champ « Écrire un message » avec bouton rond accent. Aucun nom d'outil, aucun logo, aucune donnée réelle. Textes autorisés : ceux des lignes Scene."
  copy-pages:
    description: "trois feuilles paper-2 (300 × 400 u, ombre 0 14px 30px ink à 14 %, rotations 8°, 14°, 21°) rayées de lignes ink-light à 55 % : la dissertation rendue, grise, sans une tache de couleur ; note manuscrite « Dissertation · 1/3 » en Caveat 26 px ink-light."
  red-pen:
    description: "stylo rouge : corps accent-light 360 × 20 u (lavis à 90 %) cerné d'encre 3,5 px, pointe à droite ; il flotte au-dessus de la copie (rotation -34° au repos), se penche de 6° pour tourner une page, se pose à plat à la fin du gag."
  lamp:
    description: "lampe de bureau à l'encre (pied, bras courbe, abat-jour triangulaire, 6 px) ; allumée = lavis ocre-2 large et doux derrière (aq-soft, opacité 0,75) ; éteinte = le lavis s'efface par le centre en 0,3 s et la page prend un lavis gris-lavis à 35 %."
  laptop:
    description: "ordinateur portable à l'encre (écran trapèze 620 × 366 u, clavier 700 × 40 u), l'écran porte la chat-window ; la lueur de l'écran est un lavis ocre-pale à 90 % (douleur : gris-lavis à 60 %)."
  lesson-page:
    description: "la page de la leçon (page 3) : titre « Leçon » en Caveat 34 px, 9 lignes de notes en lavis (ocre-pale et accent-pale, 1 ligne = 1 coup de pinceau), un cadre de note en haut à droite (encre 4 px, 200 × 160 u) où la note « 12 » s'écrit."
  class-tables:
    description: "quatre tables en lavis brun (trapèzes 230 à 260 u de large, 70 u de haut) en perspective légère, un portable à l'encre (100 × 40 u) par table, deux figures par table."
  chrono:
    description: "cercle d'encre 6 px de 280 u, aiguille accent 5 px depuis le centre, lavis ocre-pale derrière (opacité 0,8) ; chiffres chrono « 00:42 » au centre, « il reste » en Caveat 34 px accent dessous."
  score-columns:
    description: "deux colonnes de gouttes (20 u, pas de 44 u) qui s'empilent : ocre à gauche (7), accent à droite (9), au-dessus d'un trait d'encre 4 px ; étiquettes « équipe ocre » et « équipe bordeaux » en Caveat 30 px ink-2 (sans mot « équipe » quand la place manque : « ocre », « bordeaux »)."
  reflex-notebook:
    description: "petit carnet manuscrit 520 × 360 u (paper, ombre, spirale de 6 anneaux à l'encre) : quatre lignes Caveat 34 px ink-2 « Questionner », « Vérifier », « Contredire », « Créer », chacune cochée d'un trait ocre ; il se referme (rotateY 0 → -165° sur la charnière gauche, 0,5 s power3.inOut) et montre sa couverture paper-2."
  hands:
    description: "deux mains peintes en taches (lavis accent-pale et ocre-pale superposés, cernées d'un trait d'encre 4 px), vues de dessus, qui tiennent la page du début (page 1 redessinée en couleurs pleines : lampe ocre-2, écran ocre-pale, goutte accent)."
  signature:
    description: "« Antoine Contino » en chemin SVG (Caveat 120 px converti en tracé, ou texte Caveat révélé par un masque qui avance de gauche à droite en 1,0 s power1.inOut, à la vitesse d'une main), encre accent, qui naît de la goutte tombée ; « formateur IA » en DM Sans 34 px ink-2 dessous. Aucun logo (non fourni)."
  button:
    description: "UN bouton : une tache ocre (aqBlob 10 sommets, 520 × 110 u, opacité 0,9) séchée en bouton, texte cta « Réserver un appel » ink ; dessous les deux adresses en DM Sans 24 px ink-2. Clic : pression ×0,85 0,06 s, la tache passe en accent 0,07 s puis revient ocre, onde accent qui s'ouvre et s'efface."
  cursor:
    description: "flèche papier (#F8F1E6) cernée d'encre 2,5 px, ombre douce, 34 × 44 u ; arrive en UN mouvement courbe (0,5 s power3.out en x, power2.out en y) et clique directement : pression + onde accent. Jamais d'hésitation. Dans la douleur elle colle le sujet dans la fenêtre (clic sur le champ)."
  end-card:
    description: "page 8 du carnet : la signature, « formateur IA », le bouton ocre, les deux adresses, le curseur qui arrive et clique, puis 2,5 s de tenue vivante (granulation des taches qui dérive, grain du papier qui glisse, la traînée de la goutte qui sèche) avant le noir à 50.80."

world:
  camera: "kit de reference/aquarelle.html : #stage > #drift > #cam > #world ; aqCam(world, cam, x, y, s, blur) amène le point (x, y) du monde au centre du cadre (960, 540) à l'échelle s. Dérive permanente sur #drift (10 à 30 u/s ou 1 à 3 %/s), crans et whips sur #world et #cam (expo.inOut, flou 6 à 12 px au milieu). Toute la caméra du film va de gauche à droite ou s'enfonce ; jamais de retour."
  carnet (monde unique, 8 pages, 14 700 × 1 080 u) :
    pages: "page k (k = 1 à 8) : x de (k - 1) × 1734 à (k - 1) × 1734 + 1700, y de 0 à 1080 ; centre cx_k = 850 + (k - 1) × 1734 : P1 850 · P2 2584 · P3 4318 · P4 6052 · P5 7786 · P6 9520 · P7 11254 · P8 12988. Reliure (34 u) entre deux pages : x = 1700 + (k - 1) × 1734. Autour des pages, le bureau paper-dark."
    P1 (douleur, 0 à 4.64): "le bureau de l'étudiant la nuit (styleframes/png/A1.png) : lampe à (260, 620) allumée ocre-2, portable à (760, 575) écran 620 × 366, la chat-window dedans (sujet collé : « Rédige une dissertation de trois pages sur les causes de la Première Guerre mondiale. »), lavis bordeaux pâle de la nuit en haut à droite (1010, 180), la goutte accent au pied du portable (1180, 740) avec sa traînée vers le clavier. Note Caveat « dim. 23 h 04 » à (300, 96)."
    P2 (douleur, 4.64 à 9.80): "le bureau du prof : plateau brun à y 860, lampe à l'encre à (3100, 640), les trois copy-pages glissent et se posent à (2440, 540), (2520, 560), (2600, 580) ; le red-pen au-dessus à (2660, 440) ; note Caveat « lundi, 8 h » à (2010, 96)."
    P3 (douleur, 9.80 à 19.22): "la lesson-page : titre « Leçon » à (3600, 150), lampe du coin allumée à (4850, 300), 9 lignes de notes en lavis de (3600, 300) à (4600, 760), cadre de note à (4760, 230) ; la goutte accent (la même encre qu'en P1) au bas de la page (5080, 820)."
    pivot (19.22 à 23.30): "l'intérieur de la goutte : ground-ink, la question centrée, puis la goutte ocre qui tombe et ouvre P4."
    P4 (solution, 23.30 à 25.80): "la classe (A3, moitié gauche) : class-tables à (5592, 560), (6052, 520), (5622, 800), (6112, 770), un portable par table, 8 figures (ocre à gauche, accent à droite), lavis de sol ocre-pale."
    P5 (solution, 25.80 à 34.48): "l'écran : une grande chat-window (1300 × 720 u) centrée à (7786, 470) ; en haut la bulle « VOUS » et la réponse « IA » ; 4 gestes dessus (question tapée, coche, barre, croquis) ; en bas de la page deux bulles « IA » côte à côte à (7500, 880) et (8070, 880) : la nette (ocre) et celle qui bave (accent-pale) et se corrige."
    P6 (solution, 34.48 à 38.14): "le défi (A3, moitié droite) : « Défi 3 · Trouvez l'erreur de l'IA » à (8900, 150), chrono à (9520, 300), score-columns à (9330 à 9710, 450 à 870), deux groupes de figures de part et d'autre (ocre à gauche à (8900, 600), accent à droite à (10140, 600))."
    P7 (solution, 38.14 à 43.26): "le reflex-notebook à (11254, 430) ; sous lui, la page du début en couleurs dans les hands à (11254, 640)."
    P8 (fin, 43.26 à 50.80): "la signature à (12988, 380), « formateur IA » à (12988, 470), le button à (12988, 660), les adresses à (12988, 760) ; la goutte tombe à (12560, 330), à l'attaque du « A »."
  framings: "cadrages de référence (marges gauche et droite égales) : page entière cam(cx, 540, 1.0) · lampe de P1 cam(430, 600, 1.6) · écran du portable P1 cam(760, 575, 1.55) · copie et stylo P2 cam(2560, 560, 1.3) · P3 entière cam(4318, 540, 1.0) · double page P2 + P3 cam(3451, 560, 0.62) · P4 entière cam(6052, 540, 1.0) · écran P5 cam(7786, 545, 1.2) (le bas de la fenêtre, y 830, reste au-dessus de y 880 à l'écran) · croquis P5 cam(8160, 570, 1.4) · bulles P5 cam(7786, 860, 1.5) · P6 entière cam(9520, 540, 1.0) · carnet P7 cam(11254, 430, 1.4) puis mains cam(11254, 640, 1.1) · signature P8 cam(12988, 400, 1.15) · bouton P8 cam(12988, 600, 1.0)"
  depth: "trois niveaux dans chaque plan tenu : avant-plan = le bord flou (7 px) de la page suivante coupé par le bord droit, ou une goutte en vol, ou le stylo ; sujet net = la page ; fond = le bureau paper-dark grainé. Pendant les dérives, l'avant-plan glisse 2,5 fois plus vite que la page, le bureau 0,4 fois (parallaxe)."

negative:
  - "Aucune seconde mise en valeur : la boîte accent est la SEULE façon de souligner un mot du sous-titre, le trait ocre marque les 4 pics (aucun autre texte coloré, aucun texte lumineux)."
  - "Aucune grande phrase : sous-titre 62 px, moment typographique 84 px au plus (le pivot seulement) ; aucun mot géant, aucune grosse boîte. Rien d'autre que le sous-titre dans la bande y 890 à 980 ; jamais de sous-titre en haut à gauche ; aucun titre Fraunces qui répète la voix sur la page."
  - "Une seule chose à regarder : la caméra isole le sujet de la phrase ; marges gauche et droite égales ; la caméra va de gauche à droite ou s'enfonce, jamais d'aller-retour ; jamais d'hésitation du curseur."
  - "Aucun décor sans sens, aucun symbole abstrait, aucun compteur hors le chronomètre du défi ; aucune ligne du décor ne traverse une phrase (la reliure et les lignes des pages restent au-dessus de y 880)."
  - "Aucune teinte hors charte : accent et ses pâles, ocre et ses pâles, gris de lavis, brun des tables, encre."
  - "Aucun outil d'IA nommé, aucun logo, aucun nom d'élève, d'établissement ou de prof, aucune note réelle hors le « 12 » du récit, aucun chiffre de gain, aucune durée ni prix de formation."
  - "Aucune tache ni aucun trait qui apparaît en fondu : goutte, pinceau ou tracé ; aucune tache dédoublée pendant une couture."
  - "Pas d'Inter, Space Grotesk, Geist, system-ui. Pas d'emoji. Pas de Math.random (seeds)."
  - "Pas d'ease rebondissant ni élastique ; pas de boucle infinie (repeat:-1) ; pas de poussée lente sur chaque plan."
  - "Aucun texte visible qui ne soit pas cité dans les lignes Scene ou dans les composants ci-dessus."
  - "Jamais d'animation de letterSpacing ; jamais de tween de width, height, top, left (échelle, translation, masques)."
---

# Le carnet : charte du film

Le film est un carnet de croquis. **La douleur** se joue sur trois pages lavées de gris : dimanche, la goutte
d'encre bordeaux tombe au coin de la page et allume l'écran où l'étudiant colle le sujet ; lundi, les trois pages
grises glissent sur le bureau du prof et le stylo rouge n'a rien à annoter ; sur la page de la leçon, la lampe
s'éteint, les notes pâlissent, la note « 12 » sèche en gris, et les dernières taches de couleur s'effacent une à une.
Au **pivot**, la caméra plonge dans la goutte d'encre : le noir, la question « Et si l'IA servait à apprendre ? ».
Une goutte ocre tombe sur le noir et ouvre **la solution** : la classe en tables et en silhouettes, l'écran où
quatre gouttes sèchent en quatre gestes (questionner, vérifier, contredire, créer), les deux bulles (ce qu'elle sait,
ce qu'elle invente), le défi chronométré où les points montent et la couleur revient, le carnet des réflexes qui se
referme sur la page du début, colorée, dans des mains. **La fin** : la même goutte bordeaux tombe et trace la
signature, une tache ocre sèche en bouton, le curseur arrive et clique.

Tout ce qu'on lit est en DM Sans : la phrase de la voix en sous-titre en bas au centre, mot par mot, avec un seul mot
clé par phrase dans une petite boîte bordeaux qui se trace d'abord. Un trait de pinceau ocre marque les 4 pics
(« curiosité », « apprendre », « revient », « le leur »). Caveat écrit les notes manuscrites du carnet et la
signature ; Fraunces ne sert qu'au moment typographique du pivot et au titre « Défi 3 ».
