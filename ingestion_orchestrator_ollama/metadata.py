from sqlalchemy import create_engine, text
from config import METADATA_DB_URL

def fetch_metadata(table_name: str) -> dict:
    engine = create_engine(METADATA_DB_URL)
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM ingestion_config WHERE source_table = :table"),
            {"table": table_name}
        )
        row = result.fetchone()
        if not row:
            raise ValueError(f"Table '{table_name}' not found in metadata.")
        return dict(row)

