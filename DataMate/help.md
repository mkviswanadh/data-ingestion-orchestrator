✅ Summary of All Commands
📦 Install Dependencies
pip install -r requirements.txt

🛠️ Setup DB
mysql -u root -p
# Run CREATE DATABASE and TABLE queries

💾 Load Data
python data/load_sample_data.py

🧠 Start LLaMA 3.8
ollama run llama3:8b

🖼️ Launch Chatbot UI
streamlit run app/main.py

🔁 Run MCP Orchestrator
python orchestrator/flow.py


### Sample Data Load
python data/load_sample_data.py

### Use Ollama
**Install Ollama**
curl -fsSL https://ollama.com/install.sh | sh

**Pull LLaMA 3.8b model**
ollama pull llama3:8b

**Run LLaMA**
ollama run llama3:8b

### Run Streamlit Chatbot App

From root of your project:

streamlit run app/main.py

### Generate EDA Report (Optional)

You can trigger from the UI via sidebar button, or manually:

python -c "from app.utils.eda import generate_eda_html; generate_eda_html()"

### Run LLM MCP Orchestrator Pipeline

We're using Prefect to orchestrate LLM agent + profiler:

🔹 Install Prefect (if not already):
pip install prefect

🔹 Run the flow:
python orchestrator/flow.py


### Sample Queries to Try in Chat

| Prompt                                   | What Happens            |
| ---------------------------------------- | ----------------------- |
| "What’s the total amount spent?"         | LLM answers             |
| "Show average spend per payment method"  | SQL + chart             |
| "Plot transactions amount per category"  | SQL + barplot           |
| "Top 5 locations with highest spending?" | SQL + chart             |
| "Summarize all transactions"             | LLM writes text summary |


### Venv
python -m venv datamate_env

datamate_env/scripts/activate