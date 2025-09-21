from ydata_profiling import ProfileReport
from app.utils.db import run_query

def generate_eda_html():
    df = run_query("SELECT * FROM daily_transactions")
    profile = ProfileReport(df, title="Transactions EDA", explorative=True)
    profile.to_file("eda_report.html")
    return "eda_report.html"
