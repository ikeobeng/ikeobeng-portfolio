# This is a flask application that serves as a portfolio website.
from flask import Flask, render_template, request
import math

app = Flask(__name__)

# 1. Sample project list (You can expand this!)
projects = [
    {
        "title": "Django To-Do App",
        "description": "A simple Django app with CRUD, login, and live hosting.",
        "github": "https://github.com/ikeobeng/todo-app-django",
        "live": "https://isaacobeng.pythonanywhere.com"
    },
    {
        "title": "EU Economic Dashboard",
        "description": "Streamlit dashboard for EU economics using World Bank data.",
        "github": "https://github.com/ikeobeng/eu-economic-dashboard",
        "live": "https://eu-economic-dashboard.streamlit.app"
    },
    {
        "title": "NLP Text Classifier",
        "description": "A basic NLP app using Scikit-learn for classification.",
        "github": "https://github.com/ikeobeng/nlp-text-classifier",
        "live": ""
    },
    {
        "title": "AI Resume Screener",
        "description": "Screen and rank resumes using NLP and keyword scoring.",
        "github": "https://github.com/ikeobeng/ai-resume-screener",
        "live": ""
    },
    {
        "title": "Portfolio Website",
        "description": "This very Flask site hosted on Render.",
        "github": "https://github.com/ikeobeng-portfolio/flask-portfolio",
        "live": "https://ikeobeng-portfolio.onrender.com"
    },
    {
        "title": "Ethical AI Audit Tool",
        "description": "A prototype for evaluating AI systems for ethical concerns.",
        "github": "https://github.com/ikeobeng/ai-ethics-audit-tool",
        "live": ""
    },
    {
        "title": "UN Data Visualizer",
        "description": "Interactive data visualizations from UN datasets using Plotly.",
        "github": "https://github.com/ikeobeng/un-data-visualizer",
        "live": ""
    },
]

# 2. Flask route with pagination
@app.route("/")
def index():
    per_page = 3  # How many projects per page
    page = int(request.args.get("page", 1))
    total_projects = len(projects)
    total_pages = math.ceil(total_projects / per_page)

    start = (page - 1) * per_page
    end = start + per_page
    paginated_projects = projects[start:end]

    return render_template(
        "index.html",
        projects=paginated_projects,
        page=page,
        total_pages=total_pages
    )

if __name__ == "__main__":
    app.run(debug=True)

