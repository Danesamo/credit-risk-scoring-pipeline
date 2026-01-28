# Feuille de Route : Credit Risk Scoring Pipeline

---

## OBJECTIF DE CE DOCUMENT

Ce document est le **plan d'exécution pas à pas** du projet. Chaque étape doit être validée avant de passer à la suivante. Cocher les cases au fur et à mesure de l'avancement.

---

## VUE D'ENSEMBLE

```
PHASE 1          PHASE 2          PHASE 3          PHASE 4          PHASE 5          PHASE 6
┌────────┐      ┌────────┐      ┌────────┐      ┌────────┐      ┌────────┐      ┌────────┐
│ SETUP  │ ───▶ │  DATA  │ ───▶ │FEATURE │ ───▶ │ MODEL  │ ───▶ │  API   │ ───▶ │DEPLOI- │
│        │      │  EDA   │      │  ENG.  │      │   ML   │      │  & UI  │      │ EMENT  │
└────────┘      └────────┘      └────────┘      └────────┘      └────────┘      └────────┘
   2 jours        3 jours        4 jours         4 jours         3 jours         2 jours
```

**Durée totale estimée : 3 semaines**

---

## PHASE 1 : SETUP & ENVIRONNEMENT

**Objectif :** Préparer l'environnement de développement

### Étape 1.1 : Structure du projet
- [x] Créer l'arborescence complète des dossiers
- [ ] Initialiser le dépôt Git
- [x] Créer le fichier `.gitignore`
- [x] Créer le `README.md` initial

**Structure cible :**
```
Credit_Risk_Scoring_Project/
├── .gitignore
├── README.md
├── requirements.txt
├── docker-compose.yml
├── Makefile
├── data/
│   ├── raw/              # Données Kaggle brutes
│   ├── processed/        # Données transformées
│   └── features/         # Features engineered
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_modeling.ipynb
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── ingestion.py
│   │   └── preprocessing.py
│   ├── features/
│   │   ├── __init__.py
│   │   └── build_features.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── train.py
│   │   ├── predict.py
│   │   └── evaluate.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── api/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   └── endpoints/
├── streamlit/
│   └── app.py
├── airflow/
│   └── dags/
│       └── credit_risk_pipeline.py
├── monitoring/
│   ├── prometheus.yml
│   └── grafana/
│       └── dashboards/
├── models/
│   └── .gitkeep          # Modèles entraînés (non versionnés)
├── tests/
│   ├── __init__.py
│   ├── test_data.py
│   ├── test_features.py
│   ├── test_models.py
│   └── test_api.py
├── docs/
│   ├── 01_ETUDE_PROJET.md
│   └── 02_FEUILLE_DE_ROUTE.md
└── configs/
    └── config.yaml
```

### Étape 1.2 : Environnement Python
- [x] Créer l'environnement virtuel (`python -m venv venv`)
- [x] Créer `requirements.txt` avec les dépendances
- [x] Installer les dépendances (partiellement - packages EDA installés)

**requirements.txt initial :**
```
# Core
python>=3.12
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.3.0

# ML
xgboost>=2.0.0
shap>=0.50.0
optuna>=3.4.0
imbalanced-learn>=0.11.0

# Data
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0
duckdb>=0.9.0

# API
fastapi>=0.104.0
uvicorn>=0.24.0
pydantic>=2.5.0

# UI
streamlit>=1.28.0

# Orchestration
apache-airflow>=2.7.0

# Monitoring
prometheus-client>=0.18.0

# Visualization
matplotlib>=3.8.0
seaborn>=0.13.0
plotly>=5.18.0

# Utils
python-dotenv>=1.0.0
pyyaml>=6.0.0
loguru>=0.7.0

# Testing
pytest>=7.4.0
pytest-cov>=4.1.0

# Notebooks
jupyter>=1.0.0
ipykernel>=6.26.0
```

### Étape 1.3 : Docker
- [x] Créer le `Dockerfile` pour l'API
- [x] Créer le `docker-compose.yml` de base
- [ ] Tester le build Docker

### Étape 1.4 : Base de données
- [x] Configurer PostgreSQL (via Docker - fichiers prêts)
- [ ] Créer la base de données `credit_risk`
- [ ] Tester la connexion

