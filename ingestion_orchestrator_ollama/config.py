import os

# Metadata DB
METADATA_DB_URL = os.getenv("METADATA_DB_URL", "postgresql://user:pass@localhost:5432/metadata")

# GitHub
#GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER="mkviswanadh"
#GITHUB_TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
GITHUB_REPO = "data-ingestion-orchestrator"
GITHUB_MAIN_BRANCH = "main"
GITHUB_BRANCH_PREFIX = "feature/daggen-"
GITHUB_API_URL = "https://api.github.com"

# Airflow
AIRFLOW_API_URL = os.getenv("AIRFLOW_API_URL", "http://localhost:8080/api/v1")
AIRFLOW_API_TOKEN = os.getenv("AIRFLOW_API_TOKEN")

# LLM / Ollama
#OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "codellama")
#OLLAMA_MODEL = "codellama"
OLLAMA_MODEL = "phi"

