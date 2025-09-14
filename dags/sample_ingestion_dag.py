from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import yaml
from ingestion_templates.ingestion_script_template import run as ingestion_run  # or import differently

def load_config(pipeline_name):
    cfg_file = f"/path/to/configs/{pipeline_name}.yaml"
    with open(cfg_file) as f:
        return yaml.safe_load(f)

def run_ingestion(**context):
    pipeline_name = context['pipeline_name']
    metadata = load_config(pipeline_name)
    # you might generate script dynamically or call template
    # here you can just call a function or subprocess

    # For simplicity, let's assume ingestion_script has been generated
    # and by importable module
    ingestion_run()

with DAG('sample_ingestion',
         schedule_interval=None,
         start_date=datetime(2025,1,1),
         catchup=False) as dag:

    task = PythonOperator(
        task_id='run_ingestion_task',
        python_callable=run_ingestion,
        op_kwargs={'pipeline_name': 'orders_to_summary'}
    )

