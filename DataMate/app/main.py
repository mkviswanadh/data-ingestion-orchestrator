import streamlit as st
from components.chat import chat_interface
# from utils.eda import generate_eda_html

st.sidebar.header("⚙️ Options")
eda_button = st.sidebar.button("🔍 Run EDA Profiler")

# if eda_button:
#     path = generate_eda_html()
#     with open(path, "r") as f:
#         st.components.v1.html(f.read(), height=800, scrolling=True)

chat_interface()
