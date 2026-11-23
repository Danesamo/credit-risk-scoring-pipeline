# Fiche de suivi : V2 Scoring de crédit UEMOA

**Dernière mise à jour :** 22/11/2026
**Phase en cours :** P1 Étude de contexte, environ aux deux tiers
**Prochaine action :** lancer la recherche « données et accès » (axes C et E fusionnés), qui porte le verrou Q-11 et la question d'identité Q-12
**Pause :** du 30/10/2026 au 16/11/2026, pour d'autres travaux

---

## 1. Vue d'ensemble des phases

| Phase | Intitulé | Livrable attendu | Statut | Début | Fin |
|---|---|---|---|---|---|
| P0 | Mise en place | Tag `v1.0`, branche `v2`, BMAD opérationnel, documentation initiale | ✅ Terminé | 25/09/2026 | 05/10/2026 |
| P1 | Étude de contexte UEMOA / Bénin | Rapports sourcés et datés dans `initiative-uemoa-pilote-benin/` | 🔄 En cours | 05/10/2026 | |
| P2 | Cadrage produit | Product brief puis PRD (BMAD) | ⬜ À faire | | |
| P3 | Stratégie de données | Plan de données justifié (sources, partenaires, synthétique) | ⬜ À faire | | |
| P4 | Architecture V2 | Document d'architecture : garder / corriger / remplacer, outils à jour | ⬜ À faire | | |
| P5 | Modélisation | Scorecard de référence + challenger, calibration, équité, test out-of-time | ⬜ À faire | | |
| P6 | Industrialisation (MLOps) | Pipeline, suivi de dérive, réentraînement, API | ⬜ À faire | | |
| P7 | Extension | Autres pays UEMOA, puis étude comparative CEMAC | ⬜ À faire | | |

Légende : ⬜ À faire · 🔄 En cours · ✅ Terminé · ⏸ En pause · ❌ Abandonné

---

## 2. Tâches de la phase en cours (P1)

Le détail de l'avancement par axe est dans [00_QUESTIONS_DE_RECHERCHE.md](initiative-uemoa-pilote-benin/00_QUESTIONS_DE_RECHERCHE.md).

| # | Tâche | Responsable | Statut | Remarque |
|---|---|---|---|---|
| P1-T1 | Questions de recherche (7 axes, 20 questions) | Daniela | ✅ 06/10 | Validées comme base évolutive |
| P1-T2 | Glossaire initial | Daniela | ✅ 06/10 | Alimenté au fil de l'étude (D-010) |
| P1-T3 | Axes A, B, G puis point de décision 1 (périmètre provisoire) | Atelier BMAD + Daniela | ✅ 22/11 | Décisions D-016 à D-020 |
| P1-T4 | Guide d'entretien terrain | Daniela | ✅ 29/10 | [GUIDE_ENTRETIEN.md](initiative-uemoa-pilote-benin/GUIDE_ENTRETIEN.md) |
| P1-T5a | Recherche « données et accès » (C+E fusionnés) | Atelier BMAD + Daniela | ✅ 22/11 | [research-donnees-et-acces](initiative-uemoa-pilote-benin/research-donnees-et-acces/research-donnees-et-acces.md). Voie 1 praticable, voie 2 non démontrée, voie 3 impraticable |
| P1-T5a-bis | **Tests terrain T1 à T11** (export mobile money, identité, rapport bureau de crédit) | Daniela | ✅ 23/11 | T1, T2 et T3 faits : la voie 2 est ouverte. Reste T4 (Moov, Celtiis), la profondeur maximale et T8 (rapport du bureau de crédit) |
| P1-T5b | Revue de littérature scientifique (axe F réduit) | Atelier BMAD, puis Daniela | ⬜ | |
| P1-T5c | Axe D, emprunteurs et pratiques réelles | Daniela, terrain | ⬜ | Guide d'entretien prêt. Avance en parallèle, ne bloque pas la P1 |
| P1-T6 | Synthèse et point de décision 2 (périmètre définitif) | Daniela | ⬜ | Entrée de la P2 |
| P1-T7 | Post LinkedIn de lancement (appel aux ressources) | Daniela | ⬜ | Publication prévue le 06/10 |

## Tâches de la phase P0 (terminée)

