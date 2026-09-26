# Rapport d'Avancement - Credit Risk Scoring Pipeline

## Informations Projet

| Élément | Détail |
|---------|--------|
| **Projet** | Credit Risk Scoring Pipeline |
| **Auteur** | Daniela Samo |
| **Date début** | 25 Janvier 2026 |
| **Statut** | 🔄 En cours |

## Résumé Exécutif

Ce document trace l'avancement du projet, les décisions prises, les résultats obtenus et les problèmes rencontrés. Il sert de journal de bord et sera la base du rapport final.


# PHASE 1 : SETUP & ENVIRONNEMENT

**Statut :** ✅ Terminé | **Date :** 25/01/2026

## Réalisations

- [x] Structure du projet créée (arborescence complète)
- [x] Environnement virtuel Python configuré
- [x] Fichiers de configuration : `requirements.txt`, `config.yaml`, `.env.example`
- [x] Docker : `Dockerfile`, `docker-compose.yml` avec PostgreSQL, Prometheus, Grafana
- [x] Documentation initiale : étude projet, feuille de route

## Décisions prises

| Décision | Justification |
|----------|---------------|
| Python 3.12 | Version stable et performante |
| PostgreSQL pour le stockage | Performance sur jointures, simulation production |
| XGBoost comme algorithme principal | Performant sur données tabulaires, interprétable |

## Structure finale

```
Credit_Risk_Scoring_Project/
├── data/raw/processed/features/
├── notebooks/
├── src/data/features/models/utils/
├── api/
├── streamlit/
├── airflow/dags/
├── monitoring/
├── configs/
├── tests/
└── docs/
```


# PHASE 2 : DATA & EDA

**Statut :** ✅ Terminé | **Date :** 25-26/01/2026

## 2.1 Téléchargement des données

**Statut :** ✅ Terminé

