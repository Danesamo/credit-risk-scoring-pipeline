# Diagnostic de la V1

**Rédigé le :** 25/09/2026 (mis en forme le 26/09/2026)
**Périmètre analysé :** documentation (`docs/v1/01_ETUDE_PROJET.md`, `docs/v1/03_RAPPORT_AVANCEMENT.md`), API (`api/main.py`), feature engineering (`src/features/build_features.py`), notebook de modélisation (`notebooks/03_modeling.ipynb`), Streamlit, DAG Airflow, Docker Compose.
**Version analysée :** commit `4888cc6` (branche `main`), futur tag `v1.0`.

---

## 1. Rappel de la V1

Données Kaggle Home Credit (8 tables, 307 511 clients) → PostgreSQL → 103 features créées (225 colonnes) → XGBoost optimisé par Optuna (50 essais) → API FastAPI avec explications SHAP → Streamlit (FR/EN, EUR/USD/XAF/XOF), avec Prometheus, Grafana et Airflow.

Résultats publiés : AUC 0.7836, Gini 0.567, rappel 70 %, précision 18,6 % (seuil 0,5).

## 2. Points forts à conserver

- Chaîne complète de la donnée brute à l'interface.
- Documentation très pédagogique.
- 31 tests automatisés.
- Explications SHAP traduites en langage compréhensible.
- Interface bilingue et multi-devises, avec XAF par défaut.
- Monitoring technique (latence, volume de requêtes) en place.
- Correction récente de l'écart sur les features dérivées (commit `4888cc6`).

**Conclusion :** l'ossature est bonne et sera conservée comme base de la V2.

## 3. Défauts identifiés

| # | Défaut | Gravité | Référence |
|---|---|---|---|
| 1 | Dépendance à des scores externes absents du contexte africain | Critique | SHAP : `ext_source_mean` 1re variable (11 % de l'importance totale, 3 fois la 2e) ; scores externes cumulés ≈ 20 % |
| 2 | Écart entre entraînement et production | Critique | [api/main.py:209](../../api/main.py#L209), [build_features.py:483](../../src/features/build_features.py#L483) |
| 3 | Probabilités non calibrées | Critique | `scale_pos_weight=11.4`, [api/main.py:409](../../api/main.py#L409), [api/main.py:482](../../api/main.py#L482) |
| 4 | Genre parmi les variables les plus influentes | Élevée | SHAP : `code_gender` au 2e rang |
| 5 | Bug d'agrégation par blocs | Élevée | [build_features.py:245-253](../../src/features/build_features.py#L245-L253) |
| 6 | Validation méthodologique à renforcer | Moyenne | Notebook, cellules 11 et 15 |
| 7 | Montants non comparables entre devises | Moyenne | Conversion en EUR dans la Streamlit |
| 8 | Pas de MLOps réel | Moyenne | DAG Airflow, stockage du modèle |

### 3.1 Dépendance aux scores externes
Les variables `EXT_SOURCE_1/2/3` sont des scores de bureaux de crédit dont l'origine n'est pas documentée par Home Credit. Leur moyenne est de loin la variable la plus influente : 11 % de l'importance SHAP totale, trois fois plus que la 2e variable ; toutes les variables `ext_source` réunies pèsent environ 20 % (recalcul du 02/10/2026 sur 2 000 clients). Le rapport V1 annonçait « 40 % » : c'était une confusion entre la valeur SHAP moyenne (0,40) et un pourcentage. La population visée en Afrique (secteur informel, peu bancarisée) n'a justement pas ce type de score. **Le modèle performe surtout sur ceux qui ont déjà un historique.**

### 3.2 Écart entre entraînement et production
Le modèle attend 223 variables ; l'API n'en remplit qu'environ 17 et met toutes les autres à 0. À l'entraînement, les valeurs manquantes (hors comptes et sommes) étaient remplacées par la médiane. En production, chaque client ressemble donc à un profil qui n'existe pas dans les données d'entraînement.

### 3.3 Probabilités non calibrées
`scale_pos_weight` corrige le déséquilibre des classes pour le classement, mais gonfle les probabilités. Le profil « fiable » affiche 30 % de risque alors que le taux de défaut réel est de 8 %. Les seuils de décision (40 % / 55 %) et le score 300-850 (transformation linéaire, et non une vraie grille de score) reposent sur ces probabilités. La probabilité de base est codée en dur (0,0807). **Pour une banque, une PD doit être une probabilité calibrée** (par exemple par calibration isotonique ou de Platt sur des données hors échantillon).

### 3.4 Genre
`code_gender` est la 2e variable la plus importante, et l'interface propose un sélecteur de genre. Risque de discrimination, sur le plan éthique comme réglementaire. En V2 : exclure les variables sensibles de la décision et mesurer l'équité du modèle.

### 3.5 Bug d'agrégation par blocs
Pour les tables volumineuses, les données sont lues par blocs de lignes. Pour un client à cheval sur deux blocs, les sommes et comptes sont bien additionnés, mais les moyennes, maximums et minimums sont remplacés par ceux du dernier bloc au lieu d'être combinés.

### 3.6 Validation méthodologique
- Imputation par la médiane et encodage des variables catégorielles calculés sur tout le jeu de données avant la séparation train / validation / test : légère fuite d'information.
- Séparation aléatoire. La norme en crédit est le test **out-of-time** : entraîner sur une période, tester sur une période plus récente.
- AUC identique à 4 décimales sur la validation et le test (0,7836) : à revérifier, et non à présenter comme preuve de robustesse.

### 3.7 Montants et devises
La Streamlit convertit les montants en EUR avant de les envoyer au modèle. Or le modèle a appris sur des montants dans une devise que Home Credit ne documente pas. Les ratios ne sont pas affectés, mais les montants absolus (l'annuité est la 4e variable) ne sont pas comparables.

### 3.8 MLOps
- Airflow vérifie seulement que l'API répond ; il ne recharge pas les données et ne réentraîne pas le modèle.
- Pas de suivi de la dérive des données ou du modèle (par exemple l'indice de stabilité de population, PSI).
- Modèle stocké en pickle, sans registre de versions.
- `@app.on_event("startup")` est déprécié dans FastAPI.
- Le fichier d'exécution `airflow/db/airflow.db` est suivi par Git.

## 4. Ce que ce diagnostic implique pour la V2

1. La question des **données disponibles en Afrique** devient centrale (phases P1 et P3).
2. La **calibration** et une vraie **grille de score** sont indispensables pour parler le langage d'une banque.
3. Les **variables sensibles** et l'**équité** doivent être traitées dès la conception.
4. Le pipeline doit garantir que **la production calcule exactement les mêmes variables que l'entraînement**.
5. Le **MLOps** doit couvrir le cycle de vie du modèle, pas seulement la santé de l'API.
