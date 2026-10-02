# Cadrage initial de la V2

**Rédigé le :** 26/09/2026, à partir des échanges des 25 et 26/09/2026
**Statut :** Cadrage de départ. Il sera affiné par l'étude de contexte (P1) et le cadrage produit (P2).

---

## 1. Vision et motivation

- **Valeur portée par Daniela :** apporter des solutions concrètes à l'écosystème africain, qui répondent aux réalités et aux besoins africains, et non à des besoins extérieurs.
- **Constat de départ :** la V1 repose sur des données Kaggle (Home Credit, 2018, clients d'Asie et d'Europe de l'Est). Elle démontre une architecture, mais ne répond pas à une réalité africaine.
- **Ambition :** un projet **réel**, pas fictif, qui puisse servir à des entreprises du secteur bancaire et financier.
- **Principe de travail :** comprendre avant de construire. On ne réinvente pas la roue : l'architecture V1 est la base, et elle sera améliorée là où c'est justifié, avec des outils à jour (septembre 2026).
- **Analyser l'existant avant de construire :** identifier ce qui a déjà été fait (solutions, études, méthodes évaluées), les comparer, et définir précisément la valeur ajoutée du projet (02/10/2026). Axe obligatoire de l'étude P1.
- **Exigence :** avancer pas à pas, comprendre chaque choix d'architecture et ses alternatives, être challengée, tout documenter.

## 2. Réponses de cadrage (26/09/2026)

### 2.1 Segment visé
- **Priorité : les banques.** L'intérêt de départ de la V1 était de comprendre comment une banque sépare les emprunteurs solvables et insolvables, et comment on étiquette le défaut.
- **Nuance apportée par Daniela :** en Afrique, l'accès aux banques reste limité. Ce sont surtout les microfinances et, de plus en plus, le mobile money qui sont utilisés.
- **Conséquence :** l'étude doit couvrir tout l'écosystème du crédit (banques, microfinance / SFD, mobile money, fintechs, et leurs partenariats) avant de choisir où l'outil apporte le plus de valeur. Voir question Q-01 dans la fiche de suivi.

### 2.2 Zone géographique
- **Zone principale : UEMOA.** Daniela vit au Bénin (Cotonou).
- **Pays pilote : Bénin.**
- **Ensuite :** extension aux autres pays de l'UEMOA.
- **À terme :** étude comparative UEMOA / CEMAC (Daniela a aussi un pied dans la CEMAC).

### 2.3 Données
- Aucune source identifiée à ce jour. Les recherches de la phase P1 et la stratégie de données (P3) doivent trouver le point de départ le plus solide.

### 2.4 Méthode
- **BMAD Method** confirmée (l'oral « MCP Bimat » désignait BMAD).
- Daniela installe et configure BMAD elle-même, à partir d'un plan fourni par Claude ; les problèmes sont corrigés ensemble.

### 2.5 Ce que l'outil doit aider à décider (réponse de Daniela)
- Savoir **à qui accorder un prêt ou non**, en restant dans le cadre des défauts bancaires.
- Savoir **quel type de prêt accorder à quel profil**.
- Travailler sur la **prévision des défauts**, en tenant compte des sous-domaines bancaires.
- Daniela a indiqué avoir besoin d'être orientée sur ce point : voir section 3.

## 3. Clarification : les cinq métiers derrière « prévoir les défauts »

| # | Métier bancaire | Question | Ce qu'on prédit |
|---|---|---|---|
| 1 | Scoring d'octroi | Accorder le prêt à ce demandeur ? | Probabilité de défaut (PD) à 12 mois |
| 2 | Structuration de l'offre | Quel montant, quelle durée, quel taux pour ce profil ? | Capacité de remboursement, prix ajusté au risque |
| 3 | Scoring comportemental | Ce client en portefeuille se dégrade-t-il ? | Évolution mensuelle de la PD |
| 4 | Provisionnement | Combien la banque va-t-elle perdre sur ses prêts ? | Pertes attendues = PD × LGD × EAD |
| 5 | Stress test | Et si la conjoncture se dégrade ? | Pertes selon des scénarios |

La prévision du chiffre d'affaires d'une entreprise relève du crédit aux PME, un autre segment, écarté pour l'instant.

**Proposition (à confirmer en P2) :** cœur V2 = métier 1 + métier 2 ; métier 4 en extension. Voir décision D-005 dans le [carnet](CARNET.md).

## 4. Objectifs personnels de Daniela à travers ce projet

1. **Finance :** mettre en pratique le MScFE (WorldQuant University, 2e année en cours) et consolider sa compréhension du métier.
2. **Data Engineering :** renforcer et mettre à jour sa pratique (profil actuel : Data Engineer).
3. **IA et MLOps :** avoir la légitimité de se prononcer sur le développement et l'industrialisation de modèles.
4. **Rester focalisée :** profil « Data Engineer & AI Researcher ». Pas de dispersion, des outils à jour et justifiés.

## 5. Liens avec la formation et la carrière

### 5.1 MScFE WorldQuant University
Guide personnel de Daniela : `~/projects/Formation_Bases_Investissement/GUIDE_BASES_INVESTISSEMENT_BOURSE.md` (documenté cours après cours ; chaque cours dure environ deux mois).

| Cours | Apport au projet |
|---|---|
| Machine Learning in Finance (en cours depuis le 08/09/2026) | Scoring : modèles supervisés, régularisation, validation croisée, calibration |
| Financial Econometrics | Régression logistique, séries temporelles, liens macroéconomiques (provisions prospectives) |
| Stochastic Modeling | Chaînes de Markov, matrices de migration entre classes de risque |
| Derivative Pricing | Modèle de Merton : PD d'entreprise (guide, partie 21.3) |
| Risk Management (à venir) | Pertes attendues du portefeuille, stress tests |

### 5.2 Plan de carrière
Document : `~/projects/Career_Portfolio_2026/PLAN_CARRIERE_PORTFOLIO.md`.
- Cible n°1 : **Credit Risk Analyst / Modeler**. La V2 en est la preuve concrète.
- Manques techniques identifiés dans ce plan (dbt, qualité des données, CI/CD) : candidats à examiner en P4, retenus seulement s'ils répondent à un besoin réel du projet.

## 6. Contraintes connues

| Contrainte | Détail |
|---|---|
| Rôle | Daniela exécute les commandes ; Claude propose, explique, documente |
| Validation | Aucune action sans l'accord de Daniela |
| Date de référence | Septembre 2026 : réalités, besoins et technologies doivent être à jour |
| Données | Pas de dataset africain public équivalent à Home Credit connu à ce jour (à confirmer en P1) |
