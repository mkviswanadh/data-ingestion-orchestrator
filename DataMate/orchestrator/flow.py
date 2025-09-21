from prefect import flow, task
from app.utils.eda import generate_eda_html
from app.utils.llm_agent import query_llm

@task
def trigger_eda():
    return generate_eda_html()

@task
def llm_summary():
    return query_llm("Give me a summary of total spend per category")

@flow(name="LLM-MCP-Flow")
def llm_mcp_pipeline():
    trigger_eda()
    summary = llm_summary()
    print("Summary:", summary)

if __name__ == "__main__":
    llm_mcp_pipeline()
