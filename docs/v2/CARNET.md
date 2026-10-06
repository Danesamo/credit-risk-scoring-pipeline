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
- **Alternatives écartées :** plugin Claude Code global (s'appliquerait à tous les projets).
- **Statut :** Validée par Daniela (méthode). Mode d'installation proposé par Claude.

## D-004 : Organisation du dépôt et de la documentation
- **Date :** 26/09/2026
- **Décision :** un seul dépôt. La V1 est figée par le tag Git `v1.0`, la V2 est développée sur la branche `v2` en faisant évoluer le code existant, et sa documentation est placée dans `docs/v2/`.
- **Pourquoi :**
  - Les versions sont le rôle de Git : le tag conserve la V1 exactement telle qu'elle est, et la démo Streamlit en ligne continue de fonctionner.
  - Un sous-répertoire `v2/` pour le code dupliquerait tout le code, obligerait à maintenir deux copies et casserait l'historique qui montre comment la V1 est devenue la V2.
  - L'historique Git de la branche `v2` raconte l'évolution, ce qui a de la valeur pour un recruteur ou un partenaire.
  - La documentation V1 reste en place comme référence ; la documentation V2 est isolée dans son propre dossier pour être facile à suivre.
- **Alternatives écartées :** nouveau dépôt (perte du lien avec la V1) ; sous-répertoire `v2/` pour le code (duplication).
- **Statut :** Proposée par Claude, à la demande de Daniela (« à toi de me dire comment on organise »).

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
- **Statut :** Proposée par Claude, à valider par Daniela.

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
- **Décision :** toutes les sources sont référencées dans `REFERENCES.md` avec un identifiant `R-xxx`, leur type (primaire ou secondaire), leur date de consultation et, pour les pages web importantes, une copie archivée. Les rapports citent ces identifiants. Chaque source est vérifiée ensemble (Daniela et Claude) avant de fonder une décision.
- **Pourquoi :** exigence de rigueur de la recherche (D-010) ; traçabilité de chaque affirmation ; les pages web changent ou disparaissent.
- **Alternatives écartées :** liens dispersés dans chaque rapport (impossible à vérifier et à maintenir). Un fichier BibTeX pourra être généré plus tard si le projet donne lieu à un article.
- **Statut :** Validée par Daniela.

## D-005 : Cœur fonctionnel de la V2
- **Date :** 26/09/2026
- **Décision :** cœur = scoring d'octroi (PD à 12 mois) et structuration de l'offre (montant, durée, taux selon le profil). Provisionnement du portefeuille (pertes attendues) en extension.
- **Pourquoi :** cela répond directement à la demande de Daniela (« à qui accorder un prêt, et quel type de prêt à quel profil »), prolonge la V1, et couvre la chaîne d'un département risque de crédit.
- **Alternatives écartées :** prévision du chiffre d'affaires d'entreprises (autre segment : crédit aux PME).
- **Statut :** Proposée. À confirmer en P2 à la lumière de l'étude.

## D-006 : Répartition des rôles
- **Date :** 26/09/2026
- **Décision :** Claude analyse, propose, explique et documente. Daniela valide et exécute les commandes. Aucune action sans son accord.
- **Pourquoi :** projet réel, que Daniela doit maîtriser de bout en bout et pouvoir défendre.
- **Statut :** Validée par Daniela.
