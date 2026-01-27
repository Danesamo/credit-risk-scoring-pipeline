# Credit Risk Scoring Pipeline

End-to-end credit risk scoring system with ML model, API, monitoring, and interactive UI.

---

## Overview

This project implements a complete credit scoring pipeline that predicts the probability of loan default. It demonstrates Data Engineering and Data Science skills in a production-ready setup.

**Business Problem:** Financial institutions need to assess the creditworthiness of loan applicants, especially those with little or no credit history.

**Solution:** A machine learning pipeline that processes applicant data, generates a risk score, and provides explainable predictions.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         CREDIT RISK PIPELINE                            │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐          │
│  │  DATA    │───▶│   ETL    │───▶│ FEATURE  │───▶│  MODEL   │          │
│  │  SOURCE  │    │ PIPELINE │    │   ENG.   │    │ TRAINING │          │
│  │ (Kaggle) │    │          │    │          │    │          │          │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘          │
│       │               │               │               │                 │
│       ▼               ▼               ▼               ▼                 │
│  CSV Files      PostgreSQL      Features DB      XGBoost               │
│                                                       │                 │
│                                                       ▼                 │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐          │
│  │ GRAFANA  │◀───│PROMETHEUS│◀───│ FAST API │◀───│  SHAP    │          │
│  │DASHBOARD │    │ METRICS  │    │  SERVER  │    │ EXPLAIN  │          │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘          │
│                                       │                                 │
│                                       ▼                                 │
│                                 ┌──────────┐                           │
│                                 │STREAMLIT │                           │
│                                 │    UI    │                           │
│                                 └──────────┘                           │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                         AIRFLOW (Orchestration)                   │  │
│  └──────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Tech Stack

| Category | Technology |
|----------|------------|
| **Language** | Python 3.10+ |
| **ML** | XGBoost, scikit-learn |
| **Explainability** | SHAP |
| **Database** | PostgreSQL |
| **API** | FastAPI |
| **UI** | Streamlit |
| **Orchestration** | Apache Airflow |
| **Monitoring** | Prometheus + Grafana |
| **Containerization** | Docker + Docker Compose |

---

## Project Structure

```
Credit_Risk_Scoring_Project/
├── README.md
├── requirements.txt
├── docker-compose.yml
├── Makefile
├── .gitignore
│
├── data/
│   ├── raw/              # Raw data from Kaggle
│   ├── processed/        # Cleaned data
│   └── features/         # Engineered features
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_modeling.ipynb
│
├── src/
│   ├── data/             # Data ingestion & preprocessing
│   ├── features/         # Feature engineering
│   ├── models/           # Training & prediction
│   └── utils/            # Helper functions
│
├── api/                  # FastAPI application
├── streamlit/            # Streamlit UI
├── airflow/dags/         # Airflow DAGs
├── monitoring/           # Prometheus & Grafana configs
├── models/               # Saved models
├── tests/                # Unit tests
├── docs/                 # Documentation
└── configs/              # Configuration files
```

---

## Dataset

**Source:** [Kaggle - Home Credit Default Risk](https://www.kaggle.com/c/home-credit-default-risk)

| Table | Description | Rows |
|-------|-------------|------|
| application_train | Main application data with target | 307,511 |
| bureau | Credit history from other institutions | 1,716,428 |
| bureau_balance | Monthly bureau balances | 27,299,925 |
| previous_application | Previous Home Credit applications | 1,670,214 |
| POS_CASH_balance | POS and cash loan balances | 10,001,358 |
| credit_card_balance | Credit card balances | 3,840,312 |
| installments_payments | Payment history | 13,605,401 |

---

## Quick Start

### Prerequisites

- Python 3.10+
- Docker & Docker Compose
- Kaggle API credentials

### Installation

```bash
# Clone the repository
git clone https://github.com/Danesamo/credit-risk-scoring-pipeline.git
cd credit-risk-scoring-pipeline

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Download data from Kaggle
kaggle competitions download -c home-credit-default-risk
unzip home-credit-default-risk.zip -d data/raw/
```

### Run with Docker

```bash
# Start all services
docker-compose up -d

# Access services:
# - API: http://localhost:8000
# - Streamlit: http://localhost:8501
# - Airflow: http://localhost:8080
# - Grafana: http://localhost:3000
```

---

## Model Performance

| Metric | Value |
|--------|-------|
| AUC-ROC | TBD |
| Gini | TBD |
| Precision (default) | TBD |
| Recall (default) | TBD |

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/predict` | POST | Get credit score for an applicant |
| `/explain` | POST | Get SHAP explanation for prediction |
| `/health` | GET | Health check |
| `/metrics` | GET | Prometheus metrics |

---

## Documentation

- [Project Study (FR)](docs/01_ETUDE_PROJET.md) - Business context and methodology
- [Roadmap (FR)](docs/02_FEUILLE_DE_ROUTE.md) - Step-by-step execution plan

---

## Author

**Daniela Samo**
- Data Engineer

---

## License

This project is for educational and portfolio purposes.
Dataset subject to [Kaggle Competition Rules](https://www.kaggle.com/c/home-credit-default-risk/rules).
