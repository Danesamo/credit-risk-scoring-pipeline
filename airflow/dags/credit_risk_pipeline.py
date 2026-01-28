# =============================================================================
# CREDIT RISK SCORING - Airflow DAG
# =============================================================================
# Pipeline automatisé pour le projet Credit Risk Scoring
#
# Ce DAG orchestre les tâches suivantes :
# 1. Vérification de la santé de l'API
# 2. Test de prédiction
# 3. Collecte des métriques
# 4. Notification (optionnel)
#
# Exécution : Toutes les heures ou sur demande
# =============================================================================

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests
import json
import pendulum

# =============================================================================
# CONFIGURATION
# =============================================================================

API_URL = "http://api:8000"  # URL interne Docker

default_args = {
    'owner': 'daniela_samo',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2),
}

# =============================================================================
# FONCTIONS DES TÂCHES
# =============================================================================

def check_api_health(**context):
    """
    Vérifie que l'API est en bonne santé.

    Returns:
        dict: Informations sur l'état de l'API
    """
    try:
        response = requests.get(f"{API_URL}/health", timeout=10)
        response.raise_for_status()
        health_data = response.json()

        print(f"✅ API Status: {health_data.get('status')}")
        print(f"✅ Model Loaded: {health_data.get('model_loaded')}")
        print(f"✅ Model Version: {health_data.get('model_version')}")
        print(f"✅ AUC-ROC: {health_data.get('auc_roc')}")

        if health_data.get('status') != 'healthy':
            raise ValueError("API n'est pas en bonne santé!")

        if not health_data.get('model_loaded'):
            raise ValueError("Modèle non chargé!")

        # Passer les données au contexte XCom pour les tâches suivantes
        context['ti'].xcom_push(key='health_data', value=health_data)

        return health_data

    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de connexion à l'API: {e}")
        raise


def test_prediction(**context):
    """
    Effectue une prédiction de test pour vérifier le pipeline.

    Returns:
        dict: Résultat de la prédiction
    """
    # Données de test (profil moyen)
    test_client = {
        "amt_income_total": 50000,
        "amt_credit": 200000,
        "amt_annuity": 12000,
        "amt_goods_price": 180000,
        "code_gender": "M",
        "days_birth": -12775,  # ~35 ans
        "days_employed": -1825,  # ~5 ans
        "ext_source_1": 0.6,
        "ext_source_2": 0.6,
        "ext_source_3": 0.6
    }

    try:
        response = requests.post(
            f"{API_URL}/predict",
            json=test_client,
            timeout=30
        )
        response.raise_for_status()
        prediction = response.json()

        print(f"✅ Test Prediction Results:")
        print(f"   - Probability: {prediction.get('probability'):.2%}")
        print(f"   - Risk Level: {prediction.get('risk_level')}")
        print(f"   - Score: {prediction.get('score')}/850")

        # Vérifications de cohérence
        prob = prediction.get('probability', 0)
        if not (0 <= prob <= 1):
            raise ValueError(f"Probabilité invalide: {prob}")

        score = prediction.get('score', 0)
        if not (300 <= score <= 850):
            raise ValueError(f"Score invalide: {score}")

        context['ti'].xcom_push(key='prediction_result', value=prediction)

        return prediction

    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de prédiction: {e}")
        raise


def collect_metrics(**context):
    """
    Collecte les métriques Prometheus de l'API.

    Returns:
        str: Métriques brutes
    """
    try:
        response = requests.get(f"{API_URL}/metrics", timeout=10)
        response.raise_for_status()
        metrics = response.text

        # Extraire quelques métriques clés
        lines = metrics.split('\n')
        key_metrics = [l for l in lines if l.startswith('credit_risk_') and not l.startswith('#')]

        print(f"✅ Métriques collectées ({len(key_metrics)} métriques)")
        for metric in key_metrics[:10]:  # Afficher les 10 premières
            print(f"   {metric}")

        return metrics

    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur de collecte des métriques: {e}")
        raise


