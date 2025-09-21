# dag_generator.py

from jinja2 import Template

# Jinja2-based template for generating Airflow DAGs
DAG_TEMPLATE = """
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import sqlalchemy

def extract_and_load():
    source_engine = sqlalchemy.create_engine("{{ source_conn }}")
    target_engine = sqlalchemy.create_engine("{{ target_conn }}")

    query = "SELECT * FROM {{ source_table }}"
    df = pd.read_sql(query, con=source_engine)

    df.to_sql("{{ target_table }}", con=target_engine, if_exists='replace', index=False)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id="{{ dag_name }}",
    default_args=default_args,
    description="{{ description }}",
    schedule_interval="{{ schedule }}",
    catchup=False,
    tags=["{{ domain }}"],
) as dag:

    run_etl = PythonOperator(
        task_id="extract_and_load_data",
        python_callable=extract_and_load
    )

    run_etl
"""

def generate_dag_code(metadata: dict) -> str:
    """
    Generate the full Airflow DAG Python code as a string using metadata.

    Parameters:
        metadata (dict): Required keys:
            - source_conn
            - target_conn
            - source_table
            - target_table
            - dag_name
            - domain
            - description
            - schedule

    Returns:
        str: Full Python code of the DAG
    """
    required_keys = [
        "source_conn", "target_conn", "source_table", "target_table",
        "dag_name", "domain", "description", "schedule"
    ]
    
    for key in required_keys:
        if key not in metadata:
            raise ValueError(f"Missing required metadata key: '{key}'")

    template = Template(DAG_TEMPLATE.strip())
    return template.render(**metadata)