| # | Tâche | Responsable | Statut | Remarque |
|---|---|---|---|---|
| P0-1 | Diagnostic complet de la V1 | Daniela | ✅ 25/09 | Voir [02_DIAGNOSTIC_V1.md](02_DIAGNOSTIC_V1.md) |
| P0-2 | Cadrage initial (zone, segment, méthode, objectifs) | Daniela | ✅ 26/09 | Voir [01_CADRAGE_INITIAL.md](01_CADRAGE_INITIAL.md) |
| P0-3 | Création de la documentation V2 (`docs/v2/`) | Daniela | ✅ 26/09 | README, fiche de suivi, cadrage, diagnostic, carnet |
| P0-4 | Annuler la modification de `airflow/db/airflow.db` | Daniela | ✅ 26/09 | |
| P0-5 | Figer la V1 : tag `v1.0` + push du tag | Daniela | ✅ 26/09 | Tag visible sur GitHub |
| P0-6 | Créer la branche `v2` | Daniela | ✅ 26/09 | |
| P0-7 | Vérifier les prérequis BMAD dans le terminal Ubuntu WSL (node, npm, git, uv, Python 3.11+) | Daniela | ✅ 02/10 | Node 22, Python 3.12, uv 0.12 |
| P0-8 | Installer BMAD depuis `Credit_Risk_Scoring_Project` (`npx skills add ...`) | Daniela | ✅ 02/10 | 12 skills (version 6.13.0-next), portée projet, `.agents/skills/` + liens dans `.claude/skills/` |
| P0-9 | Nouvelle session de l'outil (VS Code reste ouvert sur `~/projects`), lancer `bmad setup` puis `bmad status` | Daniela | ✅ 02/10 | |
| P0-10 | Configurer l'emplacement des sorties BMAD dans `docs/v2/` | Daniela | ✅ 02/10 | Décision D-008 |
| P0-11 | Ranger la documentation V1 dans `docs/v1/` (`git mv`) et mettre à jour les liens | Daniela | ✅ 26/09 | Sur la branche `v2` uniquement (décision D-007) |
| P0-12 | Premier commit de la documentation V2 sur la branche `v2` | Daniela | ✅ 26/09 | Commit `f0c162c`, branche `v2` poussée sur GitHub |
| P0-13 | Commit du dispositif BMAD et des mises à jour de la documentation | Daniela | ✅ 03/10 | Commit `e1e38f5` |
| P0-14 | Créer l'initiative BMAD `uemoa-pilote-benin` (dans le chat atelier) | Daniela | ✅ 05/10 | `docs/v2/initiative-uemoa-pilote-benin/` |

---

## 3. Questions ouvertes

