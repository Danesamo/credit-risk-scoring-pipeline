# =============================================================================
# CREDIT RISK SCORING - Interface Streamlit (MODE STANDALONE)
# =============================================================================
# Interface multilingue (FR/EN) et multi-devises (XAF/XOF/EUR/USD)
# Design: Épuré, impactant, orienté métier, international
# Mode: Standalone - charge le modèle directement sans API
# =============================================================================

import streamlit as st
import os
import json
import joblib
import numpy as np
import pandas as pd
import shap
from pathlib import Path

# =============================================================================
# CONFIGURATION - MODE STANDALONE
# =============================================================================

# Chemins vers les artefacts du modèle
BASE_DIR = Path(__file__).parent.parent
MODELS_DIR = BASE_DIR / "models"

MODEL_PATH = MODELS_DIR / "xgboost_credit_risk_v1.pkl"
FEATURES_PATH = MODELS_DIR / "feature_names.json"
METRICS_PATH = MODELS_DIR / "metrics.json"

# =============================================================================
# CHARGEMENT DU MODÈLE (cache pour performance)
# =============================================================================

@st.cache_resource
def load_model():
    """Charge le modèle XGBoost et crée l'explainer SHAP."""
    model = joblib.load(MODEL_PATH)
    with open(FEATURES_PATH, 'r') as f:
        feature_names = json.load(f)
    shap_explainer = shap.TreeExplainer(model)
    return model, feature_names, shap_explainer

# Charger au démarrage
MODEL, FEATURE_NAMES_LIST, SHAP_EXPLAINER = load_model()

# Taux de conversion vers EUR (base)
EXCHANGE_RATES = {
    "EUR": 1.0,
    "USD": 1.08,
    "XAF": 655.957,  # CEMAC - Afrique Centrale
    "XOF": 655.957,  # UEMOA - Afrique de l'Ouest
}

CURRENCY_SYMBOLS = {
    "EUR": "€",
    "USD": "$",
    "XAF": "FCFA",
    "XOF": "FCFA",
}

CURRENCY_INFO = {
    "EUR": "Euro - Europe",
    "USD": "Dollar US - Amérique",
    "XAF": "Franc CFA - CEMAC (Afrique Centrale)",
    "XOF": "Franc CFA - UEMOA (Afrique de l'Ouest)",
}

# =============================================================================
# MAPPING DES FEATURES TECHNIQUES → NOMS COMPRÉHENSIBLES
# =============================================================================

FEATURE_NAMES = {
    "fr": {
        "ext_source_mean": "Historique de crédit",
        "ext_source_1": "Score de crédit externe",
        "ext_source_2": "Score de crédit externe",
        "ext_source_3": "Score de crédit externe",
        "ext_source_max": "Meilleur score crédit",
        "ext_source_min": "Score crédit minimum",
        "credit_income_ratio": "Ratio crédit/revenus",
        "annuity_income_ratio": "Poids des mensualités",
        "credit_annuity_ratio": "Durée du crédit",
        "goods_credit_ratio": "Valeur du bien financé",
        "age_years": "Âge et maturité",
        "employed_years": "Ancienneté professionnelle",
        "days_birth": "Âge du demandeur",
        "days_employed": "Stabilité professionnelle",
        "amt_income_total": "Niveau de revenus",
        "amt_credit": "Montant du crédit",
        "amt_annuity": "Mensualité demandée",
        "amt_goods_price": "Prix du bien",
        "code_gender": "Profil démographique",
        "name_education_type": "Niveau d'études",
        "instal_late_ratio": "Retards de paiement passés",
        "instal_late_count": "Nombre de retards",
        "instal_payment_ratio": "Régularité des paiements",
        "bureau_credit_count": "Nombre de crédits",
        "bureau_debt_sum": "Endettement total",
        "bureau_active_ratio": "Crédits actifs",
        "prev_app_count": "Demandes précédentes",
        "prev_approval_rate": "Taux d'acceptation passé",
        "cc_utilization_mean": "Utilisation carte crédit",
        "pos_dpd_ratio": "Incidents de paiement",
        "id_publish_to_age": "Âge lors de l'identification",
        "bureau_amt_credit_sum_mean": "Montant moyen des crédits",
        "cc_payment_to_balance_ratio": "Ratio paiement carte",
        "own_car_age": "Âge du véhicule",
        "bureau_credit_active_count": "Crédits actifs",
        "bureau_credit_closed_count": "Crédits remboursés",
        "bureau_days_credit_mean": "Ancienneté moyenne crédits",
        "prev_amt_credit_mean": "Montant moyen demandé",
        "prev_cnt_refused": "Demandes refusées",
        "instal_amt_payment_sum": "Total remboursé",
        "instal_days_late_mean": "Retard moyen (jours)",
        "pos_months_balance_mean": "Ancienneté POS",
        "cc_balance_mean": "Solde moyen carte",
        "cc_drawings_count": "Nombre de retraits",
        "days_registration": "Ancienneté du dossier",
        "days_id_publish": "Ancienneté pièce d'identité",
        "region_rating_client": "Note région client",
        "hour_appr_process_start": "Heure de la demande",
        "reg_city_not_work_city": "Ville différente du travail",
        "flag_own_car": "Propriétaire véhicule",
        "flag_own_realty": "Propriétaire immobilier",
        "cnt_children": "Nombre d'enfants",
        "cnt_fam_members": "Taille du foyer",
    },
    "en": {
        "ext_source_mean": "Credit history",
        "ext_source_1": "External credit score",
        "ext_source_2": "External credit score",
        "ext_source_3": "External credit score",
        "ext_source_max": "Best credit score",
        "ext_source_min": "Minimum credit score",
        "credit_income_ratio": "Credit/income ratio",
        "annuity_income_ratio": "Monthly payment burden",
        "credit_annuity_ratio": "Loan duration",
        "goods_credit_ratio": "Financed asset value",
        "age_years": "Age and maturity",
        "employed_years": "Professional experience",
        "days_birth": "Applicant age",
        "days_employed": "Job stability",
        "amt_income_total": "Income level",
        "amt_credit": "Credit amount",
        "amt_annuity": "Requested payment",
        "amt_goods_price": "Asset price",
        "code_gender": "Demographic profile",
        "name_education_type": "Education level",
        "instal_late_ratio": "Past payment delays",
        "instal_late_count": "Number of delays",
        "instal_payment_ratio": "Payment regularity",
        "bureau_credit_count": "Number of credits",
        "bureau_debt_sum": "Total debt",
        "bureau_active_ratio": "Active credits",
        "prev_app_count": "Previous applications",
        "prev_approval_rate": "Past approval rate",
        "cc_utilization_mean": "Credit card usage",
        "pos_dpd_ratio": "Payment incidents",
        "id_publish_to_age": "Age at ID issuance",
        "bureau_amt_credit_sum_mean": "Average credit amount",
        "cc_payment_to_balance_ratio": "Card payment ratio",
        "own_car_age": "Vehicle age",
        "bureau_credit_active_count": "Active credits",
        "bureau_credit_closed_count": "Closed credits",
        "bureau_days_credit_mean": "Average credit history",
        "prev_amt_credit_mean": "Average requested amount",
        "prev_cnt_refused": "Refused applications",
        "instal_amt_payment_sum": "Total repaid",
        "instal_days_late_mean": "Average delay (days)",
        "pos_months_balance_mean": "POS account age",
        "cc_balance_mean": "Average card balance",
        "cc_drawings_count": "Number of withdrawals",
        "days_registration": "File registration age",
        "days_id_publish": "ID document age",
        "region_rating_client": "Client region rating",
        "hour_appr_process_start": "Application hour",
        "reg_city_not_work_city": "Different work city",
        "flag_own_car": "Vehicle owner",
        "flag_own_realty": "Property owner",
        "cnt_children": "Number of children",
        "cnt_fam_members": "Family size",
    }
}

