from fastapi import FastAPI
from pydantic import BaseModel
from github_utils import fetch_github_issue
from ai_analyzer import analyze_issue

app = FastAPI(title="GitHub Issue Analyzer")

class IssueRequest(BaseModel):
    repo_url: str
    issue_number: int

@app.post("/analyze")
def analyze_github_issue(request: IssueRequest):
    issue_data = fetch_github_issue(request.repo_url, request.issue_number)
    analysis = analyze_issue(issue_data)
    return analysis
