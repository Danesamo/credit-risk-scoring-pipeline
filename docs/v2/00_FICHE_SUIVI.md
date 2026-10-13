# Fiche de suivi : V2 Scoring de crédit UEMOA

**Dernière mise à jour :** 05/10/2026
**Phase en cours :** P1 Étude de contexte
**Prochaine action :** valider les questions de recherche, puis lancer l'axe A dans le chat atelier

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
| P1-T1 | Questions de recherche (7 axes, 20 questions) | Claude + Daniela | ✅ 06/10 | Validées comme base évolutive |
| P1-T2 | Glossaire initial | Claude | ✅ 06/10 | Alimenté au fil de l'étude (D-010) |
| P1-T3 | Axes A, B, G puis point de décision 1 (périmètre provisoire) | Atelier BMAD + Daniela | ⬜ | D-011 |
| P1-T4 | Guide d'entretien terrain | Claude + Daniela | ⬜ | Après les axes A et B |
| P1-T5 | Axes E, F, C, D dans le périmètre provisoire | Atelier BMAD + Daniela | ⬜ | |
| P1-T6 | Synthèse et point de décision 2 (périmètre définitif) | Claude + Daniela | ⬜ | Entrée de la P2 |
| P1-T7 | Post LinkedIn de lancement (appel aux ressources) | Daniela | ⬜ | Publication prévue le 06/10 |

## Tâches de la phase P0 (terminée)

| # | Tâche | Responsable | Statut | Remarque |
|---|---|---|---|---|
| P0-1 | Diagnostic complet de la V1 | Claude | ✅ 25/09 | Voir [02_DIAGNOSTIC_V1.md](02_DIAGNOSTIC_V1.md) |
| P0-2 | Cadrage initial (zone, segment, méthode, objectifs) | Daniela + Claude | ✅ 26/09 | Voir [01_CADRAGE_INITIAL.md](01_CADRAGE_INITIAL.md) |
| P0-3 | Création de la documentation V2 (`docs/v2/`) | Claude | ✅ 26/09 | README, fiche de suivi, cadrage, diagnostic, carnet |
| P0-4 | Annuler la modification de `airflow/db/airflow.db` | Daniela | ✅ 26/09 | |
| P0-5 | Figer la V1 : tag `v1.0` + push du tag | Daniela | ✅ 26/09 | Tag visible sur GitHub |
| P0-6 | Créer la branche `v2` | Daniela | ✅ 26/09 | |
| P0-7 | Vérifier les prérequis BMAD dans le terminal Ubuntu WSL (node, npm, git, uv, Python 3.11+) | Daniela | ✅ 02/10 | Node 22, Python 3.12, uv 0.12 |
| P0-8 | Installer BMAD depuis `Credit_Risk_Scoring_Project` (`npx skills add ...`) | Daniela | ✅ 02/10 | 12 skills (version 6.13.0-next), portée projet, `.agents/skills/` + liens dans `.claude/skills/` |
| P0-9 | Nouvelle session Claude Code (VS Code reste ouvert sur `~/projects`), lancer `bmad setup` puis `bmad status` | Daniela | ✅ 02/10 | |
| P0-10 | Configurer l'emplacement des sorties BMAD dans `docs/v2/` | Claude | ✅ 02/10 | Décision D-008 |
| P0-11 | Ranger la documentation V1 dans `docs/v1/` (`git mv`) et mettre à jour les liens | Daniela (commandes) + Claude (liens) | ✅ 26/09 | Sur la branche `v2` uniquement (décision D-007) |
| P0-12 | Premier commit de la documentation V2 sur la branche `v2` | Daniela | ✅ 26/09 | Commit `f0c162c`, branche `v2` poussée sur GitHub |
| P0-13 | Commit du dispositif BMAD et des mises à jour de la documentation | Daniela | ✅ 03/10 | Commit `e1e38f5` |
| P0-14 | Créer l'initiative BMAD `uemoa-pilote-benin` (dans le chat atelier) | Daniela | ✅ 05/10 | `docs/v2/initiative-uemoa-pilote-benin/` |

