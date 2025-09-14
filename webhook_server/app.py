from flask import Flask, request, jsonify
import os
from github import Github

app = Flask(__name__)

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
REPO_OWNER = os.environ.get('REPO_OWNER')
REPO_NAME = os.environ.get('REPO_NAME')
BASE_BRANCH = os.environ.get('BASE_BRANCH', 'main')

if not all([GITHUB_TOKEN, REPO_OWNER, REPO_NAME]):
    raise Exception("Need GITHUB_TOKEN, REPO_OWNER, REPO_NAME in environment")

gh = Github(GITHUB_TOKEN)
repo = gh.get_repo(f"{REPO_OWNER}/{REPO_NAME}")

@app.route('/trigger-pr', methods=['POST'])
def trigger_pr():
    data = request.json
    pipeline_name = data['pipeline_name']
    config_path = data['config_path']
    config_content = data['config_content']

    branch_name = f"feature/{pipeline_name}"
    # create branch
    base_ref = repo.get_branch(BASE_BRANCH)
    repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=base_ref.commit.sha)

    # commit file
    try:
        repo.create_file(
            path=config_path,
            message=f"Add ingestion config: {pipeline_name}",
            content=config_content,
            branch=branch_name
        )
    except Exception as e:
        return jsonify({"status":"error","message":f"Could not create file: {e}"}), 500

    # create PR
    pr = repo.create_pull(
        title=f"Add ingestion config '{pipeline_name}'",
        body="This PR adds new ingestion pipeline configuration.",
        head=branch_name,
        base=BASE_BRANCH
    )
    return jsonify({"status":"success","pr_url": pr.html_url}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

