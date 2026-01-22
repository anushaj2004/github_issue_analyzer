import streamlit as st
import requests
import json

st.set_page_config(page_title="GitHub Issue Analyzer", layout="centered")

st.title("GitHub Issue Analyzer (AI Powered)")

repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/facebook/react"
)

issue_number = st.number_input(
    "Issue Number",
    min_value=1,
    step=1
)

if st.button("Analyze Issue"):
    if not repo_url or not issue_number:
        st.error("Please enter both repository URL and issue number")
    else:
        with st.spinner("Analyzing issue..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/analyze",
                    json={
                        "repo_url": repo_url,
                        "issue_number": issue_number
                    },
                    timeout=60
                )

                if response.status_code != 200:
                    st.error("Failed to analyze issue")
                    st.text(response.text)
                else:
                    result = response.json()

                    st.success("Analysis Complete")

                    # ✅ THIS IS THE KEY LINE (JSON ONLY)
                    st.subheader("AI Output (JSON Format)")
                    st.json(result)

            except Exception as e:
                st.error("Error connecting to backend")
                st.text(str(e))
