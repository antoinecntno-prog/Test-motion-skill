---
version: 1
name: "Antoine Contino, formateur IA · Le Temps perdu : charte du film"
description: >
  Charte image du film « Le Temps perdu » (57,10 s, 16:9, narratrice Gaëlle), direction A « La maison en coupe »
  (DIRECTIONS.md, choix d'Antoine le 9 octobre 2026), avec l'arbre doré de C3 pour la fin. Un théâtre d'ombres
  éclairé par derrière : la maison du père découpée en coupe comme une maison de poupée de papier, debout devant une
  toile sépia, puis son jardin. La caméra la parcourt en un seul plan continu, de l'entrée au salon, à la cuisine et à
  l'escalier, puis, après le pivot sur le noir, du même lieu passé dans le monde doré jusqu'au jardin et à l'arbre.
  Marionnettes à pivots aux rivets et aux tiges visibles, en poses raides de profil, sans expression.
  Une seule mise en valeur du texte, la boîte bordeaux du mot clé ; 4 traits dorés sous les pics. Le monde est écrit
  une fois dans reference/maison.html (fait au pilote de l'étape 4 à partir de styleframes/_ombres.js), copié tel
  quel par chaque séquence.
unit: 1920×1080, 30 i/s
principle: lisible sans le son · une seule chose à regarder · un seul accent dans le conte, l'or · la voix déclenche chaque révélation

colors:
  toile: "#EFDDB8"           # la toile sépia éclairée par derrière (le ciel, le fond des pièces allumées)
  toile-centre: "#FFF3D6"    # cœur lumineux de la toile, derrière le sujet du plan
  toile-2: "#C9A46E"         # bord de la toile, anneau du vignettage chaud
  brume: "#8A6440"           # brumes brun moyen, décor lointain (plan 3)
  brume-2: "#5E4128"         # brume dense et papier peint ; textes secondaires de la carte de fin
  ombre: "#1B120B"           # LES silhouettes : marionnettes, maison, meubles, arbre (plan 2)
  ombre-2: "#2A1C11"         # silhouettes vues à travers une vitre
  ombre-sol: "#0F0905"       # le sol au premier plan, qui porte la bande des sous-titres
  creme: "#FFF4DC"           # la lumière : halo des lampes, vitres, texte des sous-titres, texte du bouton
  or: "#C98A2E"              # L'accent du conte : flamme des lampes, reflet du dessin, maillon qui accroche la lumière, traits des pics, monde doré
  or-clair: "#E0A84A"        # lueur du monde doré, poussière d'or, chiffre de la preuve, lettres de l'Intelligence Artificielle
  nuit: "#3E2812"            # toile assombrie du monde doré (dégradé #7A5426 au centre vers #0E0804 au bord, kit defs nuit)
  bordeaux: "#7A1E2E"        # boîte du mot clé et carte de fin (signature, bouton), rien d'autre
  bordeaux-clair: "#9B2F3F"  # état pressé du bouton

# Fichiers woff2 locaux seulement (assets/fonts/, fontsource) ; aucun @import réseau.
fonts:
  Fraunces: { files: ["assets/fonts/fraunces-latin-600-normal.woff2 (600)", "assets/fonts/fraunces-latin-700-normal.woff2 (700)"] }
  DM Sans: { files: ["assets/fonts/dm-sans-latin-500-normal.woff2 (500)", "assets/fonts/dm-sans-latin-700-normal.woff2 (700)"] }
  Caveat: { files: ["assets/fonts/caveat-latin-700-normal.woff2 (700)"] }

typography:
  subtitle:   { fontFamily: "DM Sans", px: 60, weight: 500, lineHeight: 72, note: "la phrase de la voix EN BAS AU CENTRE (haut à y 896, bande y 890 à 980 qui ne porte rien d'autre), 45 signes au plus par morceau (une phrase plus longue se joue en morceaux qui se remplacent), mot par mot sur ses temps ; creme sur le sol ombre-sol, ombre 0 2px 12px ombre-sol à 90 %. Le mot paraît en 0,12 s : opacité 0 → 0,35 → 1, y +6 → 0, échelle 1,04 → 1, flou 4 → 0 px. Jamais en haut à gauche. Masqué pendant la preuve (séquence 11) et la carte de fin." }
  key-box:    { fontFamily: "DM Sans", px: 60, weight: 500, note: "UN mot ou groupe par phrase : fond bordeaux, texte creme, marge 4 14 8 px, coins 6 px ; la boîte se trace depuis la gauche (scaleX 0 → 1, 0,16 s power3.out) 0,04 s avant son mot. Pas de point final collé à la boîte quand le mot clé finit la ligne." }
  peak:       { note: "4 pics seulement ([trait : …]) : un coup de pinceau effilé or (6 px au centre, 1 px aux bouts) sous le mot, tracé depuis la gauche en 0,4 s power2.out, qui reste jusqu'à la sortie de la phrase." }
  type:       { fontFamily: "Fraunces", px: 84, weight: 600, lineHeight: 1.1, note: "DEUX moments typographiques, qui riment : « Interminable Attente » (séquence 4) et « Intelligence Artificielle » (séquence 10). Lettres de papier découpé pendues à des fils (kit lettres), sur deux lignes, le bloc centré, 84 px au plus à l'écran pendant toute la poussée de caméra (taille = 84 / échelle la plus forte), initiales I et A en 700 ; ombre sur la toile en séquence 4, or-clair lumineux en séquence 10. Un mobile : les fils du premier mot descendent du haut du cadre (ou de la branche), le second mot pend au premier (initiales sur un même axe, ses fils partent du bas du premier mot), aucun fil ne traverse un mot ; pendant ce moment le sous-titre ne montre que le début de la phrase (« Pour sa fille, IA voulait dire », « Désormais, IA voulait dire »)." }
  proof:      { fontFamily: "Fraunces", px: 150, weight: 700, note: "le chiffre « 10 h » de la preuve, or-clair, qui roule de 0 à 10 (séquence 11), centré à (960, 230) de l'écran, dans le ciel au-dessus du faîte du toit (au recul final, le toit occupe l'écran de y 448 à 523) ; dessous deux lignes DM Sans 500 40 px creme : « gagnées chaque semaine » puis « par la dernière dirigeante formée » (texte exact du site)." }
  signature:  { fontFamily: "Caveat", px: 120, weight: 700, note: "« Antoine Contino » en bordeaux sur la toile claire de la carte de fin, révélé par un masque qui avance de gauche à droite en 0,8 s power1.inOut (vitesse d'une main) ; « formateur IA » en DM Sans 500 34 px brume-2 dessous." }
  cta:        { fontFamily: "DM Sans", px: 32, weight: 700, note: "« Réserver un audit IA de 30 minutes » en creme sur le bouton bordeaux ; dessous « calendly.com/antoine-cntno/30min · antoinecontino.fr » en DM Sans 500 24 px brume-2." }

components:
  ground-toile:
    background: "plan 4 de chaque séquence, calque class=\"clip\" de toute sa durée : la toile sépia (dégradé radial toile-centre → toile → toile-2 → #5B3A20 vers le bord, centré sur le sujet du plan), fibres à 16 %, grain à 38 % en multiply, vignettage chaud. Cadrages serrés (échelle ≥ 1,4) : le cœur se resserre (r ≈ 900 px) et les bords s'assombrissent. Monde doré : la même toile en palette nuit (cœur r 1 500 px, comme A3 et C3). Carte de fin : taches et fibres à moitié. Jamais sur #root."
  grain:
    look: "une tuile de grain pré-rendue par plan de profondeur (≤ 600 Ko chacune), portée PAR le plan : elle glisse avec lui pendant les dérives et la parallaxe. Son décalage change toutes les 2 images (hash de l'indice d'image). Aucun grain fixé à l'écran."
  flamme:
    look: "la lumière vacille comme une flamme : un multiplicateur 1 ± 0,03 de la luminosité de la toile et des halos, environ 7 Hz : une clé toutes les 4 images, tirée d'un hash de l'indice d'image et alternée au-dessus puis au-dessous de 1, reliées en ligne droite (aucun lissage lent, qui se lirait comme une respiration). Les halos des lampes et de l'or suivent le même multiplicateur."
  house:
    description: "la maison en coupe : un cadre ombre percé de cases où passe la lumière de la toile (frame.md § world). Une case allumée = toile claire derrière la pièce ; une case éteinte = voile #140B05 à 58 à 66 % sur la case. Papier peint discret (motif brume-2 à 9 %) et lambris (brume-2 à 16 %) dans les pièces. Cloisons, planchers, chambranles, escalier, meubles : silhouettes ombre nettes, avec des ajours (panneaux de porte, croisillons des fenêtres, barreaux de rampe, pois du champignon) qui laissent passer la lumière."
  case-switch (signature 1, « la case qui s'éteint ») :
    motion: "une case s'éteint : le voile monte de 0 à 62 % en deux crans (0,06 s expo.out chacun, 0,2 s d'écart), la flamme de la lampe de la pièce se tasse ; une case se rallume : le voile retombe à 0 en un cran et la toile derrière passe au doré (monde doré) avec une bouffée de poussière d'or. Jamais un fondu lent."
  pere:
    description: "kit pere, échelle 0,66 (406 u de haut, il passe sous le linteau de la porte et des baies, à y 470 : 24 u de jour), la pile portée sous le bras, calée contre la hanche (y 663 à 763 debout : elle ne croise ni linteau ni appui de fenêtre), tête de profil sans expression, manteau raide qui s'arrête au genou, rivets brume-2 aux épaules, coudes, hanches et genoux ; deux tiges fines (2,2 u) partent du dos et du poignet avant (du coude avant, vers l'arrière, quand le poignet passe devant quelqu'un : à genou) et descendent jusqu'au sol (y 900), où elles entrent dans la fente de la scène, même quand la marionnette penche ou grandit ; elles ne traversent jamais la bande des sous-titres. À genou : cuisse avant à l'horizontale sous un manteau raccourci, tibia arrière à plat. Effacé (flou, pâle), son bras arrière reste net : la chaîne garde son point d'attache. Debout ou en marche, le bras arrière s'écarte du manteau (poignet hors de la silhouette du manteau) pour que la chaîne se lise attachée au poignet. Assis (salon, cuisine) : kit chaise sous lui, cuisses à l'horizontale, tourné vers la gauche vers sa lampe. Poses tenues et changées à 12 i/s. Chaîne au poignet arrière du début du film à « pour lui » (séquence 8)."
  fille:
    description: "kit fille, échelle 0,76 (251 u de haut debout), deux couettes, robe courte, profil sans expression, rivets ; une tige fine du dos jusqu'au sol (y 900). Poses : assise par terre (salon), assise sur le tabouret avec feuille et crayon (cuisine), assise sur la marche le menton dans les mains (kit menton, escalier), debout qui agite la main, bras croisés, sur la balançoire, à genoux qui dessine. Poses à 12 i/s. Jamais doublée, jamais d'écho sombre."
  horloge (le Temps perdu):
    description: "kit horloge, échelle 0,70 : comtoise trapue sur deux roulettes de bois, ventre bombé avec sa fenêtre en lentille, balancier et engrenages visibles par la fenêtre, cadran r 80 (fenêtre r 58 avec ses graduations et ses deux aiguilles) centré à 270 u au-dessus du sol, couronne à pommeaux, deux bras courts à mains rondes sur tiges (épaules à 133 u du sol, bras de 69 u : la main se pose sur le dos du père assis, jamais sur son épaule ; dans une embrasure, bras rentrés contre le ventre : 137 u de large). Elle roule (roulettes qui tournent, 12 i/s), ne marche jamais. Ni capuche, ni squelette, ni faux, ni sablier. Après le pivot : silhouette inversée dorée (or, dégradé orGrad et halo pré-rendu), même dessin."
  chaine:
    description: "kit chaine : maillons de papier ajourés (rx 9, ry 14, pas 19) du poignet arrière du père à la lentille du balancier, tendue en chaînette ; elle se tend quand l'horloge recule, se détend quand elle avance. Séquence 6 : sur « chaîne », un reflet or court le long des maillons (0,4 s). Séquence 8 : sur « pour lui », les maillons éclatent en oiseaux de papier dorés qui partent vers la droite."
  devis:
    description: "kit pile et kit devis : piles de feuilles vues de profil (lames de 7 u à 1,6 u d'écart, léger désordre tiré d'un seed), feuilles ajourées de colonnes quand une feuille se tient debout face à la toile. La pile sous le bras du père à l'entrée (14 feuilles) est celle qu'il pose sur la table. Monde doré : les feuilles finies sont or, elles volent seules et deviennent le tronc de l'arbre."
  dessin:
    description: "le dessin du petit dinosaure : carte #F8EDD3 108 × 98 u cernée d'ombre 4,5 u, penchée de -4° sur ses deux punaises ; dedans le kit dino ×0,3 (bébé brontosaure, œil ajouré) sous son champignon à pois ajourés et une ligne de sol. Épinglé au mur de la cuisine derrière le père, à (2 590, 640) (séquence 3), recouvert de devis épinglés (séquence 5), retrouvé et glissé sur ses devis (séquence 6), épinglé au poteau de la clôture (séquence 9). Le second dinosaure : la même carte sur le poteau voisin, le dino tracé en lignes or, un peu plus grand (×0,36), sous un champignon."
  lettres:
    description: "kit lettres : lettres de papier découpé suspendues à des fils fins. I et A tombent d'abord seuls, initiales, puis chaque mot se déplie depuis son initiale (les lettres glissent de derrière elle, 0,03 s d'écart, 0,12 s expo.out). Le second mot pend au premier (option pendA du kit). Séquence 4 : ombre sur la toile, fils ombre. Séquence 10 : or-clair lumineux, fils or."
  balancoire:
    description: "kit balancoire à deux cordes et une planche, pendue à la branche maîtresse de l'arbre ; vue par la fenêtre du salon dans le monde sombre (ombre-2, immobile, cordes 4,5 u), seulement quand ses deux cordes et sa planche tiennent dans un même carreau de F1 (jamais une corde seule), puis dorée au jardin. Son arc rejoue celui du balancier de l'horloge (même amplitude ±18°, même période 1,6 s)."
  arbre:
    description: "l'arbre du jardin (kit arbre, h 760, penché à droite) : nu et sombre dans le monde sombre ; au monde doré, les devis finis s'empilent autour de son tronc du sol à la fourche (le tronc devient la pile, emprunt de C3), ses branches s'allument or de la fourche vers les pointes et des feuilles de papier dorées s'y posent."
  lampes:
    description: "kit lampe ×0,8, allumée : abat-jour ombre, flamme or et son halo creme (#flamme) qui suit le multiplicateur flamme. L1 au salon, L2 à la cuisine. L2 s'éteint à la fin de la séquence 6 et sa nuit gagne tout le cadre (tache d'encre)."
  poussiere:
    description: "poussière d'or (kit etincelles) : points or-clair de 2 à 5 u qui dérivent lentement vers le haut (8 à 20 u/s), seed fixe ; seulement dans le monde doré et au relèvement des cases."
  oiseaux:
    description: "oiseaux de papier : deux triangles d'aile pliés (ombre au monde sombre, or au monde doré) qui battent à 12 i/s (3 poses) en vol courbe. Ils servent deux fois : la chaîne qui éclate (séquence 8) et le balayage de la carte de fin (séquences 11 et 12), où les plus proches passent en avant-plan, grands et flous."
  button:
    description: "UN bouton : rectangle bordeaux 640 × 96 u coins 10, texte cta creme ; il arrive ×1,1 et flou 6 px puis se pose (0,15 s expo.out). Clic : pression ×0,94 (0,06 s), couleurs bordeaux → bordeaux-clair → creme → bordeaux (0,27 s), onde bordeaux qui s'ouvre et s'efface (0,45 s ; un anneau arrondi qui s'écarte du bouton de 28 px au plus, sans toucher les textes voisins), retour à ×1 (0,12 s)."
  cursor:
    description: "curseur flèche de papier découpé (ombre à liseré creme 2 u, petit rivet), 34 × 44 u, ombre douce ; aucune tige. Il arrive en UN mouvement courbe (0,45 s power3.out en x, power2.out en y) depuis le bas droit et clique directement."
  end-card:
    description: "la toile claire du conte (ground-toile, palette du début) avec la signature, « formateur IA », le bouton, la ligne d'adresses, centrés ; tenue vivante : la flamme de la toile, le grain qui glisse, la poussière d'or qui retombe, un dernier oiseau de papier qui traverse petit en haut à droite ; puis le noir à 57,10."

world:
  camera: "kit de reference/maison.html : #stage > #drift > #cam > #world ; cam(x, y, s) amène le point (x, y) du monde au centre du cadre (960, 540) à l'échelle s, un seul objet proxy écrit par un seul onUpdate. Dérive permanente sur #drift (10 à 30 u/s ou 1 à 3 %/s, linéaire) ; crans, whips, plongées et reculs sur #cam (expo.inOut, flou de caméra 6 à 12 px au milieu, seulement sous l'échelle 3). La caméra est fluide à 30 i/s ; les poses des marionnettes changent à 12 i/s. Toute la caméra du film avance de gauche à droite ou s'enfonce, avec deux reculs francs qui montrent le tout : le recul « Soir après soir » (séquence 5) et le recul final sur la maison relevée (séquence 11). Jamais d'aller-retour sur le décor."
  maison (monde unique, 6 200 × 1 080 u ; la toile du ciel monte jusqu'à y -1 600 et le sol descend jusqu'à y 1 800) :
    sol: "y 900 sur toute la largeur ; sous le sol, ombre-sol jusqu'à y 1 800 (il remplit la bande des sous-titres à tout cadrage)."
    cadre: "la maison x 60 à 3 470, y 92 à 948, toit à deux pentes (faîte à (1 765, -120), avant-toits à (20, 100) et (3 510, 100)). Rez-de-chaussée y 438 à 900, étage y 132 à 392 (plancher entre les deux). Les cloisons E/S (x 870 à 916) et S/K (x 1 720 à 1 768) sont percées d'une baie (y 470 à 900, linteau à y 470, comme la porte : 430 u de passage) où passent les personnages. Sous y 900, tout est ombre-sol, seuil de la maison compris (aucune marche de ton dans la bande des sous-titres) ; aucune lumière ne déborde sous y 900, sauf la lumière d'or du cadran au pivot (séquence 7 après la sortie de « idée », début de la 8), quand la bande ne porte aucun sous-titre ; l'avant-plan (plan 1) est coupé au sol de l'écran."
    E (entrée, x 120 à 870): "porte d'entrée : chambranle x 320 à 510, ouverture x 336 à 494 et y 470 à 900 (430 u, plus haute que le père), corniche à y 446, seuil à y 893, battant ajouré qui s'ouvre vers la pièce (il pivote sur le montant gauche, kit A1). Dehors par la porte (plan 3) : lumière du soir #FFF4DA → #D9B784, arbre et clôture lointains en brume. Patère à (230, 600), à gauche de la porte, avec le petit manteau de la fille et son écharpe : le père ne passe jamais devant. Lambris à y 768."
    S (salon, x 916 à 1 720): "fenêtre F1 à quatre carreaux, x 960 à 1 170 et y 448 à 640 (appui à 647 : la tête de la fille à genoux et la pile du père passent dessous) ; dehors, la balançoire immobile pendue à une branche nue (plan 3, vue dans les carreaux de droite). La fille assise par terre à (1 060, 900), sa balle (r 26) à (1 150, 874). Secrétaire x 1 220 à 1 400 (plateau y 770 ; caisson à gauche, les jambes du père passent dessous à droite), lampe L1 à (1 244, 770), la pile posée vers x 1 314, le dossier ouvert vers x 1 388. Le père assis à (1 440, 900), tourné vers la gauche. La balle, qui roule vers lui, s'arrête au pied de sa chaise à (1 520, 874), entre sa tige et l'horloge. L'horloge à (1 620, 900)."
    K (cuisine, x 1 768 à 3 420): "tabouret de la fille à (1 940, 900). Table x 2 060 à 2 380 (plateau y 760), lampe L2 à (2 090, 760), pile de devis sur la table x 2 155 à 2 285. Le père assis à (2 460, 900), tourné vers la gauche, dos au mur ; au monde doré, l'horloge travaille à sa place, à (2 510, 900), devant la chaise. Le dessin épinglé au mur derrière lui à (2 590, 640), les devis épinglés dessus à x 2 585 au plus (50 u d'air avant F2). Fenêtre F2 x 2 690 à 2 860, y 470 à 740, imposte à y 525 (deux petits carreaux en haut, une grande vitre dessous ; appui à 738-747) : la tête de l'horloge (couronne à y 555, cadran y 574 à 686) tient entière dans la grande vitre, l'appui passe derrière son ventre (crépuscule puis nuit étoilée sans lune ; jours et nuits en accéléré en séquence 5). L'horloge à (2 780, 900) devant F2. Escalier de (2 960, 900) à (3 420, 438), marches de 58 × 58 u, rampe à barreaux ajourés (plan 1), poteau de départ bas (boule à y 762) : la fille qui passe tête basse devant F2 vers l'escalier, à x 2 914, garde du jour devant et derrière sa tête ; la fille assise sur la deuxième marche à (3 060, 842). Séquence 4 : le voile de la case s'amincit autour de la marche (trou du voile, kit), le mur derrière les lettres reste clair."
    étage: "chambre des parents au-dessus de E (lit à (600, 392)), bureau au-dessus de S, chambre de la fille au-dessus de K (petit lit à (2 300, 392)), grenier sous le toit ; éteint jusqu'au relèvement doré de la séquence 11."
    J (jardin, x 3 470 à 6 200): "herbes le long de y 900 ; l'arbre au pied (4 300, 900), branche maîtresse vers la droite jusqu'à (5 450, 300) ; la balançoire pendue à la branche, pivot (4 745, 330), planche à y 790 ; l'horloge au pied de l'arbre à (4 020, 900) à la séquence 9 (la petite pile d'or des devis finis à x 4 122, 20 u de sombre de chaque côté), puis à la clôture à (5 520, 900) ; clôture x 5 050 à 6 000 (h 90), deux poteaux porte-cartes à (5 200, 900) et (5 360, 900), en T et hauts seulement quand une carte y est épinglée (sinon à la hauteur de la clôture), cartes à y 770 ; la famille à (5 070, 900), à gauche de la première carte, aux séquences 10 et 11 ; collines et arbres lointains en brume (plan 3). Monde doré : au moins 20 px de sombre entre deux silhouettes d'or (le père qui pousse la balançoire à x 4 555 penché de 4°)."
  framings: "cadrages de référence (marges gauche et droite égales ; le sol à l'écran à y 880 au plus, soit y_cam ≥ 900 - 340 / s) : porte et père qui entre cam(560, 680, 1.4) · entrée cam(620, 660, 1.3) · fille et fenêtre du salon cam(1 080, 700, 1.55) · père au secrétaire cam(1 450, 700, 1.6) · horloge du salon cam(1 600, 700, 1.65) · fille au tabouret cam(1 960, 700, 1.6) · père à la table cam(2 330, 690, 1.55) · horloge devant F2 cam(2 780, 690, 1.55) · fille sur la marche cam(3 060, 670, 1.45) · cuisine entière cam(2 640, 600, 1.0) · père et fille cam(2 560, 690, 1.3) · dessin et père cam(2 600, 690, 1.6) · chaîne et horloge cam(2 780, 700, 1.7) · cadran dans le noir cam(2 780, 630, 1.93) puis jusqu'à l'échelle 2,4 (exception à la règle du sol : dans le noir, la bande reste ombre-sol, le sol de l'avant-scène à y 880 coupe le bas de l'horloge) · cuisine dorée cam(2 660, 660, 1.35) · arbre et balançoire cam(4 500, 620, 1.15) · clôture et cartes cam(5 280, 700, 1.5) · lettres sous la branche cam(5 300, 610, 1.15) · tout le monde relevé cam(2 850, 150, 0.34)"
  plan-1: "objets d'avant-plan (plan 1, parallaxe ×1,8, sombres et flous 10 à 22 px, coupés par le bord du cadre), placés dans leur plan à l'abscisse du monde où la caméra les croise : entrée, le montant d'une porte intérieure (x 90) et un portemanteau sur pied (x 860) ; salon, le dossier d'un fauteuil (x 1 240) et la cloison S/K vue de près (x 1 744) ; cuisine, une suspension de casseroles qui pend du plafond (x 2 200, haut du cadre) et la rampe de l'escalier (x 3 000 à 3 400) ; jardin, des herbes hautes (bas du cadre) et une branche basse (x 4 900, haut du cadre) ; noir du pivot, la fumée de la lampe éteinte (trois volutes courtes, discontinues, qui naissent en bas à gauche du côté de L2 et montent en biais en s'élargissant, jamais un trait continu). Tout le plan 1 est coupé au sol de l'écran (rien dans la bande des sous-titres)."
  depth: "quatre plans dans chaque plan tenu, chacun avec son propre grain : plan 1 avant-plan sombre et flou (montants de porte, cloisons, rampe d'escalier, herbes hautes, branches ; flou 10 à 22 px pré-rendu, jamais plus de 1 800 px de large) coupé par le bord du cadre, parallaxe ×1,8 ; plan 2 le sujet net (la maison et ses meubles, les marionnettes), ×1 ; plan 3 la brume (dehors par les fenêtres et la porte, collines, arbres lointains, nappes brume), ×0,5 ; plan 4 la toile lumineuse, ×0,2."
  render: "piste à tester au pilote : un canvas 2D par plan, dessiné par une fonction pure render(t) pilotée par un proxy de la timeline GSAP, avec un modèle de lumière simple ; le HTML garde les sous-titres, les moments typographiques, la preuve et la carte de fin. Textures pré-rendues une fois (budget en mémoire décodée : ≤ 25 Mo chacune, ≤ 250 Mo pour la page, sprites dorés compris ; mesuré par OM.textures()). Les silhouettes dorées sont cuites en sprites (un par liste et par palier d'échelle) ; temps de dessin visé ≤ 35 ms par image. On garde le chemin le plus rapide mesuré (rendu de 5 s du style complet avec --workers 3). Aucun filtre SVG vivant sous une caméra qui bouge, aucun flou ni filtre de caméra au-dessus de l'échelle 3, aucun objet flou de plus de 1 800 px, aucun grain fixé à l'écran."

negative:
  - "Rien du film de référence hors sa technique : aucun personnage, objet, symbole, lieu ou plan repris (ni frères, ni Mort, ni capuche, ni squelette, ni griffes, ni faux, ni pont, ni rivière, ni baguette, ni pierre, ni cape, ni symbole, ni départ final devant un grand soleil) ; aucun nom de film ou de saga ; aucun son du clip. Aucun disque de soleil ou de lune derrière un départ."
  - "Aucune tige seule à l'écran (elle se lirait comme une baguette) : chaque tige part d'une marionnette et descend jusqu'au sol. Aucun manteau qui flotte comme une cape ; aucun portique nu ; balançoire toujours à deux cordes."
  - "Aucune seconde mise en valeur : la boîte bordeaux est la SEULE façon de souligner un mot du sous-titre, le trait or marque les 4 pics ; aucun autre texte coloré."
  - "Bordeaux réservé à la boîte du mot clé et à la carte de fin ; or réservé au conte (flammes, reflets, traits des pics, monde doré)."
  - "Aucune grande phrase : sous-titre 60 px, moments typographiques 84 px au plus ; aucun mot géant, aucune grosse boîte. Rien d'autre que le sous-titre dans la bande y 890 à 980 (seule exception : la lumière d'or du pivot, quand la bande est vide) ; jamais de sous-titre en haut à gauche."
  - "Une seule chose à regarder : la caméra isole le sujet de la phrase ; marges égales ; jamais d'aller-retour du décor ; une transition = un geste lisible en une seconde."
  - "Aucun décor sans sens ni symbole abstrait ; aucune ligne du décor qui traverse une phrase."
  - "Aucun prix, aucune formule annuelle, aucune durée en heures de la journée de formation, aucun courriel, aucun téléphone, aucun nom ni lieu de client ; aucun outil d'IA nommé, aucun logo."
  - "Aucun grain fixé à l'écran. Les marionnettes changent de pose à 12 i/s, sans glissement continu et sans expression de visage."
  - "Aucune silhouette dédoublée, aucun écho sombre d'un personnage ; aucun objet doublé pendant une couture."
  - "Pas d'Inter, Space Grotesk, Geist, system-ui. Pas d'emoji. Pas de Math.random (seeds), pas de repeat:-1, pas d'animation CSS, pas d'ease rebondissant ou élastique."
  - "Jamais d'animation de letterSpacing ; jamais de tween de width, height, top, left ; pas de backdrop-filter ; pas de clip-path polygon interpolé."
  - "Aucun texte visible qui ne soit pas cité dans les lignes Scene ou dans les composants ci-dessus."
---

# Le Temps perdu : charte du film

**Le monde sombre.** Un soir, la maison du père en coupe, debout devant la toile sépia éclairée par derrière : chaque
pièce est une case de lumière. Le père entre avec sa pile de devis ; derrière lui, le Temps perdu, une horloge comtoise
trapue sur roulettes, passe la porte, enchaînée à son poignet. Au salon, la fille attend avec sa balle ; il ouvre un
dossier, l'horloge prend une heure et la case s'éteint d'un cran. À la cuisine, elle attend avec sa feuille ; il ouvre
ses devis, l'horloge prend la soirée, la nuit tombe dans la fenêtre. Sur la marche de l'escalier, les lettres I et A
tombent au-dessus d'elle et se déplient en « Interminable Attente ». Soir après soir, la cuisine passe en accéléré et le
père s'efface : il s'éloigne de la toile et son ombre grandit en pâlissant dans le flou. Elle agite la main devant son
visage ; seul le balancier répond. Elle retrouve leur dessin sous les devis épinglés, le glisse sur ses devis ; il
revient net contre la toile et voit la chaîne. La lampe s'éteint, la nuit gagne tout.

**Le pivot.** Dans le noir, le cadran de l'horloge s'allume : le Temps perdu a une idée. La lumière d'or l'envahit.

**Le monde doré.** La même cuisine en silhouettes inversées lumineuses sur la toile assombrie. L'horloge se met au
travail et la chaîne éclate en oiseaux de papier. Les devis finis volent seuls par la fenêtre et s'empilent autour du
tronc de l'arbre du jardin, qui devient l'arbre doré. Le père pousse la balançoire dans l'arc du balancier ; ils
dessinent un second dinosaure à côté du premier. Les lettres I et A retombent, dorées, et se déplient en
« Intelligence Artificielle ». La caméra recule : toutes les cases de la maison se rallument en or, le chiffre de la
preuve roule dans le ciel. Les feuilles de l'arbre s'envolent en oiseaux et balaient le cadre jusqu'à la carte de fin,
sur la toile claire du début : la signature bordeaux, le bouton, la ligne d'adresses, le clic.

Tout ce qu'on lit en bas est en DM Sans, mot par mot, avec un seul mot clé par phrase dans une petite boîte bordeaux.
Fraunces sert aux deux moments typographiques et au chiffre de la preuve ; Caveat à la signature.
