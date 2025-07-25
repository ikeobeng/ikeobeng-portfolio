# This is a flask application that serves as a portfolio website.
from flask import Flask, render_template, request
import math

app = Flask(__name__)

projects = [
    # your projects here (7+)
]

PROJECTS_PER_PAGE = 3

@app.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    total_pages = math.ceil(len(projects) / PROJECTS_PER_PAGE)
    start = (page - 1) * PROJECTS_PER_PAGE
    end = start + PROJECTS_PER_PAGE
    paginated_projects = projects[start:end]

    return render_template(
        "index.html",
        projects=paginated_projects,
        page=page,
        total_pages=total_pages,
    )

if __name__ == "__main__":
    app.run(debug=True)

