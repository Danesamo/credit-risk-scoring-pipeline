# Carnet de conception : registre des décisions V2

Chaque décision importante est consignée ici : ce qui est décidé, pourquoi, les alternatives écartées, et qui a validé.
Une décision peut être révisée : on ne l'efface pas, on ajoute une nouvelle entrée qui la remplace et on met à jour le statut de l'ancienne.

**Statuts :** Proposée · Validée · Remplacée par D-xxx · Abandonnée

---

## D-001 : Zone géographique
- **Date :** 26/09/2026
- **Décision :** UEMOA, avec le Bénin comme pays pilote. Puis extension aux autres pays de l'UEMOA, puis étude comparative UEMOA / CEMAC.
- **Pourquoi :** Daniela vit au Bénin (accès au terrain et au réseau). Commencer par un seul pays permet d'étudier le contexte en profondeur. La BCEAO étant commune à l'UEMOA, l'extension aux autres pays de la zone est naturelle. La CEMAC, avec une autre banque centrale et un autre régulateur, se prête à une comparaison.
- **Alternatives écartées :** étude directe de toute l'Afrique francophone (trop large pour une étude sérieuse).
- **Statut :** Validée par Daniela.

## D-009 : Trois niveaux de périmètre (précise D-001)
- **Date :** 02/10/2026
- **Décision :** l'étude puise à trois niveaux. Cadre UEMOA (règles communes : BCEAO, supervision bancaire, monnaie, microfinance, monnaie électronique, bureaux de crédit). Comparaison Côte d'Ivoire et Sénégal (marchés les plus grands et les mieux documentés). Terrain Bénin (entretiens, partenaires, validation). Le produit est conçu selon les règles UEMOA et paramétré, testé et validé d'abord pour le Bénin ; l'extension à un autre pays de l'UEMOA consiste à le recalibrer.
- **Pourquoi :** les règles communes rendent inutile une étude pays par pays ; la Côte d'Ivoire et le Sénégal fournissent les chiffres que le Bénin seul ne fournirait pas ; la présence de Daniela à Cotonou rend le terrain accessible. La P1 vérifiera le choix du pilote sur critères explicites (données, accès au terrain, taille du marché).
- **Statut :** Validée par Daniela.

## D-002 : Segment prioritaire
- **Date :** 26/09/2026
- **Décision :** priorité aux banques. L'étude de contexte couvre néanmoins tout l'écosystème du crédit (banques, microfinance / SFD, mobile money, fintechs, partenariats banque-opérateur).
- **Pourquoi :** c'est l'intérêt de départ de Daniela. Mais dans l'UEMOA, une partie du crédit, notamment le nano-crédit sur mobile money, passe par des partenariats où la banque porte le risque. Ignorer ces canaux ferait passer à côté de la réalité.
- **Alternatives écartées :** limiter l'étude aux banques traditionnelles.
- **Statut :** Validée par Daniela. Le choix final du maillon ciblé sera fait en P2 (question Q-01).

## D-003 : Méthode de travail BMAD
- **Date :** 26/09/2026
- **Décision :** utiliser la BMAD Method (installée le 02/10/2026, version 6.13.0-next), installée localement dans le projet via `npx skills add`, par Daniela.
- **Pourquoi :** BMAD structure le travail en étapes (clarifier, planifier, construire, ajuster) qui correspondent à l'approche « comprendre avant de construire ». Une installation locale au projet ne touche pas les autres projets (CivicWall, Fit App).
- **Alternatives écartées :** plugin global de l'outil de développement (s'appliquerait à tous les projets).
- **Statut :** Validée par Daniela (méthode). Mode d'installation défini le 26/09/2026.

## D-004 : Organisation du dépôt et de la documentation
- **Date :** 26/09/2026
- **Décision :** un seul dépôt. La V1 est figée par le tag Git `v1.0`, la V2 est développée sur la branche `v2` en faisant évoluer le code existant, et sa documentation est placée dans `docs/v2/`.
- **Pourquoi :**
  - Les versions sont le rôle de Git : le tag conserve la V1 exactement telle qu'elle est, et la démo Streamlit en ligne continue de fonctionner.
  - Un sous-répertoire `v2/` pour le code dupliquerait tout le code, obligerait à maintenir deux copies et casserait l'historique qui montre comment la V1 est devenue la V2.
  - L'historique Git de la branche `v2` raconte l'évolution, ce qui a de la valeur pour un recruteur ou un partenaire.
  - La documentation V1 reste en place comme référence ; la documentation V2 est isolée dans son propre dossier pour être facile à suivre.
- **Alternatives écartées :** nouveau dépôt (perte du lien avec la V1) ; sous-répertoire `v2/` pour le code (duplication).
- **Statut :** Proposée à la demande de Daniela (« à toi de me dire comment on organise »).

