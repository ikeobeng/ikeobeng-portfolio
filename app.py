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
        "title": "Interruption Tetris Gameplay",
        "description": "Analysis of effects of interruption on Tetris gameplay using R.",
        "github": "https://github.com/ikeobeng/interruption-tetris-gameplay",
        "live": ""
    },
    {
        "title": "Workload System Usability Study",
        "description": "Analysis of Effects of workload on system usability using R.",
        "github": "https://github.com/ikeobeng/workload-system-usability",
        "live": ""
    },
    {
        "title": "Portfolio Website",
        "description": "This very Flask site hosted on Render.",
        "github": "https://github.com/ikeobeng-portfolio/flask-portfolio",
        "live": "https://ikeobeng-portfolio.onrender.com"
    },
    {
        "title": "EU Internet Usage",
        "description": "Analysis of relationship between economic growth and internet usage using Python.",
        "github": "https://github.com/ikeobeng/eu-internet-usage",
        "live": ""
    },
    {
        "title": "Personal GitHub Profile",
        "description": "Data & AI Projects, Researcher, PhD in Economics, MSc Information Systems.",
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
# Adding thank you route
@app.route('/thank-you')
def thank_you():
    return render_template("thank_you.html")

if __name__ == "__main__":
    app.run(debug=True)

