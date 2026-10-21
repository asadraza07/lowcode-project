from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from my first AI app"

@app.route("/about")
def about():
    return "In this project I set up Git and an SSH key, created a GitHub repository called lowcode-project, and built a minimal Flask app with two routes, / and /about. I ran it in a virtual environment, installed Flask 3.0.3 from a pinned requirements.txt, and checked it in the browser. I also wrote a README and a .gitignore so the venv folder is not uploaded. I made mistakes along the way, including a typo in requirements.txt and a broken indent in app.py, and I fixed them by reading the error messages. The main thing I learned is that AI-generated code must be checked. A specific prompt gives better results than a vague one, and the README needed corrections to match my real commands. I also noticed that Flask is pinned but its dependencies are not, so pip freeze would make the setup more reproducible. Everything is committed and pushed to GitHub."

if __name__ == "__main__":
    app.run(port=5000)

