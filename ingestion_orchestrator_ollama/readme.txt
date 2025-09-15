export METADATA_DB_URL=postgresql://user:pass@localhost:5432/metadata
export GITHUB_TOKEN=ghp_...
export AIRFLOW_API_TOKEN=your_airflow_token
export AIRFLOW_API_URL=http://localhost:8080/api/v1

python orchestrator/orchestrator.py employees

