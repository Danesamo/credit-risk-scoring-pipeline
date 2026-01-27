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

**Statut :** ⬜ À faire

## Résultats attendus

| Métrique | Objectif | Résultat |
|----------|----------|----------|
| AUC-ROC | > 0.75 | - |
| Gini | > 0.50 | - |
| Recall (défauts) | > 0.60 | - |

*(À compléter)*

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

---

# MÉTRIQUES FINALES

*(À compléter à la fin du projet)*

| Métrique | Valeur |
|----------|--------|
| AUC-ROC | - |
| Gini | - |
| Precision | - |
| Recall | - |
| F1-Score | - |
| Latence API | - |

---

# LEÇONS APPRISES

*(À compléter)*

1. -
2. -
3. -

---

**Dernière mise à jour :** 27 Janvier 2026
