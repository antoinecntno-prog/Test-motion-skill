---
format: 1920x1080
duration: "57.10s"
message: "Le Temps perdu change de camp : l'IA prend le travail écrit du dirigeant et lui rend ses soirées."
arc: Hook → Problem → Pivot → Turn → Demo → Payoff → Reassurance → CTA
audience: "dirigeants de PME dont une bonne part de la semaine passe par l'écrit (devis, chiffrages, comptes rendus, relances clients) et les coachs qui les accompagnent, sur la page LinkedIn d'Antoine Contino, formateur IA"
mode: autonomous
captions: disabled
music: "pre-mixed with voice and SFX in assets/audio/mix.wav (mounted at root by the orchestrator)"
direction: "A « La maison en coupe » (DIRECTIONS.md) avec l'arbre doré de C3 pour la fin, choisie par Antoine le 9 octobre 2026"
styleframes: "styleframes/png/A1.png (4,2 s), styleframes/png/A2.png (19,6 s), styleframes/png/A3.png (39,5 s), styleframes/png/C3.png (l'arbre doré, 39,5 s)"
patterns: ../patterns/STORYBOARD-CRAFT.md, ../patterns/PATTERNS.md
---

## Video direction

- **Un seul monde** (frame.md) : la maison du père en coupe, maison de poupée de papier debout devant une toile sépia éclairée par derrière, puis son jardin (6 200 × 1 080 u). Séquences 1 à 6 = DOULEUR dans le monde sombre (entrée, salon, cuisine, escalier) ; séquence 7 = PIVOT dans le noir ; séquences 8 à 11 = SOLUTION dans le monde doré (la cuisine et le jardin, puis toute la maison relevée) ; séquence 12 = FIN sur la toile claire du début. Chaque séquence peint sa propre toile (plan 4) sur un calque `class="clip"` de toute sa durée.
- **Théâtre d'ombres** : silhouettes brun noir découpées, marionnettes à pivots aux rivets et aux tiges visibles, têtes de profil sans expression, poses tenues et changées à 12 i/s pendant que la caméra glisse à 30 i/s ; quatre plans de profondeur portant chacun leur grain, sous une lumière qui vacille comme une flamme (frame.md, composants flamme et grain).
- **Coutures invisibles** : toutes les séquences entrent en `cut` ; chaque couture tombe au sommet du flou d'un mouvement de caméra (whip, cran, recul, plongée, grue) et le `handoff_out` de la séquence N est recopié mot pour mot dans le `handoff_in` de N+1. Les transitions se construisent dans l'image : la cloison floue qui balaie le cadre (5.25, 10.76), les lettres qui volent en feuilles (20.38), la nuit d'encre qui part de la lampe (31.15), la lumière d'or du cadran (34.60), la file de feuilles qui vole au jardin (38.03), les oiseaux de papier qui balaient le cadre (53.10). Exception voulue : 34.60, coupe franche sur la lumière d'or du cadran (le cadre entier est la même lumière des deux côtés).
- **Texte** (lisible sans le son) : chaque phrase de la voix est un sous-titre en bas au centre (bande y 890 à 980, rien d'autre dedans), mot par mot sur les temps de chaque séquence (`mot@secondes`, temps locaux), 45 signes au plus par morceau. Un seul mot ou groupe par phrase dans la boîte bordeaux ([boîte : …]). Aucun autre texte coloré. Deux moments typographiques qui riment, lettres de papier pendues à des fils, Fraunces 84 px : « Interminable Attente » (séquence 4, ombre) et « Intelligence Artificielle » (séquence 10, or). La preuve (séquence 11) s'écrit dans le ciel et remplace le sous-titre.
- **Pics** : 4 traits d'or [trait : …] : « travail » (1.38), « Attente » (19.84), « Artificielle » (46.80), « rendre » (48.20).
- **Une seule chose à regarder** : chaque plan isole le sujet de la phrase ; la caméra avance de gauche à droite dans la maison puis au jardin, ou s'enfonce ; deux reculs francs montrent le tout quand il a du sens (« Soir après soir », 20.26 ; la maison relevée, 49.07) ; jamais d'aller-retour ; marges gauche et droite égales ; au cadrage de référence, le sol reste au-dessus de y 880 à l'écran (frame.md § framings).
- **Vraies interfaces** : aucune (conte). Les devis sont des feuilles de papier découpé ajourées de colonnes, sans texte lisible, sans nom d'outil.
- **Parallaxe** : pendant chaque dérive, les quatre plans glissent à des vitesses différentes : avant-plan flou (frame.md § plan-1) ×1,8, sujet ×1, brume ×0,5, toile ×0,2.
- **Grammaire de mouvement** : deux vitesses, gestes de 1 à 6 images (expo.out) et dérives linéaires qui ne s'arrêtent jamais ; la zone 0,3 à 0,9 s est réservée à la caméra et au curseur (expo, power3, power4) ; les objets arrivent trop grands et flous puis se posent ; les marionnettes changent de pose image par image à 12 i/s ; aucune tenue figée ; aucune transition « effet ».
- **Texte visible** : exactement le texte cité dans les lignes Scene et les composants de frame.md, rien d'autre.
- **Négatifs** : diaporama (tout à t = 0), écran de veille, silhouette dédoublée ou écho sombre, texte coloré à la place de la boîte, grande phrase, mot géant, symbole abstrait, curseur qui hésite, plusieurs objets qui bougent pendant une couture, tout élément du film de référence hors sa technique (frame.md § negative), tige seule, disque de soleil ou de lune.

**MONDE**
- Acte 1, douleur (0.00 à 31.37) : la maison en coupe, monde sombre ; stations entrée E (porte (415, 706), père (700, 900)), salon S (fille (1 060, 900), secrétaire (1 380, 770), père (1 500, 900), horloge (1 620, 900)), cuisine K (tabouret (1 940, 900), table (2 230, 760), père (2 460, 900), dessin (2 620, 640), horloge (2 780, 900) devant F2), escalier (marche (3 060, 842)) ; fond la toile sépia grainée, au cœur lumineux derrière la pièce du plan ; les cases s'éteignent d'un cran à chaque heure prise.
- Pivot (31.37 à 34.60) : le noir de la cuisine éteinte traversé par la fumée de la lampe, le cadran de l'horloge (2 780, 630) qui s'allume d'or.
- Acte 2, solution (34.60 à 53.10) : le même monde en palette nuit, silhouettes inversées dorées dans une poussière d'or ; stations cuisine dorée (2 660, 660), arbre d'or (4 300, 900) et balançoire (4 745, 330 → 790), clôture et cartes (5 200 et 5 360, 770), horloge (5 520, 900), la maison entière relevée cam(2 850, 150, 0.34).
- Fin (53.10 à 57.10) : la toile claire du début, la carte de fin centrée.
- Couleurs de rôle : ombre = silhouettes ; toile et creme = la lumière ; or = l'accent du conte (flammes, reflet du dessin, maillons, traits des pics, monde doré) ; bordeaux = la boîte du mot clé et la carte de fin.

**SIGNATURES**
- Mécanisme 1 « la case qui s'éteint, puis se rallume » (frame.md, case-switch) : 10.12 et 10.44 le salon perd une heure · 15.76 et 16.04 la cuisine perd la soirée · 20.68, 21.12 et 21.36 soir après soir (trois pulsations) · 31.15 la lampe s'éteint, la nuit gagne · 37.60 la cuisine se rallume en or · 49.83 à 51.30 les six cases de la maison se rallument en or (6 occurrences).
- Mécanisme 2 « le balancier » : 2.80 premier battement quand l'horloge paraît dans la porte · 9.20 il bat quand l'horloge se penche sur le père · 24.28 seul le balancier répond à la main de la fille · 31.57 il s'arrête dans le noir · 34.07 il repart, doré · 39.36 la balançoire part dans le même arc, à la même cadence (6 occurrences).
- Registres de texte : sous-titre mot à mot = opacité, montée, échelle et flou en 0,12 s ; boîte = tracée depuis la gauche (0,16 s power3.out) ; trait = pinceau d'or depuis la gauche (0,4 s power2.out) ; moment typographique = initiales qui tombent au bout de leurs fils (0,25 s power3.out) puis mots qui se déplient depuis l'initiale (0,03 s d'écart) ; preuve = chiffre qui roule ; signature = masque à la vitesse d'une main.
- Rimes : la balançoire (39.36) rejoue l'arc du balancier (2.80) ; la pile de devis portée à l'accroche (0.78) devient le tronc d'or (38.25 à 38.62) ; les lettres d'or (44.97) rejouent les lettres d'ombre (17.67) ; le second dinosaure (41.76) répond au dessin du mur (12.81, 26.76) ; les cases rallumées (49.83) rejouent les cases éteintes (10.12) ; la toile claire de la fin rejoue celle de l'ouverture.

**PARTITION CAMÉRA** (temps globaux) : 0.00 dérive sur la porte et le père qui entre cam(500, 690, 1.45) · 2.30 cran court sur la porte cam(564, 692, 1.58) · 5.05 whip E → S (couture 5.25) · 5.45 atterrissage sur la fille cam(1 080, 700, 1.55), dérive qui suit le père · 6.95 cran vers le secrétaire cam(1 450, 700, 1.6) · 8.70 cran vers l'horloge cam(1 600, 700, 1.65) · 10.60 whip S → K (couture 10.76) · 10.96 atterrissage sur la fille au tabouret cam(1 960, 700, 1.6) · 12.46 cran vers la table cam(2 330, 690, 1.55) · 14.31 cran vers l'horloge cam(2 780, 690, 1.55) · 16.26 cran vers l'escalier (couture 16.42) · 16.60 atterrissage sur la marche cam(3 060, 670, 1.45), poussée lente · 18.02 cran d'échelle sur les lettres · 20.26 recul (couture 20.38) · 20.83 la cuisine entière cam(2 640, 600, 1.0) · 22.68 poussée vers le père et la fille cam(2 560, 690, 1.3) · 25.23 cran vers le mur au dessin (couture 25.40) · 25.63 cam(2 600, 690, 1.6) · 27.60 cran de suivi vers le père cam(2 560, 705, 1.72) · 30.25 pan le long de la chaîne cam(2 780, 700, 1.7) · 31.25 plongée vers le cadran (couture 31.37) · 31.37 plongée lente dans le noir · 34.22 plongée dans la lumière du cadran jusqu'à l'échelle 2,4 · 34.60 coupe franche, la lumière se resserre sur la cuisine dorée cam(2 660, 660, 1.35) · 36.80 cran court sur la pile cam(2 720, 670, 1.45) · 37.70 whip K → J (couture 38.03) · 38.25 atterrissage sur l'arbre cam(4 500, 620, 1.15) · 40.48 cran vers la clôture cam(5 280, 700, 1.5) · 43.33 grue vers la branche (couture 43.67) · 44.02 cam(5 300, 610, 1.15) · 45.97 cran d'échelle sur les mots · 47.62 cran vers l'horloge et la famille cam(5 400, 690, 1.35) · 49.07 recul final (couture 49.47) · 50.07 la maison relevée cam(2 850, 150, 0.34) · 52.77 vague d'oiseaux vers la caméra (couture 53.10) · 53.10 toile claire, dérive d'échelle · 56.80 le noir monte.

**VOIX** : minutage dans onsets.json (DIRECTIONS.md). Silences de plus de 0,4 s, chacun écrit comme un plan avec son action : 2.06 à 2.52 (le père s'arrête au milieu de l'entrée, une ombre bouche la lumière de la porte) · 6.67 à 7.10 (la balle roule, cran vers le secrétaire) · 8.57 à 9.02 (cran vers l'horloge, l'horloge se penche) · 10.46 à 11.05 (whip vers la cuisine, atterrissage sur la fille) · 12.17 à 12.59 (cran vers la table, la pile tombe) · 16.08 à 16.76 (la fille passe tête basse, cran vers l'escalier) · 20.08 à 20.68 (recul, les lettres volent en feuilles vers le mur) · 22.57 à 25.51 (gag muet : la main devant le visage, seul le balancier répond, les bras croisés, le regard vers le mur) · 27.50 à 27.93 (elle revient vers le père, le dessin serré contre elle) · 29.16 à 29.62 (l'ombre du père revient d'un cran) · 30.89 à 31.84 (la lampe vacille et s'éteint, la nuit d'encre gagne, la fumée passe, la plongée commence) · 33.40 à 34.96 (l'or envahit l'horloge, la lumière déborde, coupe, elle se resserre) · 37.82 à 38.25 (whip vers le jardin, les feuilles s'enroulent au tronc) · 40.23 à 40.66 (la balançoire revient, cran vers la clôture) · 43.19 à 44.15 (le second dessin brille, grue vers la branche) · 49.11 à 49.83 (recul final, la maison paraît) · 52.75 à 57.10 (les oiseaux, la carte de fin, le clic, la tenue vivante, le noir).

**COUPES** (voix narrative, quota 0 à 4) : 34.60 · « L'horloge » (34.96) · changement d'acte, du pivot à la solution, sur la lumière d'or du cadran (le cadre entier est la même lumière des deux côtés). Toutes les autres jonctions sont des coutures de caméra ou d'objet.

**RYTHME** : douleur (0 à 31.37) 15 plans = 4,8 plans / 10 s, un événement toutes les 0,2 à 0,4 s ; pivot 2 plans ; solution (34.60 à 53.10) 8 plans = 4,3 plans / 10 s ; fin (53.10 à 57.10) 3 plans.

**SON** (proposition, verrouillée à l'étape 5 ; l'image ne bouge pas pour le son ; 4 whooshes, 1 scintillement ; familles : papier, flamme, vent, ailes, bois des tiges et des roulettes) : vent du soir par la porte de 0.06 à 4.64 · bois (le battant s'ouvre) 0.06 · pas, clac de bois des tiges 0.28, 0.78, 1.62 · papier (la feuille glisse) 1.38 · papier (elle se pose) 1.90 · tic-tac de bois 2.80 · roulettes de bois 2.94 · maillons de papier qui se tendent 3.41 · tic 3.84 · roulettes 4.14 · bois sourd (le battant se ferme) 4.64 · whoosh court de papier 5.05 · bois léger (elle se met à genoux) 5.66 · pas, bois des tiges 5.82, 6.10, 6.37 · balle qui tombe et roule, bois mat, de 6.48 à 7.05 · roulettes 6.65 · papier lourd (la pile posée) 7.10 · bois (la chaise) 7.50, 7.70 · papier (le dossier s'ouvre) 7.92, 8.12 · souffle de flamme 8.45 · tic-tac 9.20 · cliquetis de bois de l'aiguille de 9.90 à 10.40 · souffle de flamme qui se tasse 10.44 · whoosh court de papier 10.60 · bois (la chaise du salon) 11.20 · pas, bois des tiges 11.60, 11.86, 12.06 · crayon sur papier 11.80 · roulettes 12.36 · papier lourd (la pile tombe) 12.59 · bois (la chaise) 12.96, 13.18 · papier (l'éventail) 13.42, 13.62 · roulettes 14.01 · tic-tac 14.68 · cliquetis rapide des aiguilles de 15.56 à 16.16 · vent de nuit dans F2 15.56 · pas légers 15.76, 16.01 · souffle de flamme qui se tasse 16.04 · vent de nuit lointain dans F2 16.76 · tic-tac lointain 16.90, 17.42 · fils de bois léger 17.67 · papier 17.87 · fils qui se tendent, bois léger, 18.48 · papier (les mots se déplient) 19.00, 19.84 · tic-tac lointain 19.32 · bois léger (le talon) 19.52 · papier (les lettres deviennent des feuilles) 20.48 · punaises, bois sec, 20.68, 21.12, 21.36 · tic-tac accéléré de 20.68 à 21.58 · souffle de flamme 21.58 · pas légers 22.93, 23.13, 23.33 · souffle de la main 23.68, 23.86, 24.04 · tic sec du balancier 24.28 · bois (le pied) 25.03 · pas légers 25.70 · papier arraché 26.24, 26.56, 26.76 · punaise, bois sec, 27.06 · feuilles qui touchent le sol 27.30 · papier (le dessin glisse) 28.32 · papier (la feuille tremble) 28.86 · maillons de papier 30.50 · chaîne tendue, papier sec, 30.82 · crépitement de la flamme de 30.95 à 31.15 · souffle (la lampe s'éteint) 31.15 · la musique se tait à 31.15 · dernier tic 31.57 · clac de bois des aiguilles 32.84 · souffle de lumière 33.30 · la boîte à musique reprend, claire, sur « idée » 33.30 · montée de lumière douce (riser) de 33.47 à 34.60 · tic-tac doré 34.07 · roulettes 34.96 · bois (le père se lève) 35.20 · tampons de bois sec 35.72, 35.82, 36.00 · maillons 36.28 · battements d'ailes de 36.54 à 36.90 · papier (les feuilles se lèvent) 36.96 · ailes de papier de 37.12 à 37.70 · souffle de lumière (la case se rallume) 37.60 · whoosh de papier 37.70 · papier (la pile se pose) 38.25, 38.48, 38.62 · scintillement (l'arbre s'allume) 38.78 · corde et bois de la balançoire 39.36, 40.16 · roulettes 40.96 · crayon sur papier de 41.76 à 42.23 · fils de bois léger 44.97 · papier 45.46 · papier (les mots se déplient) 46.22, 46.80 · bois léger (les mains) 46.57 · bois léger (il hisse sa fille) 47.96 · cliquetis des aiguilles à rebours de 48.20 à 48.87 · souffle doux 48.42 · whoosh cinématique doux 49.07 · six notes de bois clair, une par case qui se rallume, de 49.83 à 51.30 · cliquetis léger du chiffre de 50.67 à 51.66 · vent doux dans l'arbre 52.48 · battements d'ailes dès 52.77 · battements d'ailes de 53.10 à 53.55 · plume sur papier de 53.50 à 54.30 · papier (le bouton se pose) 54.10 · clic de bois léger 54.90 · ailes légères 55.40.

## Frame 1: Le dirigeant passe la porte · 0.00 → 5.25

- scene: Dans l'entrée allumée de la maison en coupe, la porte s'ouvre sur le soir et le père entre de profil, la pile de devis sous le bras ; derrière lui l'horloge du Temps perdu paraît dans l'encadrement, roule dans la pièce, la chaîne de papier tendue de son balancier au poignet du père, puis la porte se referme et la caméra part en whip vers le salon
- duration: 5.25s
- transition_in: cut
- status: outline
- src: compositions/frames/01-porte.html
- voiceover: "Ce dirigeant ramenait le travail à la maison. Derrière lui, le Temps perdu passa la porte."
- type: hook
- blueprint: camera-journey (Adapt)
- focal: le père dans la porte avec sa pile, puis l'horloge qui passe la porte enchaînée à son poignet
- rules: depth-of-field-blur, sine-wave-loop
- world: dark
- handoff_in: aucun (ouverture du film) ; première image = cam(500, 690, 1.45) flou 0 : l'entrée allumée, la porte d'entrée ouverte aux deux tiers sur la lumière du soir, la silhouette du père debout dans l'encadrement, à contre-jour, entière sous le linteau, la pile de devis sous le bras ; patère au mur à gauche de la porte ; au bord droit, le début du salon et la fille assise, en partie cachés par le portemanteau flou ; sous-titre vide ; grain par plan, flamme 1 ± 0,03
- handoff_out: à 5.25 : cam(800, 695, 1.55) flou 10 px ; caméra en plein whip vers la droite (+3 500 u/s en x, power2.in puis expo.out), dérive 0 ; monde : maison en coupe, monde sombre ; entrée E allumée : porte d'entrée fermée, patère qui oscille, le père qui marche vers la droite à (820, 900) avec sa pile sous le bras, l'horloge qui roule derrière lui à (640, 900), la chaîne tendue de son balancier au poignet arrière du père ; cloison E/S et sa baie floues (plan 1) au milieu du cadre ; salon S allumé : la fille assise par terre à (1 060, 900), sa balle à (1 150, 874), la balançoire immobile dans F1, le secrétaire vide et la lampe L1 allumée, la chaise vide à (1 500, 900) ; sous-titre sorti ; grain par plan, flamme 1 ± 0,03

Word cues: Ce@0.06 dirigeant@0.28 ramenait@0.78 le@1.12 travail@1.38 à@1.62 la@1.76 maison@1.90 Derrière@2.52 lui@2.94 le@3.41 Temps@3.66 perdu@3.84 passa@4.14 la@4.44 porte@4.64

Scene 1 (0.00 à 2.30 s) : P1, le père entre avec le travail
  TEXTE ÉCRAN : sous-titre « Ce [boîte : dirigeant] ramenait le [trait : travail] à la maison. » (Ce 0.06, boîte tracée 0.24, dirigeant 0.28, ramenait 0.78, le 1.12, travail 1.38 et son trait, à 1.62, la 1.76, maison 1.90), sorti de 2.30 à 2.44 ; écart synchro (le père franchit le seuil sur « dirigeant »).
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 la porte ouverte aux deux tiers, le père à contre-jour dans l'encadrement ; 0.06 « Ce » : le battant s'ouvre en grand (pivot sur le montant gauche, 0,16 s expo.out) et un trapèze de lumière du soir se pose au sol de l'entrée ; 0.28 « dirigeant » : il franchit le seuil (pose de marche 1, 12 i/s), tête de profil vers la droite ; 0.50 la pile sous son bras se balance (rotation 3° → 0, 0,2 s) ; 0.78 « ramenait » : deuxième pas, ses tiges suivent ; 1.00 la flamme de la toile vacille ; 1.12 « le » : le courant d'air de la porte fait osciller le petit manteau de la patère, à gauche de la porte (rotation 5° → 0, finie) ; 1.38 « travail » : il remonte la pile sur son bras (y -10, 0,08 s) et la feuille du dessus glisse ; 1.62 « à » : troisième pas, la feuille tombe en tournant ; 1.76 « la » : elle plane ; 1.90 « maison » : la feuille se pose au sol, il s'arrête au milieu de l'entrée (pose raide) ; 2.10 la lumière de la porte baisse d'un cran (le soir avance).
  PISTE CAMÉRA : dérive x +28 u/s, échelle +1,5 %/s de 0.00 à 2.30, de cam(500, 690, 1.45) à cam(564, 690, 1.50) (elle suit le père vers la droite).
  COUCHES ET PROFONDEUR : avant-plan le montant flou d'une porte intérieure (x 90, flou 14 px) coupé par le bord gauche ; sujet le père net et la porte ; brume le dehors du soir par la porte (arbre et clôture lointains) ; toile claire derrière l'entrée ; couches animées 3.
  OBJET-PONT ET VECTEUR : la pile de devis sous le bras (il la posera sur la table de la cuisine, elle deviendra le tronc d'or) ; vecteur : le père marche vers la droite, la caméra le suit.
  SON : vent du soir par la porte de 0.06 à 4.64 ; bois (le battant s'ouvre) 0.06 ; pas, clac de bois des tiges 0.28, 0.78, 1.62 ; papier (la feuille glisse) 1.38 ; papier (elle se pose) 1.90.
  IMAGE CLÉ : 1.90 : l'entrée allumée, le père de profil au centre avec sa pile sous le bras, la porte ouverte sur le soir derrière lui, une feuille posée au sol ; « dirigeant » en boîte, « travail » souligné d'or.

Scene 2 (2.30 à 5.25 s) : P2, le Temps perdu passe la porte, la chaîne
  TEXTE ÉCRAN : sous-titre « Derrière lui, le [boîte : Temps perdu] passa la porte. » (Derrière 2.52, lui 2.94, le 3.41, boîte tracée 3.62, Temps 3.66, perdu 3.84, passa 4.14, la 4.44, porte 4.64), sorti de 5.05 à 5.19 ; écart : la couronne de l'horloge bouche la porte sur « Derrière » (2.52), synchro.
  ÉTAPES : 2.30 le père reste raide, il ne se retourne pas, et la caméra fait un cran court sur la porte (0,25 s expo.inOut) ; 2.52 « Derrière » : la lumière de la porte se coupe d'un coup : la couronne à pommeaux de l'horloge paraît dans l'encadrement, à contre-jour (×1,1 et flou 4 px → net, 0,12 s) ; 2.80 premier battement de son balancier dans la fenêtre du ventre (-14° → +14°, 0,4 s sine.inOut) ; 2.94 « lui » : l'horloge roule d'un cran dans l'encadrement (roulettes qui tournent, 12 i/s) ; 3.20 le père fait un pas vers la droite ; 3.41 « le » : la chaîne de papier se tend maillon par maillon du balancier au poignet arrière du père (0,015 s d'écart, 0,3 s en tout) ; 3.66 « Temps » : le cadran accroche la lumière (liseré creme) ; 3.84 « perdu » : la grande aiguille saute d'un cran ; 4.14 « passa » : l'horloge sort de la porte et roule dans l'entrée (x 415 → 600, 0,3 s, roulettes 12 i/s), dégagée du chambranle, la chaîne se détend ; 4.44 « la » : le père repart d'un pas, la chaîne se tend et tire l'horloge d'un à-coup (x 600 → 615, elle penche de -3°) ; 4.64 « porte » : le battant se referme derrière l'horloge (0,14 s expo.out), la lumière du soir se coupe ; 4.85 le petit manteau oscille dans le courant d'air ; 5.05 départ du whip vers le salon (power2.in, flou 0 → 10), la cloison E/S floue balaie le cadre ; le père et l'horloge marchent vers la droite.
  PISTE CAMÉRA : cran court d'échelle sur la porte, de cam(564, 690, 1.50) vers cam(564, 692, 1.58) de 2.30 à 2.55 (expo.inOut), puis dérive x +20 u/s, échelle +1 %/s de 2.55 à 5.05 jusqu'à cam(614, 694, 1.62) ; whip vers le salon dès 5.05 : à 5.25 cam(800, 695, 1.55) flou 10 px.
  COUCHES ET PROFONDEUR : avant-plan le portemanteau sur pied flou (x 860) coupé par le bord droit, puis la cloison E/S qui balaie le cadre ; sujet le père, l'horloge et la chaîne nets ; brume le dehors par la porte jusqu'à 4.64 ; toile claire ; couches animées 3 à 4.
  OBJET-PONT ET VECTEUR : la chaîne du poignet au balancier suit le père dans toutes les pièces ; vecteur : whip vers la droite (+3 500 u/s à la couture).
  SON : tic-tac de bois 2.80 ; roulettes de bois 2.94 ; maillons de papier qui se tendent 3.41 ; tic 3.84 ; roulettes 4.14 ; bois sourd (le battant se ferme) 4.64 ; whoosh court de papier 5.05.
  IMAGE CLÉ : 4.20 : l'entrée, le père de profil à droite avec sa pile, l'horloge sortie de la porte à gauche, la chaîne de papier tendue de son balancier au poignet du père ; « Temps perdu » en boîte.

## Frame 2: Il passe devant elle, le Temps perdu prend une heure · 5.25 → 10.76

- scene: Au salon, la fille assise près de la fenêtre lève sa balle vers son père qui passe devant elle sans tourner la tête ; la balle roule jusqu'à sa chaise ; il s'assied au secrétaire et ouvre un dossier ; l'horloge se penche sur son épaule, sa grande aiguille fait un tour ; la case du salon s'éteint de deux crans ; whip vers la cuisine
- duration: 5.51s
- transition_in: cut
- status: outline
- src: compositions/frames/02-salon.html
- voiceover: "Sa fille l'attendait pour jouer. Lui, il ouvrit un dossier. Le Temps perdu lui prit une heure."
- type: problem
- blueprint: camera-journey (Adapt)
- focal: la fille qui tend sa balle, puis le père au dossier sous la main de l'horloge
- rules: depth-of-field-blur, sine-wave-loop
- world: dark
- handoff_in: à 0.00 : cam(800, 695, 1.55) flou 10 px ; caméra en plein whip vers la droite (+3 500 u/s en x, power2.in puis expo.out), dérive 0 ; monde : maison en coupe, monde sombre ; entrée E allumée : porte d'entrée fermée, patère qui oscille, le père qui marche vers la droite à (820, 900) avec sa pile sous le bras, l'horloge qui roule derrière lui à (640, 900), la chaîne tendue de son balancier au poignet arrière du père ; cloison E/S et sa baie floues (plan 1) au milieu du cadre ; salon S allumé : la fille assise par terre à (1 060, 900), sa balle à (1 150, 874), la balançoire immobile dans F1, le secrétaire vide et la lampe L1 allumée, la chaise vide à (1 500, 900) ; sous-titre sorti ; grain par plan, flamme 1 ± 0,03
- handoff_out: à 5.51 : cam(1850, 695, 1.6) flou 10 px ; caméra en plein whip vers la droite (+3 500 u/s en x, power2.in puis expo.out), dérive 0 ; monde : maison en coupe, monde sombre ; salon S assombri (voile 45 %) : le père assis au secrétaire à (1 500, 900), le dossier ouvert, la pile posée sur le plateau, l'horloge à (1 620, 900), la balle au pied de la chaise, la lampe L1 à flamme basse ; cloison S/K et sa baie floues (plan 1) au milieu du cadre ; cuisine K allumée, crépuscule dans F2 : la fille assise sur son tabouret à (1 940, 900), sa feuille blanche et son crayon sur les genoux, la table nue, la lampe L2 allumée, la chaise vide à (2 460, 900), le dessin du petit dinosaure épinglé à (2 620, 640) ; sous-titre sorti ; grain par plan, flamme 1 ± 0,03

Word cues: Sa@0.13 fille@0.41 l'attendait@0.57 pour@1.05 jouer@1.23 Lui@1.85 il@2.45 ouvrit@2.67 un@2.87 dossier@3.03 Le@3.77 Temps@3.95 perdu@4.13 lui@4.41 prit@4.65 une@4.87 heure@5.19

Scene 1 (0.00 à 1.70 s) : P3, elle tend sa balle, il passe sans s'arrêter
  TEXTE ÉCRAN : sous-titre « Sa fille l'attendait pour [boîte : jouer]. » (Sa 0.13, fille 0.41, l'attendait 0.57, pour 1.05, boîte tracée 1.19, jouer 1.23), sorti de 1.55 à 1.69 ; écart : elle lève la balle sur « fille » (0.41), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.20 fin du whip, atterrissage sur cam(1 080, 700, 1.55) (expo.out, flou 10 → 0) : la fille près de la fenêtre, la balançoire immobile dans F1 ; le père entre par la baie E/S à gauche du cadre, en marchant ; 0.13 « Sa » : la fille tourne la tête vers lui (pose, 12 i/s) ; 0.41 « fille » : elle se met à genoux et lève sa balle à deux mains (pose) ; 0.57 « l'attendait » : il avance vers elle, la pile sous le bras, la chaîne derrière lui ; 0.80 elle tend la balle plus haut, bras tendus ; 1.05 « pour » : il passe devant elle sans tourner la tête (deux pas, 12 i/s) ; 1.23 « jouer » : elle baisse les bras, la balle lui échappe et roule vers la droite, derrière lui (rotation, 0,6 s power2.out) ; 1.40 l'horloge passe à son tour, roulant, et la tête de la fille la suit ; 1.60 la balle atteint le bord droit du cadre.
  PISTE CAMÉRA : atterrissage expo.out de 0.00 à 0.20 ; dérive x +40 u/s, échelle +1 %/s de 0.20 à 1.70, jusqu'à cam(1 140, 700, 1.57) (elle suit le père).
  COUCHES ET PROFONDEUR : avant-plan la cloison E/S floue au bord gauche (flou 16 px, parallaxe ×1,8) ; sujet la fille et sa balle nettes, le père qui passe ; brume la balançoire immobile dans F1 et le jardin du soir ; toile claire derrière le salon ; couches animées 3.
  OBJET-PONT ET VECTEUR : la balle roule vers la droite et guide la caméra jusqu'au pied de sa chaise (plan suivant).
  SON : bois léger (elle se met à genoux) 0.41 ; pas, bois des tiges 0.57, 0.85, 1.12 ; balle qui tombe et roule, bois mat, de 1.23 à 1.80 ; roulettes 1.40.
  IMAGE CLÉ : 1.10 : le salon : la fillette à genoux tend sa balle vers son père qui passe devant elle sans tourner la tête, la pile sous le bras ; la balançoire immobile dans la fenêtre ; « jouer » en boîte.

Scene 2 (1.70 à 3.45 s) : P4, il s'assied, il ouvre un dossier
  TEXTE ÉCRAN : sous-titre « Lui, il ouvrit un [boîte : dossier]. » (Lui 1.85, il 2.45, ouvrit 2.67, un 2.87, boîte tracée 2.99, dossier 3.03), sorti de 3.45 à 3.59 ; écart synchro (il s'assied sur « il », le dossier s'ouvre sur « ouvrit »).
  ÉTAPES : 1.70 départ du cran vers le secrétaire, qui suit la balle (expo.inOut 0,35 s, flou 0 → 6 → 0) ; 1.85 « Lui, » : le père pose sa pile sur le plateau (elle se tasse, ×0,97, 0,08 s) ; 2.05 fin du cran sur cam(1 450, 700, 1.6) ; 2.10 la balle s'arrête contre le pied de sa chaise (petit rebond de 6 u) ; 2.25 il tire la chaise (pose) ; 2.45 « il » : il s'assied, tourné vers la lampe (deux poses, 12 i/s) ; 2.67 « ouvrit » : il tire un dossier de la pile et l'ouvre devant lui (les deux plats s'écartent, 0,1 s expo.out) ; 2.87 « un » : trois feuilles se soulèvent en éventail (0,04 s d'écart) ; 3.03 « dossier » : il penche la tête vers elles (pose) ; 3.20 la flamme de L1 vacille (×1,06 puis 1) ; 3.30 l'horloge s'arrête derrière lui à (1 620, 900) (roulettes, 12 i/s).
  PISTE CAMÉRA : cran de cam(1 140, 700, 1.57) vers cam(1 450, 700, 1.6) de 1.70 à 2.05 ; dérive x +18 u/s, échelle +1,5 %/s de 2.05 à 3.45.
  COUCHES ET PROFONDEUR : avant-plan le dossier flou d'un fauteuil (x 1 240) coupé par le bord gauche ; sujet le père et son dossier nets sous la lampe ; brume la fenêtre F1 assombrie hors champ, nappe de brume au ras du sol ; toile derrière le salon ; couches animées 3.
  OBJET-PONT ET VECTEUR : la balle immobile au pied de la chaise ; la chaîne du poignet au balancier mène l'œil à l'horloge (plan suivant).
  SON : papier lourd (la pile posée) 1.85 ; bois (la chaise) 2.25, 2.45 ; papier (le dossier s'ouvre) 2.67, 2.87 ; souffle de flamme 3.20.
  IMAGE CLÉ : 3.10 : le père assis de profil au secrétaire, le dossier ouvert en éventail sous la lampe, la balle immobile au pied de sa chaise, l'horloge derrière lui ; « dossier » en boîte.

Scene 3 (3.45 à 5.51 s) : P5, le Temps perdu lui prend une heure
  TEXTE ÉCRAN : sous-titre « Le Temps perdu lui prit [boîte : une heure]. » (Le 3.77, Temps 3.95, perdu 4.13, lui 4.41, prit 4.65, boîte tracée 4.83, une 4.87, heure 5.19), sorti de 5.35 à 5.49 ; écart : la main de l'horloge touche l'épaule sur « lui » (4.41), synchro.
  ÉTAPES : 3.45 départ d'un cran court vers l'horloge (expo.inOut 0,3 s) ; 3.75 fin sur cam(1 600, 700, 1.65) ; 3.77 « Le » : l'horloge se penche vers le père (rotation -6°, 12 i/s) ; 3.95 « Temps » : son balancier bat (±14°) ; 4.13 « perdu » : son bras court se tend vers lui ; 4.41 « lui » : sa main ronde se pose sur l'épaule du père, qui ne bouge pas ; 4.65 « prit » : la grande aiguille fait un tour complet (0,5 s power2.inOut), la petite avance d'une heure ; 4.87 « une » : la case du salon s'éteint d'un cran (voile 0 → 30 %, 0,06 s expo.out) ; 5.19 « heure » : second cran (voile 30 → 45 %), la flamme de L1 se tasse, l'horloge se redresse (pose) ; 5.35 départ du whip vers la cuisine (power2.in, flou 0 → 10).
  PISTE CAMÉRA : cran de cam(1 478, 700, 1.62) vers cam(1 600, 700, 1.65) de 3.45 à 3.75, puis dérive x +15 u/s de 3.75 à 5.35 ; whip vers la cuisine dès 5.35 : à 5.51 cam(1 850, 695, 1.6) flou 10 px.
  COUCHES ET PROFONDEUR : avant-plan la cloison S/K floue au bord droit, qui balaie le cadre pendant le whip ; sujet l'horloge et l'épaule du père nets ; brume la fenêtre F1 au bord gauche et la balançoire au loin ; toile derrière le salon, qui baisse avec la case ; couches animées 3.
  OBJET-PONT ET VECTEUR : la case qui s'éteint (signature 1) se rejoue à la cuisine ; vecteur : whip vers la droite.
  SON : tic-tac 3.95 ; cliquetis de bois de l'aiguille de 4.65 à 5.15 ; souffle de flamme qui se tasse 5.19 ; whoosh court de papier 5.35.
  IMAGE CLÉ : 4.90 : l'horloge penchée pose sa main ronde sur l'épaule du père absorbé, la grande aiguille floue en plein tour, la balle au pied de sa chaise, la case du salon qui s'assombrit ; « une heure » en boîte.

## Frame 3: Elle attend avec sa feuille, le Temps perdu prend la soirée · 10.76 → 16.42

- scene: À la cuisine, la fille sur son tabouret lève sa feuille et son crayon ; le père quitte le salon avec sa pile et passe encore devant elle sans la voir ; il ouvre ses devis à la table, le dessin du petit dinosaure épinglé dans son dos ; devant la fenêtre où la nuit tombe, l'horloge fait tourner ses aiguilles et la case s'éteint de deux crans ; la fille traverse tête basse vers l'escalier
- duration: 5.66s
- transition_in: cut
- status: outline
- src: compositions/frames/03-cuisine.html
- voiceover: "Elle l'attendait pour dessiner. Lui, il ouvrit ses devis. Le Temps perdu lui prit la soirée."
- type: problem
- blueprint: camera-journey (Adapt)
- focal: la fille et sa feuille blanche, puis le père à ses devis et l'horloge qui prend la soirée
- rules: depth-of-field-blur, sine-wave-loop
- world: dark
- handoff_in: à 0.00 : cam(1850, 695, 1.6) flou 10 px ; caméra en plein whip vers la droite (+3 500 u/s en x, power2.in puis expo.out), dérive 0 ; monde : maison en coupe, monde sombre ; salon S assombri (voile 45 %) : le père assis au secrétaire à (1 500, 900), le dossier ouvert, la pile posée sur le plateau, l'horloge à (1 620, 900), la balle au pied de la chaise, la lampe L1 à flamme basse ; cloison S/K et sa baie floues (plan 1) au milieu du cadre ; cuisine K allumée, crépuscule dans F2 : la fille assise sur son tabouret à (1 940, 900), sa feuille blanche et son crayon sur les genoux, la table nue, la lampe L2 allumée, la chaise vide à (2 460, 900), le dessin du petit dinosaure épinglé à (2 620, 640) ; sous-titre sorti ; grain par plan, flamme 1 ± 0,03
- handoff_out: à 5.66 : cam(2900, 680, 1.5) flou 8 px ; caméra en plein cran vers la droite (+900 u/s en x, expo.inOut), dérive 0 ; monde : maison en coupe, monde sombre ; cuisine K assombrie (voile 50 %), nuit étoilée sans lune dans F2 ; le père assis à (2 460, 900), une feuille de devis tenue devant son visage, la pile ouverte sur la table, la lampe L2 à flamme basse ; le dessin du petit dinosaure épinglé à (2 620, 640) ; l'horloge à (2 780, 900) devant F2, aiguilles arrêtées, la chaîne en chaînette jusqu'au poignet du père ; la fille qui vient de s'asseoir sur la deuxième marche à (3 060, 842), le menton dans les mains ; rampe floue (plan 1) au bord droit ; sous-titre sorti ; grain par plan, flamme 1 ± 0,03

Word cues: Elle@0.29 l'attendait@0.44 pour@0.84 dessiner@1.04 Lui@1.83 il@2.42 ouvrit@2.66 ses@2.86 devis@3.06 Le@3.74 Temps@3.92 perdu@4.14 lui@4.52 prit@4.80 la@5.00 soirée@5.28

Scene 1 (0.00 à 1.70 s) : P6, elle attend avec sa feuille, il repasse sans la voir
  TEXTE ÉCRAN : sous-titre « Elle l'attendait pour [boîte : dessiner]. » (Elle 0.29, l'attendait 0.44, pour 0.84, boîte tracée 1.00, dessiner 1.04), sorti de 1.55 à 1.69 ; écart : elle lève la feuille sur « Elle » (0.29), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.20 fin du whip, atterrissage sur cam(1 960, 700, 1.6) (expo.out, flou 10 → 0) : la fille sur son tabouret, le salon sombre visible à gauche par la baie ; 0.29 « Elle » : elle lève sa feuille blanche face à la toile (carte #F8EDD3 vide, 0,08 s) ; 0.44 « l'attendait » : elle tend son crayon vers la baie ; dans le salon sombre, le père se lève de son secrétaire, la pile sous le bras (deux poses) ; 0.70 la flamme de L2 vacille ; 0.84 « pour » : il passe la baie S/K (pas, 12 i/s), la chaîne traîne derrière lui, l'horloge roule à sa suite ; 1.04 « dessiner » : elle trace un premier trait sur sa feuille (le trait se dessine, 0,15 s) et la lève vers lui ; 1.20 il passe devant elle sans tourner la tête (deux pas) ; 1.45 elle baisse sa feuille ; 1.60 l'horloge passe devant elle à son tour, elle la suit des yeux.
  PISTE CAMÉRA : atterrissage expo.out de 0.00 à 0.20 ; dérive x +30 u/s, échelle +1 %/s de 0.20 à 1.70 (elle suit le père).
  COUCHES ET PROFONDEUR : avant-plan la cloison S/K floue au bord gauche (flou 16 px) ; sujet la fille et sa feuille nettes, le père qui passe ; brume le crépuscule dans F2 au loin ; toile derrière la cuisine ; couches animées 3.
  OBJET-PONT ET VECTEUR : la feuille blanche de la fille annonce le dessin épinglé du plan suivant ; vecteur : le père marche vers la droite, la caméra le suit.
  SON : bois (la chaise du salon) 0.44 ; pas, bois des tiges 0.84, 1.10, 1.30 ; crayon sur papier 1.04 ; roulettes 1.60.
  IMAGE CLÉ : 1.10 : la fillette sur son tabouret lève sa feuille et son crayon vers son père qui passe devant elle sans la regarder, la pile sous le bras ; « dessiner » en boîte.

Scene 2 (1.70 à 3.55 s) : P7, il ouvre ses devis, le dessin dans son dos
  TEXTE ÉCRAN : sous-titre « Lui, il ouvrit ses [boîte : devis]. » (Lui 1.83, il 2.42, ouvrit 2.66, ses 2.86, boîte tracée 3.02, devis 3.06), sorti de 3.40 à 3.54 ; écart synchro (la pile tombe sur « Lui »).
  ÉTAPES : 1.70 départ du cran vers la table (expo.inOut 0,35 s, flou 0 → 6 → 0) ; 1.83 « Lui, » : il laisse tomber la pile sur la table (×0,97, 0,08 s), la lampe L2 tremble ; 2.05 fin du cran sur cam(2 330, 690, 1.55) : au mur derrière lui, le dessin du petit dinosaure épinglé ; 2.20 il tire la chaise (pose) ; 2.42 « il » : il s'assied dos au dessin, tourné vers la lampe (deux poses) ; 2.66 « ouvrit » : cinq feuilles se lèvent de la pile en éventail (0,03 s d'écart, 0,1 s expo.out) ; 2.86 « ses » : il en prend une et la tient debout devant son visage (feuille ajourée de colonnes) ; 3.06 « devis » : les autres retombent sur la pile ; 3.25 l'horloge s'arrête derrière lui devant F2 (roulettes) et la chaîne se détend en chaînette.
  PISTE CAMÉRA : cran de cam(2 010, 700, 1.62) vers cam(2 330, 690, 1.55) de 1.70 à 2.05 ; dérive x +18 u/s, échelle +1,5 %/s de 2.05 à 3.55.
  COUCHES ET PROFONDEUR : avant-plan la suspension de casseroles floue qui pend du haut du cadre (x 2 200) ; sujet le père, sa feuille et la lampe nets, le dessin au mur ; brume F2 et le crépuscule ; toile derrière la cuisine ; couches animées 3.
  OBJET-PONT ET VECTEUR : le dessin épinglé dans son dos (il sera recouvert, puis retrouvé) ; la chaîne mène l'œil à l'horloge (plan suivant).
  SON : papier lourd (la pile tombe) 1.83 ; bois (la chaise) 2.20, 2.42 ; papier (l'éventail) 2.66, 2.86 ; roulettes 3.25.
  IMAGE CLÉ : 3.00 : le père assis de profil à la table, une feuille de devis tenue devant son visage sous la lampe, le dessin du petit dinosaure épinglé au mur dans son dos, l'horloge qui arrive derrière lui ; « devis » en boîte.

Scene 3 (3.55 à 5.66 s) : P8, le Temps perdu lui prend la soirée, elle part vers l'escalier
  TEXTE ÉCRAN : sous-titre « Le Temps perdu lui prit [boîte : la soirée]. » (Le 3.74, Temps 3.92, perdu 4.14, lui 4.52, prit 4.80, boîte tracée 4.96, la 5.00, soirée 5.28), sorti de 5.45 à 5.59 ; écart : les aiguilles partent sur « prit » (4.80), synchro.
  ÉTAPES : 3.55 départ du cran vers l'horloge (expo.inOut 0,3 s), il passe sur le dessin épinglé ; 3.74 « Le » : le cadran accroche la lumière de la lampe ; 3.85 fin du cran sur cam(2 780, 690, 1.55) ; 3.92 « Temps » : le balancier bat ; 4.14 « perdu » : le bras court de l'horloge se tend vers le père, hors champ à gauche ; 4.52 « lui » : sa main ronde se referme ; 4.80 « prit » : la grande aiguille fait trois tours (0,6 s power2.in), la petite avance de trois heures ; derrière, F2 passe du crépuscule à la nuit en deux crans et des étoiles piquent ; 5.00 « la » : la case s'éteint d'un cran (voile 0 → 30 %) ; la fille traverse le cadre devant F2, tête basse, vers l'escalier (pas lents, 12 i/s) ; 5.28 « soirée » : second cran (voile 30 → 50 %), la flamme de L2 se tasse ; 5.50 départ du cran qui suit la fille vers l'escalier (expo.inOut, flou 0 → 8).
  PISTE CAMÉRA : cran de cam(2 357, 690, 1.58) vers cam(2 780, 690, 1.55) de 3.55 à 3.85, puis dérive x +16 u/s de 3.85 à 5.50 ; cran vers l'escalier dès 5.50 : à 5.66 cam(2 900, 680, 1.5) flou 8 px.
  COUCHES ET PROFONDEUR : avant-plan la rampe de l'escalier floue au bord droit ; sujet l'horloge et ses aiguilles nettes, la fille qui passe ; brume la nuit qui tombe dans F2 ; toile derrière la cuisine, qui baisse avec la case ; couches animées 3 à 4.
  OBJET-PONT ET VECTEUR : la fille tête basse mène la caméra vers l'escalier ; la case qui s'éteint (signature 1).
  SON : tic-tac 3.92 ; cliquetis rapide des aiguilles de 4.80 à 5.40 ; vent de nuit dans F2 4.80 ; pas légers 5.00, 5.25 ; souffle de flamme qui se tasse 5.28.
  IMAGE CLÉ : 5.30 : l'horloge devant la fenêtre où la nuit est tombée, ses aiguilles floues en plein tour, la petite fille qui passe tête basse vers l'escalier, la cuisine assombrie ; « la soirée » en boîte.

## Frame 4: Interminable Attente · 16.42 → 20.38

- scene: Sur la deuxième marche de l'escalier, la fille seule, le menton dans les mains ; deux fils descendent du plafond et les lettres de papier I et A tombent au-dessus d'elle, puis se déplient en « Interminable Attente » ; un trait d'or sous « Attente » ; le recul commence
- duration: 3.96s
- transition_in: cut
- status: outline
- src: compositions/frames/04-attente.html
- voiceover: "Pour sa fille, I.A. voulait dire Interminable Attente."
- type: problem
- blueprint: titlecard-reveal (Adapt)
- focal: la fille sur la marche, puis les lettres « Interminable Attente » au-dessus d'elle
- rules: sine-wave-loop, depth-of-field-blur
- world: dark
- handoff_in: à 0.00 : cam(2900, 680, 1.5) flou 8 px ; caméra en plein cran vers la droite (+900 u/s en x, expo.inOut), dérive 0 ; monde : maison en coupe, monde sombre ; cuisine K assombrie (voile 50 %), nuit étoilée sans lune dans F2 ; le père assis à (2 460, 900), une feuille de devis tenue devant son visage, la pile ouverte sur la table, la lampe L2 à flamme basse ; le dessin du petit dinosaure épinglé à (2 620, 640) ; l'horloge à (2 780, 900) devant F2, aiguilles arrêtées, la chaîne en chaînette jusqu'au poignet du père ; la fille qui vient de s'asseoir sur la deuxième marche à (3 060, 842), le menton dans les mains ; rampe floue (plan 1) au bord droit ; sous-titre sorti ; grain par plan, flamme 1 ± 0,03
- handoff_out: à 3.96 : cam(3045, 684, 1.52) flou 3 px ; caméra en début de recul vers la gauche et vers l'arrière (x -700 u/s, échelle -1,6/s, power2.in), dérive 0 ; monde : maison en coupe, monde sombre ; la fille assise sur la deuxième marche à (3 060, 842), le menton dans les mains ; « Interminable » et « Attente » en lettres de papier ombre Fraunces 84 px pendues à leurs fils au-dessus d'elle, centrées à l'écran, trait d'or sous « Attente » ; cuisine K assombrie (voile 50 %), nuit dans F2 ; le père assis à (2 460, 900), sa feuille devant le visage, la lampe L2 à flamme basse, l'horloge à (2 780, 900), la chaîne, le dessin épinglé à (2 620, 640) ; rampe floue (plan 1) au bord droit ; sous-titre sorti ; grain par plan, flamme 1 ± 0,03

Word cues: Pour@0.34 sa@0.48 fille@0.78 IA@1.25 voulait@1.74 dire@2.06 Interminable@2.58 Attente@3.42

Scene 1 (0.00 à 1.60 s) : P9, seule sur la marche, I et A tombent
  TEXTE ÉCRAN : sous-titre « Pour sa fille, [boîte : IA] voulait dire » (Pour 0.34, sa 0.48, fille 0.78, boîte tracée 1.21, IA 1.25, voulait 1.74, dire 2.06) ; il reste jusqu'à 3.70 puis sort (3.70 à 3.84) ; écart : les lettres tombent sur « IA » (1.25), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.18 fin du cran sur cam(3 060, 670, 1.45) (expo.out, flou 8 → 0) : la fille sur la deuxième marche, le menton dans les mains, toute petite dans la case sombre ; 0.34 « Pour » : ses épaules s'abaissent (pose, 12 i/s) ; 0.48 « sa » : une couette bouge (rotation 5°) ; 0.78 « fille » : le cœur lumineux de la toile se recentre sur elle (0,1 s) ; 1.00 elle lève les yeux (tête +8°) ; 1.25 « IA » : deux fils descendent du plafond (y 438) et les initiales I et A, Fraunces 700 84 px, ombre, tombent au bout (y -200 → 0 à l'écran, 0,25 s power3.out), côte à côte au-dessus d'elle, centrées à l'écran ; 1.45 elles se balancent (±6° amorti sur 1,2 s, répétitions finies).
  PISTE CAMÉRA : atterrissage expo.out de 0.00 à 0.18 ; poussée lente échelle +1,5 %/s, y +4 u/s de 0.18 à 3.84 (s'enfonce).
  COUCHES ET PROFONDEUR : avant-plan la rampe à barreaux floue au bord droit (flou 14 px, parallaxe ×1,8) ; sujet la fille nette sur la marche, les lettres ; brume la cuisine sombre à gauche et la nuit dans F2 ; toile, cœur lumineux recentré sur la marche ; couches animées 3.
  OBJET-PONT ET VECTEUR : I et A, initiales seules, se déplient en mots au plan suivant ; elles retomberont dorées à la séquence 10 (rime).
  SON : vent de nuit lointain dans F2 0.34 ; tic-tac lointain 0.48, 1.00 ; fils de bois léger 1.25 ; papier 1.45.
  IMAGE CLÉ : 1.50 : la petite fille seule sur la marche, le menton dans les mains, sous deux grandes lettres de papier I et A suspendues à leurs fils au-dessus d'elle ; « IA » en boîte.

Scene 2 (1.60 à 3.96 s) : P10, Interminable Attente
  TEXTE ÉCRAN : moment typographique : « Interminable » (2.58) puis « Attente » (3.42) se déplient depuis leurs initiales sur deux lignes centrées, Fraunces 600 84 px, ombre (initiales en 700) ; [trait : Attente] tracé sous « Attente » à 3.42 ; en bas, le sous-titre « Pour sa fille, IA voulait dire » reste jusqu'à 3.70 ; écart synchro.
  ÉTAPES : 1.60 cran d'échelle sur les lettres (0,2 s expo.inOut) ; 1.74 « voulait » : le I descend sur la première ligne, le A sur la seconde (0,2 s power3.out) ; 2.06 « dire » : les fils se tendent (les lettres s'arrêtent net) ; 2.30 la fille tourne la tête vers la cuisine, où l'horloge bat au loin ; 2.58 « Interminable » : les lettres n, t, e, r, m, i, n, a, b, l, e glissent de derrière le I (0,03 s d'écart, 0,12 s expo.out) ; 2.90 le balancier lointain bat ; 3.10 la fille tape du talon sur la marche (pose) ; 3.42 « Attente » : t, t, e, n, t, e glissent de derrière le A (0,03 s d'écart) et le trait d'or se trace dessous (0,4 s power2.out) ; 3.66 fin de la voix, les mots se balancent (±3°) ; 3.84 départ du recul (power2.in, flou 0 → 3).
  PISTE CAMÉRA : cran d'échelle ×1,04 sur les lettres de 1.60 à 1.80 (expo.inOut), puis poussée lente échelle +1,5 %/s, y +4 u/s jusqu'à 3.84, à cam(3 060, 685, 1.55) ; recul dès 3.84 : à 3.96 cam(3 045, 684, 1.52) flou 3 px.
  COUCHES ET PROFONDEUR : avant-plan la rampe floue au bord droit ; sujet les mots de papier et la fille ; brume la cuisine sombre ; toile ; couches animées 3 à 4.
  OBJET-PONT ET VECTEUR : au plan suivant, les lettres de « Interminable Attente » se détachent et volent en feuilles de devis qui s'épinglent sur le dessin (l'attente devient le travail qui le recouvre).
  SON : fils qui se tendent, bois léger, 2.06 ; papier (les mots se déplient) 2.58, 3.42 ; tic-tac lointain 2.90 ; bois léger (le talon) 3.10.
  IMAGE CLÉ : 3.50 : au-dessus de la petite fille assise sur la marche, « Interminable » et « Attente » en lettres de papier pendues à leurs fils, un trait d'or sous « Attente ».

## Frame 5: Soir après soir, il s'effaçait · 20.38 → 25.40

- scene: Recul sur la cuisine entière : les lettres volent en feuilles de devis qui s'épinglent sur le dessin ; les jours et les nuits passent en accéléré dans la fenêtre pendant que la pile monte ; le père s'éloigne de la toile en trois crans, agrandi et pâle dans le flou ; gag muet : la fille agite la main devant son visage et seul le balancier lui répond ; elle croise les bras et lève les yeux vers le mur
- duration: 5.02s
- transition_in: cut
- status: outline
- src: compositions/frames/05-effacement.html
- voiceover: "Soir après soir, il s'effaçait."
- type: problem
- blueprint: camera-journey (Adapt)
- focal: le père qui s'efface, puis la main de la fille devant son visage
- rules: depth-of-field-blur, sine-wave-loop
- world: dark
- handoff_in: à 0.00 : cam(3045, 684, 1.52) flou 3 px ; caméra en début de recul vers la gauche et vers l'arrière (x -700 u/s, échelle -1,6/s, power2.in), dérive 0 ; monde : maison en coupe, monde sombre ; la fille assise sur la deuxième marche à (3 060, 842), le menton dans les mains ; « Interminable » et « Attente » en lettres de papier ombre Fraunces 84 px pendues à leurs fils au-dessus d'elle, centrées à l'écran, trait d'or sous « Attente » ; cuisine K assombrie (voile 50 %), nuit dans F2 ; le père assis à (2 460, 900), sa feuille devant le visage, la lampe L2 à flamme basse, l'horloge à (2 780, 900), la chaîne, le dessin épinglé à (2 620, 640) ; rampe floue (plan 1) au bord droit ; sous-titre sorti ; grain par plan, flamme 1 ± 0,03
- handoff_out: à 5.02 : cam(2592, 690, 1.41) flou 5 px ; caméra en plein cran vers le mur au dessin (expo.inOut, échelle +1,1/s), dérive 0 ; monde : maison en coupe, monde sombre ; cuisine K assombrie (voile 55 %), nuit dans F2 ; le père assis à (2 460, 900) agrandi ×1,25, flou 6 px, opacité 0,4, sa feuille devant le visage, la pile haute sur la table, la lampe L2 à flamme basse ; la fille debout à (2 380, 900) devant lui, bras croisés, tête levée vers le mur ; l'horloge à (2 780, 900), balancier au repos ; trois feuilles de devis épinglées qui couvrent le dessin à (2 620, 640) ; suspension de casseroles floue (plan 1) en haut à gauche, rampe floue au bord droit ; sous-titre vide ; grain par plan, flamme 1 ± 0,03

Word cues: Soir@0.30 après@0.74 soir@0.98 il@1.46 s'effaçait@1.70

Scene 1 (0.00 à 2.30 s) : P11, soir après soir, le père s'efface
  TEXTE ÉCRAN : sous-titre « Soir après soir, il [boîte : s'effaçait]. » (Soir 0.30, après 0.74, soir 0.98, il 1.46, boîte tracée 1.66, s'effaçait 1.70), sorti de 2.25 à 2.39 ; écart : la première nuit bascule sur « Soir » (0.30), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.45 fin du recul sur la cuisine entière cam(2 640, 600, 1.0) (expo.out, flou 3 → 0) ; 0.10 les lettres se détachent de leurs fils et volent vers le mur derrière le père, où elles se changent en feuilles de devis (0,25 s power2.in) ; 0.30 « Soir » : F2 bascule nuit → jour → nuit (0,12 s par bascule), la case pulse (voile 50 → 10 → 55 %), les aiguilles font un tour, une première feuille s'épingle sur le dessin (×1,2 → 1, 0,08 s) ; 0.74 « après » : deuxième bascule, la pile du père monte de cinq feuilles, une deuxième feuille s'épingle ; 0.98 « soir » : troisième bascule, la troisième feuille couvre tout le dessin ; 1.20 la flamme de L2 baisse encore ; 1.46 « il » : le père s'éloigne de la toile, premier cran (×1,08, flou 2 px, opacité 0,8, 0,1 s expo.out), sa chaîne reste nette et sombre ; 1.70 « s'effaçait » : deuxième cran (×1,16, flou 4 px, opacité 0,6) ; 1.94 troisième cran (×1,25, flou 6 px, opacité 0,4) ; 2.10 la fille relève la tête sur sa marche.
  PISTE CAMÉRA : fin du recul expo.out de 0.00 à 0.45 ; dérive x +12 u/s, échelle +1,5 %/s de 0.45 à 2.30.
  COUCHES ET PROFONDEUR : avant-plan le montant de la baie S/K flou au bord gauche et la rampe floue au bord droit ; sujet la cuisine entière nette, le père qui pâlit ; brume F2 et ses jours et nuits ; toile qui pulse avec la case ; couches animées 4.
  OBJET-PONT ET VECTEUR : les lettres deviennent les feuilles épinglées qui recouvrent le dessin (elle les arrachera à la séquence 6) ; la chaîne reste nette pendant que le père pâlit.
  SON : papier (les lettres deviennent des feuilles) 0.10 ; punaises, bois sec, 0.30, 0.74, 0.98 ; tic-tac accéléré de 0.30 à 1.20 ; vent de nuit qui monte et retombe à chaque bascule ; souffle de flamme 1.20.
  IMAGE CLÉ : 1.95 : la cuisine entière dans la nuit, le père agrandi et pâli dans le flou à la table, sa chaîne nette jusqu'à l'horloge, des feuilles de devis épinglées sur le dessin, la petite fille sur sa marche à droite ; « s'effaçait » en boîte.

Scene 2 (2.30 à 5.02 s) : P12, gag muet : la main devant son visage, seul le balancier répond
  TEXTE ÉCRAN : aucun texte (silence de la voix) ; la bande des sous-titres reste vide.
  ÉTAPES : 2.30 départ de la poussée vers le père et la fille (expo.inOut 0,5 s) ; la fille descend de sa marche (deux poses) ; 2.55 elle traverse vers lui (pas, 12 i/s) et passe devant l'horloge ; 2.80 fin de la poussée sur cam(2 560, 690, 1.3) ; 3.10 elle s'arrête devant lui, au bout de la table ; 3.30 elle lève la main devant son visage pâle et l'agite (3.30, 3.48, 3.66, une pose par passage) ; 3.66 il ne bouge pas, sa feuille reste devant son visage ; 3.90 seul le balancier de l'horloge répond : il bat une fois vers elle (-18° → +18°, 0,3 s) ; 4.20 elle tourne la tête vers l'horloge (pose) ; 4.45 elle croise les bras (deux poses) ; 4.65 elle tape du pied (pose) ; 4.80 elle lève les yeux vers le mur aux feuilles épinglées ; 4.85 départ du cran qui suit son regard vers le mur (expo.inOut 0,4 s, flou 0 → 5).
  PISTE CAMÉRA : poussée de cam(2 662, 600, 1.03) vers cam(2 560, 690, 1.3) de 2.30 à 2.80, puis dérive x +14 u/s, échelle +1 %/s de 2.80 à 4.85 ; cran vers le mur dès 4.85 : à 5.02 cam(2 592, 690, 1.41) flou 5 px.
  COUCHES ET PROFONDEUR : avant-plan la suspension de casseroles floue en haut à gauche et la rampe floue au bord droit ; sujet la fille nette et le père pâle ; brume la nuit dans F2 ; toile assombrie ; couches animées 3.
  OBJET-PONT ET VECTEUR : le balancier qui répond (signature 2) ; le regard de la fille mène au mur aux feuilles épinglées.
  SON : pas légers 2.55, 2.75, 2.95 ; souffle de la main 3.30, 3.48, 3.66 ; tic sec du balancier 3.90 ; bois (le pied) 4.65.
  IMAGE CLÉ : 3.50 : la petite fille agite la main devant le visage pâle et flou de son père qui fixe sa feuille, l'horloge derrière elle ; aucun texte.

## Frame 6: Le petit dinosaure, la chaîne · 25.40 → 31.37

- scene: Elle arrache les feuilles épinglées et retrouve le dessin du petit dinosaure ; elle le glisse devant la feuille de devis de son père, qui revient net contre la toile ; il baisse les yeux, un reflet d'or court le long de la chaîne jusqu'à l'horloge ; la lampe vacille et s'éteint, la nuit d'encre gagne tout le cadre
- duration: 5.97s
- transition_in: cut
- status: outline
- src: compositions/frames/06-chaine.html
- voiceover: "Alors elle retrouva leur petit dinosaure. Elle le glissa sur ses devis. Enfin, il vit la chaîne."
- type: problem
- blueprint: camera-journey (Adapt)
- focal: le dessin retrouvé et glissé devant le visage du père, puis la chaîne jusqu'à l'horloge
- rules: depth-of-field-blur, sine-wave-loop
- world: dark
- handoff_in: à 0.00 : cam(2592, 690, 1.41) flou 5 px ; caméra en plein cran vers le mur au dessin (expo.inOut, échelle +1,1/s), dérive 0 ; monde : maison en coupe, monde sombre ; cuisine K assombrie (voile 55 %), nuit dans F2 ; le père assis à (2 460, 900) agrandi ×1,25, flou 6 px, opacité 0,4, sa feuille devant le visage, la pile haute sur la table, la lampe L2 à flamme basse ; la fille debout à (2 380, 900) devant lui, bras croisés, tête levée vers le mur ; l'horloge à (2 780, 900), balancier au repos ; trois feuilles de devis épinglées qui couvrent le dessin à (2 620, 640) ; suspension de casseroles floue (plan 1) en haut à gauche, rampe floue au bord droit ; sous-titre vide ; grain par plan, flamme 1 ± 0,03
- handoff_out: à 5.97 : cam(2780, 690, 1.76) flou 2 px ; caméra en début de plongée vers le cadran (y -28 u/s, échelle +4 %/s, linéaire), dérive 0 ; monde : maison en coupe, monde sombre, cuisine dans le noir : la nuit d'encre partie de la lampe L2 couvre tout le cadre (ombre-sol à 96 %) ; seul le contour du cadran de l'horloge (anneau r 56 u) à (2 780, 630) garde un liseré creme à 15 % ; un fil de fumée sombre monte de la lampe éteinte (plan 1) ; sous-titre sorti ; grain par plan sur le noir, flamme éteinte

Word cues: Alors@0.11 elle@0.60 retrouva@0.84 leur@1.16 petit@1.36 dinosaure@1.66 Elle@2.53 le@2.70 glissa@2.92 sur@3.18 ses@3.46 devis@3.62 Enfin@4.22 il@4.85 vit@5.10 la@5.18 chaîne@5.42

Scene 1 (0.00 à 2.20 s) : P13, elle arrache les feuilles, le petit dinosaure
  TEXTE ÉCRAN : sous-titre « Alors elle retrouva leur [boîte : petit dinosaure]. » (Alors 0.11, elle 0.60, retrouva 0.84, leur 1.16, boîte tracée 1.32, petit 1.36, dinosaure 1.66), sorti de 2.15 à 2.29 ; écart : le dessin paraît sur « petit » (1.36), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.23 fin du cran sur cam(2 600, 690, 1.6) ; 0.11 « Alors » : elle décroise les bras (pose) ; 0.30 elle passe derrière la chaise du père vers le mur (deux pas) ; 0.60 « elle » : elle se hisse sur la pointe des pieds, sa main atteint la première feuille ; 0.84 « retrouva » : elle l'arrache, la punaise saute, la feuille tombe en tournant (0,5 s) ; 1.16 « leur » : la deuxième, de l'autre main ; 1.36 « petit » : la troisième : le dessin du petit dinosaure sous son champignon paraît, net, et un reflet d'or passe sur la carte (0,2 s) ; 1.66 « dinosaure » : elle décroche le dessin (une punaise saute) et le serre contre elle (pose) ; 1.90 les trois feuilles touchent le sol.
  PISTE CAMÉRA : fin du cran de 0.00 à 0.23 ; dérive x +12 u/s, y +3 u/s, échelle +1,5 %/s de 0.23 à 2.20.
  COUCHES ET PROFONDEUR : avant-plan la suspension de casseroles floue en haut à gauche ; sujet la fille et le mur au dessin nets, le père pâle et flou à gauche ; brume la nuit dans F2 ; toile assombrie ; couches animées 3.
  OBJET-PONT ET VECTEUR : le dessin passe du mur aux mains de la fille, puis sur les devis du père (plan suivant).
  SON : pas légers 0.30 ; papier arraché 0.84, 1.16, 1.36 ; punaise, bois sec, 1.66 ; feuilles qui touchent le sol 1.90.
  IMAGE CLÉ : 1.50 : sur la pointe des pieds, la petite fille arrache la dernière feuille de devis épinglée : dessous, le dessin du petit dinosaure sous son champignon, un reflet d'or ; « petit dinosaure » en boîte.

Scene 2 (2.20 à 4.10 s) : P14, elle le glisse sur ses devis
  TEXTE ÉCRAN : sous-titre « Elle le [boîte : glissa] sur ses devis. » (Elle 2.53, le 2.70, boîte tracée 2.88, glissa 2.92, sur 3.18, ses 3.46, devis 3.62), sorti de 3.85 à 3.99 ; écart synchro (le dessin descend sur « glissa »).
  ÉTAPES : 2.20 elle revient vers le père, le dessin serré contre elle (pas), et la caméra l'accompagne d'un cran court (0,25 s expo.inOut) ; 2.53 « Elle » : elle se place à côté de lui ; 2.70 « le » : elle lève le dessin à deux mains au-dessus de son bras ; 2.92 « glissa » : elle glisse le dessin entre son visage et sa feuille de devis (il descend devant la feuille, 0,12 s expo.out) ; 3.18 « sur » : le dessin se pose sur la feuille et couvre ses colonnes ; 3.46 « ses » : la feuille du père tremble (rotation 2°) ; 3.62 « devis » : sa tête s'incline vers le dessin (pose) ; 3.85 son ombre revient d'un cran vers la toile (×1,25 → 1,12, flou 6 → 3 px, opacité 0,4 → 0,7, 0,1 s expo.out).
  PISTE CAMÉRA : cran de suivi vers le père, cam(2 560, 705, 1.72), de 2.20 à 2.45 (expo.inOut) : la caméra accompagne la fille ; dérive x +12 u/s, y +4 u/s, échelle +1 %/s de 2.45 à 4.85.
  COUCHES ET PROFONDEUR : avant-plan la suspension floue ; sujet le dessin net devant le visage du père, la fille ; brume la nuit dans F2 ; toile assombrie ; couches animées 3.
  OBJET-PONT ET VECTEUR : le dessin ramène le père contre la toile ; la chaîne à son poignet (plan suivant).
  SON : papier (le dessin glisse) 2.92 ; papier (la feuille tremble) 3.46.
  IMAGE CLÉ : 3.30 : la petite fille glisse le dessin du dinosaure devant la feuille de devis de son père, qui penche la tête vers lui ; « glissa » en boîte.

Scene 3 (4.10 à 5.97 s) : P15, il revient net, il voit la chaîne, la nuit gagne
  TEXTE ÉCRAN : sous-titre « Enfin, il vit la [boîte : chaîne]. » (Enfin 4.22, il 4.85, vit 5.10, la 5.18, boîte tracée 5.38, chaîne 5.42), sorti de 5.70 à 5.84 ; écart : le reflet court sur les maillons sur « vit » (5.10), synchro.
  ÉTAPES : 4.22 « Enfin » : son ombre revient tout à fait contre la toile (×1,12 → 1, flou 3 → 0, opacité 0,7 → 1, 0,08 s expo.out) : il est net et sombre comme à l'entrée ; 4.45 il pose sa feuille et regarde le dessin (pose) ; 4.70 il baisse les yeux vers son poignet (tête -20°) ; 4.85 « il » : départ du pan vers la droite le long de la chaîne (expo.inOut 0,5 s) ; 5.10 « vit » : un reflet d'or court le long des maillons, du poignet au balancier (0,4 s) ; 5.35 fin du pan sur cam(2 780, 700, 1.7) : l'horloge ; 5.42 « chaîne » : la chaîne se tend d'un coup (chaînette → droite, 0,06 s) ; 5.55 la flamme de L2 vacille trois fois (×1,1, ×0,7, ×1,05, 0,08 s d'écart) ; 5.75 L2 s'éteint : une nuit d'encre part de la lampe et couvre tout le cadre (tache d'encre, rayon 0 → 1 400 px à l'écran, 0,2 s power2.in), seul reste un liseré creme sur l'anneau du cadran ; 5.85 départ de la plongée vers le cadran.
  PISTE CAMÉRA : pan de cam(2 589, 715, 1.76) vers cam(2 780, 700, 1.7) de 4.85 à 5.35, puis dérive échelle +2 %/s de 5.35 à 5.85 ; plongée vers le cadran dès 5.85 : à 5.97 cam(2 780, 690, 1.76) flou 2 px.
  COUCHES ET PROFONDEUR : avant-plan la rampe floue au bord droit, puis la fumée de la lampe éteinte ; sujet la chaîne puis l'horloge ; brume la nuit dans F2 ; toile qui s'éteint ; couches animées 3 à 4.
  OBJET-PONT ET VECTEUR : la chaîne mène au cadran ; la nuit d'encre partie de la lampe ouvre le pivot (signature 1, la dernière case qui s'éteint).
  SON : maillons de papier 5.10 ; chaîne tendue, papier sec, 5.42 ; crépitement de la flamme de 5.55 à 5.75 ; souffle (la lampe s'éteint) 5.75 ; la musique se tait à 5.75.
  IMAGE CLÉ : 5.45 : la chaîne de papier tendue du poignet du père au balancier de l'horloge, un reflet d'or le long des maillons pendant que la lampe vacille ; « chaîne » en boîte.

## Frame 7: Le Temps perdu eut une idée · 31.37 → 34.60

- scene: Dans le noir de la cuisine éteinte, la caméra s'enfonce vers le cadran de l'horloge ; le balancier s'arrête, les aiguilles se rejoignent sur midi, une étincelle naît et le cadran s'allume d'or de l'intérieur ; l'or descend dans toute l'horloge et fait tourner ses engrenages dans une poussière d'or ; la lumière du cadran déborde et remplit le cadre
- duration: 3.23s
- transition_in: cut
- status: outline
- src: compositions/frames/07-idee.html
- voiceover: "Le Temps perdu eut alors une idée."
- type: pivot
- blueprint: camera-journey (Adapt)
- focal: le cadran qui s'allume d'or dans le noir
- rules: ambient-glow-bloom, particle-burst
- world: dark
- handoff_in: à 0.00 : cam(2780, 690, 1.76) flou 2 px ; caméra en début de plongée vers le cadran (y -28 u/s, échelle +4 %/s, linéaire), dérive 0 ; monde : maison en coupe, monde sombre, cuisine dans le noir : la nuit d'encre partie de la lampe L2 couvre tout le cadre (ombre-sol à 96 %) ; seul le contour du cadran de l'horloge (anneau r 56 u) à (2 780, 630) garde un liseré creme à 15 % ; un fil de fumée sombre monte de la lampe éteinte (plan 1) ; sous-titre sorti ; grain par plan sur le noir, flamme éteinte
- handoff_out: à 3.23 : aucun raccord de caméra (coupe franche voulue) ; raccord de lumière : le cadre entier est la lumière d'or du cadran, dégradé radial #E0A84A au centre (960, 540) vers #FFF4DC au bord, sans grain, sans forme ni texte

Word cues: Le@0.47 Temps@0.67 perdu@0.83 eut@1.17 alors@1.47 une@1.65 idée@1.93

Scene 1 (0.00 à 2.10 s) : P16, dans le noir, le cadran s'allume
  TEXTE ÉCRAN : sous-titre « Le Temps perdu eut alors une [boîte : idée]. » (Le 0.47, Temps 0.67, perdu 0.83, eut 1.17, alors 1.47, une 1.65, boîte tracée 1.89, idée 1.93) sur le noir, sorti de 2.60 à 2.74 ; écart : le cadran s'allume sur « idée » (1.93), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 le noir, le liseré du cadran, la fumée qui passe ; 0.20 le balancier s'arrête (dernier tic, liseré du balancier qui s'immobilise) ; 0.47 « Le » : le liseré du cadran respire (15 → 25 %) ; 0.67 « Temps » : la grande aiguille remonte d'un cran (son contour accroche la lumière) ; 0.83 « perdu » : un engrenage de la fenêtre du ventre accroche un liseré ; 1.17 « eut » : la petite aiguille se dresse vers midi ; 1.47 « alors » : les deux aiguilles se rejoignent sur midi (clac) ; 1.65 « une » : une étincelle d'or naît au centre du cadran (point ×0 → 1, 0,08 s) ; 1.93 « idée » : la fenêtre du cadran s'allume d'or de l'intérieur (disque or-clair r 58, ×0,2 → 1, 0,1 s expo.out) et son halo pré-rendu s'ouvre autour ; 2.05 la lumière du cadran éclaire la couronne et ses pommeaux.
  PISTE CAMÉRA : plongée lente de cam(2 780, 690, 1.76) vers cam(2 780, 632, 1.93) de 0.00 à 2.10 (linéaire).
  COUCHES ET PROFONDEUR : avant-plan la fumée sombre de la lampe éteinte qui traverse le cadre (brume-2 à 12 %) ; sujet le cadran ; brume aucune ; toile noire ; couches animées 2 à 3.
  OBJET-PONT ET VECTEUR : la lumière du cadran va descendre dans toute l'horloge (plan suivant).
  SON : dernier tic 0.20 ; clac de bois des aiguilles 1.47 ; souffle de lumière 1.93 ; la boîte à musique reprend, claire, sur « idée » 1.93.
  IMAGE CLÉ : 2.00 : le noir complet, au centre le cadran de l'horloge allumé d'or de l'intérieur, les deux aiguilles sur midi, un fil de fumée qui passe ; « idée » en boîte.

Scene 2 (2.10 à 3.23 s) : P17, l'or envahit l'horloge, la lumière déborde
  TEXTE ÉCRAN : le sous-titre de « idée » sort de 2.60 à 2.74 ; puis aucun texte.
  ÉTAPES : 2.10 l'or descend du cadran dans le corps de l'horloge : la silhouette s'inverse en or lumineux, du cadran vers les roulettes (masque qui descend, 0,2 s expo.out) ; 2.35 les engrenages du ventre tournent en or (+40°) ; 2.50 une bouffée de poussière d'or monte (24 points, seed fixe) ; 2.70 le balancier repart, doré (-18° → +18°) ; 2.85 la lumière du cadran déborde : un disque de lumière or-clair → creme s'ouvre depuis le cadran (rayon 60 → 1 200 px à l'écran, 0,38 s expo.in) ; 3.23 le cadre entier est la lumière d'or.
  PISTE CAMÉRA : dérive échelle +4 %/s de 2.10 à 2.85 ; plongée vers cam(2 780, 630, 2.4) de 2.85 à 3.23 (expo.in), sans flou de caméra.
  COUCHES ET PROFONDEUR : avant-plan la fumée qui se dissipe ; sujet l'horloge d'or ; brume aucune ; toile noire puis lumière ; couches animées 3.
  OBJET-PONT ET VECTEUR : la lumière du cadran devient tout le cadre (coupe franche à 3.23 sur la même lumière des deux côtés).
  SON : montée de lumière douce (riser) de 2.10 à 3.23 ; tic-tac doré 2.70.
  IMAGE CLÉ : 2.75 : l'horloge entière passée en silhouette d'or lumineuse dans le noir, ses engrenages qui tournent dans une poussière d'or.

## Frame 8: L'horloge se mit au travail · 34.60 → 38.03

- scene: La lumière d'or se resserre dans le cadran et découvre la cuisine passée au monde doré ; l'horloge roule jusqu'à la table, le père se lève et elle prend sa place, tamponne les devis qui deviennent d'or ; sur « pour lui » la chaîne éclate en oiseaux de papier ; les feuilles finies s'envolent seules par la fenêtre vers le jardin, le père tend la main à sa fille, la case se rallume, whip vers le jardin
- duration: 3.43s
- transition_in: cut
- status: outline
- src: compositions/frames/08-travail.html
- voiceover: "L'horloge se mit au travail pour lui. Tout s'automatisait."
- type: turn
- blueprint: camera-journey (Adapt)
- focal: l'horloge d'or au travail à la place du père, puis la chaîne qui éclate et la file de feuilles qui s'envole
- rules: particle-burst, waterfall-entry
- world: light
- handoff_in: à 0.00 : aucun raccord de caméra (coupe franche voulue) ; raccord de lumière : le cadre entier est la lumière d'or du cadran, dégradé radial #E0A84A au centre (960, 540) vers #FFF4DC au bord, sans grain, sans forme ni texte
- handoff_out: à 3.43 : cam(3500, 640, 1.27) flou 10 px ; caméra en plein whip vers la droite (+4 500 u/s en x, power2.in puis expo.out), dérive 0 ; monde : maison en coupe et jardin, monde doré (toile nuit, silhouettes inversées or) ; cuisine K rallumée en or, hors cadre à gauche : l'horloge d'or à la table à (2 460, 900) ; le père et la fille main dans la main au pied de l'escalier (2 960, 900) au bord gauche du cadre ; le mur droit de la maison et la rampe dorée floue (plan 1) au milieu du cadre ; une file de 12 feuilles d'or en vol vers la droite à y 500 à 600, en tête à (3 950, 520) ; jardin J, l'arbre nu sombre à (4 300, 900) au bord droit, la balançoire hors cadre ; poussière d'or ; sous-titre sorti ; grain par plan, flamme 1 ± 0,03

Word cues: L'horloge@0.36 se@0.90 mit@1.12 au@1.22 travail@1.40 pour@1.68 lui@1.94 Tout@2.36 s'automatisait@2.52

Scene 1 (0.00 à 2.20 s) : P18, l'horloge prend sa place, la chaîne éclate
  TEXTE ÉCRAN : sous-titre « L'horloge se mit au travail [boîte : pour lui]. » (L'horloge 0.36, se 0.90, mit 1.12, au 1.22, travail 1.40, boîte tracée 1.64, pour 1.68, lui 1.94), sorti de 2.18 à 2.32 ; écart : la chaîne éclate sur « lui » (1.94), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 la lumière d'or se resserre dans le cadran (disque 1 200 → 60 px, 0,3 s expo.out) et découvre la cuisine du monde doré au cadrage cam(2 660, 660, 1.35) : toile nuit, silhouettes inversées en or (l'horloge, le père assis, la table et sa pile, la lampe, la fille sur sa marche au bord droit), poussière d'or ; 0.36 « L'horloge » : elle roule vers la table (roulettes, 12 i/s) ; 0.60 le père se lève de sa chaise et recule d'un pas (deux poses) ; 0.90 « se » : l'horloge prend sa place à la table, ses engrenages tournent dans sa fenêtre (180°/s) ; 1.12 « mit » : son bras court tamponne la première feuille, qui devient d'or (0,06 s) ; 1.22 « au » : deuxième tampon ; 1.40 « travail » : troisième, les feuilles finies s'empilent à sa droite ; 1.68 « pour » : la chaîne du père s'illumine maillon par maillon (0,01 s d'écart) ; 1.94 « lui » : la chaîne éclate en 12 oiseaux de papier dorés (0,02 s d'écart) qui s'envolent vers la droite et sortent par F2 ; 2.05 le père lève son poignet libre (pose).
  PISTE CAMÉRA : dérive x +20 u/s, échelle +1,5 %/s de 0.00 à 2.20.
  COUCHES ET PROFONDEUR : avant-plan la suspension de casseroles floue, or sombre, en haut à gauche ; sujet l'horloge d'or au travail et le père ; brume F2 et la nuit étoilée dorée ; toile nuit ; couches animées 3 à 4.
  OBJET-PONT ET VECTEUR : les oiseaux de la chaîne partent vers la droite par F2 (vecteur du plan suivant) ; les feuilles finies, dorées.
  SON : roulettes 0.36 ; bois (le père se lève) 0.60 ; tampons de bois sec 1.12, 1.22, 1.40 ; maillons 1.68 ; battements d'ailes de 1.94 à 2.30 ; la musique, claire.
  IMAGE CLÉ : 2.00 : dans la cuisine dorée, l'horloge d'or assise à la place du père tamponne une feuille pendant que la chaîne éclate en oiseaux de papier ; le père debout lève son poignet libre ; « pour lui » en boîte.

Scene 2 (2.20 à 3.43 s) : P19, tout s'automatise, les feuilles s'envolent vers le jardin
  TEXTE ÉCRAN : sous-titre « Tout [boîte : s'automatisait]. » (Tout 2.36, boîte tracée 2.48, s'automatisait 2.52), sorti de 3.24 à 3.38 ; écart synchro (les feuilles se lèvent sur « Tout »).
  ÉTAPES : 2.20 cran court sur la pile (0,2 s expo.inOut) ; 2.36 « Tout » : les feuilles d'or se lèvent seules de la pile, une colonne de 12 (0,02 s d'écart) ; 2.52 « s'automatisait » : elles s'envolent en file par F2 vers la droite, comme des oiseaux (courbe, 0,4 s chacune) ; 2.70 le père tend la main vers sa fille sur la marche ; 2.85 elle saute de la marche et prend sa main (deux poses) ; 3.00 F2 et la case de la cuisine se rallument en or (signature 1 : voile → 0, toile dorée, bouffée de poussière) ; 3.10 départ du whip vers la droite qui suit les feuilles (power2.in, flou 0 → 10).
  PISTE CAMÉRA : cran court sur la pile, vers cam(2 720, 670, 1.45), de 2.20 à 2.40 (expo.inOut), puis dérive x +30 u/s de 2.40 à 3.10 ; whip de cam(2 741, 670, 1.45) vers cam(4 500, 620, 1.15) dès 3.10 : à 3.43 cam(3 500, 640, 1.27) flou 10 px.
  COUCHES ET PROFONDEUR : avant-plan la rampe dorée floue au bord droit, qui balaie le cadre pendant le whip ; sujet la file de feuilles d'or ; brume F2 ; toile nuit ; couches animées 4.
  OBJET-PONT ET VECTEUR : la file de feuilles d'or vole vers l'arbre du jardin, où elle deviendra le tronc ; vecteur : whip vers la droite.
  SON : papier (les feuilles se lèvent) 2.36 ; ailes de papier de 2.52 à 3.10 ; souffle de lumière (la case se rallume) 3.00 ; whoosh de papier 3.10.
  IMAGE CLÉ : 2.80 : une file de feuilles d'or s'envole seule de la table vers la fenêtre ; le père tend la main à sa fille qui saute de la marche ; « s'automatisait » en boîte.

## Frame 9: La balançoire, le second dinosaure · 38.03 → 43.67

- scene: Au jardin, la file de feuilles d'or s'empile autour du tronc de l'arbre nu, qui devient l'arbre doré ; le soir suivant, le père pousse la balançoire de sa fille dans l'arc du balancier de l'horloge ; le soir d'après, à la clôture, ils tracent un second dinosaure en lignes d'or à côté du premier dessin ; la grue remonte vers la branche
- duration: 5.64s
- transition_in: cut
- status: outline
- src: compositions/frames/09-balancoire.html
- voiceover: "Le soir suivant, il poussait la balançoire. Celui d'après, ils dessinèrent un second dinosaure."
- type: payoff
- blueprint: camera-journey (Adapt)
- focal: le tronc d'or et la balançoire poussée, puis le second dinosaure qui se trace
- rules: svg-path-draw, sine-wave-loop
- world: light
- handoff_in: à 0.00 : cam(3500, 640, 1.27) flou 10 px ; caméra en plein whip vers la droite (+4 500 u/s en x, power2.in puis expo.out), dérive 0 ; monde : maison en coupe et jardin, monde doré (toile nuit, silhouettes inversées or) ; cuisine K rallumée en or, hors cadre à gauche : l'horloge d'or à la table à (2 460, 900) ; le père et la fille main dans la main au pied de l'escalier (2 960, 900) au bord gauche du cadre ; le mur droit de la maison et la rampe dorée floue (plan 1) au milieu du cadre ; une file de 12 feuilles d'or en vol vers la droite à y 500 à 600, en tête à (3 950, 520) ; jardin J, l'arbre nu sombre à (4 300, 900) au bord droit, la balançoire hors cadre ; poussière d'or ; sous-titre sorti ; grain par plan, flamme 1 ± 0,03
- handoff_out: à 5.64 : cam(5310, 655, 1.35) flou 6 px ; caméra en pleine montée de grue (y -260 u/s, échelle -1,2/s, expo.inOut), dérive 0 ; monde : jardin J, monde doré ; l'arbre d'or au tronc de devis à (4 300, 900), sa branche maîtresse jusqu'à (5 450, 300), feuilles d'or ; la balançoire dorée vide qui oscille (±8°) hors cadre à gauche ; la clôture dorée, le dessin du petit dinosaure sur le poteau (5 200, 770), le second dinosaure en lignes d'or sur le poteau (5 360, 770), le père et la fille agenouillés devant, l'horloge d'or à (5 520, 900) ; herbes floues (plan 1) en bas ; poussière d'or ; sous-titre sorti ; grain par plan, flamme 1 ± 0,03

Word cues: Le@0.22 soir@0.45 suivant@0.59 il@1.13 poussait@1.33 la@1.61 balançoire@1.79 Celui@2.63 d'après@2.93 ils@3.55 dessinèrent@3.73 un@4.13 second@4.41 dinosaure@4.73

Scene 1 (0.00 à 2.45 s) : P20, le tronc d'or, il poussait la balançoire
  TEXTE ÉCRAN : sous-titre « Le soir suivant, il poussait la [boîte : balançoire]. » (Le 0.22, soir 0.45, suivant 0.59, il 1.13, poussait 1.33, la 1.61, boîte tracée 1.75, balançoire 1.79), sorti de 2.30 à 2.44 ; écart : le tronc s'élève sur « Le soir suivant » (0.22 à 0.59), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.22 fin du whip, atterrissage sur cam(4 500, 620, 1.15) (expo.out, flou 10 → 0) : l'arbre nu sombre, la balançoire à sa branche, la fille assise dessus et le père derrière elle en silhouettes sombres à peine lisibles sur la nuit ; l'horloge d'or au pied de l'arbre (4 120, 900) ; 0.10 la file de feuilles d'or s'enroule autour du tronc ; 0.22 « Le » : premier cran de la pile autour du tronc (du sol à y 760) ; 0.45 « soir » : deuxième cran (à y 560) ; 0.59 « suivant » : troisième cran (à la fourche, y 360) : le tronc est une pile de devis d'or ; 0.75 les branches s'allument d'or de la fourche vers les pointes (0,2 s), seize feuilles d'or s'y posent (0,01 s d'écart) ; 0.90 l'or descend les deux cordes de la balançoire et passe sur la fille et le père (silhouettes inversées, masque 0,15 s) ; 1.00 l'horloge pose une dernière feuille sur une petite pile au pied du tronc ; 1.13 « il » : le père pose ses deux mains à plat sur le dos de sa fille (pose) ; 1.33 « poussait » : il pousse, la balançoire part vers l'avant (+18°, demi-période 0,8 s sine.inOut) ; 1.61 « la » : les couettes de la fille volent en arrière ; 1.79 « balançoire » : au sommet de l'arc, une poussière d'or s'échappe de ses pieds ; au pied de l'arbre, le balancier de l'horloge bat dans le même arc, à la même cadence (rime, signature 2) ; 2.13 la balançoire revient, il la reçoit et la repousse (pose) ; 2.40 l'arc repart.
  PISTE CAMÉRA : atterrissage expo.out de 0.00 à 0.22 ; dérive x +20 u/s, échelle +1 %/s de 0.22 à 2.45.
  COUCHES ET PROFONDEUR : avant-plan des herbes hautes floues en bas (parallaxe ×1,8) et une branche basse floue en haut à droite ; sujet l'arbre d'or, la balançoire, le père et la fille ; brume collines et arbres lointains, nuit ; toile nuit ; couches animées 4.
  OBJET-PONT ET VECTEUR : la pile de devis portée à l'accroche devient le tronc d'or (rime) ; le balancier et la balançoire dans le même arc ; vecteur : la balançoire part vers la droite, la caméra glisse vers la clôture.
  SON : papier (la pile se pose) 0.22, 0.45, 0.59 ; scintillement (l'arbre s'allume) 0.75 ; corde et bois de la balançoire 1.33, 2.13 ; tic-tac doré à la même cadence ; vent doux.
  IMAGE CLÉ : 1.80 : sous l'arbre doré au tronc de devis, le père pousse la balançoire de sa fille, ses deux mains sur son dos ; au pied de l'arbre, l'horloge dont le balancier bat dans le même arc ; « balançoire » en boîte.

Scene 2 (2.45 à 5.64 s) : P21, le soir d'après, le second dinosaure
  TEXTE ÉCRAN : sous-titre en deux morceaux : « Celui d'après, ils dessinèrent » (Celui 2.63, d'après 2.93, ils 3.55, dessinèrent 3.73), remplacé à 4.10 par « un [boîte : second dinosaure]. » (un 4.13, boîte tracée 4.37, second 4.41, dinosaure 4.73), sorti de 5.25 à 5.39 ; écart : le dessin se trace sur « dessinèrent » (3.73), synchro.
  ÉTAPES : 2.45 départ du cran vers la clôture (expo.inOut 0,4 s) ; 2.63 « Celui » : le ciel tourne d'un cran (les étoiles glissent, la toile change de teinte d'un cran : un soir de plus) ; 2.85 fin du cran sur cam(5 280, 700, 1.5) : la clôture dorée, le père et la fille agenouillés devant deux poteaux, le dessin du petit dinosaure épinglé au premier (5 200, 770), une carte blanche au second (5 360, 770) ; 2.93 « d'après » : l'horloge d'or roule depuis la gauche et s'arrête à (5 520, 900) ; 3.20 la fille lève son crayon (pose) ; 3.55 « ils » : le père lève le sien (pose) ; 3.73 « dessinèrent » : le second dinosaure se trace en lignes d'or sur la carte blanche (cou, dos, queue, pattes, 0,4 s power2.out) ; 4.13 « un » : le champignon se trace au-dessus (0,15 s) ; 4.41 « second » : son œil (un point) ; 4.73 « dinosaure » : la carte s'illumine d'un halo or, les deux dessins côte à côte ; 5.00 la fille serre le bras de son père (pose) ; 5.30 départ de la grue vers la branche (expo.inOut).
  PISTE CAMÉRA : cran de cam(4 545, 620, 1.18) vers cam(5 280, 700, 1.5) de 2.45 à 2.85, puis dérive x +16 u/s, échelle +1,5 %/s de 2.85 à 5.30 ; grue dès 5.30 : à 5.64 cam(5 310, 655, 1.35) flou 6 px.
  COUCHES ET PROFONDEUR : avant-plan les herbes hautes floues en bas et une branche basse floue en haut ; sujet les deux cartes sur leurs poteaux, le père et la fille agenouillés ; brume collines en brume nuit ; toile nuit ; couches animées 3.
  OBJET-PONT ET VECTEUR : le second dinosaure répond au premier (rime) ; la grue remonte vers la branche où pendront les lettres.
  SON : roulettes 2.93 ; crayon sur papier de 3.73 à 4.20 ; vent doux ; tic-tac lointain.
  IMAGE CLÉ : 4.80 : à la clôture dorée, le dessin du petit dinosaure épinglé sur un poteau et, sur le poteau voisin, un second dinosaure tracé en lignes d'or ; le père et sa fille agenouillés devant ; « second dinosaure » en boîte.

## Frame 10: Intelligence Artificielle · 43.67 → 49.47

- scene: Sous la branche dorée, deux fils d'or descendent et les lettres I et A retombent, dorées, au-dessus du père et de sa fille, puis se déplient en « Intelligence Artificielle » ; un trait d'or ; les mots se replient ; l'horloge tourne ses aiguilles à rebours et un ruban de poussière d'or va de son cadran à la famille ; le recul final commence
- duration: 5.80s
- transition_in: cut
- status: outline
- src: compositions/frames/10-intelligence.html
- voiceover: "Désormais, I.A. voulait dire Intelligence Artificielle, pour vous rendre le temps perdu."
- type: payoff
- blueprint: titlecard-reveal (Adapt)
- focal: les lettres d'or « Intelligence Artificielle », puis les aiguilles qui reculent
- rules: sine-wave-loop, ambient-glow-bloom
- world: light
- handoff_in: à 0.00 : cam(5310, 655, 1.35) flou 6 px ; caméra en pleine montée de grue (y -260 u/s, échelle -1,2/s, expo.inOut), dérive 0 ; monde : jardin J, monde doré ; l'arbre d'or au tronc de devis à (4 300, 900), sa branche maîtresse jusqu'à (5 450, 300), feuilles d'or ; la balançoire dorée vide qui oscille (±8°) hors cadre à gauche ; la clôture dorée, le dessin du petit dinosaure sur le poteau (5 200, 770), le second dinosaure en lignes d'or sur le poteau (5 360, 770), le père et la fille agenouillés devant, l'horloge d'or à (5 520, 900) ; herbes floues (plan 1) en bas ; poussière d'or ; sous-titre sorti ; grain par plan, flamme 1 ± 0,03
- handoff_out: à 5.80 : cam(4760, 640, 1.11) flou 6 px ; caméra en plein recul vers la gauche et vers le haut (x -2 600 u/s, échelle -1,0/s, power2.in puis expo.out), dérive 0 ; monde : maison en coupe et jardin, monde doré ; jardin : l'arbre d'or à (4 300, 900), la balançoire dorée qui oscille, la clôture et ses deux dessins, le père debout avec la fille sur ses épaules à (5 280, 900), l'horloge d'or à (5 520, 900) ; la maison hors cadre à gauche, seule la cuisine allumée en or ; poussière d'or ; sous-titre sorti ; grain par plan, flamme 1 ± 0,03

Word cues: Désormais@0.48 IA@1.30 voulait@1.79 dire@2.09 Intelligence@2.55 Artificielle@3.13 pour@4.15 vous@4.29 rendre@4.53 le@4.75 temps@4.99 perdu@5.19

Scene 1 (0.00 à 2.30 s) : P22, sous la branche, I et A retombent, dorés
  TEXTE ÉCRAN : sous-titre « Désormais, [boîte : IA] voulait dire » (Désormais 0.48, boîte tracée 1.26, IA 1.30, voulait 1.79, dire 2.09) ; il reste jusqu'à 3.80 puis sort (3.80 à 3.94) ; écart : les lettres tombent sur « IA » (1.30), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.35 fin de la grue sur cam(5 300, 610, 1.15) (expo.out, flou 6 → 0) : la branche d'or en haut, la clôture et la famille en bas ; 0.48 « Désormais » : une bouffée de poussière d'or tombe de la branche ; 0.75 le père se relève, la fille aussi (deux poses) ; 1.00 elle lève le bras vers la branche (pose) ; 1.30 « IA » : deux fils d'or descendent de la branche et les initiales I et A, or-clair, Fraunces 700 84 px, tombent au bout (0,25 s power3.out), centrées à l'écran ; 1.50 elles se balancent (±6° amorti sur 1,2 s, répétitions finies) ; 1.79 « voulait » : le I descend sur la première ligne, le A sur la seconde (0,2 s power3.out) ; 2.09 « dire » : les fils se tendent, poussière d'or.
  PISTE CAMÉRA : fin de la grue expo.out de 0.00 à 0.35 ; dérive échelle +1,5 %/s, y +4 u/s de 0.35 à 2.30.
  COUCHES ET PROFONDEUR : avant-plan des herbes hautes floues en bas et une branche basse floue en haut à gauche ; sujet les lettres d'or ; brume collines nuit ; toile nuit ; couches animées 3.
  OBJET-PONT ET VECTEUR : I et A sont les lettres de la marche (séquence 4), dorées (rime).
  SON : fils de bois léger 1.30 ; papier 1.79.
  IMAGE CLÉ : 1.60 : sous la branche dorée, deux lettres de papier d'or I et A suspendues au-dessus du père et de sa fille, la clôture et les deux dessins en bas ; « IA » en boîte.

Scene 2 (2.30 à 3.95 s) : P23, Intelligence Artificielle
  TEXTE ÉCRAN : moment typographique : « Intelligence » (2.55) puis « Artificielle » (3.13) se déplient depuis leurs initiales sur deux lignes centrées, Fraunces 600 84 px or-clair (initiales en 700) ; [trait : Artificielle] tracé à 3.13 ; en bas, le sous-titre « Désormais, IA voulait dire » reste jusqu'à 3.80 ; écart synchro.
  ÉTAPES : 2.30 cran court sur les mots (0,25 s expo.inOut) ; 2.55 « Intelligence » : n, t, e, l, l, i, g, e, n, c, e glissent de derrière le I (0,03 s d'écart, 0,12 s expo.out) ; 2.90 la fille tape dans ses mains (pose) ; 3.13 « Artificielle » : r, t, i, f, i, c, i, e, l, l, e glissent de derrière le A et le trait d'or se trace dessous (0,4 s power2.out) ; 3.40 le halo des lettres monte (+20 %, 0,1 s) ; 3.60 la balançoire vide se balance au bord gauche ; 3.86 fin de la phrase, les mots se balancent (±3°).
  PISTE CAMÉRA : cran d'échelle sur les mots, vers cam(5 300, 640, 1.24), de 2.30 à 2.55 (expo.inOut) ; dérive échelle +1,5 %/s, y +4 u/s de 2.55 à 3.95.
  COUCHES ET PROFONDEUR : avant-plan herbes floues et branche basse ; sujet les mots d'or ; brume collines nuit ; toile nuit ; couches animées 3.
  OBJET-PONT ET VECTEUR : les mots se replieront dans leurs initiales et remonteront ; le regard descend vers l'horloge.
  SON : papier (les mots se déplient) 2.55, 3.13 ; bois léger (les mains) 2.90.
  IMAGE CLÉ : 3.50 : « Intelligence » et « Artificielle » en lettres de papier d'or pendues sous la branche au-dessus du père et de sa fille, un trait d'or sous « Artificielle ».

Scene 3 (3.95 à 5.80 s) : P24, pour vous rendre le temps perdu
  TEXTE ÉCRAN : sous-titre « pour vous [trait : rendre] [boîte : le temps perdu]. » (pour 4.15, vous 4.29, rendre 4.53 et son trait, boîte tracée 4.71, le 4.75, temps 4.99, perdu 5.19), sorti de 5.55 à 5.69 ; écart : les aiguilles reculent sur « rendre » (4.53), synchro.
  ÉTAPES : 3.95 les mots se replient dans leurs initiales et les fils remontent dans la branche (0,15 s power2.in), la caméra descend d'un cran vers l'horloge et la famille (0,3 s expo.inOut) ; 4.15 « pour » : l'horloge tourne son cadran vers le père et la fille (pose) ; 4.29 « vous » : le père hisse sa fille sur ses épaules (deux poses) ; 4.53 « rendre » : les aiguilles de l'horloge font un tour à rebours (0,4 s power2.inOut) ; 4.75 « le » : un ruban de poussière d'or part du cadran vers la famille ; 4.99 « temps » : second tour à rebours ; 5.19 « perdu » : la poussière se pose autour d'eux en petites étoiles ; 5.40 départ du recul final (power2.in, flou 0 → 6).
  PISTE CAMÉRA : cran vers l'horloge et la famille, cam(5 400, 690, 1.35), de 3.95 à 4.25 (expo.inOut), puis dérive x +10 u/s, échelle +1 %/s de 4.25 à 5.40 ; recul dès 5.40 : à 5.80 cam(4 760, 640, 1.11) flou 6 px.
  COUCHES ET PROFONDEUR : avant-plan herbes floues ; sujet l'horloge et la famille ; brume collines nuit ; toile nuit ; couches animées 3 à 4.
  OBJET-PONT ET VECTEUR : les aiguilles qui reculent rendent le temps ; le recul rassemble le film.
  SON : bois léger (il hisse sa fille) 4.29 ; cliquetis des aiguilles à rebours de 4.53 à 5.20 ; souffle doux 4.75 ; whoosh cinématique doux 5.40.
  IMAGE CLÉ : 5.00 : à la clôture dorée, l'horloge d'or tourne ses aiguilles à rebours vers le père qui porte sa fille sur ses épaules, un ruban de poussière d'or de son cadran jusqu'à eux ; « le temps perdu » en boîte, « rendre » souligné d'or.

## Frame 11: La maison relevée, la preuve · 49.47 → 53.10

- scene: Le recul découvre tout le monde : la maison en coupe à gauche, dont les six cases se rallument en or une à une, et à droite l'arbre d'or avec sa balançoire au-dessus de la clôture ; dans le ciel de nuit, « 10 h » roule de 0 à 10 avec « gagnées chaque semaine » et « par la dernière dirigeante formée » ; les feuilles de l'arbre s'envolent en oiseaux vers la caméra
- duration: 3.63s
- transition_in: cut
- status: outline
- src: compositions/frames/11-preuve.html
- voiceover: "La dernière dirigeante formée gagne dix heures chaque semaine."
- type: proof
- blueprint: dataviz-countup (Adapt)
- focal: le chiffre « 10 h » qui roule dans le ciel au-dessus de la maison relevée
- rules: counting-dynamic-scale
- world: light
- handoff_in: à 0.00 : cam(4760, 640, 1.11) flou 6 px ; caméra en plein recul vers la gauche et vers le haut (x -2 600 u/s, échelle -1,0/s, power2.in puis expo.out), dérive 0 ; monde : maison en coupe et jardin, monde doré ; jardin : l'arbre d'or à (4 300, 900), la balançoire dorée qui oscille, la clôture et ses deux dessins, le père debout avec la fille sur ses épaules à (5 280, 900), l'horloge d'or à (5 520, 900) ; la maison hors cadre à gauche, seule la cuisine allumée en or ; poussière d'or ; sous-titre sorti ; grain par plan, flamme 1 ± 0,03
- handoff_out: à 3.63 : cam(2850, 168, 0.35) flou 0 ; dérive échelle +1 %/s, y +6 u/s en cours ; monde : maison et jardin, monde doré, toutes les cases allumées en or, l'arbre d'or, la balançoire, la clôture et ses deux dessins, le père et la fille, l'horloge ; bloc de preuve en haut au centre (« 10 h », « gagnées chaque semaine », « par la dernière dirigeante formée ») ; une vague de 20 oiseaux de papier d'or partis de l'arbre (4 300, 400) qui volent vers la caméra, les plus proches ×3 et flous 10 px sur la moitié droite du cadre ; sous-titre vide ; grain par plan, flamme 1 ± 0,03

Word cues: La@0.36 dernière@0.65 dirigeante@0.95 formée@1.39 gagne@1.83 dix@2.19 heures@2.51 chaque@2.79 semaine@3.01

Scene 1 (0.00 à 3.63 s) : P25, la maison relevée, 10 h dans le ciel
  TEXTE ÉCRAN : aucun sous-titre ; bloc de preuve centré en haut de l'écran : « 10 h » (Fraunces 700 150 px or-clair, centré à (960, 330)) qui roule de 0 à 10 ; dessous, en DM Sans 500 40 px creme, « gagnées chaque semaine » (gagnées 2.51, chaque 2.79, semaine 3.01) puis « par la dernière dirigeante formée » (par 0.36, la 0.50, dernière 0.65, dirigeante 0.95, formée 1.39), mot par mot ; écart : le chiffre se pose sur « dix » (2.19), synchro.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.60 fin du recul sur cam(2 850, 150, 0.34) (expo.out, flou 6 → 0) : la maison en coupe à gauche, cases éteintes sauf la cuisine, l'arbre d'or et la clôture à droite, la nuit au-dessus ; 0.36 « La » : l'entrée se rallume en or (signature 1, voile → 0, bouffée de poussière) ; 0.65 « dernière » : le salon ; 0.95 « dirigeante » : la chambre des parents ; 1.10 « 0 h » arrive (×1,4 et flou 8 px → net, 0,15 s) ; 1.20 le chiffre commence à rouler (0 → 10, power2.out, chiffres entiers, tabular-nums) ; 1.39 « formée » : le bureau de l'étage ; 1.60 la chambre de la fille ; 1.83 « gagne » : le grenier, toute la maison est d'or ; 2.19 « dix » : « 10 h » se pose (×1,06 → 1, 0,1 s) ; 2.51 « heures » : la balançoire repart au jardin ; 2.79 « chaque » : une bouffée de poussière d'or monte de l'arbre ; 3.01 « semaine » : les feuilles de l'arbre frémissent ; 3.30 elles se détachent et s'envolent en oiseaux de papier vers la caméra (20 oiseaux, ×1 → ×3, flou 0 → 10 px).
  PISTE CAMÉRA : fin du recul expo.out de 0.00 à 0.60 ; dérive échelle +1 %/s, y +6 u/s de 0.60 à 3.63.
  COUCHES ET PROFONDEUR : avant-plan des herbes hautes floues en bas, puis les oiseaux qui grandissent ; sujet la maison et le jardin dorés ; brume collines nuit ; toile nuit, le ciel ; couches animées 3 à 4.
  OBJET-PONT ET VECTEUR : les feuilles d'or de l'arbre deviennent des oiseaux qui balaient le cadre vers la carte de fin.
  SON : six notes de bois clair, une par case qui se rallume, de 0.36 à 1.83 ; cliquetis léger du chiffre de 1.20 à 2.19 ; vent doux dans l'arbre 3.01 ; battements d'ailes dès 3.30.
  IMAGE CLÉ : 2.40 : toute la maison en coupe rallumée en or à gauche, l'arbre d'or et la balançoire à droite, la nuit au-dessus, et dans le ciel « 10 h » au-dessus de ses deux lignes, « gagnées chaque semaine » et « par la dernière dirigeante formée ».

## Frame 12: Réserver un audit IA · 53.10 → 57.10

- scene: Les oiseaux de papier d'or balaient le cadre et découvrent la toile claire du début ; la signature « Antoine Contino » s'écrit en bordeaux, « formateur IA » dessous ; le bouton bordeaux « Réserver un audit IA de 30 minutes » se pose avec la ligne d'adresses dessous, puis le curseur de papier arrive et clique ; tenue vivante, puis le noir
- duration: 4.00s
- transition_in: cut
- status: outline
- src: compositions/frames/12-fin.html
- voiceover: ""
- type: cta
- blueprint: cta-morph-press (Adapt)
- focal: la signature, puis le bouton et le clic
- rules: cursor-click-ripple, press-release-spring
- world: light
- handoff_in: à 0.00 : cam(2850, 168, 0.35) flou 0 ; dérive échelle +1 %/s, y +6 u/s en cours ; monde : maison et jardin, monde doré, toutes les cases allumées en or, l'arbre d'or, la balançoire, la clôture et ses deux dessins, le père et la fille, l'horloge ; bloc de preuve en haut au centre (« 10 h », « gagnées chaque semaine », « par la dernière dirigeante formée ») ; une vague de 20 oiseaux de papier d'or partis de l'arbre (4 300, 400) qui volent vers la caméra, les plus proches ×3 et flous 10 px sur la moitié droite du cadre ; sous-titre vide ; grain par plan, flamme 1 ± 0,03
- handoff_out: aucun (fin du film, noir à 4.00)

Word cues: aucun mot (carte de fin muette, tenue jusqu'à 4.00)

Scene 1 (0.00 à 0.95 s) : P26, les oiseaux balaient, la toile claire, la signature
  TEXTE ÉCRAN : signature « Antoine Contino » (Caveat 700 120 px bordeaux, centrée à (960, 360)) révélée par un masque de 0.40 à 1.20 ; « formateur IA » (DM Sans 500 34 px brume-2, à (960, 450)) à 0.85 ; aucun sous-titre.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 la vague d'oiseaux d'or grandit vers la caméra et couvre le cadre de droite à gauche (le plus proche ×6, flou 18 px, 0,3 s power2.in) ; 0.15 le bloc de preuve passe sous les ailes ; 0.30 derrière les ailes paraît la toile claire du début (ground-toile, palette claire, flamme) ; 0.40 la signature commence à s'écrire (masque 0,8 s power1.inOut) ; 0.45 les derniers oiseaux sortent par la gauche, flous ; 0.65 la poussière d'or laissée par les ailes retombe ; 0.85 « formateur IA » paraît (×1,1 et flou 4 px → net, 0,12 s).
  PISTE CAMÉRA : dérive échelle +1,5 %/s sur la toile de 0.00 à 4.00 (le grain glisse).
  COUCHES ET PROFONDEUR : avant-plan les oiseaux flous qui sortent ; sujet la signature ; brume une nappe claire au bas de la toile ; toile claire ; couches animées 3.
  OBJET-PONT ET VECTEUR : un dernier oiseau reste et traversera petit en haut (tenue vivante) ; vecteur : les oiseaux sortent vers la gauche.
  SON : battements d'ailes de 0.00 à 0.45 ; plume sur papier de 0.40 à 1.20.
  IMAGE CLÉ : 0.80 : « Antoine Contino » qui s'écrit en bordeaux sur la toile sépia claire du début, les derniers oiseaux de papier flous qui quittent le cadre à gauche.

Scene 2 (0.95 à 2.00 s) : P27, le bouton, l'adresse, le clic
  TEXTE ÉCRAN : bouton « Réserver un audit IA de 30 minutes » (DM Sans 700 32 px creme sur bordeaux, centré à (960, 640)) à 1.00 ; « calendly.com/antoine-cntno/30min · antoinecontino.fr » (DM Sans 500 24 px brume-2, centré à (960, 740)) à 1.20.
  ÉTAPES : 1.00 le bouton arrive (×1,1 et flou 6 px → net, 0,15 s expo.out) ; 1.20 la ligne d'adresses paraît mot à mot (0,04 s d'écart) ; 1.35 le curseur de papier arrive du bas droit en un seul mouvement courbe (0,45 s power3.out en x, power2.out en y) ; 1.80 clic direct : pression ×0,94 (0,06 s), couleurs bordeaux → bordeaux-clair → creme → bordeaux (0,27 s), onde bordeaux qui s'ouvre et s'efface (0,45 s) ; 1.92 retour à ×1 (0,12 s).
  PISTE CAMÉRA : dérive continue.
  COUCHES ET PROFONDEUR : avant-plan le curseur et son ombre douce ; sujet le bouton ; brume la nappe claire ; toile claire ; couches animées 2 à 3.
  OBJET-PONT ET VECTEUR : le curseur reste posé sur le bouton.
  SON : papier (le bouton se pose) 1.00 ; clic de bois léger 1.80.
  IMAGE CLÉ : 1.85 : la signature bordeaux, « formateur IA », le bouton bordeaux pressé sous le curseur de papier et son onde, la ligne d'adresses.

Scene 3 (2.00 à 4.00 s) : P28, la tenue vivante, le noir
  TEXTE ÉCRAN : le même texte tient.
  ÉTAPES : 2.00 la flamme de la toile vacille ; 2.30 un dernier oiseau de papier traverse petit en haut à droite (1,0 s, battements à 12 i/s) ; 2.70 la poussière d'or retombe lentement ; 3.10 le bouton respire une fois (×1 → 1,01 → 1, 1,2 s sine.inOut) ; 3.40 le grain glisse avec la dérive ; 3.70 à 4.00 le noir monte (opacité 0 → 1, power1.in).
  PISTE CAMÉRA : dérive continue jusqu'au noir.
  COUCHES ET PROFONDEUR : avant-plan l'oiseau qui passe ; sujet la carte de fin ; brume la nappe claire ; toile claire ; couches animées 3.
  OBJET-PONT ET VECTEUR : aucun (fin du film).
  SON : ailes légères 2.30 ; la musique finit sur sa note tenue.
  IMAGE CLÉ : 2.80 : la carte de fin entière sur la toile claire, un petit oiseau de papier qui passe en haut à droite dans la poussière d'or qui retombe.
