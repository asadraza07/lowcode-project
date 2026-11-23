from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Hello</title>
</head>
<body>
  <h1>Hello from Asad</h1>
  <p>My first AI-generated Flask app (Week 1).</p>
</body>
</html>"""


if __name__ == "__main__":
    # Development server only. debug=True must not be used in production.
    app.run(debug=True)