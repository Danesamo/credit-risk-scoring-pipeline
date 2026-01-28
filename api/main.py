# =============================================================================
# API CREDIT RISK SCORING
# =============================================================================
# Point d'entrée de l'API FastAPI
# Endpoints : /health, /predict, /explain
# =============================================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
import joblib
import json
import numpy as np
import pandas as pd
from pathlib import Path
import shap

# =============================================================================
# CONFIGURATION
# =============================================================================

# Chemins vers les artefacts du modèle
BASE_DIR = Path(__file__).parent.parent
MODELS_DIR = BASE_DIR / "models"

MODEL_PATH = MODELS_DIR / "xgboost_credit_risk_v1.pkl"
FEATURES_PATH = MODELS_DIR / "feature_names.json"
ENCODERS_PATH = MODELS_DIR / "label_encoders.pkl"
METRICS_PATH = MODELS_DIR / "metrics.json"

# =============================================================================
# CHARGEMENT DU MODÈLE (au démarrage)
# =============================================================================

# Variables globales pour le modèle
model = None
feature_names = None
label_encoders = None
metrics = None
shap_explainer = None  # Explainer SHAP pour l'explicabilité

def load_model():
    """Charge le modèle et les artefacts au démarrage."""
    global model, feature_names, label_encoders, metrics, shap_explainer

    print("Chargement du modèle...")

    # Charger le modèle XGBoost
    if MODEL_PATH.exists():
        model = joblib.load(MODEL_PATH)
        print(f"  - Modèle chargé: {MODEL_PATH.name}")
    else:
        raise FileNotFoundError(f"Modèle non trouvé: {MODEL_PATH}")

    # Charger les noms de features
    if FEATURES_PATH.exists():
        with open(FEATURES_PATH, 'r') as f:
            feature_names = json.load(f)
        print(f"  - Features chargées: {len(feature_names)} colonnes")

    # Charger les encodeurs
    if ENCODERS_PATH.exists():
        label_encoders = joblib.load(ENCODERS_PATH)
        print(f"  - Encodeurs chargés: {len(label_encoders)} colonnes")

    # Charger les métriques
    if METRICS_PATH.exists():
        with open(METRICS_PATH, 'r') as f:
            metrics = json.load(f)
        print(f"  - Métriques chargées: AUC={metrics.get('auc_roc', 'N/A')}")

    # Créer l'explainer SHAP pour XGBoost
    try:
        shap_explainer = shap.TreeExplainer(model)
        print("  - Explainer SHAP initialisé")
    except Exception as e:
        print(f"  - Warning: SHAP explainer non initialisé: {e}")
        shap_explainer = None

    print("Modèle prêt!")

# =============================================================================
# SCHÉMAS PYDANTIC (Validation des données)
# =============================================================================

class ClientData(BaseModel):
    """Données d'entrée pour la prédiction."""

    # Variables principales (exemples - à adapter selon les features réelles)
    amt_income_total: float = Field(..., description="Revenu total du client")
    amt_credit: float = Field(..., description="Montant du crédit demandé")
    amt_annuity: Optional[float] = Field(None, description="Montant de l'annuité")
    amt_goods_price: Optional[float] = Field(None, description="Prix du bien")

    # Variables démographiques
    code_gender: Optional[str] = Field("M", description="Genre (M/F)")
    days_birth: Optional[int] = Field(-10000, description="Âge en jours (négatif)")
    days_employed: Optional[int] = Field(-1000, description="Ancienneté emploi en jours")

    # Scores externes (très importants pour le modèle)
    ext_source_1: Optional[float] = Field(None, description="Score externe 1")
    ext_source_2: Optional[float] = Field(None, description="Score externe 2")
    ext_source_3: Optional[float] = Field(None, description="Score externe 3")

    # Permettre des champs additionnels
    class Config:
        extra = "allow"


class PredictionResponse(BaseModel):
    """Réponse de l'endpoint /predict."""

    probability: float = Field(..., description="Probabilité de défaut (0-1)")
    prediction: int = Field(..., description="Prédiction binaire (0=OK, 1=Défaut)")
    risk_level: str = Field(..., description="Niveau de risque (Faible/Moyen/Élevé)")
    score: int = Field(..., description="Score de crédit (300-850)")


