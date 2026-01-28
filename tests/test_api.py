# =============================================================================
# TESTS API - Credit Risk Scoring
# =============================================================================
# Tests unitaires pour l'API FastAPI
# Exécution : pytest tests/test_api.py -v
# =============================================================================

import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Ajouter le répertoire parent au path pour importer l'API
sys.path.insert(0, str(Path(__file__).parent.parent))

from api.main import app, load_model

# =============================================================================
# FIXTURES
# =============================================================================

@pytest.fixture(scope="module")
def client():
    """Client de test pour l'API."""
    # Charger le modèle avant les tests
    load_model()
    return TestClient(app)


@pytest.fixture
def valid_client_data():
    """Données client valides pour les tests."""
    return {
        "amt_income_total": 90000,
        "amt_credit": 180000,
        "amt_annuity": 9600,
        "amt_goods_price": 162000,
        "code_gender": "M",
        "days_birth": -16425,  # ~45 ans
        "days_employed": -5475,  # ~15 ans
        "ext_source_1": 0.92,
        "ext_source_2": 0.92,
        "ext_source_3": 0.92
    }


@pytest.fixture
def risky_client_data():
    """Données client à risque pour les tests."""
    return {
        "amt_income_total": 22000,
        "amt_credit": 250000,
        "amt_annuity": 19200,
        "amt_goods_price": 225000,
        "code_gender": "M",
        "days_birth": -8760,  # ~24 ans
        "days_employed": 0,  # sans emploi
        "ext_source_1": 0.18,
        "ext_source_2": 0.18,
        "ext_source_3": 0.18
    }


# =============================================================================
# TESTS ENDPOINT ROOT (/)
# =============================================================================

class TestRootEndpoint:
    """Tests pour l'endpoint racine."""

    def test_root_returns_200(self, client):
        """GET / doit retourner 200."""
        response = client.get("/")
        assert response.status_code == 200

    def test_root_contains_endpoints_info(self, client):
        """GET / doit lister les endpoints disponibles."""
        response = client.get("/")
        data = response.json()
        assert "endpoints" in data
        assert "/health" in data["endpoints"]
        assert "/predict" in data["endpoints"]
        assert "/explain" in data["endpoints"]


# =============================================================================
# TESTS ENDPOINT HEALTH (/health)
# =============================================================================

class TestHealthEndpoint:
    """Tests pour l'endpoint de santé."""

    def test_health_returns_200(self, client):
        """GET /health doit retourner 200."""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_status_healthy(self, client):
        """GET /health doit retourner status=healthy."""
        response = client.get("/health")
        data = response.json()
        assert data["status"] == "healthy"

    def test_health_model_loaded(self, client):
        """GET /health doit confirmer que le modèle est chargé."""
        response = client.get("/health")
        data = response.json()
        assert data["model_loaded"] is True

    def test_health_has_version(self, client):
        """GET /health doit inclure la version du modèle."""
        response = client.get("/health")
        data = response.json()
        assert "model_version" in data
        assert data["model_version"] is not None

    def test_health_has_auc(self, client):
        """GET /health doit inclure l'AUC-ROC."""
        response = client.get("/health")
        data = response.json()
        assert "auc_roc" in data


# =============================================================================
# TESTS ENDPOINT PREDICT (/predict)
# =============================================================================

