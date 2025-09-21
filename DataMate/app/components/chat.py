import streamlit as st
from utils.llm_agent import query_llm
from components.visualizer import visualize_query
from components.auto_visualizer import auto_render_output
import re
import streamlit as st

def chat_interface():
    st.title("💬 DataMate Chatbot")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.chat_input("How can I help you today with data insights...")
    
    if user_input:
        st.session_state.chat_history.append({"role": "user", "text": user_input})
        
        with st.spinner("DataMate is thinking..."):
            llm_response = query_llm(user_input)
            st.session_state.chat_history.append({"role": "assistant", "text": llm_response})
            # Try to extract SQL from the response
            sql_match = re.search(r"(SELECT[\s\S]+?;)", llm_response, re.IGNORECASE)

            if sql_match:
                sql_query = sql_match.group(1).strip()
                st.markdown(f"**Generated SQL:** `{sql_query}`")
                auto_render_output(sql_query)
            else:
                st.error("⚠️ LLM did not generate a valid SQL query.")
                st.markdown("### Raw LLM Output:")
                st.code(llm_response)

    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.markdown(chat["text"])
