# data-ingestion-orchestrator
data-ingestion-orchestrator

# Data Ingestion Orchestrator Prototype

## Purpose

This repo demonstrates a prototype for onboarding data ingestion pipelines using:

- CLI that talks to an LLM to get metadata
- Config generation in YAML
- Webhook server to create GitHub PR with config
- DAG template for ingestion
- Validation via GitHub Actions

## Structure

| Folder | Content |
|--------|---------|
| `llm_ingestor/` | CLI + LLM parser + config writer |
| `webhook_server/` | Flask app to receive webhook and create PR in GitHub |
| `ingestion_templates/` | Templates for ingestion scripts / tasks |
| `dags/` | Example DAG (e.g. for Airflow) |
| `scripts/` | Helpers & validation scripts |
| `.github/workflows/` | CI to validate config files |

## Setup

1. Clone this repository  
2. Setup environment variables:
   - `OPENAI_API_KEY`
   - `GITHUB_TOKEN`
   - (GitHub repo info: owner, repo name)
3. Install dependencies for each part (CLI, webhook server)  
   Eg: `pip install -r webhook_server/requirements.txt`
4. Run CLI to generate config
5. Run webhook server locally (or deploy somewhere) and point CLI to it
6. Observe PR creation in GitHub

