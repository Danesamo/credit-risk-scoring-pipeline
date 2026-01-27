# Rapport d'Avancement - Credit Risk Scoring Pipeline

---

## Informations Projet

| Élément | Détail |
|---------|--------|
| **Projet** | Credit Risk Scoring Pipeline |
| **Auteur** | Daniela Samo |
| **Date début** | 25 Janvier 2026 |
| **Statut** | 🔄 En cours |

---

## Résumé Exécutif

Ce document trace l'avancement du projet, les décisions prises, les résultats obtenus et les problèmes rencontrés. Il sert de journal de bord et sera la base du rapport final.

---

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

---

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

---

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

---

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

**Statut :** 🔄 En cours

### Configuration Optuna

| Paramètre | Valeur |
|-----------|--------|
| Nombre de trials | 100 |
| Sampler | TPE (Tree-structured Parzen Estimator) |
| Direction | Maximiser AUC |
| Seed | 42 |

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

---

# PHASE 5 : API & INTERFACE

**Statut :** ⬜ À faire

*(À compléter)*

---

# PHASE 6 : ORCHESTRATION & MONITORING

**Statut :** ⬜ À faire

*(À compléter)*

---

# PHASE 7 : DÉPLOIEMENT

**Statut :** ⬜ À faire

*(À compléter)*

---

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

---

# MÉTRIQUES FINALES

*(Mis à jour après Phase 4)*

| Métrique | Valeur | Objectif | Statut |
|----------|--------|----------|--------|
| AUC-ROC | **0.7836** | > 0.75 | ✅ |
| Gini | **0.5673** | > 0.50 | ✅ |
| Precision | 0.1862 | - | - |
| Recall | **0.6998** | > 0.60 | ✅ |
| F1-Score | 0.2941 | - | - |
| Latence API | - | < 200ms | ⬜ Phase 5 |

---

# LEÇONS APPRISES

*(Mis à jour après Phase 4)*

1. **Les scores externes (EXT_SOURCE) sont les meilleurs prédicteurs** - 40% de l'importance SHAP. L'historique crédit externe est plus prédictif que les données internes.

2. **Arbres simples généralisent mieux** - Optuna a trouvé max_depth=3 optimal vs 6 par défaut. La régularisation forte (gamma, reg_alpha, reg_lambda) évite l'overfitting.

3. **Le feature engineering paie** - Les 103 features créées en Phase 3 ont permis d'atteindre l'objectif dès le baseline (AUC 0.7778 > 0.75).

4. **Persistance Optuna avec SQLite** - Indispensable pour les longues optimisations. Permet de reprendre après crash (bug WSL2 résolu grâce à ça).

5. **Déséquilibre de classes (1:11)** - scale_pos_weight fonctionne bien. Le recall (70%) est bon, la precision basse (19%) est attendue et acceptable avec vérification humaine.

---

**Dernière mise à jour :** 27 Janvier 2026 - Phase 4 terminée