## D-007 : Documentation rangée par version (précise D-004)
- **Date :** 26/09/2026
- **Décision :** le code reste unique et évolue sur la branche `v2`, la V1 étant conservée par le tag `v1.0`. La documentation est rangée par version : `docs/v1/` (étude, rapport d'avancement, images de la V1) et `docs/v2/`. Ce rangement se fait uniquement sur la branche `v2`, avec `git mv` pour conserver l'historique, puis les liens du README et des docs V2 sont mis à jour.
- **Pourquoi :** Daniela a relevé que `docs/v2/` imbriqué à côté des fichiers V1 en vrac manquait de lisibilité. Le code n'a qu'une version vivante (Git gère les versions), alors que les deux documentations coexistent et doivent être symétriques.
- **Alternatives écartées :** dossiers `V1/` et `V2/` à la racine contenant chacun le code (duplication, perte de la lecture de l'évolution dans Git, risque de casser la démo Streamlit Cloud qui pointe vers `streamlit/app.py`).
- **Statut :** Validée par Daniela.

## D-008 : Emplacement des livrables BMAD
- **Date :** 02/10/2026
- **Décision :** les livrables BMAD sont écrits dans `docs/v2/` (surcharge `output_folder` dans `_bmad/custom/config.toml`, fichier commité). La configuration BMAD (`_bmad/`, `.agents/skills/`, `.claude/skills/`, `skills-lock.json`) est versionnée avec le projet ; seuls les réglages personnels (`*.user.toml`) restent hors Git.
- **Pourquoi :** toute la documentation V2 au même endroit ; installation BMAD reproductible à l'identique.
- **Alternatives écartées :** dossier par défaut `_bmad-output/` à la racine (documentation éclatée en deux endroits).
- **Statut :** Proposée le 02/10/2026, à valider par Daniela.

## D-010 : Double exigence recherche et industrie
- **Date :** 06/10/2026
- **Décision :** le projet suit à la fois les règles de la recherche (revue de l'existant, méthode explicite, sources citées, résultats reproductibles) et celles de l'industrie (conformité réglementaire, contraintes opérationnelles, mise en production). Un glossaire (`GLOSSAIRE.md`) fixe chaque terme clé avec ses définitions réglementaire, académique et pratique quand elles diffèrent.
- **Pourquoi :** un même mot peut changer de sens selon l'interlocuteur (le « défaut » d'un régulateur, d'un article scientifique et d'un analyste crédit). Sans définitions fixées, le modèle risque de prédire autre chose que ce dont la banque a besoin.
- **Statut :** Validée par Daniela.

## D-011 : Étude en entonnoir avec deux points de décision
- **Date :** 06/10/2026
- **Décision :** on ne répond pas aux 20 questions avant de circonscrire le projet. Les axes A, B et G donnent une vue d'ensemble, puis un premier point de décision fixe un périmètre provisoire (segment, type de crédit, définition du défaut, utilisateur). Les axes E, F, C et D sont ensuite menés uniquement dans ce périmètre. Un second point de décision fixe le périmètre définitif en entrée de la P2.
- **Pourquoi :** éviter la dispersion soulevée par Daniela. Chercher sur tout l'écosystème en profondeur coûterait des semaines sans garantir une décision.
- **Statut :** Validée par Daniela.

## D-012 : Bibliographie unique et vérification des sources
- **Date :** 06/10/2026
- **Décision :** toutes les sources sont référencées dans `REFERENCES.md` avec un identifiant `R-xxx`, leur type (primaire ou secondaire), leur date de consultation et, pour les pages web importantes, une copie archivée. Les rapports citent ces identifiants. Chaque source est vérifiée avant de fonder une décision.
- **Pourquoi :** exigence de rigueur de la recherche (D-010) ; traçabilité de chaque affirmation ; les pages web changent ou disparaissent.
- **Alternatives écartées :** liens dispersés dans chaque rapport (impossible à vérifier et à maintenir). Un fichier BibTeX pourra être généré plus tard si le projet donne lieu à un article.
- **Statut :** Validée par Daniela.

## D-013 : Question 21 (outils existants des banques) avancée avant le point de décision 1
- **Date :** 08/10/2026
- **Décision :** la question 21 (outils de scoring ou d'aide à l'octroi déjà utilisés par les banques de l'UEMOA) est traitée par une recherche dédiée juste après l'axe B, sans attendre l'axe F. Exception assumée à l'entonnoir de D-011. On ne s'appuie pas sur des hypothèses : on vérifie.
- **Pourquoi :** la réponse conditionne la valeur ajoutée du projet, donc l'orientation vers les banques (Q-01) ; elle prépare aussi les entretiens, où Daniela doit montrer qu'elle connaît déjà l'existant pour être crédible.
- **Statut :** Validée par Daniela.

## D-014 : Signal de scoring privilégié, le flux plutôt que le solde
- **Date :** 29/10/2026
- **Décision (orientation de conception, à confirmer en P3 et P5) :** le scoring s'appuiera sur les **flux de transactions mobile money sur plusieurs mois** plutôt que sur un historique de crédit ou un solde à un instant donné.
- **Pourquoi :** la population visée n'a pas d'historique de crédit (axe A : 8,7 % des adultes béninois ont emprunté à une institution financière). Le solde est une photo, le flux est un comportement. Exemple rapporté le 28/10/2026 par un expert : une commerçante encaisse de gros montants dans la journée et son compte est presque vide le lendemain, parce qu'elle a réapprovisionné son stock. Jugée sur son solde elle paraît insolvable, jugée sur ses flux réguliers elle est fiable. Des produits existants confirment l'approche : Prêt Xpress (Bénin, depuis 03/2024) et M-Shwari (Kenya, sur historique M-PESA).
- **Point ouvert soulevé le 29/10/2026 :** l'accès à ces flux. Deux voies possibles, à trancher en P2 et P3 : données transmises par l'opérateur à la banque (suppose un partenariat), ou **relevés fournis par le client lui-même avec son consentement exprès** (voie compatible avec le secret bancaire qui couvre les émetteurs de monnaie électronique, axe B). La seconde voie est la seule accessible sans partenariat opérateur.
- **Statut :** Proposée par Daniela, à confirmer après l'axe E (données disponibles).

## D-015 : Resserrement de la fin de la P1 (précise D-011)
- **Date :** 29/10/2026
- **Décision :** les axes restants passent de 5 recherches à 3. Les axes **C et E sont fusionnés** en une recherche « données et accès », consacrée aux trois voies du verrou Q-11. L'**axe F est réduit à la seule revue de littérature scientifique**, son volet concurrence étant traité par la question 21. L'**axe G** devient une section de la synthèse au lieu d'une recherche. L'**axe D** reste après le point de décision 1, car il dépend des entretiens.
- **Pourquoi :** Daniela a demandé que le resserrement ne coûte rien à la suite. Deux propositions initiales ont donc été retirées : la fusion de la question 21 avec tout l'axe F, qui aurait fait perdre la revue de littérature (exigence de D-010), et l'allègement de l'axe C, que l'orientation vers les flux mobile money (D-014) rend au contraire central. Aucune vérification n'est sacrifiée.
- **Statut :** Validée par Daniela, sous la condition qu'elle a posée : aucun impact négatif sur la suite.

---

# Point de décision 1 : le périmètre provisoire (22/11/2026)

Les cinq décisions ci-dessous ont été prises ensemble le 22/11/2026, sur la base du document [POINT_DECISION_1.md](initiative-uemoa-pilote-benin/POINT_DECISION_1.md). Elles sont **provisoires** au sens de D-011 : le point de décision 2, en fin de P1, les confirmera ou les corrigera.

## D-016 : Segment ciblé, avec repli explicite
- **Date :** 22/11/2026
- **Décision :** cibler les **particuliers et les très petites entreprises (entreprises individuelles) des banques classiques**, hors filiales d'opérateurs télécoms. **Repli validé en même temps que le choix principal** : si le terrain confirme que les banques se désengagent de ce segment pour une raison de rentabilité, l'acheteur bascule vers les **IMF de grande taille** (article 44), supervisées comme les banques, donc atteignables sans reconstruire l'outil.
- **Pourquoi :** aucune banque classique de la zone ne documente d'outil de scoring statistique pour ce segment (question 21) ; le concurrent identifié couvre les PME et non les particuliers [R-121 vérifiée] ; le besoin est massif (8,7 % des adultes empruntent à une institution contre 43 % à la famille) ; la concentration bancaire béninoise joue en faveur du projet, 4 banques portant 63 % du crédit.
- **Ce qui fragilise, assumé :** au Bénin, ce segment est passé de 20,1 % à 9,0 % des crédits accordés entre 2020 et 2025, et recule de 30 % sur la seule année 2025 [R-006 vérifiée], pendant que le crédit total doublait. L'appétit réel des banques reste la question la plus risquée du périmètre, et aucun rapport ne la tranchera : elle est en tête du guide d'entretien.
- **Alternatives écartées :** cibler directement les IMF (besoin plus visible mais moyens plus faibles, cadre juridique moins établi) ; cibler le crédit digital (déjà automatisé, donnée détenue par les opérateurs).
- **Statut :** Validée par Daniela, à titre provisoire, le repli étant validé explicitement.

## D-017 : Produit de crédit
- **Date :** 22/11/2026
- **Décision :** le crédit d'un **montant modeste à un particulier ou à une entreprise individuelle, accordé par une banque, remboursable par échéances**. Sont exclus le nano-crédit digital de 7 à 30 jours, le crédit aux PME constituées, le crédit immobilier et l'équipement lourd.
- **Pourquoi :** le nano-crédit est déjà automatisé par les opérateurs qui détiennent la donnée, et sa tarification pose une question de conformité au taux d'usure non tranchée ; les PME constituées sont le terrain du concurrent et supposent des états financiers que la cible n'a pas ; l'immobilier relève d'un autre horizon de risque et d'un autre métier.
- **Statut :** Validée par Daniela.

## D-018 : Définition du défaut (répond à Q-03)
- **Date :** 22/11/2026
- **Décision :** le défaut est **une échéance impayée depuis plus de 90 jours sur le crédit considéré**, apprécié **par crédit** et sans contamination des autres crédits du client. Un **indicateur d'alerte à 30 jours** est construit en complément, sans remplacer la cible réglementaire.
- **Pourquoi :** c'est la seule définition à la fois réglementaire et comparable au standard international. Source lue mot pour mot dans le texte officiel le 29/10/2026 : Instruction BCEAO n°026-11-2016, article 8 point 2 pour le seuil, article 11 pour l'absence de contagion sur la clientèle de détail [R-031 vérifiée]. Le délai de 180 jours ne vise que les États, les organismes publics et les PME, donc pas la cible.
- **Reste ouvert :** le traitement des **créances restructurées**, que la réglementation classe parmi les créances en souffrance. Les compter ou non comme un défaut change la variable cible. À trancher avec un professionnel.
- **Statut :** Validée par Daniela. C'est la décision la mieux étayée du point.

## D-019 : Utilisateur et rôle de l'outil (répond à Q-04)
- **Date :** 22/11/2026
- **Décision :** l'utilisateur est **l'analyste crédit de la banque, qui garde la décision**. L'outil propose et explique, il ne décide jamais. Formulation de Daniela : « il doit toujours y avoir un professionnel qui pilote l'outil ».
- **Pourquoi :** ce n'est pas une préférence mais une contrainte légale vérifiée [R-100] : une décision produisant des effets significatifs ne peut être prise sur le seul fondement d'un traitement automatisé (Code du numérique, art. 401), et le client peut exiger les informations utiles sur la logique de la décision sous 60 jours (art. 437).
- **Conséquences de conception, à porter dès l'architecture :** motifs lisibles par l'analyste et par le client ; possibilité pour l'analyste de passer outre, avec enregistrement de son motif ; la direction des risques est l'acheteur, l'analyste l'utilisateur quotidien, et les deux se convainquent par des arguments différents.
- **Statut :** Validée par Daniela.

## D-020 : Voies d'accès aux données
- **Date :** 22/11/2026
- **Décision :** instruire **trois voies par ordre de priorité, sans en abandonner aucune** : (1) les données propres de la banque et le rapport du bureau de crédit ; (2) les relevés apportés par le client avec son consentement exprès ; (3) les flux du paiement instantané de la BCEAO. La donnée des opérateurs télécoms est **écartée**.
- **Pourquoi :** la voie 1 est la plus sûre mais le bureau ne couvre que 25 % des adultes avec près de la moitié des contrats non à jour ; la voie 2 a une base légale vérifiée (art. 389, mesures précontractuelles à la demande de la personne) et constitue un créneau libre dans l'UEMOA selon la question 21, donc la différenciation possible ; la voie 3 ne dépend pas d'un opérateur unique et est déjà empruntée par le concurrent via des agrégateurs. La donnée des opérateurs leur appartient, des acteurs installés l'exploitent, et elle ne s'obtient pas sans partenariat.
- **À instruire avant le point de décision 2 :** la faisabilité technique de la voie 2 (comment un relevé devient une variable fiable), la question d'identité Q-12, et l'état réel de la voie 3.
- **Statut :** Validée par Daniela.

---

## D-005 : Cœur fonctionnel de la V2
- **Date :** 26/09/2026
- **Décision :** cœur = scoring d'octroi (PD à 12 mois) et structuration de l'offre (montant, durée, taux selon le profil). Provisionnement du portefeuille (pertes attendues) en extension.
- **Pourquoi :** cela répond directement à la demande de Daniela (« à qui accorder un prêt, et quel type de prêt à quel profil »), prolonge la V1, et couvre la chaîne d'un département risque de crédit.
- **Alternatives écartées :** prévision du chiffre d'affaires d'entreprises (autre segment : crédit aux PME).
- **Statut :** Proposée. À confirmer en P2 à la lumière de l'étude.

## D-006 : Répartition des rôles
- **Date :** 26/09/2026
- **Décision :** l'assistant analyse, propose, explique et documente. Daniela valide et exécute les commandes. Aucune action sans son accord.
- **Pourquoi :** projet réel, que Daniela doit maîtriser de bout en bout et pouvoir défendre.
- **Statut :** Validée par Daniela.