class TestPredictEndpoint:
    """Tests pour l'endpoint de prédiction."""

    def test_predict_returns_200(self, client, valid_client_data):
        """POST /predict avec données valides doit retourner 200."""
        response = client.post("/predict", json=valid_client_data)
        assert response.status_code == 200

    def test_predict_returns_probability(self, client, valid_client_data):
        """POST /predict doit retourner une probabilité."""
        response = client.post("/predict", json=valid_client_data)
        data = response.json()
        assert "probability" in data
        assert 0 <= data["probability"] <= 1

    def test_predict_returns_prediction(self, client, valid_client_data):
        """POST /predict doit retourner une prédiction binaire."""
        response = client.post("/predict", json=valid_client_data)
        data = response.json()
        assert "prediction" in data
        assert data["prediction"] in [0, 1]

    def test_predict_returns_risk_level(self, client, valid_client_data):
        """POST /predict doit retourner un niveau de risque."""
        response = client.post("/predict", json=valid_client_data)
        data = response.json()
        assert "risk_level" in data
        assert data["risk_level"] in ["Faible", "Moyen", "Élevé"]

    def test_predict_returns_score(self, client, valid_client_data):
        """POST /predict doit retourner un score de crédit."""
        response = client.post("/predict", json=valid_client_data)
        data = response.json()
        assert "score" in data
        assert 300 <= data["score"] <= 850

    def test_predict_reliable_client_low_probability(self, client, valid_client_data):
        """Un client fiable doit avoir une probabilité < 50%."""
        response = client.post("/predict", json=valid_client_data)
        data = response.json()
        assert data["probability"] < 0.50, f"Client fiable a probabilité {data['probability']}"

    def test_predict_risky_client_high_probability(self, client, risky_client_data):
        """Un client risqué doit avoir une probabilité > 50%."""
        response = client.post("/predict", json=risky_client_data)
        data = response.json()
        assert data["probability"] > 0.50, f"Client risqué a probabilité {data['probability']}"

    def test_predict_gender_encoding(self, client, valid_client_data):
        """Le genre doit être correctement encodé (M/F)."""
        # Test avec genre masculin
        valid_client_data["code_gender"] = "M"
        response_m = client.post("/predict", json=valid_client_data)
        assert response_m.status_code == 200

        # Test avec genre féminin
        valid_client_data["code_gender"] = "F"
        response_f = client.post("/predict", json=valid_client_data)
        assert response_f.status_code == 200


# =============================================================================
# TESTS VALIDATION DES INPUTS
# =============================================================================

class TestInputValidation:
    """Tests de validation des données d'entrée."""

    def test_predict_missing_required_field(self, client):
        """POST /predict sans champ requis doit retourner 422."""
        incomplete_data = {
            "amt_credit": 180000
            # amt_income_total manquant
        }
        response = client.post("/predict", json=incomplete_data)
        assert response.status_code == 422

    def test_predict_invalid_type(self, client):
        """POST /predict avec type invalide doit retourner 422."""
        invalid_data = {
            "amt_income_total": "not_a_number",  # devrait être float
            "amt_credit": 180000
        }
        response = client.post("/predict", json=invalid_data)
        assert response.status_code == 422

    def test_predict_with_optional_fields_missing(self, client):
        """POST /predict avec champs optionnels manquants doit fonctionner."""
        minimal_data = {
            "amt_income_total": 50000,
            "amt_credit": 150000
        }
        response = client.post("/predict", json=minimal_data)
        assert response.status_code == 200


# =============================================================================
# TESTS DE COHÉRENCE MÉTIER
# =============================================================================

class TestBusinessLogic:
    """Tests de cohérence métier."""

    def test_higher_ext_source_lower_risk(self, client):
        """Un score externe plus élevé doit réduire le risque."""
        base_data = {
            "amt_income_total": 50000,
            "amt_credit": 150000,
            "amt_annuity": 10000,
            "days_birth": -12000,
            "days_employed": -2000,
        }

        # Client avec bon score externe
        good_score = {**base_data, "ext_source_1": 0.9, "ext_source_2": 0.9, "ext_source_3": 0.9}
        response_good = client.post("/predict", json=good_score)
        prob_good = response_good.json()["probability"]

        # Client avec mauvais score externe
        bad_score = {**base_data, "ext_source_1": 0.2, "ext_source_2": 0.2, "ext_source_3": 0.2}
        response_bad = client.post("/predict", json=bad_score)
        prob_bad = response_bad.json()["probability"]

        assert prob_good < prob_bad, "Score externe élevé devrait réduire le risque"

    def test_score_probability_inverse_relationship(self, client, valid_client_data):
        """Le score de crédit doit être inversement proportionnel à la probabilité."""
        response = client.post("/predict", json=valid_client_data)
        data = response.json()

        # Score élevé = probabilité faible
        if data["probability"] < 0.3:
            assert data["score"] > 650
        elif data["probability"] > 0.7:
            assert data["score"] < 500


