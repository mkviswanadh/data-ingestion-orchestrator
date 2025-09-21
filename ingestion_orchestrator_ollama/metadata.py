# metadata.py

import pandas as pd
#import sqlalchemy
#from sqlalchemy import inspect

# Hardcoded or env-based MySQL target connection string
TARGET_CONN = "mysql+pymysql://user:pass@localhost:3306/target_db"

def fetch_metadata(table_name: str, csv_path: str = "ingestion_config.csv") -> dict:
    # Load metadata config from CSV
    df = pd.read_csv(csv_path)

    match = df[df['Table_Name'] == table_name]
    if match.empty:
        raise ValueError(f"❌ Table '{table_name}' not found in ingestion config.")

    row = match.iloc[0]

    # Check if table already exists in the target MySQL database
    #target_engine = sqlalchemy.create_engine(TARGET_CONN)
    #inspector = inspect(target_engine)
    #target_tables = inspector.get_table_names()

    #if table_name in target_tables:
    #    raise ValueError(f"⚠️ Table '{table_name}' already exists in target MySQL. Skipping ingestion.")

    # Prepare metadata dictionary
    dag_name = f"ingest_{row['DB_Name']}_to_mysql_{table_name}".lower()

    return {
        "source_conn": row["Source"],
        "source_table": row["Table_Name"],
        "target_conn": TARGET_CONN,
        "target_table": row["Table_Name"],
        "domain": row["Domain"],
        "description": row["Description"],
        "dag_name": dag_name,
        "schedule": "@daily"
    }
