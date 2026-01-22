<img width="792" height="839" alt="image" src="https://github.com/anushaj2004/github_issue_analyzer/" /># GitHub Issue Analyzer (AI Powered)

A simple web application that takes a public GitHub repository URL and an issue number, analyzes the issue using AI, and returns a structured JSON summary.

---

## ✨ Features

- Input GitHub repository URL and issue number
- Fetch issue title, body, and comments using GitHub API
- Analyze issue using Google Gemini AI
- Returns structured JSON output
- Simple frontend UI
- Setup in under 5 minutes

---

## 🛠 Tech Stack

- Backend: Python, FastAPI
- Frontend: Streamlit
- AI Model: Google Gemini (Flash Lite)
- APIs: GitHub REST API, Gemini API

---

## 📁 Project Structure

github-issue-analyzer/
│
├── backend/
│   ├── main.py
│   ├── ai_analyzer.py
│   ├── github_utils.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   └── app.py
│
└── README.md

---

## ⚙️ Setup & Run

### 1. Clone Repository

git clone https://github.com/your-username/github-issue-analyzer.git  
cd github-issue-analyzer

---

### 2. Backend Setup

cd backend  
python -m venv venv  

Activate virtual environment:

Windows: venv\Scripts\activate  
Mac/Linux: source venv/bin/activate  

Install dependencies:

pip install -r requirements.txt

---

### 3. Environment Variables

Create a `.env` file in backend folder:

GEMINI_API_KEY=your_gemini_api_key_here

Get API key from: https://ai.google.dev

---

### 4. Run Backend

uvicorn main:app --reload

Backend runs at:  
http://127.0.0.1:8000  
Docs: http://127.0.0.1:8000/docs

---

### 5. Run Frontend

cd frontend  
streamlit run app.py

---

## 📥 Example Input

{
  "repo_url": "https://github.com/facebook/react",
  "issue_number": 234
}

---

## 📤 Example Output

{
  "summary": "The application crashes when users attempt to log in.",
  "type": "bug",
  "priority_score": "5 - Critical because it blocks user access",
  "suggested_labels": ["bug", "login", "crash"],
  "potential_impact": "Users may face disruptions or be unable to use key features of the application."
}

---

## Output results
# GitHub Issue Analyzer (AI Powered)

A simple web application that takes a public GitHub repository URL and an issue number, analyzes the issue using AI, and returns a structured JSON summary.

---

## ✨ Features

- Input GitHub repository URL and issue number
- Fetch issue title, body, and comments using GitHub API
- Analyze issue using Google Gemini AI
- Returns structured JSON output
- Simple frontend UI
- Setup in under 5 minutes

---

## 🛠 Tech Stack

- Backend: Python, FastAPI
- Frontend: Streamlit
- AI Model: Google Gemini (Flash Lite)
- APIs: GitHub REST API, Gemini API

---

## 📁 Project Structure

github-issue-analyzer/
│
├── backend/
│   ├── main.py
│   ├── ai_analyzer.py
│   ├── github_utils.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   └── app.py
│
└── README.md

---

## ⚙️ Setup & Run

### 1. Clone Repository

git clone https://github.com/your-username/github-issue-analyzer.git  
cd github-issue-analyzer

---

### 2. Backend Setup

cd backend  
python -m venv venv  

Activate virtual environment:

Windows: venv\Scripts\activate  
Mac/Linux: source venv/bin/activate  

Install dependencies:

pip install -r requirements.txt

---

### 3. Environment Variables

Create a `.env` file in backend folder:

GEMINI_API_KEY=your_gemini_api_key_here

Get API key from: https://ai.google.dev

---

### 4. Run Backend

uvicorn main:app --reload

Backend runs at:  
http://127.0.0.1:8000  
Docs: http://127.0.0.1:8000/docs

---

### 5. Run Frontend

cd frontend  
streamlit run app.py

---

## 📥 Example Input

{
  "repo_url": "https://github.com/facebook/react",
  "issue_number": 234
}

---

## 📤 Example Output

{
  "summary": "The application crashes when users attempt to log in.",
  "type": "bug",
  "priority_score": "5 - Critical because it blocks user access",
  "suggested_labels": ["bug", "login", "crash"],
  "potential_impact": "Users may face disruptions or be unable to use key features of the application."
}

---



## ✅ Assignment Requirements Met

- Input UI
- Backend API
- GitHub API integration
- AI-based analysis
- Structured JSON output
- Clean frontend
- Clear documentation

---


## Name
Anusha J


## ✅ Assignment Requirements Met

- Input UI
- Backend API
- GitHub API integration
- AI-based analysis
- Structured JSON output
- Clean frontend
- Clear documentation

---


## Name
Anusha J
