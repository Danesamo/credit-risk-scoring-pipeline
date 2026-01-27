# ====================================
# Credit Risk Scoring Project
# Makefile
# ====================================

.PHONY: help install setup data train api streamlit docker-up docker-down test clean

# Default target
help:
	@echo "Credit Risk Scoring Pipeline - Available commands:"
	@echo ""
	@echo "  Setup:"
	@echo "    make install     - Install Python dependencies"
	@echo "    make setup       - Full setup (install + download data)"
	@echo ""
	@echo "  Data:"
	@echo "    make data        - Download data from Kaggle"
	@echo "    make load-db     - Load data into PostgreSQL"
	@echo ""
	@echo "  ML:"
	@echo "    make train       - Train the model"
	@echo "    make evaluate    - Evaluate model performance"
	@echo ""
	@echo "  Services:"
	@echo "    make api         - Run FastAPI server"
	@echo "    make streamlit   - Run Streamlit app"
	@echo ""
	@echo "  Docker:"
	@echo "    make docker-up   - Start all services with Docker"
	@echo "    make docker-down - Stop all Docker services"
	@echo "    make docker-build - Build Docker images"
	@echo ""
	@echo "  Testing:"
	@echo "    make test        - Run all tests"
	@echo "    make test-cov    - Run tests with coverage"
	@echo ""
	@echo "  Utils:"
	@echo "    make clean       - Remove generated files"
	@echo "    make lint        - Run code linting"

# -----------------
# Setup
# -----------------
install:
	pip install -r requirements.txt

setup: install data

# -----------------
# Data
# -----------------
data:
	@echo "Downloading data from Kaggle..."
	kaggle competitions download -c home-credit-default-risk -p data/raw/
	unzip -o data/raw/home-credit-default-risk.zip -d data/raw/
	rm -f data/raw/home-credit-default-risk.zip
	@echo "Data downloaded successfully!"

load-db:
	@echo "Loading data into PostgreSQL..."
	python -m src.data.ingestion
	@echo "Data loaded successfully!"

# -----------------
# ML
# -----------------
train:
	@echo "Training model..."
	python -m src.models.train
	@echo "Model trained successfully!"

evaluate:
	@echo "Evaluating model..."
	python -m src.models.evaluate
	@echo "Evaluation complete!"

# -----------------
# Services
# -----------------
api:
	uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload

streamlit:
	streamlit run streamlit/app.py --server.port 8501

# -----------------
# Docker
# -----------------
docker-build:
	docker-compose build

docker-up:
	docker-compose up -d
	@echo "Services started:"
	@echo "  - API: http://localhost:8000"
	@echo "  - Streamlit: http://localhost:8501"
	@echo "  - Airflow: http://localhost:8080"
	@echo "  - Grafana: http://localhost:3000"

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

# -----------------
# Testing
# -----------------
test:
	pytest tests/ -v

test-cov:
	pytest tests/ -v --cov=src --cov-report=html

# -----------------
# Utils
# -----------------
clean:
	@echo "Cleaning generated files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf htmlcov/ .coverage
	@echo "Clean complete!"

lint:
	@echo "Running linters..."
	flake8 src/ api/ tests/
	black --check src/ api/ tests/
	@echo "Linting complete!"

format:
	@echo "Formatting code..."
	black src/ api/ tests/
	isort src/ api/ tests/
	@echo "Formatting complete!"
