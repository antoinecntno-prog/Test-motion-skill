# Le Temps perdu : trois directions de storyboard (à choisir avant d'écrire le storyboard complet)

Même voix, même musique, mêmes bruitages pour les trois directions : seule la mise en scène change. Les trois gardent
la grammaire d'ombres du brief : silhouettes brun noir découpées devant une toile de papier sépia éclairée par
derrière, marionnettes à pivots (rivets visibles aux articulations), quatre plans de profondeur (avant-plan sombre et
flou, personnages nets, décor de brume, toile lumineuse), grain de papier, vignettage chaud. Le monde de la solution
passe en silhouettes inversées dorées sur une toile assombrie, avec une poussière d'étincelles. Les personnages et
l'horloge sont communs aux trois directions (`styleframes/_ombres.js`) : le père, sa fille de cinq ans à deux
couettes, le Temps perdu en horloge comtoise trapue sur roulettes, la chaîne de maillons de papier, le petit
dinosaure sous son champignon.

## Minutage global de la voix (secondes du film, voix montée de 57,10 s)

| # | Phrase | Début | Fin | Silence après |
|---|---|---|---|---|
| 1 | Ce dirigeant ramenait le travail à la maison. | 0.06 | 2.06 | 0.46 s |
| 2 | Derrière lui, le Temps perdu passa la porte. | 2.52 | 5.02 | 0.43 s |
| 3 | Sa fille l'attendait pour jouer. | 5.48 | 6.67 | 0.43 s |
| 4 | Lui, il ouvrit un dossier. | 7.10 | 8.57 | 0.45 s |
| 5 | Le Temps perdu lui prit une heure. | 9.02 | 10.46 | 0.59 s |
| 6 | Elle l'attendait pour dessiner. | 11.05 | 12.17 | 0.42 s |
| 7 | Lui, il ouvrit ses devis. | 12.59 | 14.12 | 0.38 s |
| 8 | Le Temps perdu lui prit la soirée. | 14.50 | 16.08 | 0.68 s |
| 9 | Pour sa fille, IA voulait dire Interminable Attente. | 16.76 | 20.08 | 0.54 s |
| 10 | Soir après soir, il s'effaçait. | 20.68 | 22.57 | 2.94 s (gag muet) |
| 11 | Alors elle retrouva leur petit dinosaure. | 25.51 | 27.50 | 0.43 s |
| 12 | Elle le glissa sur ses devis. | 27.93 | 29.16 | 0.46 s |
| 13 | Enfin, il vit la chaîne. | 29.62 | 30.89 | 0.95 s |
| 14 | Le Temps perdu eut alors une idée. (pivot sur noir) | 31.84 | 33.40 | 1.56 s |
| 15 | L'horloge se mit au travail pour lui. | 34.96 | 36.66 | 0.30 s |
| 16 | Tout s'automatisait. | 36.96 | 37.82 | 0.43 s |
| 17 | Le soir suivant, il poussait la balançoire. | 38.25 | 40.23 | 0.43 s |
| 18 | Celui d'après, ils dessinèrent un second dinosaure. | 40.66 | 43.19 | 0.96 s |
| 19 | Désormais, IA voulait dire Intelligence Artificielle, | 44.15 | 47.53 | 0.29 s |
| 20 | pour vous rendre le temps perdu. | 47.82 | 49.11 | 0.72 s |
| 21 | La dernière dirigeante formée gagne dix heures chaque semaine. | 49.83 | 52.75 | carte de fin |

Repères mot à mot : `onsets.json`. Les trois directions sont montrées aux mêmes trois moments pour se comparer :
l'entrée du Temps perdu (4,2 s), le premier sens d'IA (19,6 s), la balançoire dorée (39,5 s).

## A. « La maison en coupe » (recommandée)

**Concept.** La maison du père, découpée en coupe comme une maison de poupée de papier, debout devant la toile. La
caméra la parcourt en un seul long travelling latéral, de l'entrée au salon, puis à l'étage et jusqu'au jardin :
chaque pièce est une case de lumière où vit une scène à deux personnages. À chaque heure prise par le Temps perdu, une
case s'éteint ; dans le monde doré, les cases se rallument l'une après l'autre et la caméra sort au jardin.

**Fil des objets-ponts.** L'horloge roule de pièce en pièce avec la caméra : seul personnage continu, elle guide le
travelling. La chaîne relie le poignet du père au balancier à travers les murs. La balançoire, vue d'abord par la
fenêtre du salon, attend dehors pendant toute la douleur. Le dessin de la fillette, collé à la vitre, ouvre la
chambre. Au pivot, le balancier doré se change en balançoire dans le même arc. Signatures : la case qui s'éteint
(deux fois, puis rallumée), le balancier qui devient balançoire (rime de la fin).

**Images de style.**
- A1 (4,2 s) : plan large de la maison en coupe. Le père entre, la pile de devis sous le bras ; l'horloge roule dans
  l'encadrement de la porte, la chaîne tendue jusqu'à son poignet. Salon assombri, balançoire vue par la fenêtre,
  cuisine déjà pleine de dossiers. Avant-plan flou : montant de porte et plante, coupés par le bord du cadre.
