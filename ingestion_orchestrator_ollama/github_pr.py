# github_pr.py

import requests
import base64
import os
from config import GITHUB_OWNER, GITHUB_API_URL, GITHUB_REPO, GITHUB_TOKEN, GITHUB_BRANCH_PREFIX, GITHUB_MAIN_BRANCH


def create_github_pr(dag_name: str, dag_code: str) -> str:
    owner = GITHUB_OWNER
    repo = GITHUB_REPO
    token = GITHUB_TOKEN
    branch = GITHUB_MAIN_BRANCH
    GITHUB_API = GITHUB_API_URL
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }

    # ✅ 1. Get latest commit SHA from the branch (safe method)
    print(f"🔍 Fetching base commit SHA from branch '{branch}'...")
    res = requests.get(f"{GITHUB_API}/repos/{owner}/{repo}/branches/{branch}", headers=headers)
    
    if res.status_code != 200:
        raise Exception(f"❌ Failed to fetch branch info: {res.status_code} - {res.json().get('message')}")
    
    base_sha = res.json()["commit"]["sha"]

    # ✅ 2. Create a new branch
    pr_branch = f"{dag_name}_branch"
    print(f"🌿 Creating new branch: {pr_branch}")
    data = {
        "ref": f"refs/heads/{pr_branch}",
        "sha": base_sha
    }
    res = requests.post(f"{GITHUB_API}/repos/{owner}/{repo}/git/refs", json=data, headers=headers)
    
    if res.status_code not in (200, 201):
        raise Exception(f"❌ Failed to create branch: {res.status_code} - {res.json().get('message')}")

    # ✅ 3. Commit the DAG file to the new branch
    dag_path = f"dags/{dag_name}.py"
    print(f"📄 Committing DAG to {dag_path}")
    encoded_content = base64.b64encode(dag_code.encode()).decode()

    data = {
        "message": f"Add DAG: {dag_name}",
        "content": encoded_content,
        "branch": pr_branch
    }

    res = requests.put(
        f"{GITHUB_API}/repos/{owner}/{repo}/contents/{dag_path}",
        json=data,
        headers=headers
    )

    if res.status_code not in (200, 201):
        raise Exception(f"❌ Failed to commit DAG: {res.status_code} - {res.json().get('message')}")

    # ✅ 4. Create Pull Request
    print(f"📤 Creating Pull Request...")
    data = {
        "title": f"[DAG] {dag_name}",
        "head": pr_branch,
        "base": branch,
        "body": f"Auto-generated DAG for `{dag_name}`"
    }

    res = requests.post(f"{GITHUB_API}/repos/{owner}/{repo}/pulls", json=data, headers=headers)

    if res.status_code not in (200, 201):
        raise Exception(f"❌ Failed to create PR: {res.status_code} - {res.json().get('message')}")

    pr_url = res.json()["html_url"]
    print(f"✅ Pull Request created: {pr_url}")
    return pr_url
