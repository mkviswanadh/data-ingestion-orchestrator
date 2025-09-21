import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from utils.db import run_query
import streamlit as st

def visualize_query(query: str):
    df = run_query(query)
    df.head()
    # Normalize possible amount column
    amount_col = None
    for col in df.columns:
        if col.lower() in ['amount', 'total_amount', 'avg_amount', 'total_spent', 'sum']:
            amount_col = col
            break

    if 'category' in df.columns and amount_col:
        st.write("### Transaction Amount per Category")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(data=df, x='category', y=amount_col, ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        st.pyplot(fig)
        plt.close(fig)

    elif 'location' in df.columns and amount_col:
        st.write("### Transaction Amount per Location")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(data=df, x='location', y=amount_col, ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        st.pyplot(fig)
        plt.close(fig)

    else:
        st.warning("⚠️ Could not find suitable columns to plot.")
        st.dataframe(df)
