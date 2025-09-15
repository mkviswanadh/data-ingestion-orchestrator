from llm_ollama import call_ollama
from config import OLLAMA_MODEL

def generate_dag_code(metadata: dict) -> str:
    prompt = f"""
Write an Airflow DAG in Python that:
- Extracts data from a Postgres table '{metadata['source_table']}' using:
  {metadata['source_conn']}
- Loads it to MySQL table '{metadata['target_table']}' using:
  {metadata['target_conn']}
- Uses pandas + SQLAlchemy (no CSV)
- Wraps extract/load functions in try/except blocks with logging
- DAG name: {metadata['dag_name']}
- Schedule: {metadata['schedule']}
- Airflow 2.5+, PythonOperator
Return only code, no explanation.
"""
    return call_ollama(prompt, model=OLLAMA_MODEL)

