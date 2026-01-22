import requests
from fastapi import HTTPException
from urllib.parse import urlparse

def fetch_github_issue(repo_url: str, issue_number: int):
    try:
        parsed = urlparse(repo_url)
        path_parts = parsed.path.strip("/").split("/")

        if len(path_parts) < 2:
            raise ValueError("Invalid GitHub repository URL")

        owner, repo = path_parts[0], path_parts[1]

        issue_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
        comments_url = issue_url + "/comments"

        issue_res = requests.get(issue_url, timeout=10)
        comments_res = requests.get(comments_url, timeout=10)

        if issue_res.status_code != 200:
            raise HTTPException(
                status_code=404,
                detail="GitHub issue not found or repository is invalid"
            )

        issue = issue_res.json()
        comments = comments_res.json() if comments_res.status_code == 200 else []

        return {
            "title": issue.get("title", ""),
            "body": issue.get("body", ""),
            "comments": [c.get("body", "") for c in comments]
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Error fetching GitHub issue"
        )
