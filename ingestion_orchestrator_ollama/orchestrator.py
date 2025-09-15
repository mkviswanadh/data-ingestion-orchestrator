from metadata import fetch_metadata
from dag_generator import generate_dag_code
from github_pr import create_github_pr
from airflow_api import trigger_dag, check_dag_status

def orchestrate(table_name: str):
    print(f"🔍 Fetching metadata for table: {table_name}")
    metadata = fetch_metadata(table_name)

    print(f"🛠️ Generating Airflow DAG using Ollama...")
    dag_code = generate_dag_code(metadata)
    dag_name = metadata["dag_name"]

    print(f"📤 Creating GitHub PR for DAG: {dag_name}")
    pr_url = create_github_pr(dag_name, dag_code)
    print(f"✅ PR created: {pr_url}")

    input("🟢 Press Enter after PR is reviewed and merged to continue...")

    print("🚀 Triggering DAG...")
    run_id = trigger_dag(dag_name)
    print(f"📡 DAG run started: {run_id}")

    print("⏳ Monitoring DAG status...")
    status = check_dag_status(dag_name, run_id)

    if status == "success":
        print(f"🎉 DAG `{dag_name}` succeeded!")
    else:
        print(f"❌ DAG `{dag_name}` failed or timed out. Status: {status}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python orchestrator.py <source_table>")
    else:
        orchestrate(sys.argv[1])

