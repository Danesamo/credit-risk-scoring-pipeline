# Étude de Projet : Credit Risk Scoring Pipeline

## 1. INTRODUCTION

### 1.1 Objet du document

Ce document constitue l'étude de cadrage du projet **Credit Risk Scoring Pipeline**. Il définit le contexte métier, la problématique, les objectifs, le périmètre et l'approche technique retenue.

Ce document s'inscrit dans une démarche professionnelle de gestion de projet, telle que pratiquée en entreprise dans les secteurs bancaire et financier.

### 1.2 Public cible

- Recruteurs et managers techniques (évaluation du portfolio)
- Équipes Risk Management / Credit Risk
- Data Engineers et Data Scientists
- Tout professionnel souhaitant comprendre un projet de scoring crédit end-to-end


## 2. CONTEXTE GÉNÉRAL

### 2.1 Le crédit dans l'économie

Le crédit est un pilier fondamental de l'économie moderne. Il permet :
- Aux **particuliers** : d'accéder à la propriété, financer des études, gérer des imprévus
- Aux **entreprises** : d'investir, de se développer, de gérer leur trésorerie
- À l'**économie** : de stimuler la croissance et la consommation

**Chiffres clés (monde) :**
- Marché mondial du crédit à la consommation : > 10 000 milliards USD
- Taux de défaut moyen : 2-5% selon les régions et types de crédit
- Pertes annuelles dues aux défauts : centaines de milliards USD

### 2.2 Les acteurs du crédit

| Acteur | Rôle | Exemples |
|--------|------|----------|
| **Banques traditionnelles** | Prêts immobiliers, consommation, entreprises | BNP, Société Générale, Ecobank |
| **Établissements de crédit** | Crédit à la consommation spécialisé | Cofidis, Cetelem, Home Credit |
| **FinTech / Néobanques** | Crédit digital, micro-crédit | Flutterwave, Wave, M-Kopa |
| **Microfinance** | Inclusion financière, petits montants | Grameen Bank, FINCA |

### 2.3 Le cas Home Credit

