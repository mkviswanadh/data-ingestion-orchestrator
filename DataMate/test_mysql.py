from sqlalchemy import create_engine,text
import os
import urllib.parse
# Config
user = os.getenv("DB_USER", "root")
raw_password = os.getenv("DB_PASSWORD", "XXXXXXXX")
encoded_password = urllib.parse.quote_plus(raw_password)
host = os.getenv("DB_HOST", "localhost")
db = os.getenv("DB_NAME", "ai_tdv_finacle")

# Create SQLAlchemy engine using pymysql
engine = create_engine(f"mysql+pymysql://{user}:{encoded_password}@{host}/{db}")
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM daily_transactions LIMIT 5"))
    for row in result:
        print(row)
