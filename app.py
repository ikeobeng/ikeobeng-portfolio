# This is a flask application that serves as a portfolio website.
from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "title": "Django To-Do App",
        "description": "A Django-based web app with user authentication, CRUD features, and deployment.",
        "github": "https://github.com/ikeobeng/todo-app-django",
        "live": None,
    },
    {
        "title": "EU Economic Dashboard",
        "description": "AI-powered interactive dashboard visualizing EU economic indicators using Python and Streamlit.",
        "github": "https://github.com/ikeobeng/eu-economic-dashboard",
        "live": None,
    },
    {
        "title": "Portfolio Website",
        "description": "This Flask portfolio website showcasing my resume and projects, deployed on Render.",
        "github": None,
        "live": "https://ikeobeng-portfolio.onrender.com",
    },
]

@app.route("/")
def index():
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
