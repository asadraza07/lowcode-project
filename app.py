
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from my first AI app"

if __name__ == "__main__":
    app.run(port=5000)