# =============================================================================
# TESTS ENDPOINT EXPLAIN (/explain)
# =============================================================================

class TestExplainEndpoint:
    """Tests pour l'endpoint d'explication SHAP."""

    def test_explain_returns_200(self, client, valid_client_data):
        """POST /explain avec données valides doit retourner 200."""
        response = client.post("/explain", json=valid_client_data)
        assert response.status_code == 200

    def test_explain_returns_probability(self, client, valid_client_data):
        """POST /explain doit retourner une probabilité."""
        response = client.post("/explain", json=valid_client_data)
        data = response.json()
        assert "probability" in data
        assert 0 <= data["probability"] <= 1

    def test_explain_returns_base_probability(self, client, valid_client_data):
        """POST /explain doit retourner la probabilité de base."""
        response = client.post("/explain", json=valid_client_data)
        data = response.json()
        assert "base_probability" in data
        assert 0 <= data["base_probability"] <= 1

    def test_explain_returns_risk_factors(self, client, valid_client_data):
        """POST /explain doit retourner les facteurs de risque."""
        response = client.post("/explain", json=valid_client_data)
        data = response.json()
        assert "top_risk_factors" in data
        assert isinstance(data["top_risk_factors"], list)

    def test_explain_returns_protective_factors(self, client, valid_client_data):
        """POST /explain doit retourner les facteurs protecteurs."""
        response = client.post("/explain", json=valid_client_data)
        data = response.json()
        assert "top_protective_factors" in data
        assert isinstance(data["top_protective_factors"], list)

    def test_explain_factor_has_required_fields(self, client, valid_client_data):
        """Chaque facteur doit avoir feature, value, shap_value, impact."""
        response = client.post("/explain", json=valid_client_data)
        data = response.json()

        # Vérifier au moins un facteur de risque ou protecteur
        all_factors = data["top_risk_factors"] + data["top_protective_factors"]
        if len(all_factors) > 0:
            factor = all_factors[0]
            assert "feature" in factor
            assert "value" in factor
            assert "shap_value" in factor
            assert "impact" in factor

    def test_explain_risk_factors_have_positive_shap(self, client, risky_client_data):
        """Les facteurs de risque doivent avoir des SHAP values positifs."""
        response = client.post("/explain", json=risky_client_data)
        data = response.json()

        for factor in data["top_risk_factors"]:
            assert factor["shap_value"] > 0, f"Facteur de risque {factor['feature']} a SHAP négatif"
            assert factor["impact"] == "increases_risk"

    def test_explain_protective_factors_have_negative_shap(self, client, valid_client_data):
        """Les facteurs protecteurs doivent avoir des SHAP values négatifs."""
        response = client.post("/explain", json=valid_client_data)
        data = response.json()

        for factor in data["top_protective_factors"]:
            assert factor["shap_value"] < 0, f"Facteur protecteur {factor['feature']} a SHAP positif"
            assert factor["impact"] == "reduces_risk"


# =============================================================================
# TESTS DE PERFORMANCE
# =============================================================================

class TestPerformance:
    """Tests de performance de l'API."""

    def test_predict_latency(self, client, valid_client_data):
        """POST /predict doit répondre en moins de 500ms."""
        import time

        start = time.time()
        response = client.post("/predict", json=valid_client_data)
        latency = time.time() - start

        assert response.status_code == 200
        assert latency < 0.5, f"Latence trop élevée: {latency:.3f}s"

    def test_health_latency(self, client):
        """GET /health doit répondre en moins de 100ms."""
        import time

        start = time.time()
        response = client.get("/health")
        latency = time.time() - start

        assert response.status_code == 200
        assert latency < 0.1, f"Latence trop élevée: {latency:.3f}s"

    def test_explain_latency(self, client, valid_client_data):
        """POST /explain doit répondre en moins de 2s (SHAP est plus lent)."""
        import time

        start = time.time()
        response = client.post("/explain", json=valid_client_data)
        latency = time.time() - start

        assert response.status_code == 200
        assert latency < 2.0, f"Latence trop élevée: {latency:.3f}s"


# =============================================================================
# MAIN - Exécution directe
# =============================================================================

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
