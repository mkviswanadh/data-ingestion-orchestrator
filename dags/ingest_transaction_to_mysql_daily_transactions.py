from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import sqlalchemy

def extract_and_load():
    source_engine = sqlalchemy.create_engine("Oracle")
    target_engine = sqlalchemy.create_engine("mysql+pymysql://user:pass@localhost:3306/target_db")

    query = "SELECT * FROM Daily_transactions"
    df = pd.read_sql(query, con=source_engine)

    df.to_sql("Daily_transactions", con=target_engine, if_exists='replace', index=False)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id="ingest_transaction_to_mysql_daily_transactions",
    default_args=default_args,
    description="CASA transactions",
    schedule_interval="@daily",
    catchup=False,
    tags=["Transactions"],
) as dag:

    run_etl = PythonOperator(
        task_id="extract_and_load_data",
        python_callable=extract_and_load
    )

    run_etl