**Validation Phase 1 :**
```bash
# Checklist de validation
[ ] git status fonctionne
[ ] python -c "import pandas; print(pandas.__version__)" fonctionne
[ ] docker-compose config est valide
[ ] psql -h localhost -U user -d credit_risk connecte
```

---

## PHASE 2 : DATA & EDA

**Objectif :** Télécharger, explorer et comprendre les données

### Étape 2.1 : Téléchargement des données
- [x] Configurer l'API Kaggle (token KAGGLE_API_TOKEN)
- [x] Télécharger le dataset Home Credit
- [x] Dézipper dans `data/raw/`
- [x] Vérifier l'intégrité des fichiers (10 fichiers, 2.5 GB)

**Commandes :**
```bash
kaggle competitions download -c home-credit-default-risk
unzip home-credit-default-risk.zip -d data/raw/
```

### Étape 2.2 : Exploration initiale
- [x] Créer le notebook `01_EDA.ipynb`
- [x] Charger `application_train.csv` (307,511 lignes, 122 colonnes)
- [x] Analyser la distribution de TARGET (8.07% défauts, ratio 1:11)
- [x] Statistiques descriptives de base
- [x] Types de données et valeurs manquantes (41 colonnes >50% manquantes)

**Points à documenter :**
- Nombre de lignes/colonnes par table
- % de valeurs manquantes par colonne
- Distribution de la variable cible
- Corrélations principales

### Étape 2.3 : EDA approfondie
- [x] Visualisation de la distribution des variables numériques
- [x] Analyse des variables catégorielles (16 variables, cardinalité analysée)
- [x] Identification des outliers (DAYS_EMPLOYED anomalie 365243)
- [x] Analyse des corrélations avec TARGET (EXT_SOURCE_3: -0.179)
- [x] Exploration des tables secondaires (bureau, previous_application, etc.)

**Livrables :**
- [x] Notebook EDA complet avec visualisations
- [x] Liste des variables potentiellement importantes (EXT_SOURCE, DAYS_BIRTH, etc.)
- [x] Liste des problèmes identifiés (missing values, outliers, déséquilibre)

### Étape 2.4 : Chargement en base de données
- [x] Créer le script `src/data/ingestion.py`
- [x] Définir le schéma des tables SQL (via init_db.sql)
- [x] Charger les données dans PostgreSQL ✅ (307k + 1.7M + 1.7M = 3.7M lignes)
- [ ] Créer des index pour optimiser les requêtes

**Approche hybride adoptée :**
- PostgreSQL : application_train, bureau, previous_application
- Python/CSV : installments_payments, POS_CASH_balance, credit_card_balance (agrégation directe)

**Validation Phase 2 :**
```bash
# Checklist de validation
[ ] Notebook EDA exécutable de bout en bout
[ ] SELECT COUNT(*) FROM application_train retourne 307511
[ ] Toutes les tables sont chargées dans PostgreSQL
[ ] Document avec les insights principaux de l'EDA
```

---

## PHASE 3 : FEATURE ENGINEERING

**Objectif :** Créer des variables pertinentes pour le modèle

### Étape 3.1 : Nettoyage des données ✅
- [x] Créer `src/data/preprocessing.py`
- [x] Gérer les valeurs manquantes (imputation médiane/mode)
- [x] Gérer les outliers (capping par percentiles)
- [x] Corriger les anomalies identifiées dans l'EDA (DAYS_EMPLOYED = 365243)

**Classe DataPreprocessor créée avec :**
- `fix_anomalies()` : Correction DAYS_EMPLOYED + indicateur binaire
- `impute_missing_values()` : Médiane (num) / Mode (cat)
- `cap_outliers()` : Percentiles 1%-99%
- `optimize_dtypes()` : Réduction mémoire automatique

**Stratégies de gestion des valeurs manquantes :**
| Type de variable | Stratégie |
|-----------------|-----------|
| Numérique | Médiane ou -999 (indicateur explicite) |
| Catégorielle | Mode ou catégorie "Unknown" |
| Binaire | Mode |