| # | Question | Posée le | Sera tranchée en | Statut |
|---|---|---|---|---|
| Q-01 | Quel maillon de l'écosystème crédit cibler en priorité (banque seule, banque + partenariat mobile money, microfinance/SFD) ? | 25/09/2026 | Point de décision 1 | **Tranchée le 22/11/2026 (D-016)** : particuliers et TPE des banques classiques, à titre provisoire, avec repli validé vers les IMF de grande taille |
| Q-08 | Qui paiera l'outil, et quel modèle économique ? (les SFD ont le besoin, les banques ont les moyens) | 08/10/2026 | Point de décision 1 | **Devenue critique.** Vérification du 29/10 [R-006] : au Bénin, le segment visé (particuliers et entreprises individuelles) est passé de 20,1 % à 9,0 % des crédits mis en place entre 2020 et 2025, et recule de 30,1 % sur la seule année 2025, pendant que le crédit total double. Voir [G_PAYS_PILOTE.md](initiative-uemoa-pilote-benin/G_PAYS_PILOTE.md) |
| Q-09 | Les banques de l'UEMOA disposent-elles déjà d'outils de scoring ou d'aide à l'octroi (internes, éditeurs, scores du bureau de crédit) ? | 08/10/2026 | Recherche dédiée après l'axe B (D-013), puis entretiens | **Refermée le 22/11/2026** par la question 21, et exploitée dans D-016 |
| Q-12 | **Existe-t-il au Bénin une couche d'identité qui relie une personne à ses comptes (bancaire, mobile money) à travers plusieurs institutions ?** Au Nigeria, le numéro de téléphone est relié à un compte, ce qui suffit à prêter. Quel est l'équivalent béninois, et quelle est sa couverture réelle ? | 22/11/2026 | Recherche « données et accès » (C+E) | **Répondue le 22/11 : la couche existe, mais pas pour un tiers privé.** Depuis le décret d'avril 2020, l'opérateur rattache chaque numéro au NPI, vérifié par l'ANIP. Mais ce lien n'est communicable qu'à l'ARCEP, aux services de sécurité et à la justice. L'ANIP annonce une ouverture aux banques avec un modèle payant en 2027. Rattachement possible aujourd'hui par le nom et le numéro, si le relevé les porte (test T2) |
| Q-13 | **90 jours d'historique suffisent-ils pour prédire un défaut ?** L'export mobile money est plafonné à 3 mois. Que dit la littérature sur la profondeur minimale utile en scoring sur données de transaction ? | 23/11/2026 | Revue de littérature (axe F) | Ouvert. Conditionne directement la valeur de la voie 2a |
| Q-11 | **Verrou central du projet** : comment un outil destiné à une banque peut-il exploiter des flux mobile money dont l'opérateur est propriétaire, sans partenariat opérateur ? Résoudre ce point fonde l'originalité du travail. | 29/10/2026 | P2 et P3 | **Largement levé le 23/11/2026 par les tests terrain.** L'application MTN MoMo exporte un relevé PDF lisible par une machine, portant l'identité du titulaire, le sens des flux et le solde après chaque opération. Voie 2a techniquement praticable, mais **limitée à 90 jours d'historique** (vérifié). Restent : l'absence de signature (falsification) et les données de tiers figurant au relevé |
| Q-10 | Comment accéder aux données des institutions (outil déployé chez elles sur leurs données, pilote sous accord de confidentialité, démonstrateur sur données synthétiques calibrées) ? | 08/10/2026 | Axe E et P3 | Volet légal traité (axe B) : déploiement chez la banque favorisé, données hébergées dans l'UMOA, contrat soumis à la Commission bancaire, déclaration APDP |
| Q-02 | Quelle source de données réelle ou réaliste utiliser ? | 25/09/2026 | P3 | **Répondue le 22/11 : aucun jeu de données public ne couvre un pays de l'UEMOA avec une variable de défaut et une licence commerciale.** Les enquêtes ménages et le Findex sont réservés à la recherche ; les jeux africains avec défaut sont hors UEMOA. Restent le partenariat (éventuellement via le bac à sable LIF-BCEAO, qui couvre le scoring) et le démonstrateur sur données synthétiques calibrées |
| Q-03 | Quelle définition du défaut retenir (90 jours de retard ? autre selon produit) ? | 26/09/2026 | Point de décision 1 | **Tranchée le 22/11/2026 (D-018)** : plus de 90 jours d'impayé, par crédit, plus une alerte à 30 jours. Reste ouvert : le traitement des créances restructurées |
| Q-04 | Qui est l'utilisateur de l'outil (analyste crédit, direction des risques, agent commercial) ? | 26/09/2026 | P2 | **Tranchée le 22/11/2026 (D-019)** : l'analyste crédit garde la décision, l'outil propose et explique |
| Q-05 | Quels outils techniques ajouter (dbt, qualité des données, CI/CD, suivi d'expériences) ? | 26/09/2026 | P4 | Ouvert |
| Q-07 | Comment associer la communauté et de futurs utilisateurs (post ou sondage LinkedIn, questionnaire, entretiens avec des professionnels du crédit) sans dévoiler tout le projet ? | 02/10/2026 | Fin de P1 | En cours : post de lancement prêt (appel aux données, solutions existantes, entretiens) |
| Q-06 | Quel cadre réglementaire s'applique exactement (BCEAO, normes comptables de provisionnement, protection des données au Bénin) ? | 26/09/2026 | P1 | Largement traité (axe B, sources non vérifiées). Restent : loi microfinance 2025-14 et Code du numérique promulgué non lus (QO-B1, QO-B2), validation juridique |

---

## 4. Contacts et pistes (données, partenaires, experts)

| Date | Piste | Type | Statut |
|---|---|---|---|
| 18 au 20/11/2026 | **Village de l'Innovation, Cotonou.** Présence les 18 et 20/11. Aucun banquier rencontré : la question sur le recul du crédit aux particuliers reste posée. Échange utile avec **Bujeti**, fintech présente au Nigeria et au Kenya, qui arrive au Bénin. Leur réponse sur les commerçantes non bancarisées : au Nigeria le numéro de téléphone est rattaché à un compte bancaire ou mobile, ce qui suffit pour accorder un crédit. Pas encore opérationnels au Bénin. Conseil d'un responsable du ministère : venir en soirée, les professionnels passent après le travail | Terrain | Exploité : voir Q-12. **Bujeti non prioritaire** (décision du 22/11/2026) : acteur qui s'installe à peine, pas encore la connaissance du marché local. Priorité aux professionnels des institutions financières déjà établies au Bénin |
| 28/10/2026 | Représentant d'une institution de développement (BAD), rencontré de façon informelle. A expliqué le scoring sur flux mobile money ; co-auteur d'un article avec une entreprise kenyane. **Échange privé : ne jamais citer publiquement, ni la personne, ni l'institution.** | Expert métier | Relance à faire : demander le lien de l'article (prétexte naturel pour rouvrir le contact, puis proposer un entretien) |

---

## 5. Journal des sessions

### 25/09/2026 : Lancement de la V2
- Objectif posé : V2 adaptée aux réalités africaines, fondée sur une étude de contexte à jour.
- Diagnostic complet de la V1 ([02_DIAGNOSTIC_V1.md](02_DIAGNOSTIC_V1.md)).

### 26/09/2026 : Cadrage et organisation
- Cadrage : banques, UEMOA, Bénin pilote, méthode BMAD ([01_CADRAGE_INITIAL.md](01_CADRAGE_INITIAL.md)).
- Organisation du dépôt et des docs : décisions D-004 et D-007.
- Environnement : Ubuntu sous WSL ; BMAD installé au niveau du seul projet.
