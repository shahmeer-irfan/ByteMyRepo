# src/clone.py

import os
from git import Repo

def clone_repo(repo_url: str) -> str:
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    repo_path = f"./{repo_name}"
    if not os.path.exists(repo_path):
        Repo.clone_from(repo_url, repo_path)
    return repo_path