### Étape 3.2 : Agrégation des tables secondaires ✅
- [x] Créer `src/features/build_features.py`
- [x] Agréger `bureau` → métriques par client (SQL PostgreSQL)
- [x] Agréger `previous_application` → métriques par client (SQL PostgreSQL)
- [x] Agréger `installments_payments.csv` → comportement de paiement (Python chunked)
- [x] Agréger `credit_card_balance.csv` → utilisation carte (Python chunked)
- [x] Agréger `POS_CASH_balance.csv` → comportement POS (Python chunked)

**Classe FeatureEngineer créée avec :**
- `create_application_features()` : 16 features (ratios, âge, documents)
- `create_bureau_features()` : ~18 features depuis PostgreSQL
- `create_previous_application_features()` : ~18 features depuis PostgreSQL
- `create_installments_features()` : ~14 features (chunked CSV)
- `create_pos_cash_features()` : ~17 features (chunked CSV)
- `create_credit_card_features()` : ~21 features (chunked CSV)

**Exemples d'agrégations :**
```python
# Bureau
- Nombre de crédits actifs
- Montant total des crédits
- Nombre de retards passés
- Durée moyenne des crédits

# Previous Application
- Nombre de demandes précédentes
- Taux d'acceptation
- Montant moyen demandé vs accordé
- Type de crédit le plus fréquent

# Installments
- Nombre de paiements en retard
- Montant moyen des retards
- Ratio paiements à temps
```

### Étape 3.3 : Création de nouvelles features ✅
- [x] Ratios financiers (credit_income_ratio, annuity_income_ratio, etc.)
- [x] Indicateurs dérivés (bureau_active_ratio, prev_approval_rate, etc.)
- [x] Features comportementales (instal_late_ratio, cc_utilization_mean, etc.)
- [x] Agrégats statistiques (mean, max, sum, count par client)

**Features prioritaires à créer :**
```python
# Ratios
ANNUITY_INCOME_RATIO = AMT_ANNUITY / AMT_INCOME_TOTAL
CREDIT_INCOME_RATIO = AMT_CREDIT / AMT_INCOME_TOTAL
CREDIT_ANNUITY_RATIO = AMT_CREDIT / AMT_ANNUITY
GOODS_CREDIT_RATIO = AMT_GOODS_PRICE / AMT_CREDIT

# Âge
DAYS_BIRTH_YEARS = -DAYS_BIRTH / 365
DAYS_EMPLOYED_YEARS = -DAYS_EMPLOYED / 365
EMPLOYED_TO_BIRTH_RATIO = DAYS_EMPLOYED / DAYS_BIRTH

# Indicateurs
HAS_BUREAU = 1 if client in bureau else 0
HAS_PREVIOUS = 1 if client in previous_application else 0
```

### Étape 3.4 : Encodage des variables catégorielles
- [x] Variables catégorielles conservées → **Reporté volontairement à Phase 4**

**Raison du report :**
- XGBoost supporte les catégorielles nativement (`enable_categorical=True`)
- Certaines variables ont haute cardinalité (ORGANIZATION_TYPE: 58 valeurs) → one-hot non viable
- Approche moderne : encodage dans le pipeline de modélisation
- C'est l'approche des top Kagglers sur Home Credit

### Étape 3.5 : Sélection de features
- [x] NaN remplis (0 pour count/sum, médiane pour autres)
- [x] Sélection finale → **Reportée à Phase 4** (après analyse importance features)

### Étape 3.6 : Dataset final ✅
- [x] Merger toutes les features dans un dataset unique
- [x] Sauvegarder dans `data/features/features_v1.csv`
- [x] 307,511 lignes × 225 colonnes (452.3 MB)

**Résumé features créées :**
| Source | Nb features |
|--------|-------------|
| application | 16 |
| bureau | 18 |
| previous_application | 18 |
| installments | 13 |
| pos_cash | 17 |
| credit_card | 21 |
| **Total nouvelles** | **103** |

**Validation Phase 3 :**
```bash
# Checklist de validation
[x] Script de feature engineering reproductible (build_features.py)
[x] Dataset final avec 225 colonnes documentées
[ ] Notebook 02_feature_engineering.ipynb (optionnel - code dans src/)
[x] Aucune fuite de données (target leakage) - features basées sur historique
```

---

## PHASE 4 : MODÉLISATION ML