class HealthResponse(BaseModel):
    """Réponse de l'endpoint /health."""

    status: str
    model_loaded: bool
    model_version: str
    auc_roc: Optional[float]


class FeatureImpact(BaseModel):
    """Impact d'une feature sur la prédiction."""

    feature: str = Field(..., description="Nom de la feature")
    value: float = Field(..., description="Valeur de la feature pour ce client")
    shap_value: float = Field(..., description="Impact SHAP (+ augmente risque, - réduit)")
    impact: str = Field(..., description="Direction de l'impact (increases_risk/reduces_risk)")


class ExplainResponse(BaseModel):
    """Réponse de l'endpoint /explain."""

    probability: float = Field(..., description="Probabilité de défaut")
    base_probability: float = Field(..., description="Probabilité de base (moyenne)")
    risk_level: str = Field(..., description="Niveau de risque")
    top_risk_factors: List[FeatureImpact] = Field(..., description="Facteurs qui augmentent le risque")
    top_protective_factors: List[FeatureImpact] = Field(..., description="Facteurs qui réduisent le risque")


# =============================================================================
# APPLICATION FASTAPI
# =============================================================================

app = FastAPI(
    title="Credit Risk Scoring API",
    description="API pour prédire le risque de défaut de paiement",
    version="1.0.0"
)

# Charger le modèle au démarrage
@app.on_event("startup")
async def startup_event():
    load_model()


# =============================================================================
# ENDPOINTS
# =============================================================================

@app.get("/", tags=["Root"])
async def root():
    """Page d'accueil de l'API."""
    return {
        "message": "Credit Risk Scoring API",
        "endpoints": {
            "/health": "Vérifier l'état de l'API",
            "/predict": "Prédire le risque d'un client (POST)",
            "/explain": "Expliquer la prédiction avec SHAP (POST)",
            "/docs": "Documentation Swagger"
        }
    }


@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """
    Vérifie que l'API fonctionne et que le modèle est chargé.

    Retourne:
        - status: "healthy" si tout va bien
        - model_loaded: True si le modèle est en mémoire
        - model_version: Version du modèle
        - auc_roc: Performance du modèle
    """
    return HealthResponse(
        status="healthy" if model is not None else "unhealthy",
        model_loaded=model is not None,
        model_version="v1.0.0",
        auc_roc=metrics.get("auc_roc") if metrics else None
    )