### Source
- **Compétition :** [Home Credit Default Risk](https://www.kaggle.com/c/home-credit-default-risk)
- **Téléchargement :** API Kaggle
- **Taille totale :** 2.5 GB

### Fichiers obtenus

| Fichier | Taille | Description |
|---------|--------|-------------|
| `application_train.csv` | 159 MB | Table principale avec TARGET (307,511 lignes) |
| `application_test.csv` | 26 MB | Table test sans TARGET |
| `bureau.csv` | 163 MB | Historique crédit autres institutions |
| `bureau_balance.csv` | 359 MB | Soldes mensuels bureau |
| `previous_application.csv` | 387 MB | Demandes précédentes Home Credit |
| `POS_CASH_balance.csv` | 375 MB | Soldes POS/Cash |
| `credit_card_balance.csv` | 405 MB | Soldes cartes de crédit |
| `installments_payments.csv` | 690 MB | Historique paiements |
| `HomeCredit_columns_description.csv` | 37 KB | Description des colonnes |
| `sample_submission.csv` | 524 KB | Format soumission Kaggle |

## 2.2 Exploration initiale (EDA)

**Statut :** ✅ Terminé | **Date :** 25/01/2026

### Données chargées

- **307,511 clients** dans application_train
- **122 variables** : 104 numériques + 16 catégorielles + 2 (ID, TARGET)
- **Mémoire** : 286.2 MB

### Variable cible (TARGET)

| Classe | Nombre | Pourcentage |
|--------|--------|-------------|
| 0 (Pas de défaut) | 282,686 | 91.93% |
| 1 (Défaut) | 24,825 | 8.07% |

**Constat :** Déséquilibre de classes important (ratio 1:11)

**Action retenue :** Utiliser `scale_pos_weight` dans XGBoost (ratio ~11)

### Valeurs manquantes

| Catégorie | Nombre de colonnes |
|-----------|-------------------|
| Sans valeurs manquantes | 55 |
| < 10% manquantes | 10 |
| 10-50% manquantes | 16 |
| > 50% manquantes | 41 |

**Variables les plus problématiques (>65% manquantes) :**
- COMMONAREA_AVG/MODE/MEDI (~70%)
- NONLIVINGAPARTMENTS (~69%)
- LIVINGAPARTMENTS (~68%)
- OWN_CAR_AGE (~66%)

**Action retenue :** Imputation par médiane ou valeur spéciale (-999), évaluer suppression des colonnes >70%

### Corrélations avec TARGET

**Top corrélations négatives (réduisent le risque) :**
1. EXT_SOURCE_3 : **-0.179** (score externe le plus prédictif)
2. EXT_SOURCE_2 : **-0.160**
3. EXT_SOURCE_1 : **-0.155**

**Top corrélations positives (augmentent le risque) :**
1. DAYS_BIRTH : **+0.078** (clients plus jeunes = plus de défauts)
2. REGION_RATING_CLIENT_W_CITY : **+0.061**
3. REGION_RATING_CLIENT : **+0.059**

**Observation clé :** Les variables EXT_SOURCE (scores externes) sont les plus prédictives. À investiguer leur origine.

### Insights métier

| Variable | Observation | Données |
|----------|-------------|---------|
| **Genre** | Hommes plus risqués que femmes | M: 10.14% vs F: 6.99% |
| **Type de contrat** | Cash loans plus risqués | Cash: 8.35% vs Revolving: 5.48% |
| **Éducation** | Éducation faible = plus de risque | Lower secondary: 10.93% vs Higher: 5.36% |
| **Âge** | Jeunes plus risqués | 20-30 ans: ~11% vs 60-70 ans: ~5% |

### Tables secondaires identifiées

| Table | Lignes | Colonnes | Clé de jointure |
|-------|--------|----------|-----------------|
| bureau | 1,716,428 | 17 | SK_ID_CURR |
| bureau_balance | 27,299,925 | 3 | SK_ID_BUREAU |
| previous_application | 1,670,214 | 37 | SK_ID_CURR |
| POS_CASH_balance | 10,001,358 | 8 | SK_ID_CURR |
| credit_card_balance | 3,840,312 | 23 | SK_ID_CURR |
| installments_payments | 13,605,401 | 8 | SK_ID_CURR |

## 2.3 Chargement en base de données

**Statut :** ✅ Terminé | **Date :** 26/01/2026

### Approche hybride adoptée

| Données | Stockage | Raison |
|---------|----------|--------|
| application_train | PostgreSQL | Table principale |
| bureau | PostgreSQL | Requêtes SQL d'agrégation |
| previous_application | PostgreSQL | Requêtes SQL d'agrégation |
| installments_payments | CSV | Trop gros (690 MB), agrégation Python |
| POS_CASH_balance | CSV | Trop gros, agrégation Python |
| credit_card_balance | CSV | Trop gros, agrégation Python |

### Données chargées dans PostgreSQL

| Table | Lignes |
|-------|--------|
| application_train | 307,511 |
| bureau | 1,716,428 |
| previous_application | 1,670,214 |
| **Total** | **3,694,153** |

### Décisions techniques

- `chunk_size = 10000` pour éviter crash mémoire WSL
- PostgreSQL local (pas Docker) - port 5432 déjà utilisé
- Script : `src/data/ingestion.py`


# PHASE 3 : FEATURE ENGINEERING

**Statut :** ✅ Terminé | **Date :** 26/01/2026

## 3.1 Scripts créés

| Script | Rôle |
|--------|------|
| `src/data/preprocessing.py` | Nettoyage, imputation, outliers |
| `src/features/build_features.py` | Agrégation, création features, assemblage |

## 3.2 Features créées

| Source | Nb features | Exemples |
|--------|-------------|----------|
| application | 16 | credit_income_ratio, age_years, ext_source_mean |
| bureau | 18 | bureau_credit_count, bureau_debt_sum, bureau_active_ratio |
| previous_application | 18 | prev_app_count, prev_approval_rate |
| installments | 13 | instal_late_count, instal_payment_ratio |
| pos_cash | 17 | pos_dpd_count, pos_dpd_ratio |
| credit_card | 21 | cc_utilization_mean, cc_over_limit_count |
| **Total nouvelles** | **103** | |

## 3.3 Dataset final

| Métrique | Valeur |
|----------|--------|
| Lignes | 307,511 |
| Colonnes | 225 |
| Taille fichier | 452.3 MB |
| Emplacement | `data/features/features_v1.csv` |

## 3.4 Traitement des valeurs manquantes

- Features count/sum : remplis avec **0** (pas d'historique = 0)
- Autres features : remplis avec **médiane**


# PHASE 4 : MODÉLISATION

**Statut :** ✅ Terminé | **Date :** 27/01/2026

## 4.1 Chargement du dataset de features

**Statut :** ✅ Terminé

### Dataset chargé

| Métrique | Valeur |
|----------|--------|
| Source | `data/features/features_v1.csv` |
| Lignes | 307,511 |
| Colonnes | 225 |
| Mémoire | 746.6 MB |

### Distribution TARGET (confirmée)

| Classe | Nombre | Pourcentage |
|--------|--------|-------------|
| 0 (Pas de défaut) | 282,686 | 91.93% |
| 1 (Défaut) | 24,825 | 8.07% |

**Ratio classe (neg/pos) :** 11.4 → utilisé pour `scale_pos_weight`

## 4.2 Préparation des données

**Statut :** ✅ Terminé

### Types de colonnes identifiés

| Type | Nombre |
|------|--------|
| Catégorielles (object) | 16 |
| Numériques | 207 |
| ID + Target | 2 |

### Cardinalité des variables catégorielles

| Variable | Valeurs uniques | Traitement |
|----------|-----------------|------------|
| organization_type | 58 | LabelEncoder |
| occupation_type | 18 | LabelEncoder |
| name_income_type | 8 | LabelEncoder |
| name_type_suite | 7 | LabelEncoder |
| wallsmaterial_mode | 7 | LabelEncoder |
| weekday_appr_process_start | 7 | LabelEncoder |
| ... (10 autres) | 2-6 | LabelEncoder |

**Choix technique :** LabelEncoder plutôt que One-Hot car :
- `organization_type` a 58 valeurs → One-Hot créerait 58 colonnes
- XGBoost gère bien les encodages ordinaux
- Réduit la dimensionnalité

### Features finales pour modélisation

| Métrique | Valeur |
|----------|--------|
| X shape | (307,511 × 223) |
| Colonnes exclues | sk_id_curr (ID), target |

## 4.3 Split Train / Validation / Test

**Statut :** ✅ Terminé

### Répartition

| Set | Lignes | Pourcentage | Usage |
|-----|--------|-------------|-------|
| Train | 215,257 | 70% | Entraînement du modèle |
| Validation | 46,127 | 15% | Tuning hyperparamètres |
| Test | 46,127 | 15% | Évaluation finale (jamais vu) |

### Vérification stratification

| Set | Ratio défaut |
|-----|--------------|
| Train | 8.07% |
| Validation | 8.07% |
| Test | 8.07% |

**Observation :** La stratification (`stratify=y`) garantit que chaque set a la même distribution de la cible. C'est critique pour un dataset déséquilibré.

## 4.4 Baseline Model

**Statut :** ✅ Terminé

### Paramètres du baseline

| Paramètre | Valeur | Justification |
|-----------|--------|---------------|
| n_estimators | 100 | Standard, point de départ |
| max_depth | 6 | Défaut XGBoost |
| learning_rate | 0.1 | Compromis vitesse/précision |
| scale_pos_weight | 11.39 | Corrige le déséquilibre (ratio classes) |
| random_state | 42 | Reproductibilité |
| eval_metric | 'auc' | Correspond à notre objectif |

### Résultats Baseline (Validation Set)

| Métrique | Valeur | Objectif | Statut |
|----------|--------|----------|--------|
| **AUC-ROC** | **0.7778** | > 0.75 | ✅ Atteint |
| **Gini** | **0.5556** | > 0.50 | ✅ Atteint |

### Interprétation des résultats baseline

**AUC-ROC = 0.7778 signifie :**
- Le modèle a **77.78% de chances** de classer correctement un client défaillant au-dessus d'un client sain
- C'est un score **bon** pour un baseline sans optimisation
- Comparable aux solutions Kaggle de niveau intermédiaire

**Gini = 0.5556 (formule : 2×AUC - 1) :**
- Mesure la capacité discriminante sur une échelle 0-1
- 0 = modèle aléatoire, 1 = modèle parfait
- 0.55 = bonne discrimination

**Ce que ça révèle sur les features :**
- Les 103 features créées en Phase 3 sont **prédictives**
- Le `scale_pos_weight=11.39` gère correctement le déséquilibre
- Marge d'amélioration avec Optuna : +1-3% attendu

## 4.5 Optimisation Hyperparamètres (Optuna)

**Statut :** ✅ Terminé

### Configuration Optuna

| Paramètre | Valeur |
|-----------|--------|
| Nombre de trials | 50 |
| Sampler | TPE (Tree-structured Parzen Estimator) |
| Direction | Maximiser AUC |
| Seed | 42 |
| Persistance | SQLite (`models/optuna_study.db`) |

### Plages de recherche

| Hyperparamètre | Plage | Rôle |
|----------------|-------|------|
| n_estimators | 100-500 | Nombre d'arbres |
| max_depth | 3-10 | Profondeur (contrôle overfitting) |
| learning_rate | 0.01-0.3 | Vitesse apprentissage |
| min_child_weight | 1-10 | Régularisation splits |
| subsample | 0.6-1.0 | % lignes par arbre |
| colsample_bytree | 0.6-1.0 | % features par arbre |
| gamma | 0-5 | Seuil minimum gain |
| reg_alpha | 0-10 | Régularisation L1 |
| reg_lambda | 0-10 | Régularisation L2 |

### Résultats Optuna

**Statut :** ✅ Terminé | **Durée :** ~15 minutes (50 trials)

| Métrique | Valeur |
|----------|--------|
| Meilleur AUC | **0.7836** |
| Meilleur trial | Trial 25 |
| Amélioration vs baseline | **+0.58%** |

### Meilleurs paramètres trouvés

| Paramètre | Valeur Baseline | Valeur Optuna | Changement |
|-----------|-----------------|---------------|------------|
| n_estimators | 100 | **475** | ↑ Plus d'arbres |
| max_depth | 6 | **3** | ↓ Arbres simples |
| learning_rate | 0.1 | **0.075** | ↓ Plus lent |
| min_child_weight | 1 | **3** | ↑ Régularisation |
| subsample | 1.0 | **0.79** | ↓ Sous-échantillonnage |
| colsample_bytree | 1.0 | **0.88** | ↓ Sous-échantillonnage features |
| gamma | 0 | **2.98** | ↑ Régularisation forte |
| reg_alpha | 0 | **3.76** | ↑ L1 regularization |
| reg_lambda | 1 | **6.39** | ↑ L2 regularization |

### Interprétation des paramètres optimaux

**Pattern découvert : "Beaucoup d'arbres simples avec forte régularisation"**

1. **max_depth=3** (vs 6) : Arbres peu profonds généralisent mieux, évitent l'overfitting
2. **n_estimators=475** (vs 100) : Compense la simplicité par le nombre
3. **Forte régularisation** (gamma, reg_alpha, reg_lambda) : Pénalise la complexité
4. **Sous-échantillonnage** (subsample=0.79, colsample=0.88) : Diversifie les arbres, réduit la variance

**Conclusion :** Le modèle optimal privilégie la généralisation à la performance brute sur le train set.

## 4.6 Modèle Final

**Statut :** ✅ Terminé

Le modèle final a été entraîné avec les meilleurs paramètres Optuna sur le train set complet (215,257 lignes).

## 4.7 Évaluation Finale (Test Set)

**Statut :** ✅ Terminé

### Métriques principales

| Métrique | Objectif | Résultat | Statut |
|----------|----------|----------|--------|
| **AUC-ROC** | > 0.75 | **0.7836** | ✅ Atteint |
| **Gini** | > 0.50 | **0.5673** | ✅ Atteint |
| **Recall** | > 0.60 | **0.6998** | ✅ Atteint |
| Precision | - | 0.1862 | Attendu |
| F1-Score | - | 0.2941 | Attendu |
| Accuracy | - | 0.73 | - |

### Matrice de confusion

```
                      Prédit
                 Non-défaut   Défaut
Réel  Non-défaut   30,954     11,449   (73% correct)
      Défaut        1,117      2,607   (70% détectés)
```

### Classification Report

| Classe | Precision | Recall | F1-Score | Support |
|--------|-----------|--------|----------|---------|
| Pas de défaut | 0.97 | 0.73 | 0.83 | 42,403 |
| Défaut | 0.19 | 0.70 | 0.29 | 3,724 |

### Interprétation métier

**Performance du modèle :**

1. **Détection des défauts (Recall = 70%)** ✅
   - Sur 100 clients qui feront défaut, le modèle en détecte 70
   - 30% de défauts passent entre les mailles (faux négatifs)
   - C'est un bon score pour un modèle de crédit

2. **Fausses alertes (Precision = 19%)**
   - Sur 100 clients flaggés "à risque", 19 feront vraiment défaut
   - 81% sont des fausses alertes
   - **C'est attendu** avec un déséquilibre 1:11 et un seuil de 0.5

3. **Trade-off bancaire**
   - Le modèle favorise la détection (recall élevé) au prix de faux positifs
   - En production : vérification humaine des alertes recommandée
   - Alternative : ajuster le seuil de décision selon le coût métier

**Pourquoi l'AUC Test = AUC Validation ?**

Le fait que l'AUC soit identique (0.7836) sur validation et test est **une bonne nouvelle** :
- Pas d'overfitting sur le validation set
- Le modèle généralise bien aux données inconnues
- Les paramètres Optuna sont robustes

## 4.8 Explicabilité SHAP

**Statut :** ✅ Terminé

### Top 10 Features (Importance SHAP)

| Rang | Feature | Importance | Interprétation |
|------|---------|------------|----------------|
| 1 | **ext_source_mean** | 0.4042 | Moyenne des scores externes - **le plus prédictif** |
| 2 | **code_gender** | 0.1287 | Genre du client |
| 3 | **goods_credit_ratio** | 0.1140 | Ratio prix bien / crédit demandé |
| 4 | **amt_annuity** | 0.1117 | Montant de l'annuité |
| 5 | **credit_annuity_ratio** | 0.1100 | Ratio crédit / annuité (durée implicite) |
| 6 | **instal_late_ratio** | 0.0980 | Ratio paiements en retard |
| 7 | **name_education_type** | 0.0922 | Niveau d'éducation |
| 8 | **ext_source_max** | 0.0870 | Score externe maximum |
| 9 | **ext_source_min** | 0.0818 | Score externe minimum |
| 10 | **instal_payment_ratio** | 0.0803 | Ratio montant payé / dû |

### Analyse des features importantes

**1. Variables EXT_SOURCE (Rang 1, 8, 9)**

Les scores externes dominent la prédiction :
- `ext_source_mean` seul contribue à 40% de l'importance
- Ces scores proviennent de bureaux de crédit externes
- **Insight métier :** L'historique crédit externe est le meilleur prédicteur

**2. Variables comportementales (Rang 6, 10)**

- `instal_late_ratio` : Historique de retards de paiement
- `instal_payment_ratio` : Comportement de remboursement
- **Insight métier :** Le comportement passé prédit le comportement futur

**3. Variables financières (Rang 3, 4, 5)**

- Ratios financiers créés en Phase 3
- Mesurent la capacité de remboursement
- **Insight métier :** L'adéquation crédit/revenus est critique

**4. Variables démographiques (Rang 2, 7)**

- Genre et éducation influencent le risque
- **Attention :** Ces variables peuvent poser des questions éthiques (discrimination)
- En production : évaluer l'impact sur l'équité du modèle

### Graphiques SHAP générés

| Fichier | Description |
|---------|-------------|
| `models/shap_importance.png` | Bar chart des 20 features les plus importantes |
| `models/shap_summary.png` | Impact directionnel de chaque feature |

## 4.9 Fichiers générés

**Statut :** ✅ Terminé

### Modèle et artefacts

| Fichier | Description | Taille |
|---------|-------------|--------|
| `models/xgboost_credit_risk_v1.pkl` | Modèle XGBoost entraîné | ~2 MB |
| `models/feature_names.json` | Liste des 223 features | ~8 KB |
| `models/label_encoders.pkl` | 16 encodeurs catégoriels | ~50 KB |
| `models/metrics.json` | Métriques et best_params | ~2 KB |
| `models/optuna_study.db` | Base SQLite Optuna (50 trials) | ~200 KB |

### Visualisations

| Fichier | Description |
|---------|-------------|
| `models/confusion_matrix.png` | Matrice de confusion |
| `models/roc_curve.png` | Courbe ROC (AUC = 0.7836) |
| `models/precision_recall_curve.png` | Courbe Precision-Recall |
| `models/shap_importance.png` | Feature importance SHAP |
| `models/shap_summary.png` | Summary plot SHAP |

## 4.10 Résumé Phase 4

### Objectifs vs Résultats

| Objectif | Cible | Résultat | Statut |
|----------|-------|----------|--------|
| AUC-ROC | > 0.75 | **0.7836** | ✅ +4.5% au-dessus |
| Gini | > 0.50 | **0.5673** | ✅ +13.5% au-dessus |
| Recall (défauts) | > 0.60 | **0.6998** | ✅ +16.6% au-dessus |

### Amélioration apportée par Optuna

| Métrique | Baseline | Final | Gain |
|----------|----------|-------|------|
| AUC | 0.7778 | 0.7836 | +0.58% |

### Décisions techniques validées

| Décision | Résultat |
|----------|----------|
| LabelEncoder pour catégorielles | ✅ Fonctionne bien avec XGBoost |
| scale_pos_weight=11.39 | ✅ Bon recall (70%) |
| Split 70/15/15 stratifié | ✅ Pas d'overfitting |
| Optuna 50 trials + SQLite | ✅ Optimisation efficace et persistante |

### Leçons apprises

1. **Les features EXT_SOURCE sont dominantes** : 40% de l'importance totale
2. **Arbres simples > arbres profonds** : max_depth=3 optimal
3. **La régularisation est cruciale** : évite l'overfitting sur dataset déséquilibré
4. **Le baseline était déjà bon** : les 103 features créées en Phase 3 sont de qualité


# PHASE 5 : API & INTERFACE

**Statut :** ✅ Terminé | **Date :** 27-28/01/2026

## 5.1 API FastAPI

**Statut :** ✅ Terminé

### Fichier créé

`api/main.py` - API REST complète pour le scoring crédit

### Endpoints implémentés

| Endpoint | Méthode | Description | Statut |
|----------|---------|-------------|--------|
| `/` | GET | Page d'accueil avec liste des endpoints | ✅ |
| `/health` | GET | Santé de l'API et version du modèle | ✅ |
| `/predict` | POST | Prédiction du risque de défaut | ✅ |
| `/explain` | POST | Explicabilité SHAP individuelle | ✅ |
| `/docs` | GET | Documentation Swagger automatique | ✅ |

### Schémas Pydantic (intégrés dans main.py)

| Schéma | Usage |
|--------|-------|
| `ClientData` | Validation des données client en entrée |
| `PredictionResponse` | Format de réponse standardisé |
| `ExplainResponse` | Réponse avec facteurs SHAP |
| `FeatureImpact` | Détail d'un facteur (feature, value, shap_value, impact) |
| `HealthResponse` | Statut de l'API |

### Réponse `/predict`

```json
{
  "probability": 0.365,
  "prediction": 0,
  "risk_level": "Faible",
  "score": 649
}
```

### Réponse `/explain`

```json
{
  "probability": 0.365,
  "base_probability": 0.08,
  "risk_level": "Faible",
  "top_risk_factors": [
    {"feature": "credit_income_ratio", "value": 2.0, "shap_value": 0.12, "impact": "increases_risk"}
  ],
  "top_protective_factors": [
    {"feature": "ext_source_mean", "value": 0.92, "shap_value": -0.45, "impact": "reduces_risk"}
  ]
}
```

### Artefacts chargés au démarrage

| Fichier | Usage |
|---------|-------|
| `xgboost_credit_risk_v1.pkl` | Modèle XGBoost |
| `feature_names.json` | Liste des 223 features |
| `label_encoders.pkl` | Encodeurs catégoriels |
| `metrics.json` | Métriques du modèle |

### Lancement

```bash
cd api
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 5.2 Interface Streamlit

**Statut :** ✅ Terminé

### Fichier créé

`streamlit/app.py` - Interface web complète et professionnelle

### Fonctionnalités implémentées

| Fonctionnalité | Description | Statut |
|----------------|-------------|--------|
| **Multilingue** | Français et Anglais | ✅ Bonus |
| **Multi-devises** | EUR, USD, XAF (CEMAC), XOF (UEMOA) | ✅ Bonus |
| **Formulaire** | Saisie des données client | ✅ |
| **Profils exemples** | 3 profils pré-calibrés | ✅ |
| **Résultats visuels** | Score, probabilité, décision | ✅ |
| **Indicateur risque** | Barre de progression avec légende | ✅ |
| **Facteurs clés** | Points positifs / Points d'attention | ✅ |
| **Détails techniques** | JSON brut de l'API | ✅ |

### Support multi-devises

| Devise | Taux vs EUR | Zone |
|--------|-------------|------|
| EUR | 1.00 | Europe |
| USD | 1.08 | Amérique |
| XAF | 655.957 | Afrique Centrale (CEMAC) |
| XOF | 655.957 | Afrique de l'Ouest (UEMOA) |

**Note :** Les montants sont convertis en EUR avant envoi à l'API, garantissant des prédictions cohérentes quelle que soit la devise affichée.

### Profils de démonstration calibrés

**Profils adaptés par zone économique** (recherche économique SMIG/SMIC) :

| Zone | Devise | Revenu "Fiable" | Revenu "Moyen" | Revenu "Risqué" |
|------|--------|-----------------|----------------|-----------------|
| CEMAC | XAF | 14.4M FCFA/an | 6M FCFA/an | 1.2M FCFA/an |
| UEMOA | XOF | 11.2M FCFA/an | 4.8M FCFA/an | 996K FCFA/an |
| Europe | EUR | 72 000 €/an | 36 000 €/an | 14 400 €/an |
| USA | USD | 156 000 $/an | 62 000 $/an | 31 200 $/an |

**Calibration des scores (identique toutes devises)** :

| Profil | Score externe | Ancienneté | Probabilité | Décision |
|--------|---------------|------------|-------------|----------|
| **Fiable** | 0.85 | 15 ans | **30.3%** | ✅ Crédit recommandé |
| **Moyen** | 0.62 | 4 ans | **52.0%** | ⚠️ Étude approfondie |
| **Risqué** | 0.15 | 0 an | **77.3%** | ❌ Crédit déconseillé |

**Note :** La devise par défaut est XAF (zone CEMAC) pour refléter le contexte économique africain.

### Seuils de décision

| Probabilité | Décision | Couleur |
|-------------|----------|---------|
| < 40% | ✅ Crédit recommandé | Vert |
| 40% - 55% | ⚠️ Étude approfondie | Orange |
| > 55% | ❌ Crédit déconseillé | Rouge |

### Lancement

```bash
streamlit run streamlit/app.py
```

## 5.3 Tests API

**Statut :** ✅ Terminé | **Date :** 28/01/2026

### Fichier créé

`tests/test_api.py` - Suite de tests complète pour l'API

### Exécution

```bash
pytest tests/test_api.py -v
```

### Résultats : 31/31 PASSED ✅

| Catégorie | Tests | Passés | Description |
|-----------|-------|--------|-------------|
| Root Endpoint | 2 | ✅ 2 | Page d'accueil API |
| Health Endpoint | 5 | ✅ 5 | Santé et état du modèle |
| Predict Endpoint | 8 | ✅ 8 | Prédictions et formats |
| Input Validation | 3 | ✅ 3 | Validation des données |
| Business Logic | 2 | ✅ 2 | Cohérence métier |
| Explain Endpoint | 8 | ✅ 8 | SHAP values et facteurs |
| Performance | 3 | ✅ 3 | Latence predict < 500ms, explain < 2s |
| **TOTAL** | **31** | **✅ 31** | **100% succès** |

### Tests clés

| Test | Ce qu'il vérifie |
|------|------------------|
| `test_health_model_loaded` | Modèle XGBoost chargé en mémoire |
| `test_predict_returns_probability` | Probabilité entre 0 et 1 |
| `test_predict_returns_score` | Score crédit entre 300 et 850 |
| `test_higher_ext_source_lower_risk` | Score externe ↑ = Risque ↓ |
| `test_reliable_client_low_probability` | Client fiable → probabilité < 50% |
| `test_risky_client_high_probability` | Client risqué → probabilité > 50% |
| `test_predict_latency` | Réponse en < 500ms |
| `test_explain_returns_risk_factors` | Facteurs de risque retournés |
| `test_explain_risk_factors_have_positive_shap` | SHAP > 0 pour facteurs de risque |
| `test_explain_protective_factors_have_negative_shap` | SHAP < 0 pour facteurs protecteurs |

### Couverture des tests

- **Endpoints** : `/`, `/health`, `/predict`, `/explain` testés
- **Validation** : Champs manquants, types invalides
- **Logique métier** : Cohérence des prédictions
- **Explicabilité** : SHAP values cohérents (positif = risque, négatif = protection)
- **Performance** : Latence mesurée

## 5.4 Architecture Phase 5

```
┌─────────────────┐     HTTP/JSON      ┌─────────────────┐
│   STREAMLIT     │ ◄────────────────► │    FASTAPI      │
│   (Frontend)    │                    │    (Backend)    │
│   Port 8501     │                    │    Port 8000    │
└─────────────────┘                    └────────┬────────┘
                                                │
                                                ▼
                                       ┌─────────────────┐
                                       │  XGBoost Model  │
                                       │  (223 features) │
                                       └─────────────────┘
```

## 5.5 Captures d'écran

**12 captures d'écran ajoutées dans `docs/images/`** :

| Fichier | Description |
|---------|-------------|
| `profil_fiable_1.png` | Formulaire - Client cadre supérieur (fiable) |
| `profil_fiable_2.png` | Résultat - Score 683/850, Risque 30.3% ✅ |
| `profil_moyen_1.png` | Formulaire - Client cadre moyen |
| `profil_moyen_2.png` | Résultat - Score 563/850, Risque 52.0% ⚠️ |
| `profil_risque_1.png` | Formulaire - Client débutant (risqué) |
| `profil_risque_2.png` | Résultat - Score 424/850, Risque 77.3% ❌ |
| + 6 autres captures | Détails SHAP et interface |

## 5.6 Éléments bonus implémentés

| Élément | Description | Statut |
|---------|-------------|--------|
| Endpoint `/explain` | SHAP values individuelles avec facteurs de risque/protection | ✅ Implémenté |
| Support multilingue | Français et Anglais | ✅ Implémenté |
| Support multi-devises | EUR, USD, XAF, XOF | ✅ Implémenté |
| **Visualisation SHAP Streamlit** | Interface moderne avec cards dynamiques | ✅ Implémenté |

## 5.7 Visualisation SHAP - Détails

**Statut :** ✅ Terminé | **Date :** 28/01/2026

### Fonctionnalités implémentées

| Fonctionnalité | Description |
|----------------|-------------|
| **Cards modernes** | Design avec dégradés, ombres, coins arrondis |
| **Noms compréhensibles** | 40+ features traduites (ex: `ext_source_mean` → "Historique de crédit") |
| **Descriptions contextuelles** | Explications sous chaque facteur important |
| **Barres d'impact** | Visualisation de l'intensité de chaque facteur |
| **Badges d'impact** | "Impact fort", "Impact modéré", "Impact faible" |
| **Filtrage dynamique** | Nombre de facteurs adapté au profil du client |
| **Recommandations** | Message personnalisé selon le niveau de risque |

### Logique de filtrage dynamique

| Profil | Probabilité | Max Atouts | Max Vigilances |
|--------|-------------|------------|----------------|
| Fiable | < 40% | 6 | 3 |
| Moyen | 40-55% | 4 | 4 |
| Risqué | > 55% | 3 | 6 |

### Résultats des tests

| Profil | Probabilité | Atouts affichés | Vigilances affichées |
|--------|-------------|-----------------|----------------------|
| Fiable | 36.0% | 6 | 3 |
| Moyen | 40.5% | 4 | 4 |
| Risqué | 81.3% | 3 | 6 |

### Principe de conception

L'interface a été conçue pour être **compréhensible par tous** :
- Clients lambda
- Analystes crédit
- Régulateurs

Pas de jargon technique, pas de valeurs SHAP brutes - uniquement des explications claires et actionnables.

## 5.7 Validation Phase 5

```bash
# Checklist de validation
[x] API démarre sans erreur
[x] curl localhost:8000/health retourne "healthy"
[x] curl localhost:8000/predict fonctionne avec données JSON
[x] Streamlit s'affiche correctement
[x] Les 3 profils donnent des résultats cohérents
[x] Multi-devises fonctionne (EUR = XAF en probabilité)
[x] Multilingue FR/EN fonctionne
[x] pytest tests/test_api.py → 31/31 PASSED ✅
[x] Endpoint /explain fonctionne avec SHAP values
```

## 5.8 Leçons apprises Phase 5

1. **Calibration des profils de démo est critique** - Les premiers profils donnaient des résultats incohérents. Il a fallu ajuster les valeurs pour que Fiable < Moyen < Risqué en probabilité.

2. **Le score externe domine la prédiction** - Avec 40% d'importance, un changement de 0.45 à 0.72 fait passer de 70% à 40% de probabilité.

3. **Conversion devises bidirectionnelle** - Afficher en devise locale mais calculer en EUR garantit la cohérence des prédictions.

4. **Session state Streamlit** - Les callbacks `on_click` doivent modifier le state AVANT la création des widgets pour éviter les erreurs.


# PHASE 6 : ORCHESTRATION & MONITORING

**Statut :** ✅ Terminé | **Date :** 28/01/2026

## 6.1 Vue d'ensemble

La Phase 6 ajoute une couche de **monitoring et orchestration** au système de scoring crédit :

```
┌─────────────────────────────────────────────────────────────────────┐
│                        ARCHITECTURE PHASE 6                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────┐     ┌─────────┐     ┌─────────────┐                  │
│   │Streamlit│────►│   API   │────►│  PostgreSQL │                  │
│   │  :8501  │     │  :8000  │     │   :5432     │                  │
│   └─────────┘     └────┬────┘     └─────────────┘                  │
│                        │                                            │
│                        │ /metrics                                   │
│                        ▼                                            │
│   ┌─────────────────────────────────────────────────────────┐      │
│   │                    PROMETHEUS :9090                      │      │
│   │  Collecte les métriques toutes les 15 secondes          │      │
│   │  • Combien de requêtes ? (Counter)                      │      │
│   │  • Quelle latence ? (Histogram → P50, P95, P99)         │      │
│   │  • Le modèle est-il chargé ? (Gauge)                    │      │
│   └───────────────────────┬─────────────────────────────────┘      │
│                           │                                         │
│                           ▼                                         │
│   ┌─────────────────────────────────────────────────────────┐      │
│   │                     GRAFANA :3000                        │      │
│   │  Affiche les métriques sous forme de graphiques         │      │
│   │  • Tableaux de bord visuels                             │      │
│   │  • Alertes configurables                                │      │
│   └─────────────────────────────────────────────────────────┘      │
│                                                                     │
│   ┌─────────────────────────────────────────────────────────┐      │
│   │                     AIRFLOW :8080                        │      │
│   │  Exécute automatiquement des tâches planifiées          │      │
│   │  • Vérification santé API (toutes les heures)           │      │
│   │  • Tests automatiques                                   │      │
│   │  • Collecte de rapports                                 │      │
│   └─────────────────────────────────────────────────────────┘      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## 6.2 Métriques Prometheus - Explications détaillées

### Qu'est-ce que Prometheus ?

**Prometheus** est un système de surveillance qui :
1. **Collecte** des données de l'API toutes les 15 secondes
2. **Stocke** ces données dans une base temporelle
3. **Permet de requêter** ces données pour créer des graphiques

### Les 3 types de métriques

#### 1. Counter (Compteur) - "Combien ?"

Un compteur ne fait qu'**augmenter**. Il compte le nombre total d'événements.

| Métrique | Ce qu'elle compte | Exemple d'utilisation |
|----------|-------------------|----------------------|
| `credit_risk_requests_total` | Nombre de requêtes reçues par l'API | "L'API a reçu 1,247 requêtes depuis le démarrage" |
| `credit_risk_predictions_total` | Nombre de prédictions par niveau de risque | "Il y a eu 89 prédictions 'Moyen' et 14 prédictions 'Élevé'" |

**Comment lire un Counter dans Grafana :**
- La valeur brute (ex: 1,247) = total depuis le démarrage
- Le "rate" ou "increase" = combien par seconde/minute (plus utile)

#### 2. Histogram (Histogramme) - "Combien de temps ?"

Un histogramme mesure la **distribution des durées**. Il permet de calculer les **percentiles**.

| Métrique | Ce qu'elle mesure | Exemple |
|----------|-------------------|---------|
| `credit_risk_request_latency_seconds` | Temps de réponse de l'API | "La requête a pris 0.045 secondes" |
| `credit_risk_prediction_latency_seconds` | Temps de calcul du modèle | "La prédiction a pris 0.012 secondes" |

#### 3. Gauge (Jauge) - "Quelle valeur maintenant ?"

Une jauge peut **monter ou descendre**. Elle représente une valeur à un instant T.

| Métrique | Ce qu'elle représente | Valeurs possibles |
|----------|----------------------|-------------------|
| `credit_risk_model_loaded` | Le modèle est-il chargé ? | 1 = Oui, 0 = Non |
| `credit_risk_last_prediction_probability` | Dernière probabilité calculée | 0.00 à 1.00 (ex: 0.45 = 45%) |

### Comprendre les Percentiles (P50, P95, P99)

**⭐ EXPLICATION SIMPLE DES PERCENTILES ⭐**

Imaginez que vous mesurez le temps de réponse de 100 requêtes et que vous les triez de la plus rapide à la plus lente :

```
Requête #1:   0.010s  ← La plus rapide
Requête #2:   0.011s
Requête #3:   0.012s
...
Requête #50:  0.045s  ← P50 (Médiane) : 50% des requêtes sont plus rapides
...
Requête #95:  0.120s  ← P95 : 95% des requêtes sont plus rapides
...
Requête #99:  0.350s  ← P99 : 99% des requêtes sont plus rapides
Requête #100: 0.500s  ← La plus lente
```

| Percentile | Signification | Utilité |
|------------|---------------|---------|
| **P50 (Médiane)** | 50% des requêtes sont plus rapides que cette valeur | Performance "normale" |
| **P95** | 95% des requêtes sont plus rapides | Performance "quasi-pire cas" |
| **P99** | 99% des requêtes sont plus rapides | Performance du pire cas (hors extrêmes) |

**Pourquoi P95 et P99 sont importants ?**

- **P50 = 45ms** → La moitié des utilisateurs attendent moins de 45ms ✅
- **P95 = 120ms** → 5% des utilisateurs attendent plus de 120ms ⚠️
- **P99 = 350ms** → 1% des utilisateurs attendent plus de 350ms ⚠️

En production, on surveille P95 et P99 car :
- Les utilisateurs "malchanceux" ont une mauvaise expérience
- Un P99 élevé peut indiquer un problème (ex: garbage collection, base de données lente)

**Exemple concret pour ce projet :**

| Métrique | Valeur observée | Interprétation |
|----------|-----------------|----------------|
| Latence P50 | 12ms | "La moitié des prédictions prennent moins de 12ms" |
| Latence P95 | 45ms | "95% des prédictions prennent moins de 45ms" |
| Latence P99 | 89ms | "Même le pire cas reste sous 100ms" ✅ |

## 6.3 Dashboard Grafana - Explication de chaque panneau

### Qu'est-ce que Grafana ?

**Grafana** transforme les données Prometheus en **graphiques visuels**. C'est le "tableau de bord" de supervision.

### Accès

| Information | Valeur |
|-------------|--------|
| URL | http://localhost:3000 |
| Utilisateur | admin |
| Mot de passe | admin |

### Les 8 panneaux du dashboard expliqués

#### Panneau 1 : "Requêtes (5 min)"

```
┌─────────────────────┐
│     REQUÊTES        │
│       47            │
│    (5 dernières     │
│      minutes)       │
└─────────────────────┘
```

**Ce que ça montre :** Le nombre total de requêtes reçues par l'API dans les 5 dernières minutes.

**Comment l'interpréter :**
- 0 → Aucune activité (normal si personne n'utilise l'application)
- 10-50 → Activité légère (tests, quelques utilisateurs)
- 100+ → Activité importante (utilisation en production)

#### Panneau 2 : "Latence P95"

```
┌─────────────────────┐
│    LATENCE P95      │
│      45 ms          │
└─────────────────────┘
```

**Ce que ça montre :** 95% des requêtes répondent en moins de cette durée.

**Comment l'interpréter :**
| Valeur | Interprétation |
|--------|----------------|
| < 100ms | ✅ Excellent - API très réactive |
| 100-500ms | ⚠️ Acceptable - Peut être amélioré |
| > 500ms | ❌ Problème - Investiguer la cause |

#### Panneau 3 : "Modèle chargé"

```
┌─────────────────────┐
│   MODÈLE CHARGÉ     │
│        ✅           │
│   (valeur = 1)      │
└─────────────────────┘
```

**Ce que ça montre :** Le modèle XGBoost est-il chargé en mémoire ?

**Comment l'interpréter :**
- **1 (✅)** → Le modèle est prêt, les prédictions fonctionnent
- **0 (❌)** → ALERTE ! Le modèle n'est pas chargé, les prédictions échoueront

#### Panneau 4 : "Dernière prédiction"

```
┌─────────────────────┐
│ DERNIÈRE PRÉDICTION │
│       45.2%         │
└─────────────────────┘
```

**Ce que ça montre :** La probabilité de défaut de la dernière prédiction effectuée.

**Comment l'interpréter :**
| Valeur | Niveau de risque |
|--------|------------------|
| < 30% | Risque Faible |
| 30-55% | Risque Moyen |
| > 55% | Risque Élevé |

#### Panneau 5 : "Requêtes/sec par endpoint"

```
┌────────────────────────────────────────────────┐
│ Requêtes par seconde                           │
│                                                │
│  0.5 │    ╭──╮                                 │
│      │   ╱    ╲      /predict                  │
│  0.3 │  ╱      ╲────╱                          │
│      │ ╱                    /health            │
│  0.1 │╱─────────────────────────────           │
│      └──────────────────────────────────────   │
│        10:00   10:05   10:10   10:15           │
└────────────────────────────────────────────────┘
```

**Ce que ça montre :** L'évolution du nombre de requêtes par seconde, séparé par endpoint.

**Comment l'interpréter :**
- **Pics** → Moments d'activité intense
- **Creux** → Périodes calmes
- **Ligne plate à 0** → Aucune activité

**Endpoints surveillés :**
- `/predict` → Prédictions de risque (le plus important)
- `/explain` → Explications SHAP
- `/health` → Vérifications de santé (souvent automatiques)

#### Panneau 6 : "Latence (percentiles)"

```
┌────────────────────────────────────────────────┐
│ Latence des requêtes (ms)                      │
│                                                │
│ 100 │         ╭╮                               │
│     │        ╱  ╲    P99                       │
│  50 │   ╭───╱    ╲───╮    P95                  │
│     │  ╱              ╲──╱                     │
│  20 │─╱────────────────────── P50              │
│     └──────────────────────────────────────    │
│        10:00   10:05   10:10   10:15           │
└────────────────────────────────────────────────┘
```

**Ce que ça montre :** L'évolution de la latence au fil du temps, avec 3 courbes :
- **P50 (ligne du bas)** : Latence médiane
- **P95 (ligne du milieu)** : 95% des requêtes sont plus rapides
- **P99 (ligne du haut)** : 99% des requêtes sont plus rapides

**Comment l'interpréter :**
- **Courbes stables** → Performance constante ✅
- **Pic soudain** → Problème ponctuel (ex: charge importante)
- **Montée progressive** → Dégradation à investiguer ⚠️
- **P99 très au-dessus de P50** → Quelques requêtes sont très lentes

#### Panneau 7 : "Prédictions par risque"

```
┌────────────────────────────────────────────────┐
│ Prédictions par niveau de risque               │
│                                                │
│              ┌─────────┐                       │
│           ╱╲ │ Moyen   │ 88%                   │
│         ╱    ╲─────────┘                       │
│       ╱        ╲                               │
│     ╱            ╲  ┌─────────┐                │
│   ╱                ╲│ Élevé   │ 12%            │
│ ╱                    ─────────┘                │
│                      ┌─────────┐               │
│                      │ Faible  │ 0%            │
│                      └─────────┘               │
└────────────────────────────────────────────────┘
```

**Ce que ça montre :** La répartition des prédictions par niveau de risque.

**Comment l'interpréter :**

| Distribution | Signification |
|--------------|---------------|
| Majorité "Faible" | Clients de bonne qualité |
| Majorité "Moyen" | Portefeuille intermédiaire (normal) |
| Beaucoup d'"Élevé" | ⚠️ Attention aux profils à risque |

**Pourquoi "Faible" peut être à 0% ?**

Les seuils de décision sont :
- **Faible** : probabilité < 30%
- **Moyen** : probabilité 30% - 55%
- **Élevé** : probabilité > 55%

Le modèle ayant un biais vers les probabilités moyennes (dû au déséquilibre des classes 1:11), peu de prédictions tombent sous 30%.

#### Panneau 8 : "Prédictions par heure"

```
┌────────────────────────────────────────────────┐
│ Prédictions par heure                          │
│                                                │
│  50 │                ████                      │
│     │      ████      ████                      │
│  25 │ ████ ████ ████ ████ ████                 │
│     │ ████ ████ ████ ████ ████                 │
│   0 └──────────────────────────────────────    │
│      10h   11h   12h   13h   14h               │
└────────────────────────────────────────────────┘
```

**Ce que ça montre :** Le nombre de prédictions effectuées chaque heure.

**Comment l'interpréter :**
- Permet d'identifier les **heures de pointe**
- Utile pour la **planification de capacité**
- Aide à détecter des **anomalies** (pic ou creux inhabituel)

## 6.4 Apache Airflow - Explication détaillée

### Qu'est-ce qu'Airflow ?

**Apache Airflow** est un outil d'**orchestration** qui :
1. Exécute des tâches **automatiquement** selon un planning
2. Gère les **dépendances** entre tâches
3. Permet de **visualiser** l'exécution des workflows

### Accès

| Information | Valeur |
|-------------|--------|
| URL | http://localhost:8080 |
| Utilisateur | admin |
| Mot de passe | *(généré automatiquement - voir les logs du container)* |

### Le DAG "credit_risk_monitoring"

**DAG** = Directed Acyclic Graph = Un ensemble de tâches avec leurs dépendances.

```
┌─────────────────────────────────────────────────────────────────────┐
│                   DAG : credit_risk_monitoring                      │
│                   Fréquence : Toutes les heures                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌──────────────────┐                                              │
│   │ check_api_health │  Tâche 1 : Vérifie que l'API répond          │
│   │    (1ère)        │  → Appelle GET /health                       │
│   └────────┬─────────┘  → Si échec : alerte                         │
│            │                                                        │
│            ▼                                                        │
│   ┌──────────────────┐                                              │
│   │ test_prediction  │  Tâche 2 : Teste une prédiction              │
│   │    (2ème)        │  → Appelle POST /predict avec données test   │
│   └────────┬─────────┘  → Vérifie que la réponse est valide         │
│            │                                                        │
│            ▼                                                        │
│   ┌──────────────────┐                                              │
│   │ collect_metrics  │  Tâche 3 : Collecte les métriques            │
│   │    (3ème)        │  → Appelle GET /metrics                      │
│   └────────┬─────────┘  → Extrait les compteurs et latences         │
│            │                                                        │
│            ▼                                                        │
│   ┌──────────────────┐                                              │
│   │ generate_report  │  Tâche 4 : Génère un rapport                 │
│   │    (4ème)        │  → Résume les résultats des 3 tâches         │
│   └──────────────────┘  → Log dans la console Airflow               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Les 4 tâches en détail

| Tâche | Que fait-elle ? | Pourquoi c'est utile ? |
|-------|-----------------|------------------------|
| **check_api_health** | Vérifie que l'API est en vie | Détecte rapidement si l'API est tombée |
| **test_prediction** | Effectue une vraie prédiction | Vérifie que le modèle fonctionne |
| **collect_metrics** | Récupère les métriques Prometheus | Permet de suivre l'évolution |
| **generate_report** | Crée un résumé | Garde une trace dans les logs |

### Interface Airflow expliquée

```
┌─────────────────────────────────────────────────────────────────────┐
│ AIRFLOW - DAGs                                                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│ ┌─────────────────────────────────────────────────────────────────┐ │
│ │ DAG                    │ Schedule │ Last Run  │ Status │ Actions│ │
│ ├────────────────────────┼──────────┼───────────┼────────┼────────┤ │
│ │ credit_risk_monitoring │ @hourly  │ 10:00:00  │ ✅     │ ▶ ⏸    │ │
│ └─────────────────────────────────────────────────────────────────┘ │
│                                                                     │
│ Légende des statuts :                                               │
│ ✅ Success - Toutes les tâches ont réussi                          │
│ 🔄 Running - En cours d'exécution                                   │
│ ❌ Failed - Au moins une tâche a échoué                            │
│ ⏸  Paused - Le DAG est en pause (ne s'exécute pas)                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Lecture des logs dans Airflow

Pour chaque tâche, vous pouvez voir :
1. **Le statut** : Success ✅, Failed ❌, Running 🔄
2. **La durée** : Combien de temps la tâche a pris
3. **Les logs** : Ce que la tâche a affiché (messages, erreurs)

## 6.5 Configuration Docker Compose

### Services déployés

| Service | Image | Port | Rôle |
|---------|-------|------|------|
| **postgres** | postgres:15-alpine | 5432 | Base de données |
| **api** | Python 3.12 (build local) | 8000 | API FastAPI avec modèle XGBoost |
| **streamlit** | Python 3.12 (build local) | 8501 | Interface utilisateur |
| **prometheus** | prom/prometheus:v2.47.0 | 9090 | Collecte des métriques |
| **grafana** | grafana/grafana:10.2.0 | 3000 | Visualisation des métriques |
| **airflow** | apache/airflow:3.1.6-python3.12 | 8080 | Orchestration des tâches |

### Commandes utiles

```bash
# Démarrer tous les services
docker compose up -d

# Voir l'état des services
docker compose ps

# Voir les logs d'un service
docker compose logs api
docker compose logs airflow

# Arrêter tous les services
docker compose down

# Redémarrer un service spécifique
docker compose restart api
```

### Réseau interne Docker

Les services communiquent entre eux via leurs noms de container :

```
┌─────────────────────────────────────────────────────────────────────┐
│                   Réseau : credit_risk_network                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   Streamlit ────────► http://api:8000/predict                       │
│   (pas localhost!)                                                  │
│                                                                     │
│   Prometheus ───────► http://api:8000/metrics                       │
│   (scrape toutes les 15s)                                           │
│                                                                     │
│   Grafana ──────────► http://prometheus:9090                        │
│   (requêtes PromQL)                                                 │
│                                                                     │
│   API ──────────────► postgres:5432                                 │
│   (connexion base)                                                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Important :** Dans Docker, les services utilisent les noms de container (ex: `api`, `prometheus`), pas `localhost`.

## 6.6 Résumé des interfaces

| Interface | URL | Login | Ce qu'on y fait |
|-----------|-----|-------|-----------------|
| **Swagger API** | http://localhost:8000/docs | - | Tester les endpoints manuellement |
| **Streamlit** | http://localhost:8501 | - | Faire des prédictions (interface utilisateur) |
| **Prometheus** | http://localhost:9090 | - | Explorer les métriques brutes (avancé) |
| **Grafana** | http://localhost:3000 | admin/admin | Visualiser les dashboards de monitoring |
| **Airflow** | http://localhost:8080 | admin/(voir logs) | Gérer les tâches planifiées |

## 6.7 Problèmes rencontrés et solutions

| Problème | Cause | Solution |
|----------|-------|----------|
| Port 5432 déjà utilisé | PostgreSQL local actif | `sudo service postgresql stop` |
| Port 8000 déjà utilisé | Uvicorn local actif | `pkill -f uvicorn` |
| Airflow permission denied | UID/GID incorrect | `sudo chown -R 50000:0 airflow/ && sudo chmod -R 775 airflow/` |
| SHAP erreur 503 "string to float" | Version SHAP incompatible (0.49 vs 0.50) | Mettre à jour Dockerfile vers Python 3.12 et SHAP >= 0.50.0 |
| Streamlit "API non disponible" | `localhost` ne fonctionne pas dans Docker | Utiliser `os.getenv("API_URL")` = `http://api:8000` |
| `docker-compose` command not found | Ancienne syntaxe | Utiliser `docker compose` (sans tiret) |

## 6.8 Validation Phase 6

```bash
# Checklist de validation complète
[x] docker compose up -d démarre sans erreur
[x] docker compose ps montre 6 services "healthy" ou "running"
[x] http://localhost:8000/health retourne "healthy"
[x] http://localhost:8000/metrics retourne les métriques Prometheus
[x] http://localhost:8501 affiche Streamlit (API connectée)
[x] http://localhost:9090 affiche Prometheus
[x] http://localhost:3000 affiche Grafana avec le dashboard
[x] http://localhost:8080 affiche Airflow avec le DAG
[x] Le DAG s'exécute avec succès (4 tâches vertes)
[x] Grafana affiche les métriques après quelques prédictions
[x] L'endpoint /explain fonctionne (SHAP v0.50.0)
```


# PHASE 7 : DÉPLOIEMENT & DOCUMENTATION

**Statut :** 🔄 En cours | **Date :** 28/01/2026

## 7.1 Documentation finalisée

**Statut :** ✅ Terminé

### Fichiers mis à jour

| Fichier | Modifications |
|---------|---------------|
| `README.md` | Version française complète, screenshots, versions corrigées |
| `docs/01_ETUDE_PROJET.md` | Python 3.10+ → 3.12+ |
| `docs/03_RAPPORT_AVANCEMENT.md` | Profils réalistes, captures d'écran, Phase 7 |

### Corrections apportées

- **Versions des outils** : Vérifiées via `pip show` (Airflow 3.1.6, SHAP 0.50.0, etc.)
- **Profils multi-devises réalistes** : Basés sur recherche économique (SMIG CEMAC/UEMOA, SMIC Europe, salaires USA)
- **Captures d'écran** : 12 images ajoutées dans `docs/images/`

## 7.2 Profils économiques réalistes

**Statut :** ✅ Terminé

### Recherche économique effectuée

| Zone | Salaire minimum | Cadre supérieur (mensuel) |
|------|-----------------|---------------------------|
| CEMAC (XAF) | ~83 000 FCFA | ~1.2M FCFA |
| UEMOA (XOF) | ~55 000 FCFA | ~933K FCFA |
| Europe (EUR) | ~2 000 € | ~6 000 € |
| USA (USD) | ~$15/h (~$31K/an) | ~$13K/mois |

### Implémentation

- `PROFILES_BY_CURRENCY` : Dictionnaire avec valeurs natives par devise
- `DEFAULT_VALUES` : Valeurs par défaut adaptées à chaque zone
- XAF défini comme devise par défaut (contexte africain)

## 7.3 Déploiement Streamlit Cloud

**Statut :** ⬜ À faire

### Prérequis
- [x] Code fonctionnel en local
- [x] Tests passent (31/31)
- [x] Documentation à jour
- [ ] Commit et push vers GitHub
- [ ] Connexion Streamlit Cloud ↔ GitHub
- [ ] Déploiement et test en ligne

## 7.4 Finalisation

**Statut :** ⬜ À faire

- [ ] Ajouter lien de démo au README
- [ ] Post LinkedIn (optionnel)
- [ ] Archivage du projet


# JOURNAL DES PROBLÈMES & SOLUTIONS

| Date | Problème | Solution |
|------|----------|----------|
| 25/01/2026 | API Kaggle erreur 403 | Accepter les règles de la compétition sur le site web |
| 25/01/2026 | Extension Jupyter VS Code échoue | Utiliser Jupyter Notebook dans le navigateur |
| 25/01/2026 | `pip install` bloqué (externally-managed) | Créer et utiliser un environnement virtuel |
| 26/01/2026 | Crash WSL pendant ingestion PostgreSQL | Réduire chunk_size de 50000 à 10000 |
| 26/01/2026 | Port 5432 déjà utilisé par Docker | Utiliser PostgreSQL local au lieu de Docker |
| 26/01/2026 | KeyError colonnes (majuscules/minuscules) | Uniformiser tout en minuscules |
| 27/01/2026 | Kernel Jupyter ne fonctionne pas dans VS Code | Utiliser Jupyter navigateur (sans token) |
| 27/01/2026 | Déconnexion WSL pendant Optuna (erreur 1006) | Race condition systemd WSL2 → `rm -rf ~/.vscode-server` + `wsl --shutdown` |


# MÉTRIQUES FINALES

*(Mis à jour après Phase 5)*

| Métrique | Valeur | Objectif | Statut |
|----------|--------|----------|--------|
| AUC-ROC | **0.7836** | > 0.75 | ✅ |
| Gini | **0.5673** | > 0.50 | ✅ |
| Precision | 0.1862 | - | - |
| Recall | **0.6998** | > 0.60 | ✅ |
| F1-Score | 0.2941 | - | - |
| Latence API | **< 100ms** | < 200ms | ✅ |
| Interface | **Multilingue** | - | ✅ Bonus |
| Devises | **4 (EUR/USD/XAF/XOF)** | - | ✅ Bonus |


# LEÇONS APPRISES

*(Mis à jour après Phase 5)*

1. **Les scores externes (EXT_SOURCE) sont les meilleurs prédicteurs** - 40% de l'importance SHAP. L'historique crédit externe est plus prédictif que les données internes.

2. **Arbres simples généralisent mieux** - Optuna a trouvé max_depth=3 optimal vs 6 par défaut. La régularisation forte (gamma, reg_alpha, reg_lambda) évite l'overfitting.

3. **Le feature engineering paie** - Les 103 features créées en Phase 3 ont permis d'atteindre l'objectif dès le baseline (AUC 0.7778 > 0.75).

4. **Persistance Optuna avec SQLite** - Indispensable pour les longues optimisations. Permet de reprendre après crash (bug WSL2 résolu grâce à ça).

5. **Déséquilibre de classes (1:11)** - scale_pos_weight fonctionne bien. Le recall (70%) est bon, la precision basse (19%) est attendue et acceptable avec vérification humaine.

6. **Calibration des profils de démo est critique** - Les valeurs "intuitives" ne correspondent pas au comportement du modèle. Il faut tester empiriquement et ajuster.

7. **Le score externe domine tout** - Un changement de 0.45 à 0.72 sur ext_source fait passer de 70% à 40% de probabilité. L'impact est non-linéaire et massif.

8. **Conversion devises bidirectionnelle** - Afficher en devise locale (UX) mais calculer en EUR (cohérence) est la bonne approche. Les prédictions sont identiques quelle que soit la devise.

9. **Streamlit session_state** - Les callbacks `on_click` modifient le state AVANT le rerun, permettant de mettre à jour les widgets. Modifier après création = erreur.

10. **Profils multi-devises réalistes** - Les montants doivent être natifs à chaque zone économique, pas de simples conversions mécaniques. Un cadre supérieur gagne ~1.2M FCFA en Afrique centrale, pas 59M FCFA (conversion 90K€). La recherche économique (SMIG, salaires moyens) est indispensable pour un projet réaliste.

**Dernière mise à jour :** 28 Janvier 2026 - Phase 7 en cours : documentation finalisée, profils multi-devises réalistes, captures d'écran ajoutées


# GLOSSAIRE TECHNIQUE

Pour faciliter la compréhension de ce rapport, voici les termes techniques utilisés :

| Terme | Explication simple |
|-------|-------------------|
| **AUC-ROC** | Score de 0 à 1 mesurant la qualité du modèle. 0.5 = hasard, 1.0 = parfait. Notre modèle : 0.78 = bon |
| **Counter** | Compteur qui ne fait qu'augmenter (ex: nombre de requêtes) |
| **DAG** | Graphe de tâches avec dépendances (Directed Acyclic Graph) |
| **Endpoint** | URL d'accès à une fonctionnalité de l'API (ex: /predict, /health) |
| **Feature** | Variable utilisée par le modèle pour faire une prédiction |
| **Gauge** | Valeur qui peut monter ou descendre (ex: dernière probabilité) |
| **Gini** | Mesure de discrimination : 2×AUC - 1. Notre modèle : 0.57 = bon |
| **Histogram** | Distribution de valeurs permettant de calculer les percentiles |
| **Latence** | Temps entre une requête et sa réponse |
| **P50/P95/P99** | Percentiles - voir section 6.2 pour explication détaillée |
| **Precision** | Parmi les alertes "risque", combien sont de vrais risques |
| **PromQL** | Langage de requête de Prometheus |
| **Recall** | Parmi les vrais risques, combien sont détectés |
| **SHAP** | Méthode d'explication des prédictions (SHapley Additive exPlanations) |
| **Seuil** | Valeur de coupure pour décider (ex: >55% = risque élevé) |
| **XGBoost** | Algorithme de machine learning utilisé dans ce projet |
