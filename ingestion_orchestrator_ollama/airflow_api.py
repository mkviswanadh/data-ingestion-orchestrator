import requests
import time
from config import AIRFLOW_API_URL, AIRFLOW_API_TOKEN

HEADERS = {
    "Authorization": f"Bearer {AIRFLOW_API_TOKEN}",
    "Content-Type": "application/json"
}

def trigger_dag(dag_id: str) -> str:
    resp = requests.post(
        f"{AIRFLOW_API_URL}/dags/{dag_id}/dagRuns",
        headers=HEADERS,
        json={"conf": {}}
    )
    return resp.json().get("dag_run_id")

def check_dag_status(dag_id: str, run_id: str, max_wait=600):
    for _ in range(max_wait // 10):
        resp = requests.get(f"{AIRFLOW_API_URL}/dags/{dag_id}/dagRuns/{run_id}", headers=HEADERS)
        status = resp.json().get("state")
        if status in ["success", "failed"]:
            return status
        time.sleep(10)
    return "timeout"