**Home Credit** est un établissement de crédit international présent dans 9 pays (Asie, Europe de l'Est). Leur mission : fournir des crédits aux personnes ayant peu ou pas d'historique bancaire.

**Problème spécifique :** Comment évaluer la solvabilité de clients qui n'ont pas d'historique de crédit traditionnel (pas de score FICO, pas de compte bancaire historique) ?


## 3. PROBLÉMATIQUE MÉTIER

### 3.1 Qu'est-ce que le risque de crédit ?

> **Définition :** Le risque de crédit est le risque qu'un emprunteur ne rembourse pas tout ou partie de son prêt selon les termes du contrat.

Ce risque se manifeste par :
- **Défaut de paiement (Default)** : L'emprunteur cesse de rembourser
- **Retard de paiement (Delinquency)** : Paiements en retard (30, 60, 90 jours)
- **Perte en cas de défaut (LGD)** : Montant non récupéré après défaut

### 3.2 Pourquoi c'est un problème critique ?

#### Pour l'institution financière :

| Impact | Description |
|--------|-------------|
| **Pertes financières directes** | Capital non remboursé = perte sèche |
| **Coût du recouvrement** | Procédures, contentieux, ressources humaines |
| **Exigences en capital** | Plus de défauts = plus de fonds propres requis (réglementation) |
| **Réputation** | Trop de défauts = mauvaise sélection = perte de confiance investisseurs |

#### Pour l'économie :

- Crise des subprimes (2008) : mauvaise évaluation du risque crédit → crise financière mondiale
- Effet domino sur tout le système bancaire

### 3.3 L'approche traditionnelle et ses limites

#### Méthode traditionnelle (jugement expert) :

1. Analyse du dossier par un analyste crédit
2. Vérification des revenus, emploi, patrimoine
3. Consultation du score bureau de crédit (FICO, etc.)
4. Décision subjective basée sur l'expérience

#### Limites :

| Limite | Problème |
|--------|----------|
| **Subjectivité** | Deux analystes peuvent décider différemment |
| **Lenteur** | Plusieurs jours pour une décision |
| **Coût** | Analystes qualifiés = coût élevé |
| **Scalabilité** | Impossible de traiter des millions de demandes |
| **Exclusion** | Pas d'historique crédit = refus automatique |

### 3.4 La solution : Credit Scoring automatisé

> **Credit Scoring :** Modèle statistique/ML qui attribue un score de risque à chaque demandeur, prédisant la probabilité de défaut.

#### Avantages :

| Avantage | Bénéfice |
|----------|----------|
| **Objectivité** | Mêmes critères pour tous |
| **Rapidité** | Décision en secondes |
| **Scalabilité** | Millions de demandes traitées |
| **Inclusion** | Données alternatives → plus de personnes éligibles |
| **Cohérence** | Décisions reproductibles et auditables |


## 4. CADRE RÉGLEMENTAIRE

### 4.1 Accords de Bâle (Bâle II / Bâle III)

Les accords de Bâle sont des normes internationales qui régissent le secteur bancaire :

| Accord | Année | Pertinence pour le scoring |
|--------|-------|---------------------------|
| **Bâle II** | 2004 | Introduction de l'approche IRB (Internal Ratings-Based) - les banques peuvent utiliser leurs propres modèles de scoring |
| **Bâle III** | 2010 | Renforcement des exigences en capital, stress tests |

#### Paramètres clés à estimer :

| Paramètre | Définition | Notre projet |
|-----------|------------|--------------|
| **PD (Probability of Default)** | Probabilité de défaut à 1 an | ✅ C'est notre cible |
| **LGD (Loss Given Default)** | % de perte si défaut | Non couvert |
| **EAD (Exposure at Default)** | Montant exposé au moment du défaut | Non couvert |

### 4.2 Exigences de transparence et d'explicabilité

Depuis le RGPD (Europe) et les réglementations similaires :
- Le client a le droit de comprendre pourquoi sa demande est refusée
- Les modèles "boîte noire" sont problématiques
- **Solution :** Utiliser SHAP pour l'explicabilité (ce que nous ferons)


## 5. OBJECTIFS DU PROJET

### 5.1 Objectifs métier

| # | Objectif | Mesure de succès |
|---|----------|------------------|
| 1 | Prédire la probabilité de défaut de paiement | AUC-ROC > 0.75 |
| 2 | Fournir des explications pour chaque décision | SHAP values disponibles |
| 3 | Permettre des décisions en temps réel | Latence API < 200ms |
| 4 | Identifier les facteurs de risque principaux | Top 10 features documentées |

### 5.2 Objectifs techniques (Data Engineering)

| # | Objectif | Mesure de succès |
|---|----------|------------------|
| 1 | Pipeline ETL automatisé et reproductible | DAG Airflow fonctionnel |
| 2 | API de scoring production-ready | FastAPI avec tests |
| 3 | Monitoring des performances du modèle | Dashboard Grafana |
| 4 | Infrastructure containerisée | Docker Compose complet |
| 5 | Code propre et documenté | README + docstrings |

### 5.3 Objectifs portfolio (personnel)

| # | Objectif | Livrable |
|---|----------|----------|
| 1 | Démontrer des compétences DE + ML | Repo GitHub public |
| 2 | Projet déployé et accessible | App Streamlit live |
| 3 | Visibilité professionnelle | Post LinkedIn avec démo |


## 6. PÉRIMÈTRE DU PROJET

### 6.1 Ce qui est inclus (IN SCOPE)

| Composant | Description |
|-----------|-------------|
| **Ingestion des données** | Chargement du dataset Kaggle dans PostgreSQL |
| **Feature Engineering** | Création de variables à partir des données brutes |
| **Modélisation** | Entraînement XGBoost + évaluation |
| **Explicabilité** | SHAP pour interpréter les prédictions |
| **API de scoring** | FastAPI pour servir le modèle |
| **Interface utilisateur** | Streamlit pour démo interactive |
| **Orchestration** | Airflow pour automatiser le pipeline |
| **Monitoring** | Prometheus + Grafana pour surveiller l'API |
| **Containerisation** | Docker pour la reproductibilité |

### 6.2 Ce qui est exclu (OUT OF SCOPE)

| Élément | Raison |
|---------|--------|
| Déploiement cloud production | Coût (projet portfolio gratuit) |
| Données en temps réel | Dataset statique Kaggle |
| Modèle LGD / EAD | Focus sur PD uniquement |
| Interface de gestion des utilisateurs | Pas de gestion d'accès |
| Retraining automatique | V2 potentielle |

### 6.3 Contraintes

| Contrainte | Impact |
|------------|--------|
| **Budget : 0€** | Utilisation d'outils open-source uniquement |
| **Dataset fixe** | Kaggle Home Credit (pas de données propriétaires) |
| **Ressources locales** | Développement sur machine personnelle |


## 7. PRÉSENTATION DES DONNÉES

### 7.1 Source : Kaggle Home Credit Default Risk

**Lien :** https://www.kaggle.com/c/home-credit-default-risk

**Contexte :** Compétition Kaggle (2018) organisée par Home Credit pour améliorer leur modèle de scoring.

### 7.2 Structure des données

| Table | Description | Lignes | Colonnes |
|-------|-------------|--------|----------|
| **application_train.csv** | Demandes de crédit avec label TARGET | 307,511 | 122 |
| **application_test.csv** | Demandes sans label (pour soumission) | 48,744 | 121 |
| **bureau.csv** | Historique crédit d'autres institutions | 1,716,428 | 17 |
| **bureau_balance.csv** | Soldes mensuels des crédits bureau | 27,299,925 | 3 |
| **previous_application.csv** | Demandes précédentes chez Home Credit | 1,670,214 | 37 |
| **POS_CASH_balance.csv** | Soldes mensuels crédits POS/Cash | 10,001,358 | 8 |
| **credit_card_balance.csv** | Soldes mensuels cartes de crédit | 3,840,312 | 23 |
| **installments_payments.csv** | Historique des paiements | 13,605,401 | 8 |

### 7.3 Variable cible

```
TARGET :
  - 0 = Pas de défaut (remboursement OK)
  - 1 = Défaut de paiement

Distribution : ~8% de défauts (déséquilibre de classes)
```

### 7.4 Types de variables disponibles

| Catégorie | Exemples | Utilité |
|-----------|----------|---------|
| **Démographiques** | Âge, genre, situation familiale | Profil client |
| **Financières** | Revenus, montant crédit, annuité | Capacité de remboursement |
| **Emploi** | Type de contrat, ancienneté, secteur | Stabilité des revenus |
| **Logement** | Type, région, taille | Stabilité et patrimoine |
| **Comportementales** | Historique de paiements, retards | Comportement passé |
| **Documents** | Documents fournis ou manquants | Sérieux du dossier |


## 8. APPROCHE MÉTHODOLOGIQUE

### 8.1 Vue d'ensemble du pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         PIPELINE CREDIT RISK                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐          │
│  │  DATA    │───▶│   ETL    │───▶│ FEATURE  │───▶│  MODEL   │          │
│  │  SOURCE  │    │ PIPELINE │    │   ENG.   │    │ TRAINING │          │
│  │ (Kaggle) │    │          │    │          │    │          │          │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘          │
│       │               │               │               │                 │
│       ▼               ▼               ▼               ▼                 │
│  CSV Files      PostgreSQL      Features DB      XGBoost Model         │
│                                                       │                 │
│                                                       ▼                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐          │
│  │ GRAFANA  │◀───│PROMETHEUS│◀───│ FAST API │◀───│  MODEL   │          │
│  │DASHBOARD │    │ METRICS  │    │  SERVER  │    │  SHAP    │          │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘          │
│       │                               │                                 │
│       │                               ▼                                 │
│       │                         ┌──────────┐                           │
│       └────────────────────────▶│STREAMLIT │                           │
│                                 │    UI    │                           │
│                                 └──────────┘                           │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                         AIRFLOW                                   │  │
│  │                    (Orchestration)                                │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 8.2 Étapes détaillées

#### Phase 1 : Ingestion et stockage
1. Téléchargement des données Kaggle
2. Exploration initiale (EDA)
3. Chargement dans PostgreSQL

#### Phase 2 : Feature Engineering
1. Nettoyage des données (valeurs manquantes, outliers)
2. Agrégation des tables secondaires
3. Création de nouvelles features (ratios, agrégats, etc.)
4. Encodage des variables catégorielles

#### Phase 3 : Modélisation
1. Split train/validation/test
2. Gestion du déséquilibre de classes (SMOTE ou class_weight)
3. Entraînement XGBoost
4. Hyperparameter tuning (Optuna ou GridSearch)
5. Évaluation (AUC, précision, rappel, matrice de confusion)

#### Phase 4 : Explicabilité
1. Calcul des SHAP values
2. Feature importance globale
3. Explications individuelles

#### Phase 5 : Mise en production
1. API FastAPI avec endpoint de prédiction
2. Interface Streamlit pour démo
3. Containerisation Docker
4. Orchestration Airflow

#### Phase 6 : Monitoring
1. Métriques Prometheus (latence, requêtes, erreurs)
2. Dashboard Grafana
3. Alertes (optionnel)


## 9. STACK TECHNIQUE

### 9.1 Choix technologiques

| Catégorie | Technologie | Justification |
|-----------|-------------|---------------|
| **Langage** | Python 3.12+ | Standard industrie Data/ML |
| **ML** | XGBoost | Performant, rapide, interprétable |
| **Explicabilité** | SHAP | Standard pour l'explicabilité ML |
| **Base de données** | PostgreSQL | Robuste, SQL standard, gratuit |
| **API** | FastAPI | Moderne, rapide, documentation auto |
| **UI** | Streamlit | Rapide à développer, gratuit à déployer |
| **Orchestration** | Airflow | Standard industrie pour les pipelines |
| **Monitoring** | Prometheus + Grafana | Stack standard observabilité |
| **Container** | Docker + Docker Compose | Reproductibilité, portabilité |

### 9.2 Pourquoi ces choix ?

**XGBoost plutôt que Deep Learning :**
- Données tabulaires → arbres > réseaux de neurones
- Plus interprétable
- Plus rapide à entraîner
- Moins de données nécessaires

**PostgreSQL plutôt que fichiers CSV :**
- Requêtes SQL pour le feature engineering
- Intégrité des données
- Préparation pour un contexte production

**FastAPI plutôt que Flask :**
- Performance supérieure (async)
- Documentation OpenAPI automatique
- Validation Pydantic intégrée


## 10. CRITÈRES DE SUCCÈS

### 10.1 Métriques techniques

| Métrique | Seuil minimum | Cible | Commentaire |
|----------|---------------|-------|-------------|
| **AUC-ROC** | 0.70 | 0.75+ | Discrimination du modèle |
| **Gini** | 0.40 | 0.50+ | 2*AUC - 1 |
| **Rappel (défauts)** | 0.60 | 0.70+ | Détecter les vrais défauts |
| **Précision (défauts)** | 0.30 | 0.40+ | Limiter les faux positifs |
| **Latence API** | < 500ms | < 200ms | Temps de réponse |

### 10.2 Livrables attendus

| Livrable | Description | Validation |
|----------|-------------|------------|
| Repo GitHub | Code source complet | Public et documenté |
| README.md | Documentation du projet | Clair et professionnel |
| App Streamlit | Démo interactive | Accessible en ligne |
| Docker Compose | Infrastructure complète | `docker-compose up` fonctionne |
| Notebook EDA | Exploration des données | Visualisations et insights |
| Dashboard Grafana | Monitoring | Métriques visibles |


## 11. RISQUES ET MITIGATION

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Déséquilibre de classes (8% défauts) | Élevée | Moyen | SMOTE, class_weight, seuil ajusté |
| Overfitting sur les données Kaggle | Moyenne | Élevé | Validation croisée, holdout set |
| Ressources machine limitées | Moyenne | Moyen | Sous-échantillonnage si nécessaire |
| Complexité feature engineering | Élevée | Moyen | Commencer simple, itérer |
| Déploiement Streamlit Cloud | Faible | Faible | Alternatives : HuggingFace, Railway |


## 12. RESSOURCES ET DOCUMENTATION

### 12.1 Ressources pour comprendre le métier (Credit Risk)

#### Articles et guides professionnels

| Ressource | Description | Lien |
|-----------|-------------|------|
| **Investopedia - Credit Risk** | Introduction claire au risque de crédit | https://www.investopedia.com/terms/c/creditrisk.asp |
| **Corporate Finance Institute** | Guide complet sur l'analyse crédit | https://corporatefinanceinstitute.com/resources/commercial-lending/credit-risk/ |
| **Risk.net** | Actualités et analyses professionnelles | https://www.risk.net/risk-management/credit-risk |
| **Moody's Analytics** | Ressources sur le credit scoring | https://www.moodysanalytics.com/articles/2019/credit-scoring |

#### Réglementation Bâle

| Ressource | Description | Lien |
|-----------|-------------|------|
| **BIS - Basel Framework** | Textes officiels Bâle III | https://www.bis.org/basel_framework/ |
| **European Banking Authority** | Application en Europe | https://www.eba.europa.eu/ |

#### Livres recommandés (approche entreprise)

| Livre | Auteur | Pourquoi le lire |
|-------|--------|------------------|
| *Credit Risk Modeling using Excel and VBA* | Gunter Löeffler | Pratique, orienté implémentation |
| *Credit Risk Analytics* | Bart Baesens | ML appliqué au crédit |
| *Developing Credit Risk Models Using SAS* | D. Hartman | Méthodologie industrielle |

### 12.2 Ressources techniques (Data Science / ML)

#### Tutoriels et notebooks

| Ressource | Description | Lien |
|-----------|-------------|------|
| **Kaggle Home Credit - Kernels** | Solutions de la compétition | https://www.kaggle.com/c/home-credit-default-risk/code |
| **Will Koehrsen - Start Here** | Excellent notebook de démarrage | https://www.kaggle.com/code/willkoehrsen/start-here-a-gentle-introduction |
| **Feature Engineering Guide** | Feature engineering détaillé | https://www.kaggle.com/code/jsaguiar/lightgbm-with-simple-features |

#### Documentation technique

| Outil | Documentation |
|-------|---------------|
| **XGBoost** | https://xgboost.readthedocs.io/ |
| **SHAP** | https://shap.readthedocs.io/ |
| **FastAPI** | https://fastapi.tiangolo.com/ |
| **Airflow** | https://airflow.apache.org/docs/ |
| **Streamlit** | https://docs.streamlit.io/ |

### 12.3 Ressources Data Engineering

| Ressource | Description | Lien |
|-----------|-------------|------|
| **DataExpert - Portfolio Projects** | Projets DE pour portfolio | https://www.dataexpert.io/blog/data-engineering-portfolio-projects-get-hired |
| **Seattle Data Guy** | Conseils DE pratiques | https://www.youtube.com/@SeattleDataGuy |
| **Data Engineering Wiki** | Référence communautaire | https://dataengineering.wiki/ |

### 12.4 Exemples de projets similaires (GitHub)

| Projet | Description | Lien |
|--------|-------------|------|
| **Credit Risk MLOps** | Pipeline complet avec MLflow | https://github.com/topics/credit-risk-modeling |
| **Home Credit Solutions** | Solutions Kaggle open-source | https://github.com/topics/home-credit |


## 13. GLOSSAIRE

| Terme | Définition |
|-------|------------|
| **AUC-ROC** | Area Under the Receiver Operating Characteristic curve. Mesure de la capacité discriminante d'un modèle. |
| **Default** | Défaut de paiement. Non-respect des obligations de remboursement. |
| **EDA** | Exploratory Data Analysis. Analyse exploratoire des données. |
| **Feature Engineering** | Création de nouvelles variables à partir des données brutes. |
| **Gini** | Coefficient mesurant la qualité d'un modèle de scoring (Gini = 2*AUC - 1). |
| **IRB** | Internal Ratings-Based. Approche permettant aux banques d'utiliser leurs propres modèles de risque (Bâle II). |
| **LGD** | Loss Given Default. Perte en cas de défaut (% du montant exposé). |
| **PD** | Probability of Default. Probabilité de défaut à un horizon donné. |
| **SHAP** | SHapley Additive exPlanations. Méthode d'explicabilité des modèles ML. |
| **Scoring** | Modèle attribuant une note de risque à un demandeur de crédit. |


## 14. CLARIFICATIONS ET CHOIX STRATÉGIQUES

### 14.1 Données récentes vs Méthodologie : Qu'est-ce qui compte ?

**Les deux comptent, mais pour des raisons différentes :**

| Contexte | Données récentes | Méthodologie solide |
|----------|------------------|---------------------|
| **En entreprise** | CRITIQUE - les comportements clients évoluent | CRITIQUE - sinon résultats faux |
| **Pour un portfolio** | MOINS important | TRÈS important |

#### Pourquoi les données récentes comptent en entreprise ?

Un modèle entraîné sur des données de 2018 sera obsolète en 2026 car :
- Les comportements de paiement ont changé (COVID, inflation, crise économique)
- Les produits financiers évoluent
- La réglementation change (RGPD, Bâle III renforcé)
- Les profils de clients se transforment (digital natives, gig economy)

#### Pourquoi c'est moins critique pour un portfolio ?

**Le recruteur sait que tu n'as pas accès à des données bancaires fraîches.** Il évalue :
- Ta capacité à structurer un pipeline de données proprement
- Ton application des bonnes techniques de feature engineering
- Ta rigueur dans l'interprétation des résultats
- Ta capacité à mettre en production un modèle

> **Principe clé :** La donnée est le carburant, la méthodologie est le moteur. Un bon moteur avec du carburant ancien démontre tes compétences. Un mauvais moteur avec du carburant frais ne prouve rien.

### 14.2 Pourquoi le dataset Home Credit ?

**C'est un choix intentionnel et stratégique, pas un choix par défaut.**

#### Avantages de Home Credit

| Raison | Explication |
|--------|-------------|
| **Problème réel** | Home Credit est une vraie entreprise avec un vrai problème métier |
| **Données riches** | 8 tables relationnelles (307k clients, 27M+ lignes bureau_balance) |
| **Complexité réaliste** | Jointures, agrégations, données manquantes = réalité du métier |
| **Cas difficile** | Clients sans historique bancaire = scoring alternatif (plus challengeant) |
| **Bien documenté** | Compétition Kaggle = beaucoup de ressources et benchmarks |
| **Reconnu** | Les recruteurs du secteur financier connaissent ce dataset |

#### Comparaison avec d'autres datasets

| Dataset | Avantage | Inconvénient | Verdict |
|---------|----------|--------------|---------|
| **Home Credit** | Complexité réaliste (8 tables) | Données de 2018 | ✅ Meilleur choix portfolio |
| **Lending Club** | Plus récent (jusqu'à 2020) | Structure trop simple (1 table) | ⚠️ Moins démonstratif |
| **German Credit** | Classique académique | Trop petit (1000 lignes) | ❌ Trop basique |
| **Give Me Some Credit** | Déséquilibre intéressant | Peu de features | ⚠️ Acceptable |

#### Le cas particulier : Clients sans historique

Home Credit cible des clients qui n'ont **pas ou peu d'historique bancaire**. C'est un problème :
- **Plus difficile** que le scoring classique (pas de score FICO disponible)
- **Plus pertinent** pour l'Afrique et les marchés émergents (inclusion financière)
- **Plus innovant** car il force à utiliser des données alternatives

> **Alignement carrière :** Ce cas d'usage est parfaitement aligné avec ton objectif de travailler en Afrique où l'inclusion financière et le scoring alternatif sont des enjeux majeurs (Mobile Money, FinTech).

### 14.3 Pourquoi PostgreSQL plutôt que rester sur CSV ?

**Le dataset Kaggle EST en CSV. Nous le chargeons dans PostgreSQL. Voici pourquoi :**

#### Workflow du projet

```
CSV (Kaggle)  →  PostgreSQL  →  Feature Engineering  →  Modèle
   SOURCE         STOCKAGE         TRAITEMENT          OUTPUT
```

#### Justifications techniques

| Raison | Explication |
|--------|-------------|
| **Performance** | SQL est optimisé pour les jointures sur des millions de lignes |
| **Mémoire** | `bureau_balance.csv` (27M lignes) ne tiendra pas en RAM avec Pandas |
| **Requêtes complexes** | GROUP BY, sous-requêtes, window functions natifs |
| **Reproductibilité** | Les requêtes SQL sont versionnables et auditables |
| **Simulation production** | En entreprise, les données viennent d'une BDD, jamais de CSV |
| **Compétence démontrée** | Montre que tu sais travailler avec des bases de données |

#### Exemple concret

```python
# ❌ Avec CSV/Pandas (lent, mémoire intensive)
bureau = pd.read_csv('bureau.csv')  # 1.7M lignes chargées en RAM
bureau_balance = pd.read_csv('bureau_balance.csv')  # 27M lignes = crash probable
merged = bureau.merge(bureau_balance, on='SK_ID_BUREAU')  # Très lent
agg = merged.groupby('SK_ID_CURR').agg({...})  # Encore plus lent

# ✅ Avec PostgreSQL (rapide, optimisé)
query = """
SELECT
    b.SK_ID_CURR,
    COUNT(DISTINCT b.SK_ID_BUREAU) as nb_bureau_credits,
    AVG(b.AMT_CREDIT_SUM) as avg_credit_amount,
    SUM(CASE WHEN bb.STATUS = 'C' THEN 1 ELSE 0 END) as nb_closed
FROM bureau b
LEFT JOIN bureau_balance bb ON b.SK_ID_BUREAU = bb.SK_ID_BUREAU
GROUP BY b.SK_ID_CURR
"""
# Exécuté côté serveur PostgreSQL, seul le résultat agrégé revient en Python
```

#### Alternative légère : DuckDB

Si PostgreSQL semble lourd pour un projet local, **DuckDB** est une alternative :
- SQL analytique sur fichiers (pas de serveur)
- Très performant pour l'OLAP
- S'intègre directement avec Pandas/Parquet

```python
import duckdb
result = duckdb.query("SELECT * FROM 'bureau.csv' WHERE AMT_CREDIT_SUM > 100000")
```

> **Choix final :** Nous utiliserons PostgreSQL pour démontrer la compétence BDD relationnelle (standard industrie), avec possibilité de basculer sur DuckDB si les ressources machine sont limitées.


## 15. CONCLUSION

Ce projet de Credit Risk Scoring Pipeline combine :

1. **Une problématique métier réelle** : Le risque de crédit est au cœur de l'activité bancaire
2. **Des compétences Data Engineering** : Pipeline complet, orchestration, monitoring
3. **Des compétences Data Science** : ML, feature engineering, explicabilité
4. **Une orientation production** : API, Docker, monitoring

C'est exactement le type de projet que recherchent les employeurs en 2026 : un profil capable de comprendre le métier ET de construire des solutions techniques end-to-end.


**Document rédigé le :** 25 Janvier 2026
**Auteur :** Daniela Samo 
**Version :** 1.1 (ajout section 14 - Clarifications)
**Prochain document :** `02_FEUILLE_DE_ROUTE.md` (Plan d'exécution pas à pas)