# Descriptions contextuelles des facteurs
FEATURE_DESCRIPTIONS = {
    "fr": {
        "ext_source_mean": "Votre historique de remboursement auprès d'autres établissements",
        "credit_income_ratio": "Le montant demandé par rapport à vos revenus annuels",
        "annuity_income_ratio": "La part de vos revenus consacrée au remboursement",
        "age_years": "L'expérience financière liée à votre âge",
        "days_employed": "La stabilité de votre situation professionnelle",
        "amt_income_total": "Votre capacité financière globale",
        "instal_late_ratio": "Votre comportement de paiement passé",
        "name_education_type": "Votre niveau de formation",
    },
    "en": {
        "ext_source_mean": "Your repayment history with other institutions",
        "credit_income_ratio": "The requested amount relative to your annual income",
        "annuity_income_ratio": "The share of income dedicated to repayment",
        "age_years": "Financial experience related to your age",
        "days_employed": "The stability of your professional situation",
        "amt_income_total": "Your overall financial capacity",
        "instal_late_ratio": "Your past payment behavior",
        "name_education_type": "Your education level",
    }
}

# =============================================================================
# TRADUCTIONS
# =============================================================================

TRANSLATIONS = {
    "fr": {
        "title": "Credit Risk Scoring",
        "subtitle": "Évaluez le risque de défaut en quelques secondes",
        "client_info": "Informations du client",
        "annual_income": "Revenus annuels",
        "credit_amount": "Montant du crédit",
        "monthly_payment": "Mensualité",
        "client_age": "Âge du client",
        "employment_years": "Ancienneté emploi (années)",
        "external_score": "Score crédit externe",
        "example_profiles": "Exemples de profils",
        "reliable_profile": "Profil Fiable",
        "medium_profile": "Profil Moyen",
        "risky_profile": "Profil Risqué",
        "analyze_risk": "Analyser le risque",
        "analyzing": "Analyse en cours...",
        "credit_score": "Score de crédit",
        "default_probability": "Probabilité de défaut",
        "risk_level": "Niveau de risque",
        "risk_indicator": "Indicateur de risque",
        "key_factors": "Facteurs clés",
        "positive_points": "Points positifs",
        "attention_points": "Points d'attention",
        "technical_details": "Détails techniques",
        "low_risk": "Risque faible",
        "medium_risk": "Risque modéré",
        "high_risk": "Risque élevé",
        "credit_recommended": "Crédit recommandé",
        "further_study": "Étude approfondie",
        "credit_not_recommended": "Crédit déconseillé",
        "reliable_client": "Ce client présente un profil fiable.",
        "needs_analysis": "Ce dossier nécessite une analyse complémentaire.",
        "high_risk_client": "Le risque de défaut est trop élevé.",
        "good_credit_history": "Bon historique de crédit",
        "stable_employment": "Emploi stable",
        "comfortable_income": "Revenus confortables",
        "controlled_debt": "Endettement maîtrisé",
        "limited_credit_history": "Historique crédit limité",
        "low_employment_seniority": "Ancienneté emploi faible",
        "modest_income": "Revenus modestes",
        "high_debt": "Endettement élevé",
        "vs_average": "vs moyenne",
        "language": "Langue",
        "currency": "Devise",
        "settings": "Paramètres",
        "copyright": "© 2026 Daniela Samo. Tous droits réservés.",
        "model": "Modèle XGBoost",
        "help_income": "Revenus totaux annuels du client",
        "help_credit": "Montant total du crédit demandé",
        "help_monthly": "Montant de la mensualité",
        "help_age": "Âge du demandeur",
        "help_employment": "Nombre d'années dans l'emploi actuel",
        "help_score": "Score de crédit externe (0 = mauvais, 1 = excellent)",
        "api_unavailable": "API non disponible. Lancez: uvicorn api.main:app --reload",
        "current_profile": "Profil actif",
        "risk_position": "Position actuelle",
        "default_risk": "de risque de défaut",
        "detailed_analysis": "Analyse détaillée de votre profil",
        "your_strengths": "Vos atouts",
        "watch_points": "Points de vigilance",
        "factors_count": "facteurs",
        "strong_impact": "Impact fort",
        "medium_impact": "Impact modéré",
        "low_impact": "Impact faible",
        "recommendation": "Recommandation",
        "recommendation_low": "Votre profil est solide. Vous pouvez envisager sereinement votre demande de crédit.",
        "recommendation_medium": "Quelques points méritent attention. Un apport personnel plus important ou une durée plus longue pourrait améliorer votre dossier.",
        "recommendation_high": "Nous vous conseillons de réduire le montant demandé ou d'améliorer votre situation avant de faire une demande.",
        "no_factors": "Aucun facteur significatif identifié",
        "see_details": "Voir le détail",
        "hide_details": "Masquer le détail",
    },
    "en": {
        "title": "Credit Risk Scoring",
        "subtitle": "Assess default risk in seconds",
        "client_info": "Client Information",
        "annual_income": "Annual Income",
        "credit_amount": "Credit Amount",
        "monthly_payment": "Monthly Payment",
        "client_age": "Client Age",
        "employment_years": "Employment (years)",
        "external_score": "External Credit Score",
        "example_profiles": "Example Profiles",
        "reliable_profile": "Reliable Profile",
        "medium_profile": "Medium Profile",
        "risky_profile": "Risky Profile",
        "analyze_risk": "Analyze Risk",
        "analyzing": "Analyzing...",
        "credit_score": "Credit Score",
        "default_probability": "Default Probability",
        "risk_level": "Risk Level",
        "risk_indicator": "Risk Indicator",
        "key_factors": "Key Factors",
        "positive_points": "Positive Points",
        "attention_points": "Points of Attention",
        "technical_details": "Technical Details",
        "low_risk": "Low Risk",
        "medium_risk": "Medium Risk",
        "high_risk": "High Risk",
        "credit_recommended": "Credit Recommended",
        "further_study": "Further Study Required",
        "credit_not_recommended": "Credit Not Recommended",
        "reliable_client": "This client has a reliable profile.",
        "needs_analysis": "This application requires further analysis.",
        "high_risk_client": "Default risk is too high.",
        "good_credit_history": "Good credit history",
        "stable_employment": "Stable employment",
        "comfortable_income": "Comfortable income",
        "controlled_debt": "Controlled debt",
        "limited_credit_history": "Limited credit history",
        "low_employment_seniority": "Low employment seniority",
        "modest_income": "Modest income",
        "high_debt": "High debt ratio",
        "vs_average": "vs average",
        "language": "Language",
        "currency": "Currency",
        "settings": "Settings",
        "copyright": "© 2026 Daniela Samo. All rights reserved.",
        "model": "XGBoost Model",
        "help_income": "Client's total annual income",
        "help_credit": "Total credit amount requested",
        "help_monthly": "Monthly payment amount",
        "help_age": "Applicant's age",
        "help_employment": "Years in current employment",
        "help_score": "External credit score (0 = poor, 1 = excellent)",
        "api_unavailable": "API unavailable. Run: uvicorn api.main:app --reload",
        "current_profile": "Active profile",
        "risk_position": "Current position",
        "default_risk": "default risk",
        "detailed_analysis": "Detailed analysis of your profile",
        "your_strengths": "Your strengths",
        "watch_points": "Points to watch",
        "factors_count": "factors",
        "strong_impact": "Strong impact",
        "medium_impact": "Medium impact",
        "low_impact": "Low impact",
        "recommendation": "Recommendation",
        "recommendation_low": "Your profile is solid. You can confidently proceed with your credit application.",
        "recommendation_medium": "A few points need attention. A larger down payment or longer term could strengthen your application.",
        "recommendation_high": "We advise reducing the requested amount or improving your situation before applying.",
        "no_factors": "No significant factors identified",
        "see_details": "See details",
        "hide_details": "Hide details",
    }
}