@app.post("/predict", response_model=PredictionResponse, tags=["Prediction"])
async def predict(client: ClientData):
    """
    Prédit le risque de défaut pour un client.

    Args:
        client: Données du client (revenus, crédit, etc.)

    Retourne:
        - probability: Probabilité de défaut (0-1)
        - prediction: 0 (pas de défaut) ou 1 (défaut)
        - risk_level: Faible / Moyen / Élevé
        - score: Score de crédit style FICO (300-850)
    """
    if model is None:
        raise HTTPException(status_code=503, detail="Modèle non chargé")

    try:
        # Convertir les données client en dictionnaire
        client_dict = client.model_dump()

        # Créer un DataFrame avec TOUTES les features (initialisées à 0.0 en float)
        df = pd.DataFrame({col: [0.0] for col in feature_names})

        # Mapping des champs API vers les features du modèle
        field_mapping = {
            'amt_income_total': 'amt_income_total',
            'amt_credit': 'amt_credit',
            'amt_annuity': 'amt_annuity',
            'amt_goods_price': 'amt_goods_price',
            'days_birth': 'days_birth',
            'days_employed': 'days_employed',
            'ext_source_1': 'ext_source_1',
            'ext_source_2': 'ext_source_2',
            'ext_source_3': 'ext_source_3',
        }

        # Remplir avec les valeurs fournies
        for api_field, model_field in field_mapping.items():
            if api_field in client_dict and client_dict[api_field] is not None:
                if model_field in feature_names:
                    df.loc[0, model_field] = float(client_dict[api_field])

        # Encoder code_gender (M=1, F=0)
        if 'code_gender' in client_dict and 'code_gender' in feature_names:
            gender = client_dict['code_gender']
            if gender == 'M':
                df.loc[0, 'code_gender'] = 1.0
            elif gender == 'F':
                df.loc[0, 'code_gender'] = 0.0
            else:
                df.loc[0, 'code_gender'] = 0.0

        # Calculer des features dérivées importantes
        ext_sources = [
            client_dict.get('ext_source_1') or 0,
            client_dict.get('ext_source_2') or 0,
            client_dict.get('ext_source_3') or 0
        ]
        valid_sources = [float(s) for s in ext_sources if s and s > 0]

        if valid_sources:
            if 'ext_source_mean' in feature_names:
                df.loc[0, 'ext_source_mean'] = float(np.mean(valid_sources))
            if 'ext_source_max' in feature_names:
                df.loc[0, 'ext_source_max'] = float(max(valid_sources))
            if 'ext_source_min' in feature_names:
                df.loc[0, 'ext_source_min'] = float(min(valid_sources))

        # Prédiction
        proba = model.predict_proba(df)[0][1]  # Probabilité de défaut
        pred = int(proba >= 0.5)

        # Niveau de risque
        if proba < 0.3:
            risk_level = "Faible"
        elif proba < 0.6:
            risk_level = "Moyen"
        else:
            risk_level = "Élevé"

        # Score de crédit (inverse de la probabilité, échelle 300-850)
        score = int(850 - (proba * 550))
        score = max(300, min(850, score))  # Borner entre 300 et 850

        return PredictionResponse(
            probability=round(proba, 4),
            prediction=pred,
            risk_level=risk_level,
            score=score
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur de prédiction: {str(e)}")


@app.post("/explain", response_model=ExplainResponse, tags=["Explanation"])
async def explain(client: ClientData):
    """
    Explique la prédiction pour un client en utilisant SHAP.

    SHAP (SHapley Additive exPlanations) décompose la prédiction en montrant
    la contribution de chaque feature. C'est essentiel pour :
    - Comprendre POURQUOI un client est considéré à risque
    - Justifier les décisions auprès des régulateurs
    - Identifier les axes d'amélioration pour le client

    Args:
        client: Données du client (mêmes données que /predict)

    Retourne:
        - probability: Probabilité de défaut
        - base_probability: Probabilité moyenne (baseline)
        - top_risk_factors: Features qui AUGMENTENT le risque
        - top_protective_factors: Features qui RÉDUISENT le risque
    """
    if model is None:
        raise HTTPException(status_code=503, detail="Modèle non chargé")

    if shap_explainer is None:
        raise HTTPException(status_code=503, detail="Explainer SHAP non disponible")

    try:
        # Convertir les données client en dictionnaire
        client_dict = client.model_dump()

        # Créer un DataFrame avec TOUTES les features (initialisées à 0.0 en float)
        df = pd.DataFrame({col: [0.0] for col in feature_names})

        # Mapping des champs API vers les features du modèle
        field_mapping = {
            'amt_income_total': 'amt_income_total',
            'amt_credit': 'amt_credit',
            'amt_annuity': 'amt_annuity',
            'amt_goods_price': 'amt_goods_price',
            'days_birth': 'days_birth',
            'days_employed': 'days_employed',
            'ext_source_1': 'ext_source_1',
            'ext_source_2': 'ext_source_2',
            'ext_source_3': 'ext_source_3',
        }

        # Remplir avec les valeurs fournies
        for api_field, model_field in field_mapping.items():
            if api_field in client_dict and client_dict[api_field] is not None:
                if model_field in feature_names:
                    df.loc[0, model_field] = float(client_dict[api_field])

        # Encoder code_gender (M=1, F=0)
        if 'code_gender' in client_dict and 'code_gender' in feature_names:
            gender = client_dict['code_gender']
            if gender == 'M':
                df.loc[0, 'code_gender'] = 1.0
            elif gender == 'F':
                df.loc[0, 'code_gender'] = 0.0
            else:
                df.loc[0, 'code_gender'] = 0.0

        # Calculer des features dérivées importantes
        ext_sources = [
            client_dict.get('ext_source_1') or 0,
            client_dict.get('ext_source_2') or 0,
            client_dict.get('ext_source_3') or 0
        ]
        valid_sources = [float(s) for s in ext_sources if s and s > 0]

        if valid_sources:
            if 'ext_source_mean' in feature_names:
                df.loc[0, 'ext_source_mean'] = float(np.mean(valid_sources))
            if 'ext_source_max' in feature_names:
                df.loc[0, 'ext_source_max'] = float(max(valid_sources))
            if 'ext_source_min' in feature_names:
                df.loc[0, 'ext_source_min'] = float(min(valid_sources))

        # Prédiction
        proba = model.predict_proba(df)[0][1]

        # Niveau de risque
        if proba < 0.3:
            risk_level = "Faible"
        elif proba < 0.6:
            risk_level = "Moyen"
        else:
            risk_level = "Élevé"

        # Calcul des SHAP values
        shap_values = shap_explainer.shap_values(df)

        # Pour XGBoost binaire, shap_values peut être une liste [class0, class1]
        if isinstance(shap_values, list):
            shap_vals = shap_values[1][0]  # Classe 1 (défaut), premier sample
        else:
            shap_vals = shap_values[0]

        # Probabilité de base (expected value)
        if isinstance(shap_explainer.expected_value, (list, np.ndarray)):
            base_value = float(shap_explainer.expected_value[1])
        else:
            base_value = float(shap_explainer.expected_value)

        # Convertir base_value en probabilité si c'est en log-odds
        # Pour XGBoost, on utilise directement la probabilité moyenne du dataset
        base_probability = 0.0807  # 8.07% - taux de défaut dans le dataset

        # Créer un dictionnaire feature -> (valeur, shap_value)
        feature_impacts = []
        for i, feat in enumerate(feature_names):
            if abs(shap_vals[i]) > 0.001:  # Ignorer les impacts négligeables
                feature_impacts.append({
                    "feature": feat,
                    "value": float(df.loc[0, feat]),
                    "shap_value": float(shap_vals[i]),
                    "impact": "increases_risk" if shap_vals[i] > 0 else "reduces_risk"
                })

        # Trier par impact absolu
        feature_impacts.sort(key=lambda x: abs(x["shap_value"]), reverse=True)

        # =================================================================
        # FILTRAGE DYNAMIQUE - Adapté au profil du client
        # =================================================================
        # La logique : un profil FIABLE doit montrer PLUS d'atouts que de vigilances
        # Un profil RISQUÉ doit montrer PLUS de vigilances que d'atouts
        # Cela rend l'explication intuitive et compréhensible
        # =================================================================

        # Seuil minimum d'impact pour être affiché
        MIN_IMPACT_THRESHOLD = 0.025

        # Déterminer les limites selon le niveau de risque
        if proba < 0.40:  # Profil FIABLE
            max_protective = 6  # Beaucoup d'atouts
            max_risk = 3        # Peu de vigilances
        elif proba < 0.55:  # Profil MOYEN
            max_protective = 4  # Équilibré
            max_risk = 4
        else:  # Profil RISQUÉ
            max_protective = 3  # Peu d'atouts
            max_risk = 6        # Beaucoup de vigilances

        # Séparer facteurs de risque et facteurs protecteurs
        all_risk_factors = [f for f in feature_impacts if f["shap_value"] > 0]
        all_protective_factors = [f for f in feature_impacts if f["shap_value"] < 0]

        # Filtrer par seuil de significativité
        significant_risk = [f for f in all_risk_factors if abs(f["shap_value"]) >= MIN_IMPACT_THRESHOLD]
        significant_protective = [f for f in all_protective_factors if abs(f["shap_value"]) >= MIN_IMPACT_THRESHOLD]

        # Garantir un minimum de 2 facteurs par catégorie
        if len(significant_risk) < 2:
            significant_risk = all_risk_factors[:2]
        if len(significant_protective) < 2:
            significant_protective = all_protective_factors[:2]

        # Appliquer les limites selon le profil
        risk_factors = significant_risk[:max_risk]
        protective_factors = significant_protective[:max_protective]

        return ExplainResponse(
            probability=round(proba, 4),
            base_probability=base_probability,
            risk_level=risk_level,
            top_risk_factors=[FeatureImpact(**f) for f in risk_factors],
            top_protective_factors=[FeatureImpact(**f) for f in protective_factors]
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erreur d'explication: {str(e)}")


# =============================================================================
# LANCEMENT (pour tests locaux)
# =============================================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