**Objectif :** Entraîner et évaluer le modèle de scoring

### Étape 4.1 : Préparation des données
- [x] Créer `notebooks/03_modeling.ipynb` (approche notebook pour visualisations)
- [x] Charger `data/features/features_v1.csv` (307,511 × 225)
- [x] **Encodage des variables catégorielles** :
  - [x] Identifier les colonnes catégorielles (16 colonnes type object)
  - [x] LabelEncoder pour toutes les catégorielles
- [x] Split train/validation/test (70/15/15) stratifié
- [x] Gérer le déséquilibre de classes (`scale_pos_weight=11.39`)

**Stratégie pour le déséquilibre :**
```python
# Option 1: XGBoost scale_pos_weight
scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()

# Option 2: SMOTE (à utiliser avec précaution)
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)
```

### Étape 4.2 : Baseline model
- [x] Entraîner un modèle XGBoost avec paramètres par défaut
- [x] Évaluer sur validation set (AUC = 0.7778)
- [x] Documenter les métriques de base (Gini = 0.5556)

**Métriques à calculer :**
- AUC-ROC
- Gini (2*AUC - 1)
- Precision, Recall, F1-score
- Matrice de confusion
- Courbe ROC et Precision-Recall

### Étape 4.3 : Hyperparameter tuning
- [x] Définir l'espace de recherche des hyperparamètres (9 paramètres)
- [x] Utiliser Optuna pour l'optimisation (50 trials, SQLite persistant)
- [x] Évaluation sur validation set (pas CV pour rapidité)
- [x] Sélectionner le meilleur modèle (Trial 25, AUC = 0.7836)

**Paramètres à tuner :**
```python
param_space = {
    'max_depth': [3, 5, 7, 9],
    'learning_rate': [0.01, 0.05, 0.1],
    'n_estimators': [100, 200, 500],
    'min_child_weight': [1, 3, 5],
    'subsample': [0.7, 0.8, 0.9],
    'colsample_bytree': [0.7, 0.8, 0.9],
    'gamma': [0, 0.1, 0.2],
    'reg_alpha': [0, 0.1, 1],
    'reg_lambda': [1, 2, 5]
}
```

### Étape 4.4 : Évaluation finale
- [x] Évaluer sur le test set (46,127 lignes jamais vues)
- [x] Générer toutes les métriques (AUC=0.7836, Recall=0.70, Precision=0.19)
- [x] Générer visualisations (confusion matrix, ROC, PR curve)
- [x] Analyser les erreurs (70% détection, 81% fausses alertes acceptables)

### Étape 4.5 : Explicabilité SHAP
- [x] Calculer les SHAP values (échantillon 1000 lignes)
- [x] Feature importance globale (ext_source_mean = 40%)
- [x] Graphiques : summary plot bar + summary plot
- [x] Top 10 features documentées avec interprétation métier

**Visualisations SHAP à créer :**
```python
# Global
shap.summary_plot(shap_values, X_test)
shap.summary_plot(shap_values, X_test, plot_type="bar")

# Individuel
shap.force_plot(explainer.expected_value, shap_values[0], X_test.iloc[0])
shap.waterfall_plot(shap_values[0])
```

### Étape 4.6 : Sauvegarde du modèle
- [x] Sauvegarder le modèle (`models/xgboost_credit_risk_v1.pkl`)
- [x] Sauvegarder les label encoders (`models/label_encoders.pkl`)
- [x] Sauvegarder les noms de features (`models/feature_names.json`)
- [x] Sauvegarder les métriques (`models/metrics.json`)
- [x] Sauvegarder les graphiques (5 fichiers PNG)

**Validation Phase 4 :**
```bash
# Checklist de validation
[x] AUC-ROC > 0.75 sur le test set ✅ (0.7836)
[x] Notebook 03_modeling.ipynb complet ✅
[x] Modèle sauvegardé dans models/ ✅
[x] Visualisations SHAP générées ✅
[x] Métriques documentées ✅
```

---

## PHASE 5 : API & INTERFACE

**Objectif :** Exposer le modèle via une API et créer une interface démo