# =============================================================================
# CONFIGURATION PAGE
# =============================================================================

st.set_page_config(
    page_title="Credit Risk Scoring",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="expanded"
)

# =============================================================================
# STYLES CSS
# =============================================================================

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Cards pour l'analyse SHAP */
    .shap-card {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 0.75rem 0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        border-left: 4px solid #3b82f6;
    }

    .shap-card-positive {
        border-left-color: #10b981;
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
    }

    .shap-card-negative {
        border-left-color: #f59e0b;
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
    }

    .shap-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.5rem;
    }

    .shap-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1e293b;
        margin: 0;
    }

    .shap-impact {
        font-size: 0.75rem;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-weight: 500;
    }

    .impact-strong {
        background-color: #dbeafe;
        color: #1d4ed8;
    }

    .impact-medium {
        background-color: #e0e7ff;
        color: #4338ca;
    }

    .impact-low {
        background-color: #f1f5f9;
        color: #64748b;
    }

    .shap-description {
        font-size: 0.9rem;
        color: #64748b;
        margin-top: 0.5rem;
        line-height: 1.4;
    }

    .shap-bar-container {
        height: 8px;
        background-color: #e2e8f0;
        border-radius: 4px;
        margin-top: 0.75rem;
        overflow: hidden;
    }

    .shap-bar-positive {
        height: 100%;
        background: linear-gradient(90deg, #10b981 0%, #34d399 100%);
        border-radius: 4px;
        transition: width 0.5s ease-out;
    }

    .shap-bar-negative {
        height: 100%;
        background: linear-gradient(90deg, #f59e0b 0%, #fbbf24 100%);
        border-radius: 4px;
        transition: width 0.5s ease-out;
    }

    /* Summary cards */
    .summary-card {
        background: white;
        border-radius: 12px;
        padding: 1.25rem;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    .summary-card-green {
        border: 2px solid #10b981;
    }

    .summary-card-orange {
        border: 2px solid #f59e0b;
    }

    .summary-number {
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
    }

    .summary-label {
        font-size: 0.85rem;
        color: #64748b;
        margin-top: 0.25rem;
    }

    /* Recommendation box */
    .recommendation-box {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-radius: 12px;
        padding: 1.25rem;
        margin-top: 1rem;
        border-left: 4px solid #3b82f6;
    }

    .recommendation-title {
        font-size: 1rem;
        font-weight: 600;
        color: #1e40af;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .recommendation-text {
        font-size: 0.95rem;
        color: #1e293b;
        line-height: 1.5;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# PROFILS PRÉ-DÉFINIS PAR DEVISE - Basés sur données réelles 2024-2025
# =============================================================================
# Sources :
# - CEMAC/UEMOA : AfricaPaieRH, ANSD Sénégal, SikaFinance
# - Europe : Eurostat, INSEE, Connexion-Emploi
# - USA : Bureau of Labor Statistics, Indeed, WorldSalaries
#
# Contexte économique :
# - XAF (CEMAC) : SMIG moyen ~83 000 FCFA, Cadre sup ~1 200 000 FCFA/mois
# - XOF (UEMOA) : SMIG moyen ~55 000 FCFA, Cadre sup ~933 000 FCFA/mois
# - EUR : SMIC ~2 000 €, Cadre sup ~6 000 €/mois
# - USD : Minimum ~$2 500, Senior Manager ~$13 000/mois
#
# Les profils illustrent 3 niveaux de décision:
# - Fiable: Crédit recommandé (mensualité < 20% revenus)
# - Moyen: Étude approfondie (mensualité 25-35% revenus)
# - Risqué: Crédit déconseillé (mensualité > 100% revenus!)
# =============================================================================

PROFILES_BY_CURRENCY = {
    # =========================================================================
    # FCFA - Afrique Centrale (XAF) - Zone CEMAC
    # Cameroun, Gabon, Congo, Tchad, RCA, Guinée Équatoriale
    # =========================================================================
    "XAF": {
        "fiable": {
            # Cadre supérieur / Directeur / Manager senior
            # Référence : Analystes financiers, hauts fonctionnaires
            # Objectif : Probabilité < 35% → "Crédit recommandé"
            "revenus": 14400000,    # 1 200 000 FCFA/mois
            "credit": 35000000,     # Crédit immobilier (terrain + construction)
            "annuite": 280000,      # Mensualité ~23% revenus mensuels
            "age": 45,
            "anciennete": 15,
            "score": 0.85           # Excellent historique
        },
        "moyen": {
            # Cadre moyen / Fonctionnaire catégorie A / Technicien senior
            # Référence : Développeurs, comptables, enseignants du supérieur
            # Objectif : Probabilité 40-55% → "Étude approfondie"
            "revenus": 6000000,     # 500 000 FCFA/mois
            "credit": 15000000,     # Crédit auto ou petit immobilier
            "annuite": 150000,      # Mensualité 30% revenus mensuels
            "age": 35,
            "anciennete": 4,        # Ancienneté moyenne
            "score": 0.62           # Historique crédit correct mais pas excellent
        },
        "risque": {
            # Jeune diplômé / Travailleur informel / Débutant
            # Référence : Proche du SMIG (~70 000 FCFA moyenne CEMAC)
            # Objectif : Probabilité > 60% → "Crédit déconseillé"
            "revenus": 1200000,     # 100 000 FCFA/mois
            "credit": 5000000,      # Crédit trop ambitieux
            "annuite": 120000,      # Mensualité = 120% revenus mensuels!
            "age": 24,
            "anciennete": 0,
            "score": 0.15           # Mauvais historique ou pas d'historique
        }
    },

    # =========================================================================
    # FCFA - Afrique de l'Ouest (XOF) - Zone UEMOA
    # Sénégal, Côte d'Ivoire, Mali, Burkina Faso, Bénin, Togo, Niger
    # Salaires légèrement inférieurs à la CEMAC en moyenne
    # =========================================================================
    "XOF": {
        "fiable": {
            # Cadre supérieur - Référence ANSD : 11 200 000 FCFA/an
            # Objectif : Probabilité < 35% → "Crédit recommandé"
            "revenus": 14400000,    # 1 200 000 FCFA/mois (haut de fourchette)
            "credit": 35000000,     # Crédit immobilier
            "annuite": 280000,      # Mensualité ~23% revenus
            "age": 45,
            "anciennete": 15,
            "score": 0.85           # Excellent historique
        },
        "moyen": {
            # Cadre moyen / Fonctionnaire
            # Objectif : Probabilité 40-55% → "Étude approfondie"
            "revenus": 6000000,     # 500 000 FCFA/mois
            "credit": 15000000,     # Crédit véhicule/équipement
            "annuite": 150000,      # Mensualité 30% revenus
            "age": 35,
            "anciennete": 4,        # Ancienneté moyenne
            "score": 0.62           # Historique correct mais pas excellent
        },
        "risque": {
            # Débutant - SMIG Côte d'Ivoire : 75 000 FCFA
            # Objectif : Probabilité > 60% → "Crédit déconseillé"
            "revenus": 1200000,     # 100 000 FCFA/mois
            "credit": 5000000,      # Surendettement
            "annuite": 120000,      # Mensualité 120% revenus!
            "age": 24,
            "anciennete": 0,
            "score": 0.15           # Mauvais historique
        }
    },

    # =========================================================================
    # EUR - Europe (France, Allemagne, Belgique, etc.)
    # SMIC France : 1 802 €, Allemagne : 2 161 €
    # Cadre moyen France : 4 570 € net, Allemagne : 5 000-6 000 € brut
    # =========================================================================
    "EUR": {
        "fiable": {
            # Cadre supérieur / Directeur - Top 10% des salaires
            # Objectif : Probabilité < 35% → "Crédit recommandé"
            "revenus": 72000,       # 6 000 €/mois
            "credit": 180000,       # Crédit immobilier
            "annuite": 900,         # Mensualité 15% revenus
            "age": 45,
            "anciennete": 15,
            "score": 0.85           # Excellent historique
        },
        "moyen": {
            # Cadre moyen / Employé qualifié
            # Objectif : Probabilité 40-55% → "Étude approfondie"
            "revenus": 42000,       # 3 500 €/mois
            "credit": 120000,       # Crédit immobilier modeste
            "annuite": 600,         # Mensualité ~17% revenus
            "age": 35,
            "anciennete": 4,        # Ancienneté moyenne
            "score": 0.62           # Historique correct mais pas excellent
        },
        "risque": {
            # Travailleur au SMIC / Intérimaire / Étudiant
            # Objectif : Probabilité > 60% → "Crédit déconseillé"
            "revenus": 24000,       # 2 000 €/mois (SMIC)
            "credit": 60000,        # Crédit trop élevé pour ses moyens
            "annuite": 700,         # Mensualité 35% revenus - limite haute
            "age": 24,
            "anciennete": 0,
            "score": 0.15           # Mauvais historique
        }
    },

    # =========================================================================
    # USD - États-Unis
    # Salaire médian : $62 088/an, Manager : $106-137k, Senior : $170k
    # =========================================================================
    "USD": {
        "fiable": {
            # Senior Manager / Director - Top earners
            # Objectif : Probabilité < 35% → "Crédit recommandé"
            "revenus": 156000,      # $13 000/mois
            "credit": 400000,       # Mortgage typique USA
            "annuite": 2000,        # Monthly payment ~15% income
            "age": 45,
            "anciennete": 15,
            "score": 0.85           # Excellent historique
        },
        "moyen": {
            # Manager / Professional
            # Objectif : Probabilité 40-55% → "Étude approfondie"
            "revenus": 90000,       # $7 500/mois
            "credit": 250000,       # Home loan
            "annuite": 1300,        # Monthly payment ~17% income
            "age": 35,
            "anciennete": 4,        # Ancienneté moyenne
            "score": 0.62           # Historique correct mais pas excellent
        },
        "risque": {
            # Entry-level / Service worker
            # Objectif : Probabilité > 60% → "Crédit déconseillé"
            "revenus": 42000,       # $3 500/mois
            "credit": 120000,       # Overleveraged
            "annuite": 1400,        # Payment ~33% income - high risk
            "age": 24,
            "anciennete": 0,
            "score": 0.15           # Mauvais historique
        }
    }
}

def get_profiles_for_currency(currency):
    """Retourne les profils adaptés à la devise sélectionnée."""
    return PROFILES_BY_CURRENCY.get(currency, PROFILES_BY_CURRENCY["XAF"])

# Initialiser le profil sélectionné si non existant
if 'selected_profile' not in st.session_state:
    st.session_state.selected_profile = None

# Profil actif (pour affichage - persiste après sélection)
if 'active_profile' not in st.session_state:
    st.session_state.active_profile = None

# =============================================================================
# SIDEBAR - PARAMÈTRES
# =============================================================================

with st.sidebar:
    st.markdown("## ⚙️ Settings / Paramètres")

    # Sélecteur de langue
    lang = st.selectbox(
        "🌍 Language / Langue",
        options=["fr", "en"],
        format_func=lambda x: "🇫🇷 Français" if x == "fr" else "🇬🇧 English",
        index=0
    )

    # Sélecteur de devise (XAF par défaut)
    currency = st.selectbox(
        "💱 Currency / Devise",
        options=["XAF", "XOF", "EUR", "USD"],
        format_func=lambda x: f"{CURRENCY_SYMBOLS[x]} - {CURRENCY_INFO[x]}",
        index=0  # XAF par défaut
    )

    st.markdown("---")

    # Info sur la devise
    st.info(f"**{currency}** = {EXCHANGE_RATES[currency]} pour 1 EUR")

    st.markdown("---")
    st.markdown(
        f"""
        **Credit Risk Scoring v1.0**

        {TRANSLATIONS[lang]['model']}
        AUC-ROC: 0.7836

        ---

        {TRANSLATIONS[lang]['copyright']}
        """
    )

# Raccourci pour les traductions
T = TRANSLATIONS[lang]

# =============================================================================
# FONCTIONS UTILITAIRES
# =============================================================================

def convert_to_eur(amount, from_currency):
    """Convertit un montant vers EUR."""
    return amount / EXCHANGE_RATES[from_currency]

def convert_from_eur(amount, to_currency):
    """Convertit un montant depuis EUR."""
    return amount * EXCHANGE_RATES[to_currency]

def format_currency(amount, curr):
    """Formate un montant avec le symbole de devise."""
    if curr in ["XAF", "XOF"]:
        return f"{amount:,.0f} {CURRENCY_SYMBOLS[curr]}"
    elif curr == "EUR":
        return f"{amount:,.0f} {CURRENCY_SYMBOLS[curr]}"
    else:
        return f"{CURRENCY_SYMBOLS[curr]}{amount:,.0f}"

def get_risk_color(probability):
    """Retourne la couleur et le label selon le niveau de risque."""
    # Seuils ajustés au comportement réel du modèle XGBoost
    # Le modèle donne rarement < 30% même pour de bons profils
    if probability < 0.40:
        return "#10b981", T["low_risk"]
    elif probability < 0.55:
        return "#f59e0b", T["medium_risk"]
    else:
        return "#ef4444", T["high_risk"]

def get_decision(probability):
    """Retourne la décision métier."""
    # Seuils métier réalistes
    if probability < 0.40:
        return f"✅ {T['credit_recommended']}", T["reliable_client"]
    elif probability < 0.55:
        return f"⚠️ {T['further_study']}", T["needs_analysis"]
    else:
        return f"❌ {T['credit_not_recommended']}", T["high_risk_client"]

def call_api(data):
    """Prédiction directe avec le modèle (mode standalone)."""
    try:
        # Créer un DataFrame avec toutes les features
        df = pd.DataFrame({col: [0.0] for col in FEATURE_NAMES_LIST})

        # Mapping des champs
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
            if api_field in data and data[api_field] is not None:
                if model_field in FEATURE_NAMES_LIST:
                    df.loc[0, model_field] = float(data[api_field])

        # Encoder code_gender
        if 'code_gender' in data and 'code_gender' in FEATURE_NAMES_LIST:
            df.loc[0, 'code_gender'] = 1.0 if data['code_gender'] == 'M' else 0.0

        # Features dérivées ext_source
        ext_sources = [data.get('ext_source_1') or 0, data.get('ext_source_2') or 0, data.get('ext_source_3') or 0]
        valid_sources = [float(s) for s in ext_sources if s and s > 0]

        if valid_sources:
            if 'ext_source_mean' in FEATURE_NAMES_LIST:
                df.loc[0, 'ext_source_mean'] = float(np.mean(valid_sources))
            if 'ext_source_max' in FEATURE_NAMES_LIST:
                df.loc[0, 'ext_source_max'] = float(max(valid_sources))
            if 'ext_source_min' in FEATURE_NAMES_LIST:
                df.loc[0, 'ext_source_min'] = float(min(valid_sources))

        # Prédiction
        proba = MODEL.predict_proba(df)[0][1]

        # Niveau de risque et score
        if proba < 0.3:
            risk_level = "Faible"
        elif proba < 0.6:
            risk_level = "Moyen"
        else:
            risk_level = "Élevé"

        score = int(850 - (proba * 550))
        score = max(300, min(850, score))

        return {
            "probability": round(proba, 4),
            "prediction": int(proba >= 0.5),
            "risk_level": risk_level,
            "score": score
        }, None

    except Exception as e:
        return None, str(e)

def call_explain_api(data):
    """Explication SHAP directe (mode standalone)."""
    try:
        # Créer un DataFrame avec toutes les features
        df = pd.DataFrame({col: [0.0] for col in FEATURE_NAMES_LIST})

        # Mapping des champs
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

        for api_field, model_field in field_mapping.items():
            if api_field in data and data[api_field] is not None:
                if model_field in FEATURE_NAMES_LIST:
                    df.loc[0, model_field] = float(data[api_field])

        if 'code_gender' in data and 'code_gender' in FEATURE_NAMES_LIST:
            df.loc[0, 'code_gender'] = 1.0 if data['code_gender'] == 'M' else 0.0

        ext_sources = [data.get('ext_source_1') or 0, data.get('ext_source_2') or 0, data.get('ext_source_3') or 0]
        valid_sources = [float(s) for s in ext_sources if s and s > 0]

        if valid_sources:
            if 'ext_source_mean' in FEATURE_NAMES_LIST:
                df.loc[0, 'ext_source_mean'] = float(np.mean(valid_sources))
            if 'ext_source_max' in FEATURE_NAMES_LIST:
                df.loc[0, 'ext_source_max'] = float(max(valid_sources))
            if 'ext_source_min' in FEATURE_NAMES_LIST:
                df.loc[0, 'ext_source_min'] = float(min(valid_sources))

        # Prédiction
        proba = MODEL.predict_proba(df)[0][1]

        if proba < 0.3:
            risk_level = "Faible"
        elif proba < 0.6:
            risk_level = "Moyen"
        else:
            risk_level = "Élevé"

        # SHAP values
        shap_values = SHAP_EXPLAINER.shap_values(df)
        if isinstance(shap_values, list):
            shap_vals = shap_values[1][0]
        else:
            shap_vals = shap_values[0]

        # Feature impacts
        feature_impacts = []
        for i, feat in enumerate(FEATURE_NAMES_LIST):
            if abs(shap_vals[i]) > 0.001:
                feature_impacts.append({
                    "feature": feat,
                    "value": float(df.loc[0, feat]),
                    "shap_value": float(shap_vals[i]),
                    "impact": "increases_risk" if shap_vals[i] > 0 else "reduces_risk"
                })

        feature_impacts.sort(key=lambda x: abs(x["shap_value"]), reverse=True)

        # Filtrage dynamique selon le profil
        MIN_IMPACT_THRESHOLD = 0.025
        if proba < 0.40:
            max_protective, max_risk = 6, 3
        elif proba < 0.55:
            max_protective, max_risk = 4, 4
        else:
            max_protective, max_risk = 3, 6

        all_risk = [f for f in feature_impacts if f["shap_value"] > 0]
        all_protective = [f for f in feature_impacts if f["shap_value"] < 0]

        sig_risk = [f for f in all_risk if abs(f["shap_value"]) >= MIN_IMPACT_THRESHOLD]
        sig_protective = [f for f in all_protective if abs(f["shap_value"]) >= MIN_IMPACT_THRESHOLD]

        if len(sig_risk) < 2:
            sig_risk = all_risk[:2]
        if len(sig_protective) < 2:
            sig_protective = all_protective[:2]

        return {
            "probability": round(proba, 4),
            "base_probability": 0.0807,
            "risk_level": risk_level,
            "top_risk_factors": sig_risk[:max_risk],
            "top_protective_factors": sig_protective[:max_protective]
        }, None

    except Exception as e:
        return None, str(e)

def get_feature_display_name(feature_key, language):
    """Retourne le nom affichable d'une feature."""
    return FEATURE_NAMES.get(language, {}).get(feature_key, feature_key.replace("_", " ").title())

def get_feature_description(feature_key, language):
    """Retourne la description d'une feature."""
    return FEATURE_DESCRIPTIONS.get(language, {}).get(feature_key, "")

def get_impact_level(shap_value):
    """Détermine le niveau d'impact basé sur la valeur SHAP."""
    abs_val = abs(shap_value)
    if abs_val >= 0.15:
        return "strong"
    elif abs_val >= 0.05:
        return "medium"
    else:
        return "low"

def render_shap_card(factor, is_positive, language, T):
    """Génère le HTML pour une card de facteur SHAP."""
    feature = factor.get("feature", "unknown")
    shap_value = factor.get("shap_value", 0)

    # Nom et description lisibles
    display_name = get_feature_display_name(feature, language)
    description = get_feature_description(feature, language)

    # Niveau d'impact
    impact_level = get_impact_level(shap_value)
    if impact_level == "strong":
        impact_label = T["strong_impact"]
        impact_class = "impact-strong"
    elif impact_level == "medium":
        impact_label = T["medium_impact"]
        impact_class = "impact-medium"
    else:
        impact_label = T["low_impact"]
        impact_class = "impact-low"

    # Classe de la card
    card_class = "shap-card-positive" if is_positive else "shap-card-negative"
    bar_class = "shap-bar-positive" if is_positive else "shap-bar-negative"

    # Largeur de la barre (normalisée)
    bar_width = min(abs(shap_value) * 200, 100)  # Max 100%

    html = f"""
    <div class="shap-card {card_class}">
        <div class="shap-header">
            <p class="shap-title">{display_name}</p>
            <span class="shap-impact {impact_class}">{impact_label}</span>
        </div>
        <div class="shap-bar-container">
            <div class="{bar_class}" style="width: {bar_width}%;"></div>
        </div>
        {f'<p class="shap-description">{description}</p>' if description else ''}
    </div>
    """
    return html

# Valeurs par défaut selon la devise - Basées sur profil "Moyen" de chaque zone
# Ces valeurs correspondent à un cadre moyen / employé qualifié
DEFAULT_VALUES = {
    # Afrique Centrale (CEMAC) : Cadre moyen ~500 000 FCFA/mois
    "XAF": {"income": 6000000, "credit": 15000000, "monthly": 150000},
    # Afrique de l'Ouest (UEMOA) : Cadre moyen ~500 000 FCFA/mois
    "XOF": {"income": 6000000, "credit": 15000000, "monthly": 150000},
    # Europe : Cadre moyen ~3 500 €/mois
    "EUR": {"income": 42000, "credit": 120000, "monthly": 600},
    # USA : Manager ~7 500 $/mois
    "USD": {"income": 90000, "credit": 250000, "monthly": 1300},
}

# =============================================================================
# INTERFACE PRINCIPALE
# =============================================================================

# Header - Grand titre visible
st.markdown(f"""
<div style="text-align: center; padding: 1rem 0 2rem 0;">
    <h1 style="font-size: 3.5rem; font-weight: 900; margin: 0; letter-spacing: -1px;">
        🏦 {T["title"]}
    </h1>
    <p style="font-size: 1.3rem; opacity: 0.8; margin-top: 0.5rem;">
        {T["subtitle"]}
    </p>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# FORMULAIRE
# =============================================================================

st.markdown(f"### 📋 {T['client_info']}")

# Valeurs par défaut selon la devise
defaults = DEFAULT_VALUES[currency]

# Si un profil est sélectionné, mettre à jour les valeurs du formulaire
# IMPORTANT: Ceci doit être fait AVANT la création des widgets
# Les profils sont déjà dans la devise native, pas besoin de conversion
current_profiles = get_profiles_for_currency(currency)
if st.session_state.selected_profile and st.session_state.selected_profile in current_profiles:
    profile = current_profiles[st.session_state.selected_profile]
    st.session_state.w_revenus = int(profile["revenus"])
    st.session_state.w_credit = int(profile["credit"])
    st.session_state.w_annuite = int(profile["annuite"])
    st.session_state.w_age = profile["age"]
    st.session_state.w_anciennete = profile["anciennete"]
    st.session_state.w_score = profile["score"]
    # Réinitialiser le profil après avoir appliqué les valeurs
    st.session_state.selected_profile = None

col1, col2 = st.columns(2)

with col1:
    revenus = st.number_input(
        f"{T['annual_income']} ({CURRENCY_SYMBOLS[currency]})",
        min_value=0,
        max_value=int(1000000000 if currency in ["XAF", "XOF"] else 10000000),
        value=defaults["income"],
        step=int(1000000 if currency in ["XAF", "XOF"] else 1000),
        help=T["help_income"],
        key="w_revenus"
    )

    credit = st.number_input(
        f"{T['credit_amount']} ({CURRENCY_SYMBOLS[currency]})",
        min_value=0,
        max_value=int(5000000000 if currency in ["XAF", "XOF"] else 10000000),
        value=defaults["credit"],
        step=int(5000000 if currency in ["XAF", "XOF"] else 5000),
        help=T["help_credit"],
        key="w_credit"
    )

    annuite = st.number_input(
        f"{T['monthly_payment']} ({CURRENCY_SYMBOLS[currency]})",
        min_value=0,
        max_value=int(50000000 if currency in ["XAF", "XOF"] else 100000),
        value=defaults["monthly"],
        step=int(50000 if currency in ["XAF", "XOF"] else 50),
        help=T["help_monthly"],
        key="w_annuite"
    )

with col2:
    age = st.slider(
        T["client_age"],
        min_value=18,
        max_value=80,
        value=35,
        help=T["help_age"],
        key="w_age"
    )

    anciennete = st.slider(
        T["employment_years"],
        min_value=0,
        max_value=40,
        value=5,
        help=T["help_employment"],
        key="w_anciennete"
    )

    score_externe = st.slider(
        T["external_score"],
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.05,
        help=T["help_score"],
        key="w_score"
    )

# =============================================================================
# EXEMPLES PRÉ-REMPLIS (avec callbacks)
# =============================================================================

def select_profile(profile_name):
    """Callback pour sélectionner un profil."""
    st.session_state.selected_profile = profile_name
    st.session_state.active_profile = profile_name

st.markdown("---")
st.markdown(f"##### 💡 {T['example_profiles']}")

# Noms des profils pour l'affichage
PROFILE_NAMES = {
    "fiable": {"fr": "Profil Fiable", "en": "Reliable Profile", "icon": "✅"},
    "moyen": {"fr": "Profil Moyen", "en": "Medium Profile", "icon": "⚠️"},
    "risque": {"fr": "Profil Risqué", "en": "Risky Profile", "icon": "❌"}
}

# Afficher le profil actif avec option de reset
if st.session_state.active_profile:
    profile_info = PROFILE_NAMES[st.session_state.active_profile]
    profile_display = profile_info["fr"] if lang == "fr" else profile_info["en"]
    col_info, col_reset = st.columns([4, 1])
    with col_info:
        st.info(f"{profile_info['icon']} **{T['current_profile']}:** {profile_display}")
    with col_reset:
        if st.button("✖", help="Réinitialiser / Reset"):
            st.session_state.active_profile = None
            st.rerun()

col1, col2, col3 = st.columns(3)

# Marquer visuellement le profil actif
active = st.session_state.active_profile

# Générer les tooltips dynamiques selon la devise
profiles = get_profiles_for_currency(currency)
symbol = CURRENCY_SYMBOLS[currency]

def format_tooltip_amount(amount):
    """Formate le montant pour le tooltip selon la devise."""
    if currency in ["XAF", "XOF"]:
        if amount >= 1000000:
            return f"{amount/1000000:.1f}M {symbol}"
        else:
            return f"{amount/1000:.0f}k {symbol}"
    else:
        return f"{amount/1000:.0f}k {symbol}"

with col1:
    p = profiles["fiable"]
    tooltip = f"Cadre supérieur | {format_tooltip_amount(p['revenus'])}/an | Score {p['score']} | {p['anciennete']} ans emploi"
    btn_label = f"{'✓ ' if active == 'fiable' else ''}👤 {T['reliable_profile']}"
    st.button(
        btn_label,
        use_container_width=True,
        help=tooltip,
        on_click=select_profile,
        args=("fiable",),
        type="primary" if active == "fiable" else "secondary"
    )

with col2:
    p = profiles["moyen"]
    tooltip = f"Employé | {format_tooltip_amount(p['revenus'])}/an | Score {p['score']} | {p['anciennete']} ans emploi"
    btn_label = f"{'✓ ' if active == 'moyen' else ''}👤 {T['medium_profile']}"
    st.button(
        btn_label,
        use_container_width=True,
        help=tooltip,
        on_click=select_profile,
        args=("moyen",),
        type="primary" if active == "moyen" else "secondary"
    )

with col3:
    p = profiles["risque"]
    tooltip = f"Précaire | {format_tooltip_amount(p['revenus'])}/an | Score {p['score']} | {p['anciennete']} an emploi"
    btn_label = f"{'✓ ' if active == 'risque' else ''}👤 {T['risky_profile']}"
    st.button(
        btn_label,
        use_container_width=True,
        help=tooltip,
        on_click=select_profile,
        args=("risque",),
        type="primary" if active == "risque" else "secondary"
    )

# =============================================================================
# BOUTON D'ANALYSE
# =============================================================================

st.markdown("---")

if st.button(f"🔍 {T['analyze_risk']}", type="primary", use_container_width=True):

    # Convertir vers EUR pour l'API
    revenus_eur = convert_to_eur(revenus, currency)
    credit_eur = convert_to_eur(credit, currency)
    annuite_eur = convert_to_eur(annuite, currency)

    # Préparer les données
    data = {
        "amt_income_total": revenus_eur,
        "amt_credit": credit_eur,
        "amt_annuity": annuite_eur * 12,
        "amt_goods_price": credit_eur * 0.9,
        "days_birth": -age * 365,
        "days_employed": -anciennete * 365,
        "ext_source_1": score_externe,
        "ext_source_2": score_externe,
        "ext_source_3": score_externe,
        "code_gender": "M"
    }

    with st.spinner(T["analyzing"]):
        result, error = call_api(data)

    if error:
        st.error(f"❌ {error}")
    else:
        probability = result["probability"]
        score = result["score"]
        color, risk_label = get_risk_color(probability)
        decision, decision_text = get_decision(probability)

        st.markdown("---")

        # Résultat principal
        st.markdown(f"## {decision}")
        st.markdown(f"*{decision_text}*")

        # Métriques
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                label=T["credit_score"],
                value=f"{score}/850",
                delta=f"{score-600:+d} {T['vs_average']}" if score != 600 else None
            )

        with col2:
            st.metric(
                label=T["default_probability"],
                value=f"{probability*100:.1f}%"
            )

        with col3:
            st.metric(
                label=T["risk_level"],
                value=risk_label
            )

        # Jauge visuelle avec légende
        st.markdown(f"##### {T['risk_indicator']}")

        # Afficher la barre avec couleur selon le risque
        risk_pct = min(probability, 1.0)
        col_left, col_bar, col_right = st.columns([1, 6, 1])
        with col_left:
            st.markdown("✅ 0%")
        with col_bar:
            st.progress(risk_pct)
        with col_right:
            st.markdown("❌ 100%")

        # Afficher la position exacte
        st.caption(f"↑ {T['risk_position']}: **{probability*100:.1f}%** {T['default_risk']}")

        # =============================================================
        # ANALYSE SHAP DÉTAILLÉE - Visualisation moderne
        # =============================================================
        st.markdown("---")
        st.markdown(f"### 🔍 {T['detailed_analysis']}")

        # Appeler l'API explain pour obtenir les facteurs SHAP
        explain_result, explain_error = call_explain_api(data)

        if explain_error:
            # Fallback vers l'ancienne méthode si /explain échoue
            st.warning("Analyse détaillée temporairement indisponible")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"**{T['positive_points']}**")
                if score_externe > 0.5:
                    st.success(f"✓ {T['good_credit_history']}")
                if anciennete > 3:
                    st.success(f"✓ {T['stable_employment']}")
            with col2:
                st.markdown(f"**{T['attention_points']}**")
                if score_externe <= 0.5:
                    st.error(f"✗ {T['limited_credit_history']}")
                if anciennete <= 3:
                    st.error(f"✗ {T['low_employment_seniority']}")
        else:
            # Récupérer les facteurs
            protective_factors = explain_result.get("top_protective_factors", [])
            risk_factors = explain_result.get("top_risk_factors", [])

            # Résumé en cards
            col_summary1, col_summary2 = st.columns(2)

            with col_summary1:
                st.markdown(f"""
                <div class="summary-card summary-card-green">
                    <p class="summary-number" style="color: #10b981;">✅ {len(protective_factors)}</p>
                    <p class="summary-label">{T['your_strengths']}</p>
                </div>
                """, unsafe_allow_html=True)

            with col_summary2:
                st.markdown(f"""
                <div class="summary-card summary-card-orange">
                    <p class="summary-number" style="color: #f59e0b;">⚠️ {len(risk_factors)}</p>
                    <p class="summary-label">{T['watch_points']}</p>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # Affichage des facteurs en deux colonnes
            col_pos, col_neg = st.columns(2)

            with col_pos:
                st.markdown(f"#### ✅ {T['your_strengths']}")
                if protective_factors:
                    for factor in protective_factors[:5]:  # Max 5 facteurs
                        html = render_shap_card(factor, is_positive=True, language=lang, T=T)
                        st.markdown(html, unsafe_allow_html=True)
                else:
                    st.info(T["no_factors"])

            with col_neg:
                st.markdown(f"#### ⚠️ {T['watch_points']}")
                if risk_factors:
                    for factor in risk_factors[:5]:  # Max 5 facteurs
                        html = render_shap_card(factor, is_positive=False, language=lang, T=T)
                        st.markdown(html, unsafe_allow_html=True)
                else:
                    st.info(T["no_factors"])

            # Recommandation personnalisée
            if probability < 0.40:
                rec_text = T["recommendation_low"]
                rec_icon = "💚"
            elif probability < 0.55:
                rec_text = T["recommendation_medium"]
                rec_icon = "💡"
            else:
                rec_text = T["recommendation_high"]
                rec_icon = "⚠️"

            st.markdown(f"""
            <div class="recommendation-box">
                <p class="recommendation-title">{rec_icon} {T['recommendation']}</p>
                <p class="recommendation-text">{rec_text}</p>
            </div>
            """, unsafe_allow_html=True)

        # Détails techniques
        with st.expander(f"🔧 {T['technical_details']}"):
            st.json(result)

# =============================================================================
# FOOTER
# =============================================================================

st.markdown("---")
st.markdown(
    f"""
    <div style="text-align: center; color: #888; font-size: 0.85rem;">
        Credit Risk Scoring v1.0 | XGBoost | AUC-ROC: 0.7836<br>
        <strong>{T['copyright']}</strong><br>
        <em style="font-size: 0.75rem;">Licensed under MIT License</em>
    </div>
    """,
    unsafe_allow_html=True
)
