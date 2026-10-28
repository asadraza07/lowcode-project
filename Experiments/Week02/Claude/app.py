import re

from flask import Flask, render_template, request

app = Flask(__name__)

NAME_MAX = 100
EMAIL_MAX = 254
MESSAGE_MAX = 5000

# Pragmatic email check: local@domain.tld, no whitespace, no extra "@".
EMAIL_RE = re.compile(
    r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9](?:[A-Za-z0-9\-]*[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9\-]*[A-Za-z0-9])?)+"
)


@app.route("/")
def home():
    return "Hello from my first AI app"

@app.route("/about")
def about():
    return "In this project I set up Git and an SSH key, created a GitHub repository called lowcode-project, and built a minimal Flask app with two routes, / and /about. I ran it in a virtual environment, installed Flask 3.0.3 from a pinned requirements.txt, and checked it in the browser. I also wrote a README and a .gitignore so the venv folder is not uploaded. I made mistakes along the way, including a typo in requirements.txt and a broken indent in app.py, and I fixed them by reading the error messages. The main thing I learned is that AI-generated code must be checked. A specific prompt gives better results than a vague one, and the README needed corrections to match my real commands. I also noticed that Flask is pinned but its dependencies are not, so pip freeze would make the setup more reproducible. Everything is committed and pushed to GitHub."


def validate_contact(name, email, message):
    """Return a dict mapping field name -> error message (empty if valid)."""
    errors = {}

    clean_name = name.strip()
    if not clean_name:
        errors["name"] = "Please enter your name."
    elif len(clean_name) > NAME_MAX:
        errors["name"] = f"Name must be at most {NAME_MAX} characters."

    clean_email = email.strip()
    if not clean_email:
        errors["email"] = "Please enter your email address."
    elif len(clean_email) > EMAIL_MAX or not EMAIL_RE.fullmatch(clean_email):
        errors["email"] = "Please enter a valid email address."

    clean_message = message.strip()
    if not clean_message:
        errors["message"] = "Please enter a message."
    elif len(clean_message) > MESSAGE_MAX:
        errors["message"] = f"Message must be at most {MESSAGE_MAX} characters."

    return errors


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Keep exactly what the user typed so the form can be re-displayed.
        values = {
            "name": request.form.get("name", ""),
            "email": request.form.get("email", ""),
            "message": request.form.get("message", ""),
        }
        errors = validate_contact(**values)

        if errors:
            return render_template("contact.html", values=values, errors=errors), 400

        # Nothing is stored or sent; just confirm receipt.
        return render_template("contact_success.html", name=values["name"].strip())

    return render_template(
        "contact.html",
        values={"name": "", "email": "", "message": ""},
        errors={},
    )


if __name__ == "__main__":
    app.run(port=5000)
