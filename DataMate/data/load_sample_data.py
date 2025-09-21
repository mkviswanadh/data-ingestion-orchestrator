from sqlalchemy import create_engine
import pandas as pd
import random
from datetime import datetime, timedelta
import urllib.parse
import os

# If using dotenv (.env file)
from dotenv import load_dotenv
load_dotenv()

def insert_data():
    # Config
    user = os.getenv("DB_USER", "root")
    raw_password = os.getenv("DB_PASSWORD", "")
    encoded_password = urllib.parse.quote_plus(raw_password)
    host = os.getenv("DB_HOST", "localhost")
    db = os.getenv("DB_NAME", "ai_tdv_finacle")

    # Create SQLAlchemy engine using pymysql
    engine = create_engine(f"mysql+pymysql://{user}:{encoded_password}@{host}/{db}")

    # Sample data generators
    categories = ['Groceries', 'Utilities', 'Entertainment', 'Healthcare', 'Transport']
    payment_methods = ['Credit Card', 'Debit Card', 'Cash', 'UPI']
    locations = ['New York', 'Chicago', 'Los Angeles', 'San Francisco', 'Houston']

    # Generate 1000 sample transactions
    data = []
    for _ in range(1000):
        transaction_date = datetime.today() - timedelta(days=random.randint(0, 30))
        customer_id = random.randint(1000, 1050)
        amount = round(random.uniform(10.0, 500.0), 2)
        category = random.choice(categories)
        location = random.choice(locations)
        payment_method = random.choice(payment_methods)

        data.append({
            "transaction_date": transaction_date.date(),
            "customer_id": customer_id,
            "amount": amount,
            "category": category,
            "location": location,
            "payment_method": payment_method
        })

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Insert using pandas (replace or append)
    df.to_sql("daily_transactions", con=engine, if_exists="append", index=False)

    print("✅ Inserted 1000 sample records into 'daily_transactions' successfully.")

if __name__ == "__main__":
    insert_data()
