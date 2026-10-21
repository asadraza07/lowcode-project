from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from my first AI app"

@app.route("/about")
def about():
    return "Your 150-word answer here."

if __name__ == "__main__":
    app.run(port=5000)