def generate_report(**context):
    """
    Génère un rapport récapitulatif du pipeline.
    """
    ti = context['ti']

    # Récupérer les données des tâches précédentes
    health_data = ti.xcom_pull(key='health_data', task_ids='check_api_health')
    prediction = ti.xcom_pull(key='prediction_result', task_ids='test_prediction')

    report = f"""
    ╔══════════════════════════════════════════════════════════════╗
    ║        CREDIT RISK SCORING - RAPPORT PIPELINE                ║
    ╠══════════════════════════════════════════════════════════════╣
    ║  Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                              ║
    ╠══════════════════════════════════════════════════════════════╣
    ║  SANTÉ API                                                   ║
    ║  ─────────                                                   ║
    ║  • Status: {health_data.get('status', 'N/A') if health_data else 'N/A':12}                                     ║
    ║  • Modèle: {'Chargé' if health_data and health_data.get('model_loaded') else 'Non chargé':12}                                     ║
    ║  • AUC-ROC: {health_data.get('auc_roc', 'N/A') if health_data else 'N/A'}                                        ║
    ╠══════════════════════════════════════════════════════════════╣
    ║  TEST PRÉDICTION                                             ║
    ║  ───────────────                                             ║
    ║  • Probabilité: {prediction.get('probability', 0)*100:.1f}%                                       ║
    ║  • Niveau: {prediction.get('risk_level', 'N/A') if prediction else 'N/A':12}                                     ║
    ║  • Score: {prediction.get('score', 'N/A') if prediction else 'N/A'}/850                                          ║
    ╠══════════════════════════════════════════════════════════════╣
    ║  ✅ PIPELINE EXÉCUTÉ AVEC SUCCÈS                             ║
    ╚══════════════════════════════════════════════════════════════╝
    """

    print(report)
    return report


# =============================================================================
# DÉFINITION DU DAG
# =============================================================================

with DAG(
    dag_id='credit_risk_pipeline',
    default_args=default_args,
    description='Pipeline de monitoring et validation du modèle Credit Risk',
    schedule='@hourly',  # Exécution toutes les heures
    start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
    catchup=False,
    tags=['credit-risk', 'ml', 'monitoring'],
) as dag:

    # Documentation du DAG
    dag.doc_md = """
    # Credit Risk Scoring Pipeline

    Ce DAG automatise les tâches de monitoring et validation du modèle de scoring crédit.

    ## Tâches
    1. **check_api_health**: Vérifie que l'API est opérationnelle
    2. **test_prediction**: Effectue une prédiction de test
    3. **collect_metrics**: Collecte les métriques Prometheus
    4. **generate_report**: Génère un rapport récapitulatif

    ## Schedule
    - Exécution automatique: Toutes les heures
    - Exécution manuelle: Possible via l'interface Airflow

    ## Auteur
    Daniela Samo - 2026
    """

    # Tâche 1: Vérifier la santé de l'API
    task_health = PythonOperator(
        task_id='check_api_health',
        python_callable=check_api_health,
        doc_md="Vérifie que l'API FastAPI est en bonne santé et que le modèle est chargé."
    )

    # Tâche 2: Test de prédiction
    task_predict = PythonOperator(
        task_id='test_prediction',
        python_callable=test_prediction,
        doc_md="Effectue une prédiction de test avec un profil client standard."
    )

    # Tâche 3: Collecte des métriques
    task_metrics = PythonOperator(
        task_id='collect_metrics',
        python_callable=collect_metrics,
        doc_md="Collecte les métriques Prometheus exposées par l'API."
    )

    # Tâche 4: Génération du rapport
    task_report = PythonOperator(
        task_id='generate_report',
        python_callable=generate_report,
        doc_md="Génère un rapport récapitulatif de l'exécution du pipeline."
    )

    # Définir les dépendances (ordre d'exécution)
    task_health >> task_predict >> task_metrics >> task_report