- A2 (19,6 s) : la caméra est montée à l'étage. Sur la dernière marche, la fillette assise, le menton dans les
  mains ; au-dessus d'elle, deux grandes lettres de papier, I et A, dépliées en « Interminable Attente ». Dans la case
  voisine, le père penché sur ses devis s'éloigne de la toile : son ombre grandit, floue et pâle. L'horloge bat au
  fond du couloir.
- A3 (39,5 s) : le monde doré. Toile assombrie, maison en lumière, cases rallumées. Au jardin, le père pousse la
  balançoire de sa fille, en silhouettes dorées ; par la fenêtre de la cuisine, l'horloge dorée sort les devis
  finis. Poussière d'étincelles.

## B. « Le montreur »

**Concept.** Le film montre le théâtre d'ombres lui-même : la toile, et au-dessus de son bord, les tiges et les
rouages. L'horloge est le montreur : ses engrenages tirent les tiges du père, qui refait chaque soir les mêmes
gestes. La fillette n'a aucune tige : elle bouge librement. Au renversement, l'horloge raccroche ses tiges aux devis,
qui marchent seuls jusqu'à la pile dorée, et les tiges du père tombent : il pousse la balançoire de ses propres
mains.

**Fil des objets-ponts.** Les tiges passent du père aux devis. L'engrenage qui tourne dit le temps du travail en
cycle. Les lettres I et A pendent à des fils, comme un mobile au-dessus de la scène. La balançoire pend aux mêmes
fils que tenaient les tiges. Signatures : la tige qui tire le bras du père (deux fois), le fil coupé (rime de la fin).

**Images de style.**
- B1 (4,2 s) : la scène du théâtre d'ombres, vue de la salle, avec le bord haut de la toile dans le cadre.
  L'horloge entre côté cour ; au-dessus de la toile, son train d'engrenages relié par des tiges aux bras du père.
- B2 (19,6 s) : le père tiré loin de la toile par ses tiges, ombre immense et floue ; la fillette nette contre la
  toile, sans tige. Les lettres I et A suspendues à des fils, dépliées en « Interminable Attente ».
- B3 (39,5 s) : monde doré. Les tiges de l'horloge font marcher une file de devis vers la pile dorée ; les tiges du
  père pendent, coupées ; il pousse la balançoire, suspendue aux fils.

## C. « La forêt de dossiers »

**Concept.** Les dossiers que le père rapporte poussent dans la maison comme des troncs. Soir après soir, la forêt de
papier se referme entre le père et sa fille, et l'horloge y circule comme une bête de la forêt. La fillette la
traverse pour retrouver le dessin. Au renversement, l'horloge avale les troncs l'un après l'autre et les rend en
devis dorés : il reste un seul arbre, vivant, où pend la balançoire.

**Fil des objets-ponts.** La pile sous le bras devient tronc, puis feuille dorée. La chaîne pousse comme une liane.
Les feuilles de papier tombent comme des feuilles mortes, puis remontent en étincelles d'or. Signatures : le tronc de
dossiers qui monte (deux fois), le dernier tronc qui devient l'arbre de la balançoire (rime de la fin).

**Images de style.**
- C1 (4,2 s) : l'entrée de la maison, dont les murs se perdent déjà entre des troncs de dossiers. Le père entre,
  la pile sous le bras ; l'horloge se glisse entre deux troncs derrière lui, la chaîne enroulée comme une liane.
- C2 (19,6 s) : la fillette, toute petite, au pied de troncs de dossiers immenses ; les lettres I et A pendent aux
  branches, dépliées en « Interminable Attente » ; le père, loin entre les troncs, flou et pâle.
- C3 (39,5 s) : monde doré. Un seul arbre de lumière à la place de la forêt, la balançoire à sa branche ; le père
  pousse sa fille ; l'horloge dorée au pied de l'arbre rend les dernières feuilles en devis.

## Choix

Direction retenue par Antoine le 9 octobre 2026 : **A « La maison en coupe »**, avec l'arbre doré de C3 pour la fin
(le tronc fait de la dernière pile de devis, la balançoire à sa branche).

Ajustements faits en écrivant le storyboard (STORYBOARD.md, frame.md) :
- le dessin du petit dinosaure quitte l'entrée de A1 : il est épinglé au mur de la cuisine, dans le dos du père,
  recouvert de devis soir après soir, puis retrouvé par la fille ;
- la fille attend sur la deuxième marche de l'escalier de la cuisine (A2 la montrait à l'étage) : la caméra reste au
  rez-de-chaussée jusqu'au pivot et avance de gauche à droite ;
- l'escalier passe du salon à la cuisine, et les cloisons ont une baie où passent les personnages ;
- au monde doré, les devis finis volent par la fenêtre et s'empilent autour du tronc de l'arbre du jardin, qui devient
  l'arbre doré de C3 ; l'horloge suit la famille au jardin.