### Étape 5.1 : API FastAPI
- [x] Créer `api/main.py`
- [x] Schémas Pydantic intégrés (ClientData, PredictionResponse, HealthResponse, ExplainResponse)
- [x] Endpoint `/predict` pour le scoring
- [x] Endpoint `/explain` pour les SHAP values ✅
- [x] Endpoint `/health` pour le monitoring

**Endpoints implémentés :**
```
GET /
  Output: Liste des endpoints disponibles

POST /predict
  Input: données client (JSON)
  Output: {probability, prediction, risk_level, score}

POST /explain
  Input: données client (JSON)
  Output: {probability, base_probability, risk_level, top_risk_factors, top_protective_factors}

GET /health
  Output: {status, model_loaded, model_version, auc_roc}

GET /docs
  Output: Documentation Swagger automatique
```

### Étape 5.2 : Tests API
- [x] Créer `tests/test_api.py`
- [x] Tests unitaires des endpoints (17 tests : root, health, predict, explain)
- [x] Tests de validation des inputs (3 tests)
- [x] Tests de logique métier (2 tests)
- [x] Tests de performance (3 tests) - latence predict < 500ms, explain < 2s
- [x] Tests endpoint `/explain` (6 tests SHAP values)
- [x] **Résultat : 31/31 tests PASSED ✅**

### Étape 5.3 : Interface Streamlit
- [x] Créer `streamlit/app.py`
- [x] Formulaire de saisie des données client
- [x] Affichage du score et de la décision
- [x] **BONUS : Support multilingue (FR/EN)**
- [x] **BONUS : Support multi-devises (EUR, USD, XAF, XOF)**
- [x] Exemples pré-remplis calibrés (Fiable, Moyen, Risqué)
- [x] Indicateur visuel de risque avec légende
- [x] Facteurs clés (positifs/négatifs)
- [x] Visualisation SHAP interactive via API /explain ✅

**Sections de l'interface (implémentées) :**
```
1. Header avec titre et sous-titre
2. Sidebar : langue, devise, infos modèle, copyright
3. Formulaire : revenus, crédit, mensualité, âge, emploi, score
4. Boutons profils : Fiable, Moyen, Risqué (avec indication active)
5. Résultat : Décision, Score/850, Probabilité, Niveau de risque
6. Indicateur : Barre 0%-100% avec position
7. Facteurs : Points positifs ✓ / Points d'attention ✗
8. Détails techniques : JSON brut
```

