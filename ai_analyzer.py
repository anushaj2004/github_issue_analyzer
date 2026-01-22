import requests
import json
import os
from dotenv import load_dotenv
from fastapi import HTTPException

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found in environment")

# WORKING + STABLE GEMINI MODEL
GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-flash-lite-latest:generateContent?key=" + GEMINI_API_KEY
)

def analyze_issue(issue_data):
    # STRICT PROMPT (EXAM SAFE)
    prompt = f"""
You are an AI system that MUST return output ONLY in valid JSON.
Do NOT add explanations, markdown, or extra text.

Analyze the following GitHub issue.

Title:
{issue_data['title']}

Body:
{issue_data['body']}

Comments:
{issue_data['comments']}

Return JSON EXACTLY in this format:

{{
  "summary": "One clear sentence summarizing the user's problem or request.",
  "type": "bug | feature_request | documentation | question | other",
  "priority_score": "1 (low) to 5 (critical) with a short justification",
  "suggested_labels": ["label1", "label2", "label3"],
  "potential_impact": "Impact on users if this issue is a bug, otherwise say 'Not applicable'."
}}

Rules:
- summary must be ONE sentence
- type must be ONE of the allowed values
- suggested_labels must have 2 or 3 items
- priority_score must include the number AND reason
- Output MUST be valid JSON only
"""

    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    response = requests.post(
        GEMINI_URL,
        headers={"Content-Type": "application/json"},
        json=payload,
        timeout=30
    )

    if response.status_code != 200:
        raise HTTPException(
            status_code=500,
            detail=f"Gemini API error: {response.text}"
        )

    data = response.json()

    candidates = data.get("candidates", [])
    if not candidates:
        raise HTTPException(
            status_code=500,
            detail="Gemini returned no candidates"
        )

    text = candidates[0]["content"]["parts"][0]["text"]

    #  JSON SAFETY + NORMALIZATION
    try:
        result = json.loads(text)
    except Exception:
        result = {
            "summary": text[:120],
            "type": "other",
            "priority_score": "3 - Medium priority",
            "suggested_labels": ["needs-review", "triage"],
            "potential_impact": "Not applicable"
        }

    # 🔒 FORCE EXACT OUTPUT FORMAT
    result = {
        "summary": str(result.get("summary", "")),
        "type": result.get("type", "other"),
        "priority_score": str(result.get("priority_score", "3 - Medium priority")),
        "suggested_labels": result.get("suggested_labels", [])[:3],
        "potential_impact": result.get("potential_impact") if result.get("type") == "bug" else "Not applicable",

    }

    if result["type"] not in [
        "bug",
        "feature_request",
        "documentation",
        "question",
        "other"
    ]:
        result["type"] = "other"

    if len(result["suggested_labels"]) < 2:
        result["suggested_labels"] = ["needs-review", "triage"]

    return result