---

## 3. Questions ouvertes

| # | Question | Posée le | Sera tranchée en | Statut |
|---|---|---|---|---|
| Q-01 | Quel maillon de l'écosystème crédit cibler en priorité (banque seule, banque + partenariat mobile money, microfinance/SFD) ? | 25/09/2026 | Point de décision 1 | Ouvert. Axe A : SFD n°1 (besoin), banques n°2. Orientation de travail de Daniela (08/10) : les banques, capables de payer l'outil ; piste d'un cœur commun adaptable aux grandes IMF |
| Q-08 | Qui paiera l'outil, et quel modèle économique ? (les SFD ont le besoin, les banques ont les moyens) | 08/10/2026 | P2 | Ouvert |
| Q-09 | Les banques de l'UEMOA disposent-elles déjà d'outils de scoring ou d'aide à l'octroi (internes, éditeurs, scores du bureau de crédit) ? | 08/10/2026 | Recherche dédiée après l'axe B (D-013), puis entretiens | Ouvert, conditionne la valeur ajoutée |
| Q-10 | Comment accéder aux données des institutions (outil déployé chez elles sur leurs données, pilote sous accord de confidentialité, démonstrateur sur données synthétiques calibrées) ? | 08/10/2026 | Axe E et P3 | Volet légal traité (axe B) : déploiement chez la banque favorisé, données hébergées dans l'UMOA, contrat soumis à la Commission bancaire, déclaration APDP |
| Q-02 | Quelle source de données réelle ou réaliste utiliser ? | 25/09/2026 | P3 | Ouvert |
| Q-03 | Quelle définition du défaut retenir (90 jours de retard ? autre selon produit) ? | 26/09/2026 | Point de décision 1 | Piste solide (axe B) : particulier en banque = échéance impayée depuis plus de 90 jours, appréciée par crédit (Instr. 026-11-2016, art. 8 et 11). Restent : traitement des créances restructurées, vérification de R-031 |
| Q-04 | Qui est l'utilisateur de l'outil (analyste crédit, direction des risques, agent commercial) ? | 26/09/2026 | P2 | Ouvert |
| Q-05 | Quels outils techniques ajouter (dbt, qualité des données, CI/CD, suivi d'expériences) ? | 26/09/2026 | P4 | Ouvert |
| Q-07 | Comment associer la communauté et de futurs utilisateurs (post ou sondage LinkedIn, questionnaire, entretiens avec des professionnels du crédit) sans dévoiler tout le projet ? | 02/10/2026 | Fin de P1 | En cours : post de lancement prêt (appel aux données, solutions existantes, entretiens) |
| Q-06 | Quel cadre réglementaire s'applique exactement (BCEAO, normes comptables de provisionnement, protection des données au Bénin) ? | 26/09/2026 | P1 | Largement traité (axe B, sources non vérifiées). Restent : loi microfinance 2025-14 et Code du numérique promulgué non lus (QO-B1, QO-B2), validation juridique |

---

## 4. Contacts et pistes (données, partenaires, experts)

| Date | Piste | Type | Statut |
|---|---|---|---|
| | *(aucune pour l'instant)* | | |

---

## 5. Journal des sessions

### 25/09/2026 : Lancement de la V2
- Objectif posé : V2 adaptée aux réalités africaines, fondée sur une étude de contexte à jour.
- Diagnostic complet de la V1 ([02_DIAGNOSTIC_V1.md](02_DIAGNOSTIC_V1.md)).

### 26/09/2026 : Cadrage et organisation
- Cadrage : banques, UEMOA, Bénin pilote, méthode BMAD ([01_CADRAGE_INITIAL.md](01_CADRAGE_INITIAL.md)).
- Organisation du dépôt et des docs : décisions D-004 et D-007.
- Environnement : Ubuntu sous WSL ; BMAD installé au niveau du seul projet.
