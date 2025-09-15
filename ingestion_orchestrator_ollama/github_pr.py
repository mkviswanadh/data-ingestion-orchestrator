import requests
import base64
from config import GITHUB_API_URL, GITHUB_REPO, GITHUB_TOKEN, GITHUB_BRANCH_PREFIX, GITHUB_MAIN_BRANCH

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def create_branch(branch_name, base_sha):
    requests.post(
        f"{GITHUB_API_URL}/repos/{GITHUB_REPO}/git/refs",
        headers=HEADERS,
        json={"ref": f"refs/heads/{branch_name}", "sha": base_sha}
    )

def upload_dag(branch, dag_path, content, message):
    b64_content = base64.b64encode(content.encode()).decode()
    url = f"{GITHUB_API_URL}/repos/{GITHUB_REPO}/contents/{dag_path}"
    return requests.put(url, headers=HEADERS, json={
        "message": message,
        "content": b64_content,
        "branch": branch
    })

def create_pull_request(branch, dag_name):
    pr = requests.post(
        f"{GITHUB_API_URL}/repos/{GITHUB_REPO}/pulls",
        headers=HEADERS,
        json={
            "title": f"[Auto DAG] {dag_name}",
            "head": branch,
            "base": GITHUB_MAIN_BRANCH,
            "body": f"Auto-generated DAG for `{dag_name}` by LLM orchestrator."
        }
    )
    return pr.json().get("html_url", "PR creation failed")

def create_github_pr(dag_name, dag_code):
    # Get base SHA of main
    res = requests.get(f"{GITHUB_API_URL}/repos/{GITHUB_REPO}/git/ref/heads/{GITHUB_MAIN_BRANCH}", headers=HEADERS)
    base_sha = res.json()["object"]["sha"]
    branch = f"{GITHUB_BRANCH_PREFIX}{dag_name}"

    create_branch(branch, base_sha)
    upload_dag(branch, f"dags/{dag_name}.py", dag_code, f"Add DAG {dag_name}")
    return create_pull_request(branch, dag_name)