### Étape 5.4 : Intégration API ↔ Streamlit
- [x] Streamlit appelle l'API FastAPI
- [x] Gestion des erreurs (API indisponible, erreur 400/500)
- [x] Loading states (spinner pendant l'analyse)
- [x] Conversion devises bidirectionnelle

**Validation Phase 5 :**
```bash
# Checklist de validation
[x] curl localhost:8000/predict fonctionne
[x] curl localhost:8000/health retourne healthy
[x] Streamlit s'affiche correctement
[x] 3 profils donnent résultats cohérents (36% < 40% < 81%)
[x] Multi-devises : EUR et XAF donnent même probabilité
[x] Multilingue : FR et EN fonctionnent
[x] pytest tests/test_api.py → 31/31 PASSED ✅
```

---

## PHASE 6 : ORCHESTRATION & MONITORING

**Objectif :** Automatiser le pipeline et monitorer l'application

### Étape 6.1 : Métriques Prometheus
- [x] Ajouter endpoint `/metrics` dans FastAPI
- [x] Métriques : `requests_total`, `predictions_total`, `latency`
- [x] Compteurs par endpoint et niveau de risque
- [x] Histogrammes de latence (P50, P95, P99)

**Métriques exposées :**
```python
# Compteurs
credit_risk_requests_total{endpoint, method, status}
credit_risk_predictions_total{risk_level}

# Histogrammes
credit_risk_request_latency_seconds
credit_risk_prediction_latency_seconds

# Gauges
credit_risk_model_loaded
credit_risk_last_prediction_probability
```

### Étape 6.2 : Dashboard Grafana
- [x] Créer `monitoring/grafana/dashboards/credit_risk_dashboard.json`
- [x] 8 panels : stats, graphiques, pie chart
- [x] Rafraîchissement automatique (5s)
- [x] Couleurs par niveau de risque

### Étape 6.3 : DAG Airflow
- [x] Créer `airflow/dags/credit_risk_pipeline.py`
- [x] Task 1 : Vérification santé API
- [x] Task 2 : Test de prédiction
- [x] Task 3 : Collecte métriques
- [x] Task 4 : Génération rapport

**Structure du DAG :**
```python
check_api_health >> test_prediction >> collect_metrics >> generate_report
```

### Étape 6.4 : Docker Compose complet
- [x] PostgreSQL (base de données)
- [x] API FastAPI (backend)
- [x] Streamlit (frontend)
- [x] Prometheus (métriques)
- [x] Grafana (dashboards)
- [x] Airflow (orchestration)

**Commande de lancement :**
```bash
docker-compose up -d
```

**Validation Phase 6 :**
```bash
# Checklist de validation
[x] docker-compose up démarre tous les services
[x] Endpoint /metrics expose les métriques Prometheus
[x] DAG Airflow créé et documenté
[x] Dashboard Grafana avec 8 panels
[x] Toutes les interfaces accessibles (8000, 8501, 9090, 3000, 8080)
```

---

## PHASE 7 : FINALISATION & DÉPLOIEMENT

**Objectif :** Déployer publiquement et documenter

### Étape 7.1 : Documentation
- [x] README.md complet avec :
  - Description du projet
  - Architecture
  - Installation
  - Usage
  - Résultats
  - Screenshots (12 captures d'écran)
- [x] Profils réalistes multi-devises (FCFA, EUR, USD)
- [x] Données basées sur sources officielles (ANSD, BLS, Eurostat, AfricaPaieRH)
- [x] Docstrings dans le code
- [x] Commentaires pour les parties complexes

### Étape 7.2 : Déploiement Streamlit Cloud
- [ ] Créer le repo GitHub public
- [ ] Connecter à Streamlit Cloud
- [ ] Configurer les secrets
- [ ] Tester l'app déployée

### Étape 7.3 : Post LinkedIn
- [ ] Rédiger le post
- [ ] Screenshots/GIF de l'app
- [ ] Lien vers le repo et la démo
- [ ] Hashtags pertinents

**Validation Finale :**
```bash
# Checklist finale
[x] Repo GitHub public et propre
[x] README professionnel (français, captures, métriques)
[ ] App Streamlit accessible en ligne (Streamlit Cloud)
[x] docker-compose up fonctionne en local
[ ] Post LinkedIn publié
```

---

## SUIVI DE PROGRESSION

| Phase | Status | Date début | Date fin | Notes |
|-------|--------|------------|----------|-------|
| Phase 1 : Setup | ✅ Terminé | 25/01/2026 | 25/01/2026 | Structure, requirements, Docker configurés |
| Phase 2 : Data & EDA | ✅ Terminé | 25/01/2026 | 26/01/2026 | EDA ✅, PostgreSQL: 3.7M lignes chargées |
| Phase 3 : Feature Engineering | ✅ Terminé | 26/01/2026 | 26/01/2026 | 103 features créées, dataset 225 colonnes |
| Phase 4 : Modélisation | ✅ Terminé | 27/01/2026 | 27/01/2026 | AUC 0.7836, Optuna 50 trials, SHAP |
| Phase 5 : API & UI | ✅ Terminé | 27/01/2026 | 28/01/2026 | FastAPI + Streamlit + SHAP dynamique |
| Phase 6 : Orchestration | ✅ Terminé | 28/01/2026 | 28/01/2026 | Prometheus, Grafana, Airflow, Docker |
| Phase 7 : Déploiement | 🔄 En cours | 28/01/2026 | | README ✅, Captures ✅, GitHub à pousser |

**Légende :** ⬜ À faire | 🔄 En cours | ✅ Terminé | ❌ Bloqué

---

## NOTES ET DÉCISIONS

*(Espace pour noter les décisions prises et les changements de plan)*

| Date | Décision | Raison |
|------|----------|--------|
| 25/01/2026 | PostgreSQL comme BDD principale | Performance sur jointures, simulation production |
| 25/01/2026 | DuckDB en alternative si ressources limitées | Flexibilité |
| 25/01/2026 | scale_pos_weight pour déséquilibre | Ratio 1:11, SMOTE trop lourd sur 300k lignes |
| 25/01/2026 | EXT_SOURCE variables prioritaires | Corrélations les plus fortes (-0.18) |
| 25/01/2026 | Jupyter navigateur plutôt que VS Code | Problème extension Jupyter VS Code |
| 26/01/2026 | Approche hybride pour l'ingestion | Tables principales en PostgreSQL, grosses tables agrégées en Python |
| 26/01/2026 | Réduction chunk_size à 10000 | Éviter crash mémoire WSL (était 50000) |
| 26/01/2026 | PostgreSQL local (pas Docker) | Port 5432 déjà utilisé par PostgreSQL système |
| 27/01/2026 | Encodage catégorielles reporté à Phase 4 | XGBoost supporte `enable_categorical=True`, plus flexible |
| 27/01/2026 | Notebook pour Phase 4 (pas scripts) | Graphiques interactifs, SHAP plots, exploration |
| 27/01/2026 | Jupyter navigateur (pas VS Code) | Problème kernel VS Code, accès direct sans token |
| 27/01/2026 | Support multilingue FR/EN | Valorisation portfolio international |
| 27/01/2026 | Support multi-devises (EUR/USD/XAF/XOF) | Marchés Europe + Amérique + Afrique |
| 27/01/2026 | Seuils décision ajustés (40%/55%) | Calibrés sur comportement réel du modèle |
| 27/01/2026 | Profils démo calibrés empiriquement | Score externe domine (40% importance) |
| 27/01/2026 | Schémas Pydantic inline (pas schemas.py) | Simplicité, tout dans main.py |
| 28/01/2026 | Tests API avec pytest (31 tests) | Qualité code, CI/CD ready |
| 28/01/2026 | Endpoint /explain avec SHAP | Explicabilité individuelle des prédictions |
| 28/01/2026 | Visualisation SHAP dynamique | Nombre de facteurs adapté au profil (6-3, 4-4, 3-6) |
| 28/01/2026 | Traduction 40+ features | Interface compréhensible par tous (clients, analystes) |
| 28/01/2026 | Métriques Prometheus dans API | Endpoint /metrics pour monitoring |
| 28/01/2026 | Dashboard Grafana 8 panels | Visualisation temps réel des métriques |
| 28/01/2026 | DAG Airflow pipeline | Automatisation health check + prédiction + rapport |
| 28/01/2026 | SQLite pour Airflow (dev) | Simplicité, pas besoin de BDD séparée |
| 28/01/2026 | Python 3.12 dans Docker | SHAP 0.50.0 nécessite Python ≥ 3.11 |
| 28/01/2026 | SHAP 0.50.0 (upgrade) | Erreur "[5E-1]" avec version 0.49.x |
| 28/01/2026 | Airflow 3.1.6 standalone | Génère automatiquement le mot de passe admin |
| 28/01/2026 | API_URL via env variable | Streamlit dans Docker utilise `http://api:8000` |
| 28/01/2026 | README en français | Cible principale : marché francophone africain |
| 28/01/2026 | Profils réalistes par devise | Sources : ANSD, BLS, Eurostat, AfricaPaieRH |
| 28/01/2026 | XAF devise par défaut | Cohérence avec le contexte économique cible |
| 28/01/2026 | 12 captures d'écran | Démonstration des 3 profils (Fiable/Moyen/Risqué) |

---

**Document créé le :** Janvier 2026
**Dernière mise à jour :** 28 Janvier 2026 - Phase 7 en cours (README + Captures)

---

## VERSIONS TECHNIQUES FINALES

| Composant | Version | Notes |
|-----------|---------|-------|
| Python | 3.12.3 | Requis pour SHAP 0.50.0 |
| XGBoost | 3.1.3 | Modèle principal |
| SHAP | 0.50.0 | Explicabilité (nécessite Python ≥ 3.11) |
| FastAPI | 0.128.0 | API REST |
| Streamlit | 1.53.1 | Interface utilisateur |
| PostgreSQL | 15-alpine | Base de données |
| Prometheus | v2.47.0 | Collecte métriques |
| Grafana | 10.2.0 | Dashboards |
| Apache Airflow | 3.1.6 | Orchestration |
| Docker Compose | v2 | Commande : `docker compose` (sans tiret) |
