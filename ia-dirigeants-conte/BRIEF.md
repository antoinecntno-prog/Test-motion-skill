# Brief du film : l'IA pour les dirigeants qui écrivent, conte d'ombres

Rempli le 08/10/2026 d'après la demande d'Antoine. Les hypothèses sont marquées « Hypothèse ».

## 1. Sujet (obligatoire)

- La cible, en une ligne : les dirigeants de PME et les coachs dont une bonne part de la semaine passe par l'écrit.
- La douleur, concrète : les devis, les chiffrages, les comptes rendus, les fiches techniques, les réponses aux appels
  d'offres et les relances clients mangent la semaine ; le dirigeant est mené par ses dossiers.
- La promesse (source unique : page d'accueil d'antoinecontino.fr, lue par Antoine le 08/10/2026) : « L'IA
  simplifiée, taillée sur mesure. » « On part de vos problèmes. » Formation dans les locaux du client, sur ses dossiers
  anonymisés ; chaque tâche récurrente devient un outil réutilisable ; le participant fabrique lui-même un outil de
  bout en bout. « Aucun prérequis technique : si vous savez écrire un mail, vous savez suivre la journée. »
- Preuve publique : « 10 h gagnées chaque semaine par la dernière dirigeante formée » (dirigeante d'un cabinet de
  coaching). Dans le film seulement si Antoine la valide à l'étape 1, sans nom ni lieu, chiffre qui roule à l'écran.
- Le récit (concept d'Antoine, 08/10/2026) : un homme et une femme se sont aimés au lycée, la vie les sépare, chacun
  garde l'autre au fond du cœur ; elle revient et le libère de ses chaînes de papier pour qu'il vive sa vie. Double
  sens implicite : lui est le dirigeant sous l'eau, elle est l'IA ; la clé arrive à la fin (deux lettres d'or, IA).
- La fin voulue : une scène décrite par la dernière phrase du conte, sans morale ; puis la signature et un seul bouton.

## 2. Design global (obligatoire)

- Ambiance : théâtre d'ombres rétroéclairé, silhouettes brun noir découpées devant une toile de papier sépia éclairée
  par derrière ; marionnettes à pivots et tiges visibles ; quatre plans de profondeur ; grain de papier par plan de
  parallaxe ; monde de la solution en silhouettes inversées lumineuses et poussière d'étincelles dorées.
- Références visuelles : la grammaire visuelle seule de la séquence animée de 2010 réalisée par Ben Hibon (Framestore),
  vidéo et deux images fournies par Antoine, gardées hors du dépôt. Aucun personnage, objet, symbole, lieu ou plan de
  ce film ; aucun nom de film ou de saga ; aucun son du clip.
- Couleurs : toile sépia claire, silhouettes brun noir, brumes en bruns intermédiaires, lumière crème ; un seul accent
  dans le conte, l'ocre doré de la lumière de la solution (#C98A2E, clair #E0A84A) ; bordeaux #7A1E2E réservé au mot
  clé des sous-titres et à la carte de fin (signature, bouton).
- Polices : fraunces (moment typographique du pivot, titre de conte éventuel), dm-sans (sous-titres, CTA), caveat
  (signature manuscrite).
- Personnages : marionnettes d'ombres à pivots ; lui, un dirigeant, et sa fille de sept ans ; elle, la lycéenne
  à la longue tresse, qui revient en jeune femme à taille humaine découpée en lumière dorée, au cœur d'une lumière
  faite de milliers de pages (aucune grande figure drapée, pour rester loin de la référence).

## 3. Marque et appel à l'action

- Nom exact de la marque : « Antoine Contino, formateur IA ».
- Logo : aucun ; signature manuscrite en Caveat, bordeaux.
- Appel à l'action : un seul bouton « Réserver un audit IA de 30 minutes » ; ligne sous le bouton :
  calendly.com/antoine-cntno/30min · antoinecontino.fr.
- Diffusion : vidéo native sur le profil LinkedIn personnel d'Antoine, 16:9, 1920 x 1080, 30 images/s, 45 à 50 s.
  Une large part du public regarde sans le son : le film se comprend par l'image et les sous-titres.

## 4. Matière et confidentialité

- Photos et captures : aucune ; tout est découpé en ombres.
- À anonymiser : la dirigeante formée reste sans nom ni lieu ; aucun dossier lisible avec un nom réel.
- Jamais dans la douleur : aucun logiciel ni client nommé.
- Faits à ne pas affirmer : les prix et les formules à l'année, la durée en heures de la journée, les mails et
  téléphones, les noms et lieux de clients ; toute affirmation absente de la page d'accueil d'antoinecontino.fr.
- Hypothèse : le site est bloqué par le proxy de ce conteneur ; les citations de l'offre viennent du relevé d'Antoine.

## 5. Son

- Voix : une narratrice française au ton posé (demande d'Antoine du 08/10/2026), Eleven v4 ; deux voix féminines de la
  bibliothèque ElevenLabs proposées à l'étape 2 ; accord d'Antoine avant tout crédit.
- Musique : partition de `musique-film.py`, boîte à musique sur des cordes graves, sourde avant le pivot, plus claire
  après.
- Bruitages : papier, flamme, vent, battements d'ailes, claquement de bois des tiges.
- Niveau : musique 6 à 8 dB sous la voix, effacée sous chaque phrase ; mixage autour de -16 LUFS.

## 6. Pilotage

- Validations : complètes (script, voix, directions, storyboard, pilote, son), réponse d'Antoine à chaque porte.
- Budget : crédits ElevenLabs sur accord explicite ; constructeurs à effort moyen.
- Technique : HyperFrames 0.8.82 du dépôt ; conteneur sans GPU ; piste du canvas 2D `render(t)` à mesurer au pilote,
  débit mesuré en `--workers 3` sur 5 s du style complet.
- Livraison : brouillon MP4, puis rendu final en `--workers 3` et copie web réencodée. La couverture et le post
  LinkedIn viendront sur demande.
